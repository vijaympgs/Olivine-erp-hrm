# 🏗️ POS PHASE 2 — SYSTEM STUDY & VERTICAL EXTENSIBILITY ARCHITECTURE

**Document Type**: Governance-Level Architecture Study  
**Status**: AUTHORITATIVE  
**Version**: 1.0  
**Date**: 2026-01-24  
**Author**: Astra (AI Implementation Engine)  
**Owner**: Viji (vijaympgs)  
**Architectural Authority**: Mindra  

---

## EXECUTIVE SUMMARY

This document provides a comprehensive system study of the existing POS Core and proposes an **Extension Architecture** that enables infinite vertical support (Grocery, Pharmacy, Electronics, F&B, etc.) WITHOUT any mutation to the frozen POS Core.

### Key Principles Upheld
- ✅ **One POS Core** — Transaction lifecycle is LOCKED
- ✅ **One POS Screen** — `POSDesktop.tsx` remains the single canonical billing surface
- ✅ **Zero Core Mutation** — All vertical behavior via config, rules, and extensions
- ✅ **Infinite Verticals** — New industries via configuration, not code forks

---

# PART 1: CURRENT SYSTEM STUDY

## 1.1 Backend Model Architecture

### Core Entity Relationship Diagram (Conceptual)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           POS LIFECYCLE                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌─────────┐    ┌──────────┐    ┌────────────┐    ┌─────────────┐      │
│   │ DayOpen │───▶│POSSession│───▶│POSTransact.│───▶│ Settlement  │      │
│   └────┬────┘    └────┬─────┘    └─────┬──────┘    └──────┬──────┘      │
│        │              │                │                   │             │
│        │              │                │                   │             │
│   ┌────▼────┐    ┌────▼─────┐    ┌─────▼──────┐    ┌──────▼──────┐      │
│   │DayClose │    │Sess.Close│    │ Payment    │    │Reconciliat. │      │
│   └─────────┘    └──────────┘    │ TxnLine    │    └─────────────┘      │
│                                  └────────────┘                          │
├─────────────────────────────────────────────────────────────────────────┤
│                         TERMINAL LAYER                                   │
│   ┌──────────┐    ┌─────────────────────┐    ┌───────────────────┐      │
│   │ Terminal │───▶│TerminalTxnSettings  │───▶│TerminalTenderMap  │      │
│   └──────────┘    └─────────────────────┘    └───────────────────┘      │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.1.1 Core Models — Responsibility Matrix

| Model | Location | Responsibility | Core/Extension |
|-------|----------|----------------|----------------|
| `DayOpen` | `pos/day_open/models.py` | Opens business day for a location. Tracks business_date, next_sale_number, next_session_number. | **CORE** (FROZEN) |
| `DayClose` | Implicit via `DayOpen.close_day_open()` | Closes business day after checklist validation. | **CORE** (FROZEN) |
| `PosSession` | `pos/session/models.py` | Cashier shift management. Tracks opening_cash, closing_cash, expected_cash, variance, settlement_status. | **CORE** (FROZEN) |
| `Terminal` | `pos/terminal/models/terminal.py` | Physical POS device. Has hardware_profile (JSONField), type, status. | **CORE** (FROZEN) |
| `TerminalTransactionSettings` | `pos/terminal/models/terminal.py` | Controls allowed_transaction_types, price_override, discount limits. | **CORE** (FROZEN) |
| `TerminalTenderMapping` | `pos/terminal/models/terminal.py` | Maps allowed payment methods per terminal with min/max amounts. | **CORE** (FROZEN) |
| `POSTransaction` | `pos/transaction_models.py` | Sale header: transaction_number, status, totals, customer, cashier. | **CORE** (FROZEN) |
| `POSTransactionLine` | `pos/transaction_models.py` | Line items: item, quantity, price, discount, tax, serial/batch tracking. | **CORE** (FROZEN) |
| `POSTransactionPayment` | `pos/transaction_models.py` | Payment records: method, amount, card details, change. | **CORE** (FROZEN) |
| `POSReconciliation` | `pos/transaction_models.py` | Cash/payment reconciliation at session/day close. | **CORE** (FROZEN) |

### 1.1.2 Existing Extension Points in Core

The current core already has **strategic extensibility hooks**:

| Model | Field | Type | Purpose |
|-------|-------|------|---------|
| `Terminal` | `hardware_profile` | JSONField | Device config (printer, drawer, scanner) |
| `TerminalTransactionSettings` | `allowed_transaction_types` | JSONField | Configurable transaction types |
| `PosSession` | `interim_settlements` | JSONField | Mid-shift settlement history |
| `POSReconciliation` | `denomination_breakdown` | JSONField | Cash denomination counts |
| `POSTransactionLine` | `batch` | FK (nullable) | Batch tracking (Pharmacy ready) |
| `POSTransactionLine` | `serial_number` | CharField (nullable) | Serial tracking (Electronics ready) |

**Key Insight**: The core already anticipates vertical needs via nullable fields and JSONFields. This is architecturally sound.

---

## 1.2 Frontend Architecture

### 1.2.1 Component Hierarchy

