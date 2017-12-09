#!/usr/bin/pwsh
$lines = Get-Content -path ../task02.input
$result = 0
foreach ($line in $lines) {
    foreach ($word in $line.split("`t")) {
        foreach ($word2 in $line.split("`t")) {
            if ($word -ne $word2) {
                if (0 -eq $word % $word2) {
                    Write-Output "#1 $word % $word2 = 0"
                    $div = $word / $word2
                    Write-Output "#2 $word / $word2 = $div"
                    $result = $result + $div
                    break
                }
            }
        }
    }
}
Write-Output $result