/**
 * Global Layout Configuration
 * 
 * This file serves as the central source of truth for all layout-related settings.
 * Settings can be overridden by user preferences stored in localStorage.
 */

export interface LayoutConfig {
    // Section A: Sidebar
    sidebar: {
        width: number;
        collapsedWidth: number;
        defaultCollapsed: boolean;
        showSubtitles: boolean;
        subtitleWrap: 'single-line' | 'wrap'; // Control subtitle text wrapping
        menuItemSpacing: 'compact' | 'normal' | 'comfortable'; // Control vertical spacing
        showPhase2: boolean; // Toggle Phase 2 menu items visibility
        // Module visibility toggles
        showRetail: boolean;
        showFinance: boolean;
        showCRM: boolean;
        showHRM: boolean;
        showTestConsole: boolean;
        testConsoleOptions: {
            showRetail: boolean;
            showFinance: boolean;
            showCRM: boolean;
            showHRM: boolean;
            showMeet: boolean;
        };

        // Background & Colors
        backgroundColor: string;
        surfaceColor: string;
        borderColor: string;
        dividerColor: string;
        dividerStyle: "gradient" | "solid" | "none";

        // Rail (L1) Settings
        rail: {
            width: number;
            backgroundColor: string;
            borderColor: string;
            activeIconBg: string;
            activeIconColor: string;
            inactiveIconColor: string;
            hoverIconBg: string;
            hoverIconColor: string;
        };

        // Panel (L2/L3) Settings
        panel: {
            width: number;
            backgroundColor: string;
            borderColor: string;
            headerBackgroundColor: string;
            headerTextColor: string;
            activeItemBg: string;
            activeItemColor: string;
        };

        // Menu Text Colors
        menuText: {
            level0Color: string;
            level0FontWeight: 400 | 500 | 600 | 700;
            level0FontSize: string;
            level0FontFamily: string;
            level1Color: string;
            level1FontWeight: 400 | 500 | 600 | 700;
            level1FontSize: string;
            level1FontFamily: string;
            level2Color: string;
            level2FontWeight: 400 | 500 | 600;
            level2FontSize: string;
            level2FontFamily: string;
            level3Color: string;
            level3FontWeight: 400 | 500 | 600;
            level3FontSize: string;
            level3FontFamily: string;
            hoverColor: string;
            hoverBackgroundColor: string;
        };

        // Selection Style
        menuSelection: {
            style: "flat" | "rounded" | "pill" | "full-span" | "left-border" | "custom";
            borderRadius: string;
            fullWidth: boolean;
            borderPosition: "left" | "right" | "top" | "bottom" | "none";
            borderWidth: number;
            showInsetGlow: boolean;
            glowIntensity: "none" | "subtle" | "medium" | "strong";
        };

        // Spacing
        menuSpacing: {
            itemSpacing: "compact" | "normal" | "comfortable" | "spacious" | "custom";
            customItemGap: number;
            customGroupGap: number;
            itemPaddingY: "compact" | "normal" | "comfortable" | "custom";
            customPaddingY: number;
            itemPaddingX: number;
            indentationSize: "compact" | "normal" | "wide" | "custom";
            customIndentation: number;
        };

        // Icons
        menuIcons: {
            showLevel0Icons: boolean;
            showLevel1Icons: boolean;
            showLevel2Icons: boolean;
            iconSize: "small" | "normal" | "large";
            iconOpacity: number;
            iconStrokeWidth: number;
            iconColorInactive: string;
            iconColorActive: string;
            iconColorHover: string;
        };

        // Behavior
        menuBehavior: {
            collapseAnimation: boolean;
            hoverEffect: "subtle" | "normal" | "prominent" | "none";
            transitionSpeed: "fast" | "normal" | "slow";
        };
    };

    // Active Menu Item Styling
    activeMenuItem: {
        style: "foxpro" | "modern" | "minimal" | "custom";
        backgroundColor: string;
        textColor: string;
        borderColor: string;
        borderWidth: number;
        fontWeight: number;
    };

    // Section B: Application Header
    header: {
        height: number;
        backgroundColor: string;
        borderColor: string;
        showUserMenu: boolean;
        showNotifications: boolean;
        showSearch: boolean;
        // AppHeader Styling
        bgStyle?: "solid" | "gradient";
        bgColor?: string;
        gradientStart?: string;
        gradientEnd?: string;
        brandColor?: string;        // "Olivine" text color
        companyColor?: string;      // Company name text color
        iconColor?: string;         // Icon colors
    };

    // Section C: Primary Workspace
    workspace: {
        backgroundColor: string;
        padding: number;
    };

