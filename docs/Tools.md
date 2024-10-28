# Tools

## Extract and Pack

The Extract and Pack module as the name implies filters the selected layers by the feature in the boundary layer, extracts the information with the methods *intersect* or *within* and packs this data on a specific folder defined by the user.

The following steps will allow you to execute the Extract and Pack functionality:

1. On the VistaCare Communications Plugin go to `Tools --> Extract and Pack`.
2. Fill the following options:

    * Boundary Layer: A Polygon layer with the features will be used as a boundary.
    * Boundary Feature: Define the feature that will be the borders of the information extracted.
    * Layers to Extract: Choose all the layers that are required to be exported.
    * Selection Type: Select one option to match the information (Intersect or Within).
    * Folder for export: Choose the place where they will be located the information extracted.

3. Click on `OK` and wait until the module finishes the execution. 

<a class="" data-lightbox="Extract and Pack" href="_static/extract_and_pack.gif" title="Extract and Pack" data-title="Extract and Pack"><img src="_static/extract_and_pack.gif" class="align-center" width="800px" height="500px" alt="Extract and Pack">
</a>

## Katapult Importer

The Katapult module allow the user to transfor and load  information from Katapult to the database. this operation is soported for *Poles, Anchors, Civics, Spans*.

The following steps will allow you to execute the Katapult Importer functionality:

1. On the VistaCare Communications Plugin go to `Tools --> Katapult Importer`.
2. Choose the project where you want to import the data.
3. Choose which kind of Layer are you going to import (Anchors example).
4. Fill the options available for each Layer case (Anchors example):

    * Shapefile Anchors: Information extracted from Katapult that contain the Anchors data.
    * Shapefile Guys: Information extracted from Katapult that contain the Guys data.
    * Anchors: Anchors Layer with the database structure.
    * Guys: Guys Layer with the database structure.

3. Click on `Import Data` and wait until the module finishes the execution. 
4. Click on `Finish`.

<a class="" data-lightbox="Katapult Importer" href="_static/katapult_importer.gif" title="Katapult Importer" data-title="Katapult Importer"><img src="_static/katapult_importer.gif" class="align-center" width="800px" height="500px" alt="Katapult Importer">
</a>

## Katapult Importer API Version

The Katapult Importer API Plugin allows QGIS users to seamlessly import infrastructure data from Katapult into QGIS by entering a specific Katapult Job ID. The plugin leverages the Katapult API to retrieve job-related data, loading it directly into a database memory layer within QGIS. This supports *`Poles` and `Anchors`* layer.

### Key Features
1. Katapult API Integration: Retrieves detailed job data from Katapult using a job ID input.
2. Memory Layer Loading: Automatically imports data into a temporary database memory layer within QGIS
3.  QGIS Integration: Works smoothly with QGIS’s layer structure, allowing further geospatial analysis and editing.

### How It Works

<a class="" data-lightbox="Katapult Importer API Version" href="_static/katapult_inporter_api.gif" title="Katapult Importer API Version" data-title="Katapult Importer API Version"><img src="_static/katapult_inporter_api.gif" class="align-center" width="800px" height="500px" alt="Zoom to Feature">
</a>

## SpidaCalc Validator

Plugin to extract information from SPIDACALC JSON and generate PDF, XLS report for required missing information.

The following steps will allow you to execute the SpidaCalc Validator functionality:

1. On the VistaCare Plugin go to `Tools --> SpidaCalc Validator`.
2. Choose application to validate SpidaCalc JSON file.

    * Pole Profile
    * Anchor Importer (SpidaCalc to DB)
    * Vertical Separation

3. On user interface, select JSON file to work on.
4. **(Optional)** Choose folder location you want to save your reports.
5. Click `OK` button to generate table

<a class="" data-lightbox="Spidacalc Validator" href="_static/spidacalc_validator_gif.gif" title="Spidacalc Validator" data-title="Spidacalc Validator"><img src="_static/spidacalc_validator_gif.gif" class="align-center" width="800px" height="500px" alt="Spidacalc Validator">
</a>

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>

1. Brief Description in Text Box: 
   * Description in <span style="color: #000000; font-weight:bold">'BLACK'</span> font color are general information
   * Description in <span style="color: #FF0000; font-weight:bold">'RED'</span> font color are pole feature missing information
   * Description in <span style="color: #008000; font-weight:bold">'GREEN'</span> font color are completed reports
2. For **PDF report**, missing information from JSON or any other information source will have its value as `None` and font color to <span style="color: #FF0000; font-weight:bold">'RED'</span>.
3. For **XLS report**, missing information from JSON or any other information source will have a value of `None` and its cell font color to <span style="color: #FF0000; font-weight:bold">'RED'</span>. Also, if a layer is missing, rest of the row of layer and pole will be empty.
</div>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>All the detailed information can be found in the generated reports.</p>
</div>

## Layout Modifier

The Layout modifier module allows us to modify the page's Layer and the Layout for the Atlas configuration to exchange the Layers IDs and the Layour components between each field selected.

The following steps will allow you to execute the Layout Modifier functionality:

1. On the VistaCare Communications Plugin go to `Tools --> Layout Modifier`.
2. Fill the following options:

    * Layout: Layout to be modified.
    * Page Layer: Layer that is used to create the Atlas.
    * Field Page Layer: The field that is used to order the pages on the Atlas.
    * Initial ID: the ID that will be migrated.
    * Final ID: the Target ID to be replaced.

3. Click on `OK` and wait until the module finishes the execution. 

<a class="" data-lightbox="Layout Modifier" href="_static/layout_modifier.gif" title="Layout Modifier" data-title="Layout Modifier"><img src="_static/layout_modifier.gif" class="align-center" width="800px" height="500px" alt="Layout Modifier">
</a>