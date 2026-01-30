import React, { useState, useEffect } from "react";
import {
    Plus, Trash2, ChevronLeft, Search, XCircle
} from "lucide-react";
import { useNavigate, useParams, useSearchParams } from "react-router-dom";
import { salesService, SalesInvoiceLine } from "@services/salesService";
import { useAuthContext } from "@auth/auth.context";
import { TransactionToolbar, TransactionStatus } from "@ui/TransactionToolbar";
import { useGlobalLocation } from "@contexts/GlobalLocationContext";
import { CustomerLookupSidebar, CustomerLookupResult } from "@core/ui-canon/frontend/ui/components/CustomerLookupSidebar";
import { ProductLookupModal, ProductLookupResult } from "@core/ui-canon/frontend/ui/components/ProductLookupModal";

const InvoiceDetailPage: React.FC = () => {
    const navigate = useNavigate();
    const { user } = useAuthContext();
    const { currentLocationId, currentLocationName } = useGlobalLocation();
    const { id } = useParams();
    const isNew = !id || id === "new";

    // Form State
    const [header, setHeader] = useState({
        invoice_number: 'Draft',
        status: 'DRAFT',
        customer_name: '',
        customer_id: '',
        location: '',
        location_id: '',
        company_id: '',
        invoice_date: new Date().toISOString().split('T')[0],
        due_date: '',

        // Audit
        created_at: '',
        approved_by: '', // If validation/posting happens
    });

    const [lines, setLines] = useState<SalesInvoiceLine[]>([]);

    // UI State
    const [loading, setLoading] = useState(false);
    const [isCustomerLookupOpen, setIsCustomerLookupOpen] = useState(false);
    const [isProductLookupOpen, setIsProductLookupOpen] = useState(false);
    const [activeLineId, setActiveLineId] = useState<string | null>(null);

    const [searchParams] = useSearchParams();

    // 1. Load Defaults & Pre-fill from SO
    useEffect(() => {
        const loadDefaults = async () => {
            if (!user?.currentCompanyId) return;

            if (isNew) {
                // Base defaults
                setHeader(prev => ({
                    ...prev,
                    location: currentLocationName || '',
                    location_id: currentLocationId || '',
                    company_id: user.currentCompanyId || '',
                    invoice_number: 'NEW'
                }));

                const soId = searchParams.get('so_id');
                if (soId) {
                    try {
                        setLoading(true);
                        const order = await salesService.getOrder(soId);
                        setHeader(prev => ({
                            ...prev,
                            customer_id: order.customer,
                            customer_name: order.customer_name,
                            location_id: order.warehouse_location, // Use order location
                            // Override context location if order has specific one?
                            // For now keeping order location seems safer for fulfillment.
                            remarks: `Invoice for Order ${order.order_number}`
                        }));

                        setLines(order.lines.map((l: any) => ({
                            id: `temp-${Date.now()}-${l.id}`, // New temp IDs for invoice lines
                            item: l.item,
                            item_code: l.item_code,
                            item_name: l.item_name,
                            description: l.item_name,
                            quantity_invoiced: parseFloat(l.ordered_qty), // Default to full qty
                            unit_price_invoiced: parseFloat(l.unit_price),
                            line_total: parseFloat(l.ordered_qty) * parseFloat(l.unit_price)
                        })));
                    } catch (err) {
                        console.error("Failed to load source order", err);
                        alert("Failed to load source order details.");
                    } finally {
                        setLoading(false);
                    }
                } else if (lines.length === 0) {
                    addLine();
                }
            }
        };
        loadDefaults();
    }, [isNew, user, currentLocationId, currentLocationName, searchParams]);

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
            salesService.getInvoice(id)
                .then((data: any) => {
                    setHeader({
                        invoice_number: data.invoice_number,
                        status: data.invoice_status,
                        customer_name: data.customer_name || 'Customer',
                        customer_id: data.customer,
                        location: data.location_name || 'Location',
                        location_id: '', // Not strictly in Invoice model sometimes, but context is key
                        company_id: data.company,
                        invoice_date: data.invoice_date,
                        due_date: data.due_date,
                        created_at: data.created_at,
                        approved_by: ''
                    });
                    setLines(data.lines.map((l: any) => ({
                        id: l.id,
                        item: l.item,
                        item_code: l.item_code,
                        item_name: l.item_name,
                        description: l.description,
                        quantity_invoiced: parseFloat(l.quantity_invoiced),
                        unit_price_invoiced: parseFloat(l.unit_price_invoiced),
                        line_total: parseFloat(l.line_total || 0)
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
            description: '',
            quantity_invoiced: 1,
            unit_price_invoiced: 0,
            line_total: 0,
            item_code: '',
            item_name: ''
        }]);
    };

    const updateLine = (id: string, field: keyof SalesInvoiceLine, value: any) => {
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

    // 3. Selection Handlers
    const handleCustomerSelect = (customer: CustomerLookupResult) => {
        setHeader(prev => ({
            ...prev,
            customer_id: customer.id,
            customer_name: customer.customer_name
        }));
        setIsCustomerLookupOpen(false);
    };

    const handleProductSelect = (product: ProductLookupResult) => {
        if (activeLineId) {
            setLines(lines.map(line => {
                if (line.id === activeLineId) {
                    return {
                        ...line,
                        item: product.id,
                        item_code: product.item_code,
                        item_name: product.item_name,
                        unit_price_invoiced: product.retail_price || 0,
                        line_total: (line.quantity_invoiced || 1) * (product.retail_price || 0)
                    };
                }
                return line;
            }));
        }
        setIsProductLookupOpen(false);
        setActiveLineId(null);
    };

    const handleItemCodeKeyDown = (lineId: string, e: React.KeyboardEvent<HTMLInputElement>) => {
        if (e.key === 'Enter' || e.key === 'F12') {
            const line = lines.find(l => l.id === lineId);
            if (line && (!line.item_code || e.key === 'F12')) {
                e.preventDefault();
                setActiveLineId(lineId);
                setIsProductLookupOpen(true);
            }
        }
    };

    // Actions
    const handleSave = async () => {
        if (!header.customer_id) { alert("Customer is required."); return; }

        const payload = {
            company: header.company_id,
            customer: header.customer_id,
            invoice_date: header.invoice_date,
            due_date: header.due_date,
            invoice_status: (header.status === 'NEW' ? 'DRAFT' : header.status) as any,
            lines: lines.map(l => ({
                item: l.item,
                description: l.description,
                quantity_invoiced: l.quantity_invoiced,
                unit_price_invoiced: l.unit_price_invoiced,
                line_total: l.quantity_invoiced * l.unit_price_invoiced
            }))
        };

        try {
            setLoading(true);
            if (isNew) {
                const res = await salesService.createInvoice(payload);
                window.history.replaceState(null, '', `/sales/invoices/${res.id}`);
                navigate(`/sales/invoices/${res.id}`, { replace: true });
            } else {
                // Update technically not always allowed for posted invoices, but for draft yes
                // await salesService.updateInvoice(id, payload);
                alert("Update logic pending backend support.");
            }
        } catch (error) {
            console.error("Save failed", error);
            alert("Failed to save invoice.");
        } finally { setLoading(false); }
    };

    const handleToolbarAction = (action: string) => {
        switch (action) {
            case 'new': navigate('/sales/invoices/new'); break;
            case 'save': handleSave(); break;
            case 'cancel': navigate('/sales/invoices'); break;
            case 'exit': navigate('/sales/invoices'); break;
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
                                Sales Invoice <span className="text-[#0078d4] font-light ml-1">{header.invoice_number}</span>
                            </h1>
                            <span className={`ml-2 px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider 
                                ${header.status === 'PAID' ? 'bg-[#dff6dd] text-[#107c10]' :
                                    header.status === 'POSTED' ? 'bg-[#deecf9] text-[#0078d4]' :
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
                                    placeholder="Select Customer (Enter/Click)..."
                                    onClick={() => header.status === 'DRAFT' && setIsCustomerLookupOpen(true)}
                                    onKeyDown={(e) => {
                                        if (e.key === 'Enter' && header.status === 'DRAFT') {
                                            setIsCustomerLookupOpen(true);
                                        }
                                    }}
                                />
                                <Search size={14} className="text-gray-400" />
                            </div>
                        </div>
                        <div className="space-y-1">
                            <label className="text-xs font-semibold text-[#605e5c] uppercase">Location</label>
                            <input type="text" value={header.location} disabled className="w-full border-b border-[#e1dfdd] bg-gray-50 text-[#a19f9d] px-1 py-0.5" />
                        </div>
                        <div className="space-y-1">
                            <label className="text-xs font-semibold text-[#605e5c] uppercase">Invoice Date</label>
                            <input type="date" value={header.invoice_date} onChange={e => setHeader({ ...header, invoice_date: e.target.value })} className="w-full border-b border-[#8a8886] outline-none" disabled={header.status !== 'DRAFT'} />
                        </div>
                        <div className="space-y-1">
                            <label className="text-xs font-semibold text-[#605e5c] uppercase">Due Date</label>
                            <input type="date" value={header.due_date} onChange={e => setHeader({ ...header, due_date: e.target.value })} className="w-full border-b border-[#8a8886] outline-none" disabled={header.status !== 'DRAFT'} />
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
                                        <th className="p-3 border-l border-[#edebe9]">Description</th>
                                        <th className="p-3 w-24 text-right border-l border-[#edebe9]">Qty</th>
                                        <th className="p-3 w-24 text-right border-l border-[#edebe9]">Unit Price</th>
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
                                                    onKeyDown={(e) => handleItemCodeKeyDown(line.id!, e)}
                                                    placeholder="Enter or F12"
                                                />
                                            </td>
                                            <td className="p-0 border-l border-[#edebe9]">
                                                <input
                                                    type="text"
                                                    value={line.description || line.item_name || ''}
                                                    onChange={(e) => updateLine(line.id!, 'description', e.target.value)}
                                                    className="w-full p-3 outline-none bg-transparent"
                                                />
                                            </td>
                                            <td className="p-0 border-l border-[#edebe9]">
                                                <input
                                                    type="number"
                                                    value={line.quantity_invoiced}
                                                    onChange={(e) => updateLine(line.id!, 'quantity_invoiced', parseFloat(e.target.value))}
                                                    className="w-full p-3 text-right outline-none bg-transparent"
                                                />
                                            </td>
                                            <td className="p-0 border-l border-[#edebe9]">
                                                <input
                                                    type="number"
                                                    value={line.unit_price_invoiced}
                                                    onChange={(e) => updateLine(line.id!, 'unit_price_invoiced', parseFloat(e.target.value))}
                                                    className="w-full p-3 text-right outline-none bg-transparent"
                                                />
                                            </td>
                                            <td className="p-3 text-right border-l border-[#edebe9]">
                                                {(line.quantity_invoiced * line.unit_price_invoiced).toFixed(2)}
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
            <CustomerLookupSidebar
                isOpen={isCustomerLookupOpen}
                onClose={() => setIsCustomerLookupOpen(false)}
                onSelect={handleCustomerSelect}
                companyId={header.company_id}
            />

            <ProductLookupModal
                isOpen={isProductLookupOpen}
                onClose={() => setIsProductLookupOpen(false)}
                onSelect={handleProductSelect}
                companyId={header.company_id}
                mode="SALES"
            />
        </div>
    );
};

export default InvoiceDetailPage;