    // Section D: Status Bar
    statusBar: {
        height: number;
        show: boolean;
        backgroundColor: string;
        borderColor: string;
        showConnectionStatus: boolean;
        showSessionInfo: boolean;
    };

    // General Settings
    general: {
        theme: "light" | "dark" | "auto";
        compactMode: boolean;
        animationsEnabled: boolean;
        fontFamily: string;
        fontSize: {
            xs: string;
            sm: string;
            base: string;
            lg: string;
            xl: string;
        };
    };

    // Form Settings
    forms: {
        defaultGridColumns: number;
        inputPadding: string;
        labelFontSize: string;
        errorColor: string;
    };

    // Button Settings
    buttons: {
        primary: {
            backgroundColor: string;
            textColor: string;
            hoverBackgroundColor: string;
            hoverTextColor: string;
        };
        secondary: {
            backgroundColor: string;
            textColor: string;
            borderColor: string;
            hoverBackgroundColor: string;
        };
    };

    // Lookup Panel Settings
    lookup: {
        width: string;
        startPosition: "right" | "left";
        hasBackdrop: boolean;
        headerStyle: "flat" | "gradient";
        animationDuration: number;
        zIndex: number;
    };

    // Modal Settings
    modal: {
        maxWidth: string;
        backgroundColor: string;
        borderColor: string;
        borderRadius: string;
        backdropColor: string;
        backdropBlur: string;
        shadowIntensity: "none" | "sm" | "md" | "lg" | "xl" | "2xl";
        padding: string;
        zIndex: number;
    };

    // Typography Hierarchy
    typography: {
        // L1: Page Titles
        l1: {
            fontSize: string;
            fontWeight: number;
            color: string;
            lineHeight: string;
            letterSpacing: string;
        };
        // L2: Section Headers
        l2: {
            fontSize: string;
            fontWeight: number;
            color: string;
            lineHeight: string;
            letterSpacing: string;
        };
        // L3: Subsection Headers
        l3: {
            fontSize: string;
            fontWeight: number;
            color: string;
            lineHeight: string;
            letterSpacing: string;
        };
        // L4: Form Labels & Body Text (Standard)
        l4: {
            fontSize: string;
            fontWeight: number;
            color: string;
            lineHeight: string;
            letterSpacing: string;
        };
        // Form-specific typography
        formLabel: {
            fontSize: string;
            fontWeight: number;
            color: string;
        };
        formInput: {
            fontSize: string;
            fontWeight: number;
            color: string;
        };
        formHelper: {
            fontSize: string;
            fontWeight: number;
            color: string;
        };
        formError: {
            fontSize: string;
            fontWeight: number;
            color: string;
        };
    };
}

/**
 * Default Layout Configuration
 * FoxPro-style with modern adaptations
 */
