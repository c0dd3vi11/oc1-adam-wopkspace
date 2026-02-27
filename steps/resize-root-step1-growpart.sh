#!/usr/bin/env bash
set -euo pipefail

echo "[step1] Before:"
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT

echo "[step1] Expanding partition /dev/sda2 to fill disk /dev/sda"
sudo growpart /dev/sda 2

echo "[step1] After growpart:"
lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINT
