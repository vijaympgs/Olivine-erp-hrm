import axios from "axios";

const API_BASE_URL = "/api";

export type TemplateMode = "SIMPLE" | "VARIANT_MATRIX" | "HYBRID";
export type ValueMode = "SINGLE" | "MULTI" | "DERIVED";

export interface ProductAttributeTemplateLineFormData {
  attribute: string;
  is_required: boolean;
  is_variant_dimension: boolean;
  value_mode: ValueMode;
  default_value?: string | null;
  sequence_no: number;
  is_search_facet: boolean;
  is_pricing_relevant: boolean;
  is_reporting_relevant: boolean;
  is_pos_visible: boolean;
}

export interface ProductAttributeTemplateFormData {
  company: string;
  template_code: string;
  template_name: string;
  description?: string;
  template_mode: TemplateMode;
  is_core_template: boolean;
  is_editable: boolean;
  item_type_scope?: string | null;
  category_scope_id?: string | null;
  is_active: boolean;
  version_no: number;
  lines: ProductAttributeTemplateLineFormData[];
}

export interface ProductAttributeTemplateListItem {
  id: string;
  company: string;
  company_name?: string;
  template_code: string;
  template_name: string;
  template_mode: TemplateMode;
  version_no: number;
  is_core_template: boolean;
  is_editable: boolean;
  is_active: boolean;
  line_count: number;
}

export interface ProductAttributeTemplateDetail extends ProductAttributeTemplateFormData {
  id: string;
  company_name?: string;
  created_at: string;
  updated_at: string;
}

export interface ProductAttributeTemplateFilters {
  company_id?: string;
  template_mode?: string;
  include_inactive?: boolean;
  search?: string;
}

class ProductAttributeTemplateService {
  private baseURL = `${API_BASE_URL}/attribute-templates`;

  async getTemplates(filters?: ProductAttributeTemplateFilters): Promise<{ results: ProductAttributeTemplateListItem[]; count: number }> {
    const params = new URLSearchParams();

    if (filters?.company_id) params.append('company_id', filters.company_id);
    if (filters?.template_mode) params.append('template_mode', filters.template_mode);
    if (filters?.search) params.append('search', filters.search);
    if (filters?.include_inactive) params.append('include_inactive', 'true');

    const response = await axios.get(`${this.baseURL}/?${params.toString()}`);
    return response.data;
  }

  async getTemplate(id: string): Promise<ProductAttributeTemplateDetail> {
    const response = await axios.get(`${this.baseURL}/${id}/`);
    return response.data;
  }

  async createTemplate(data: ProductAttributeTemplateFormData): Promise<ProductAttributeTemplateDetail> {
    const response = await axios.post(`${this.baseURL}/`, data);
    return response.data;
  }

  async updateTemplate(id: string, data: ProductAttributeTemplateFormData): Promise<ProductAttributeTemplateDetail> {
    const response = await axios.put(`${this.baseURL}/${id}/`, data);
    return response.data;
  }

  async deleteTemplate(id: string): Promise<void> {
    await axios.delete(`${this.baseURL}/${id}/`);
  }
}

export const productAttributeTemplateService = new ProductAttributeTemplateService();

