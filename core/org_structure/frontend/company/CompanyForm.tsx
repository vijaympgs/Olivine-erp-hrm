import React, { useEffect } from "react";
import { useForm, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { Company, LegalEntityType, CompanyStatus } from "./company.types";
import { CompanySchema } from "./company.schema";
import slugify from "slugify";

interface CompanyFormProps {
  initialData?: Company;
  onCancel: () => void;
  onSave: (data: Omit<Company, "id">) => void;
}

export type CompanyFormData = Omit<Company, "id">;

const legalEntityOptions: LegalEntityType[] = ["Sole Proprietor", "Partnership", "LLP", "Pvt Ltd", "Franchise"];
const statusOptions: CompanyStatus[] = ["Active", "Inactive"];

export const CompanyForm: React.FC<CompanyFormProps> = ({ initialData, onCancel, onSave }) => {
  const {
    control,
    handleSubmit,
    watch,
    setValue,
    formState: { errors },
  } = useForm<CompanyFormData>({
    resolver: zodResolver(CompanySchema),
    mode: "onChange",
    defaultValues: initialData || {
      company_code: "",
      company_name: "",
      legal_entity_type: "Sole Proprietor",
      default_currency: "INR",
      timezone: "Asia/Kolkata",
      status: "Active",
      address: null,
    },
  });

  const companyName = watch("company_name");
  const companyCode = watch("company_code");

  // Auto-generate company_code from company_name if company_code is empty or matches previous auto value
  useEffect(() => {
    if (!companyCode || companyCode === slugify(companyName || "", { lower: true })) {
      const generated = slugify(companyName || "", { lower: true, strict: true }).slice(0, 20);
      setValue("company_code", generated);
    }
  }, [companyName, companyCode, setValue]);

  const onSubmit = (data: CompanyFormData) => {
    onSave(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <div>
        <label htmlFor="company_name" className="block text-sm font-medium text-gray-700">
          Company Name
        </label>
        <Controller
          name="company_name"
          control={control}
          render={({ field }) => (
            <input
              {...field}
              id="company_name"
              type="text"
              className={`mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500 sm:text-sm ${
                errors.company_name ? "border-red-500" : ""
              }`}
            />
          )}
        />
        {errors.company_name && (
          <p className="text-red-600 text-sm mt-1">{errors.company_name.message}</p>
        )}
      </div>

      <div>
        <label htmlFor="company_code" className="block text-sm font-medium text-gray-700">
          Company Code
        </label>
        <Controller
          name="company_code"
          control={control}
          render={({ field }) => (
            <input
              {...field}
              id="company_code"
              type="text"
              maxLength={20}
              className={`mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500 sm:text-sm ${
                errors.company_code ? "border-red-500" : ""
              }`}
            />
          )}
        />
        {errors.company_code && (
          <p className="text-red-600 text-sm mt-1">{errors.company_code.message}</p>
        )}
      </div>

      <div>
        <label htmlFor="legal_entity_type" className="block text-sm font-medium text-gray-700">
          Legal Entity Type
        </label>
        <Controller
          name="legal_entity_type"
          control={control}
          render={({ field }) => (
            <select
              {...field}
              id="legal_entity_type"
              className={`mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500 sm:text-sm ${
                errors.legal_entity_type ? "border-red-500" : ""
              }`}
            >
              {legalEntityOptions.map((o) => (
                <option key={o} value={o}>
                  {o}
                </option>
              ))}
            </select>
          )}
        />
        {errors.legal_entity_type && (
          <p className="text-red-600 text-sm mt-1">{errors.legal_entity_type.message}</p>
        )}
      </div>

      <div>
        <label htmlFor="default_currency" className="block text-sm font-medium text-gray-700">
          Default Currency
        </label>
        <Controller
          name="default_currency"
          control={control}
          render={({ field }) => (
            <input
              {...field}
              id="default_currency"
              type="text"
              maxLength={10}
              className={`mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500 sm:text-sm ${
                errors.default_currency ? "border-red-500" : ""
              }`}
            />
          )}
        />
        {errors.default_currency && (
          <p className="text-red-600 text-sm mt-1">{errors.default_currency.message}</p>
        )}
      </div>

      <div>
        <label htmlFor="timezone" className="block text-sm font-medium text-gray-700">
          Timezone
        </label>
        <Controller
          name="timezone"
          control={control}
          render={({ field }) => (
            <input
              {...field}
              id="timezone"
              type="text"
              maxLength={50}
              className={`mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500 sm:text-sm ${
                errors.timezone ? "border-red-500" : ""
              }`}
            />
          )}
        />
        {errors.timezone && <p className="text-red-600 text-sm mt-1">{errors.timezone.message}</p>}
      </div>

      <div>
        <label htmlFor="status" className="block text-sm font-medium text-gray-700">
          Status
        </label>
        <Controller
          name="status"
          control={control}
          render={({ field }) => (
            <select
              {...field}
              id="status"
              className={`mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500 sm:text-sm ${
                errors.status ? "border-red-500" : ""
              }`}
            >
              {statusOptions.map((o) => (
                <option key={o} value={o}>
                  {o}
                </option>
              ))}
            </select>
          )}
        />
        {errors.status && <p className="text-red-600 text-sm mt-1">{errors.status.message}</p>}
      </div>

      {/* Address could be a JSON editor or string for now - simplified as textarea */}
      <div>
        <label htmlFor="address" className="block text-sm font-medium text-gray-700">
          Address (JSON)
        </label>
        <Controller
          name="address"
          control={control}
          render={({ field }) => (
            <textarea
              {...field}
              id="address"
              rows={3}
              className="mt-1 block w-full rounded-md border border-gray-300 shadow-sm focus:border-emerald-500 focus:ring-emerald-500 sm:text-sm"
            />
          )}
        />
      </div>

      <div className="flex justify-end space-x-2 pt-2">
        <button
          type="button"
          onClick={onCancel}
          className="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400"
        >
          Cancel
        </button>
        <button
          type="submit"
          className="px-4 py-2 bg-emerald-600 text-white rounded hover:bg-emerald-700"
        >
          Save
        </button>
      </div>
    </form>
  );
};


