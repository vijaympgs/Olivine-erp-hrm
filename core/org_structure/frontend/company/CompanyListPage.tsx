import React, { useState } from "react";
import { useCompanies } from "./useCompanies";
import { Company, CompanyStatus, LegalEntityType } from "./company.types";
import { CompanyForm } from "./CompanyForm";

export const CompanyListPage: React.FC = () => {
  const { companies, loading, error, createCompany, updateCompany } = useCompanies();
  const [showForm, setShowForm] = useState(false);
  const [editCompany, setEditCompany] = useState<Company | null>(null);
  const [filterStatus, setFilterStatus] = useState<CompanyStatus | "">("");
  const [filterLegalEntityType, setFilterLegalEntityType] = useState<LegalEntityType | "">("");

  const filteredCompanies = companies.filter((c) => {
    if (filterStatus && c.status !== filterStatus) return false;
    if (filterLegalEntityType && c.legal_entity_type !== filterLegalEntityType) return false;
    return true;
  });

  const handleEdit = (company: Company) => {
    setEditCompany(company);
    setShowForm(true);
  };

  const handleAdd = () => {
    setEditCompany(null);
    setShowForm(true);
  };

  const handleSave = async (data: Omit<Company, "id">) => {
    try {
      if (editCompany) {
        // Prevent inactivation if last active
        if (
          editCompany.status === "Active" &&
          data.status === "Inactive" &&
          companies.filter((c) => c.status === "Active").length === 1
        ) {
          alert("At least one active company must exist.");
          return;
        }

        await updateCompany(editCompany.id, data);
      } else {
        await createCompany(data);
      }
      setShowForm(false);
      setEditCompany(null);
    } catch (e: any) {
      alert(e.message || "Failed to save company");
    }
  };

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-xl font-bold">Companies</h1>
        <button
          onClick={handleAdd}
          className="px-4 py-2 rounded bg-emerald-600 text-white hover:bg-emerald-700"
        >
          Add Company
        </button>
      </div>

      {/* Filters */}
      <div className="flex space-x-4 mb-4">
        <select
          value={filterStatus}
          onChange={(e) => setFilterStatus(e.target.value as CompanyStatus | "")}
          className="border border-gray-300 rounded px-2 py-1"
        >
          <option value="">All Statuses</option>
          <option value="Active">Active</option>
          <option value="Inactive">Inactive</option>
        </select>

        <select
          value={filterLegalEntityType}
          onChange={(e) =>
            setFilterLegalEntityType(e.target.value as LegalEntityType | "")
          }
          className="border border-gray-300 rounded px-2 py-1"
        >
          <option value="">All Legal Entity Types</option>
          {[
            "Sole Proprietor",
            "Partnership",
            "LLP",
            "Pvt Ltd",
            "Franchise",
          ].map((type) => (
            <option key={type} value={type}>
              {type}
            </option>
          ))}
        </select>
      </div>

      {loading && <p>Loading companies...</p>}
      {error && <p className="text-red-600">{error}</p>}

      <table className="w-full border border-gray-300 rounded-md">
        <thead className="bg-gray-100">
          <tr>
            <th className="border-b p-2 text-left">Code</th>
            <th className="border-b p-2 text-left">Name</th>
            <th className="border-b p-2 text-left">Legal Entity Type</th>
            <th className="border-b p-2 text-left">Default Currency</th>
            <th className="border-b p-2 text-left">Timezone</th>
            <th className="border-b p-2 text-left">Status</th>
            <th className="border-b p-2 text-left">Actions</th>
          </tr>
        </thead>
        <tbody>
          {filteredCompanies.map((company) => (
            <tr
              key={company.id}
              className="hover:bg-gray-50 cursor-pointer"
              onClick={() => handleEdit(company)}
            >
              <td className="border-b p-2">{company.company_code}</td>
              <td className="border-b p-2">{company.company_name}</td>
              <td className="border-b p-2">{company.legal_entity_type}</td>
              <td className="border-b p-2">{company.default_currency}</td>
              <td className="border-b p-2">{company.timezone}</td>
              <td className="border-b p-2">{company.status}</td>
              <td className="border-b p-2 text-center">
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    handleEdit(company);
                  }}
                  className="text-emerald-600 hover:underline"
                >
                  Edit
                </button>
              </td>
            </tr>
          ))}
          {filteredCompanies.length === 0 && (
            <tr>
              <td colSpan={7} className="p-4 text-center text-gray-500">
                No companies found.
              </td>
            </tr>
          )}
        </tbody>
      </table>

      {/* Modal for Create/Edit Form */}
      {showForm && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
          <div className="bg-white p-6 rounded shadow-lg w-full max-w-lg max-h-full overflow-auto">
            <h2 className="text-lg font-semibold mb-4">
              {editCompany ? "Edit Company" : "Add Company"}
            </h2>
            <CompanyForm
              initialData={editCompany || undefined}
              onCancel={() => setShowForm(false)}
              onSave={handleSave}
            />
          </div>
        </div>
      )}
    </div>
  );
};


