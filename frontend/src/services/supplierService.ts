import axios from "axios";

const API_BASE_URL = "/api";

export type SupplierStatus = "ACTIVE" | "INACTIVE" | "BLOCKED";

export interface Address {
  line1?: string;
  line2?: string;
  city?: string;
  state?: string;
  country?: string;
  postal_code?: string;
}

export interface SupplierFormData {
  company: string;
  supplier_code: string;
  supplier_name: string;
  contact_person?: string | null;
  phone?: string | null;
  email?: string | null;
  gst_vat_no?: string | null;
  pan_no?: string | null;
  address?: Address | null;
  payment_terms?: string | null;
  currency?: string | null;
  lead_time_days?: number | null;
  is_preferred: boolean;
  status: SupplierStatus;
  // ICT Fields
  is_intercompany_supplier: boolean;
  linked_company_id?: string | null;
  auto_accept_ic_po: boolean;
  default_ic_price_list_id?: string | null;
  default_tax_profile_id?: string | null;
}

export interface SupplierListItem {
  id: string;
  company: string;
  company_name?: string;
  supplier_code: string;
  supplier_name: string;
  contact_person?: string | null;
  phone?: string | null;
  email?: string | null;
  is_preferred: boolean;
  status: SupplierStatus;
}

export interface SupplierDetail extends SupplierFormData {
  id: string;
  company_name?: string;
  created_at: string;
  updated_at: string;
}

export interface SupplierFilters {
  company_id?: string;
  status?: string;
  is_preferred?: boolean;
  include_all?: boolean;
  search?: string;
}

class SupplierService {
  private baseURL = `${API_BASE_URL}/suppliers`;

  async getSuppliers(filters?: SupplierFilters): Promise<{ results: SupplierListItem[]; count: number }> {
    const params = new URLSearchParams();

    if (filters?.company_id) params.append('company_id', filters.company_id);
    if (filters?.status) params.append('status', filters.status);
    if (filters?.is_preferred !== undefined) params.append('is_preferred', String(filters.is_preferred));
    if (filters?.search) params.append('search', filters.search);
    if (filters?.include_all) params.append('include_all', 'true');

    const response = await axios.get(`${this.baseURL}/?${params.toString()}`);
    const data = response.data;
    if (Array.isArray(data)) {
      return { results: data, count: data.length };
    }
    return data;
  }

  async getSupplier(id: string): Promise<SupplierDetail> {
    const response = await axios.get(`${this.baseURL}/${id}/`);
    return response.data;
  }

  async createSupplier(data: SupplierFormData): Promise<SupplierDetail> {
    const response = await axios.post(`${this.baseURL}/`, data);
    return response.data;
  }

  async updateSupplier(id: string, data: SupplierFormData): Promise<SupplierDetail> {
    const response = await axios.put(`${this.baseURL}/${id}/`, data);
    return response.data;
  }

  async deleteSupplier(id: string): Promise<void> {
    await axios.delete(`${this.baseURL}/${id}/`);
  }
}

export const supplierService = new SupplierService();

