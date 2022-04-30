-- We recover the top 10 parts more used during reparations
SELECT 
  model_id,
  ARRAY_AGG( reference_id ORDER BY model_id, total_ref DESC LIMIT 10) data

FROM (
    SELECT model_id, reference_id, count(reference_id) as total_ref
  FROM `{REDACTED}.hackupc2022.sales`
  GROUP BY model_id, reference_id
  ORDER BY model_id, total_ref desc
)

GROUP BY model_id
ORDER BY model_id