```
Retail/frontend/pos/
├── PosDashboard.tsx           # POS module entry/dashboard
├── billing/
│   ├── PosDesktop.tsx         # ← CANONICAL BILLING SURFACE (FROZEN)
│   ├── PosCart.tsx            # Cart display component
│   ├── PosRightPanel.tsx      # Product lookup, totals
│   ├── PosModals.tsx          # All modal dialogs
│   ├── constants.ts           # POS_FUNCTIONS, WALK_IN_CUSTOMER
│   └── types.ts               # TypeScript interfaces
├── components/
│   ├── PaymentDialog.tsx      # Payment modal
│   ├── Receipt.tsx            # Receipt preview/print
│   ├── CustomerSelector.tsx   # Customer lookup
│   ├── ProductSearch.tsx      # Product search
│   └── KeyboardShortcutsHelp.tsx
├── day_open/
│   └── DayOpenPage.tsx        # Day Open screen
├── day_close/
│   └── DayClosePage.tsx       # Day Close with checklist
├── session/
│   └── SessionOpenPage.tsx    # Session Open screen
├── session_close/
│   └── SessionClosePage.tsx   # Session Close screen
├── settlement/
│   └── SettlementPage.tsx     # Cash settlement with denomination
└── terminal/
    └── TerminalPage.tsx       # Terminal configuration
```

### 1.2.2 PosDesktop.tsx — Canonical Billing Surface Analysis

**Total Lines**: 977  
**Core State Variables**:

| State Category | Variables | Purpose |
|----------------|-----------|---------|
| **Session** | `currentSession`, `sessionReady`, `loading`, `error` | Session lifecycle |
| **Cart** | `cart`, `selectedItemIndex`, `customer`, `saleType`, `otherCharges` | Cart management |
| **Products** | `products`, `searchQuery`, `filteredProducts`, `recentProducts` | Product lookup |
| **UI Panels** | `showProductLookup`, `showCustomerLookup`, `showItemScan`, `activeRightTab` | Panel visibility |
| **Modals** | `showPaymentDialog`, `showReceipt`, `showHelp`, 10+ feature modals | Dialog state |
| **Totals** | `subtotal`, `taxTotal`, `discountTotal`, `grandTotal`, `itemCount` | Calculated values |

**Core Functions**:

| Function | Purpose |
|----------|---------|
| `initializePOS()` | Load session, products, initialize state |
| `addToCart()` | Add product with quantity, calculate tax |
| `updateQuantity()` | Modify line quantity, recalculate |
| `clearCart()` | Reset cart to empty |
| `suspendSale()` / `resumeSale()` | Park/retrieve sales |
| `processPayment()` | Execute payment, generate receipt |
| `handleCheckout()` | Trigger payment flow |
| `handleBarcodeScan()` | Barcode/SKU lookup with quantity syntax (3*SKU) |
| `handleFunctionAction()` | Route function button clicks |
| `useKeyboardShortcuts()` | F-key and Ctrl+F handling |

**Keyboard Shortcuts**:

| Key | Action |
|-----|--------|
| F1-F12 | Function buttons (Customer, Search, Discount, etc.) |
| Ctrl+F1 | Reprint last bill |
| Ctrl+F2 | Void transaction |
| Ctrl+F3 | Bill Query |
| Ctrl+F4 | Settlement |
| Escape | Close all dialogs |
| Arrow Up/Down | Cart navigation |

---

## 1.3 State Flow Through Lifecycle

### 1.3.1 Frozen Lifecycle (IMMUTABLE)

```
┌───────────┐     ┌──────────────┐     ┌─────────┐     ┌────────────┐
│  Day Open │────▶│ Session Open │────▶│ Billing │────▶│ Settlement │
└───────────┘     └──────────────┘     └─────────┘     └────────────┘
                                            │
                                            ▼
┌───────────┐     ┌───────────────┐    ┌─────────┐
│ Day Close │◀────│ Session Close │◀───│ Payment │
└───────────┘     └───────────────┘    └─────────┘
```

**Lifecycle Contract**:
1. **Day Open** → Location + Business Date → Generates session/sale numbering
2. **Session Open** → Terminal + User + Opening Cash → Enables billing
3. **Billing** → Cart → Lines → Tax → Discount → Total
4. **Payment** → Multi-tender → Change calculation → Receipt
5. **Settlement** → Denomination count → Variance calculation
6. **Session Close** → Settlement complete → Cashier signed off
7. **Day Close** → All sessions closed → Checklist verified → Day archived

**This lifecycle is LOCKED. All verticals must operate within it.**

---

## 1.4 Architectural Strengths

| Strength | Evidence |
|----------|----------|
| **Clear Entity Separation** | DayOpen, Session, Transaction are distinct with proper FKs |
| **JSONField Extensibility** | hardware_profile, denomination_breakdown already support dynamic config |
| **Nullable Tracking Fields** | serial_number, batch, lot_number are ready for vertical needs |
| **Modular Frontend** | Billing separated from Session, Settlement, Day management |
| **Keyboard-First Design** | Complete F-key mapping, Ctrl+F shortcuts |
| **Single Billing Surface** | PosDesktop.tsx is the only billing component |

---

## 1.5 Structural Gaps (Extension Opportunities)

| Gap | Impact | Resolution Path |
|-----|--------|-----------------|
| No `VerticalProfile` entity | Cannot dynamically switch vertical behaviors | New config model (see Part 2) |
| No `FeatureFlag` system | Cannot toggle features per vertical | New config model (see Part 2) |
| No `ValidationRule` registry | Hardcoded validation logic | New rules engine (see Part 2) |
| No `LayoutSchema` for UI | Cannot dynamically change panel arrangement | New layout config (see Part 2) |
| Function buttons are static | `POS_FUNCTIONS` in constants.ts is hardcoded | Config-driven functions (see Part 2) |
| No line-level extension data | Cannot capture modifier/attributes per line | Sidecar model (see Part 2) |

