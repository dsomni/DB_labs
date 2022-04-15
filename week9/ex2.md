# Function

CREATE OR REPLACE FUNCTION public.customer_pager(s numeric, f numeric)
RETURNS TABLE(
customer_id integer,
store_id smallint,
first_name character varying(45),
last_name character varying(45),
email character varying(50),
address_id smallint,
activebool boolean,
create_date date,
last_update timestamp without time zone,
active integer
) AS
$BODY$
BEGIN
IF (s<0 OR f<0 OR s> 600 OR f>600) THEN
RAISE 'Invalid start or/and finish parameters range!';
ELSEIF (s>f) THEN
RAISE 'Invalid paramters: start can not be greater than fisnish!';
ELSE
RETURN QUERY SELECT \*
FROM
customer
ORDER BY
address_id
OFFSET s ROWS
FETCH FIRST (f-s) ROW ONLY;
END IF;
END;
$BODY$
LANGUAGE plpgsql;

### P.S.

I assume start index as 0.
Examples of query you can find in files ex2.example[id].jpg
