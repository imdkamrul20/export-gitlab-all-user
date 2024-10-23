import requests
import json
import csv

# GitLab configuration
GITLAB_URL = 'https://gitlab.example.com'  # Replace with your GitLab instance URL
ACCESS_TOKEN = '<your_access_token>'       # Replace with your GitLab personal access token

# API request to get all users
url = f'{GITLAB_URL}/api/v4/users?per_page=100'
headers = {'PRIVATE-TOKEN': ACCESS_TOKEN}

response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    users = response.json()
    
    # Open a CSV file for writing
    with open('gitlab_users.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'username', 'name', 'email', 'state', 'created_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write each user's data into the CSV
        for user in users:
            writer.writerow({
                'id': user['id'],
                'username': user['username'],
                'name': user['name'],
                'email': user.get('email', 'N/A'),  # Some users might not have an email, so we use 'N/A'
                'state': user['state'],
                'created_at': user['created_at']
            })

    print("CSV file 'gitlab_users.csv' created successfully.")

else:
    print(f"Failed to retrieve users. Status code: {response.status_code}")
