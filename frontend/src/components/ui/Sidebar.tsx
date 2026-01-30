import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { 
  ChevronDown, ChevronRight, LayoutDashboard, Users, Database, 
  User, UserCheck, FileText, TrendingUp, UserPlus, DollarSign, Clock, 
  Target, BookOpen, Heart, Briefcase, Shield, LogOut, Link, Bot, Copy,
  Lock, FileSearch, ScanText, Database as DatabaseIcon, Code, Network
} from 'lucide-react';
import { menuConfig } from '../../app/menuConfig';
import { layoutManager } from '../../config/layoutConfig';

// Icon mapping
const iconMap: Record<string, React.ElementType> = {
  LayoutDashboard,
  Users,
  Database,
  Network,
  User,
  UserCheck,
  FileText,
  TrendingUp,
  UserPlus,
  DollarSign,
  Clock,
  Target,
  BookOpen,
  Heart,
  Briefcase,
  Shield,
  LogOut,
  Link,
  Bot,
  Copy,
  Wrench: Target,
  FileSearch,
  ScanText,
  DatabaseIcon,
  Code,
  PieChart: Target,
  FileInput: FileText,
  Filter: Target,
  Calendar: Clock,
  FileCheck: FileText,
  List: FileText,
  Calculator: Target,
  Play: Target,
  Watch: Clock,
  CheckSquare: Target,
  Flag: Target,
  Star: Target,
  MonitorPlay: Target,
  Map: Target,
  Award: Target,
  MessageCircle: Target,
  Medal: Target,
  Activity: Target,
  CalendarHeart: Target,
  GitBranch: Target,
  BarChart2: Target,
  Book: Target,
  Monitor: Target,
  FileMinus: FileText,
  MessageSquare: Target,
  Box: Target,
  ShieldCheck: Target,
  Server: Target,
  Key: Target,
  Gift: Target,
  Sparkles: Target,
  File: FileText,
};

interface MenuItemProps {
  item: {
    id: string;
    label: string;
    icon?: string;
    path?: string;
    children?: MenuItemProps['item'][];
  };
  level: number;
  expandedItems: Set<string>;
  toggleExpand: (id: string) => void;
}

