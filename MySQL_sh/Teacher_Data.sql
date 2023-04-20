CREATE DATABASE TEACHER;
USE TEACHER;

CREATE TABLE T
(
    TNO  CHAR(4)    NOT NULL,
    TN   CHAR(10)   NOT NULL,
    SEX  CHAR(2)    NOT NULL CHECK (SEX IN ('��', 'Ů')),
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
    ('S1', '��һ��', '��', 46, '����', '�����'),
    ('S5', '����', 'Ů', 35, '��ʦ', '�������'),
    ('S3', '������', 'Ů', 40, '������', '��Ϣ����'),
    ('S4', '�ܱ�', '��', 24, '����', '�����'),
    ('S6', 'Ǯ��', '��', 22, '����', '�������'),
    ('S2', '��Ӣ', 'Ů', 30, '��ʦ', '��Ϣ����');

INSERT INTO C (CNO, CN, CX, CT) VALUES
    ('C1', '��ѧ', '����', 4),
    ('C6', '����ѵ��', 'רҵ', 2),
    ('C3', '������', 'רҵ����', 3),
    ('C4', '�������', 'רҵ����', 2),
    ('C5', '���ݽṹ', 'רҵ����', 3),
    ('C7', 'DB_Design', 'רҵ', 4),
    ('C2', 'Ӣ��', '����', 6);

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