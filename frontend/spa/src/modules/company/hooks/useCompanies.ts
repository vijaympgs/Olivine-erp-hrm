import { useCallback, useEffect, useState } from 'react';
import { Company } from '../types/company';
import { CompanyService } from '../services/companyService';

export function useCompanies(filters: Record<string, any> = {}) {
  const [data, setData] = useState<Company[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await CompanyService.fetchAll(filters);
      setData(response.data);
    } catch (err: any) {
      setError(err.message || 'Error fetching company data');
    } finally {
      setLoading(false);
    }
  }, [filters]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  return { data, loading, error, refresh: fetchData };
}

