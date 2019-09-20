#!/bin/bash
# Timing, in seconds

# Set to fail script if any command fails.
set -e

function finish {
  end=$(date +%s.%N)
  runtime=$( echo "$end - $start" | bc -l )
  echo "Completed: $(date '+%Y-%m-%d %H:%M:%S')"
  echo "Runtime: $runtime secs"
}
trap finish EXIT

echo "Started: $(date '+%Y-%m-%d %H:%M:%S')"
start=$(date +%s.%N)

echo "Do something..."
