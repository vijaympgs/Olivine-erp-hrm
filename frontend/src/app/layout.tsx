import React from "react";
import { Outlet, useLocation } from "react-router-dom";
import { Sidebar } from "@ui/Sidebar";
import { AppHeader } from "@ui/AppHeader";
import { ChatBot } from "@ui/ChatBot";

export const AppLayout: React.FC = () => {
  const location = useLocation();

  // Hide sidebar only for full-screen apps: POS billing and test console
  const isFullScreenApp = location.pathname === '/pos/ui' ||
    location.pathname === '/test-console' ||
    location.pathname === '/operations/pos/pos' ||
    location.pathname === '/pos/billing' ||
    location.pathname === '/system-tools/dataops-studio' ||
    location.pathname === '/admin/file-search';

  // Remove padding and max-width for full-screen apps
  const mainClassName = isFullScreenApp
    ? "flex-1 overflow-auto"
    : "flex-1 overflow-auto p-6 pt-16 max-w-7xl mx-auto w-full";

  return (
    <div className="flex flex-col h-screen bg-olivine-bg overflow-hidden">
      <AppHeader />
      <div className="flex flex-1 overflow-hidden">
        {!isFullScreenApp && <Sidebar />}
        <main className={mainClassName.replace('pt-16', '')}>
          <Outlet />
        </main>
      </div>
      <ChatBot />
    </div>
  );
};
