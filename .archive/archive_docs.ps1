
$source = "c:\00mindra\olivine-erp-platform"
$dest = "c:\00mindra\olivine-erp-platform\.archive"

if (-not (Test-Path $dest)) {
    New-Item -ItemType Directory -Force -Path $dest
}

# List of files to KEEP (Everything else goes)
$keep = @(
    "RETAIL_MODULE_COMPLETE.md",
    "TOOLBAR_IMPLEMENTATION_COMPLETE.md",
    "NEXT_SESSION.md",
    "viji-next-session.txt"
)

# Get all MD files in root
$files = Get-ChildItem -Path $source -Filter "*.md" -File

foreach ($file in $files) {
    if ($keep -notcontains $file.Name) {
        Move-Item -Path $file.FullName -Destination $dest -Force
        Write-Host "Archived: $($file.Name)"
    } else {
        Write-Host "Kept: $($file.Name)" -ForegroundColor Green
    }
}
