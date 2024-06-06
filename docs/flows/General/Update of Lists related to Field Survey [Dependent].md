# Update of Lists related to Field Survey [Dependent]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/d575c968-e542-47d7-9bfd-91c8a389f683/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>

## Description
Flow used to add **Daily Field Collection** data contained in Excel spreadsheets to Sharepoint lists. The data contained in Excel spreadsheets is obtained through the **KatapultTracker.py** code.

## Trigger Action
Flow is triggered from a call in another Flow.

## Variables
* **siteAddress**: **String** type variable that stores the address of the SharePoint subsite.
<br></br>

* **katapultFolder**: **String** type variable that stores the Katapult Folder path.
<br></br>

* **listsNames**: **Object** type variable used to store the name of the SharePoint lists used in the Flow and their respective IDs.
<br></br>

* **date**: **String** type variable used to store the initial date and incremented date when Flow execution occurs on the days of the week in which Flow is configured to update field collection data from previous days to the current date.
<br></br>

* **path**: **String** type variable that stores the path where Excel files are saved.
<br></br>

* **driveID**: **String** type variable that stores the Document Library Drive ID of the SharePoint subsite.
<br></br>

* **statusValues**: **Array** type variable used to store the "Job Status" present in the "Job List" and modify them based on some conditions.
<br></br>

## Decision Points
* **Condition - is startDateRule Passed as a Parameter to Flow**: Condition used to check whether the startDateRule is among the parameters passed to Flow.
<br></br>
    * Type: If
<br></br>

* **Condition - Does the startDateRule Contain the Current Day**: Condition used to check whether the current day of the week is present in the startDateRule parameter, and if so, then the startDateRule is used to define the start date.
<br></br>
    * Type: If
<br></br>

* **Switch - Extracted files**: Identifies which of the 2 possible Excel spreadsheets was created and directs Flow to the actions relating to each case.
<br></br>
    * Type: Switch
    * Cases - Case 1: DailyFieldCollections, Case 2: DailyUpdatedJobList
<br></br>

* **Switch - DailyFieldCollections Status**: Identifies which of the 3 possible collection status the field collection belongs to and directs Flow to actions relating to each case.
<br></br>
    * Type: Switch
    * Cases - Case 1: Collected, Case 2: Recollected, Case 3: Missed
<br></br>

* **Condition - Is Date of the Obtained Data Equal to Current Date**: Condition used to prevent the **Job List** from being updated with outdated data.
<br></br>
    * Type: If
<br></br>

* **Condition - Job is already in Job List**: Condition used to identify whether the Job is already present in the **Job List**. If so, the Job is just updated in the **Job List**. If not, the Job is created in the **Job List**.
<br></br>
    * Type: If
<br></br>

## Related Flows
* [Daily Update of Lists by Subsite [Schedule]](Daily%20Update%20of%20Lists%20by%20Subsite%20[Schedule].md)

## Workflow End
1. "**Do until** - Variable date eq Current Date"  
    **->** "**Apply to each** file extracted in the extract folder action"  
    **->** "**Switch** - Extracted files"  
    **->** "**Case** DailyFieldCollections.xlsx"  
    **->** "**Apply to each** DailyFieldCollections row"  
    **->** "**Switch** - DailyFieldCollections Status"  
    **->** "**Case** Collected"  
    **->** "**Create item** - Daily Field Collections" & "**Create item** - Field Pre QC"
<br></br>

2. "**Do until** - Variable date eq Current Date"  
    **->** "**Apply to each** file extracted in the extract folder action"  
    **->** "**Switch** - Extracted files"  
    **->** "**Case** DailyFieldCollections.xlsx"  
    **->** "**Apply to each** DailyFieldCollections row"  
    **->** "**Switch** - DailyFieldCollections Status"  
    **->** "**Case** Recollected"  
    **->** "**Create item** - Deficiency Field Recollections"
<br></br>

3. "**Do until** - Variable date eq Current Date"  
    **->** "**Apply to each** file extracted in the extract folder action"  
    **->** "**Switch** - Extracted files"  
    **->** "**Case** DailyFieldCollections.xlsx"  
    **->** "**Apply to each** DailyFieldCollections row"  
    **->** "**Switch** - DailyFieldCollections Status"  
    **->** "**Case** Missed"  
    **->** "**Create item** - Deficiency Field Recollections - Missed"
<br></br>

4. "**Do until** - Variable date eq Current Date"  
    **->** "**Apply to each** file extracted in the extract folder action"  
    **->** "**Switch** - Extracted files"  
    **->** "**Case** DailyUpdatedJobList.xlsx"  
    **->** "**Condition** - Is Date of the Obtained Data Equal to Current Date"  
    **->** "**Case** True"  
    **->** "**Apply to each** - DailyUpdatedJobList Table"  
    **->** "**Condition** - Job is already in Job List"  
    **->** "**Case** True"  
    **->** "**Update item** - Job List
<br></br>

5. "**Do until** - Variable date eq Current Date"  
    **->** "**Apply to each** file extracted in the extract folder action"  
    **->** "**Switch** - Extracted files"  
    **->** "**Case** DailyUpdatedJobList.xlsx"  
    **->** "**Condition** - Is Date of the Obtained Data Equal to Current Date"  
    **->** "**Case** True"  
    **->** "**Apply to each** - DailyUpdatedJobList Table"  
    **->** "**Condition** - Job is already in Job List"  
    **->** "**Case** False"  
    **->** "**Create item** - Job List
<br></br>

6. "**Do until** - Variable date eq Current Date"  
    **->** "**Apply to each** file extracted in the extract folder action"  
    **->** "**Switch** - Extracted files"  
    **->** "**Case** DailyUpdatedJobList.xlsx"  
    **->** "**Condition** - Is Date of the Obtained Data Equal to Current Date"  
    **->** "**Case** False"  
    **->** "Terminate"
<br></br>

## SharePoint Lists Affected by the Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Field_Collection/Group%20Dates.aspx" target="_blank">Daily Field Collections</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Deficiency%20Field%20Collections/AllItems.aspx" target="_blank">Deficiency Field Recollections</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Deficiency%20Field%20Collections%20%20Missed/AllItems.aspx" target="_blank">Deficiency Field Collections - Missed</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Field%20Pre%20QC/Grouped%20by%20date.aspx" target="_blank">Field Pre QC</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The links above point to the lists present on the **Engineering** subsite, however Flow will update the equivalent lists in each set subsite.</p>
</div>

## Excel Spreadsheets Involved in the Process
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2Fengineering%2FShared%20Documents%2FField%20Survey%2FDaily%20Field%20Collections&viewid=08c9b4b0%2D1976%2D4850%2Da879%2D28ef79748a25" target="_blank">DailyFieldCollections.xlsx</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2Fengineering%2FShared%20Documents%2FField%20Survey%2FDaily%20Field%20Collections&viewid=08c9b4b0%2D1976%2D4850%2Da879%2D28ef79748a25" target="_blank">DailyUpdatedJobList.xlsx</a>

## Example of Execution