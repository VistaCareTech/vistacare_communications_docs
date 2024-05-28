# Date Calculator [Dependent]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/b815d044-7c10-4fa8-b8b9-3a8fe29b79e6/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>

## Description
Flow used to calculate the dates of tasks present in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>.

## Trigger Action
When an HTTP request is received from:
* ***Bell - Bracebridge UBF - Task Capacities [Dependent] Flow***

## Decision Points
* **Condition - If Variables Tasks contains Task**: Condition used to identify whether each task present in <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20Capacities/AllItems.aspx" target="_blank">Task Capacities</a> is part of the predefined tasks for the Job.
<br></br>
    * Type: if
<br></br>
* **Condition - Selecting the Start Date**: Condition used to identify whether the task is already present in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>. If so, Flow is directed to the next condition. If not, task receives the **Start Date** defined in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>.
<br></br>
    * Type: if
<br></br>
* **Condition 2**: Condition used to identify whether the task present in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a> has the **Status Not Started** and the **Date Locked** attribute is false. If so, the task's **Start Date** is defined based on the **Due Date** of the previous task. If not, the **Start Date** of the task already present in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a> is maintained.
<br></br>
    * Type: if
<br></br>
* **Switch - If Start Date is Sat or Sun**: Identifies the day of the week for the Start Date, and if it is Saturday or Sunday, the date is moved to the nearest Monday.
<br></br>
    * Type: switch
    * Cases - Case Sat: 6, Case Sun: 0
<br></br>
* **Condition - Create or Update Task**: Condition that directs Flow to the Create Item action if the task does not yet exist in the <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>, or to Update Item if the task already exists.
<br></br>
    * Type: if
<br></br>
* **Condition - If task Not Started**: Condition that identifies whether the task has the **Not Started Status**. If so, the Flow is directed to the **Update Item** action configured to receive a new **Start Date** in addition to other attributes such as **Due Date**. If not, the Flow is directed to an **Update Item** where the **Start Date** is not changed but the **Due Date** is changed.
<br></br>
    * Type: if

## Workflow End
* Condition - If Variables Tasks contains Task > Case False > Terminate action
* Condition - Create or Update Task > Case True > Create Item action (<a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>)
* Condition - Create or Update Task > Case False > Condition - If task Not Started > Case True > Update Item action (<a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>)
* Condition - Create or Update Task > Case False > Condition - If task Not Started > Case False > Update Item action (<a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>)

## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>

## Excel Spreadsheets Involved in the Process


## Example of Execution

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Triggering and executing Flow takes a few minutes to complete, although in the demonstrations below it appears to take less time.</p>
</div>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>This Flow is only triggered by "Bell - Bracebridge UBF - Task Capacities [Dependent]", while this other is only triggered by "Bell - Bracebridge UBF - Job List [Automatic]" or by "Bell - Bracebridge UBF - Task List [Automatic]".</p>
</div>

<a class="" data-lightbox="Adding a Job and its Tasks to the Task List" href="../../../_static/flows/Bell - Bracebridge UBF - Job List [Automatic]_Adding New Tasks.gif" title="Adding a Job and its Tasks to the Task List" data-title="Adding a Job and its Tasks to the Task List"><img src="../../../_static/flows/Bell - Bracebridge UBF - Job List [Automatic]_Adding New Tasks.gif" class="align-center" width="800px" height="500px" alt="Adding a Job and its Tasks to the Task List">
</a>