import React, { useEffect, useState, Fragment } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { Button } from "@ui/Button";
import { Select } from "@ui/Select";

interface Employee {
  id: number;
  employee_id: string;
  first_name: string;
  last_name: string;
  photo_url?: string | null;
  email: string;
  phone_number: string | null;
  department: string | null;
  role: string | null;
  manager_name?: string | null;
  status: string;
  hire_date: string | null;
}

export const EmployeeListPage: React.FC = () => {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [search, setSearch] = useState('');
  const [filteredEmployees, setFilteredEmployees] = useState<Employee[]>([]);

  useEffect(() => {
    fetchEmployees();
  }, []);

  const fetchEmployees = async () => {
    try {
      const response = await axios.get('/api/hr/employees/');
      setEmployees(response.data);
      setFilteredEmployees(response.data);
    } catch (error) {
      console.error('Failed to fetch employees', error);
    }
  };

  const handleSearchChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const value = e.target.value;
    setSearch(value);
    const filtered = employees.filter(emp => {
      const fullName = emp.first_name + ' ' + emp.last_name;
      return (
        fullName.toLowerCase().includes(value.toLowerCase()) ||
        emp.employee_id.toLowerCase().includes(value.toLowerCase()) ||
        (emp.email && emp.email.toLowerCase().includes(value.toLowerCase()))
      );
    });
    setFilteredEmployees(filtered);
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm('Are you sure you want to delete this employee?')) return;
    try {
      await axios.delete(`/api/hr/employees/${id}/`);
      setEmployees(prev => prev.filter(emp => emp.id !== id));
      setFilteredEmployees(prev => prev.filter(emp => emp.id !== id));
    } catch (error) {
      alert('Failed to delete employee');
    }
  };

  return (
    <Fragment>
      <div className="page-container">
        <h1 className="text-2xl font-bold mb-6">Employee Management</h1>

        <div className="mb-4 flex items-center justify-between">
          <input
            type="text"
            placeholder="Search by name, employee ID, email..."
            value={search}
            onChange={handleSearchChange}
            className="rounded border border-gray-300 px-4 py-2 w-full max-w-md focus:outline-none focus:ring-2 focus:ring-olivine-accent"
          />
          <Link to="/hr/employees/create">
            <Button>Create New Employee</Button>
          </Link>
        </div>

        <div className="overflow-x-auto rounded border border-gray-300">
          <table className="min-w-full divide-y divide-gray-300">
            <thead className="bg-gray-100">
              <tr>
                <th scope="col" className="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider w-16">Photo</th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider w-28">Employee ID</th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Name</th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Role</th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Department</th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Email</th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Manager</th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Status</th>
                <th scope="col" className="px-4 py-3 text-left text-xs font-semibold text-gray-600 uppercase tracking-wider">Hire Date</th>
                <th scope="col" className="relative px-4 py-3 w-32">
                  <span className="sr-only">Actions</span>
                </th>
              </tr>
            </thead>
            <tbody className="bg-white divide-y divide-gray-200">
              {filteredEmployees.map(emp => (
                <tr key={emp.id} className="hover:bg-gray-50">
                  <td className="px-4 py-3 whitespace-nowrap">
                    {emp.photo_url ? (
                      <img
                        src={emp.photo_url}
                        alt={`${emp.first_name} ${emp.last_name}`}
                        className="h-10 w-10 rounded-full object-cover"
                      />
                    ) : (
                      <div className="h-10 w-10 rounded-full bg-gray-300 flex items-center justify-center text-gray-400">--</div>
                    )}
                  </td>
                  <td className="px-4 py-3 whitespace-nowrap text-sm font-medium text-gray-900">{emp.employee_id}</td>
                  <td className="px-4 py-3 whitespace-nowrap text-sm text-gray-700">{emp.first_name} {emp.last_name}</td>
                  <td className="px-4 py-3 whitespace-nowrap text-sm text-gray-700">{emp.role || '-'}</td>
                  <td className="px-4 py-3 whitespace-nowrap text-sm text-gray-700">{emp.department || '-'}</td>
                  <td className="px-4 py-3 whitespace-nowrap text-sm text-gray-700">{emp.email}</td>
                  <td className="px-4 py-3 whitespace-nowrap text-sm text-gray-700">
                    {emp.manager_name || '-'}
                  </td>
                  <td className="px-4 py-3 whitespace-nowrap">
                    <span
                      className={`inline-block rounded-full px-2 py-0.5 text-xs font-semibold uppercase ${emp.status === 'active' ? 'bg-green-100 text-green-800' :
                          emp.status === 'terminated' ? 'bg-red-100 text-red-800' :
                            emp.status === 'on_leave' ? 'bg-yellow-100 text-yellow-800' : ''
                        }`}
                    >
                      {emp.status.replace('_', ' ')}
                    </span>
                  </td>
                  <td className="px-4 py-3 whitespace-nowrap text-sm text-gray-700">{emp.hire_date || '-'}</td>
                  <td className="px-4 py-3 whitespace-nowrap text-right text-sm font-medium space-x-2">
                    <Link to={`/hr/employees/edit/${emp.id}`}>
                      <Button>Edit</Button>
                    </Link>
                    <Button variant="danger" onClick={() => handleDelete(emp.id)}>Delete</Button>
                  </td>
                </tr>
              ))}
              {filteredEmployees.length === 0 && (
                <tr>
                  <td colSpan={10} className="px-4 py-4 text-center text-sm text-gray-500">
                    No employees found.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </Fragment>
  );
};



