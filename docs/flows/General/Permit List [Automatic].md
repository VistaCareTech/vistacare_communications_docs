# Permit List [Automatic]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/a5db4067-098b-422e-9757-55a69159de16/details" target="_blank">Flow Link</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Flow used to update Permit tasks in the **Task List** based on information present in the **Permit Lists**.

## Trigger Action
When an item is created or modified in the **Permit List**.


## Variables
* **siteAddress**: **String** type variable that stores the address of the SharePoint subsite.
<br></br>

* **listsNames**: **Object** type variable used to store the name of the SharePoint lists used in the Flow and their respective IDs.
<br></br>


## Decision Points
* **Condition - If the Column Has Changed**: Condition used to allow the Flow to be executed only when the modification that triggered the Flow occurred in one of the **Yes/No** Type Columns (**Ready for Pole Modeling**, **Pole Profiles updated**, **Modelling/PP QC**, **Ready for CAD Plans**, **Ready for Final PEng Review**, **Package Corrections Complete**, **Permit Signed and Ready for Submission**, **Updates Required**, **Re-Signed and Ready for Submission**, and **Permit Submitted**).
<br></br>
    * Type: if
<br></br>


## Related Flows
* [Get SharePoint Lists IDs [Dependent]](../General/Get%20SharePoint%20Lists%20IDs%20[Dependent].md)


## Workflow End
A. First End:  
    &emsp; 1. "**Apply to each** - Column"  
    &emsp; 1. "**Condition** - If the Column Has Changed"  
    &emsp; 3. "**Case** True"  
    &emsp; 4. "**Update item** - Task List"  

B. Second End:  
    &emsp; 1. "**Apply to each** - Column"  
    &emsp; 2. "**Condition** - If the Column Has Changed"  
    &emsp; 3. "**Case** False"  
    &emsp; 4. "Terminate"


## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/xplore/629E/Lists/Tasks/AllItems.aspx" target="_blank">Task List</a>

* <a href="https://vistacaretech.sharepoint.com/sites/engineering/xplore/Lists/Lawrence%20Station%20Permit%20List/AllItems.aspx" target="_blank">Lawrence Station Permit List</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The links above point to the lists present on the <b>Xplore</b> subsite, however Flow will update the equivalent lists in each set subsite.</p>
</div>


## Excel Spreadsheets Involved in the Process
* There is no excel spreadsheets involved in the process.


## Example of Execution