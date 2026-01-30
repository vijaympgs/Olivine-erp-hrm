import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AppShell } from './AppShell';
import { DashboardPage } from '../modules/dashboard/pages/DashboardPage';
import { CompanyPage } from '../modules/company/CompanyPage';
import { LoginPage } from '../modules/auth/LoginPage';

export const AppRoutes: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />

        <Route path="/*" element={<AppShell />}>  {/* Main protected routes with sidebar/topbar */}
          <Route path="dashboard" element={<DashboardPage />} />
          <Route path="setup/company" element={<CompanyPage />} />
          <Route path="setup/locations" element={<div className="p-6">Locations Placeholder</div>} />
          <Route path="procurement" element={<div className="p-6">Procurement Placeholder</div>} />
          <Route path="inventory" element={<div className="p-6">Inventory Placeholder</div>} />
          <Route path="pricing" element={<div className="p-6">Pricing Placeholder</div>} />
          <Route path="pos" element={<div className="p-6">POS Placeholder</div>} />
          <Route path="finance" element={<div className="p-6">Finance Placeholder</div>} />
          <Route path="analytics" element={<div className="p-6">Analytics Placeholder</div>} />
          <Route path="admin" element={<div className="p-6">Admin Placeholder</div>} />
          <Route path="*" element={<Navigate to="/dashboard" />} />
        </Route>
      </Routes>
    </Router>
  );
}


