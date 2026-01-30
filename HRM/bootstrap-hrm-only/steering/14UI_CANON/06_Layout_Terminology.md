# CONSOLIDATED DESIGN SYSTEM
Generated consolidation of 5 files.



================================================================================
FILE START: UI_LAYOUT_TERMINOLOGY.md
================================================================================

--- 
title: "Documentation File" 
description: "Documentation file with automatic timestamp" 
date: "2025-11-14 10:28:50" 
modified: "2025-11-14 10:28:50" 
author: "Development Team" 
version: "1.0.0" 
category: "documentation" 
tags: [docs, timestamp] 
project: "Django POS System" 
path: "d:\Python\01practice\docs\LAYOUT_TERMINOLOGY\UI_LAYOUT_TERMINOLOGY.md" 
last_reviewed: "2025-11-14 10:28:50" 
review_status: "draft" 
--- 
 
--- 
title: "Documentation File" 
description: "Documentation file with automatic timestamp" 
date: "2025-11-14 10:12:37" 
modified: "2025-11-14 10:12:37" 
author: "Development Team" 
version: "1.0.0" 
category: "documentation" 
tags: [docs, timestamp] 
project: "Django POS System" 
path: "d:\Python\01practice\docs\LAYOUT_TERMINOLOGY\UI_LAYOUT_TERMINOLOGY.md" 
last_reviewed: "2025-11-14 10:12:37" 
review_status: "draft" 
--- 
 
# UI Layout Terminology Reference

## 🎯 **Purpose**

This document establishes standardized terminology for all application UI sections. Use this reference when communicating about UI modifications, improvements, or issues to ensure clear and precise communication.

---

## 🔐 **Login Screen Sections**

### **Login > Sign-in Message Area**
- **Location**: Top section of the login screen
- **Purpose**: Welcome messages, system notifications, alerts
- **Content**: Welcome text, system status, important announcements
- **Reference**: "Update the sign-in message area with a new welcome message"

### **Login > Credentials Capture Section**
- **Location**: Central form area of the login screen
- **Purpose**: User authentication input fields
- **Content**: Username/email field, password field, input validation
- **Reference**: "Add validation to the credentials capture section"

### **Login > Theme Selection Area**
- **Location**: Typically right side or bottom of login form
- **Purpose**: Theme customization and appearance settings
- **Content**: Theme switcher, color scheme options, display preferences
- **Reference**: "Enhance the theme selection area with more options"

### **Login > Sign-in Buttons**
- **Location**: Bottom of the login form
- **Purpose**: Authentication action triggers
- **Content**: Login button, forgot password link, sign-up option
- **Reference**: "Modify the sign-in buttons styling and behavior"

---

## 🖥️ **Main Application Layout (Post-Login)**

### **Section A: Sidebar Structure (Left)**
- **Location**: Left side of the main application screen
- **Purpose**: Primary navigation and menu system
- **Content**: Navigation menu items, user profile, quick actions, collapsible sections
- **Reference**: "Add new menu items to Section A: Sidebar Structure"
- **Components**: 
  - Main navigation menu
  - User profile section
  - Quick action buttons
  - Collapse/expand functionality

### **Section B: Application Header (Top)**
- **Location**: Top horizontal bar of the main application
- **Purpose**: Global navigation, user info, and system controls
- **Content**: Application title, user account menu, notifications, global search, logout
- **Reference**: "Update Section B: Application Header with new user menu"
- **Components**:
  - Application branding/logo
  - User account dropdown
  - Notification center
  - Global search bar
  - System settings access

### **Section C: Primary Workspace**
- **Location**: Central/main content area of the application
- **Purpose**: Main content rendering and form display area
- **Content**: Dynamic forms, data tables, dashboards, detailed views
- **Reference**: "Render the new form in Section C: Primary Workspace"
- **Components**:
  - Dynamic content area
  - Form containers
  - Data display tables
  - Interactive components
  - Content-specific toolbars

### **Section D: Status Bar**
- **Location**: Bottom horizontal bar of the application
- **Purpose**: System status, connection info, and contextual help
- **Content**: Connection status, user session info, help links, system messages
- **Reference**: "Update Section D: Status Bar with real-time connection info"
- **Components**:
  - Connection status indicator
  - Session information
  - Help/documentation links
  - System messages
  - Version information

---

## 📐 **Visual Layout Diagram**

