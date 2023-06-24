import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class myFrame1 extends JFrame {

    public myFrame1(String title) {

        super(title);

        this.setLayout(new FlowLayout(FlowLayout.LEFT));

        this.add(new JButton("第一个"));
        this.add(new JButton("第二个"));
        this.add(new JButton("第三个"));

        this.add(new JButton("第四个"));
        this.add(new JButton("第五个"));
        this.add(new JButton("第六个"));

        this.add(new JButton("第七个"));
        this.add(new JButton("第八个"));
        this.add(new JButton("第九个"));


        this.setSize(400,300);
        this.setLocation(400,400);
        this.setResizable(true);
        this.setVisible(true);
        this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
    }
}
