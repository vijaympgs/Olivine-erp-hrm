import React from 'react';

interface TransactionToolbarProps {
  onSave?: () => void;
  onCancel?: () => void;
  onPrint?: () => void;
  actions?: Array<{ id: string; label: string }>;
}

export const TransactionToolbar: React.FC<TransactionToolbarProps> = ({ 
  onSave, 
  onCancel, 
  onPrint,
  actions = []
}) => {
  return (
    <div className="bg-white border-b border-gray-200 px-4 py-2">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-2">
          {actions.map(action => (
            <button
              key={action.id}
              className="px-3 py-1.5 text-sm font-medium text-gray-700 hover:bg-gray-100 rounded-md transition-colors"
            >
              {action.label}
            </button>
          ))}
        </div>
        <div className="flex items-center space-x-2">
          {onSave && (
            <button
              onClick={onSave}
              className="px-3 py-1.5 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700"
            >
              Save
            </button>
          )}
          {onPrint && (
            <button
              onClick={onPrint}
              className="px-3 py-1.5 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
            >
              Print
            </button>
          )}
          {onCancel && (
            <button
              onClick={onCancel}
              className="px-3 py-1.5 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
            >
              Cancel
            </button>
          )}
        </div>
      </div>
    </div>
  );
};
