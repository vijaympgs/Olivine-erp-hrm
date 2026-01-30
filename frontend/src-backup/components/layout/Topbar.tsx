import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { menuConfig } from "@app/menuConfig";

function findLabelByPath(path: string, menus: any[]): string | null {
  for (const menu of menus) {
    if (menu.path === path) return menu.label;
    if (menu.children) {
      const found = findLabelByPath(path, menu.children);
      if (found) return found;
    }
  }
  return null;
}

export const Topbar: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const currentLabel = findLabelByPath(location.pathname, menuConfig) || '';

  const handleLogout = () => {
    localStorage.removeItem('erp_auth_token');
    navigate('/login');
  };

  return (
    <div className="flex items-center justify-between bg-white px-6 py-4 border-b border-gray-200">
      <div className="text-xl font-semibold">{currentLabel}</div>
      <div className="flex items-center space-x-4">
        <div className="w-8 h-8 rounded-full bg-gray-400 flex items-center justify-center text-white font-bold">VM</div>
        <button
          onClick={handleLogout}
          className="px-3 py-1 rounded bg-red-600 text-white hover:bg-red-700"
        >
          Logout
        </button>
      </div>
    </div>
  );
};

