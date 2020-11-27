-- create database safety_index;
-- use safety_index;

-- drop table crime_info;
-- drop table offense_code;

CREATE TABLE OFFENSE_CODE(
CODE int primary key,
NAME varchar(64) not null,
DANGER char(1) not null);

-- DELETE FROM OFFENSE_CODE WHERE DANGER = "" limit 100;

-- CREATE TABLE CRIME_INFO(
-- CRIME_NUMBER int primary key,
-- OFFENSE_CODE char(4),
-- MONTH char(2),
-- DAY_OF_WEEK char(10),
-- DISTRICT char(3) not null,
-- HOUR char(2),
-- LATTITUDE char(12) not null,
-- LONGTITUDE char(12) not null,
-- SHOOTING char(1),
-- CHECK (LATITUDE>0),
-- CHECK (LONGTITUDE>0),
-- FOREIGN KEY (OFFENSE_CODE) REFERENCES OFFENSE_CODE(CODE));

DELETE FROM OFFENSE_CODE limit 10000;
DELETE FROM CRIME_INFO limit 1000000;


-- CREATE TABLE CRIME_INFO(
-- CRIME_NUMBER char(6) primary key,
-- OFFENSE_CODE char(4),
-- MONTH char(2),
-- DAY_OF_WEEK char(10),
-- DISTRICT char(3),
-- HOUR char(2),
-- LATTITUDE char(12),
-- LONGTITUDE char(12),
-- SHOOTING char(1));

-- -- -- SET NAMES "utf8" 
-- -- -- select * from FULLDATA into outfile'/tmp/FULLDATA.csv' fields terminated by ',' optionally enclosed by '"' lines terminated by '\n';

-- -- DROP TRIGGER DAY_OF_WEEK;
-- -- DROP TRIGGER DISTRICT;
-- -- DROP TRIGGER SHOOTING;

-- -- -- urn DAY_OF_WEEK into [1,7]

-- DELIMITER ||
-- create trigger DAY_OF_WEEK
-- before insert on CRIME_INFO
-- for each row
-- begin
-- declare msg varchar(30);
-- 	if new.day_of_week = "Monday" 
--     then set new.day_of_week = "1";
-- 	elseif new.day_of_week = "Tuesday" 
--     then set new.day_of_week = "2";
-- 	elseif new.day_of_week = "Wednesday" 
--     then set new.day_of_week = "3";
-- 	elseif new.day_of_week = "Thursday" 
--     then set new.day_of_week = "4";
-- 	elseif new.day_of_week = "Friday" 
--     then set new.day_of_week = "5";
-- 	elseif new.day_of_week = "Saturday" 
--     then set new.day_of_week = "6";
-- 	elseif new.day_of_week = "Sunday" 
--     then set new.day_of_week = "7";
-- 	else set msg= concat("wrong day_of_week:", new.day_of_week);
-- 	signal sqlstate 'HY100' set message_text = msg;
--     end if;
-- end;
-- ||

-- -- Turn DISTRICT [A1,A15,A7,B2,B3,C11,C6,D14,D4,E13,E18,E5] into [1,12]


-- DELIMITER ||
-- create trigger DISTRICT
-- before insert on CRIME_INFO
-- for each row
-- begin
-- declare msg varchar(30);
-- 	if new.district = "A1" 
--     then set new.district = "1";
-- 	elseif new.district = "A7" 
--     then set new.district = "2";
-- 	elseif new.district = "A15" 
--     then set new.district = "3";
-- 	elseif new.district = "B2" 
--     then set new.district = "4";
-- 	elseif new.district = "B3" 
--     then set new.district = "5";
-- 	elseif new.district = "C6" 
--     then set new.district = "6";
-- 	elseif new.district = "C11" 
--     then set new.district = "7";
-- 	elseif new.district = "D4" 
--     then set new.district = "8";
-- 	elseif new.district = "D14" 
--     then set new.district = "9";
-- 	elseif new.district = "E5" 
--     then set new.district = "10";
-- 	elseif new.district = "E13" 
--     then set new.district = "11";
-- 	elseif new.district = "E18" 
--     then set new.district = "12";
-- 	else set msg= concat("wrong district:", new.district);
-- 	signal sqlstate 'HY100' set message_text = msg;
--     end if;
-- end;
-- ||

-- Turn SHOOTING 's "T" into "3"

-- DELIMITER ||
-- create trigger SHOOTING
-- before insert on CRIME_INFO
-- for each row
-- begin
-- 	if new.SHOOTING = "T" 
--     then set new.SHOOTING = "3";
--     else set new.SHOOTING = "0";
--     end if;
-- end;
-- ||

-- DELETE FROM CRIME_INFO LIMIT 200000;
-- SELECT COUNT(CRIME_NUMBER) FROM CRIME_INFO;

-- -- SELECT * FROM OFFENSE_CODE;
-- -- DELETE FROM OFFENSE_CODE limit 10;

-- -- INSERT INTO OFFENSE_CODE 
-- -- VALUES ("404", "A&B HANDS, FEET, ETC.  - MED. ATTENTION REQ.", "1");
-- -- INSERT INTO OFFENSE_CODE 
-- -- VALUES ("424", "A&B HANDS, FEET, ETC. - PO MED. ATTENTION REQ.", "1");
-- -- INSERT INTO OFFENSE_CODE 
-- -- VALUES ("803", "A&B ON POLICE OFFICER", "2");
-- -- INSERT INTO OFFENSE_CODE 
-- -- VALUES ("724", "AUTO THEFT", "3");
-- -- INSERT INTO OFFENSE_CODE 
-- -- VALUES ("3803", "M/V ACCIDENT - PERSONAL INJURY","2");
-- -- INSERT INTO OFFENSE_CODE 
-- -- VALUES (NULL, "M/V ACCIDENT - PERSONAL INJURY", "2");



-- -- DELETE FROM CRIME_INFO LIMIT 10;

-- -- SELECT * FROM CRIME_INFO;
-- -- DELETE FROM CRIME_INFO limit 10;

-- -- INSERT INTO CRIME_INFO 
-- -- VALUES ("318744","404","10","Saturday","E13","8","42.31720702","-71.09879922", "T");
-- -- INSERT INTO CRIME_INFO 
-- -- VALUES ("273185","3803","12","Thursday","A1","17","42.27531312","-71.11587798",null);
-- -- INSERT INTO CRIME_INFO 
-- -- VALUES ("265100","724","1","Monday","C6","15","42.31354088","-71.07220579",null);
-- -- INSERT INTO CRIME_INFO 
-- -- VALUES ("318766","404","10","Saturday","E13","8","42.31720702","-71.09879922", NULL);

DROP VIEW FULLDATA;

-- CREATE VIEW FULLDATA AS 
-- SELECT * FROM CRIME_INFO C INNER JOIN OFFENSE_CODE O
-- ON C.OFFENSE_CODE = O.CODE;

-- SELECT CRIME_NUMBER, OFFENSE_CODE, NAME, MONTH, DAY_OF_WEEK, HOUR, DISTRICT, LATITUDE, LONGTITUDE, SHOOTING, DANGER 
-- FROM FULLDATA;
-- SELECT COUNT(OFFENSE_CODE) FROM FULLDATA;

-- -- DO NOT USE SQL BELOW
-- -- UPDATE FULLDATA
-- -- SET DANGER = '3'
-- -- WHERE SHOOTING = "T";