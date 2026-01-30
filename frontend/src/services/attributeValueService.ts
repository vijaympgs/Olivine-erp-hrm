import axios from "axios";

const API_BASE_URL = "/api";

export interface AttributeValue {
  id: string;
  company: string;
  company_name?: string;
  attribute: string;
  attribute_code?: string;
  attribute_name?: string;
  value_code: string;
  value_label: string;
  sort_order?: number | null;
  is_default: boolean;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface AttributeValueListItem {
  id: string;
  company: string;
  company_name?: string;
  attribute: string;
  attribute_code?: string;
  attribute_name?: string;
  value_code: string;
  value_label: string;
  sort_order?: number | null;
  is_default: boolean;
  is_active: boolean;
}

export interface AttributeValueFilters {
  company_id?: string;
  attribute_id?: string;
  include_inactive?: boolean;
  search?: string;
}

export interface AttributeValueFormData {
  company: string;
  attribute: string;
  value_code: string;
  value_label: string;
  sort_order?: number | null;
  is_default: boolean;
  is_active: boolean;
}

class AttributeValueService {
  private baseURL = `${API_BASE_URL}/attribute-values`;

  async getAttributeValues(filters?: AttributeValueFilters): Promise<{ results: AttributeValueListItem[]; count: number }> {
    const params = new URLSearchParams();

    if (filters?.company_id) params.append('company_id', filters.company_id);
    if (filters?.attribute_id) params.append('attribute_id', filters.attribute_id);
    if (filters?.search) params.append('search', filters.search);
    if (filters?.include_inactive) params.append('include_inactive', 'true');

    const response = await axios.get(`${this.baseURL}/?${params.toString()}`);
    return response.data;
  }

  async getAttributeValue(id: string): Promise<AttributeValue> {
    const response = await axios.get(`${this.baseURL}/${id}/`);
    return response.data;
  }

  async createAttributeValue(data: AttributeValueFormData): Promise<AttributeValue> {
    const response = await axios.post(`${this.baseURL}/`, data);
    return response.data;
  }

  async updateAttributeValue(id: string, data: AttributeValueFormData): Promise<AttributeValue> {
    const response = await axios.put(`${this.baseURL}/${id}/`, data);
    return response.data;
  }

  async deleteAttributeValue(id: string): Promise<void> {
    await axios.delete(`${this.baseURL}/${id}/`);
  }
}

export const attributeValueService = new AttributeValueService();

