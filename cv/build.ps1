# Regenera el CV en PDF (tamaño Oficio) desde las fuentes HTML con Chrome headless.
# Uso:  powershell -ExecutionPolicy Bypass -File cv\build.ps1
# Salidas:
#   cv/CV_JuanValentinAlducin.pdf     (ES, desde cv.html)
#   cv/CV_JuanValentinAlducin_EN.pdf  (EN, desde cv-en.html)
# Ambos son los artefactos que descarga el sitio.

$ErrorActionPreference = "Stop"

$chrome = @(
  "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
  "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
  "$env:ProgramFiles (x86)\Microsoft\Edge\Application\msedge.exe",
  "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1

if (-not $chrome) { throw "No se encontró Chrome ni Edge para generar el PDF." }

# (fuente HTML, PDF de salida)
$targets = @(
  @{ src = "cv.html";    out = "CV_JuanValentinAlducin.pdf" },
  @{ src = "cv-en.html"; out = "CV_JuanValentinAlducin_EN.pdf" }
)

foreach ($t in $targets) {
  $src = Join-Path $PSScriptRoot $t.src
  $out = Join-Path $PSScriptRoot $t.out
  # user-data-dir único por llamada: evita el singleton de Chrome headless (no-op en llamadas seguidas)
  $udd = Join-Path $env:TEMP ("cvbuild_" + [guid]::NewGuid().ToString("N"))
  & $chrome --headless --disable-gpu --no-pdf-header-footer --user-data-dir="$udd" --print-to-pdf="$out" "$src"
  Remove-Item $udd -Recurse -Force -ErrorAction SilentlyContinue
  Write-Host "CV generado: $out"
}
