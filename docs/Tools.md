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

<a class="" data-fancybox="Extract and Pack" href="_static/extract_and_pack.mp4" data-caption="Extract and Pack"><img src="_static/extract_and_pack.gif" class="align-center" width="800px" height="500px" alt="Extract and Pack">
</a>

## Katapult Importer

The Katapult module allow the user to transfor and load  information from Katapult to the database. this operation is supported for *Poles, Anchors, Civics, Spans*.

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

<a class="" data-fancybox="Katapult Importer" href="_static/katapult_importer.mp4" data-caption="Katapult Importer"><img src="_static/katapult_importer.gif" class="align-center" width="800px" height="500px" alt="Katapult Importer">
</a>

## SpidaCalc Validator

Tool to extract information from SPIDACALC JSON and generate PDF, XLS report for required missing information.

The following steps will allow you to execute the SpidaCalc Validator functionality:

1. On the VistaCare Plugin go to `Tools --> SpidaCalc Validator`.
2. Choose application to validate SpidaCalc JSON file.

    * Pole Profile
    * Anchor Importer (SpidaCalc to DB)
    * Vertical Separation

3. On user interface, select JSON file to work on.
4. **(Optional)** Choose folder location you want to save your reports.
5. Click `OK` button to generate table

<a class="" data-fancybox="Spidacalc Validator" href="_static/spidacalc_validator_gif.mp4" data-caption="Spidacalc Validator"><img src="_static/spidacalc_validator_gif.gif" class="align-center" width="800px" height="500px" alt="Spidacalc Validator">
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


## BOM Report

This tool extracts BOM and BOL information and generates a report in .xlxs format. 

The following steps will allow you to execute BOM Report functionality:

1. Open `fdsa_boundaries` attribute table and select fsa needed for BOM Report.
2. On the VistaCare Communications Plugin go to `Tools --> BOM Report`.
3. Fill in the drop down menu. Follow the table below for recommended menu and layer to select.
4. Select BOM template Excel file from directory.
5. **Optional** Select where to save the .xlxs file result
6. Click `OK`

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>BOM Report Dropdown menu and Layer Guide</p>
</div>

| Drop down Menu                                               | **Layer Table to use**        |                                                                                                                                                                                                                              
| ------------------------------------------------------------ | ----------------------------- | 
| FSA Layer                                                    | fdsa_boundaries			   | 
| Splice Layer                                                 | splice                        |
| Poles Layer                                                  | poles                         |
| Cable Layer                                                  | cables                        |
| Conduit Layer                                                | conduit                       |
| UG Layer                                                     | UG_structure				   |
| Strand Layer												   | Strand			               |
| CSP Layer													   | csp						   |
| Anchor Layer												   | anchors					   |
| Guys Layer												   | guys						   |
| Peng Layer												   | peng_scope					   |
| Span Layer												   | spans						   |
| Slack Layer												   | slack 						   |
| Arbs														   | arbs_m						   |
| Wiring Limits												   | wire_limits				   |
| BOM Sheet Name											   | BOM-(with *BOM* keyword)	   |
| BOL Sheet Name											   | BOL-(with *BOL* keyword)	   |


### How it works

<a data-fancybox="BOM and BOL Report" href="_static/boms_report.mp4" data-caption="BOM and BOL Report">
  <img src="_static/boms_report_thumbnail.jpg" alt="BOM and BOL Report" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>
<br>

## Consumable List

This tool extracts BOM Consumable list and generates individual .xlxs per fsa selected.

The following steps will allow you to execute Consumable List functionality:

1. Open `fdsa_boundaries` attribute table and select fsa needed for Consumable List.
2. On the VistaCare Communications Plugin go to `Tools --> Consumable List`.
3. Fill in the drop down menu. Follow the table below for recommended menu and layer to select.
4. Select Consumable List template Excel file from directory.
5. **Optional** Select where to save the .xlxs file result
6. Click `OK`

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Consumable List Dropdown menu and Layer Guide</p>
</div>

