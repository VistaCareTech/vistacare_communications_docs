# 12 - Get Daily QGIS Process From Excel Spreadsheet

## Description
Uses data contained in Excel spreadsheets to add information regarding HLD processes to Sharepoint Lists. The data contained in the excel spreadsheets is obtained using the code QueriesHLD_Daily.py, which must be run manually, similar to what occurred with the process of obtaining data referring to the Daily Field Collection.

## Trigger Action
When a file is created or modified in the [QGIS Import](https://vistacaretech.sharepoint.com/:f:/s/engineering/ElFRUrUbNuZAjkyo3kK-Lj4BtqGnchckDbE6-8GuURn-2w?e=M0bUCC) folder (Engineering site)

## Decision Points
* **Condition 3**: Condition used to prevent Flow from being executed twice in sequence, since the "Create Table" action modifies the Excel spreadsheet and this is one of the triggers for activating Flow.
<br></br>
    * Type: if
<br></br>
* **Switch:** Identifies which of the 4 possible Excel spreadsheets was created or modified and directs Flow to the actions relating to each case.
<br></br>
    * Type: switch
    * Cases - Case 1: JobListHLD, Case 2: DailyQgisImport, Case 3: DailyHLD, Case 4: DailyHLDQC

## Workflow End
* Condition 3 > Case True > Terminate action
* Update Item action ([Job List](https://vistacaretech.sharepoint.com/sites/engineering/Lists/Job%20List/AllItems.aspx))
* Create Item action ([QGIS Import](https://vistacaretech.sharepoint.com/sites/engineering/Lists/QGIS%20Import/AllItems.aspx))
* Create Item action ([HLD](https://vistacaretech.sharepoint.com/sites/engineering/Lists/HLD/AllItems.aspx))
* Create Item action ([HLD QC](https://vistacaretech.sharepoint.com/sites/engineering/Lists/HLD%20QC/AllItems.aspx))

## SharePoint Lists Affected by the Workflow
* [Job List](https://vistacaretech.sharepoint.com/sites/engineering/Lists/Job%20List/AllItems.aspx)
* [QGIS Import](https://vistacaretech.sharepoint.com/sites/engineering/Lists/QGIS%20Import/AllItems.aspx)
* [HLD](https://vistacaretech.sharepoint.com/sites/engineering/Lists/HLD/AllItems.aspx)
* [HLD QC](https://vistacaretech.sharepoint.com/sites/engineering/Lists/HLD%20QC/AllItems.aspx)

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>All lists belong to Engineering site.</p>
</div>

## Excel Spreadsheets Involved in the Process
* [JobListHLD.xlsx](https://vistacaretech.sharepoint.com/:x:/s/engineering/EavIAQHk8lVCp_eCj_eZhXMBlZWXHnbXwpsJ8NVPu-1wKA?e=uSqAw0)
* [DailyQgisImport.xlsx](https://vistacaretech.sharepoint.com/:x:/s/engineering/ESadELGi-_lMgRxLt0LZG6IBBPs9nmuztFjFL9xAbNuFyA?e=ZVSv0h)
* [DailyHLD.xlsx](https://vistacaretech.sharepoint.com/:x:/s/engineering/EYj9SwCVdHhIv3rZjQQXnxgB_Rsc3-7IgdEpJZRSVI-99g?e=1e9RrU)
* [DailyHLDQC.xlsx](https://vistacaretech.sharepoint.com/:x:/s/engineering/EdqvLrhXdCZPutcLHu9g4KMBZ1jeqKZErf8Ov486PyKOSw?e=J8HXiU)
* <a href="https://vistacaretech.sharepoint.com/:x:/s/engineering/EdqvLrhXdCZPutcLHu9g4KMBZ1jeqKZErf8Ov486PyKOSw?e=J8HXiU" target="_blank">DailyHLDQC.xlsx</a>

## Video to GIF (Example of execution)