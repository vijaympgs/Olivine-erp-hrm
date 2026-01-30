import React, { useState } from "react";
import {
    Save, Printer, Mail, MoreHorizontal, Plus, Trash2,
    Calendar, User, FileText, ChevronDown, Check
} from "lucide-react";

interface QuoteLine {
    id: string;
    product_name: string;
    sku: string;
    quantity: number;
    unit_price: number;
    discount: number;
    tax_rate: number;
}

const QuoteWireframe: React.FC = () => {
    const [lines, setLines] = useState<QuoteLine[]>([
        { id: '1', product_name: 'Wireless Mouse', sku: 'WM-001', quantity: 2, unit_price: 25.00, discount: 0, tax_rate: 18 },
        { id: '2', product_name: 'Mechanical Keyboard', sku: 'KB-PRO', quantity: 1, unit_price: 120.00, discount: 10, tax_rate: 18 },
        { id: '3', product_name: 'USB-C Cable (2m)', sku: 'USB-C-2M', quantity: 5, unit_price: 8.50, discount: 0, tax_rate: 18 },
    ]);

    const addLine = () => {
        const newId = (lines.length + 1).toString();
        setLines([...lines, { id: newId, product_name: '', sku: '', quantity: 1, unit_price: 0, discount: 0, tax_rate: 0 }]);
    };

    const updateLine = (id: string, field: keyof QuoteLine, value: any) => {
        setLines(lines.map(line => line.id === id ? { ...line, [field]: value } : line));
    };

    const removeLine = (id: string) => {
        setLines(lines.filter(line => line.id !== id));
    };

    const calculateLineTotal = (line: QuoteLine) => {
        const sub = line.quantity * line.unit_price;
        const disc = sub * (line.discount / 100);
        const tax = (sub - disc) * (line.tax_rate / 100);
        return sub - disc + tax;
    };

    const subtotal = lines.reduce((sum, line) => sum + (line.quantity * line.unit_price), 0);
    const totalDiscount = lines.reduce((sum, line) => sum + (line.quantity * line.unit_price * (line.discount / 100)), 0);
    const totalTax = lines.reduce((sum, line) => sum + ((line.quantity * line.unit_price - (line.quantity * line.unit_price * (line.discount / 100))) * (line.tax_rate / 100)), 0);
    const grandTotal = subtotal - totalDiscount + totalTax;

    return (
        <div className="flex flex-col h-full bg-[#fbfbfb] text-sm text-gray-800">
            {/* 1. Command Bar (Dynamics 365 Style) */}
            <div className="flex items-center px-4 py-2 bg-white border-b border-gray-200 shadow-sm gap-2">
                <button className="flex items-center gap-2 px-3 py-1.5 bg-blue-700 text-white font-medium hover:bg-blue-800 transition-colors">
                    <Save size={16} /> Save
                </button>
                <div className="h-6 w-px bg-gray-300 mx-2"></div>
                <button className="flex items-center gap-2 px-3 py-1.5 text-gray-700 hover:bg-gray-100 transition-colors font-medium">
                    <Check size={16} /> Activate Quote
                </button>
                <button className="flex items-center gap-2 px-3 py-1.5 text-gray-700 hover:bg-gray-100 transition-colors">
                    <Printer size={16} /> Print
                </button>
                <button className="flex items-center gap-2 px-3 py-1.5 text-gray-700 hover:bg-gray-100 transition-colors">
                    <Mail size={16} /> Email
                </button>
                <div className="flex-1"></div>
                <button className="p-2 text-gray-500 hover:text-gray-900 transition-colors">
                    <MoreHorizontal size={18} />
                </button>
            </div>

            {/* 2. Header / Form Context */}
            <div className="p-6 pb-2">
                <div className="flex justify-between items-start mb-6">
                    <div>
                        <h1 className="text-2xl font-light text-gray-900 mb-1">Quote <span className="font-semibold">QT-2025-0842</span></h1>
                        <p className="text-gray-500">Draft • Created on Dec 20, 2025</p>
                    </div>
                    <div className="text-right">
                        <span className="text-3xl font-light text-gray-900">${grandTotal.toFixed(2)}</span>
                        <p className="text-gray-500 text-xs uppercase tracking-wider font-semibold">Total Amount</p>
                    </div>
                </div>

                {/* Form Fields Grid */}
                <div className="grid grid-cols-4 gap-6 bg-white p-4 border border-gray-200 shadow-sm mb-6">
                    <div className="space-y-1">
                        <label className="text-xs font-semibold text-gray-500 uppercase">Customer</label>
                        <div className="flex items-center gap-2 border-b border-gray-300 pb-1">
                            <User size={14} className="text-blue-600" />
                            <input type="text" value="Acme Corp (Intl)" className="w-full outline-none bg-transparent font-medium text-blue-700" />
                        </div>
                    </div>
                    <div className="space-y-1">
                        <label className="text-xs font-semibold text-gray-500 uppercase">Description</label>
                        <div className="border-b border-gray-300 pb-1">
                            <input type="text" value="Q4 Hardware Refresh" className="w-full outline-none bg-transparent" />
                        </div>
                    </div>
                    <div className="space-y-1">
                        <label className="text-xs font-semibold text-gray-500 uppercase">Effective Date</label>
                        <div className="flex items-center gap-2 border-b border-gray-300 pb-1">
                            <Calendar size={14} className="text-gray-400" />
                            <input type="text" value="12/20/2025" className="w-full outline-none bg-transparent" />
                        </div>
                    </div>
                    <div className="space-y-1">
                        <label className="text-xs font-semibold text-gray-500 uppercase">Payment Terms</label>
                        <div className="flex items-center gap-2 border-b border-gray-300 pb-1">
                            <FileText size={14} className="text-gray-400" />
                            <input type="text" value="Net 30" className="w-full outline-none bg-transparent" />
                        </div>
                    </div>
                </div>
            </div>

            {/* 3. Lines Grid (Excel Style) */}
            <div className="flex-1 px-6 overflow-hidden flex flex-col">
                <div className="flex items-center justify-between mb-2">
                    <div className="flex gap-4">
                        <button className="text-blue-700 font-semibold border-b-2 border-blue-700 pb-1 text-sm">Product Lines</button>
                        <button className="text-gray-500 hover:text-gray-800 pb-1 text-sm">Services</button>
                        <button className="text-gray-500 hover:text-gray-800 pb-1 text-sm">Notes</button>
                    </div>
                    <button onClick={addLine} className="flex items-center gap-1 text-xs font-bold uppercase tracking-wide text-blue-700 hover:underline">
                        <Plus size={14} /> Add Product
                    </button>
                </div>

                <div className="bg-white border border-gray-300 flex-1 overflow-auto shadow-sm">
                    <table className="w-full border-collapse">
                        <thead>
                            <tr className="bg-gray-100 text-gray-600 text-xs uppercase tracking-wider text-left border-b border-gray-300">
                                <th className="p-2 border-r border-gray-300 w-10 text-center">#</th>
                                <th className="p-2 border-r border-gray-300 w-32">SKU</th>
                                <th className="p-2 border-r border-gray-300">Product Name</th>
                                <th className="p-2 border-r border-gray-300 w-24 text-right">Quantity</th>
                                <th className="p-2 border-r border-gray-300 w-24 text-right">Unit Price</th>
                                <th className="p-2 border-r border-gray-300 w-20 text-right">Disc %</th>
                                <th className="p-2 border-r border-gray-300 w-20 text-right">Tax %</th>
                                <th className="p-2 w-32 text-right">Total</th>
                                <th className="p-2 w-10"></th>
                            </tr>
                        </thead>
                        <tbody className="text-sm">
                            {lines.map((line, index) => (
                                <tr key={line.id} className="border-b border-gray-200 hover:bg-blue-50 group">
                                    <td className="p-0 border-r border-gray-200 text-center text-gray-400 bg-gray-50 text-xs cursor-grab select-none">{index + 1}</td>
                                    <td className="p-0 border-r border-gray-200">
                                        <input
                                            type="text"
                                            value={line.sku}
                                            className="w-full p-2 outline-none bg-transparent focus:bg-white focus:ring-1 focus:ring-blue-500 focus:z-10"
                                            onChange={(e) => updateLine(line.id, 'sku', e.target.value)}
                                        />
                                    </td>
                                    <td className="p-0 border-r border-gray-200">
                                        <input
                                            type="text"
                                            value={line.product_name}
                                            className="w-full p-2 outline-none bg-transparent focus:bg-white focus:ring-1 focus:ring-blue-500 focus:z-10"
                                            onChange={(e) => updateLine(line.id, 'product_name', e.target.value)}
                                        />
                                    </td>
                                    <td className="p-0 border-r border-gray-200">
                                        <input
                                            type="number"
                                            value={line.quantity}
                                            className="w-full p-2 outline-none bg-transparent text-right focus:bg-white focus:ring-1 focus:ring-blue-500 focus:z-10"
                                            onChange={(e) => updateLine(line.id, 'quantity', parseFloat(e.target.value))}
                                        />
                                    </td>
                                    <td className="p-0 border-r border-gray-200">
                                        <input
                                            type="number"
                                            value={line.unit_price}
                                            className="w-full p-2 outline-none bg-transparent text-right focus:bg-white focus:ring-1 focus:ring-blue-500 focus:z-10"
                                            onChange={(e) => updateLine(line.id, 'unit_price', parseFloat(e.target.value))}
                                        />
                                    </td>
                                    <td className="p-0 border-r border-gray-200">
                                        <input
                                            type="number"
                                            value={line.discount}
                                            className="w-full p-2 outline-none bg-transparent text-right focus:bg-white focus:ring-1 focus:ring-blue-500 focus:z-10"
                                            onChange={(e) => updateLine(line.id, 'discount', parseFloat(e.target.value))}
                                        />
                                    </td>
                                    <td className="p-0 border-r border-gray-200">
                                        <input
                                            type="number"
                                            value={line.tax_rate}
                                            className="w-full p-2 outline-none bg-transparent text-right focus:bg-white focus:ring-1 focus:ring-blue-500 focus:z-10"
                                            onChange={(e) => updateLine(line.id, 'tax_rate', parseFloat(e.target.value))}
                                        />
                                    </td>
                                    <td className="p-2 text-right font-medium bg-gray-50">
                                        {calculateLineTotal(line).toFixed(2)}
                                    </td>
                                    <td className="p-0 text-center">
                                        <button onClick={() => removeLine(line.id)} className="p-2 text-gray-400 hover:text-red-500 opacity-0 group-hover:opacity-100 transition-opacity">
                                            <Trash2 size={14} />
                                        </button>
                                    </td>
                                </tr>
                            ))}
                            {/* Ghost Row for Quick Add */}
                            <tr className="border-b border-gray-200 hover:bg-gray-50 opacity-50 cursor-pointer" onClick={addLine}>
                                <td className="p-2 border-r border-gray-200 text-center text-xs">+</td>
                                <td className="p-2 border-r border-gray-200 italic" colSpan={7}>Click to add new line...</td>
                                <td></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            {/* 4. Totals Footer */}
            <div className="bg-white border-t border-gray-200 p-6 shadow-[0_-4px_6px_-1px_rgba(0,0,0,0.05)]">
                <div className="flex justify-end gap-12 text-sm">
                    <div className="text-right space-y-2">
                        <p className="text-gray-500 uppercase text-xs font-semibold">Subtotal</p>
                        <p className="font-medium">{subtotal.toFixed(2)}</p>
                    </div>
                    <div className="text-right space-y-2">
                        <p className="text-gray-500 uppercase text-xs font-semibold">Discount</p>
                        <p className="font-medium text-red-600">-{totalDiscount.toFixed(2)}</p>
                    </div>
                    <div className="text-right space-y-2">
                        <p className="text-gray-500 uppercase text-xs font-semibold">Tax</p>
                        <p className="font-medium">{totalTax.toFixed(2)}</p>
                    </div>
                    <div className="text-right space-y-2 pl-8 border-l border-gray-200">
                        <p className="text-gray-500 uppercase text-xs font-bold text-blue-800">Total Amount</p>
                        <p className="text-2xl font-light text-blue-900">${grandTotal.toFixed(2)}</p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default QuoteWireframe;