export const defaultLayoutConfig: LayoutConfig = {
    sidebar: {
        width: 256,
        collapsedWidth: 80,
        defaultCollapsed: false,
        showSubtitles: false,
        subtitleWrap: 'single-line', // Default to single line
        menuItemSpacing: 'normal', // Default to normal spacing
        showPhase2: false, // Phase 2 features hidden by default
        // Module visibility (all enabled by default)
        showRetail: true,
        showFinance: true,
        showCRM: true,
        showHRM: true,
        showTestConsole: true,
        testConsoleOptions: {
            showRetail: true,
            showFinance: true,
            showCRM: true,
            showHRM: true,
            showMeet: true,
        },

        // Background & Colors (Olivine Console Dark Theme)
        backgroundColor: '#0E0F1A',
        surfaceColor: '#14162A',
        borderColor: 'rgba(255,255,255,0.06)',
        dividerColor: 'rgba(255,255,255,0.08)',
        dividerStyle: 'gradient',

        // Rail Defaults (Matches EnterpriseSidebar)
        rail: {
            width: 72,
            backgroundColor: '#E2E8F0', // slate-200
            borderColor: '#CBD5E1', // slate-300
            activeIconBg: '#2563EB', // blue-600
            activeIconColor: '#FFFFFF', // white
            inactiveIconColor: '#475569', // slate-600
            hoverIconBg: '#CBD5E1', // slate-300
            hoverIconColor: '#0F172A', // slate-900
        },

        // Panel Defaults (Matches EnterpriseSidebar)
        panel: {
            width: 320,
            backgroundColor: '#F1F5F9', // slate-100
            borderColor: '#CBD5E1', // slate-300
            headerBackgroundColor: '#F8FAFC', // slate-50
            headerTextColor: '#64748B', // slate-500
            activeItemBg: '#EFF6FF', // blue-50
            activeItemColor: '#1E40AF', // blue-800
        },

        // Menu Text Colors
        menuText: {
            level0Color: '#A4A7C1',
            level0FontWeight: 600,
            level0FontSize: '11px',
            level0FontFamily: 'Segoe UI',
            level1Color: '#8B8FAF',
            level1FontWeight: 500,
            level1FontSize: '12px',
            level1FontFamily: 'Segoe UI',
            level2Color: '#8B8FAF',
            level2FontWeight: 400,
            level2FontSize: '12px',
            level2FontFamily: 'Segoe UI',
            level3Color: '#8B8FAF',
            level3FontWeight: 400,
            level3FontSize: '11px',
            level3FontFamily: 'Segoe UI',
            hoverColor: '#E7E9F1',
            hoverBackgroundColor: 'rgba(255,255,255,0.05)',
        },

        // Selection Style
        menuSelection: {
            style: 'flat',
            borderRadius: '0px',
            fullWidth: false,
            borderPosition: 'left',
            borderWidth: 3,
            showInsetGlow: true,
            glowIntensity: 'subtle',
        },

        // Spacing
        menuSpacing: {
            itemSpacing: 'normal',
            customItemGap: 4,
            customGroupGap: 16,
            itemPaddingY: 'normal',
            customPaddingY: 10,
            itemPaddingX: 12,
            indentationSize: 'normal',
            customIndentation: 20,
        },

        // Icons
        menuIcons: {
            showLevel0Icons: true,
            showLevel1Icons: false,
            showLevel2Icons: false,
            iconSize: 'normal',
            iconOpacity: 0.85,
            iconStrokeWidth: 1.5,
            iconColorInactive: '#6F7396',
            iconColorActive: '#7C6AF2',
            iconColorHover: '#E7E9F1',
        },

        // Behavior
        menuBehavior: {
            collapseAnimation: true,
            hoverEffect: 'normal',
            transitionSpeed: 'normal',
        },
    },

    activeMenuItem: {
        style: 'foxpro',
        backgroundColor: '#22D3EE', // Cyan
        textColor: '#DC2626',       // Red
        borderColor: '#DC2626',     // Red
        borderWidth: 2,
        fontWeight: 700,
    },

    header: {
        height: 64,
        backgroundColor: '#FFFFFF',
        borderColor: '#E5E7EB',
        showUserMenu: true,
        showNotifications: true,
        showSearch: true,
        // AppHeader Styling
        bgStyle: 'gradient',
        bgColor: '#14162A',
        gradientStart: '#14162A',
        gradientEnd: '#101223',
    },

    workspace: {
        backgroundColor: '#FFFFFF',
        padding: 16,
    },

    statusBar: {
        height: 48,
        show: true,
        backgroundColor: '#F9FAFB',
        borderColor: '#E5E7EB',
        showConnectionStatus: true,
        showSessionInfo: true,
    },

    general: {
        theme: 'light',
        compactMode: false,
        animationsEnabled: true,
        fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        fontSize: {
            xs: '12px',
            sm: '14px',
            base: '16px',
            lg: '18px',
            xl: '20px',
        },
    },

    forms: {
        defaultGridColumns: 3,
        inputPadding: '6px 8px',
        labelFontSize: '12px',
        errorColor: '#DC2626',
    },

    buttons: {
        primary: {
            backgroundColor: '#F97316',      // Orange-500 (matches panel activeItemBg when set to orange)
            textColor: '#FFFFFF',            // White (matches panel activeItemColor when set to white)
            hoverBackgroundColor: '#EA580C', // Orange-600
            hoverTextColor: '#FFFFFF',
        },
        secondary: {
            backgroundColor: '#FFFFFF',
            textColor: '#374151',            // Gray-700
            borderColor: '#D1D5DB',          // Gray-300
            hoverBackgroundColor: '#F9FAFB', // Gray-50
        },
    },

    // Lookup Panel Settings (Mindra Human Card Style)
    lookup: {
        width: '650px', // Enhanced width for enterprise density
        startPosition: 'right', // Slide from right
        hasBackdrop: false, // Non-modal (form remains usable)
        headerStyle: 'flat', // No gradients
        animationDuration: 300,
        zIndex: 60, // Above Header (z-50) for overlap protection
    },

    // Modal Settings
    modal: {
        maxWidth: '90vw', // Fit within workspace
        backgroundColor: '#FFFFFF',
        borderColor: '#E5E7EB',
        borderRadius: '8px',
        backdropColor: 'rgba(0, 0, 0, 0.5)',
        backdropBlur: '4px',
        shadowIntensity: 'xl',
        padding: '24px',
        zIndex: 50,
    },

    // Typography Hierarchy
    typography: {
        // L1: Page Titles
        l1: {
            fontSize: '24px',
            fontWeight: 700,
            color: '#111827',
            lineHeight: '1.25',
            letterSpacing: '-0.025em',
        },
        // L2: Section Headers
        l2: {
            fontSize: '18px',
            fontWeight: 600,
            color: '#1F2937',
            lineHeight: '1.375',
            letterSpacing: '-0.0125em',
        },
        // L3: Subsection Headers
        l3: {
            fontSize: '14px',
            fontWeight: 600,
            color: '#374151',
            lineHeight: '1.5',
            letterSpacing: '0',
        },
        // L4: Form Labels & Body Text (Standard)
        l4: {
            fontSize: '12px',
            fontWeight: 400,
            color: '#4B5563',
            lineHeight: '1.5',
            letterSpacing: '0',
        },
        // Form-specific typography
        formLabel: {
            fontSize: '12px',
            fontWeight: 500,
            color: '#374151',
        },
        formInput: {
            fontSize: '14px',
            fontWeight: 400,
            color: '#111827',
        },
        formHelper: {
            fontSize: '12px',
            fontWeight: 400,
            color: '#6B7280',
        },
        formError: {
            fontSize: '12px',
            fontWeight: 500,
            color: '#DC2626',
        },
    }
};

