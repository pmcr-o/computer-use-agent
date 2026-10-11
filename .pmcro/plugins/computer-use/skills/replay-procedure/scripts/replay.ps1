[CmdletBinding()]param([Parameter(Mandatory=$true)][string]$ProcedurePath,[string]$AdapterScript='',[switch]$Apply)
Set-StrictMode -Version Latest;$ErrorActionPreference='Stop';$p=Get-Content -LiteralPath $ProcedurePath -Raw|ConvertFrom-Json -DateKind String
if($p.schema -ne 'pmcro.computer-use-procedure/v1'){throw 'invalid procedure schema'}
if(-not $Apply){Write-Output "dry run: replay procedure $($p.id) via $($p.adapterRoute) status=$($p.adapterStatus) steps=$($p.steps.Count)";return}
if($p.adapterStatus -ne 'CONFIRMED'){throw 'HALT: computer-use adapter is not CONFIRMED'};if(-not $AdapterScript){throw 'AdapterScript required'}
$adapter=(Resolve-Path -LiteralPath $AdapterScript).Path;& $adapter -ProcedurePath (Resolve-Path -LiteralPath $ProcedurePath).Path;if($LASTEXITCODE -ne 0){throw "adapter failed: $LASTEXITCODE"};return