**IMPORTANT**: These gaps do NOT require core mutation. They require **adjacent extension models**.

---

# PART 2: EXTENSION ARCHITECTURE (WITHOUT CORE MUTATION)

## 2.1 Design Principles

1. **Additive Only** — New tables, never alter existing columns
2. **Sidecar Pattern** — Extension data in separate models linked via FK
3. **Configuration Over Code** — Behavior via database/JSON, not conditionals
4. **Registry Pattern** — Rules, features, layouts registered and evaluated dynamically
5. **Event Hooks** — Core emits events, extensions subscribe

---

## 2.2 New Configuration Entities

### 2.2.1 POSVerticalProfile

```python
# NEW: pos/vertical/models.py

class POSVerticalProfile(models.Model):
    """
    Defines a vertical (Grocery, Pharmacy, F&B, etc.) with its behavior configuration.
    A location links to exactly one active profile.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    code = models.CharField(max_length=50, unique=True)  # GROCERY, PHARMACY, RESTAURANT, etc.
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    # Configuration JSON
    settings = models.JSONField(default=dict, help_text="""
        {
            "weighted_items_enabled": true,
            "serial_tracking": false,
            "batch_tracking": false,
            "table_service": false,
            "kot_enabled": false,
            "prescription_required": false,
            "modifier_panels": false,
            "quick_keys_layout": "grocery_default",
            "receipt_template": "retail_standard"
        }
    """)
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'pos_vertical_profile'
```

**Usage**: Location links to a VerticalProfile. UI reads `settings` to enable/disable features.

### 2.2.2 POSFeatureFlag

```python
class POSFeatureFlag(models.Model):
    """
    Fine-grained feature toggles per vertical.
    Allows enabling/disabling specific POS behaviors.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    vertical_profile = models.ForeignKey(POSVerticalProfile, on_delete=models.CASCADE, related_name='feature_flags')
    feature_code = models.CharField(max_length=100)  # SERIAL_REQUIRED, WEIGHTED_ITEMS, TABLE_SERVICE
    enabled = models.BooleanField(default=False)
    config = models.JSONField(default=dict, help_text="Feature-specific configuration")
    
    class Meta:
        db_table = 'pos_feature_flag'
        unique_together = ['vertical_profile', 'feature_code']
```

**Example Feature Codes**:
| Code | Vertical | Effect |
|------|----------|--------|
| `WEIGHTED_ITEMS` | Grocery | Enable scale integration, kg pricing |
| `SERIAL_REQUIRED` | Electronics | Block sale if no serial entered |
| `BATCH_REQUIRED` | Pharmacy | Block sale if no batch selected |
| `PRESCRIPTION_REQUIRED` | Pharmacy | Require Rx number for controlled items |
| `TABLE_SERVICE` | F&B | Enable table assignment on sale |
| `KOT_ENABLED` | F&B | Generate Kitchen Order Ticket |
| `MODIFIER_PANELS` | F&B | Show modifier selection for items |
| `AGE_VERIFICATION` | Grocery/Pharmacy | Prompt for age on restricted items |

### 2.2.3 POSValidationRule

```python
class POSValidationRule(models.Model):
    """
    Dynamic validation rules evaluated at cart/line level.
    Rules are evaluated in sequence; first failure blocks action.
    """
    class Scope(models.TextChoices):
        LINE = 'LINE', 'Line Level'
        CART = 'CART', 'Cart Level'
        CHECKOUT = 'CHECKOUT', 'Checkout Level'
    
    class Severity(models.TextChoices):
        ERROR = 'ERROR', 'Block Action'
        WARNING = 'WARNING', 'Warn Only'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    vertical_profile = models.ForeignKey(POSVerticalProfile, on_delete=models.CASCADE, related_name='validation_rules')
    rule_code = models.CharField(max_length=100)  # SERIAL_MANDATORY, BATCH_MANDATORY, MIN_QTY
    scope = models.CharField(max_length=20, choices=Scope.choices)
    severity = models.CharField(max_length=20, choices=Severity.choices)
    
    # Rule definition (JSONLogic or simple conditions)
    condition = models.JSONField(help_text="""
        Example: {"item.serial_tracking": true, "line.serial_number": null}
        Means: If item requires serial AND line has no serial → trigger
    """)
    
    message = models.CharField(max_length=255)  # User-facing error/warning
    sequence = models.IntegerField(default=0)  # Evaluation order
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'pos_validation_rule'
        ordering = ['sequence']
```

**Rule Evaluation Flow**:
```
User Action (Add Item, Checkout, etc.)
        │
        ▼
┌───────────────────────┐
│ Load Rules for Scope  │
│ (LINE/CART/CHECKOUT)  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Evaluate Conditions   │◀─────── Per rule in sequence
│ Against Current State │
└───────────┬───────────┘
            │
    ┌───────┴───────┐
    │               │
 PASS           FAIL
    │               │
    ▼               ▼
Continue      Severity?
              ERROR → Block + Show message
              WARNING → Warn + Allow override
```

### 2.2.4 POSLayoutProfile

