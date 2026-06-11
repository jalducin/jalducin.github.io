# Deploy manual del portafolio a AWS (S3 + CloudFront).
# El flujo normal es automático vía GitHub Actions (push a main). Este script es para deploy local.
# Uso:  powershell -ExecutionPolicy Bypass -File scripts\deploy-aws.ps1

$ErrorActionPreference = "Stop"
$Bucket  = "jalducin-portfolio-957266312835"
$DistId  = "EG4961CAMR9Z8"
$Root    = Split-Path -Parent $PSScriptRoot

Push-Location $Root
try {
  Write-Host "Sync -> s3://$Bucket"
  aws s3 sync . "s3://$Bucket" `
    --exclude ".git/*" --exclude ".github/*" --exclude "openspec/*" `
    --exclude "ai-specs/*" --exclude "docs/*" --exclude ".claude/*" `
    --exclude ".gemini/*" --exclude "scripts/*" --exclude "*.md" `
    --exclude ".gitignore" --exclude "cv/build.ps1" --exclude "cv/og.html" `
    --delete

  Write-Host "Invalidando CloudFront ($DistId)"
  aws cloudfront create-invalidation --distribution-id $DistId --paths "/*" | Out-Null

  Write-Host "Listo. https://d3r3bnavnwzqaw.cloudfront.net"
}
finally { Pop-Location }
