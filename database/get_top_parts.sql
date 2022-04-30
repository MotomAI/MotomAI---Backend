#standardSQL
SELECT 
  model_id,
  v.name,
  brand_id,
  b.name
  year,
  ARRAY_AGG( struct(reference_id) ORDER BY model_id DESC LIMIT 10) references_used,

FROM (
    SELECT model_id, reference_id, count(reference_id) as total_ref_used
  FROM `bot-testing-345117.hackupc2022.sales`
  GROUP BY model_id, reference_id
  ORDER BY model_id, total_ref_used desc
) s INNER JOIN
`bot-testing-345117.hackupc2022.versions` v on s.model_id = v.id inner join `bot-testing-345117.hackupc2022.brands` b on b.id = v.brand_id
GROUP BY model_id, brand_id, year, name
ORDER BY model_id