import java.util.*;
import java.lang.*;

class Bank
{
	String name;
	long acc_no;
	double balance;
}

class Deposit
{
	long acc_no;
	double deposit_amount;
	String date;
}

class Withdraw
{
	long acc_no;
	double withdraw_amount;
	String date;
}

class BankingSystem
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);

		Vector bank=new Vector();
		Vector deposit=new Vector();
		Vector withdraw=new Vector();

		String name,date;
		long acc_no;
		double balance,withdraw_amount,deposit_amount;
		int choice=0;

		Bank b[]=new Bank[1000];
		Withdraw w[]=new Withdraw[1000];
		Deposit d[]=new Deposit[1000];
		for(int n=0;n<1000;n++)
		{
			b[n]=new Bank();
			w[n]=new Withdraw();
			d[n]=new Deposit();
		}

		int i=0,j=0,k=0;
		while(choice!=5)
		{
			System.out.println("\nEnter your Choice number to perform action :\n1. New Customer\n2. Withdraw Amount\n3. Deposit Amount\n4. View Account Details\n5. EXIT");
			choice=sc.nextInt();
			sc.nextLine();
			switch(choice)
			{
				case 1:
					System.out.println("Enter Name : ");
					b[i].name=sc.nextLine();
					System.out.println("Enter Account Number : ");
					b[i].acc_no=sc.nextLong();
					System.out.println("Enter Balance : ");
					b[i].balance=sc.nextDouble();
					bank.add(b[i].name);
					bank.add(b[i].acc_no);
					bank.add(b[i].balance);
					i++;
					break;

				case 2:
					System.out.println("Enter Account Number : ");
					w[j].acc_no=sc.nextLong();
					for(int m=0;m<b.length;m++)
					{
						if(b[m].acc_no==w[j].acc_no)
						{
							System.out.println("Enter Date : ");
							w[j].date=sc.next();
							System.out.println("Enter Amount to Withdraw : ");
							w[j].withdraw_amount=sc.nextDouble();
							withdraw.add(w[j].acc_no);
							withdraw.add(w[j].date);
							withdraw.add(w[j].withdraw_amount);
							for(int n=0;n<b.length;n++)
							{
								if(w[j].acc_no==b[n].acc_no)
								{
									b[n].balance=b[n].balance-w[j].withdraw_amount;
									bank.set(bank.indexOf(w[j].acc_no)+1,b[n].balance);
								}
							}
							j++;
							break;
						}
						else
						{
							if(m==b.length-1)
							{
								System.out.println("Account dose not exist in System!\nAdd new acount using New Customer");	
							}
						}
					}
					break;

				case 3:
					System.out.println("Enter Account Number : ");
					d[k].acc_no=sc.nextLong();
					for(int m=0;m<b.length;m++)
					{
						if(b[m].acc_no==d[k].acc_no)
						{
							System.out.println("Enter Date : ");
							d[k].date=sc.next();
							System.out.println("Enter Amount to Deposit : ");
							d[k].deposit_amount=sc.nextDouble();
							deposit.add(d[k].acc_no);
							deposit.add(d[k].date);
							deposit.add(d[k].deposit_amount);
							for(int n=0;n<b.length;n++)
							{
								if(d[k].acc_no==b[n].acc_no)
								{
									b[n].balance=b[n].balance+d[k].deposit_amount;
									bank.set(bank.indexOf(d[k].acc_no)+1,b[n].balance);
								}
							}
							k++;
							break;
						}
						else
						{
							if(m==b.length-1)
							{
								System.out.println("Account dose not exist in System!\nAdd new acount using New Customer");	
							}
						}	
					}	
					break;

				case 4:
					System.out.println("Enter Account Number : ");
					acc_no=sc.nextLong();
					for(int m=0;m<b.length;m++)
					{
						if(b[m].acc_no==acc_no)
						{
							int no=bank.indexOf(acc_no);
							System.out.println("\nName : "+bank.elementAt(no-1)+"\nAccount Number : "+bank.elementAt(no)+"\nBalance : "+bank.elementAt(no+1));
							break;
						}
						else
						{
							if(m==b.length-1)
							{
								System.out.println("Account dose not exist in System!\nAdd new acount using New Customer");	
							}
						}
					}
					break;

				case 5:
					break;

				default:
					System.out.println("Invalid Choice!!");
			}
		}
	}
}