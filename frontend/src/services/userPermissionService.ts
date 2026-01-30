import api from "./api";

// ============================================================================
// TYPE DEFINITIONS
// ============================================================================

export interface Permission {
    can_access?: boolean;
    can_view: boolean;
    can_create: boolean;
    can_edit: boolean;
    can_delete: boolean;
    override?: boolean;
}

export interface UserPermissions {
    [menuItemId: string]: Permission;
}

export interface Role {
    id: number;
    role_key: string;
    role_name: string;
    description?: string;
    is_system_role: boolean;
    is_active: boolean;
}

export interface MenuItem {
    id: string;
    menu_id: string;
    menu_name: string;
    parent_menu?: number | null;
    module_name: string;
    menu_order: number;
    is_active: boolean;
}

export interface MenuItemHierarchy {
    id: string;
    name: string;
    module: string;
    order: number;
    parent_id: string | null;
    children: MenuItemHierarchy[];
}

export interface PermissionMatrix {
    roles: Role[];
    menu_items: MenuItem[];
    matrix: {
        [roleKey: string]: {
            [menuId: string]: Permission;
        };
    };
}

export interface User {
    id: number;
    username: string;
    email: string;
    first_name: string;
    last_name: string;
    full_name: string;
    is_active: boolean;
    role?: string; // Current role key
    pos_location_id?: number; // POS location assignment
    profile?: {
        employee_code?: string;
        department?: string;
        designation?: string;
    };
}

export interface UserRole {
    id: number;
    user: number;
    role: number;
    user_username: string;
    role_name: string;
    assigned_by_username: string;
    assigned_at: string;
    is_active: boolean;
}

export interface UserLocation {
    id: string;
    user: number;
    location: number;
    user_username: string;
    location_name: string;
    access_type: "back_office" | "pos" | "both";
    is_active: boolean;
    is_default: boolean;
}

export interface RoleTemplate {
    name: string;
    description: string;
    default_permissions: Permission;
}

// ============================================================================
// USER PERMISSION SERVICE
// ============================================================================

