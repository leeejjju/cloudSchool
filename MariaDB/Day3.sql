
select database();
use autoever;
show tables;

-- EQUI JOIN -> 지정 컬럼에서 겹치는 애들 기준으로 합침 
select * 
from emp, dept
where emp.deptno = dept.deptno -- and ename='MILLER';

-- 1
select e.ename, e.sal 
from emp e, dept d 
where e.deptno = d.deptno and d.loc = 'NEW YORK';
-- sub query로도 해결 가능 (권장됨!! 효율성!!)
select ename, sal 
from emp 
where deptno in (select deptno from dept where loc = 'NEW YORK');

-- 2
select e.ename, e.hiredate 
from emp e, dept d 
where e.deptno = d.deptno and d.dname = 'ACCOUNTING';

-- NON EQUI JOIN 
select ename, sal, grade 
from emp e, salgrade s 
where e.sal between s.losal and s.hisal -- 여기가 = 이외 연산자인게 포인뜨 
order by sal;

-- SELF JOIN -> 사원이름과 그의 매니저 이름을 함께 출력 
select e.ename name, m.ename manager 
from emp e, emp m 
where m.empno = e.mgr
order by manager

select e.ename, e.job, k.ename manager
from emp e, emp k 
where e.mgr = k.empno and k.ename = 'KING'

-- same as CROSS JOIN
select * 
from emp cross join dept

-- same as EQUI JOIN 
select e.ename, d.dname 
from emp e inner join dept d on e.deptno = d.deptno 
where 1 -- 분리된 일반 조건이 포인트 

select e.ename, d.dname 
from emp e inner join dept d using(deptno) -- 컬럼명 같으면 using으로 나타내기 가능 


-- outer join
select * 
from dept left outer join emp 
on dept.deptno = emp.deptno
union 
select * 
from dept right outer join emp 
on dept.deptno = emp.deptno

-- 연습문제 join

-- 1
select e.ename, e.deptno, d.dname 
from emp e, dept d 
where e.deptno = d.deptno

-- 2
select e.ename, e.job, e.sal, d.dname
from emp e, dept d 
where e.deptno = d.deptno and d.loc = 'NEW YORK'

select ename, job, sal, dname 
from emp inner join dept 
using (deptno)
where loc = 'NEW YORK'

-- 3 
select e.ename, d.dname, d.loc 
from emp e, dept d 
where e.deptno = d.deptno and e.comm is not null 

select e.ename, d.dname, d.loc
from emp e inner join dept d 
using (deptno)
where e.comm is not null 

-- 4
select e.ename, e.job, d.dname, d.loc 
from emp e, dept d 
where e.ename like "%L%"

-- 5 
select e.ename name, e.hiredate, m.ename manager_name, m.hiredate 
from emp e, emp m 
where e.mgr = m.empno and e.hiredate < m.hiredate


-- create table

-- 조회를 자주 할 예정, 일련번호 첫 값은 1, 한글을 사용할 예정 
create table contact(
	num integer auto_increment primary key, 
	name varchar(20), 
	address char(100), -- 자주 바뀔듯 -> no varchar
	tel varchar(20),
	email char(100), -- 자주 바뀔듯 -> no varchar
	birthday date
)engine=MyISAM auto_increment=1 charset=utf8;

alter table contact add age integer;
alter table contact drop age;
alter table contact modify tel integer;
alter table contact modify name varchar(20) not null; -- null 허용여부 변경은 컬럼 자료형 변경에 속함!! 
alter table contact change tel phone varchar(20);

desc contact;
drop table contact;

-- check, unique example 
create table sample(
	id integer auto_increase primary key,
	name varchar(20), 
	gender varchar(1) CHECK(gender = 'M' or gender = 'F'),
	age integer CHECK(age >= 1 and age <= 100),
	unique (name)
);

alter table sample modify id integer auto_increment;
desc sample;

insert into sample values (0, 'HMPark', 'M', 23);
insert into sample values (0, 'NONAME', 'N', 25); -- err
insert into sample values (0, 'JJLee', 'F', 24);  
insert into sample values (0, 'ALIAN', 'F', -10); -- err 
insert into sample values (0, 'HMPark', 'M', 32); -- err 
select * from sample;


-- foreign key example 
create table tEmployee( 
	name char(10) primary key,
	salary int not null,
	addr varchar(30) not null);

desc temployee;

insert into tEmployee values ('군계', 650, '제주도');
insert into tEmployee values ('쥬니', 480, '수원');
insert into tEmployee values ('헨리', 500, '서울');

select * from temployee;

create table tproject( 
	projectid int primary key,
	employee char(10),
	project varchar(30),
	cost int);

insert into tproject values (1, '쥬니', '요가', 300);
insert into tproject values (2, '헨리', '사이클', 200);

-- employee에 없는 이름도 삽입이 가능한 상황... 
insert into tproject values (3, '외부인', '요가', 300);
-- 헨리가 짤렸는데도 프로젝트 테이블에는 헨리 흔적이 남아있는 이슈도... 
delete from temployee where name = '헨리';
select * from tproject;
-- 위 이슈들을 해결하는 방안이 바로 외래키! 

-- 외래키 포함해서 다시 만들어봅쉬당... 
drop table temployee;
create table tEmployee( 
	name char(10) primary key,
	salary int not null,
	addr varchar(30) not null);

drop table tproject;
create table tproject( 
	projectid int primary key,
	employee char(10),
	project varchar(30),
	cost int,
	foreign key(employee) references tEmployee(name));

-- 다시 아까의 동작을 해봅시당 
insert into tEmployee values ('군계', 650, '제주도');
insert into tEmployee values ('쥬니', 480, '수원');
insert into tEmployee values ('헨리', 500, '서울');
insert into tproject values (1, '쥬니', '요가', 300);
insert into tproject values (2, '헨리', '사이클', 200);

-- employee에 없는 이름은 foreign key 제약조건에 위배되므로 불가. 
insert into tproject values (3, '외부인', '요가', 300);
-- 참조중인 데이터는 삭제하지 못하는 기능도 추가!  
delete from temployee where name = '헨리';

select * from temployee;
select * from tproject;