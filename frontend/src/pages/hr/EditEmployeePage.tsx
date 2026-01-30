import React, { useEffect, useState, ChangeEvent } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";
import { Button } from "@ui/Button";

interface EmployeeFormData {
  employee_id: string;
  first_name: string;
  last_name: string;
  email: string;
  phone_number: string;
  department: string;
  role: string;
  manager_id?: number;
  status: string;
  hire_date: string;
  photo_url?: string;
}

interface FormErrors {
  [key: string]: string;
}

export const EditEmployeePage: React.FC = () => {
  const navigate = useNavigate();
  const { id } = useParams<{ id: string }>();
  const [formData, setFormData] = useState<EmployeeFormData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [formErrors, setFormErrors] = useState<FormErrors>({});
  const [photo, setPhoto] = useState<File | null>(null);

  useEffect(() => {
    fetchEmployee();
  }, []);

  useEffect(() => {
    if (formData && formData.photo_url) {
      setPhoto(null); // Reset photo upload field if there's an existing photo
    }
  }, [formData]);

  const fetchEmployee = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`/api/hr/employees/${id}/`);
      setFormData({ ...response.data, manager_id: response.data.manager?.id });
    } catch (err: any) {
      setError('Failed to load employee data');
    } finally {
      setLoading(false);
    }
  };

  const validate = (): boolean => {
    if (!formData) return false;
    const errors: FormErrors = {};
    if (!formData.employee_id.trim()) {
      errors.employee_id = "Employee ID is required";
    }
    if (!formData.first_name.trim()) {
      errors.first_name = "First Name is required";
    }
    if (!formData.last_name.trim()) {
      errors.last_name = "Last Name is required";
    }
    if (!formData.email.trim()) {
      errors.email = "Email is required";
    } else if (!/^[\w-.]+@[\w-]+\.[a-z]{2,}$/i.test(formData.email)) {
      errors.email = "Invalid email address";
    }
    if (formData.phone_number && !/^\+?[\d\s-]{7,15}$/.test(formData.phone_number)) {
      errors.phone_number = "Invalid phone number";
    }
    if (!formData.hire_date) {
      errors.hire_date = "Hire Date is required";
    } else if (new Date(formData.hire_date) > new Date()) {
      errors.hire_date = "Hire Date cannot be in the future";
    }
    setFormErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => (prev ? { ...prev, [name]: value } : prev));
  };

  const handlePhotoChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setPhoto(e.target.files[0]);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!validate() || !formData) return;
    setError(null);
    setLoading(true);
    try {
      const formPayload = new FormData();
      Object.entries(formData).forEach(([key, value]) => {
        formPayload.append(key, value !== undefined && value !== null ? String(value) : '');
      });
      if (photo) {
        formPayload.append('photo', photo);
      }
      await axios.put(`/api/hr/employees/${id}/`, formPayload, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      navigate('/hr/employees');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to update employee');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="p-6">Loading...</div>;
  }

  if (error) {
    return <div className="p-6 text-red-600">{error}</div>;
  }

  if (!formData) {
    return <div className="p-6">No data to display.</div>;
  }

  return (
    <div className="p-6 max-w-3xl mx-auto">
      <h1 className="text-2xl font-bold mb-6">Edit Employee</h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="mb-4 flex items-center space-x-4">
          {formData?.photo_url ? (
            <img src={formData.photo_url} alt="Current" className="h-16 w-16 rounded-full object-cover" />
          ) : (
            <div className="h-16 w-16 rounded-full bg-gray-300 flex items-center justify-center text-gray-500">--</div>
          )}
          <div className="flex-grow">
            <label className="block mb-1 font-semibold">Photo</label>
            <input
              type="file"
              accept="image/*"
              onChange={handlePhotoChange}
              className="border border-gray-300 rounded px-3 py-1 w-full"
            />
          </div>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block mb-1 font-semibold">Employee ID</label>
            <input
              type="text"
              name="employee_id"
              value={formData.employee_id}
              onChange={handleChange}
              className={`w-full rounded border px-3 py-2 ${formErrors.employee_id ? 'border-red-500' : 'border-gray-300'}`}
              required
            />
            {formErrors.employee_id && <p className="mt-1 text-xs text-red-500">{formErrors.employee_id}</p>}
          </div>

          <div>
            <label className="block mb-1 font-semibold">First Name</label>
            <input
              type="text"
              name="first_name"
              value={formData.first_name}
              onChange={handleChange}
              className={`w-full rounded border px-3 py-2 ${formErrors.first_name ? 'border-red-500' : 'border-gray-300'}`}
              required
            />
            {formErrors.first_name && <p className="mt-1 text-xs text-red-500">{formErrors.first_name}</p>}
          </div>

          <div>
            <label className="block mb-1 font-semibold">Last Name</label>
            <input
              type="text"
              name="last_name"
              value={formData.last_name}
              onChange={handleChange}
              className={`w-full rounded border px-3 py-2 ${formErrors.last_name ? 'border-red-500' : 'border-gray-300'}`}
              required
            />
            {formErrors.last_name && <p className="mt-1 text-xs text-red-500">{formErrors.last_name}</p>}
          </div>

          <div>
            <label className="block mb-1 font-semibold">Email</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className={`w-full rounded border px-3 py-2 ${formErrors.email ? 'border-red-500' : 'border-gray-300'}`}
              required
            />
            {formErrors.email && <p className="mt-1 text-xs text-red-500">{formErrors.email}</p>}
          </div>
          <div>
            <label className="block mb-1 font-semibold">Phone Number</label>
            <input
              type="text"
              name="phone_number"
              value={formData.phone_number}
              onChange={handleChange}
              className={`w-full rounded border px-3 py-2 ${formErrors.phone_number ? 'border-red-500' : 'border-gray-300'}`}
            />
            {formErrors.phone_number && <p className="mt-1 text-xs text-red-500">{formErrors.phone_number}</p>}
          </div>

          <div>
            <label className="block mb-1 font-semibold">Department</label>
            <input
              type="text"
              name="department"
              value={formData.department}
              onChange={handleChange}
              className="w-full rounded border border-gray-300 px-3 py-2"
            />
          </div>

          <div>
            <label className="block mb-1 font-semibold">Role</label>
            <input
              type="text"
              name="role"
              value={formData.role}
              onChange={handleChange}
              className="w-full rounded border border-gray-300 px-3 py-2"
            />
          </div>

          <div>
            <label className="block mb-1 font-semibold">Status</label>
            <select
              name="status"
              value={formData.status}
              onChange={handleChange}
              className="w-full rounded border border-gray-300 px-3 py-2"
            >
              <option value="active">Active</option>
              <option value="terminated">Terminated</option>
              <option value="on_leave">On Leave</option>
            </select>
          </div>

          <div>
            <label className="block mb-1 font-semibold">Hire Date</label>
            <input
              type="date"
              name="hire_date"
              value={formData.hire_date}
              onChange={handleChange}
              className={`w-full rounded border px-3 py-2 ${formErrors.hire_date ? 'border-red-500' : 'border-gray-300'}`}
              required
            />
            {formErrors.hire_date && <p className="mt-1 text-xs text-red-500">{formErrors.hire_date}</p>}
          </div>
        </div>
        <div>
          <Button type="submit" disabled={loading} className="mt-4">
            {loading ? 'Updating...' : 'Update Employee'}
          </Button>
        </div>
      </form>
    </div>
  );
};



