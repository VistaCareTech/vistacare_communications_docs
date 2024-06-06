# Task Capacities [Dependent]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/a4d1ba00-b59c-4e14-9d5a-ea0e869080d1/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Flow used to obtain data from the **Task Capacities** SharePoint list referring to the **Job** to which the **Task** is related. Then pass this data to the next Flow (**Date Calculator [Dependent]** Flow).


## Trigger Action
When an HTTP request is received from **Job List [Automatic]** or  **Task List [Automatic]** Flows.


## Variables
* **First Task ID**: **Integer** type variable used to store the ID of the first **Task** referring to this **Job** in the **Task List**, that is, the ID of the **Parent Task**.
<br></br>

* **Active Task Sync**: **Float** type variable used to store the **Step**/**#** of the first type of **Task** present in the **Task Capacities** SharePoint list referring to a **Job** that has the attribute **Active Task Sync** in the **Job List** SharePoint list.
<br></br>


## Decision Points
* **Condition - If There Are No Tasks For This Job in The Task List Yet**: Condition used to identify whether the **Job** already has tasks related to it in the **Task List**.
<br></br>
    * Type: if
<br></br>
* **Condition - If Has Active Task Sync**: Condition used to identify whether the **Job** in the **Job List** has any task assigned as **Active Task Sync**.
<br></br>
    * Type: if
<br></br>


## Related Flows
* [Task List [Automatic]](Task%20List%20[Automatic].md)
* [Job List [Automatic]](Job%20List%20[Automatic].md)
* [Date Calculator [Dependent]](Date%20Calculator%20[Dependent].md)


## Workflow End
A. First End:  
    &emsp; 1. "**HTTP** - Date Calculator [Dependent]"  
    &emsp; 2. "**Update item** - Job Name Row First Task on Task List"


## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20Capacities/AllItems.aspx" target="_blank">Task Capacities</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The links above point to the lists present on the <b>Bracebridge UBF</b> subsite, however Flow will update the equivalent lists in each set subsite.</p>
</div>


## Excel Spreadsheets Involved in the Process
* There is no excel spreadsheets involved in the process.


## Example of Execution

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Triggering and executing Flow takes a few minutes to complete, although in the demonstrations below it appears to take less time.</p>
</div>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>This Flow is only triggered by "Job List [Automatic]" or by "Task List [Automatic]".</p>
</div>

<a class="" data-lightbox="Adding a Job and its Tasks to the Task List" href="../../../_static/flows/Bell - Bracebridge UBF - Job List [Automatic]_Adding New Tasks.gif" title="Adding a Job and its Tasks to the Task List" data-title="Adding a Job and its Tasks to the Task List"><img src="../../../_static/flows/Bell - Bracebridge UBF - Job List [Automatic]_Adding New Tasks.gif" class="align-center" width="800px" height="500px" alt="Adding a Job and its Tasks to the Task List">
</a>