# Daily Update of Lists by Subsite [Schedule]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/7d8c6806-8952-4cd7-824b-c26c6d712bc8/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Flow used to trigger the execution of other Flows on a daily basis, which are responsible for updating Sharepoint List. Also responsible for passing on the necessary parameters for the execution of these other Flows.


## Trigger Action
Flow is automatically activated daily at sunset.

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>If necessary, it can be configured to trigger several times a day at different times.</p>
</div>


## Variables
* **parameters**: **Array** type variable that stores the **siteAddress**, **katapultFolder**, **timeToStart** and **startDateRule** values ​​in **Object** format.
<br></br>
    * **siteAddress**: is the address of the SharePoint subsite to have its lists updated.
        * Type: String
        * Example: "https://vistacaretech.sharepoint.com/sites/engineering/"
<br></br>
    * **katapultFolder**: is the Katapult Folder path where the project jobs are.
        * Type: String
        * Example: "Xplore/Elgin"
<br></br>
    * **timeToStart**: is the rule that determines the time for the update to start.
        * Type: Expression
        * Example: concat(substring(body('Get_forecast_for_today')?['responses']?['almanac']?['sunset'], 0, 19), 'Z')
<br></br>
    * **startDateRule [optional]**: is the rule that determines which days of the week Flow will also update the previous days and the number of previous days to be updated. Where the key represents the day of the week from Sunday(0) to Saturday(6) and the value represents the number of previous days to be updated. 
        * Type: Object
        * Example: {"0": -7, "3": -1} - On Sundays it updates data for the last 7 days, including the current day. And on Wednesdays it updates the data for the last day, including the current day.
<br></br>

* **listsNames**: **Object** type variable used to store the name of the SharePoint lists used in the Flow and their respective IDs when executing the "Apply to each siteAddress" action.
<br></br>


## Decision Points
There is no decision point.


## Related Flows
* [Update of Lists related to Field Survey [Dependent]](../General/Update%20of%20Lists%20Related%20to%20Field%20Survey%20[Dependent].md)
* [Get SharePoint Lists IDs [Dependent]](../General/Get%20SharePoint%20Lists%20IDs%20[Dependent].md)


## Workflow End
A. First End:  
    &emsp; 1. "**Apply to each** siteAddress"  
    &emsp; 2. "**HTTP** - Update of Lists related to Field Survey [Dependent]"


## SharePoint Lists Affected by the Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Field_Collection/Group%20Dates.aspx" target="_blank">Daily Field Collections</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Deficiency%20Field%20Collections/AllItems.aspx" target="_blank">Deficiency Field Recollections</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Deficiency%20Field%20Collections%20%20Missed/AllItems.aspx" target="_blank">Deficiency Field Collections - Missed</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Field%20Pre%20QC/Grouped%20by%20date.aspx" target="_blank">Field Pre QC</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The links above point to the lists present on the <b>Engineering</b> subsite, however Flow will update the equivalent lists in each set subsite.</p>
</div>


## Excel Spreadsheets Involved in the Process
There is no excel spreadsheets involved in the process.


## Example of Execution