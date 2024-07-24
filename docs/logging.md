# Database Tracking Documentation 

The development of a tracking system in the database is crucial for maintaining the integrity, security, and traceability of data. This system allows for the recording of all modifications made to database tables, providing a detailed history of each change, including the action performed, the user who carried it out, and the exact time of the change. This information is vital for auditing activities, debugging issues, and recovering data in case of errors or accidental deletions. 

## Database Tracking 



The following steps will allow you to execute the database tracking functionality, On the AZURE - XCI server, specifically on the Postgres database:

<a class="" data-lightbox="Overview_Database_logging" href="_static/Logging_database/Overview_Database_logging.png" title="QGIS Install" data-title="QGIS Install"><img src="_static/Logging_database/Overview_Database_logging.png" class="align-center" width="800px" height="500px" alt="Overview_Database_logging">
</a>

### 1. Creating the Logging Table

 we create the tracking_history table in the logging schema. This table records details of change operations (inserts, updates, and deletes) in other database tables. Each column has a specific purpose:

``` Sql -- Create the logging table with the feature_id column after table_name
CREATE TABLE public.tracking_history (
    audit_id serial PRIMARY KEY,                         
    change_time timestamptz NOT NULL DEFAULT now(),      
    action char(20) NOT NULL CHECK (action IN ('INSERT', 'UPDATE', 'DELETE')), 
    username text NOT NULL,                               
    table_name text NOT NULL,                            
    feature_id integer,                                   
    old_geom geometry,                                   
    new_geom geometry,                                    
    row_data jsonb NOT NULL                               
); 
```

<a class="" data-lightbox="Creating_Tracking_table" href="_static/Logging_database/Creating_Tracking_table.png" title="Creating_Tracking_table" data-title="Creating_Tracking_table"><img src="_static/Logging_database/Creating_Tracking_table.png" class="align-center" width="800px" height="500px" alt="Creating_Tracking_table">
</a>

### 2. Creating the Trigger Function

We define a trigger function that logs changes in the monitored tables. Depending on the type of operation (INSERT, UPDATE, DELETE), the function inserts a record into the tracking_history table with the details of the change:

``` Sql -- Create or replace the trigger function for the changelog
CREATE OR REPLACE FUNCTION public.tracking_trigger_function()
RETURNS TRIGGER
LANGUAGE plpgsql
SECURITY DEFINER ---This line ensures that the function runs with the permissions of the function owner (solution)
AS $$
BEGIN
    BEGIN
        -- If the operation is DELETE
        IF TG_OP = 'DELETE' THEN
            -- Insert a log entry for the DELETE operation
            INSERT INTO public.tracking_history (change_time, action, username, table_name, feature_id, old_geom, new_geom, row_data)
            VALUES (now(), 'DELETE', session_user, TG_TABLE_NAME, OLD.id, OLD.geom, NULL, to_jsonb(OLD));
        
        -- If the operation is INSERT
        ELSIF TG_OP = 'INSERT' THEN
            -- Insert a log entry for the INSERT operation
            INSERT INTO public.tracking_history (change_time, action, username, table_name, feature_id, old_geom, new_geom, row_data)
            VALUES (now(), 'INSERT', session_user, TG_TABLE_NAME, NEW.id, NULL, NEW.geom, to_jsonb(NEW));
        
        -- If the operation is UPDATE
        ELSIF TG_OP = 'UPDATE' THEN
            -- Check if there is a previous update record
            IF NOT EXISTS (SELECT 1 FROM public.tracking_history WHERE feature_id = NEW.id AND action = 'UPDATE') THEN
                -- Save the original geometry before any updates
                INSERT INTO public.tracking_history (change_time, action, username, table_name, feature_id, old_geom, new_geom, row_data)
                VALUES (now(), 'ORIGINAL', session_user, TG_TABLE_NAME, NEW.id, OLD.geom, NULL, to_jsonb(OLD));
            END IF;

            -- Save the new update
            INSERT INTO public.tracking_history (change_time, action, username, table_name, feature_id, old_geom, new_geom, row_data)
            VALUES (now(), 'UPDATE', session_user, TG_TABLE_NAME, NEW.id, OLD.geom, NEW.geom, to_jsonb(NEW));
            
            -- Notify the 'layer_update' channel
            PERFORM pg_notify('layer_update', 'update');
        END IF;
    EXCEPTION WHEN OTHERS THEN
        -- Log the error or handle it
        RAISE NOTICE 'Error in trigger function: %', SQLERRM;
    END;
    RETURN NULL;
END;
$$;

```
### 3. Creating Triggers for Specific Tables

