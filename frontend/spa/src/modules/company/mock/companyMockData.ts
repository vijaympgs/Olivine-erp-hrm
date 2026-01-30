// Mock data for local dev and UI prototyping
import { Company } from '../types/company';

export const companyMockData: Company[] = [
  {
    id: 'f5a7-1cde-481e-aa21-e5a1f52a1c7e',
    company_code: 'OLIVINE',
    company_name: 'Olivine Digital Retail Pvt Ltd',
    legal_entity_type: 'Pvt Ltd',
    address: {
      street: '123 Business Lane', city: 'Bangalore', region: 'Karnataka', country: 'India', zipcode: '560001',
    },
    default_currency: 'INR',
    timezone: 'Asia/Kolkata',
    status: 'Active'
  },
  {
    id: 'b1e2-12e4-39b3-8f63-8e1a0b71a63d',
    company_code: 'OLIVINE-UK',
    company_name: 'Olivine UK Enterprises',
    legal_entity_type: 'LLP',
    address: {
      street: '456 High Street', city: 'London', region: 'England', country: 'UK', zipcode: 'E1 6AN',
    },
    default_currency: 'GBP',
    timezone: 'Europe/London',
    status: 'Active'
  }
];