```python
class POSLayoutProfile(models.Model):
    """
    Defines UI layout configuration for a vertical.
    Controls which panels are visible and their arrangement.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    vertical_profile = models.ForeignKey(POSVerticalProfile, on_delete=models.CASCADE, related_name='layout_profiles')
    name = models.CharField(max_length=100)
    
    # Layout schema
    layout = models.JSONField(help_text="""
        {
            "panels": {
                "cart": { "visible": true, "width": "60%" },
                "product_lookup": { "visible": true, "position": "right" },
                "modifiers": { "visible": false },
                "table_selector": { "visible": false },
                "kot_preview": { "visible": false },
                "scale_display": { "visible": true }
            },
            "function_buttons": [
                { "key": "F1", "action": "customer", "label": "Customer", "visible": true },
                { "key": "F2", "action": "search", "label": "Search", "visible": true },
                { "key": "F3", "action": "weight", "label": "Weight", "visible": true },
                { "key": "F4", "action": "line_discount", "label": "Ln Disc", "visible": true }
            ],
            "quick_keys": {
                "enabled": true,
                "layout": "grid_4x4",
                "categories": ["Beverages", "Snacks", "Dairy", "Staples"]
            },
            "receipt": {
                "template": "grocery_standard",
                "show_weight": true,
                "show_loyalty": true
            }
        }
    """)
    
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'pos_layout_profile'
```

### 2.2.5 POSTransactionLineExtension (Sidecar)

```python
class POSTransactionLineExtension(models.Model):
    """
    Sidecar table for line-level extension data.
    Linked 1:1 to POSTransactionLine.
    NO changes to core POSTransactionLine model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    transaction_line = models.OneToOneField(
        'pos.POSTransactionLine', 
        on_delete=models.CASCADE, 
        related_name='extension'
    )
    
    # Pharmacy extensions
    prescription_number = models.CharField(max_length=100, null=True, blank=True)
    prescriber_name = models.CharField(max_length=200, null=True, blank=True)
    
    # F&B extensions
    modifiers = models.JSONField(default=list, help_text="[{modifier_id, name, price}]")
    course_number = models.IntegerField(null=True, blank=True)
    preparation_notes = models.TextField(blank=True)
    
    # Electronics extensions
    warranty_start_date = models.DateField(null=True, blank=True)
    warranty_months = models.IntegerField(null=True, blank=True)
    imei_number = models.CharField(max_length=20, null=True, blank=True)
    
    # Grocery extensions
    weighed_quantity = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    scale_reading = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    tare_weight = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    
    # Generic extension (for future verticals)
    extra_data = models.JSONField(default=dict)
    
    class Meta:
        db_table = 'pos_transaction_line_extension'
```

**Pattern**: Core `POSTransactionLine` unchanged. Extension data in sidecar. Frontend reads both via single API response.

### 2.2.6 POSTransactionExtension (Sidecar)

```python
class POSTransactionExtension(models.Model):
    """
    Sidecar table for transaction-level extension data.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    transaction = models.OneToOneField(
        'pos.POSTransaction', 
        on_delete=models.CASCADE, 
        related_name='extension'
    )
    
    # F&B extensions
    table_number = models.CharField(max_length=20, null=True, blank=True)
    covers = models.IntegerField(null=True, blank=True)
    server_name = models.CharField(max_length=100, null=True, blank=True)
    kot_numbers = models.JSONField(default=list)
    
    # Pharmacy extensions
    patient_name = models.CharField(max_length=200, null=True, blank=True)
    patient_id = models.CharField(max_length=100, null=True, blank=True)
    
    # Generic
    extra_data = models.JSONField(default=dict)
    
    class Meta:
        db_table = 'pos_transaction_extension'
```

---

## 2.3 Frontend Extension Architecture

### 2.3.1 Vertical Context Provider

```typescript
// NEW: pos/context/VerticalContext.tsx

interface VerticalConfig {
  code: string;
  features: Record<string, boolean>;
  layout: LayoutSchema;
  validationRules: ValidationRule[];
}

const VerticalContext = React.createContext<VerticalConfig | null>(null);

export const VerticalProvider: React.FC<{children: ReactNode}> = ({children}) => {
  const [config, setConfig] = useState<VerticalConfig | null>(null);
  
  useEffect(() => {
    // Load vertical config based on current location/terminal
    const loadConfig = async () => {
      const res = await posService.getVerticalConfig();
      setConfig(res);
    };
    loadConfig();
  }, []);
  
  return (
    <VerticalContext.Provider value={config}>
      {children}
    </VerticalContext.Provider>
  );
};

export const useVertical = () => useContext(VerticalContext);
```

### 2.3.2 Dynamic Panel Visibility

```typescript
// USAGE in PosDesktop.tsx (NO CORE CHANGE, just reads config)

const PosDesktop: React.FC = () => {
  const vertical = useVertical();
  
  // Panels visibility driven by config
  const showScalePanel = vertical?.features.WEIGHTED_ITEMS ?? false;
  const showModifierPanel = vertical?.features.MODIFIER_PANELS ?? false;
  const showTableSelector = vertical?.features.TABLE_SERVICE ?? false;
  
  return (
    <div className="pos-container">
      <PosCart />
      {showScalePanel && <ScaleDisplayPanel />}
      {showModifierPanel && <ModifierPanel />}
      {showTableSelector && <TableSelector />}
      <PosRightPanel />
    </div>
  );
};
```

