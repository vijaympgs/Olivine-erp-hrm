import React, { useEffect, useState } from 'react';
import { X, BookOpen } from 'lucide-react';
import ReactMarkdown from 'react-markdown';

interface PlatformVersionModalProps {
    isOpen: boolean;
    onClose: () => void;
}

export const PlatformVersionModal: React.FC<PlatformVersionModalProps> = ({ isOpen, onClose }) => {
    const [content, setContent] = useState<string>('');
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        if (isOpen) {
            // Fetch the markdown file
            fetch('/PLATFORM_VERSION_INFO.md')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Failed to load version information');
                    }
                    return response.text();
                })
                .then(text => {
                    setContent(text);
                    setLoading(false);
                })
                .catch(err => {
                    setError(err.message);
                    setLoading(false);
                });
        }
    }, [isOpen]);

    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 z-[9999] flex items-center justify-center bg-black/60 backdrop-blur-sm">
            {/* Modal Container */}
            <div className="relative w-full max-w-6xl h-[90vh] bg-white shadow-2xl rounded-lg overflow-hidden border border-gray-200">

                {/* Header */}
                <div className="flex items-center justify-between px-6 py-4 bg-gradient-to-r from-purple-900 to-gray-900 text-white border-b border-purple-800">
                    <div className="flex items-center gap-3">
                        <BookOpen className="w-6 h-6" />
                        <div>
                            <h2 className="text-xl font-bold tracking-tight text-yellow-300">Platform Version Information (Current-Advanced Version)</h2>
                            <p className="text-xs text-purple-200 mt-0.5">Olivine Platform v3.0 - Comprehensive Overview</p>
                            <p className="text-[10px] text-purple-300/70 mt-1 font-mono">
                                📦 Repo: vijaympgs/olvine-erp
                            </p>
                        </div>
                    </div>
                    <button
                        onClick={onClose}
                        className="p-2 hover:bg-white/10 rounded-lg transition-colors"
                        aria-label="Close"
                    >
                        <X className="w-5 h-5" />
                    </button>
                </div>

                {/* Content */}
                <div className="h-[calc(90vh-80px)] overflow-y-auto bg-gray-50">
                    <div className="max-w-5xl mx-auto px-8 py-6">
                        {loading && (
                            <div className="flex items-center justify-center h-64">
                                <div className="text-center">
                                    <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-purple-600 mx-auto mb-4"></div>
                                    <p className="text-gray-600">Loading version information...</p>
                                </div>
                            </div>
                        )}

                        {error && (
                            <div className="bg-red-50 border-l-4 border-red-500 p-4 rounded">
                                <p className="text-red-700 font-medium">Error: {error}</p>
                            </div>
                        )}

                        {!loading && !error && (
                            <div className="prose prose-sm max-w-none prose-headings:font-bold prose-h1:text-3xl prose-h1:text-purple-900 prose-h1:border-b prose-h1:border-purple-200 prose-h1:pb-2 prose-h2:text-2xl prose-h2:text-gray-800 prose-h2:mt-8 prose-h3:text-xl prose-h3:text-gray-700 prose-p:text-gray-600 prose-a:text-purple-600 prose-a:no-underline hover:prose-a:underline prose-code:text-purple-600 prose-code:bg-purple-50 prose-code:px-1 prose-code:py-0.5 prose-code:rounded prose-pre:bg-gray-900 prose-pre:text-gray-100 prose-strong:text-gray-900 prose-table:text-sm prose-th:bg-purple-100 prose-th:text-purple-900 prose-td:border-gray-300">
                                <ReactMarkdown>{content}</ReactMarkdown>
                            </div>
                        )}
                    </div>
                </div>

                {/* Footer */}
                <div className="absolute bottom-0 left-0 right-0 px-6 py-3 bg-gray-100 border-t border-gray-200 flex items-center justify-between">
                    <p className="text-xs text-gray-500">
                        Press <kbd className="px-2 py-1 bg-white border border-gray-300 rounded shadow-sm font-mono text-xs">Ctrl</kbd> + <kbd className="px-2 py-1 bg-white border border-gray-300 rounded shadow-sm font-mono text-xs">L</kbd> to toggle this window
                    </p>
                    <button
                        onClick={onClose}
                        className="px-4 py-2 bg-gray-900 text-white text-sm font-medium rounded hover:bg-gray-800 transition-colors"
                    >
                        Close
                    </button>
                </div>
            </div>
        </div>
    );
};
