"""
Unified Full Admin Registration for Olivine ERP
This file consolidates registrations for modules that do not have their own admin.py
or need specific unified registration (HRM, FMS, CRM).
"""

from django.contrib import admin

# HRM Imports
from HRM.backend.hrm.models import (
    # Employee Management
    EmployeeRecord, EmployeeAddress, EmployeeProfile, EmployeeSkill, EmployeeDocument, SkillCategory,
    # Organization
    Department, OrganizationalUnit, Position, EmployeePosition, Company as HRMCompany,
    ContractTemplate, ContractPosition, ContractOrganizationalUnit,
    # Performance
    RatingScale, RatingLevel, RatingDistribution, RatingGuideline, ReviewCycle, CalibrationSession,
    # Learning & Development
    Course, CourseContent, CourseSession, Instructor, CourseLearningPath,
    # Compensation & Payroll
    SalaryStructure, PayGrade, CompensationRange, JobLevel, MarketData,
    PayrollRun, PayrollCalculation, PayrollDisbursement, PayrollSchedule, EarningCode,
    # Recruitment
    JobPosting, JobApplication, ApplicationQuestion, ScreeningProcess, ScreeningCriteria,
    BackgroundCheck, BackgroundCheckProvider, ApplicationAnswer, ApplicationDocument,
    ApplicationCandidate, ScreeningTemplate, OfferLetter, OfferLetterTemplate, OfferPosition,
    # Time & Attendance
    TimeEntry, Shift, AttendancePolicy, AttendanceDevice, Timesheet, TimesheetEntry, TimesheetApproval, AttendanceException,
    # Badges
    Badge, BadgeAward, BadgeNomination, BadgeCategory, RecognitionFeed,
    # Tax
    TaxCalculation, TaxRate, TaxJurisdiction, TaxWithholding, TaxExemption, TaxPayrollRun,
    # Toolbar
    ERPToolbarControl, ERPMenuItem, Role, RolePermission, UserRole,
)

# FMS Imports
from FMS.backend.finance.models import AccountGroup, AccountLedger, JournalEntry, JournalItem

# CRM Imports
from CRM.backend.models.customer import Customer as CRMCustomer, Lead, Contact

# ============================================================================
# HRM REGISTRATIONS
# ============================================================================

@admin.register(EmployeeRecord)
class EmployeeRecordAdmin(admin.ModelAdmin):
    list_display = ['company_code', 'employee_number', 'first_name', 'last_name', 'employment_status']
    search_fields = ['employee_number', 'first_name', 'last_name']
    list_filter = ['employment_status']

@admin.register(EmployeeAddress)
class EmployeeAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'address_type', 'city', 'country']
    search_fields = ['employee__first_name', 'city']

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee']
    search_fields = ['employee__first_name']

@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'skill_name', 'proficiency_level']
    search_fields = ['employee__first_name', 'skill_name']

@admin.register(EmployeeDocument)
class EmployeeDocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'document_type', 'document_name']
    search_fields = ['employee__first_name', 'document_name']

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

@admin.register(OrganizationalUnit)
class OrganizationalUnitAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 'unit_type', 'is_active']
    search_fields = ['name', 'code']
    list_filter = ['unit_type', 'is_active']

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'position_code', 'job_grade', 'is_active']
    search_fields = ['title', 'position_code']
    list_filter = ['job_grade', 'is_active']

@admin.register(EmployeePosition)
class EmployeePositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'position', 'is_primary', 'status']
    search_fields = ['employee__first_name', 'position__title']

@admin.register(ContractTemplate)
class ContractTemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'template_name', 'template_code', 'status']
    search_fields = ['template_name']

@admin.register(RatingScale)
class RatingScaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'scale_name', 'scale_code', 'status']
    search_fields = ['scale_name']

@admin.register(RatingLevel)
class RatingLevelAdmin(admin.ModelAdmin):
    list_display = ['id', 'level_name', 'rating_scale', 'numeric_value']
    search_fields = ['level_name']

@admin.register(ReviewCycle)
class ReviewCycleAdmin(admin.ModelAdmin):
    list_display = ['id', 'cycle_name', 'start_date', 'end_date']
    search_fields = ['cycle_name']

