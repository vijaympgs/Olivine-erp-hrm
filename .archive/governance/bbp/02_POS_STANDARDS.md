# POS Standards - Development & Documentation Guidelines

**Created:** 01-Nov-2025 14:50:24 IST  
**Last Updated:** 08-Nov-2025 22:30:00 IST  
**Purpose:** Standards for documentation, UI, development, and file naming

---

## 📝 Documentation Standards

### **Date & Time Format:**
**Format:** `dd-MMM-yyyy HH:mm:ss IST`

**Example:**
```markdown
**Created:** 01-Nov-2025 14:49:00 IST  
**Last Updated:** 01-Nov-2025 14:49:00 IST
```

**PowerShell Command (IST):**
```powershell
[System.TimeZoneInfo]::ConvertTimeBySystemTimeZoneId([System.DateTime]::UtcNow, 'India Standard Time').ToString('dd-MMM-yyyy HH:mm:ss')
```

### **Document Headers:**
Every document MUST have:
```markdown
**Created:** dd-MMM-yyyy HH:mm:ss IST  
**Last Updated:** dd-MMM-yyyy HH:mm:ss IST  
**Purpose:** [Brief description]
```

---

## 🎨 UI Standards

### **Border Radius (Corner Styling)**
**CRITICAL:** All new forms and UI components MUST use **NO rounded corners**.

- **Forms:** `borderRadius: 0`
- **Dialogs:** `borderRadius: 0`
- **Cards:** `borderRadius: 0`
- **Papers:** `borderRadius: 0`
- **Buttons:** `borderRadius: 0` (unless button design specifically requires it)
- **Input Fields:** `'& .MuiOutlinedInput-root': { borderRadius: 0 }`

**Example:**
```javascript
<Paper sx={{ borderRadius: 0 }}>
  {/* Content */}
</Paper>

<Dialog
  PaperProps={{
    sx: { borderRadius: 0 }
  }}
>
  {/* Dialog content */}
</Dialog>

<TextField
  sx={{
    '& .MuiOutlinedInput-root': { borderRadius: 0 }
  }}
/>
```

### **Form Layout (Scroll-Free Canvas)**
- Master & transactional forms **must occupy the primary working canvas without vertical scrollbars**.
- Reserve scrollbars only for reports or history pages.
- Trim padding/margins on embedded forms (e.g., workflow steps) so content fits within the header–status bar window.
- Prefer condensed layouts (`showHeader={false}`, reduced helper text) when reusing forms inside workflows.

### **Primary Working Canvas Strip**
- The base content area below the header and above the status bar is the **Primary Working Canvas Strip**; it must use the same soft gray gradient as our workflow canvas.
- Avoid pure white gaps above the status bar; either extend the page background or provide a purpose-built footer/identifier.

### **POS Screen Polish Checklist**
- **Theme & Canvas:** Apply the shared off-white/grey working canvas, reuse `PageTitle`, and honor theme palette tokens for accents.
- **Header & Actions:** Keep header height consistent, align icons/subtitles, and right-justify action buttons with identical sizing and gaps.
- **Grid & Layout:** Cap content width at 1200–1400px, maintain equal gutters, stretch cards to balanced heights, and remove stray borders/dividers.
- **Rails & Timelines:** Ensure left rails reach the status bar, step tiles share padding/typography, and condensed variants do not clip content.
- **Status / Recap Strips:** Standardize recap chips (expected vs counted, variance, interim counts) and keep status bars visible except within POS Billing.
- **Forms & Controls:** Normalize control heights, helper text spacing, disabled and error colors; default to `size="medium"` unless condensed mode is required.
- **Responsive & Overflow:** Verify breakpoints to avoid sideways scroll; confirm mobile layouts stack cleanly.
- **Keyboard & Shortcuts:** Surface shortcut cues (e.g., `Ctrl+F4`) using consistent helper-text styling.
- **Footer Strip:** Keep the global status bar present (excluding POS Billing) and aligned with surrounding layout.