```
┌─────────────────────────────────────────────────────────────┐
│                    Section B: Application Header            │
│  [Logo] [Search] [Notifications] [User Menu] [Settings]     │
├─────────────┬───────────────────────────────────────────────┤
│             │                                               │
│  Section A: │              Section C: Primary Workspace     │
│   Sidebar   │                                               │
│   Structure │         [Dynamic Content Area]                │
│             │                                               │
│  [Menu]     │         [Forms/Tables/Dashboards]             │
│  [Profile]  │                                               │
│  [Actions]  │                                               │
│             │                                               │
├─────────────┴───────────────────────────────────────────────┤
│                    Section D: Status Bar                    │
│  [Connection] [Session] [Help] [System Messages] [Version]  │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔗 **Additional UI Components**

### **Primary Workspace Bottom Basestrip**
- **Location**: Bottom area within Section C (Primary Workspace)
- **Purpose**: Secondary navigation and action controls for the active content
- **Content**: Tab navigation, action buttons, pagination, context-specific tools
- **Reference**: "Add pagination controls to the primary workspace bottom basestrip"

### **Component Interactions**
- **Sidebar → Primary Workspace**: Menu selection triggers content rendering
- **Header → Primary Workspace**: Global actions affect workspace content
- **Status Bar → All Sections**: System status affects entire application
- **Theme Selection → All Sections**: Theme changes apply globally

---

## 💬 **Usage Examples**

### **Clear Communication Examples**

#### **✅ Good Examples**
- "Update the sign-in message area with a new welcome message"
- "Add validation to the credentials capture section"
- "Enhance Section A: Sidebar Structure with collapsible menu items"
- "Modify Section B: Application Header to include a global search bar"
- "Render the new user form in Section C: Primary Workspace"
- "Update Section D: Status Bar with real-time connection status"
- "Add action buttons to the primary workspace bottom basestrip"

#### **❌ Ambiguous Examples**
- "Fix the login screen" (Which part?)
- "Update the menu" (Which menu?)
- "Change the header" (What specifically?)
- "Modify the main area" (Which area?)

### **Common Modification Scenarios**

#### **Login Screen Modifications**
- "Update the sign-in message area with promotional content"
- "Add two-factor authentication to the credentials capture section"
- "Include dark/light theme toggle in the theme selection area"
- "Add social login options to the sign-in buttons"

#### **Main Application Modifications**
- "Add new menu category to Section A: Sidebar Structure"
- "Implement notification center in Section B: Application Header"
- "Create new dashboard view in Section C: Primary Workspace"
- "Add real-time status indicators to Section D: Status Bar"

#### **Content-Specific Modifications**
- "Render the inventory management form in Section C: Primary Workspace"
- "Add export functionality to the primary workspace bottom basestrip"
- "Update the theme selection area to include custom themes"

---

## 📋 **Communication Best Practices**

### **When Requesting Changes**
1. **Always specify the section** using the established terminology
2. **Be specific about the component** within the section
3. **Describe the desired behavior** clearly
4. **Mention any interactions** with other sections

### **Example Template**


================================================================================
FILE END: UI_LAYOUT_TERMINOLOGY.md
================================================================================



================================================================================
FILE START: MENU_TREE_STRUCTURE.md
================================================================================

# Application Menu Structure
# Updated on 27-12-2025, 18:41 by Agent
This document reflects the current menu structure defined in `frontend/src/app/menuConfig.ts`.

---

## 🟥 Retail Now (`/`) - Industry news & trends

## 🛡️ User & Permissions - Security & access control

### 🔒 Permission Matrix (`/admin/user-permissions`) - Manage role permissions

---

## 🏪 Retail - Core retail business management

### 📊 Retail Dashboard (`/retail/dashboard`) - Operations overview

### 💳 Store Ops - POS operations and checkout

*   **Checkout** (`/operations/pos/pos`) - Checkout process
*   **Daily Operations** - 
    *   **Day Open** (`/operations/pos/day-open`) - Opening store day operations
    *   **Shift Start** (`/operations/pos/session-open`) - Start shift
    *   **Shift End** (`/operations/pos/session-close`) - End shift
    *   **Day Close** (`/operations/pos/day-close`) - Store closing operations
    *   **Reconciliation** (`/operations/pos/settlement`) - End of day settlements
*   **Registers** (`/operations/pos/terminal-configuration`) - POS terminal setup
### 📈 Sales - Manage sales orders and pricing

*   **Quotes & Estimates** (`/sales/quotes`) - Quotation management
*   **Fulfillment** (`/sales/orders`) - Order processing
*   **Invoices** (`/sales/invoices`) - Billing and invoicing
*   **Returns & Refunds** (`/sales/returns`) - Manage returns and refunds
*   **Configuration** (`/sales/configuration`) - Sales rules and approvals
### 🗄️ Merchandising - Product definition and pricing

*   **Catalog** (`/inventory/item-master`) - Master product list
*   **Code Masters** (`/setup/simple-masters`) - Category and Brand management
*   **Variants** (`/inventory/attributes`) - Product attribute configurations
*   **Attribute Values** (`/inventory/attribute-values`) - Manage attribute values
*   **Attribute Templates** (`/inventory/attribute-templates`) - Templates for attributes
*   **Price Lists** (`/inventory/price-lists`) - Pricing and discounts
*   **UOM** (`/inventory/uoms`) - Measurement units
### 📦 Inventory - Manage stock and movements

*   **Stock on Hand** - Current availability
    *   **Overview** (`/inventory/levels`) - All items summary
    *   **By Location** (`/inventory/levels?location=`) - Stock per warehouse
    *   **Low Stock** (`/inventory/levels/low_stock`) - Reorder alerts
*   **Logistics** - Replenishment and transfers
    *   **Stock Flow** (`/inventory/movements`) - Track inventory movements
    *   **Internal Transfers** (`/inventory/transfers`) - Stock transfers
    *   **Intercompany** (`/inventory/intercompany`) - Valid between companies
    *   **Reorder Policies** (`/inventory/reorder-policies`) - Min stock and reorder rules
*   **Physical Inventory** - Stock control
    *   **Stock Take** (`/inventory/stock-takes`) - Inventory audit counts
    *   **Adjustments** (`/inventory/adjustments`) - Inventory corrections
### 🛍️ Procurement - Purchasing and sourcing

*   **Vendors** (`/partners/suppliers`) - Manage suppliers and contacts
*   **Requisitions** (`/procurement/requisitions`) - Internal demand (PR)
*   **Requests for Quotation** (`/procurement/rfqs`) - Vendor bidding (RFQ)
*   **Purchase Orders** (`/procurement/orders`) - Commitment to supplier
*   **ASNs** (`/procurement/asns`) - Advance Shipment Notices
*   **Goods Receipts** (`/procurement/receipts`) - Receive stock (GRN)
*   **Invoice Matching** (`/procurement/bills`) - 3-way matching
*   **Purchase Returns** (`/procurement/returns`) - Return to vendor
*   **Payments** (`/procurement/payments`) - Vendor payments
*   **Compliance** (`/procurement/compliance`) - Vendor compliance
*   **Configuration** (`/procurement/configuration`) - Rules and approvals
### 👥 Customers - Manage customer relations

*   **Directory** (`/partners/customers`) - Customer data and contacts
*   **Groups** (`/customers/groups`) - Segments and groups
*   **Loyalty** (`/customers/loyalty`) - Rewards and loyalty plans
## 💰 Financial Management - Core accounting and financial operations

### 📊 Finance Dashboard - Financial overview and summaries

*   **Financial Overview** (`/finance/dashboard`) - 
*   **Cash Flow Summary** (`/finance/cashflow-summary`) - 
*   **Profit & Loss Summary** (`/finance/pl-summary`) - 
*   **Balance Sheet Summary** (`/finance/bs-summary`) - 
*   **Financial Alerts** (`/finance/alerts`) - 
### 📖 General Ledger - Chart of accounts and journals

*   **Chart of Accounts** (`/finance/coa`) - 
*   **Account Groups** (`/finance/account-groups`) - 
*   **Journal Entries** (`/finance/journal-entries`) - 
*   **Recurring Journals** (`/finance/recurring-journals`) - 
*   **Reversing Entries** (`/finance/reversing-entries`) - 
*   **Trial Balance** (`/finance/trial-balance`) - 
*   **General Ledger** (`/finance/gl`) - 
### 💳 Accounts Receivable - Customer invoicing and collections

*   **Customer Invoices** (`/finance/ar/invoices`) - 
*   **Credit Notes** (`/finance/ar/credit-notes`) - 
*   **Debit Notes** (`/finance/ar/debit-notes`) - 
*   **Receipts** (`/finance/ar/receipts`) - 
*   **Payment Allocation** (`/finance/ar/allocation`) - 
*   **Customer Advances** (`/finance/ar/advances`) - 
*   **Outstanding Receivables** (`/finance/ar/outstanding`) - 
*   **Aging Analysis** (`/finance/ar/aging`) - 
*   **Write-offs** (`/finance/ar/writeoffs`) - 
### 🧾 Accounts Payable - Vendor bills and payments

*   **Vendor Bills** (`/finance/ap/bills`) - 
*   **Debit Notes (Returns)** (`/finance/ap/debit-notes`) - 
*   **Credit Notes** (`/finance/ap/credit-notes`) - 
*   **Payments** (`/finance/ap/payments`) - 
*   **Vendor Advances** (`/finance/ap/advances`) - 
*   **Outstanding Payables** (`/finance/ap/outstanding`) - 
*   **Aging Analysis** (`/finance/ap/aging`) - 
*   **Expense Claims** (`/finance/ap/expense-claims`) - 
### 🏛️ Cash & Bank - Cash and bank operations

*   **Bank Accounts** (`/finance/bank/accounts`) - 
*   **Cash Accounts** (`/finance/bank/cash-accounts`) - 
*   **Deposits & Withdrawals** (`/finance/bank/deposits`) - 
*   **Bank Reconciliation** (`/finance/bank/reconciliation`) - 
*   **Cheque Management** (`/finance/bank/cheques`) - 
### 💵 Payments - Payment configuration and processing

*   **Payment Methods** (`/finance/payments/methods`) - 
*   **Payment Terms** (`/finance/payments/terms`) - 
*   **Online Payments** (`/finance/payments/online`) - 
*   **Refunds & Reversals** (`/finance/payments/refunds`) - 
*   **Payment Reconciliation** (`/finance/payments/reconciliation`) - 
### 🔢 Tax Management - GST, TDS and statutory compliance

*   **Tax Configuration** (`/finance/tax/config`) - 
*   **GST (Input / Output)** (`/finance/tax/gst`) - 
*   **TDS / TCS** (`/finance/tax/tds-tcs`) - 
*   **Tax Invoices** (`/finance/tax/invoices`) - 
*   **Tax Returns** (`/finance/tax/returns`) - 
*   **Tax Reconciliation** (`/finance/tax/reconciliation`) - 
*   **E-Invoicing / E-Way Bill** (`/finance/tax/einvoicing`) - 
### 📈 Financial Reports - Statutory and accounting reports

*   **Balance Sheet** (`/finance/reports/balance-sheet`) - 
*   **Profit & Loss** (`/finance/reports/pl`) - 
*   **Cash Flow** (`/finance/reports/cashflow`) - 
*   **Trial Balance** (`/finance/reports/trial-balance`) - 
*   **Day Book** (`/finance/reports/day-book`) - 
*   **Cash Book** (`/finance/reports/cash-book`) - 
*   **Bank Book** (`/finance/reports/bank-book`) - 
*   **Sales Register** (`/finance/reports/sales-register`) - 
*   **Purchase Register** (`/finance/reports/purchase-register`) - 
### 🔒 Period Closing - Month and year end controls

*   **Period Close** (`/finance/closing/period-close`) - 
*   **Year Close** (`/finance/closing/year-close`) - 
*   **Opening Balances** (`/finance/closing/opening-balances`) - 
*   **Period Lock** (`/finance/closing/period-lock`) - 
*   **Audit Trail** (`/finance/closing/audit-trail`) - 
## 👥 Customer Relationship Management - Sales, marketing and customer service

### 📊 CRM Dashboard & Analytics - CRM metrics and insights

*   **CRM Dashboard** (`/crm/dashboard`) - Overview and KPIs
*   **Sales Pipeline Overview** (`/crm/pipeline-overview`) - Pipeline visualization
*   **Customer Health Score** (`/crm/health-score`) - Customer engagement metrics
*   **Revenue Forecasting** (`/crm/revenue-forecast`) - Sales predictions
*   **Activity Metrics** (`/crm/activity-metrics`) - Team activity tracking
*   **Team Performance** (`/crm/team-performance`) - Sales team metrics
*   **Key Performance Indicators** (`/crm/kpis`) - CRM KPIs
*   **Real-time Alerts** (`/crm/alerts`) - Notifications and alerts
### ➕ Lead Management - Capture and qualify leads

*   **Lead Capture** (`/crm/leads/capture`) - Create new leads
*   **Lead Import/Export** (`/crm/leads/import-export`) - Bulk lead operations
*   **Lead Qualification** (`/crm/leads/qualification`) - Qualify leads
*   **Lead Scoring** (`/crm/leads/scoring`) - Score and prioritize
*   **Lead Assignment Rules** (`/crm/leads/assignment`) - Auto-assign leads
*   **Lead Routing** (`/crm/leads/routing`) - Route to sales reps
*   **Lead Nurturing Campaigns** (`/crm/leads/nurturing`) - Nurture campaigns
*   **Lead Conversion** (`/crm/leads/conversion`) - Convert to opportunities
*   **Lead Source Tracking** (`/crm/leads/source-tracking`) - Track lead sources
*   **Duplicate Lead Management** (`/crm/leads/duplicates`) - Merge duplicates
*   **Lead Reports** (`/crm/leads/reports`) - Lead analytics
### 👤 Contact Management - Manage customer contacts

*   **Contact Directory** (`/crm/contacts`) - All contacts
*   **Contact Profiles** (`/crm/contacts/profiles`) - Detailed profiles
*   **Contact Segmentation** (`/crm/contacts/segmentation`) - Segment contacts
*   **Contact Hierarchy** (`/crm/contacts/hierarchy`) - Org relationships
*   **Contact Roles** (`/crm/contacts/roles`) - Job roles
*   **Contact Activities** (`/crm/contacts/activities`) - Activity history
*   **Contact Timeline** (`/crm/contacts/timeline`) - Interaction timeline
*   **Contact Merge/Deduplication** (`/crm/contacts/merge`) - Merge duplicates
*   **Contact Import/Export** (`/crm/contacts/import-export`) - Bulk operations
*   **Contact Enrichment** (`/crm/contacts/enrichment`) - Data enrichment
*   **Social Media Integration** (`/crm/contacts/social`) - Social profiles
### 🏢 Account Management - Manage customer accounts

*   **Account Directory** (`/crm/accounts`) - All accounts
*   **Account Profiles** (`/crm/accounts/profiles`) - Account details
*   **Account Hierarchy** (`/crm/accounts/hierarchy`) - Parent-child structure
*   **Parent-Child Accounts** (`/crm/accounts/parent-child`) - Account relationships
*   **Account Teams** (`/crm/accounts/teams`) - Assign teams
*   **Account Planning** (`/crm/accounts/planning`) - Strategic planning
*   **Account Health Score** (`/crm/accounts/health`) - Account health
*   **Account Segmentation** (`/crm/accounts/segmentation`) - Segment accounts
*   **Territory Management** (`/crm/accounts/territory`) - Sales territories
*   **Account Activities** (`/crm/accounts/activities`) - Activity tracking
*   **Account Reports** (`/crm/accounts/reports`) - Account analytics
### 🎯 Opportunity Management - Manage sales opportunities

*   **Opportunity Pipeline** (`/crm/opportunities/pipeline`) - Sales pipeline
*   **Opportunity Stages** (`/crm/opportunities/stages`) - Stage management
*   **Opportunity Forecasting** (`/crm/opportunities/forecasting`) - Sales forecasting
*   **Win/Loss Analysis** (`/crm/opportunities/win-loss`) - Deal analysis
*   **Opportunity Products** (`/crm/opportunities/products`) - Product line items
*   **Opportunity Teams** (`/crm/opportunities/teams`) - Sales teams
*   **Opportunity Splits** (`/crm/opportunities/splits`) - Revenue splits
*   **Competitive Analysis** (`/crm/opportunities/competitive`) - Competitor tracking
*   **Deal Registration** (`/crm/opportunities/deal-registration`) - Register deals
*   **Opportunity Reports** (`/crm/opportunities/reports`) - Opportunity analytics
*   **Sales Methodology** (`/crm/opportunities/methodology`) - Sales process
### 📈 Sales Pipeline & Forecasting - Pipeline and revenue forecasting

*   **Pipeline Management** (`/crm/pipeline/management`) - Manage pipeline
*   **Sales Stages** (`/crm/pipeline/stages`) - Define stages
*   **Pipeline Analytics** (`/crm/pipeline/analytics`) - Pipeline insights
*   **Forecast Categories** (`/crm/pipeline/forecast-categories`) - Categorize forecasts
*   **Quota Management** (`/crm/pipeline/quota`) - Sales quotas
*   **Territory Planning** (`/crm/pipeline/territory`) - Plan territories
*   **Sales Forecasting** (`/crm/pipeline/forecasting`) - Forecast revenue
*   **Pipeline Velocity** (`/crm/pipeline/velocity`) - Deal velocity
*   **Conversion Rates** (`/crm/pipeline/conversion`) - Stage conversion
*   **Revenue Projections** (`/crm/pipeline/projections`) - Revenue forecast
*   **What-if Scenarios** (`/crm/pipeline/whatif`) - Scenario planning
### 📄 Quote & Proposal Management - CPQ and proposals

*   **Quote Generation** (`/crm/quotes/generate`) - Create quotes
*   **Quote Templates** (`/crm/quotes/templates`) - Quote templates
*   **Product Catalog** (`/crm/quotes/catalog`) - Product catalog
*   **Price Books** (`/crm/quotes/price-books`) - Pricing lists
*   **Discount Management** (`/crm/quotes/discounts`) - Manage discounts
*   **Quote Approval Workflow** (`/crm/quotes/approval`) - Approval process
*   **Quote Versioning** (`/crm/quotes/versioning`) - Version control
*   **E-signature Integration** (`/crm/quotes/esignature`) - Digital signatures
*   **Quote Analytics** (`/crm/quotes/analytics`) - Quote metrics
*   **CPQ (Configure, Price, Quote)** (`/crm/quotes/cpq`) - Advanced CPQ
### 📣 Campaign Management - Marketing campaigns

*   **Campaign Planning** (`/crm/campaigns/planning`) - Plan campaigns
*   **Campaign Execution** (`/crm/campaigns/execution`) - Execute campaigns
*   **Campaign Tracking** (`/crm/campaigns/tracking`) - Track performance
*   **Campaign ROI** (`/crm/campaigns/roi`) - Return on investment
*   **Target Lists** (`/crm/campaigns/target-lists`) - Audience segments
*   **Campaign Members** (`/crm/campaigns/members`) - Campaign participants
*   **Multi-channel Campaigns** (`/crm/campaigns/multichannel`) - Cross-channel
*   **Campaign Automation** (`/crm/campaigns/automation`) - Automated campaigns
*   **A/B Testing** (`/crm/campaigns/ab-testing`) - Test variations
*   **Campaign Reports** (`/crm/campaigns/reports`) - Campaign analytics
*   **Marketing Attribution** (`/crm/campaigns/attribution`) - Attribution models
### 📧 Email Marketing & Automation - Email campaigns and automation

*   **Email Templates** (`/crm/email/templates`) - Email templates
*   **Email Campaigns** (`/crm/email/campaigns`) - Email campaigns
*   **Email Sequences** (`/crm/email/sequences`) - Email sequences
*   **Drip Campaigns** (`/crm/email/drip`) - Automated drip
*   **Email Tracking** (`/crm/email/tracking`) - Track opens/clicks
*   **Email Analytics** (`/crm/email/analytics`) - Email metrics
*   **Unsubscribe Management** (`/crm/email/unsubscribe`) - Manage opt-outs
*   **Email Deliverability** (`/crm/email/deliverability`) - Delivery rates
*   **Marketing Automation** (`/crm/email/automation`) - Workflow automation
*   **Workflow Automation** (`/crm/email/workflows`) - Automated workflows
*   **Trigger-based Emails** (`/crm/email/triggers`) - Event-triggered
### 🎧 Customer Service & Support - Support and service management

*   **Case Management** (`/crm/service/cases`) - Support cases
*   **Ticket System** (`/crm/service/tickets`) - Support tickets
*   **Service Level Agreements (SLA)** (`/crm/service/sla`) - SLA tracking
*   **Case Routing** (`/crm/service/routing`) - Auto-route cases
*   **Case Escalation** (`/crm/service/escalation`) - Escalation rules
*   **Knowledge Base** (`/crm/service/knowledge`) - Help articles
*   **Self-service Portal** (`/crm/service/portal`) - Customer portal
*   **Live Chat** (`/crm/service/chat`) - Live chat support
*   **Chatbot Integration** (`/crm/service/chatbot`) - AI chatbot
*   **Service Analytics** (`/crm/service/analytics`) - Support metrics
*   **Customer Satisfaction (CSAT)** (`/crm/service/csat`) - Satisfaction surveys
### 💬 Customer Engagement & Communication - Multi-channel engagement

*   **Activity Timeline** (`/crm/engagement/timeline`) - Interaction history
*   **Email Integration** (`/crm/engagement/email`) - Email sync
*   **Calendar Integration** (`/crm/engagement/calendar`) - Calendar sync
*   **Task Management** (`/crm/engagement/tasks`) - Task tracking
*   **Meeting Scheduler** (`/crm/engagement/meetings`) - Schedule meetings
*   **Call Logging** (`/crm/engagement/calls`) - Log calls
*   **SMS Integration** (`/crm/engagement/sms`) - SMS messaging
*   **WhatsApp Integration** (`/crm/engagement/whatsapp`) - WhatsApp messaging
*   **Social Media Engagement** (`/crm/engagement/social`) - Social interactions
*   **Communication History** (`/crm/engagement/history`) - All communications
*   **Engagement Scoring** (`/crm/engagement/scoring`) - Engagement metrics
### 🏆 Customer Loyalty & Retention - Loyalty programs and retention

*   **Loyalty Programs** (`/crm/loyalty/programs`) - Loyalty schemes
*   **Points Management** (`/crm/loyalty/points`) - Points tracking
*   **Rewards Catalog** (`/crm/loyalty/rewards`) - Reward items
*   **Tier Management** (`/crm/loyalty/tiers`) - Membership tiers
*   **Member Portal** (`/crm/loyalty/portal`) - Member access
*   **Redemption Management** (`/crm/loyalty/redemption`) - Redeem rewards
*   **Loyalty Analytics** (`/crm/loyalty/analytics`) - Program metrics
*   **Churn Prediction** (`/crm/loyalty/churn`) - Predict churn
*   **Win-back Campaigns** (`/crm/loyalty/winback`) - Re-engage customers
*   **Customer Lifetime Value (CLV)** (`/crm/loyalty/clv`) - Lifetime value
### 🤝 Partner & Channel Management - Partner and reseller management

*   **Partner Portal** (`/crm/partners/portal`) - Partner access
*   **Partner Onboarding** (`/crm/partners/onboarding`) - Onboard partners
*   **Partner Performance** (`/crm/partners/performance`) - Track performance
*   **Deal Registration** (`/crm/partners/deals`) - Register deals
*   **Partner Incentives** (`/crm/partners/incentives`) - Incentive programs
*   **Co-marketing Programs** (`/crm/partners/comarketing`) - Joint marketing
*   **Partner Training** (`/crm/partners/training`) - Training programs
*   **Partner Resources** (`/crm/partners/resources`) - Resource library
*   **Partner Analytics** (`/crm/partners/analytics`) - Partner metrics
*   **Channel Conflict Resolution** (`/crm/partners/conflict`) - Resolve conflicts
### 💼 Sales Enablement - Sales tools and resources

*   **Sales Content Library** (`/crm/enablement/library`) - Sales materials
*   **Sales Playbooks** (`/crm/enablement/playbooks`) - Sales guides
*   **Competitive Intelligence** (`/crm/enablement/competitive`) - Competitor info
*   **Product Training** (`/crm/enablement/training`) - Product knowledge
*   **Sales Scripts** (`/crm/enablement/scripts`) - Call scripts
*   **Objection Handling** (`/crm/enablement/objections`) - Handle objections
*   **Best Practices** (`/crm/enablement/best-practices`) - Sales best practices
*   **Sales Tools** (`/crm/enablement/tools`) - Sales utilities
*   **Mobile Sales App** (`/crm/enablement/mobile`) - Mobile access
*   **Offline Access** (`/crm/enablement/offline`) - Work offline
### 📈 Analytics & Reporting - CRM analytics and insights

*   **Sales Analytics** - Sales performance metrics
    *   **Sales Performance Reports** (`/crm/analytics/sales-performance`) - Team performance
    *   **Win/Loss Analysis** (`/crm/analytics/win-loss`) - Deal outcomes
    *   **Sales Cycle Analysis** (`/crm/analytics/sales-cycle`) - Cycle time
    *   **Revenue Reports** (`/crm/analytics/revenue`) - Revenue metrics
    *   **Activity Reports** (`/crm/analytics/activity`) - Sales activities
    *   **Leaderboards** (`/crm/analytics/leaderboards`) - Top performers
*   **Customer Analytics** - Customer insights
    *   **Customer Segmentation** (`/crm/analytics/segmentation`) - Segment analysis
    *   **Customer Behavior Analysis** (`/crm/analytics/behavior`) - Behavior patterns
    *   **Customer Journey Analytics** (`/crm/analytics/journey`) - Journey mapping
    *   **Churn Analysis** (`/crm/analytics/churn`) - Churn metrics
    *   **Customer Profitability** (`/crm/analytics/profitability`) - Profit by customer
    *   **RFM Analysis** (`/crm/analytics/rfm`) - Recency, Frequency, Monetary
*   **Marketing Analytics** - Marketing performance
    *   **Campaign Performance** (`/crm/analytics/campaign-performance`) - Campaign metrics
    *   **Lead Source ROI** (`/crm/analytics/lead-source`) - Source effectiveness
    *   **Marketing Attribution** (`/crm/analytics/attribution`) - Attribution models
    *   **Conversion Funnel** (`/crm/analytics/funnel`) - Funnel analysis
    *   **Email Performance** (`/crm/analytics/email-performance`) - Email metrics
    *   **Social Media Analytics** (`/crm/analytics/social`) - Social metrics
*   **Custom Reports** - Build custom reports
    *   **Report Builder** (`/crm/analytics/builder`) - Create reports
    *   **Dashboard Designer** (`/crm/analytics/designer`) - Design dashboards
    *   **Scheduled Reports** (`/crm/analytics/scheduled`) - Automated reports
    *   **Export to Excel/PDF** (`/crm/analytics/export`) - Export data
### ⚡ Workflow & Automation - Automate CRM processes

*   **Workflow Rules** (`/crm/automation/rules`) - Automation rules
*   **Process Builder** (`/crm/automation/process`) - Build processes
*   **Approval Processes** (`/crm/automation/approvals`) - Approval workflows
*   **Assignment Rules** (`/crm/automation/assignment`) - Auto-assignment
*   **Auto-response Rules** (`/crm/automation/autoresponse`) - Automated responses
*   **Escalation Rules** (`/crm/automation/escalation`) - Auto-escalation
*   **Field Updates** (`/crm/automation/field-updates`) - Update fields
*   **Email Alerts** (`/crm/automation/email-alerts`) - Automated emails
*   **Task Creation** (`/crm/automation/tasks`) - Auto-create tasks
*   **Record Updates** (`/crm/automation/records`) - Update records
*   **Time-based Actions** (`/crm/automation/timebased`) - Scheduled actions
### 🔗 Integration & Data Management - Connect and manage data

*   **Email Integration (Gmail, Outlook)** (`/crm/integration/email`) - Email sync
*   **Calendar Sync** (`/crm/integration/calendar`) - Calendar integration
*   **Social Media Integration** (`/crm/integration/social`) - Social platforms
*   **Telephony Integration (CTI)** (`/crm/integration/telephony`) - Phone system
*   **Marketing Automation Integration** (`/crm/integration/marketing`) - Marketing tools
*   **E-commerce Integration** (`/crm/integration/ecommerce`) - Online stores
*   **Accounting Integration** (`/crm/integration/accounting`) - Accounting systems
*   **Data Import/Export** (`/crm/integration/data`) - Bulk data operations
*   **API Management** (`/crm/integration/api`) - API access
*   **Webhook Configuration** (`/crm/integration/webhooks`) - Event webhooks
*   **Third-party Apps** (`/crm/integration/apps`) - App integrations
*   **AppExchange/Marketplace** (`/crm/integration/marketplace`) - App marketplace
### ⚙️ CRM Configuration & Administration - CRM setup and administration

*   **User Management** (`/crm/config/users`) - Manage users
*   **Roles & Permissions** (`/crm/config/roles`) - Access control
*   **Profiles & Permission Sets** (`/crm/config/profiles`) - User profiles
*   **Sharing Rules** (`/crm/config/sharing`) - Record sharing
*   **Field-level Security** (`/crm/config/field-security`) - Field permissions
*   **Page Layouts** (`/crm/config/layouts`) - Customize layouts
*   **Record Types** (`/crm/config/record-types`) - Record categories
*   **Validation Rules** (`/crm/config/validation`) - Data validation
*   **Custom Fields** (`/crm/config/fields`) - Add custom fields
*   **Custom Objects** (`/crm/config/objects`) - Create objects
*   **Picklist Management** (`/crm/config/picklists`) - Manage picklists
*   **Email Templates** (`/crm/config/email-templates`) - Template library
*   **System Settings** (`/crm/config/settings`) - CRM configuration
*   **Audit Trail** (`/crm/config/audit`) - Track changes
*   **Data Backup & Recovery** (`/crm/config/backup`) - Backup data
## 👥 Human Resources - Manage employee lifecycle and payroll

### 📈 HR Dashboard (`/hr/dashboard`) - HR overview and KPIs

### 👥 Employee Management - Employee records and services

*   **Employee Directory** (`/hr/employees`) - View and manage employees
*   **Organizational Chart** (`/hr/org-chart`) - Org structure
*   **Employee Self-Service** (`/hr/self-service`) - Employee portal
*   **Document Management** (`/hr/documents`) - HR documents
*   **Employee Lifecycle** (`/hr/lifecycle`) - Onboarding to exit
### 🏆 Talent Acquisition - Hiring pipeline

*   **Job Requisitions** (`/hr/jobs`) - Open positions
*   **Candidate Management** (`/hr/candidates`) - Applicants and pipeline
*   **Interview Scheduling** (`/hr/interviews`) - Schedule and track interviews
*   **Offer Management** (`/hr/offers`) - Prepare and send offers
*   **Onboarding** (`/hr/onboarding`) - New hire onboarding
### 💰 Compensation & Payroll - Salaries, benefits and payroll

*   **Payroll Processing** (`/hr/payroll`) - Run payroll
*   **Salary Structures** (`/hr/salary-structures`) - Grades and components
*   **Benefits Administration** (`/hr/benefits`) - Benefits plans
*   **Bonus & Incentives** (`/hr/bonuses`) - Bonuses and incentives
*   **Taxation & Compliance** (`/hr/tax`) - Tax setup and filings
*   **Statutory Filings** (`/hr/statutory`) - Regulatory filings
### ⏰ Time & Attendance - Scheduling and attendance

*   **Clock-In/Out** (`/hr/time/clock`) - Record time
*   **Attendance Tracking** (`/hr/time/attendance`) - Attendance reports
*   **Leave & Absence** (`/hr/time/leave`) - Leave requests
*   **Shift Scheduling** (`/hr/time/shifts`) - Shift planning
*   **Overtime Management** (`/hr/time/overtime`) - Overtime tracking
### 🏆 Performance Management - Goals, reviews and growth

*   **Goal Setting** (`/hr/performance/goals`) - Define objectives
*   **Appraisals & Feedback** (`/hr/performance/appraisals`) - Performance reviews
*   **Calibration & Ranking** (`/hr/performance/calibration`) - Normalize ratings
*   **Succession Planning** (`/hr/performance/succession`) - Talent pipeline
*   **360 Degree Reviews** (`/hr/performance/360`) - Peer and manager feedback
### 📖 Learning & Development - Training and competencies

*   **Training Catalog** (`/hr/learning/catalog`) - Available courses
*   **Course Management** (`/hr/learning/courses`) - Create and manage courses
*   **Certifications & Compliance** (`/hr/learning/certifications`) - Certifications and compliance
*   **Skill & Competency Management** (`/hr/learning/skills`) - Skills and competencies
*   **Learning Paths & Career Dev** (`/hr/learning/paths`) - Career paths
### 💬 Employee Engagement & Recognition - Surveys, rewards and collaboration

*   **Surveys & Feedback** (`/hr/engagement/surveys`) - Collect feedback
*   **Rewards & Recognition** (`/hr/engagement/rewards`) - Recognize achievements
*   **Social Collaboration** (`/hr/engagement/social`) - Company social feed
### 🥧 Workforce Planning & Analytics - Headcount and analytics

*   **Headcount Planning** (`/hr/workforce/headcount`) - Plan staffing
*   **Attrition & Retention** (`/hr/workforce/attrition`) - Track turnover
*   **Diversity & Inclusion** (`/hr/workforce/diversity`) - D&I insights
*   **Workforce Costs** (`/hr/workforce/costs`) - Labor cost analysis
### 🔒 Compliance & Policies - Policies, compliance and incidents

*   **Labor Law Compliance** (`/hr/compliance/labor-law`) - Labor laws compliance
*   **Company Policies** (`/hr/compliance/policies`) - Company policies
*   **Grievance Management** (`/hr/compliance/grievances`) - Handle grievances
*   **Incident Tracking** (`/hr/compliance/incidents`) - Record incidents
### 🚪 Offboarding & Exit Management - Resignations and exits

*   **Resignation Processing** (`/hr/offboarding/resignation`) - Process resignations
*   **Exit Interviews** (`/hr/offboarding/exit-interviews`) - Capture feedback
*   **Knowledge Transfer** (`/hr/offboarding/knowledge-transfer`) - Transition knowledge
*   **Final Settlement** (`/hr/offboarding/final-settlement`) - Payroll finalization
### 📈 HR Reports & Analytics - HR reports and dashboards

*   **Standard Reports** (`/hr/reports/standard`) - Pre-built HR reports
*   **Custom Reports** (`/hr/reports/custom`) - Build your own reports
*   **Dashboards & Visualizations** (`/hr/reports/dashboards`) - HR dashboards
*   **Data Export & Integration** (`/hr/reports/export`) - Export and integrate data
### 🛡️ Access & Security - Roles, SSO and audits

*   **Roles & Permissions** (`/hr/roles`) - User roles and access control
*   **Security Policies** (`/hr/security`) - Security policies
*   **Audit Logs** (`/hr/audit`) - HR security audit logs
*   **SSO Configuration** (`/hr/sso`) - Single sign-on setup
### ⚙️ Integrations & Configuration - Integrations and settings

*   **Third-Party Integrations** (`/hr/integrations/third-party`) - Connect external apps
*   **System Settings** (`/hr/integrations/system`) - HR module settings
*   **API Management** (`/hr/integrations/api`) - API access and keys
*   **Data Privacy & Security** (`/hr/integrations/privacy`) - Privacy and data security
---

## ⚡ Phase 2 - Advanced Features - Enterprise capabilities for FMS, HRM & CRM

### 💰 Financial Management (Phase 2) - Advanced financial features

*   **Multi-Currency & FX** (`/finance/phase2/multi-currency`) - Foreign exchange management
*   **Inter-company & Consolidation** (`/finance/phase2/consolidation`) - Group consolidation
*   **Fixed Assets Management** (`/finance/phase2/fixed-assets`) - Asset tracking & depreciation
*   **Budgeting & Planning** (`/finance/phase2/budgeting`) - Budget management
*   **Treasury Management** (`/finance/phase2/treasury`) - Cash & liquidity management
*   **Revenue Recognition** (`/finance/phase2/revenue-recognition`) - ASC 606 compliance
*   **Cost Accounting & Job Costing** (`/finance/phase2/cost-accounting`) - Project costing
*   **Period-End & Year-End Closing** (`/finance/phase2/period-close`) - Closing procedures
### 👥 Human Resources (Phase 2) - Advanced HR capabilities

*   **Performance Management** (`/hr/phase2/performance`) - Goals & reviews
*   **Learning & Development** (`/hr/phase2/learning`) - Training programs
*   **Succession Planning** (`/hr/phase2/succession`) - Talent pipeline
*   **Employee Engagement** (`/hr/phase2/engagement`) - Recognition & surveys
*   **Workforce Analytics** (`/hr/phase2/analytics`) - HR metrics & insights
*   **Compliance & Policies** (`/hr/phase2/compliance`) - Labor law compliance
### 🤝 CRM (Phase 2) - Advanced CRM features

*   **CPQ (Configure, Price, Quote)** (`/crm/phase2/cpq`) - Quote management
*   **Marketing Automation** (`/crm/phase2/marketing-automation`) - Campaign automation
*   **Customer Service & Support** (`/crm/phase2/service`) - Support ticketing
*   **Loyalty & Retention** (`/crm/phase2/loyalty`) - Loyalty programs
*   **Partner & Channel Management** (`/crm/phase2/partners`) - Partner portal
*   **Sales Enablement** (`/crm/phase2/sales-enablement`) - Sales tools & content
*   **Advanced Analytics** (`/crm/phase2/analytics`) - Predictive analytics
---

## 🛡️ System Administration - Configure and manage system settings

### 👥 User Management (`/admin/users`) - Manage user accounts and roles

### 📐 Layout Settings (`/admin/layout-settings`) - Configure layout and appearance

### 🔒 Security Settings (`/admin/security`) - System security configurations

### Audit Logs (`/admin/audit`) - User activity auditing

### 💾 Backup & Recovery (`/admin/backup`) - Data backup and restore

## ⚙️ System Configuration - Setup company and system settings

### 🏢 Company Settings (`/setup/company`) - Company details and preferences

### 📍 Location Setup (`/setup/locations`) - Manage company locations

### 📅 Fiscal Periods (`/setup/fiscal`) - Financial year and periods

### 🪙 Currencies & Exchange (`/setup/currencies`) - Currency management

### 🔢 Tax Configuration (`/setup/tax`) - Tax rules and settings


================================================================================
FILE END: MENU_TREE_STRUCTURE.md
================================================================================



================================================================================
FILE START: COMPONENT_LIBRARY.md
================================================================================

# Component Library Reference

**Version**: 1.0  
**Stack**: React + Tailwind CSS + Lucide Icons  
**Design System**: Enterprise Retail ERP

---

## 🎨 Design Tokens

```javascript
// Import path: ../tokens/designTokens.js
import { colors, spacing, typography } from '../tokens/designTokens';
```

### Color Palette

| Token | Usage |
|-------|-------|
| `primary-500` | Primary actions, links, focus states |
| `primary-600` | Primary hover states |
| `primary-700` | Primary active states |
| `success-500` | Success states, active status |
| `success-100` | Success backgrounds |
| `accent-500` | Destructive actions, errors |
| `accent-100` | Error backgrounds |
| `warning-500` | Warning states |
| `surface-50` | Page backgrounds |
| `surface-100` | Card backgrounds, hover states |
| `surface-200` | Borders, dividers |
| `surface-600` | Secondary text |
| `surface-700` | Label text |
| `surface-900` | Primary text, headings |
| `neutralBg-50` | Main page background |

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `xs` | 4px | Tight spacing |
| `sm` | 8px | Small gaps |
| `md` | 16px | Standard padding |
| `lg` | 24px | Section spacing |
| `xl` | 32px | Large gaps |
| `2xl` | 48px | Page margins |

---

## 🧱 Base Components

### Button

```jsx
<Button
  variant="primary"      // primary | secondary | outline | accent | ghost
  size="md"              // sm | md | lg
  loading={false}        // Shows spinner
  disabled={false}
  onClick={handleClick}
