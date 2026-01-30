import EmployeeFormStandalone from "@ui/employee/EmployeeFormStandalone";
import { useState } from "react";

const EmployeeMasterPage: React.FC = () => {
  const employeeData = {
    employee_code: 'EMP001',
    first_name: 'John',
    last_name: 'Doe',
    email: 'john.doe@example.com',
    status: 'active' as const,
  };
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = (data: FormData) => {
    console.log('Form submit:', data);
    setIsSubmitting(true);
    // Simulate API call
    setTimeout(() => {
      setIsSubmitting(false);
      console.log('Employee saved successfully');
    }, 1000);
  };

  const handleCancel = () => {
    console.log('Form cancel');
  };

  return (
    <div className="h-full">
      {/* Section C: Primary Workspace - Employee Form */}
      <EmployeeFormStandalone
        initialData={employeeData}
        onSubmit={handleSubmit}
        onCancel={handleCancel}
        isSubmitting={isSubmitting}
      />
    </div>
  );
};

export default EmployeeMasterPage;


