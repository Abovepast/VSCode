CREATE DATABASE SPJ_Data;
Use SPJ_Data;

CREATE TABLE S
(
    SNO   char(2) primary key,
    SNAME nchar(10),
    SADDR nchar(10)
);
CREATE TABLE P
(
    PNO    char(2) primary key,
    PNAME  nchar(5),
    COLOR  nchar(3),
    WEIGHT int
);
CREATE TABLE J
(
    JNO     char(2) primary key,
    JNAME   nchar(10),
    JCITY   nchar(5),
    BALANCE decimal(5,2)
);
CREATE TABLE SPJ(
                    SNO Char(2),
                    PNO Char(2),
                    JNO Char(2),
                    PRICE Decimal(4,2),
                    QTY int,
                    primary key (SNO,PNO,JNO),
                    constraint SPJ_SNO foreign key(SNO) references S(SNO),
                    constraint SPJ_PNO foreign key(PNO) references P(PNO),
                    constraint SPJ_JNO foreign key(JNO) references J(JNO)
);

INSERT INTO S (SNO, SNAME, SADDR) VALUES
    ('S1','原料公司','南京北门23号'),
    ('S2','红星钢管厂','上海浦东100号'),
    ('S3','零件制造公司','南京东晋路55号'),
    ('S4','配件公司','江西上饶58号'),
    ('S5','原料厂','北京红星路88号'),
    ('S8','东方配件厂','天津叶西路100号');

INSERT INTO P (PNO, PNAME, COLOR, WEIGHT) VALUES
    ('P1','钢筋','黑', 25),
    ('P2','钢管','白', 26),
    ('P3','螺母','红', 11),
    ('P4','螺丝','黄', 12),
    ('P5','齿轮','红', 18);

INSERT INTO J (JNO, JNAME, JCITY, BALANCE) VALUES
    ('J1','东方明珠','上海', 0.00),
    ('J2','炼油厂','长春', -11.20),
    ('J3','地铁三号','北京', 678.00),
    ('J4','明珠线','上海', 456.00),
    ('J5','炼钢工地','天津', 123.00),
    ('J6','南浦大桥','上海', 234.70),
    ('J7','红星水泥厂','江西', 343.00);

INSERT INTO SPJ (SNO, PNO, JNO, PRICE, QTY) VALUES
    ('S1','P1','J1', 22.60, 80),
    ('S1','P1','J4', 22.60, 60),
    ('S1','P3','J1', 22.80, 100),
    ('S1','P3','J4', 22.80, 60),
    ('S3','P3','J5', 22.10, 100),
    ('S3','P4','J1', 11.90, 30),
    ('S3','P4','J4', 11.90, 60),
    ('S4','P2','J4', 33.80, 60),
    ('S5','P5','J1', 22.80, 20),
    ('S5','P5','J4', 22.80, 60),
    ('S8','P3','J1', 13.00, 20),
    ('S1','P3','J6', 22.80, 6),
    ('S3','P4','J6', 11.90, 6),
    ('S4','P2','J6', 33.80, 8),
    ('S5','P5','J6', 22.80, 8);



