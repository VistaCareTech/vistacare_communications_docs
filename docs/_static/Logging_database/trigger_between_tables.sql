SELECT sq.sum_length FROM  (
   select p.id, sum(length) as sum_length
		from testing.spans sp,
			 testing.peng_scope p
		WHERE 'UNINON102-DP01-AR13-HO' like p.permit_number
		OR '' like p.permit_number
		AND sp.case = 'New Strand'
		AND sp.permit_number = p.permit_number 
		GROUP BY p.id
		order by p.id
   ) AS sq
   
select p.id, sp.id as sum_length
		from spans sp,
			 peng_scope p
		WHERE 'UNINON102-DP01-AR13-HO' = p.permit_number
		AND sp.case = 'New Strand'
		AND sp.permit_number = p.permit_number 

SELECT * FROM testing.spans s 
	WHERE s.id = 2958
	
SELECT newstrand_distance FROM testing.peng_scope p 
	WHERE p.permit_number = 'UNINON102-DP01-AR13-HO'

CREATE OR REPLACE FUNCTION testing.insert_and_update_pengscope()
RETURNS trigger AS
$function$ 
BEGIN
	RAISE NOTICE 'NEW Value: %', NEW.permit_number;
	RAISE NOTICE 'OLD Value: %', OLD.permit_number;
UPDATE testing.peng_scope p 
SET newstrand_distance = sq.sum_length
FROM  (
   select p.id, sum(length) as sum_length
		from testing.spans sp,
			 testing.peng_scope p
		WHERE
			CASE WHEN OLD.permit_number <> '' THEN 
			    OLD.permit_number = p.permit_number
			ELSE
			    NEW.permit_number = p.permit_number
			END
		        
			AND sp.case = 'New Strand'
			AND sp.permit_number = p.permit_number 
			GROUP BY p.id
			ORDER BY p.id
   ) AS sq
WHERE  p.id = sq.id;

RETURN NEW;
END;
$function$
LANGUAGE plpgsql VOLATILE -- Says the function is implemented in the plpgsql language; VOLATILE says the function has side effects.
COST 100;


CREATE TRIGGER trigger_update_pengscope
AFTER UPDATE
ON testing.spans
FOR EACH ROW
EXECUTE PROCEDURE 
testing.insert_and_update_pengscope();


drop trigger trigger_update_pengscope on testing.spans;