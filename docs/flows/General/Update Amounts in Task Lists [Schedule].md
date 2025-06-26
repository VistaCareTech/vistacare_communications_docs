# Update Amounts in Task Lists [Schedule]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/bc1c4d79-e1d1-4c80-a58e-526b610513f9/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Scheduled flow that obtains data from the Excel spreadsheets present in the Documents of each area and also from the fdsa_boundaries table/layer of QGIS and then uses this data to update the values ​​of Actual Amount and Quote Amount present in the Tak Lists.


## Trigger Action
Flow is automatically activated daily, but it can be changed to activate more times a day if necessary.


## Variables
* **listsNames**: **Object** type variable used to store the name of the SharePoint lists used in the Flow and their respective IDs.
<br></br>

* **UpdatedOLT**: **Array** type variable that stores the OLTs that have been updated.
<br></br>


## Decision Points
* **Condition - If there is spreadsheet in documents**: Condition used to check if there is an Excel spreadsheet with the Summary of OLTs for each area.
<br></br>
    * Type: if
<br></br>

* **Condition - If the Row Contains an FSA**: Condition used to check if the FSA taken from the spreadsheet is not in the **Job List**, as well as data validation, and if so, then th FSA is added to **Job List**.
<br></br>
    * Type: if
<br></br>

* **Condition - Has Updates**: Condition used to check if the FSA has different values ​​than those already present in the **Task List**, and if so, then the Task List is updated.
<br></br>
    * Type: if
<br></br>

* **Condition - If FSA is not in Job List**: Condition used to check if the FSA taken from the spreadsheet is not in the **Job List**, and if so, then th FSA is added to **Job List**.
<br></br>
    * Type: if
<br></br>

* **Condition - If FSA Started to be Worked on in QGIS**: Condition used to check if the FSA started already has values ​​greater than 0 in the **fdsa_boundaries layer**. And if so, then update the values ​​in the **Task List**.
<br></br>
    * Type: if
<br></br>


## Workflow End
A. First End:  
    &emsp; 1. "**HTTP** - SELECT * in fdsa boundaries"  
    &emsp; 2. "**HTTP** - select * in peng scope"  
    &emsp; 3. "**Apply to each** - Subsite"  
    &emsp; 4. "**Apply to each** - FSA in Job List"  
    &emsp; 5. "**Condition** - If FSA Has Updates"  
    &emsp; 6. "**Case** True"  
    &emsp; 7. "**HTTP** - Task Capacities [Dependent]"  
    &emsp; 8. "**Update item** - Job List 3"  

B. Second End:  
    &emsp; 1. "**HTTP** - SELECT * in fdsa boundaries"  
    &emsp; 2. "**HTTP** - select * in peng scope"  
    &emsp; 3. "**Apply to each** - Subsite"  
    &emsp; 4. "**Apply to each** - FSA in Job List"  
    &emsp; 5. "**Condition** - If FSA Has Updates"  
    &emsp; 6. "**Case** False"  
    &emsp; 7. "Terminate"


## Related Flows
* [Get SharePoint Lists IDs [Dependent]](../General/Get%20SharePoint%20Lists%20IDs%20[Dependent].md)
* [Task Capacities [Dependent]](Task%20Capacities%20[Dependent].md)
* [Date Calculator [Dependent]](Date%20Calculator%20[Dependent].md)


## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/xplore/1190E/Lists/Task%20List1/1000%20Tasks.aspx" target="_blank">Task List</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/xplore/1190E/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The links above point to the lists present on the <b>Fox Harbour OLT - 1190E</b> subsite, however Flow will update the equivalent lists in each set subsite.</p>
</div>


## Related Documentation
   ### [Update of Task Lists](Update%20of%20Task%20Lists.md)
   ### [get_permit_number Azure Function](../../azure_functions/get_permit_number.md)


## Example of Execution

<a data-fancybox="Update Amounts in Task Lists [Schedule]" href="../../../_static/flows/Update Amounts in Task Lists [Schedule].mp4" data-caption="Update Amounts in Task Lists [Schedule]">
  <img src="../../../_static/flows/update_amounts_in_task_lists_[schedule]_thumbnail.jpg" alt="Update Amounts in Task Lists [Schedule]" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>