#!/bin/bash

# TODO: This is not a product-ready script for downloading raw GA4 event data from
# BigQuery. `bq query` is not intended for downloading large datasets. It is recommended to use
# `bq extract` with a GCP storage bucket for larger datasets.

# Make sure to run
# gcloud auth login
# gcloud config set project vaulted-sol-400319

# --- Configuration ---
PROJECT_ID="vaulted-sol-400319"
DATASET="analytics_408618944" # The BigQuery dataset corresponding to exported GA4 Dallas Free Press data
TABLE_PREFIX="events_"   # GA4 event tables are typically partitioned by date
START_DATE="20250207"    # Format: YYYYMMDD
END_DATE="20250325"      # Format: YYYYMMDD
MAX_ROWS=10000 # The `bq query` cli command has a default limit of 100 rows.
RELATIVE_DEST_FOLDER="data/ga-dfp/raw" # Relative to the working directory
DEST_FOLDER="$(pwd)/${RELATIVE_DEST_FOLDER}"
EXPORT_FORMAT="JSON"      # Can be CSV or JSON

# --- Ensure destination folder exists ---
mkdir -p "$DEST_FOLDER"

# --- Date loop ---
current_date="$START_DATE"
while [[ "$current_date" -le "$END_DATE" ]]; do
  TABLE="${PROJECT_ID}.${DATASET}.${TABLE_PREFIX}${current_date}"
  EXTENSION=$(echo "$EXPORT_FORMAT" | tr '[:upper:]' '[:lower:]')
  DEST_FILE="${DEST_FOLDER}/${current_date}.${EXTENSION}"

  echo "📥 Querying and saving: $TABLE -> $DEST_FILE"

  if [[ "$EXPORT_FORMAT" == "CSV" ]]; then
    bq query \
      --use_legacy_sql=false \
      --project_id="$PROJECT_ID" \
      --format=csv \
      --nouse_cache \
      --max_rows="$MAX_ROWS" \
      "SELECT * FROM \`${TABLE}\`" > "$DEST_FILE"
  else
    bq query \
      --use_legacy_sql=false \
      --project_id="$PROJECT_ID" \
      --format=json \
      --nouse_cache \
      --max_rows="$MAX_ROWS" \
      "SELECT * FROM \`${TABLE}\`" > "$DEST_FILE"
  fi

  if [[ $? -ne 0 ]]; then
    echo "❌ Failed: $TABLE"
  else
    echo "✅ Saved to $DEST_FILE"
  fi

  # macOS date increment
  current_date=$(date -j -v+1d -f "%Y%m%d" "$current_date" +"%Y%m%d")
done