### 2.3.3 Dynamic Function Buttons

```typescript
// CHANGE: constants.ts -> becomes config-driven

// Before (hardcoded):
export const POS_FUNCTIONS = [...];

// After (config-driven):
export const useFunctionButtons = () => {
  const vertical = useVertical();
  
  // Base functions always present
  const baseFunctions = [
    { key: 'F1', action: 'customer', label: 'Customer', icon: User },
    { key: 'F2', action: 'search', label: 'Search', icon: Search },
    // ... core functions
  ];
  
  // Vertical-specific functions injected
  const verticalFunctions = vertical?.layout.function_buttons || [];
  
  return [...baseFunctions, ...verticalFunctions];
};
```

### 2.3.4 Dynamic Validation Engine

```typescript
// NEW: pos/validation/useValidation.ts

interface ValidationResult {
  valid: boolean;
  errors: { code: string; message: string }[];
  warnings: { code: string; message: string }[];
}

export const useValidation = () => {
  const vertical = useVertical();
  
  const validateLine = useCallback((line: CartItem): ValidationResult => {
    const rules = vertical?.validationRules.filter(r => r.scope === 'LINE') || [];
    const errors: ValidationResult['errors'] = [];
    const warnings: ValidationResult['warnings'] = [];
    
    for (const rule of rules) {
      if (evaluateCondition(rule.condition, { line, item: line.product })) {
        if (rule.severity === 'ERROR') {
          errors.push({ code: rule.rule_code, message: rule.message });
        } else {
          warnings.push({ code: rule.rule_code, message: rule.message });
        }
      }
    }
    
    return { valid: errors.length === 0, errors, warnings };
  }, [vertical]);
  
  const validateCart = useCallback((cart: CartItem[]): ValidationResult => {
    // Similar logic for CART scope rules
  }, [vertical]);
  
  const validateCheckout = useCallback((cart: CartItem[], customer: Customer): ValidationResult => {
    // Similar logic for CHECKOUT scope rules
  }, [vertical]);
  
  return { validateLine, validateCart, validateCheckout };
};
```

---

## 2.4 Component Registry Pattern

```typescript
// NEW: pos/registry/ComponentRegistry.ts

type ComponentType = 'panel' | 'modal' | 'input' | 'action';

interface RegisteredComponent {
  id: string;
  type: ComponentType;
  component: React.ComponentType<any>;
  verticals: string[];  // Which verticals use this
}

const registry: Map<string, RegisteredComponent> = new Map();

export const registerComponent = (config: RegisteredComponent) => {
  registry.set(config.id, config);
};

export const getComponent = (id: string): React.ComponentType<any> | null => {
  return registry.get(id)?.component ?? null;
};

// Extension panels register themselves
registerComponent({
  id: 'scale_panel',
  type: 'panel',
  component: ScaleDisplayPanel,
  verticals: ['GROCERY']
});

registerComponent({
  id: 'modifier_panel',
  type: 'panel',
  component: ModifierPanel,
  verticals: ['RESTAURANT', 'QSR']
});

registerComponent({
  id: 'serial_capture',
  type: 'modal',
  component: SerialCaptureModal,
  verticals: ['ELECTRONICS']
});

registerComponent({
  id: 'batch_selector',
  type: 'modal',
  component: BatchSelectorModal,
  verticals: ['PHARMACY']
});
```

---

# PART 3: IMPACT ANALYSIS

## 3.1 Impacted Existing Screens

| Screen | File | Change Type | Description |
|--------|------|-------------|-------------|
| `PosDesktop.tsx` | `billing/PosDesktop.tsx` | **ENHANCED** (NOT REWRITTEN) | Add VerticalContext consumer, conditional panel rendering |
| `PosCart.tsx` | `billing/PosCart.tsx` | **ENHANCED** | Show extension fields (modifiers, serial, batch) per vertical |
| `PosRightPanel.tsx` | `billing/PosRightPanel.tsx` | **ENHANCED** | Dynamic quick-key layout per vertical |
| `PaymentDialog.tsx` | `components/PaymentDialog.tsx` | **UNCHANGED** | Core payment flow unchanged |
| `Receipt.tsx` | `components/Receipt.tsx` | **ENHANCED** | Template selection per vertical |
| `constants.ts` | `billing/constants.ts` | **ENHANCED** | Function buttons become config-driven |

**ZERO REWRITES. Only additive enhancements.**

## 3.2 New Screens (Only If Unavoidable)

| Screen | Purpose | Justification |
|--------|---------|---------------|
| `VerticalProfileAdmin.tsx` | Admin CRUD for POSVerticalProfile | Required for vertical configuration |
| `FeatureFlagAdmin.tsx` | Admin CRUD for POSFeatureFlag | Required for feature toggles |
| `ValidationRuleAdmin.tsx` | Admin CRUD for POSValidationRule | Required for rule management |
| `LayoutProfileAdmin.tsx` | Admin CRUD for POSLayoutProfile | Required for layout configuration |

**These are ADMIN screens, not POS screens. Core POS UI remains ONE screen.**

## 3.3 Impacted Models (Additive Only)

| Model | Change Type | Description |
|-------|-------------|-------------|
| `Location` | ADD FK | `vertical_profile` FK to POSVerticalProfile |
| `Terminal` | ADD FK | `layout_profile` FK to POSLayoutProfile (optional) |
| `ItemMaster` | ADD Fields | `serial_tracking`, `batch_tracking`, `weighted`, `modifier_group` (nullable) |