### **Lookup Pattern (Item/Customer Lookup Standard)**
All lookup dialogs MUST follow the same pattern as Item and Customer lookup:

#### **Dialog Structure:**
```javascript
<Dialog 
  open={open} 
  onClose={handleClose} 
  maxWidth="sm" 
  fullWidth
  PaperProps={{
    sx: { borderRadius: 0 }
  }}
>
  <DialogTitle sx={{ bgcolor: themeColor, color: 'white' }}>
    <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
        <Icon /> {/* Optional: Relevant icon */}
        <Typography variant="h6" fontWeight="bold">
          Select [Entity Name]
        </Typography>
      </Box>
      <Button
        variant="contained"
        size="small"
        startIcon={<AddIcon />}
        onClick={handleNew}
        sx={{ borderRadius: 0 }}
      >
        New
      </Button>
    </Box>
  </DialogTitle>

  <DialogContent sx={{ p: 2 }}>
    {/* Search Field - Always at top */}
    <TextField
      fullWidth
      placeholder="Search by name, code, or identifier..."
      value={searchTerm}
      onChange={(e) => setSearchTerm(e.target.value)}
      InputProps={{
        startAdornment: (
          <InputAdornment position="start">
            <SearchIcon />
          </InputAdornment>
        ),
      }}
      sx={{ 
        mb: 2,
        '& .MuiOutlinedInput-root': { borderRadius: 0 }
      }}
      autoFocus
    />

    {/* Results List */}
    {loading ? (
      <Box sx={{ display: 'flex', justifyContent: 'center', p: 4 }}>
        <CircularProgress />
      </Box>
    ) : items.length === 0 ? (
      <Box sx={{ textAlign: 'center', py: 4 }}>
        <Typography color="text.secondary">
          {searchTerm ? 'No items found' : 'Start typing to search'}
        </Typography>
      </Box>
    ) : (
      <List sx={{ maxHeight: 400, overflow: 'auto' }}>
        {items.map((item) => (
          <ListItem
            key={item.id}
            button
            onClick={() => handleSelect(item)}
            sx={{
              border: 1,
              borderColor: 'divider',
              borderRadius: 0, // NO rounded corners
              mb: 1,
              '&:hover': {
                bgcolor: 'action.hover',
              },
            }}
          >
            <ListItemText
              primary={<Typography variant="subtitle1" fontWeight="bold">{item.name}</Typography>}
              secondary={/* Additional info */}
            />
          </ListItem>
        ))}
      </List>
    )}
  </DialogContent>

  <DialogActions sx={{ p: 2, borderTop: 1, borderColor: 'divider' }}>
    <Button onClick={handleClose} sx={{ borderRadius: 0 }}>Cancel</Button>
  </DialogActions>
</Dialog>
```

#### **Lookup Requirements:**
1. **Dialog Position:** Centered on screen
2. **Size:** `maxWidth="sm"` with `fullWidth` prop
3. **Title Bar:** Theme color background, white text, "New" button on right
4. **Search Field:** Always at top of DialogContent, with search icon
5. **Auto-focus:** Search field should have `autoFocus`
6. **Results:** Scrollable list (maxHeight: 400px)
7. **List Items:** No rounded corners (`borderRadius: 0`)
8. **Empty State:** Show helpful message when no results
9. **Loading State:** Show CircularProgress while loading

### **Master Screen Pattern**
Based on: `NEXT-SESSION/08_MASTER_SCREEN_UI_PATTERN.md`

#### **Card Header:**
- Text: "List" (except multi-master forms)
- Background: `themeColor` (no gradient)
- Text color: White
- Border radius: 0

#### **Theme Loading:**
```javascript
const [themeColor, setThemeColor] = useState('#1976d2');

useEffect(() => {
  api.get('/theme/active-theme/')
    .then(res => setThemeColor(res.data.primary_color))
    .catch(() => {/* fallback */});
}, []);
```

#### **Form Dialog:**
- Title: `themeColor` background, white text, NO icons
- Content: `p: 1`, max-height scrollable
- Grid: `spacing={1}`
- First field: `mt: 1` (line space)
- **Border radius: 0** (CRITICAL)

