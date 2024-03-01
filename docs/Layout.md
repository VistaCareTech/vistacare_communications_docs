# Layout

## Layout Modifier

## Conduit and splice

The `Conduit and splice` allows the user to create diagrams on the QGIS Layout based on the conduit, splice and conduit connection layers.

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>When you run the functionality Conduit and Splice it is necessary to select the splices to be drawn, if you do not select the splice you will obtain the following message.</p>
</div>

<a class="" data-lightbox="Conduit and splice" href="_static/layout/alert_conduit_splice.png" title="Conduit and splice alert" data-title="Conduit and splice alert"><img src="_static/layout/alert_conduit_splice.png" class="align-center" width="800px" height="100px" alt="Conduit and splice alert">
</a>

The following steps will allow you to execute the Conduit and splice functionality:

1. On the VistaCare Communications Plugin go to `Layout --> Conduit and splice`.
2. Fill the options available for each case:

    * Layout: Choose one of the Layouts create on the QGIS Projects.
    * Splice layer: Information Point type Layer with the Splice database structure.
    * Conduit connections layer: Alphanumeric type Layer with the Conduit connection database structure.
    * Conduit layer: Line type Layer with the Conduit database structure.

3. Click on `OK` and wait until the module finishes the execution. 
4. Click on `Close` and review the results on the Layout edited.

<a class="" data-lightbox="Conduit and splice" href="_static/layout/conduit_splice.gif" title="Conduit and splice" data-title="Conduit and splice"><img src="_static/layout/conduit_splice.gif" class="align-center" width="800px" height="500px" alt="Conduit and splice">
</a>

## Conduit relations creator

The `Conduit relations creator` allows the user to create connections between conduits based on the id and the size of the conduit related.

The following steps will allow you to execute the Conduit and splice functionality:

1. On the VistaCare Communications Plugin go to `Layout --> Conduit Relations Creator`.
2. Fill the options available for each case:
    
    * Conduit connections layer: Alphanumeric type Layer with the Conduit connection database structure.
    * Conduit layer: Line type Layer with the Conduit database structure.
    * Splice layer: Information Point type Layer with the Splice database structure.
    * Select a Splice: Click and choose from the interface the splice that intersects the conduits involved in the relation to be created.
    * Init Conduit ID: Choose one of the IDs options displayed on the interface as initial conduit ID.
    * End Conduit ID: Choose one of the IDs options displayed on the interface as Final conduit ID.

3. Click on `OK` and wait until the module finishes the execution. 
4. Click on `Close` and review the results on the Conduit connections layer.

<a class="" data-lightbox="Conduit relations creator" href="_static/layout/conduit_connections.gif" title="Conduit relations creator" data-title="Conduit relations creator"><img src="_static/layout/conduit_connections.gif" class="align-center" width="800px" height="500px" alt="Conduit relations creator">
</a>