>
  Button Text
</Button>
```

| Variant | Usage |
|---------|-------|
| `primary` | Primary actions (Save, Submit, Create) |
| `secondary` | Secondary actions |
| `outline` | Tertiary actions (Edit, View) |
| `accent` | Destructive actions (Delete, Cancel) |
| `ghost` | Minimal actions (Close, Dismiss) |

### Input

```jsx
<Input
  type="text"            // text | number | email | password | date
  value={value}
  onChange={handleChange}
  placeholder="Enter value"
  error="Error message"  // Shows error state
  disabled={false}
  required={false}
/>
```

### Select

```jsx
<Select
  value={value}
  onChange={handleChange}
  options={[
    { value: 'opt1', label: 'Option 1' },
    { value: 'opt2', label: 'Option 2' },
  ]}
  placeholder="Select option"
  error="Error message"
  disabled={false}
/>
```

### Checkbox

```jsx
<Checkbox
  checked={checked}
  onChange={handleChange}
  label="Checkbox label"
  disabled={false}
/>
```

### Toggle / Switch

```jsx
<Toggle
  checked={checked}
  onChange={handleChange}
  label="Toggle label"
  disabled={false}
/>
```

### DatePicker

```jsx
<DatePicker
  value={date}
  onChange={handleChange}
  minDate={minDate}
  maxDate={maxDate}
  placeholder="Select date"
