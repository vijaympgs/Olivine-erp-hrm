import React from "react";
import { createBrowserRouter, Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../auth/useAuth";
import { LoginPage } from "../pages/LoginPage";
import { LocationSelectionPage } from "../pages/Auth/LocationSelectionPage";
import { ShowcasePage } from "../pages/ShowcasePage";
import DashboardPage from "../pages/DashboardPage";
import { AppLayout } from "./layout";
import { CompanySettings } from "../pages/CompanySettings";
import { LocationSetup } from "../pages/LocationSetup";
import EmployeeMasterPage from "../pages/hr/EmployeeMasterPage";
import EmployeeDirectoryPage from "@hrm/src/pages/EmployeeDirectory";
import { EmployeeRecords } from "@hrm/src/pages/EmployeeRecords";
import LayoutSettingsPage from "../pages/admin/LayoutSettingsPage";
// User management pages - commented out as they may not exist in HRM-only mode
// import UserAndPermissionPage from "@core/auth-access/frontend/user-management/pages/UserAndPermissionPage";
// import UserManagementPage from "@core/auth-access/frontend/user-management/pages/UserManagementPage";
import { ProfilePage } from "../pages/Settings/ProfilePage";
import { SimpleMasterSetup } from "../pages/setup/SimpleMasterSetup";
import { TestConsolePage } from "../pages/TestConsolePage";
import FileSearchExplorerPage from "../pages/admin/FileSearchExplorerPage";
import VisualExtractorPage from "../pages/system_tools/visual_extractor/VisualExtractorPage";
import DataOpsStudioPage from "../pages/system_tools/dataops_studio/DataOpsStudioPage";
import HtmlPreviewPage from "../pages/system_tools/html_preview/HtmlPreviewPage";
import HRMDashboardPage from "@hrm/src/pages/Dashboard";
import OrganizationalChart from "@hrm/src/pages/OrganizationalChart";
import ProfileViewPage from "@hrm/src/pages/ProfileView";
import EmployeeSelfServicePage from "@hrm/src/pages/EmployeeSelfService";
import EmployeeLifecyclePage from "@hrm/src/pages/EmployeeLifecycle";

const RequireAuth: React.FC = () => {
  const { isAuthenticated, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div className="flex h-screen items-center justify-center text-sm text-olivine-muted">
        Loading...
      </div>
    );
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <Outlet />;
};

export const router = createBrowserRouter([
  {
    path: "/login",
    element: <LoginPage />
  },
  {
    path: "/location-selection",
    element: <LocationSelectionPage />
  },
  {
    path: "/showcase",
    element: <ShowcasePage />
  },
  {
    element: <RequireAuth />,
    children: [
      {
        path: "/",
        element: <AppLayout />,
        children: [
          { path: "/", element: <HRMDashboardPage /> },
          { path: "test-console", element: <TestConsolePage /> },
          { path: "setup/simple-masters", element: <SimpleMasterSetup /> },
          { path: "setup/company", element: <CompanySettings /> },
          { path: "setup/locations", element: <LocationSetup /> },
          { path: "hr/employees", element: <EmployeeDirectoryPage /> },
          { path: "hr/employee-master", element: <EmployeeRecords /> },
          { path: "admin/layout-settings", element: <LayoutSettingsPage /> },
          // { path: "admin/user-permissions", element: <UserAndPermissionPage /> },
          { path: "admin", element: <Navigate to="admin/layout-settings" replace /> },
          { path: "setup", element: <Navigate to="setup/company" replace /> },
          // { path: "admin/users", element: <UserManagementPage /> },
          { path: "admin/file-search", element: <FileSearchExplorerPage /> },
          { path: "system-tools/visual-extractor", element: <VisualExtractorPage /> },
          { path: "system-tools/dataops-studio", element: <DataOpsStudioPage /> },
          { path: "system-tools/html-preview", element: <HtmlPreviewPage /> },
          { path: "hr/dashboard", element: <HRMDashboardPage /> },
          { path: "hr/employees/records", element: <EmployeeRecords /> },
          { path: "hr/employees/org-chart", element: <OrganizationalChart /> },
          { path: "hr/employees/profile", element: <ProfileViewPage /> },
          { path: "hr/employees/profile/:id", element: <ProfileViewPage /> },
          { path: "hr/employees/self-service", element: <EmployeeSelfServicePage /> },
          { path: "hr/employees/self-service/request/new", element: <EmployeeSelfServicePage /> },
          { path: "hr/employees/lifecycle", element: <EmployeeLifecyclePage /> },
          { path: "hr/*", element: <HRMDashboardPage /> },
          { path: "settings/profile", element: <ProfilePage /> }
        ]
      }
    ]
  },
  { path: "*", element: <Navigate to="/" replace /> }
]);
