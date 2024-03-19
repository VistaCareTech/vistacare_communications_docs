# Bell - St Charles - Task List Backup [Schedule]

## Description
Daily saves the information contained in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Tasks/1000%20Tasks.aspx" target="_blank">Task List</a> in an Excel spreadsheet located in <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/StCharles/ElH9AaTWHopImN8vPjMknOIB9QoHmYEQ4KhiSmpveaxM9Q?e=QUhLcU" target="_blank">Backup</a> folder on the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/default.aspx" target="_blank">Bell/St Charles</a> subsite.

## Trigger Action
Flow is automatically activated daily at 1 AM.

## Decision Points
* **Condition**: Condition used to control the maximum number of backups kept in the directory. If there are more than 30 versions of the backup saved in that directory, then the oldest version is deleted to free up space for the most recent version.
<br></br>
    * Type - if

## Workflow End
* Create an Excel file in the <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/StCharles/ElH9AaTWHopImN8vPjMknOIB9QoHmYEQ4KhiSmpveaxM9Q?e=QUhLcU" target="_blank">Backup</a> folder

## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Tasks/1000%20Tasks.aspx" target="_blank">Task List</a>

## Excel Spreadsheets Involved in the Process
* <a href="https://vistacaretech.sharepoint.com/:f:/s/engineering/Bell/StCharles/ElH9AaTWHopImN8vPjMknOIB9QoHmYEQ4KhiSmpveaxM9Q?e=QUhLcU" target="_blank">TaskList_YYYY-MM-DDTHH_MM_SS.xlsx</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The names of Excel spreadsheets are generated automatically taking into account the date and time.</p>
</div>

## Video to GIF (Example of execution)