/>
```

### Textarea

```jsx
<textarea
  value={value}
  onChange={handleChange}
  rows={3}
  className="w-full px-3 py-2 border border-surface-300 rounded-md shadow-sm focus:ring-primary-500 focus:border-primary-500"
  placeholder="Enter text..."
/>
```

---

## 📐 Layout Components

### Card

```jsx
<div className="bg-white rounded-lg shadow-sm border border-surface-200 p-6">
  {/* Card content */}
</div>
```

### Modal

```jsx
{showModal && (
  <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div className="bg-white rounded-lg p-6 max-w-md w-full mx-4">
      <h2 className="text-lg font-semibold text-surface-900 mb-4">Modal Title</h2>
      {/* Modal content */}
      <div className="flex justify-end space-x-3 pt-4">
        <Button variant="outline" onClick={onClose}>Cancel</Button>
        <Button onClick={onConfirm}>Confirm</Button>
      </div>
    </div>
  </div>
)}
```

### Drawer (Side Panel)

```jsx
{showDrawer && (
  <div className="fixed inset-0 z-50 flex">
    <div className="fixed inset-0 bg-black bg-opacity-50" onClick={onClose} />
    <div className="ml-auto w-96 bg-white h-full shadow-xl p-6 overflow-y-auto">
      <h2 className="text-lg font-semibold text-surface-900 mb-4">Drawer Title</h2>
      {/* Drawer content */}
    </div>
  </div>
)}
```

### Tabs

```jsx
const [activeTab, setActiveTab] = useState('general');

