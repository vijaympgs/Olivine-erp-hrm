# Olivine ERP: Config-Driven Toolbar Implementation Reference

This document serves as the canonical reference for the **Standardized Toolbar Governance System** implemented across the Olivine ERP platform (Retail & FMS modules).

## 🏛️ 1. Architecture Overview

The system uses a **Registry-Driven approach**. Instead of hardcoding buttons on every page, use a central component that filters a "Super-String" of capabilities based on backend configuration.

### **Core Components:**
- **Central Registry (Backend)**: `ERPToolbarControl` and `ERPMenuItem` models in Django.
- **Unified Component (Frontend)**: `MasterToolbarConfigDriven.tsx`.
- **Logic Hook**: `useToolbarConfig.ts` (fetches permissions and registry strings).

---

## 🛠️ 2. The Character-Based Registry String

Toolbar capabilities are defined by a specific sequence of characters. Every character maps to a unique action, icon, and keyboard shortcut.

**The Super-String Mapping:**
`NESCKZTJAVPMRDHOXIYL1234QFBGW?`

| Char | Action | Shortcut | Char | Action | Shortcut |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **N** | New | F2 | **V** | View | F7 |
| **E** | Edit | F3 | **P** | Print | Ctrl+P |
| **S** | Save | F8 | **R** | Refresh | F9 |
| **C** | Cancel | Esc | **Z** | Authorize | F10 |
| **K** | Clear | F5 | **T** | Submit | Alt+S |
| **X** | Exit | Esc | **D** | Delete | F4 |

---

## 🚀 3. Implementation Workflow (How to wire a new UI)

To implement the toolbar on a new page (e.g., *Item Master*), follow these 3 steps:

### **Step A: Register in Backend**
Ensure the `menu_id` in the database has an `applicable_toolbar_config`.
*Example for Sales Ordered:* `NESCKZTJAVPMRDX` (Allows CRUD + Workflow + Output).

### **Step B: Import & Render**
In your React page component:

```tsx
import { MasterToolbar, MasterMode } from "../../../../core/ui-canon/frontend/ui/components/MasterToolbarConfigDriven";

export const SalesOrderPage: React.FC = () => {
    const [mode, setMode] = useState<MasterMode>('VIEW');

    return (
        <>
            <MasterToolbar 
                viewId="SALES_ORDER" // Matches menu_id in DB
                mode={mode} 
                onAction={(action) => handleToolbarAction(action)} 
            />
            {/* Page Content */}
        </>
    );
};
```

### **Step C: Handle Actions**
Implement the `handleToolbarAction` bridge to connect the toolbar to your page logic:

```tsx
const handleToolbarAction = (action: string) => {
    switch (action) {
        case 'new':    startNewTransaction(); break;
        case 'save':   submitForm(); break;
        case 'edit':   setMode('EDIT'); break;
        case 'exit':   navigate('/dashboard'); break;
        // ... etc
    }
};
```

---

## 🔄 4. Dynamic Mode Switching (The Pivot)

The toolbar automatically handles visibility based on the `mode` prop:

| Mode | Behavior |
| :--- | :--- |
| **VIEW** | Shows navigation, new, edit, print, search, and workflow buttons. |
| **EDIT / CREATE** | Swaps everything out for **Save**, **Cancel**, and **Clear**. |

This ensures the user only sees "Safe" actions during data entry, preventing accidental navigation or deletions while a form is dirty.

---

## 📈 5. Benefits of this Implementation
1. **Zero Frontend Maintenance**: Changing an icon or shortcut in `MasterToolbarConfigDriven.tsx` updates the entire ERP instantly.
2. **Permission Lock**: If a user lacks "Delete" permissions in the backend, the character `D` is stripped from the string, and the button disappears automatically.
3. **Consistency**: Shortcuts like **F8 (Save)** and **F2 (New)** are identical across 100+ screens.
4. **Lean Payload**: The UI only renders the buttons permitted for the specific context.

---
*Created: 2026-01-09*  
*Owner: Astra (ERP Development Owner)*
