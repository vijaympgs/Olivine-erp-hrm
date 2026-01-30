# UI Standardization Implementation Checklist

## Phase 1: Core Infrastructure ✅ COMPLETE

- [x] Extended `LayoutConfig` interface with modal settings
- [x] Extended `LayoutConfig` interface with typography hierarchy (L1-L4)
- [x] Added default values for all new settings
- [x] Updated `applyConfig()` to map settings to CSS variables
- [x] Created UI audit utility (`uiAudit.ts`)
- [x] Documented implementation plan
- [x] Created quick reference guide

## Phase 2: UI Components (TODO)

### BaseModal Component
- [ ] Create `frontend/core/ui-canon/frontend/ui/components/BaseModal.tsx`
- [ ] Implement props interface (title, children, onClose, size, etc.)
- [ ] Apply all modal CSS variables automatically
- [ ] Add keyboard support (ESC to close)
- [ ] Add click-outside-to-close functionality
- [ ] Ensure fits within `--modal-max-width`
- [ ] Export as default modal for all new components

### Typography Utility Classes
- [ ] Add utility classes to `globals.css` or create `typography.css`
- [ ] Define `.typography-l1`, `.typography-l2`, `.typography-l3`, `.typography-l4`
- [ ] Define `.form-label`, `.form-input`, `.form-helper`, `.form-error`
- [ ] Test in browser to verify CSS variables are applied
- [ ] Document usage in component library

## Phase 3: Layout Settings Page (TODO)

### Add UI Standards Section
- [ ] Create new accordion section "UI Standards" in `LayoutSettingsPage.tsx`
- [ ] Add Modal Settings subsection:
  - [ ] Max Width input
  - [ ] Background color picker
  - [ ] Border color picker
  - [ ] Border radius slider
  - [ ] Backdrop color picker with opacity
  - [ ] Shadow intensity dropdown
  - [ ] Padding input
- [ ] Add Typography Settings subsection:
  - [ ] L1 controls (size, weight, color)
  - [ ] L2 controls (size, weight, color)
  - [ ] L3 controls (size, weight, color)
  - [ ] L4 controls (size, weight, color)
  - [ ] Form-specific controls (label, input, helper, error)
- [ ] Add live preview panel showing all typography levels
- [ ] Update `handleSave()` to persist new settings
- [ ] Update `useEffect` to load new settings on mount

## Phase 4: Migrate Existing Components (TODO)

### Identify Components to Migrate
- [ ] Scan codebase for existing modals
- [ ] List all form components
- [ ] Prioritize by usage frequency

### Modal Migration
- [ ] Update `ProductLookupModal.tsx` to use BaseModal
- [ ] Update `SupplierLookupModal.tsx` to use BaseModal
- [ ] Update `CustomerLookupModal.tsx` to use BaseModal
- [ ] Update any other lookup modals
- [ ] Update confirmation dialogs
- [ ] Update settings modals
- [ ] Test each modal for:
  - [ ] Fits within workspace (90vw)
  - [ ] Applies correct backdrop
  - [ ] Uses centralized colors
  - [ ] Keyboard navigation works

### Form Migration
- [ ] Update `CustomerForm.tsx` to use L4 typography
- [ ] Update `SupplierForm.tsx` to use L4 typography
- [ ] Update `ItemForm.tsx` to use L4 typography
- [ ] Update `PurchaseOrderFormPage.tsx` to use L4 typography
- [ ] Update all other transaction forms
- [ ] Test each form for:
  - [ ] Labels use `--form-label-*` variables
  - [ ] Inputs use `--form-input-*` variables
  - [ ] Helpers use `--form-helper-*` variables
  - [ ] Errors use `--form-error-*` variables

## Phase 5: UI Audit & Reporting (TODO)

### Generate Retail Module Audit
- [ ] Run `downloadUIAuditReport('Retail')` from Test Console
- [ ] Review CSV output
- [ ] Identify all "Missing" items
- [ ] Identify all "Placeholder" items
- [ ] Create prioritized backlog for missing UIs

