import java.util.Scanner;

// Solution by Gaurav Mishra

public class RPS {
public static void main(String[] args) {
System.out.println("Rock(1) | Paper(2) | Siccoros(3)");

System.out.println("=======================================");


Scanner sc=new Scanner(System.in);

System.out.print("Choose value for player 1 : ");
int player1=sc.nextInt();

// sc.close();

System.out.print("Choose value for player 2 : ");

int player2=sc.nextInt();

sc.close();

if(player1==1){
System.out.println("Player1 choose = Rock");
}else if(player1==2){
System.out.println("Player1 choose = Paper");
}else if(player1==3){
System.out.println("Player1 choose = Siccoros");
}else{
System.out.println("Please choose value between 1 to 3");
}


if(player2==1){
System.out.println("Player2 choose = Rock");
}else if(player2==2){
System.out.println("Player2 choose = Paper");
}else if(player2==3){
System.out.println("Player2 choose = Siccoros");
}else{
System.out.println("Please choose value between 1 to 3");
}
System.out.println("=======================================");
System.out.println("=============== RESULT ================");
System.out.println("=======================================");
switch (player1) {
case 1:
if(player2==2){
System.out.println("Player2 wins");
}else{
System.out.println("Player1 wins");
}

break;

case 2:
if(player2==3){
System.out.println("Player2 wins");
}else{
System.out.println("Player1 wins");
}

break;

case 3:
if(player2==1){
System.out.println("Player2 wins");
}else{
System.out.println("Player1 wins");
}

break;


default:
System.out.println("Try next time");
break;
}

System.out.println("=======================================");



}
}