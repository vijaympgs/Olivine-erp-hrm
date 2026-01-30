import React from 'react';
import { PageContainer } from '../../../../olivine-app-core/src/ui/components/PageContainer';
import { useNavigate } from 'react-router-dom';

export const DashboardPage: React.FC = () => {
  const navigate = useNavigate();

  const moduleCards = [
    {
      title: 'Core Setup',
      bullets: ['Company, Locations, Attributes'],
      path: '/setup/company',
    },
    {
      title: 'Merchandise & Partners',
      bullets: ['Products, Customers, Suppliers'],
      path: '/setup/company',
    },
    {
      title: 'Operations',
      bullets: ['Procurement, Inventory, POS'],
      path: '/procurement',
    },
    {
      title: 'Finance & Reporting',
      bullets: ['Pricing, Sales, Analytics'],
      path: '/finance',
    },
    {
      title: 'Loyalty & CRM',
      bullets: ['Customer Engagement'],
      path: '/analytics',
    },
    {
      title: 'Platform & Integrations',
      bullets: ['API, Extensions, Modules'],
      path: '/admin',
    },
  ];

  const kpiCards = [
    { title: 'Total Sales (Today)', value: '$0', bgColor: 'bg-blue-500' },
    { title: 'Open Purchase Requisitions', value: '0', bgColor: 'bg-green-500' },
    { title: 'Low Stock Items', value: '0', bgColor: 'bg-yellow-500' },
    { title: 'Pending Supplier Payments', value: '0', bgColor: 'bg-red-500' },
  ];

  return (
    <PageContainer title="Dashboard">
      <div>
        <h1 className="text-3xl font-semibold">Dashboard</h1>
        <p className="text-gray-600">Overview of key Retail ERP operations.</p>
      </div>

      <section className="grid grid-cols-1 md:grid-cols-4 gap-4">
        {kpiCards.map((card) => (
          <div key={card.title} className={`${card.bgColor} p-4 rounded-lg text-white`}>
            <div className="text-sm font-medium">{card.title}</div>
            <div className="text-2xl font-bold">{card.value}</div>
          </div>
        ))}
      </section>

      <section className="mt-8 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        {moduleCards.map((module) => (
          <div key={module.title} className="bg-white rounded-lg shadow p-4">
            <h2 className="text-xl font-semibold mb-2">{module.title}</h2>
            <ul className="list-disc list-inside mb-4">
              {module.bullets.map((bullet, idx) => (
                <li key={idx}>{bullet}</li>
              ))}
            </ul>
            <button
              className="px-4 py-2 bg-emerald-600 text-white rounded hover:bg-emerald-700"
              onClick={() => navigate(module.path)}
            >
              Go to module
            </button>
          </div>
        ))}
      </section>

      <section className="mt-8 bg-white rounded-lg p-4">
        <h3 className="text-lg font-semibold mb-2">Activity & Tasks</h3>
        <div>Activity & Tasks stream (coming soon).</div>
      </section>
    </PageContainer>
  );
};

