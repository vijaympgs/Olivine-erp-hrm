/**
 * UI Audit Utility
 * 
 * Scans the application menu configuration and router to identify
 * which UI components are implemented vs. missing/incomplete.
 */

import { menuConfig, MenuItem } from '../app/menuConfig';
import { router } from '../app/router';

export interface UIAuditEntry {
    menuId: string;
    componentName: string;
    fullPath: string;
    routePath?: string;
    routeExists: boolean;
    uiStatus: 'Complete' | 'In Progress' | 'Missing' | 'Placeholder';
    module: string;
    level: number;
    notes: string;
}

/**
 * Flatten menu structure to get all leaf items
 */
const flattenMenu = (items: MenuItem[], parentPath: string = '', module: string = '', level: number = 1): UIAuditEntry[] => {
    let result: UIAuditEntry[] = [];

    items.forEach(item => {
        const fullPath = parentPath ? `${parentPath} > ${item.label}` : item.label;
        const currentModule = level === 1 ? item.label : module;

        // If item has a path, it's a leaf/screen
        if (item.path) {
            result.push({
                menuId: item.id,
                componentName: item.label,
                fullPath: fullPath,
                routePath: item.path,
                routeExists: false, // Will be populated later
                uiStatus: 'Missing', // Will be determined later
                module: currentModule,
                level: level,
                notes: ''
            });
        }

        // Recursively process children
        if (item.children && item.children.length > 0) {
            result = result.concat(flattenMenu(item.children, fullPath, currentModule, level + 1));
        }
    });

    return result;
};

/**
 * Check if a route exists in the router configuration
 */
const checkRouteExists = (path: string): boolean => {
    try {
        // Get all routes from the router
        const routes = router.routes;

        // Recursively search for the path
        const searchRoutes = (routeList: any[]): boolean => {
            for (const route of routeList) {
                if (route.path === path || route.path === path.substring(1)) {
                    return true;
                }
                if (route.children) {
                    if (searchRoutes(route.children)) {
                        return true;
                    }
                }
            }
            return false;
        };

        return searchRoutes(routes);
    } catch (error) {
        console.error('Error checking route:', error);
        return false;
    }
};

/**
 * Generate complete UI audit report
 */
export const generateUIAudit = (filterModule?: string): UIAuditEntry[] => {
    // Get all menu items
    let allItems = flattenMenu(menuConfig);

    // Filter by module if specified
    if (filterModule) {
        allItems = allItems.filter(item => item.module === filterModule);
    }

    // Check route existence for each item
    allItems.forEach(item => {
        if (item.routePath) {
            item.routeExists = checkRouteExists(item.routePath);

            // Determine UI status based on route existence
            if (item.routeExists) {
                // Route exists - could be Complete, In Progress, or Placeholder
                // This would require actual component inspection to determine
                // For now, mark as "In Progress" if route exists
                item.uiStatus = 'In Progress';
                item.notes = 'Route defined - requires manual verification';
            } else {
                item.uiStatus = 'Missing';
                item.notes = 'No route defined in router';
            }
        }
    });

    return allItems;
};

/**
 * Generate CSV report from audit data
 */
export const generateCSVReport = (auditData: UIAuditEntry[]): string => {
    const headers = [
        'Menu ID',
        'Component Name',
        'Full Path',
        'Route Path',
        'Route Exists',
        'UI Status',
        'Module',
        'Level',
        'Notes'
    ];

    const rows = auditData.map(item => [
        item.menuId,
        item.componentName.replace(/,/g, ';'), // Escape commas
        item.fullPath.replace(/,/g, ';'),
        item.routePath || '',
        item.routeExists ? 'Yes' : 'No',
        item.uiStatus,
        item.module,
        item.level.toString(),
        item.notes.replace(/,/g, ';')
    ]);

    return [
        headers.join(','),
        ...rows.map(row => row.join(','))
    ].join('\n');
};

/**
 * Download CSV report
 */
export const downloadUIAuditReport = (module?: string) => {
    const auditData = generateUIAudit(module);
    const csvContent = generateCSVReport(auditData);

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);

    const filename = module
        ? `ui_audit_${module.toLowerCase().replace(/\s+/g, '_')}_${new Date().toISOString().split('T')[0]}.csv`
        : `ui_audit_complete_${new Date().toISOString().split('T')[0]}.csv`;

    link.setAttribute('href', url);
    link.setAttribute('download', filename);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
};

/**
 * Get summary statistics
 */
export const getAuditSummary = (auditData: UIAuditEntry[]) => {
    const total = auditData.length;
    const complete = auditData.filter(item => item.uiStatus === 'Complete').length;
    const inProgress = auditData.filter(item => item.uiStatus === 'In Progress').length;
    const missing = auditData.filter(item => item.uiStatus === 'Missing').length;
    const placeholder = auditData.filter(item => item.uiStatus === 'Placeholder').length;

    return {
        total,
        complete,
        inProgress,
        missing,
        placeholder,
        completionPercentage: total > 0 ? Math.round((complete / total) * 100) : 0,
        implementedPercentage: total > 0 ? Math.round(((complete + inProgress) / total) * 100) : 0
    };
};

