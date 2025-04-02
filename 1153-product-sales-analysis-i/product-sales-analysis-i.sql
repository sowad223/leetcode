# Write your MySQL query statement below
Select Product_name, year, price
from Product as A
Right Join 
Sales as B
On A.product_id = B.product_id;