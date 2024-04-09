# Bell - Bracebridge UBF - Task List Backup [Schedule]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/de4474e6-0a99-4fb3-925a-94d7cd886bf7/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>

## Description
Daily saves the information contained in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a> in an Excel spreadsheet located in <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/BracebridgeUBF/EgRg0ZhAsQJItve9WdAy6XABT1AvCXZymwdqJwo48O8cZg?e=CVuG5f" target="_blank">Backup</a> folder on the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/default.aspx" target="_blank">Bell/Bracebridge UBF</a> subsite.

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

## Example of Execution

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Triggering and executing Flow takes a few minutes to complete, although in the demonstrations below it appears to take less time.</p>
</div>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>This Flow is scheduled to trigger automatically every day, however in the demonstration below it was triggered manually.</p>
</div>

<a class="" data-lightbox="Task List Backup" href="../../../_static/flows/Bell - Bracebridge UBF - Task List Backup [Schedule].gif" title="Task List Backup" data-title="Task List Backup"><img src="../../../_static/flows/Bell - Bracebridge UBF - Task List Backup [Schedule].gif" class="align-center" width="800px" height="500px" alt="Task List Backup">
</a>