const MenuItem: React.FC<MenuItemProps> = ({ item, level, expandedItems, toggleExpand }) => {
  const navigate = useNavigate();
  const location = useLocation();
  const config = layoutManager.getConfig();
  const hasChildren = item.children && item.children.length > 0;
  const isExpanded = expandedItems.has(item.id);
  const isActive = item.path && location.pathname === item.path;
  const Icon = item.icon ? iconMap[item.icon] : null;

  const handleClick = () => {
    if (hasChildren) {
      toggleExpand(item.id);
    } else if (item.path) {
      navigate(item.path);
    }
  };

  // Get text color based on level
  const getTextColor = (lvl: number) => {
    switch (lvl) {
      case 0: return config.sidebar.menuText.level0Color;
      case 1: return config.sidebar.menuText.level1Color;
      case 2: return config.sidebar.menuText.level2Color;
      case 3: return config.sidebar.menuText.level3Color;
      default: return config.sidebar.menuText.level1Color;
    }
  };

  // Get font size based on level
  const getFontSize = (lvl: number) => {
    switch (lvl) {
      case 0: return config.sidebar.menuText.level0FontSize;
      case 1: return config.sidebar.menuText.level1FontSize;
      case 2: return config.sidebar.menuText.level2FontSize;
      case 3: return config.sidebar.menuText.level3FontSize;
      default: return config.sidebar.menuText.level1FontSize;
    }
  };

  // Get font weight based on level
  const getFontWeight = (lvl: number) => {
    switch (lvl) {
      case 0: return config.sidebar.menuText.level0FontWeight;
      case 1: return config.sidebar.menuText.level1FontWeight;
      case 2: return config.sidebar.menuText.level2FontWeight;
      case 3: return config.sidebar.menuText.level3FontWeight;
      default: return config.sidebar.menuText.level1FontWeight;
    }
  };

  // Get padding based on spacing setting
  const getPaddingY = () => {
    switch (config.sidebar.menuItemSpacing) {
      case 'compact': return 'py-1';
      case 'normal': return 'py-2';
      case 'comfortable': return 'py-3';
      default: return 'py-2';
    }
  };

  // Get active item style based on selection style
  const getActiveStyle = () => {
    if (!isActive) return {};
    
    const selectionStyle = config.sidebar.menuSelection;
    const activeItem = config.activeMenuItem;
    
    switch (selectionStyle.style) {
      case 'flat':
        return {
          backgroundColor: activeItem.backgroundColor,
          color: activeItem.textColor,
          fontWeight: activeItem.fontWeight,
        };
      case 'left-border':
        return {
          borderLeft: `${activeItem.borderWidth}px solid ${activeItem.borderColor}`,
          backgroundColor: activeItem.backgroundColor,
          color: activeItem.textColor,
        };
      case 'rounded':
        return {
          backgroundColor: activeItem.backgroundColor,
          color: activeItem.textColor,
          borderRadius: selectionStyle.borderRadius,
        };
      case 'pill':
        return {
          backgroundColor: activeItem.backgroundColor,
          color: activeItem.textColor,
          borderRadius: '9999px',
        };
      default:
        return {
          backgroundColor: activeItem.backgroundColor,
          color: activeItem.textColor,
        };
    }
  };

  return (
    <div>
      <button
        onClick={handleClick}
        className={`w-full flex items-center space-x-2 text-sm font-medium transition-colors ${getPaddingY()}`}
        style={{
          paddingLeft: `${level * 12 + 12}px`,
          color: isActive ? undefined : getTextColor(level),
          fontSize: getFontSize(level),
          fontWeight: getFontWeight(level),
          ...getActiveStyle(),
        }}
      >
        {Icon && <Icon className="w-4 h-4 flex-shrink-0" />}
        <span className="flex-1 text-left truncate">{item.label}</span>
        {hasChildren && (
          <span className="flex-shrink-0">
            {isExpanded ? <ChevronDown className="w-4 h-4" /> : <ChevronRight className="w-4 h-4" />}
          </span>
        )}
      </button>
      {hasChildren && isExpanded && item.children && (
        <div className="mt-1">
          {item.children.map((child: any) => (
            <MenuItem
              key={child.id}
              item={child}
              level={level + 1}
              expandedItems={expandedItems}
              toggleExpand={toggleExpand}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export const Sidebar: React.FC = () => {
  const [expandedItems, setExpandedItems] = useState<Set<string>>(new Set(['platform', 'hrm']));
  const config = layoutManager.getConfig();

  const toggleExpand = (id: string) => {
    setExpandedItems(prev => {
      const newSet = new Set(prev);
      if (newSet.has(id)) {
        newSet.delete(id);
      } else {
        newSet.add(id);
      }
      return newSet;
    });
  };

  // Filter menu items based on visibility settings
  const filteredMenuConfig = menuConfig.filter(item => {
    if (item.id === 'hrm') return config.sidebar.showHRM;
    if (item.id === 'retail') return config.sidebar.showRetail;
    if (item.id === 'fms') return config.sidebar.showFinance;
    if (item.id === 'crm') return config.sidebar.showCRM;
    return true;
  });

  return (
    <div 
      className="flex flex-col h-full overflow-y-auto"
      style={{
        width: `${config.sidebar.width}px`,
        backgroundColor: config.sidebar.backgroundColor,
        borderColor: config.sidebar.borderColor,
      }}
    >
      <div 
        className="p-4 border-b"
        style={{ borderColor: config.sidebar.dividerColor }}
      >
        <h1 
          className="text-xl font-bold"
          style={{ color: config.sidebar.menuText.level0Color }}
        >
          Olivine HRM
        </h1>
        <p 
          className="text-xs mt-1"
          style={{ color: config.sidebar.menuText.level1Color }}
        >
          Human Resource Management
        </p>
      </div>
      
      <nav className="flex-1 py-4">
        <ul className="space-y-1">
          {filteredMenuConfig.map((item: any) => (
            <MenuItem
              key={item.id}
              item={item}
              level={0}
              expandedItems={expandedItems}
              toggleExpand={toggleExpand}
            />
          ))}
        </ul>
      </nav>
    </div>
  );
};
