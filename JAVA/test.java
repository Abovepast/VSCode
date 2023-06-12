public class test {
    public static void main(String[] args) {
        Resume resume = new Resume("李四", "男", 20);

        resume.introduce();
    }
}

class Resume {
    private String name;
    private String sex;
    private int age;

    public Resume () {}
    public Resume (String name,String sex,int age) {
        this.name = name;
        this.sex = sex;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public String getSex() {
        return sex;
    }

    public int getAge() {
        return age;
    }

    public void introduce() {
        System.out.printf("姓名：%s\n性别：%s\n年龄：%d",name,sex,age);
    }
}
