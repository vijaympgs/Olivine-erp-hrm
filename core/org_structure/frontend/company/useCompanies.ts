import { useState, useEffect, useCallback } from "react";
import {
  Company,
  LegalEntityType,
  CompanyStatus,
} from "./company.types";
import * as companyService from "./company.service";

interface UseCompaniesResult {
  companies: Company[];
  loading: boolean;
  error: string | null;
  createCompany: (company: Omit<Company, "id">) => Promise<void>;
  updateCompany: (id: string, fields: Partial<Omit<Company, "id">>) => Promise<void>;
  reloadCompanies: () => Promise<void>;
}

export function useCompanies(): UseCompaniesResult {
  const [companies, setCompanies] = useState<Company[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);

  const loadCompanies = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await companyService.listCompanies();
      setCompanies(data);
    } catch (e: any) {
      setError(e.message || "Failed to load companies");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadCompanies();
  }, [loadCompanies]);

  const createCompany = async (company: Omit<Company, "id">) => {
    setLoading(true);
    setError(null);
    try {
      const newCompany = await companyService.createCompany(company);
      setCompanies((prev) => [...prev, newCompany]);
    } catch (e: any) {
      setError(e.message || "Failed to create company");
      throw e;
    } finally {
      setLoading(false);
    }
  };

  const updateCompany = async (id: string, fields: Partial<Omit<Company, "id">>) => {
    setLoading(true);
    setError(null);
    try {
      const updated = await companyService.updateCompany(id, fields);
      setCompanies((prev) =>
        prev.map((c) => (c.id === id ? updated : c))
      );
    } catch (e: any) {
      setError(e.message || "Failed to update company");
      throw e;
    } finally {
      setLoading(false);
    }
  };

  const reloadCompanies = async () => {
    await loadCompanies();
  };

  return {
    companies,
    loading,
    error,
    createCompany,
    updateCompany,
    reloadCompanies,
  };
}


