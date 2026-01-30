import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Plus, RefreshCw, Search, Download } from "lucide-react";
import { salesService, SalesReturn } from "@services/salesService";
import { useAuthContext } from "@auth/auth.context";

const ReturnListPage: React.FC = () => {
    const navigate = useNavigate();
    const { user } = useAuthContext();
    const [returns, setReturns] = useState<SalesReturn[]>([]);
    const [loading, setLoading] = useState(false);

    const fetchReturns = async () => {
        try {
            setLoading(true);
            const data = await salesService.getReturns();
            setReturns(Array.isArray(data) ? data : data.results || []);
        } catch (error) {
            console.error("Failed to fetch returns", error);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        if (user?.currentCompanyId) {
            fetchReturns();
        }
    }, [user?.currentCompanyId]);

    const getStatusColor = (status: string) => {
        switch (status) {
            case "REQUESTED": return "bg-yellow-100 text-yellow-700";
            case "APPROVED": return "bg-blue-100 text-blue-700";
            case "RECEIVED": return "bg-purple-100 text-purple-700";
            case "REFUNDED": return "bg-green-100 text-green-700";
            case "REJECTED": return "bg-red-100 text-red-700";
            case "DRAFT": return "bg-gray-100 text-gray-700";
            default: return "bg-gray-100 text-gray-700";
        }
    };

    return (
        <div className="flex flex-col h-full bg-white">
            {/* Page Title */}
            <div className="px-6 py-3 border-b border-[#edebe9] bg-white">
                <h1 className="text-xl font-semibold text-[#201f1e]">Returns & Refunds</h1>
            </div>

            {/* Command Bar */}
            <div className="flex items-center px-4 py-2 border-b border-[#edebe9] bg-white gap-2">
                <button
                    onClick={() => navigate('/sales/returns/new')}
                    className="flex items-center gap-2 px-3 py-1.5 bg-[#0078d4] text-white font-medium hover:bg-[#106ebe] transition-colors rounded-sm"
                >
                    <Plus size={16} /> Request Return
                </button>
                <div className="h-6 w-px bg-gray-300 mx-2"></div>
                <button
                    onClick={fetchReturns}
                    className="flex items-center gap-2 px-3 py-1.5 bg-[#f3f2f1] text-[#323130] font-medium hover:bg-[#edebe9] transition-colors rounded-sm"
                >
                    <RefreshCw size={16} /> Refresh
                </button>
                <button className="flex items-center gap-2 px-3 py-1.5 bg-[#f3f2f1] text-[#323130] font-medium hover:bg-[#edebe9] transition-colors rounded-sm">
                    <Download size={16} /> Export
                </button>
            </div>

            {/* Grid Header */}
            <div className="flex-1 overflow-auto">
                {loading ? (
                    <div className="p-10 text-center text-gray-500">Loading returns...</div>
                ) : (
                    <table className="w-full border-collapse">
                        <thead className="bg-[#f3f2f1] sticky top-0 z-10">
                            <tr className="text-left text-xs font-semibold text-[#605e5c] uppercase tracking-wider">
                                <th className="p-3 w-10 border-b border-[#edebe9] text-center">
                                    <input type="checkbox" />
                                </th>
                                <th className="p-3 border-b border-[#edebe9] w-40">Return #</th>
                                <th className="p-3 border-b border-[#edebe9]">Customer</th>
                                <th className="p-3 border-b border-[#edebe9] w-32">Type</th>
                                <th className="p-3 border-b border-[#edebe9] w-32">Status</th>
                            </tr>
                        </thead>
                        <tbody className="text-sm text-[#201f1e]">
                            {returns.map((ret) => (
                                <tr
                                    key={ret.id}
                                    onClick={() => navigate(`/sales/returns/${ret.id}`)}
                                    className="border-b border-[#edebe9] hover:bg-[#f3f9ff] cursor-pointer transition-colors"
                                >
                                    <td className="p-3 text-center" onClick={(e) => e.stopPropagation()}>
                                        <input type="checkbox" />
                                    </td>
                                    <td className="p-3 text-[#0078d4] font-semibold hover:underline">{ret.rma_number}</td>
                                    <td className="p-3 font-medium">{ret.customer_name || 'Unknown'}</td>
                                    <td className="p-3 text-[#605e5c]">{ret.return_type || 'RMA'}</td>
                                    <td className="p-3">
                                        <span className={`px-2 py-1 rounded-full text-xs font-semibold ${getStatusColor(ret.return_status)}`}>
                                            {ret.return_status}
                                        </span>
                                    </td>
                                </tr>
                            ))}
                            {returns.length === 0 && (
                                <tr>
                                    <td colSpan={5} className="p-8 text-center text-gray-500 italic">No returns found.</td>
                                </tr>
                            )}
                        </tbody>
                    </table>
                )}
            </div>
        </div>
    );
};

export default ReturnListPage;

