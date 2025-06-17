# QGIS Project Files [Automatic]

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>notify.engineering account owns this <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/c9ff2ccc-25b8-4e09-be92-817b9fc7aff4/details" target="_blank">Flow Link</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Initial Flow in the process of updating the **projects table** in the database with the data present in the **QGIS Project Files** Sharepoint List. It performs the function of identifying whether the modification that triggered the Flow corresponds to what was expected. If so, it makes an HTTP call to the **Azure function qgis_project_files** passing the information of the item that was changed in the **QGIS Project Files** List.


## Trigger Action
When an item is created or modified in the **QGIS Project Files**.


## Variables

Parameters passed through the **HTTP - qgis project files Azure Function** action:

* **dbname**: **String** type variable that stores the name of database which contains the **projects** table.
<br></br>

* **host**: **String** type variable that stores the host that is used to access the database.
<br></br>

* **port**: **integer** type variable that stores the port that is used to access the database.
<br></br>

* **Script**: **String** type variable that stores the script that should be executed in the **Azure function qgis_project_files**.
<br></br>

* **project**: **String** type variable that stores the project/client referring to the project file that will be inserted into the database.
<br></br>

* **area**: **String** type variable that stores the area referring to the project file that will be inserted into the database.
<br></br>

* **group**: **String** type variable that stores the group referring to the project file that will be inserted into the database.
<br></br>

* **url**: **String** type variable that stores the url where it is possible download the project file that will be inserted into the database.
<br></br>

* **update**: **datetime** type variable that stores the date the project file was created.
<br></br>


## Decision Points
* **Condition - If the Item Has an Attached File**: Condition used to allow the Flow to run only when the item has a project file attached.
<br></br>
    * Type: if
<br></br>


## Workflow End
A. First End:  
    &emsp; 1. "**Condition** - If the Item Has an Attached File"  
    &emsp; 2. "**Case** True"  
    &emsp; 3. "**HTTP** - qgis project files Azure Function"  
    &emsp; 4. "Azure function inserts or updates the project file in the projects table" 

B. Second End:  
    &emsp; 1. "**Condition** - If the Item Has an Attached File"  
    &emsp; 2. "**Case** False"  
    &emsp; 3. "Terminate"


## SharePoint Lists Affected by Workflow
* <a href="https://vistacaretech.sharepoint.com/sites/engineering/Lists/QGIS%20Project%20Files/AllItems.aspx" target="_blank">QGIS Project Files</a>



## Related Documentation
   ### [qgis_project_files Azure Function](../../azure_functions/qgis_project_files.md)
   ### [QGIS Project Files Main Documentation](../../viewers/qgis_project_files_main.md)