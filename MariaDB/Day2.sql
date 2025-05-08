use autoever;


select sal, round(sal, -2) as 반올림
from emp; -- 5단위에 대해 반올림을 못하는 경우가 발생!!!! (96년도 정처기 킬러문제의 전설...)

select sal, FLOOR(sal/100+0.5)*100 as 반올림 
from emp; -- 대체재: 0.5를 더하고 소수를 버리는 수제 반올림 

select * 
from emp 
where mod(empno, 2) = 1;

select bit_length(ename), char_length(ename), length(ename)
from emp;

select lower(ename) from emp;

select left(ename, 2) from emp;

select ename, hiredate 
from emp
where substring(hiredate, 6, 2) = '02';

select ename, hiredate
from emp
where hiredate like "_____02%"; --헐 작은따옴표는 안되는구나... 

select ename, hiredate
from emp
where month(hiredate) = 02;

-- 날짜에 interval의 기간으로 산술연산 가능 
select current_date() as today, curdate()+interval 1 day as tomorrow

-- 날짜간의 뺼셈 (이거 왜안되지....)
select datediff(curdate(), str_to_date('1987-05-05', '%y-%m-%d'));

select binary(15) -- 실망스럽내요 

-- null에 대한 치환 (주로 연산에서 많이 씀! )
select name, grade, ifnull(score, 0)
from tstaff;


select job, sum(sal) 
from emp
group by job
having sum(sal) > 5000 -- 그룹화 이후의 조건 필터 

select deptno, count(*), round(avg(sal), 0)
from emp
group by deptno
having count(*) > 3;

select count(*), max(sal), min(sal), sum(sal)
from emp;

select max(sal), min(sal), sum(sal)
from emp
group by job ;

select count(*)
from emp 
group by job;

select max(sal)-min(sal)
from emp;

select addr, 
row_number() over(order by birthyear asc, name asc) as "idx", 
name, birthyear
from usertbl;

select addr, 
row_number() over(partition by addr order by birthyear asc, name asc) as "idx", 
name, birthyear
from usertbl;

select addr, 
ntile(3) over(order by birthyear asc) as "idx", 
name, birthyear
from usertbl;


select name, addr, birthyear, 
birthyear - (LEAD(birthyear, 1) over (order by birthyear desc)) as "뒷사람과 나이차이"
from usertbl;

select name, addr, birthyear, 
birthyear - (LEAD(birthyear, 1) over (partition by addr order by birthyear desc)) as "뒷사람과 나이차이"
from usertbl;

select name, addr, birthyear,
cume_dist() over (order by birthyear desc) *100
from usertbl;


select deptno
from dept
union -- 중복 비허용 
select deptno
from emp

select deptno
from dept
union all -- 중복허용 
select deptno
from emp

select deptno
from dept
intersect -- 교집합
select deptno
from emp

select deptno
from dept
except -- 차집합
select deptno
from emp


select dname 
from dept
where deptno = (select deptno from emp where ename = 'MILLER')

-- 최대 인구수 도시 
select name, popu
from tcity t 
order by popu desc 
limit 1;

select name 
from tcity 
where popu = (select max(popu) from tcity) 


select ename, sal
from emp
where sal > (select avg(sal) from emp);

-- emp테이블에서, dept테이블의 loc가 dallas인 사람의 이름과 deptno 출력 (foreign key는 deptno)
select ename, deptno 
from emp 
where deptno = (select deptno from dept where upper(loc) = 'DALLAS')

-- tstaff 테이블에서 depart와 gender가 안중근과 동일한 데이터를 출력  
select *
from tstaff 
where depart = (select depart from tstaff where name = '안중근') 
	and gender = (select gender from tstaff where name = '안중근')

-- 우왕 이건 다중열 서브쿼리래.(단일행 소속) 파이썬 깔이네요. 
select * 
from tstaff
where (depart, gender) = (select depart, gender from tstaff where name = '안중근')

-- 다중행 서브쿼리 
select empno, ename, sal, deptno 
from emp 
where sal in (select max(sal) from emp group by deptno)

-- deptno가 30인 데이터의 모든 sal보다 큰 sal을 가진 데이터의 ename과 sal을 조회 
select ename, sal 
from emp 
where sal > (select max(sal) from emp where deptno = 30)

select ename, sal 
from emp 
where sal > all(select sal from emp where deptno = 30)

select ename, sal, job 
from emp 
where sal > (select min(sal) from emp where upper(job) = 'SALESMAN') and upper(job) <> 'SALESMAN'

-- 연습문제 
-- 1
select ename, hiredate 
from emp 
where deptno in (select deptno from emp where ename = 'BLAKE') -- and ename != 'BLAKE';

-- 2
select empno, ename
from emp 
where sal > (select avg(sal) from emp)
order by sal desc ;

-- 3
select empno, ename, sal 
from emp 
where deptno in (select deptno from emp where ename like "%T%")
order by empno;

-- 4
select ename, job, sal 
from emp 
where deptno = (select deptno from dept where loc = 'DALLAS');

-- 5 
select ename, sal 
from emp 
where mgr = (select empno from emp where ename = 'KING');

-- 6
select * 
from emp 
where sal > (select min(sal) from emp where deptno = 30);



-- join
select * from emp;
select * from dept; -- deptno


select * 
from emp, dept;






