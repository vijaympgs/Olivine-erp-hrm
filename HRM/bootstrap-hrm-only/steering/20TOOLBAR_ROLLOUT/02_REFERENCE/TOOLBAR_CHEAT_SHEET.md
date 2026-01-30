# ⚡ TOOLBAR CONFIG CHEAT SHEET

**Quick Reference** - Copy the config string you need!

---

## 🎯 MOST COMMON CONFIGS

### Masters (Simple)
**Examples**: UOM, Brands, Categories, Tax Classes  
**Config**: `NESCKVDXRQF`

### Masters (Advanced)  
**Examples**: Item Master, Customers, Suppliers  
**Config**: `NESCKVDXRQFIO`

### Transactions (Full Workflow)
**Examples**: Purchase Orders, Sales Orders, Invoices  
**Config**: `NESCKZTJAVPMRDX1234QF`

### Reports
**Examples**: Stock Valuation, Sales Analysis  
**Config**: `VRXPYQFG`

### Configuration Screens
**Examples**: Company Settings, System Parameters  
**Config**: `ESCKXR`

---

## 🔤 CHARACTER CODES (Quick Lookup)

| Code | Action | Shortcut |
|------|--------|----------|
| N | New | F2 |
| E | Edit | F3 |
| S | Save | F8 |
| C | Cancel | Esc |
| K | Clear | F5 |
| V | View | F7 |
| D | Delete | F4 |
| X | Exit | Esc |
| R | Refresh | F9 |
| Q | Search | Ctrl+F |
| F | Filter | Alt+F |
| I | Import | Ctrl+I |
| O | Export | Ctrl+E |
| Z | Authorize | F10 |
| T | Submit | Alt+S |
| J | Reject | Alt+R |
| A | Amend | Alt+A |
| P | Print | Ctrl+P |
| M | Email | Ctrl+M |
| 1234 | Nav (First/Prev/Next/Last) | Home/PgUp/PgDn/End |

---

## 📋 DECISION FLOWCHART

```
What type of screen?
│
├─ Master Data (UOM, Item, Customer)
│  ├─ Simple (no import/export) → NESCKVDXRQF
│  └─ Advanced (with import/export) → NESCKVDXRQFIO
│
├─ Transaction (PO, SO, Invoice)
│  ├─ With approval workflow → NESCKZTJAVPMRDX1234QF
│  └─ No approval (Stock Adj) → NESCKVDXRQF
│
├─ Report/Dashboard → VRXPYQFG
│
└─ Configuration/Settings → ESCKXR
```

---

## ✅ EXAMPLES

| Screen | Type | Config |
|--------|------|--------|
| UOM Setup | Masters (Simple) | `NESCKVDXRQF` |
| Item Master | Masters (Advanced) | `NESCKVDXRQFIO` |
| Purchase Order | Transaction | `NESCKZTJAVPMRDX1234QF` |
| Stock Movement | Transaction (Simple) | `NESCKVDXRQF` |
| Stock Report | Report | `VRXPYQFG` |
| Company Settings | Configuration | `ESCKXR` |

---

**Full Guide**: See `TOOLBAR_CONFIGURATION_GUIDE.md`