We create triggers for any target table, so that any insert, update, or delete operation on these tables is recorded in tracking_history.

``` Sql -- Create the trigger for the 'cables' table
CREATE TRIGGER tracking_trigger_cables
AFTER INSERT OR UPDATE OR DELETE ON public.cables
FOR EACH ROW EXECUTE FUNCTION public.tracking_trigger_function();
```
### 4. Checking Results in the Logging Table

To verify the records in the audit table, you can use the following query to order the results by audit_id:

``` Sql -- Check the results in the audit table
SELECT * FROM public.tracking_history
ORDER BY audit_id ASC;
```
<a class="" data-lightbox="QGIS Install" href="_static/Logging_database/Cheking_results_Tracking_table.png" title="QGIS Install" data-title="QGIS Install"><img src="_static/Logging_database/Cheking_results_Tracking_table.png" class="align-center" width="800px" height="500px" alt="Cheking_results_Tracking_table">
</a>


* You can also filter the records by date ranges and username:

``` Sql -- Select by date ranges and users in public.tracking_history
SELECT *
FROM public.tracking_history
WHERE change_time BETWEEN '2024-06-07 00:00:00' AND '2024-06-07 23:59:59'
AND username = 'jonathan.diaz';
```
<a class="" data-lightbox="QGIS Install" href="_static/Logging_database/Filter_by_time.png" title="QGIS Install" data-title="QGIS Install"><img src="_static/Logging_database/Filter_by_time.png" class="align-center" width="800px" height="500px" alt="select_data_from_tracking_table">
</a>
### 5. Recovering Deleted Data

To Recover deleted data in cables_test, select the relevant data from the audit table using the audit_id and reinsert it into the original table.

``` Sql 
-- Recovering deleted data in 'cables_test'
INSERT INTO public.cables (
    id, 
    geom, 
    status, 
    design_state, 
    category, 
    armor_type, 
    cable_type, 
    tether_type, 
    environment_type, 
    duct_size, 
    fiber_capacity, 
    transport_demand, 
    feeder_demand, 
    distribution_demand, 
    spare, 
    total_distribution_demand, 
    total_demand, 
    calc_length, 
    premise_length, 
    start_structure_id, 
    end_structure_id, 
    loopback, 
    wiring_limits, 
    construction_complete, 
    cable_id, 
    peng_visible, 
    placement, 
    terminal_mc
)
SELECT 
    (row_data->>'id')::integer AS id,
    old_geom,
    row_data->>'status' AS status,
    row_data->>'design_state' AS design_state,
    row_data->>'category' AS category,
    row_data->>'armor_type' AS armor_type,
    row_data->>'cable_type' AS cable_type,
    row_data->>'tether_type' AS tether_type,
    row_data->>'environment_type' AS environment_type,
    row_data->>'duct_size' AS duct_size,
    (row_data->>'fiber_capacity')::integer AS fiber_capacity,
    (row_data->>'transport_demand')::integer AS transport_demand,
    (row_data->>'feeder_demand')::integer AS feeder_demand,
    (row_data->>'distribution_demand')::integer AS distribution_demand,
    (row_data->>'spare')::integer AS spare,
    (row_data->>'total_distribution_demand')::integer AS total_distribution_demand,
    (row_data->>'total_demand')::integer AS total_demand,
    (row_data->>'calc_length')::double precision AS calc_length,
    (row_data->>'premise_length')::double precision AS premise_length,
    row_data->>'start_structure_id' AS start_structure_id,
    row_data->>'end_structure_id' AS end_structure_id,
    row_data->>'loopback' AS loopback,
    row_data->>'wiring_limits' AS wiring_limits,
    (row_data->>'construction_complete')::boolean AS construction_complete,
    row_data->>'cable_id' AS cable_id,
    row_data->>'peng_visible' AS peng_visible,
    row_data->>'placement' AS placement,
    row_data->>'terminal_mc' AS terminal_mc
FROM public.tracking_history
WHERE action = 'DELETE'
AND audit_id = 33 -- this is an example for audit_id
AND table_name = 'cables_test';
```

### 6. Recovering Updated Data

To recover updated data in cables_test, select the relevant data from the audit table and insert or update it in the original table using ON CONFLICT.

