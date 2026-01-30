import { z } from "zod";
import { LegalEntityType, CompanyStatus } from "./company.types";

// Define zod enums as TS types cannot be used at runtime
const legalEntityTypes = ["Sole Proprietor", "Partnership", "LLP", "Pvt Ltd", "Franchise"] as const;
const companyStatuses = ["Active", "Inactive"] as const;

export const CompanySchema = z.object({
  id: z.string().uuid(),
  company_code: z.string().max(20).min(1),
  company_name: z.string().max(100).min(1),
  legal_entity_type: z.enum(legalEntityTypes),
  default_currency: z.string().max(10).min(1),
  timezone: z.string().max(50).min(1),
  status: z.enum(companyStatuses),
  address: z.any().optional().nullable(),
});

// We could add custom methods for uniqueness in the service or UI validation layer


