'use client';

import React, { useState, useMemo, useCallback, useEffect } from 'react';
import {
    Box, Typography, Paper, TextField, InputAdornment, List, ListItemButton,
    ListItemText, Chip, Table, TableBody, TableCell, TableContainer, TableHead,
    TableRow, Tabs, Tab, IconButton, Stack, Accordion, AccordionSummary, AccordionDetails,
    Grid, ToggleButton, ToggleButtonGroup, CircularProgress
} from '@mui/material';
import { useTheme } from '@mui/material/styles';
import SearchIcon from '@mui/icons-material/Search';
import RefreshIcon from '@mui/icons-material/Refresh';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import ClearIcon from '@mui/icons-material/Clear';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ViewListIcon from '@mui/icons-material/ViewList';
import GridOnIcon from '@mui/icons-material/GridOn';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import TerminalIcon from '@mui/icons-material/Terminal';
import InfoIcon from '@mui/icons-material/Info';
import SaveIcon from '@mui/icons-material/Save';
import FilterListIcon from '@mui/icons-material/FilterList';
import TableViewIcon from '@mui/icons-material/TableView';
import AutoGraphIcon from '@mui/icons-material/AutoGraph';
import FormatAlignLeftIcon from '@mui/icons-material/FormatAlignLeft';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';

// API Base URL
const API_BASE = 'http://localhost:8000/api/dataops';

// Types
interface TableInfo {
    name: string;
    rowCount: number;
    columnCount: number;
    module: string;
}

interface ColumnInfo {
    name: string;
    type: string;
    primaryKey: boolean;
    nullable: boolean;
    default: string;
}

interface Relationship {
    direction: 'incoming' | 'outgoing';
    fromTable: string;
    fromCol: string;
    toTable: string;
    toCol: string;
    fieldName: string;
    relationType: string;
}

interface DatabaseInfo {
    type: string;
    name: string;
    version: string;
    tableCount: number;
    host: string;
    port: string;
}

