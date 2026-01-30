import React from "react";
import { ShoppingCart, Package, Truck, Activity, TrendingUp, DollarSign, AlertCircle, CheckCircle } from "lucide-react";
import {
    ResponsiveContainer, AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip,
    BarChart, Bar, Legend
} from "recharts";

// Mock Data
const revenueData = [
    { name: 'Mon', sales: 4000, target: 2400 },
    { name: 'Tue', sales: 3000, target: 1398 },
    { name: 'Wed', sales: 2000, target: 9800 },
    { name: 'Thu', sales: 2780, target: 3908 },
    { name: 'Fri', sales: 1890, target: 4800 },
    { name: 'Sat', sales: 2390, target: 3800 },
    { name: 'Sun', sales: 3490, target: 4300 },
];

const stockData = [
    { name: 'Shirts', stock: 120 },
    { name: 'Pants', stock: 80 },
    { name: 'Shoes', stock: 40 },
    { name: 'Accs', stock: 150 },
];

const StatCard = ({ title, value, sub, icon: Icon, color, trend }: any) => (
    <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm flex items-start justify-between">
        <div>
            <p className="text-gray-500 text-sm font-medium mb-1">{title}</p>
            <h3 className="text-2xl font-bold text-gray-900 mb-1">{value}</h3>
            <div className={`flex items-center text-xs font-semibold ${trend && trend.startsWith('+') ? 'text-green-600' : 'text-red-600'}`}>
                {trend && trend.startsWith('+') ? <TrendingUp size={12} className="mr-1" /> : <Activity size={12} className="mr-1" />}
                {sub}
            </div>
        </div>
        <div className={`p-3 rounded-lg ${color}`}>
            <Icon size={20} className="text-white" />
        </div>
    </div>
);

const RetailDashboardPage: React.FC = () => {
    return (
        <div className="p-8 bg-[#f8f9fa] min-h-screen text-gray-800">
            <div className="flex justify-between items-center mb-8">
                <div>
                    <h1 className="text-2xl font-bold text-gray-900">Retail Operations</h1>
                    <p className="text-gray-500 text-sm">Real-time overview of your retail store performance</p>
                </div>
                <div className="flex gap-2">
                    <span className="bg-white border border-gray-200 px-3 py-1 rounded-md text-sm font-medium text-gray-600">Last 7 Days</span>
                </div>
            </div>

            {/* KPI Cards */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                <StatCard
                    title="Total Sales"
                    value="$24,500"
                    sub="+12% vs last week"
                    icon={ShoppingCart}
                    trend="+12%"
                    color="bg-[#0078d4]"
                />
                <StatCard
                    title="Inventory Material"
                    value="$1.2M"
                    sub="Valuation"
                    icon={Package}
                    trend="+2%"
                    color="bg-emerald-500"
                />
                <StatCard
                    title="Open Procurement"
                    value="14"
                    sub="POs Pending"
                    icon={Truck}
                    trend="-5%"
                    color="bg-amber-500"
                />
                <StatCard
                    title="Active Registers"
                    value="8/10"
                    sub="POS Online"
                    icon={CheckCircle}
                    trend="+0%"
                    color="bg-purple-500"
                />
            </div>

            {/* Charts Section */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
                {/* Revenue Chart */}
                <div className="lg:col-span-2 bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
                    <h3 className="text-lg font-bold text-gray-900 mb-6">Revenue Trends</h3>
                    <div className="h-[300px] w-full">
                        <ResponsiveContainer width="100%" height="100%">
                            <AreaChart data={revenueData}>
                                <defs>
                                    <linearGradient id="colorSales" x1="0" y1="0" x2="0" y2="1">
                                        <stop offset="5%" stopColor="#0078d4" stopOpacity={0.1} />
                                        <stop offset="95%" stopColor="#0078d4" stopOpacity={0} />
                                    </linearGradient>
                                </defs>
                                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f0f0f0" />
                                <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{ fill: '#9ca3af', fontSize: 12 }} />
                                <YAxis axisLine={false} tickLine={false} tick={{ fill: '#9ca3af', fontSize: 12 }} />
                                <Tooltip />
                                <Area type="monotone" dataKey="sales" stroke="#0078d4" strokeWidth={3} fillOpacity={1} fill="url(#colorSales)" />
                            </AreaChart>
                        </ResponsiveContainer>
                    </div>
                </div>

                {/* Module Stats */}
                <div className="space-y-6">
                    {/* Procurement Stats */}
                    <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
                        <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2"><Truck size={18} className="text-amber-500" /> Procurement Requests</h3>
                        <div className="space-y-4">
                            <div className="flex justify-between items-center p-3 bg-amber-50 rounded-lg">
                                <span className="text-sm font-medium text-amber-900">Pending Approval (PR)</span>
                                <span className="text-lg font-bold text-amber-700">5</span>
                            </div>
                            <div className="flex justify-between items-center p-3 bg-blue-50 rounded-lg">
                                <span className="text-sm font-medium text-blue-900">Open RFQs</span>
                                <span className="text-lg font-bold text-blue-700">3</span>
                            </div>
                            <div className="flex justify-between items-center p-3 bg-green-50 rounded-lg">
                                <span className="text-sm font-medium text-green-900">Goods In-Transit</span>
                                <span className="text-lg font-bold text-green-700">12</span>
                            </div>
                        </div>
                    </div>

                    {/* Low Stock Stats */}
                    <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
                        <h3 className="text-lg font-bold text-gray-900 mb-4 flex items-center gap-2"><AlertCircle size={18} className="text-red-500" /> Low Stock Alerts</h3>
                        <div className="space-y-3">
                            <div className="flex items-center justify-between text-sm py-2 border-b border-gray-50 last:border-0">
                                <span className="text-gray-600">Cotton Fabric (RM-001)</span>
                                <span className="text-red-600 font-bold bg-red-50 px-2 py-0.5 rounded text-xs">10 MTR</span>
                            </div>
                            <div className="flex items-center justify-between text-sm py-2 border-b border-gray-50 last:border-0">
                                <span className="text-gray-600">Polyester Thread</span>
                                <span className="text-red-600 font-bold bg-red-50 px-2 py-0.5 rounded text-xs">5 SPL</span>
                            </div>
                            <div className="flex items-center justify-between text-sm py-2 border-b border-gray-50 last:border-0">
                                <span className="text-gray-600">Zipper 5mm</span>
                                <span className="text-red-600 font-bold bg-red-50 px-2 py-0.5 rounded text-xs">0 PCS</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default RetailDashboardPage;

