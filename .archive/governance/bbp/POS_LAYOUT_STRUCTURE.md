# POS Desktop Layout Structure

**Created:** 07-Nov-2025  
**Last Updated:** 07-Nov-2025  
**Purpose:** Reference document for POS layout sections and panels

---

## 📐 Layout Structure

### **SECTION 1: TOP BAR / HEADER SECTION**
**ID:** `top-bar-section`  
**Location:** Top of screen  
**Purpose:** Session info, time, quick actions  
**Current Status:** Empty placeholder

---

### **SECTION 2: MAIN CONTENT AREA**
**Split Layout:** 70% Left | 30% Right

#### **PANEL A: LEFT PANEL (Product Area)**
**ID:** `left-panel-product-area`  
**Width:** 70%  
**Border:** Blue dashed (for visibility)  
**Purpose:** Unified area for product search, filters, and product grid/list  
**Content:** Search input, filters, quick actions, product grid/list, categories  
**Current Status:** Empty placeholder

---

#### **PANEL B: RIGHT PANEL (Transaction Area)**
**ID:** `right-panel-transaction-area`  
**Width:** 30%  
**Border:** Green dashed (for visibility)

##### **Sub-section B1: Cart/Items Header**
**ID:** `cart-items-header`  
**Location:** Top of right panel  
**Purpose:** Cart title, item count, clear button  
**Content:** Cart title, item count, clear button  
**Current Status:** Empty placeholder

##### **Sub-section B2: Cart Items List**
**ID:** `cart-items-list`  
**Location:** Below header, scrollable area  
**Purpose:** Item rows, quantity controls, line totals  
**Content:** Item rows, quantity controls, line totals  
**Current Status:** Empty placeholder

##### **Sub-section B3: Customer & Discount Section**
**ID:** `customer-discount-section`  
**Location:** Below cart items list  
**Purpose:** Customer selector, discount input  
**Content:** Customer selector, discount input  
**Current Status:** Empty placeholder

##### **Sub-section B4: Totals Section**
**ID:** `totals-section`  
**Location:** Below customer/discount section  
**Purpose:** Subtotal, Tax, Discount, Total amount  
**Content:** Subtotal, Tax, Discount, Total amount  
**Current Status:** Empty placeholder

##### **Sub-section B5: Payment Buttons Section**
**ID:** `payment-buttons-section`  
**Location:** Bottom of right panel  
**Purpose:** Cash, Card, UPI, etc. payment buttons  
**Content:** Cash, Card, UPI, etc. payment buttons  
**Current Status:** Empty placeholder

---

### **SECTION 3: BOTTOM BAR / FOOTER SECTION**
**ID:** `bottom-bar-section`  
**Location:** Bottom of screen  
**Purpose:** Quick actions, keyboard shortcuts, status  
**Current Status:** Empty placeholder

---

## 🎨 Visual Indicators

- **Blue dashed border:** Left Panel (Product Area)
- **Green dashed border:** Right Panel (Transaction Area)
- **Placeholder text:** Shows section name and purpose
- **ID attributes:** Each section has a unique ID for easy targeting

---

## 📝 Usage

You can now guide me by referring to these section IDs:

**Example:**
- "In `product-search-bar`, add a search input field"
- "In `cart-items-list`, create a table with columns..."
- "Move `totals-section` above `payment-buttons-section`"

All sections are ready for your guidance!

