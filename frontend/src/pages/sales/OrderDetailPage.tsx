import React, { useState, useEffect } from "react";
import {
    Plus, Trash2, ChevronLeft, Search, Loader2
} from "lucide-react";
import { useNavigate, useParams } from "react-router-dom";
import { salesService, SalesOrderLine } from "@services/salesService";
import { useAuthContext } from "@auth/auth.context";
import { useGlobalLocation } from "@contexts/GlobalLocationContext";
import { MasterToolbar, MasterMode } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";
import { CustomerLookupSidebar, CustomerLookupResult } from "@core/ui-canon/frontend/ui/components/CustomerLookupSidebar";
import { ProductLookupModal, ProductLookupResult } from "@core/ui-canon/frontend/ui/components/ProductLookupModal";

const OrderDetailPage: React.FC = () => {
    const navigate = useNavigate();
    const { user } = useAuthContext();
    const { currentLocationId, currentLocationName } = useGlobalLocation();
    const { id } = useParams();
    const isNew = !id || id === "new";

    // Form State
    const [header, setHeader] = useState({
        order_number: 'Draft',
        status: 'DRAFT',
        customer_name: '',
        customer_id: '',
        sales_person: '',
        sales_person_id: '',
        location: '',
        location_id: '',
        company_id: '',
        order_date: new Date().toISOString().split('T')[0],
        required_delivery_date: '',
        remarks: '',

        // Audit
        approved_by: '',
        approved_at: '',
        rejected_by: '',
        rejected_at: ''
    });

    const [lines, setLines] = useState<SalesOrderLine[]>([]);

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
                    order_number: 'NEW'
                }));
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
            salesService.getOrder(id)
                .then((data: any) => {
                    setHeader({
                        order_number: data.order_number,
                        status: data.order_status,
                        customer_name: data.customer_name || 'Customer',
                        customer_id: data.customer,
                        sales_person: data.sales_person_name || 'User',
                        sales_person_id: data.created_by,
                        location: data.location_name || 'Location',
                        location_id: data.warehouse_location || '', // Note: warehouse_location from backend
                        company_id: data.company,
                        order_date: data.order_date,
                        required_delivery_date: data.required_delivery_date || '',
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
                        ordered_qty: parseFloat(l.ordered_qty),
                        unit_price: parseFloat(l.unit_price),
                        discount_percent: parseFloat(l.discount_percent || 0),
                        tax_percent: parseFloat(l.tax_percent || 0),
                        line_total: parseFloat(l.line_total || 0),
                        warehouse_location: l.warehouse_location
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
            ordered_qty: 1,
            unit_price: 0,
            discount_percent: 0,
            tax_percent: 0,
            item_code: '',
            item_name: ''
        }]);
    };

    const updateLine = (id: string, field: keyof SalesOrderLine | 'qty', value: any) => {
        setLines(lines.map(line => {
            if (line.id === id) {
                const key = field === 'qty' ? 'ordered_qty' : field;
                return { ...line, [key]: value };
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
                        uom: String(product.uom_id),
                        uom_code: product.stock_uom,
                        unit_price: product.retail_price || 0
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
        if (!header.location_id) { alert("Location is required."); return; }
        if (!header.customer_id) { alert("Customer is required."); return; }

        const payload = {
            company: header.company_id,
            warehouse_location: header.location_id,
            customer: header.customer_id,
            order_date: header.order_date,
            required_delivery_date: header.required_delivery_date,
            order_status: (header.status === 'NEW' ? 'DRAFT' : header.status) as any,
            remarks: header.remarks,
            lines: lines.map(l => ({
                item: l.item,
                uom: l.uom,
                ordered_qty: l.ordered_qty,
                unit_price: l.unit_price,
                discount_percent: l.discount_percent,
                tax_percent: l.tax_percent
            }))
        };

        try {
            setLoading(true);
            if (isNew) {
                const res = await salesService.createOrder(payload);
                navigate(`/sales/orders/${res.id}`, { replace: true });
            } else if (id) {
                await salesService.updateOrder(id, payload);
            }
        } catch (error) {
            console.error("Save failed", error);
            alert("Failed to save order.");
        } finally { setLoading(false); }
    };

    const handleNavigate = async (direction: 'next' | 'prev' | 'first' | 'last') => {
        try {
            // Fetch simplified list for navigation (assuming default sort order)
            // TODO: respecting current list filters would require context/store
            const response = await salesService.getOrders({ limit: 1000 });
            const orders = response.results || response; // Handle paginated or flat response

            if (isNew) return;

            const currentIndex = orders.findIndex((o: any) => o.id === id);
            if (currentIndex === -1) return;

            let nextIndex = currentIndex;
            if (direction === 'next') nextIndex = currentIndex + 1;
            if (direction === 'prev') nextIndex = currentIndex - 1;
            if (direction === 'first') nextIndex = 0;
            if (direction === 'last') nextIndex = orders.length - 1;

            if (nextIndex >= 0 && nextIndex < orders.length) {
                navigate(`/sales/orders/${orders[nextIndex].id}`);
            }
        } catch (e) {
            console.error("Navigation failed", e);
        }
    };

    const handleToolbarAction = (action: string) => {
        switch (action) {
            case 'save': handleSave(); break;
            case 'cancel':
                if (['CONFIRMED', 'APPROVED'].includes(header.status)) {
                    if (confirm('Are you sure you want to CANCEL this order? This action cannot be undone.')) {
                        const payload = { ...header, status: 'CANCELLED' };
                        // We need to send the full payload as per updateOrder expectation usually
                        const fullPayload = {
                            company: header.company_id,
                            warehouse_location: header.location_id,
                            customer: header.customer_id,
                            order_date: header.order_date,
                            required_delivery_date: header.required_delivery_date,
                            order_status: 'CANCELLED' as any,
                            remarks: header.remarks,
                            lines: lines.map(l => ({
                                item: l.item,
                                uom: l.uom,
                                ordered_qty: l.ordered_qty,
                                unit_price: l.unit_price,
                                discount_percent: l.discount_percent,
                                tax_percent: l.tax_percent
                            }))
                        };

                        if (id) salesService.updateOrder(id, fullPayload).then(() => window.location.reload());
                    }
                } else {
                    navigate('/sales/orders');
                }
                break;
            case 'exit':
            case 'back':
                navigate('/sales/orders');
                break;
            case 'submit':
                // Submit logic implies moving to non-draft state (e.g. PROCESSING or CONFIRMED depending on workflow)
                // Assuming 'submit' triggers validation and status update
                if (id) salesService.submitOrder(id).then(() => window.location.reload());
                break;
            case 'authorize':
                if (confirm('Authorize this order? This will lock the order.')) {
                    // Assuming authorize endpoint or update status
                    // For now, mocking update to CONFIRMED
                    const payload = { ...header, status: 'CONFIRMED' };
                    // Construct full payload properly
                    const fullPayload = {
                        company: header.company_id,
                        warehouse_location: header.location_id,
                        customer: header.customer_id,
                        order_date: header.order_date,
                        required_delivery_date: header.required_delivery_date,
                        order_status: 'CONFIRMED' as any,
                        remarks: header.remarks,
                        lines: lines.map(l => ({
                            item: l.item,
                            uom: l.uom,
                            ordered_qty: l.ordered_qty,
                            unit_price: l.unit_price,
                            discount_percent: l.discount_percent,
                            tax_percent: l.tax_percent
                        }))
                    };
                    if (id) salesService.updateOrder(id, fullPayload).then(() => window.location.reload());
                }
                break;
            case 'create_invoice':
                navigate(`/sales/invoices/new?so_id=${id}`);
                break;
            case 'lookup_item': setIsProductLookupOpen(true); break;
            case 'lookup_customer': setIsCustomerLookupOpen(true); break;
            case 'print': alert("Print Preview"); break;
            case 'email': alert("Email Service"); break;

            // Navigation
            case 'next': handleNavigate('next'); break;
            case 'previous': handleNavigate('prev'); break;
            case 'first': handleNavigate('first'); break;
            case 'last': handleNavigate('last'); break;
            default: console.log("Action:", action);
        }
    };

    const getToolbarMode = (): MasterMode => {
        if (isNew) return 'CREATE';
        if (header.status === 'DRAFT') return 'EDIT';
        return 'VIEW_FORM';
    };

    const getAllowedActions = () => {
        const base = ['exit', 'print', 'email', 'first', 'previous', 'next', 'last'];
        if (isNew) return ['save', 'cancel', ...base];
        if (header.status === 'DRAFT') return ['save', 'cancel', 'delete', 'authorize', ...base]; // Draft
        if (['CONFIRMED', 'APPROVED'].includes(header.status)) return ['create_invoice', 'print', 'email', 'cancel', 'first', 'previous', 'next', 'last', 'exit']; // Locked
        return base;
    };

    const headerStatusColor = (status: string) => {
        switch (status) {
            case 'APPROVED':
            case 'CONFIRMED': return 'bg-[#dff6dd] text-[#107c10]';
            case 'REJECTED': return 'bg-[#fde7e9] text-[#a4262c]';
            case 'PARTIALLY_SHIPPED':
            case 'PROCESSING': return 'bg-[#fff4ce] text-[#323130]';
            case 'DRAFT': return 'bg-[#deecf9] text-[#0078d4]';
            default: return 'bg-[#f3f2f1] text-[#201f1e]';
        }
    };

    return (
        <div className="flex flex-col h-full bg-[#faf9f8] text-sm text-[#201f1e] overflow-hidden">
            {/* 1. Header with MasterToolbar */}
            <div className="bg-white border-b border-[#edebe9] shrink-0">
                <MasterToolbar
                    viewId="ORDERS"
                    mode={getToolbarMode()}
                    onAction={handleToolbarAction}
                    title={`Sales Order ${isNew ? 'New' : header.order_number}`}
                    allowedActions={getAllowedActions()}
                />

                {/* Status Strip */}
                <div className="px-6 py-2 bg-[#f8f8f8] border-b border-[#edebe9] flex justify-between items-center">
                    <div className="flex items-center gap-3">
                        <button onClick={() => navigate('/sales/orders')} className="p-1 hover:bg-[#e1dfdd] rounded-full transition-colors" title="Back">
                            <ChevronLeft size={16} className="text-[#605e5c]" />
                        </button>
                        <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider ${headerStatusColor(header.status)}`}>
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
                                    <label className="text-xs font-semibold text-[#605e5c] uppercase">Sales Person</label>
                                    <input type="text" value={header.sales_person} disabled className="w-full border-b border-[#e1dfdd] bg-gray-50 text-[#a19f9d] px-1 py-0.5" />
                                </div>
                                <div className="space-y-1">
                                    <label className="text-xs font-semibold text-[#605e5c] uppercase">Location</label>
                                    <input type="text" value={header.location} disabled className="w-full border-b border-[#e1dfdd] bg-gray-50 text-[#a19f9d] px-1 py-0.5" />
                                </div>
                                <div className="space-y-1">
                                    <label className="text-xs font-semibold text-[#605e5c] uppercase">Order Date</label>
                                    <input type="date" value={header.order_date} onChange={e => setHeader({ ...header, order_date: e.target.value })} className="w-full border-b border-[#8a8886] outline-none" disabled={header.status !== 'DRAFT'} />
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
                                                            onKeyDown={(e) => handleItemCodeKeyDown(line.id!, e)}
                                                            placeholder="Enter or F12"
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
                                                            value={line.ordered_qty}
                                                            onChange={(e) => updateLine(line.id!, 'ordered_qty', parseFloat(e.target.value))}
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
                                                        {(line.ordered_qty * line.unit_price).toFixed(2)}
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

export default OrderDetailPage;
