import { useState, useCallback } from "react";
import { ProductLookupResult } from "@ui/components/ProductLookupModal";

export const useProductLookup = () => {
    const [isLookupOpen, setIsLookupOpen] = useState(false);
    const [selectedProduct, setSelectedProduct] = useState<ProductLookupResult | null>(null);

    const openLookup = useCallback(() => {
        setIsLookupOpen(true);
    }, []);

    const closeLookup = useCallback(() => {
        setIsLookupOpen(false);
    }, []);

    const handleProductSelect = useCallback((product: ProductLookupResult) => {
        setSelectedProduct(product);
        setIsLookupOpen(false);
    }, []);

    const clearSelection = useCallback(() => {
        setSelectedProduct(null);
    }, []);

    return {
        isLookupOpen,
        selectedProduct,
        openLookup,
        closeLookup,
        handleProductSelect,
        clearSelection
    };
};


