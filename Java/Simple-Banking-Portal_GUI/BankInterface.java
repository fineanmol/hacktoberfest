import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.lang.*;
import java.util.*;

class BankInterface extends JFrame implements ActionListener
{
	JFrame bank, new_cust_frame, deposit_frame, withdraw_frame, view_data_frame;
	JLabel welcome, instr, name, acc_no, balance, password, date, amount;
	JButton new_cust, deposit, withdraw, view_data;
	JButton exit, add_cust, login_dep, login_wid, login_summ, depositB, withdrawB, logout;
	JTextField name_tf, acc_no_tf, balance_tf, acc_no_tf_dep, acc_no_tf_wid, acc_no_tf_summ, date_dep, dep_amt, date_wid, wid_amt;
	JPasswordField password_pf, password_pf_dep, password_pf_wid, password_pf_summ;

	BankInterface()
	{
		bank=new JFrame("Banking Portal");
		bank.setSize(500,500);
		bank.setResizable(false);
		bank.setVisible(true);
		bank.setLayout(null);	
		bank.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		welcome=new JLabel("Welcome to Banking Portal");
		welcome.setFont(new Font("Courier New",Font.BOLD,20));
		welcome.setHorizontalAlignment(SwingConstants.CENTER);
		welcome.setSize(400,40);
		welcome.setLocation(50,50);
		bank.add(welcome);

		new_cust=new JButton("New Customer");
		new_cust.setFont(new Font("Cambria",Font.PLAIN,16));
		new_cust.setHorizontalAlignment(SwingConstants.CENTER);
		new_cust.setSize(400,40);
		new_cust.setLocation(50,130);
		new_cust.addActionListener(this);
		bank.add(new_cust);

		deposit=new JButton("Deposit Amount");
		deposit.setFont(new Font("Cambria",Font.PLAIN,16));
		deposit.setHorizontalAlignment(SwingConstants.CENTER);
		deposit.setSize(400,40);
		deposit.setLocation(50,190);
		deposit.addActionListener(this);
		bank.add(deposit);

		withdraw=new JButton("Withdraw Amount");
		withdraw.setFont(new Font("Cambria",Font.PLAIN,16));
		withdraw.setHorizontalAlignment(SwingConstants.CENTER);
		withdraw.setSize(400,40);
		withdraw.setLocation(50,250);
		withdraw.addActionListener(this);
		bank.add(withdraw);

		view_data=new JButton("View Account Summary");
		view_data.setFont(new Font("Cambria",Font.PLAIN,16));
		view_data.setHorizontalAlignment(SwingConstants.CENTER);
		view_data.setSize(400,40);
		view_data.setLocation(50,310);
		view_data.addActionListener(this);
		bank.add(view_data);

		exit=new JButton("EXIT");
		exit.setFont(new Font("Courier New",Font.BOLD,12));
		exit.setHorizontalAlignment(SwingConstants.CENTER);
		exit.setSize(100,20);
		exit.setLocation(200,390);
		exit.addActionListener(this);
		bank.add(exit);
	}

