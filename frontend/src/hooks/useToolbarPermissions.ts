/**
 * useToolbarPermissions Hook
 * 
 * Fetches resolved toolbar permissions from backend API.
 * Implements client-side caching and error handling.
 * 
 * This hook replaces useToolbarConfig with permission-driven logic.
 */
import { useState, useEffect } from 'react';
import api from '@services/api';

export type MasterMode = 'VIEW' | 'NEW' | 'EDIT' | 'CREATE' | 'VIEW_FORM';

interface ToolbarPermissionsResponse {
    menu_id: string;
    mode: MasterMode;
    toolbar_string: string;
    permission_mask: string;
    allowed_characters: string[];
    allowed_actions: string[];
    error?: string;
}

interface UseToolbarPermissionsReturn {
    allowedActions: string[];
    loading: boolean;
    error: string | null;
    toolbarString: string;
    permissionMask: string;
}

/**
 * Hook to fetch and manage toolbar permissions
 * 
 * @param viewId - Menu ID (e.g., 'PURCHASE_ORDERS')
 * @param mode - UI mode ('VIEW', 'NEW', 'EDIT')
 * @param skip - Optional flag to skip API call (for fallback to old system)
 * @returns Resolved permissions and loading state
 * 
 * @example
 * const { allowedActions, loading } = useToolbarPermissions('PURCHASE_ORDERS', 'VIEW');
 * // allowedActions: ['new', 'edit', 'view', 'delete', 'refresh', ...]
 */
export const useToolbarPermissions = (
    viewId: string,
    mode: MasterMode,
    skip: boolean = false
): UseToolbarPermissionsReturn => {
    const [allowedActions, setAllowedActions] = useState<string[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const [toolbarString, setToolbarString] = useState<string>('');
    const [permissionMask, setPermissionMask] = useState<string>('');

    useEffect(() => {
        // Skip API call if flag is set (for fallback to old system)
        if (skip) {
            setLoading(false);
            setAllowedActions([]);
            return;
        }

        const fetchPermissions = async () => {
            if (!viewId) {
                setLoading(false);
                return;
            }

            try {
                setLoading(true);
                setError(null);

                // Normalize mode: CREATE -> NEW (backend only understands VIEW, NEW, EDIT)
                const normalizedMode = mode === 'CREATE' ? 'NEW' : mode;

                const response = await api.get<ToolbarPermissionsResponse>(
                    `user_management/toolbar-permissions/`,
                    {
                        params: {
                            menu_id: viewId,
                            mode: normalizedMode
                        }
                    }
                );

                if (response.data.error) {
                    setError(response.data.error);
                    setAllowedActions([]);
                    setToolbarString('');
                    setPermissionMask('');
                } else {
                    setAllowedActions(response.data.allowed_actions || []);
                    setToolbarString(response.data.toolbar_string || '');
                    setPermissionMask(response.data.permission_mask || '');
                    setError(null);
                }
            } catch (err: any) {
                console.error('Failed to fetch toolbar permissions:', err);

                // Provide helpful error message
                if (err.response?.status === 404) {
                    setError(`Screen "${viewId}" not found in menu registry`);
                } else if (err.response?.status === 401) {
                    setError('Authentication required');
                } else {
                    setError(err.response?.data?.error || 'Failed to load permissions');
                }

                // Fallback: allow only exit action
                setAllowedActions(['exit']);
                setToolbarString('');
                setPermissionMask('');
            } finally {
                setLoading(false);
            }
        };

        fetchPermissions();
    }, [viewId, mode]);

    return {
        allowedActions,
        loading,
        error,
        toolbarString,
        permissionMask
    };
};

/**
 * Legacy compatibility: useToolbarConfig
 * 
 * This is a wrapper around useToolbarPermissions for backward compatibility.
 * Converts the new permission system to the old config format.
 * 
 * @deprecated Use useToolbarPermissions instead
 */
export const useToolbarConfig = (viewId: string, mode: MasterMode) => {
    const { allowedActions, loading, error } = useToolbarPermissions(viewId, mode);

    // Convert allowed_actions array to old permission object format
    const permissions = {
        new: allowedActions.includes('new'),
        edit: allowedActions.includes('edit'),
        save: allowedActions.includes('save'),
        cancel: allowedActions.includes('cancel'),
        clear: allowedActions.includes('clear'),
        view: allowedActions.includes('view'),
        delete: allowedActions.includes('delete'),
        exit: allowedActions.includes('exit'),
        refresh: allowedActions.includes('refresh'),
        search: allowedActions.includes('search'),
        filter: allowedActions.includes('filter'),
        import: allowedActions.includes('import'),
        export: allowedActions.includes('export'),
        authorize: allowedActions.includes('authorize'),
        submit: allowedActions.includes('submit'),
        reject: allowedActions.includes('reject'),
        amend: allowedActions.includes('amend'),
        print: allowedActions.includes('print'),
        email: allowedActions.includes('email'),
        first: allowedActions.includes('first'),
        previous: allowedActions.includes('previous'),
        next: allowedActions.includes('next'),
        last: allowedActions.includes('last'),
        hold: allowedActions.includes('hold'),
        void: allowedActions.includes('void'),
        notes: allowedActions.includes('notes'),
        attach: allowedActions.includes('attach'),
        settings: allowedActions.includes('settings'),
        help: allowedActions.includes('help'),
    };

    return {
        config: {
            permissions,
            viewId,
            mode
        },
        loading,
        error
    };
};

