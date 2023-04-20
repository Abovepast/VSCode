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
    ('S1','ԭ�Ϲ�˾','�Ͼ�����23��'),
    ('S2','���Ǹֹܳ�','�Ϻ��ֶ�100��'),
    ('S3','������칫˾','�Ͼ�����·55��'),
    ('S4','�����˾','��������58��'),
    ('S5','ԭ�ϳ�','��������·88��'),
    ('S8','���������','���Ҷ��·100��');

INSERT INTO P (PNO, PNAME, COLOR, WEIGHT) VALUES
    ('P1','�ֽ�','��', 25),
    ('P2','�ֹ�','��', 26),
    ('P3','��ĸ','��', 11),
    ('P4','��˿','��', 12),
    ('P5','����','��', 18);

INSERT INTO J (JNO, JNAME, JCITY, BALANCE) VALUES
    ('J1','��������','�Ϻ�', 0.00),
    ('J2','���ͳ�','����', -11.20),
    ('J3','��������','����', 678.00),
    ('J4','������','�Ϻ�', 456.00),
    ('J5','���ֹ���','���', 123.00),
    ('J6','���ִ���','�Ϻ�', 234.70),
    ('J7','����ˮ�೧','����', 343.00);

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



