# Tools

## Extract and Pack

The Extract and Pack module as the name implies filters the selected layers by the feature in the boundary layer, extracts the information with the methods *intersect* or *within* and packs this data on a specific folder defined by the user.

The following steps will allow you to execute the Extract and Pack functionality:

1. On the VistaCare Plugin go to `Tools --> Extract and Pack`.
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
## SpidaCalc Validator
## Layout Modifier

The Layout modifier module allows us to modify the page's Layer and the Layout for the Atlas configuration to exchange the Layers IDs and the Layour components between each field selected.

The following steps will allow you to execute the Layout Modifier functionality:

1. On the VistaCare Plugin go to `Tools --> Layout Modifier`.
2. Fill the following options:

    * Layout: Layout to be modified.
    * Page Layer: Layer that is used to create the Atlas.
    * Field Page Layer: The field that is used to order the pages on the Atlas.
    * Initial ID: the ID that will be migrated.
    * Final ID: the Target ID to be replaced.

3. Click on `OK` and wait until the module finishes the execution. 

<a class="" data-lightbox="Layout Modifier" href="_static/layout_modifier.gif" title="Layout Modifier" data-title="Layout Modifier"><img src="_static/layout_modifier.gif" class="align-center" width="800px" height="500px" alt="Layout Modifier">
</a>