<div className="border-b border-surface-200">
  <nav className="flex space-x-8">
    {['general', 'settings', 'advanced'].map(tab => (
      <button
        key={tab}
        onClick={() => setActiveTab(tab)}
        className={`py-4 px-1 border-b-2 font-medium text-sm ${
          activeTab === tab
            ? 'border-primary-500 text-primary-600'
            : 'border-transparent text-surface-500 hover:text-surface-700'
        }`}
      >
        {tab.charAt(0).toUpperCase() + tab.slice(1)}
      </button>
    ))}
  </nav>
</div>
```

### Accordion

```jsx
const [expanded, setExpanded] = useState(null);

<div className="space-y-2">
  {sections.map((section, index) => (
    <div key={index} className="border border-surface-200 rounded-lg">
      <button
        onClick={() => setExpanded(expanded === index ? null : index)}
        className="w-full px-4 py-3 flex justify-between items-center"
      >
        <span className="font-medium">{section.title}</span>
        <ChevronDown className={`w-5 h-5 transition-transform ${expanded === index ? 'rotate-180' : ''}`} />
      </button>
      {expanded === index && (
        <div className="px-4 pb-4">{section.content}</div>
      )}
    </div>
  ))}
</div>
```

### Sidebar

```jsx
<div className="w-64 bg-white border-r border-surface-200 h-screen">
  <div className="p-4">
    <h2 className="text-lg font-semibold">Navigation</h2>
  </div>
  <nav className="mt-4">
    {menuItems.map(item => (
      <a
        key={item.id}
        href={item.href}
        className={`flex items-center px-4 py-2 text-sm ${
          activeItem === item.id
            ? 'bg-primary-50 text-primary-700 border-r-2 border-primary-500'
            : 'text-surface-600 hover:bg-surface-50'
        }`}
      >
        {item.icon}
        <span className="ml-3">{item.label}</span>
      </a>
    ))}
  </nav>
