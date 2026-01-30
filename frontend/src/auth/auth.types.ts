export type UserRole = "admin" | "storeManager" | "staff";

export interface Company {
  id: string;
  name: string;
  code: string;
}

export interface User {
  id: string;
  name: string;
  email: string;
  role: UserRole;
  companyName?: string;
  authorizedCompanies?: Company[];
  currentCompanyId?: string;
  permissions?: Record<string, { can_view: boolean; can_create: boolean; can_edit: boolean; can_delete: boolean }>;
  is_superuser?: boolean;  // Django admin flag
  is_staff?: boolean;       // Django staff flag
}

export interface AuthState {
  isAuthenticated: boolean;
  isLoading: boolean;
  user: User | null;
}

export interface LoginPayload {
  username: string; // Can be email or username
  password: string;
  companyId?: string;
  rememberMe?: boolean;
}

