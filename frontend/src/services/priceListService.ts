import axios from "axios";

const API_BASE_URL = "/api";

export type PriceListType = "RETAIL" | "WHOLESALE" | "EMPLOYEE" | "DISTRIBUTOR";
export type PriceListChannel = "STORE" | "ONLINE" | "WHOLESALE" | "ALL";
export type PriceListStatus = "DRAFT" | "ACTIVE" | "EXPIRED" | "ARCHIVED";

export interface PriceListLine {
  id?: string;
  item: string;
  item_code?: string;
  item_name?: string;
  item_variant: string;
  sku_code?: string;
  variant_name?: string;
  uom: string;
  uom_code?: string;
  base_price: number;
  tax_inclusive: boolean;
  location_scope?: string | null;
  location_name?: string;
  status: string;
}

export interface PriceListFormData {
  company: string;
  price_list_code: string;
  price_list_name: string;
  currency: string;
  price_list_type: PriceListType;
  channel?: PriceListChannel | null;
  valid_from: string;
  valid_to?: string | null;
  is_default: boolean;
  status: PriceListStatus;
  lines?: PriceListLine[];
}

export interface PriceListListItem {
  id: string;
  company: string;
  company_name?: string;
  price_list_code: string;
  price_list_name: string;
  currency: string;
  price_list_type: PriceListType;
  channel?: PriceListChannel | null;
  valid_from: string;
  valid_to?: string | null;
  is_default: boolean;
  status: PriceListStatus;
  line_count?: number;
}

export interface PriceListDetail extends PriceListFormData {
  id: string;
  company_name?: string;
  lines: PriceListLine[];
  line_count?: number;
  created_at: string;
  updated_at: string;
}

export interface PriceListFilters {
  company_id?: string;
  price_list_type?: string;
  channel?: string;
  status?: string;
  include_all?: boolean;
  search?: string;
}

class PriceListService {
  private baseURL = `${API_BASE_URL}/price-lists`;

  async getPriceLists(filters?: PriceListFilters): Promise<{ results: PriceListListItem[]; count: number }> {
    const params = new URLSearchParams();

    if (filters?.company_id) params.append('company_id', filters.company_id);
    if (filters?.price_list_type) params.append('price_list_type', filters.price_list_type);
    if (filters?.channel) params.append('channel', filters.channel);
    if (filters?.status) params.append('status', filters.status);
    if (filters?.search) params.append('search', filters.search);
    if (filters?.include_all) params.append('include_all', 'true');

    const response = await axios.get(`${this.baseURL}/?${params.toString()}`);
    const data = response.data;
    if (Array.isArray(data)) {
      return { results: data, count: data.length };
    }
    return data;
  }

  async getPriceList(id: string): Promise<PriceListDetail> {
    const response = await axios.get(`${this.baseURL}/${id}/`);
    return response.data;
  }

  async createPriceList(data: PriceListFormData): Promise<PriceListDetail> {
    const response = await axios.post(`${this.baseURL}/`, data);
    return response.data;
  }

  async updatePriceList(id: string, data: PriceListFormData): Promise<PriceListDetail> {
    const response = await axios.put(`${this.baseURL}/${id}/`, data);
    return response.data;
  }

  async deletePriceList(id: string): Promise<void> {
    await axios.delete(`${this.baseURL}/${id}/`);
  }
}

export const priceListService = new PriceListService();

