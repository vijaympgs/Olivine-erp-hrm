import api from "./api";

export interface RequisitionLine {
    id?: string;
    item_id: string; // Canonical ID
    uom_id: string;  // Canonical ID
    item_variant?: string; // SKU ID
    requested_qty: number;
    required_by_date?: string;
    remarks?: string;
    // UI Display helpers
    item_code?: string;
    item_name?: string;
    uom_name?: string;
}

export interface PurchaseRequisition {
    id: string;
    pr_number: string;
    company: string;
    requesting_location: string;
    requested_by: string;
    date: string;
    required_by_date?: string;
    status: string;
    priority: string;
    supplier_hint?: string;
    remarks?: string;
    approval_required: boolean;
    lines: RequisitionLine[];
    created_at: string;
}

export const procurementService = {
    getRequisitions: async (params?: any) => {
        const response = await api.get('/procurement/requisitions/', { params });
        return response.data;
    },

    getRequisition: async (id: string) => {
        const response = await api.get(`/procurement/requisitions/${id}/`);
        return response.data;
    },

    createRequisition: async (data: Partial<PurchaseRequisition>) => {
        const response = await api.post('/procurement/requisitions/', data);
        return response.data;
    },

    updateRequisition: async (id: string, data: Partial<PurchaseRequisition>) => {
        const response = await api.patch(`/procurement/requisitions/${id}/`, data);
        return response.data;
    },

    deleteRequisition: async (id: string) => {
        await api.delete(`/procurement/requisitions/${id}/`);
    },

    submitRequisition: async (id: string) => {
        const response = await api.post(`/procurement/requisitions/${id}/submit/`);
        return response.data;
    },
    approveRequisition: async (id: string) => {
        const response = await api.post(`/procurement/requisitions/${id}/approve/`);
        return response.data;
    },
    rejectRequisition: async (id: string) => {
        const response = await api.post(`/procurement/requisitions/${id}/reject/`);
        return response.data;
    }
};

