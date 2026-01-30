# 🏗️ SHARED UI STRATEGY - APP SHELL
**Proposal**: Move Common UI Components to Shared Library

---

## 💡 **THE SUGGESTION**

**YES!** Moving the App Shell components (Login, Sidebar, Header, StatusBar) to a common location is the **Code Gold Standard** for modular ERPs.

### **Why?**
1.  **Consistency**: One Sidebar definition = Same look across Retail, HRM, FMS.
2.  **Maintenance**: Update the logo or menu structure in ONE place.
3.  **Performance**: Shared chunks in build (if using shared dependencies).
4.  **Developer Experience**: "Import and use" rather than "Copy and paste".

---

## 📍 **WHERE TO MOVE?**

We identified two potential locations, but `Common` is cleaner for cross-module sharing.

**Destination**: `c:\00mindra\olivine-platform\Common\ui-canon`

### **Proposed Structure:**

```
Common/ui-canon/
├── components/
│   ├── shell/
│   │   ├── Sidebar.tsx        # Unified Navigation
│   │   ├── AppHeader.tsx      # Top Bar & User Menu
│   │   ├── StatusBar.tsx      # System Status
│   │   └── AppShell.tsx       # Wrapper Component
│   └── auth/
│       └── LoginForm.tsx      # Standard Login Screen
```

---

## 🛠️ **HOW TO IMPLEMENT**

### **1. Move the Components**
Extract `Sidebar.tsx`, `AppHeader.tsx`, etc. from `Retail/frontend` (or wherever they are best defined now) and move them to `Common/ui-canon`.

### **2. Configure Configuration (tsconfig.json)**
Ensure all modules can import from Common.

```json
// in tsconfig.json
"paths": {
  "@common-ui/*": ["../Common/ui-canon/components/*"]
}
```

### **3. Consuming in App**
Each module (Retail, HRM, etc.) then becomes a content provider wrapped in the shell:

```tsx
// Retail/frontend/src/App.tsx
import { AppShell } from '@common-ui/shell';

function App() {
  return (
    <AppShell
      module="Retail"
      menuItems={retailMenu}
    >
      <RetailRoutes />
    </AppShell>
  );
}
```

---

## 🚀 **NEXT STEPS**

In the next session, we can:
1.  **Refactor**: Move the components to `Common/ui-canon`.
2.  **Export**: Create an `index.ts` to export them.
3.  **Update Retail**: Refactor Retail to use the shared shell.
4.  **Standardize**: Ensure HRM/FMS use the same shell.

**This is the best way to ensure the "Unified Platform" feel.**
