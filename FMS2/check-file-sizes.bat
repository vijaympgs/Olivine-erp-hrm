@echo off
echo Checking FMS BBP file sizes and completion status...
echo.

REM Create a temporary file to store results
set "temp_file=file_sizes.txt"
echo File Size Analysis > %temp_file%
echo ================== >> %temp_file%
echo. >> %temp_file%

REM Check files in 01.Finance Setup & Configuration
echo 01.Finance Setup and Configuration >> %temp_file%
echo --------------------------- >> %temp_file%

for %%f in ("FMS\01.Finance Setup & Configuration\1.1.Core Financial Setup\*.md") do (
    for %%A in ("%%f") do (
        REM Check if file contains "END OF SECTION 16" to determine completion
        findstr /C:"END OF SECTION 16" "%%f" >nul 2>&1
        if errorlevel 1 (
            echo %%~nxf: %%~zA bytes - NOT STARTED ^(Missing END OF SECTION 16^) >> %temp_file%
        ) else (
            echo %%~nxf: %%~zA bytes - COMPLETED ^(Has all 16 sections^) >> %temp_file%
        )
    )
)

for %%f in ("FMS\01.Finance Setup & Configuration\1.2.Tax Categories\*.md") do (
    for %%A in ("%%f") do (
        REM Check if file contains "END OF SECTION 16" to determine completion
        findstr /C:"END OF SECTION 16" "%%f" >nul 2>&1
        if errorlevel 1 (
            echo %%~nxf: %%~zA bytes - NOT STARTED ^(Missing END OF SECTION 16^) >> %temp_file%
        ) else (
            echo %%~nxf: %%~zA bytes - COMPLETED ^(Has all 16 sections^) >> %temp_file%
        )
    )
)

for %%f in ("FMS\01.Finance Setup & Configuration\1.3.Budgets\*.md") do (
    for %%A in ("%%f") do (
        REM Check if file contains "END OF SECTION 16" to determine completion
        findstr /C:"END OF SECTION 16" "%%f" >nul 2>&1
        if errorlevel 1 (
            echo %%~nxf: %%~zA bytes - NOT STARTED ^(Missing END OF SECTION 16^) >> %temp_file%
        ) else (
            echo %%~nxf: %%~zA bytes - COMPLETED ^(Has all 16 sections^) >> %temp_file%
        )
    )
)

echo. >> %temp_file%

REM Check files in 02.Finance Operations & Entries
echo 02.Finance Operations and Entries >> %temp_file%
echo ----------------------------- >> %temp_file%

for %%f in ("FMS\02.Finance Operations & Entries\*.md") do (
    for %%A in ("%%f") do (
        REM Check if file contains "END OF SECTION 16" to determine completion
        findstr /C:"END OF SECTION 16" "%%f" >nul 2>&1
        if errorlevel 1 (
            echo %%~nxf: %%~zA bytes - NOT STARTED ^(Missing END OF SECTION 16^) >> %temp_file%
        ) else (
            echo %%~nxf: %%~zA bytes - COMPLETED ^(Has all 16 sections^) >> %temp_file%
        )
    )
)

echo. >> %temp_file%

REM Check files in 03.Bank Reconciliation
echo 03.Bank Reconciliation >> %temp_file%
echo --------------------- >> %temp_file%

for %%f in ("FMS\03.Bank Reconciliation\*.md") do (
    for %%A in ("%%f") do (
        REM Check if file contains "END OF SECTION 16" to determine completion
        findstr /C:"END OF SECTION 16" "%%f" >nul 2>&1
        if errorlevel 1 (
            echo %%~nxf: %%~zA bytes - NOT STARTED ^(Missing END OF SECTION 16^) >> %temp_file%
        ) else (
            echo %%~nxf: %%~zA bytes - COMPLETED ^(Has all 16 sections^) >> %temp_file%
        )
    )
)

echo. >> %temp_file%

REM Check files in 04.Fixed_Assets
echo 04.Fixed Assets >> %temp_file%
echo -------------- >> %temp_file%

