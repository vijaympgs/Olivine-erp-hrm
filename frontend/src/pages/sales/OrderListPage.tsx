import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Loader2, AlertCircle } from "lucide-react";
import { salesService, SalesOrder } from "../../services/salesService";
import { MasterToolbar } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";

const OrderListPage: React.FC = () => {
    const navigate = useNavigate();
    const [orders, setOrders] = useState<SalesOrder[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const [selectedIds, setSelectedIds] = useState<string[]>([]);
    const [searchQuery, setSearchQuery] = useState('');

    const fetchOrders = async () => {
        setLoading(true);
        try {
            const data = await salesService.getOrders();
            if (Array.isArray(data)) {
                setOrders(data);
            } else if (data && data.results) {
                setOrders(data.results);
            } else {
                setOrders([]);
            }
        } catch (err) {
            console.error(err);
            setError("Failed to load orders");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchOrders();
    }, []);

    const handleDelete = async () => {
        if (!selectedIds.length) return;
        if (!window.confirm(`Delete ${selectedIds.length} order(s)?`)) return;

        setLoading(true);
        for (const id of selectedIds) {
            try {
                await salesService.deleteOrder(id);
            } catch (e) {
                console.error(`Failed to delete order ${id}`, e);
            }
        }
        setSelectedIds([]);
        fetchOrders();
    };

    const handleToolbarAction = (action: string) => {
        switch (action) {
            case 'new':
                navigate('/sales/orders/new');
                break;
            case 'refresh':
                fetchOrders();
                break;
            case 'delete':
                handleDelete();
                break;
            default:
                console.log(`Action ${action} handled by MasterToolbar but not locally mapped.`);
        }
    };

    const handleSelectAll = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.checked) setSelectedIds(orders.map(o => o.id));
        else setSelectedIds([]);
    };

    const handleSelectRow = (id: string) => {
        if (selectedIds.includes(id)) setSelectedIds(selectedIds.filter(i => i !== id));
        else setSelectedIds([...selectedIds, id]);
    };

    const getStatusColor = (status: string) => {
        switch (status) {
            case 'APPROVED':
            case 'CONFIRMED': return 'bg-[#dff6dd] text-[#107c10]';
            case 'PARTIALLY_SHIPPED':
            case 'PROCESSING': return 'bg-[#fff4ce] text-[#323130]';
            case 'FULLY_SHIPPED':
            case 'DELIVERED': return 'bg-[#dff6dd] text-[#107c10]';
            case 'CANCELLED': return 'bg-[#fde7e9] text-[#a4262c]';
            case 'DRAFT': return 'bg-[#deecf9] text-[#0078d4]';
            default: return 'bg-[#f3f2f1] text-[#201f1e]';
        }
    };

    // Filter orders based on search query
    const filteredOrders = orders.filter(o =>
        o.order_number?.toLowerCase().includes(searchQuery.toLowerCase()) ||
        o.customer_name?.toLowerCase().includes(searchQuery.toLowerCase())
    );

    return (
        <div className="flex flex-col h-full bg-[#faf9f8] text-sm text-[#201f1e]">
            {/* Master Toolbar */}
            <div className="shrink-0">
                <MasterToolbar
                    viewId="ORDERS"
                    mode="VIEW"
                    onAction={handleToolbarAction}
                    hasSelection={selectedIds.length > 0}
                    title="Sales Orders"
                    onSearch={(query: string) => setSearchQuery(query)}
                    showSearch={true}
                />
            </div>

            {/* Content */}
            <div className="flex-1 overflow-auto p-6">
                {loading ? (
                    <div className="flex items-center justify-center h-full text-[#605e5c]">
                        <Loader2 className="animate-spin mr-2" size={20} /> Loading orders...
                    </div>
                ) : error ? (
                    <div className="flex items-center justify-center h-full text-[#a4262c]">
                        <AlertCircle className="mr-2" size={20} /> {error}
                    </div>
                ) : (
                    <div className="bg-white border border-[#edebe9] shadow-sm rounded-sm overflow-hidden">
                        <table className="w-full border-collapse">
                            <thead className="bg-[#f3f2f1] text-[#323130]">
                                <tr className="text-xs uppercase tracking-wider text-left border-b border-[#edebe9]">
                                    <th className="p-2 w-10 text-center">
                                        <input
                                            type="checkbox"
                                            onChange={handleSelectAll}
                                            checked={orders.length > 0 && selectedIds.length === orders.length}
                                        />
                                    </th>
                                    <th className="p-2 w-40 border-l border-[#edebe9]">Order #</th>
                                    <th className="p-2 border-l border-[#edebe9]">Customer</th>
                                    <th className="p-2 w-32 border-l border-[#edebe9]">Date</th>
                                    <th className="p-2 w-32 border-l border-[#edebe9] text-right">Total</th>
                                    <th className="p-2 w-40 border-l border-[#edebe9] text-center">Status</th>
                                </tr>
                            </thead>
                            <tbody className="text-sm">
                                {filteredOrders.length === 0 ? (
                                    <tr>
                                        <td colSpan={6} className="p-8 text-center text-[#605e5c]">
                                            No orders found.
                                        </td>
                                    </tr>
                                ) : (
                                    filteredOrders.map((order) => (
                                        <tr key={order.id} className="border-b border-[#f3f2f1] hover:bg-[#f3f9ff] transition-colors">
                                            <td className="p-2 text-center">
                                                <input
                                                    type="checkbox"
                                                    checked={selectedIds.includes(order.id)}
                                                    onChange={() => handleSelectRow(order.id)}
                                                />
                                            </td>
                                            <td className="p-2 border-l border-[#edebe9] font-medium">
                                                <button
                                                    onClick={() => navigate(`/sales/orders/${order.id}`)}
                                                    className="text-[#0078d4] hover:underline"
                                                >
                                                    {order.order_number}
                                                </button>
                                            </td>
                                            <td className="p-2 border-l border-[#edebe9]">{order.customer_name || 'Unknown'}</td>
                                            <td className="p-2 border-l border-[#edebe9]">{order.order_date}</td>
                                            <td className="p-2 border-l border-[#edebe9] text-right font-medium">
                                                {order.grand_total?.toFixed(2)}
                                            </td>
                                            <td className="p-2 border-l border-[#edebe9] text-center">
                                                <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider ${getStatusColor(order.order_status)}`}>
                                                    {order.order_status}
                                                </span>
                                            </td>
                                        </tr>
                                    ))
                                )}
                            </tbody>
                        </table>
                    </div>
                )}
            </div>
        </div>
    );
};

export default OrderListPage;
