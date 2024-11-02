#!/bin/bash

# Define a unique part of the container image name here
image_search_term="ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest"

# Find the container ID automatically using the ancestor filter for the image name
container_id=$(docker ps --filter "ancestor=$image_search_term" --format "{{.ID}}" | head -n 1)

# Check if a container was found
if [ -z "$container_id" ]; then
  echo "No running container found with image: $image_search_term"
  exit 1
else
  echo "Found container ID: $container_id"
fi

# Define the path to the log file within the container and the local output file
log_path="/tmp/streamlit_stdout.log"
output_file="$PWD/temp_folder/local_log_file.log"

# Stream logs from the container to the local file
docker exec -it "$container_id" tail -f "$log_path" > "$output_file"
