# Date Calculator [Dependent]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/b815d044-7c10-4fa8-b8b9-3a8fe29b79e6/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Flow used to calculate the dates of tasks present in the **Task List**.


## Trigger Action
When an HTTP request is received from **Task Capacities [Dependent]** Flow.


## Variables
* **First Task ID**: **Integer** type variable used to store the ID of the first **Task** referring to this **Job** in the **Task List**, that is, the ID of the **Parent Task**.
<br></br>

* **Active Task Sync**: **Float** type variable used to store the **Step**/**#** of the first type of **Task** present in the **Task Capacities** SharePoint list referring to a **Job** that has the attribute **Active Task Sync** in the **Job List** SharePoint list.
<br></br>


## Decision Points
* **Condition - If Variables Tasks contains Task**: Condition used to identify whether each task present in **Task Capacities** is part of the predefined tasks for the Job.
<br></br>
    * Type: if
<br></br>

* **Condition - Selecting the Start Date**: Condition used to identify whether the task is already present in the **Task List**. If so, Flow is directed to the next condition. If not, task receives the **Start Date** defined in the **Job List**.
<br></br>
    * Type: if
<br></br>

* **Condition - Does the Task Have Not Started Status and Date Locked False**: Condition used to identify whether the task present in the **Task List** has the **Status Not Started** and the **Date Locked** attribute is false. If so, the task's **Start Date** is defined based on the **Due Date** of the previous task. If not, the **Start Date** of the task already present in the **Task List** is maintained.
<br></br>
    * Type: if
<br></br>

* **Switch - If Start Date is Sat or Sun**: Identifies the day of the week for the Start Date, and if it is Saturday or Sunday, the date is moved to the nearest Monday.
<br></br>
    * Type: switch
    * Cases - Case Sat: 6, Case Sun: 0
<br></br>

* **Condition - Create or Update Task**: Condition that directs Flow to the Create Item action if the task does not yet exist in the **Task List**, or to Update Item if the task already exists.
<br></br>
    * Type: if
<br></br>

* **Condition - If task Not Started**: Condition that identifies whether the task has the **Not Started Status**. If so, the Flow is directed to the **Update Item** action configured to receive a new **Target Start Date** in addition to other attributes such as **Target Due Date**. If not, the Flow is directed to the next condition.
<br></br>
    * Type: if

* **Condition - If task In Progress**: Condition that identifies whether the task has the **In Progress Status**. If so, the Flow is directed to the **Update Item** action configured to receive a new **Target Due Date**. If not, the Flow is directed to an **Update Item** where neither the **Target Start Date** nor the **Target Due Date** are updated.
<br></br>
    * Type: if


## Related Flows
* [Task List [Automatic]](Task%20List%20[Automatic].md)
* [Job List [Automatic]](Job%20List%20[Automatic].md)
* [Task Capacities [Dependent]](Task%20Capacities%20[Dependent].md)


## Workflow End
A. First End:  
    &emsp; 1. "**Apply to each**"  
    &emsp; 2. "**Condition** - If Variables Tasks contains Task"  
    &emsp; 3. "**Case** True"  
    &emsp; 4. "**Condition** - Create or Update Task"  
    &emsp; 5. "**Case** True"  
    &emsp; 6. "**Create Item** - Task List"

B. Second End:  
    &emsp; 1. "**Apply to each**"  
    &emsp; 2. "**Condition** - If Variables Tasks contains Task"  
    &emsp; 3. "**Case** True"  
    &emsp; 4. "**Condition** - Create or Update Task"  
    &emsp; 5. "**Case** False"  
    &emsp; 6. "**Condition** - If task Not Started"  
    &emsp; 7. "**Case** True"  
    &emsp; 8. "**Update Item** - Task List 1"

C. Third End:  
    &emsp; 1. "**Apply to each**"  
    &emsp; 2. "**Condition** - If Variables Tasks contains Task"  
    &emsp; 3. "**Case** True"  
    &emsp; 4. "**Condition** - Create or Update Task"  
    &emsp; 5. "**Case** False"  
    &emsp; 6. "**Condition** - If task Not Started"  
    &emsp; 7. "**Case** False"  
    &emsp; 8. "**Condition** - If task In Progress"  
    &emsp; 9. "**Case** True"  
    &emsp; 10. "**Update Item** - Task List 2"

D. Fourth End:  
    &emsp; 1. "**Apply to each**"  
    &emsp; 2. "**Condition** - If Variables Tasks contains Task"  
    &emsp; 3. "**Case** True"  
    &emsp; 4. "**Condition** - Create or Update Task"  
    &emsp; 5. "**Case** False"  
    &emsp; 6. "**Condition** - If task Not Started"  
    &emsp; 7. "**Case** False"  
    &emsp; 8. "**Condition** - If task In Progress"  
    &emsp; 9. "**Case** False"  
    &emsp; 10. "**Update Item** - Task List 3"

E. Fifth End:  
    &emsp; 1. "**Apply to each**"  
    &emsp; 2. "**Condition** - If Variables Tasks contains Task"  
    &emsp; 3. "**Case** False"  
    &emsp; 4. "Terminate"  


## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Task%20List/1000%20Tasks.aspx" target="_blank">Task List</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The links above point to the lists present on the <b>Bracebridge UBF</b> subsite, however Flow will update the equivalent lists in each set subsite.</p>
</div>


## Excel Spreadsheets Involved in the Process
* There is no excel spreadsheets involved in the process.


## Example of Execution

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Triggering and executing Flow takes a few minutes to complete, although in the demonstrations below it appears to take less time.</p>
</div>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>This Flow is only triggered by "Task Capacities [Dependent]", while this other is only triggered by "Job List [Automatic]" or by "Task List [Automatic]".</p>
</div>

<a data-fancybox="Adding a Job and its Tasks to the Task List" href="../../../_static/flows/job_list/bell_-_bracebridge_ubf_-_job_list_[automatic]_adding_new_tasks.mp4" data-caption="Adding a Job and its Tasks to the Task List">
  <img src="../../../_static/flows/job_list/bell_-_bracebridge_ubf_-_job_list_[automatic]_adding_new_tasks_thumbnail.jpg" alt="Adding new Jobs to the Job List" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>