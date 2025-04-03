# Write your MySQL query statement below
with cte1 as (
    select player_id, min(event_date) as "first_login"
    from activity
    group by player_id
),
cte2 as(
    select *
    from activity
    where (player_id,date_sub(event_date, interval 1 day)) in (select * from cte1)
)
select round((select count(*) from cte2)/(select count(*) from cte1),2) as fraction;
