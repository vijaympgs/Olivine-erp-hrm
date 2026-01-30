import React from 'react';

export type MasterMode = 'LIST' | 'VIEW' | 'EDIT' | 'CREATE';

interface MasterToolbarProps {
  viewId: string;
  mode: MasterMode;
  onAction: (action: string) => void;
  selectedCount?: number;
}

export const MasterToolbar: React.FC<MasterToolbarProps> = ({ viewId, mode, onAction, selectedCount = 0 }) => {
  const getActions = (): Array<{ id: string; label: string; icon: string }> => {
    switch (mode) {
      case 'LIST':
        return [
          { id: 'new', label: 'New', icon: '+' },
          { id: 'refresh', label: 'Refresh', icon: '↻' },
          { id: 'search', label: 'Search', icon: '🔍' },
          { id: 'filter', label: 'Filter', icon: '⚙' },
          { id: 'view', label: 'View', icon: '👁' },
          { id: 'edit', label: 'Edit', icon: '✎' },
          { id: 'delete', label: 'Delete', icon: '🗑' },
          { id: 'import', label: 'Import', icon: '↑' },
          { id: 'export', label: 'Export', icon: '↓' },
          { id: 'exit', label: 'Exit', icon: '✕' },
        ];
      case 'VIEW':
        return [
          { id: 'edit', label: 'Edit', icon: '✎' },
          { id: 'delete', label: 'Delete', icon: '🗑' },
          { id: 'exit', label: 'Exit', icon: '✕' },
        ];
      case 'EDIT':
      case 'CREATE':
        return [
          { id: 'save', label: 'Save', icon: '💾' },
          { id: 'clear', label: 'Clear', icon: '🧹' },
          { id: 'exit', label: 'Exit', icon: '✕' },
        ];
      default:
        return [];
    }
  };

  const actions = getActions();
  
  // Selection-aware enable/disable for LIST mode
  const isActionDisabled = (actionId: string): boolean => {
    if (mode !== 'LIST') return false;
    
    switch (actionId) {
      case 'view':
      case 'edit':
        return selectedCount !== 1;
      case 'delete':
        return selectedCount === 0;
      default:
        return false;
    }
  };

  return (
    <div className="bg-white border-b border-gray-200 px-4 py-2">
      <div className="flex items-center space-x-2">
        <span className="text-sm font-medium text-gray-700 mr-4">{viewId}</span>
        <span className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded">{mode}</span>
        <div className="h-4 w-px bg-gray-300 mx-2" />
        {actions.map(action => (
          <button
            key={action.id}
            onClick={() => onAction(action.id)}
            disabled={isActionDisabled(action.id)}
            className={`px-3 py-1.5 text-sm font-medium rounded-md transition-colors ${
              isActionDisabled(action.id)
                ? 'text-gray-400 cursor-not-allowed'
                : 'text-gray-700 hover:bg-gray-100'
            }`}
          >
            <span className="mr-1">{action.icon}</span>
            {action.label}
          </button>
        ))}
      </div>
    </div>
  );
};
