show databases;
use autoever;
show tables;

-- select문 연습 

select * from tStaff;
select name from tStaff;

select *  
from tCity;


-- alias문으로 결과 컬럼에 별명 붙이기 
select area as "면적(제곱km)", name as "도시명", popu as "인구(만명)"
from tCity
where popu > 50 -- 조건절 
order by 도시명; -- 실행순서상 얘는 별명 사용가능 

select name "이름", popu*10000 as "인구"
from tcity

select name "이름", popu*10000 "인구(명)", area "면적(제곱km)", popu*10000/area "인구밀도(명/제곱km)"
from tCity

select 60 * 60 * 40; -- 이게되네

select concat(ename, " : ", job) as "employee"
from EMP;

select count(distinct region) 
from tcity

select count(*)
from tcity

select region, name, area, popu
from tcity
order by region asc, name desc -- 오름차순asc, 내림차순desc 

select * from tcity order by 2; -- 두번째 속성인 area 기준이 되엇스빈다... 


select name from tcity t where popu < 10;
select * from tcity where region = '전라';
select name from tStaff where salary >= 400;
select * from tCity where metro = 'Y'; -- MariaDB는 조건절의 대소문자를 구분하지 않음...

select * from tStaff where score = null; -- 이러시믄 아무것도 안 되세여 
select * from tStaff where score is null; -- 일케 해주셔야 댐... 

select * from tStaff order by salary;


select *
from tcity t 
where popu >= 100 and popu <= 1000;

select *
from tcity
where popu between 100 and 1000; -- 1000 100 순서로 쓰면 작동 안됨 / 위의 and구문보다 더 빠르다 

select *
from tcity t
where name like '%천%' or name like '_산';

select *
from tcity t 
where name not like '_산';

select * 
from tcity t 
where region = '강원' or region = '경기'

select *
from tcity t 
where region in ('강원', '경기') -- in 구문: 서브쿼리 등에서 주로 쓰게 됨. 

select *
from tcity
order by popu desc 
limit 5; -- top 5

select *
from tcity
order by popu desc 
limit 5, 5; -- top 6~10

select *
from tcity
order by popu desc
offset 0 rows fetch next 5 rows only; -- offset fetch 버전 (오라클에서도 통함)

select *
from tcity
order by popu desc
offset 5 rows fetch next 5 rows only; -- offset fetch 버전 (오라클에서도 통함)

-- 연습문제

select * 
from emp
where comm is not null;

select ename, sal, comm
from emp
where comm >= sal*1.1;

select *
from emp
where job in ('CLERK', 'ANALYST') and sal not in (1000, 3000, 5000)

select ename, sal
from emp
where ename like '%a%e%' or ename like '%e%a%'

select *
from emp
where (ename like '%l%l%' and deptno = 30) or (mgr = 7782) 





