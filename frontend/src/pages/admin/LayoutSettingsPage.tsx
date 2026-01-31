import React, { useState, useEffect, useCallback } from "react";
import { toast } from "react-toastify";
import { layoutManager } from "../../config/layoutConfig";
import { Save, RotateCcw, LogOut, Search, ChevronRight, ChevronDown, Settings, Layout, Monitor, Type, Palette, Shield } from "lucide-react";
import { useNavigate } from "react-router-dom";
import { getSystemFonts } from "../../utils/systemFonts";
import { Button } from '@ui/Button';

// ==========================================
// 2. REPLICATED COMPONENTS (POS UX PATTERN)
// ==========================================

const Switch = ({ checked, onChange, disabled }: { checked: boolean, onChange: (val: boolean) => void, disabled?: boolean }) => (
    <label className={`relative inline-flex items-center cursor-pointer ${disabled ? 'opacity-50 cursor-not-allowed' : ''}`}>
        <input type="checkbox" checked={checked} onChange={(e) => !disabled && onChange(e.target.checked)} className="sr-only peer" disabled={disabled} />
        <div className="w-11 h-6 bg-slate-200 peer-focus:outline-none rounded-full peer peer-checked:bg-blue-600 after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:after:translate-x-full"></div>
    </label>
);

const SectionHeader = ({ prefix, title }: { prefix: string, title: string }) => (
    <div className="flex items-center mb-6 gap-3 bg-slate-100 p-4 border-l-4 border-slate-900 shadow-sm mt-8">
        <span className="text-xl font-black text-slate-400 tabular-nums w-8">{prefix}</span>
        <h2 className="text-lg font-black text-slate-900 tracking-tighter uppercase" style={{ fontWeight: 900 }}>{title}</h2>
    </div>
);

const CategoryHeader = ({ index, title, isExpanded, onToggle, count, icon: Icon }: { index: string, title: string, isExpanded: boolean, onToggle: () => void, count?: number, icon?: any }) => (
    <div
        className="flex items-center justify-between gap-4 py-2 px-3 bg-slate-50 hover:bg-slate-100 cursor-pointer transition-colors border-l border-slate-200 ml-4 group shadow-sm mb-1"
        onClick={onToggle}
    >
        <div className="flex items-center gap-3">
            <div className="text-slate-400 group-hover:text-blue-600">
                {isExpanded ? <ChevronDown size={14} className="w-4 h-4" /> : <ChevronRight size={14} className="w-4 h-4" />}
            </div>
            <span className="text-[11px] font-bold text-blue-600 w-10 tabular-nums">{index}</span>
            {Icon && <Icon size={14} className="text-slate-500" />}
            <h3 className="text-[11px] font-black text-slate-700 tracking-tight uppercase" style={{ fontWeight: 900 }}>{title}</h3>
        </div>
        {count !== undefined && (
            <div className="text-[9px] font-bold text-slate-400 bg-white px-2 py-0.5 border border-slate-100">
                {count} Settings
            </div>
        )}
    </div>
);

const SettingRow = ({ index, label, description, children, helpText }: { index: string, label: string, description?: string, children: React.ReactNode, helpText?: string }) => (
    <div className="py-3 px-4 border-b border-slate-100 last:border-0 hover:bg-blue-50/50 transition-colors group bg-white shadow-sm mb-1 border-l border-slate-200 ml-12">
        <div className="flex items-start gap-6">
            <span className="text-[8pt] font-normal text-blue-500 tabular-nums w-12 shrink-0 pt-1 tracking-tighter opacity-70">
                {index}
            </span>
            <div className="flex-1">
                <div className="flex justify-between items-center mb-1">
                    <div className="flex-1">
                        <h4 className="text-[14px] font-medium text-slate-800 leading-tight group-hover:text-blue-700 transition-colors">
                            {label}
                        </h4>
                    </div>
                    <div className="flex items-center gap-8 shrink-0">
                        <div className="min-w-[60px] flex justify-end">
                            {children}
                        </div>
                    </div>
                </div>
                <div>
                    <p className="text-[11px] text-slate-500 font-medium leading-relaxed max-w-3xl">
                        {description}
                        {helpText && (
                            <span className="ml-2 text-blue-600 font-bold text-[10px]">:: ℹ️ {helpText}</span>
                        )}
                    </p>
                </div>
            </div>
        </div>
    </div>
);

// This matches the structure expected by the UI and should map to LayoutConfig
interface LayoutSettings {
    // Sidebar Top Level
    sidebarWidth: number;
    sidebarCollapsed: boolean;
    showSubtitles: boolean;
    subtitleWrap: 'single-line' | 'wrap';
    menuItemSpacing: 'compact' | 'normal' | 'comfortable';
    showPhase2: boolean;
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

    // Sidebar Styling
    sidebarBackgroundColor: string;
    sidebarSurfaceColor: string;
    sidebarBorderColor: string;
    sidebarDividerColor: string;
    sidebarDividerStyle: "gradient" | "solid" | "none";

