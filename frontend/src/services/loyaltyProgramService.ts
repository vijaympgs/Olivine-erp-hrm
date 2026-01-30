import axios from "axios";

const API_BASE_URL = "/api";

export interface LoyaltyProgram {
    id: string;
    company: string;
    company_name?: string;
    program_code: string;
    program_name: string;
    description?: string;
    points_per_currency: number;
    min_transaction_amount: number;
    redemption_rate: number;
    min_points_for_redemption: number;
    max_redemption_percent: number;
    has_tiers: boolean;
    tier_config?: any;
    start_date: string;
    end_date?: string | null;
    points_expiry_months?: number | null;
    is_active: boolean;
    created_at: string;
    updated_at: string;
}

export interface LoyaltyProgramListItem {
    id: string;
    program_name: string;
    is_active: boolean;
}

export interface LoyaltyProgramFilters {
    company?: string;
    search?: string;
    is_active?: boolean;
}

export interface LoyaltyProgramCreateUpdate {
    program_name: string;
    is_active?: boolean;
}

class LoyaltyProgramService {
    private baseUrl = `${API_BASE_URL}/loyalty-programs`;

    async getLoyaltyPrograms(filters?: LoyaltyProgramFilters): Promise<LoyaltyProgramListItem[]> {
        const params = new URLSearchParams();
        if (filters?.company) params.append('company', filters.company);
        if (filters?.search) params.append('search', filters.search);
        if (filters?.is_active !== undefined) params.append('is_active', String(filters.is_active));

        const response = await axios.get(`${this.baseUrl}/?${params.toString()}`);
        return response.data.results || response.data;
    }

    async getLoyaltyProgram(id: string): Promise<LoyaltyProgram> {
        const response = await axios.get(`${this.baseUrl}/${id}/`);
        return response.data;
    }

    async createLoyaltyProgram(data: LoyaltyProgramCreateUpdate): Promise<LoyaltyProgram> {
        const response = await axios.post(`${this.baseUrl}/`, data);
        return response.data;
    }

    async updateLoyaltyProgram(id: string, data: Partial<LoyaltyProgramCreateUpdate>): Promise<LoyaltyProgram> {
        const response = await axios.patch(`${this.baseUrl}/${id}/`, data);
        return response.data;
    }

    async deactivateLoyaltyProgram(id: string): Promise<LoyaltyProgram> {
        const response = await axios.post(`${this.baseUrl}/${id}/deactivate/`);
        return response.data;
    }

    async activateLoyaltyProgram(id: string): Promise<LoyaltyProgram> {
        const response = await axios.post(`${this.baseUrl}/${id}/activate/`);
        return response.data;
    }
}

export const loyaltyProgramService = new LoyaltyProgramService();

