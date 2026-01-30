import React, { createContext, useContext, useEffect, useState } from "react";
import type { AuthState, LoginPayload, User } from "./auth.types";
import { authService } from "./auth.service";
import { userPermissionService } from "@services/userPermissionService";
import { hasRoleAccess, SYSTEM_ROLES } from "../config/rolePermissions";

interface AuthContextValue extends AuthState {
  login: (payload: LoginPayload) => Promise<void>;
  logout: () => void;
  updateProfile: (data: Partial<User>) => Promise<void>;
  hasPermission: (menuId: string, action?: 'view' | 'create' | 'edit' | 'delete') => boolean;
  hasRoleMenuAccess: (menuId: string) => boolean;
}

const AuthContext = createContext<AuthContextValue | undefined>(undefined);

const LOCAL_STORAGE_KEY = "olivine-auth";

const initialState: AuthState = {
  isAuthenticated: false,
  isLoading: true,
  user: null
};

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [state, setState] = useState<AuthState>(initialState);

  useEffect(() => {
    const stored = localStorage.getItem(LOCAL_STORAGE_KEY);
    if (stored) {
      try {
        const parsed = JSON.parse(stored) as AuthState;
        setState({ ...parsed, isLoading: false });
      } catch {
        setState(prev => ({ ...prev, isLoading: false }));
      }
    } else {
      setState(prev => ({ ...prev, isLoading: false }));
    }
  }, []);

  const login = async (payload: LoginPayload) => {
    const user: User = await authService.login(payload);

    // Fetch permissions
    try {
      const perms = await userPermissionService.getUserPermissions(parseInt(user.id));
      user.permissions = perms as any;
      console.log('User permissions loaded:', perms);
    } catch (e) {
      console.error("Failed to fetch permissions", e);
      // Set permissions to undefined so hasPermission can handle the fallback
      user.permissions = undefined;
    }

    const nextState: AuthState = {
      isAuthenticated: true,
      isLoading: false,
      user
    };
    setState(nextState);
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(nextState));
  };

  const logout = () => {
    setState({
      isAuthenticated: false,
      isLoading: false,
      user: null
    });
    localStorage.removeItem(LOCAL_STORAGE_KEY);
  };

  /**
   * Check if user has fine-grained permission for a specific action on a menu item.
   * This is for CRUD operations.
   */
  const hasPermission = (menuId: string, action: 'view' | 'create' | 'edit' | 'delete' = 'view') => {
    // If user is not authenticated, deny access
    if (!state.isAuthenticated || !state.user) return false;

    // Admin users have all permissions
    if (state.user?.role === SYSTEM_ROLES.ADMIN) return true;

    // For now, allow access to all menu items if permissions are not loaded
    // This is a temporary fallback to prevent sidebar from being empty
    if (!state.user?.permissions) {
      console.warn(`Permissions not loaded for user ${state.user.id}, allowing access to ${menuId}`);
      return true;
    }

    const p = state.user?.permissions?.[menuId];
    if (!p) {
      // If specific permission not found, allow access (fallback)
      console.warn(`Permission not found for menu item ${menuId}, allowing access`);
      return true;
    }

    switch (action) {
      case 'create': return p.can_create;
      case 'edit': return p.can_edit;
      case 'delete': return p.can_delete;
      default: return p.can_view;
    }
  };

  /**
   * Check if user's ROLE has access to a menu item.
   * Sidebar visibility is driven by ROLE, not username.
   * No hardcoded username checks.
   */
  const hasRoleMenuAccess = (menuId: string): boolean => {
    // If user is not authenticated, deny access
    if (!state.isAuthenticated || !state.user) return false;

    // Use centralized role permission check
    return hasRoleAccess(state.user.role, menuId);
  };

  const updateProfile = async (data: Partial<User>) => {
    try {
      const updatedUser = await authService.updateProfile(data);
      // Merge with existing user data to preserve other fields (like companies)
      const nextUser = { ...state.user!, ...updatedUser };
      const nextState = { ...state, user: nextUser };

      setState(nextState);
      localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(nextState));
    } catch (e) {
      console.error("Failed to update profile", e);
      throw e;
    }
  };

  return (
    <AuthContext.Provider value={{ ...state, login, logout, updateProfile, hasPermission, hasRoleMenuAccess }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuthContext = () => {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuthContext must be used within AuthProvider");
  return ctx;
};


