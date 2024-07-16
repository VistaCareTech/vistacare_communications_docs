# Port Burwell

## PAR Profiles

This module, similar to Bracebridge's Pole Profile, allows users to generate pole profiles in DXF format, ensuring compatibility with numerous CAD applications. It works exclusively with SpidaCalc JSON files containing a single layer. For JSON files with double layers, use the Bracebridge --> Pole Profile plugin.

The following steps will allow you to execute PAR Profile.
1. In the VistaCare Communications Plugin go to `Port Burwell --> PAR Profiles`.
2. Select the JSON file to work on.
3. Tick the tickbox which pole you want to generate the profile.
4. Fill in Direction column for pole bearing with respect to roadside, default value is 0 degrees.
5. **(Optional)** Choose folder location you want to save your profiles.
6. Click `OK` button to generate the profiles.

<a class="" data-lightbox="PAR Profile" href="_static/PAR_profile.gif" title="PAR Profile" data-title="PAR Profile"><img src="_static/PAR_profile.gif" class="align-center" width="800px" height="500px" alt="PAR Profile">
</a>

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>The plugin performs the following actions:</p>
<ul>
    <li>Generates a side-by-side image of the selected poles in a single AutoCAD file (named the same as the JSON file)</li>
    <li>Creates individual AutoCAD files for each selected pole (named based on the pole label)</li>
</ul>
<p>Additionally, make sure to open the related QGS project file and select the <code>Poles</code> layer or a related layer from <code>Pole Information Source Layer</code> drop down to capture the table information accurately.</p>
</div>
