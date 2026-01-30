import React from 'react';
import { NavLink } from 'react-router-dom';
import { menuConfig } from "@app/menuConfig";

console.log('Sidebar menuConfig:', menuConfig);

export const Sidebar: React.FC = () => {
  return (
    <div className="w-64 bg-slate-900 text-slate-100 min-h-screen flex flex-col">
      <div className="text-2xl font-bold p-4 border-b border-slate-700">Retail ERP</div>
      <div className="px-3 py-2 bg-red-600 text-white font-bold">Sidebar Visible Test</div>
      <nav className="flex-1 overflow-y-auto p-4 space-y-4">
        {menuConfig.map((section) => (
          <MenuSection key={section.id} item={section} level={0} />
        ))}
      </nav>
    </div>
  );
};

interface MenuItemProps {
  item: any;
  level: number;
}

const MenuSection: React.FC<MenuItemProps> = ({ item, level }) => {
  console.log('Rendering menu item:', item, 'at level', level);

  if (item.disabled) {
    return (
      <div className={`px-3 py-2 rounded-md cursor-default opacity-50 select-none ml-${level * 4}`}>{item.label}</div>
    );
  }

  return (
    <div className={`ml-${level * 4} space-y-1`}>
      {item.path ? (
        <NavLink
          to={item.path}
          className={({ isActive }) =>
            `block px-3 py-2 rounded-md transition-colors ${
              isActive ? 'bg-slate-800 font-semibold' : 'hover:bg-slate-800'
            }`
          }
        >
          {item.label}
        </NavLink>
      ) : (
        <div className="font-semibold text-slate-300 py-1">{item.label}</div>
      )}
      {item.children && item.children.map((child: any) => (
        <MenuSection key={child.id} item={child} level={level + 1} />
      ))}
    </div>
  );
};


