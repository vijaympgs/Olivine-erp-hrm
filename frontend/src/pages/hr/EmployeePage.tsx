import React, { useEffect, useState } from "react";
import axios from "axios";
import EmployeeList from "@ui/employee/EmployeeList";
import EmployeeForm from "@ui/employee/EmployeeForm";
import { Button } from "@ui/Button";
import { toast } from "react-toastify";

export const EmployeePage: React.FC = () => {
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [selectedEmployeeId, setSelectedEmployeeId] = useState(null);
  const [editingEmployee, setEditingEmployee] = useState(null);
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    fetchEmployees();
  }, []);

  const fetchEmployees = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.get('/api/hr/employees/');
      setEmployees(response.data);
    } catch (err) {
      setError('Failed to load employees');
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = (id) => {
    const emp = employees.find(e => e.id === id) || null;
    setSelectedEmployeeId(id);
    setEditingEmployee(emp);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!window.confirm('Are you sure you want to delete this employee?')) return;
    try {
      await axios.delete(`/api/hr/employees/${id}/`);
      toast.success('Employee deleted successfully');
      fetchEmployees();
    } catch (error) {
      toast.error('Failed to delete employee');
    }
  };

  const handleFormSubmit = async (data) => {
    try {
      if (editingEmployee) {
        await axios.put(`/api/hr/employees/${editingEmployee.id}/`, data);
      } else {
        await axios.post('/api/hr/employees/', data);
      }
      toast.success('Employee saved successfully');
      setShowForm(false);
      setEditingEmployee(null);
      fetchEmployees();
    } catch (error) {
      toast.error('Failed to save employee');
    }
  };

  const handleFormCancel = () => {
    setShowForm(false);
    setEditingEmployee(null);
  };

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Employee Management</h1>
        {!showForm && <Button onClick={() => setShowForm(true)}>+ New Employee</Button>}
      </div>

      {error && <div className="mb-4 text-red-600">{error}</div>}

      {showForm ? (
        <EmployeeForm
          initialData={editingEmployee || undefined}
          onSubmit={handleFormSubmit}
          onCancel={handleFormCancel}
          isSubmitting={loading}
        />
      ) : (
        <EmployeeList
          employees={employees}
          loading={loading}
          onEdit={handleEdit}
          onDelete={handleDelete}
          selectedEmployeeId={selectedEmployeeId || undefined}
          onSelect={setSelectedEmployeeId}
        />
      )}
    </div>
  );
};

export default EmployeePage;


