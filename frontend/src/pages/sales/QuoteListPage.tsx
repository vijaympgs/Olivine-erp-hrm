import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Loader2, AlertCircle, RefreshCw, Trash2, Search } from "lucide-react";
import { salesService, SalesQuote } from "../../services/salesService";
import { MasterToolbar, MasterMode } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";

const QuoteListPage: React.FC = () => {
    const navigate = useNavigate();
    const [quotes, setQuotes] = useState<SalesQuote[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);
    const [selectedIds, setSelectedIds] = useState<string[]>([]);
    const [searchQuery, setSearchQuery] = useState('');

    const fetchQuotes = async () => {
        setLoading(true);
        try {
            const data = await salesService.getQuotes();
            // Handle both Array and Pagination Result
            if (Array.isArray(data)) {
                setQuotes(data);
            } else if (data && data.results) {
                setQuotes(data.results);
            } else {
                setQuotes([]);
            }
        } catch (err) {
            console.error(err);
            setError("Failed to load quotes");
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        fetchQuotes();
    }, []);

    const handleDelete = async () => {
        if (!selectedIds.length) return;
        if (!window.confirm(`Delete ${selectedIds.length} quote(s)?`)) return;

        setLoading(true);
        // Sequential delete to avoid overwhelming if many
        for (const id of selectedIds) {
            try {
                await salesService.deleteQuote(id);
            } catch (e) {
                console.error(`Failed to delete quote ${id}`, e);
            }
        }
        setSelectedIds([]);
        fetchQuotes();
    };

    const handleToolbarAction = (action: string) => {
        switch (action) {
            case 'new':
                navigate('/sales/quotes/new');
                break;
            case 'refresh':
                fetchQuotes();
                break;
            case 'delete':
                handleDelete();
                break;
            default:
                console.log(`Action ${action} handled by MasterToolbar but not locally mapped (check logic).`);
        }
    };

    const handleSelectAll = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.checked) setSelectedIds(quotes.map(q => q.id));
        else setSelectedIds([]);
    };

    const handleSelectRow = (id: string) => {
        if (selectedIds.includes(id)) setSelectedIds(selectedIds.filter(i => i !== id));
        else setSelectedIds([...selectedIds, id]);
    };

    const getStatusColor = (status: string) => {
        switch (status) {
            case 'APPROVED': return 'bg-[#dff6dd] text-[#107c10]';
            case 'DRAFT': return 'bg-[#eff6fc] text-[#0078d4]';
            case 'REJECTED': return 'bg-[#fde7e9] text-[#a4262c]';
            case 'SUBMITTED': return 'bg-[#fff4ce] text-[#323130]';
            default: return 'bg-[#f3f2f1] text-[#201f1e]';
        }
    };

    // Filter quotes based on search query
    const filteredQuotes = quotes.filter(q =>
        q.quote_number?.toLowerCase().includes(searchQuery.toLowerCase()) ||
        q.customer_name?.toLowerCase().includes(searchQuery.toLowerCase()) ||
        q.remarks?.toLowerCase().includes(searchQuery.toLowerCase())
    );

    return (
        <div className="flex flex-col h-full bg-[#faf9f8] text-sm text-[#201f1e]">
            {/* Master Toolbar */}
            <div className="shrink-0">
                <MasterToolbar
                    viewId="QUOTES"
                    mode="VIEW"
                    onAction={handleToolbarAction}
                    hasSelection={selectedIds.length > 0}
                    title="Sales Quotes"
                    onSearch={(query: string) => setSearchQuery(query)}
                    showSearch={true}
                />
            </div>

            {/* Content */}
            <div className="flex-1 overflow-auto p-6">
                {loading ? (
                    <div className="flex items-center justify-center h-full text-[#605e5c]">
                        <Loader2 className="animate-spin mr-2" size={20} /> Loading quotes...
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
                                    <th className="p-3 w-10 text-center">
                                        <input
                                            type="checkbox"
                                            onChange={handleSelectAll}
                                            checked={quotes.length > 0 && selectedIds.length === quotes.length}
                                        />
                                    </th>
                                    <th className="p-3 w-32 border-l border-[#edebe9]">Quote #</th>
                                    <th className="p-3 border-l border-[#edebe9]">Customer</th>
                                    <th className="p-3 w-32 border-l border-[#edebe9]">Date</th>
                                    <th className="p-3 w-32 border-l border-[#edebe9] text-right">Total</th>
                                    <th className="p-3 w-32 border-l border-[#edebe9] text-center">Status</th>
                                </tr>
                            </thead>
                            <tbody className="text-sm">
                                {filteredQuotes.length === 0 ? (
                                    <tr>
                                        <td colSpan={6} className="p-8 text-center text-[#605e5c]">
                                            No quotes found.
                                        </td>
                                    </tr>
                                ) : (
                                    filteredQuotes.map((quote) => (
                                        <tr key={quote.id} className="border-b border-[#f3f2f1] hover:bg-[#f3f9ff] transition-colors">
                                            <td className="p-3 text-center">
                                                <input
                                                    type="checkbox"
                                                    checked={selectedIds.includes(quote.id)}
                                                    onChange={() => handleSelectRow(quote.id)}
                                                />
                                            </td>
                                            <td className="p-3 border-l border-[#edebe9] font-medium">
                                                <button
                                                    onClick={() => navigate(`/sales/quotes/${quote.id}`)}
                                                    className="text-[#0078d4] hover:underline"
                                                >
                                                    {quote.quote_number}
                                                </button>
                                            </td>
                                            <td className="p-3 border-l border-[#edebe9]">{quote.customer_name || 'Unknown'}</td>
                                            <td className="p-3 border-l border-[#edebe9]">{quote.quote_date}</td>
                                            <td className="p-3 border-l border-[#edebe9] text-right font-medium">
                                                {quote.grand_total?.toFixed(2)}
                                            </td>
                                            <td className="p-3 border-l border-[#edebe9] text-center">
                                                <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider ${getStatusColor(quote.quote_status)}`}>
                                                    {quote.quote_status}
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

export default QuoteListPage;
