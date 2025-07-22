import React from 'react';

export default function Layout({ children }) {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-900 flex items-center justify-center px-4">
      <div className="max-w-md w-full space-y-8">
        {children}
      </div>
    </div>
  );
}