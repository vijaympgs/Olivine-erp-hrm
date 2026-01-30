import { useState, useEffect } from 'react';
import { useAuth } from '@auth/useAuth';

export interface ToolbarPermissions {
    new: boolean;
    edit: boolean;
    save: boolean;
    cancel: boolean;
    clear: boolean;
    authorize: boolean;
    submit: boolean;
    reject: boolean;
    amend: boolean;
    view: boolean;
    print: boolean;
    email: boolean;
    refresh: boolean;
    delete: boolean;
    hold: boolean;
    void: boolean;
    exit: boolean;
    upload: boolean;
    download: boolean;
    clone: boolean;
    first: boolean;
    prev: boolean;
    next: boolean;
    last: boolean;
    search: boolean;
    filter: boolean;
    notes: boolean;
    attach: boolean;
    settings: boolean;
    help: boolean;
}

export interface ToolbarConfig {
    viewId: string;
    viewName: string;
    viewType: string;
    module: string;
    submodule: string | null;
    toolbarConfig: string;
    permissions: ToolbarPermissions;
    hasOverride: boolean;
    routePath: string | null;
    componentName: string | null;
    breadcrumbs: string[];
}

export function useToolbarConfig(viewId: string) {
    const { user } = useAuth();
    const [config, setConfig] = useState<ToolbarConfig | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        async function fetchConfig() {
            if (!viewId || !user?.currentCompanyId) {
                setLoading(false);
                return;
            }

            try {
                setLoading(true);
                setError(null);

                const response = await fetch(
                    `/api/user_management/ui-config/${viewId}/?company_id=${user.currentCompanyId}`,
                    {
                        headers: {
                            'Authorization': `Bearer ${user.token}`,
                            'Content-Type': 'application/json'
                        }
                    }
                );

                if (!response.ok) {
                    throw new Error(`Failed to load toolbar config: ${response.statusText}`);
                }

                const data = await response.json();
                setConfig(data);
            } catch (err) {
                console.error('Failed to load toolbar config:', err);
                setError(err instanceof Error ? err.message : 'Unknown error');

                // Fallback to default config
                setConfig({
                    viewId,
                    viewName: viewId,
                    viewType: 'LIST',
                    module: 'RETAIL',
                    submodule: null,
                    toolbarConfig: '1,1,1,1,1,1,1,1,1,1,1,1,1,1,1',
                    permissions: {
                        new: true,
                        edit: true,
                        save: true,
                        cancel: true,
                        clear: true,
                        authorize: true,
                        submit: true,
                        reject: true,
                        amend: true,
                        view: true,
                        print: true,
                        email: true,
                        refresh: true,
                        delete: true,
                        hold: true,
                        void: true,
                        exit: true,
                        upload: true,
                        download: true,
                        clone: true,
                        first: true,
                        prev: true,
                        next: true,
                        last: true,
                        search: true,
                        filter: true,
                        notes: true,
                        attach: true,
                        settings: true,
                        help: true
                    },
                    hasOverride: false,
                    routePath: null,
                    componentName: null,
                    breadcrumbs: ['Home', viewId]
                });
            } finally {
                setLoading(false);
            }
        }

        fetchConfig();
    }, [viewId, user?.currentCompanyId, user?.token]);

    return { config, loading, error };
}