| Drop down Menu                                               | **Layer Table to use**        |                                                                                                                                                                                                                       
| ------------------------------------------------------------ | ----------------------------- | 
| FSA Layer                                                    | fdsa_boundaries			   | 
| Splice Layer                                                 | splice                        |
| Poles Layer                                                  | poles                         |
| Cable Layer                                                  | cables                        |
| Conduit Layer                                                | conduit                       |
| UG Layer                                                     | UG_structure				   |
| Strand Layer												   | Strand			               |
| CSP Layer													   | csp						   |
| Anchor Layer												   | anchors					   |
| Guys Layer												   | guys						   |
| Peng Layer												   | peng_scope					   |
| Span Layer												   | spans						   |
| Slack Layer												   | slack 						   |
| Arbs														   | arbs_m						   |
| Sheet Name										           | Material Order Form    	   |

### How it works

<a data-fancybox="Consumable List BOM" href="_static/consumable_list.mp4" data-caption="Consumable List BOM">
  <img src="_static/consumable_list_thumbnail.jpg" alt="Consumable List BOM" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>
<br>

## Span Clearance And Vertical Separation

The Span Clearance And Vertical Separation module allows the user to obtain an Excel spreadsheet with the results of the Wire to Wire and To Ground Clearance process executed in SpidaCalc. Also is a CSV generator for P'Eng Report Exhibit 1 DESIGN DATA Vertical Separation (At Pole).

The following steps will allow you to execute the Span Clearance And Vertical Separation functionality:

1. On the VistaCare Communications Plugin go to `Tools --> Span Clearance And Vertical Separation`.
2. Select the JSON file to work on.
3. Tick the checkbox which pole you want to generate.
4. **(Optional)** Choose folder location you want to save the files.
5. Click `OK` button to generate table

<a class="" data-fancybox="Span Clearance" href="_static/span_clearance_vert_separation.mp4" data-caption="Span Clearance"><img src="_static/span_clearance_vert_separation.gif" class="align-center" width="800px" height="500px" alt="Span Clearance">
</a>

### Span Clearance And Vertical Separation Errors

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>When running the functionality Span Clearance And Vertical Separation, it is possible to obtain one of the following messages.</p>
</div>
  
1. Bar message will show if wrong JSON file is used (non SpidaCalc json file). Make sure to use SpidaCalc generated JSON file.
  
<a class="" data-lightbox="Vertical Separation" href="_static/vertical_separation_img/vs_bar_msg_wrong_json_short.png" title="Wrong JSON file" data-title="Wrong JSON file"><img src="_static/vertical_separation_img/vs_bar_msg_wrong_json_short.png" class="align-center" width="800px" height="500px" alt="Wrong JSON file">
</a>

2. Bar message will show if `Proposed` layer has an issue and script will not proceed.

<a class="" data-lightbox="Vertical Separation" href="_static/vertical_separation_img/vs_bar_msg_layer_issue_short.png" title="Layer issue" data-title="Layer issue"><img src="_static/vertical_separation_img/vs_bar_msg_layer_issue_short.png" class="align-center" width="800px" height="500px" alt="Layer issue">
</a>

3. If selected pole was unable to extract information due to an error, it will display the pole and its error in the textbox. A hyperlink of the output will be displayed in the textbox.

<a class="" data-lightbox="Vertical Separation" href="_static/vertical_separation_img/vs_textbox_information.png" title="Textbox information" data-title="Textbox information"><img src="_static/vertical_separation_img/vs_textbox_information.png" class="align-center" width="800px" height="500px" alt="Textbox information">

## Pole Profile

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>If output folder location is empty, output files will be save at input json folder location </p>
</div>
 
Image generator for Pole Profile P'Eng Reports. This tool lets you create a 2D image for pole profile
in an SVG or DXF format. SVG format gives the user a scalable vector graphic that maintains high quality 
image and can be easily edited with various vector graphic software. DXF format provides compatibility 
with numerous CAD applications.

The following steps will allow you to execute Pole Profile

