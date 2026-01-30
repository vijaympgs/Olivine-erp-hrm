import axios from "axios";

const API_BASE_URL = "/api";

export interface Company {
  id: string;
  company_code: string;
  company_name: string;
  legal_entity_type: "SOLE_PROPRIETOR" | "PARTNERSHIP" | "LLP" | "PVT_LTD" | "FRANCHISE";
  address?: {
    line1?: string;
    line2?: string;
    city?: string;
    state?: string;
    country?: string;
    postal_code?: string;
  };
  default_currency: string;
  timezone: string;
  status: "ACTIVE" | "INACTIVE";
  created_at: string;
  updated_at: string;
}

export interface CompanyListItem {
  id: string;
  company_code: string;
  company_name: string;
  legal_entity_type: string;
  default_currency: string;
  status: string;
}

export interface CompanyFilters {
  status?: string;
  legal_entity_type?: string;
  search?: string;
}

export interface CompanyFormData {
  company_code?: string;
  company_name: string;
  legal_entity_type: string;
  address?: {
    line1?: string;
    line2?: string;
    city?: string;
    state?: string;
    country?: string;
    postal_code?: string;
  };
  default_currency: string;
  timezone: string;
  status: string;
}

// Helper to normalize business_entities Company to CompanyListItem format
function normalizeCompany(beCompany: any): CompanyListItem {
  return {
    id: beCompany.id?.toString() || beCompany.code,
    company_code: beCompany.code || beCompany.company_code,
    company_name: beCompany.name || beCompany.company_name,
    legal_entity_type: beCompany.legal_entity_type,
    default_currency: beCompany.default_currency,
    status: beCompany.status,
  };
}

// Helper to normalize for full Company object
function normalizeFullCompany(beCompany: any): Company {
  return {
    id: beCompany.id?.toString() || beCompany.code,
    company_code: beCompany.code || beCompany.company_code,
    company_name: beCompany.name || beCompany.company_name,
    legal_entity_type: beCompany.legal_entity_type,
    address: beCompany.address_dict || beCompany.address,
    default_currency: beCompany.default_currency,
    timezone: beCompany.timezone || 'UTC',
    status: beCompany.status,
    created_at: beCompany.created_at,
    updated_at: beCompany.updated_at,
  };
}

class CompanyService {
  // Use business_entities as the primary source (correct data)
  private baseURL = `${API_BASE_URL}/business/companies`;

  async getCompanies(filters?: CompanyFilters): Promise<{ results: CompanyListItem[]; count: number }> {
    const params = new URLSearchParams();

    if (filters?.status) params.append('status', filters.status);
    if (filters?.legal_entity_type) params.append('legal_entity_type', filters.legal_entity_type);
    if (filters?.search) params.append('search', filters.search);

    const response = await axios.get(`${this.baseURL}/?${params.toString()}`);
    const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
    const normalized = data.map(normalizeCompany);
    return { results: normalized, count: normalized.length };
  }

  async getCompany(id: string): Promise<Company> {
    const response = await axios.get(`${this.baseURL}/${id}/`);
    return normalizeFullCompany(response.data);
  }

  async createCompany(data: CompanyFormData): Promise<Company> {
    // Transform to business_entities format
    const beData = {
      code: data.company_code,
      name: data.company_name,
      legal_entity_type: data.legal_entity_type,
      default_currency: data.default_currency,
      timezone: data.timezone || 'UTC',
      country: data.address?.country || 'IN',
      address_line1: data.address?.line1 || '',
      address_line2: data.address?.line2 || '',
      city: data.address?.city || '',
      state: data.address?.state || '',
      postal_code: data.address?.postal_code || '',
      status: data.status,
    };
    const response = await axios.post(`${this.baseURL}/`, beData);
    return normalizeFullCompany(response.data);
  }

  async updateCompany(id: string, data: CompanyFormData): Promise<Company> {
    const beData = {
      code: data.company_code,
      name: data.company_name,
      legal_entity_type: data.legal_entity_type,
      default_currency: data.default_currency,
      timezone: data.timezone || 'UTC',
      country: data.address?.country || 'IN',
      address_line1: data.address?.line1 || '',
      address_line2: data.address?.line2 || '',
      city: data.address?.city || '',
      state: data.address?.state || '',
      postal_code: data.address?.postal_code || '',
      status: data.status,
    };
    const response = await axios.put(`${this.baseURL}/${id}/`, beData);
    return normalizeFullCompany(response.data);
  }

  async deleteCompany(id: string): Promise<void> {
    await axios.delete(`${this.baseURL}/${id}/`);
  }

  async deactivateCompany(id: string): Promise<Company> {
    const response = await axios.post(`${this.baseURL}/${id}/deactivate/`);
    return normalizeFullCompany(response.data);
  }

  async activateCompany(id: string): Promise<Company> {
    const response = await axios.post(`${this.baseURL}/${id}/activate/`);
    return normalizeFullCompany(response.data);
  }

  async getActiveCompanies(): Promise<CompanyListItem[]> {
    // Fetch active Companies (not Operating Companies - that's internal architecture)
    const response = await axios.get(`${this.baseURL}/?status=ACTIVE`);
    const data = Array.isArray(response.data) ? response.data : (response.data.results || []);
    return data.map(normalizeCompany);
  }
}

export const companyService = new CompanyService();

