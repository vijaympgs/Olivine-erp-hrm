import React from "react";
import { AuthProvider } from "../auth/auth.context";
import { GlobalLocationProvider } from "../core/contexts/GlobalLocationContext";

interface AppProvidersProps {
  children: React.ReactNode;
}

export const AppProviders: React.FC<AppProvidersProps> = ({ children }) => {
  return (
    <AuthProvider>
      <GlobalLocationProvider>
        {children}
      </GlobalLocationProvider>
    </AuthProvider>
  );
};

