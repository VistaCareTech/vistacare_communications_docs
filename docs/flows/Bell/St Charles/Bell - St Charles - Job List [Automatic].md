# Bell - St Charles - Job List [Automatic]

<a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/0eb9728c-cb6b-49c1-92d0-ec233dbeddf3/details" target="_blank">Flow Link</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>notify.engineering account owns this Flow. If you are not a co-owner you will not be able to access it.</p>
</div>

## Description
Flow used to add Jobs and their data from the Katapult API to the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a> and also to add a Job and its tasks to the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Tasks/1000%20Tasks.aspx" target="_blank">Task List</a>.

## Trigger Action
When an item is created or modified in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>.

## Decision Points
* **Condition - If a job was created with New as name**: Condition used to identify whether the modification that triggered the Flow is the command to obtain the Jobs recently created in Katapult. If so, Flow is directed to perform the necessary actions to update the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a> with the most recent Jobs. If not, then Flow is directed to the next condition.
<br></br>
    * Type: if
<br></br>
* **Condition - If the Job received a Start Date**: Condition used to identify whether the Job that triggered the Flow had its **Start Date** changed. If so, then ***Bell - St Charles - Task Capacities [Dependent] Flow*** is called to start the process of creating tasks in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Tasks/1000%20Tasks.aspx" target="_blank">Task List</a>.
<br></br>
    * Type: if
<br></br>
* **Condition 7**: Condition used to check each Job found in the Katapult API, and identify if it is not present in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>, and if the Job is not present, then Flow is directed to the actions that will add the missing Job.
<br></br>
    * Type: if
<br></br>
* **Condition 6**: Condition used to identify whether the Job found in the Katapult API has the **date_created** attribute. If so, the Job is added to the list of Jobs that will be added to the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>.

## Workflow End
* Condition - If the Job received a Start Date > Case False > Condition - If the Job received a Start Date > Case False > Terminate action
* Condition > Case False > Condition 2 > Case False > Terminate action
* Create Item action (<a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>)
* HTTP action (***Bell - St Charles - Task Capacities [Dependent] Flow***)

## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/StCharles/Lists/Tasks/1000%20Tasks.aspx" target="_blank">Task List</a>

## Excel Spreadsheets Involved in the Process


## Example of Execution

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>Triggering and executing Flow takes a few minutes to complete, although in the demonstrations below it appears to take less time.</p>
</div>

* **Adding new Jobs to the Job List**

<a class="" data-lightbox="Adding new Jobs to the Job List" href="../../../_static/flows/Bell - St Charles - Job List [Automatic]_Adding New Jobs.gif" title="Adding new Jobs to the Job List" data-title="Adding new Jobs to the Job List"><img src="../../../_static/flows/Bell - St Charles - Job List [Automatic]_Adding New Jobs.gif" class="align-center" width="800px" height="500px" alt="Adding new Jobs to the Job List">
</a>

* **Adding a Job and its Tasks to the Task List**

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The flows "Bell - St Charles - Task Capacities [Dependent]" and "Bell - St Charles - Date Calculator [Dependent]" participate in this process.</p>
</div>

<a class="" data-lightbox="Adding a Job and its Tasks to the Task List" href="../../../_static/flows/Bell - St Charles - Job List [Automatic]_Adding New Tasks.gif" title="Adding a Job and its Tasks to the Task List" data-title="Adding a Job and its Tasks to the Task List"><img src="../../../_static/flows/Bell - St Charles - Job List [Automatic]_Adding New Tasks.gif" class="align-center" width="800px" height="500px" alt="Adding a Job and its Tasks to the Task List">
</a>