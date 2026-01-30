import React, { createContext, useContext, useState, useEffect } from "react";
import { useAuth } from "../../auth/useAuth";
import api from "@services/api";

interface GlobalLocationContextType {
    currentLocationId: string | null;
    currentLocationName: string | null;
    currentLocationCode: string | null;
    setLocation: (id: string, name: string, code: string) => void;
    isLoading: boolean;
    isPosSessionActive: boolean;
    setIsPosSessionActive: (active: boolean) => void;
}

const GlobalLocationContext = createContext<GlobalLocationContextType | undefined>(undefined);

export const GlobalLocationProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const [currentLocationId, setCurrentLocationId] = useState<string | null>(null);
    const [currentLocationName, setCurrentLocationName] = useState<string | null>(null);
    const [currentLocationCode, setCurrentLocationCode] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [isPosSessionActive, setIsPosSessionActive] = useState(false);
    const { user } = useAuth();

    useEffect(() => {
        // Load persisted location on mount
        const savedId = localStorage.getItem('session_location_id');
        const savedName = localStorage.getItem('session_location_name');
        const savedCode = localStorage.getItem('session_location_code');

        if (savedId && savedName) {
            setCurrentLocationId(savedId);
            setCurrentLocationName(savedName);
            setCurrentLocationCode(savedCode || '');
            setIsLoading(false);
        } else if (user) {
            // If no session location, try to fetch default active location for company
            // Or default to first available.
            // For now, we just stop loading and let the selector inside AppHeader handle enforcement
            setIsLoading(false);
        } else {
            setIsLoading(false);
        }
    }, [user]);

    const setLocation = (id: string, name: string, code: string) => {
        setCurrentLocationId(id);
        setCurrentLocationName(name);
        setCurrentLocationCode(code);

        // Persist
        localStorage.setItem('session_location_id', id);
        localStorage.setItem('session_location_name', name);
        localStorage.setItem('session_location_code', code);
        localStorage.setItem('session_location_selected_at', new Date().toISOString());
    };

    return (
        <GlobalLocationContext.Provider value={{
            currentLocationId,
            currentLocationName,
            currentLocationCode,
            setLocation,
            isLoading,
            isPosSessionActive,
            setIsPosSessionActive
        }}>
            {children}
        </GlobalLocationContext.Provider>
    );
};

export const useGlobalLocation = () => {
    const context = useContext(GlobalLocationContext);
    if (context === undefined) {
        throw new Error('useGlobalLocation must be used within a GlobalLocationProvider');
    }
    return context;
};


