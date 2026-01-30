/**
 * ROLE PERMISSION MATRIX CONFIGURATION
 * =====================================
 * EnterpriseGPT uses a ROLE–USER separation model.
 * Roles are FIXED system permission profiles.
 * Users are INSTANCES that are assigned to exactly one role.
 * 
 * RULES:
 * - Roles are seeded and protected
 * - Roles must NOT be created/edited/deleted via UI
 * - Permissions are mapped centrally per role
 */

// Fixed system roles - non-deletable, non-editable
export const SYSTEM_ROLES = {
    ADMIN: 'admin',
    BACKOFFICE_MANAGER: 'backofficemanager',
    BACKOFFICE_USER: 'backofficeuser',
    POS_MANAGER: 'posmanager',
    POS_USER: 'posuser',
} as const;

export type SystemRoleKey = typeof SYSTEM_ROLES[keyof typeof SYSTEM_ROLES];

// Role definitions with descriptions
export const ROLE_DEFINITIONS: Record<SystemRoleKey, {
    name: string;
    description: string;
    isSystemRole: boolean;
}> = {
    [SYSTEM_ROLES.ADMIN]: {
        name: 'Administrator',
        description: 'Full access to all modules and admin features',
        isSystemRole: true,
    },
    [SYSTEM_ROLES.BACKOFFICE_MANAGER]: {
        name: 'Back Office Manager',
        description: 'Back office operations, approvals (Procurement, Inventory, Pricing, etc.)',
        isSystemRole: true,
    },
    [SYSTEM_ROLES.BACKOFFICE_USER]: {
        name: 'Back Office User',
        description: 'Back office screens (read/write as permitted), no approvals',
        isSystemRole: true,
    },
    [SYSTEM_ROLES.POS_MANAGER]: {
        name: 'POS Manager',
        description: 'POS configuration, day open/close, reconciliation, terminal management',
        isSystemRole: true,
    },
    [SYSTEM_ROLES.POS_USER]: {
        name: 'POS User',
        description: 'POS billing, on-the-fly customer/item creation (as configured), no admin access',
        isSystemRole: true,
    },
};

/**
 * SIDEBAR VISIBILITY MATRIX
 * Defines which top-level menu modules are visible to each role.
 * Visibility is driven by ROLE, not username.
 */
export const ROLE_MENU_VISIBILITY: Record<SystemRoleKey, {
    // Top-level modules
    retailNow: boolean;
    security: boolean;
    retail: boolean;
    finance: boolean;
    crm: boolean;
    hr: boolean;
    // Sub-categories within Retail
    storeOps: boolean;
    sales: boolean;
    merchandising: boolean;
    inventory: boolean;
    procurement: boolean;
    customers: boolean;
    // Special access
    approvals: boolean;
    reports: boolean;
    configuration: boolean;
}> = {
    // Administrator → sees all menus
    [SYSTEM_ROLES.ADMIN]: {
        retailNow: true,
        security: true,
        retail: true,
        finance: true,
        crm: true,
        hr: true,
        storeOps: true,
        sales: true,
        merchandising: true,
        inventory: true,
        procurement: true,
        customers: true,
        approvals: true,
        reports: true,
        configuration: true,
    },
    // Back Office Manager → back office + reports + approvals
    [SYSTEM_ROLES.BACKOFFICE_MANAGER]: {
        retailNow: true,
        security: false,
        retail: true,
        finance: true,
        crm: true,
        hr: false,
        storeOps: false,
        sales: true,
        merchandising: true,
        inventory: true,
        procurement: true,
        customers: true,
        approvals: true, // Key differentiator
        reports: true,
        configuration: false,
    },
    // Back Office User → operational back office screens only
    [SYSTEM_ROLES.BACKOFFICE_USER]: {
        retailNow: true,
        security: false,
        retail: true,
        finance: false,
        crm: false,
        hr: false,
        storeOps: false,
        sales: true,
        merchandising: true,
        inventory: true,
        procurement: true,
        customers: true,
        approvals: false, // No approvals
        reports: false,
        configuration: false,
    },
    // POS Manager → POS + limited inventory views
    [SYSTEM_ROLES.POS_MANAGER]: {
        retailNow: true,
        security: false,
        retail: true,
        finance: false,
        crm: false,
        hr: false,
        storeOps: true, // Core POS operations
        sales: false,
        merchandising: false,
        inventory: true, // Limited - stock on hand
        procurement: false,
        customers: true, // For loyalty
        approvals: false,
        reports: true, // POS reports only
        configuration: true, // POS config only
    },
    // POS User → Checkout / Billing only
    [SYSTEM_ROLES.POS_USER]: {
        retailNow: false,
        security: false,
        retail: true,
        finance: false,
        crm: false,
        hr: false,
        storeOps: true, // Checkout only
        sales: false,
        merchandising: false,
        inventory: false,
        procurement: false,
        customers: false,
        approvals: false,
        reports: false,
        configuration: false,
    },
};

/**
 * Menu item IDs that map to permission categories
 * Used for filtering sidebar based on role
 */
