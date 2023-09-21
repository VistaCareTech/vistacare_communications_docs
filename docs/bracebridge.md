# Bracebridge

## Bracebridge Tracker

The Bracebridge Tracker module 

The following steps will allow you to execute the Bracebridge Tracker functionality:

1. On the VistaCare Communications Plugin go to `Bracebridge --> Bracebridge Tracker`.
2. Fill the following options:

    * FSA Layer: FSA Layer with the database structure.
    * Plans Layer: Plans Layer with the database structure.
    * Cables Layer: Cables Layer with the database structure.
    * Conduit Layer: Conduit Layer with the database structure.
    * Fibre drops Layer: Fibre drops Layer with the database structure.
    * Splices Layer: Splices Layer with the database structure.
    * UG Structures Layer: UG Structures Layer with the database structure.
    * Strands Layer: Strands Layer with the database structure.
    * Anchors Layer: Anchors Layer with the database structure.
    * Poles Layer: Poles Layer with the database structure.
    * Folder for export: Choose the place where the excel file will be exported.

3. Click on `OK` and wait until the module finishes the execution. 

<a class="" data-lightbox="Bracebridge Tracker" href="_static/bracebridge_tracker.gif" title="Bracebridge Tracker" data-title="Bracebridge Tracker"><img src="_static/bracebridge_tracker.gif" class="align-center" width="800px" height="500px" alt="Bracebridge Tracker">
</a>

## Pole Profile

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>If output folder location is empty, output files will be save at input json folder location </p>
</div>

SVG 2D image generator for Pole Profile P'Eng Reports.

The following steps will allow you to execute Pole Profile

1. On the VistaCare Plugin go to `Bracebridge --> Pole Profile`.
2. Select the JSON file to work on.
3. Tick the checkbox which pole you want to generate the profile.
4. Fill in Direction column for pole bearing with respect to roadside, default value is 0 degrees.
5. **(Optional)** Choose folder location you want to save your profiles.
6. Click `OK` button to generate the profiles.

<a class="" data-lightbox="Pole Profile" href="_static/pole_profile_gif.gif" title="Pole Profile" data-title="Pole Profile"><img src="_static/pole_profile_gif.gif" class="align-center" width="800px" height="500px" alt="Pole Profile">
</a> 

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

## Vertical Separation

CSV generator for P'Eng Report Exhibit 1 DESIGN DATA Vertical Separation (At Pole) 

The following steps will allow you to execute Vertical Separation

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>If output folder location is empty, output files will be save at input json folder location </p>
</div>

1. On the VistaCare Plugin go to `Bracebridge --> Vertical Separation`.
2. Select the JSON file to work on.
3. Tick the checkbox which pole you want to generate .
4. **(Optional)** Choose folder location you want to save your table.
5. Click `OK` button to generate table

<a class="" data-lightbox="Vertical Separation" href="_static/vertical_separation_gif.gif" title="Vertical Separation" data-title="Vertical Separation"><img src="_static/vertical_separation_gif.gif" class="align-center" width="800px" height="500px" alt="Vertical Separation">
</a>

### Vertical Separation Errors

<div class="warning">
<p class="admonition-title">WARNING</p>
<p>When running the functionality Vertical Separation, it is possible to obtain one of the following messages.</p>
</div>

1. Bar message will show if wrong JSON file is used (non SpidaCalc json file). Make sure to use SpidaCalc generated JSON file.

<a class="" data-lightbox="Vertical Separation" href="_static/vertical_separation_img/vs_bar_msg_wrong_json_short.png" title="Wrong JSON file" data-title="Wrong JSON file"><img src="_static/vertical_separation_img/vs_bar_msg_wrong_json_short.png" class="align-center" width="800px" height="500px" alt="Wrong JSON file">
</a>

2. Bar message will show if `Proposed` layer has an issue and script will not proceed.

<a class="" data-lightbox="Vertical Separation" href="_static/vertical_separation_img/vs_bar_msg_layer_issue_short.png" title="Layer issue" data-title="Layer issue"><img src="_static/vertical_separation_img/vs_bar_msg_layer_issue_short.png" class="align-center" width="800px" height="500px" alt="Layer issue">
</a>

3. If selected pole was unable to extract information due to an error, it will display the pole and its error in the textbox. A hyperlink of the output will be displayed in the textbox.

<a class="" data-lightbox="Vertical Separation" href="_static/vertical_separation_img/vs_textbox_information.png" title="Textbox information" data-title="Textbox information"><img src="_static/vertical_separation_img/vs_textbox_information.png" class="align-center" width="800px" height="500px" alt="Textbox information">
</a>

## Mr Automation

The Mr Automation Plugin is designed to simplify the assessment of different make ready conditions. It imports data from SPIDA Calc JSON files and Katapult API which automatically evaluates the conditions to generate a well-structured Excel report.

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>If output folder location is empty, output files will be save at input json folder location </p>
</div>

The following steps will allow you to execute Mr Automation

1. On the VistaCare Plugin go to `Bracebridge --> Mr Automation`.
2. Select the JSON file to work on.
3. Select the Katapult API file to work on. 
4. Tick the checkbox which pole you want to generate .
5. **(Optional)** Choose folder location you want to save your table.
6. Click `OK` button to generate excel report.

<a class="" data-lightbox="Mr Automation" href="_static/MR_gif.gif" title="Mr Automation" data-title="Mr Automation"><img src="_static/MR_gif.gif" class="align-center" width="800px" height="500px" alt="Mr Automation">
</a> 