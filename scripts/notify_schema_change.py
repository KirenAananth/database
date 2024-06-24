import os
import sys
import json

# Function to extract metadata from directory structure
def extract_metadata(dir_path):
    parts = dir_path.split('/')
    if len(parts) < 8:
        return None  # Directory structure does not match expected format

    return {
        'Tenant_Name': parts[3],
        'Env': parts[5],
        'Region': parts[6],
        'Cluster': parts[7]
    }

# Main function
def main():
    # Check if the change file is inside the schema directory
    if not os.getenv('GITHUB_EVENT_PATH'):
        print("Environment variable GITHUB_EVENT_PATH not found. Exiting.")
        sys.exit(1)

    with open(os.getenv('GITHUB_EVENT_PATH'), 'r') as event_file:
        event_data = json.load(event_file)

    if 'pull_request' not in event_data['action']:
        print("No pull request action found. Exiting.")
        sys.exit(0)

    pr_files = event_data['pull_request']['files']
    schema_files_changed = False

    for file in pr_files:
        if file['filename'].startswith('database/schema'):
            schema_files_changed = True
            break

    if not schema_files_changed:
        print("No schema files changed. Exiting.")
        sys.exit(0)

    # Extract metadata from directory path
    dir_path = os.getenv('GITHUB_WORKSPACE')
    metadata = extract_metadata(dir_path)

    if not metadata:
        print("Directory structure does not match expected format. Exiting.")
        sys.exit(1)

    # Prepare Slack message
    message = f"Schema change detected!\nTenant_Name: {metadata['Tenant_Name']}\nEnv: {metadata['Env']}\nRegion: {metadata['Region']}\nCluster: {metadata['Cluster']}"

    # Print message (for verification)
    print(message)

    # Send Slack message (you can use a webhook or another method here)

if __name__ == "__main__":
    main()