	public void NewCustomer()
	{
		new_cust_frame=new JFrame("New Customer Portal");
		new_cust_frame.setSize(400,300);
		new_cust_frame.setResizable(false);
		new_cust_frame.setVisible(true);
		new_cust_frame.setLayout(null);	
		new_cust_frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

		instr=new JLabel("Fill the below details to add new customer : ");
		instr.setFont(new Font("Cambria",Font.BOLD,17));
		instr.setHorizontalAlignment(SwingConstants.CENTER);
		instr.setSize(350,30);
		instr.setLocation(25,10);
		new_cust_frame.add(instr);

		name=new JLabel("Name : ");
		name.setFont(new Font("Calibri",Font.PLAIN,16));
		name.setHorizontalAlignment(SwingConstants.RIGHT);
		name.setSize(100,20);
		name.setLocation(25,60);
		new_cust_frame.add(name);

		name_tf=new JTextField();
		name_tf.setSize(200,20);
		name_tf.setLocation(125,60);
		new_cust_frame.add(name_tf);

		acc_no=new JLabel("Account No. : ");
		acc_no.setFont(new Font("Calibri",Font.PLAIN,16));
		acc_no.setHorizontalAlignment(SwingConstants.RIGHT);
		acc_no.setSize(100,20);
		acc_no.setLocation(25,100);
		new_cust_frame.add(acc_no);

		acc_no_tf=new JTextField();
		acc_no_tf.setSize(150,20);
		acc_no_tf.setLocation(125,100);
		new_cust_frame.add(acc_no_tf);

		balance=new JLabel("Balance : ");
		balance.setFont(new Font("Calibri",Font.PLAIN,16));
		balance.setHorizontalAlignment(SwingConstants.RIGHT);
		balance.setSize(100,20);
		balance.setLocation(25,140);
		new_cust_frame.add(balance);

		balance_tf=new JTextField();
		balance_tf.setSize(150,20);
		balance_tf.setLocation(125,140);
		new_cust_frame.add(balance_tf);

		password=new JLabel("Password : ");
		password.setFont(new Font("Calibri",Font.PLAIN,16));
		password.setHorizontalAlignment(SwingConstants.RIGHT);
		password.setSize(100,20);
		password.setLocation(25,180);
		new_cust_frame.add(password);

		password_pf=new JPasswordField();
		password_pf.setSize(150,20);
		password_pf.setLocation(125,180);
		new_cust_frame.add(password_pf);

		add_cust=new JButton("Add Customer");
		add_cust.setFont(new Font("Cambria",Font.BOLD,17));
		add_cust.setHorizontalAlignment(SwingConstants.CENTER);
		add_cust.setSize(150,30);
		add_cust.setLocation(125,225);
		add_cust.addActionListener(this);
		new_cust_frame.add(add_cust);
	}

	public void DepositAmount()
	{
		deposit_frame=new JFrame("Amount Deposit Portal");
		deposit_frame.setSize(400,220);
		deposit_frame.setResizable(false);
		deposit_frame.setVisible(true);
		deposit_frame.setLayout(null);	
		deposit_frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

		instr=new JLabel("Login to Deposit Amount : ");
		instr.setFont(new Font("Cambria",Font.BOLD,17));
		instr.setHorizontalAlignment(SwingConstants.CENTER);
		instr.setSize(350,30);
		instr.setLocation(25,10);
		deposit_frame.add(instr);

		acc_no=new JLabel("Account No. : ");
		acc_no.setFont(new Font("Calibri",Font.PLAIN,16));
		acc_no.setHorizontalAlignment(SwingConstants.RIGHT);
		acc_no.setSize(100,20);
		acc_no.setLocation(25,60);
		deposit_frame.add(acc_no);

		acc_no_tf_dep=new JTextField();
		acc_no_tf_dep.setSize(150,20);
		acc_no_tf_dep.setLocation(125,60);
		deposit_frame.add(acc_no_tf_dep);

		password=new JLabel("Password : ");
		password.setFont(new Font("Calibri",Font.PLAIN,16));
		password.setHorizontalAlignment(SwingConstants.RIGHT);
		password.setSize(100,20);
		password.setLocation(25,100);
		deposit_frame.add(password);

		password_pf_dep=new JPasswordField();
		password_pf_dep.setSize(150,20);
		password_pf_dep.setLocation(125,100);
		deposit_frame.add(password_pf_dep);

		login_dep=new JButton("Login");
		login_dep.setFont(new Font("Cambria",Font.BOLD,17));
		login_dep.setHorizontalAlignment(SwingConstants.CENTER);
		login_dep.setSize(150,30);
		login_dep.setLocation(125,145);
		login_dep.addActionListener(this);
		deposit_frame.add(login_dep);
	}

