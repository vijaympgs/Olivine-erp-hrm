import axios from "axios";

const API_BASE_URL = "/api";

export type UOMType = "STOCK" | "PURCHASE" | "SALES" | "GENERIC";

export interface UnitOfMeasureFormData {
  company: string;
  uom_code: string;
  uom_name: string;
  uom_type: UOMType;
  decimal_allowed: boolean;
  rounding_precision?: number | null;
  is_core_uom: boolean;
  is_active: boolean;
}

export interface UnitOfMeasureListItem {
  id: string;
  company: string;
  company_name?: string;
  uom_code: string;
  uom_name: string;
  uom_type: UOMType;
  decimal_allowed: boolean;
  is_core_uom: boolean;
  is_active: boolean;
}

export interface UnitOfMeasureDetail extends UnitOfMeasureFormData {
  id: string;
  company_name?: string;
  created_at: string;
  updated_at: string;
}

export interface UOMFilters {
  company_id?: string;
  uom_type?: string;
  include_inactive?: boolean;
  search?: string;
}

class UOMService {
  private baseURL = `${API_BASE_URL}/uoms`;

  async getUOMs(filters?: UOMFilters): Promise<{ results: UnitOfMeasureListItem[]; count: number }> {
    const params = new URLSearchParams();

    if (filters?.company_id) params.append('company_id', filters.company_id);
    if (filters?.uom_type) params.append('uom_type', filters.uom_type);
    if (filters?.search) params.append('search', filters.search);
    if (filters?.include_inactive) params.append('include_inactive', 'true');

    const response = await axios.get(`${this.baseURL}/?${params.toString()}`);
    // Handle both paginated and non-paginated responses
    if (Array.isArray(response.data)) {
      return { results: response.data, count: response.data.length };
    }
    return response.data;
  }

  async getUOM(id: string): Promise<UnitOfMeasureDetail> {
    const response = await axios.get(`${this.baseURL}/${id}/`);
    return response.data;
  }

  async createUOM(data: UnitOfMeasureFormData): Promise<UnitOfMeasureDetail> {
    const response = await axios.post(`${this.baseURL}/`, data);
    return response.data;
  }

  async updateUOM(id: string, data: UnitOfMeasureFormData): Promise<UnitOfMeasureDetail> {
    const response = await axios.put(`${this.baseURL}/${id}/`, data);
    return response.data;
  }

  async deleteUOM(id: string): Promise<void> {
    await axios.delete(`${this.baseURL}/${id}/`);
  }

  async checkUsage(id: string): Promise<{ in_use: boolean }> {
    const response = await axios.get(`${this.baseURL}/${id}/check_usage/`);
    return response.data;
  }
}

export const uomService = new UOMService();