@admin.register(CalibrationSession)
class CalibrationSessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'session_name', 'status']
    search_fields = ['session_name']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_name', 'course_code', 'course_type', 'status']
    search_fields = ['course_name', 'course_code']

@admin.register(CourseSession)
class CourseSessionAdmin(admin.ModelAdmin):
    list_display = ['id', 'session_name', 'course', 'status']
    search_fields = ['session_name']

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', 'instructor_name', 'is_active']
    search_fields = ['instructor_name']

@admin.register(SalaryStructure)
class SalaryStructureAdmin(admin.ModelAdmin):
    list_display = ['id', 'structure_type', 'status']
    search_fields = ['structure_type']

@admin.register(PayGrade)
class PayGradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'grade_code', 'grade_level']
    search_fields = ['grade_code']

@admin.register(PayrollRun)
class PayrollRunAdmin(admin.ModelAdmin):
    list_display = ['id', 'run_number', 'status']
    search_fields = ['run_number']

@admin.register(PayrollCalculation)
class PayrollCalculationAdmin(admin.ModelAdmin):
    list_display = ['id', 'payroll_run', 'employee']
    search_fields = ['employee__first_name']

@admin.register(EarningCode)
class EarningCodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'earning_type', 'is_taxable']
    search_fields = ['code']

@admin.register(TimeEntry)
class TimeEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'entry_date', 'status']
    search_fields = ['employee__first_name']

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['id', 'shift_name', 'start_time', 'end_time', 'is_active']
    search_fields = ['shift_name']

@admin.register(AttendancePolicy)
class AttendancePolicyAdmin(admin.ModelAdmin):
    list_display = ['id', 'policy_name', 'policy_type']
    search_fields = ['policy_name']

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ['id', 'timesheet_number', 'employee', 'status']
    search_fields = ['timesheet_number']

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['id', 'badge_code', 'badge_category', 'status']
    search_fields = ['badge_code']

@admin.register(BadgeAward)
class BadgeAwardAdmin(admin.ModelAdmin):
    list_display = ['id', 'badge', 'recipient_employee', 'status']
    search_fields = ['badge__badge_code']

@admin.register(BadgeCategory)
class BadgeCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_code']
    search_fields = ['category_code']

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'application_number', 'candidate', 'status']
    search_fields = ['application_number']

@admin.register(ApplicationCandidate)
class ApplicationCandidateAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']

@admin.register(OfferLetter)
class OfferLetterAdmin(admin.ModelAdmin):
    list_display = ['id', 'candidate', 'offer_status']
    search_fields = ['candidate__first_name']

@admin.register(TaxJurisdiction)
class TaxJurisdictionAdmin(admin.ModelAdmin):
    list_display = ['id', 'jurisdiction_name', 'jurisdiction_type', 'status']
    search_fields = ['jurisdiction_name']

@admin.register(TaxCalculation)
class TaxCalculationAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'tax_year', 'calculation_status']
    search_fields = ['employee__first_name']


# ============================================================================
# FMS REGISTRATIONS
# ============================================================================

@admin.register(AccountGroup)
class AccountGroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'nature', 'is_primary']
    list_filter = ['nature', 'is_primary']
    search_fields = ['name', 'code']

@admin.register(AccountLedger)
class AccountLedgerAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'group', 'current_balance', 'is_active']
    list_filter = ['group', 'is_active']
    search_fields = ['name', 'code']

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ['entry_number', 'date', 'status']
    list_filter = ['status', 'date']
    search_fields = ['entry_number', 'reference']

@admin.register(JournalItem)
class JournalItemAdmin(admin.ModelAdmin):
    list_display = ['entry', 'ledger', 'debit', 'credit']
    search_fields = ['entry__entry_number', 'ledger__name']


# ============================================================================
# CRM REGISTRATIONS
# ============================================================================

@admin.register(CRMCustomer)
class CRMCustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'company', 'status']
    list_filter = ['status']
    search_fields = ['first_name', 'last_name', 'email', 'company']

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ['title', 'customer', 'value', 'stage', 'probability']
    list_filter = ['stage']
    search_fields = ['title', 'customer__first_name']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['subject', 'customer', 'contact_type', 'contact_date']
    list_filter = ['contact_type', 'contact_date']
    search_fields = ['subject', 'customer__first_name']

print("Unified Full Admin models registered.")