</div>
```

---

## 📊 Data Display Components

### Table

```jsx
<Table
  columns={[
    { header: 'Code', accessor: 'code', sortable: true },
    { header: 'Name', accessor: 'name', sortable: true },
    { 
      header: 'Status', 
      accessor: 'status',
      cell: (row) => <Badge status={row.status} />
    },
    {
      header: 'Actions',
      cell: (row) => (
        <div className="flex space-x-2">
          <Button variant="outline" size="sm" onClick={() => onEdit(row)}>Edit</Button>
          <Button variant="accent" size="sm" onClick={() => onDelete(row.id)}>Delete</Button>
        </div>
      )
    }
  ]}
  data={data}
  loading={loading}
  empty={data.length === 0}
  emptyMessage="No data found"
  onSort={handleSort}
/>
```

### DataGrid (with selection)

```jsx
<DataGrid
  columns={columns}
  data={data}
  selectable={true}
  selectedRows={selectedRows}
  onSelectionChange={setSelectedRows}
  pagination={pagination}
  onPaginationChange={setPagination}
/>
```

### Tree View

```jsx
<TreeView
  data={treeData}
  selectedNode={selectedNode}
  expandedNodes={expandedNodes}
  onNodeSelect={handleNodeSelect}
  onNodeExpand={handleNodeExpand}
  onNodeMove={handleNodeMove}
