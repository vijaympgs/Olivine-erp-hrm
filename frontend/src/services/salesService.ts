import api from "./api";

// ----------------------------------------------------------------------
// Enums & Types
// ----------------------------------------------------------------------

export type QuoteStatus = 'DRAFT' | 'SUBMITTED' | 'APPROVED' | 'SENT_TO_CUSTOMER' | 'ACCEPTED' | 'REJECTED' | 'EXPIRED' | 'PARTIALLY_CONVERTED' | 'FULLY_CONVERTED' | 'CANCELLED';
export type OrderStatus = 'DRAFT' | 'PENDING_APPROVAL' | 'APPROVED' | 'CONFIRMED' | 'PROCESSING' | 'PARTIALLY_SHIPPED' | 'FULLY_SHIPPED' | 'PARTIALLY_INVOICED' | 'FULLY_INVOICED' | 'DELIVERED' | 'CLOSED' | 'CANCELLED';
export type InvoiceStatus = 'DRAFT' | 'VALIDATED' | 'APPROVED' | 'SENT_TO_CUSTOMER' | 'PARTIALLY_PAID' | 'FULLY_PAID' | 'OVERDUE' | 'WRITTEN_OFF' | 'CANCELLED';
export type ReturnStatus = 'DRAFT' | 'PENDING_APPROVAL' | 'APPROVED' | 'RECEIVED' | 'INSPECTING' | 'ACCEPTED' | 'REJECTED' | 'REFUNDED' | 'EXCHANGED' | 'CLOSED' | 'CANCELLED';

export interface SalesQuoteLine {
    id?: string;
    line_number?: number;
    item: string; // ID
    item_variant?: string; // ID
    uom: string; // ID
    quantity: number;
    unit_price: number;
    discount_percent?: number;
    tax_percent?: number;
    line_total?: number;
    delivery_date?: string;
    remarks?: string;
    // Display helpers (Read Only)
    item_code?: string;
    item_name?: string;
    variant_code?: string;
    uom_code?: string;
}

export interface SalesQuote {
    id: string;
    quote_number: string;
    company: string; // ID
    customer: string; // ID
    quote_date: string;
    valid_until_date: string;
    quote_status: QuoteStatus;
    currency_code: string;
    subtotal: number;
    tax_amount: number;
    grand_total: number;
    remarks?: string;
    lines: SalesQuoteLine[];
    created_at?: string;
    created_by?: string;
    // Display helpers (Read Only)
    customer_name?: string;
    sales_person_name?: string;
    location_name?: string;
    customer_details?: any; // Full object in detail view
}

export interface SalesOrderLine {
    id?: string;
    line_number?: number;
    item: string;
    item_variant?: string;
    uom: string;
    ordered_qty: number;
    unit_price: number;
    discount_percent?: number;
    tax_percent?: number;
    line_total?: number;
    warehouse_location?: string; // ID
    required_delivery_date?: string;
    // Display helpers
    item_code?: string;
    item_name?: string;
    variant_code?: string;
    uom_code?: string;
}

export interface SalesOrder {
    id: string;
    order_number: string;
    company: string;
    customer: string;
    order_date: string;
    required_delivery_date?: string;
    order_status: OrderStatus;
    currency_code: string;
    grand_total: number;
    lines: SalesOrderLine[];
    shipping_address?: string;
    billing_address?: string;
    created_at?: string;
    // Display helpers
    customer_name?: string;
    sales_person_name?: string;
    customer_details?: any;
    location_name?: string;
    warehouse_location?: string;
}

export interface SalesInvoiceLine {
    id?: string;
    line_number?: number;
    item?: string;
    description: string;
    uom?: string;
    quantity_invoiced: number;
    unit_price_invoiced: number;
    line_total: number;
    // Display helpers
    item_code?: string;
    item_name?: string;
}

export interface SalesInvoice {
    id: string;
    invoice_number: string;
    company: string;
    customer: string;
    invoice_date: string;
    due_date: string;
    invoice_status: InvoiceStatus;
    grand_total: number;
    amount_due: number;
    lines: SalesInvoiceLine[];
    created_at?: string;
    // Display helpers
    customer_name?: string;
    customer_details?: any;
}