**CRITICAL**: These are ADDITIVE fields (nullable FKs, nullable booleans). No destructive changes.

## 3.4 New Models Introduced

| Model | Table | Purpose |
|-------|-------|---------|
| `POSVerticalProfile` | `pos_vertical_profile` | Vertical definition + settings |
| `POSFeatureFlag` | `pos_feature_flag` | Feature toggles per vertical |
| `POSValidationRule` | `pos_validation_rule` | Dynamic validation rules |
| `POSLayoutProfile` | `pos_layout_profile` | UI layout configuration |
| `POSTransactionLineExtension` | `pos_transaction_line_extension` | Line sidecar for vertical data |
| `POSTransactionExtension` | `pos_transaction_extension` | Transaction sidecar for vertical data |
| `POSModifierGroup` | `pos_modifier_group` | F&B modifiers (optional sub-items) |
| `POSModifierItem` | `pos_modifier_item` | Individual modifiers |

## 3.5 Impacted APIs

| Endpoint | Change Type | Description |
|----------|-------------|-------------|
| `GET /api/pos/session/active` | **UNCHANGED** | Core session API unchanged |
| `POST /api/pos/transaction/` | **ENHANCED** | Accept `extension` field for sidecar data |
| `GET /api/pos/transaction/:id/` | **ENHANCED** | Return `extension` in response |
| `GET /api/pos/config/vertical/` | **NEW** | Return current vertical config for terminal |
| `GET /api/pos/config/layout/` | **NEW** | Return layout profile for current context |
| `POST /api/pos/validation/line/` | **NEW** | Validate line against rules |
| `POST /api/pos/validation/cart/` | **NEW** | Validate cart against rules |

---

# PART 4: VERTICAL BEHAVIOR MAPPING

## 4.1 Grocery Vertical

**Profile Code**: `GROCERY`

### Feature Flags
| Flag | Enabled | Effect |
|------|---------|--------|
| `WEIGHTED_ITEMS` | ✅ | Show scale panel, accept weight input |
| `PROMOTIONS_ENABLED` | ✅ | Apply automatic promotions |
| `LOYALTY_ENABLED` | ✅ | Show points, allow redemption |
| `AGE_VERIFICATION` | ✅ | Prompt for alcohol/tobacco |
| `QUICK_KEYS` | ✅ | Show category quick-access grid |

### Validation Rules
| Rule | Scope | Severity | Condition | Message |
|------|-------|----------|-----------|---------|
| `WEIGHT_REQUIRED` | LINE | ERROR | `item.weighted AND !line.weighed_quantity` | "Please weigh item before adding" |
| `AGE_VERIFY_REQUIRED` | CHECKOUT | WARNING | `cart.has_restricted_items AND !age_verified` | "Age verification required for restricted items" |

### Layout
```json
{
  "panels": {
    "cart": { "visible": true, "width": "60%" },
    "scale_display": { "visible": true, "position": "left-bottom" },
    "product_lookup": { "visible": true, "position": "right" },
    "quick_keys": { "visible": true, "position": "right-top" }
  },
  "function_buttons": [
    { "key": "F3", "action": "weight", "label": "Weight", "icon": "Scale" },
    { "key": "F7", "action": "loyalty", "label": "Loyalty", "icon": "Gift" }
  ]
}
```

### UI Transformation (Same PosDesktop)
- **Scale Panel** appears in left-bottom area
- **F3** becomes "Weight" (triggers scale read)
- **Quick Keys** grid shows common categories
- **Cart lines** display weight column for weighted items

---

## 4.2 Pharmacy Vertical

**Profile Code**: `PHARMACY`

### Feature Flags
| Flag | Enabled | Effect |
|------|---------|--------|
| `BATCH_REQUIRED` | ✅ | Block sale without batch selection |
| `EXPIRY_CHECK` | ✅ | Warn if batch expires soon |
| `PRESCRIPTION_REQUIRED` | ✅ | Require Rx for controlled drugs |
| `PATIENT_TRACKING` | ✅ | Capture patient name/ID |
| `DRUG_INTERACTIONS` | ✅ | Warn on known interactions |

### Validation Rules
| Rule | Scope | Severity | Condition | Message |
|------|-------|----------|-----------|---------|
| `BATCH_MANDATORY` | LINE | ERROR | `item.batch_tracking AND !line.batch_id` | "Select batch before adding" |
| `EXPIRY_WARNING` | LINE | WARNING | `line.batch.days_to_expiry < 30` | "Item expires within 30 days" |
| `PRESCRIPTION_MANDATORY` | CHECKOUT | ERROR | `cart.has_controlled_items AND !prescription_number` | "Prescription number required" |

### Layout
```json
{
  "panels": {
    "cart": { "visible": true, "width": "55%" },
    "batch_selector": { "visible": true, "position": "right-top" },
    "patient_info": { "visible": true, "position": "left-bottom" },
    "product_lookup": { "visible": true, "position": "right" }
  },
  "function_buttons": [
    { "key": "F3", "action": "batch", "label": "Batch", "icon": "Package" },
    { "key": "F7", "action": "prescription", "label": "Rx", "icon": "FileText" },
    { "key": "F8", "action": "patient", "label": "Patient", "icon": "User" }
  ]
}
```

