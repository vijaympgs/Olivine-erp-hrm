// Axios service for Company module (mst01, BBP)
import axios from 'axios';
import { Company } from '../types/company';

const API_PREFIX = '/api/company';

export const CompanyService = {
  fetchAll(params?: Record<string, any>) {
    // params: filters, pagination, sorting
    return axios.get<Company[]>(API_PREFIX, { params });
  },

  fetchById(id: string) {
    return axios.get<Company>(`${API_PREFIX}/${id}`);
  },

  create(data: Omit<Company, 'id'>) {
    return axios.post<Company>(API_PREFIX, data);
  },

  update(id: string, data: Partial<Omit<Company, 'id'>>) {
    return axios.put<Company>(`${API_PREFIX}/${id}`, data);
  },

  delete(id: string) {
    // Soft delete (set status)
    return axios.patch<Company>(`${API_PREFIX}/${id}`, { status: 'Inactive' });
  }
};

