# GitLab Issue Remover

This script allows you to delete issues from a specified GitLab project that have specific labels. It also saves the details of the deleted issues in an Excel file for record-keeping.

## Prerequisites

- Python 3.x
- `gitlab` Python package
- `openpyxl` Python package

You can install the required packages using the following commands:
```bash
pip install python-gitlab openpyxl
```

#### Configuration

Before running the script, you need to configure the following variables:

	1.	Access Token: Your GitLab private access token.
	2.	Project ID: The ID of the GitLab project from which you want to delete issues.
	3.	Labels: The labels that the issues must have to be deleted. You can specify a single label as a string or multiple labels as a list.
	4.	GitLab URL: The URL of your GitLab instance.

#### Example:
```python
access_token = 'your-private-access-token'
project_id = 123456
label_name = ['bug', 'urgent']
gitlab_url = 'https://gitlab.example.com'
```

#### Script Explanation

	1.	Initialization: The script initializes the connection to the GitLab instance using the provided access token and URL.
	2.	Project Access: It retrieves the specified project using the project ID.
	3.	Issue Deletion: The script fetches issues with the specified labels in pages of 100 issues each. It deletes each issue and keeps track of the deleted issues.
	4.	Excel Logging: The details of the deleted issues (ID, title, labels) are saved in an Excel file named removed.xlsx.

#### Running the Script

To run the script, simply execute it using Python:

```bash
python gitlab-remover.py
```

#### Notes

	•	Ensure that you have appropriate permissions to delete issues in the specified project.
	•	Deleting issues is a permanent action. Use this script with caution.
	•	The Excel file removed.xlsx will be saved in the directory where you run the script.

License

This project is licensed under the GPL-3.0 license - see the LICENSE file for details.
