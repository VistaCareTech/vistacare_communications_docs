# Recovery From Backup [Manual]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/84ce37ba-b27a-441e-a2d1-756144804bc1/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>

## Description
Flow created to facilitate adding backup data to the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>. When there is a problem with the Task List, for example tasks deleted by mistake, the user can search the <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/BracebridgeUBF/EgRg0ZhAsQJItve9WdAy6XABT1AvCXZymwdqJwo48O8cZg?e=CVuG5f" target="_blank">Backup</a> folder for a backup file, and then use this Flow to automatically recover the missing data in the Task List.

## Trigger Action
User needs to select the backup file they want to recover in the "List rows present in a table" action, and then click on run Flow.

## Decision Points

## Workflow End
* Create Item action (<a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>)

## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>

## Excel Spreadsheets Involved in the Process
* <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/BracebridgeUBF/EgRg0ZhAsQJItve9WdAy6XABT1AvCXZymwdqJwo48O8cZg?e=CVuG5f" target="_blank">TaskList_YYYY-MM-DDTHH_MM_SS.xlsx</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The names of Excel spreadsheets are generated automatically taking into account the date and time.</p>
</div>

## Example of Execution