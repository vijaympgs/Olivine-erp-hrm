import React from 'react';

interface PageContainerProps {
  children: React.ReactNode;
}

export const PageContainer: React.FC<PageContainerProps> = ({ children }) => {
  return <div className="p-6 max-w-6xl mx-auto space-y-6">{children}</div>;
};

