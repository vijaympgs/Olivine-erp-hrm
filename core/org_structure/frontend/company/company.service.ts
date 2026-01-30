import { Company } from "./company.types";
import { v4 as uuidv4 } from "uuid";

let companies: Company[] = [
  {
    id: uuidv4(),
    company_code: "COMP001",
    company_name: "Default Company",
    legal_entity_type: "Pvt Ltd",
    default_currency: "INR",
    timezone: "Asia/Kolkata",
    status: "Active",
    address: null,
  },
];

// Utility to check unique company_code globally (excluding optional ID for update)
function isCompanyCodeUnique(code: string, excludeId?: string): boolean {
  return !companies.some(
    (c) => c.company_code.toLowerCase() === code.toLowerCase() && c.id !== excludeId
  );
}

export const listCompanies = async (): Promise<Company[]> => {
  // Simulate API delay
  await new Promise((res) => setTimeout(res, 300));
  return [...companies];
};

export const createCompany = async (newCompany: Omit<Company, "id">): Promise<Company> => {
  if (!isCompanyCodeUnique(newCompany.company_code)) {
    throw new Error("Company code must be unique");
  }

  const company: Company = {
    id: uuidv4(),
    ...newCompany,
  };
  companies.push(company);
  return company;
};

export const updateCompany = async (
  id: string,
  updatedFields: Partial<Omit<Company, "id">>
): Promise<Company> => {
  const index = companies.findIndex((c) => c.id === id);
  if (index === -1) {
    throw new Error("Company not found");
  }

  if (
    updatedFields.company_code &&
    !isCompanyCodeUnique(updatedFields.company_code, id)
  ) {
    throw new Error("Company code must be unique");
  }

  companies[index] = {
    ...companies[index],
    ...updatedFields,
  };

  return companies[index];
};

export const countActiveCompanies = (): number => {
  return companies.filter((c) => c.status === "Active").length;
};


