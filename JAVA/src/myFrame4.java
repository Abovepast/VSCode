import javax.swing.*;
import java.awt.*;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class myFrame4 extends JFrame {
    public myFrame4(String title) {
        super(title);

        this.setLayout(new FlowLayout());
        JTextField textField = new JTextField(20);
        this.add(textField);

        textField.addKeyListener(new KeyAdapter() {
            @Override
            public void keyTyped(KeyEvent e) {
                super.keyTyped(e);
            }

            @Override
            public void keyPressed(KeyEvent e) {
                char typedChar = e.getKeyChar();
                int typedInt = e.getKeyCode();

                System.out.println("输入的键是"+typedChar+",输入的键ASCII值是"+typedInt);
            }
        });

        this.setSize(400,300);
        this.setResizable(true);
        this.setLocation(200,200);
        this.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        this.setVisible(true);
    }
}
