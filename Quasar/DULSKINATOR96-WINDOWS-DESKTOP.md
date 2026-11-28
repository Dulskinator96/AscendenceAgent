# Dulskinator96 — Windows desktop system profile

**Status:** historical user-reported hardware baseline; fresh local inventory pending.
**Recorded:** 2026-11-27. **Machine:** owner's primary desktop, separate from the [Quasar machine profile](QUASAR-SYSTEM-PROFILE.md).
**Purpose:** target-specific planning and reproducible local AI/software experiments. The branch location does not make the machines identical.

| Component | Historical reported configuration |
|---|---|
| System | Acer Predator Orion 3000 |
| Operating system | Windows 11 Home, x64 (historical; current edition/build unverified) |
| CPU | Intel Core i7-10700 |
| System memory | 16 GB DDR4 nominal |
| GPU | NVIDIA GeForce RTX 2060 SUPER |
| Dedicated VRAM | 8 GB nominal, historically reported; recheck with NVIDIA driver tooling |

## Evidence boundary
The owner previously reported this configuration (including 2026-11-20). Earlier inventory recollections include inconsistent graphics-memory readings (~4 GB from one probe versus 8 GB reported). A fresh NVIDIA-SMI reading is necessary before using VRAM as a measured constraint. These are historical reports, not a new live hardware probe. Exact OEM submodel, OS build, current usable RAM, driver, disk capacities/free space, virtualization, thermal state and installed runtime versions are unknown at this checkpoint. No benchmark or inference speed is inferred.

## Read-only verification (run on the owner's Windows desktop)

```powershell
$report = & {
    "=== DULSKINATOR96 WINDOWS DESKTOP | $((Get-Date).ToUniversalTime().ToString('o')) ==="
    Get-CimInstance Win32_ComputerSystem | Select-Object Manufacturer,Model,SystemType,@{n='RAM_GiB';e={[math]::Round($_.TotalPhysicalMemory/1GB,2)}} | Format-List | Out-String
    Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,BuildNumber,OSArchitecture | Format-List | Out-String
    Get-CimInstance Win32_Processor | Select-Object Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed,VirtualizationFirmwareEnabled | Format-List | Out-String
    Get-CimInstance Win32_PhysicalMemory | Select-Object @{n='Capacity_GiB';e={[math]::Round($_.Capacity/1GB,2)}},Speed,ConfiguredClockSpeed | Format-Table -AutoSize | Out-String
    Get-CimInstance Win32_VideoController | Select-Object Name,DriverVersion | Format-List | Out-String
    if (Get-Command nvidia-smi -ErrorAction SilentlyContinue) {
        nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader
    } else { "NVIDIA-SMI unavailable; dedicated VRAM not verified" }
    Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' | Select-Object DeviceID,@{n='Total_GiB';e={[math]::Round($_.Size/1GB,1)}},@{n='Free_GiB';e={[math]::Round($_.FreeSpace/1GB,1)}} | Format-Table -AutoSize | Out-String
    foreach ($tool in 'python','node','git','ollama') {
        if (Get-Command $tool -ErrorAction SilentlyContinue) {
            "$tool : $(& $tool --version 2>&1 | Out-String)"
        } else { "$tool : not found on PATH" }
    }
} | Out-String
$report
Set-Clipboard -Value $report
```

Collect only necessary non-sensitive specifications. Do not publish serials, product IDs, IP/MAC addresses, local usernames, secrets, installed personal files, or raw unrestricted system dumps. The clipboard output is for review before updating this public record. No installs, driver changes, benchmarks or firmware edits are performed.

## Experimental planning
For any actual Laura or other local model comparison, record run-specific OS, CPU/RAM/GPU/VRAM, driver and model versions/digests, quantization, context, inference settings, device/offload, latency, resource use and frozen cases. Match conditions before attributing improvements to a mechanism. The profile alone is not evidence of model capability. Never substitute Quasar's AMD/RTX 4060 specs or a cloud runner's specifications for this target.
