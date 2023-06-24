import javax.swing.*;

public class myFrame3 extends JFrame {
    public myFrame3(String title) {
        super(title);

        JButton btn = new JButton("按钮");
        JPanel root = new JPanel();

        this.add(root.add(btn));

        btn.addActionListener((e -> {
            System.out.println("按钮被点击了");
        }));

        this.setSize(400,300);
        this.setLocation(400,400);
        this.setResizable(true);
        this.setVisible(true);
        this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
    }
}