/**
 * Style Presets for Active Menu Items
 */
export const activeMenuPresets = {
    foxpro: {
        label: 'FoxPro Classic',
        description: 'Cyan background with red text (nostalgic)',
        backgroundColor: '#22D3EE',
        textColor: '#DC2626',
        borderColor: '#DC2626',
    },
    modern: {
        label: 'Modern Blue',
        description: 'Blue background with white text',
        backgroundColor: '#2563EB',
        textColor: '#FFFFFF',
        borderColor: '#1D4ED8',
    },
    minimal: {
        label: 'Minimal Gray',
        description: 'Light gray background with dark text',
        backgroundColor: '#F3F4F6',
        textColor: '#111827',
        borderColor: '#3B82F6',
    },
};

/**
 * Layout Manager Class
 * Handles loading, saving, and applying layout configurations
 */
export class LayoutManager {
    private static instance: LayoutManager;
    private config: LayoutConfig;
    private readonly STORAGE_KEY = "olivine_layout_config";

    private constructor() {
        this.config = this.loadConfig();
        this.applyConfig();
    }

    static getInstance(): LayoutManager {
        if (!LayoutManager.instance) {
            LayoutManager.instance = new LayoutManager();
        }
        return LayoutManager.instance;
    }

    /**
     * Load configuration from localStorage or use defaults
     */
    private loadConfig(): LayoutConfig {
        try {
            const saved = localStorage.getItem(this.STORAGE_KEY);
            if (saved) {
                const parsed = JSON.parse(saved);
                // Merge with defaults to ensure all properties exist
                return this.mergeConfig(defaultLayoutConfig, parsed);
            }
        } catch (error) {
            console.error('Failed to load layout config:', error);
        }
        return { ...defaultLayoutConfig };
    }

    /**
     * Deep merge configuration objects
     */
    private mergeConfig(defaults: any, overrides: any): any {
        const result = { ...defaults };
        for (const key in overrides) {
            if (overrides[key] && typeof overrides[key] === 'object' && !Array.isArray(overrides[key])) {
                result[key] = this.mergeConfig(defaults[key] || {}, overrides[key]);
            } else {
                result[key] = overrides[key];
            }
        }
        return result;
    }

    /**
     * Save configuration to localStorage
     */
    saveConfig(config: LayoutConfig): void {
        try {
            this.config = config;
            localStorage.setItem(this.STORAGE_KEY, JSON.stringify(config));
            this.applyConfig();

            // Dispatch event for same-tab updates
            window.dispatchEvent(new CustomEvent('layout-config-update'));
        } catch (error) {
            console.error('Failed to save layout config:', error);
        }
    }

    /**
     * Get current configuration
     */
    getConfig(): LayoutConfig {
        return { ...this.config };
    }

    /**
     * Reset to default configuration
     */
    resetConfig(): void {
        this.config = { ...defaultLayoutConfig };
        localStorage.removeItem(this.STORAGE_KEY);
        this.applyConfig();
    }

