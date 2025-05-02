# <img src="../_static/qgis_plugins/icons/peng/peng.png" alt="PEng" width="24px"> PEng


## <img src="../_static/qgis_plugins/icons/peng/span_clearance.png" alt="Span Clearance and Vertical Separation" width="24px"> Span Clearance and Vertical Separation

CSV generator for PEng Report Exhibit 1 DESIGN DATA Vertical Separation (At Pole) 

### How It Works

The following steps will allow you to execute Vertical Separation:

1. On the VistaCare Plugin go to **PEng --> Span Clearance and Vertical Separation**.
2. Select the JSON file to work on.
3. Tick the checkbox which pole you want to generate .
4. **(Optional)** Choose folder location you want to save your table.
5. Click **OK** button to generate table

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>If <b>Output Folder Location</b> is empty, output files will be save at input json folder location </p>
</div>

<a class="" data-lightbox="Vertical Separation" href="../_static/qgis_plugins/peng/vertical_separation_gif.gif" title="Vertical Separation" data-title="Vertical Separation"><img src="../_static/qgis_plugins/peng/vertical_separation_gif.gif" class="align-center" width="800px" height="500px" alt="Vertical Separation">
</a>

### Span Clearance and Vertical Separation Errors

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>When running the functionality Span Clearance and Vertical Separation, it is possible to obtain one of the following messages.</p>
</div>

1. Bar message will show if wrong JSON file is used (non SpidaCalc json file). Make sure to use SpidaCalc generated JSON file.

<a class="" data-lightbox="Vertical Separation" href="../_static/qgis_plugins/peng/vertical_separation_img/vs_bar_msg_wrong_json_short.png" title="Wrong JSON file" data-title="Wrong JSON file"><img src="../_static/qgis_plugins/peng/vertical_separation_img/vs_bar_msg_wrong_json_short.png" class="align-center" width="800px" height="500px" alt="Wrong JSON file">
</a>

2. Bar message will show if **Proposed** layer has an issue and script will not proceed.

<a class="" data-lightbox="Vertical Separation" href="../_static/qgis_plugins/peng/vertical_separation_img/vs_bar_msg_layer_issue_short.png" title="Layer issue" data-title="Layer issue"><img src="../_static/qgis_plugins/peng/vertical_separation_img/vs_bar_msg_layer_issue_short.png" class="align-center" width="800px" height="500px" alt="Layer issue">
</a>

3. If selected pole was unable to extract information due to an error, it will display the pole and its error in the textbox. A hyperlink of the output will be displayed in the textbox.

<a class="" data-lightbox="Vertical Separation" href="../_static/qgis_plugins/peng/vertical_separation_img/vs_textbox_information.png" title="Textbox information" data-title="Textbox information"><img src="../_static/qgis_plugins/peng/vertical_separation_img/vs_textbox_information.png" class="align-center" width="800px" height="500px" alt="Textbox information">
</a>


## <img src="../_static/qgis_plugins/icons/peng/spidacalc_validator.png" alt="SpidaCalc Validator" width="24px"> SpidaCalc Validator

Plugin to extract information from SpidaCalc JSON and generate PDF, XLS report for required missing information.

### How It Works

The following steps will allow you to execute the SpidaCalc Validator functionality:

1. On the VistaCare Plugin go to **PEng --> SpidaCalc Validator**.
2. Choose application to validate SpidaCalc JSON file.

    * Pole Profile
    * Anchor Importer (SpidaCalc to DB)
    * Vertical Separation

3. On user interface, select JSON file to work on.
4. **(Optional)** Choose folder location you want to save your reports.
5. Click **OK** button to generate table

<a class="" data-lightbox="Spidacalc Validator" href="../_static/qgis_plugins/peng/spidacalc_validator_gif.gif" title="Spidacalc Validator" data-title="Spidacalc Validator"><img src="../_static/qgis_plugins/peng/spidacalc_validator_gif.gif" class="align-center" width="800px" height="500px" alt="Spidacalc Validator">
</a>

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>

1. Brief Description in Text Box: 
   * Description in <span style="color: #000000; font-weight:bold">'BLACK'</span> font color are general information
   * Description in <span style="color: #FF0000; font-weight:bold">'RED'</span> font color are pole feature missing information
   * Description in <span style="color: #008000; font-weight:bold">'GREEN'</span> font color are completed reports

2. For **PDF report**, missing information from JSON or any other information source will have its value as **None** and font color to <span style="color: #FF0000; font-weight:bold">'RED'</span>.

3. For **XLS report**, missing information from JSON or any other information source will have a value of **None** and its cell font color to <span style="color: #FF0000; font-weight:bold">'RED'</span>. Also, if a layer is missing, rest of the row of layer and pole will be empty.
</div>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>All the detailed information can be found in the generated reports.</p>
</div>