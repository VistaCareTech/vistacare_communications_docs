# Database Triggers Documentation 

Below you will find the list of triggers currently implemented in the database. 

## Elgin

**Folder location:** `K:\ENGINEERING\Xplornet Communications Inc (XCI)\Ontario\QGIS\Scripts\Triggers`

| **Table/Folder Name** |               **Trigger Name**              | **Insert** | **Update** |
|:---------------------:|:-------------------------------------------:|:----------:|:----------:|
|        anchors        | trigger_insert_anchor_pole_scid             |      X     |            |
|        anchors        | trigger_insert_anchors_geom_points          |      X     |            |
|        anchors        | trigger_insert_and_update_location_anchors  |      X     |      X     |
|        anchors        | trigger_update_anchors_geom_points          |            |      X     |
|         cables        | trigger_insert_and_update_location_cables   |      X     |      X     |
|        conduit        | trigger_insert_and_update_location_conduits |      X     |      X     |
|        conduit        | trigger_update_conduits                     |            |      X     |
|       peng_scope      | trigger_update_civiccount_pengscope         |            |      X     |
|       peng_scope      | trigger_update_pengscope_from_pengscope     |      X     |      X     |
|         spans         | trigger_insert_update_spans                 |      X     |      X     |
|         spans         | trigger_update_pengscope_from_span          |      X     |      X     |
|         strand        | trigger_insert_and_update_location_strand   |      X     |      X     |

## Big Bay and Patterson Lake

## Newfoundland