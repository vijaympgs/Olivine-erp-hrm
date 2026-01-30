'use client';

import React, { useState, useEffect } from 'react';
import {
    Box,
    Typography,
    Stack,
    Paper,
    Divider,
    CircularProgress,
    IconButton,
    Tooltip,
    Tabs,
    Tab,
    List,
    ListSubheader,
    ListItemButton,
    ListItemText,
} from '@mui/material';
import { styled, alpha, useTheme } from '@mui/material/styles';
import RefreshIcon from '@mui/icons-material/Refresh';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import WarningAmberRoundedIcon from '@mui/icons-material/WarningAmberRounded';
import { menuConfig } from '../../../app/menuConfig';
import { layoutManager } from '../../../config/layoutConfig';

// Component registry maps routes to component files
const componentRegistry: Record<string, string> = {
    '/': '../Dashboard/DashboardPage.tsx',
    '/dashboard': '../Dashboard/DashboardPage.tsx',
    '/retail/dashboard': '../retail/RetailDashboardPage.tsx',
    '/admin/layout-settings': '../admin/LayoutSettingsPage.tsx',
    '/admin/file-search': '../admin/FileSearchExplorerPage.tsx',
    '/system-tools/visual-extractor': '../system_tools/visual_extractor/VisualExtractorPage.tsx',
    '/system-tools/web-console': '../system_tools/web_console/WebConsolePage.tsx',
    '/system-tools/html-preview': '../system_tools/html_preview/HtmlPreviewPage.tsx',
    '/test-console': '../TestConsolePage.tsx',
    '/hr/dashboard': '../hr/DashboardPage.tsx',
    '/hr/employees/records': '../hr/EmployeeRecordsPage.tsx',
    '/hr/employees/org-chart': '../hr/OrganizationalChartPage.tsx',
    '/hr/employees/profile': '../hr/ProfileViewPage.tsx',
    '/hr/employees/self-service': '../hr/EmployeeSelfServicePage.tsx',
    '/hr/employees/lifecycle': '../hr/EmployeeLifecyclePage.tsx',
};

// Function to flatten menu items and extract those with paths
const extractMenuItems = (items: any[], parentId = '', topLevelParentId = ''): any[] => {
    let result: any[] = [];
    items.forEach(item => {
        const currentTopLevelParent = topLevelParentId || item.id;
        if (item.path) {
            result.push({
                id: item.id,
                text: item.label,
                path: item.path,
                parentId,
                topLevelParentId: currentTopLevelParent
            });
        }
        if (item.children) {
            result = result.concat(extractMenuItems(item.children, item.id, currentTopLevelParent));
        }
    });
    return result;
};

// Function to group items by category
const groupItemsByCategory = (items: any[], layoutConfig: any) => {
    const categories: any[] = [];
    
    // Always include Platform category (System Administration and System Tools)
    const platformItems = items.filter(item => 
        item.parentId === 'administration' || item.parentId === 'system-tools'
    ).map(item => ({
        text: item.text,
        path: item.path
    }));
    
    if (platformItems.length > 0) {
        categories.push({
            id: 'platform',
            title: 'Platform',
            items: platformItems
        });
    }
    
    // Include HRM category if enabled
    if (layoutConfig.sidebar.showHRM) {
        const hrmItems = items.filter(item => 
            item.topLevelParentId === 'hrm' && item.path
        ).map(item => ({
            text: item.text,
            path: item.path
        }));
        
        if (hrmItems.length > 0) {
            categories.push({
                id: 'hrm',
                title: 'Human Resources',
                items: hrmItems
            });
        }
    }
    
    // Include Retail category if enabled
    if (layoutConfig.sidebar.showRetail) {
        const retailItems = items.filter(item => 
            item.path.includes('/retail/') || item.path === '/test-console'
        ).map(item => ({
            text: item.text,
            path: item.path
        }));
        
        if (retailItems.length > 0) {
            categories.push({
                id: 'retail',
                title: 'Retail',
                items: retailItems
            });
        }
    }
    
    // Include Finance category if enabled
    if (layoutConfig.sidebar.showFinance) {
        const financeItems = items.filter(item => 
            item.path.includes('/finance/')
        ).map(item => ({
            text: item.text,
            path: item.path
        }));
        
        if (financeItems.length > 0) {
            categories.push({
                id: 'finance',
                title: 'Finance',
                items: financeItems
            });
        }
    }
    
    // Include CRM category if enabled
    if (layoutConfig.sidebar.showCRM) {
        const crmItems = items.filter(item => 
            item.path.includes('/crm/')
        ).map(item => ({
            text: item.text,
            path: item.path
        }));
        
        if (crmItems.length > 0) {
            categories.push({
                id: 'crm',
                title: 'CRM',
                items: crmItems
            });
        }
    }
    
    return categories;
};

const SidebarContainer = styled(Paper)(({ theme }) => ({
    width: 280,
    flexShrink: 0,
    borderRadius: theme.shape.borderRadius,
    borderColor: alpha(theme.palette.divider, 0.7),
    padding: theme.spacing(1.5),
    display: 'flex',
    flexDirection: 'column',
    gap: theme.spacing(1.5),
}));

