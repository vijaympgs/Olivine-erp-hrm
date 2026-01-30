# State Patterns Reference

**Version**: 1.0  
**Stack**: React (useState, useEffect, useCallback, useMemo)  
**Purpose**: Standardized state management patterns for ERP modules

---

## 🎯 Overview

This document defines the canonical state patterns used across all Master and Transaction screens. All implementations must follow these patterns for consistency.

---

## 📋 List State Pattern

Used for all list/table views (Masters, Transactions).

### Standard List State

```javascript
// Core data state
const [data, setData] = useState([]);
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);

// Selection state
const [selectedItems, setSelectedItems] = useState([]);
const [selectedItem, setSelectedItem] = useState(null);

// Filter state
const [filters, setFilters] = useState({
  search: '',
  status: 'all',
  category: 'all',
  dateRange: null,
  // Module-specific filters...
});

// View state
const [viewMode, setViewMode] = useState('table'); // 'table' | 'card' | 'tree'
const [density, setDensity] = useState('comfortable'); // 'compact' | 'comfortable'

// Pagination state
const [pagination, setPagination] = useState({
  page: 1,
  limit: 20,
  total: 0,
});

// Sort state
const [sortBy, setSortBy] = useState({ 
  field: 'created_at', 
  direction: 'desc' 
});

// Modal/Form state
const [showForm, setShowForm] = useState(false);
const [formMode, setFormMode] = useState('create'); // 'create' | 'edit' | 'view'
```

### List State Actions

```javascript
// Fetch data
const fetchData = useCallback(async () => {
  setLoading(true);
  setError(null);
  try {
    const params = new URLSearchParams({
      page: pagination.page,
      limit: pagination.limit,
      sort: sortBy.field,
      order: sortBy.direction,
      search: filters.search,
      status: filters.status !== 'all' ? filters.status : '',
    });
    
    const response = await fetch(`${API_URL}?${params}`);
    if (!response.ok) throw new Error('Failed to fetch data');
    
    const result = await response.json();
    setData(result.data);
    setPagination(prev => ({ ...prev, total: result.total }));
  } catch (err) {
    setError(err.message);
  } finally {
    setLoading(false);
  }
}, [pagination.page, pagination.limit, sortBy, filters]);

// Handle create
const handleCreate = useCallback(() => {
  setSelectedItem(null);
  setFormMode('create');
  setShowForm(true);
}, []);

// Handle edit
const handleEdit = useCallback((item) => {
  setSelectedItem(item);
  setFormMode('edit');
  setShowForm(true);
}, []);

// Handle delete
const handleDelete = useCallback(async (id) => {
  if (!confirm('Are you sure you want to delete this item?')) return;
  
  setLoading(true);
  try {
    await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
    setData(prev => prev.filter(item => item.id !== id));
  } catch (err) {
    setError(err.message);
  } finally {
    setLoading(false);
  }
}, []);

// Handle sort
const handleSort = useCallback((field) => {
  setSortBy(prev => ({
    field,
    direction: prev.field === field && prev.direction === 'asc' ? 'desc' : 'asc',
  }));
}, []);

// Handle filter change
const handleFilterChange = useCallback((key, value) => {
  setFilters(prev => ({ ...prev, [key]: value }));
  setPagination(prev => ({ ...prev, page: 1 })); // Reset to first page
}, []);

// Clear filters
const clearFilters = useCallback(() => {
  setFilters({
    search: '',
    status: 'all',
    category: 'all',
    dateRange: null,
  });
}, []);
```

### Filtered & Sorted Data (Memoized)

```javascript
const filteredData = useMemo(() => {
  return data.filter(item => {
    const matchesSearch = !filters.search || 
      item.name?.toLowerCase().includes(filters.search.toLowerCase()) ||
      item.code?.toLowerCase().includes(filters.search.toLowerCase());
    
    const matchesStatus = filters.status === 'all' || item.status === filters.status;
    const matchesCategory = filters.category === 'all' || item.category === filters.category;
    
    return matchesSearch && matchesStatus && matchesCategory;
  });
}, [data, filters]);

const sortedData = useMemo(() => {
  return [...filteredData].sort((a, b) => {
    const aVal = a[sortBy.field];
    const bVal = b[sortBy.field];
    
    if (aVal == null) return 1;
    if (bVal == null) return -1;
    
    const comparison = typeof aVal === 'string' 
      ? aVal.localeCompare(bVal)
      : aVal - bVal;
    
    return sortBy.direction === 'asc' ? comparison : -comparison;
  });
}, [filteredData, sortBy]);
```

