import React from 'react';
import { Card } from '@ui/Card';

const CRMDashboardPage: React.FC = () => {
    return (
        <div className="p-6 space-y-6">
            <div className="flex justify-between items-center">
                <h1 className="text-2xl font-bold tracking-tight">CRM Dashboard</h1>
            </div>

            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
                <Card>
                    <div className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <h3 className="text-sm font-medium">Total Leads</h3>
                    </div>
                    <div>
                        <div className="text-2xl font-bold">0</div>
                        <p className="text-xs text-muted-foreground">+0% from last month</p>
                    </div>
                </Card>

                <Card>
                    <div className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <h3 className="text-sm font-medium">Active Opportunities</h3>
                    </div>
                    <div>
                        <div className="text-2xl font-bold">0</div>
                        <p className="text-xs text-muted-foreground">+0% from last month</p>
                    </div>
                </Card>

                <Card>
                    <div className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <h3 className="text-sm font-medium">Conversion Rate</h3>
                    </div>
                    <div>
                        <div className="text-2xl font-bold">0%</div>
                        <p className="text-xs text-muted-foreground">+0% from last month</p>
                    </div>
                </Card>

                <Card>
                    <div className="flex flex-row items-center justify-between space-y-0 pb-2">
                        <h3 className="text-sm font-medium">Pipeline Value</h3>
                    </div>
                    <div>
                        <div className="text-2xl font-bold">$0.00</div>
                        <p className="text-xs text-muted-foreground">+0% from last month</p>
                    </div>
                </Card>
            </div>

            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
                <Card className="col-span-4">
                    <div className="pt-2">
                        <h3 className="font-semibold leading-none tracking-tight">Sales Overview</h3>
                    </div>
                    <div className="pl-2 pt-4">
                        <div className="h-[200px] flex items-center justify-center text-muted-foreground">
                            Chart Placeholder
                        </div>
                    </div>
                </Card>
                <Card className="col-span-3">
                    <div className="pt-2">
                        <h3 className="font-semibold leading-none tracking-tight">Recent Leads</h3>
                    </div>
                    <div className="pt-4">
                        <div className="h-[200px] flex items-center justify-center text-muted-foreground">
                            No recent leads
                        </div>
                    </div>
                </Card>
            </div>
        </div>
    );
};

export default CRMDashboardPage;
