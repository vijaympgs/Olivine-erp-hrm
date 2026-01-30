# Command Button Audit Script
# Scans Retail pages for standalone command buttons

Write-Host "=== RETAIL COMMAND BUTTON AUDIT ===" -ForegroundColor Cyan
Write-Host ""

# Define button patterns to search for
$buttonPatterns = @(
    "Add New",
    "Create New",
    "\+ New",
    "Save",
    "Submit",
    "Cancel",
    "Delete",
    "Edit",
    "Update",
    "<button",
    "onClick.*Add",
    "onClick.*Create",
    "onClick.*Save",
    "onClick.*Submit",
    "onClick.*Delete",
    "onClick.*Edit"
)

# Directories to scan
$scanDirs = @(
    "frontend\apps\retail",
    "frontend\src\pages\sales",
    "frontend\src\pages\setup"
)

$results = @()

foreach ($dir in $scanDirs) {
    if (Test-Path $dir) {
        Write-Host "Scanning: $dir" -ForegroundColor Yellow
        
        Get-ChildItem -Path $dir -Recurse -Filter "*.tsx" | ForEach-Object {
            $file = $_
            $content = Get-Content $file.FullName -Raw
            
            # Skip if file contains MasterToolbar (likely already compliant)
            if ($content -match "MasterToolbar") {
                # Check if it ALSO has standalone buttons
                $hasStandaloneButtons = $false
                
                foreach ($pattern in $buttonPatterns) {
                    if ($content -match $pattern) {
                        # Check if it's not within MasterToolbar component
                        if ($content -match "(?<!MasterToolbar[^>]*>.*?)$pattern") {
                            $hasStandaloneButtons = $true
                            break
                        }
                    }
                }
                
                if (-not $hasStandaloneButtons) {
                    return # Skip this file, it's compliant
                }
            }
            
            # Check for button patterns
            foreach ($pattern in $buttonPatterns) {
                if ($content -match $pattern) {
                    $lineNumber = 0
                    $lines = Get-Content $file.FullName
                    
                    for ($i = 0; $i -lt $lines.Count; $i++) {
                        if ($lines[$i] -match $pattern) {
                            $results += [PSCustomObject]@{
                                File = $file.FullName.Replace((Get-Location).Path + "\", "")
                                Line = $i + 1
                                Pattern = $pattern
                                Context = $lines[$i].Trim()
                            }
                        }
                    }
                }
            }
        }
    }
}

# Display Results
Write-Host ""
Write-Host "=== FINDINGS ===" -ForegroundColor Cyan
Write-Host ""

if ($results.Count -eq 0) {
    Write-Host "✅ No standalone command buttons found!" -ForegroundColor Green
} else {
    Write-Host "Found $($results.Count) potential standalone buttons:" -ForegroundColor Yellow
    Write-Host ""
    
    $results | Group-Object File | ForEach-Object {
        Write-Host "📄 $($_.Name)" -ForegroundColor Yellow
        $_.Group | ForEach-Object {
            Write-Host "   Line $($_.Line): $($_.Pattern)" -ForegroundColor Gray
            Write-Host "   → $($_.Context.Substring(0, [Math]::Min(80, $_.Context.Length)))" -ForegroundColor DarkGray
        }
        Write-Host ""
    }
}

Write-Host ""
Write-Host "=== SUMMARY ===" -ForegroundColor Cyan
Write-Host "Total files scanned: $(($scanDirs | ForEach-Object { if (Test-Path $_) { (Get-ChildItem -Path $_ -Recurse -Filter '*.tsx').Count } else { 0 } } | Measure-Object -Sum).Sum)"
Write-Host "Files with potential issues: $($results | Select-Object -ExpandProperty File -Unique | Measure-Object | Select-Object -ExpandProperty Count)"
Write-Host "Total button instances: $($results.Count)"
