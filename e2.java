根据题目要求，我们需要创建一个包含不同类型员工的数组，并实现根据指定月份计算工资的功能。下面是一个示例的代码实现：

java
Copy code
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 创建 Employee 数组，存放不同类型的员工
        Employee[] employees = new Employee[5];
        employees[0] = new SalariedEmployee("John", 10000);
        employees[1] = new HourlyEmployee("Alice", 20, 180);
        employees[2] = new SalesEmployee("Bob", 5000, 0.1);
        employees[3] = new BasePlusSalesEmployee("Charlie", 5000, 0.1, 2000);
        employees[4] = new Employee("David"); // 默认员工对象

        System.out.print("请输入月份：");
        int month = scanner.nextInt();

        for (Employee employee : employees) {
            System.out.println("员工姓名：" + employee.getName());
            System.out.println("工资：" + employee.getSalary(month));
            System.out.println();
        }

        scanner.close();
    }
}

class Employee {
    private String name;
    private int birthMonth;

    public Employee(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public int getBirthMonth() {
        return birthMonth;
    }

    public void setBirthMonth(int birthMonth) {
        this.birthMonth = birthMonth;
    }

    public double getSalary(int month) {
        double salary = 0;
        if (month == birthMonth) {
            salary += 100;
        }
        return salary;
    }
}

class SalariedEmployee extends Employee {
    private double monthlySalary;

    public SalariedEmployee(String name, double monthlySalary) {
        super(name);
        this.monthlySalary = monthlySalary;
    }

    public double getMonthlySalary() {
        return monthlySalary;
    }

    public void setMonthlySalary(double monthlySalary) {
        this.monthlySalary = monthlySalary;
    }

    @Override
    public double getSalary(int month) {
        double salary = super.getSalary(month);
        salary += monthlySalary;
        return salary;
    }
}

class HourlyEmployee extends Employee {
    private double hourlySalary;
    private double hoursWorked;

    public HourlyEmployee(String name, double hourlySalary, double hoursWorked) {
        super(name);
        this.hourlySalary = hourlySalary;
        this.hoursWorked = hoursWorked;
    }

    public double getHourlySalary() {
        return hourlySalary;
    }

    public void setHourlySalary(double hourlySalary) {
        this.hourlySalary = hourlySalary;
    }

    public double getHoursWorked() {
        return hoursWorked;
    }

    public void setHoursWorked(double hoursWorked) {
        this.hoursWorked = hoursWorked;
    }

    @Override
    public double getSalary(int month) {
        double salary = super.getSalary(month);
        if (hoursWorked > 160) {
            double extraHours = hoursWorked - 160;
            salary += hourlySalary * (1.5 * extraHours + 160);
        } else {
            salary += hourlySalary * hoursWorked;
        }
        return salary;
    }
}

class SalesEmployee extends Employee {
    private double monthlySales;
    private double commissionRate;

    public SalesEmployee(String name, double monthlySales, double commissionRate) {
        super(name);
        this.monthlySales = monthlySales;
        this.commissionRate = commissionRate;
    }

    public double getMonthlySales() {
        return monthlySales;
    }

    public void setMonthlySales(double monthlySales) {
        this.monthlySales = monthlySales;
    }

    public double getCommissionRate() {
        return commissionRate;
    }

    public void setCommissionRate(double commissionRate) {
        this.commissionRate = commissionRate;
    }

    @Override
    public double getSalary(int month) {
        double salary = super.getSalary(month);
        salary += monthlySales * commissionRate;
        return salary;
    }
}

class BasePlusSalesEmployee extends SalesEmployee {
    private double baseSalary;

    public BasePlusSalesEmployee(String name, double monthlySales, double commissionRate, double baseSalary) {
        super(name, monthlySales, commissionRate);
        this.baseSalary = baseSalary;
    }

    public double getBaseSalary() {
        return baseSalary;
    }

    public void setBaseSalary(double baseSalary) {
        this.baseSalary = baseSalary;
    }

    @Override
    public double getSalary(int month) {
        double salary = super.getSalary(month);
        salary += baseSalary;
        return salary;
    }
}