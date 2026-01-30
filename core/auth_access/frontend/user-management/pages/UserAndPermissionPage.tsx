import React, { useState, useEffect, useMemo, useCallback } from "react";
import {
    Box,
    Typography,
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Paper,
    Checkbox,
    Button,
    Tabs,
    Tab,
    FormControl,
    InputLabel,
    Select,
    MenuItem,
    IconButton,
    CircularProgress,
    Chip,
    Alert,
    Snackbar,
    Dialog,
    DialogTitle,
    DialogContent,
    DialogActions,
    List,
    ListItem,
    ListItemText,
    ListItemIcon,
    Divider,
} from "@mui/material";
import {
    Save as SaveIcon,
    ChevronRight as ChevronRightIcon,
    ExpandMore as ExpandMoreIcon,
    Download as DownloadIcon,
    Upload as UploadIcon,
    Visibility as VisibilityIcon,
    Close as CloseIcon,
    Security as SecurityIcon,
    Check as CheckIcon,
} from "@mui/icons-material";
import { menuConfig, MenuItem as MenuConfigItem } from "@app/menuConfig";
import {
    userPermissionService,
    Role,
    UserPermissions,
    User
} from "@services/userPermissionService";
import { SYSTEM_ROLES, ROLE_DEFINITIONS } from "../../../config/rolePermissions";

// ============================================================================
// TYPES
// ============================================================================

interface MenuRow {
    id: string;
    label: string;
    level: number;
    isHeader?: boolean;
    parentId?: string;
    hasChildren?: boolean;
}

// Permission types matching reference
const PERMISSION_TYPES = ['access', 'view', 'create', 'edit', 'delete'] as const;

// Role order: Admin > Back Office Manager > Back Office User > POS Manager > POS User
const ROLE_ORDER = ['admin', 'backofficemanager', 'backofficeuser', 'posmanager', 'posuser'];

const sortRoles = (roles: Role[]): Role[] => {
    return [...roles].sort((a, b) => {
        const aIdx = ROLE_ORDER.indexOf(a.role_key);
        const bIdx = ROLE_ORDER.indexOf(b.role_key);
        if (aIdx === -1 && bIdx === -1) return 0;
        if (aIdx === -1) return 1;
        if (bIdx === -1) return -1;
        return aIdx - bIdx;
    });
};

// ============================================================================
// HELPER: Flatten menu config with hierarchy
// ============================================================================

const flattenMenuConfig = (items: MenuConfigItem[], level: number = 0, parentId?: string): MenuRow[] => {
    const rows: MenuRow[] = [];

    items.forEach(item => {
        if (item.divider) return;

        const hasChildren = !!item.children && item.children.length > 0;

        rows.push({
            id: item.id,
            label: item.label,
            level,
            isHeader: hasChildren,
            parentId,
            hasChildren,
        });

        if (item.children) {
            rows.push(...flattenMenuConfig(item.children, level + 1, item.id));
        }
    });

    return rows;
};

// Get retail menu items (focus on Retail module)
const getRetailMenuRows = (): MenuRow[] => {
    const retailMenu = menuConfig.find(item => item.id === 'retail');
    const securityMenu = menuConfig.find(item => item.id === 'security');

    const rows: MenuRow[] = [];

    if (securityMenu) {
        rows.push(...flattenMenuConfig([securityMenu], 0));
    }

    if (retailMenu && retailMenu.children) {
        retailMenu.children.forEach(child => {
            rows.push(...flattenMenuConfig([child], 0));
        });
    }

    return rows;
};

// ============================================================================
// PERMISSION MATRIX COMPONENT - EXACT REFERENCE DESIGN
// ============================================================================

interface PermissionMatrixProps {
    roles: Role[];
    menuRows: MenuRow[];
    permissions: { [roleKey: string]: { [menuId: string]: { [key: string]: boolean } } };
    onPermissionChange: (roleKey: string, menuId: string, field: string, value: boolean) => void;
    onSelectAllForRole: (roleKey: string, permType: string, value: boolean) => void;
    onToggleAll: (value: boolean) => void;
    onSave: () => void;
    saving: boolean;
    loading: boolean;
}

