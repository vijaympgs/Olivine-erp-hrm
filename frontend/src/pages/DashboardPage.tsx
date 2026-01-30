import React, { useState } from "react";
import {
    Activity, TrendingUp, AlertTriangle, Zap, ShoppingBag,
    Cpu, Globe, Leaf, Anchor, Target, ArrowRight, Brain,
    Layers, Clock, BarChart3, RotateCcw, Monitor
} from "lucide-react";

// --- ROBUST 8-CARD DATA WITH CACHE-BUSTED IMAGES ---
const feedData = [
    {
        id: 10,
        category: "Executive Synthesis",
        title: "Supply Chain Volatility Alert",
        summary: "APAC logistics index spiked to 45/100. Critical Q3 margin impact projected at -1.2%. Activate alternate supplier network now.",
        image: "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&q=80&w=800&v=3", // Warehouse
        icon: Brain,
        color: "bg-gray-900",
        timestamp: "Just now",
        url: "https://www.reuters.com/business/supply-chains/"
    },
    {
        id: 1,
        category: "Retail Momentum",
        title: "Consumer Confidence Rebounds",
        summary: "Global footfall is up 12% as shoppers return to physical stores for 'experience', despite sticky inflation.",
        image: "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&q=80&w=600&v=3", // Store
        icon: Activity,
        color: "bg-blue-600",
        timestamp: "15m",
        url: "https://nrf.com/research/consumer-view-winter-2024"
    },
    {
        id: 5,
        category: "AI & Innovation",
        title: "AI Forecasting Model Success",
        summary: "New predictive models have reduced demand forecast bias by 22%, significantly lowering safety stock needs.",
        image: "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=600&v=3", // Tech/Chip
        icon: Zap,
        color: "bg-purple-600",
        timestamp: "45m",
        url: "https://techcrunch.com/category/artificial-intelligence/"
    },
    {
        id: 2,
        category: "Consumer Behavior",
        title: "Shift to 'Experience' Retail",
        summary: "Urban centers report a marked preference for experiential retail over pure convenience this quarter.",
        image: "https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?auto=format&fit=crop&q=80&w=600&v=3", // Shopping/Bags
        icon: ShoppingBag,
        color: "bg-emerald-600",
        timestamp: "1h",
        url: "https://www.mckinsey.com/industries/retail/our-insights"
    },
    {
        id: 9,
        category: "Market Risk",
        title: "Electronics Chip Shortage",
        summary: "High-risk alert for Consumer Electronics category due to renewed supply constraints in Taiwan.",
        image: "https://images.unsplash.com/photo-1591405351996-2917711468f7?auto=format&fit=crop&q=80&w=600&v=3", // Circuit Board (Robust)
        icon: Target,
        color: "bg-amber-500",
        timestamp: "2h",
        url: "https://www.bloomberg.com/markets/commodities"
    },
    {
        id: 6,
        category: "Supply Chain",
        title: "Last-Mile Costs Rising",
        summary: "Logistics fuel surcharges have driven last-mile delivery costs up by 8% month-over-month.",
        image: "https://images.unsplash.com/photo-1580674684081-7617fbf3d745?auto=format&fit=crop&q=80&w=600&v=3", // Boxes/Delivery
        icon: Anchor,
        color: "bg-indigo-600",
        timestamp: "3h",
        url: "https://www.wsj.com/news/logistics-report"
    },
    {
        id: 3,
        category: "Channel Shifts",
        title: "Click & Collect Surge",
        summary: "BOPIS (Buy Online, Pickup In-Store) adoption has surpassed pure Home Delivery in EU region.",
        image: "https://images.unsplash.com/photo-1556742111-a301076d9d18?auto=format&fit=crop&q=80&w=600&v=3", // Mobile Payment/POS
        icon: Layers,
        color: "bg-cyan-600",
        timestamp: "1d",
        url: "https://www.shopify.com/retail/bopis"
    },
    {
        id: 7,
        category: "Sustainability",
        title: "Plastic Packaging Regulation",
        summary: "New EU directives on single-use plastic packaging effective next quarter. Store readiness is at 65%.",
        image: "https://images.unsplash.com/photo-1611284446314-60a58ac0deb9?auto=format&fit=crop&q=80&w=600&v=3", // Green/Recycle (Robust)
        icon: Leaf,
        color: "bg-teal-600",
        timestamp: "1d",
        url: "https://hbr.org/topic/subject/sustainability"
    },
    {
        id: 8,
        category: "Competitive",
        title: "Competitor Price War",
        summary: "Major competitor launching aggressive markdown campaign in Home Care category starting Monday.",
        image: "https://images.unsplash.com/photo-1607083206869-4c7672e72a8a?auto=format&fit=crop&q=80&w=600&v=3", // Sale Sign
        icon: Globe,
        color: "bg-rose-600",
        timestamp: "2d",
        url: "https://www.retaildive.com/"
    },
    {
        id: 4,
        category: "Tech Adoption",
        title: "POS Modernization",
        summary: "Rollout of new cloud-based POS terminals is 90% complete across all flagship locations.",
        image: "https://images.unsplash.com/photo-1556740738-b6a63e27c4df?auto=format&fit=crop&q=80&w=600&v=3", // Payment Terminal
        icon: Cpu,
        color: "bg-slate-600",
        timestamp: "3d",
        url: "https://www.forbes.com/retail/"
    }
];

