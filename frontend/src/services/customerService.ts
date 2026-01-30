import axios from "axios";

const API_BASE_URL = "/api";

export type CustomerType = "INDIVIDUAL" | "BUSINESS";
export type CustomerStatus = "ACTIVE" | "INACTIVE" | "BLACKLISTED";

export interface Address {
  line1?: string;
  line2?: string;
  city?: string;
  state?: string;
  country?: string;
  postal_code?: string;
}

export interface CustomerFormData {
  company: string;
  customer_code: string;
  customer_name: string;
  customer_type: CustomerType;
  phone?: string | null;
  email?: string | null;
  tax_id?: string | null;
  billing_address?: Address | null;
  shipping_address?: Address | null;
  credit_limit?: number | null;
  credit_blocked: boolean;
  status: CustomerStatus;
  // ICT Fields
  is_intercompany_customer: boolean;
  linked_company_id?: string | null;
  auto_accept_ic_so: boolean;
  default_ic_price_list_id?: string | null;
  default_tax_profile_id?: string | null;
}

export interface CustomerListItem {
  id: string;
  company: string;
  company_name?: string;
  customer_code: string;
  customer_name: string;
  customer_type: CustomerType;
  phone?: string | null;
  email?: string | null;
  status: CustomerStatus;
}

export interface CustomerDetail extends CustomerFormData {
  id: string;
  company_name?: string;
  created_at: string;
  updated_at: string;
}

export interface CustomerFilters {
  company_id?: string;
  customer_type?: string;
  status?: string;
  include_all?: boolean;
  search?: string;
}

class CustomerService {
  private baseURL = `${API_BASE_URL}/customers`;

  async getCustomers(filters?: CustomerFilters): Promise<{ results: CustomerListItem[]; count: number }> {
    const params = new URLSearchParams();

    if (filters?.company_id) params.append('company_id', filters.company_id);
    if (filters?.customer_type) params.append('customer_type', filters.customer_type);
    if (filters?.status) params.append('status', filters.status);
    if (filters?.search) params.append('search', filters.search);
    if (filters?.include_all) params.append('include_all', 'true');

    const response = await axios.get(`${this.baseURL}/?${params.toString()}`);
    const data = response.data;
    // Handle both paginated and non-paginated responses
    if (Array.isArray(data)) {
      return { results: data, count: data.length };
    }
    return data;
  }

  async getCustomer(id: string): Promise<CustomerDetail> {
    const response = await axios.get(`${this.baseURL}/${id}/`);
    return response.data;
  }

  async createCustomer(data: CustomerFormData): Promise<CustomerDetail> {
    const response = await axios.post(`${this.baseURL}/`, data);
    return response.data;
  }

  async updateCustomer(id: string, data: CustomerFormData): Promise<CustomerDetail> {
    const response = await axios.put(`${this.baseURL}/${id}/`, data);
    return response.data;
  }

  async deleteCustomer(id: string): Promise<void> {
    await axios.delete(`${this.baseURL}/${id}/`);
  }
}

export const customerService = new CustomerService();