export const MENU_CATEGORY_MAPPING: Record<string, keyof typeof ROLE_MENU_VISIBILITY[SystemRoleKey]> = {
    // Top-level modules
    'retail-now': 'retailNow',
    'security': 'security',
    'retail': 'retail',
    'finance': 'finance',
    'crm': 'crm',
    'hr': 'hr',
    // Retail sub-categories
    'pos': 'storeOps',
    'sales': 'sales',
    'master-data': 'merchandising',
    'inventory': 'inventory',
    'procurement': 'procurement',
    'customers': 'customers',
};

/**
 * POS-specific screens that only POS roles can access
 */
export const POS_ONLY_MENU_IDS = [
    'pos-checkout',
    'pos-day-open',
    'pos-day-close',
    'pos-session-open',
    'pos-session-close',
    'pos-settlement',
    'pos-terminal-configuration',
];

/**
 * Admin-only screens
 */
export const ADMIN_ONLY_MENU_IDS = [
    'security',
    'user-permissions',
];

/**
 * Check if a role has access to a specific menu item
 */
export function hasRoleAccess(role: string | undefined, menuId: string): boolean {
    // Fallback: allow access if role not specified (for backward compatibility)
    if (!role) return true;

    const normalizedRole = role.toLowerCase();

    // Admin has full access
    if (normalizedRole === 'admin') return true;

    // Check admin-only screens (non-admin users cannot access)
    if (ADMIN_ONLY_MENU_IDS.includes(menuId)) {
        return false;
    }

    // Check POS-only screens
    if (POS_ONLY_MENU_IDS.includes(menuId)) {
        return normalizedRole === "posmanager" || normalizedRole === "posuser";
    }

    // Check category-level access
    const category = MENU_CATEGORY_MAPPING[menuId];
    if (category && normalizedRole in ROLE_MENU_VISIBILITY) {
        const roleVisibility = ROLE_MENU_VISIBILITY[normalizedRole as SystemRoleKey];
        if (roleVisibility) {
            return roleVisibility[category];
        }
    }

    // Default: allow access (for items not in mapping)
    return true;
}

/**
 * Get visible menu IDs for a role
 */
export function getVisibleMenusForRole(role: string | undefined): string[] {
    if (!role) return Object.keys(MENU_CATEGORY_MAPPING);

    const normalizedRole = role.toLowerCase() as SystemRoleKey;

    // Admin sees all
    if (normalizedRole === SYSTEM_ROLES.ADMIN) {
        return Object.keys(MENU_CATEGORY_MAPPING);
    }

    const roleVisibility = ROLE_MENU_VISIBILITY[normalizedRole];
    if (!roleVisibility) return [];

    return Object.entries(MENU_CATEGORY_MAPPING)
        .filter(([_, category]) => roleVisibility[category])
        .map(([menuId]) => menuId);
}

// =============================================================================
// MULTI-STORE / MULTI-COMPANY SCOPING CONFIGURATION
// =============================================================================

/**
 * Scoping rules for roles:
 * - Users may be scoped to one or more Stores
 * - Users may be scoped to one Company (default)
 * - POS roles must be store-scoped
 * - Back Office roles may be multi-store
 * - Administrator bypasses scoping checks
 */
export const ROLE_SCOPING_RULES: Record<SystemRoleKey, {
    requiresStoreScope: boolean;
    allowsMultiStore: boolean;
    bypassesScoping: boolean;
}> = {
    [SYSTEM_ROLES.ADMIN]: {
        requiresStoreScope: false,
        allowsMultiStore: true,
        bypassesScoping: true, // Admin bypasses all scoping
    },
    [SYSTEM_ROLES.BACKOFFICE_MANAGER]: {
        requiresStoreScope: false,
        allowsMultiStore: true, // Can access multiple stores
        bypassesScoping: false,
    },
    [SYSTEM_ROLES.BACKOFFICE_USER]: {
        requiresStoreScope: false,
        allowsMultiStore: true, // Can access multiple stores
        bypassesScoping: false,
    },
    [SYSTEM_ROLES.POS_MANAGER]: {
        requiresStoreScope: true, // Must be scoped to a store
        allowsMultiStore: true, // Can manage multiple stores
        bypassesScoping: false,
    },
    [SYSTEM_ROLES.POS_USER]: {
        requiresStoreScope: true, // Must be scoped to a store
        allowsMultiStore: false, // Single store only
        bypassesScoping: false,
    },
};

/**
 * TODO: Implement scoping enforcement helpers
 * 
 * function isUserScopedToLocation(user: User, locationId: number): boolean
 * function getUserAccessibleLocations(user: User): Location[]
 * function validateUserLocationAccess(user: User, locationId: number): void
 * 
 * These should use the UserLocationMapping model in the backend
 * and the user's location_mappings in the frontend state.
 */

/**
 * Check if a role requires store scoping
 */
export function roleRequiresStoreScope(role: string | undefined): boolean {
    if (!role) return false;
    const normalizedRole = role.toLowerCase() as SystemRoleKey;
    return ROLE_SCOPING_RULES[normalizedRole]?.requiresStoreScope ?? false;
}

/**
 * Check if a role bypasses scoping checks
 */
export function roleBypassesScoping(role: string | undefined): boolean {
    if (!role) return false;
    const normalizedRole = role.toLowerCase() as SystemRoleKey;
    return ROLE_SCOPING_RULES[normalizedRole]?.bypassesScoping ?? false;
}

