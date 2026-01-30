import axios from "axios";

const API_BASE_URL = "/api";

export type AttributeInputType = "TEXT" | "NUMBER" | "BOOLEAN" | "LIST" | "MULTI";
export type AttributeValueSource = "FIXED_LIST" | "FREE_TEXT" | "DERIVED";

export interface Attribute {
  id: string;
  company: string;
  company_name?: string;
  attribute_code: string;
  attribute_name: string;
  input_type: AttributeInputType;
  value_source: AttributeValueSource;
  is_variant_dimension?: boolean;
  is_search_facet?: boolean;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface AttributeListItem {
  id: string;
  company: string;
  company_name?: string;
  attribute_code: string;
  attribute_name: string;
  input_type: string;
  value_source: string;
  is_variant_dimension: boolean;
  is_search_facet: boolean;
  is_active: boolean;
}

export interface AttributeFilters {
  company_id?: string;
  input_type?: string;
  value_source?: string;
  include_inactive?: boolean;
  search?: string;
}

export interface AttributeFormData {
  company: string;
  attribute_code: string;
  attribute_name: string;
  input_type: AttributeInputType;
  value_source: AttributeValueSource;
  is_variant_dimension: boolean;
  is_search_facet: boolean;
  is_active: boolean;
}

class AttributeService {
  private baseURL = `${API_BASE_URL}/attributes`;

  async getAttributes(filters?: AttributeFilters): Promise<{ results: AttributeListItem[]; count: number }> {
    const params = new URLSearchParams();

    if (filters?.company_id) params.append('company_id', filters.company_id);
    if (filters?.input_type) params.append('input_type', filters.input_type);
    if (filters?.value_source) params.append('value_source', filters.value_source);
    if (filters?.search) params.append('search', filters.search);
    if (filters?.include_inactive) params.append('include_inactive', 'true');

    const response = await axios.get(`${this.baseURL}/?${params.toString()}`);
    return response.data;
  }

  async getAttribute(id: string): Promise<Attribute> {
    const response = await axios.get(`${this.baseURL}/${id}/`);
    return response.data;
  }

  async createAttribute(data: AttributeFormData): Promise<Attribute> {
    const response = await axios.post(`${this.baseURL}/`, data);
    return response.data;
  }

  async updateAttribute(id: string, data: AttributeFormData): Promise<Attribute> {
    const response = await axios.put(`${this.baseURL}/${id}/`, data);
    return response.data;
  }

  async deleteAttribute(id: string): Promise<void> {
    await axios.delete(`${this.baseURL}/${id}/`);
  }
}

export const attributeService = new AttributeService();

