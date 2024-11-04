#!/bin/bash

# Variables
SOURCE_DIR="/home/ubuntu/krushna"            # back up directoty
BACKUP_DIR="/tmp"                             # Directory to store backups
DATE=$(date +%Y%m%d_%H%M%S)                   # Date and time 
BACKUP_FILE="backup_$DATE.tar.gz"             # Backup filename with date and time

# Create backup directory if not exits
mkdir -p "$BACKUP_DIR"

# Create the backup
tar -czf "$BACKUP_DIR/$BACKUP_FILE" "$SOURCE_DIR"

echo "Backup created: $BACKUP_DIR/$BACKUP_FILE"