	public void WithdrawAmount()
	{
		withdraw_frame=new JFrame("Amount Withdrawal Portal");
		withdraw_frame.setSize(400,220);
		withdraw_frame.setResizable(false);
		withdraw_frame.setVisible(true);
		withdraw_frame.setLayout(null);	
		withdraw_frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

		instr=new JLabel("Login to Withdraw Amount : ");
		instr.setFont(new Font("Cambria",Font.BOLD,17));
		instr.setHorizontalAlignment(SwingConstants.CENTER);
		instr.setSize(350,30);
		instr.setLocation(25,10);
		withdraw_frame.add(instr);

		acc_no=new JLabel("Account No. : ");
		acc_no.setFont(new Font("Calibri",Font.PLAIN,16));
		acc_no.setHorizontalAlignment(SwingConstants.RIGHT);
		acc_no.setSize(100,20);
		acc_no.setLocation(25,60);
		withdraw_frame.add(acc_no);

		acc_no_tf_wid=new JTextField();
		acc_no_tf_wid.setSize(150,20);
		acc_no_tf_wid.setLocation(125,60);
		withdraw_frame.add(acc_no_tf_wid);

		password=new JLabel("Password : ");
		password.setFont(new Font("Calibri",Font.PLAIN,16));
		password.setHorizontalAlignment(SwingConstants.RIGHT);
		password.setSize(100,20);
		password.setLocation(25,100);
		withdraw_frame.add(password);

		password_pf_wid=new JPasswordField();
		password_pf_wid.setSize(150,20);
		password_pf_wid.setLocation(125,100);
		withdraw_frame.add(password_pf_wid);

		login_wid=new JButton("Login");
		login_wid.setFont(new Font("Cambria",Font.BOLD,17));
		login_wid.setHorizontalAlignment(SwingConstants.CENTER);
		login_wid.setSize(150,30);
		login_wid.setLocation(125,145);
		login_wid.addActionListener(this);
		withdraw_frame.add(login_wid);
	}

	public void AccountSummary()
	{
		view_data_frame=new JFrame("Account Summary");
		view_data_frame.setSize(400,220);
		view_data_frame.setResizable(false);
		view_data_frame.setVisible(true);
		view_data_frame.setLayout(null);	
		view_data_frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

		instr=new JLabel("Login to View Account Summary : ");
		instr.setFont(new Font("Cambria",Font.BOLD,17));
		instr.setHorizontalAlignment(SwingConstants.CENTER);
		instr.setSize(350,30);
		instr.setLocation(25,10);
		view_data_frame.add(instr);

		acc_no=new JLabel("Account No. : ");
		acc_no.setFont(new Font("Calibri",Font.PLAIN,16));
		acc_no.setHorizontalAlignment(SwingConstants.RIGHT);
		acc_no.setSize(100,20);
		acc_no.setLocation(25,60);
		view_data_frame.add(acc_no);

		acc_no_tf_summ=new JTextField();
		acc_no_tf_summ.setSize(150,20);
		acc_no_tf_summ.setLocation(125,60);
		view_data_frame.add(acc_no_tf_summ);

		password=new JLabel("Password : ");
		password.setFont(new Font("Calibri",Font.PLAIN,16));
		password.setHorizontalAlignment(SwingConstants.RIGHT);
		password.setSize(100,20);
		password.setLocation(25,100);
		view_data_frame.add(password);

		password_pf_summ=new JPasswordField();
		password_pf_summ.setSize(150,20);
		password_pf_summ.setLocation(125,100);
		view_data_frame.add(password_pf_summ);

		login_summ=new JButton("Login");
		login_summ.setFont(new Font("Cambria",Font.BOLD,17));
		login_summ.setHorizontalAlignment(SwingConstants.CENTER);
		login_summ.setSize(150,30);
		login_summ.setLocation(125,145);
		login_summ.addActionListener(this);
		view_data_frame.add(login_summ);
	}

