import { useState, useEffect } from "react";
import { layoutManager, LayoutConfig } from "../config/layoutConfig";

/**
 * React Hook for Layout Configuration
 * 
 * Provides access to the current layout configuration and methods to update it.
 * Automatically re-renders components when configuration changes.
 * 
 * @example
 * ```tsx
 * const { config, updateConfig, resetConfig } = useLayoutConfig();
 * 
 * // Get current sidebar width
 * const sidebarWidth = config.sidebar.width;
 * 
 * // Update sidebar width
 * updateConfig({
 *   ...config,
 *   sidebar: { ...config.sidebar, width: 300 }
 * });
 * ```
 */
export const useLayoutConfig = () => {
    const [config, setConfig] = useState<LayoutConfig>(layoutManager.getConfig());

    useEffect(() => {
        // Listen for storage events (changes from other tabs)
        const handleStorageChange = (e: StorageEvent) => {
            if (e.key === 'olivine_layout_config') {
                setConfig(layoutManager.getConfig());
            }
        };

        // Listen for same-tab configuration updates
        const handleLayoutConfigUpdate = () => {
            setConfig(layoutManager.getConfig());
        };

        window.addEventListener('storage', handleStorageChange);
        window.addEventListener('layout-config-update', handleLayoutConfigUpdate);
        
        return () => {
            window.removeEventListener('storage', handleStorageChange);
            window.removeEventListener('layout-config-update', handleLayoutConfigUpdate);
        };
    }, []);

    const updateConfig = (newConfig: LayoutConfig) => {
        layoutManager.saveConfig(newConfig);
        setConfig(newConfig);
    };

    const resetConfig = () => {
        layoutManager.resetConfig();
        setConfig(layoutManager.getConfig());
    };

    const updateSection = <K extends keyof LayoutConfig>(
        section: K,
        updates: Partial<LayoutConfig[K]>
    ) => {
        layoutManager.updateSection(section, updates);
        setConfig(layoutManager.getConfig());
    };

    return {
        config,
        updateConfig,
        resetConfig,
        updateSection,
    };
};

/**
 * Hook to get a specific section of the layout configuration
 * 
 * @example
 * ```tsx
 * const sidebarConfig = useLayoutSection('sidebar');
 * console.log(sidebarConfig.width); // 256
 * ```
 */
export const useLayoutSection = <K extends keyof LayoutConfig>(
    section: K
): LayoutConfig[K] => {
    const { config } = useLayoutConfig();
    return config[section];
};

/**
 * Hook to check if a specific feature is enabled
 * 
 * @example
 * ```tsx
 * const showSubtitles = useLayoutFeature('sidebar', 'showSubtitles');
 * const compactMode = useLayoutFeature('general', 'compactMode');
 * ```
 */
export const useLayoutFeature = <
    K extends keyof LayoutConfig,
    F extends keyof LayoutConfig[K]
>(
    section: K,
    feature: F
): LayoutConfig[K][F] => {
    const sectionConfig = useLayoutSection(section);
    return sectionConfig[feature];
};