const DataOpsStudioPage: React.FC = () => {
    const theme = useTheme();
    const [selectedTable, setSelectedTable] = useState<string>('');
    const [activeTab, setActiveTab] = useState(0);
    const [searchQuery, setSearchQuery] = useState('');
    const [expandedCategories, setExpandedCategories] = useState<Record<string, boolean>>({});
    const [relView, setRelView] = useState<'table' | 'graph'>('table');
    const [sqlQuery, setSqlQuery] = useState('');

    // Data State
    const [tables, setTables] = useState<TableInfo[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [columns, setColumns] = useState<ColumnInfo[]>([]);
    const [rows, setRows] = useState<any[]>([]);
    const [totalCount, setTotalCount] = useState(0);
    const [relationships, setRelationships] = useState<Relationship[]>([]);
    const [databaseInfo, setDatabaseInfo] = useState<DatabaseInfo | null>(null);
    const [sqlResults, setSqlResults] = useState<{ columns: string[], rows: any[] } | null>(null);
    const [contentLoading, setContentLoading] = useState(false);

    // Fetch Schema on Mount
    useEffect(() => {
        const fetchSchema = async () => {
            try {
                const res = await fetch(`${API_BASE}/schema/`);
                const data = await res.json();
                if (data.success && data.tables) {
                    setTables(data.tables);
                    // Auto-expand all categories
                    const initial: Record<string, boolean> = {};
                    data.tables.forEach((t: TableInfo) => initial[t.module] = true);
                    setExpandedCategories(initial);
                    // Select first table
                    if (data.tables.length > 0) {
                        setSelectedTable(data.tables[0].name);
                    }
                }
            } catch (err) {
                console.error("Schema fetch failed", err);
            } finally {
                setIsLoading(false);
            }
        };
        fetchSchema();
    }, []);

    // Fetch Database Info on Mount
    useEffect(() => {
        const fetchDbInfo = async () => {
            try {
                const res = await fetch(`${API_BASE}/database-info/`);
                const data = await res.json();
                if (data.success) {
                    setDatabaseInfo(data.database);
                }
            } catch (err) {
                console.error("Database info fetch failed", err);
            }
        };
        fetchDbInfo();
    }, []);

    // Fetch Content + Relationships when table changes
    useEffect(() => {
        if (!selectedTable) return;

        const fetchData = async () => {
            setContentLoading(true);
            try {
                // Fetch Content
                const contentRes = await fetch(`${API_BASE}/content/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ table: selectedTable })
                });
                const contentData = await contentRes.json();
                if (contentData.success) {
                    setColumns(contentData.columns || []);
                    setRows(contentData.rows || []);
                    setTotalCount(contentData.totalCount || 0);
                }

                // Fetch Relationships
                const relRes = await fetch(`${API_BASE}/relationships/`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ table: selectedTable })
                });
                const relData = await relRes.json();
                if (relData.success) {
                    setRelationships(relData.relationships || []);
                }
            } catch (err) {
                console.error("Data fetch failed", err);
                setColumns([]);
                setRows([]);
                setRelationships([]);
            } finally {
                setContentLoading(false);
            }
        };
        fetchData();
    }, [selectedTable]);

    // Execute SQL Query
    const executeSql = async () => {
        if (!sqlQuery.trim()) return;
        try {
            const res = await fetch(`${API_BASE}/query/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: sqlQuery })
            });
            const data = await res.json();
            if (data.success) {
                setSqlResults({ columns: data.columns, rows: data.rows });
            } else {
                alert("Error: " + data.error);
                setSqlResults(null);
            }
        } catch (err) {
            console.error("Query failed", err);
            alert("Query failed: " + err);
            setSqlResults(null);
        }
    };

    // Refresh schema
    const refreshSchema = async () => {
        setIsLoading(true);
        try {
            const res = await fetch(`${API_BASE}/schema/`);
            const data = await res.json();
            if (data.success) {
                setTables(data.tables);
            }
        } catch (err) {
            console.error("Refresh failed", err);
        } finally {
            setIsLoading(false);
        }
    };

    // Group tables by module
    const groupedTables = useMemo(() => {
        const groups: Record<string, TableInfo[]> = {};
        tables.forEach(t => {
            if (!groups[t.module]) groups[t.module] = [];
            groups[t.module].push(t);
        });
        return groups;
    }, [tables]);

    // Get current table info
    const currentTableInfo = useMemo(() => {
        return tables.find(t => t.name === selectedTable);
    }, [tables, selectedTable]);

    return (
        <Box sx={{ display: 'flex', flexDirection: 'column', height: '100%', bgcolor: '#f5f5f5' }}>
            {/* Header */}
            <Paper square elevation={0} sx={{
                py: 1.5, px: 3,
                borderBottom: '1px solid #e0e0e0',
                display: 'flex', justifyContent: 'space-between', alignItems: 'center',
                bgcolor: '#fff'
            }}>
                <Stack direction="row" spacing={1} alignItems="center">
                    <Typography variant="h6" color="primary" sx={{ fontWeight: 700, fontSize: '1.1rem' }}>DataOps Studio</Typography>
                    <Typography variant="body2" sx={{ color: '#666', borderLeft: '1px solid #ccc', pl: 1 }}>
                        Browse database tables organized by menu structure
                    </Typography>
                </Stack>
                <Typography variant="subtitle2" sx={{ fontWeight: 600, color: '#333' }}>
                    {databaseInfo ? `${databaseInfo.type} ${databaseInfo.version}` : 'Loading...'}
                </Typography>
            </Paper>

            <Box sx={{ flex: 1, display: 'flex', overflow: 'hidden', p: 2, gap: 2 }}>

                {/* LEFT PANEL - Table List */}
                <Paper variant="outlined" sx={{ width: 320, display: 'flex', flexDirection: 'column', bgcolor: '#fff', borderRadius: 1 }}>
                    <Box sx={{ p: 2, borderBottom: '1px solid #eee', bgcolor: '#fcfcfc' }}>
                        <Stack direction="row" justifyContent="space-between" alignItems="center" sx={{ mb: 1.5 }}>
                            <Typography variant="subtitle1" sx={{ fontWeight: 600, color: '#1565c0' }}>DataOps Tables</Typography>
                            <IconButton size="small" onClick={refreshSchema} disabled={isLoading}>
                                <RefreshIcon fontSize="small" color="action" />
                            </IconButton>
                        </Stack>
                        <TextField
                            fullWidth placeholder="Search tables..." size="small"
                            value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)}
                            InputProps={{ startAdornment: <InputAdornment position="start"><SearchIcon fontSize="small" sx={{ color: '#999' }} /></InputAdornment> }}
                            sx={{ '& .MuiOutlinedInput-root': { bgcolor: '#fff' } }}
                        />
                        <Typography variant="caption" sx={{ mt: 1, display: 'block', color: '#666' }}>
                            {tables.length} tables • {databaseInfo?.tableCount || 0} models
                        </Typography>
                    </Box>

                    <Box sx={{ flex: 1, overflow: 'auto' }}>
                        {isLoading ? (
                            <Box sx={{ display: 'flex', justifyContent: 'center', py: 4 }}>
                                <CircularProgress size={24} />
                            </Box>
                        ) : (
                            Object.keys(groupedTables).sort().map(module => (
                                <Accordion
                                    key={module}
                                    expanded={!!expandedCategories[module]}
                                    onChange={() => setExpandedCategories(p => ({ ...p, [module]: !p[module] }))}
                                    disableGutters elevation={0}
                                    sx={{
                                        '&::before': { display: 'none' },
                                        border: 'none',
                                        bgcolor: 'transparent'
                                    }}
                                >
                                    <AccordionSummary
                                        expandIcon={<ExpandMoreIcon sx={{ fontSize: 16, color: 'rgba(255,255,255,0.7)' }} />}
                                        sx={{
                                            minHeight: 32,
                                            bgcolor: '#417690',
                                            px: 2,
                                            '&.Mui-expanded': { minHeight: 32, margin: 0 },
                                            '& .MuiAccordionSummary-content': { margin: 0, '&.Mui-expanded': { margin: 0 } }
                                        }}
                                    >
                                        <Typography variant="body2" sx={{
                                            fontWeight: 600,
                                            color: '#fff',
                                            textTransform: 'uppercase',
                                            fontSize: '11px',
                                            letterSpacing: '0.05em',
                                            whiteSpace: 'nowrap',
                                            overflow: 'hidden',
                                            textOverflow: 'ellipsis'
                                        }}>
                                            {module} ({groupedTables[module].length})
                                        </Typography>
                                    </AccordionSummary>
                                    <AccordionDetails sx={{ p: 0 }}>
                                        <List dense disablePadding>
                                            {groupedTables[module]
                                                .filter(t => t.name.toLowerCase().includes(searchQuery.toLowerCase()))
                                                .map(t => (
                                                    <ListItemButton
                                                        key={t.name}
                                                        selected={selectedTable === t.name}
                                                        onClick={() => setSelectedTable(t.name)}
                                                        sx={{
                                                            pl: 2, py: 0.5,
                                                            borderBottom: '1px solid #f8f8f8',
                                                            bgcolor: '#fff',
                                                            minHeight: 28,
                                                            '&:hover': { bgcolor: '#f5f5f5' },
                                                            '&.Mui-selected': { bgcolor: '#fffee0' }, // Classic Django selected highlight or close to it
                                                            '&.Mui-selected:hover': { bgcolor: '#fffee0' }
                                                        }}
                                                    >
                                                        <ListItemText
                                                            primary={<Typography variant="body2" sx={{ color: selectedTable === t.name ? '#202020' : '#447e9b', fontSize: '13px', lineHeight: 1.2, fontWeight: selectedTable === t.name ? 700 : 500 }}>{t.name}</Typography>}
                                                        // Removed secondary text to match the clean look of the screenshot, or keep minimal if needed. The screenshot doesn't show row counts.
                                                        // Let's keep it visible but very subtle if valuable, or remove to match "exactly".
                                                        // User said "exactly like this", screenshot has NO secondary text.
                                                        />
                                                    </ListItemButton>
                                                ))}
                                        </List>
                                    </AccordionDetails>
                                </Accordion>
                            ))
                        )}
                    </Box>
                </Paper>

                {/* RIGHT PANEL - Content */}
                <Paper variant="outlined" sx={{ flex: 1, display: 'flex', flexDirection: 'column', bgcolor: '#fff', borderRadius: 1, overflow: 'hidden' }}>

                    {/* Tab Header */}
                    <Box sx={{
                        borderBottom: '1px solid #eee',
                        display: 'flex', alignItems: 'center', justifyContent: 'space-between',
                        px: 2, bgcolor: '#fcfcfc', minHeight: 48
                    }}>
                        <Tabs value={activeTab} onChange={(_, v) => setActiveTab(v)} sx={{ minHeight: 48 }}>
                            <CustomTab icon={<ViewListIcon fontSize="small" />} label="SCHEMA" />
                            <CustomTab icon={<GridOnIcon fontSize="small" />} label="DATA" />
                            <CustomTab icon={<AccountTreeIcon fontSize="small" />} label="RELATIONSHIPS" />
                            <CustomTab icon={<TerminalIcon fontSize="small" />} label="SQL QUERY" />
                            <CustomTab icon={<InfoIcon fontSize="small" />} label="DATABASE INFO" />
                        </Tabs>

                        <Stack direction="row" alignItems="center" spacing={2}>
                            <Typography variant="h6" sx={{ color: '#1565c0', fontWeight: 600, fontFamily: 'monospace' }}>{selectedTable}</Typography>
                            <Stack direction="row" spacing={1}>
                                <Chip label={`${columns.length} columns`} variant="outlined" size="small" sx={{ color: '#666', borderColor: '#ddd' }} />
                                <Chip label={`${totalCount} rows`} variant="outlined" size="small" sx={{ color: '#666', borderColor: '#ddd' }} />
                                {contentLoading && <CircularProgress size={16} />}
                            </Stack>
                        </Stack>
                    </Box>

                    {/* Tab Content */}
                    <Box sx={{ flex: 1, overflow: 'auto', p: 0, bgcolor: '#fff' }}>

                        {/* SCHEMA TAB */}
                        {activeTab === 0 && (
                            <Box sx={{ p: 3 }}>
                                <Typography variant="h6" color="primary" sx={{ mb: 2, fontWeight: 600 }}>Columns ({columns.length})</Typography>
                                <TableContainer>
                                    <Table size="small">
                                        <TableHead>
                                            <TableRow>
                                                <HeaderCell>Column</HeaderCell>
                                                <HeaderCell>Type</HeaderCell>
                                                <HeaderCell>Nullable</HeaderCell>
                                                <HeaderCell>Default</HeaderCell>
                                                <HeaderCell>Primary Key</HeaderCell>
                                            </TableRow>
                                        </TableHead>
                                        <TableBody>
                                            {columns.map(c => (
                                                <TableRow key={c.name} hover>
                                                    <Cell sx={{ color: '#1565c0', fontFamily: 'monospace' }}>{c.name}</Cell>
                                                    <Cell sx={{ textTransform: 'uppercase' }}>{c.type}</Cell>
                                                    <Cell>{c.nullable ? <span style={{ color: 'green' }}>Yes</span> : 'No'}</Cell>
                                                    <Cell>{c.default}</Cell>
                                                    <Cell>{c.primaryKey ? <span style={{ color: '#1565c0', fontWeight: 'bold' }}>Yes</span> : 'No'}</Cell>
                                                </TableRow>
                                            ))}
                                        </TableBody>
                                    </Table>
                                </TableContainer>
                            </Box>
                        )}

                        {/* DATA TAB */}
                        {activeTab === 1 && (
                            <Box sx={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
                                <Box sx={{ p: 1.5, borderBottom: '1px solid #eee', display: 'flex', gap: 1, alignItems: 'center' }}>
                                    <Typography variant="body2" sx={{ color: '#666' }}>
                                        Showing {rows.length} of {totalCount} rows
                                    </Typography>
                                    <Box sx={{ flex: 1 }} />
                                    <IconButton size="small"><FilterListIcon /></IconButton>
                                </Box>
                                <TableContainer sx={{ flex: 1 }}>
                                    <Table size="small" stickyHeader>
                                        <TableHead>
                                            <TableRow>
                                                {rows.length > 0 && Object.keys(rows[0]).map((key) => (
                                                    <TableCell key={key} sx={{ fontWeight: 600, whiteSpace: 'nowrap', bgcolor: 'background.paper', borderBottom: '1px solid #e0e0e0' }}>{key}</TableCell>
                                                ))}
                                            </TableRow>
                                        </TableHead>
                                        <TableBody>
                                            {rows.map((row: any, idx) => (
                                                <TableRow key={idx} hover>
                                                    {Object.values(row).map((val: any, i) => (
                                                        <TableCell key={i} sx={{ whiteSpace: 'nowrap', borderBottom: '1px solid #f0f0f0', maxWidth: 200, overflow: 'hidden', textOverflow: 'ellipsis' }}>
                                                            {val === null ? <em style={{ color: '#999' }}>null</em> : String(val)}
                                                        </TableCell>
                                                    ))}
                                                </TableRow>
                                            ))}
                                            {rows.length === 0 && (
                                                <TableRow>
                                                    <TableCell colSpan={columns.length || 6} align="center" sx={{ py: 4, color: '#888' }}>
                                                        No data found in this table
                                                    </TableCell>
                                                </TableRow>
                                            )}
                                        </TableBody>
                                    </Table>
                                </TableContainer>
                                <Box sx={{ p: 1, borderTop: '1px solid #eee', display: 'flex', justifyContent: 'flex-end' }}>
                                    <Typography variant="caption" sx={{ color: '#666' }}>
                                        Showing first 50 rows • Total: {totalCount}
                                    </Typography>
                                </Box>
                            </Box>
                        )}

                        {/* RELATIONSHIPS TAB */}
                        {activeTab === 2 && (
                            <Box sx={{ p: 3 }}>
                                <Stack direction="row" justifyContent="space-between" alignItems="center" sx={{ mb: 3 }}>
                                    <Typography variant="h6" color="primary" sx={{ fontWeight: 600 }}>
                                        Table Relationships ({relationships.length})
                                    </Typography>
                                    <ToggleButtonGroup value={relView} exclusive onChange={(_, v) => v && setRelView(v)} size="small">
                                        <ToggleButton value="table" sx={{ px: 2 }}><TableViewIcon fontSize="small" sx={{ mr: 1 }} /> Table View</ToggleButton>
                                        <ToggleButton value="graph" sx={{ px: 2 }}><AutoGraphIcon fontSize="small" sx={{ mr: 1 }} /> Graph View</ToggleButton>
                                    </ToggleButtonGroup>
                                </Stack>

                                {relationships.length > 0 ? (
                                    <TableContainer>
                                        <Table size="small">
                                            <TableHead>
                                                <TableRow>
                                                    <HeaderCell>Direction</HeaderCell>
                                                    <HeaderCell>From Table</HeaderCell>
                                                    <HeaderCell>From Column</HeaderCell>
                                                    <HeaderCell></HeaderCell>
                                                    <HeaderCell>To Table</HeaderCell>
                                                    <HeaderCell>To Column</HeaderCell>
                                                    <HeaderCell>Type</HeaderCell>
                                                </TableRow>
                                            </TableHead>
                                            <TableBody>
                                                {relationships.map((r, i) => (
                                                    <TableRow key={i} hover>
                                                        <Cell>
                                                            <Chip
                                                                label={r.direction}
                                                                size="small"
                                                                color={r.direction === 'outgoing' ? 'primary' : 'secondary'}
                                                                icon={r.direction === 'outgoing' ? <ArrowForwardIcon /> : <ArrowBackIcon />}
                                                                sx={{ fontSize: 10 }}
                                                            />
                                                        </Cell>
                                                        <Cell sx={{ color: '#1565c0', fontFamily: 'monospace' }}>{r.fromTable}</Cell>
                                                        <Cell sx={{ fontFamily: 'monospace' }}>{r.fromCol}</Cell>
                                                        <Cell sx={{ textAlign: 'center' }}>→</Cell>
                                                        <Cell sx={{ color: '#1565c0', fontFamily: 'monospace' }}>{r.toTable}</Cell>
                                                        <Cell sx={{ fontFamily: 'monospace' }}>{r.toCol}</Cell>
                                                        <Cell>{r.relationType}</Cell>
                                                    </TableRow>
                                                ))}
                                            </TableBody>
                                        </Table>
                                    </TableContainer>
                                ) : (
                                    <Box sx={{ textAlign: 'center', py: 6, color: '#888' }}>
                                        <AccountTreeIcon sx={{ fontSize: 48, mb: 2, opacity: 0.5 }} />
                                        <Typography variant="h6">No Foreign Keys</Typography>
                                        <Typography variant="body2">This table has no foreign key relationships</Typography>
                                    </Box>
                                )}
                            </Box>
                        )}

                        {/* SQL QUERY TAB */}
                        {activeTab === 3 && (
                            <Box sx={{ p: 3, display: 'flex', flexDirection: 'column', height: '100%' }}>
                                <Paper variant="outlined" sx={{ p: 1, mb: 2 }}>
                                    <Stack direction="row" spacing={1} sx={{ mb: 1, borderBottom: '1px solid #f0f0f0', pb: 1 }}>
                                        <IconButton size="small" onClick={executeSql} color="primary"><PlayArrowIcon /></IconButton>
                                        <IconButton size="small" onClick={() => { setSqlQuery(''); setSqlResults(null); }}><ClearIcon /></IconButton>
                                        <IconButton size="small"><FormatAlignLeftIcon /></IconButton>
                                        <IconButton size="small"><SaveIcon /></IconButton>
                                        <Box sx={{ flex: 1 }} />
                                        <Typography variant="caption" sx={{ color: '#888', pt: 0.5 }}>
                                            Ctrl+Enter (Execute) • SELECT queries only
                                        </Typography>
                                    </Stack>
                                    <TextField
                                        fullWidth multiline rows={6}
                                        placeholder="SELECT * FROM table_name LIMIT 100;"
                                        value={sqlQuery} onChange={e => setSqlQuery(e.target.value)}
                                        onKeyDown={(e) => { if (e.ctrlKey && e.key === 'Enter') executeSql(); }}
                                        sx={{
                                            '& textarea': { fontFamily: 'monospace', color: '#1565c0', fontSize: 13 },
                                            '& .MuiOutlinedInput-notchedOutline': { border: 'none' }
                                        }}
                                    />
                                </Paper>

                                {sqlResults ? (
                                    <Box sx={{ flex: 1, overflow: 'auto' }}>
                                        <Typography variant="body2" sx={{ mb: 1, color: '#666' }}>
                                            Results: {sqlResults.rows.length} rows
                                        </Typography>
                                        <TableContainer sx={{ maxHeight: '100%' }}>
                                            <Table size="small" stickyHeader>
                                                <TableHead>
                                                    <TableRow>
                                                        {sqlResults.columns.map((col) => (
                                                            <TableCell key={col} sx={{ fontWeight: 600, bgcolor: 'background.paper' }}>{col}</TableCell>
                                                        ))}
                                                    </TableRow>
                                                </TableHead>
                                                <TableBody>
                                                    {sqlResults.rows.map((row, i) => (
                                                        <TableRow key={i} hover>
                                                            {sqlResults.columns.map((col, j) => (
                                                                <TableCell key={j} sx={{ whiteSpace: 'nowrap' }}>{String(row[col])}</TableCell>
                                                            ))}
                                                        </TableRow>
                                                    ))}
                                                </TableBody>
                                            </Table>
                                        </TableContainer>
                                    </Box>
                                ) : (
                                    <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', flex: 1 }}>
                                        <TerminalIcon sx={{ fontSize: 48, color: '#999', mb: 2 }} />
                                        <Typography variant="h6" sx={{ color: '#666' }}>No query executed yet</Typography>
                                        <Typography variant="caption" sx={{ color: '#888' }}>Enter a SELECT query above and press Ctrl+Enter or click Execute</Typography>
                                    </Box>
                                )}
                            </Box>
                        )}

                        {/* DATABASE INFO TAB */}
                        {activeTab === 4 && (
                            <Box sx={{ p: 3 }}>
                                <Typography variant="h6" color="primary" sx={{ mb: 3, fontWeight: 600 }}>Database Information</Typography>
                                {databaseInfo ? (
                                    <Grid container spacing={3}>
                                        <InfoCard label="Database Type" value={databaseInfo.type} />
                                        <InfoCard label="Version" value={databaseInfo.version} />
                                        <InfoCard label="Database Path / Name" value={databaseInfo.name} />
                                        <InfoCard label="Host" value={databaseInfo.host} />
                                        <InfoCard label="Port" value={databaseInfo.port} />
                                        <InfoCard label="Total Tables" value={String(databaseInfo.tableCount)} />
                                    </Grid>
                                ) : (
                                    <Box sx={{ textAlign: 'center', py: 4 }}>
                                        <CircularProgress />
                                    </Box>
                                )}
                            </Box>
                        )}

                    </Box>
                </Paper>
            </Box>
        </Box>
    );
};

// Helper Components
const CustomTab = (props: any) => (
    <Tab {...props} iconPosition="start" sx={{ minHeight: 48, textTransform: 'uppercase', fontSize: 12, fontWeight: 600, color: '#666', '&.Mui-selected': { color: '#1565c0' } }} />
);

const HeaderCell = ({ children }: any) => <TableCell sx={{ color: '#1565c0', fontWeight: 600, borderBottom: '1px solid #e0e0e0', fontSize: 13 }}>{children}</TableCell>;
const Cell = ({ children, sx = {} }: any) => <TableCell sx={{ borderBottom: '1px solid #f0f0f0', fontSize: 13, py: 1.5, ...sx }}>{children}</TableCell>;
const InfoCard = ({ label, value }: any) => (
    <Grid size={{ xs: 12, md: 6 }}>
        <Paper variant="outlined" sx={{ p: 3 }}>
            <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>{label}</Typography>
            <Typography variant="h6" color="primary" sx={{ fontWeight: 600, wordBreak: 'break-all' }}>{value}</Typography>
        </Paper>
    </Grid>
);

export default DataOpsStudioPage;
