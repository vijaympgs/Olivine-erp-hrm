import axios from "axios";

const API_BASE_URL = "/api";

export interface CustomerGroup {
    id: string;
    company: string;
    company_name?: string;
    group_code: string;
    group_name: string;
    description?: string;
    default_price_list?: string | null;
    discount_percent?: number;
    payment_terms?: string | null;
    credit_limit?: number | null;
    is_active: boolean;
    created_at: string;
    updated_at: string;
}

export interface CustomerGroupListItem {
    id: string;
    group_name: string;
    is_active: boolean;
}

export interface CustomerGroupFilters {
    company?: string;
    search?: string;
    is_active?: boolean;
}

export interface CustomerGroupCreateUpdate {
    company?: string;
    group_code: string;
    group_name: string;
    description?: string;
    default_price_list?: string | null;
    discount_percent?: number | null;
    payment_terms?: string | null;
    credit_limit?: number | null;
    is_active?: boolean;
}

class CustomerGroupService {
    private baseUrl = `${API_BASE_URL}/customer-groups`;

    async getCustomerGroups(filters?: CustomerGroupFilters): Promise<CustomerGroupListItem[]> {
        const params = new URLSearchParams();
        if (filters?.company) params.append('company', filters.company);
        if (filters?.search) params.append('search', filters.search);
        if (filters?.is_active !== undefined) params.append('is_active', String(filters.is_active));

        const response = await axios.get(`${this.baseUrl}/?${params.toString()}`);
        return response.data.results || response.data;
    }

    async getCustomerGroup(id: string): Promise<CustomerGroup> {
        const response = await axios.get(`${this.baseUrl}/${id}/`);
        return response.data;
    }

    async createCustomerGroup(data: CustomerGroupCreateUpdate): Promise<CustomerGroup> {
        const response = await axios.post(`${this.baseUrl}/`, data);
        return response.data;
    }

    async updateCustomerGroup(id: string, data: Partial<CustomerGroupCreateUpdate>): Promise<CustomerGroup> {
        const response = await axios.patch(`${this.baseUrl}/${id}/`, data);
        return response.data;
    }

    async deactivateCustomerGroup(id: string): Promise<CustomerGroup> {
        const response = await axios.post(`${this.baseUrl}/${id}/deactivate/`);
        return response.data;
    }

    async activateCustomerGroup(id: string): Promise<CustomerGroup> {
        const response = await axios.post(`${this.baseUrl}/${id}/activate/`);
        return response.data;
    }
}

export const customerGroupService = new CustomerGroupService();

