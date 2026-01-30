import React, { useState, useEffect } from "react";
import {
    Plus, Trash2, ChevronLeft, Search, XCircle
} from "lucide-react";
import { useNavigate, useParams } from "react-router-dom";
import { salesService, SalesReturnLine, ReturnStatus } from "@services/salesService";
import { useAuthContext } from "@auth/auth.context";
import { TransactionToolbar, TransactionStatus } from "@ui/TransactionToolbar";
import { useGlobalLocation } from "@contexts/GlobalLocationContext";

const ReturnDetailPage: React.FC = () => {
    const navigate = useNavigate();
    const { user } = useAuthContext();
    const { currentLocationId, currentLocationName } = useGlobalLocation();
    const { id } = useParams();
    const isNew = !id || id === "new";

    // Form State
    const [header, setHeader] = useState({
        rma_number: 'Draft',
        status: 'DRAFT',
        customer_name: '',
        customer_id: '',
        location: '',
        location_id: '',
        company_id: '',
        return_date: new Date().toISOString().split('T')[0],
        return_type: 'RMA',
        original_order: '', // Reference
        remarks: '',

        // Audit
        approved_by: '',
        approved_at: ''
    });

    // Local Type extending Service Type to include UI helpers if needed
    // But better to stick to Service Type + explicit UI handling
    const [lines, setLines] = useState<SalesReturnLine[]>([]);

    // UI State
    const [loading, setLoading] = useState(false);
    const [isCustomerLookupOpen, setIsCustomerLookupOpen] = useState(false);
    const [isProductLookupOpen, setIsProductLookupOpen] = useState(false);
    const [activeLineId, setActiveLineId] = useState<string | null>(null);

    // 1. Load Defaults
    useEffect(() => {
        const loadDefaults = async () => {
            if (!user?.currentCompanyId) return;

            if (isNew) {
                setHeader(prev => ({
                    ...prev,
                    location: currentLocationName || '',
                    location_id: currentLocationId || '',
                    company_id: user.currentCompanyId || '',
                    rma_number: 'NEW'
                }));
                if (lines.length === 0) addLine();
            }
        };
        loadDefaults();
    }, [isNew, user, currentLocationId, currentLocationName]);

    // Update location
    useEffect(() => {
        if (isNew && currentLocationId) {
            setHeader(prev => ({
                ...prev,
                location: currentLocationName || '',
                location_id: currentLocationId || ''
            }));
        }
    }, [currentLocationId, currentLocationName, isNew]);

    // 2. Load Data
    useEffect(() => {
        if (!isNew && id) {
            setLoading(true);
            salesService.getReturn(id)
                .then((data: any) => {
                    setHeader({
                        rma_number: data.rma_number,
                        status: data.return_status,
                        customer_name: data.customer_name || 'Customer',
                        customer_id: data.customer,
                        location: data.location_name || 'Location',
                        location_id: data.location_id || '',
                        company_id: data.company,
                        return_date: data.created_at || new Date().toISOString().split('T')[0], // API mismatch? Using created_at or need specific field? Service has no return_date
                        return_type: data.return_type || 'RMA',
                        original_order: data.original_order || '', // Service doesn't explicitly show this field, might be in 'remarks' or 'details'? 
                        remarks: data.remarks || '',
                        approved_by: data.approved_by_name,
                        approved_at: data.approved_at
                    });
                    setLines(data.lines.map((l: any) => ({
                        id: l.id,
                        item: l.item,
                        item_code: l.item_code,
                        item_name: l.item_name,
                        return_qty_requested: parseFloat(l.return_qty_requested),
                        reason_code: l.reason_code,
                        return_disposition: l.return_disposition
                    })));
                })
                .catch(err => console.error(err))
                .finally(() => setLoading(false));
        }
    }, [id, isNew]);

    const addLine = () => {
        const newId = `temp-${Date.now()}`;
        setLines([...lines, {
            id: newId,
            item: '',
            return_qty_requested: 1,
            reason_code: 'DAMAGED',
            item_code: '',
            item_name: ''
        }]);
    };

    const updateLine = (id: string, field: keyof SalesReturnLine, value: any) => {
        setLines(lines.map(line => {
            if (line.id === id) {
                return { ...line, [field]: value };
            }
            return line;
        }));
    };

    const removeLine = (id: string) => {
        if (lines.length > 1) {
            setLines(lines.filter(line => line.id !== id));
        }
    };

    // Actions
    const handleSave = async () => {
        if (!header.customer_id) { alert("Customer is required."); return; }

        const payload = {
            company: header.company_id,
            customer: header.customer_id,
            rma_number: header.rma_number, // Backend auto-generates often, but if partial...
            return_status: (header.status === 'NEW' ? 'DRAFT' : header.status) as ReturnStatus,
            return_type: header.return_type,
            lines: lines.map(l => ({
                item: l.item,
                return_qty_requested: l.return_qty_requested,
                reason_code: l.reason_code,
                return_disposition: l.return_disposition
            }))
        };

        try {
            setLoading(true);
            if (isNew) {
                const res = await salesService.createReturn(payload);
                window.history.replaceState(null, '', `/sales/returns/${res.id}`);
                navigate(`/sales/returns/${res.id}`, { replace: true });
            } else if (id) {
                await salesService.updateReturn(id, payload);
            }
        } catch (error) {
            console.error("Save failed", error);
            alert("Failed to save return.");
        } finally { setLoading(false); }
    };

    const handleToolbarAction = (action: string) => {
        switch (action) {
            case 'new': navigate('/sales/returns/new'); break;
            case 'save': handleSave(); break;
            case 'cancel': navigate('/sales/returns'); break;
            case 'exit': navigate('/sales/returns'); break;
            case 'lookup_item': setIsProductLookupOpen(true); break;
            case 'lookup_customer': setIsCustomerLookupOpen(true); break;
            default: console.log("Action:", action);
        }
    };

    return (
        <div className="flex flex-col h-full bg-[#faf9f8] text-sm text-[#201f1e] overflow-hidden">
            {/* 1. Header with TransactionToolbar */}
            <div className="bg-white border-b border-[#edebe9] shrink-0">
                <TransactionToolbar
                    status={header.status as TransactionStatus}
                    onAction={handleToolbarAction}
                />
                <div className="px-6 py-4">
                    <div className="flex justify-between items-center mb-1">
                        <div className="flex items-center gap-3">
                            <button onClick={() => navigate(-1)} className="p-1 hover:bg-[#f3f2f1] rounded-full transition-colors">
                                <ChevronLeft size={20} className="text-[#605e5c]" />
                            </button>
                            <h1 className="text-xl font-semibold text-[#201f1e]">
                                Sales Return (RMA) <span className="text-[#0078d4] font-light ml-1">{header.rma_number}</span>
                            </h1>
                            <span className={`ml-2 px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider 
                                ${header.status === 'APPROVED' ? 'bg-[#dff6dd] text-[#107c10]' :
                                    header.status === 'RECEIVED' ? 'bg-[#deecf9] text-[#0078d4]' :
                                        'bg-[#f3f2f1] text-[#605e5c]'}`}>
                                {header.status}
                            </span>
                        </div>
                    </div>
                </div>
            </div>

            {/* 2. Context Grid */}
            <div className="flex-1 overflow-auto">
                <div className="max-w-7xl mx-auto py-6 px-6">
                    <div className="grid grid-cols-4 gap-6 bg-white p-6 border border-[#edebe9] shadow-sm rounded-sm mb-6">
                        <div className="space-y-1">
                            <label className="text-xs font-semibold text-[#605e5c] uppercase">Customer</label>
                            <div className="flex items-center border-b border-[#8a8886]">
                                <input
                                    type="text"
                                    value={header.customer_name}
                                    readOnly
                                    className="w-full py-0.5 outline-none cursor-pointer hover:text-blue-600 bg-transparent"
                                    placeholder="Select Customer..."
                                    onClick={() => header.status === 'DRAFT' && setIsCustomerLookupOpen(true)}
                                />
                                <Search size={14} className="text-gray-400" />
                            </div>
                        </div>
                        <div className="space-y-1">
                            <label className="text-xs font-semibold text-[#605e5c] uppercase">Receiving Location</label>
                            <input type="text" value={header.location} disabled className="w-full border-b border-[#e1dfdd] bg-gray-50 text-[#a19f9d] px-1 py-0.5" />
                        </div>
                        <div className="space-y-1">
                            <label className="text-xs font-semibold text-[#605e5c] uppercase">Date</label>
                            <input type="date" value={header.return_date} onChange={e => setHeader({ ...header, return_date: e.target.value })} className="w-full border-b border-[#8a8886] outline-none" disabled={header.status !== 'DRAFT'} />
                        </div>
                        <div className="space-y-1">
                            <label className="text-xs font-semibold text-[#605e5c] uppercase">Reference</label>
                            <input type="text" value={header.original_order} onChange={e => setHeader({ ...header, original_order: e.target.value })} className="w-full border-b border-[#8a8886] outline-none" placeholder="Original Order #" disabled={header.status !== 'DRAFT'} />
                        </div>
                    </div>

                    {/* 3. Lines Grid */}
                    <div className="bg-white border border-[#edebe9] shadow-sm rounded-sm p-6 mb-6">
                        <div className="flex items-center justify-between mb-4">
                            <h3 className="font-semibold text-[#0078d4] flex items-center gap-2">
                                <Plus size={18} /> Return Items
                            </h3>
                            {header.status === 'DRAFT' && (
                                <button onClick={addLine} className="text-xs font-bold uppercase tracking-wide text-[#0078d4] hover:underline flex items-center gap-1">
                                    <Plus size={14} /> Add Item
                                </button>
                            )}
                        </div>
                        <div className="border border-[#edebe9] rounded-sm overflow-hidden">
                            <table className="w-full border-collapse">
                                <thead className="bg-[#f3f2f1] text-[#323130]">
                                    <tr className="text-xs uppercase tracking-wider text-left border-b border-[#edebe9]">
                                        <th className="p-3 w-12 text-center">#</th>
                                        <th className="p-3 w-32 border-l border-[#edebe9]">SKU</th>
                                        <th className="p-3 border-l border-[#edebe9]">Product Name</th>
                                        <th className="p-3 w-24 text-right border-l border-[#edebe9]">Qty</th>
                                        <th className="p-3 w-40 text-left border-l border-[#edebe9]">Reason</th>
                                        <th className="p-3 w-12 text-center border-l border-[#edebe9]"></th>
                                    </tr>
                                </thead>
                                <tbody className="text-sm">
                                    {lines.map((line, index) => (
                                        <tr key={line.id} className="border-b border-[#f3f2f1] hover:bg-[#f3f9ff] transition-colors">
                                            <td className="p-3 text-center text-[#a19f9d]">{index + 1}</td>
                                            <td className="p-0 border-l border-[#edebe9]">
                                                <input
                                                    type="text"
                                                    value={line.item_code || ''}
                                                    readOnly
                                                    className="w-full p-3 outline-none cursor-pointer text-[#0078d4]"
                                                    onClick={() => { setActiveLineId(line.id!); setIsProductLookupOpen(true); }}
                                                    placeholder="Select..."
                                                />
                                            </td>
                                            <td className="p-0 border-l border-[#edebe9]">
                                                <input
                                                    type="text"
                                                    value={line.item_name || ''}
                                                    readOnly
                                                    className="w-full p-3 outline-none bg-transparent"
                                                />
                                            </td>
                                            <td className="p-0 border-l border-[#edebe9]">
                                                <input
                                                    type="number"
                                                    value={line.return_qty_requested}
                                                    onChange={(e) => updateLine(line.id!, 'return_qty_requested', parseFloat(e.target.value))}
                                                    className="w-full p-3 text-right outline-none bg-transparent"
                                                />
                                            </td>
                                            <td className="p-0 border-l border-[#edebe9]">
                                                <select
                                                    value={line.reason_code}
                                                    onChange={(e) => updateLine(line.id!, 'reason_code', e.target.value)}
                                                    className="w-full p-3 outline-none bg-transparent"
                                                >
                                                    <option value="DAMAGED">Damaged</option>
                                                    <option value="DEFECTIVE">Defective</option>
                                                    <option value="WRONG_ITEM">Wrong Item</option>
                                                    <option value="OTHER">Other</option>
                                                </select>
                                            </td>
                                            <td className="p-3 text-center border-l border-[#edebe9]">
                                                {header.status === 'DRAFT' && lines.length > 1 && (
                                                    <button onClick={() => removeLine(line.id!)} className="text-[#a19f9d] hover:text-[#a4262c]">
                                                        <Trash2 size={16} />
                                                    </button>
                                                )}
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>

            {/* Lookups */}
            {isCustomerLookupOpen && <div className="hidden">Customer Lookup Mock</div>}
            {isProductLookupOpen && <div className="hidden">Product Lookup Mock</div>}
        </div>
    );
};

export default ReturnDetailPage;

