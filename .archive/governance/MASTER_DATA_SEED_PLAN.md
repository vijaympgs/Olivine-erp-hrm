# Master Data Seed Implementation Plan

**Date**: 2025-12-21  
**Objective**: Create comprehensive seed data for all master entities

---

## 📋 **MASTERS INVENTORY**

### ✅ **Already Have Seed Data:**
1. Company
2. Locations
3. Attributes
4. Attribute Values
5. UOMs
6. Product Attribute Templates
7. Items (with Variants)
8. Customers
9. Suppliers
10. Terminals
11. Price Lists

### 🔨 **TO BE CREATED:**

#### **Priority 1 - Essential Masters:**
12. **Categories** (Product Hierarchy with parent-child)
13. **Brands** (10-15 brands)
14. **Tax Classes** (GST rates for India)

#### **Priority 2 - Business Logic:**
15. **Payment Methods** (Cash, Card, UPI, etc.)
16. **Customer Groups** (Retail, Wholesale, VIP, Corporate)
17. **Loyalty Programs** (Points-based)
18. **Discount Rules** (Promotional discounts)

#### **Priority 3 - Operational:**
19. **Shipping Methods** (Standard, Express, Same-day)
20. **Warehouse Bins** (if separate from Locations)

---

## 🎯 **IMPLEMENTATION APPROACH:**

### **Step 1: Create Seed Script**
- File: `backend/domain/company/management/commands/seed_masters.py`
- Pattern: Reuse existing `seed_data.py` structure
- Use `get_or_create` to avoid duplicates

### **Step 2: Data Structure**

#### **Categories (Hierarchical):**
```
Apparel
├── Men's Wear
│   ├── Shirts
│   ├── T-Shirts
│   ├── Jeans
│   └── Accessories
├── Women's Wear
│   ├── Tops
│   ├── Dresses
│   ├── Bottoms
│   └── Accessories
└── Kids Wear
    ├── Boys
    └── Girls

Electronics
├── Mobile & Tablets
│   ├── Smartphones
│   └── Tablets
├── Computers
│   ├── Laptops
│   └── Desktops
└── Accessories

Home & Living
├── Furniture
│   ├── Chairs
│   ├── Tables
│   └── Beds
└── Decor
```

#### **Brands:**
- Nike, Adidas, Puma, Reebok, Levi's (Apparel)
- Samsung, Apple, Sony, LG, OnePlus (Electronics)
- IKEA, Godrej, Nilkamal, Urban Ladder (Furniture)
- Generic/House Brand

#### **Tax Classes (India GST):**
- GST 0% (Exempt) - Books, Fresh Food
- GST 5% (Essential) - Sugar, Tea, Coffee
- GST 12% (Standard) - Computers, Processed Food
- GST 18% (Most Goods) - Soaps, Toothpaste, Apparel
- GST 28% (Luxury) - Cars, Tobacco, Aerated Drinks

#### **Payment Methods:**
- Cash
- Credit Card
- Debit Card
- UPI (PhonePe, Google Pay, Paytm)
- Net Banking
- Wallet
- Gift Card/Voucher

#### **Customer Groups:**
- Retail Customers (Default)
- Wholesale Customers (Bulk buyers)
- VIP Customers (Premium members)
- Corporate Clients (B2B)
- Staff/Employee

---

## 📁 **FILES TO CREATE/MODIFY:**

### **New Files:**
1. `backend/domain/company/management/commands/seed_masters.py`
2. `docs/MASTER_DATA_SEED_GUIDE.md`

### **Modified Files:**
1. Update existing models if needed (add missing fields)
2. Update admin.py registrations

---

## ✅ **SUCCESS CRITERIA:**

- [ ] All 20 masters have seed data
- [ ] Data is realistic and usable
- [ ] No duplicate entries
- [ ] Proper parent-child relationships (Categories)
- [ ] All foreign keys properly linked
- [ ] Command runs without errors
- [ ] Data visible in admin panel
- [ ] Product Lookup shows seeded items

---

## 🚀 **EXECUTION PLAN:**

1. Create `seed_masters.py` command
2. Add Categories (hierarchical)
3. Add Brands
4. Add Tax Classes
5. Add Payment Methods
6. Add Customer Groups
7. Add Loyalty Programs (if model exists)
8. Add Discount Rules (if model exists)
9. Add Shipping Methods (if model exists)
10. Test and verify

---

**Status**: Ready to implement  
**Next**: Create seed_masters.py command
