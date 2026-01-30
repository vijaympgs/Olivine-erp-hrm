import React from 'react';
import { Card } from '@ui/Card';

const FinanceDashboardPage: React.FC = () => {
    return (
        <div className="p-6 space-y-6">
            <div className="flex justify-between items-center">
                <h1 className="text-2xl font-bold tracking-tight">Finance Dashboard</h1>
            </div>

            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
                <Card>
                    <div className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <h3 className="text-sm font-medium">Total Revenue</h3>
                    </div>
                    <div>
                        <div className="text-2xl font-bold">$0.00</div>
                        <p className="text-xs text-muted-foreground">+0% from last month</p>
                    </div>
                </Card>

                <Card>
                    <div className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <h3 className="text-sm font-medium">Expenses</h3>
                    </div>
                    <div>
                        <div className="text-2xl font-bold">$0.00</div>
                        <p className="text-xs text-muted-foreground">+0% from last month</p>
                    </div>
                </Card>

                <Card>
                    <div className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <h3 className="text-sm font-medium">Profit Margin</h3>
                    </div>
                    <div>
                        <div className="text-2xl font-bold">0%</div>
                        <p className="text-xs text-muted-foreground">+0% from last month</p>
                    </div>
                </Card>

                <Card>
                    <div className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <h3 className="text-sm font-medium">Pending Invoices</h3>
                    </div>
                    <div>
                        <div className="text-2xl font-bold">0</div>
                        <p className="text-xs text-muted-foreground">0 overdue</p>
                    </div>
                </Card>
            </div>

            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
                <Card className="col-span-4">
                    <div className="pt-2">
                        <h3 className="font-semibold leading-none tracking-tight">Cash Flow</h3>
                    </div>
                    <div className="pl-2 pt-4">
                        <div className="h-[200px] flex items-center justify-center text-muted-foreground">
                            Chart Placeholder
                        </div>
                    </div>
                </Card>
                <Card className="col-span-3">
                    <div className="pt-2">
                        <h3 className="font-semibold leading-none tracking-tight">Recent Transactions</h3>
                    </div>
                    <div className="pt-4">
                        <div className="h-[200px] flex items-center justify-center text-muted-foreground">
                            No recent transactions
                        </div>
                    </div>
                </Card>
            </div>
        </div>
    );
};

export default FinanceDashboardPage;
