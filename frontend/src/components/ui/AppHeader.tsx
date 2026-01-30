import React, { useState, useEffect } from 'react';
import { Search, Bell, User, LogOut, ChevronRight } from 'lucide-react';
import { useLocation } from 'react-router-dom';
import { layoutManager } from '../../config/layoutConfig';

export const AppHeader: React.FC = () => {
  const location = useLocation();
  const config = layoutManager.getConfig();
  const [searchQuery, setSearchQuery] = useState('');
  const [showNotifications, setShowNotifications] = useState(false);
  const [showUserMenu, setShowUserMenu] = useState(false);

  // Build breadcrumb path from current route
  const buildBreadcrumb = () => {
    const path = location.pathname;
    const parts = path.split('/').filter(Boolean);
    
    const breadcrumbMap: Record<string, string> = {
      'hr': 'Human Resources',
      'employees': 'Employee Management',
      'records': 'Employee Records',
      'admin': 'System Administration',
      'layout-settings': 'Layout Settings',
      'users': 'User Management',
    };

    const breadcrumbs: Array<{ label: string; path: string }> = [];
    let currentPath = '';

    parts.forEach((part, index) => {
      currentPath += `/${part}`;
      const label = breadcrumbMap[part] || part.charAt(0).toUpperCase() + part.slice(1);
      breadcrumbs.push({ label, path: currentPath });
    });

    return breadcrumbs;
  };

  const breadcrumbs = buildBreadcrumb();

  // Apply header styles from config
  const headerStyle: React.CSSProperties = {
    height: `${config.header.height}px`,
    backgroundColor: config.header.bgStyle === 'gradient' 
      ? `linear-gradient(to right, ${config.header.gradientStart}, ${config.header.gradientEnd})`
      : config.header.bgColor,
    borderColor: config.header.borderColor,
  };

  return (
    <header 
      className="flex items-center justify-between px-6 border-b"
      style={headerStyle}
    >
      {/* Left: Breadcrumb */}
      <div className="flex items-center space-x-2">
        {breadcrumbs.length > 0 && (
          <nav className="flex items-center space-x-2">
            {breadcrumbs.map((crumb, index) => (
              <React.Fragment key={crumb.path}>
                <span 
                  className="text-sm font-medium hover:underline cursor-pointer"
                  style={{ color: config.header.companyColor || '#374151' }}
                >
                  {crumb.label}
                </span>
                {index < breadcrumbs.length - 1 && (
                  <ChevronRight 
                    size={14} 
                    className="text-gray-400" 
                  />
                )}
              </React.Fragment>
            ))}
          </nav>
        )}
      </div>

      {/* Center: Search */}
      {config.header.showSearch && (
        <div className="flex-1 max-w-xl mx-8">
          <div className="relative">
            <Search 
              className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" 
              size={16}
            />
            <input
              type="text"
              placeholder="Search..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm"
              style={{ backgroundColor: 'rgba(255, 255, 255, 0.9)' }}
            />
          </div>
        </div>
      )}

      {/* Right: Notifications, User Menu */}
      <div className="flex items-center space-x-4">
        {config.header.showNotifications && (
          <button
            className="relative p-2 rounded-full hover:bg-white/20 transition-colors"
            onClick={() => setShowNotifications(!showNotifications)}
          >
            <Bell size={20} style={{ color: config.header.iconColor || '#6B7280' }} />
            <span className="absolute top-0 right-0 w-2 h-2 bg-red-500 rounded-full"></span>
          </button>
        )}

        {config.header.showUserMenu && (
          <div className="relative">
            <button
              className="flex items-center space-x-2 p-2 rounded-lg hover:bg-white/20 transition-colors"
              onClick={() => setShowUserMenu(!showUserMenu)}
            >
              <div 
                className="w-8 h-8 rounded-full flex items-center justify-center text-white font-bold"
                style={{ backgroundColor: config.header.brandColor || '#3B82F6' }}
              >
                JD
              </div>
              <div className="text-left">
                <div 
                  className="text-sm font-medium"
                  style={{ color: config.header.companyColor || '#374151' }}
                >
                  John Doe
                </div>
                <div className="text-xs text-gray-500">Administrator</div>
              </div>
            </button>

            {showUserMenu && (
              <div className="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg border border-gray-200 py-2 z-50">
                <button className="w-full px-4 py-2 text-left text-sm hover:bg-gray-100 flex items-center space-x-2">
                  <User size={16} />
                  <span>Profile</span>
                </button>
                <button className="w-full px-4 py-2 text-left text-sm hover:bg-gray-100 flex items-center space-x-2">
                  <LogOut size={16} />
                  <span>Logout</span>
                </button>
              </div>
            )}
          </div>
        )}
      </div>
    </header>
  );
};
