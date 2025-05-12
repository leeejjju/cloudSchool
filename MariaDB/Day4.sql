use autoever;
show tables;

-- 제약조건 
select * from information_schema.TABLE_CONSTRAINTS tc; 

-- default 
drop table tcitydefault;
create table tCityDefault(
name char(10), 
area int ,
popu int ,
metro char(1) default 'n' not null,
region char(6) not null,
constraint pk_tcity primary key(name)
);
desc tCityDefault;

insert into tcitydefault values('k', 1, 1, default, 'seoul');
insert into tcitydefault (name, area, popu, region) values('l', 1, 1, 'seoul');
select * from tcitydefault;

-- auto_increment 
create table tSale(
saleno int auto_increment primary key,
customer varchar(10));
desc tSale;

insert into tsale (customer) values ('JJLee');
insert into tsale values(2, 'HMPark');
insert into tsale (customer) values ('DBCho');
select * from tsale;

insert into tsale values (10, 'NONAME'); -- 일케 건너뛰어버리면 사이 일련번호는 못 쓰게 되는거... 
insert into tsale (customer) values ('YELee');
select * from tsale; -- 쩜프한놈을 지우더라도 일련번호는 되돌아가지 않음. 걍 직접입력 자체가 넘 위험한거... 

alter table tsale auto_increment=100; -- 시작값을 재설정 
insert into tsale (customer) values ('GRKim');
select * from tsale;

-- insert 
desc tcity;
truncate table tcity; -- 데이터 비우기 

insert into tcity(name, area, popu, metro, region)
values ('진주', 50, 100, 'n', '경기');
insert into tcity 
values ('한민', 23, 1014, 'n', '경북');
select * from tcity;

update tcity set popu=207 where name='진주';
update tcity set area=24 where name='진주';
update tcity set popu=1007 where name='한민';
update tcity set metro='y' where name='진주';
select * from tcity;

-- 여러개 한번에 삽입도 가능: 보통 샘플 만들 때 사용함  
insert into tcity 
values 
('예은', 24, 303, 'n', '경북'),
('다빈', 25, 706, 'n', '경북'),
('가륜', 26, 728, 'n', '경북');
select * from tcity;

-- 원본 데이터 복원... 
INSERT INTO tCity (name, area, popu, metro, region) VALUES
('서울',605,974,'y','경기'),
('부산',765,342,'y','경상'),
('오산',42,21,'n','경기'),
('청주',940,83,'n','충청'),
('전주',205,65,'n','전라'),
('순천',910,27,'n','전라'),
('춘천',1116,27,'n','강원'),
('홍천',1819,7,'n','강원');



insert into tstaff(name, depart, gender, joindate, grade, salary, score)
select name, region, metro, '20110629', '신입', area, popu 
from tcity 
where region='경기';

select * from tstaff -- where depart='경기';

-- select문으로 테이블 만들기 -> 구조만 카피하고싶으면 조건절을 false로... 
create table deptcopy as 
select * from dept
where 0;

select * from dept;
select * from deptcopy;


-- 테이블을 생성 
create table memberTBL 
(select userID, name, addr from usertbl limit 3);
select * from memberTBL;

-- 제약조건을 추가 
alter table memberTBL add constraint pk_memberTBL primary key(userID);

insert into memberTBL values('asdf', 'asdf', 'asdf');
insert into memberTBL values('zxcv', 'zxcv', 'zxcv');
insert into memberTBL values('qwer', 'qwer', 'qwer');
select * from memberTBL;

-- ignore: 여러 구분 실행시 오류가 있어도 금마만 무시하고 나머지는 정상 실행되게 해줌. 
insert ignore into memberTBL values('asdf', 'asdf', 'asdf'); -- err 
insert ignore into memberTBL values('wert', 'wert', 'wert');
select * from memberTBL;

-- delete 
delete from tcity 
where name='부산';
select * from tcity;
INSERT INTO tCity VALUES ('부산',765,342,'y','경상');

-- update 
update tcity set popu=1000, region='충청' where name='서울';
select * from tcity;
-- 서브쿼리 이용 update 

update dept 
loc=(select loc from dept where deptno=40) 
where deptno=20;

delete 
from emp 
where deptno = (select deptno from dept where dname='SALES');

select * from emp;
select * from dept;

show databases;
use autoever;
show tables;

--  트랜잭션을 알아보아요! (상단에 auto로 되어있는거 잠시 수동으로 바꿔줍시당 )
-- 데이터 삭제 
delete from emp where ename = 'SCOTT';
select * from emp;

-- 롤백 
rollback;
select * from emp;

-- 데이터 추가
insert into dept values(50, '총무', '서울');
select * from dept;

-- 작업완료 
commit; 

-- 작업을 취소해도 커밋한 부분까지는 굳혀집니다. -> 변경 내역이 반영됩니다. 
rollback;
select * from dept;


insert into dept values (60, '영업', '철원');
drop table tstaff; -- 임마는 DDL이라 성공시 auto commit된다...!!! 
rollback;
select * from dept; -- 그래서 넣고 커밋 안한 영업 데이터가 살아잇슴!!!  


-- savePoint를 알아보아요...

insert into dept values(70, '비서', '파주');
select * from dept;

-- 중간저장점 생성 
savepoint s1;
-- 추가 작업 
insert into dept values(80, '회계', '포천');
select * from dept;
-- 롤백하면 어디로 갈까?? 
-- >> savepoint 없엇다면 마지막 커밋 혹은 DDL 위치로 가고, 있으면 글로 가고... 
-- 그래서 중간중간 일정 시간마다 savepoint를 만들기도 함. 
rollback to s1;
select * from dept;



