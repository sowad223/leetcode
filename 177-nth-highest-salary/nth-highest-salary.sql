CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT

BEGIN
    declare offset_val int;
    set offset_val=N-1;
    RETURN (
        
      # Write your MySQL query statement below.
        select distinct salary 
        from employee 
        order by salary desc 
        limit 1 offset offset_val
  );
END
