# How to Fetch GitLab Users and Convert to CSV Using Python

This guide will show you how to fetch all users from your GitLab instance using its API and convert the user data from JSON to CSV format, all in one Python script.

### Prerequisites
- Python 3 installed on your system
- `requests` library for Python

### Steps

#### 1. Install the `requests` Library
If you don’t already have the `requests` library installed, you can install it using `pip`:

```bash
pip install requests
```
### 2. Update the Script

- **Replace** `https://gitlab.example.com` with the URL of your GitLab instance.
- **Replace** `<your_access_token>` with your GitLab personal access token.

For example:

```python
# GitLab configuration
GITLAB_URL = 'https://your-gitlab-instance.com'  # Replace with your GitLab instance URL
ACCESS_TOKEN = 'your_personal_access_token'      # Replace with your GitLab personal access token
```
### 4. Run the Script

1. Save the script to a `.py` file, for example, `gitlab_users_to_csv.py`.
2. Run the script using the following command:

```bash
python gitlab_users_to_csv.py
