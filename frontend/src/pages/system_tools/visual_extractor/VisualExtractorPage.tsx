import React, { useState, useCallback, useRef } from "react";
import { useNavigate } from "react-router-dom";
import { ScanText, Upload, Clipboard, Trash2, Image as ImageIcon, Copy, Check } from "lucide-react";
import { toast } from "react-toastify";
import { Button } from '@ui/Button';

// ==========================================
// 1. COMPONENTS
// ==========================================

const PanelHeader = ({ title, icon: Icon, children }: { title: string, icon: any, children?: React.ReactNode }) => (
    <div className="flex items-center justify-between px-4 py-3 bg-slate-50 border-b border-slate-200">
        <div className="flex items-center gap-2">
            <Icon size={16} className="text-slate-500" />
            <span className="text-xs font-bold text-slate-700 uppercase tracking-wider">{title}</span>
        </div>
        <div className="flex items-center gap-2">
            {children}
        </div>
    </div>
);

// ==========================================
// 2. MAIN PAGE
// ==========================================

const VisualExtractorPage: React.FC = () => {
    const navigate = useNavigate();
    const fileInputRef = useRef<HTMLInputElement>(null);
    const extractionIdRef = useRef(0);
    const [image, setImage] = useState<string | null>(null);
    const [markdownText, setMarkdownText] = useState<string>("");
    const [isDragging, setIsDragging] = useState(false);
    const [isProcessing, setIsProcessing] = useState(false);
    const [copied, setCopied] = useState(false);

    const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
        const files = e.target.files;
        if (files && files.length > 0) {
            Array.from(files).forEach(processFile);
        }
        // CRITICAL FIX: Reset input value to allow re-selecting the same file
        e.target.value = '';
    };

    const processFile = (file: File) => {
        if (!file.type.startsWith('image/')) {
            toast.error("Please upload an image file");
            return;
        }

        const reader = new FileReader();
        reader.onload = (e) => {
            const dataUrl = e.target?.result as string;
            setImage(dataUrl);
            performExtraction(file);
        };
        reader.readAsDataURL(file);
    };

    const performExtraction = async (file: File) => {
        const currentId = ++extractionIdRef.current;

        setMarkdownText("");
        setIsProcessing(true);

        try {
            const formData = new FormData();
            formData.append("image", file);

            const response = await fetch(
                "http://localhost:8000/api/system-tools/extract-text/",
                {
                    method: "POST",
                    body: formData,
                }
            );

            if (!response.ok) throw new Error("Backend processing failed");

            const data = await response.json();

            if (currentId !== extractionIdRef.current) return;

            if (data.success) {
                setMarkdownText(data.markdown);
                const meta = data.metadata;
                if (meta) {
                    toast.success(`Extraction complete (${meta.processing_time_ms}ms, ${meta.confidence}% confidence)`);
                } else {
                    toast.success("Extraction complete");
                }
            } else {
                throw new Error(data.error || "Unknown error");
            }
        } catch (error: any) {
            if (currentId !== extractionIdRef.current) return;
            setMarkdownText(`# ERROR\n\n${error.message}`);
        } finally {
            if (currentId === extractionIdRef.current) {
                setIsProcessing(false);
            }
        }
    };

    const handlePaste = useCallback((e: React.ClipboardEvent | ClipboardEvent) => {
        const clipboardData = (e as React.ClipboardEvent).clipboardData || (window as any).clipboardData;
        const items = clipboardData?.items;

        if (!items) return;

        for (let i = 0; i < items.length; i++) {
            if (items[i].type.indexOf("image") !== -1) {
                const blob = items[i].getAsFile();
                if (blob) {
                    // Force unique filename to prevent backend caching collisions
                    const uniqueFile = new File([blob], `paste_${Date.now()}.png`, { type: blob.type });

                    // MANDATORY RESET: Clear visual state immediately
                    setImage(null);
                    setMarkdownText("");

                    processFile(uniqueFile);
                    break; // HARD STOP after first image
                }
            }
        }
    }, []);

    const handlePasteFromClipboard = async () => {
        try {
            const items = await navigator.clipboard.read();
            let foundImage = false;
            for (const item of items) {
                const imageTypes = item.types.filter(type => type.startsWith('image/'));
                if (imageTypes.length > 0) {
                    const blob = await item.getType(imageTypes[0]);
                    const file = new File([blob], `pasted_image_${Date.now()}.png`, { type: imageTypes[0] });

                    // MANDATORY RESET: Clear visual state immediately
                    setImage(null);
                    setMarkdownText("");

                    processFile(file);
                    foundImage = true;
                    break; // HARD STOP after first image
                }
            }
            if (!foundImage) {
                toast.info("No image found in clipboard. Use Snipping Tool and then Paste.");
            }
        } catch (err) {
            toast.error("Clipboard access denied. Please use Ctrl+V.");
        }
    };

    const onDragOver = (e: React.DragEvent) => {
        e.preventDefault();
        setIsDragging(true);
    };

    const onDragLeave = () => {
        setIsDragging(false);
    };

    const onDrop = (e: React.DragEvent) => {
        e.preventDefault();
        setIsDragging(false);
        const files = e.dataTransfer.files;
        if (files && files.length > 0) {
            Array.from(files).forEach(processFile);
        }
    };

    const handleClear = () => {
        setImage(null);
        setMarkdownText("");
        setIsProcessing(false);
        if (fileInputRef.current) {
            fileInputRef.current.value = '';
        }
    };

    const handleCopy = () => {
        if (!markdownText) return;
        navigator.clipboard.writeText(markdownText);
        setCopied(true);
        toast.success("Copied to clipboard");
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <div
            className="flex flex-col h-full bg-slate-50 overflow-hidden outline-none"
            onPaste={handlePaste}
            tabIndex={0}
        >
            {/* Toolbar - Astra Universal Pattern */}
            <div className="flex-none z-50 px-4 py-1 bg-[#f3f2f1] border-b border-[#d1d1d1] h-[42px] select-none shadow-sm flex items-center justify-between">
                <div className="flex items-center gap-1">
                    <button
                        onClick={handleCopy}
                        disabled={!markdownText || isProcessing}
                        className="flex items-center gap-2 px-3 py-1.5 hover:bg-white rounded border border-transparent hover:border-[#ccc] transition-all group disabled:opacity-30"
                    >
                        <Copy size={14} className="text-blue-600" />
                        <span className="text-[11px] font-medium text-[#444] group-hover:text-black">Copy (Ctrl+C)</span>
                    </button>
                    <button
                        onClick={handlePasteFromClipboard}
                        className="flex items-center gap-2 px-3 py-1.5 hover:bg-white rounded border border-transparent hover:border-[#ccc] transition-all group"
                        title="Paste from Snipping Tool / Clipboard"
                    >
                        <Clipboard size={14} className="text-amber-600" />
                        <span className="text-[11px] font-medium text-[#444] group-hover:text-black">Paste</span>
                    </button>
                    <button
                        onClick={handleClear}
                        disabled={!image && !markdownText}
                        className="flex items-center gap-2 px-3 py-1.5 hover:bg-white rounded border border-transparent hover:border-[#ccc] transition-all group disabled:opacity-30"
                    >
                        <Trash2 size={14} className="text-red-500" />
                        <span className="text-[11px] font-medium text-[#444] group-hover:text-black">Clear</span>
                    </button>
                    <div className="w-px h-4 bg-gray-300 mx-1"></div>
                    <button onClick={() => navigate(-1)} className="flex items-center gap-2 px-3 py-1.5 hover:bg-white rounded border border-transparent hover:border-[#ccc] transition-all group">
                        <ScanText size={14} className="text-slate-600" />
                        <span className="text-[11px] font-medium text-[#444] group-hover:text-black">Exit</span>
                    </button>
                </div>
                <div className="text-xs font-semibold text-gray-500 tracking-tight italic">
                    Platform Utility: Visual Content Extractor
                </div>
            </div>

            <div className="flex-1 flex overflow-hidden">
                {/* Left Panel - Image Input */}
                <div className="w-[40%] flex flex-col border-r border-slate-200 bg-white shadow-inner">
                    <PanelHeader title="Image Input" icon={ImageIcon}>
                        <label className="cursor-pointer">
                            <input
                                type="file"
                                className="hidden"
                                onChange={handleFileUpload}
                                accept="image/*"
                                ref={fileInputRef}
                            />
                            <div className="flex items-center gap-1.5 px-2 py-1 text-[10px] font-bold text-blue-600 hover:bg-blue-50 transition-colors rounded uppercase tracking-tighter">
                                <Upload size={12} />
                                Upload File
                            </div>
                        </label>
                    </PanelHeader>

                    <div className="flex-1 p-6 flex flex-col overflow-hidden bg-slate-50/50">
                        <div
                            className={`flex-1 border-2 border-dashed rounded-lg flex flex-col items-center justify-center transition-all relative overflow-hidden cursor-pointer ${isDragging ? 'border-blue-500 bg-blue-50/50 shadow-inner' : 'border-slate-300 bg-white hover:border-slate-400'
                                } ${image ? 'border-none bg-black/5' : ''}`}
                            onDragOver={onDragOver}
                            onDragLeave={onDragLeave}
                            onDrop={onDrop}
                            onClick={() => !image && fileInputRef.current?.click()}
                        >
                            {image ? (
                                <img src={image} alt="Preview" className="max-w-full max-h-full object-contain shadow-2xl transition-transform hover:scale-[1.02] duration-300" />
                            ) : (
                                <div className="text-center p-8 pointer-events-none">
                                    <div className="w-20 h-20 bg-slate-100 rounded-full shadow-sm flex items-center justify-center mx-auto mb-6 text-slate-400">
                                        <Upload size={32} />
                                    </div>
                                    <p className="text-sm font-bold text-slate-700 mb-2">Primary Upload Zone</p>
                                    <p className="text-xs text-slate-500 mb-4 px-10 text-center">Drag screenshots here, click to browse, or paste directly with <kbd className="px-1.5 py-0.5 bg-slate-100 border border-slate-300 rounded text-[10px]">Ctrl + V</kbd></p>
                                    <div className="inline-flex items-center gap-2 px-4 py-2 bg-blue-600 text-white rounded text-xs font-bold shadow-md hover:bg-blue-700 transition-colors">
                                        Select Image
                                    </div>
                                </div>
                            )}

                            {isProcessing && (
                                <div className="absolute inset-0 bg-white/60 backdrop-blur-[2px] z-10 flex flex-col items-center justify-center">
                                    <div className="w-12 h-12 border-4 border-blue-600 border-t-transparent rounded-full animate-spin mb-4"></div>
                                    <p className="text-sm font-bold text-blue-800 animate-pulse">Running OCR Pipeline...</p>
                                </div>
                            )}
                        </div>
                    </div>
                </div>

                {/* Right Panel - Extracted Markdown */}
                <div className="w-[60%] flex flex-col bg-white">
                    <PanelHeader title="Extracted Markdown" icon={ScanText}>
                        <div className="flex gap-1">
                            <button
                                onClick={handleCopy}
                                disabled={!markdownText || isProcessing}
                                className="flex items-center gap-1.5 px-2 py-1 text-[10px] font-bold text-slate-600 hover:bg-slate-100 disabled:opacity-30 transition-colors rounded uppercase tracking-tighter"
                            >
                                {copied ? <Check size={12} className="text-emerald-500" /> : <Copy size={12} />}
                                {copied ? 'Copied' : 'Copy'}
                            </button>
                            <button
                                onClick={handleClear}
                                disabled={!image && !markdownText}
                                className="flex items-center gap-1.5 px-2 py-1 text-[10px] font-bold text-red-600 hover:bg-red-50 disabled:opacity-30 transition-colors rounded uppercase tracking-tighter"
                            >
                                <Trash2 size={12} />
                                Clear Result
                            </button>
                        </div>
                    </PanelHeader>

                    <div className="flex-1 p-6 overflow-hidden bg-white">
                        <div className={`h-full border border-slate-200 rounded-lg overflow-hidden flex flex-col transition-all ${isProcessing ? 'opacity-40 animate-pulse' : 'bg-slate-50'}`}>
                            <textarea
                                readOnly
                                value={markdownText}
                                placeholder={isProcessing ? "Processing..." : "Markdown will appear here after ingestion..."}
                                className="flex-1 p-6 text-[13px] font-mono text-slate-700 bg-transparent resize-none focus:outline-none custom-scrollbar leading-relaxed"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default VisualExtractorPage;