const PermissionMatrix: React.FC<PermissionMatrixProps> = ({
    roles,
    menuRows,
    permissions,
    onPermissionChange,
    onSelectAllForRole,
    onToggleAll,
    onSave,
    saving,
    loading,
}) => {
    const [expandedRows, setExpandedRows] = useState<Set<string>>(new Set());
    const [templateDialogOpen, setTemplateDialogOpen] = useState(false);
    const [roleTemplates, setRoleTemplates] = useState<any[]>([]);
    const [allSelected, setAllSelected] = useState(false);

    // Check if all permissions for a role-permType combination are selected (inline for performance)
    const isColumnAllSelected = (roleKey: string, permType: string): boolean => {
        const rolePerms = permissions[roleKey];
        if (!rolePerms) return false;
        const field = `can_${permType}`;
        return menuRows.every(row => rolePerms[row.id]?.[field] === true);
    };

    // Check if any permission for a role-permType combination is selected
    const isColumnPartiallySelected = (roleKey: string, permType: string): boolean => {
        const rolePerms = permissions[roleKey];
        if (!rolePerms) return false;
        const field = `can_${permType}`;
        const selected = menuRows.filter(row => rolePerms[row.id]?.[field] === true);
        return selected.length > 0 && selected.length < menuRows.length;
    };

    useEffect(() => {
        const allHeaders = menuRows.filter(r => r.isHeader).map(r => r.id);
        setExpandedRows(new Set(allHeaders));
    }, [menuRows]);

    // Simple toggle - no useCallback needed for admin form
    const toggleExpand = (id: string) => {
        setExpandedRows(prev => {
            const next = new Set(prev);
            if (next.has(id)) next.delete(id);
            else next.add(id);
            return next;
        });
    };

    // Simple visibility check
    const isVisible = (row: MenuRow): boolean => {
        if (!row.parentId) return true;

        let currentParentId: string | undefined = row.parentId;
        const menuRowsMap = new Map(menuRows.map(r => [r.id, r]));

        while (currentParentId) {
            if (!expandedRows.has(currentParentId)) return false;
            const parentRow = menuRowsMap.get(currentParentId);
            currentParentId = parentRow?.parentId;
        }

        return true;
    };

    const handleViewTemplates = async () => {
        try {
            const templates = await userPermissionService.getRoleTemplates();
            // Convert object to array if necessary - handle both array and Record types
            const templatesArray: any[] = Array.isArray(templates)
                ? templates
                : Object.values(templates as Record<string, any>);
            setRoleTemplates(templatesArray);
        } catch (error) {
            // Use fallback templates
            setRoleTemplates([
                { role_key: 'admin', role_name: 'Administrator', description: 'Full access to all features', permissions: ['all'] },
                { role_key: 'backofficemanager', role_name: 'Back Office Manager', description: 'Back office operations and approvals', permissions: ['view', 'create', 'edit'] },
                { role_key: 'backofficeuser', role_name: 'Back Office User', description: 'Back office screens access', permissions: ['view', 'create'] },
                { role_key: 'posmanager', role_name: 'POS Manager', description: 'POS operations and management', permissions: ['view', 'create', 'edit'] },
                { role_key: 'posuser', role_name: 'POS User', description: 'POS billing and on-the-fly creation', permissions: ['view'] },
            ]);
        }
        setTemplateDialogOpen(true);
    };

    if (loading) {
        return (
            <Box display="flex" justifyContent="center" alignItems="center" flex={1}>
                <CircularProgress size={48} sx={{ color: '#3b82f6' }} />
            </Box>
        );
    }

    return (
        <Box display="flex" flexDirection="column" flex={1} overflow="hidden">
            {/* View Role Template Dialog */}
            <Dialog
                open={templateDialogOpen}
                onClose={() => setTemplateDialogOpen(false)}
                maxWidth="sm"
                fullWidth
            >
                <DialogTitle sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <Box display="flex" alignItems="center" gap={1}>
                        <SecurityIcon sx={{ color: '#3b82f6' }} />
                        <Typography variant="h6">Role Templates</Typography>
                    </Box>
                    <IconButton onClick={() => setTemplateDialogOpen(false)} size="small">
                        <CloseIcon />
                    </IconButton>
                </DialogTitle>
                <DialogContent dividers>
                    <List>
                        {roleTemplates.map((template, idx) => (
                            <React.Fragment key={template.role_key}>
                                <ListItem>
                                    <ListItemIcon>
                                        <SecurityIcon sx={{ color: '#3b82f6' }} />
                                    </ListItemIcon>
                                    <ListItemText
                                        primary={
                                            <Typography fontWeight={600}>{template.role_name}</Typography>
                                        }
                                        secondary={
                                            <Box>
                                                <Typography variant="body2" color="text.secondary">
                                                    {template.description}
                                                </Typography>
                                                <Box display="flex" gap={0.5} mt={0.5} flexWrap="wrap">
                                                    {(template.permissions || []).map((perm: string) => (
                                                        <Chip
                                                            key={perm}
                                                            label={perm}
                                                            size="small"
                                                            sx={{
                                                                backgroundColor: '#dbeafe',
                                                                color: '#1d4ed8',
                                                                fontSize: '10px',
                                                            }}
                                                        />
                                                    ))}
                                                </Box>
                                            </Box>
                                        }
                                    />
                                </ListItem>
                                {idx < roleTemplates.length - 1 && <Divider />}
                            </React.Fragment>
                        ))}
                    </List>
                </DialogContent>
                <DialogActions>
                    <Button onClick={() => setTemplateDialogOpen(false)}>Close</Button>
                </DialogActions>
            </Dialog>

            {/* Action Buttons Row - Light Blue Background */}
            <Box
                display="flex"
                justifyContent="flex-end"
                alignItems="center"
                gap={1}
                mb={1}
                flexShrink={0}
                sx={{
                    backgroundColor: '#dbeafe',
                    padding: '8px 12px',
                    borderRadius: '6px',
                }}
            >
                <Button
                    variant="outlined"
                    size="small"
                    startIcon={<VisibilityIcon sx={{ fontSize: '16px' }} />}
                    onClick={handleViewTemplates}
                    sx={{
                        borderColor: '#3b82f6',
                        color: '#3b82f6',
                        fontSize: '12px',
                        textTransform: 'none',
                        px: 1.5,
                        py: 0.5,
                    }}
                >
                    View Role Template
                </Button>
                <Button
                    variant="outlined"
                    size="small"
                    startIcon={<DownloadIcon sx={{ fontSize: '16px' }} />}
                    sx={{
                        borderColor: '#3b82f6',
                        color: '#3b82f6',
                        fontSize: '12px',
                        textTransform: 'none',
                        px: 1.5,
                        py: 0.5,
                    }}
                >
                    Download Excel
                </Button>
                <Button
                    variant="outlined"
                    size="small"
                    startIcon={<UploadIcon sx={{ fontSize: '16px' }} />}
                    sx={{
                        borderColor: '#3b82f6',
                        color: '#3b82f6',
                        fontSize: '12px',
                        textTransform: 'none',
                        px: 1.5,
                        py: 0.5,
                    }}
                >
                    Upload Excel
                </Button>
                <Button
                    variant="outlined"
                    size="small"
                    startIcon={<CheckIcon sx={{ fontSize: '16px' }} />}
                    onClick={() => {
                        const newValue = !allSelected;
                        setAllSelected(newValue);
                        onToggleAll(newValue);
                    }}
                    sx={{
                        borderColor: allSelected ? '#10b981' : '#3b82f6',
                        color: allSelected ? '#10b981' : '#3b82f6',
                        fontSize: '12px',
                        textTransform: 'none',
                        px: 1.5,
                        py: 0.5,
                    }}
                >
                    {allSelected ? 'Deselect All' : 'Select All'}
                </Button>
                <Button
                    variant="contained"
                    size="small"
                    startIcon={<SaveIcon sx={{ fontSize: '16px' }} />}
                    onClick={onSave}
                    disabled={saving}
                    sx={{
                        backgroundColor: '#3b82f6',
                        fontSize: '12px',
                        textTransform: 'none',
                        px: 1.5,
                        py: 0.5,
                        '&:hover': { backgroundColor: '#2563eb' },
                    }}
                >
                    {saving ? 'Saving...' : 'Save Permissions'}
                </Button>
            </Box>

            {/* Permission Matrix Table with Exact Reference Header */}
            <TableContainer
                component={Paper}
                sx={{
                    flex: 1,
                    overflow: 'auto',
                    border: '1px solid #e2e8f0',
                    borderRadius: '4px',
                }}
            >
                <Table stickyHeader size="small" sx={{ tableLayout: 'fixed', width: '100%' }}>
                    {/* EXACT REFERENCE HEADER */}
                    <TableHead>
                        {/* Row 1: Role Names with Descriptions */}
                        <TableRow>
                            {/* Menu Item Column Header */}
                            <TableCell
                                rowSpan={2}
                                sx={{
                                    backgroundColor: '#3b82f6',
                                    color: '#fff',
                                    fontWeight: 600,
                                    fontSize: '11px',
                                    width: '180px',
                                    minWidth: '180px',
                                    padding: '6px 10px',
                                    borderRight: '1px solid #60a5fa',
                                    position: 'sticky',
                                    left: 0,
                                    zIndex: 3,
                                    verticalAlign: 'middle',
                                }}
                            >
                                Menu Item
                            </TableCell>

                            {/* Role Headers */}
                            {sortRoles(roles).map((role, idx) => (
                                <TableCell
                                    key={role.role_key}
                                    colSpan={5}
                                    sx={{
                                        backgroundColor: '#3b82f6',
                                        color: '#fff',
                                        textAlign: 'center',
                                        padding: '4px 2px',
                                        borderRight: idx < roles.length - 1 ? '1px solid #60a5fa' : 'none',
                                    }}
                                >
                                    <Typography
                                        variant="caption"
                                        sx={{
                                            fontWeight: 700,
                                            fontSize: '11px',
                                            display: 'block',
                                            color: '#fff',
                                        }}
                                    >
                                        {role.role_name}
                                    </Typography>
                                    <Typography
                                        variant="caption"
                                        sx={{
                                            fontSize: '9px',
                                            color: 'rgba(255,255,255,0.85)',
                                            display: 'block',
                                        }}
                                    >
                                        {role.description || 'System role'}
                                    </Typography>
                                </TableCell>
                            ))}
                        </TableRow>

                        {/* Row 2: Permission Types - 90 Degree Rotated */}
                        <TableRow>
                            {sortRoles(roles).map((role, roleIdx) => (
                                <React.Fragment key={`perm-headers-${role.role_key}`}>
                                    {PERMISSION_TYPES.map((perm, permIdx) => (
                                        <TableCell
                                            key={`${role.role_key}-${perm}-header`}
                                            sx={{
                                                backgroundColor: '#3b82f6',
                                                color: '#fff',
                                                textAlign: 'center',
                                                padding: 0,
                                                height: '45px',
                                                width: '28px',
                                                minWidth: '28px',
                                                maxWidth: '28px',
                                                borderRight: permIdx === 4
                                                    ? (roleIdx < roles.length - 1 ? '1px solid #60a5fa' : 'none')
                                                    : '1px solid rgba(255,255,255,0.2)',
                                                position: 'relative',
                                                verticalAlign: 'bottom',
                                            }}
                                        >
                                            {/* 90 Degree Rotated Text - Centered */}
                                            <Box
                                                sx={{
                                                    position: 'absolute',
                                                    top: '50%',
                                                    left: '50%',
                                                    transform: 'translate(-50%, -50%) rotate(-90deg)',
                                                    transformOrigin: 'center center',
                                                    whiteSpace: 'nowrap',
                                                    fontSize: '9px',
                                                    fontWeight: 500,
                                                    color: '#fff',
                                                    textAlign: 'center',
                                                }}
                                            >
                                                {perm.charAt(0).toUpperCase() + perm.slice(1)}
                                            </Box>
                                        </TableCell>
                                    ))}
                                </React.Fragment>
                            ))}
                        </TableRow>

                        {/* Row 3: Select All Checkboxes */}
                        <TableRow>
                            <TableCell
                                sx={{
                                    backgroundColor: '#dbeafe',
                                    padding: '2px 6px',
                                    fontWeight: 600,
                                    fontSize: '10px',
                                    color: '#1e40af',
                                    position: 'sticky',
                                    left: 0,
                                    zIndex: 2,
                                }}
                            >
                                Select All â†“
                            </TableCell>
                            {sortRoles(roles).map((role, roleIdx) => (
                                <React.Fragment key={`select-all-${role.role_key}`}>
                                    {PERMISSION_TYPES.map((perm, permIdx) => {
                                        const allChecked = isColumnAllSelected(role.role_key, perm);
                                        const partialChecked = isColumnPartiallySelected(role.role_key, perm);
                                        return (
                                            <TableCell
                                                key={`${role.role_key}-${perm}-selectall`}
                                                align="center"
                                                sx={{
                                                    backgroundColor: '#dbeafe',
                                                    padding: '1px',
                                                    width: '28px',
                                                    minWidth: '28px',
                                                    maxWidth: '28px',
                                                    borderRight: permIdx === 4
                                                        ? (roleIdx < roles.length - 1 ? '1px solid #93c5fd' : 'none')
                                                        : '1px solid #bfdbfe',
                                                }}
                                            >
                                                <Checkbox
                                                    size="small"
                                                    checked={allChecked}
                                                    indeterminate={partialChecked && !allChecked}
                                                    onChange={(e) => onSelectAllForRole(role.role_key, perm, e.target.checked)}
                                                    sx={{
                                                        padding: '1px',
                                                        color: '#60a5fa',
                                                        '&.Mui-checked': {
                                                            color: '#2563eb',
                                                        },
                                                        '&.MuiCheckbox-indeterminate': {
                                                            color: '#60a5fa',
                                                        },
                                                        '& .MuiSvgIcon-root': {
                                                            fontSize: '14px',
                                                        },
                                                    }}
                                                />
                                            </TableCell>
                                        );
                                    })}
                                </React.Fragment>
                            ))}
                        </TableRow>
                    </TableHead>

                    {/* Body */}
                    <TableBody>
                        {menuRows.map(row => {
                            if (!isVisible(row)) return null;

                            const isSection = row.isHeader;
                            // Lighter grey background with good contrast to blue header
                            const bgColor = isSection ? "#e0e7ef" : "#f0f4f8";

                            return (
                                <TableRow
                                    key={row.id}
                                    sx={{
                                        backgroundColor: bgColor,
                                        '&:hover': { backgroundColor: '#f8fafc' },
                                    }}
                                >
                                    {/* Menu Item Name */}
                                    <TableCell
                                        sx={{
                                            backgroundColor: bgColor,
                                            width: '180px',
                                            minWidth: '180px',
                                            padding: '3px 6px',
                                            paddingLeft: `${6 + row.level * 14}px`,
                                            borderRight: '1px solid #e2e8f0',
                                            position: 'sticky',
                                            left: 0,
                                            zIndex: 1,
                                        }}
                                    >
                                        <Box display="flex" alignItems="center">
                                            {row.hasChildren ? (
                                                <IconButton
                                                    size="small"
                                                    onClick={() => toggleExpand(row.id)}
                                                    sx={{ padding: '1px', marginRight: '2px' }}
                                                >
                                                    {expandedRows.has(row.id) ? (
                                                        <ExpandMoreIcon sx={{ fontSize: '14px' }} />
                                                    ) : (
                                                        <ChevronRightIcon sx={{ fontSize: '14px' }} />
                                                    )}
                                                </IconButton>
                                            ) : (
                                                <Box width={18} />
                                            )}
                                            <Typography
                                                variant="body2"
                                                sx={{
                                                    fontWeight: isSection ? 600 : 400,
                                                    color: isSection ? '#1e293b' : '#475569',
                                                    fontSize: isSection ? '11px' : '10px',
                                                }}
                                            >
                                                {row.label}
                                            </Typography>
                                        </Box>
                                    </TableCell>

                                    {/* Permission Checkboxes */}
                                    {sortRoles(roles).map((role, roleIdx) => {
                                        const rolePerms = permissions[role.role_key] || {};
                                        const menuPerms = rolePerms[row.id] || {};

                                        return (
                                            <React.Fragment key={`${role.role_key}-${row.id}`}>
                                                {PERMISSION_TYPES.map((perm, permIdx) => (
                                                    <TableCell
                                                        key={`${role.role_key}-${row.id}-${perm}`}
                                                        align="center"
                                                        sx={{
                                                            padding: '1px',
                                                            width: '28px',
                                                            minWidth: '28px',
                                                            maxWidth: '28px',
                                                            borderRight: permIdx === 4
                                                                ? (roleIdx < roles.length - 1 ? '1px solid #e2e8f0' : 'none')
                                                                : '1px solid #f1f5f9',
                                                        }}
                                                    >
                                                        <Checkbox
                                                            size="small"
                                                            checked={!!menuPerms[`can_${perm}`]}
                                                            onChange={(e) => onPermissionChange(
                                                                role.role_key,
                                                                row.id,
                                                                `can_${perm}`,
                                                                e.target.checked
                                                            )}
                                                            sx={{
                                                                padding: '1px',
                                                                color: '#cbd5e1',
                                                                '&.Mui-checked': {
                                                                    color: '#3b82f6',
                                                                },
                                                                '& .MuiSvgIcon-root': {
                                                                    fontSize: '14px',
                                                                },
                                                            }}
                                                        />
                                                    </TableCell>
                                                ))}
                                            </React.Fragment>
                                        );
                                    })}
                                </TableRow>
                            );
                        })}
                    </TableBody>
                </Table>
            </TableContainer>
        </Box>
    );
};

