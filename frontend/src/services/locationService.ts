import api from "./api";

// api instance has baseURL '/api' configured
const API_BASE_URL = "";

export type LocationType = "STORE" | "WAREHOUSE" | "OFFICE" | "OTHER";
export type ChannelType = "RETAIL" | "ONLINE" | "WHOLESALE" | "FRANCHISE";

export interface Location {
  id: string;
  company: string;
  company_name?: string;
  location_code: string;
  name: string;
  display_name?: string | null;
  location_type: LocationType;
  channel_type?: ChannelType | null;
  parent_location?: string | null;
  parent_location_name?: string | null;
  address_line1: string;
  address_line2?: string | null;
  city: string;
  state: string;
  country: string;
  postal_code?: string | null;
  phone?: string | null;
  email?: string | null;
  timezone?: string | null;
  opening_date?: string | null;
  closing_date?: string | null;
  is_pos_enabled: boolean;
  is_dc?: boolean;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface LocationListItem {
  id: string;
  company: string;
  company_name?: string;
  location_code: string;
  name: string;
  location_type: string;
  channel_type?: string | null;
  is_pos_enabled: boolean;
  is_dc?: boolean;
  is_active: boolean;
  city: string;
}

export interface LocationFilters {
  company_id?: string;
  location_type?: string;
  channel_type?: string;
  is_active?: string;
  is_pos_enabled?: string;
  is_dc?: string;
  include_inactive?: boolean;
  search?: string;
}

export interface LocationFormData {
  company: string;
  location_code: string;
  name: string;
  display_name?: string | null;
  location_type: LocationType;
  channel_type?: ChannelType | null;
  parent_location?: string | null;
  address_line1: string;
  address_line2?: string | null;
  city: string;
  state: string;
  country: string;
  postal_code?: string | null;
  phone?: string | null;
  email?: string | null;
  timezone?: string | null;
  opening_date?: string | null;
  closing_date?: string | null;
  is_pos_enabled: boolean;
  is_dc?: boolean;
  is_active: boolean;
}


class LocationService {
  // Use legacy company API (as location model remains in domain.company)
  private baseURL = `${API_BASE_URL}/locations`;

  async getLocations(filters?: LocationFilters): Promise<{ results: LocationListItem[]; count: number }> {
    const params = new URLSearchParams();

    if (filters?.company_id) params.append('company_id', filters.company_id);
    if (filters?.location_type) params.append('location_type', filters.location_type);
    if (filters?.channel_type) params.append('channel_type', filters.channel_type);
    if (filters?.is_active) params.append('is_active', filters.is_active);
    if (filters?.is_pos_enabled) params.append('is_pos_enabled', filters.is_pos_enabled);
    if (filters?.is_dc) params.append('is_dc', filters.is_dc);
    if (filters?.search) params.append('search', filters.search);
    if (filters?.include_inactive) params.append('include_inactive', 'true');

    const response = await api.get(`${this.baseURL}/?${params.toString()}`);
    // Handle both array/paginated response
    const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
    return { results: data, count: data.length };
  }

  async getUserAccessibleLocations(userId: string, companyId?: string): Promise<LocationListItem[]> {
    const params = new URLSearchParams();
    params.append('user_id', userId);
    if (companyId) params.append('company_id', companyId);

    const response = await api.get(`${API_BASE_URL}/auth/user-locations/`, { params });

    return response.data.map((item: any) => {
      const loc = item.location_details || {};
      return {
        id: loc.id,
        company: loc.company,
        location_code: loc.code,
        name: loc.name,
        location_type: loc.location_type,
        city: loc.city,
        is_active: loc.is_active,
        is_pos_enabled: loc.is_pos_enabled,
        channel_type: null
      } as LocationListItem;
    });
  }

  async getLocation(id: string): Promise<Location> {
    const response = await api.get(`${this.baseURL}/${id}/`);
    return response.data;
  }

  async createLocation(data: LocationFormData): Promise<Location> {
    // Backend expects 'code', frontend sends 'location_code'
    // Serializer handles source='code', but let's be explicit if needed
    // Actually the serializer takes 'location_code' field and maps it to 'code', so we are good.
    const response = await api.post(`${this.baseURL}/`, data);
    return response.data;
  }

  async updateLocation(id: string, data: LocationFormData): Promise<Location> {
    const response = await api.put(`${this.baseURL}/${id}/`, data);
    return response.data;
  }

  async deleteLocation(id: string): Promise<void> {
    await api.delete(`${this.baseURL}/${id}/`);
  }
}

export const locationService = new LocationService();

