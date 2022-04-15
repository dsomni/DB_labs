# Function

CREATE FUNCTION public.get_addresses_with_11_and_city_btw_400_600()
RETURNS TABLE(
address_id integer,
address character varying
)
LANGUAGE 'sql'
COST 100
IMMUTABLE PARALLEL UNSAFE
AS $BODY$
SELECT A.address_id, A.address
FROM address as A
WHERE A.address LIKE '%11%' AND A.city_id > 400 AND A.city_id < 600;
$BODY$;