/>
```

### Card Grid

```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
  {data.map(item => (
    <div key={item.id} className="bg-white rounded-lg shadow-sm border border-surface-200 p-4">
      <h3 className="font-semibold text-surface-900">{item.name}</h3>
      <p className="text-sm text-surface-600 mt-1">{item.description}</p>
      <div className="mt-4 flex justify-end space-x-2">
        <Button variant="outline" size="sm">Edit</Button>
        <Button variant="accent" size="sm">Delete</Button>
      </div>
    </div>
  ))}
</div>
```

### Badge / Tag

```jsx
// Status Badge
<span className={`px-2 py-1 text-xs font-medium rounded-full ${
  status === 'active' 
    ? 'bg-success-100 text-success-800' 
    : status === 'inactive'
    ? 'bg-surface-100 text-surface-600'
    : 'bg-warning-100 text-warning-800'
}`}>
  {status}
</span>

// Tag
<span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-primary-100 text-primary-800">
  {tag}
  <button onClick={onRemove} className="ml-1 text-primary-600 hover:text-primary-800">×</button>
</span>
```

---

## 💬 Feedback Components

### Toast / Notification

```jsx
// Success Toast
<div className="fixed bottom-4 right-4 bg-success-500 text-white px-4 py-3 rounded-lg shadow-lg flex items-center">
  <CheckCircle className="w-5 h-5 mr-2" />
  <span>Operation successful</span>
</div>

// Error Toast
<div className="fixed bottom-4 right-4 bg-accent-500 text-white px-4 py-3 rounded-lg shadow-lg flex items-center">
  <AlertCircle className="w-5 h-5 mr-2" />
  <span>Operation failed</span>
</div>
```

### Alert

```jsx
// Success Alert
<div className="bg-success-50 border border-success-200 rounded-md p-4">
  <div className="flex">
    <CheckCircle className="h-5 w-5 text-success-400" />
    <div className="ml-3">
      <h3 className="text-sm font-medium text-success-800">Success</h3>
      <p className="text-sm text-success-700 mt-1">{message}</p>
    </div>
  </div>
</div>

// Error Alert
<div className="bg-accent-50 border border-accent-200 rounded-md p-4">
  <div className="flex">
    <AlertCircle className="h-5 w-5 text-accent-400" />
    <div className="ml-3">
      <h3 className="text-sm font-medium text-accent-800">Error</h3>
      <p className="text-sm text-accent-700 mt-1">{message}</p>
    </div>
  </div>
</div>
```

### Spinner / Loader

```jsx
// Inline Spinner
<div className="animate-spin rounded-full h-5 w-5 border-2 border-primary-500 border-t-transparent" />

// Full Page Loader
<div className="flex justify-center items-center h-64">
  <div className="animate-spin rounded-full h-12 w-12 border-4 border-gray-300 border-t-primary-500" />
</div>
```

### Skeleton Loader

```jsx
// Text Skeleton
<div className="animate-pulse">
  <div className="h-4 bg-surface-200 rounded w-3/4 mb-2" />
  <div className="h-4 bg-surface-200 rounded w-1/2" />
</div>

// Card Skeleton
<div className="animate-pulse bg-white rounded-lg border border-surface-200 p-4">
  <div className="h-6 bg-surface-200 rounded w-1/3 mb-4" />
  <div className="h-4 bg-surface-200 rounded w-full mb-2" />
  <div className="h-4 bg-surface-200 rounded w-2/3" />
</div>
```

### Progress Bar

```jsx
<div className="w-full bg-surface-200 rounded-full h-2">
  <div 
    className="bg-primary-500 h-2 rounded-full transition-all duration-300"
    style={{ width: `${progress}%` }}
  />
</div>
```

---

## 🧭 Navigation Components

### Breadcrumb

```jsx
<nav className="flex items-center space-x-2 text-sm">
  {breadcrumbs.map((crumb, index) => (
    <React.Fragment key={crumb.path}>
      {index > 0 && <ChevronRight className="w-4 h-4 text-surface-400" />}
      {index === breadcrumbs.length - 1 ? (
        <span className="text-surface-900 font-medium">{crumb.label}</span>
      ) : (
        <a href={crumb.path} className="text-surface-500 hover:text-primary-600">
          {crumb.label}
        </a>
      )}
    </React.Fragment>
  ))}
</nav>
```

### Pagination

```jsx
<div className="flex items-center justify-between px-4 py-3 bg-white border-t border-surface-200">
  <div className="text-sm text-surface-600">
    Showing {(page - 1) * limit + 1} to {Math.min(page * limit, total)} of {total} results
  </div>
  <div className="flex space-x-2">
    <Button 
      variant="outline" 
      size="sm" 
      disabled={page === 1}
      onClick={() => setPage(page - 1)}
    >
      Previous
    </Button>
    <Button 
      variant="outline" 
      size="sm" 
      disabled={page * limit >= total}
      onClick={() => setPage(page + 1)}
    >
      Next
    </Button>
  </div>
</div>
```

### Dropdown Menu

```jsx
const [open, setOpen] = useState(false);

<div className="relative">
  <Button onClick={() => setOpen(!open)}>
    Actions <ChevronDown className="w-4 h-4 ml-2" />
  </Button>
  
  {open && (
    <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg border border-surface-200 z-10">
      {menuItems.map(item => (
        <button
          key={item.id}
          onClick={() => { item.onClick(); setOpen(false); }}
          className="block w-full text-left px-4 py-2 text-sm text-surface-700 hover:bg-surface-50"
        >
          {item.label}
        </button>
      ))}
    </div>
  )}
