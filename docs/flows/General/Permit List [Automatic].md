# Permit List [Automatic]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/193e769a-ba57-4ef8-9c9a-925a8ecc454c/details" target="_blank">Flow Link</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description



## Trigger Action
When an item is created or modified in the **Permit List**.


## Variables
* **siteAddress**: **String** type variable that stores the address of the SharePoint subsite.
<br></br>

* **listsNames**: **Object** type variable used to store the name of the SharePoint lists used in the Flow and their respective IDs.
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
A. First End:  
    &emsp; 1. "**Condition** - If Task Had Its Status, StartDate or DueDate changed"  
    &emsp; 2. "**Case** True"  
    &emsp; 3. "**HTTP** - Task Capacities [Dependent]"  

B. Second End:  
    &emsp; 1. "**Condition** - If Task Had Its Status, StartDate or DueDate changed"  
    &emsp; 2. "**Case** False"  
    &emsp; 3. "Terminate"


## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The links above point to the lists present on the <b>Bracebridge UBF</b> subsite, however Flow will update the equivalent lists in each set subsite.</p>
</div>


## Excel Spreadsheets Involved in the Process
* There is no excel spreadsheets involved in the process.


## Example of Execution