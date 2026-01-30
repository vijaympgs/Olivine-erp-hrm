import apiClient from "./api";

// ==============================================================================
// TYPES
// ==============================================================================

export interface StockLevel {
    id: string;
    company: string;
    variant: string;
    variant_sku: string;
    variant_name: string;
    item_name: string;
    location: string;
    location_name: string;
    on_hand_qty: number;
    reserved_qty: number;
    available_qty: number;
    batch?: string;
    batch_number?: string;
    serial_number?: string;
    last_updated_at: string;
}

export interface LowStockItem {
    variant_id: string;
    variant_sku: string;
    variant_name: string;
    location_id: string;
    location_name: string;
    current_qty: number;
    min_qty: number;
    reorder_qty: number;
    shortage: number;
}

export interface IntercompanyTransferLine {
    id?: string;
    line_number: number;
    item: string;
    item_name?: string;
    item_variant: string;
    variant_sku?: string;
    variant_name?: string;
    uom: string;
    uom_name?: string;
    requested_qty: number;
    shipped_qty: number;
    received_qty: number;
    transfer_price: number;
    line_total: number;
    serial_numbers?: any;
    lot_number?: string;
    remarks?: string;
}

export interface IntercompanyTransfer {
    id?: string;
    transfer_number?: string;
    source_company: string;
    source_company_name?: string;
    source_location: string;
    source_location_name?: string;
    destination_company: string;
    destination_company_name?: string;
    destination_location: string;
    destination_location_name?: string;
    transfer_date: string;
    expected_receipt_date?: string;
    actual_receipt_date?: string;
    status: 'DRAFT' | 'SUBMITTED' | 'APPROVED' | 'IN_TRANSIT' | 'RECEIVED' | 'COMPLETED' | 'CANCELLED';
    status_display?: string;
    carrier_name?: string;
    tracking_number?: string;
    vehicle_number?: string;
    transfer_price_total: number;
    approved_by_source?: string;
    approved_by_destination?: string;
    remarks?: string;
    created_by?: string;
    created_by_name?: string;
    created_at?: string;
    updated_at?: string;
    lines: IntercompanyTransferLine[];
    currency_code?: string;
    invoicing_status?: string;
}

// ==============================================================================
// INVENTORY SERVICE
// ==============================================================================

export const inventoryService = {
    // STOCK LEVELS
    async getStockLevels(filters?: { company_id?: string; location?: string; variant?: string; batch?: string; search?: string }): Promise<StockLevel[]> {
        const response = await apiClient.get<StockLevel[]>('/inventory/levels/', {
            params: filters
        });
        return response.data;
    },

    async getLowStock(companyId: string, locationId?: string): Promise<LowStockItem[]> {
        const response = await apiClient.get<LowStockItem[]>('/inventory/levels/low_stock/', {
            params: { company: companyId, location: locationId }
        });
        return response.data;
    },

    // MOVEMENTS
    async getMovements(filters?: any): Promise<any[]> {
        const response = await apiClient.get('/inventory/movements/', { params: filters });
        return response.data;
    },

    async getInventorySummary(companyId: string): Promise<{ total_items: number; total_quantity: number; location_count: number; low_stock_count: number }> {
        const response = await apiClient.get('/inventory/levels/summary/', {
            params: { company_id: companyId }
        });
        return response.data;
    },

    // INTERCOMPANY TRANSFERS
    async getIntercompanyTransfers(filters?: { company_id?: string; status?: string; search?: string }): Promise<IntercompanyTransfer[]> {
        const response = await apiClient.get<IntercompanyTransfer[]>('/inventory/intercompany-transfers/', {
            params: filters
        });
        return response.data;
    },

    async getIntercompanyTransfer(id: string): Promise<IntercompanyTransfer> {
        const response = await apiClient.get<IntercompanyTransfer>(`/inventory/intercompany-transfers/${id}/`);
        return response.data;
    },

    async createIntercompanyTransfer(data: Partial<IntercompanyTransfer>): Promise<IntercompanyTransfer> {
        const response = await apiClient.post<IntercompanyTransfer>('/inventory/intercompany-transfers/', data);
        return response.data;
    },

    async updateIntercompanyTransfer(id: string, data: Partial<IntercompanyTransfer>): Promise<IntercompanyTransfer> {
        const response = await apiClient.put<IntercompanyTransfer>(`/inventory/intercompany-transfers/${id}/`, data);
        return response.data;
    },

    async deleteIntercompanyTransfer(id: string): Promise<void> {
        await apiClient.delete(`/inventory/intercompany-transfers/${id}/`);
    },

    // Workflow Actions
    async submitIntercompanyTransfer(id: string): Promise<IntercompanyTransfer> {
        const response = await apiClient.post<IntercompanyTransfer>(`/inventory/intercompany-transfers/${id}/submit/`);
        return response.data;
    },

    async approveIntercompanyTransfer(id: string): Promise<IntercompanyTransfer> {
        const response = await apiClient.post<IntercompanyTransfer>(`/inventory/intercompany-transfers/${id}/approve/`);
        return response.data;
    },

    async shipIntercompanyTransfer(id: string): Promise<IntercompanyTransfer> {
        const response = await apiClient.post<IntercompanyTransfer>(`/inventory/intercompany-transfers/${id}/ship/`);
        return response.data;
    },

    async receiveIntercompanyTransfer(id: string, data?: any): Promise<IntercompanyTransfer> {
        const response = await apiClient.post<IntercompanyTransfer>(`/inventory/intercompany-transfers/${id}/receive/`, data);
        return response.data;
    },

    async completeIntercompanyTransfer(id: string): Promise<IntercompanyTransfer> {
        const response = await apiClient.post<IntercompanyTransfer>(`/inventory/intercompany-transfers/${id}/complete/`);
        return response.data;
    },

    async cancelIntercompanyTransfer(id: string): Promise<IntercompanyTransfer> {
        const response = await apiClient.post<IntercompanyTransfer>(`/inventory/intercompany-transfers/${id}/cancel/`);
        return response.data;
    },

    // PDF Generation
    async downloadShadowInvoice(id: string): Promise<Blob> {
        const response = await apiClient.get(`/inventory/intercompany-transfers/${id}/shadow-invoice/`, {
            responseType: 'blob'
        });
        return response.data;
    },

    // Phase 3: Derived Pricing
    async getTransferPrice(itemVariantId: string, priceListId?: string, quantity?: number): Promise<{
        unit_price: number;
        price_source: string;
        price_list_name: string | null;
        currency: string;
        found: boolean;
    }> {
        const response = await apiClient.post('/inventory/intercompany-transfers/get_price/', {
            item_variant_id: itemVariantId,
            price_list_id: priceListId,
            quantity: quantity || 1
        });
        return response.data;
    }
};


