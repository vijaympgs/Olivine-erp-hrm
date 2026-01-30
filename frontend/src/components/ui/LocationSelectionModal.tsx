import React from 'react';

interface LocationSelectionModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSelect: (location: any) => void;
}

export const LocationSelectionModal: React.FC<LocationSelectionModalProps> = ({ isOpen, onClose, onSelect }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <div className="absolute inset-0 bg-black bg-opacity-50" onClick={onClose} />
      <div className="relative bg-white rounded-lg shadow-lg max-w-md w-full mx-4 p-6">
        <h3 className="text-lg font-medium text-gray-900 mb-4">Select Location</h3>
        <p className="text-sm text-gray-500">Location selection modal - stub component</p>
        <div className="flex justify-end space-x-3 mt-6">
          <button
            onClick={onClose}
            className="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
};