export const userPermissionService = {
    // -------------------------------------------------------------------------
    // PERMISSION MATRIX
    // -------------------------------------------------------------------------

    // Get complete permission matrix for all roles and menu items
    getPermissionMatrix: async (): Promise<PermissionMatrix> => {
        const response = await api.get('/user-management/permission-matrix/');
        return response.data;
    },

    // Bulk update permissions for a role
    saveBulkRolePermissions: async (roleKey: string, permissions: UserPermissions) => {
        const response = await api.post('/user-management/permission-matrix/bulk/', {
            role_key: roleKey,
            permissions
        });
        return response.data;
    },

    // Get permissions for a specific role
    getRolePermissions: async (roleKey: string): Promise<UserPermissions> => {
        const response = await api.get(`/user-management/roles/${roleKey}/permissions/`);
        // Transform array response to object if needed
        if (Array.isArray(response.data)) {
            const perms: UserPermissions = {};
            response.data.forEach((item: any) => {
                const menuId = item.menu_item_name || item.menu_item;
                perms[menuId] = {
                    can_view: item.can_view,
                    can_create: item.can_create,
                    can_edit: item.can_edit,
                    can_delete: item.can_delete
                };
            });
            return perms;
        }
        return response.data;
    },

    // -------------------------------------------------------------------------
    // USER MANAGEMENT
    // -------------------------------------------------------------------------

    // Get all users
    getUsers: async (): Promise<User[]> => {
        const response = await api.get('/user-management/users/');
        return response.data;
    },

    // Get effective permissions for a specific user
    getUserPermissions: async (userId: number): Promise<{ user_id: number; username: string; permissions: UserPermissions }> => {
        const response = await api.get(`/user-management/users/${userId}/permissions/`);
        return response.data;
    },

    // Create a new user
    createUser: async (data: Partial<User>): Promise<User> => {
        const response = await api.post('/user-management/users/', data);
        return response.data;
    },

    // Update an existing user
    updateUser: async (id: number, data: Partial<User>): Promise<User> => {
        const response = await api.patch(`/user-management/users/${id}/`, data);
        return response.data;
    },

    // Delete a user
    deleteUser: async (id: number): Promise<void> => {
        await api.delete(`/user-management/users/${id}/`);
    },

    // -------------------------------------------------------------------------
    // ROLE MANAGEMENT
    // -------------------------------------------------------------------------

    // Get all roles
    getRoles: async (): Promise<Role[]> => {
        const response = await api.get('/user-management/roles/');
        return response.data;
    },

    // Create a new role
    createRole: async (data: Partial<Role>): Promise<Role> => {
        const response = await api.post('/user-management/roles/', data);
        return response.data;
    },

    // -------------------------------------------------------------------------
    // MENU ITEMS
    // -------------------------------------------------------------------------

    // Get menu items (flat list)
    getMenuItems: async (module: string = 'retail'): Promise<MenuItem[]> => {
        const response = await api.get(`/user-management/menu-items/?module=${module}`);
        return response.data;
    },

    // Get menu items in hierarchical structure
    getMenuHierarchy: async (module: string = 'retail'): Promise<MenuItemHierarchy[]> => {
        const response = await api.get(`/user-management/menu-items/hierarchy/?module=${module}`);
        return response.data;
    },

    // -------------------------------------------------------------------------
    // USER-ROLE MAPPING
    // -------------------------------------------------------------------------

    // Get user-role mappings
    getUserRoles: async (userId?: number): Promise<UserRole[]> => {
        const url = userId
            ? `/user-management/user-roles/?user_id=${userId}`
            : "/user-management/user-roles/";
        const response = await api.get(url);
        return response.data;
    },

    // Assign role to user
    assignUserRole: async (userId: number, roleKey: string) => {
        const response = await api.post('/user-management/user-roles/', {
            user_id: userId,
            role_key: roleKey
        });
        return response.data;
    },

    // Bulk update user roles
    bulkUpdateUserRoles: async (userId: number, roleKeys: string[]) => {
        const response = await api.post('/user-management/user-roles/bulk/', {
            user_id: userId,
            role_keys: roleKeys
        });
        return response.data;
    },

    // -------------------------------------------------------------------------
    // USER-LOCATION MAPPING
    // -------------------------------------------------------------------------

    // Get user-location mappings
    getUserLocations: async (userId?: number): Promise<UserLocation[]> => {
        const url = userId
            ? `/user-management/user-locations/?user_id=${userId}`
            : "/user-management/user-locations/";
        const response = await api.get(url);
        return response.data;
    },

    // Assign location to user
    assignUserLocation: async (userId: number, locationId: number, accessType: string = 'both', isDefault: boolean = false) => {
        const response = await api.post('/user-management/user-locations/', {
            user_id: userId,
            location_id: locationId,
            access_type: accessType,
            is_default: isDefault
        });
        return response.data;
    },

    // Bulk update user locations
    bulkUpdateUserLocations: async (userId: number, locationIds: number[], accessType: string = 'both') => {
        const response = await api.post('/user-management/user-locations/bulk/', {
            user_id: userId,
            location_ids: locationIds,
            access_type: accessType
        });
        return response.data;
    },

    // -------------------------------------------------------------------------
    // ROLE TEMPLATES
    // -------------------------------------------------------------------------

    // Get available role templates
    getRoleTemplates: async (): Promise<Record<string, RoleTemplate>> => {
        const response = await api.get('/user-management/role-templates/');
        return response.data;
    },

    // Apply role template to user
    applyRoleTemplate: async (userId: number, roleKey: string) => {
        const response = await api.post('/user-management/apply-role-template/', {
            user_id: userId,
            role_key: roleKey
        });
        return response.data;
    },

    // -------------------------------------------------------------------------
    // LOCATIONS (from Company module)
    // -------------------------------------------------------------------------

    // Get all locations
    getLocations: async () => {
        const response = await api.get('/companies/locations/');
        return response.data.results || response.data;
    },

    // -------------------------------------------------------------------------
    // LEGACY ENDPOINTS (for backward compatibility)
    // -------------------------------------------------------------------------

    saveUserLocationMapping: async (data: any) => {
        if (data.id) {
            return (await api.put(`/user-management/user-locations/${data.id}/`, data)).data;
        }
        return (await api.post('/user-management/user-locations/', {
            user_id: data.user,
            location_id: data.location,
            access_type: data.access_type || 'both',
            is_default: data.is_default || false
        })).data;
    }
};


