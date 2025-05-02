# <img src="../_static/qgis_plugins/icons/cad/cad.png" alt="CAD" width="24px"> CAD


## <img src="../_static/qgis_plugins/icons/cad/cad_block_export_wizard.png" alt="CAD Block Export Wizard" width="24px"> CAD Block Export Wizard 

CAD Block Export Wizard is designed to streamline export of GIS information into CAD blocks with attributes and layer. Integrating with UI this gives user the flexibility of handling multiple entities such as Poles, Splice, MPT's, Civic, Cables, etc. This functionality also ensures the CRS are transformed uniformly while using memory data without affecting the original data. 

This development currently support exports for the following entities:
- Pole
- Splice
- MPT
- Cable
- Drop Cable
- Civic
- Underground Structures such as Handhole(GLB), Flowerpot, DIP
- Slack Loop
- Strand
- Conduit
- Span
- Arbs
- Road
- Wiring Limit
- Anchor: including downguy and overhead guy
- Tie in
- CSP
- Plan Page
- FSA Boundary

### How It Works

<a class="" data-lightbox="CAD Export" href="../_static/qgis_plugins/cad/cad_export.gif" title="CAD Export" data-title="CAD Export"><img src="../_static/qgis_plugins/cad/cad_export.gif" class="align-center" width="800px" height="500px" alt="CAD Export">
</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>Make sure to run <b>Audit</b> command after export is completed</p>
</div>

### NL Project CAD Export Field Names Guide

| **Page**                                                     | **Layer Table to use**        | **Attribute - Field**                                                                                                                                                                                                                                             |
| ------------------------------------------------------------ | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Poles                                                        | Access Structure Pole Master  | POLE NUMBER - **nlp_bell_id**<br>POLE OWNER - **Owner**<br>POLE AGE - **Age**<br>POLE HEIGHT- **Height**<br>POLE CLASS - **Class**                                                                                                                                |
| Splice                                                       | Splice                        | LABEL - **label_export**<br>PLACEMENT - **placement**<br>CLASS - **class**                                                                                                                                                                                               |
| MPT                                                          | Cables                        | CATEGORY - **category**<br>LABEL - **label**<br>DESIGN STATE - **design_state**<br>FIBER CAPACITY - **fiber_capacity**<br>PLACEMENT - **placement**<br>FINAL LENGTH - **final_length**<br>PREMISE LENGTH - **premise_length**                                     |
| Cable                                                        | cables                        | CABLE DESIGN - **cable_plan_label**<br>PERMIT DESIGN - **label_export**<br>LABEL - **label**<br>ARMOR TYPE - **armor_type**<br>FIBER CAPACITY - **fiber_capacity**<br>PREMISE LENGTH - **premise_length**<br>PLACEMENT - **placement**<br>CATEGORY - **category** |
| Drop Cable                                                   | fibre_drops                   | TYPE - **type**<br>FIBER CAPACITY - **fiber_capacity**                                                                                                                                                                                                            |
| Civic                                                        | \* Drop Layer - Demand Points | PROGRAM - **program**<br>STREET NUMBER - **STREET_NUM**<br>STREET NAME - **STREET_NAM**<br>HOME COUNT - **HOMECOUNT**<br>PLUS CODE - **pluscode**                                                                                                                 |
| Underground Structures:<br>Handhole(GLB),<br>Flowerpot,<br>DIP | UG_structure                  | TYPE - **type**<br>LABEL - **label**<br>STATUS - **status**                                                                                                                                                                                                       |
| Slack Loop                                                   | slack                         | LENGTH - **length**<br>STATUS - **status**                                                                                                                                                                                                                        |
| Strand                                                       | strand                        | STATUS - **status**                                                                                                                                                                                                                                               |
| Conduit                                                      | conduit                       | TYPE - **type**<br>SIZE - **size**<br>STATUS - **status**                                                                                                                                                                                                         |
| Span                                                         | spans                         | CASE - **case**<br>LENGTH - **length**                                                                                                                                                                                                                            |
| Wiring Limit                                                 | wiring_limits                 | HOME PASSED - **homes_passed**<br>FIBER DEMAND - **fiber_demand**                                                                                                                                                                                                 |
| Anchor including guy                                         | anchors                       | STATUS - **status**                                                                                                                                                                                                                                               |
| Tie in                                                       | tie_in                        | LENGTH - **length**                                                                                                                                                                                                                                               |
| CSP                                                          | csp                           | SIZE - **size**<br>STATUS - **status**<br>LABEL - **label_export**                                                                                                                                                                                                |
| Plan Page                                                    | plan_pages_32622              | PAGES - **page**  


## <img src="../_static/qgis_plugins/icons/cad/katapult_profiles.png" alt="Katapult Profiles" width="24px"> Katapult Profiles

