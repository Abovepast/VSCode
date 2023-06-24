import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class myFrame extends JFrame {
    JDialog dialog = new JDialog(this,"子窗口",false);

    public myFrame(String title) {

        super(title);

        dialog.setSize(300,200);
        dialog.setLocation(420,440);
        dialog.setResizable(true);

        dialog.setDefaultCloseOperation(JDialog.HIDE_ON_CLOSE);

        JPanel root = new JPanel();
        this.add(root);



        this.add(new JButton("上面"),BorderLayout.NORTH);
        this.add(new JButton("下面"),BorderLayout.SOUTH);
        this.add(new JButton("左边"),BorderLayout.WEST);
        this.add(new JButton("右边"),BorderLayout.EAST);

        JButton button = new JButton("打开");
        this.add(button,BorderLayout.CENTER);
//        this.add(new JButton("中间"),BorderLayout.CENTER);

        this.setSize(400,300);
        this.setLocation(400,400);
        this.setResizable(true);
        this.setVisible(true);
        this.setDefaultCloseOperation(this.EXIT_ON_CLOSE);


        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                dialog.setVisible(true);
            }
        });



    }

}
