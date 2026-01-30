export type LegalEntityType = "Sole Proprietor" | "Partnership" | "LLP" | "Pvt Ltd" | "Franchise";

export type CompanyStatus = "Active" | "Inactive";

export interface Company {
  id: string;
  company_code: string; // unique, max length 20
  company_name: string; // max length 100
  legal_entity_type: LegalEntityType;
  default_currency: string; // ISO Code, max length 10
  timezone: string; // Olson tz, max length 50
  status: CompanyStatus;
  address?: Record<string, any> | null; // optional JSON address
}


