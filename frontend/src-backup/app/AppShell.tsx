import React from 'react';
import { Outlet, useLocation, Navigate } from 'react-router-dom';
import { Sidebar } from '../components/layout/Sidebar';
import { Topbar } from '../components/layout/Topbar';

export const AppShell: React.FC = () => {
  const location = useLocation();

  console.log('AppShell rendering');

  const token = localStorage.getItem('erp_auth_token');
  if (!token && location.pathname !== '/login') {
    return <Navigate to="/login" replace />;
  }

  if (location.pathname === '/login') {
    return <Outlet />;
  }

  return (
    <div className="min-h-screen flex bg-slate-100">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Topbar />
        <main className="flex-1 overflow-auto">
          <Outlet />
        </main>
      </div>
    </div>
  );
};


