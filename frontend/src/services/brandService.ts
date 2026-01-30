import axios from "axios";

const API_BASE_URL = "/api";

export interface Brand {
    id: string;
    name: string;
    is_active: boolean;
    created_at: string;
    updated_at: string;
}

export interface BrandListItem {
    id: string;
    name: string;
    is_active: boolean;
}

export interface BrandFilters {
    company?: string;
    search?: string;
    is_active?: boolean;
}

export interface BrandCreateUpdate {
    name: string;
    is_active?: boolean;
}

class BrandService {
    private baseUrl = `${API_BASE_URL}/brands`;

    async getBrands(filters?: BrandFilters): Promise<BrandListItem[]> {
        const params = new URLSearchParams();
        if (filters?.company) params.append('company', filters.company);
        if (filters?.search) params.append('search', filters.search);
        if (filters?.is_active !== undefined) params.append('is_active', String(filters.is_active));

        const response = await axios.get(`${this.baseUrl}/?${params.toString()}`);
        return response.data.results || response.data;
    }

    async getBrand(id: string): Promise<Brand> {
        const response = await axios.get(`${this.baseUrl}/${id}/`);
        return response.data;
    }

    async createBrand(data: BrandCreateUpdate): Promise<Brand> {
        const response = await axios.post(`${this.baseUrl}/`, data);
        return response.data;
    }

    async updateBrand(id: string, data: Partial<BrandCreateUpdate>): Promise<Brand> {
        const response = await axios.patch(`${this.baseUrl}/${id}/`, data);
        return response.data;
    }

    async deactivateBrand(id: string): Promise<Brand> {
        return this.updateBrand(id, { is_active: false });
    }

    async activateBrand(id: string): Promise<Brand> {
        return this.updateBrand(id, { is_active: true });
    }
}

export const brandService = new BrandService();

