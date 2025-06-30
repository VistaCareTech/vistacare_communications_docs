# Task List Backup [Schedule]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/9e3c2868-e253-4385-93a0-28b17001cd9a/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Daily saves the information contained in the **Task List** in an Excel spreadsheet located in **Backup** folder for each subsite.


## Trigger Action
Flow is automatically activated daily at 10 PM.

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>If necessary, it can be configured to trigger several times a day at different times.</p>
</div>


## Variables
* **siteAddress**: **Array** type variable that stores the address of the SharePoint subsites in String format.
<br></br>

* **path**: **String** type variable that stores the path where Excel files are saved.
<br></br>

* **driveID**: **String** type variable that stores the Document Library Drive ID of the SharePoint subsite.
<br></br>

* **listsNames**: **Object** type variable used to store the name of the SharePoint lists used in the Flow and their respective IDs.
<br></br>

* **taskList_ColumnValue**: **Object** type variable used to store the column/field and its values ​​of an **Task** present in the **Task List**.
<br></br>

* **numberOfBackups**: **Integer** type variable used to determine the maximum number of backup files to be kept in the Backup folder.
<br></br>

* **counter**: **Integer** type variable variable used to assist in counting the number of backup files existing in the Backup folder.
<br></br>


## Decision Points
* **Condition - Are there more than 30 backup files**: Condition used to control the maximum number of backups kept in the directory. If there are more than 30 versions of the backup saved in that directory, then the oldest version is deleted to free up space for the most recent version.
<br></br>
    * Type - if


## Related Flows
* [Get SharePoint Lists IDs [Dependent]](../General/Get%20SharePoint%20Lists%20IDs%20[Dependent].md)


## Workflow End
A. First End:  
    &emsp; 1. "**Apply to each** - siteAdresses"  
    &emsp; 2. "**Create an Excel File** in the Backup folder"


## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The links above point to the lists present on the <b>Bracebridge UBF</b> subsite, however Flow will update the equivalent lists in each set subsite.</p>
</div>


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


<a data-fancybox="Task List Backup" href="../../../_static/flows/task_list_backup/bell_-_st_charles_-_task_list_backup_[schedule].mp4" data-caption="Task List Backup">
  <img src="../../../_static/flows/task_list_backup/bell_-_st_charles_-_task_list_backup_[schedule]_thumbnail.jpg" alt="Task List Backup" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>