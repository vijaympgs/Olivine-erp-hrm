# Retail ERP Frontend

Modern React + TypeScript frontend for the Retail ERP Platform with enterprise-grade navigation and UI components.

## 🚀 Quick Start

```bash
npm install
npm run dev
```

The application will be available at `http://localhost:5173/`

## 🏗️ Architecture

- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS + Material-UI
- **Icons**: Lucide React (modern, consistent icons)
- **Routing**: React Router v6
- **Forms**: React Hook Form + Zod validation
- **HTTP Client**: Axios

## 📁 Project Structure

```
src/
├── app/                    # Application configuration
│   ├── layout.tsx         # Main app layout
│   ├── menuConfig.ts      # Sidebar navigation config
│   ├── providers.tsx      # Context providers
│   └── router.tsx         # Route definitions
├── auth/                  # Authentication logic
├── modules/               # Feature modules
│   ├── customers/         # Customer management
│   ├── inventory/         # Inventory management
│   ├── procurement/       # Purchase orders
│   └── ...               # Other business modules
├── pages/                 # Page components
├── ui/                    # Reusable UI components
│   └── components/        # Component library
└── utils/                 # Utility functions
```

## 🎨 Enterprise Sidebar Features

The sidebar includes comprehensive navigation similar to SAP, NetSuite, and other enterprise systems:

### **Core Business Modules**
- **Sales & Revenue**: POS, Orders, Quotes, Invoices, Returns, Pricing
- **Customer Management**: Directory, Groups, Loyalty, CRM, Analytics
- **Inventory Management**: Items, Stock, Movements, Adjustments, Transfers
- **Procurement**: Suppliers, Purchase Orders, Receiving, Vendor Bills
- **Financial Management**: Accounts, Ledger, AR/AP, Payments, Tax

### **Operations & Management**
- **Store Operations**: Locations, Terminals, Shifts, Cash Management
- **Human Resources**: Employees, Roles, Payroll, Attendance
- **Reports & Analytics**: Executive Dashboard, Sales, Inventory, Financial

### **Configuration & Administration**
- **System Configuration**: Company, Locations, Fiscal Periods, Currencies
- **Master Data**: Attributes, Categories, Brands, Units of Measure
- **Integrations**: API Management, Webhooks, Data Sync
- **System Administration**: Users, Security, Audit Logs, Backup

### **Sidebar Features**
- **Collapsible Design**: Toggle between full and icon-only view
- **Smart Expansion**: Remembers expanded/collapsed state
- **Active State Tracking**: Highlights current page and parent sections
- **Enterprise Styling**: Professional gradient design with proper spacing
- **Responsive**: Works on all screen sizes
- **Keyboard Navigation**: Full accessibility support

## 🔧 Development

### Adding New Menu Items

Edit `src/app/menuConfig.ts`:

```typescript
{
  id: 'new-module',
  label: 'New Module',
  icon: 'IconName', // From lucide-react
  children: [
    { 
      id: 'sub-item', 
      label: 'Sub Item', 
      path: '/new-module/sub-item',
      icon: 'SubIcon'
    }
  ]
}
```

### Available Icons

The sidebar uses [Lucide React](https://lucide.dev/) icons. Common enterprise icons:
- `LayoutDashboard`, `TrendingUp`, `Users`, `Package`
- `ShoppingBag`, `DollarSign`, `Store`, `BarChart3`
- `Settings`, `Database`, `Shield`, `Activity`

### Styling Guidelines

- Use Tailwind CSS classes for consistency
- Follow the existing color scheme (slate/blue/purple gradients)
- Maintain proper spacing and typography hierarchy
- Ensure accessibility with proper contrast ratios

## 🌐 API Integration

The frontend connects to the Django REST API at `http://localhost:8000/api/`

Configure the API base URL in `.env`:
```env
VITE_API_BASE_URL=http://localhost:8000/api
```

## 🧪 Testing

```bash
npm run lint        # ESLint checking
npm run build       # Production build
npm run preview     # Preview production build
```

## 📦 Deployment

The application builds to static files that can be served by any web server:

```bash
npm run build
# Files will be in dist/ directory
```

For Docker deployment, use the included `Dockerfile`.

## 🔐 Environment Variables

Create a `.env` file:

```env
VITE_API_BASE_URL=http://localhost:8000/api
VITE_APP_NAME=Retail ERP Platform
VITE_APP_VERSION=1.0.0
```

## 🎯 Next Steps

1. **Connect to Backend**: Implement API calls for each module
2. **Add Authentication**: Complete the auth flow with JWT tokens
3. **Build Forms**: Create data entry forms for each business entity
4. **Add Charts**: Implement dashboard analytics with Chart.js or similar
5. **Mobile Optimization**: Enhance responsive design for tablets/phones