
$source = "c:\00mindra\olivine-erp-platform"
$dest = "c:\00mindra\olivine-erp-platform\.archive"

if (-not (Test-Path $dest)) {
    New-Item -ItemType Directory -Force -Path $dest
}

# List of files to KEEP
$keep = @(
    "NEXT_SESSION.md",
    "olivine-erp-folder-files.txt",
    "viji-next-session.txt"
)

# Get all files in root (excluding directories)
$files = Get-ChildItem -Path $source -File

foreach ($file in $files) {
    if ($keep -notcontains $file.Name) {
        Move-Item -Path $file.FullName -Destination $dest -Force
        Write-Host "Archived: $($file.Name)"
    } else {
        Write-Host "Kept: $($file.Name)" -ForegroundColor Green
    }
}
