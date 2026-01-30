// Generated from BBP 1.1.2 — Company Data Model

export type CompanyStatus = 'Active' | 'Inactive';
export type CompanyLegalEntityType =
  | 'Sole Proprietor'
  | 'Partnership'
  | 'LLP'
  | 'Pvt Ltd'
  | 'Franchise';

export interface CompanyAddress {
  [key: string]: any;
}

export interface Company {
  id: string;
  company_code: string;
  company_name: string;
  legal_entity_type: CompanyLegalEntityType;
  address?: CompanyAddress;
  default_currency: string;
  timezone: string;
  status: CompanyStatus;
}

