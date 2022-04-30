SELECT model_id , random_date ,  count(model_id) as times_sell 
FROM `____.hackupc2022.sales`
group by model_id, random_date
order by random_date