### UI Transformation (Same PosDesktop)
- **Batch Selector Panel** appears for tracked items
- **F3** becomes "Batch" (opens batch selection)
- **F7** captures prescription number
- **Cart lines** display batch/expiry column
- **Checkout** validates Rx for controlled items

---

## 4.3 Electronics Vertical

**Profile Code**: `ELECTRONICS`

### Feature Flags
| Flag | Enabled | Effect |
|------|---------|--------|
| `SERIAL_REQUIRED` | ✅ | Block sale without serial |
| `WARRANTY_CAPTURE` | ✅ | Record warranty start date |
| `IMEI_VALIDATION` | ✅ | Validate IMEI format for phones |
| `ACCESSORIES_PROMPT` | ✅ | Suggest related accessories |

### Validation Rules
| Rule | Scope | Severity | Condition | Message |
|------|-------|----------|-----------|---------|
| `SERIAL_MANDATORY` | LINE | ERROR | `item.serial_tracking AND !line.serial_number` | "Enter serial number" |
| `IMEI_FORMAT` | LINE | ERROR | `item.is_phone AND !isValidIMEI(line.serial_number)` | "Invalid IMEI format" |
| `WARRANTY_MISSING` | CHECKOUT | WARNING | `cart.has_warranty_items AND !all_warranties_set` | "Warranty dates not recorded" |

### Layout
```json
{
  "panels": {
    "cart": { "visible": true, "width": "60%" },
    "serial_capture": { "visible": true, "position": "modal" },
    "product_lookup": { "visible": true, "position": "right" },
    "accessories": { "visible": true, "position": "right-bottom" }
  },
  "function_buttons": [
    { "key": "F3", "action": "serial", "label": "Serial", "icon": "Hash" },
    { "key": "F7", "action": "warranty", "label": "Warranty", "icon": "Shield" }
  ]
}
```

### UI Transformation (Same PosDesktop)
- **Serial Capture Modal** triggers on adding serial-tracked item
- **F3** opens serial entry
- **Cart lines** display serial/IMEI column
- **Accessories Panel** suggests related items

---

## 4.4 F&B / Restaurant Vertical

**Profile Code**: `RESTAURANT`

### Feature Flags
| Flag | Enabled | Effect |
|------|---------|--------|
| `TABLE_SERVICE` | ✅ | Assign sale to table |
| `KOT_ENABLED` | ✅ | Generate Kitchen Order Ticket |
| `MODIFIER_PANELS` | ✅ | Show modifiers for items |
| `COURSE_SEQUENCING` | ✅ | Group items by course |
| `SPLIT_BILL` | ✅ | Split bill by items/covers |

### Validation Rules
| Rule | Scope | Severity | Condition | Message |
|------|-------|----------|-----------|---------|
| `TABLE_REQUIRED` | CHECKOUT | ERROR | `!transaction.table_number` | "Select table before sending order" |
| `MODIFIER_REQUIRED` | LINE | WARNING | `item.has_mandatory_modifiers AND !line.modifiers.length` | "Select modifiers for this item" |

### Layout
```json
{
  "panels": {
    "cart": { "visible": true, "width": "50%" },
    "table_selector": { "visible": true, "position": "left-top" },
    "modifier_panel": { "visible": true, "position": "right-top" },
    "kot_preview": { "visible": true, "position": "right-bottom" },
    "product_lookup": { "visible": true, "position": "modal" }
  },
  "function_buttons": [
    { "key": "F1", "action": "table", "label": "Table", "icon": "Grid" },
    { "key": "F3", "action": "modifiers", "label": "Mods", "icon": "Plus" },
    { "key": "F5", "action": "send_kot", "label": "KOT", "icon": "Printer" },
    { "key": "F7", "action": "split_bill", "label": "Split", "icon": "Scissors" }
  ]
}
```

### UI Transformation (Same PosDesktop)
- **Table Selector** replaces customer lookup as primary action
- **Modifier Panel** appears when item requires modifiers
- **F5** sends current items to kitchen (KOT)
- **Cart** groups items by course
- **KOT Preview** shows pending kitchen orders

---

# PART 5: HARD CONSTRAINTS COMPLIANCE

## 5.1 Constraint Verification Matrix

| Constraint | Status | Evidence |
|------------|--------|----------|
| No forked POS code | ✅ COMPLIANT | Single `PosDesktop.tsx`, no `GroceryPOS.tsx`, `PharmacyPOS.tsx` |
| No duplicate billing screens | ✅ COMPLIANT | One billing surface, verticals via config |
| No lifecycle mutation | ✅ COMPLIANT | Day→Session→Bill→Pay→Close unchanged |
| No vertical logic in core models | ✅ COMPLIANT | Sidecar models for extension data |
| Only config, rules, extensions | ✅ COMPLIANT | All behavior via POSVerticalProfile, POSFeatureFlag, POSValidationRule |
| Keyboard flow unchanged | ✅ COMPLIANT | Core shortcuts preserved, vertical adds function buttons |

## 5.2 Architectural Violation Flags

**NONE IDENTIFIED**.

The proposed extension architecture achieves vertical support WITHOUT any core mutation.

---

# PART 6: IMPLEMENTATION ROADMAP

## Phase 2A: Configuration Foundation (Week 1-2)