1. On the VistaCare Plugin go to `Bracebridge --> Pole Profile`.
2. Select the JSON file to work on.
3. Choose the pole profile format and pole profile file type. 
4. Tick the checkbox which pole you want to generate the profile.
5. Fill in Direction column for pole bearing with respect to roadside, default value is 0 degrees.
6. **(Optional)** Choose folder location you want to save your profiles.
7. Click `OK` button to generate the profiles.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>When selecting both <code>XCI</code> and <code>DXF</code> formats along with multiple poles, the plugin performs the following actions:</p>
<ul>
    <li>Generates a side-by-side image of the selected poles in a single AutoCAD file (named the same as the JSON file)</li>
    <li>Creates individual AutoCAD files for each selected pole (named based on the pole label)</li>
</ul>
<p>Additionally, make sure to open the related QGS project file and select the <code>Poles</code> layer or a related layer from <code>Pole Information Source Layer</code> drop down to capture the table information accurately.</p>
</div>

<a data-fancybox="Pole Profiles" href="_static/new_pole_profile.mp4" data-caption="Pole Profiles">
  <img src="_static/new_pole_profile_thumbnail.jpg" alt="Pole Profiles" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>
<br>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>Format Summary Table</p>

<!--Markdown Table Generator Data from https://tabletomarkdown.com/generate-markdown-table/ -->
| Display                                                | **H1 Format**                                                                                                                    | **Lakeland Format**                                                         | **XCI Format**                                                              |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Font Color                                             | RED for MR changes on Hydro space<br>Black on Telco space                                                                    | RED for MR changes on Hydro space<br>Black on Telco space               | RED for MR changes on Hydro space<br>Black on Telco space               |
| Primary wires                                          | All wires are drawn                                                                                                          | Lowest primary height is drawn                                          | Lowest primary height is drawn                                          |
| Primary wires with MR                                  | **'PRIM.'** will be in Bold, Red,<br>**Original Value** in Bold, Red<br>then **MR Value** in **'****()****'** ,Bold, Red | 'PRIM.' in Red<br>Original value in Red<br>then MR value in '()', Red   | 'PRIM.' in Red<br>Original value in '()' and Red<br>then MR value in Red   |
| Neutral/Sec wire                                       | All wires are drawn                                                                                                          | All wires are drawn                                                     | All wires are drawn                                                     |
| Neutral/Sec wire with MR                               | **'NEUT./SEC.'** in Bold, Red<br>**Original Value** in Bold, Red<br>**MR value** in **'****()****'**, Bold, Red          | 'NEUT./SEC.' in Red<br>Original Value in Red<br>MR value in '()', Red   | 'NEUT./SEC.' in  Red<br>Original Value in '()', Red<br>MR value in  Red |
| Proposed guys with<br>Proposed Telco wire              | **'P.BELL/ P.D.G.'** in Bold                                                                                             | **'P.BELL/ P.D.G.'** in Bold                                        | **'P.XPLORE/ D.G.'** in Bold,<br>Blue font color                                  |
| Proposed Telco wire and <br>proposed guy for represenation | Black Color \`DOT\`                                                                                                          | Black Color \`DOT\`                                                     | Blue Color \`DOT\`                                                      |
| Feature in new heights<br>and Original height          | Original height in normal weight<br>New height in '()' in normal weight                                                      | Original height in normal weight<br>New height in '()' in normal weight | Original height in '()'<br>New height in Normal weight<br>              |
| New Feature height value display                       | **New height** in Bold                                                                                                       | **New height** in Bold                                                  | **New height** in Bold                                                  |
| Feature text display                                   | Display in upper case<br>eg. TRANSF.                                                                                         | Display in upper case<br>eg. TRANSF.                                    | Display in upper case<br>eg. TRANSF.                                    |
| Feature height value display                           | Height Value in normal weight                                                                                                | Height Value in normal weight                                           | Height Value in normal weight                                           |
</div>

### Pole Profiles Errors

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>When running the functionality Pole Profiles, it is possible to obtain one of the following messages.</p>
</div>

1. Bar message will show if wrong JSON file is used (non SpidaCalc json file). Make sure to use SpidaCalc generated JSON file.

<a class="" data-lightbox="Pole Profile" href="_static/pole_profile_img/pp_bar_wrong_json_short.png" title="Wrong JSON file" data-title="Wrong JSON file"><img src="_static/pole_profile_img/pp_bar_wrong_json_short.png" class="align-center" width="800px" height="500px" alt="Wrong JSON file">
</a>

2. Bar message will show if JSON file has missing layers (`Existing` or `Proposed`) and script will not proceed.

<a class="" data-lightbox="Pole Profile" href="_static/pole_profile_img/pp_bar_missing_layer_short.png" title="Missing Layer" data-title="Missing Layer"><img src="_static/pole_profile_img/pp_bar_missing_layer_short.png" class="align-center" width="800px" height="500px" alt="Missing Layer">
</a>

3. Bar message will show how many poles have error during populating table information after selecting JSON file(**A**). It will also specify the pole name with its error on the text box (**B**).

<a class="" data-lightbox="Pole Profile" href="_static/pole_profile_img/pp_exclude_poles_with_errors.png" title="Poles with errors" data-title="Poles with errors"><img src="_static/pole_profile_img/pp_exclude_poles_with_errors.png" class="align-center" width="800px" height="500px" alt="Poles with errors">
</a>

4. If any pole in the table have error during pole profile creation, it will specify the pole with its error on the text box.

<a class="" data-lightbox="Pole Profile" href="_static/pole_profile_img/pp_error_during_generation.png" title="Errors during generation" data-title="Errors during generation"><img src="_static/pole_profile_img/pp_error_during_generation.png" class="align-center" width="800px" height="500px" alt="Errors during generation">
</a>

## PAR Profiles

This module, similar to `Pole Profile`, this allows users to generate pole profiles in DXF format, ensuring compatibility with numerous CAD applications. It works exclusively with SpidaCalc JSON files containing a single or double pole layer. If the pole has two layer, it will generate poles for both layers and won't do comparison for both layer unlike with `Pole Profiles`.

The following steps will allow you to execute PAR Profile.
1. In the VistaCare Communications Plugin go to `Tools --> PAR Profiles`.
2. Select the JSON file to work on.
3. Tick the tickbox which pole you want to generate the profile.
4. Fill in Direction column for pole bearing with respect to roadside, default value is 0 degrees.
5. **(Optional)** Choose folder location you want to save your profiles.
6. Click `OK` button to generate the profiles.

<a data-fancybox="PAR Profiles" href="_static/PAR_profile.mp4" data-caption="PAR Profiles">
  <img src="_static/PAR_profile_thumbnail.jpg" alt="PAR Profiles" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>
<br>

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>The tool performs the following actions:</p>
<ul>
    <li>Generates a side-by-side image of the selected poles in a single AutoCAD file (named the same as the JSON file)</li>
    <li>Creates individual AutoCAD files for each selected pole (pole label), if two layer exist for the pole it will name as (pole label_layer name)</li>
</ul>
<p>Additionally, make sure to open the related QGS project file and select the <code>Poles</code> layer or a related layer from <code>Pole Information Source Layer</code> drop down to capture the table information accurately.</p>
</div>

## Katapult Profiles

Similar with `Pole Profiles` and `PAR Profiles`, this module allows the user to generate a CAD format pole profiles using the information from Katapult. The module interface allows the user to choose some or all of poles to be generated. This also has a search bar wherein the user can narrow down the poles from the table.

The following steps will allow you to generate pole profiles using Katapult:
1. In the VistaCare Communications Plugin go to `Tools --> Katapult Profiles`.
2. From browser, copy the Katapult job id and paste it in the line edit. 
   <a class="" data-lightbox="Katapult Profiles" href="_static/katapult_job_id.png" title="Katapult job id" data-title="Katapult job id"><img src="_static/katapult_job_id.png" class="align-center" width="800px" height="500px" alt="Katapult job id">
    </a>
3. Select the poles to be generated.
4. **(Optional)** Choose folder location you want to save your profiles. Default location is at C:/Users/{username}/Desktop/{Katapult Job Name}
5. Click `OK` button to generate the profiles.

### How it Works

<!-- <a class="" data-lightbox="Katapult Profiles" href="_static/katapult_profiles.gif" title="Katapult Profiles" data-title="Katapult Profiles"><img src="_static/katapult_profiles.gif" class="align-center" width="800px" height="500px" alt="Katapult Profiles">
</a> -->

<a data-fancybox="Katapult Profiles" href="_static/katapult_profiles.mp4" data-caption="Katapult Profiles">
  <img src="_static/katapult_profiles_thumbnail.jpg" alt="Katapult Profiles" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>
<br>

## Counts Calculator

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>Counts Calculator can be excecute from CSP or Splice layers</p>
</div>

It uses a tree structure to traverse the nodes along the cable structure. As it moves through each node, it uses the *total_distribution_demand* variable to calculate the counts and update or create the necessary counts.

The following steps will allow you to execute the Counts Calculator functionality:

1. On the VistaCare Communications Plugin go to `Tools --> Counts Calculator`.
2. Fill the following options:

    * CSP Layer: A Point layer with the features will be used as a Start point.
    * Splice Layer: A Point layer with the features will be used as a Start point.
    * FSA Layer: A Polygon layer with the features will be used as a boundary.
    * Cables Layer: A Line layer with the features will be used as a network.
    * Counts Layer: A Text layer where it is going to be storage the information calculated.
    * Invert Start Cables: Radio button that allows to invert the start of the cables excecution.

3. Click on `Select a CSP` or `Select a Splice` to choose the feature where is going to start the calculation.

3. Click on `OK` and wait until the module finishes the execution. 

<a class="" data-fancybox="Counts calculator" href="_static/counts_calculator.mp4" data-caption="Counts calculator"><img src="_static/counts_calculator.gif" class="align-center" width="800px" height="500px" alt="Counts calculator">
</a>

## Spans Generator

This module allows the user to generate `Spans` feature using information from `Strand` feature and poles layer (Point geometry) as endpoint. 

The following steps will allow you to generate `Spans` feature:
1. In the VistaCare Communications Plugin go to `Tools --> Spans Generator`.
2. Select the Pole information layer from Layers table.
3. Select the Strand Information source layer.
4. In Generate Span Distance groupbox, select which layer where you want to save the spans feature (`Spans`).
5. Click `OK` button to generate the spans.

### How it Works

<a data-fancybox="Spans Generator" href="_static/spans_generator.mp4" data-caption="Spans Generator">
  <img src="_static/spans_generator.jpg" alt="Spans Generator" 
      class="align-center" style="width: 700px; height: 400px; cursor: pointer;">
</a>

---

## Strand Automate

The **Strand Automate** tool creates continuous strand lines from your span network with one click. It groups spans based on their type (case field), follows the network, and outputs properly segmented strand lines.

**What the tool does:**
- Reads and filters your spans based on their *case* (New Strand, Overlash, Existing, etc.).
- Follows the spans and automatically traces each continuous route.
- Breaks and starts new strands when the angle between spans is too sharp (tight corner).
- Produces a temporary strand layer

**How to use:**
1. Open the plugin and select **Tools → Strand Automate**.
2. Select your *Spans* layer.
3. Adjust angle tolerance if needed.
4. Click **OK**.

**Output:**
- A new memory layer named **strands_automate** containing strand features.

---

## Anchor Automate

The **Anchor Automate** tool analyzes your span geometry and automatically generates anchor lines at the poles where anchors are required. It only works where spans have New Strand in their case and has different
behavior when New Strand is touching Existing Strand since they have existing anchors.

**What the tool does:**
- Detects each junction where spans meet.
- Measures the angle between incoming/outgoing spans.
- Decides the correct anchor configuration based on angle thresholds:
  - **Single span touching pole** → 1 dead end anchor opposite the span  
  - **Two spans touching pole** → outward bisector anchor (or two anchors, when appropriate)   
- Draws the anchor line at the correct offset distance from the pole.

**How to use:**
1. Open the plugin and go to **Tools → Anchor Automate**.
2. Select your *Spans* layer.
3. Choose angle settings or use defaults.
4. Click **OK**.

**Output:**
- A memory layer named **anchor_lines** containing anchors placed at the correct junction angles.

---

## Splicing Test Sheet Generator

The **Splicing Test Sheet Generator** tool automatically creates standardized *`Testing <FSA>_YYYYMMDD_HHMM.xlsx`* workbooks used by field technicians during fiber testing.

It gathers all splices, terminals, and fiber routes for each selected FDSA, then builds a structured Excel workbook based on the VistaCare testing template.

**What the tool does:**
- Identifies the CSP inside the selected FDSA.
- Follows the distribution cables to every splice in the FDSA.
- Creates one testing sheet per splice using your provided Excel template.
- Fills in:
  - Fiber numbers  
  - Cable names  
  - Terminal assignments  
  - Required testing notes  
- Produces a clean, technician-ready package.

**How to use:**
1. Go to **Tools → Splicing Test Sheet Generator**.
2. Pick your output folder.
3. Before running the tool, select one or many FDSA boundaries.
4. Click **OK**.

**Output:**
- Completed Excel workbooks named **`Testing_<FSA>.xlsx`** for each FSA

---

## Splicing Package Generator

The **Splicing Package Generator** automatically builds full splice packages, combining splice data, cable routing, and fiber assignments into a standardized Excel deliverable.

**What the tool does:**
- Extracts all splice points and their connected cables.
- Fills in splice details based on VistaCare’s fiber routing logic.
- Generates per-splice worksheets showing:
  - Cable-to-cable fiber mapping  
  - Fiber assignment tables    

**How to use:**
1. Before running the tool, select one or many FDSA boundaries
2. Navigate to **Tools → Splicing Package Generator**.
3. Pick your output folder.
4. Click **OK**.

**Output:**
- A complete Excel splicing package **`<FSA>_Splice_Package_<yyyymmdd>.xlsx`** for each FSA ready for construction crews.

---

## Tube Sheet Generator

The **Tube Sheet Generator** creates standardized **fiber tube sheet Excel deliverables** for one or more selected FDSAs.  
It analyzes the cable and splice network starting from the CSP, follows fiber routing through splices, and generates a clear ribbon-by-ribbon representation of fiber usage.

This tool is designed specifically for **NWT projects** and follows NWT tube sheet standards.

### How to use

1. Select one or more **FDSA features** in the FDSA layer.
2. Open the VistaCare Communications Plugin and go to  
   `Tools --> Tube Sheet Generator`
3. Choose an **Export Folder**.
4. Click `OK` and wait for the process to complete.

A summary of generated files and skipped FDSAs will be displayed after completion.

---

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>

⚠️ This tool is **NWT-only** and follows NWT-specific tube sheet rules and layouts.

</p>
</div>

---

### Required layer fields

The tool validates required fields before processing and will skip an FDSA if any are missing.

**Cables layer**
- `category`
- `plan_id`
- `fiber_capacity`
- `count`

**Splice layer**
- `location`
- `sp_id` (optional, used for labeling)

**CSP layer**
- `size`
- `name` or `csp_name` (optional, used for labeling)
- `location` (optional, used for labeling)
- `CLLI` (optional, used for labeling)

**FDSA layer**
- `name`
- `clli_code` (optional, used for labeling)
---

### CSP behavior by size

| CSP Size | Behavior |
|--------|---------|
| 144 / 288 | CSP Stub tables generated |
| 576 | Dual-stub logic (Stub A / Stub B) |
| 1008+ | Full CSP table with feeder block |

---

### Output

- One Excel file per selected FDSA
- File naming format:  
  **`<FDSA_NAME>_Tube_Sheet_<YYYYMMDD_HHMM>.xlsx`**
- Each workbook contains:
  - CSP table or CSP stub tables
  - One table per cable generation
  - Ribbon-level fiber allocation
  - Clear splice labeling (`SPLICE @ LOCATION`)

---

### Skipped FDSAs

An FDSA may be skipped if:
- It has no geometry
- No CSP is found inside the boundary
- No cables intersect the FDSA
- Required fields are missing
- **CSP size is 576 and exactly two CSP stub cables cannot be identified within the FDSA**

Skipped FDSAs and reasons are reported in the results panel.

---

## Add Plus Code & Lat/Long to Layer

This tool populates **WGS84 latitude, longitude, and Plus Codes** for point layers.  
It automatically detects existing fields, transforms coordinates to EPSG:4326, and safely writes values without overwriting existing data unless explicitly enabled.

The tool only writes to fields that already exist in the layer and supports working on selected features only.

The following steps will allow you to execute the Add Plus Code & Lat/Long to Layer functionality:

1. On the VistaCare Communications Plugin go to `Tools --> Add Plus Code & Lat/Long to Layer`.
2. Select a **Point Layer** from the dropdown list.
3. (Optional) Enable **Use only selected features** to process only selected points.
4. (Optional) Enable **Overwrite existing values** to replace populated fields.
5. Adjust precision settings if required:
   * **Plus code length** (default: 11)
   * **Lat/Long precision (decimals)** (default: 8)
6. Click `Run` and wait for the tool to complete.

A detailed execution log will be displayed showing updated and skipped features.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>

**Accepted field names (case-insensitive):**

* Latitude: `lat`, `latitude`  
* Longitude: `lon`, `lng`, `long`, `longitude`  
* Plus Code: `pluscode`, `plus_code`, `pluscodes`, `plus_codes`

If a field is not found, that value will be skipped and reported in the log.

</p>
</div>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>

* Coordinates are always calculated in **WGS84 (EPSG:4326)** regardless of the layer CRS.
* Multipart and single-point geometries are supported.
* Features with missing geometry are skipped.
* All edits are grouped into a single undoable edit operation.

</p>
</div>

### Precision Reference

| Plus Code Length | Approximate Area |
| ---------------- | ---------------- |
| 10               | ~14 × 14 m       |
| 11               | ~2.8 × 3.5 m     |
| 12               | ~0.56 × 0.87 m   |

Typical values:
* **Plus Code Length:** 11  
* **Lat/Long Precision:** 8 decimals

<br>
## Cable Labeling Plan ID [NWT]

This tool labels feeder, distribution, preterm, terminal, and drop cables for the selected FDSA polygons and writes `plan_id` values directly back to the cables layer.

<div class="note">
<p class="admonition-title">WARNING</p>
<p>This tool edits existing layers directly and cannot be undone.</p>
</div>

The following steps will allow you to execute the Cable Labeling Plan ID functionality:

1. Open `fdsa_boundaries` attribute table and select one FDSA polygon.
2. On the VistaCare Communications Plugin go to `Tools --> Cable Labeling Plan ID [NWT]`.
3. Fill in the required layers:

    * Cables Layer
    * Splice Layer
    * CSP Layer
    * FDSA Boundaries Layer

4. Set optional parameters:

    * Starting Distribution Letter

5. Click `OK`.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>

Behavior:
* Feeders are numbered by splice depth from the FSA CSP.
* Distribution and preterm cables are treated as branch-carrying cables.
* 576 CSPs reserve the first two branch letters for the two longest CSP-side stubs.
* Terminals inherit their parent branch and are ordered by distance along parent branch.
* Drops inherit their terminal label.
* Any cable that cannot be labeled is written as `UNCONNECTED`.

</p>
</div>

## Counts Calculator [NWT]

This tool assigns fiber counts to cables and writes the results to the counts table.

<div class="note">
<p class="admonition-title">WARNING</p>
<p>This tool edits existing layers directly and cannot be undone.</p>
</div>

The following steps will allow you to execute the Counts Calculator functionality:

1. Open `fdsa_boundaries` attribute table and select one FDSA polygon.
2. On the VistaCare Communications Plugin go to `Tools --> Counts Calculator [NWT]`.
3. Fill in the required layers:

    * Cables Layer
    * CSP Layer
    * Splice Layer
    * Boundary Layer
    * Counts Layer

4. Set optional parameters:

    * Count Prefix
    * Feeder Prefix
    * Start at Selected Splice
    * Splice Start Count

5. Click `OK`.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>

Behavior:
* Uses existing `plan_id` values to build the branch hierarchy.
* Treats distribution and preterm as branch cables.
* Drops are ignored.
* Rows with `manual=true` are preserved.
* Supports optional splice-start mode for downstream subtree recalculation.

</p>
</div>

## QGIS Labels [NWT]

This tool validates cables inside a selected FSA using splice demand information and network topology. It also builds multi-line `qgis_label` values and adds them to the cables layer.

<div class="note">
<p class="admonition-title">WARNING</p>
<p>This tool edits existing layers directly and cannot be undone.</p>
</div>

The following steps will allow you to execute the QGIS Labels functionality:

1. Open `fdsa_boundaries` attribute table and select one FDSA polygon.
2. On the VistaCare Communications Plugin go to `Tools --> QGIS Labels [NWT]`.
3. Fill in the required layers:

    * Cables Layer
    * FSA Layer
    * CSP Layer
    * Splice Layer

4. Set optional parameters:

    * Label Field Name
    * Count Label Mode (Show all counts, Live counts, No counts)

5. Click `OK`.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>

Behavior:
* Distribution and preterm cables are splice-validated before labels are written.
* Midspan preterm attachments are supported.
* Unreachable cables inside the selected FSA have labels cleared.

Common Errors:
* `Cable not connected.`
* `No splice located at cable branch.`
* `Splice data does not match feeding cable.`

</p>
</div>

## Cable Spec Report (CSR) [NWT]

This tool exports one Cable Spec Report per selected FSA. The report summarizes routed cable paths, poles, slack, and terminals.

The following steps will allow you to output the Cable Spec Report:

1. Open `fdsa_boundaries` attribute table and select one or more FSA polygons.
2. On the VistaCare Communications Plugin go to `Tools --> Cable Spec Report (CSR) [NWT]`.
3. Fill in the required layers:

    * Cables Layer
    * Counts Layer
    * Spans Layer
    * Poles Layer
    * Splice Layer
    * CSP Layer
    * FSA Layer
    * Slack Layer
    * Strand Layer
    * Conduit Layer
    * UG Structure Layer

5. Select the output folder.
6. Click `OK`.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>

The report includes:
* Distribution and preterm branch summaries
* Pole-to-pole routing distances
* Slack locations and endpoint slack
* Terminal and tether details
* Start/end location labels resolved from poles, splices, CSPs, and structures

Default output folder:
`C:\Temp\CSR`

</p>
</div>

## Major Materials Order Form [NWT]

This tool generates a Major Materials Cable Order Form workbook for selected FDSAs.

The following steps will allow you to execute the Major Materials Order Form functionality:

1. Open `fdsa_boundaries` attribute table and select one or more FSA polygons.
2. On the VistaCare Communications Plugin go to `Tools --> Major Materials Order Form [NWT]`.
3. Select the BOM template Excel file (autofilled).
4. Select the output folder.
5. Click `OK`.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>

Features:
* Generates formatted Excel order forms
* Supports single-FSA and multi-FSA exports
* Automatically creates timestamped filenames
* Uses the NWT BOM template

Default output folder:
`C:\Temp\CablesBOM`

</p>
</div>

## BOM Report [NWT]

This tool exports the NWT Bill of Materials (BOM) and Bill of Labour (BOL) for the currently selected FDSA polygons.

The following steps will allow you to execute the BOM Report functionality:

1. Open `fdsa_boundaries` attribute table and select one or more FSA polygons.
2. On the VistaCare Communications Plugin go to `Tools --> BOM Report [NWT]`.
3. Fill in the following options:

    * FDSA boundaries layer: Select the polygon layer containing the selected FDSA features.
    * BOM/BOL template path: Select the NWT BOM/BOL template Excel file (autofilled).
    * Output folder: Choose where the generated `.xlsx` file will be saved.

4. Click `OK`.

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>

Required project setup:
* The FDSA layer must contain `clli_code` and `name` fields.
* The project must contain every layer referenced in the template `Sort Codes` sheet.
* The project must contain every layer referenced in the template `Key Indicators` sheet.
* Any fields referenced by template filter expressions, sum fields, or unique fields must exist.

Default template:
`K:\ENGINEERING\Programming\NWT_BOM_BOL_TEMPLATE_V3.xlsx`

Default output folder:
`C:\Temp\NWTBOMBOL`

</p>
</div>