    /**
     * Darken a hex color by a percentage
     */
    private darkenColor(hex: string, percent: number): string {
        // Remove # if present
        hex = hex.replace('#', '');

        // Convert to RGB
        const r = parseInt(hex.substring(0, 2), 16);
        const g = parseInt(hex.substring(2, 4), 16);
        const b = parseInt(hex.substring(4, 6), 16);

        // Darken by percentage
        const factor = 1 - (percent / 100);
        const newR = Math.round(r * factor);
        const newG = Math.round(g * factor);
        const newB = Math.round(b * factor);

        // Convert back to hex
        const toHex = (n: number) => {
            const hex = n.toString(16);
            return hex.length === 1 ? '0' + hex : hex;
        };

        return `#${toHex(newR)}${toHex(newG)}${toHex(newB)}`;
    }

    /**
     * Apply configuration to CSS variables
     */
    applyConfig(): void {
        const root = document.documentElement;

        // Sidebar
        root.style.setProperty('--sidebar-width', `${this.config.sidebar.width}px`);
        root.style.setProperty('--sidebar-collapsed-width', `${this.config.sidebar.collapsedWidth}px`);
        root.style.setProperty('--sidebar-bg', this.config.sidebar.backgroundColor);
        root.style.setProperty('--sidebar-border', this.config.sidebar.borderColor);

        // Sidebar Rail
        root.style.setProperty('--sidebar-rail-width', `${this.config.sidebar.rail.width}px`);
        root.style.setProperty('--sidebar-rail-bg', this.config.sidebar.rail.backgroundColor);
        root.style.setProperty('--sidebar-rail-border', this.config.sidebar.rail.borderColor);
        root.style.setProperty('--sidebar-rail-active-bg', this.config.sidebar.rail.activeIconBg);
        root.style.setProperty('--sidebar-rail-active-color', this.config.sidebar.rail.activeIconColor);
        root.style.setProperty('--sidebar-rail-inactive-color', this.config.sidebar.rail.inactiveIconColor);
        root.style.setProperty('--sidebar-rail-hover-bg', this.config.sidebar.rail.hoverIconBg);
        root.style.setProperty('--sidebar-rail-hover-color', this.config.sidebar.rail.hoverIconColor);

        // Sidebar Panel
        root.style.setProperty('--sidebar-panel-width', `${this.config.sidebar.panel.width}px`);
        root.style.setProperty('--sidebar-panel-bg', this.config.sidebar.panel.backgroundColor);
        root.style.setProperty('--sidebar-panel-border', this.config.sidebar.panel.borderColor);
        root.style.setProperty('--sidebar-panel-header-bg', this.config.sidebar.panel.headerBackgroundColor);
        root.style.setProperty('--sidebar-panel-header-text', this.config.sidebar.panel.headerTextColor);
        root.style.setProperty('--sidebar-panel-active-bg', this.config.sidebar.panel.activeItemBg);
        root.style.setProperty('--sidebar-panel-active-color', this.config.sidebar.panel.activeItemColor);

        // Menu Text Typography
        root.style.setProperty('--menu-level0-font-size', this.config.sidebar.menuText.level0FontSize);
        root.style.setProperty('--menu-level0-font-weight', String(this.config.sidebar.menuText.level0FontWeight));
        root.style.setProperty('--menu-level0-font-family', this.config.sidebar.menuText.level0FontFamily);

        root.style.setProperty('--menu-level1-font-size', this.config.sidebar.menuText.level1FontSize);
        root.style.setProperty('--menu-level1-font-weight', String(this.config.sidebar.menuText.level1FontWeight));
        root.style.setProperty('--menu-level1-font-family', this.config.sidebar.menuText.level1FontFamily);

        root.style.setProperty('--menu-level2-font-size', this.config.sidebar.menuText.level2FontSize);
        root.style.setProperty('--menu-level2-font-weight', String(this.config.sidebar.menuText.level2FontWeight));
        root.style.setProperty('--menu-level2-font-family', this.config.sidebar.menuText.level2FontFamily);

        root.style.setProperty('--menu-level3-font-size', this.config.sidebar.menuText.level3FontSize);
        root.style.setProperty('--menu-level3-font-weight', String(this.config.sidebar.menuText.level3FontWeight));
        root.style.setProperty('--menu-level3-font-family', this.config.sidebar.menuText.level3FontFamily);

        // Active Menu Item
        root.style.setProperty('--active-bg', this.config.activeMenuItem.backgroundColor);
        root.style.setProperty('--active-text', this.config.activeMenuItem.textColor);
        root.style.setProperty('--active-border', this.config.activeMenuItem.borderColor);
        root.style.setProperty('--active-border-width', `${this.config.activeMenuItem.borderWidth}px`);
        root.style.setProperty('--active-font-weight', `${this.config.activeMenuItem.fontWeight}`);

        // Menu Selection Style
        root.style.setProperty('--menu-border-radius', this.config.sidebar.menuSelection.borderRadius);


        // Header
        root.style.setProperty('--header-height', `${this.config.header.height}px`);
        root.style.setProperty('--header-bg', this.config.header.backgroundColor);
        root.style.setProperty('--header-border', this.config.header.borderColor);

        // Workspace
        root.style.setProperty('--workspace-bg', this.config.workspace.backgroundColor);
        root.style.setProperty('--workspace-padding', `${this.config.workspace.padding}px`);

        // Status Bar
        root.style.setProperty('--statusbar-height', `${this.config.statusBar.height}px`);
        root.style.setProperty('--statusbar-bg', this.config.statusBar.backgroundColor);
        root.style.setProperty('--statusbar-border', this.config.statusBar.borderColor);

        // Lookup Panel
        if (this.config.lookup) {
            root.style.setProperty('--lookup-width', this.config.lookup.width);
            root.style.setProperty('--lookup-z-index', String(this.config.lookup.zIndex));
            root.style.setProperty('--lookup-transition', `${this.config.lookup.animationDuration}ms`);
        }

        // General
        root.style.setProperty('--font-family', this.config.general.fontFamily);
        root.style.setProperty('--font-size-xs', this.config.general.fontSize.xs);
        root.style.setProperty('--font-size-sm', this.config.general.fontSize.sm);
        root.style.setProperty('--font-size-base', this.config.general.fontSize.base);
        root.style.setProperty('--font-size-lg', this.config.general.fontSize.lg);
        root.style.setProperty('--font-size-xl', this.config.general.fontSize.xl);

        // Forms
        root.style.setProperty('--form-error-color', this.config.forms.errorColor);

        // Modal
        root.style.setProperty('--modal-max-width', this.config.modal.maxWidth);
        root.style.setProperty('--modal-bg', this.config.modal.backgroundColor);
        root.style.setProperty('--modal-border', this.config.modal.borderColor);
        root.style.setProperty('--modal-border-radius', this.config.modal.borderRadius);
        root.style.setProperty('--modal-backdrop', this.config.modal.backdropColor);
        root.style.setProperty('--modal-backdrop-blur', this.config.modal.backdropBlur);
        root.style.setProperty('--modal-shadow', this.config.modal.shadowIntensity);
        root.style.setProperty('--modal-padding', this.config.modal.padding);
        root.style.setProperty('--modal-z-index', String(this.config.modal.zIndex));

        // Typography - L1 (Page Titles)
        root.style.setProperty('--typography-l1-size', this.config.typography.l1.fontSize);
        root.style.setProperty('--typography-l1-weight', String(this.config.typography.l1.fontWeight));
        root.style.setProperty('--typography-l1-color', this.config.typography.l1.color);
        root.style.setProperty('--typography-l1-line-height', this.config.typography.l1.lineHeight);
        root.style.setProperty('--typography-l1-letter-spacing', this.config.typography.l1.letterSpacing);

        // Typography - L2 (Section Headers)
        root.style.setProperty('--typography-l2-size', this.config.typography.l2.fontSize);
        root.style.setProperty('--typography-l2-weight', String(this.config.typography.l2.fontWeight));
        root.style.setProperty('--typography-l2-color', this.config.typography.l2.color);
        root.style.setProperty('--typography-l2-line-height', this.config.typography.l2.lineHeight);
        root.style.setProperty('--typography-l2-letter-spacing', this.config.typography.l2.letterSpacing);

        // Typography - L3 (Subsection Headers)
        root.style.setProperty('--typography-l3-size', this.config.typography.l3.fontSize);
        root.style.setProperty('--typography-l3-weight', String(this.config.typography.l3.fontWeight));
        root.style.setProperty('--typography-l3-color', this.config.typography.l3.color);
        root.style.setProperty('--typography-l3-line-height', this.config.typography.l3.lineHeight);
        root.style.setProperty('--typography-l3-letter-spacing', this.config.typography.l3.letterSpacing);

        // Typography - L4 (Form Labels & Body)
        root.style.setProperty('--typography-l4-size', this.config.typography.l4.fontSize);
        root.style.setProperty('--typography-l4-weight', String(this.config.typography.l4.fontWeight));
        root.style.setProperty('--typography-l4-color', this.config.typography.l4.color);
        root.style.setProperty('--typography-l4-line-height', this.config.typography.l4.lineHeight);
        root.style.setProperty('--typography-l4-letter-spacing', this.config.typography.l4.letterSpacing);

        // Typography - Form Specific
        root.style.setProperty('--form-label-size', this.config.typography.formLabel.fontSize);
        root.style.setProperty('--form-label-weight', String(this.config.typography.formLabel.fontWeight));
        root.style.setProperty('--form-label-color', this.config.typography.formLabel.color);

        root.style.setProperty('--form-input-size', this.config.typography.formInput.fontSize);
        root.style.setProperty('--form-input-weight', String(this.config.typography.formInput.fontWeight));
        root.style.setProperty('--form-input-color', this.config.typography.formInput.color);

        root.style.setProperty('--form-helper-size', this.config.typography.formHelper.fontSize);
        root.style.setProperty('--form-helper-weight', String(this.config.typography.formHelper.fontWeight));
        root.style.setProperty('--form-helper-color', this.config.typography.formHelper.color);

        root.style.setProperty('--form-error-size', this.config.typography.formError.fontSize);
        root.style.setProperty('--form-error-weight', String(this.config.typography.formError.fontWeight));
        root.style.setProperty('--form-error-color-text', this.config.typography.formError.color);

        // Apply theme
        if (this.config.general.theme === 'dark') {
            root.classList.add('dark');
        } else {
            root.classList.remove('dark');
        }

        // Apply compact mode
        if (this.config.general.compactMode) {
            root.classList.add('compact-mode');
        } else {
            root.classList.remove('compact-mode');
        }

        // Buttons - Use panel active item colors for primary buttons
        root.style.setProperty('--button-primary-bg', this.config.sidebar.panel.activeItemBg);
        root.style.setProperty('--button-primary-text', this.config.sidebar.panel.activeItemColor);
        // Darken the active bg by 10% for hover (simple approach)
        root.style.setProperty('--button-primary-hover-bg', this.darkenColor(this.config.sidebar.panel.activeItemBg, 10));
        root.style.setProperty('--button-primary-hover-text', this.config.sidebar.panel.activeItemColor);
        root.style.setProperty('--button-secondary-bg', this.config.buttons.secondary.backgroundColor);
        root.style.setProperty('--button-secondary-text', this.config.buttons.secondary.textColor);
        root.style.setProperty('--button-secondary-border', this.config.buttons.secondary.borderColor);
        root.style.setProperty('--button-secondary-hover-bg', this.config.buttons.secondary.hoverBackgroundColor);

        // Apply animations
        if (!this.config.general.animationsEnabled) {
            root.classList.add('no-animations');
        } else {
            root.classList.remove('no-animations');
        }
    }

