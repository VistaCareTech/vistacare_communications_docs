# <img src="../_static/qgis_plugins/icons/design/design.png" alt="Design" width="24px"> Design


## <img src="../_static/qgis_plugins/icons/design/conduit_and_splice.png" alt="Conduit and Splice" width="24px"> Conduit and Splice

The **Conduit and Splice** allows the user to create diagrams on the QGIS Layout based on the conduit, splice and conduit connection layers.

### How It Works

The following steps will allow you to execute the Conduit and Splice functionality:

1. On the VistaCare Communications Plugin go to **Design --> Conduit and Splice**.
2. Fill the options available for each case:

    * **Layout**: Choose one of the Layouts create on the QGIS Projects.
    * **Splice layer**: Information Point type Layer with the Splice database structure.
    * **Conduit connections layer**: Alphanumeric type Layer with the Conduit connection database structure.
    * **Conduit layer**: Line type Layer with the Conduit database structure.

3. Click on **OK** and wait until the module finishes the execution. 
4. Click on **Close** and review the results on the Layout edited.

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>When you run the functionality Conduit and Splice it is necessary to select the splices to be drawn, if you do not select the splice you will obtain the following message.</p>
</div>

<a class="" data-lightbox="Conduit and Splice" href="../_static/qgis_plugins/design/alert_conduit_splice.png" title="Conduit and Splice alert" data-title="Conduit and Splice alert"><img src="../_static/qgis_plugins/design/alert_conduit_splice.png" class="align-center" width="800px" height="100px" alt="Conduit and Splice alert">
</a>

<a class="" data-lightbox="Conduit and Splice" href="../_static/qgis_plugins/design/conduit_splice.gif" title="Conduit and Splice" data-title="Conduit and Splice"><img src="../_static/qgis_plugins/design/conduit_splice.gif" class="align-center" width="800px" height="500px" alt="Conduit and Splice">
</a>


## <img src="../_static/qgis_plugins/icons/design/conduit_relations_creator.png" alt="Conduit Relations Creator" width="24px"> Conduit Relations Creator

The **Conduit Relations Creator** allows the user to create connections between conduits based on the id and the size of the conduit related.

### How It Works

The following steps will allow you to execute the Conduit and Splice functionality:

1. On the VistaCare Communications Plugin go to **Design --> Conduit Relations Creator**.
2. Fill the options available for each case:
    
    * **Conduit connections layer**: Alphanumeric type Layer with the Conduit connection database structure.
    * **Conduit layer**: Line type Layer with the Conduit database structure.
    * **Splice layer**: Information Point type Layer with the Splice database structure.
    * **Select a Splice**: Click and choose from the interface the splice that intersects the conduits involved in the relation to be created.
    * **Init Conduit ID**: Choose one of the IDs options displayed on the interface as initial conduit ID.
    * **End Conduit ID**: Choose one of the IDs options displayed on the interface as Final conduit ID.

3. Click on **OK** and wait until the module finishes the execution. 
4. Click on **Close** and review the results on the Conduit connections layer.

<a class="" data-lightbox="Conduit Relations Creator" href="../_static/qgis_plugins/design/conduit_connections.gif" title="Conduit Relations Creator" data-title="Conduit Relations Creator"><img src="../_static/qgis_plugins/design/conduit_connections.gif" class="align-center" width="800px" height="500px" alt="Conduit Relations Creator">
</a>


## <img src="../_static/qgis_plugins/icons/design/counts_calculator.png" alt="Counts Calculator" width="24px"> Counts Calculator

It uses a tree structure to traverse the nodes along the cable structure. As it moves through each node, it uses the *total_distribution_demand* variable to calculate the counts and update or create the necessary counts.

### How It Works

The following steps will allow you to execute the Counts Calculator functionality:

1. On the VistaCare Communications Plugin go to **Design --> Counts Calculator**.
2. Fill the following options:

    * **CSP Layer**: A Point layer with the features will be used as a Start point.
    * **Splice Layer**: A Point layer with the features will be used as a Start point.
    * **FSA Layer**: A Polygon layer with the features will be used as a boundary.
    * **Cables Layer**: A Line layer with the features will be used as a network.
    * **Counts Layer**: A Text layer where it is going to be storage the information calculated.
    * **Invert Start Cables**: Radio button that allows to invert the start of the cables excecution.

3. Click on **Select a CSP** or **Select a Splice** to choose the feature where is going to start the calculation.

4. Click on **OK** and wait until the module finishes the execution. 

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Counts Calculator can be excecute from CSP or Splice layers</p>
</div>

<a class="" data-lightbox="Counts calculator" href="../_static/qgis_plugins/design/counts_calculator.gif" title="Counts calculator" data-title="Counts calculator"><img src="../_static/qgis_plugins/design/counts_calculator.gif" class="align-center" width="800px" height="500px" alt="Counts calculator">
</a>


## <img src="../_static/qgis_plugins/icons/design/layout_modifier.png" alt="Layout Modifier" width="24px"> Layout Modifier

The **Layout Modifier** module allows us to modify the page's Layer and the Layout for the Atlas configuration to exchange the Layers IDs and the Layour components between each field selected.

### How It Works

The following steps will allow you to execute the Layout Modifier functionality:

1. On the VistaCare Communications Plugin go to **Design --> Layout Modifier**.
2. Fill the following options:

    * **Layout**: Layout to be modified.
    * **Page Layer**: Layer that is used to create the Atlas.
    * **Field Page Layer**: The field that is used to order the pages on the Atlas.
    * **Initial ID**: the ID that will be migrated.
    * **Final ID**: the Target ID to be replaced.

3. Click on **OK** and wait until the module finishes the execution. 

<a class="" data-lightbox="Layout Modifier" href="../_static/qgis_plugins/design/layout_modifier.gif" title="Layout Modifier" data-title="Layout Modifier"><img src="../_static/qgis_plugins/design/layout_modifier.gif" class="align-center" width="800px" height="500px" alt="Layout Modifier">
</a>