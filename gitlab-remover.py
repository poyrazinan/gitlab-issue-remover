import gitlab
from openpyxl import Workbook

# Access token of gitlab user
access_token = 'your-private-access-token'
# ID of Project
project_id = your_gitlab_project_id
# Array or name of Labels
# If you write ['Label1', 'Label2'] the issue that should have both of label.
# If you write 'Label1' the issue that should have the label. 
label_name = ['label1', 'label2']
# Url of gitlab
gitlab_url = 'your-gitlab-url-here'
# Object of gitlab
gl = gitlab.Gitlab(url=gitlab_url, private_token=access_token)
# Gets project
project = gl.projects.get(id=project_id)
# Deleted amount
deleted_count = 0
# Scaning page
page = 1
# Item per page (Max 100)
per_page = 100 
# Deleted data for excel
deleted_data = []
# We will break it in
while True:
    # Gets issue list on gitlab
    issues = project.issues.list(labels=label_name, page=page, per_page=per_page)
    # If there is no any issue it will breaks
    if len(issues) == 0:
        break
    # We loop issues
    for issue in issues:
        # Labels in string
        issue_labels_str = ', '.join(issue.labels)
        # We will save it for excel
        deleted_data.append((issue.id, issue.title, issue_labels_str))
        # Debug message
        print(f'Deleted issue {issue.id} from gitlab')
        # Deleting issue
        issue.delete()
        # We increase the deleted amount
        deleted_count += 1
    
    # If you don't want to remove issues, you need to enable this option.
    # Removing an issue changes the page count. After deletion,
    # the page count is different from before because issues are deleted.
    # page = page+1

## Workbook section
# Workbook object
wb = Workbook()
ws = wb.active
# We append headers
ws.append(['Issue ID', 'Issue Title', 'Labels'])
# We add the rows of deleted_data if there is any data
if len(deleted_data) != 0:
    for row in deleted_data:
        ws.append(row)
# We save the workbook to current direction
wb.save('removed.xlsx')
# Finishing task
print(f"Total {deleted_count} issues with the label '{label_name}' have been deleted.")

