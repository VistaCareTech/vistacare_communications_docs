# Get SharePoint Lists IDs [Dependent]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/94f4b7c5-8033-45cb-8597-079af2998288/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Auxiliary Flow used to facilitate obtaining IDs from SharePoint lists.


## Trigger Action
When an HTTP request is received.


## Variables
* **listsNames**: **Object** type variable used to store the name of the requested SharePoint lists and their respective IDs.
<br></br>

* **driveID**: **String** type variable that stores the requested Document Library Drive ID of the SharePoint subsite.
<br></br>


## Decision Points
There is no decision point.


## Related Flows
It can be called from any other Flow.


## Workflow End
A. First End:  
    &emsp; 1. "**Apply to each** list"  
    &emsp; 2. "**Response**" with listsNames and driveID


## SharePoint Lists Affected by Workflow
Flow can get the ID of any SharePoint List passed as a parameter.


## Excel Spreadsheets Involved in the Process
There is no excel spreadsheets involved in the process.


## Example of Execution