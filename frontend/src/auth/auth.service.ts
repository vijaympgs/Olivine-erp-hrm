import axios from "axios";
import type { LoginPayload, User } from "./auth.types";

const API_BASE_URL = "/api/auth";

export const authService = {
  async login(payload: LoginPayload): Promise<User> {
    const { username, password, companyId } = payload;

    // Call Backend Login Endpoint
    // Expects: { token: string, user: {...} }
    const response = await axios.post(`${API_BASE_URL}/login/`, {
      username, // Backend should handle both email and username
      password,
      companyId
    });

    const { token, user, available_companies, context } = response.data;

    // Store Token
    if (token) {
      localStorage.setItem('auth_token', token);
    }

    // Map Backend User to Frontend User Interface
    return {
      id: user.id?.toString() || '0',
      name: user.name || 'User',
      email: user.email,
      role: user.is_superuser ? 'admin' : 'staff', // Simple mapping
      authorizedCompanies: available_companies,
      currentCompanyId: context?.company_id
    };
  },

  async updateProfile(data: Partial<User>): Promise<User> {
    const response = await axios.put(`${API_BASE_URL}/profile/`, data, {
      headers: {
        Authorization: `Token ${localStorage.getItem('auth_token')}`
      }
    });

    // Map response same as login if needed, or just return merged data
    // For now, assume backend returns compatible structure, but we might need to re-map.
    // Let's rely on login mapping logic or refresh the user data.
    const user = response.data;

    return {
      id: user.id?.toString(),
      name: `${user.first_name} ${user.last_name}`.trim() || user.username,
      email: user.email,
      role: user.is_superuser ? 'admin' : 'staff', // Re-evaluate role if it changed or persists
      // Companies likely not changed by profile update
    } as User;
  },

  logout() {
    localStorage.removeItem('auth_token');
  }
};