### Categorize Findings
- [ ] List all menu items with no route
- [ ] List all routes with placeholder components
- [ ] List all routes with incomplete components
- [ ] Estimate effort for each missing item
- [ ] Create implementation tickets

### Generate Reports for Other Modules
- [ ] Run audit for Finance module
- [ ] Run audit for CRM module
- [ ] Run audit for HRM module
- [ ] Consolidate into master report
- [ ] Share with stakeholders

## Phase 6: Documentation & Training (TODO)

### Developer Documentation
- [ ] Add section to component library docs
- [ ] Create video walkthrough of using BaseModal
- [ ] Create video walkthrough of using typography system
- [ ] Document common patterns and anti-patterns
- [ ] Add to onboarding materials

### User Documentation
- [ ] Document how to customize UI standards in Layout Settings
- [ ] Create screenshots of Layout Settings UI Standards section
- [ ] Explain impact of changing typography globally
- [ ] Add to admin user guide

## Phase 7: Testing & Validation (TODO)

### Visual Regression Testing
- [ ] Capture screenshots of all forms before migration
- [ ] Migrate components
- [ ] Capture screenshots after migration
- [ ] Compare for unintended changes
- [ ] Fix any regressions

### Functional Testing
- [ ] Test all modals open/close correctly
- [ ] Test keyboard navigation in modals
- [ ] Test form validation still works
- [ ] Test error messages display correctly
- [ ] Test responsive behavior on different screen sizes

### Performance Testing
- [ ] Measure CSS variable lookup performance
- [ ] Compare to hardcoded values
- [ ] Optimize if necessary

## Phase 8: Rollout (TODO)

### Staged Rollout
- [ ] Deploy to dev environment
- [ ] Test with dev team
- [ ] Deploy to staging environment
- [ ] Test with QA team
- [ ] Deploy to production
- [ ] Monitor for issues

### Communication
- [ ] Announce new system to dev team
- [ ] Share quick reference guide
- [ ] Conduct training session
- [ ] Set up office hours for questions

---

## Success Criteria

### Must Have:
- ✅ All CSS variables defined and mapped
- ✅ UI audit utility functional
- [ ] BaseModal component created and tested
- [ ] At least 5 existing modals migrated
- [ ] At least 5 existing forms migrated
- [ ] Layout Settings page updated with new controls
- [ ] Full Retail module audit completed

### Should Have:
- [ ] Typography utility classes created
- [ ] All lookup modals migrated to BaseModal
- [ ] All transaction forms using L4 typography
- [ ] Documentation complete
- [ ] Training materials created

### Nice to Have:
- [ ] Visual regression test suite
- [ ] Automated audit in CI/CD pipeline
- [ ] Live preview in Layout Settings
- [ ] Export/import of UI standards presets

---

## Timeline Estimate

| Phase | Estimated Time | Priority |
|-------|----------------|----------|
| Phase 1: Core Infrastructure | ✅ DONE | Critical |
| Phase 2: UI Components | 2-3 hours | Critical |
| Phase 3: Layout Settings Page | 2-3 hours | High |
| Phase 4: Migrate Components | 4-6 hours | High |
| Phase 5: UI Audit & Reporting | 1-2 hours | Medium |
| Phase 6: Documentation | 2-3 hours | Medium |
| Phase 7: Testing | 2-3 hours | High |
| Phase 8: Rollout | 1-2 hours | Critical |

**Total Estimated Time:** 14-22 hours (2-3 days)

---

## Notes

### Current Status (2026-01-05):
- Phase 1 is 100% complete
- All infrastructure is in place
- Ready to proceed with Phase 2

### Next Immediate Steps:
1. Create BaseModal component
2. Add UI Standards section to Layout Settings
3. Run Retail module audit
4. Begin migrating high-traffic modals

### Blockers:
- None currently

### Questions/Decisions Needed:
- Should we create a separate `typography.css` file or add to `globals.css`?
- Should BaseModal support different size presets (sm, md, lg, xl)?
- Should we auto-migrate components or do it manually?
- What's the priority order for component migration?

---

*Last Updated: 2026-01-05 22:57 IST*
*Status: Phase 1 Complete, Ready for Phase 2*
