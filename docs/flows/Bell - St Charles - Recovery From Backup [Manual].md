# Bell - St Charles - Recovery From Backup [Manual]

## Description
Flow created to facilitate adding backup data to the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Tasks/1000%20Tasks.aspx" target="_blank">Task List</a>. When there is a problem with the Task List, for example tasks deleted by mistake, the user can search the <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/StCharles/ElH9AaTWHopImN8vPjMknOIB9QoHmYEQ4KhiSmpveaxM9Q?e=QUhLcU" target="_blank">Backup</a> folder for a backup file, and then use this Flow to automatically recover the missing data in the Task List.

## Trigger Action
User needs to select the backup file they want to recover in the "List rows present in a table" action, and then click on run Flow.

## Decision Points

## Workflow End
* Create Item action (<a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Tasks/1000%20Tasks.aspx" target="_blank">Task List</a>)

## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Tasks/1000%20Tasks.aspx" target="_blank">Task List</a>

## Excel Spreadsheets Involved in the Process
* <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/StCharles/ElH9AaTWHopImN8vPjMknOIB9QoHmYEQ4KhiSmpveaxM9Q?e=QUhLcU" target="_blank">TaskList_YYYY-MM-DDTHH_MM_SS.xlsx</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The names of Excel spreadsheets are generated automatically taking into account the date and time.</p>
</div>

## Video to GIF (Example of execution)