# Update Job List With New Jobs [Dependent]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/0ae5ed80-1b7e-41f7-8167-14e6aa80a24a/details" target="_blank">Flow</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Auxiliary Flow used to add new Jobs and their data from the Katapult API to the **Job List**.


## Trigger Action
When an HTTP request is received.


## Variables
* **Customer**: **String** type variable used stores the name of the customer of a specific Job/Project.
<br></br>

* **Area**: **String** type variable used stores the area of a specific Job/Project.
<br></br>


## Decision Points
* **Condition - Does Job has a date created attribute*: Condition used to identify whether the Job found in the Katapult API has the **date_created** attribute. If so, the Job is added to the list of Jobs that will be added to the **Job List**.
<br></br>
    * Type: if
<br></br>


## Related Flows
It can be called from any other Flow.


## Workflow End
A. First End:  
    &emsp; 1. "**Apply to each** - KatapultID"  
    &emsp; 2. "**Condition** - Does Job has a date created attribute"  
    &emsp; 3. "**Create item** - Job List"


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

<a data-fancybox="Adding new Jobs to the Job List" href="../../../_static/flows/job_list/bell_-_bracebridge_ubf_-_job_list_[automatic]_adding_new_jobs.mp4" data-caption="Adding new Jobs to the Job List">
  <img src="../../../_static/flows/job_list/bell_-_bracebridge_ubf_-_job_list_[automatic]_adding_new_jobs_thumbnail.jpg" alt="Adding new Jobs to the Job List" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

<br>