    /**
     * Update a specific section of the configuration
     */
    updateSection<K extends keyof LayoutConfig>(
        section: K,
        updates: Partial<LayoutConfig[K]>
    ): void {
        this.config[section] = {
            ...this.config[section],
            ...updates,
        };
        this.saveConfig(this.config);
    }

    /**
     * Apply a preset style for active menu items
     */
    applyActiveMenuPreset(preset: keyof typeof activeMenuPresets): void {
        const presetData = activeMenuPresets[preset];
        this.updateSection('activeMenuItem', {
            style: preset,
            backgroundColor: presetData.backgroundColor,
            textColor: presetData.textColor,
            borderColor: presetData.borderColor,
        });
    }
}

/**
 * Sidebar Style Presets
 */
export const sidebarStylePresets = {
    'compact-dark': {
        name: 'Compact Dark',
        description: 'Dense, dark theme with minimal spacing',
        config: {
            backgroundColor: '#0A0B14',
            surfaceColor: '#10111A',
            borderColor: 'rgba(255,255,255,0.04)',
            dividerColor: 'rgba(255,255,255,0.06)',
            dividerStyle: 'solid' as const,
            menuText: {
                level0Color: '#9CA3AF',
                level0FontWeight: 600 as const,
                level1Color: '#6B7280',
                level1FontWeight: 500 as const,
                level2Color: '#6B7280',
                level2FontWeight: 400 as const,
                level3Color: '#6B7280',
                level3FontWeight: 400 as const,
                hoverColor: '#F3F4F6',
                hoverBackgroundColor: 'rgba(255,255,255,0.03)',
            },
            menuSelection: {
                style: 'flat' as const,
                borderRadius: '0px',
                fullWidth: true,
                borderPosition: 'left' as const,
                borderWidth: 2,
                showInsetGlow: false,
                glowIntensity: 'none' as const,
            },
            menuSpacing: {
                itemSpacing: 'compact' as const,
                customItemGap: 2,
                customGroupGap: 12,
                itemPaddingY: 'compact' as const,
                customPaddingY: 6,
                itemPaddingX: 10,
                indentationSize: 'compact' as const,
                customIndentation: 16,
            },
            menuIcons: {
                showLevel0Icons: true,
                showLevel1Icons: false,
                showLevel2Icons: false,
                iconSize: 'small' as const,
                iconOpacity: 0.75,
                iconStrokeWidth: 1.5,
                iconColorInactive: '#6B7280',
                iconColorActive: '#60A5FA',
                iconColorHover: '#F3F4F6',
            },
            menuBehavior: {
                collapseAnimation: true,
                hoverEffect: 'subtle' as const,
                transitionSpeed: 'fast' as const,
            },
        },
    },
    'spacious-light': {
        name: 'Spacious Light',
        description: 'Light theme with generous spacing and breathing room',
        config: {
            backgroundColor: '#FFFFFF',
            surfaceColor: '#F9FAFB',
            borderColor: '#E5E7EB',
            dividerColor: '#E5E7EB',
            dividerStyle: 'gradient' as const,
            menuText: {
                level0Color: '#374151',
                level0FontWeight: 600 as const,
                level1Color: '#6B7280',
                level1FontWeight: 500 as const,
                level2Color: '#6B7280',
                level2FontWeight: 400 as const,
                level3Color: '#9CA3AF',
                level3FontWeight: 400 as const,
                hoverColor: '#111827',
                hoverBackgroundColor: '#F3F4F6',
            },
            menuSelection: {
                style: 'pill' as const,
                borderRadius: '999px',
                fullWidth: false,
                borderPosition: 'none' as const,
                borderWidth: 0,
                showInsetGlow: false,
                glowIntensity: 'none' as const,
            },
            menuSpacing: {
                itemSpacing: 'spacious' as const,
                customItemGap: 8,
                customGroupGap: 24,
                itemPaddingY: 'comfortable' as const,
                customPaddingY: 14,
                itemPaddingX: 16,
                indentationSize: 'wide' as const,
                customIndentation: 28,
            },
            menuIcons: {
                showLevel0Icons: true,
                showLevel1Icons: true,
                showLevel2Icons: false,
                iconSize: 'large' as const,
                iconOpacity: 0.9,
                iconStrokeWidth: 1.5,
                iconColorInactive: '#9CA3AF',
                iconColorActive: '#3B82F6',
                iconColorHover: '#1F2937',
            },
            menuBehavior: {
                collapseAnimation: true,
                hoverEffect: 'prominent' as const,
                transitionSpeed: 'normal' as const,
            },
        },
    },
    'classic': {
        name: 'Classic',
        description: 'Traditional FoxPro-inspired style with balanced spacing',
        config: {
            backgroundColor: '#F9FAFB',
            surfaceColor: '#FFFFFF',
            borderColor: '#E5E7EB',
            dividerColor: '#D1D5DB',
            dividerStyle: 'solid' as const,
            menuText: {
                level0Color: '#1F2937',
                level0FontWeight: 700 as const,
                level1Color: '#374151',
                level1FontWeight: 600 as const,
                level2Color: '#4B5563',
                level2FontWeight: 500 as const,
                level3Color: '#6B7280',
                level3FontWeight: 400 as const,
                hoverColor: '#111827',
                hoverBackgroundColor: '#F3F4F6',
            },
            menuSelection: {
                style: 'left-border' as const,
                borderRadius: '0px',
                fullWidth: true,
                borderPosition: 'left' as const,
                borderWidth: 4,
                showInsetGlow: false,
                glowIntensity: 'none' as const,
            },
            menuSpacing: {
                itemSpacing: 'normal' as const,
                customItemGap: 4,
                customGroupGap: 16,
                itemPaddingY: 'normal' as const,
                customPaddingY: 10,
                itemPaddingX: 12,
                indentationSize: 'normal' as const,
                customIndentation: 20,
            },
            menuIcons: {
                showLevel0Icons: true,
                showLevel1Icons: false,
                showLevel2Icons: false,
                iconSize: 'normal' as const,
                iconOpacity: 0.8,
                iconStrokeWidth: 2,
                iconColorInactive: '#9CA3AF',
                iconColorActive: '#22D3EE',
                iconColorHover: '#1F2937',
            },
            menuBehavior: {
                collapseAnimation: false,
                hoverEffect: 'normal' as const,
                transitionSpeed: 'normal' as const,
            },
        },
    },
};

// Export singleton instance
export const layoutManager = LayoutManager.getInstance();

// Export helper function to get current config
export const getLayoutConfig = () => layoutManager.getConfig();

// Export helper function to update config
export const updateLayoutConfig = (config: LayoutConfig) => layoutManager.saveConfig(config);

// Export helper function to reset config
export const resetLayoutConfig = () => layoutManager.resetConfig();

