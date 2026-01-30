import axios from "axios";

const API_BASE_URL = "/api";

export interface Category {
    id: string;
    name: string;
    parent_id?: string | null;
    is_active: boolean;
    created_at: string;
    updated_at: string;
    children?: Category[]; // For frontend tree construction
}

export interface CategoryListItem {
    id: string;
    name: string;
    parent_id?: string | null;
    is_active: boolean;
    children?: CategoryListItem[];
}

export interface CategoryFilters {
    company?: string;
    search?: string;
    is_active?: boolean;
    parent_id?: string | null;
}

export interface CategoryCreateUpdate {
    name: string;
    parent_id?: string | null;
    is_active?: boolean;
}

class CategoryService {
    private baseUrl = `${API_BASE_URL}/categories`;

    async getCategories(filters?: CategoryFilters): Promise<CategoryListItem[]> {
        const params = new URLSearchParams();
        if (filters?.company) params.append('company', filters.company);
        if (filters?.search) params.append('search', filters.search);
        if (filters?.is_active !== undefined) params.append('is_active', String(filters.is_active));
        if (filters?.parent_id) params.append('parent', filters.parent_id);

        const response = await axios.get(`${this.baseUrl}/?${params.toString()}`);
        return response.data.results || response.data;
    }

    async getCategoryTree(companyId: string): Promise<CategoryListItem[]> {
        const flatList = await this.getCategories({ company: companyId });
        return this.buildTree(flatList);
    }

    private buildTree(items: CategoryListItem[], parentId: string | null = null): CategoryListItem[] {
        return items
            .filter(item => item.parent_id === parentId || (!parentId && !item.parent_id))
            .map(item => ({
                ...item,
                children: this.buildTree(items, item.id)
            }));
    }

    async getCategory(id: string): Promise<Category> {
        const response = await axios.get(`${this.baseUrl}/${id}/`);
        return response.data;
    }

    async createCategory(data: CategoryCreateUpdate): Promise<Category> {
        const response = await axios.post(`${this.baseUrl}/`, data);
        return response.data;
    }

    async updateCategory(id: string, data: Partial<CategoryCreateUpdate>): Promise<Category> {
        const response = await axios.patch(`${this.baseUrl}/${id}/`, data);
        return response.data;
    }

    async deactivateCategory(id: string): Promise<Category> {
        return this.updateCategory(id, { is_active: false });
    }

    async activateCategory(id: string): Promise<Category> {
        return this.updateCategory(id, { is_active: true });
    }
}

export const categoryService = new CategoryService();

