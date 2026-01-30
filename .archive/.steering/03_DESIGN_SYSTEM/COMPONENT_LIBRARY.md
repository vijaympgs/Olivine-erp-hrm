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
