# Daily Update of Lists by Subsite [Schedule]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/d575c968-e542-47d7-9bfd-91c8a389f683/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>

## Description
Flow used to add **Daily Field Collection** data contained in Excel spreadsheets to Sharepoint lists. The data contained in Excel spreadsheets is obtained through the **KatapultTracker.py** code.

## Trigger Action
Flow is automatically activated daily at sunset.

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>If necessary, it can be configured to trigger several times a day at different times.</p>
</div>

## Variables
* **parameters**: **Array** type variable that stores the **siteAddress**, **katapultFolder**, **timeToStart** and **startDateRule** values ​​in **Object** format.
<br></br>
    * Type: Switch
    * Cases - Case 1: DailyFieldCollections, Case 2: DailyUpdatedJobList
    * siteAddress: Switch
    * katapultFolder:
    * timeToStart: Switch
    * startDateRule:

    is the address of the subsite to have its lists updated

This is the address of Katapult, the folder where the project jobs are located.

This is the rule that determines the time for the update to start

This is the rule that determines which days of the week Flow will also update the previous days and the number of previous days to be updated.
<br></br>


    "siteAddress": "https://vistacaretech.sharepoint.com/sites/engineering/",
    "katapultFolder": "Xplore/Elgin",
    "timeToStart": "
",
    "startDateRule": {
      "0": -7,
      "3": -1
    }


* **path**: **String** type variable that stores the path where Excel files are saved.
<br></br>

* **date**: **String** type variable used to store the initial date and incremented date when Flow execution occurs on the days of the week in which Flow is configured to update field collection data from previous days to the current date.
<br></br>

* **listsNames**: **Object** type variable used to store the name of the SharePoint lists used in the Flow and their respective IDs when executing the "Apply to each siteAddress" action.
<br></br>

* **siteAddress**: **String** type variable that stores the address of the SharePoint subsite when executing the "Apply to each siteAddress" action.
<br></br>

* **katapultFolder**: **String** type variable that stores the Katapult Folder path when executing the "Apply to each siteAddress" action.
<br></br>

* **driveID**: **String** type variable that stores the Document Library Drive ID of the SharePoint subsite when executing the "Apply to each siteAddress" action.
<br></br>

* **statusValues**: **Array** type variable used to store the "Job Status" present in the "Job List" and modify them based on some conditions.
<br></br>

## Decision Points
* There is no decision point.

## Workflow End
* "**Do until** - Variable date eq Current Date" > "**Apply to each** file extracted in the extract folder action" > "**Switch** - Extracted files" >  "**Case** DailyFieldCollections.xlsx" > "**Apply to each** DailyFieldCollections row" > "**Switch** - DailyFieldCollections Status" > "**Case** Collected" > "**Create item** - Daily Field Collections" AND "**Create item** - Field Pre QC"
<br></br>

* Condition 3 > Case True > Terminate action
* Update Item action (<a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>)
* Create Item action (<a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/QGIS%20Import/AllItems.aspx" target="_blank">QGIS Import</a>)
* Create Item action (<a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/HLD/AllItems.aspx" target="_blank">HLD</a>)
* Create Item action (<a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/HLD%20QC/AllItems.aspx" target="_blank">HLD QC</a>)

## Other Flows Triggered
[Update of Lists related to Field Survey [Dependent]](../General/Update%20of%20Lists%20related%20to%20Field%20Survey%20[Dependent].md)

## SharePoint Lists Affected by the Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/QGIS%20Import/AllItems.aspx" target="_blank">QGIS Import</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/HLD/AllItems.aspx" target="_blank">HLD</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/HLD%20QC/AllItems.aspx" target="_blank">HLD QC</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>All lists belong to Engineering site.</p>
</div>

## Excel Spreadsheets Involved in the Process
* <a href="https://vistacaretech.sharepoint.com/:x:/s/engineering/EavIAQHk8lVCp_eCj_eZhXMBlZWXHnbXwpsJ8NVPu-1wKA?e=uSqAw0" target="_blank">JobListHLD.xlsx</a>
* <a href="https://vistacaretech.sharepoint.com/:x:/s/engineering/ESadELGi-_lMgRxLt0LZG6IBBPs9nmuztFjFL9xAbNuFyA?e=ZVSv0h" target="_blank">DailyQgisImport.xlsx</a>
* <a href="https://vistacaretech.sharepoint.com/:x:/s/engineering/EYj9SwCVdHhIv3rZjQQXnxgB_Rsc3-7IgdEpJZRSVI-99g?e=1e9RrU" target="_blank">DailyHLD.xlsx</a>
* <a href="https://vistacaretech.sharepoint.com/:x:/s/engineering/EdqvLrhXdCZPutcLHu9g4KMBZ1jeqKZErf8Ov486PyKOSw?e=J8HXiU" target="_blank">DailyHLDQC.xlsx</a>

## Example of execution