	public void actionPerformed(ActionEvent ae)
	{
		if(ae.getSource()==exit)
		{
			System.exit(0);
		}

		if(ae.getSource()==new_cust)
		{
			NewCustomer();
		}

		if(ae.getSource()==deposit)
		{
			DepositAmount();
		}

		if(ae.getSource()==withdraw)
		{
			WithdrawAmount();
		}

		if(ae.getSource()==view_data)
		{
			AccountSummary();
		}

		if(ae.getSource()==add_cust)
		{
			int n=JOptionPane.showConfirmDialog(null,"Add new customer?","New Customer Confirmation",JOptionPane.YES_NO_OPTION);
			if(n==JOptionPane.YES_OPTION)
			{
				try
				{
					File obj=new File("BankDB.txt");
					if(obj.createNewFile())
					{
						System.out.println("File Created");
					}
					else
					{
						System.out.println("File Exists");
					}
					FileWriter writer=new FileWriter("BankDB.txt",true);
					writer.write(name_tf.getText()+"\r\n"+acc_no_tf.getText()+"\r\n"+balance_tf.getText()+"\r\n"+password_pf.getText()+"\r\n");
					writer.close();
				}
				catch(Exception e)
				{
					System.out.println(e);
				}
				new_cust_frame.dispose();				
			}
		}

		if(ae.getSource()==login_dep)
		{
			int n=JOptionPane.showConfirmDialog(null,"Are you sure?","Login Confirmation",JOptionPane.YES_NO_OPTION);
			if(n==JOptionPane.YES_OPTION)
			{
				try
				{
					File obj=new File("BankDB.txt");
					Scanner read=new Scanner(obj);
					Vector v=new Vector();
					while(read.hasNextLine())
					{
						v.add(read.nextLine());
					}
					int x=v.indexOf(acc_no_tf_dep.getText());
					int y=v.indexOf(password_pf_dep.getText());
					if(y==(x+2))
					{
						JOptionPane.showMessageDialog(null,"Login Successful!");
						deposit_frame.remove(instr);
						deposit_frame.remove(acc_no);
						deposit_frame.remove(acc_no_tf_dep);
						deposit_frame.remove(password);
						deposit_frame.remove(password_pf_dep);
						deposit_frame.remove(login_dep);
						
						deposit_frame.dispose();

						deposit_frame=new JFrame("Amount Deposit Portal");
						deposit_frame.setSize(400,220);
						deposit_frame.setResizable(false);
						deposit_frame.setVisible(true);
						deposit_frame.setLayout(null);	
						deposit_frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

						date=new JLabel("Date : ");
						date.setFont(new Font("Calibri",Font.PLAIN,16));
						date.setHorizontalAlignment(SwingConstants.RIGHT);
						date.setSize(100,20);
						date.setLocation(25,40);
						deposit_frame.add(date);

						date_dep=new JTextField();
						date_dep.setSize(125,20);
						date_dep.setLocation(200,40);
						deposit_frame.add(date_dep);

						amount=new JLabel("Amount to Deposit : ");
						amount.setFont(new Font("Calibri",Font.PLAIN,16));
						amount.setHorizontalAlignment(SwingConstants.RIGHT);
						amount.setSize(150,20);
						amount.setLocation(25,80);
						deposit_frame.add(amount);

						dep_amt=new JTextField();
						dep_amt.setSize(125,20);
						dep_amt.setLocation(200,80);
						deposit_frame.add(dep_amt);

						depositB=new JButton("Deposit");
						depositB.setFont(new Font("Cambria",Font.BOLD,17));
						depositB.setHorizontalAlignment(SwingConstants.CENTER);
						depositB.setSize(150,30);
						depositB.setLocation(125,145);
						depositB.addActionListener(this);
						deposit_frame.add(depositB);
					}
					else
					{
						JOptionPane.showMessageDialog(null,"Login Failed!");
					}
				}
				catch(Exception e)
				{
					System.out.println(e);
				}
			}
		}

		if(ae.getSource()==depositB)
		{
			double bal=0;
			int n=JOptionPane.showConfirmDialog(null,"Are you sure?","Deposit Confirmation",JOptionPane.YES_NO_OPTION);
			if(n==JOptionPane.YES_OPTION)
			{
				try
				{
					File obj=new File("DepositTransactionsDB.txt");
					if(obj.createNewFile())
					{
						System.out.println("File Created");
					}
					else
					{
						System.out.println("File Exists");
					}
					FileWriter writer=new FileWriter("DepositTransactionsDB.txt",true);
					writer.write(acc_no_tf_dep.getText()+"\r\n"+date_dep.getText()+"\r\n"+dep_amt.getText()+"\r\n");
					writer.close();
				}
				catch(Exception e)
				{
					System.out.println(e);
				}

				try
				{
					File obj1=new File("BankDB.txt");
					Scanner read=new Scanner(obj1);
					Vector v=new Vector();
					while(read.hasNextLine())
					{
						v.add(read.nextLine());
					}
					int x=v.indexOf(acc_no_tf_dep.getText());
					bal=Double.parseDouble(v.elementAt(x+1).toString());
					bal=bal+Double.parseDouble(dep_amt.getText());
					v.set(x+1,bal);

					FileWriter writer=new FileWriter("BankDB.txt");
					for(int a=0;a<v.size();a++)
					{
						writer.append(v.elementAt(a)+"\r\n");
					}
					writer.close();
				}
				catch(Exception e)
				{
					System.out.println(e);
				}

				JOptionPane.showMessageDialog(null,"Deposit Successful!\nCurrent Balance : "+bal);
				deposit_frame.dispose();
			}
		}

		if(ae.getSource()==login_wid)
		{
			int n=JOptionPane.showConfirmDialog(null,"Are you sure?","Login Confirmation",JOptionPane.YES_NO_OPTION);
			if(n==JOptionPane.YES_OPTION)
			{
				try
				{
					File obj=new File("BankDB.txt");
					Scanner read=new Scanner(obj);
					Vector v=new Vector();
					while(read.hasNextLine())
					{
						v.add(read.nextLine());
					}
					int x=v.indexOf(acc_no_tf_wid.getText());
					int y=v.indexOf(password_pf_wid.getText());
					if(y==(x+2))
					{
						JOptionPane.showMessageDialog(null,"Login Successful!");
						withdraw_frame.remove(instr);
						withdraw_frame.remove(acc_no);
						withdraw_frame.remove(acc_no_tf_wid);
						withdraw_frame.remove(password);
						withdraw_frame.remove(password_pf_wid);
						withdraw_frame.remove(login_wid);
						
						withdraw_frame.dispose();

						withdraw_frame=new JFrame("Amount Withdrawal Portal");
						withdraw_frame.setSize(400,220);
						withdraw_frame.setResizable(false);
						withdraw_frame.setVisible(true);
						withdraw_frame.setLayout(null);	
						withdraw_frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

						date=new JLabel("Date : ");
						date.setFont(new Font("Calibri",Font.PLAIN,16));
						date.setHorizontalAlignment(SwingConstants.RIGHT);
						date.setSize(100,20);
						date.setLocation(25,40);
						withdraw_frame.add(date);

						date_wid=new JTextField();
						date_wid.setSize(125,20);
						date_wid.setLocation(200,40);
						withdraw_frame.add(date_wid);

						amount=new JLabel("Amount to Withdraw : ");
						amount.setFont(new Font("Calibri",Font.PLAIN,16));
						amount.setHorizontalAlignment(SwingConstants.RIGHT);
						amount.setSize(150,20);
						amount.setLocation(25,80);
						withdraw_frame.add(amount);

						wid_amt=new JTextField();
						wid_amt.setSize(125,20);
						wid_amt.setLocation(200,80);
						withdraw_frame.add(wid_amt);

						withdrawB=new JButton("Withdraw");
						withdrawB.setFont(new Font("Cambria",Font.BOLD,17));
						withdrawB.setHorizontalAlignment(SwingConstants.CENTER);
						withdrawB.setSize(150,30);
						withdrawB.setLocation(125,145);
						withdrawB.addActionListener(this);
						withdraw_frame.add(withdrawB);
					}
					else
					{
						JOptionPane.showMessageDialog(null,"Login Failed!");
					}
				}
				catch(Exception e)
				{
					System.out.println(e);
				}
			}
		}

		if(ae.getSource()==withdrawB)
		{
			double bal=0;
			int n=JOptionPane.showConfirmDialog(null,"Are you sure?","Withdrawal Confirmation",JOptionPane.YES_NO_OPTION);
			if(n==JOptionPane.YES_OPTION)
			{
				try
				{
					File obj=new File("WithdrawTransactionsDB.txt");
					if(obj.createNewFile())
					{
						System.out.println("File Created");
					}
					else
					{
						System.out.println("File Exists");
					}
					FileWriter writer=new FileWriter("WithdrawTransactionsDB.txt",true);
					writer.write(acc_no_tf_wid.getText()+"\r\n"+date_wid.getText()+"\r\n"+wid_amt.getText()+"\r\n");
					writer.close();
				}
				catch(Exception e)
				{
					System.out.println(e);
				}

				try
				{
					File obj1=new File("BankDB.txt");
					Scanner read=new Scanner(obj1);
					Vector v=new Vector();
					while(read.hasNextLine())
					{
						v.add(read.nextLine());
					}
					int x=v.indexOf(acc_no_tf_wid.getText());
					bal=Double.parseDouble(v.elementAt(x+1).toString());
					bal=bal-Double.parseDouble(wid_amt.getText());
					v.set(x+1,bal);

					FileWriter writer=new FileWriter("BankDB.txt");
					for(int a=0;a<v.size();a++)
					{
						writer.append(v.elementAt(a)+"\r\n");
					}
					writer.close();
				}
				catch(Exception e)
				{
					System.out.println(e);
				}

				JOptionPane.showMessageDialog(null,"Withdraw Successful!\nCurrent Balance : "+bal);
				withdraw_frame.dispose();
			}
		}

		if(ae.getSource()==login_summ)
		{
			int n=JOptionPane.showConfirmDialog(null,"Are you sure?","Login Confirmation",JOptionPane.YES_NO_OPTION);
			if(n==JOptionPane.YES_OPTION)
			{
				try
				{
					File obj=new File("BankDB.txt");
					Scanner read=new Scanner(obj);
					Vector v=new Vector();
					while(read.hasNextLine())
					{
						v.add(read.nextLine());
					}
					int x=v.indexOf(acc_no_tf_summ.getText());
					int y=v.indexOf(password_pf_summ.getText());
					if(y==(x+2))
					{
						JOptionPane.showMessageDialog(null,"Login Successful!");
						view_data_frame.remove(instr);
						view_data_frame.remove(acc_no);
						view_data_frame.remove(acc_no_tf_summ);
						view_data_frame.remove(password);
						view_data_frame.remove(password_pf_summ);
						view_data_frame.remove(login_summ);
						
						view_data_frame.dispose();

						view_data_frame=new JFrame("Account Summary");
						view_data_frame.setSize(400,250);
						view_data_frame.setResizable(false);
						view_data_frame.setVisible(true);
						view_data_frame.setLayout(null);	
						view_data_frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

						JTextArea summary=new JTextArea();
						summary.setFont(new Font("Cambria",Font.PLAIN,16));
						summary.setSize(300,140);
						summary.setLocation(50,25);
						summary.setEditable(false);
						summary.setText("\n    Name : "+v.elementAt(x-1)+"\n\n    Account No. : "+v.elementAt(x)+"\n\n    Balance : "+v.elementAt(x+1)+"\n");
						view_data_frame.add(summary);

						logout=new JButton("Logout");
						logout.setFont(new Font("TIMES NEW ROMAN",Font.BOLD,16));
						logout.setHorizontalAlignment(SwingConstants.CENTER);
						logout.setSize(100,25);
						logout.setLocation(150,190);
						logout.addActionListener(this);
						view_data_frame.add(logout);
					}
					else
					{
						JOptionPane.showMessageDialog(null,"Login Failed!");
					}
				}
				catch(Exception e)
				{
					System.out.println(e);
				}
			}
		}

		if(ae.getSource()==logout)
		{
			int n=JOptionPane.showConfirmDialog(null,"Are you sure?","Logout Confirmation",JOptionPane.YES_NO_OPTION);
			if(n==JOptionPane.YES_OPTION)
			{
				view_data_frame.dispose();
			}							
		}
		
	}

	public static void main(String args[])
	{
		BankInterface bi=new BankInterface();
	}
}