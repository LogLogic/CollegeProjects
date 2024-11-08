# This PowerShell script scans a specified subnet range by pinging only the IP addresses that end in odd numbers. Designed for network diagnostics, it iterates through a defined IP range, pings each odd-numbered IP once, and stores the results in a text file. Each result logs the IP address along with its reachability status.
# LogLogic 06/13/2024 CYB-300
# Define the subnet range
$subnet = "192.168.0."
$startRange = 1
$endRange = 255

# Initialize an arrey to hold IPs ending with add number
$oddIPs = @()

#Populate the arrey with IPs ending with an odd number within the range
for ($i = $startRange; $i -le $endRange; $i++) {
    if ($i %2 -ne 0) {
        $oddIPs += "$subnet$i"
    }
}

# Initialize an arrey to hold the results
$pingResults = @()

# Ping each odd-numbered IP address and store the result
foreach ($ip in $oddIPs) {
    $pingResult = Test-Connection -ComputerName $ip -Count 1 -Quiet
    $pingResults += "$ip : $pingResult"
}

# Output the results to a text file
$pingResults | Out-File -FilePath "ping.txt"

Write-Output "Ping results have been saved to ping.txt"
