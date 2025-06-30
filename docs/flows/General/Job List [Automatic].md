# Job List [Automatic]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/f1dd99c5-fc23-47b9-8368-ba816d4137da/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Flow used to add Jobs and their data from the Katapult API to the **Job List** and also to add a Job and its tasks to the **Task List**.


## Trigger Action
When an item is created or modified in the **Job List**.


## Variables
* **siteAddress**: **String** type variable that stores the address of the SharePoint subsite.
<br></br>

* **katapultFolder**: **String** type variable that stores the Katapult Folder path.
<br></br>

* **listsNames**: **Object** type variable used to store the name of the SharePoint lists used in the Flow and their respective IDs.
<br></br>


## Decision Points
* **Condition - If a job was created with New as name**: Condition used to identify whether the modification that triggered the Flow is the command to obtain the Jobs recently created in Katapult. If so, Flow is directed to perform the necessary actions to update the **Job List** with the most recent Jobs. If not, then Flow is directed to the next condition.
<br></br>
    * Type: if
<br></br>

* **Condition - If the Job received a Start Date**: Condition used to identify whether the Job that triggered the Flow had its **Start Date** changed. If so, then **Task Capacities [Dependent] Flow** is called to start the process of creating tasks in the **Task List**.
<br></br>
    * Type: if
<br></br>


## Related Flows
* [Task Capacities [Dependent]](Task%20Capacities%20[Dependent].md)
* [Date Calculator [Dependent]](Date%20Calculator%20[Dependent].md)
* [Update Job List With New Jobs [Dependent]](Update%20Job%20List%20With%20New%20Jobs%20[Dependent].md)
* [Get SharePoint Lists IDs [Dependent]](../General/Get%20SharePoint%20Lists%20IDs%20[Dependent].md)


## Workflow End
A. First End:  
    &emsp; 1. "**Condition** - If a job was created with New as name"  
    &emsp; 2. "**Case** True"  
    &emsp; 3. "**HTTP** - Update Job List With New Jobs [Dependent]"  

B. Second End:  
    &emsp; 1. "**Condition** - If a job was created with New as name"  
    &emsp; 2. "**Case** False"  
    &emsp; 3. "**Condition** - If the Job received a Start Date"  
    &emsp; 4. "**Case** True"  
    &emsp; 5. "**HTTP** - Task Capacities [Dependent]"  

C. Third End:  
    &emsp; 1. "**Condition** - If a job was created with New as name"  
    &emsp; 2. "**Case** False"  
    &emsp; 3. "**Condition** - If the Job received a Start Date"  
    &emsp; 4. "**Case** False"  
    &emsp; 5. "Terminate"


## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Bell/BracebridgeUBF/Lists/Job%20List/AllItems.aspx" target="_blank">Job List</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The links above point to the lists present on the <b>Bracebridge UBF</b> subsite, however Flow will update the equivalent lists in each set subsite.</p>
</div>


## Excel Spreadsheets Involved in the Process
There is no excel spreadsheets involved in the process.


## Example of Execution

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Triggering and executing Flow takes a few minutes to complete, although in the demonstrations below it appears to take less time.</p>
</div>

* **Adding new Jobs to the Job List**

<a data-fancybox="Adding new Jobs to the Job List" href="../../../_static/flows/job_list/bell_-_bracebridge_ubf_-_job_list_[automatic]_adding_new_jobs.mp4" data-caption="Adding new Jobs to the Job List">
  <img src="../../../_static/flows/job_list/bell_-_bracebridge_ubf_-_job_list_[automatic]_adding_new_jobs_thumbnail.jpg" alt="Adding new Jobs to the Job List" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>

* **Adding a Job and its Tasks to the Task List**

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>"Task Capacities [Dependent]" and "Date Calculator [Dependent]" Flows participate in this process.</p>
</div>

<a data-fancybox="Adding a Job and its Tasks to the Task List" href="../../../_static/flows/job_list/bell_-_bracebridge_ubf_-_job_list_[automatic]_adding_new_tasks.mp4" data-caption="Adding a Job and its Tasks to the Task List">
  <img src="../../../_static/flows/job_list/bell_-_bracebridge_ubf_-_job_list_[automatic]_adding_new_tasks_thumbnail.jpg" alt="Adding new Jobs to the Job List" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>