#### **Status Toggle:**
- Color: Theme color (NOT blue)
- Label: "Active" text included
- Alignment: Same `mt` for same-row fields

#### **Table Headers:**
- Background: Theme color
- Text: White
- Border radius: 0

---

## 🖥️ Functional Checklist (All Screens)

### **Master/Transaction/Preference/Report Screens:**

#### **Loading States:**
- [ ] Loading skeleton/spinner
- [ ] Error handling with user-friendly messages
- [ ] Empty state handling

#### **Validation:**
- [ ] Client-side validation
- [ ] Server-side validation feedback
- [ ] Required field indicators
- [ ] Format validation (email, phone, etc.)

#### **Actions:**
- [ ] Create/Add button visible and functional
- [ ] Edit action updates existing record
- [ ] Delete with confirmation
- [ ] Save/Cancel buttons clear

#### **Notifications:**
- [ ] Success message (pale green)
- [ ] Error message (pale red)
- [ ] Positioned next to sidebar start
- [ ] Auto-dismiss after timeout

#### **Status Bar:**
- [ ] Always visible as footer
- [ ] Light grey background
- [ ] 3D borders on separators
- [ ] 4 sections: Message, User, System, Connection

---

## 📁 File Naming Conventions

### **Markdown Files:**
- **Format:** `NN_PURPOSE_DESCRIPTION.md`
- **NN:** Sequence number (00-99)
- **Examples:**
  - `00_POS_BBP.md` - Main blueprint
  - `01_POS_TRACKER.md` - Tracker
  - `02_POS_STANDARDS.md` - This file
  - `03_POS_CICD.md` - CICD log
  - `04_POS_OTHER_REFERENCES.md` - References

### **Code Files:**
- **Components:** `PascalCase` (e.g., `DayOpenPage.jsx`)
- **Services:** `camelCase` (e.g., `posService.js`)
- **Models:** `PascalCase` (e.g., `DayOpen`)
- **ViewSets:** `PascalCaseViewSet` (e.g., `DayOpenViewSet`)

---

## 🔧 Development Standards

### **Backend (Django):**
1. **Models:** UUID primary keys, proper ForeignKeys, indexes
2. **Serializers:** Proper validation, read_only fields
3. **ViewSets:** Consistent filtering, pagination, permissions
4. **URLs:** RESTful routing, proper basename

### **Frontend (React):**
1. **Components:** Functional with hooks, proper state management
2. **Services:** Centralized API calls, consistent error handling
3. **Routing:** Consistent paths, proper guards
4. **Styles:** Material-UI theme-based, responsive

---

## 📊 Status Indicators

### **Symbols:**
- ✅ Complete
- ⏳ Pending
- 🔄 In Progress
- ❌ Blocked
- ⚠️ Warning

### **Progress Format:**
```
**Progress:** XX% Complete
- Backend: XX%
- Frontend: XX%
- Integration: XX%
```

---

## 🎯 Checklist Template

```markdown
## Implementation Checklist

### Backend:
- [ ] Model created
- [ ] Migrations applied
- [ ] Serializer complete
- [ ] ViewSet with actions
- [ ] URLs registered
- [ ] Admin configured

### Frontend:
- [ ] Page component created
- [ ] Routing configured
- [ ] Service methods
- [ ] API integration
- [ ] Validation
- [ ] Error handling

### Testing:
- [ ] CRUD operations
- [ ] Validation rules
- [ ] Error cases
- [ ] Permissions
```

---

## 🔍 Code Review Checklist

### **Backend:**
- [ ] No hardcoded values
- [ ] Proper error handling
- [ ] Query optimization (select_related, prefetch_related)
- [ ] Proper indexes
- [ ] Validations in serializer

### **Frontend:**
- [ ] No console logs in production
- [ ] Proper state management
- [ ] Loading states
- [ ] Error boundaries
- [ ] Responsive design

---

This document is the reference for all POS-related development standards.

