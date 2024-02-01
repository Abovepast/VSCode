// See https://aka.ms/new-console-template for more information
using System.Data.SqlClient;
string myConnectionString;
myConnectionString = "Initial Catalog=Northwind;Data Source=(localdb);MSSQLLocalDB;IntegratedSecurity=SSPI;";
SqlConnection myConnection = new SqlConnection(myConnectionString);                  //定义连接对象

string myInsertQuery = "  INSERT t_student(xh, name, class, sex) values(0001,'张三','信息32','男')";                       //定义插入数据的字符串
SqlCommand myCommand = new SqlCommand(myInsertQuery);                     //定义查询命令对象
myCommand.Connection = myConnection;
myConnection.Open();                                //打开连接
myCommand.ExecuteNonQuery();                             //执行操作
myConnection.Close();
