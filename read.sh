#!/bin/bash
# Read lines from a given file.

File=auto_correlation.py

{
read line1
read line2
} < $File

echo "First line in $File is:" 
echo "$line1"
echo
echo "Second liine in $File is:"
echo "$line2"

exit 0
