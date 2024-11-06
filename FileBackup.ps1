# Departmental File Backup Organizer

# This PowerShell script efficiently sorts and backs up files from a source directory by moving them to department-specific folders. Files with "HR" or "Sales" in their names are moved to dedicated backup folders, with filenames appended to indicate backup status.
# LogLogic 06/13/24 CYB_300

# Define source and destination folders
$sourceFolder = "C:\officefiles"
$HRDestination = "C:\HR_Backup"
$SalesDestination = "C:\sales_backup"

# Create the destination folders if they don't exist
if (-not (Test-Path $HRDestination)) {
    New-Item -ItemType Directory -Path $HRDestination | Out-Null
}

if (-not (Test-Path $SalesDestination)) {
    New-Item -ItemType Directory -Path $SalesDestination | Out-Null
}

# Get all files in the source folder
$files = Get-ChildItem -Path $sourceFolder

# Loop through each file and move to respective folders
foreach ($file in $files) {
    if ($file.Name -match "HR") {
        $newFileName = $file.BaseName + "_backup" + $file.Extension
        Move-Item -Path $file.FullName -Destination (Join-Path -Path $HRDestination -ChildPath $newFileName)
    }
    elseif ($file.Name -match "Sales") {
        $newFileName = $file.BaseName + "_backup" + $file.Extension
        Move-Item -Path $file.FullName -Destination (Join-Path -Path $SalesDestination -ChildPath $newFileName)
    }
}


Write-Output "Files have been separated and moved to respective backup folders."
