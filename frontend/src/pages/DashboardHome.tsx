import React, { useState } from "react";
import {
  TrendingUp,
  TrendingDown,
  ShoppingCart,
  Users,
  Package,
  DollarSign,
  AlertTriangle,
  ArrowUpRight,
  ArrowDownRight,
  Store,
  CreditCard,
  BarChart3,
  PieChart,
  Clock,
  CheckCircle2,
  XCircle,
  Minus,
  ChevronRight,
  MapPin,
  Box,
  Truck,
  RefreshCcw
} from "lucide-react";

interface MetricCardProps {
  title: string;
  value: string;
  change: number;
  changeLabel: string;
  icon: React.ReactNode;
  color: "blue" | "green" | "purple" | "orange" | "red" | "teal";
  subMetrics?: { label: string; value: string }[];
}

const MetricCard: React.FC<MetricCardProps> = ({ title, value, change, changeLabel, icon, color, subMetrics }) => {
  const colorClasses = {
    blue: { text: 'text-blue-600', bg: 'bg-blue-50', border: 'border-blue-100' },
    green: { text: 'text-green-600', bg: 'bg-green-50', border: 'border-green-100' },
    purple: { text: 'text-purple-600', bg: 'bg-purple-50', border: 'border-purple-100' },
    orange: { text: 'text-orange-600', bg: 'bg-orange-50', border: 'border-orange-100' },
    red: { text: 'text-red-600', bg: 'bg-red-50', border: 'border-red-100' },
    teal: { text: 'text-teal-600', bg: 'bg-teal-50', border: 'border-teal-100' }
  };

  const colors = colorClasses[color];
  const isPositive = change >= 0;

  return (
    <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-all duration-200 group">
      <div className="flex justify-between items-start mb-4">
        <div>
          <p className="text-sm font-medium text-gray-500 mb-1">{title}</p>
          <h3 className="text-3xl font-bold text-gray-900 tracking-tight">{value}</h3>
        </div>
        <div className={`p-3 rounded-xl ${colors.bg} ${colors.text} group-hover:scale-110 transition-transform duration-200`}>
          {icon}
        </div>
      </div>

      <div className="flex items-center gap-2 mb-4">
        <div className={`flex items-center px-2 py-0.5 rounded-full text-xs font-semibold ${isPositive ? 'bg-green-50 text-green-700' : 'bg-red-50 text-red-700'}`}>
          {isPositive ? <TrendingUp className="w-3 h-3 mr-1" /> : <TrendingDown className="w-3 h-3 mr-1" />}
          {Math.abs(change)}%
        </div>
        <span className="text-xs text-gray-400 font-medium">{changeLabel}</span>
      </div>

      {subMetrics && (
        <div className="pt-4 border-t border-gray-50 flex items-center justify-between gap-4">
          {subMetrics.map((metric, idx) => (
            <div key={idx} className="flex flex-col">
              <span className="text-[10px] uppercase tracking-wider text-gray-400 font-semibold">{metric.label}</span>
              <span className="text-sm font-semibold text-gray-700">{metric.value}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export const DashboardHome: React.FC = () => {
  const [selectedPeriod, setSelectedPeriod] = useState<'today' | 'week' | 'month' | 'quarter'>('today');

  return (
    <div className="space-y-5">
      {/* Header with Period Selector */}
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold text-gray-900">Executive Dashboard</h1>
        <div className="flex items-center gap-2 bg-white border border-gray-200 rounded-lg p-1">
          {(['today', 'week', 'month', 'quarter'] as const).map((period) => (
            <button
              key={period}
              onClick={() => setSelectedPeriod(period)}
              className={`px-4 py-1.5 text-xs font-semibold rounded-md transition-all ${selectedPeriod === period
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
                }`}
            >
              {period.charAt(0).toUpperCase() + period.slice(1)}
            </button>
          ))}
        </div>
      </div>

      {/* Primary KPIs */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <MetricCard
          title="Total Revenue"
          value="$2,847,392"
          change={12.5}
          changeLabel="vs last period"
          icon={<DollarSign className="w-5 h-5" />}
          color="blue"
          subMetrics={[
            { label: 'Target', value: '$3,000,000' },
            { label: 'Achievement', value: '94.9%' }
          ]}
        />
        <MetricCard
          title="Orders Processed"
          value="8,247"
          change={8.2}
          changeLabel="vs last period"
          icon={<ShoppingCart className="w-5 h-5" />}
          color="green"
          subMetrics={[
            { label: 'Avg Order Value', value: '$345.32' },
            { label: 'Conversion Rate', value: '3.8%' }
          ]}
        />
        <MetricCard
          title="Active Customers"
          value="24,847"
          change={15.3}
          changeLabel="vs last period"
          icon={<Users className="w-5 h-5" />}
          color="purple"
          subMetrics={[
            { label: 'New Customers', value: '1,284' },
            { label: 'Retention Rate', value: '89.2%' }
          ]}
        />
        <MetricCard
          title="Gross Margin"
          value="42.8%"
          change={2.1}
          changeLabel="vs last period"
          icon={<BarChart3 className="w-5 h-5" />}
          color="teal"
          subMetrics={[
            { label: 'COGS', value: '$1,628,452' },
            { label: 'Net Profit', value: '$1,218,940' }
          ]}
        />
      </div>

      {/* Secondary Metrics Row */}
      <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
        {[
          { label: 'Inventory Value', value: '$4.2M', icon: <Box className="w-5 h-5" />, color: 'text-blue-600', bg: 'bg-blue-50' },
          { label: 'Avg Fulfillment', value: '1.8 days', icon: <Truck className="w-5 h-5" />, color: 'text-green-600', bg: 'bg-green-50' },
          { label: 'Stock Turnover', value: '6.2x', icon: <RefreshCcw className="w-5 h-5" />, color: 'text-purple-600', bg: 'bg-purple-50' },
          { label: 'Active Stores', value: '47', icon: <Store className="w-5 h-5" />, color: 'text-orange-600', bg: 'bg-orange-50' },
          { label: 'Payment Success', value: '98.4%', icon: <CreditCard className="w-5 h-5" />, color: 'text-teal-600', bg: 'bg-teal-50' }
        ].map((stat, idx) => (
          <div key={idx} className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm flex flex-col justify-between hover:border-gray-200 hover:shadow-md transition-all">
            <div className="flex justify-between items-start mb-2">
              <div className={`p-2 rounded-lg ${stat.bg} ${stat.color}`}>
                {stat.icon}
              </div>
            </div>
            <div>
              <p className="text-2xl font-bold text-gray-900">{stat.value}</p>
              <p className="text-xs font-medium text-gray-500 uppercase tracking-wide mt-1">{stat.label}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Main Analytics Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Sales Performance */}
        <div className="lg:col-span-2 bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h3 className="text-lg font-bold text-gray-900">Sales Performance</h3>
              <p className="text-sm text-gray-500 mt-1">Revenue breakdown by channel</p>
            </div>
            <button className="text-sm font-medium text-blue-600 hover:text-blue-700 flex items-center transition-colors">
              View Details <ChevronRight className="w-4 h-4 ml-0.5" />
            </button>
          </div>
          <div className="space-y-4">
            {[
              { channel: 'E-Commerce', revenue: '$1,247,892', orders: 4821, growth: 18.2, color: 'bg-blue-500' },
              { channel: 'Retail Stores', revenue: '$892,450', orders: 2156, growth: 8.5, color: 'bg-green-500' },
              { channel: 'Wholesale', revenue: '$487,320', orders: 892, growth: -3.2, color: 'bg-purple-500' },
              { channel: 'Mobile App', revenue: '$219,730', orders: 378, growth: 24.8, color: 'bg-orange-500' }
            ].map((item) => (
              <div key={item.channel} className="group border border-gray-100 rounded-xl p-4 hover:border-blue-100 hover:bg-blue-50/30 transition-all duration-200">
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-4">
                    <div className={`w-1.5 h-10 ${item.color} rounded-full`}></div>
                    <div>
                      <p className="text-sm font-bold text-gray-900">{item.channel}</p>
                      <p className="text-xs text-gray-500 font-medium">{item.orders.toLocaleString()} orders</p>
                    </div>
                  </div>
                  <div className="text-right">
                    <p className="text-base font-bold text-gray-900">{item.revenue}</p>
                    <p className={`text-xs font-semibold flex items-center justify-end ${item.growth >= 0 ? 'text-green-600' : 'text-red-600'}`}>
                      {item.growth >= 0 ? <TrendingUp className="w-3 h-3 mr-1" /> : <TrendingDown className="w-3 h-3 mr-1" />}
                      {Math.abs(item.growth)}%
                    </p>
                  </div>
                </div>
                <div className="w-full bg-gray-100 rounded-full h-1.5 overflow-hidden">
                  <div className={`${item.color} h-1.5 rounded-full group-hover:scale-x-105 transition-transform origin-left duration-500`} style={{ width: `${(parseFloat(item.revenue.replace(/[$,]/g, '')) / 2847392) * 100}%` }}></div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Top Products */}
        <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h3 className="text-lg font-bold text-gray-900">Top Products</h3>
              <p className="text-sm text-gray-500 mt-1">Best sellers this period</p>
            </div>
          </div>
          <div className="space-y-3">
            {[
              { name: 'iPhone 15 Pro Max', sku: 'APL-IP15PM-256', sales: '$284,920', units: 826, trend: 'up' },
              { name: 'Samsung Galaxy S24', sku: 'SAM-GS24-128', sales: '$198,450', units: 612, trend: 'up' },
              { name: 'MacBook Air M3', sku: 'APL-MBA-M3-512', sales: '$176,320', units: 142, trend: 'up' },
              { name: 'AirPods Pro 2', sku: 'APL-APP2-USB', sales: '$89,240', units: 357, trend: 'down' },
              { name: 'iPad Pro 13"', sku: 'APL-IPP13-256', sales: '$72,180', units: 58, trend: 'up' }
            ].map((product, idx) => (
              <div key={product.sku} className="flex items-center gap-4 p-3 rounded-xl hover:bg-gray-50 transition-colors border border-transparent hover:border-gray-100 group">
                <div className="flex items-center justify-center w-8 h-8 rounded-lg bg-gray-100 text-sm font-bold text-gray-600 group-hover:bg-white group-hover:shadow-sm transition-all">
                  {idx + 1}
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-semibold text-gray-900 truncate">{product.name}</p>
                  <p className="text-xs text-gray-500 font-mono">{product.sku}</p>
                </div>
                <div className="text-right">
                  <p className="text-sm font-bold text-gray-900">{product.sales}</p>
                  <p className="text-xs text-gray-500">{product.units} units</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Regional Performance & Inventory */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Regional Sales */}
        <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h3 className="text-lg font-bold text-gray-900">Regional Performance</h3>
              <p className="text-sm text-gray-500 mt-1">Sales by geographic region</p>
            </div>
          </div>
          <div className="space-y-4">
            {[
              { region: 'North America', revenue: '$1,247,892', share: 43.8, stores: 18, growth: 12.4 },
              { region: 'Europe', revenue: '$892,450', share: 31.3, stores: 15, growth: 8.9 },
              { region: 'Asia Pacific', revenue: '$487,320', share: 17.1, stores: 10, growth: 22.1 },
              { region: 'Middle East', revenue: '$219,730', share: 7.8, stores: 4, growth: 15.6 }
            ].map((region) => (
              <div key={region.region} className="border border-gray-100 rounded-xl p-4 hover:bg-gray-50 transition-colors">
                <div className="flex items-center justify-between mb-3">
                  <div className="flex items-center gap-3">
                    <div className="p-2 bg-blue-50 rounded-lg text-blue-600">
                      <MapPin className="w-4 h-4" />
                    </div>
                    <div>
                      <p className="text-sm font-semibold text-gray-900">{region.region}</p>
                      <p className="text-xs text-gray-500">{region.stores} stores</p>
                    </div>
                  </div>
                  <div className="text-right">
                    <p className="text-sm font-bold text-gray-900">{region.revenue}</p>
                    <p className="text-xs text-green-600 font-semibold">+{region.growth}%</p>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <div className="flex-1 bg-gray-100 rounded-full h-2 overflow-hidden">
                    <div className="bg-blue-500 h-2 rounded-full" style={{ width: `${region.share}%` }}></div>
                  </div>
                  <span className="text-xs font-semibold text-gray-600 w-12 text-right">{region.share}%</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Inventory Status */}
        <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h3 className="text-lg font-bold text-gray-900">Inventory Overview</h3>
              <p className="text-sm text-gray-500 mt-1">Stock levels and alerts</p>
            </div>
          </div>

          {/* Inventory Summary */}
          <div className="grid grid-cols-3 gap-4 mb-6">
            <div className="bg-green-50/50 border border-green-100 rounded-xl p-4 text-center">
              <div className="flex justify-center mb-2">
                <CheckCircle2 className="w-5 h-5 text-green-600" />
              </div>
              <p className="text-2xl font-bold text-green-900 mb-1">2,847</p>
              <p className="text-xs font-medium text-green-700 uppercase tracking-wide">In Stock</p>
            </div>
            <div className="bg-orange-50/50 border border-orange-100 rounded-xl p-4 text-center">
              <div className="flex justify-center mb-2">
                <AlertTriangle className="w-5 h-5 text-orange-600" />
              </div>
              <p className="text-2xl font-bold text-orange-900 mb-1">142</p>
              <p className="text-xs font-medium text-orange-700 uppercase tracking-wide">Low Stock</p>
            </div>
            <div className="bg-red-50/50 border border-red-100 rounded-xl p-4 text-center">
              <div className="flex justify-center mb-2">
                <XCircle className="w-5 h-5 text-red-600" />
              </div>
              <p className="text-2xl font-bold text-red-900 mb-1">23</p>
              <p className="text-xs font-medium text-red-700 uppercase tracking-wide">Out of Stock</p>
            </div>
          </div>

          {/* Critical Items */}
          <div>
            <p className="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3">Critical Items</p>
            <div className="space-y-2">
              {[
                { name: 'iPhone 15 Pro - 256GB', sku: 'APL-IP15P-256', stock: 8, status: 'critical', reorder: 50 },
                { name: 'Galaxy Buds Pro', sku: 'SAM-GBP-BLK', stock: 12, status: 'low', reorder: 100 },
                { name: 'MacBook Pro 14"', sku: 'APL-MBP14-512', stock: 5, status: 'critical', reorder: 25 }
              ].map((item) => (
                <div key={item.sku} className="flex items-center justify-between p-3 bg-gray-50 rounded-xl border border-gray-100 hover:border-gray-200 transition-colors">
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-semibold text-gray-900 truncate">{item.name}</p>
                    <p className="text-xs text-gray-500 font-mono mt-0.5">{item.sku}</p>
                  </div>
                  <div className="flex items-center gap-4">
                    <div className="text-right">
                      <p className="text-sm font-bold text-gray-900">{item.stock} units</p>
                      <p className="text-xs text-gray-500">Reorder: {item.reorder}</p>
                    </div>
                    <span className={`text-[10px] px-2.5 py-1 rounded-full font-bold uppercase tracking-wide ${item.status === 'critical' ? 'bg-red-100 text-red-700' : 'bg-orange-100 text-orange-700'
                      }`}>
                      {item.status}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Order Status & Recent Activity */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 pb-10">
        {/* Order Status */}
        <div className="bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
          <div className="mb-6">
            <h3 className="text-lg font-bold text-gray-900">Order Status</h3>
            <p className="text-sm text-gray-500 mt-1">Current order pipeline</p>
          </div>
          <div className="space-y-4">
            {[
              { status: 'Pending', count: 247, value: '$89,420', color: 'bg-yellow-500', icon: <Clock className="w-4 h-4" /> },
              { status: 'Processing', count: 184, value: '$67,230', color: 'bg-blue-500', icon: <Package className="w-4 h-4" /> },
              { status: 'Shipped', count: 521, value: '$189,450', color: 'bg-purple-500', icon: <Truck className="w-4 h-4" /> },
              { status: 'Delivered', count: 1847, value: '$672,180', color: 'bg-green-500', icon: <CheckCircle2 className="w-4 h-4" /> }
            ].map((order) => (
              <div key={order.status} className="flex items-center justify-between p-4 border border-gray-100 rounded-xl hover:bg-gray-50 transition-all">
                <div className="flex items-center gap-4">
                  <div className={`${order.color} p-2.5 rounded-lg text-white shadow-sm`}>
                    {order.icon}
                  </div>
                  <div>
                    <p className="text-sm font-bold text-gray-900">{order.status}</p>
                    <p className="text-xs text-gray-500">{order.count} orders</p>
                  </div>
                </div>
                <p className="text-sm font-bold text-gray-900 font-mono">{order.value}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Recent Transactions */}
        <div className="lg:col-span-2 bg-white p-6 rounded-xl border border-gray-100 shadow-sm">
          <div className="flex items-center justify-between mb-6">
            <div>
              <h3 className="text-lg font-bold text-gray-900">Recent Transactions</h3>
              <p className="text-sm text-gray-500 mt-1">Latest order activity</p>
            </div>
            <button className="text-sm font-medium text-blue-600 hover:text-blue-700 flex items-center transition-colors">
              View All <ChevronRight className="w-4 h-4 ml-0.5" />
            </button>
          </div>
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="border-b border-gray-100">
                  <th className="text-left py-3 px-4 text-xs font-semibold text-gray-400 uppercase tracking-wider">Order ID</th>
                  <th className="text-left py-3 px-4 text-xs font-semibold text-gray-400 uppercase tracking-wider">Customer</th>
                  <th className="text-left py-3 px-4 text-xs font-semibold text-gray-400 uppercase tracking-wider">Channel</th>
                  <th className="text-right py-3 px-4 text-xs font-semibold text-gray-400 uppercase tracking-wider">Amount</th>
                  <th className="text-center py-3 px-4 text-xs font-semibold text-gray-400 uppercase tracking-wider">Status</th>
                  <th className="text-right py-3 px-4 text-xs font-semibold text-gray-400 uppercase tracking-wider">Time</th>
                </tr>
              </thead>
              <tbody>
                {[
                  { id: 'ORD-2024-8247', customer: 'Sarah Johnson', channel: 'E-Commerce', amount: '$1,234.50', status: 'Delivered', time: '2m ago', statusColor: 'green' },
                  { id: 'ORD-2024-8246', customer: 'Michael Chen', channel: 'Retail', amount: '$589.99', status: 'Shipped', time: '8m ago', statusColor: 'purple' },
                  { id: 'ORD-2024-8245', customer: 'Emily Rodriguez', channel: 'Mobile App', amount: '$2,456.75', status: 'Processing', time: '15m ago', statusColor: 'blue' },
                  { id: 'ORD-2024-8244', customer: 'David Kim', channel: 'Wholesale', amount: '$8,923.25', status: 'Delivered', time: '22m ago', statusColor: 'green' },
                  { id: 'ORD-2024-8243', customer: 'Lisa Anderson', channel: 'E-Commerce', amount: '$445.80', status: 'Pending', time: '28m ago', statusColor: 'yellow' }
                ].map((txn) => (
                  <tr key={txn.id} className="border-b border-gray-50 hover:bg-gray-50/80 transition-colors group">
                    <td className="py-4 px-4">
                      <p className="text-sm font-semibold text-gray-900 group-hover:text-blue-600 transition-colors">{txn.id}</p>
                    </td>
                    <td className="py-4 px-4">
                      <p className="text-sm text-gray-700">{txn.customer}</p>
                    </td>
                    <td className="py-4 px-4">
                      <p className="text-sm text-gray-500">{txn.channel}</p>
                    </td>
                    <td className="py-4 px-4 text-right">
                      <p className="text-sm font-bold text-gray-900 font-mono">{txn.amount}</p>
                    </td>
                    <td className="py-4 px-4 text-center">
                      <span className={`inline-flex items-center justify-center px-2.5 py-1 text-xs font-semibold rounded-full min-w-[80px] ${txn.statusColor === 'green' ? 'bg-green-50 text-green-700 border border-green-100' :
                        txn.statusColor === 'purple' ? 'bg-purple-50 text-purple-700 border border-purple-100' :
                          txn.statusColor === 'blue' ? 'bg-blue-50 text-blue-700 border border-blue-100' :
                            'bg-yellow-50 text-yellow-700 border border-yellow-100'
                        }`}>
                        {txn.status}
                      </span>
                    </td>
                    <td className="py-4 px-4 text-right">
                      <p className="text-sm text-gray-400">{txn.time}</p>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
};

