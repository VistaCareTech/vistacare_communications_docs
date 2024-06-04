# Backup and Recovery of Tasks Lists

## Description
Set of Flows responsible for backing up **Task Lists** and facilitating the recovery of a **Task List** with Backup data.

## Flowchart
<a class="" data-lightbox="Flowchart" href="../../../_static/flows/Backup_and_Recovery_of_Tasks_Lists_-_Flowchart.png" title="Backup and Recovery of Tasks Lists Flowchart" data-title="Backup and Recovery of Tasks Lists Flowchart">
<img src="../../../_static/flows/Backup_and_Recovery_of_Tasks_Lists_-_Flowchart.png" class="align-center" width="500px" alt="Backup and Recovery of Tasks Lists Flowchart">
</a>
<br></br>

## How It Works
This set of Flows work independently:

- **Task List Backup [Schedule]**: is automatically activated daily at 10 PM. When triggered, it saves the information contained in the **Task List** in a backup file.
<br></br>

- **Recovery From Backup [Manual]**: facilitate adding backup data to the **Task List**. To do this, the user selects the backup file they want and then clicks on run Flow.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>For more details on how it works, access the documentation for each Flow in the list below.</p>
</div>

## Flows
   ### [Task List Backup [Schedule]](Task%20List%20Backup%20[Schedule].md)
   ### [Recovery From Backup [Manual]](Recovery%20From%20Backup%20[Manual].md)