    // Sidebar Sub-objects
    sidebarRail: {
        width: number;
        backgroundColor: string;
        borderColor: string;
        activeIconBg: string;
        activeIconColor: string;
        inactiveIconColor: string;
        hoverIconBg: string;
        hoverIconColor: string;
    };
    sidebarPanel: {
        width: number;
        backgroundColor: string;
        borderColor: string;
        headerBackgroundColor: string;
        headerTextColor: string;
        activeItemBg: string;
        activeItemColor: string;
    };
    sidebarMenuText: {
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

    // Header Settings
    headerHeight: number;
    headerBgStyle: "solid" | "gradient";
    headerBgColor: string;
    headerGradientStart: string;
    headerGradientEnd: string;
    headerBorderColor: string;
    headerBrandColor: string;
    headerCompanyColor: string;
    headerIconColor: string;
    showUserMenu: boolean;
    showNotifications: boolean;
    showSearch: boolean;

    // Status Bar Settings
    statusBarHeight: number;
    showStatusBar: boolean;
    showConnectionStatus: boolean;

    // Modal Settings
    modalMaxWidth: string;
    modalBackgroundColor: string;
    modalBorderColor: string;
    modalBorderRadius: string;
    modalPadding: string;

    // Typography Settings
    typographyL1Size: string;
    typographyL1Weight: number;
    typographyL1Color: string;
    typographyL2Size: string;
    typographyL2Weight: number;
    typographyL2Color: string;
    typographyL3Size: string;
    typographyL3Weight: number;
    typographyL3Color: string;
    typographyL4Size: string;
    typographyL4Weight: number;
    typographyL4Color: string;
}

const LayoutSettingsPage: React.FC = () => {
    const navigate = useNavigate();
    const systemFonts = getSystemFonts();

    const [settings, setSettings] = useState<LayoutSettings | null>(null);
    const [isSaving, setIsSaving] = useState(false);
    const [expandedSections, setExpandedSections] = useState<Record<string, boolean>>({
        '1.1': true, '1.2': true, '1.3': true,
        '2.1': true, '2.2': true, '2.3': true, '2.4': true, '2.5': true, '2.6': true,
        '3.1': true, '3.2': true,
        '4.1': true, '4.2': true,
    });
    const [expandAll, setExpandAll] = useState(true);

    useEffect(() => {
        const config = layoutManager.getConfig();
        setSettings({
            sidebarWidth: config.sidebar.width,
            sidebarCollapsed: config.sidebar.defaultCollapsed,
            showSubtitles: config.sidebar.showSubtitles,
            subtitleWrap: config.sidebar.subtitleWrap,
            menuItemSpacing: config.sidebar.menuItemSpacing,
            showPhase2: config.sidebar.showPhase2,
            showRetail: config.sidebar.showRetail,
            showFinance: config.sidebar.showFinance,
            showCRM: config.sidebar.showCRM,
            showHRM: config.sidebar.showHRM,
            showTestConsole: config.sidebar.showTestConsole,
            testConsoleOptions: config.sidebar.testConsoleOptions,
            sidebarBackgroundColor: config.sidebar.backgroundColor,
            sidebarSurfaceColor: config.sidebar.surfaceColor,
            sidebarBorderColor: config.sidebar.borderColor,
            sidebarDividerColor: config.sidebar.dividerColor,
            sidebarDividerStyle: config.sidebar.dividerStyle,
            sidebarRail: { ...config.sidebar.rail },
            sidebarPanel: { ...config.sidebar.panel },
            sidebarMenuText: { ...config.sidebar.menuText },
            headerHeight: config.header.height,
            headerBgStyle: config.header.bgStyle || 'solid',
            headerBgColor: config.header.bgColor || config.header.backgroundColor,
            headerGradientStart: config.header.gradientStart || '',
            headerGradientEnd: config.header.gradientEnd || '',
            headerBorderColor: config.header.borderColor,
            headerBrandColor: config.header.brandColor || '',
            headerCompanyColor: config.header.companyColor || '',
            headerIconColor: config.header.iconColor || '',
            showUserMenu: config.header.showUserMenu,
            showNotifications: config.header.showNotifications,
            showSearch: config.header.showSearch,
            statusBarHeight: config.statusBar.height,
            showStatusBar: config.statusBar.show,
            showConnectionStatus: config.statusBar.showConnectionStatus,
            modalMaxWidth: config.modal.maxWidth,
            modalBackgroundColor: config.modal.backgroundColor,
            modalBorderColor: config.modal.borderColor,
            modalBorderRadius: config.modal.borderRadius,
            modalPadding: config.modal.padding,
            typographyL1Size: config.typography.l1.fontSize,
            typographyL1Weight: config.typography.l1.fontWeight,
            typographyL1Color: config.typography.l1.color,
            typographyL2Size: config.typography.l2.fontSize,
            typographyL2Weight: config.typography.l2.fontWeight,
            typographyL2Color: config.typography.l2.color,
            typographyL3Size: config.typography.l3.fontSize,
            typographyL3Weight: config.typography.l3.fontWeight,
            typographyL3Color: config.typography.l3.color,
            typographyL4Size: config.typography.l4.fontSize,
            typographyL4Weight: config.typography.l4.fontWeight,
            typographyL4Color: config.typography.l4.color,
        });
    }, []);

    const handleChange = useCallback((key: keyof LayoutSettings, value: any) => {
        setSettings(prev => prev ? ({ ...prev, [key]: value }) : null);
    }, []);

    const toggleSection = (key: string) => {
        setExpandedSections(prev => ({ ...prev, [key]: !prev[key] }));
    };

    const handleExpandCollapseAll = (shouldExpand: boolean) => {
        setExpandAll(shouldExpand);
        const updated: Record<string, boolean> = {};
        Object.keys(expandedSections).forEach(key => updated[key] = shouldExpand);
        setExpandedSections(updated);
    };

    const handleSave = useCallback(() => {
        if (!settings) return;
        setIsSaving(true);
        try {
            const currentConfig = layoutManager.getConfig();
            const newConfig = {
                ...currentConfig,
                sidebar: {
                    ...currentConfig.sidebar,
                    width: settings.sidebarWidth,
                    defaultCollapsed: settings.sidebarCollapsed,
                    showSubtitles: settings.showSubtitles,
                    subtitleWrap: settings.subtitleWrap,
                    menuItemSpacing: settings.menuItemSpacing,
                    showPhase2: settings.showPhase2,
                    showRetail: settings.showRetail,
                    showFinance: settings.showFinance,
                    showCRM: settings.showCRM,
                    showHRM: settings.showHRM,
                    showTestConsole: settings.showTestConsole,
                    testConsoleOptions: settings.testConsoleOptions,
                    backgroundColor: settings.sidebarBackgroundColor,
                    surfaceColor: settings.sidebarSurfaceColor,
                    borderColor: settings.sidebarBorderColor,
                    dividerColor: settings.sidebarDividerColor,
                    dividerStyle: settings.sidebarDividerStyle,
                    rail: settings.sidebarRail,
                    panel: settings.sidebarPanel,
                    menuText: settings.sidebarMenuText,
                },
                header: {
                    ...currentConfig.header,
                    height: settings.headerHeight,
                    bgStyle: settings.headerBgStyle,
                    bgColor: settings.headerBgColor,
                    gradientStart: settings.headerGradientStart,
                    gradientEnd: settings.headerGradientEnd,
                    borderColor: settings.headerBorderColor,
                    brandColor: settings.headerBrandColor,
                    companyColor: settings.headerCompanyColor,
                    iconColor: settings.headerIconColor,
                    showUserMenu: settings.showUserMenu,
                    showNotifications: settings.showNotifications,
                    showSearch: settings.showSearch,
                },
                statusBar: {
                    ...currentConfig.statusBar,
                    height: settings.statusBarHeight,
                    show: settings.showStatusBar,
                    showConnectionStatus: settings.showConnectionStatus,
                },
                modal: {
                    ...currentConfig.modal,
                    maxWidth: settings.modalMaxWidth,
                    backgroundColor: settings.modalBackgroundColor,
                    borderColor: settings.modalBorderColor,
                    borderRadius: settings.modalBorderRadius,
                    padding: settings.modalPadding,
                },
                typography: {
                    ...currentConfig.typography,
                    l1: { ...currentConfig.typography.l1, fontSize: settings.typographyL1Size, fontWeight: settings.typographyL1Weight, color: settings.typographyL1Color },
                    l2: { ...currentConfig.typography.l2, fontSize: settings.typographyL2Size, fontWeight: settings.typographyL2Weight, color: settings.typographyL2Color },
                    l3: { ...currentConfig.typography.l3, fontSize: settings.typographyL3Size, fontWeight: settings.typographyL3Weight, color: settings.typographyL3Color },
                    l4: { ...currentConfig.typography.l4, fontSize: settings.typographyL4Size, fontWeight: settings.typographyL4Weight, color: settings.typographyL4Color },
                },
            };

            layoutManager.saveConfig(newConfig as any);
            toast.success('Settings saved successfully');
            setTimeout(() => window.location.reload(), 1000);
        } catch (error) {
            toast.error('Failed to save settings');
        } finally {
            setIsSaving(false);
        }
    }, [settings]);

    const handleReset = useCallback(() => {
        if (window.confirm('Reset all settings to default?')) {
            layoutManager.resetConfig();
            window.location.reload();
        }
    }, []);

    if (!settings) return null;

    return (
        <div className="flex flex-col bg-slate-50 overflow-hidden h-full w-full">
            {/* Toolbar */}
            <div className="flex-none z-50 px-4 py-1 bg-[#f3f2f1] border-b border-[#d1d1d1] h-[42px] select-none shadow-sm flex items-center justify-between">
                <div className="flex items-center gap-1">
                    <button onClick={handleSave} disabled={isSaving} className="flex items-center gap-2 px-3 py-1.5 hover:bg-white rounded border border-transparent hover:border-[#ccc] transition-all group">
                        <Save size={14} className="text-emerald-600" />
                        <span className="text-[11px] font-medium text-[#444] group-hover:text-black">Save (F8)</span>
                    </button>
                    <button onClick={handleReset} className="flex items-center gap-2 px-3 py-1.5 hover:bg-white rounded border border-transparent hover:border-[#ccc] transition-all group">
                        <RotateCcw size={14} className="text-amber-500" />
                        <span className="text-[11px] font-medium text-[#444] group-hover:text-black">Clear</span>
                    </button>
                    <div className="w-px h-4 bg-gray-300 mx-1"></div>
                    <button onClick={() => navigate('/admin')} className="flex items-center gap-2 px-3 py-1.5 hover:bg-white rounded border border-transparent hover:border-[#ccc] transition-all group">
                        <LogOut size={14} className="text-red-500" />
                        <span className="text-[11px] font-medium text-[#444] group-hover:text-black">Exit (Esc)</span>
                    </button>
                </div>
                <div className="text-xs font-semibold text-gray-500 tracking-tight italic">
                    Astra Layout & Appearance Configuration
                </div>
            </div>

            {/* Header Area */}
            <div className="flex-none bg-white">
                <div className="max-w-6xl mx-auto px-6">
                    <div className="pt-6 pb-4 flex justify-between items-center border-b border-slate-100">
                        <div>
                            <h1 className="text-2xl font-black text-slate-900 tracking-tight leading-none mb-1">Layout Settings</h1>
                            <p className="text-[11px] text-slate-500 font-medium">Configure global UI standards, sidebar behaviors and color schemes</p>
                        </div>
                        <div className="flex items-center gap-2">
                            <Button variant={expandAll ? 'primary' : 'ghost'} size="sm" onClick={() => handleExpandCollapseAll(true)} className="h-8 rounded-none text-[10px] font-bold uppercase tracking-widest px-4 shadow-sm">Expand All</Button>
                            <Button variant={!expandAll ? 'primary' : 'ghost'} size="sm" onClick={() => handleExpandCollapseAll(false)} className="h-8 rounded-none text-[10px] font-bold uppercase tracking-widest px-4 shadow-sm">Collapse All</Button>
                        </div>
                    </div>
                </div>
            </div>

            {/* Content Body */}
            <div className="flex-1 overflow-y-auto custom-scrollbar bg-slate-50/30">
                <div className="max-w-6xl mx-auto p-6 pt-2 pb-24">
                    {/* Section 1: Application Header */}
                    <SectionHeader prefix="1" title="Application Header" />
                    <CategoryHeader index="1.1" title="Header Branding" isExpanded={expandedSections['1.1']} onToggle={() => toggleSection('1.1')} count={3} icon={Shield} />
                    {expandedSections['1.1'] && (
                        <div className="space-y-px">
                            <SettingRow index="1.1.1" label='"Olivine" Text Color' description="Brand primary identity color">
                                <div className="flex space-x-2">
                                    <input type="color" value={settings.headerBrandColor} onChange={(e) => handleChange('headerBrandColor', e.target.value)} className="w-8 h-8 rounded border cursor-pointer" />
                                    <input type="text" value={settings.headerBrandColor} onChange={(e) => handleChange('headerBrandColor', e.target.value)} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                </div>
                            </SettingRow>
                            <SettingRow index="1.1.2" label="Company Name Color" description="Secondary identity text color">
                                <div className="flex space-x-2">
                                    <input type="color" value={settings.headerCompanyColor} onChange={(e) => handleChange('headerCompanyColor', e.target.value)} className="w-8 h-8 rounded border cursor-pointer" />
                                    <input type="text" value={settings.headerCompanyColor} onChange={(e) => handleChange('headerCompanyColor', e.target.value)} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                </div>
                            </SettingRow>
                            <SettingRow index="1.1.3" label="Icon Colors" description="Colors for search, notifications, and profile icons">
                                <div className="flex space-x-2">
                                    <input type="color" value={settings.headerIconColor} onChange={(e) => handleChange('headerIconColor', e.target.value)} className="w-8 h-8 rounded border cursor-pointer" />
                                    <input type="text" value={settings.headerIconColor} onChange={(e) => handleChange('headerIconColor', e.target.value)} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                </div>
                            </SettingRow>
                        </div>
                    )}

                    <CategoryHeader index="1.2" title="Header Surface & Geometry" isExpanded={expandedSections['1.2']} onToggle={() => toggleSection('1.2')} count={3} icon={Palette} />
                    {expandedSections['1.2'] && (
                        <div className="space-y-px">
                            <SettingRow index="1.2.1" label="Background Style" description="Toggle between solid and gradient backgrounds">
                                <select value={settings.headerBgStyle} onChange={(e) => handleChange('headerBgStyle', e.target.value as any)} className="h-8 min-w-[140px] border border-slate-200 rounded px-2 text-[12px]">
                                    <option value="solid">Solid Color</option>
                                    <option value="gradient">Gradient</option>
                                </select>
                            </SettingRow>
                            <SettingRow index="1.2.2" label="Surface Colors" description="Configure background or gradient stops">
                                {settings.headerBgStyle === 'solid' ? (
                                    <div className="flex space-x-2">
                                        <input type="color" value={settings.headerBgColor} onChange={(e) => handleChange('headerBgColor', e.target.value)} className="w-8 h-8 rounded border cursor-pointer" />
                                        <input type="text" value={settings.headerBgColor} onChange={(e) => handleChange('headerBgColor', e.target.value)} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                    </div>
                                ) : (
                                    <div className="flex flex-col gap-2">
                                        <div className="flex space-x-2 items-center"><span className="text-[9px] font-bold w-12 text-slate-400">START:</span><input type="color" value={settings.headerGradientStart} onChange={(e) => handleChange('headerGradientStart', e.target.value)} className="w-8 h-8 rounded border cursor-pointer" /><input type="text" value={settings.headerGradientStart} onChange={(e) => handleChange('headerGradientStart', e.target.value)} className="w-24 px-2 py-1 border rounded text-xs font-mono" /></div>
                                        <div className="flex space-x-2 items-center"><span className="text-[9px] font-bold w-12 text-slate-400">END:</span><input type="color" value={settings.headerGradientEnd} onChange={(e) => handleChange('headerGradientEnd', e.target.value)} className="w-8 h-8 rounded border cursor-pointer" /><input type="text" value={settings.headerGradientEnd} onChange={(e) => handleChange('headerGradientEnd', e.target.value)} className="w-24 px-2 py-1 border rounded text-xs font-mono" /></div>
                                    </div>
                                )}
                            </SettingRow>
                            <SettingRow index="1.2.3" label="Height & Border" description="Control vertical spacing and divider color">
                                <div className="flex gap-4">
                                    <div className="flex items-center gap-2"><span className="text-[10px] font-bold text-slate-400">PX:</span><input type="number" value={settings.headerHeight} onChange={(e) => handleChange('headerHeight', parseInt(e.target.value))} className="w-16 h-8 border border-slate-200 rounded px-2 text-[12px] text-center" /></div>
                                    <div className="flex items-center gap-2"><span className="text-[10px] font-bold text-slate-400">BORDER:</span><input type="text" value={settings.headerBorderColor} onChange={(e) => handleChange('headerBorderColor', e.target.value)} className="w-32 h-8 border border-slate-200 rounded px-2 text-[11px] font-mono" /></div>
                                </div>
                            </SettingRow>
                        </div>
                    )}

                    <CategoryHeader index="1.3" title="Header Components" isExpanded={expandedSections['1.3']} onToggle={() => toggleSection('1.3')} count={3} icon={Monitor} />
                    {expandedSections['1.3'] && (
                        <div className="space-y-px">
                            <SettingRow index="1.3.1" label="User Menu" description="Toggle visibility of the user profile dropdown">
                                <Switch checked={settings.showUserMenu} onChange={(v) => handleChange('showUserMenu', v)} />
                            </SettingRow>
                            <SettingRow index="1.3.2" label="Notification Center" description="Toggle visibility of the notifications bell icon">
                                <Switch checked={settings.showNotifications} onChange={(v) => handleChange('showNotifications', v)} />
                            </SettingRow>
                            <SettingRow index="1.3.3" label="Search Bar" description="Toggle visibility of the global search input">
                                <Switch checked={settings.showSearch} onChange={(v) => handleChange('showSearch', v)} />
                            </SettingRow>
                        </div>
                    )}

                    {/* Section 2: Sidebar */}
                    <SectionHeader prefix="2" title="Sidebar" />
                    <CategoryHeader index="2.1" title="Left Rail (L1)" isExpanded={expandedSections['2.1']} onToggle={() => toggleSection('2.1')} count={4} icon={Layout} />
                    {expandedSections['2.1'] && (
                        <div className="space-y-px">
                            <SettingRow index="2.1.1" label="Rail Width" description="Width of the leftmost navigation rail">
                                <div className="flex items-center gap-2"><span className="text-[10px] font-bold text-slate-400">PX:</span><input type="number" value={settings.sidebarRail.width} onChange={(e) => handleChange('sidebarRail', { ...settings.sidebarRail, width: parseInt(e.target.value) })} className="w-16 h-8 border border-slate-200 rounded px-2 text-[12px] text-center" /></div>
                            </SettingRow>
                            <SettingRow index="2.1.2" label="Background Color" description="Main background for the L1 rail">
                                <div className="flex space-x-2">
                                    <input type="color" value={settings.sidebarRail.backgroundColor} onChange={(e) => handleChange('sidebarRail', { ...settings.sidebarRail, backgroundColor: e.target.value })} className="w-8 h-8 rounded border cursor-pointer" />
                                    <input type="text" value={settings.sidebarRail.backgroundColor} onChange={(e) => handleChange('sidebarRail', { ...settings.sidebarRail, backgroundColor: e.target.value })} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                </div>
                            </SettingRow>
                            <SettingRow index="2.1.3" label="Active Icon Styling" description="Background and color for selected module">
                                <div className="flex gap-4">
                                    <div className="flex items-center gap-2"><span className="text-[9px] font-bold text-slate-400">BG:</span><input type="color" value={settings.sidebarRail.activeIconBg} onChange={(e) => handleChange('sidebarRail', { ...settings.sidebarRail, activeIconBg: e.target.value })} className="w-6 h-6 rounded border cursor-pointer" /></div>
                                    <div className="flex items-center gap-2"><span className="text-[9px] font-bold text-slate-400">ICON:</span><input type="color" value={settings.sidebarRail.activeIconColor} onChange={(e) => handleChange('sidebarRail', { ...settings.sidebarRail, activeIconColor: e.target.value })} className="w-6 h-6 rounded border cursor-pointer" /></div>
                                </div>
                            </SettingRow>
                            <SettingRow index="2.1.4" label="Default Collapsed" description="Start with the sidebar in collapsed (rail-only) mode">
                                <Switch checked={settings.sidebarCollapsed} onChange={(v) => handleChange('sidebarCollapsed', v)} />
                            </SettingRow>
                        </div>
                    )}

                    <CategoryHeader index="2.2" title="Right Panel (L2/L3)" isExpanded={expandedSections['2.2']} onToggle={() => toggleSection('2.2')} count={7} icon={Layout} />
                    {expandedSections['2.2'] && (
                        <div className="space-y-px">
                            <SettingRow index="2.2.1" label="Panel Width" description="Width of the submenu panel">
                                <div className="flex items-center gap-2"><span className="text-[10px] font-bold text-slate-400">PX:</span><input type="number" value={settings.sidebarPanel.width} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, width: parseInt(e.target.value) })} className="w-16 h-8 border border-slate-200 rounded px-2 text-[12px] text-center" /></div>
                            </SettingRow>
                            <SettingRow index="2.2.2" label="Background Color" description="Main background for L2/L3 panels">
                                <div className="flex space-x-2">
                                    <input type="color" value={settings.sidebarPanel.backgroundColor} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, backgroundColor: e.target.value })} className="w-8 h-8 rounded border cursor-pointer" />
                                    <input type="text" value={settings.sidebarPanel.backgroundColor} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, backgroundColor: e.target.value })} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                </div>
                            </SettingRow>
                            <SettingRow index="2.2.3" label="Border Color" description="Border color for panel edges">
                                <div className="flex space-x-2">
                                    <input type="color" value={settings.sidebarPanel.borderColor} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, borderColor: e.target.value })} className="w-8 h-8 rounded border cursor-pointer" />
                                    <input type="text" value={settings.sidebarPanel.borderColor} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, borderColor: e.target.value })} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                </div>
                            </SettingRow>
                            <SettingRow index="2.2.4" label="Header Background" description="Background color for panel headers">
                                <div className="flex space-x-2">
                                    <input type="color" value={settings.sidebarPanel.headerBackgroundColor} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, headerBackgroundColor: e.target.value })} className="w-8 h-8 rounded border cursor-pointer" />
                                    <input type="text" value={settings.sidebarPanel.headerBackgroundColor} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, headerBackgroundColor: e.target.value })} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                </div>
                            </SettingRow>
                            <SettingRow index="2.2.5" label="Header Text Color" description="Text color for panel headers">
                                <div className="flex space-x-2">
                                    <input type="color" value={settings.sidebarPanel.headerTextColor} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, headerTextColor: e.target.value })} className="w-8 h-8 rounded border cursor-pointer" />
                                    <input type="text" value={settings.sidebarPanel.headerTextColor} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, headerTextColor: e.target.value })} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                </div>
                            </SettingRow>
                            <SettingRow index="2.2.6" label="Active Item Background" description="Background color for selected menu items">
                                <div className="flex space-x-2">
                                    <input type="color" value={settings.sidebarPanel.activeItemBg} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, activeItemBg: e.target.value })} className="w-8 h-8 rounded border cursor-pointer" />
                                    <input type="text" value={settings.sidebarPanel.activeItemBg} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, activeItemBg: e.target.value })} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                </div>
                            </SettingRow>
                            <SettingRow index="2.2.7" label="Active Item Color" description="Text color for selected menu items">
                                <div className="flex space-x-2">
                                    <input type="color" value={settings.sidebarPanel.activeItemColor} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, activeItemColor: e.target.value })} className="w-8 h-8 rounded border cursor-pointer" />
                                    <input type="text" value={settings.sidebarPanel.activeItemColor} onChange={(e) => handleChange('sidebarPanel', { ...settings.sidebarPanel, activeItemColor: e.target.value })} className="w-24 px-2 py-1 border rounded text-xs font-mono" />
                                </div>
                            </SettingRow>
                        </div>
                    )}

                    <CategoryHeader index="2.3" title="Menu Typography" isExpanded={expandedSections['2.3']} onToggle={() => toggleSection('2.3')} count={4} icon={Type} />
                    {expandedSections['2.3'] && (
                        <div className="space-y-px">
                            <SettingRow index="2.3.1" label="Level 0 (Module Headers)" description="Typography for top-level module names">
                                <div className="flex gap-4 items-center">
                                    <input type="text" value={settings.sidebarMenuText.level0FontSize} onChange={(e) => handleChange('sidebarMenuText', { ...settings.sidebarMenuText, level0FontSize: e.target.value })} className="w-16 h-8 border border-slate-200 rounded px-2 text-[11px] font-mono" />
                                    <select value={settings.sidebarMenuText.level0FontWeight} onChange={(e) => handleChange('sidebarMenuText', { ...settings.sidebarMenuText, level0FontWeight: parseInt(e.target.value) as any })} className="h-8 border border-slate-200 rounded px-2 text-[11px]">
                                        <option value="400">Normal</option><option value="600">Semibold</option><option value="700">Bold</option>
                                    </select>
                                </div>
                            </SettingRow>
                            <SettingRow index="2.3.2" label="Menu Subtitles" description="Show descriptive text under main menu items">
                                <Switch checked={settings.showSubtitles} onChange={(v) => handleChange('showSubtitles', v)} />
                            </SettingRow>
                            <SettingRow index="2.3.3" label="Subtitle Wrapping" description="Control how long subtitles are displayed">
                                <select value={settings.subtitleWrap} onChange={(e) => handleChange('subtitleWrap', e.target.value as any)} className="h-8 border border-slate-200 rounded px-2 text-[11px]">
                                    <option value="single-line">Single Line (Truncated)</option>
                                    <option value="wrap">Multiple Lines (Full Text)</option>
                                </select>
                            </SettingRow>
                            <SettingRow index="2.3.4" label="Menu Spacing" description="Vertical density of the navigation items">
                                <select value={settings.menuItemSpacing} onChange={(e) => handleChange('menuItemSpacing', e.target.value as any)} className="h-8 border border-slate-200 rounded px-2 text-[11px]">
                                    <option value="compact">Compact (Tight)</option>
                                    <option value="normal">Normal (Standard)</option>
                                    <option value="comfortable">Comfortable (Relaxed)</option>
                                </select>
                            </SettingRow>
                        </div>
                    )}

                    <CategoryHeader index="2.4" title="Feature Toggles" isExpanded={expandedSections['2.4']} onToggle={() => toggleSection('2.4')} count={1} icon={Settings} />
                    {expandedSections['2.4'] && (
                        <div className="space-y-px">
                            <SettingRow index="2.4.1" label="Phase 2 Features" description="Enable access to experimental Phase 2 menu modules">
                                <Switch checked={settings.showPhase2} onChange={(v) => handleChange('showPhase2', v)} />
                            </SettingRow>
                        </div>
                    )}

                    <CategoryHeader index="2.5" title="Module Visibility" isExpanded={expandedSections['2.5']} onToggle={() => toggleSection('2.5')} count={5} icon={Monitor} />
                    {expandedSections['2.5'] && (
                        <div className="space-y-px">
                            <SettingRow index="2.5.1" label="Retail Operations" description="Main retail, stores and inventory modules">
                                <Switch checked={settings.showRetail} onChange={(v) => handleChange('showRetail', v)} />
                            </SettingRow>
                            <SettingRow index="2.5.2" label="Financial Management" description="Accounting, billing and finance modules">
                                <Switch checked={settings.showFinance} onChange={(v) => handleChange('showFinance', v)} />
                            </SettingRow>
                            <SettingRow index="2.5.3" label="CRM" description="Customer Relationship Management">
                                <Switch checked={settings.showCRM} onChange={(v) => handleChange('showCRM', v)} />
                            </SettingRow>
                            <SettingRow index="2.5.4" label="Human Resources" description="Employee directory and HR management">
                                <Switch checked={settings.showHRM} onChange={(v) => handleChange('showHRM', v)} />
                            </SettingRow>
                            <SettingRow index="2.5.5" label="Test Console" description="Developer toolkit and system test explorer">
                                <Switch checked={settings.showTestConsole} onChange={(v) => handleChange('showTestConsole', v)} />
                            </SettingRow>
                        </div>
                    )}

                    <CategoryHeader index="2.6" title="Test Console Settings" isExpanded={expandedSections['2.6']} onToggle={() => toggleSection('2.6')} count={5} icon={Shield} />
                    {expandedSections['2.6'] && (
                        <div className="space-y-px">
                            <SettingRow index="2.6.1" label="Retail in TC" description="Include Retail modules in Test Console Explorer">
                                <Switch checked={settings.testConsoleOptions.showRetail} onChange={(v) => handleChange('testConsoleOptions', { ...settings.testConsoleOptions, showRetail: v })} />
                            </SettingRow>
                            <SettingRow index="2.6.2" label="FMS in TC" description="Include Finance modules in Test Console Explorer">
                                <Switch checked={settings.testConsoleOptions.showFinance} onChange={(v) => handleChange('testConsoleOptions', { ...settings.testConsoleOptions, showFinance: v })} />
                            </SettingRow>
                            <SettingRow index="2.6.3" label="CRM in TC" description="Include CRM modules in Test Console Explorer">
                                <Switch checked={settings.testConsoleOptions.showCRM} onChange={(v) => handleChange('testConsoleOptions', { ...settings.testConsoleOptions, showCRM: v })} />
                            </SettingRow>
                            <SettingRow index="2.6.4" label="HRM in TC" description="Include HRM modules in Test Console Explorer">
                                <Switch checked={settings.testConsoleOptions.showHRM} onChange={(v) => handleChange('testConsoleOptions', { ...settings.testConsoleOptions, showHRM: v })} />
                            </SettingRow>
                            <SettingRow index="2.6.5" label="Meet in TC" description="Include Meet modules in Test Console Explorer">
                                <Switch checked={settings.testConsoleOptions.showMeet} onChange={(v) => handleChange('testConsoleOptions', { ...settings.testConsoleOptions, showMeet: v })} />
                            </SettingRow>
                        </div>
                    )}

                    {/* Section 3: Status Bar */}
                    <SectionHeader prefix="3" title="Status Bar" />
                    <CategoryHeader index="3.1" title="Status Bar Geometry" isExpanded={expandedSections['3.1']} onToggle={() => toggleSection('3.1')} count={1} icon={Layout} />
                    {expandedSections['3.1'] && (
                        <div className="space-y-px">
                            <SettingRow index="3.1.1" label="Height" description="Vertical height of the system status bar">
                                <div className="flex items-center gap-2"><span className="text-[10px] font-bold text-slate-400">PX:</span><input type="number" value={settings.statusBarHeight} onChange={(e) => handleChange('statusBarHeight', parseInt(e.target.value))} className="w-16 h-8 border border-slate-200 rounded px-2 text-[12px] text-center" /></div>
                            </SettingRow>
                        </div>
                    )}
                    <CategoryHeader index="3.2" title="Status Bar Components" isExpanded={expandedSections['3.2']} onToggle={() => toggleSection('3.2')} count={2} icon={Monitor} />
                    {expandedSections['3.2'] && (
                        <div className="space-y-px">
                            <SettingRow index="3.2.1" label="Visible" description="Overall visibility of the status bar"><Switch checked={settings.showStatusBar} onChange={(v) => handleChange('showStatusBar', v)} /></SettingRow>
                            <SettingRow index="3.2.2" label="Connection Status" description="Show online/offline indicator"><Switch checked={settings.showConnectionStatus} onChange={(v) => handleChange('showConnectionStatus', v)} /></SettingRow>
                        </div>
                    )}

                    {/* Section 4: UI Standards */}
                    <SectionHeader prefix="4" title="UI Standards" />
                    <CategoryHeader index="4.1" title="Modal Standards" isExpanded={expandedSections['4.1']} onToggle={() => toggleSection('4.1')} count={3} icon={Shield} />
                    {expandedSections['4.1'] && (
                        <div className="space-y-px">
                            <SettingRow index="4.1.1" label="Max Width" description="Maximum width for standard modals"><input type="text" value={settings.modalMaxWidth} onChange={(e) => handleChange('modalMaxWidth', e.target.value)} className="w-32 h-8 border border-slate-200 rounded px-2 text-[11px] font-mono" /></SettingRow>
                        </div>
                    )}
                    <CategoryHeader index="4.2" title="Typography Standards" isExpanded={expandedSections['4.2']} onToggle={() => toggleSection('4.2')} count={4} icon={Type} />
                    {expandedSections['4.2'] && (
                        <div className="space-y-px">
                            <SettingRow index="4.2.1" label="L1 - Page Title" description="Base size headers"><input type="text" value={settings.typographyL1Size} onChange={(e) => handleChange('typographyL1Size', e.target.value)} className="w-24 h-8 border border-slate-200 rounded px-2 text-[11px] font-mono" /></SettingRow>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default LayoutSettingsPage;
