# ETLs

<!-- THIS DESCRIPTION IS THE PREDECESOR OF ANCHOR SPIDA TO DB DEVELOPMENT. RETAINED FOR FUTURE REFERENCE
## SpidaCalc to DB

SpidaCalc to DB allows us to extract the information from the SpidaCalc JSON file, transform it in the format managed on the database and load it in the Database with the correct format allowing the deleting of the duplicate anchors.

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>The duplicate anchors are defined by two variables, the <b><i>angle space</i></b> between the anchors and the anchors that are in the same <b><i>radius</i></b> that the top vertex of the anchor.</p>
</div> 

The following steps will allow you to execute the SpidaCalc to DB functionality:

1. On the VistaCare Communications Plugin go to `ETLs ==> SpidaCalc To DB`.
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
-->

## Anchor Spida to DB

The "Anchor Spida to DB" functionality provides a solution for importing and managing anchor, overhed guy and down guy data from SpidaCalc into a GIS database. With features such as layer evaluation, status determination, memory layer visualization, and dynamic user interface components, this tool streamlines the process of visualizing, analyzing, and exporting spatial data from SpidaCalc into QGIS.

### Key Features
1. **Anchor, Overhead and Down Guy Import:** This tool imports anchors, overhead and down guys from SpidaCalc JSON file containing detailed information on poles, anchors, overhead and down guys. It reads and extract pertinent data needed for the functionality.
2. **Memory Layers for Anchor and Poles:** This tool creates a temporary memory layer for poles and anchors. These memory layers are populated with features to allow the spatial visualization of poles, anchors, overhead and down guys within QGIS interface.
3. **Single and Double Layer Evaluation:** This tool supports both single and double layer (existing and proposed )data evaluation.
4. **Anchor and Guys Status Evaluation:** This tool evaluates the status of anchors and guys as 'New' or 'Existing'.
5. **Anchor and Guys Geometry Creation:** This tool automatically generates line geometries for anchor based on pole coordinates, azimuth and lead length. Overhead guys computes and creates a line connecting poles to ensure accurate visual representation.

### How It Works

<a class="" data-lightbox="Anchor Spida to DB" href="_static/Anchor_Spida_to_DB.gif" title="Anchor Spida to DB" data-title="Anchor Spida to DB"><img src="_static/Anchor_Spida_to_DB.gif" class="align-center" width="800px" height="500px" alt="Anchor Spida to DB">
</a>