const Panel = styled(Paper)(({ theme }) => ({
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    borderRadius: theme.shape.borderRadius,
    borderColor: alpha(theme.palette.divider, 0.7),
    minHeight: 480,
}));

const CodeBlock = styled('pre')(({ theme }) => ({
    flex: 1,
    margin: 0,
    padding: theme.spacing(2),
    overflow: 'auto',
    backgroundColor: '#0b1120',
    color: '#cbd5f5',
    fontFamily: '"Fira Code", Menlo, Consolas, monospace',
    fontSize: 13,
    borderRadius: `0 0 ${theme.shape.borderRadius}px ${theme.shape.borderRadius}px`,
}));

const HtmlPreviewPage: React.FC = () => {
    const theme = useTheme();
    const [layoutConfig, setLayoutConfig] = useState<any>(null);
    const [screenCategories, setScreenCategories] = useState<any[]>([]);
    const [selectedPath, setSelectedPath] = useState<string | null>(null);
    const [filePath, setFilePath] = useState<string | null>(null);
    const [code, setCode] = useState('');
    const [loadingCode, setLoadingCode] = useState(false);
    const [loadError, setLoadError] = useState<string | null>(null);
    const [reloadToken, setReloadToken] = useState(0);
    const [activeTab, setActiveTab] = useState('source');

    // Initialize and set up layout config listener
    useEffect(() => {
        const config = layoutManager.getConfig();
        setLayoutConfig(config);
        
        // Extract all menu items with paths
        const allMenuItems = extractMenuItems(menuConfig);
        
        // Group items by category based on layout settings
        const categories = groupItemsByCategory(allMenuItems, config);
        setScreenCategories(categories);
        
        // Set initial selected path
        if (categories.length > 0 && categories[0].items.length > 0) {
            setSelectedPath(categories[0].items[0].path);
        }
        
        // Listen for layout config updates
        const handleLayoutUpdate = () => {
            const newConfig = layoutManager.getConfig();
            setLayoutConfig(newConfig);
            const newCategories = groupItemsByCategory(allMenuItems, newConfig);
            setScreenCategories(newCategories);
        };
        
        window.addEventListener('layout-config-update', handleLayoutUpdate);
        
        return () => {
            window.removeEventListener('layout-config-update', handleLayoutUpdate);
        };
    }, []);

    // Load code when selected path changes
    useEffect(() => {
        if (!selectedPath) {
            setFilePath(null);
            setCode('');
            setLoadError(null);
            return;
        }
        const targetFile = componentRegistry[selectedPath];
        setFilePath(targetFile || null);

        // Simulate loading code (in real implementation, would use dynamic import)
        if (targetFile) {
            setLoadingCode(true);
            setLoadError(null);

            // Simulated code loading
            setTimeout(() => {
                setCode(`// Component: ${targetFile}
// Route: ${selectedPath}
// 
// This is a preview placeholder.
// In a full implementation, the actual component source would be loaded here.

import React from 'react';

const Component = () => {
  return (
    <div>
      <h1>Screen Preview</h1>
      <p>Route: ${selectedPath}</p>
      <p>File: ${targetFile}</p>
    </div>
  );
};

export default Component;`);
                setLoadingCode(false);
            }, 500);
        } else {
            setCode('// Source unavailable for this screen.');
            setLoadError('No preview available for this screen.');
        }
    }, [selectedPath, reloadToken]);

    const handleRefresh = () => {
        if (!filePath) return;
        setReloadToken((token) => token + 1);
    };

    const handleCopyCode = () => {
        if (!code) return;
        navigator.clipboard.writeText(code).catch((error) => {
            console.error('HtmlPreviewPage: copy failed', error);
        });
    };

    return (
        <Box
            sx={{
                flex: 1,
                display: 'flex',
                flexDirection: 'column',
                minHeight: '100vh',
                backgroundColor: theme.palette.background.default,
                px: { xs: 1.5, md: 3 },
                py: { xs: 2, md: 3 },
            }}
        >
            <Stack spacing={0.5} sx={{ mb: 2.5 }}>
                <Typography variant="h5" sx={{ fontWeight: 600 }}>
                    HTML Preview Tool
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Explore wireframes by module, inspect their source code, and review the live markup render.
                    Ideal for design reviews and QA runs.
                </Typography>
            </Stack>

            <Stack
                direction={{ xs: 'column', lg: 'row' }}
                spacing={2.5}
                alignItems="stretch"
                sx={{ flex: 1 }}
            >
                <SidebarContainer variant="outlined">
                    <Stack direction="row" justifyContent="space-between" alignItems="center">
                        <Typography variant="subtitle2" sx={{ fontWeight: 600 }}>
                            Wireframe Explorer
                        </Typography>
                        <Tooltip title="Force reload">
                            <span>
                                <IconButton
                                    size="small"
                                    onClick={handleRefresh}
                                    disabled={!filePath}
                                    sx={{ color: theme.palette.text.secondary }}
                                >
                                    <RefreshIcon fontSize="small" />
                                </IconButton>
                            </span>
                        </Tooltip>
                    </Stack>
                    <Divider />
                    <Box sx={{ flex: 1, overflowY: 'auto' }}>
                        <List
                            disablePadding
                            subheader={
                                <ListSubheader component="div" sx={{ bgcolor: 'transparent', px: 0, fontWeight: 600 }}>
                                    All Screens
                                </ListSubheader>
                            }
                        >
                            {screenCategories.map((category) => (
                                <Box key={category.id} sx={{ mb: 1.5 }}>
                                    <Typography variant="body2" sx={{ fontWeight: 600, px: 0.5, mb: 0.5, textTransform: 'uppercase', fontSize: 11, color: 'text.secondary' }}>
                                        {category.title}
                                    </Typography>
                                    <List disablePadding dense>
                                        {category.items.map((item: any) => (
                                            <ListItemButton
                                                key={item.path}
                                                selected={selectedPath === item.path}
                                                onClick={() => setSelectedPath(item.path)}
                                                sx={{
                                                    borderRadius: 1,
                                                    mb: 0.5,
                                                    '&.Mui-selected': {
                                                        backgroundColor: alpha(theme.palette.primary.main, 0.12),
                                                        color: theme.palette.primary.main,
                                                        '&:hover': {
                                                            backgroundColor: alpha(theme.palette.primary.main, 0.2),
                                                        },
                                                    },
                                                }}
                                            >
                                                <ListItemText
                                                    primary={item.text}
                                                    primaryTypographyProps={{ fontSize: 13, fontWeight: selectedPath === item.path ? 600 : 400 }}
                                                />
                                            </ListItemButton>
                                        ))}
                                    </List>
                                </Box>
                            ))}
                        </List>
                    </Box>
                </SidebarContainer>

                <Stack spacing={2.5} sx={{ flex: 1, minHeight: 520 }}>
                    <Panel variant="outlined">
                        <Tabs
                            value={activeTab}
                            onChange={(_, value) => setActiveTab(value)}
                            aria-label="HTML console tabs"
                            sx={{
                                px: 2,
                                borderBottom: `1px solid ${alpha(theme.palette.divider, 0.7)}`,
                            }}
                        >
                            <Tab
                                label="Source"
                                value="source"
                                sx={{ textTransform: 'none', fontWeight: 600 }}
                            />
                            <Tab
                                label="Preview"
                                value="preview"
                                sx={{ textTransform: 'none', fontWeight: 600 }}
                            />
                        </Tabs>

                        {activeTab === 'source' && (
                            <Box sx={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                                <Stack
                                    direction="row"
                                    alignItems="center"
                                    justifyContent="space-between"
                                    sx={{ px: 2, py: 1, borderBottom: `1px solid ${alpha(theme.palette.divider, 0.7)}` }}
                                >
                                    <Box>
                                        <Typography variant="subtitle2" sx={{ fontWeight: 600 }}>
                                            Source Viewer
                                        </Typography>
                                        <Typography variant="caption" color="text.secondary">
                                            {filePath ? filePath.replace('../', 'src/pages/') : 'Select a screen from the explorer'}
                                        </Typography>
                                    </Box>
                                    <Tooltip title="Copy code">
                                        <span>
                                            <IconButton size="small" onClick={handleCopyCode} disabled={!code}>
                                                <ContentCopyIcon fontSize="small" />
                                            </IconButton>
                                        </span>
                                    </Tooltip>
                                </Stack>
                                {loadingCode ? (
                                    <Stack
                                        direction="row"
                                        alignItems="center"
                                        justifyContent="center"
                                        sx={{ flex: 1, py: 4 }}
                                        spacing={1}
                                    >
                                        <CircularProgress size={18} />
                                        <Typography variant="body2" color="text.secondary">
                                            Loading source...
                                        </Typography>
                                    </Stack>
                                ) : (
                                    <CodeBlock>{code || '// Select a screen to view its source'}</CodeBlock>
                                )}
                            </Box>
                        )}

                        {activeTab === 'preview' && (
                            <Box
                                sx={{
                                    flex: 1,
                                    display: 'flex',
                                    flexDirection: 'column',
                                    alignItems: 'center',
                                    justifyContent: 'center',
                                    backgroundColor: alpha(theme.palette.background.default, 0.6),
                                    p: 4,
                                }}
                            >
                                {loadError ? (
                                    <Stack spacing={1} alignItems="center" justifyContent="center" textAlign="center">
                                        <WarningAmberRoundedIcon color="warning" />
                                        <Typography variant="body2" color="text.secondary">
                                            {loadError}
                                        </Typography>
                                    </Stack>
                                ) : (
                                    <Stack spacing={2} alignItems="center">
                                        <Typography variant="h6" color="text.secondary">
                                            Preview Mode
                                        </Typography>
                                        <Typography variant="body2" color="text.secondary" textAlign="center">
                                            Component preview would render here in a full implementation.
                                            <br />
                                            Selected: {selectedPath || 'None'}
                                        </Typography>
                                    </Stack>
                                )}
                            </Box>
                        )}
                    </Panel>
                </Stack>
            </Stack>
        </Box>
    );
};

export default HtmlPreviewPage;