Similar with **Pole Profiles** and **PAR Profiles**, this module allows the user to generate a CAD format pole profiles using the information from Katapult. The module interface allows the user to choose some or all of poles to be generated. This also has a search bar wherein the user can narrow down the poles from the table.

### How it Works

The following steps will allow you to generate pole profiles using Katapult:
1. In the VistaCare Communications Plugin go to **CAD --> Katapult Profiles**.
2. From browser, copy the Katapult job id and paste it in the line edit. 
   <a class="" data-lightbox="Katapult Profiles" href="../_static/qgis_plugins/cad/katapult_job_id.png" title="Katapult job id" data-title="Katapult job id"><img style="border-width:2px; border-style:solid; border-color:#000000;" src="../_static/qgis_plugins/cad/katapult_job_id.png" class="align-center" width="800px" height="500px" alt="Katapult job id">
    </a>
3. Select the poles to be generated.
4. **(Optional)** Choose folder location you want to save your profiles. Default location is at `C:/Users/{username}/Desktop/{Katapult Job Name}`
5. Click **OK** button to generate the profiles.

<a class="" data-lightbox="Katapult Profiles" href="../_static/qgis_plugins/cad/katapult_profiles.gif" title="Katapult Profiles" data-title="Katapult Profiles"><img src="../_static/qgis_plugins/cad/katapult_profiles.gif" class="align-center" width="800px" height="500px" alt="Katapult Profiles">
</a>


## <img src="../_static/qgis_plugins/icons/cad/par_profiles.png" alt="PAR Profiles" width="24px"> PAR Profiles

This module, similar to **Pole Profile**, this allows users to generate pole profiles in DXF format, ensuring compatibility with numerous CAD applications. It works exclusively with **SpidaCalc JSON files** containing a single or double pole layer. If the pole has two layer, it will generate poles for both layers and won't do comparison for both layer unlike with **Pole Profiles**.

The plugin performs the following actions:
* Generates a side-by-side image of the selected poles in a single AutoCAD file (named the same as the JSON file)
* Creates individual AutoCAD files for each selected pole (pole label), if two layer exist for the pole it will name as (pole label_layer name)

### How it Works

The following steps will allow you to execute PAR Profile.
1. In the VistaCare Communications Plugin go to **CAD--> PAR Profiles**.
2. Select the **JSON file** to work on.
3. Tick the tickbox which pole you want to generate the profile.
4. Fill in **Direction** column for pole bearing with respect to roadside, default value is 0 degrees.
5. **(Optional)** Choose folder location you want to save your profiles.
6. Click **OK** button to generate the profiles.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Make sure to open the related QGS project file and select the <b>Poles</b> layer or a related layer from <b>Pole Information Source Layer</b> drop down to capture the table information accurately.</p>
</div>

<a class="" data-lightbox="PAR Profile" href="../_static/qgis_plugins/cad/PAR_profile.gif" title="PAR Profile" data-title="PAR Profile"><img src="../_static/qgis_plugins/cad/PAR_profile.gif" class="align-center" width="800px" height="500px" alt="PAR Profile">
</a>


## <img src="../_static/qgis_plugins/icons/cad/pole_profiles.png" alt="Pole Profiles" width="24px"> Pole Profiles

Image generator for Pole Profile PEng Reports. This plugin lets you create a 2D image for pole profile
in an SVG or DXF format. SVG format gives the user a scalable vector graphic that maintains high quality 
image and can be easily edited with various vector graphic software. DXF format provides compatibility 
with numerous CAD applications.

When selecting both **XCI** and **DXF** formats along with multiple poles, the plugin performs the following actions:
* Generates a side-by-side image of the selected poles in a single AutoCAD file (named the same as the JSON file)
* Creates individual AutoCAD files for each selected pole (named based on the pole label)

### How it Works

The following steps will allow you to execute Pole Profile

1. On the VistaCare Plugin go to **CAD --> Pole Profile**.
2. Select the JSON file to work on.
3. Choose the pole profile format and pole profile file type. 
4. Tick the checkbox which pole you want to generate the profile.
5. Fill in Direction column for pole bearing with respect to roadside, default value is 0 degrees.
6. **(Optional)** Choose folder location you want to save your profiles.
7. Click **OK** button to generate the profiles.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Make sure to open the related QGS project file and select the <b>Poles</b> layer or a related layer from <b>Pole Information Source Layer</b> drop down to capture the table information accurately.</p>
</div>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>If <b>Output File Location</b> is empty, output files will be save at input json folder location.</p>
</div>

<a class="" data-lightbox="Pole Profile" href="../_static/qgis_plugins/cad/new_pole_profile_gif.gif" title="Pole Profile" data-title="Pole Profile"><img src="../_static/qgis_plugins/cad/new_pole_profile_gif.gif" class="align-center" width="800px" height="500px" alt="Pole Profile">
</a> 

