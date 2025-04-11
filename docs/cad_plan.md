# Cad Plan

## CAD Plan Block Export

CAD Plan Block export is designed to streamline export of GIS information into CAD blocks with attributes and layer. Integrating with UI this gives user the flexibility of handling multiple entities such as Poles, Splice, MPT's, Civic, Cables, etc. This functionality also ensures the CRS are transformed uniformly while using memory data without affecting the original data. 

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

<a class="" data-lightbox="CAD Export" href="_static/cad_export.gif" title="CAD Export" data-title="CAD Export"><img src="_static/cad_export.gif" class="align-center" width="800px" height="500px" alt="CAD Export">
</a>

<div class="note">
<p class="admonition-title">IMPORTANT</p>
<p>Make sure to run <b>`Audit`</b> command after export is completed</p>
</div>

<div class="seealso">
<p class="admonition-title">TIP</p>
<p>NL Project CAD export Field name Guide </p>
</div>

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