# Final UI Updates - Steps 5 & 6

## Step 5: Remove "Active Menu Item Styling" Section

**File**: `frontend/src/pages/admin/LayoutSettingsPage.tsx`

**Location**: Around lines 577-700 (look for the section starting with `{/* Active State Styling */}`)

**Action**: DELETE the entire section from:
```typescript
{/* Active State Styling */}
<div className="bg-white border border-gray-200 rounded-lg p-6">
```

Until the closing `</div>` of that section (before the next major section).

This will fix ALL remaining lint errors!

---

## Step 6: Add "AppHeader Settings" Section

**File**: `frontend/src/pages/admin/LayoutSettingsPage.tsx`

**Location**: After the "Sidebar Styling & Appearance" section (right after its closing `</div>`)

**Action**: ADD this complete section:

```typescript
                {/* AppHeader Settings */}
                <div className="bg-white border border-gray-200 rounded-lg p-6">
                    <h2 className="text-lg font-semibold text-gray-900 mb-4">
                        Application Header
                    </h2>
                    <p className="text-sm text-gray-500 mb-4">
                        Customize the application header appearance
                    </p>
                    
                    <div className="space-y-4">
                        {/* Header Background Style */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                Header Background Style
                            </label>
                            <select
                                value={settings.headerBgStyle}
                                onChange={(e) => handleChange('headerBgStyle', e.target.value as 'solid' | 'gradient')}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            >
                                <option value="solid">Solid Color</option>
                                <option value="gradient">Gradient</option>
                            </select>
                        </div>
                        
                        {/* Conditional Rendering Based on Style */}
                        {settings.headerBgStyle === 'solid' ? (
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    Background Color
                                </label>
                                <div className="flex space-x-2">
                                    <input
                                        type="color"
                                        value={settings.headerBgColor}
                                        onChange={(e) => handleChange('headerBgColor', e.target.value)}
                                        className="w-12 h-10 border border-gray-300 rounded cursor-pointer"
                                    />
                                    <input
                                        type="text"
                                        value={settings.headerBgColor}
                                        onChange={(e) => handleChange('headerBgColor', e.target.value)}
                                        className="flex-1 px-3 py-2 border border-gray-300 rounded-md text-sm font-mono"
                                        placeholder="#14162A"
                                    />
                                </div>
                            </div>
                        ) : (
                            <div className="space-y-3">
                                <div className="grid grid-cols-2 gap-4">
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 mb-2">
                                            Gradient Start Color
                                        </label>
                                        <input
                                            type="color"
                                            value={settings.headerGradientStart}
                                            onChange={(e) => handleChange('headerGradientStart', e.target.value)}
                                            className="w-full h-10 border border-gray-300 rounded cursor-pointer"
                                        />
                                    </div>
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 mb-2">
                                            Gradient End Color
                                        </label>
                                        <input
                                            type="color"
                                            value={settings.headerGradientEnd}
                                            onChange={(e) => handleChange('headerGradientEnd', e.target.value)}
                                            className="w-full h-10 border border-gray-300 rounded cursor-pointer"
                                        />
                                    </div>
                                </div>
                                <div className="grid grid-cols-2 gap-4">
                                    <input
                                        type="text"
                                        value={settings.headerGradientStart}
                                        onChange={(e) => handleChange('headerGradientStart', e.target.value)}
                                        className="px-3 py-2 border border-gray-300 rounded-md text-sm font-mono"
                                        placeholder="#14162A"
                                    />
                                    <input
                                        type="text"
                                        value={settings.headerGradientEnd}
                                        onChange={(e) => handleChange('headerGradientEnd', e.target.value)}
                                        className="px-3 py-2 border border-gray-300 rounded-md text-sm font-mono"
                                        placeholder="#101223"
                                    />
                                </div>
                            </div>
                        )}
                        
                        {/* Header Border Color */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                Header Border Color
                            </label>
                            <input
                                type="text"
                                value={settings.headerBorderColor}
                                onChange={(e) => handleChange('headerBorderColor', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm font-mono"
                                placeholder="rgba(255,255,255,0.06)"
                            />
                        </div>
                        
                        {/* Preview */}
                        <div className="mt-4 p-4 bg-gray-50 rounded-lg">
                            <p className="text-sm font-medium text-gray-700 mb-3">Preview:</p>
                            <div
                                className="h-16 rounded-md flex items-center px-4 border-b"
                                style={{
                                    background: settings.headerBgStyle === 'gradient'
                                        ? `linear-gradient(to bottom, ${settings.headerGradientStart}, ${settings.headerGradientEnd})`
                                        : settings.headerBgColor,
                                    borderBottomColor: settings.headerBorderColor,
                                }}
                            >
                                <span className="text-white font-semibold">Olivine</span>
                                <span className="text-gray-300 ml-2">Retail</span>
                            </div>
                        </div>
                    </div>
                </div>
```

---

## ✅ After Completion:

- ✅ All lint errors will be resolved
- ✅ No redundant sections
- ✅ New AppHeader customization available
- ✅ Clean, organized Layout Settings page

---

## 🎯 Quick Checklist:

- [ ] Step 5: Remove old "Active Menu Item Styling" section (~lines 577-700)
- [ ] Step 6: Add new "AppHeader Settings" section (after Sidebar Styling accordion)
- [ ] Save file
- [ ] Verify no lint errors
- [ ] Test the new AppHeader settings!

---

**You're almost done!** Just these 2 UI updates remaining! 🚀
