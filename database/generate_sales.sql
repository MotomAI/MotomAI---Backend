-- Generate between 0 and 1000 sales for model during last two years
WITH parameters AS (
    SELECT CAST(round(1000*RAND()) AS integer) ids_count, DATE '2020-01-01' start_date, DATE '2022-04-30' finish_date
  )
  SELECT  DATE_FROM_UNIX_DATE(CAST(start + (finish - start) * RAND() AS INT64)) random_date, model_id

  FROM parameters, 
  UNNEST(GENERATE_ARRAY(1, 39586)) model_id,
  UNNEST(GENERATE_ARRAY(1, CAST(round(1000*RAND()) AS integer))) id,

  UNNEST([STRUCT(UNIX_DATE(start_date) AS start, UNIX_DATE(finish_date) AS finish)])

  order by model_id