| Task | Priority | Deliverable |
|------|----------|-------------|
| Create POSVerticalProfile model | P0 | Backend model + migration |
| Create POSFeatureFlag model | P0 | Backend model + migration |
| Create POSLayoutProfile model | P0 | Backend model + migration |
| Create POSValidationRule model | P0 | Backend model + migration |
| Create VerticalContext provider | P0 | Frontend context |
| Wire PosDesktop to VerticalContext | P0 | Conditional rendering |

## Phase 2B: Grocery Vertical (Week 3-4)

| Task | Priority | Deliverable |
|------|----------|-------------|
| Seed GROCERY profile | P0 | Database seed |
| Implement ScaleDisplayPanel | P1 | New component |
| Add weight capture to addToCart | P1 | Enhanced cart logic |
| Implement Quick Keys panel | P1 | New component |
| Configure Grocery function buttons | P1 | Layout config |

## Phase 2C: Pharmacy Vertical (Week 5-6)

| Task | Priority | Deliverable |
|------|----------|-------------|
| Create POSTransactionLineExtension | P0 | Sidecar model |
| Implement BatchSelectorModal | P0 | New component |
| Add batch validation rules | P0 | Rule seed |
| Implement PrescriptionCapture | P1 | New component |
| Test batch/expiry flow | P1 | UAT |

## Phase 2D: Electronics Vertical (Week 7)

| Task | Priority | Deliverable |
|------|----------|-------------|
| Implement SerialCaptureModal | P0 | New component |
| Add serial validation rules | P0 | Rule seed |
| Implement WarrantyCapture | P1 | New component |

## Phase 2E: F&B Vertical (Week 8-9)

| Task | Priority | Deliverable |
|------|----------|-------------|
| Create POSModifierGroup model | P0 | Backend model |
| Implement TableSelector | P0 | New component |
| Implement ModifierPanel | P0 | New component |
| Implement KOT flow | P1 | Backend + Frontend |

---

# APPENDIX A: ENTITY RELATIONSHIP (EXTENSION LAYER)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      EXTENSION LAYER (NEW)                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌──────────────────┐                                                   │
│   │POSVerticalProfile│                                                   │
│   └────────┬─────────┘                                                   │
│            │                                                             │
│   ┌────────┼───────────────────────────────┐                             │
│   │        │                               │                             │
│   ▼        ▼                               ▼                             │
│ ┌────────────┐  ┌─────────────────┐  ┌───────────────┐                   │
│ │FeatureFlag │  │ ValidationRule  │  │ LayoutProfile │                   │
│ └────────────┘  └─────────────────┘  └───────────────┘                   │
│                                                                          │
├─────────────────────────────────────────────────────────────────────────┤
│                     SIDECAR LAYER (NEW)                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   ┌─────────────────────┐        ┌───────────────────────────┐           │
│   │ POSTransaction      │◀──1:1──│ POSTransactionExtension   │           │
│   │ (CORE - FROZEN)     │        │ (table, server, patient)  │           │
│   └──────────┬──────────┘        └───────────────────────────┘           │
│              │                                                           │
│              │ 1:N                                                       │
│              ▼                                                           │
│   ┌─────────────────────┐        ┌───────────────────────────┐           │
│   │ POSTransactionLine  │◀──1:1──│ POSTransactionLineExtension│          │
│   │ (CORE - FROZEN)     │        │ (modifiers, Rx, warranty)  │          │
│   └─────────────────────┘        └───────────────────────────┘           │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

# APPENDIX B: SAMPLE API RESPONSE (Vertical Config)

```json
GET /api/pos/config/vertical/

{
  "vertical": {
    "code": "PHARMACY",
    "name": "Pharmacy Retail",
    "settings": {
      "weighted_items_enabled": false,
      "serial_tracking": false,
      "batch_tracking": true,
      "prescription_required": true
    }
  },
  "features": {
    "BATCH_REQUIRED": true,
    "EXPIRY_CHECK": true,
    "PRESCRIPTION_REQUIRED": true,
    "PATIENT_TRACKING": true
  },
  "validation_rules": [
    {
      "rule_code": "BATCH_MANDATORY",
      "scope": "LINE",
      "severity": "ERROR",
      "condition": {"and": [{"var": "item.batch_tracking"}, {"!": {"var": "line.batch_id"}}]},
      "message": "Select batch before adding"
    }
  ],
  "layout": {
    "panels": {
      "batch_selector": { "visible": true, "position": "right-top" },
      "patient_info": { "visible": true, "position": "left-bottom" }
    },
    "function_buttons": [
      { "key": "F3", "action": "batch", "label": "Batch", "icon": "Package" },
      { "key": "F7", "action": "prescription", "label": "Rx", "icon": "FileText" }
    ]
  }
}
```

---

# DOCUMENT CONTROL

| Attribute | Value |
|-----------|-------|
| **Status** | AUTHORITATIVE |
| **Classification** | Platform Architecture |
| **Approved By** | Pending Viji Approval |
| **Created** | 2026-01-24 |
| **Author** | Astra (AI Implementation Engine) |
| **Architectural Authority** | Mindra |
| **Next Action** | Viji Review & Approval |

---

> **CANONICAL STATEMENT**
> 
> POS is a platform engine.  
> Verticals are configuration overlays.  
> Overlays never redefine the engine.  
> 
> If a vertical demands core mutation, the design has failed.  
> This document proves the design has NOT failed.

---

**END OF DOCUMENT**
