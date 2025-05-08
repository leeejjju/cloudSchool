use autoever
select database();

CREATE TABLE TCAR
(
car VARCHAR(30) NOT NULL, -- 이름
capacity INT NOT NULL, -- 배기량
price INT NOT NULL, -- 가격
maker VARCHAR(30) NOT NULL -- 제조사
);
INSERT INTO TCAR (car, capacity, price, maker) VALUES ('소나타', 2000, 2500, '현대');
INSERT INTO TCAR (car, capacity, price, maker) VALUES ('티볼리', 1600, 2300, '쌍용');
INSERT INTO TCAR (car, capacity, price, maker) VALUES ('A8', 3000, 4800, 'Audi');
INSERT INTO TCAR (car, capacity, price, maker) VALUES ('SM5', 2000, 2600, '삼성');


CREATE TABLE TMAKER
(
maker VARCHAR(30) NOT NULL, -- 회사
factory CHAR(10) NOT NULL, -- 공장
domestic CHAR(1) NOT NULL -- 국산 여부. Y/N
);
INSERT INTO TMAKER (maker, factory, domestic) VALUES ('현대', '부산', 'y');
INSERT INTO TMAKER (maker, factory, domestic) VALUES ('쌍용', '청주', 'y');
INSERT INTO TMAKER (maker, factory, domestic) VALUES ('Audi', '독일', 'n');
INSERT INTO TMAKER (maker, factory, domestic) VALUES ('기아', '서울', 'y');

show tables