``` Sql 
--- Recovering updated data in 'cables_test'
WITH selected_record AS (
    SELECT 
        (row_data->>'id')::integer AS id,
        (row_data->>'geom')::geometry AS geom,
        row_data->>'status' AS status,
        row_data->>'design_state' AS design_state,
        row_data->>'category' AS category,
        row_data->>'armor_type' AS armor_type,
        row_data->>'cable_type' AS cable_type,
        row_data->>'tether_type' AS tether_type,
        row_data->>'environment_type' AS environment_type,
        row_data->>'duct_size' AS duct_size,
        (row_data->>'fiber_capacity')::integer AS fiber_capacity,
        (row_data->>'transport_demand')::integer AS transport_demand,
        (row_data->>'feeder_demand')::integer AS feeder_demand,
        (row_data->>'distribution_demand')::integer AS distribution_demand,
        (row_data->>'spare')::integer AS spare,
        (row_data->>'total_distribution_demand')::integer AS total_distribution_demand,
        (row_data->>'total_demand')::integer AS total_demand,
        (row_data->>'calc_length')::double precision AS calc_length,
        (row_data->>'premise_length')::double precision AS premise_length,
        row_data->>'start_structure_id' AS start_structure_id,
        row_data->>'end_structure_id' AS end_structure_id,
        row_data->>'loopback' AS loopback,
        row_data->>'wiring_limits' AS wiring_limits,
        (row_data->>'construction_complete')::boolean AS construction_complete,
        row_data->>'cable_id' AS cable_id,
        row_data->>'peng_visible' AS peng_visible,
        row_data->>'placement' AS placement,
        row_data->>'terminal_mc' AS terminal_mc
    FROM public.tracking_history
    WHERE audit_id = 35
)
-- Inserting audit_id selected in the 'cables_test' table
INSERT INTO public.cables (
    id, 
    geom, 
    status, 
    design_state, 
    category, 
    armor_type, 
    cable_type, 
    tether_type, 
    environment_type, 
    duct_size, 
    fiber_capacity, 
    transport_demand, 
    feeder_demand, 
    distribution_demand, 
    spare, 
    total_distribution_demand, 
    total_demand, 
    calc_length, 
    premise_length, 
    start_structure_id, 
    end_structure_id, 
    loopback, 
    wiring_limits, 
    construction_complete, 
    cable_id, 
    peng_visible, 
    placement, 
    terminal_mc
)
SELECT 
    id,
    geom,
    status,
    design_state,
    category,
    armor_type,
    cable_type,
    tether_type,
    environment_type,
    duct_size,
    fiber_capacity,
    transport_demand,
    feeder_demand,
    distribution_demand,
    spare,
    total_distribution_demand,
    total_demand,
    calc_length,
    premise_length,
    start_structure_id,
    end_structure_id,
    loopback,
    wiring_limits,
    construction_complete,
    cable_id,
    peng_visible,
    placement,
    terminal_mc
FROM selected_record
ON CONFLICT (id) DO UPDATE
SET 
    geom = EXCLUDED.geom,
    status = EXCLUDED.status,
    design_state = EXCLUDED.design_state,
    category = EXCLUDED.category,
    armor_type = EXCLUDED.armor_type,
    cable_type = EXCLUDED.cable_type,
    tether_type = EXCLUDED.tether_type,
    environment_type = EXCLUDED.environment_type,
    duct_size = EXCLUDED.duct_size,
    fiber_capacity = EXCLUDED.fiber_capacity,
    transport_demand = EXCLUDED.transport_demand,
    feeder_demand = EXCLUDED.feeder_demand,
    distribution_demand = EXCLUDED.distribution_demand,
    spare = EXCLUDED.spare,
    total_distribution_demand = EXCLUDED.total_distribution_demand,
    total_demand = EXCLUDED.total_demand,
    calc_length = EXCLUDED.calc_length,
    premise_length = EXCLUDED.premise_length,
    start_structure_id = EXCLUDED.start_structure_id,
    end_structure_id = EXCLUDED.end_structure_id,
    loopback = EXCLUDED.loopback,
    wiring_limits = EXCLUDED.wiring_limits,
    construction_complete = EXCLUDED.construction_complete,
    cable_id = EXCLUDED.cable_id,
    peng_visible = EXCLUDED.peng_visible,
    placement = EXCLUDED.placement,
    terminal_mc = EXCLUDED.terminal_mc;
```
<a class="" data-lightbox="logging_database" href="_static/Logging_database/logging_database.gif" title="logging_database" data-title="Bracebridge Tracker"><img src="_static/Logging_database/logging_database.gif" class="align-center" width="800px" height="500px" alt="logging_database">
</a>

