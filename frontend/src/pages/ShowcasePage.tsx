import React, { useState, useEffect } from "react";
import { ChevronRight, ChevronLeft, Maximize2 } from "lucide-react";

// --- PPT SLIDE TEMPLATES ---

// 1. TITLE SLIDE
const TitleSlide = () => (
    <div className="h-full w-full bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 text-white flex flex-col items-center justify-center p-20 relative overflow-hidden">
        {/* Abstract Background Shapes */}
        <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-blue-600/20 rounded-full blur-[100px] -translate-y-1/2 translate-x-1/2"></div>
        <div className="absolute bottom-0 left-0 w-[600px] h-[600px] bg-emerald-600/10 rounded-full blur-[100px] translate-y-1/3 -translate-x-1/4"></div>

        <div className="z-10 flex flex-col items-center text-center animate-fade-in-up">
            <div className="mb-6 px-4 py-2 border-l-4 border-emerald-500 bg-white/5 backdrop-blur-sm">
                <span className="text-emerald-400 font-bold tracking-widest uppercase text-sm">Product Showcase</span>
            </div>
            <h1 className="text-7xl font-extrabold tracking-tight mb-6 leading-tight">
                Olivine <span className="text-blue-400">Retail ERP</span>
            </h1>
            <p className="text-2xl text-slate-300 font-light max-w-2xl mx-auto leading-relaxed">
                Orchestrating excellence through unified intelligence.
            </p>
        </div>

        <div className="absolute bottom-12 text-sm text-slate-500 font-mono tracking-widest uppercase">
            Confidential • 2025 Roadmap
        </div>
    </div>
);

// 2. CONTENT SLIDE (Large Image + Footer Bar)
const ContentSlide = ({ image, title, caption, lines }: { image: string, title: string, caption?: string, lines?: string[] }) => (
    <div className="h-full w-full bg-slate-50 flex flex-col relative overflow-hidden animate-fade-in">

        {/* IMAGE AREA (Full width, dominant) */}
        <div className="flex-1 w-full bg-slate-100 flex items-center justify-center relative p-8">
            <div className="relative h-full w-full flex items-center justify-center shadow-lg bg-white border border-slate-200">
                {/* Image scaling logic to ensure cover while containing content */}
                <img
                    src={image}
                    alt={title}
                    className="w-full h-full object-contain"
                />
            </div>
        </div>

        {/* FOOTER BAR (Deep colored band) */}
        <div className="h-[140px] w-full bg-slate-900 text-white flex flex-col justify-center px-16 relative shrink-0">
            {/* Accent Line */}
            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-blue-500 to-emerald-500"></div>

            <div className="flex items-center justify-between">
                <div>
                    <h2 className="text-3xl font-bold mb-2 tracking-tight">{title}</h2>
                    {caption && <p className="text-slate-300 text-lg font-light leading-snug max-w-4xl">{caption}</p>}
                </div>

                {/* Right side tags */}
                {lines && (
                    <div className="flex flex-col items-end gap-1 text-right">
                        {lines.map((line, i) => (
                            <span key={i} className="text-sm font-medium text-blue-400 bg-blue-900/30 px-3 py-1 rounded-sm uppercase tracking-wide">
                                {line}
                            </span>
                        ))}
                    </div>
                )}
            </div>
        </div>
    </div>
);


