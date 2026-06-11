# Regenera el CV en PDF (tamaño Oficio) desde cv/cv.html con Chrome headless.
# Uso:  powershell -ExecutionPolicy Bypass -File cv\build.ps1
# Salida: cv/CV_JuanValentinAlducin.pdf (lo que descarga el sitio).

$ErrorActionPreference = "Stop"
$src    = Join-Path $PSScriptRoot "cv.html"
$out    = Join-Path $PSScriptRoot "CV_JuanValentinAlducin.pdf"

$chrome = @(
  "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
  "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
  "$env:ProgramFiles (x86)\Microsoft\Edge\Application\msedge.exe",
  "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $chrome) { throw "No se encontró Chrome ni Edge para generar el PDF." }

& $chrome --headless --disable-gpu --no-pdf-header-footer `
  --print-to-pdf="$out" "$src"

Write-Host "CV generado: $out"
