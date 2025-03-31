# Write your MySQL query statement below
select e.name , bn.bonus
from Employee e 
left join Bonus bn on e.empid = bn.empid
where bonus < '1000' or bonus is null
