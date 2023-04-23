--4.42
select TN from T
where exists (select * from TC
    where TNO=T.TNO and CNO='C2');--exists子查询

select TN from T,TC
where T.TNO=TC.TNO and CNO='C2';--联接

SELECT TN FROM T
WHERE TNO IN (SELECT TNO FROM TC
    WHERE CNO='c2');--嵌套

--4.43
select TN from T
WHERE not EXISTS(SELECT * from TC
    WHERE tno=T.tno and cno='c2');

--4.44
SELECT TN FROM T
WHERE NOT EXISTS(SELECT * FROM C
    WHERE NOT EXISTS(SELECT * FROM TC
        WHERE TNO=T.TNO AND CNO=C.CNO));

INSERT INTO TC(TNO,CNO,YEAR) VALUES
('S3','C6',2),
('S3','C2',3),
('S3','C3',3);

INSERT INTO S VALUES('S9','大成销售公司','');