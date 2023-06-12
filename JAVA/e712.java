import java.util.*;
public class e712 {
    public static void main(String[] args) {
        TreeSet ts = new TreeSet();
        ts.add(new Student_e712("Lucy",18));
        ts.add(new Student_e712("Tom",20));
        ts.add(new Student_e712("dzj",20));
        ts.add(new Student_e712("hzh",20));

        System.out.println(ts);
    }
}

class Student_e712 implements Comparable{

    //属性
    private String name;
    private int age;
    //构造方法
    Student_e712 () {}
    Student_e712 (String name, int age) {
       this.name = name;
       this.age = age;
    }
    //get-set
    public String name() {
        return this.name;
    }
    public int age() {
        return this.age;
    }
    //重写方法
    @Override
    public String toString() {
        return "年龄："+age+",姓名："+name;
    }

    //用户方法

    @Override   //重写比较方法，年龄小的放前面
    public int compareTo(Object o) {
        Student_e712 stu = (Student_e712) o;   //强制类型转换，目的是调用成员属性,编写比较方法

        if(this.age - stu.age > 0) {
            return 1;
        }
        if(this.age-stu.age == 0) {
            return 0;
        }
        return -1;
    }
}
