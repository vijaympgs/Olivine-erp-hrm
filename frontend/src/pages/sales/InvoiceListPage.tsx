import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { RefreshCw, Search, Download } from "lucide-react";

interface InvoiceSummary {
    id: string;
    invoice_number: string;
    customer: string;
    date: string;
    due_date: string;
    status: "Draft" | "Posted" | "Partially Paid" | "Fully Paid" | "Cancelled";
    total: number;
}

const InvoiceListPage: React.FC = () => {
    const navigate = useNavigate();
    // Mock Data
    const [invoices] = useState<InvoiceSummary[]>([
        { id: '1', invoice_number: 'INV-2025-0501', customer: 'Globex Inc', date: '2025-12-19', due_date: '2026-01-19', status: 'Posted', total: 5400.00 },
        { id: '2', invoice_number: 'INV-2025-0502', customer: 'Soylent Corp', date: '2025-12-18', due_date: '2026-01-18', status: 'Fully Paid', total: 1250.50 },
    ]);

    const getStatusColor = (status: string) => {
        switch (status) {
            case "Draft": return "bg-gray-100 text-gray-700";
            case "Posted": return "bg-blue-100 text-blue-700";
            case "Partially Paid": return "bg-yellow-100 text-yellow-700";
            case "Fully Paid": return "bg-green-100 text-green-700";
            case "Cancelled": return "bg-red-100 text-red-700";
            default: return "bg-gray-100 text-gray-700";
        }
    };

    return (
        <div className="flex flex-col h-full bg-white">
            {/* Page Title */}
            <div className="px-6 py-3 border-b border-[#edebe9] bg-white">
                <h1 className="text-xl font-semibold text-[#201f1e]">Invoices</h1>
            </div>

            {/* Command Bar */}
            <div className="flex items-center px-4 py-2 border-b border-[#edebe9] bg-white gap-2">
                <button className="flex items-center gap-2 px-3 py-1.5 bg-[#f3f2f1] text-[#323130] font-medium hover:bg-[#edebe9] transition-colors rounded-sm">
                    <Download size={16} /> Export
                </button>
                <div className="h-6 w-px bg-gray-300 mx-2"></div>
                <button className="flex items-center gap-2 px-3 py-1.5 text-[#323130] hover:bg-[#f3f2f1] transition-colors rounded-sm">
                    <RefreshCw size={16} /> Refresh
                </button>
                <div className="flex-1"></div>
                <div className="flex items-center gap-2 border border-[#8a8886] px-2 py-1 rounded-sm w-64">
                    <Search size={14} className="text-[#605e5c]" />
                    <input type="text" placeholder="Search invoices..." className="border-none outline-none text-sm w-full" />
                </div>
            </div>

            {/* Grid Header */}
            <div className="flex-1 overflow-auto">
                <table className="w-full border-collapse">
                    <thead className="bg-[#f3f2f1] sticky top-0 z-10">
                        <tr className="text-left text-xs font-semibold text-[#605e5c] uppercase tracking-wider">
                            <th className="p-3 w-10 border-b border-[#edebe9] text-center">
                                <input type="checkbox" />
                            </th>
                            <th className="p-3 border-b border-[#edebe9] w-40">Invoice #</th>
                            <th className="p-3 border-b border-[#edebe9]">Customer</th>
                            <th className="p-3 border-b border-[#edebe9] w-32">Date</th>
                            <th className="p-3 border-b border-[#edebe9] w-32">Due Date</th>
                            <th className="p-3 border-b border-[#edebe9] w-40">Status</th>
                            <th className="p-3 border-b border-[#edebe9] w-32 text-right">Total</th>
                        </tr>
                    </thead>
                    <tbody className="text-sm text-[#201f1e]">
                        {invoices.map((invoice) => (
                            <tr
                                key={invoice.id}
                                className="border-b border-[#edebe9] hover:bg-[#f3f9ff] cursor-pointer transition-colors"
                                onClick={() => navigate(`/sales/invoices/${invoice.id}`)}
                            >
                                <td className="p-3 text-center" onClick={(e) => e.stopPropagation()}>
                                    <input type="checkbox" />
                                </td>
                                <td className="p-3 text-[#0078d4] font-semibold hover:underline">{invoice.invoice_number}</td>
                                <td className="p-3 font-medium">{invoice.customer}</td>
                                <td className="p-3 text-[#605e5c]">{invoice.date}</td>
                                <td className="p-3 text-[#605e5c]">{invoice.due_date}</td>
                                <td className="p-3">
                                    <span className={`px-2 py-1 rounded-full text-xs font-semibold ${getStatusColor(invoice.status)}`}>
                                        {invoice.status}
                                    </span>
                                </td>
                                <td className="p-3 text-right font-medium">${invoice.total.toFixed(2)}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default InvoiceListPage;