for %%f in ("FMS\04.Fixed_Assets\*.md") do (
    for %%A in ("%%f") do (
        REM Check if file contains "END OF SECTION 16" to determine completion
        findstr /C:"END OF SECTION 16" "%%f" >nul 2>&1
        if errorlevel 1 (
            REM Check if file size is under 100 bytes
            if %%~zA LSS 100 (
                echo %%~nxf: %%~zA bytes - EMPTY PLACEHOLDER ^(Under 100 bytes^) >> %temp_file%
            ) else (
                echo %%~nxf: %%~zA bytes - NOT STARTED ^(Missing END OF SECTION 16^) >> %temp_file%
            )
        ) else (
            echo %%~nxf: %%~zA bytes - COMPLETED ^(Has all 16 sections^) >> %temp_file%
        )
    )
)

echo. >> %temp_file%

REM Check files in 05.Inventory Management
echo 05.Inventory Management >> %temp_file%
echo -------------------- >> %temp_file%

for %%f in ("FMS\05.Inventory Management\*.md") do (
    for %%A in ("%%f") do (
        REM Check if file contains "END OF SECTION 16" to determine completion
        findstr /C:"END OF SECTION 16" "%%f" >nul 2>&1
        if errorlevel 1 (
            REM Check if file size is under 100 bytes
            if %%~zA LSS 100 (
                echo %%~nxf: %%~zA bytes - EMPTY PLACEHOLDER ^(Under 100 bytes^) >> %temp_file%
            ) else (
                echo %%~nxf: %%~zA bytes - NOT STARTED ^(Missing END OF SECTION 16^) >> %temp_file%
            )
        ) else (
            echo %%~nxf: %%~zA bytes - COMPLETED ^(Has all 16 sections^) >> %temp_file%
        )
    )
)

echo. >> %temp_file%

REM Check files in 06.Finance Closing & Compliance
echo 06.Finance Closing and Compliance >> %temp_file%
echo ------------------------------ >> %temp_file%

for %%f in ("FMS\06.Finance Closing & Compliance\*.md") do (
    for %%A in ("%%f") do (
        REM Check if file contains "END OF SECTION 16" to determine completion
        findstr /C:"END OF SECTION 16" "%%f" >nul 2>&1
        if errorlevel 1 (
            REM Check if file size is under 100 bytes
            if %%~zA LSS 100 (
                echo %%~nxf: %%~zA bytes - EMPTY PLACEHOLDER ^(Under 100 bytes^) >> %temp_file%
            ) else (
                echo %%~nxf: %%~zA bytes - NOT STARTED ^(Missing END OF SECTION 16^) >> %temp_file%
            )
        ) else (
            echo %%~nxf: %%~zA bytes - COMPLETED ^(Has all 16 sections^) >> %temp_file%
        )
    )
)

echo. >> %temp_file%

REM Check files in 07.Finance Analytics & Insights
echo 07.Finance Analytics and Insights >> %temp_file%
echo ----------------------------- >> %temp_file%

for %%f in ("FMS\07.Finance Analytics & Insights\*.md") do (
    for %%A in ("%%f") do (
        REM Check if file contains "END OF SECTION 16" to determine completion
        findstr /C:"END OF SECTION 16" "%%f" >nul 2>&1
        if errorlevel 1 (
            REM Check if file size is under 100 bytes
            if %%~zA LSS 100 (
                echo %%~nxf: %%~zA bytes - EMPTY PLACEHOLDER ^(Under 100 bytes^) >> %temp_file%
            ) else (
                echo %%~nxf: %%~zA bytes - NOT STARTED ^(Missing END OF SECTION 16^) >> %temp_file%
            )
        ) else (
            echo %%~nxf: %%~zA bytes - COMPLETED ^(Has all 16 sections^) >> %temp_file%
        )
    )
)

echo. >> %temp_file%
echo Analysis completed at %date% %time% >> %temp_file%

REM Display results
type %temp_file%

echo.
echo Results saved to: %temp_file%
echo.
pause