// --- MAIN DECK CONTROLLER ---
export const ShowcasePage = () => {
    const [currentSlide, setCurrentSlide] = useState(0);

    const slides = [
        { type: 'title' },
        {
            type: 'content',
            image: '/showcase/login.png',
            title: 'Secure Access',
            caption: 'Enterprise-grade authentication gateway providing workspace-based access control.',
            lines: ['Authentication', 'Single Sign-On']
        },
        {
            type: 'content',
            image: '/showcase/dashboard.png',
            title: 'Intelligence Pulse',
            caption: 'A real-time command center tracking retail momentum, supply chain risks, and market shifts.',
            lines: ['Live Metrics', 'News Feed']
        },
        // --- RETAIL OPERATIONS ---
        {
            type: 'content',
            image: '/showcase/pos_checkout.png',
            title: 'High-Speed Checkout',
            caption: 'Optimized POS interface for rapid transaction processing in high-volume environments.',
            lines: ['Cashier Interface', 'Touch Optimized']
        },
        {
            type: 'content',
            image: '/showcase/pos_daily_ops.png',
            title: 'Shift Management',
            caption: 'Comprehensive controls for opening/closing days, managing cash floats, and shift reconciliation.',
            lines: ['Day Open/Close', 'Cash Drawer']
        },
        {
            type: 'content',
            image: '/showcase/pos_terminals.png',
            title: 'Fleet Configuration',
            caption: 'Centralized management of POS terminals, receipt printers, and hardware profiles.',
            lines: ['Hardware', 'Peripherals']
        },
        // --- SALES ---
        {
            type: 'content',
            image: '/showcase/sales_quotes.png',
            title: 'Proposal Engine',
            caption: 'Generate, track, and convert professional quotations with integrated version control.',
            lines: ['Quotes', 'Estimates']
        },
        {
            type: 'content',
            image: '/showcase/sales_orders.png',
            title: 'Order Fulfillment',
            caption: 'End-to-end order processing from confirmation to logicstics orchestration.',
            lines: ['Order Tracking', 'Status Flow']
        },
        {
            type: 'content',
            image: '/showcase/sales_invoices.png',
            title: 'Billing & Compliance',
            caption: 'Automated invoice generation with region-specific tax calculation and e-invoicing support.',
            lines: ['Invoicing', 'Taxation']
        },
        // --- MERCHANDISING ---
        {
            type: 'content',
            image: '/showcase/catalog.png',
            title: 'Item Master',
            caption: 'Centralized product definition with support for complex hierarchies, variants, and attributes.',
            lines: ['Catalog', 'SKU Mgmt']
        },
        {
            type: 'content',
            image: '/showcase/merch_price_lists.png',
            title: 'Dynamic Pricing',
            caption: 'Manage multiple price books, promotional rules, and customer-specific discount matrices.',
            lines: ['Price Books', 'Promotions']
        },
        // --- INVENTORY ---
        {
            type: 'content',
            image: '/showcase/inventory.png',
            title: 'Inventory Visibility',
            caption: 'Real-time stock levels across all store and warehouse nodes with movement tracking.',
            lines: ['Stock Levels', 'Adjustments']
        },
        // --- PROCUREMENT ---
        {
            type: 'content',
            image: '/showcase/proc_requisitions.png',
            title: 'Demand Planning',
            caption: 'Internal purchase requisition workflows with multi-level approval hierarchies.',
            lines: ['Requisitions', 'Approvals']
        },
        {
            type: 'content',
            image: '/showcase/procurement.png',
            title: 'Supplier Management',
            caption: 'Manage vendor relationships and purchase orders for replenishment.',
            lines: ['Purchase Orders', 'Vendors']
        },
        {
            type: 'content',
            image: '/showcase/proc_goods_receipts.png',
            title: 'Inbound Logistics',
            caption: 'Validate goods receipt against POs with 3-way matching for financial integrity.',
            lines: ['GRN', 'Quality Check']
        },
        // --- CUSTOMERS ---
        {
            type: 'content',
            image: '/showcase/customers.png',
            title: 'Customer 360',
            caption: 'A unified view of customer interactions, purchase history, and loyalty status.',
            lines: ['CRM', 'Loyalty']
        },
        // --- CONFIG ---
        {
            type: 'content',
            image: '/showcase/setup_company.png',
            title: 'Enterprise Config',
            caption: 'Define multi-entity structures, tax settings, and global system parameters.',
            lines: ['Multi-Company', 'Settings']
        }
    ];

    const nextSlide = () => setCurrentSlide(prev => Math.min(prev + 1, slides.length - 1));
    const prevSlide = () => setCurrentSlide(prev => Math.max(prev - 1, 0));

    // Keyboard Navigation
    useEffect(() => {
        const handleKeyDown = (e: KeyboardEvent) => {
            if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') nextSlide();
            if (e.key === 'ArrowLeft') prevSlide();
        };
        window.addEventListener('keydown', handleKeyDown);
        return () => window.removeEventListener('keydown', handleKeyDown);
    }, []);

    const slide = slides[currentSlide];

    return (
        <div className="h-screen w-screen bg-black flex items-center justify-center font-sans overflow-hidden">

            {/* PPT SLIDE CONTAINER (Fixed Aspect Ratio 16:9) */}
            <div className="aspect-video h-full w-full max-w-[177.78vh] max-h-[56.25vw] bg-white shadow-2xl relative overflow-hidden">

                {slide.type === 'title' && <TitleSlide />}
                {slide.type === 'content' && (
                    <ContentSlide
                        image={slide.image!}
                        title={slide.title!}
                        caption={slide.caption}
                        lines={slide.lines}
                    />
                )}

                {/* SLIDE NUMBER (Subtle overlay) */}
                <div className="absolute bottom-4 right-4 text-[10px] text-slate-400 font-mono opacity-50">
                    {currentSlide + 1} / {slides.length}
                </div>

            </div>

            {/* Global Animation Styles */}
            <style>{`
                @keyframes fade-in-up {
                    0% { opacity: 0; transform: translateY(20px); }
                    100% { opacity: 1; transform: translateY(0); }
                }
                @keyframes fade-in {
                    0% { opacity: 0; }
                    100% { opacity: 1; }
                }
                .animate-fade-in-up { animation: fade-in-up 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
                .animate-fade-in { animation: fade-in 0.5s ease-out forwards; }
            `}</style>
        </div>
    );
};

