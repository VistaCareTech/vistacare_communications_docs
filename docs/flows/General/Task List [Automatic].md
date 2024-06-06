# Task List [Automatic]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/193e769a-ba57-4ef8-9c9a-925a8ecc454c/details" target="_blank">Flow Link</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Initial flow in the process of automatically updating task dates present in the **Task List**. It plays the role of identifying whether the modification that triggered the Flow matches what was expected. If so, it calls **Task Capacities [Dependent]** Flow which will execute the next part in the process of automatically updating the dates in the Task List.


## Trigger Action
When an item is created or modified in the **Task List**.


## Variables
* **siteAddress**: **String** type variable that stores the address of the SharePoint subsite.
<br></br>

* **listsNames**: **Object** type variable used to store the name of the SharePoint lists used in the Flow and their respective IDs.
<br></br>

* **taskID**: **Integer** type variable used to store the ID of the task that triggered the Flow.
<br></br>


## Decision Points
* **Condition - If Task Had Its Status, StartDate or DueDate changed**: Condition used to allow the Flow to be executed only when the modification that generated the trigger was in one of the attributes that affect the dates (**Status**, **StartDate** and **DueDate**).
<br></br>
    * Type: if
<br></br>

* **Condition - If Task Has Status Completed**: Condition used to identify whether the Status attribute was changed to **Completed**, and then direct Flow to the appropriate action.
<br></br>
    * Type: if
<br></br>

* **Condition - If Task Has Status In Progress**: Condition used to identify whether the Status attribute was changed to **In Progress**, and then direct Flow to the appropriate action.
<br></br>
    * Type: if


## Related Flows
* [Task Capacities [Dependent]](Task%20Capacities%20[Dependent].md)
* [Date Calculator [Dependent]](Date%20Calculator%20[Dependent].md)
* [Get SharePoint Lists IDs [Dependent]](../General/Get%20SharePoint%20Lists%20IDs%20[Dependent].md)


## Workflow End
1. "**Condition** - If Task Had Its Status, StartDate or DueDate changed"  
    **->** "**Case** True"
    **->** "**HTTP** - Task Capacities [Dependent]"  
<br></br>

2. "**Condition** - If Task Had Its Status, StartDate or DueDate changed"  
    **->** "**Case** False"
    **->** "Terminate"
<br></br>


## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The links above point to the lists present on the **Bracebridge UBF** subsite, however Flow will update the equivalent lists in each set subsite.</p>
</div>


## Excel Spreadsheets Involved in the Process
* There is no excel spreadsheets involved in the process.


## Example of Execution