// ============================================================================
// USER-ROLE MAPPING COMPONENT (Matching Reference Design)
// ============================================================================

interface UserRoleMappingProps {
    users: User[];
    roles: Role[];
    loading: boolean;
    onSaveMapping: (userId: number, roleKey: string) => Promise<void>;
}

const UserRoleMapping: React.FC<UserRoleMappingProps> = ({
    users,
    roles,
    loading,
    onSaveMapping,
}) => {
    const [userRoles, setUserRoles] = useState<Record<number, string>>({});
    const [saving, setSaving] = useState(false);

    useEffect(() => {
        const rolesMap: Record<number, string> = {};
        users.forEach(u => rolesMap[u.id] = u.role || 'posuser');
        setUserRoles(rolesMap);
    }, [users]);

    const handleSaveAll = async () => {
        setSaving(true);
        try {
            for (const userId of Object.keys(userRoles)) {
                await onSaveMapping(Number(userId), userRoles[Number(userId)]);
            }
        } finally {
            setSaving(false);
        }
    };

    if (loading) {
        return (
            <Box display="flex" justifyContent="center" alignItems="center" flex={1}>
                <CircularProgress size={48} sx={{ color: '#3b82f6' }} />
            </Box>
        );
    }

    return (
        <Box flex={1} overflow="auto" p={2}>
            {/* Header - Matching Reference */}
            <Box mb={2}>
                <Typography variant="h6" sx={{ fontWeight: 600, color: '#1e293b', mb: 0.5 }}>
                    Assign Users to Roles
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Map users to roles. Users will inherit permissions from their assigned role.
                </Typography>
            </Box>

            <TableContainer component={Paper} sx={{ borderRadius: '4px', boxShadow: 1 }}>
                <Table size="medium">
                    <TableHead>
                        <TableRow>
                            <TableCell sx={{ backgroundColor: '#374151', color: '#fff', fontWeight: 600, py: 1.5 }}>Username</TableCell>
                            <TableCell sx={{ backgroundColor: '#374151', color: '#fff', fontWeight: 600, py: 1.5 }}>Email</TableCell>
                            <TableCell sx={{ backgroundColor: '#374151', color: '#fff', fontWeight: 600, py: 1.5 }}>Current Role</TableCell>
                            <TableCell sx={{ backgroundColor: '#374151', color: '#fff', fontWeight: 600, py: 1.5, width: 220 }}>Assign Role</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {users.length === 0 ? (
                            <TableRow>
                                <TableCell colSpan={4} align="center" sx={{ py: 4 }}>
                                    <Typography color="text.secondary">No users found. Create users from the Admin panel.</Typography>
                                </TableCell>
                            </TableRow>
                        ) : (
                            users.map(user => (
                                <TableRow key={user.id} sx={{ '&:hover': { backgroundColor: '#f9fafb' } }}>
                                    <TableCell sx={{ py: 2, color: '#2563eb' }}>{user.username}</TableCell>
                                    <TableCell sx={{ py: 2, color: '#2563eb' }}>{user.email || '-'}</TableCell>
                                    <TableCell sx={{ py: 2 }}>
                                        <Chip
                                            label={roles.find(r => r.role_key === user.role)?.role_name || user.role || 'Not assigned'}
                                            size="small"
                                            sx={{
                                                backgroundColor: '#374151',
                                                color: '#fff',
                                                fontWeight: 500,
                                            }}
                                        />
                                    </TableCell>
                                    <TableCell sx={{ py: 1 }}>
                                        <FormControl size="small" sx={{ minWidth: 180 }}>
                                            <InputLabel id={`role-select-${user.id}`}>Select Role</InputLabel>
                                            <Select
                                                labelId={`role-select-${user.id}`}
                                                label="Select Role"
                                                value={userRoles[user.id] || ''}
                                                onChange={(e) => setUserRoles({ ...userRoles, [user.id]: e.target.value })}
                                            >
                                                {roles.map(r => (
                                                    <MenuItem key={r.role_key} value={r.role_key}>{r.role_name}</MenuItem>
                                                ))}
                                            </Select>
                                        </FormControl>
                                    </TableCell>
                                </TableRow>
                            ))
                        )}
                    </TableBody>
                </Table>
            </TableContainer>

            {/* Save Button */}
            {users.length > 0 && (
                <Box display="flex" justifyContent="flex-end" mt={2} gap={1}>
                    <Button variant="outlined" onClick={() => {
                        const rolesMap: Record<number, string> = {};
                        users.forEach(u => rolesMap[u.id] = u.role || 'posuser');
                        setUserRoles(rolesMap);
                    }}>
                        Reset
                    </Button>
                    <Button
                        variant="contained"
                        startIcon={<SaveIcon />}
                        onClick={handleSaveAll}
                        disabled={saving}
                        sx={{
                            backgroundColor: '#374151',
                            '&:hover': { backgroundColor: '#1f2937' },
                        }}
                    >
                        {saving ? 'Saving...' : 'Save Mappings'}
                    </Button>
                </Box>
            )}
        </Box>
    );
};

