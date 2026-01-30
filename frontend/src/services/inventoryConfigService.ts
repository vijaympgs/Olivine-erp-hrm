import apiClient from "./api";

// ==============================================================================
// TYPES
// ==============================================================================

export interface ValuationMethod {
    id: string;
    company: string;
    company_name?: string;
    method: "FIFO" | "LIFO" | "WEIGHTED_AVG";
    method_display?: string;
    is_active: boolean;
    created_at?: string;
    updated_at?: string;
}

export interface InventoryParameter {
    id: string;
    company: string;
    company_name?: string;
    allow_negative_stock: boolean;
    auto_reorder_enabled: boolean;
    default_valuation_method: string;
    stock_take_variance_threshold: number;
    created_at?: string;
    updated_at?: string;
}

export interface ApprovalRule {
    rule_id: string;
    company: string;
    company_name?: string;
    rule_type: "ADJUSTMENT" | "TRANSFER" | "STOCK_TAKE";
    rule_type_display?: string;
    threshold_amount?: number;
    threshold_quantity?: number;
    approver_role: string;
    is_active: boolean;
    created_at?: string;
    updated_at?: string;
}

export interface MovementType {
    type_id: string;
    company: string;
    code: string;
    name: string;
    direction: "IN" | "OUT" | "TRANSFER";
    direction_display?: string;
    is_system: boolean;
    is_active: boolean;
    created_at?: string;
}

export interface AdjustmentReasonCode {
    reason_id: string;
    company: string;
    reason_code: string;
    description: string;
    is_negative: boolean;
    is_active: boolean;
    created_at?: string;
}

// ==============================================================================
// VALUATION METHOD SERVICE
// ==============================================================================

export const valuationMethodService = {
    async getByCompany(companyId: string): Promise<ValuationMethod | null> {
        try {
            const response = await apiClient.get<ValuationMethod[]>('/inventory/valuation-methods/', {
                params: { company_id: companyId }
            });
            return response.data.length > 0 ? response.data[0] : null;
        } catch (error) {
            console.error('Error fetching valuation method:', error);
            throw error;
        }
    },

    async create(data: Partial<ValuationMethod>): Promise<ValuationMethod> {
        const response = await apiClient.post<ValuationMethod>('/inventory/valuation-methods/', data);
        return response.data;
    },

    async update(id: string, data: Partial<ValuationMethod>): Promise<ValuationMethod> {
        const response = await apiClient.patch<ValuationMethod>(`/inventory/valuation-methods/${id}/`, data);
        return response.data;
    }
};

// ==============================================================================
// INVENTORY PARAMETER SERVICE
// ==============================================================================

export const inventoryParameterService = {
    async getByCompany(companyId: string): Promise<InventoryParameter | null> {
        try {
            const response = await apiClient.get<InventoryParameter[]>('/inventory/parameters/', {
                params: { company_id: companyId }
            });
            return response.data.length > 0 ? response.data[0] : null;
        } catch (error) {
            console.error('Error fetching inventory parameters:', error);
            throw error;
        }
    },

    async create(data: Partial<InventoryParameter>): Promise<InventoryParameter> {
        const response = await apiClient.post<InventoryParameter>('/inventory/parameters/', data);
        return response.data;
    },

    async update(id: string, data: Partial<InventoryParameter>): Promise<InventoryParameter> {
        const response = await apiClient.patch<InventoryParameter>(`/inventory/parameters/${id}/`, data);
        return response.data;
    }
};

// ==============================================================================
// APPROVAL RULE SERVICE
// ==============================================================================

export const approvalRuleService = {
    async getAll(filters?: { company_id?: string; rule_type?: string; is_active?: boolean }): Promise<ApprovalRule[]> {
        const response = await apiClient.get<ApprovalRule[]>('/inventory/approval-rules/', {
            params: filters
        });
        return response.data;
    },

    async create(data: Partial<ApprovalRule>): Promise<ApprovalRule> {
        const response = await apiClient.post<ApprovalRule>('/inventory/approval-rules/', data);
        return response.data;
    },

    async update(id: string, data: Partial<ApprovalRule>): Promise<ApprovalRule> {
        const response = await apiClient.patch<ApprovalRule>(`/inventory/approval-rules/${id}/`, data);
        return response.data;
    },

    async delete(id: string): Promise<void> {
        await apiClient.delete(`/inventory/approval-rules/${id}/`);
    },

    async toggleActive(id: string, isActive: boolean): Promise<ApprovalRule> {
        const response = await apiClient.patch<ApprovalRule>(`/inventory/approval-rules/${id}/`, {
            is_active: isActive
        });
        return response.data;
    }
};

// ==============================================================================
// MOVEMENT TYPE SERVICE
// ==============================================================================

export const movementTypeService = {
    async getAll(filters?: { company_id?: string; direction?: string; is_active?: boolean }): Promise<MovementType[]> {
        const response = await apiClient.get<MovementType[]>('/inventory/movement-types/', {
            params: filters
        });
        return response.data;
    },

    async create(data: Partial<MovementType>): Promise<MovementType> {
        const response = await apiClient.post<MovementType>('/inventory/movement-types/', data);
        return response.data;
    },

    async update(id: string, data: Partial<MovementType>): Promise<MovementType> {
        const response = await apiClient.patch<MovementType>(`/inventory/movement-types/${id}/`, data);
        return response.data;
    },

    async delete(id: string): Promise<void> {
        await apiClient.delete(`/inventory/movement-types/${id}/`);
    }
};

// ==============================================================================
// REASON CODE SERVICE
// ==============================================================================

export const reasonCodeService = {
    async getAll(filters?: { company_id?: string; is_active?: boolean }): Promise<AdjustmentReasonCode[]> {
        const response = await apiClient.get<AdjustmentReasonCode[]>('/inventory/reason-codes/', {
            params: filters
        });
        return response.data;
    },

    async create(data: Partial<AdjustmentReasonCode>): Promise<AdjustmentReasonCode> {
        const response = await apiClient.post<AdjustmentReasonCode>('/inventory/reason-codes/', data);
        return response.data;
    },

    async update(id: string, data: Partial<AdjustmentReasonCode>): Promise<AdjustmentReasonCode> {
        const response = await apiClient.patch<AdjustmentReasonCode>(`/inventory/reason-codes/${id}/`, data);
        return response.data;
    },

    async delete(id: string): Promise<void> {
        await apiClient.delete(`/inventory/reason-codes/${id}/`);
    }
};

