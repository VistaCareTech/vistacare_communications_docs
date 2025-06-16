# qgis_project_files Azure Function

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>Jhon and Laercio owns this <a href="https://portal.azure.com/#view/WebsitesExtension/FunctionTabMenuBlade/~/codeTest/resourceId/%2Fsubscriptions%2Fa732d279-234b-4d36-8cc7-a36e6b76014f%2Fresourcegroups%2Fvistacare-communications%2Fproviders%2FMicrosoft.Web%2Fsites%2Fvistacare-engineering-function1%2Ffunctions%2Fqgis_project_files" target="_blank">qgis_project_files Azure Function</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Azure function responsible for receiving an HTTP call from the <a href="https://make.powerautomate.com/environments/Default-a5273f41-687e-4e5e-9fba-18c6ce465b41/flows/shared/c9ff2ccc-25b8-4e09-be92-817b9fc7aff4/details" target="_blank">QGIS Project Files [Automatic]</a> flow, passing the necessary data to execute the code.


## Trigger Action
When an HTTP call is made.


## Programming Language
* Python
* SQL script


## Files
* **function_app.py**: part of the code responsible for establishing the azure function, receiving the parameters, calling the adds_data_to_the_projects_table function, and returning the result.
<br></br>

* **main.py**: part of the code responsible for establishing the connection with the database and executing the script to insert the item into the projects table.
<br></br>


## Libraries
* json
* azure.functions
* logging
* azure.identity
* azure.keyvault.secrets
* psycopg2


## Variables
* **user**: **String** type variable that stores the user that is used to access the database (Azure keyvault).
<br></br>

* **password**: **String** type variable that stores the password that is used to access the database (Azure keyvault).
<br></br>

* **dbname**: **String** type variable that stores the name of database which contains the **projects** table.
<br></br>

* **host**: **String** type variable that stores the host that is used to access the database.
<br></br>

* **port**: **integer** type variable that stores the port that is used to access the database.
<br></br>

* **script**: **String** type variable that stores the script executed to insert the new entry into the **projects** table.
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

* **result**: **String** type variable that stores the id after the project file is inserted in the table.
<br></br>


## Related Documentation
   ### [QGIS Project Files [Automatic] Flow](../flows/General/QGIS%20Project%20Files%20[Automatic].md)
   ### [QGIS Project Files Main Documentation](../viewers/qgis_project_files_main.md)