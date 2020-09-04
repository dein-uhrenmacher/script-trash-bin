import javax.swing.*;
class main{
    public static void main(String args[]){
       JFrame frame = new JFrame("PVP-Helferchen");
       frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
       frame.setSize(300,300);
       JButton button = new JButton("Start");
       frame.getContentPane().add(button); // Adds Button to content pane of frame
       frame.setVisible(true);
    }
}