</div>
```

---

## 📝 Form Patterns

### Standard Form Layout

```jsx
<form onSubmit={handleSubmit} className="space-y-6">
  {/* Two Column Grid */}
  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
    <div>
      <label className="block text-sm font-medium text-surface-700 mb-1">
        Field Label *
      </label>
      <Input value={value} onChange={onChange} error={errors.field} />
    </div>
  </div>

  {/* Full Width Field */}
  <div>
    <label className="block text-sm font-medium text-surface-700 mb-1">
      Description
    </label>
    <textarea rows={3} className="w-full ..." />
  </div>

  {/* Form Actions */}
  <div className="flex justify-end space-x-3 pt-4 border-t border-surface-200">
    <Button type="button" variant="outline" onClick={onCancel}>Cancel</Button>
    <Button type="submit" loading={isSubmitting}>Save</Button>
  </div>
</form>
```

### Tabbed Form

```jsx
<div>
  {/* Tab Navigation */}
  <div className="border-b border-surface-200 mb-6">
    <nav className="flex space-x-8">
      {tabs.map(tab => (
        <button
          key={tab.id}
          onClick={() => setActiveTab(tab.id)}
          className={`py-4 px-1 border-b-2 font-medium text-sm ${
            activeTab === tab.id
              ? 'border-primary-500 text-primary-600'
              : 'border-transparent text-surface-500'
          }`}
        >
          {tab.label}
        </button>
      ))}
    </nav>
  </div>

  {/* Tab Content */}
  {activeTab === 'general' && <GeneralTab />}
  {activeTab === 'settings' && <SettingsTab />}
</div>
```

---

## 🎯 Usage Guidelines

### Consistency Rules

1. **Always use design tokens** - Never hardcode colors or spacing
2. **Follow naming conventions** - PascalCase for components, camelCase for hooks
3. **Maintain accessibility** - All interactive elements must be keyboard accessible
4. **Responsive first** - Design for mobile, enhance for desktop

### Import Pattern

```jsx
// Standard imports for any component
import React, { useState, useEffect, useCallback, useMemo } from 'react';
import { colors, spacing, typography } from '../tokens/designTokens';
import Button from '../components/Button';
import Input from '../components/Input';
import Table from '../components/Table';
import { Search, Plus, Edit, Trash2, ChevronDown } from 'lucide-react';
```

---

## 📚 Related Documentation

- **Design Tokens**: `../tokens/designTokens.js`
- **State Patterns**: `docs/steering/STATE_PATTERNS.md`
- **Prompt Templates**: `docs/steering/prompts.master.md`
- **MST Templates**: `docs/templates/mst01.md`, `docs/templates/mst02.md`, `docs/templates/mst03.md`
- **TXN Templates**: `docs/templates/txn01.md`, `docs/templates/txn02.md`, `docs/templates/txn03.md`


================================================================================
FILE END: COMPONENT_LIBRARY.md
================================================================================



================================================================================
FILE START: STATE_PATTERNS.md
================================================================================

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


================================================================================
FILE END: STATE_PATTERNS.md
================================================================================



================================================================================
FILE START: typography.md
================================================================================

OLIVINE TYPOGRAPHY RULES (AUTHORITATIVE)

1. FONT FAMILY
- Primary font: Inter
- Fallbacks:
  'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
- Only ONE font family is allowed across the application.
- No per-component or per-module font overrides.

2. FONT WEIGHTS (STRICT)
- Regular: 400
- Medium: 500
- Semibold: 600
- Do NOT use 300, 700, or higher.
- Bold text must be rare and intentional.

3. FONT SIZES (ERP-OPTIMIZED SCALE)
- Page Title: 20–22px (600)
- Section Title: 14–15px (600)
- Body Text: 13–14px (400)
- Form Label: 12–13px (500)
- Helper / Subtitle Text: 12px (400)
- Table Text: 13px (400)

4. LINE HEIGHTS
- Titles: 1.2
- Body & Labels: 1.4
- Helper / Subtitle Text: 1.5
- Line-height must never be below 1.4 for body text.

5. SIDEBAR TYPOGRAPHY
- Section Header:
  - 12px, 600, line-height 1.4
- Menu Item Label:
  - 13–14px, 500, line-height 1.4
- Menu Item Subtitle:
  - 12px, 400, line-height 1.5
- Label and subtitle MUST be aligned on the same left text axis.
- Label and subtitle MUST live in the same text container.
- Subtitle must start directly under the label text, not under icons.

6. FORMS (EMPLOYEE, MASTER FORMS)
- Section Title:
  - 14–15px, 600
- Field Label:
  - 12–13px, 500
- Input Text:
  - 13–14px, 400
- Helper / Error Text:
  - 12px, 400
- Inputs must NOT be bold.
- Helper text must NOT be smaller than 12px.

7. TABLES & NUMERIC DATA
- Table Header:
  - 12px, 600
- Table Cell Text:
  - 13px, 400
- Numeric columns must use tabular numerals.
- Enable:
  font-feature-settings: "tnum";
- Tables must feel visually quieter than forms.

8. SPACING & RHYTHM
- Maintain consistent vertical spacing between:
  - Label → Input
  - Label → Subtitle
- No arbitrary spacing per component.
- Typography rhythm must be consistent across modules.

9. ACCESSIBILITY & TONE
- Avoid overly light gray text for subtitles.
- No italics for helper text.
- Typography must remain readable for long working hours.

10. NON-NEGOTIABLE RULE
- Typography is token-driven, not component-driven.
- Any deviation must update the typography tokens first.


/* =========================================================
   OLIVINE TYPOGRAPHY DESIGN TOKENS (AUTHORITATIVE)
   ========================================================= */

/* ---------- CSS VARIABLES (GLOBAL) ---------- */
:root {
  /* Font Family */
  --font-family-primary: 'Inter', system-ui, -apple-system,
    BlinkMacSystemFont, 'Segoe UI', sans-serif;

  /* Font Weights */
  --font-weight-regular: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;

  /* Font Sizes */
  --font-size-page-title: 20px;
  --font-size-section-title: 14px;
  --font-size-body: 13px;
  --font-size-label: 12px;
  --font-size-helper: 12px;
  --font-size-table: 13px;

  /* Line Heights */
  --line-height-tight: 1.2;
  --line-height-normal: 1.4;
  --line-height-relaxed: 1.5;

  /* Letter Spacing */
  --letter-spacing-normal: 0;
}

/* ---------- GLOBAL BASE ---------- */
body {
  font-family: var(--font-family-primary);
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-normal);
}

/* ---------- SIDEBAR ---------- */
.sidebar-section-title {
  font-size: var(--font-size-label);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-normal);
}

.sidebar-item-label {
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-medium);
  line-height: var(--line-height-normal);
}

.sidebar-item-subtitle {
  font-size: var(--font-size-helper);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-relaxed);
}

/* ---------- FORMS ---------- */
.form-section-title {
  font-size: var(--font-size-section-title);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-tight);
}

.form-label {
  font-size: var(--font-size-label);
  font-weight: var(--font-weight-medium);
  line-height: var(--line-height-normal);
}

.form-input,
.form-select,
.form-textarea {
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-normal);
}

.form-helper-text,
.form-error-text {
  font-size: var(--font-size-helper);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-relaxed);
}

/* ---------- TABLES ---------- */
.table-header {
  font-size: var(--font-size-label);
  font-weight: var(--font-weight-semibold);
  line-height: var(--line-height-normal);
}

.table-cell {
  font-size: var(--font-size-table);
  font-weight: var(--font-weight-regular);
  line-height: var(--line-height-normal);
  font-feature-settings: "tnum";
}

/* =========================================================
   TYPESCRIPT TOKENS (for React / MUI / Design System)
   ========================================================= */

export const typographyTokens = {
  fontFamily: {
    primary:
      "'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
  },

  fontWeight: {
    regular: 400,
    medium: 500,
    semibold: 600,
  },

  fontSize: {
    pageTitle: "20px",
    sectionTitle: "14px",
    body: "13px",
    label: "12px",
    helper: "12px",
    table: "13px",
  },

  lineHeight: {
    tight: 1.2,
    normal: 1.4,
    relaxed: 1.5,
  },

  numeric: {
    fontFeatureSettings: "tnum",
  },
};

/* =========================================================
   NON-NEGOTIABLE RULE
   =========================================================
   - Components must consume these tokens.
   - No hardcoded font sizes, weights, or families.
   - Any typography change must update tokens first.
   ========================================================= */


================================================================================
FILE END: typography.md
================================================================================

