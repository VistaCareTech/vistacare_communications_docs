# Bell - Bracebridge UBF - Task Capacities [Dependent]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/c5070d7b-449f-42f7-9a3a-e93cdd42d7a3/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>

## Description
Flow used to obtain data from the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20Capacities/AllItems.aspx" target="_blank">Task Capacities</a> list referring to the **Job** to which the **Task** is related. Then pass this data to the next Flow (***Bell - Bracebridge UBF - Date Calculator [Dependent] Flow***).

## Trigger Action
When an HTTP request is received from:
* ***Bell - Bracebridge UBF - Job List [Automatic] Flow***
* ***Bell - Bracebridge UBF - Task List [Automatic] Flow***

## Decision Points
* **Condition - If There Are No Tasks For This Job in The Task List Yet**: Condition used to identify whether the **Job** already has tasks related to it in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>.
<br></br>
    * Type: if
<br></br>
* **Condition - If Has Active Task Sync**: Condition used to identify whether the **Job** in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a> has any task assigned as **Active Task Sync**.
<br></br>
    * Type: if
<br></br>

## Workflow End
* HTTP action (***Bell - Bracebridge UBF - Date Calculator [Dependent] Flow***)

## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20Capacities/AllItems.aspx" target="_blank">Task Capacities</a>

## Excel Spreadsheets Involved in the Process


## Example of Execution

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Triggering and executing Flow takes a few minutes to complete, although in the demonstrations below it appears to take less time.</p>
</div>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>This Flow is only triggered by "Bell - Bracebridge UBF - Job List [Automatic]" or by "Bell - Bracebridge UBF - Task List [Automatic]".</p>
</div>

<a class="" data-lightbox="Adding a Job and its Tasks to the Task List" href="../../../_static/flows/Bell - Bracebridge UBF - Job List [Automatic]_Adding New Tasks.gif" title="Adding a Job and its Tasks to the Task List" data-title="Adding a Job and its Tasks to the Task List"><img src="../../../_static/flows/Bell - Bracebridge UBF - Job List [Automatic]_Adding New Tasks.gif" class="align-center" width="800px" height="500px" alt="Adding a Job and its Tasks to the Task List">
</a>