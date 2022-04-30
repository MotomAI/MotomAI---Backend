SELECT model_id, CAST(round(49*RAND()) AS integer) cont_part
FROM
UNNEST(GENERATE_ARRAY(0, 99)) model_id
