import React, { useRef } from 'react';
import { MasterToolbar } from "@core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";
import { useNavigate } from 'react-router-dom';

const FileSearchExplorerPage: React.FC = () => {
    const navigate = useNavigate();
    const iframeRef = useRef<HTMLIFrameElement>(null);

    return (
        <div className="flex flex-col h-full bg-white">
            <MasterToolbar
                viewId="FILE_SEARCH_EXPLORER"
                mode={"Explorer" as any}
                allowedActions={['exit']}
                showLabels={true}
                onAction={(action: string) => {
                    if (action === 'exit') {
                        navigate(-1);
                    }
                    console.log('Action:', action);
                }}
            />

            <div className="flex-1 overflow-hidden relative z-10">
                <iframe
                    ref={iframeRef}
                    src="/file-search-explorer.html"
                    tabIndex={0}
                    allow="clipboard-read; clipboard-write; keyboard-map"
                    className="w-full h-full border-none pointer-events-auto"
                    style={{ position: "relative", zIndex: 10 }}
                    title="File Search Explorer"
                    onLoad={() => {
                        iframeRef.current?.focus();
                        iframeRef.current?.contentWindow?.postMessage(
                            { type: "FOCUS_SEARCH" },
                            "*"
                        );
                    }}
                    onClick={() => {
                        iframeRef.current?.focus();
                    }}
                />
            </div>
        </div>
    );
};

export default FileSearchExplorerPage;
