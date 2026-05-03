$exe = "dist\MyEnterpriseXMLApp.exe"

if (!(Test-Path $exe)) {
  Write-Host "::error ::EXE not found"
  exit 1
}

$deps = dumpbin /dependents $exe

if ($deps -match "python") {
  Write-Host "::error ::Python DLL detected in EXE"
  exit 1
}

Write-Host "✅ EXE is self-contained"
