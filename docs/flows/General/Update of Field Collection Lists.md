# Update of Field Collection Lists

## Description
Set of Flows responsible for obtaining the field collection data and updating the **Job List**, **Daily Field Collections**, **Deficiency Field Recollections**, **Deficiency Field Collections - Missed** and **Field Pre QC** SharePoint lists with this data.

## Flowchart
<a class="" data-lightbox="Flowchart" href="../../../_static/flows/Update_of_Field_Collection_Lists_-_Flowchart.png" title="Update of Field Collection Lists Flowchart" data-title="Update of Field Collection Lists Flowchart">
<img src="../../../_static/flows/Update_of_Field_Collection_Lists_-_Flowchart.png" class="align-center" width="200px" alt="Update of Field Collection Flowchart">
</a>
<br></br>

## How It Works
The **Daily Update of Lists by Subsite [Schedule]** Flow is automatically triggered daily at sunset.
This flow will then call the **Update of Lists Related to Field Survey [Dependent]** Flow for each subsite set.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>For more details on how it works, access the documentation for each Flow in the list below.</p>
</div>

## Flows
   ### [Daily Update of Lists by Subsite [Schedule]](Daily%20Update%20of%20Lists%20by%20Subsite%20[Schedule].md)
   ### [Update of Lists Related to Field Survey [Dependent]](Update%20of%20Lists%20Related%20to%20Field%20Survey%20[Dependent].md)
