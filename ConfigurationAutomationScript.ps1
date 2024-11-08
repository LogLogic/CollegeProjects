# System Configuration and Security Task Automation Script

# This PowerShell script automates key configuration and security-related tasks, including renaming the computer, setting the time zone, listing running services, managing idle lock time, stopping specific services, and exporting security logs. The script is useful for initial system setup and security hardening in Windows environments.
# LogLogic 06/24/24 CYB_300

# a. Rename computer to First Initial_Last Name 
$NewComputerName = "LogLogic"
Rename-Computer -NewName $NewComputerName -Force -Restart

# b. Change time zone to the time zone associated with Denver, Colorado
$TimeZone = "Mountain Standard Time"
Set-TimeZone -Id $TimeZone

# c. Get a list of running services
$RunningServices = Get-Service | Where-Object { $_.Status -eq 'Running' }
$RunningServices | Out-File -FilePath "C:\Users\RunningServices.txt"

# d. Stop the Print Spooler service
$ServiceName = "Spooler"
Stop-Service -Name $ServiceName -Force

# e. Set idle lock time for screensaver to 3 minutes
$IdleTime = 180
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop\" -Name "ScreenSaveTimeOut" -Value $IdleTime
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop\" -Name "ScreenSaveActive" -Value "1"

# f. Send the output of first 50 entries in security event log to a text file named “SecurityLog_LastName.txt”
$SecurityLogFile = "C:\Users\SecurityLog_LogLogic.txt"
Get-EventLog -LogName Security -Newest 50 | Out-File -FilePath $SecurityLogFile

  
