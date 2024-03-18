# Bell - Bracebridge UBF - Task List Backup [Schedule]

## Description
Daily saves the information contained in the Task List in an Excel spreadsheet located in <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/BracebridgeUBF/EgRg0ZhAsQJItve9WdAy6XABT1AvCXZymwdqJwo48O8cZg?e=CVuG5f" target="_blank">Backup</a> folder on the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/default.aspx" target="_blank">Bell/Bracebridge UBF</a> subsite.

## Trigger Action
Flow is automatically activated daily at 1 AM.

## Decision Points
* **Condition**: Condition used to control the maximum number of backups kept in the directory. If there are more than 30 versions of the backup saved in that directory, then the oldest version is deleted to free up space for the most recent version.
<br></br>
    * Type - if

## Workflow End
* Create an Excel file in the <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/BracebridgeUBF/EgRg0ZhAsQJItve9WdAy6XABT1AvCXZymwdqJwo48O8cZg?e=CVuG5f" target="_blank">Backup</a> folder

## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>

## Excel Spreadsheets Involved in the Process
* <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/BracebridgeUBF/EgRg0ZhAsQJItve9WdAy6XABT1AvCXZymwdqJwo48O8cZg?e=CVuG5f" target="_blank">TaskList_YYYY-MM-DDTHH_MM_SS.xlsx</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The names of Excel spreadsheets are generated automatically taking into account the date and time.</p>
</div>

## Video to GIF (Example of execution)