const StandardCard = ({ data }: { data: typeof feedData[0] }) => {
    const handleClick = () => {
        if (data.url) {
            window.open(data.url, '_blank', 'noopener,noreferrer');
        }
    };

    return (
        <div onClick={handleClick} className="group bg-white border border-gray-200 hover:border-[#0078d4] h-[280px] flex flex-col cursor-pointer transition-colors duration-200 shadow-sm hover:shadow-md relative overflow-hidden">

            {/* 1. COMPACT FIXED HEIGHT IMAGE (120px) - Taller for visual balance */}
            <div className="h-[120px] w-full relative overflow-hidden shrink-0 bg-gray-100">
                <img
                    src={data.image}
                    alt={data.title}
                    className="w-full h-full object-cover grayscale-[20%] group-hover:grayscale-0 transition-all duration-500 transform group-hover:scale-105"
                    onError={(e) => {
                        (e.target as HTMLImageElement).src = 'https://images.unsplash.com/photo-1531297461136-82bfd4245b71?auto=format&fit=crop&w=800&q=80'; // Reliable Tech
                    }}
                />

                {/* Tag - Top Left */}
                <div className={`absolute top-0 left-0 px-2 py-1 text-[9px] font-bold uppercase tracking-wider flex items-center gap-1.5 text-white ${data.color} bg-opacity-95 backdrop-blur-sm shadow-sm`}>
                    <data.icon size={9} />
                    <span>{data.category}</span>
                </div>
                {/* Time - Top Right */}
                <div className="absolute top-0 right-0 px-1.5 py-1 bg-black/70 backdrop-blur-sm text-[9px] font-medium text-white flex items-center gap-1">
                    <Clock size={9} /> {data.timestamp}
                </div>
            </div>

            {/* 2. CONTENT AREA (Ensured Height) */}
            <div className="p-4 flex flex-col flex-1 overflow-hidden justify-between">
                <div>
                    {/* Headline */}
                    <h3 className="text-[15px] font-bold text-gray-900 leading-tight mb-2 group-hover:text-[#0078d4] transition-colors line-clamp-2">
                        {data.title}
                    </h3>

                    {/* Summary Text */}
                    <p className="text-[12px] text-gray-500 leading-relaxed line-clamp-3 font-serif">
                        {data.summary}
                    </p>
                </div>

                {/* Read More */}
                <div className="flex items-center text-[10px] text-[#0078d4] opacity-0 group-hover:opacity-100 transition-opacity font-bold mt-1">
                    READ MORE <ArrowRight size={10} className="ml-1" />
                </div>
            </div>
        </div>
    );
};

const DashboardPage: React.FC = () => {
    const [filter, setFilter] = useState('All');
    const [isRefreshing, setIsRefreshing] = useState(false);
    const categories = ['All', 'Retail Momentum', 'Consumer Behavior', 'AI & Innovation', 'Supply Chain', 'Market Risk'];

    const handleRefresh = () => {
        setIsRefreshing(true);
        setTimeout(() => setIsRefreshing(false), 800);
    };

    const filteredFeed = filter === 'All' ? feedData : feedData.filter(item => item.category === filter);

    return (
        // Fixed: Removed -m-8 to prevent overlap with app header
        // Adjusted height to work within AppLayout padding
        <div className="flex flex-col h-full bg-[#f8f9fa] overflow-hidden font-sans">
            {/* Styles to aggressively remove any accidental scrollbars */}
            <style>{`
                ::-webkit-scrollbar {
                    display: none;
                }
                * {
                    -ms-overflow-style: none;
                    scrollbar-width: none;
                }
            `}</style>

            {/* COMPACT SINGLE ROW HEADER - PX-4 */}
            <div className="bg-white border-b border-gray-200 px-4 py-2 sticky top-0 z-20 shadow-sm shrink-0 flex items-center justify-between gap-4 h-[50px]">
                {/* LEFT: Logo/Title */}
                <div className="flex items-center gap-2 shrink-0">
                    <h1 className="text-xl font-light text-gray-900 flex items-center gap-2 tracking-tight">
                        RETAIL <span className="font-bold text-gray-900">NOW</span>
                        <span className="relative flex h-2 w-2 mt-0.5">
                            <span className="animate-ping absolute inline-flex h-full w-full bg-red-400 opacity-75"></span>
                            <span className="relative inline-flex h-2 w-2 bg-red-600"></span>
                        </span>
                    </h1>
                    <div className="h-4 w-px bg-gray-300 mx-1"></div>
                    <span className="text-[10px] text-gray-500 uppercase tracking-widest font-medium">Intelligence Pulse</span>
                </div>

                {/* CENTER: Flat Filter Bar */}
                <div className="flex gap-0 border border-gray-200 bg-white shadow-sm overflow-hidden rounded-none">
                    {categories.map(cat => (
                        <button
                            key={cat}
                            onClick={() => setFilter(cat)}
                            className={`px-3 py-1 text-[10px] font-bold transition-all whitespace-nowrap border-r last:border-r-0 border-gray-100 uppercase tracking-wide ${filter === cat
                                ? 'bg-gray-900 text-white'
                                : 'bg-white text-gray-500 hover:bg-gray-50 hover:text-gray-900'
                                }`}
                        >
                            {cat}
                        </button>
                    ))}
                </div>

                {/* RIGHT: Actions */}
                <div className="flex items-center gap-2 shrink-0">
                    <button
                        onClick={handleRefresh}
                        className={`p-2 rounded-none hover:bg-gray-100 text-gray-400 hover:text-gray-900 transition-all ${isRefreshing ? 'animate-spin text-[#0078d4]' : ''}`}
                        title="Refresh Feed"
                    >
                        <RotateCcw size={16} />
                    </button>
                </div>
            </div>

            {/* FULL WIDTH GRID */}
            <div className="w-full px-4 py-4 h-full flex items-center justify-start">
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 w-full">
                    {/* Render Cards - RESTORED TO 8 */}
                    {filteredFeed.slice(0, 8).map((data) => (
                        <StandardCard key={data.id} data={data} />
                    ))}
                </div>
            </div>
        </div>
    );
};

export default DashboardPage;

