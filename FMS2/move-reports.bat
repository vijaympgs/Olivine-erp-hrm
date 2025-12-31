@echo off
echo Moving report files from Finance Closing & Compliance to Finance Analytics & Insights...
echo.

REM Move Compliance Reports (6.8) to Analytics & Insights
echo Moving 6.8 Compliance Reports.md...
move "FMS\06.Finance Closing & Compliance\6.8 Compliance Reports.md" "FMS\07.Finance Analytics & Insights\"

echo.
echo File move operation completed.
echo.
pause