// ============================================================================
// USER-LOCATION MAPPING COMPONENT (Matching Reference Design)
// ============================================================================

interface UserLocationMappingProps {
    users: User[];
    roles: Role[];
    locations: any[];
    loading: boolean;
    onSaveMapping: (userId: number, locationId: number | null) => Promise<void>;
}

const UserLocationMapping: React.FC<UserLocationMappingProps> = ({
    users,
    roles,
    locations,
    loading,
    onSaveMapping,
}) => {
    const [userLocations, setUserLocations] = useState<Record<number, number | ''>>({});
    const [saving, setSaving] = useState(false);

    // Filter to only show POS users (posmanager, posuser)
    const posUsers = users.filter(u => ['posmanager', 'posuser'].includes(u.role || ''));

    useEffect(() => {
        const locMap: Record<number, number | ''> = {};
        posUsers.forEach(u => locMap[u.id] = u.pos_location_id || '');
        setUserLocations(locMap);
    }, [users]);

    const handleSaveAll = async () => {
        setSaving(true);
        try {
            for (const userId of Object.keys(userLocations)) {
                const locId = userLocations[Number(userId)];
                await onSaveMapping(Number(userId), locId || null);
            }
        } finally {
            setSaving(false);
        }
    };

    if (loading) {
        return (
            <Box display="flex" justifyContent="center" alignItems="center" flex={1}>
                <CircularProgress size={48} sx={{ color: '#3b82f6' }} />
            </Box>
        );
    }

    return (
        <Box flex={1} overflow="auto" p={2}>
            {/* Header - Matching Reference */}
            <Box mb={2}>
                <Typography variant="h6" sx={{ fontWeight: 600, color: '#1e293b', mb: 0.5 }}>
                    Map POS Users to Locations
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Assign store locations to POS users. Each POS user can be mapped to only one location.
                </Typography>
            </Box>

            <TableContainer component={Paper} sx={{ borderRadius: '4px', boxShadow: 1 }}>
                <Table size="medium">
                    <TableHead>
                        <TableRow>
                            <TableCell sx={{ backgroundColor: '#374151', color: '#fff', fontWeight: 600, py: 1.5 }}>Username</TableCell>
                            <TableCell sx={{ backgroundColor: '#374151', color: '#fff', fontWeight: 600, py: 1.5 }}>Email</TableCell>
                            <TableCell sx={{ backgroundColor: '#374151', color: '#fff', fontWeight: 600, py: 1.5 }}>Role</TableCell>
                            <TableCell sx={{ backgroundColor: '#374151', color: '#fff', fontWeight: 600, py: 1.5 }}>Current Location</TableCell>
                            <TableCell sx={{ backgroundColor: '#374151', color: '#fff', fontWeight: 600, py: 1.5, width: 200 }}>Assign Location</TableCell>
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {posUsers.length === 0 ? (
                            <TableRow>
                                <TableCell colSpan={5} align="center" sx={{ py: 4 }}>
                                    <Typography color="text.secondary">
                                        No POS users found. Only users with 'posuser' or 'posmanager' role can be mapped to locations.
                                    </Typography>
                                </TableCell>
                            </TableRow>
                        ) : (
                            posUsers.map(user => (
                                <TableRow key={user.id} sx={{ '&:hover': { backgroundColor: '#f9fafb' } }}>
                                    <TableCell sx={{ py: 2, color: '#2563eb' }}>{user.username}</TableCell>
                                    <TableCell sx={{ py: 2, color: '#2563eb' }}>{user.email || '-'}</TableCell>
                                    <TableCell sx={{ py: 2 }}>
                                        <Chip
                                            label={roles.find(r => r.role_key === user.role)?.role_name || user.role}
                                            size="small"
                                            sx={{
                                                backgroundColor: '#374151',
                                                color: '#fff',
                                                fontWeight: 500,
                                            }}
                                        />
                                    </TableCell>
                                    <TableCell sx={{ py: 2, color: '#6b7280' }}>
                                        {user.pos_location_id
                                            ? locations.find(l => l.id === user.pos_location_id)?.name || 'Unknown'
                                            : 'Not assigned'}
                                    </TableCell>
                                    <TableCell sx={{ py: 1 }}>
                                        <FormControl size="small" sx={{ minWidth: 160 }}>
                                            <Select
                                                value={userLocations[user.id] || ''}
                                                onChange={(e) => setUserLocations({
                                                    ...userLocations,
                                                    [user.id]: e.target.value as number | ''
                                                })}
                                                displayEmpty
                                            >
                                                <MenuItem value="">
                                                    <em>Select Location</em>
                                                </MenuItem>
                                                {locations.map(loc => (
                                                    <MenuItem key={loc.id} value={loc.id}>
                                                        {loc.name} {loc.code ? `(${loc.code})` : ''}
                                                    </MenuItem>
                                                ))}
                                            </Select>
                                        </FormControl>
                                    </TableCell>
                                </TableRow>
                            ))
                        )}
                    </TableBody>
                </Table>
            </TableContainer>

            {/* Action Buttons - Matching Reference */}
            {posUsers.length > 0 && (
                <Box display="flex" justifyContent="flex-end" mt={2} gap={1}>
                    <Button
                        variant="outlined"
                        onClick={() => {
                            const locMap: Record<number, number | ''> = {};
                            posUsers.forEach(u => locMap[u.id] = u.pos_location_id || '');
                            setUserLocations(locMap);
                        }}
                    >
                        Reset
                    </Button>
                    <Button
                        variant="contained"
                        startIcon={<SaveIcon />}
                        onClick={handleSaveAll}
                        disabled={saving}
                        sx={{
                            backgroundColor: '#374151',
                            '&:hover': { backgroundColor: '#1f2937' },
                        }}
                    >
                        {saving ? 'Saving...' : 'Save Mappings'}
                    </Button>
                </Box>
            )}
        </Box>
    );
};

