# Application Menu Structure - Complete Tree
**Last Updated**: 2025-12-28 10:06 IST  
**Updated By**: Astra (AI Agent)  
**Source**: `frontend/src/app/menuConfig.ts`

This document provides a complete hierarchical tree structure of all application menus.

---

## 📋 **COMPLETE MENU TREE**

```
🏪 OLIVINE RETAIL ERP PLATFORM
│
├── 🟥 Retail Now (/)
│   └── Industry news & trends
│
├── 🛡️ User & Permissions
│   └── 🔒 Permission Matrix (/admin/user-permissions)
│
├── ─────────────────────────────────────
│
├── 🏪 RETAIL - Core retail business management
│   │
│   ├── 📊 Retail Dashboard (/retail/dashboard)
│   ├── 🧪 Test Console (/test-console)
│   │
│   ├── 💳 Store Ops - POS operations and checkout
│   │   ├── Checkout (/operations/pos/pos)
│   │   ├── Daily Operations
│   │   │   ├── Day Open (/operations/pos/day-open)
│   │   │   ├── Shift Start (/operations/pos/session-open)
│   │   │   ├── Shift End (/operations/pos/session-close)
│   │   │   ├── Day Close (/operations/pos/day-close)
│   │   │   └── Reconciliation (/operations/pos/settlement)
│   │   └── Registers (/operations/pos/terminal-configuration)
│   │
│   ├── 📈 Sales - Manage sales orders and pricing
│   │   ├── Quotes & Estimates (/sales/quotes)
│   │   ├── Fulfillment (/sales/orders)
│   │   ├── Invoices (/sales/invoices)
│   │   ├── Returns & Refunds (/sales/returns)
│   │   └── Configuration (/sales/configuration)
│   │
│   ├── 🗄️ Merchandising - Product definition and pricing
│   │   ├── Catalog (/inventory/item-master)
│   │   ├── Code Masters (/setup/simple-masters)
│   │   ├── Variants (/inventory/attributes)
│   │   ├── Attribute Values (/inventory/attribute-values)
│   │   ├── Attribute Templates (/inventory/attribute-templates)
│   │   ├── Price Lists (/inventory/price-lists)
│   │   └── UOM (/inventory/uoms)
│   │
│   ├── 📦 Inventory - Manage stock and movements
│   │   ├── Stock on Hand - Current availability
│   │   │   ├── Overview (/inventory/levels)
│   │   │   ├── By Location (/inventory/levels?location=)
│   │   │   └── Low Stock (/inventory/levels/low_stock)
│   │   ├── Logistics - Replenishment and transfers
│   │   │   ├── Stock Flow (/inventory/movements)
│   │   │   ├── Internal Transfers (/inventory/transfers)
│   │   │   ├── Intercompany (/inventory/intercompany)
│   │   │   └── Reorder Policies (/inventory/reorder-policies)
│   │   └── Physical Inventory - Stock control
│   │       ├── Stock Take (/inventory/stock-takes)
│   │       └── Adjustments (/inventory/adjustments)
│   │
│   ├── 🛍️ Procurement - Purchasing and sourcing
│   │   ├── Vendors (/partners/suppliers)
│   │   ├── Requisitions (/procurement/requisitions)
│   │   ├── Requests for Quotation (/procurement/rfqs)
│   │   ├── Purchase Orders (/procurement/orders)
│   │   ├── ASNs (/procurement/asns)
│   │   ├── Goods Receipts (/procurement/receipts)
│   │   ├── Invoice Matching (/procurement/bills)
│   │   ├── Purchase Returns (/procurement/returns)
│   │   ├── Payments (/procurement/payments)
│   │   ├── Compliance (/procurement/compliance)
│   │   └── Configuration (/procurement/configuration)
│   │
│   └── 👥 Customers - Manage customer relations
│       ├── Directory (/partners/customers)
│       ├── Groups (/customers/groups)
│       └── Loyalty (/customers/loyalty)
│
├── 💰 FINANCIAL MANAGEMENT - Core accounting and financial operations
│   │
│   ├── 📊 Finance Dashboard - Financial overview and summaries
│   │   ├── Financial Overview (/finance/dashboard)
│   │   ├── Cash Flow Summary (/finance/cashflow-summary)
│   │   ├── Profit & Loss Summary (/finance/pl-summary)
│   │   ├── Balance Sheet Summary (/finance/bs-summary)
│   │   └── Financial Alerts (/finance/alerts)
│   │
│   ├── 📖 General Ledger - Chart of accounts and journals
│   │   ├── Chart of Accounts (/finance/coa)
│   │   ├── Account Groups (/finance/account-groups)
│   │   ├── Journal Entries (/finance/journal-entries)
│   │   ├── Recurring Journals (/finance/recurring-journals)
│   │   ├── Reversing Entries (/finance/reversing-entries)
│   │   ├── Trial Balance (/finance/trial-balance)
│   │   └── General Ledger (/finance/gl)
│   │
│   ├── 💳 Accounts Receivable - Customer invoicing and collections
│   │   ├── Customer Invoices (/finance/ar/invoices)
│   │   ├── Credit Notes (/finance/ar/credit-notes)
│   │   ├── Debit Notes (/finance/ar/debit-notes)
│   │   ├── Receipts (/finance/ar/receipts)
│   │   ├── Payment Allocation (/finance/ar/allocation)
│   │   ├── Customer Advances (/finance/ar/advances)
│   │   ├── Outstanding Receivables (/finance/ar/outstanding)
│   │   ├── Aging Analysis (/finance/ar/aging)
│   │   └── Write-offs (/finance/ar/writeoffs)
│   │
│   ├── 🧾 Accounts Payable - Vendor bills and payments
│   │   ├── Vendor Bills (/finance/ap/bills)
│   │   ├── Debit Notes (Returns) (/finance/ap/debit-notes)
│   │   ├── Credit Notes (/finance/ap/credit-notes)
│   │   ├── Payments (/finance/ap/payments)
│   │   ├── Vendor Advances (/finance/ap/advances)
│   │   ├── Outstanding Payables (/finance/ap/outstanding)
│   │   ├── Aging Analysis (/finance/ap/aging)
│   │   └── Expense Claims (/finance/ap/expense-claims)
│   │
│   ├── 🏛️ Cash & Bank - Cash and bank operations
│   │   ├── Bank Accounts (/finance/bank/accounts)
│   │   ├── Cash Accounts (/finance/bank/cash-accounts)
│   │   ├── Deposits & Withdrawals (/finance/bank/deposits)
│   │   ├── Bank Reconciliation (/finance/bank/reconciliation)
│   │   └── Cheque Management (/finance/bank/cheques)
│   │
│   ├── 💵 Payments - Payment configuration and processing
│   │   ├── Payment Methods (/finance/payments/methods)
│   │   ├── Payment Terms (/finance/payments/terms)
│   │   ├── Online Payments (/finance/payments/online)
│   │   ├── Refunds & Reversals (/finance/payments/refunds)
│   │   └── Payment Reconciliation (/finance/payments/reconciliation)
│   │
│   ├── 🔢 Tax Management - GST, TDS and statutory compliance
│   │   ├── Tax Configuration (/finance/tax/config)
│   │   ├── GST (Input / Output) (/finance/tax/gst)
│   │   ├── TDS / TCS (/finance/tax/tds-tcs)
│   │   ├── Tax Invoices (/finance/tax/invoices)
│   │   ├── Tax Returns (/finance/tax/returns)
│   │   ├── Tax Reconciliation (/finance/tax/reconciliation)
│   │   └── E-Invoicing / E-Way Bill (/finance/tax/einvoicing)
│   │
│   ├── 📈 Financial Reports - Statutory and accounting reports
│   │   ├── Balance Sheet (/finance/reports/balance-sheet)
│   │   ├── Profit & Loss (/finance/reports/pl)
│   │   ├── Cash Flow (/finance/reports/cashflow)
│   │   ├── Trial Balance (/finance/reports/trial-balance)
│   │   ├── Day Book (/finance/reports/day-book)
│   │   ├── Cash Book (/finance/reports/cash-book)
│   │   ├── Bank Book (/finance/reports/bank-book)
│   │   ├── Sales Register (/finance/reports/sales-register)
│   │   └── Purchase Register (/finance/reports/purchase-register)
│   │
│   └── 🔒 Period Closing - Month and year end controls
│       ├── Period Close (/finance/closing/period-close)
│       ├── Year Close (/finance/closing/year-close)
│       ├── Opening Balances (/finance/closing/opening-balances)
│       ├── Period Lock (/finance/closing/period-lock)
│       └── Audit Trail (/finance/closing/audit-trail)
│
├── 👥 CUSTOMER RELATIONSHIP MANAGEMENT (CRM) - Sales, marketing and customer service
│   │
│   ├── 📊 CRM Dashboard & Analytics - CRM metrics and insights
│   │   ├── CRM Dashboard (/crm/dashboard)
│   │   ├── Sales Pipeline Overview (/crm/pipeline-overview)
│   │   ├── Customer Health Score (/crm/health-score)
│   │   ├── Revenue Forecasting (/crm/revenue-forecast)
│   │   ├── Activity Metrics (/crm/activity-metrics)
│   │   ├── Team Performance (/crm/team-performance)
│   │   ├── Key Performance Indicators (/crm/kpis)
│   │   └── Real-time Alerts (/crm/alerts)
│   │
│   ├── ➕ Lead Management - Capture and qualify leads
│   │   ├── Lead Capture (/crm/leads/capture)
│   │   ├── Lead Import/Export (/crm/leads/import-export)
│   │   ├── Lead Qualification (/crm/leads/qualification)
│   │   ├── Lead Scoring (/crm/leads/scoring)
│   │   ├── Lead Assignment Rules (/crm/leads/assignment)
│   │   ├── Lead Routing (/crm/leads/routing)
│   │   ├── Lead Nurturing Campaigns (/crm/leads/nurturing)
│   │   ├── Lead Conversion (/crm/leads/conversion)
│   │   ├── Lead Source Tracking (/crm/leads/source-tracking)
│   │   ├── Duplicate Lead Management (/crm/leads/duplicates)
│   │   └── Lead Reports (/crm/leads/reports)
│   │
│   ├── 👤 Contact Management - Manage customer contacts
│   │   ├── Contact Directory (/crm/contacts)
│   │   ├── Contact Profiles (/crm/contacts/profiles)
│   │   ├── Contact Segmentation (/crm/contacts/segmentation)
│   │   ├── Contact Hierarchy (/crm/contacts/hierarchy)
│   │   ├── Contact Roles (/crm/contacts/roles)
│   │   ├── Contact Activities (/crm/contacts/activities)
│   │   ├── Contact Timeline (/crm/contacts/timeline)
│   │   ├── Contact Merge/Deduplication (/crm/contacts/merge)
│   │   ├── Contact Import/Export (/crm/contacts/import-export)
│   │   ├── Contact Enrichment (/crm/contacts/enrichment)
│   │   └── Social Media Integration (/crm/contacts/social)
│   │
│   ├── 🏢 Account Management - Manage customer accounts
│   │   ├── Account Directory (/crm/accounts)
│   │   ├── Account Profiles (/crm/accounts/profiles)
│   │   ├── Account Hierarchy (/crm/accounts/hierarchy)
│   │   ├── Parent-Child Accounts (/crm/accounts/parent-child)
│   │   ├── Account Teams (/crm/accounts/teams)
│   │   ├── Account Planning (/crm/accounts/planning)
│   │   ├── Account Health Score (/crm/accounts/health)
│   │   ├── Account Segmentation (/crm/accounts/segmentation)
│   │   ├── Territory Management (/crm/accounts/territory)
│   │   ├── Account Activities (/crm/accounts/activities)
│   │   └── Account Reports (/crm/accounts/reports)
│   │
│   ├── 🎯 Opportunity Management - Manage sales opportunities
│   │   ├── Opportunity Pipeline (/crm/opportunities/pipeline)
│   │   ├── Opportunity Stages (/crm/opportunities/stages)
│   │   ├── Opportunity Forecasting (/crm/opportunities/forecasting)
│   │   ├── Win/Loss Analysis (/crm/opportunities/win-loss)
│   │   ├── Opportunity Products (/crm/opportunities/products)
│   │   ├── Opportunity Teams (/crm/opportunities/teams)
│   │   ├── Opportunity Splits (/crm/opportunities/splits)
│   │   ├── Competitive Analysis (/crm/opportunities/competitive)
│   │   ├── Deal Registration (/crm/opportunities/deal-registration)
│   │   ├── Opportunity Reports (/crm/opportunities/reports)
│   │   └── Sales Methodology (/crm/opportunities/methodology)
│   │
│   ├── 📈 Sales Pipeline & Forecasting - Pipeline and revenue forecasting
│   │   ├── Pipeline Management (/crm/pipeline/management)
│   │   ├── Sales Stages (/crm/pipeline/stages)
│   │   ├── Pipeline Analytics (/crm/pipeline/analytics)
│   │   ├── Forecast Categories (/crm/pipeline/forecast-categories)
│   │   ├── Quota Management (/crm/pipeline/quota)
│   │   ├── Territory Planning (/crm/pipeline/territory)
│   │   ├── Sales Forecasting (/crm/pipeline/forecasting)
│   │   ├── Pipeline Velocity (/crm/pipeline/velocity)
│   │   ├── Conversion Rates (/crm/pipeline/conversion)
│   │   ├── Revenue Projections (/crm/pipeline/projections)
│   │   └── What-if Scenarios (/crm/pipeline/whatif)
│   │
│   ├── 📄 Quote & Proposal Management - CPQ and proposals
│   │   ├── Quote Generation (/crm/quotes/generate)
│   │   ├── Quote Templates (/crm/quotes/templates)
│   │   ├── Product Catalog (/crm/quotes/catalog)
│   │   ├── Price Books (/crm/quotes/price-books)
│   │   ├── Discount Management (/crm/quotes/discounts)
│   │   ├── Quote Approval Workflow (/crm/quotes/approval)
│   │   ├── Quote Versioning (/crm/quotes/versioning)
│   │   ├── E-signature Integration (/crm/quotes/esignature)
│   │   ├── Quote Analytics (/crm/quotes/analytics)
│   │   └── CPQ (Configure, Price, Quote) (/crm/quotes/cpq)
│   │
│   ├── 📣 Campaign Management - Marketing campaigns
│   │   ├── Campaign Planning (/crm/campaigns/planning)
│   │   ├── Campaign Execution (/crm/campaigns/execution)
│   │   ├── Campaign Tracking (/crm/campaigns/tracking)
│   │   ├── Campaign ROI (/crm/campaigns/roi)
│   │   ├── Target Lists (/crm/campaigns/target-lists)
│   │   ├── Campaign Members (/crm/campaigns/members)
│   │   ├── Multi-channel Campaigns (/crm/campaigns/multichannel)
│   │   ├── Campaign Automation (/crm/campaigns/automation)
│   │   ├── A/B Testing (/crm/campaigns/ab-testing)
│   │   ├── Campaign Reports (/crm/campaigns/reports)
│   │   └── Marketing Attribution (/crm/campaigns/attribution)
│   │
│   ├── 📧 Email Marketing & Automation - Email campaigns and automation
│   │   ├── Email Templates (/crm/email/templates)
│   │   ├── Email Campaigns (/crm/email/campaigns)
│   │   ├── Email Sequences (/crm/email/sequences)
│   │   ├── Drip Campaigns (/crm/email/drip)
│   │   ├── Email Tracking (/crm/email/tracking)
│   │   ├── Email Analytics (/crm/email/analytics)
│   │   ├── Unsubscribe Management (/crm/email/unsubscribe)
│   │   ├── Email Deliverability (/crm/email/deliverability)
│   │   ├── Marketing Automation (/crm/email/automation)
│   │   ├── Workflow Automation (/crm/email/workflows)
│   │   └── Trigger-based Emails (/crm/email/triggers)
│   │
│   ├── 🎧 Customer Service & Support - Support and service management
│   │   ├── Case Management (/crm/service/cases)
│   │   ├── Ticket System (/crm/service/tickets)
│   │   ├── Service Level Agreements (SLA) (/crm/service/sla)
│   │   ├── Case Routing (/crm/service/routing)
│   │   ├── Case Escalation (/crm/service/escalation)
│   │   ├── Knowledge Base (/crm/service/knowledge)
│   │   ├── Self-service Portal (/crm/service/portal)
│   │   ├── Live Chat (/crm/service/chat)
│   │   ├── Chatbot Integration (/crm/service/chatbot)
│   │   ├── Service Analytics (/crm/service/analytics)
│   │   └── Customer Satisfaction (CSAT) (/crm/service/csat)
│   │
│   ├── 💬 Customer Engagement & Communication - Multi-channel engagement
│   │   ├── Activity Timeline (/crm/engagement/timeline)
│   │   ├── Email Integration (/crm/engagement/email)
│   │   ├── Calendar Integration (/crm/engagement/calendar)
│   │   ├── Task Management (/crm/engagement/tasks)
│   │   ├── Meeting Scheduler (/crm/engagement/meetings)
│   │   ├── Call Logging (/crm/engagement/calls)
│   │   ├── SMS Integration (/crm/engagement/sms)
│   │   ├── WhatsApp Integration (/crm/engagement/whatsapp)
│   │   ├── Social Media Engagement (/crm/engagement/social)
│   │   ├── Communication History (/crm/engagement/history)
│   │   └── Engagement Scoring (/crm/engagement/scoring)
│   │
│   ├── 🏆 Customer Loyalty & Retention - Loyalty programs and retention
│   │   ├── Loyalty Programs (/crm/loyalty/programs)
│   │   ├── Points Management (/crm/loyalty/points)
│   │   ├── Rewards Catalog (/crm/loyalty/rewards)
│   │   ├── Tier Management (/crm/loyalty/tiers)
│   │   ├── Member Portal (/crm/loyalty/portal)
│   │   ├── Redemption Management (/crm/loyalty/redemption)
│   │   ├── Loyalty Analytics (/crm/loyalty/analytics)
│   │   ├── Churn Prediction (/crm/loyalty/churn)
│   │   ├── Win-back Campaigns (/crm/loyalty/winback)
│   │   └── Customer Lifetime Value (CLV) (/crm/loyalty/clv)
│   │
│   ├── 🤝 Partner & Channel Management - Partner and reseller management
│   │   ├── Partner Portal (/crm/partners/portal)
│   │   ├── Partner Onboarding (/crm/partners/onboarding)
│   │   ├── Partner Performance (/crm/partners/performance)
│   │   ├── Deal Registration (/crm/partners/deals)
│   │   ├── Partner Incentives (/crm/partners/incentives)
│   │   ├── Co-marketing Programs (/crm/partners/comarketing)
│   │   ├── Partner Training (/crm/partners/training)
│   │   ├── Partner Resources (/crm/partners/resources)
│   │   ├── Partner Analytics (/crm/partners/analytics)
│   │   └── Channel Conflict Resolution (/crm/partners/conflict)
│   │
│   ├── 💼 Sales Enablement - Sales tools and resources
│   │   ├── Sales Content Library (/crm/enablement/library)
│   │   ├── Sales Playbooks (/crm/enablement/playbooks)
│   │   ├── Competitive Intelligence (/crm/enablement/competitive)
│   │   ├── Product Training (/crm/enablement/training)
│   │   ├── Sales Scripts (/crm/enablement/scripts)
│   │   ├── Objection Handling (/crm/enablement/objections)
│   │   ├── Best Practices (/crm/enablement/best-practices)
│   │   ├── Sales Tools (/crm/enablement/tools)
│   │   ├── Mobile Sales App (/crm/enablement/mobile)
│   │   └── Offline Access (/crm/enablement/offline)
│   │
│   ├── 📈 Analytics & Reporting - CRM analytics and insights
│   │   ├── Sales Analytics - Sales performance metrics
│   │   │   ├── Sales Performance Reports (/crm/analytics/sales-performance)
│   │   │   ├── Win/Loss Analysis (/crm/analytics/win-loss)
│   │   │   ├── Sales Cycle Analysis (/crm/analytics/sales-cycle)
│   │   │   ├── Revenue Reports (/crm/analytics/revenue)
│   │   │   ├── Activity Reports (/crm/analytics/activity)
│   │   │   └── Leaderboards (/crm/analytics/leaderboards)
│   │   ├── Customer Analytics - Customer insights
│   │   │   ├── Customer Segmentation (/crm/analytics/segmentation)
│   │   │   ├── Customer Behavior Analysis (/crm/analytics/behavior)
│   │   │   ├── Customer Journey Analytics (/crm/analytics/journey)
│   │   │   ├── Churn Analysis (/crm/analytics/churn)
│   │   │   ├── Customer Profitability (/crm/analytics/profitability)
│   │   │   └── RFM Analysis (/crm/analytics/rfm)
│   │   ├── Marketing Analytics - Marketing performance
│   │   │   ├── Campaign Performance (/crm/analytics/campaign-performance)
│   │   │   ├── Lead Source ROI (/crm/analytics/lead-source)
│   │   │   ├── Marketing Attribution (/crm/analytics/attribution)
│   │   │   ├── Conversion Funnel (/crm/analytics/funnel)
│   │   │   ├── Email Performance (/crm/analytics/email-performance)
│   │   │   └── Social Media Analytics (/crm/analytics/social)
│   │   └── Custom Reports - Build custom reports
│   │       ├── Report Builder (/crm/analytics/builder)
│   │       ├── Dashboard Designer (/crm/analytics/designer)
│   │       ├── Scheduled Reports (/crm/analytics/scheduled)
│   │       └── Export to Excel/PDF (/crm/analytics/export)
│   │
│   ├── ⚡ Workflow & Automation - Automate CRM processes
│   │   ├── Workflow Rules (/crm/automation/rules)
│   │   ├── Process Builder (/crm/automation/process)
│   │   ├── Approval Processes (/crm/automation/approvals)
│   │   ├── Assignment Rules (/crm/automation/assignment)
│   │   ├── Auto-response Rules (/crm/automation/autoresponse)
│   │   ├── Escalation Rules (/crm/automation/escalation)
│   │   ├── Field Updates (/crm/automation/field-updates)
│   │   ├── Email Alerts (/crm/automation/email-alerts)
│   │   ├── Task Creation (/crm/automation/tasks)
│   │   ├── Record Updates (/crm/automation/records)
│   │   └── Time-based Actions (/crm/automation/timebased)
│   │
│   ├── 🔗 Integration & Data Management - Connect and manage data
│   │   ├── Email Integration (Gmail, Outlook) (/crm/integration/email)
│   │   ├── Calendar Sync (/crm/integration/calendar)
│   │   ├── Social Media Integration (/crm/integration/social)
│   │   ├── Telephony Integration (CTI) (/crm/integration/telephony)
│   │   ├── Marketing Automation Integration (/crm/integration/marketing)
│   │   ├── E-commerce Integration (/crm/integration/ecommerce)
│   │   ├── Accounting Integration (/crm/integration/accounting)
│   │   ├── Data Import/Export (/crm/integration/data)
│   │   ├── API Management (/crm/integration/api)
│   │   ├── Webhook Configuration (/crm/integration/webhooks)
│   │   ├── Third-party Apps (/crm/integration/apps)
│   │   └── AppExchange/Marketplace (/crm/integration/marketplace)
│   │
│   └── ⚙️ CRM Configuration & Administration - CRM setup and administration
│       ├── User Management (/crm/config/users)
│       ├── Roles & Permissions (/crm/config/roles)
│       ├── Profiles & Permission Sets (/crm/config/profiles)
│       ├── Sharing Rules (/crm/config/sharing)
│       ├── Field-level Security (/crm/config/field-security)
│       ├── Page Layouts (/crm/config/layouts)
│       ├── Record Types (/crm/config/record-types)
│       ├── Validation Rules (/crm/config/validation)
│       ├── Custom Fields (/crm/config/fields)
│       ├── Custom Objects (/crm/config/objects)
│       ├── Picklist Management (/crm/config/picklists)
│       ├── Email Templates (/crm/config/email-templates)
│       ├── System Settings (/crm/config/settings)
│       ├── Audit Trail (/crm/config/audit)
│       └── Data Backup & Recovery (/crm/config/backup)
│
├── 👥 HUMAN RESOURCES - Manage employee lifecycle and payroll
│   │
│   ├── 📈 HR Dashboard (/hr/dashboard)
│   │
│   ├── 👥 Employee Management - Employee records and services
│   │   ├── Employee Directory (/hr/employees)
│   │   ├── Organizational Chart (/hr/org-chart)
│   │   ├── Employee Self-Service (/hr/self-service)
│   │   ├── Document Management (/hr/documents)
│   │   └── Employee Lifecycle (/hr/lifecycle)
│   │
│   ├── 🏆 Talent Acquisition - Hiring pipeline
│   │   ├── Job Requisitions (/hr/jobs)
│   │   ├── Candidate Management (/hr/candidates)
│   │   ├── Interview Scheduling (/hr/interviews)
│   │   ├── Offer Management (/hr/offers)
│   │   └── Onboarding (/hr/onboarding)
│   │
│   ├── 💰 Compensation & Payroll - Salaries, benefits and payroll
│   │   ├── Payroll Processing (/hr/payroll)
│   │   ├── Salary Structures (/hr/salary-structures)
│   │   ├── Benefits Administration (/hr/benefits)
│   │   ├── Bonus & Incentives (/hr/bonuses)
│   │   ├── Taxation & Compliance (/hr/tax)
│   │   └── Statutory Filings (/hr/statutory)
│   │
│   ├── ⏰ Time & Attendance - Scheduling and attendance
│   │   ├── Clock-In/Out (/hr/time/clock)
│   │   ├── Attendance Tracking (/hr/time/attendance)
│   │   ├── Leave & Absence (/hr/time/leave)
│   │   ├── Shift Scheduling (/hr/time/shifts)
│   │   └── Overtime Management (/hr/time/overtime)
│   │
│   ├── 🏆 Performance Management - Goals, reviews and growth
│   │   ├── Goal Setting (/hr/performance/goals)
│   │   ├── Appraisals & Feedback (/hr/performance/appraisals)
│   │   ├── Calibration & Ranking (/hr/performance/calibration)
│   │   ├── Succession Planning (/hr/performance/succession)
│   │   └── 360 Degree Reviews (/hr/performance/360)
│   │
│   ├── 📖 Learning & Development - Training and competencies
│   │   ├── Training Catalog (/hr/learning/catalog)
│   │   ├── Course Management (/hr/learning/courses)
│   │   ├── Certifications & Compliance (/hr/learning/certifications)
│   │   ├── Skill & Competency Management (/hr/learning/skills)
│   │   └── Learning Paths & Career Dev (/hr/learning/paths)
│   │
│   ├── 💬 Employee Engagement & Recognition - Surveys, rewards and collaboration
│   │   ├── Surveys & Feedback (/hr/engagement/surveys)
│   │   ├── Rewards & Recognition (/hr/engagement/rewards)
│   │   └── Social Collaboration (/hr/engagement/social)
│   │
│   ├── 🥧 Workforce Planning & Analytics - Headcount and analytics
│   │   ├── Headcount Planning (/hr/workforce/headcount)
│   │   ├── Attrition & Retention (/hr/workforce/attrition)
│   │   ├── Diversity & Inclusion (/hr/workforce/diversity)
│   │   └── Workforce Costs (/hr/workforce/costs)
│   │
│   ├── 🔒 Compliance & Policies - Policies, compliance and incidents
│   │   ├── Labor Law Compliance (/hr/compliance/labor-law)
│   │   ├── Company Policies (/hr/compliance/policies)
│   │   ├── Grievance Management (/hr/compliance/grievances)
│   │   └── Incident Tracking (/hr/compliance/incidents)
│   │
│   ├── 🚪 Offboarding & Exit Management - Resignations and exits
│   │   ├── Resignation Processing (/hr/offboarding/resignation)
│   │   ├── Exit Interviews (/hr/offboarding/exit-interviews)
│   │   ├── Knowledge Transfer (/hr/offboarding/knowledge-transfer)
│   │   └── Final Settlement (/hr/offboarding/final-settlement)
│   │
│   ├── 📈 HR Reports & Analytics - HR reports and dashboards
│   │   ├── Standard Reports (/hr/reports/standard)
│   │   ├── Custom Reports (/hr/reports/custom)
│   │   ├── Dashboards & Visualizations (/hr/reports/dashboards)
│   │   └── Data Export & Integration (/hr/reports/export)
│   │
│   ├── 🛡️ Access & Security - Roles, SSO and audits
│   │   ├── Roles & Permissions (/hr/roles)
│   │   ├── Security Policies (/hr/security)
│   │   ├── Audit Logs (/hr/audit)
│   │   └── SSO Configuration (/hr/sso)
│   │
│   └── ⚙️ Integrations & Configuration - Integrations and settings
│       ├── Third-Party Integrations (/hr/integrations/third-party)
│       ├── System Settings (/hr/integrations/system)
│       ├── API Management (/hr/integrations/api)
│       └── Data Privacy & Security (/hr/integrations/privacy)
│
├── ─────────────────────────────────────
│
├── ⚡ PHASE 2 - ADVANCED FEATURES - Enterprise capabilities for FMS, HRM & CRM
│   │
│   ├── 💰 Financial Management (Phase 2) - Advanced financial features
│   │   ├── Multi-Currency & FX (/finance/phase2/multi-currency)
│   │   ├── Inter-company & Consolidation (/finance/phase2/consolidation)
│   │   ├── Fixed Assets Management (/finance/phase2/fixed-assets)
│   │   ├── Budgeting & Planning (/finance/phase2/budgeting)
│   │   ├── Treasury Management (/finance/phase2/treasury)
│   │   ├── Revenue Recognition (/finance/phase2/revenue-recognition)
│   │   ├── Cost Accounting & Job Costing (/finance/phase2/cost-accounting)
│   │   └── Period-End & Year-End Closing (/finance/phase2/period-close)
│   │
│   ├── 👥 Human Resources (Phase 2) - Advanced HR capabilities
│   │   ├── Performance Management (/hr/phase2/performance)
│   │   ├── Learning & Development (/hr/phase2/learning)
│   │   ├── Succession Planning (/hr/phase2/succession)
│   │   ├── Employee Engagement (/hr/phase2/engagement)
│   │   ├── Workforce Analytics (/hr/phase2/analytics)
│   │   └── Compliance & Policies (/hr/phase2/compliance)
│   │
│   └── 🤝 CRM (Phase 2) - Advanced CRM features
│       ├── CPQ (Configure, Price, Quote) (/crm/phase2/cpq)
│       ├── Marketing Automation (/crm/phase2/marketing-automation)
│       ├── Customer Service & Support (/crm/phase2/service)
│       ├── Loyalty & Retention (/crm/phase2/loyalty)
│       ├── Partner & Channel Management (/crm/phase2/partners)
│       ├── Sales Enablement (/crm/phase2/sales-enablement)
│       └── Advanced Analytics (/crm/phase2/analytics)
│
├── ─────────────────────────────────────
│
├── 🛡️ SYSTEM ADMINISTRATION - Configure and manage system settings
│   ├── 👥 User Management (/admin/users)
│   ├── 📐 Layout Settings (/admin/layout-settings)
│   ├── 🔒 Security Settings (/admin/security)
│   ├── Audit Logs (/admin/audit)
│   └── 💾 Backup & Recovery (/admin/backup)
│
└── ⚙️ SYSTEM CONFIGURATION - Setup company and system settings
    ├── 🏢 Company Settings (/setup/company)
    ├── 📍 Location Setup (/setup/locations)
    ├── 📅 Fiscal Periods (/setup/fiscal)
    ├── 🪙 Currencies & Exchange (/setup/currencies)
    └── 🔢 Tax Configuration (/setup/tax)
```

---

## 📊 **MENU STATISTICS**

### **Module Summary**
- **Retail Operations**: 6 subgroups, 50+ menu items
- **Financial Management**: 9 subgroups, 60+ menu items
- **CRM**: 18 subgroups, 180+ menu items
- **Human Resources**: 12 subgroups, 70+ menu items
- **Phase 2 Features**: 3 modules, 20+ advanced features
- **System Admin**: 2 modules, 10+ configuration items

### **Total Count**
- **Main Modules**: 4 (Retail, Finance, CRM, HR)
- **Subgroups**: 45+
- **Total Menu Items**: 370+
- **Depth Levels**: Up to 4 levels deep

---

## 🎯 **INSPIRATION SOURCES**

This menu structure is inspired by:
- **Tally ERP**: Comprehensive accounting and inventory
- **NetSuite**: Enterprise resource planning
- **SAP Business One**: Integrated business management
- **Salesforce**: CRM excellence
- **HubSpot**: Marketing automation
- **Microsoft Dynamics 365**: Complete business solution

---

**Last Updated**: 2025-12-28 10:06 IST  
**Maintained By**: Astra (AI Agent) & Viji (Product Owner)  
**Source File**: `frontend/src/app/menuConfig.ts`
