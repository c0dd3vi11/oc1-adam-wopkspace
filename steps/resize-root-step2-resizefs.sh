#!/usr/bin/env bash
set -euo pipefail

echo "[step2] Checking fs type"
findmnt -no FSTYPE /

echo "[step2] Expanding ext4 filesystem on /dev/sda2"
sudo resize2fs /dev/sda2

echo "[step2] Final state"
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT
df -hT /