### Format Summary Table


<!--Markdown Table Generator Data from https://tabletomarkdown.com/generate-markdown-table/ -->
| Display                                                | **H1 Format**                                                                                                                    | **Lakeland Format**                                                         | **XCI Format**                                                              |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Font Color                                             | RED for MR changes on Hydro space<br>Black on Telco space                                                                    | RED for MR changes on Hydro space<br>Black on Telco space               | RED for MR changes on Hydro space<br>Black on Telco space               |
| Primary wires                                          | All wires are drawn                                                                                                          | Lowest primary height is drawn                                          | Lowest primary height is drawn                                          |
| Primary wires with MR                                  | **'PRIM.'** will be in Bold, Red,<br>**Original Value** in Bold, Red<br>then **MR Value** in **'****()****'** ,Bold, Red | 'PRIM.' in Red<br>Original value in Red<br>then MR value in '()', Red   | 'PRIM.' in Red<br>Original value in '()' and Red<br>then MR value in Red   |
| Neutral/Sec wire                                       | All wires are drawn                                                                                                          | All wires are drawn                                                     | All wires are drawn                                                     |
| Neutral/Sec wire with MR                               | **'NEUT./SEC.'** in Bold, Red<br>**Original Value** in Bold, Red<br>**MR value** in **'()'**, Bold, Red          | 'NEUT./SEC.' in Red<br>Original Value in Red<br>MR value in '()', Red   | 'NEUT./SEC.' in  Red<br>Original Value in '()', Red<br>MR value in  Red |
| Proposed guys with<br>Proposed Telco wire              | **'P.BELL/ P.D.G.'** in Bold                                                                                             | **'P.BELL/ P.D.G.'** in Bold                                        | **'P.XPLORE/ D.G.'** in Bold,<br>Blue font color                                  |
| Proposed Telco wire and <br>proposed guy for represenation | Black Color \**DOT\**                                                                                                          | Black Color \**DOT\**                                                     | Blue Color \**DOT\**                                                      |
| Feature in new heights<br>and Original height          | Original height in normal weight<br>New height in '()' in normal weight                                                      | Original height in normal weight<br>New height in '()' in normal weight | Original height in '()'<br>New height in Normal weight<br>              |
| New Feature height value display                       | **New height** in Bold                                                                                                       | **New height** in Bold                                                  | **New height** in Bold                                                  |
| Feature text display                                   | Display in upper case<br>eg. TRANSF.                                                                                         | Display in upper case<br>eg. TRANSF.                                    | Display in upper case<br>eg. TRANSF.                                    |
| Feature height value display                           | Height Value in normal weight                                                                                                | Height Value in normal weight                                           | Height Value in normal weight                                           |


### Pole Profiles Errors

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>When running the functionality Pole Profiles, it is possible to obtain one of the following messages.</p>
</div>

1. Bar message will show if wrong JSON file is used (non SpidaCalc json file). Make sure to use SpidaCalc generated JSON file.

<a class="" data-lightbox="Pole Profile" href="../_static/qgis_plugins/cad/pole_profile_img/pp_bar_wrong_json_short.png" title="Wrong JSON file" data-title="Wrong JSON file"><img src="../_static/qgis_plugins/cad/pole_profile_img/pp_bar_wrong_json_short.png" class="align-center" width="800px" height="500px" alt="Wrong JSON file">
</a>

2. Bar message will show if JSON file has missing layers (**Existing** or **Proposed**) and script will not proceed.

<a class="" data-lightbox="Pole Profile" href="../_static/qgis_plugins/cad/pole_profile_img/pp_bar_missing_layer_short.png" title="Missing Layer" data-title="Missing Layer"><img src="../_static/qgis_plugins/cad/pole_profile_img/pp_bar_missing_layer_short.png" class="align-center" width="800px" height="500px" alt="Missing Layer">
</a>

3. Bar message will show how many poles have error during populating table information after selecting JSON file(**A**). It will also specify the pole name with its error on the text box (**B**).

<a class="" data-lightbox="Pole Profile" href="../_static/qgis_plugins/cad/pole_profile_img/pp_exclude_poles_with_errors.png" title="Poles with errors" data-title="Poles with errors"><img src="../_static/qgis_plugins/cad/pole_profile_img/pp_exclude_poles_with_errors.png" class="align-center" width="800px" height="500px" alt="Poles with errors">
</a>

4. If any pole in the table have error during pole profile creation, it will specify the pole with its error on the text box.

<a class="" data-lightbox="Pole Profile" href="../_static/qgis_plugins/cad/pole_profile_img/pp_error_during_generation.png" title="Errors during generation" data-title="Errors during generation"><img src="../_static/qgis_plugins/cad/pole_profile_img/pp_error_during_generation.png" class="align-center" width="800px" height="500px" alt="Errors during generation">
</a>