// ============================================================================
// MAIN PAGE COMPONENT
// ============================================================================

const UserAndPermissionPage: React.FC = () => {
    const [activeTab, setActiveTab] = useState(0);
    const [loading, setLoading] = useState(false);
    const [saving, setSaving] = useState(false);
    const [snackbar, setSnackbar] = useState<{ open: boolean; message: string; severity: 'success' | 'error' }>({
        open: false,
        message: '',
        severity: 'success',
    });

    // Data State
    const [roles, setRoles] = useState<Role[]>([]);
    const [users, setUsers] = useState<User[]>([]);
    const [locations, setLocations] = useState<any[]>([]);
    const [permissions, setPermissions] = useState<{ [roleKey: string]: { [menuId: string]: { [key: string]: boolean } } }>({});

    // Get menu rows from menuConfig
    const menuRows = useMemo(() => getRetailMenuRows(), []);

    useEffect(() => {
        loadData();
    }, []);

    const loadData = async () => {
        setLoading(true);
        try {
            const rolesData = await userPermissionService.getRoles();
            setRoles(rolesData);

            const permsData: typeof permissions = {};
            rolesData.forEach(role => {
                permsData[role.role_key] = {};
                menuRows.forEach(menuRow => {
                    permsData[role.role_key][menuRow.id] = {
                        can_access: false,
                        can_view: false,
                        can_create: false,
                        can_edit: false,
                        can_delete: false,
                    };
                });
            });

            try {
                const matrixData = await userPermissionService.getPermissionMatrix();
                if (matrixData.matrix) {
                    Object.keys(matrixData.matrix).forEach(roleKey => {
                        if (permsData[roleKey]) {
                            Object.keys(matrixData.matrix[roleKey]).forEach(menuId => {
                                if (permsData[roleKey][menuId]) {
                                    permsData[roleKey][menuId] = {
                                        ...permsData[roleKey][menuId],
                                        ...matrixData.matrix[roleKey][menuId],
                                    };
                                }
                            });
                        }
                    });
                }
            } catch (e) {
                console.log('Using default permissions');
            }

            setPermissions(permsData);

            const [usersData, locationsData] = await Promise.all([
                userPermissionService.getUsers(),
                userPermissionService.getLocations(),
            ]);
            setUsers(usersData);
            setLocations(Array.isArray(locationsData) ? locationsData : (locationsData || []));

        } catch (error) {
            console.error('Failed to load data:', error);
            setSnackbar({ open: true, message: 'Failed to load data', severity: 'error' });

            // Fallback roles with exact descriptions from reference
            const defaultRoles: Role[] = [
                { id: 1, role_key: 'admin', role_name: 'Administrator', description: 'Full access to all features', is_system_role: true, is_active: true },
                { id: 2, role_key: 'posmanager', role_name: 'POS Manager', description: 'POS operations and management', is_system_role: true, is_active: true },
                { id: 3, role_key: 'posuser', role_name: 'POS User', description: 'POS billing and on-the-fly creation', is_system_role: true, is_active: true },
                { id: 4, role_key: 'backofficemanager', role_name: 'Back Office Manager', description: 'Back office operations and approvals', is_system_role: true, is_active: true },
                { id: 5, role_key: 'backofficeuser', role_name: 'Back Office User', description: 'Back office screens access', is_system_role: true, is_active: true },
            ];
            setRoles(defaultRoles);

            const permsData: typeof permissions = {};
            defaultRoles.forEach(role => {
                permsData[role.role_key] = {};
                menuRows.forEach(menuRow => {
                    permsData[role.role_key][menuRow.id] = {
                        can_access: false,
                        can_view: false,
                        can_create: false,
                        can_edit: false,
                        can_delete: false,
                    };
                });
            });
            setPermissions(permsData);
        } finally {
            setLoading(false);
        }
    };

    // Simple permission change - no useCallback for faster updates
    const handlePermissionChange = (roleKey: string, menuId: string, field: string, value: boolean) => {
        setPermissions(prev => ({
            ...prev,
            [roleKey]: {
                ...(prev[roleKey] || {}),
                [menuId]: {
                    ...(prev[roleKey]?.[menuId] || {}),
                    [field]: value
                }
            }
        }));
    };

    // Select/Deselect all permissions for a specific role and permission type
    const handleSelectAllForRole = (roleKey: string, permType: string, value: boolean) => {
        setPermissions(prev => {
            const updated = { ...prev };
            if (!updated[roleKey]) updated[roleKey] = {};

            menuRows.forEach(row => {
                if (!updated[roleKey][row.id]) {
                    updated[roleKey][row.id] = {
                        can_access: false,
                        can_view: false,
                        can_create: false,
                        can_edit: false,
                        can_delete: false,
                    };
                }
                updated[roleKey][row.id][`can_${permType}`] = value;
            });

            return updated;
        });
    };

    // Toggle all permissions for all roles
    const handleToggleAll = (value: boolean) => {
        setPermissions(() => {
            const updated: typeof permissions = {};

            roles.forEach(role => {
                updated[role.role_key] = {};
                menuRows.forEach(row => {
                    updated[role.role_key][row.id] = {
                        can_access: value,
                        can_view: value,
                        can_create: value,
                        can_edit: value,
                        can_delete: value,
                    };
                });
            });

            return updated;
        });
    };

    const handleSaveAllPermissions = async () => {
        setSaving(true);
        try {
            for (const role of roles) {
                const rolePermissions = permissions[role.role_key];
                if (rolePermissions) {
                    const formattedPerms: UserPermissions = {};
                    Object.keys(rolePermissions).forEach(menuId => {
                        formattedPerms[menuId] = {
                            can_view: rolePermissions[menuId].can_view || false,
                            can_create: rolePermissions[menuId].can_create || false,
                            can_edit: rolePermissions[menuId].can_edit || false,
                            can_delete: rolePermissions[menuId].can_delete || false,
                        };
                    });
                    await userPermissionService.saveBulkRolePermissions(role.role_key, formattedPerms);
                }
            }
            setSnackbar({ open: true, message: 'All permissions saved successfully', severity: 'success' });
        } catch (error) {
            console.error('Failed to save permissions:', error);
            setSnackbar({ open: true, message: 'Failed to save permissions', severity: 'error' });
        } finally {
            setSaving(false);
        }
    };

    const handleApplyTemplate = async (userId: number, roleKey: string) => {
        try {
            await userPermissionService.applyRoleTemplate(userId, roleKey);
            setSnackbar({ open: true, message: 'Role template applied successfully', severity: 'success' });
        } catch (error) {
            console.error('Failed to apply template:', error);
            setSnackbar({ open: true, message: 'Failed to apply template', severity: 'error' });
        }
    };

    const handleSaveLocationMapping = async (userId: number, locationId: number | null) => {
        try {
            if (locationId) {
                await userPermissionService.assignUserLocation(userId, locationId, 'both', true);
            }
            // TODO: Add API for unassigning location when locationId is null
            setSnackbar({ open: true, message: 'Location mapping saved', severity: 'success' });
        } catch (error) {
            console.error('Failed to save location mapping:', error);
            setSnackbar({ open: true, message: 'Failed to save location mapping', severity: 'error' });
        }
    };

    return (
        <Box
            sx={{
                height: '100%',
                display: 'flex',
                flexDirection: 'column',
                overflow: 'hidden',
                p: 2,
            }}
        >
            {/* Page Header - Matching Reference */}
            <Box mb={1} flexShrink={0}>
                <Typography
                    variant="h6"
                    sx={{
                        fontWeight: 500,
                        color: '#1e40af',
                        fontStyle: 'italic',
                    }}
                >
                    User and Permission
                </Typography>
                <Typography variant="body2" color="text.secondary" sx={{ fontSize: '12px' }}>
                    Manage role-based permissions across all menu categories, sub-categories, and menu items. Assign users to roles in a separate tab.
                </Typography>
            </Box>

            {/* Tabs - Matching Reference */}
            <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 1, flexShrink: 0 }}>
                <Tabs
                    value={activeTab}
                    onChange={(_, v) => setActiveTab(v)}
                    sx={{
                        minHeight: '36px',
                        '& .MuiTab-root': {
                            fontWeight: 400,
                            textTransform: 'none',
                            minHeight: '36px',
                            padding: '6px 16px',
                            fontSize: '13px',
                            color: '#3b82f6',
                        },
                        '& .Mui-selected': {
                            color: '#3b82f6',
                            fontWeight: 500,
                        },
                        '& .MuiTabs-indicator': {
                            backgroundColor: '#3b82f6',
                        },
                    }}
                >
                    <Tab label="Role Permissions Matrix" />
                    <Tab label="User-Role Mapping" />
                    <Tab label="User-Location Mapping" />
                </Tabs>
            </Box>

            {/* Tab Content */}
            <Box flex={1} display="flex" flexDirection="column" overflow="hidden">
                {activeTab === 0 && (
                    <PermissionMatrix
                        roles={roles}
                        menuRows={menuRows}
                        permissions={permissions}
                        onPermissionChange={handlePermissionChange}
                        onSelectAllForRole={handleSelectAllForRole}
                        onToggleAll={handleToggleAll}
                        onSave={handleSaveAllPermissions}
                        saving={saving}
                        loading={loading}
                    />
                )}

                {activeTab === 1 && (
                    <UserRoleMapping
                        users={users}
                        roles={roles}
                        loading={loading}
                        onSaveMapping={handleApplyTemplate}
                    />
                )}

                {activeTab === 2 && (
                    <UserLocationMapping
                        users={users}
                        roles={roles}
                        locations={locations}
                        loading={loading}
                        onSaveMapping={handleSaveLocationMapping}
                    />
                )}
            </Box>

            {/* Snackbar */}
            <Snackbar
                open={snackbar.open}
                autoHideDuration={4000}
                onClose={() => setSnackbar({ ...snackbar, open: false })}
                anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
            >
                <Alert
                    onClose={() => setSnackbar({ ...snackbar, open: false })}
                    severity={snackbar.severity}
                    sx={{ width: '100%' }}
                >
                    {snackbar.message}
                </Alert>
            </Snackbar>
        </Box>
    );
};

export default UserAndPermissionPage;



