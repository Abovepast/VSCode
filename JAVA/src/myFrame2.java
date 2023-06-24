import javax.swing.*;
import java.awt.*;

public class myFrame2 extends JFrame {
    public myFrame2(String title) {
        super(title);

        this.setLayout(new GridLayout(4,4));

        int n=12;
        while(n-- != 0) {
            this.add(new JButton("btn"+(12-n)));
        }

        this.setSize(400,300);
        this.setLocation(400,400);
        this.setResizable(true);
        this.setVisible(true);
        this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);
    }
}
