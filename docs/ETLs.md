# ETLs

## SpidaCalc to DB

SpidaCalc to DB allows us to extract the information from the SpidaCalc JSON file, transform it in the format managed on the database and load it in the Database with the correct format allowing the deleting of the duplicate anchors.

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The duplicate anchors are defined by two variables, the <b><i>angle space</i></b> between the anchors and the anchors that are in the same <b><i>radius</i></b> that the top vertex of the anchor.</p>
</div>

The following steps will allow you to execute the SpidaCalc to DB functionality:

1. On the VistaCare Communications Plugin go to `ETLs --> SpidaCalc To DB`.
2. Fill the following options:

    * Anchor P Eng: Line Layer with the Archor P Eng structure.
    * Poles: A pole layer related to the Anchors.
    * JSON File: File that contains all the anchor information from SpidaCalc.
    * Anchors Angle: Tolerance angle to define possible duplicates.
    * Radius: Tolerance radius to define possible duplicates.

3. Click on `Load Temp Anchor` and wait until the module loads the temporal anchors to be imported.
4. Click on `Next`. 
5. Click on `Load Table` to discover the possible duplicates.
6. Check which are the duplicate anchors and select the `Temp Anchors` or `Anchors` to remove from the database.
7. Click on `Import and Remove Duplicates`.

<a class="" data-lightbox="SpidaCalc To DB" href="_static/spidacalc_to_db.gif" title="SpidaCalc To DB" data-title="SpidaCalc To DB"><img src="_static/spidacalc_to_db.gif" class="align-center" width="800px" height="500px" alt="SpidaCalc To DB">
</a>