---

## 📝 Form State Pattern

Used for all create/edit forms.

### Standard Form State

```javascript
// Form data
const [formData, setFormData] = useState({
  id: null,
  code: '',
  name: '',
  description: '',
  status: 'active',
  // Module-specific fields...
});

// Validation state
const [errors, setErrors] = useState({});
const [touched, setTouched] = useState({});

// Submission state
const [isSubmitting, setIsSubmitting] = useState(false);
const [isDirty, setIsDirty] = useState(false);

// For edit mode - track original data
const [originalData, setOriginalData] = useState(null);
```

### Form Initialization

```javascript
// Initialize form with data (for edit mode)
useEffect(() => {
  if (initialData) {
    setFormData(initialData);
    setOriginalData(initialData);
    setIsDirty(false);
  } else {
    // Reset to defaults for create mode
    setFormData({
      id: null,
      code: '',
      name: '',
      description: '',
      status: 'active',
    });
    setOriginalData(null);
    setIsDirty(false);
  }
  setErrors({});
  setTouched({});
}, [initialData]);
```

### Form Field Handlers

```javascript
// Handle field change
const handleChange = useCallback((field, value) => {
  setFormData(prev => ({ ...prev, [field]: value }));
  setIsDirty(true);
  
  // Clear error on change
  if (errors[field]) {
    setErrors(prev => {
      const newErrors = { ...prev };
      delete newErrors[field];
      return newErrors;
    });
  }
}, [errors]);

// Handle field blur (for touched state)
const handleBlur = useCallback((field) => {
  setTouched(prev => ({ ...prev, [field]: true }));
}, []);

// Validate single field
const validateField = useCallback((field, value) => {
  switch (field) {
    case 'code':
      if (!value?.trim()) return 'Code is required';
      if (value.length > 20) return 'Code must be 20 characters or less';
      break;
    case 'name':
      if (!value?.trim()) return 'Name is required';
      if (value.length > 100) return 'Name must be 100 characters or less';
      break;
    // Add more field validations...
  }
  return null;
}, []);

// Validate entire form
const validateForm = useCallback(() => {
  const newErrors = {};
  
  Object.keys(formData).forEach(field => {
    const error = validateField(field, formData[field]);
    if (error) newErrors[field] = error;
  });
  
  setErrors(newErrors);
  return Object.keys(newErrors).length === 0;
}, [formData, validateField]);
```

### Form Submission

```javascript
const handleSubmit = async (e) => {
  e.preventDefault();
  
  // Mark all fields as touched
  const allTouched = Object.keys(formData).reduce((acc, key) => {
    acc[key] = true;
    return acc;
  }, {});
  setTouched(allTouched);
  
  // Validate
  if (!validateForm()) return;
  
  setIsSubmitting(true);
  try {
    if (formData.id) {
      // Update
      await fetch(`${API_URL}/${formData.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
    } else {
      // Create
      await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
    }
    
    onSave(formData);
    onClose();
  } catch (err) {
    setErrors({ submit: err.message });
  } finally {
    setIsSubmitting(false);
  }
};

// Handle cancel with dirty check
const handleCancel = useCallback(() => {
  if (isDirty) {
    if (!confirm('You have unsaved changes. Are you sure you want to cancel?')) {
      return;
    }
  }
  onClose();
}, [isDirty, onClose]);
```

---

## 🔄 Modal State Pattern

Used for modal dialogs (forms, confirmations, details).

### Standard Modal State

```javascript
// Modal visibility
const [isOpen, setIsOpen] = useState(false);

// Modal mode
const [mode, setMode] = useState('create'); // 'create' | 'edit' | 'view' | 'delete'

// Modal data
const [modalData, setModalData] = useState(null);

// Loading state for modal actions
const [modalLoading, setModalLoading] = useState(false);
```

### Modal Actions

```javascript
// Open modal for create
const openCreateModal = useCallback(() => {
  setModalData(null);
  setMode('create');
  setIsOpen(true);
}, []);

// Open modal for edit
const openEditModal = useCallback((item) => {
  setModalData(item);
  setMode('edit');
  setIsOpen(true);
}, []);

// Open modal for view
const openViewModal = useCallback((item) => {
  setModalData(item);
  setMode('view');
  setIsOpen(true);
}, []);

// Open delete confirmation
const openDeleteModal = useCallback((item) => {
  setModalData(item);
  setMode('delete');
  setIsOpen(true);
}, []);

