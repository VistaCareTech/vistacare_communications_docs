# Auxiliary Flows

## Description
Set of Flows responsible for assisting in the execution of specific tasks. They can be called from any other Flow in any other project.

## Flowchart
<a class="" data-lightbox="Flowchart" href="../../../_static/flows/Auxiliary_Flows_-_Flowchart.png" title="Auxiliary Flows Flowchart" data-title="Auxiliary Flows Flowchart">
<img src="../../../_static/flows/Auxiliary_Flows_-_Flowchart.png" class="align-center" width="500px" alt="Auxiliary Flows Flowchart">
</a>
<br></br>

## How It Works
These Flows work independently:

- **Get SharePoint Lists IDs [Dependent]**: can be called from any other Flow. When triggered, it searches for the IDs of the SharePoint Lists passed by the Flow that triggered it, and then returns a list with the name and ID of the requested lists.
<br></br>

- **Update Job List With New Jobs [Dependent]**: can be called from any other Flow. When triggered, it compares the Jobs already present in the **Job List** with the Jobs present in Katapult, and then adds the missing Jobs to the **Job List**.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>For more details on how it works, access the documentation for each Flow in the list below.</p>
</div>

## Flows
   ### [Get SharePoint Lists IDs [Dependent]](Get%20SharePoint%20Lists%20IDs%20[Dependent].md)
   ### [Update Job List With New Jobs [Dependent]](Update%20Job%20List%20With%20New%20Jobs%20[Dependent].md)