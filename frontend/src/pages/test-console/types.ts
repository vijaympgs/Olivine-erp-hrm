
import { ReactNode } from "react";
import { TestReadinessEntry } from "@services/qaService";

export interface EnrichedSuite extends TestReadinessEntry {
    name: string;
    path: string; // Breadcrumb path
    bbp_path?: string | null;
}

export interface ModuleDef {
    id: string;
    label: string;
    suites: EnrichedSuite[];
}

export interface ApplicationDef {
    id: string;
    label: string;
    icon: ReactNode;
    description: string;
    modules: ModuleDef[];
}


