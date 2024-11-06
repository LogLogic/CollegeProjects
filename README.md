# CollegeProjects

## Odd IP Address Ping Scanner
(OddIPsPing.ps1)

This PowerShell script scans a specified subnet range by pinging only the IP addresses that end in odd numbers. 
Designed for network diagnostics, it iterates through a defined IP range, pings each odd-numbered IP once, 
and stores the results in a text file. Each result logs the IP address along with its reachability status.

Features:

Selective IP Scanning: Targets only odd-numbered IPs within the range.
Automated Reachability Testing: Uses Test-Connection to ping addresses, making it ideal for quick network health checks.
Logging to File: Saves ping results to ping.txt, providing a straightforward reference for network diagnostics.
_______________________________

## Departmental File Backup Organizer
(FileBackup.ps1)

This PowerShell script efficiently sorts and backs up files from a source directory by moving them to department-specific folders. 
Files with "HR" or "Sales" in their names are moved to dedicated backup folders, with filenames appended to indicate backup status.

Features:

Automated Folder Creation: Creates HR_Backup and sales_backup directories if they don't already exist.
Departmental Sorting: Identifies files by checking for "HR" or "Sales" in the filename, then moves them to the appropriate backup folder.
File Renaming: Adds "_backup" to each filename, preserving the original file extension.
Status Output: Confirms when the files have been successfully sorted and backed up.
_______________________________

## System Configuration and Security Task Automation Script
(ConfigurationAutomationScript.ps1)

This PowerShell script automates key configuration and security-related tasks, including renaming the computer, setting the time zone, listing running services, managing idle lock time, stopping specific services, and exporting security logs. 
The script is useful for initial system setup and security hardening in Windows environments.

Key Functions:

Computer renaming and automated restart
Time zone configuration
Retrieval and logging of running services
Screensaver lock enforcement
Security event log export
_______________________________

## MousePicnic Text Adventure Game
(PythonTextGame)

This Python-based text adventure game challenges players to help a little mouse prepare for a picnic. 
Navigate through various rooms, gather essential items, and avoid encounters with the Owl, Fox, and Snake, 
who will end the game if met. 
The goal is to collect all six items and reach the Back Door to win.

Features:

Interactive navigation with commands like "go North" and "get [item name]"
Unique rooms containing items and characters
Win condition: Collect all items and reach the exit
Loss condition: Avoid rooms with villain characters
Built-in inventory system to track collected items
_______________________________
