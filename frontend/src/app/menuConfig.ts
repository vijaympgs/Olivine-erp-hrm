export interface MenuItem {
  id: string;
  label: string;
  icon?: string;
  path?: string;
  badge?: string;
  children?: MenuItem[];
  disabled?: boolean;
  divider?: boolean;
  subtitle?: string;
  isPhase2?: boolean; // Flag to mark Phase 2 features
}

export const menuConfig: MenuItem[] = [
  {
    id: 'platform',
    label: 'Platform',
    subtitle: 'Core system and platform configuration',
    icon: 'Shield',
    children: [
      {
        id: 'administration',
        label: 'System Administration',
        subtitle: 'Configure and manage system settings',
        icon: 'Lock',
        children: [
          { id: 'user-management', label: 'User Management', path: '/admin/users', icon: 'UserCog', subtitle: 'Manage user accounts and roles' },
          { id: 'layout-settings', label: 'Layout Settings', path: '/admin/layout-settings', icon: 'Layout', subtitle: 'Configure layout and appearance' },
        ],
      },
      {
        id: 'system-tools',
        label: 'System Tools',
        subtitle: 'Platform utility and developer tools',
        icon: 'Tool',
        children: [
          { id: 'file-search', label: 'File Search Explorer', path: '/admin/file-search', icon: 'FileSearch', subtitle: 'Search within codebase' },
          { id: 'visual-extractor', label: 'Visual Extractor', path: '/system-tools/visual-extractor', icon: 'ScanText', subtitle: 'OCR image to markdown text' },
          { id: 'dataops-studio', label: 'DataOps Studio', path: '/system-tools/dataops-studio', icon: 'Database', subtitle: 'Database exploration & queries' },
          { id: 'html-preview', label: 'HTML Preview Tool', path: '/system-tools/html-preview', icon: 'Code', subtitle: 'Wireframe source inspector' },
        ]
      },
    ]
  },
  {
    id: 'hrm',
    label: 'Human Resources',
    subtitle: 'Manage employee lifecycle and payroll',
    icon: 'UserCog',
    children: [
      // 01. Dashboards & Reports
      {
        id: 'hr-dashboards',
        label: 'Dashboards & Reports',
        icon: 'LayoutDashboard',
        children: [
          { id: 'hr-dashboard', label: 'HR Dashboard', path: '/hr/dashboard', icon: 'LayoutDashboard', subtitle: 'HRM Dashboard' },
          { id: 'analytics-reports', label: 'Analytics Reports', path: '/hr/reports/analytics', icon: 'PieChart', subtitle: 'Analytics Reports' },
          { id: 'compliance-reports', label: 'Compliance Reports', path: '/hr/reports/compliance', icon: 'FileText', subtitle: 'Compliance Reports' },
          { id: 'custom-reports', label: 'Custom Reports', path: '/hr/reports/custom', icon: 'Settings', subtitle: 'Custom Reports' },
        ]
      },
      // 02. Employee Management
      {
        id: 'employee-mgmt',
        label: 'Employee Management',
        icon: 'Users',
        children: [
          { id: 'employee-records', label: 'Employee Records', path: '/hr/employees/records', icon: 'Database', subtitle: 'Employee Records' },
          { id: 'org-chart', label: 'Organizational Chart', path: '/hr/employees/org-chart', icon: 'Sitemap', subtitle: 'Organizational Chart' },
          { id: 'profile-view', label: 'Profile View', path: '/hr/employees/profile', icon: 'User', subtitle: 'Profile View' },
          { id: 'self-service', label: 'Employee Self Service', path: '/hr/employees/self-service', icon: 'UserCheck', subtitle: 'Employee Self Service' },
          { id: 'document-mgmt', label: 'Document Management', path: '/hr/employees/documents', icon: 'FileText', subtitle: 'Document Management' },
          { id: 'lifecycle', label: 'Employee Lifecycle', path: '/hr/employees/lifecycle', icon: 'TrendingUp', subtitle: 'Employee Lifecycle' },
        ]
      },
      // 03. Talent & Onboarding
      {
        id: 'talent-onboarding',
        label: 'Talent & Onboarding',
        icon: 'UserPlus',
        children: [
          { id: 'app-capture', label: 'Application Capture', path: '/hr/talent/applications', icon: 'FileInput', subtitle: 'Application Capture' },
          { id: 'screening', label: 'Screening', path: '/hr/talent/screening', icon: 'Filter', subtitle: 'Screening' },
          { id: 'interview-scheduling', label: 'Interview Scheduling', path: '/hr/talent/interviews', icon: 'Calendar', subtitle: 'Interview Scheduling' },
          { id: 'offer-mgmt', label: 'Offer Management', path: '/hr/talent/offers', icon: 'FileCheck', subtitle: 'Offer Management' },
          { id: 'new-hire', label: 'New Hire Setup', path: '/hr/talent/new-hire', icon: 'UserCheck', subtitle: 'New Hire Setup' },
        ]
      },
      // 04. Compensation & Payroll
      {
        id: 'comp-payroll',
        label: 'Compensation & Payroll',
        icon: 'DollarSign',
        children: [
          { id: 'salary-structures', label: 'Salary Structures', path: '/hr/payroll/structures', icon: 'List', subtitle: 'Salary Structures' },
          { id: 'tax-calc', label: 'Tax Calculations', path: '/hr/payroll/tax', icon: 'Calculator', subtitle: 'Tax Calculations' },
          { id: 'payroll-run', label: 'Payroll Run', path: '/hr/payroll/run', icon: 'Play', subtitle: 'Payroll Run' },
        ]
      },
      // 05. Time & Attendance
      {
        id: 'time-attendance',
        label: 'Time & Attendance',
        icon: 'Clock',
        children: [
          { id: 'clock-in-out', label: 'Clock-In/Out', path: '/hr/time/clock', icon: 'Watch', subtitle: 'Clock-In/Out' },
          { id: 'timesheets', label: 'Timesheets', path: '/hr/time/timesheets', icon: 'Calendar', subtitle: 'Timesheets' },
          { id: 'approval-workflow', label: 'Approval Workflow', path: '/hr/time/approvals', icon: 'CheckSquare', subtitle: 'Approval Workflow' },
        ]
      },
      // 06. Performance & Goals
      {
        id: 'perf-goals',
        label: 'Performance & Goals',
        icon: 'Target',
        children: [
          { id: 'goal-setting', label: 'Goal Setting', path: '/hr/performance/goals', icon: 'Flag', subtitle: 'Goal Setting' },
          { id: 'perf-reviews', label: 'Performance Reviews', path: '/hr/performance/reviews', icon: 'Star', subtitle: 'Performance Reviews' },
          { id: 'feedback-360', label: '360-Degree Feedback', path: '/hr/performance/feedback', icon: 'Users', subtitle: '360-Degree Feedback' },
          { id: 'dev-plans', label: 'Development Plans', path: '/hr/performance/development', icon: 'TrendingUp', subtitle: 'Development Plans' },
        ]
      },
      // 07. Learning
      {
        id: 'learning',
        label: 'Learning',
        icon: 'BookOpen',
        children: [
          { id: 'training-programs', label: 'Training Programs', path: '/hr/learning/programs', icon: 'MonitorPlay', subtitle: 'Training Programs' },
          { id: 'course-catalog', label: 'Course Catalog', path: '/hr/learning/catalog', icon: 'List', subtitle: 'Course Catalog' },
          { id: 'learning-paths', label: 'Learning Paths', path: '/hr/learning/paths', icon: 'Map', subtitle: 'Learning Paths' },
          { id: 'certifications', label: 'Certifications', path: '/hr/learning/certifications', icon: 'Award', subtitle: 'Certifications' },
        ]
      },
      // 08. Engagement
      {
        id: 'engagement',
        label: 'Engagement',
        icon: 'Heart',
        children: [
          { id: 'surveys', label: 'Surveys', path: '/hr/engagement/surveys', icon: 'MessageCircle', subtitle: 'Surveys' },
          { id: 'recognition', label: 'Recognition Programs', path: '/hr/engagement/recognition', icon: 'Medal', subtitle: 'Recognition Programs' },
          { id: 'wellness', label: 'Wellness Programs', path: '/hr/engagement/wellness', icon: 'Activity', subtitle: 'Wellness Programs' },
          { id: 'events', label: 'Events', path: '/hr/engagement/events', icon: 'CalendarHeart', subtitle: 'Events' },
        ]
      },
      // 09. Workforce Planning
      {
        id: 'workforce-planning',
        label: 'Workforce Planning',
        icon: 'Briefcase',
        children: [
          { id: 'headcount', label: 'Headcount Planning', path: '/hr/workforce/headcount', icon: 'Users', subtitle: 'Headcount Planning' },
          { id: 'succession', label: 'Succession Planning', path: '/hr/workforce/succession', icon: 'GitBranch', subtitle: 'Succession Planning' },
          { id: 'skills-gap', label: 'Skills Gap Analysis', path: '/hr/workforce/skills-gap', icon: 'BarChart2', subtitle: 'Skills Gap Analysis' },
          { id: 'wf-analytics', label: 'Workforce Analytics', path: '/hr/workforce/analytics', icon: 'PieChart', subtitle: 'Workforce Analytics' },
        ]
      },
      // 10. Compliance
      {
        id: 'hr-compliance',
        label: 'Compliance',
        icon: 'Shield',
        children: [
          { id: 'policy-mgmt', label: 'Policy Management', path: '/hr/compliance/policies', icon: 'Book', subtitle: 'Policy Management' },
          { id: 'compliance-training', label: 'Compliance Training', path: '/hr/compliance/training', icon: 'Monitor', subtitle: 'Compliance Training' },
          { id: 'audit-mgmt', label: 'Audit Management', path: '/hr/compliance/audit', icon: 'FileSearch', subtitle: 'Audit Management' },
          { id: 'compliance-reporting', label: 'Reporting', path: '/hr/compliance/reporting', icon: 'FileText', subtitle: 'Reporting' },
          { id: 'compliance-checklist', label: 'Compliance Checklist', path: '/hr/compliance/checklist', icon: 'CheckSquare', subtitle: 'Compliance Checklist' },
        ]
      },
      // 11. Offboarding
      {
        id: 'offboarding',
        label: 'Offboarding',
        icon: 'LogOut',
        children: [
          { id: 'resignation', label: 'Resignation Process', path: '/hr/offboarding/resignation', icon: 'FileMinus', subtitle: 'Resignation Process' },
          { id: 'exit-interviews', label: 'Exit Interviews', path: '/hr/offboarding/interviews', icon: 'MessageSquare', subtitle: 'Exit Interviews' },
          { id: 'asset-return', label: 'Asset Return', path: '/hr/offboarding/assets', icon: 'Box', subtitle: 'Asset Return' },
          { id: 'offboarding-checklist', label: 'Offboarding Checklist', path: '/hr/offboarding/checklist', icon: 'CheckSquare', subtitle: 'Offboarding Checklist' },
        ]
      },
      // 12. Security
      {
        id: 'hr-security',
        label: 'Security',
        icon: 'Lock',
        children: [
          { id: 'role-access', label: 'Role-Based Access', path: '/hr/security/roles', icon: 'ShieldCheck', subtitle: 'Role-Based Access' },
          { id: 'security-logs', label: 'Audit Logs', path: '/hr/security/logs', icon: 'List', subtitle: 'Audit Logs' },
        ]
      },
      // 13. Integrations
      {
        id: 'hr-integrations',
        label: 'Integrations',
        icon: 'Link',
        children: [
          { id: 'erp-connector', label: 'ERP Connector', path: '/hr/integrations/erp', icon: 'Server', subtitle: 'ERP Connector' },
          { id: 'payroll-integration', label: 'Payroll Integration', path: '/hr/integrations/payroll', icon: 'DollarSign', subtitle: 'Payroll Integration' },
          { id: 'background-check', label: 'Background Check', path: '/hr/integrations/background', icon: 'UserCheck', subtitle: 'Background Check' },
          { id: 'sso', label: 'Single Sign-On', path: '/hr/integrations/sso', icon: 'Key', subtitle: 'Single Sign-On' },
          { id: 'benefits-provider', label: 'Benefits Provider', path: '/hr/integrations/benefits', icon: 'Gift', subtitle: 'Benefits Provider' },
        ]
      },
      // 14. AI Assistant
      {
        id: 'ai-assistant',
        label: 'AI Assistant',
        icon: 'Bot',
        children: [
          { id: 'hr-chatbot', label: 'HR Chatbot', path: '/hr/ai/chatbot', icon: 'MessageCircle', subtitle: 'HR Chatbot' },
          { id: 'smart-recs', label: 'Smart Recommendations', path: '/hr/ai/recommendations', icon: 'Sparkles', subtitle: 'Smart Recommendations' },
        ]
      },
      // 15. Templates
      {
        id: 'hr-templates',
        label: 'Templates',
        icon: 'Copy',
        children: [
          { id: 'task-list', label: 'HRM TaskList', path: '/hr/templates/tasks', icon: 'CheckSquare', subtitle: 'HRM TaskList' },
          { id: 'doc-templates', label: 'Document Templates', path: '/hr/templates/documents', icon: 'File', subtitle: 'Document Templates' },
        ]
      },
    ]
  },
];
