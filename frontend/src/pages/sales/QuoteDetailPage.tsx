import React, { useState, useEffect } from "react";
import {
    Plus, Trash2, ChevronLeft, Search, Loader2
} from "lucide-react";
import { useNavigate, useParams } from "react-router-dom";
import { salesService, SalesQuoteLine } from "@services/salesService";
import { useAuthContext } from "@auth/auth.context";
import { useGlobalLocation } from "@contexts/GlobalLocationContext";
import { MasterToolbar, MasterMode } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";

const QuoteDetailPage: React.FC = () => {
    const navigate = useNavigate();
    const { user } = useAuthContext();
    const { currentLocationId, currentLocationName } = useGlobalLocation();
    const { id } = useParams();
    const isNew = !id || id === "new";

    // Form State
    const [header, setHeader] = useState({
        quote_number: 'Draft',
        status: 'DRAFT',
        customer_name: '',
        customer_id: '',
        sales_person: '',
        sales_person_id: '',
        location: '',
        location_id: '',
        company_id: '',
        quote_date: new Date().toISOString().split('T')[0],
        valid_until: '',
        remarks: '',

        // Audit
        approved_by: '',
        approved_at: '',
        rejected_by: '',
        rejected_at: ''
    });

    const [lines, setLines] = useState<SalesQuoteLine[]>([]);

    // UI State
    const [loading, setLoading] = useState(false);
    const [isCustomerLookupOpen, setIsCustomerLookupOpen] = useState(false);
    const [isProductLookupOpen, setIsProductLookupOpen] = useState(false);
    const [activeLineId, setActiveLineId] = useState<string | null>(null);

    // 1. Load Dependencies & Defaults
    useEffect(() => {
        const loadDefaults = async () => {
            if (!user?.currentCompanyId) return;

            if (isNew) {
                setHeader(prev => ({
                    ...prev,
                    sales_person: user.name || '',
                    sales_person_id: user.id || '',
                    // Mandate Global Location Context
                    location: currentLocationName || '',
                    location_id: currentLocationId || '',
                    company_id: user.currentCompanyId || '',
                    quote_number: 'NEW'
                }));
                // Start with one empty line
                if (lines.length === 0) addLine();
            }
        };
        loadDefaults();
    }, [isNew, user, currentLocationId, currentLocationName]);

    // Update location context dynamically for new drafts
    useEffect(() => {
        if (isNew && currentLocationId) {
            setHeader(prev => ({
                ...prev,
                location: currentLocationName || '',
                location_id: currentLocationId || ''
            }));
        }
    }, [currentLocationId, currentLocationName, isNew]);

    // 2. Load Data if Editing
    useEffect(() => {
        if (!isNew && id) {
            setLoading(true);
            salesService.getQuote(id)
                .then((data: any) => {
                    setHeader({
                        quote_number: data.quote_number,
                        status: data.quote_status,
                        customer_name: data.customer_name || 'Customer',
                        customer_id: data.customer,
                        sales_person: data.sales_person_name || 'User',
                        sales_person_id: data.created_by,
                        location: data.location_name || 'Location',
                        location_id: data.location || '',
                        company_id: data.company,
                        quote_date: data.quote_date,
                        valid_until: data.valid_until_date || '',
                        remarks: data.remarks || '',
                        approved_by: data.approved_by_name,
                        approved_at: data.approved_at,
                        rejected_by: data.rejected_by_name,
                        rejected_at: data.rejected_at
                    });
                    setLines(data.lines.map((l: any) => ({
                        id: l.id,
                        item: l.item,
                        item_code: l.item_code,
                        item_name: l.item_name,
                        uom: l.uom,
                        uom_code: l.uom_code,
                        quantity: parseFloat(l.quantity),
                        unit_price: parseFloat(l.unit_price),
                        discount_percent: parseFloat(l.discount_percent || 0),
                        tax_percent: parseFloat(l.tax_percent || 0),
                        line_total: parseFloat(l.line_total || 0),
                        remarks: l.remarks
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
            uom: '',
            quantity: 1,
            unit_price: 0,
            discount_percent: 0,
            tax_percent: 0,
            item_code: '',
            item_name: ''
        }]);
    };

    const updateLine = (id: string, field: keyof SalesQuoteLine, value: any) => {
        setLines(lines.map(line => {
            if (line.id === id) {
                const updated = { ...line, [field]: value };
                return updated;
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
        if (!header.location_id) { alert("Location is required."); return; }
        if (!header.customer_id) { alert("Customer is required."); return; }

        const payload = {
            company: header.company_id,
            customer: header.customer_id,
            quote_date: header.quote_date,
            valid_until_date: header.valid_until,
            quote_status: (header.status === 'NEW' ? 'DRAFT' : header.status) as any,
            remarks: header.remarks,
            lines: lines.map(l => ({
                item: l.item,
                uom: l.uom,
                quantity: l.quantity,
                unit_price: l.unit_price,
                discount_percent: l.discount_percent,
                tax_percent: l.tax_percent,
                remarks: l.remarks
            }))
        };

        try {
            setLoading(true);
            if (isNew) {
                const res = await salesService.createQuote(payload);
                navigate(`/sales/quotes/${res.id}`, { replace: true });
            } else if (id) {
                await salesService.updateQuote(id, payload);
            }
        } catch (error) {
            console.error("Save failed", error);
            alert("Failed to save quote.");
        } finally { setLoading(false); }
    };

    const handleToolbarAction = (action: string) => {
        switch (action) {
            case 'save': handleSave(); break;
            case 'cancel':
            case 'exit':
            case 'back':
                navigate('/sales/quotes');
                break;
            case 'submit':
                if (id) salesService.submitQuote(id).then(() => window.location.reload());
                break;
            case 'lookup_item': setIsProductLookupOpen(true); break;
            case 'lookup_customer': setIsCustomerLookupOpen(true); break;
            default: console.log("Action:", action);
        }
    };

    const getToolbarMode = (): MasterMode => {
        if (isNew) return 'CREATE';
        if (header.status === 'DRAFT') return 'EDIT';
        return 'VIEW_FORM'; // Read Only for Approved/Submitted
    };

    const handleProductSelect = (product: any) => {
        if (activeLineId) {
            setLines(lines.map(line => line.id === activeLineId ? {
                ...line,
                item: product.id,
                item_code: product.item_code,
                item_name: product.item_name,
                uom: product.stock_uom_id || '',
                unit_price: product.standard_price || 0
            } : line));
        }
        setIsProductLookupOpen(false);
    };

    const getStatusColor = (status: string) => {
        switch (status) {
            case 'APPROVED': return 'bg-[#dff6dd] text-[#107c10]';
            case 'REJECTED': return 'bg-[#fde7e9] text-[#a4262c]';
            case 'SUBMITTED': return 'bg-[#fff4ce] text-[#323130]';
            case 'DRAFT': return 'bg-[#deecf9] text-[#0078d4]';
            default: return 'bg-[#f3f2f1] text-[#201f1e]';
        }
    };

    return (
        <div className="flex flex-col h-full bg-[#faf9f8] text-sm text-[#201f1e] overflow-hidden">
            {/* 1. Header with MasterToolbar */}
            <div className="bg-white border-b border-[#edebe9] shrink-0">
                <MasterToolbar
                    viewId="QUOTES"
                    mode={getToolbarMode()}
                    onAction={handleToolbarAction}
                    title={`Sales Quote ${isNew ? 'New' : header.quote_number}`}
                />

                {/* Status Strip (Optional) */}
                <div className="px-6 py-2 bg-[#f8f8f8] border-b border-[#edebe9] flex justify-between items-center">
                    <div className="flex items-center gap-3">
                        <button onClick={() => navigate('/sales/quotes')} className="p-1 hover:bg-[#e1dfdd] rounded-full transition-colors" title="Back">
                            <ChevronLeft size={16} className="text-[#605e5c]" />
                        </button>
                        <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider ${getStatusColor(header.status)}`}>
                            {header.status}
                        </span>
                    </div>
                </div>
            </div>

            {/* 2. Context Grid */}
            <div className="flex-1 overflow-auto">
                <div className="max-w-7xl mx-auto py-6 px-6">
                    {loading ? (
                        <div className="flex items-center justify-center p-12 text-[#605e5c]">
                            <Loader2 className="animate-spin mr-2" size={24} /> Loading...
                        </div>
                    ) : (
                        <>
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
                                    <label className="text-xs font-semibold text-[#605e5c] uppercase">Sales Person</label>
                                    <input type="text" value={header.sales_person} disabled className="w-full border-b border-[#e1dfdd] bg-gray-50 text-[#a19f9d] px-1 py-0.5" />
                                </div>
                                <div className="space-y-1">
                                    <label className="text-xs font-semibold text-[#605e5c] uppercase">Location</label>
                                    <input type="text" value={header.location} disabled className="w-full border-b border-[#e1dfdd] bg-gray-50 text-[#a19f9d] px-1 py-0.5" />
                                </div>
                                <div className="space-y-1">
                                    <label className="text-xs font-semibold text-[#605e5c] uppercase">Quote Date</label>
                                    <input type="date" value={header.quote_date} onChange={e => setHeader({ ...header, quote_date: e.target.value })} className="w-full border-b border-[#8a8886] outline-none" disabled={header.status !== 'DRAFT'} />
                                </div>
                            </div>

                            {/* 3. Lines Grid */}
                            <div className="bg-white border border-[#edebe9] shadow-sm rounded-sm p-6 mb-6">
                                <div className="flex items-center justify-between mb-4">
                                    <h3 className="font-semibold text-[#0078d4] flex items-center gap-2">
                                        <Plus size={18} /> Line Items
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
                                                <th className="p-3 w-28 text-right border-l border-[#edebe9]">Unit Price</th>
                                                <th className="p-3 w-28 text-right border-l border-[#edebe9]">Total</th>
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
                                                            disabled={header.status !== 'DRAFT'}
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
                                                            value={line.quantity}
                                                            onChange={(e) => updateLine(line.id!, 'quantity', parseFloat(e.target.value))}
                                                            className="w-full p-3 text-right outline-none bg-transparent"
                                                            disabled={header.status !== 'DRAFT'}
                                                        />
                                                    </td>
                                                    <td className="p-0 border-l border-[#edebe9]">
                                                        <input
                                                            type="number"
                                                            value={line.unit_price}
                                                            onChange={(e) => updateLine(line.id!, 'unit_price', parseFloat(e.target.value))}
                                                            className="w-full p-3 text-right outline-none bg-transparent"
                                                            disabled={header.status !== 'DRAFT'}
                                                        />
                                                    </td>
                                                    <td className="p-3 text-right border-l border-[#edebe9]">
                                                        {(line.quantity * line.unit_price).toFixed(2)}
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
                        </>
                    )}
                </div>
            </div>

            {/* Lookups */}
            {isCustomerLookupOpen && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
                    <div className="bg-white p-8 rounded shadow-lg text-center">
                        <h2 className="text-xl font-bold mb-4">Customer Select</h2>
                        <p className="mb-4">Customer Lookup Modal not yet implemented.</p>
                        <button onClick={() => setIsCustomerLookupOpen(false)} className="px-4 py-2 bg-blue-600 text-white rounded">Close</button>
                    </div>
                </div>
            )}
            {isProductLookupOpen && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
                    <div className="bg-white p-8 rounded shadow-lg text-center">
                        <h2 className="text-xl font-bold mb-4">Product Select</h2>
                        <p className="mb-4">Product Lookup Modal not yet implemented/imported.</p>
                        <button onClick={() => setIsProductLookupOpen(false)} className="px-4 py-2 bg-blue-600 text-white rounded">Close</button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default QuoteDetailPage;
