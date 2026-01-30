import axios from "axios";

const API_BASE_URL = "/api";

export type ItemType = "STOCKED" | "SERVICE" | "KIT" | "GIFT";
export type ItemStatus = "DRAFT" | "ACTIVE" | "BLOCKED" | "DISCONTINUED" | "ARCHIVED";

export interface VariantAttribute {
  id?: string;
  attribute: string;
  attribute_code?: string;
  attribute_name?: string;
  attribute_value: string;
  value_code?: string;
  value_label?: string;
}

export interface VariantUOM {
  id?: string;
  uom: string;
  uom_code?: string;
  uom_name?: string;
  is_default_sales: boolean;
  barcode?: string;
  retail_price?: number | null;
  status: string;
}

export interface ItemVariant {
  id?: string;
  sku_code: string;
  variant_name: string;
  is_default_variant: boolean;
  sales_uom: string;
  sales_uom_code?: string;
  purchase_uom?: string | null;
  purchase_uom_code?: string;
  stock_uom: string;
  stock_uom_code?: string;
  is_active: boolean;
  variant_attributes?: VariantAttribute[];
  uom_mappings?: VariantUOM[];
  created_at?: string;
  updated_at?: string;
}

export interface ItemFormData {
  company: string;
  item_code: string;
  item_name: string;
  short_name?: string;
  description?: string; // Short description
  item_type: ItemType;
  attribute_template?: string | null;
  category_id?: string | null;
  brand_id?: string | null;
  stock_uom: string;
  tax_class_id?: string | null;

  // Pricing
  price_list_id?: string | null;
  standard_price?: number | null;
  mrp?: number | null;
  standard_cost?: number | null;

  // Inventory Planning
  reorder_level?: number | null;
  safety_stock?: number | null;
  lead_time_days?: number | null;

  // Dimensions
  length?: number | null;
  width?: number | null;
  height?: number | null;
  weight?: number | null;

  // Metadata
  tags?: string[];

  is_serialized: boolean;
  is_lot_tracked: boolean;
  status: ItemStatus;
}

export interface ItemListItem {
  id: string;
  company: string;
  company_name?: string;
  item_code: string;
  item_name: string;
  short_name?: string;
  item_type: ItemType;
  stock_uom: string;
  stock_uom_code?: string;
  status: ItemStatus;
  variant_count?: number;
}

export interface ItemDetail extends ItemFormData {
  id: string;
  company_name?: string;
  stock_uom_code?: string;
  template_code?: string;
  variants?: ItemVariant[];
  created_at: string;
  updated_at: string;
}

export interface ItemFilters {
  company_id?: string;
  item_type?: string;
  status?: string;
  include_all?: boolean;
  search?: string;
}

class ItemService {
  private baseURL = `${API_BASE_URL}/items`;

  async getItems(filters?: ItemFilters): Promise<{ results: ItemListItem[]; count: number }> {
    const params = new URLSearchParams();

    if (filters?.company_id) params.append('company_id', filters.company_id);
    if (filters?.item_type) params.append('item_type', filters.item_type);
    if (filters?.status) params.append('status', filters.status);
    if (filters?.search) params.append('search', filters.search);
    if (filters?.include_all) params.append('include_all', 'true');

    const response = await axios.get(`${this.baseURL}/?${params.toString()}`);
    if (Array.isArray(response.data)) {
      return { results: response.data, count: response.data.length };
    }
    return response.data;
  }

  async getItem(id: string): Promise<ItemDetail> {
    const response = await axios.get(`${this.baseURL}/${id}/`);
    return response.data;
  }

  async createItem(data: ItemFormData): Promise<ItemDetail> {
    const response = await axios.post(`${this.baseURL}/`, data);
    return response.data;
  }

  async updateItem(id: string, data: ItemFormData): Promise<ItemDetail> {
    const response = await axios.put(`${this.baseURL}/${id}/`, data);
    return response.data;
  }

  async deleteItem(id: string): Promise<void> {
    await axios.delete(`${this.baseURL}/${id}/`);
  }
}

export const itemService = new ItemService();

