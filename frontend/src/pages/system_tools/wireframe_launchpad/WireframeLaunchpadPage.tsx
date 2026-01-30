'use client';

import React from 'react';
import { Link } from 'react-router-dom';
import {
    Box,
    Typography,
    Card,
    CardContent,
    Stack,
    Button,
    Chip,
    Divider,
    Tooltip,
} from '@mui/material';
import LaunchIcon from '@mui/icons-material/Launch';

// Screen categories for Olivine Platform
const screenCategories = [
    {
        id: 'platform',
        title: 'Platform',
        description: 'Core system and platform utilities',
        color: '#7c3aed',
        items: [
            { text: 'Layout Settings', path: '/admin/layout-settings', description: 'UI appearance configuration' },
            { text: 'File Search Explorer', path: '/admin/file-search', description: 'Search within codebase' },
            { text: 'Visual Extractor', path: '/system-tools/visual-extractor', description: 'OCR image to text' },
            { text: 'Web Console', path: '/system-tools/web-console', description: 'Embedded web browser' },
            { text: 'HTML Preview', path: '/system-tools/html-preview', description: 'Wireframe inspector' },
            { text: 'DataOps Studio', path: '/system-tools/dataops-studio', description: 'Database management' },
            { text: 'Wireframe Launchpad', path: '/system-tools/wireframe-launchpad', description: 'Quick screen access' },
        ],
    },
    {
        id: 'retail',
        title: 'Retail',
        description: 'Core retail business operations',
        color: '#0284c7',
        items: [
            { text: 'Retail Dashboard', path: '/retail/dashboard', description: 'Operations overview' },
            { text: 'Test Console', path: '/test-console', description: 'Permission prototyping' },
            { text: 'Item Master', path: '/retail/inventory/item-master', description: 'Product catalog' },
            { text: 'Supplier Master', path: '/retail/procurement/suppliers', description: 'Vendor management' },
        ],
    },
    {
        id: 'pos',
        title: 'Point of Sale',
        description: 'POS and billing operations',
        color: '#059669',
        items: [
            { text: 'POS Desktop', path: '/pos/desktop', description: 'Main billing screen' },
            { text: 'Day Open', path: '/pos/day-open', description: 'Start business day' },
            { text: 'Session Open', path: '/pos/session-open', description: 'Start cashier session' },
            { text: 'Settlement', path: '/pos/settlement', description: 'End-of-day settlement' },
        ],
    },
    {
        id: 'hrm',
        title: 'HRM',
        description: 'Human resource management',
        color: '#dc2626',
        items: [
            { text: 'Employee Master', path: '/hrm/employees', description: 'Staff directory' },
            { text: 'Org Chart', path: '/hrm/org-chart', description: 'Organization structure' },
            { text: 'Attendance', path: '/hrm/attendance', description: 'Time tracking' },
        ],
    },
    {
        id: 'crm',
        title: 'CRM',
        description: 'Customer relationship management',
        color: '#f59e0b',
        items: [
            { text: 'Customer Master', path: '/crm/customers', description: 'Customer database' },
            { text: 'Leads', path: '/crm/leads', description: 'Lead management' },
            { text: 'Campaigns', path: '/crm/campaigns', description: 'Marketing campaigns' },
        ],
    },
    {
        id: 'fms',
        title: 'Finance',
        description: 'Financial management system',
        color: '#10b981',
        items: [
            { text: 'Journal Entry', path: '/finance/journal', description: 'Accounting entries' },
            { text: 'Chart of Accounts', path: '/finance/coa', description: 'Account structure' },
            { text: 'Reports', path: '/finance/reports', description: 'Financial reports' },
        ],
    },
];

const WireframeLaunchpadPage: React.FC = () => {
    return (
        <Box sx={{ p: 4 }}>
            <Typography variant="h3" gutterBottom>
                Wireframe Launchpad
            </Typography>
            <Typography variant="subtitle1" color="text.secondary" sx={{ maxWidth: 720 }}>
                Use this launchpad to jump directly into any available wireframe. Screens are grouped by the
                same categories used in the main navigation. Ideal for quick reviews, demos, and QA runs.
            </Typography>

            <Divider sx={{ my: 3 }} />

            {/* Using flex-wrap box instead of Grid */}
            <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 3 }}>
                {screenCategories.map((category) => (
                    <Box key={category.id} sx={{ width: { xs: '100%', md: 'calc(50% - 12px)' } }}>
                        <Card variant="outlined" sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
                            <CardContent sx={{ flexGrow: 1 }}>
                                <Stack direction="row" spacing={1} alignItems="center" mb={1}>
                                    <Typography variant="h5" sx={{ color: category.color }}>
                                        {category.title}
                                    </Typography>
                                    <Chip
                                        label={`${category.items.length} screens`}
                                        size="small"
                                        sx={{ textTransform: 'capitalize' }}
                                    />
                                </Stack>
                                {category.description && (
                                    <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                                        {category.description}
                                    </Typography>
                                )}

                                <Stack spacing={1.5}>
                                    {category.items.map((item) => (
                                        <Tooltip
                                            key={item.path}
                                            title={item.description || ''}
                                            placement="top"
                                            arrow
                                        >
                                            <Button
                                                component={Link}
                                                to={item.path}
                                                variant="outlined"
                                                endIcon={<LaunchIcon fontSize="small" />}
                                                sx={{
                                                    justifyContent: 'space-between',
                                                    textTransform: 'none',
                                                }}
                                            >
                                                <Box sx={{ textAlign: 'left' }}>
                                                    <Typography variant="subtitle1">{item.text}</Typography>
                                                    {item.description && (
                                                        <Typography variant="caption" color="text.secondary">
                                                            {item.description}
                                                        </Typography>
                                                    )}
                                                </Box>
                                            </Button>
                                        </Tooltip>
                                    ))}
                                </Stack>
                            </CardContent>
                        </Card>
                    </Box>
                ))}
            </Box>
        </Box>
    );
};

export default WireframeLaunchpadPage;

