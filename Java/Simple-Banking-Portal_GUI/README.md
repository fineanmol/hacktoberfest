# Simple-Banking-Portal
Console and GUI Application of a simple Banking Portal using Java.

<h2>Overview</h2>

A simple banking portal to allow user to add new customer, deposit or withdraw amount from their account and show them their account details.
<br>This project consists of two applications :
1. Console Application - a text-based interface for the user to manage their bank account
2. GUI Application - a GUI-based application providing a simplified experience of banking system to the user


<h2>Structure</h2>

The project consists of the following files : 

<b>BankingSystem.java :</b> It consists of Java program for the console application of a Banking Portal.<br>
The console application is a text-based interface where the user shall add account details every time they run the program and use further options of withdrawing/depositing and account summary.

<b>BankInterface.java :</b> It consists of Java Swing program for a GUI application of a Banking Portal.<br>
The GUI application is created using javax.swing, java.awt packages along with file handling system to store the data of user. In this application, user gets a graphic interface of the Banking Portal with simplified buttons and dialog messages for confirmation and alert. The program also uses File handling system which stores account data, deposit and withdraw transactions in seperate files. While using this application, user need not add account details every time they run the program and hence making it easier to use. Deposit/Withdraw actions by the user will add the transaction data to the respective file and change the balance amount in BankDB.txt file corresponding to the account no. and action.

<b>BankDB.txt :</b> File to store account details for GUI application.

<b>DepositTransactionsDB.txt :</b> File to store Deposit Transaction history for GUI application.

<b>WithdrawTransactionsDB.txt :</b> File to store Withdraw Transaction history for GUI application.
