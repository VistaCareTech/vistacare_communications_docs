# Update of Task Lists

## Description
Set of Flows responsible for adding new tasks to the **Task List** as well as updating existing tasks based on the data present in the **Job List**, **Task Capacities**, **PENG Task Capacities**, and **Task List** SharePoint lists.

## Flowchart

## How It Works
This set of Flows can be initiated by one of the two Flows below:

- **Job List [Automatic]**: by adding a new **Job** with the **Start Date** attribute to the **Job List**, or by changing the **Start Date** attribute of a **Job** already existing in the **Job List**.
<br></br>

- **Task List [Automatic]**: by adding a new Task or changing the Status attribute of a Task already existing in the Task List.
<br></br>

The Flow that was triggered will then call **Task Capacities [Dependent]** which will then call **Date Calculator [Dependent]**.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>For more details on how it works, access the documentation for each Flow in the list below.</p>
</div>

## Flows
   ### [Job List [Automatic]](Job%20List%20[Automatic].md)
   ### [Task List [Automatic]](Task%20List%20[Automatic].md)
   ### [Task Capacities [Dependent]](Task%20Capacities%20[Dependent].md)
   ### [Date Calculator [Dependent]](Date%20Calculator%20[Dependent].md)