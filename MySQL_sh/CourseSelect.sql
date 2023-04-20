CREATE DATABASE CourseSelect;
USE CourseSelect;
CREATE TABLE Student(
    s_id VARCHAR(20) NOT NULL,
    s_name VARCHAR(20) NOT NULL,
    s_birth DATE NOT NULL,
    s_sex VARCHAR(10) NOT NULL,
    PRIMARY KEY(s_id)
);
CREATE TABLE Teacher(
    t_id VARCHAR(20) NOT NULL,
    t_name VARCHAR(20) NOT NULL,
    PRIMARY KEY(t_id)
);
CREATE TABLE Course(
    c_id VARCHAR(20) NOT NULL,
    c_name VARCHAR(20) NOT NULL,
    t_id VARCHAR(20) NOT NULL,
    PRIMARY KEY(c_id),
    FOREIGN KEY (t_id) REFERENCES Teacher(t_id)
);
CREATE TABLE Score(
    s_id VARCHAR(20) NOT NULL ,
    c_id VARCHAR(20) NOT NULL ,
    s_score INT,
    PRIMARY KEY(s_id,c_id),
    FOREIGN KEY (s_id) references Student(s_id),
    FOREIGN KEY (c_id) references Course(c_id)
);
insert into Student (s_id,s_name,s_birth,s_sex) values
('01' , '赵雷' , '2000-01-01' , '男'),
('02' , '钱电' , '2000-12-21' , '男'),
('03' , '孙风' , '2000-05-20' , '男'),
('04' , '李云' , '2000-08-06' , '男'),
('05' , '周梅' , '2001-12-01' , '女'),
('06' , '吴兰' , '2002-03-01' , '女'),
('07' , '郑竹' , '1999-07-01' , '女'),
('08' , '王菊' , '2000-01-20' , '女');

insert into Teacher (t_id, t_name) values
('01' , '张三'),
('02' , '李四'),
('03' , '王五');

insert into Course(c_id, c_name, t_id) values
('01' , '语文' , '02'),
('02' , '数学' , '01'),
('03' , '英语' , '03');

insert into Score(s_id, c_id, s_score) values
('01' , '01' , 80),
('01' , '02' , 90),
('01' , '03' , 99),
('02' , '01' , 70),
('02' , '02' , 60),
('02' , '03' , 80),
('03' , '01' , 80),
('03' , '02' , 80),
('03' , '03' , 80),
('04' , '01' , 50),
('04' , '02' , 30),
('04' , '03' , 20),
('05' , '01' , 76),
('05' , '02' , 87),
('06' , '01' , 31),
('06' , '03' , 34),
('07' , '02' , 89),
('07' , '03' , 98);