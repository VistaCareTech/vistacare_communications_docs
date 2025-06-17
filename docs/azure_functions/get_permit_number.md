# get_permit_number Azure Function

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>Jhon and Laercio owns this <a href="https://portal.azure.com/#view/WebsitesExtension/FunctionTabMenuBlade/~/codeTest/resourceId/%2Fsubscriptions%2Fa732d279-234b-4d36-8cc7-a36e6b76014f%2FresourceGroups%2Fvc-engineering%2Fproviders%2FMicrosoft.Web%2Fsites%2FPermitNumberTracker%2Ffunctions%2Fget_permit_number" target="_blank">get_permit_number Azure Function</a>. If you are not a co-owner you will not be able to access it.</p>
</div>


## Description
Azure function responsible for receiving an HTTP call receiving a SQL script with SELECT command, execute that script and then return the result.


## Trigger Action
When an HTTP call is made.


## Programming Language
* Python
* SQL script


## Files
* **function_app.py**: part of the code responsible for establishing the azure function, receiving the parameters, calling the get_peng_scope_data function, and returning the result.
<br></br>

* **main.py**: part of the code responsible for establishing the connection with the database, executing the script to select data from a table and returning the result.
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

* **result**: **String** type variable that stores the result obtained with the SQL script.
<br></br>


## Related Documentation
   ### [Update of Task Lists](../flows/General/Update%20of%20Task%20Lists.md)
   ### [Update Amounts in Task Lists [Schedule] Flow](../flows/General/Update%20Amounts%20in%20Task%20Lists%20[Schedule].md)