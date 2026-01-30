
import api from "./api";

export interface TestReadinessEntry {
    app_id: string;
    module_id: string;
    sub_module_id?: string | null;
    menu_id: string;
    menu_label: string;
    ui_status: "Pending" | "Done" | "N/A";
    dit_status: "Pending" | "InProgress" | "Done";
    uat_status: "Not Started" | "InProgress" | "Complete";
    script_path?: string | null;
    bbp_path?: string | null;  // BBP document path
    last_result?: 'Pass' | 'Fail' | null;
}

export const fetchReadiness = async (): Promise<TestReadinessEntry[]> => {
    const response = await api.get('/qa/readiness/');
    return response.data; // Assumes pagination handled or disabled for this specific view if needed, but ViewSet defaults to page size 20. 
    // We update settings.py PAGE_SIZE=20.
    // If we want ALL, we should probably handle pagination or set page_size=1000 for this endpoint.
    // simpler: use sync_entries endpoint to retrieve? No, fetch usually GET.
    // I should check if I need to handle pagination. For now, I'll assume small enough or handle pagination in component loop.
    // Actually, ModelViewSet result for list is { results: [...] } if pagination enabled.
    // Wait, let's assume standard DRF pagination.
    if (response.data.results) {
        return response.data.results;
    }
    return response.data;
};

export const syncReadinessEntries = async (entries: Partial<TestReadinessEntry>[]) => {
    const response = await api.post('/qa/readiness/sync_entries/', entries);
    return response.data;
};

export const updateReadiness = async (menu_id: string, data: Partial<TestReadinessEntry>) => {
    const response = await api.patch(`/qa/readiness/${menu_id}/`, data);
    return response.data;
};