export interface SalesReturnLine {
    id?: string;
    item: string;
    return_qty_requested: number;
    reason_code: string;
    return_disposition?: string;
    // Display helpers
    item_code?: string;
    item_name?: string;
}

export interface SalesReturn {
    id: string;
    rma_number: string;
    company: string;
    customer: string;
    return_status: ReturnStatus;
    return_type: string;
    lines: SalesReturnLine[];
    created_at?: string;
    // Display helpers
    customer_name?: string;
    customer_details?: any;
}

export interface SalesConfig {
    id?: string;
    company: string;
    quote_enabled: boolean;
    quote_validity_days: number;
    quote_revision_enabled: boolean;
    sales_approval_matrix?: any[];
}

// ----------------------------------------------------------------------
// Service
// ----------------------------------------------------------------------

export const salesService = {
    // --- QUOTES ---
    getQuotes: async (params?: any) => {
        const response = await api.get('/sales/quotes/', { params });
        return response.data;
    },
    getQuote: async (id: string) => {
        const response = await api.get(`/sales/quotes/${id}/`);
        return response.data;
    },
    createQuote: async (data: Partial<SalesQuote>) => {
        const response = await api.post('/sales/quotes/', data);
        return response.data;
    },
    updateQuote: async (id: string, data: Partial<SalesQuote>) => {
        const response = await api.patch(`/sales/quotes/${id}/`, data);
        return response.data;
    },
    deleteQuote: async (id: string) => {
        await api.delete(`/sales/quotes/${id}/`);
    },
    submitQuote: async (id: string) => {
        const response = await api.post(`/sales/quotes/${id}/submit/`);
        return response.data;
    },
    approveQuote: async (id: string) => {
        const response = await api.post(`/sales/quotes/${id}/approve/`);
        return response.data;
    },
    rejectQuote: async (id: string) => {
        const response = await api.post(`/sales/quotes/${id}/reject/`);
        return response.data;
    },

    // --- ORDERS ---
    getOrders: async (params?: any) => {
        const response = await api.get('/sales/orders/', { params });
        return response.data;
    },
    getOrder: async (id: string) => {
        const response = await api.get(`/sales/orders/${id}/`);
        return response.data;
    },
    createOrder: async (data: Partial<SalesOrder>) => {
        const response = await api.post('/sales/orders/', data);
        return response.data;
    },
    updateOrder: async (id: string, data: Partial<SalesOrder>) => {
        const response = await api.patch(`/sales/orders/${id}/`, data);
        return response.data;
    },
    deleteOrder: async (id: string) => {
        await api.delete(`/sales/orders/${id}/`);
    },
    submitOrder: async (id: string) => {
        const response = await api.post(`/sales/orders/${id}/submit/`);
        return response.data;
    },

    // --- INVOICES ---
    getInvoices: async (params?: any) => {
        const response = await api.get('/sales/invoices/', { params });
        return response.data;
    },
    getInvoice: async (id: string) => {
        const response = await api.get(`/sales/invoices/${id}/`);
        return response.data;
    },
    createInvoice: async (data: Partial<SalesInvoice>) => {
        const response = await api.post('/sales/invoices/', data);
        return response.data;
    },

    // --- RETURNS ---
    getReturns: async (params?: any) => {
        const response = await api.get('/sales/returns/', { params });
        return response.data;
    },
    getReturn: async (id: string) => {
        const response = await api.get(`/sales/returns/${id}/`);
        return response.data;
    },
    createReturn: async (data: Partial<SalesReturn>) => {
        const response = await api.post('/sales/returns/', data);
        return response.data;
    },
    updateReturn: async (id: string, data: Partial<SalesReturn>) => {
        const response = await api.patch(`/sales/returns/${id}/`, data);
        return response.data;
    },

    // --- CONFIG ---
    getConfig: async () => {
        const response = await api.get('/sales/config/');
        return response.data;
    },
    updateConfig: async (data: Partial<SalesConfig>) => {
        const response = await api.patch('/sales/config/', data);
        return response.data;
    }
};
