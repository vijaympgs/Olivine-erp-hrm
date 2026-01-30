$path = "c:\00mindra\retail-erp-platform\frontend\src\modules\pos\billing\PosDesktop.tsx"
$content = Get-Content $path -Raw
# Using substring matching to be safe
if ($content -match ", Info, Clock, History, History, UserPlus, Printer, Receipt} from 'lucide-react';") {
    $content = $content.Replace(", Info, Clock, History, History, UserPlus, Printer, Receipt} from 'lucide-react';", ", Info, Clock, History, UserPlus } from 'lucide-react';")
    [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
    Write-Host "Fixed imports successfully" -ForegroundColor Green
} else {
    Write-Host "Pattern not found" -ForegroundColor Red
}