// Close modal
const closeModal = useCallback(() => {
  setIsOpen(false);
  setModalData(null);
  setMode('create');
}, []);
```

---

## 🔀 Entity State Machine Pattern

Used for entities with status workflows.

### Status Definition

```javascript
// Status configuration
const STATUS_CONFIG = {
  draft: {
    label: 'Draft',
    color: 'bg-surface-100 text-surface-600',
    allowedTransitions: ['active', 'deleted'],
    actions: ['edit', 'delete', 'activate'],
  },
  active: {
    label: 'Active',
    color: 'bg-success-100 text-success-800',
    allowedTransitions: ['inactive'],
    actions: ['edit', 'deactivate'],
  },
  inactive: {
    label: 'Inactive',
    color: 'bg-warning-100 text-warning-800',
    allowedTransitions: ['active'],
    actions: ['activate'],
  },
  maintenance: {
    label: 'Maintenance',
    color: 'bg-accent-100 text-accent-800',
    allowedTransitions: ['active'],
    actions: ['activate'],
  },
};

// Check if transition is allowed
const canTransition = (currentStatus, newStatus) => {
  return STATUS_CONFIG[currentStatus]?.allowedTransitions?.includes(newStatus);
};

// Get allowed actions for status
const getAllowedActions = (status) => {
  return STATUS_CONFIG[status]?.actions || [];
};
```

### Status Transition Handler

```javascript
const handleStatusChange = useCallback(async (item, newStatus) => {
  if (!canTransition(item.status, newStatus)) {
    setError(`Cannot transition from ${item.status} to ${newStatus}`);
    return;
  }
  
  setLoading(true);
  try {
    await fetch(`${API_URL}/${item.id}/status`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: newStatus }),
    });
    
    setData(prev => prev.map(d => 
      d.id === item.id ? { ...d, status: newStatus } : d
    ));
  } catch (err) {
    setError(err.message);
  } finally {
    setLoading(false);
  }
}, []);
```

### Status Badge Component

```javascript
const StatusBadge = ({ status }) => {
  const config = STATUS_CONFIG[status] || {
    label: status,
    color: 'bg-surface-100 text-surface-600',
  };
  
  return (
    <span className={`px-2 py-1 text-xs font-medium rounded-full ${config.color}`}>
      {config.label}
    </span>
  );
};
```

---

## 🌐 API Hook Pattern

Reusable hooks for API operations.

### useApi Hook

```javascript
const useApi = (baseUrl) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const request = useCallback(async (method, endpoint = '', data = null) => {
    setLoading(true);
    setError(null);
    
    try {
      const config = {
        method,
        headers: { 'Content-Type': 'application/json' },
      };
      
      if (data && ['POST', 'PUT', 'PATCH'].includes(method)) {
        config.body = JSON.stringify(data);
      }
      
      const response = await fetch(`${baseUrl}${endpoint}`, config);
      
      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Request failed');
      }
      
      return await response.json();
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [baseUrl]);

  return {
    loading,
    error,
    get: (endpoint) => request('GET', endpoint),
    post: (endpoint, data) => request('POST', endpoint, data),
    put: (endpoint, data) => request('PUT', endpoint, data),
    patch: (endpoint, data) => request('PATCH', endpoint, data),
    delete: (endpoint) => request('DELETE', endpoint),
  };
};
```

### useCrud Hook

```javascript
const useCrud = (apiUrl) => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchAll = useCallback(async (params = {}) => {
    setLoading(true);
    try {
      const query = new URLSearchParams(params).toString();
      const response = await fetch(`${apiUrl}?${query}`);
      const result = await response.json();
      setData(result.data || result);
      return result;
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [apiUrl]);

  const fetchOne = useCallback(async (id) => {
    setLoading(true);
    try {
      const response = await fetch(`${apiUrl}/${id}`);
      return await response.json();
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [apiUrl]);

  const create = useCallback(async (item) => {
    setLoading(true);
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(item),
      });
      const newItem = await response.json();
      setData(prev => [...prev, newItem]);
      return newItem;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [apiUrl]);

  const update = useCallback(async (id, item) => {
    setLoading(true);
    try {
      const response = await fetch(`${apiUrl}/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(item),
      });
      const updatedItem = await response.json();
      setData(prev => prev.map(d => d.id === id ? updatedItem : d));
      return updatedItem;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [apiUrl]);

  const remove = useCallback(async (id) => {
    setLoading(true);
    try {
      await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });
      setData(prev => prev.filter(d => d.id !== id));
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [apiUrl]);

  return {
    data,
    loading,
    error,
    fetchAll,
    fetchOne,
    create,
    update,
    remove,
    setData,
  };
};
```

---

## 📊 Transaction State Pattern

Used for transaction screens (Sales, PO, GRN, etc.).

### Transaction Header State

```javascript
const [transaction, setTransaction] = useState({
  id: null,
  transactionNumber: '',
  transactionDate: new Date().toISOString().split('T')[0],
  referenceNumber: '',
  status: 'draft',
  notes: '',
  // Header-specific fields...
});
```

### Transaction Line Items State

```javascript
const [lineItems, setLineItems] = useState([]);

// Add line item
const addLineItem = useCallback(() => {
  setLineItems(prev => [...prev, {
    id: `temp-${Date.now()}`,
    itemId: null,
    description: '',
    quantity: 1,
    unitPrice: 0,
    discount: 0,
    tax: 0,
    total: 0,
  }]);
}, []);

// Update line item
const updateLineItem = useCallback((id, field, value) => {
  setLineItems(prev => prev.map(item => {
    if (item.id !== id) return item;
    
    const updated = { ...item, [field]: value };
    
    // Recalculate totals
    const qty = parseFloat(updated.quantity) || 0;
    const price = parseFloat(updated.unitPrice) || 0;
    const discount = parseFloat(updated.discount) || 0;
    const taxRate = parseFloat(updated.taxRate) || 0;
    
    const subtotal = qty * price;
    const discountAmount = subtotal * (discount / 100);
    const taxableAmount = subtotal - discountAmount;
    const taxAmount = taxableAmount * (taxRate / 100);
    
    updated.subtotal = subtotal;
    updated.discountAmount = discountAmount;
    updated.taxAmount = taxAmount;
    updated.total = taxableAmount + taxAmount;
    
    return updated;
  }));
}, []);

// Remove line item
const removeLineItem = useCallback((id) => {
  setLineItems(prev => prev.filter(item => item.id !== id));
}, []);
```

### Transaction Totals (Memoized)

```javascript
const totals = useMemo(() => {
  return lineItems.reduce((acc, item) => ({
    subtotal: acc.subtotal + (item.subtotal || 0),
    discount: acc.discount + (item.discountAmount || 0),
    tax: acc.tax + (item.taxAmount || 0),
    total: acc.total + (item.total || 0),
  }), { subtotal: 0, discount: 0, tax: 0, total: 0 });
}, [lineItems]);
```

### Transaction Workflow State

```javascript
const TRANSACTION_STATUS = {
  draft: {
    label: 'Draft',
    color: 'bg-surface-100 text-surface-600',
    next: ['submitted'],
    actions: ['edit', 'delete', 'submit'],
  },
  submitted: {
    label: 'Submitted',
    color: 'bg-primary-100 text-primary-800',
    next: ['approved', 'rejected'],
    actions: ['approve', 'reject'],
  },
  approved: {
    label: 'Approved',
    color: 'bg-success-100 text-success-800',
    next: ['posted'],
    actions: ['post'],
  },
  rejected: {
    label: 'Rejected',
    color: 'bg-accent-100 text-accent-800',
    next: ['draft'],
    actions: ['revise'],
  },
  posted: {
    label: 'Posted',
    color: 'bg-success-100 text-success-800',
    next: [],
    actions: ['view'],
  },
};
```

---

## 🎯 Usage in Prompts

When specifying state requirements in prompts, reference these patterns:

```
State Pattern:
- List: Standard list state (data, loading, filters, pagination)
- Form: Standard form state (formData, errors, isSubmitting)
- Modal: Standard modal state (isOpen, mode, modalData)
- Status: Use STATUS_CONFIG pattern with states [ACTIVE, INACTIVE, MAINTENANCE]
- API: Use useCrud hook for /api/pos/terminals/
```

---

## 📚 Related Documentation

- **Component Library**: `docs/steering/COMPONENT_LIBRARY.md`
- **Prompt Templates**: `docs/steering/prompts.master.md`
- **Design Tokens**: `../tokens/designTokens.js`
- **MST Templates**: `docs/templates/mst01.md`, `docs/templates/mst02.md`, `docs/templates/mst03.md`
- **TXN Templates**: `docs/templates/txn01.md`, `docs/templates/txn02.md`, `docs/templates/txn03.md`
