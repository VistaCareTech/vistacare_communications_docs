# Bell - Bracebridge UBF - Task List [Automatic]

<a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/b7692d94-0a89-4d2e-a962-3f1ca8bcb6f0/details" target="_blank">Flow Link</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>notify.engineering account owns this Flow. If you are not a co-owner you will not be able to access it.</p>
</div>

## Description
Initial flow in the process of automatically updating task dates present in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>. It plays the role of identifying whether the modification that triggered the Flow matches what was expected. If so, it calls ***Bell - Bracebridge UBF - Task Capacities [Dependent] Flow*** which will execute the next part in the process of automatically updating the dates in the Task List.

## Trigger Action
When an item is created or modified in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>.

## Decision Points
* **Condition - If Task Had Its Status, StartDate or DueDate changed**: Condition used to allow the Flow to be executed only when the modification that generated the trigger was in one of the attributes that affect the dates (**Status**, **StartDate** and **DueDate**).
<br></br>
    * Type: if
<br></br>
* **Condition**: Condition used to identify whether the Status attribute was changed to **Completed**, and then direct Flow to the appropriate action.
<br></br>
    * Type: if
<br></br>
* **Condition 2**: Condition used to identify whether the Status attribute was changed to **In Progress**, and then direct Flow to the appropriate action.
<br></br>
    * Type: if

## Workflow End
* Condition - If Task Had Its Status, StartDate or DueDate changed > Case False > Terminate action
* Condition > Case False > Condition 2 > Case False > Terminate action
* HTTP action (***Bell - St Charles - Task Capacities [Dependent] Flow***)

## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>

## Excel Spreadsheets Involved in the Process


## Video to GIF (Example of execution)