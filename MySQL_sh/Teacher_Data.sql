CREATE DATABASE TEACHER;
USE TEACHER;

CREATE TABLE T
(
    TNO  CHAR(4)    NOT NULL,
    TN   CHAR(10)   NOT NULL,
    SEX  CHAR(2)    NOT NULL CHECK (SEX IN ('男', '女')),
    AGE  INT    NOT NULL CHECK (AGE > 18),
    ZC   CHAR(10),
    DEPT VARCHAR(12),
    PRIMARY KEY (TNO)
);
CREATE TABLE C
(
    CNO CHAR(4) NOT NULL,
    CN  VARCHAR(10) NOT NULL,
    CX  CHAR(8),
    CT  INT NOT NULL CHECK (CT > 1),
    PRIMARY KEY (CNO)
);
CREATE TABLE TC
(
    TNO  CHAR(4) NOT NULL,
    CNO  CHAR(4) NOT NULL,
    YEAR INT    NOT NULL CHECK (YEAR > 1),
    PRIMARY KEY (TNO, CNO),
    CONSTRAINT TC_T FOREIGN KEY (TNO) REFERENCES T (TNO),
    CONSTRAINT TC_C FOREIGN KEY (CNO) REFERENCES C (CNO)
);

INSERT INTO T (TNO, TN, SEX, AGE, ZC, DEPT) VALUES
    ('S1', '王一民', '男', 46, '教授', '计算机'),
    ('S5', '邹敏', '女', 35, '讲师', '软件工程'),
    ('S3', '赵忠秀', '女', 40, '副教授', '信息技术'),
    ('S4', '周彬', '男', 24, '助教', '计算机'),
    ('S6', '钱良', '男', 22, '助教', '软件工程'),
    ('S2', '刘英', '女', 30, '讲师', '信息技术');

INSERT INTO C (CNO, CN, CX, CT) VALUES
    ('C1', '数学', '基础', 4),
    ('C6', '工程训练', '专业', 2),
    ('C3', '汇编程序', '专业基础', 3),
    ('C4', '网络基础', '专业基础', 2),
    ('C5', '数据结构', '专业基础', 3),
    ('C7', 'DB_Design', '专业', 4),
    ('C2', '英语', '基础', 6);

INSERT INTO TC (TNO, CNO, YEAR) VALUES
    ('S1', 'C1', 8),
    ('S1', 'C2', 6),
    ('S1', 'C3', 3),
    ('S4', 'C2', 2),
    ('S2', 'C2', 4),
    ('S3', 'C1', 6),
    ('S3', 'C7', 5),
    ('S3', 'C4', 4),
    ('S3', 'C5', 5),
    ('S2', 'C7', 3),
    ('S4', 'C5', 2),
    ('S4', 'C6', 2),
    ('S2', 'C1', 8),
    ('S5', 'C2', 2);