#include<iostream>
#include<string.h>
using namespace std;

//function used 
void player_name(string &,string & );   //function to name player 1 and player 2   
void display(char [3][3]);              //Display current status of our gaming board
void P1(char [3][3],string);            //take choice of player1
void P2(char [3][3],string);            //take choice of player2
bool check1(char [3][3]);               //check player 1 is wining or not
bool check2(char [3][3]);               //check player 2 is wining or not

//our main function
main()
{
    string player1,player2;
    cout<<"*************************************************************************"<<endl;
    cout<<"\t\tWelcome to Tic Tac Toe"<<endl;
    cout<<"*************************************************************************"<<endl;
    player_name(player1,player2);
    
    char box[][3]={                     //declearation of our board and providing key value to it
        {'1','2','3'},
        {'4','5','6'},
        {'7','8','9'}
    };        

    cout<<endl<<"------------------------------------------------------------------------";
    cout<<endl<<"\tX if for "<<player1<<"\t and \tO  is for "<<player2;
    cout<<endl<<"------------------------------------------------------------------------"<<endl;
    display(box);

    int key=1;                          //key is used to switched between the user
    for(int i=1;i<=9;i++)          
    {
        if(key==1)                      // key =1 for player 1
        {
            P1(box,player1);
            key=0;                      //switching key, key =0 for player 2
        }
        else{
            P2(box,player2);
            key=1;
        }
        display(box);

        if(check1(box))
        {
            cout<<"*************************************************************************"<<endl;
            cout<<"\t\t\t"<<player1<<" is winner !!!"<<endl;
            cout<<"*************************************************************************"<<endl;
            return 0;
        }
        if(check2(box))
        {
            cout<<"*************************************************************************"<<endl;
            cout<<"\t\t\t"<<player2<<" is winner !!!";
            cout<<"*************************************************************************"<<endl;
            return 0;
        }

    }   
        cout<<"*************************************************************************"<<endl;
        cout<<endl<<"\t\t\t"<<"Tie!!"<<endl;                                  //if no one win then last statement will execute 
        cout<<"*************************************************************************"<<endl;
}

void player_name(string &player1,string &player2 )
{
    cout<<"Enter name of player 1 ";
        getline(cin,player1);

    cout<<endl<<"Enter name of player 2 ";
        getline(cin,player2);
}


void P1(char box[3][3],string player1)
{
    char pos;
    flag:
    cout<<endl<<player1<<" your turn ";
        cin>>pos;
    cout<<endl;
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            if(box[i][j]==pos)
            {  
                box[i][j]='X';
                return;
            }
    cout<<endl<<"Enter a valid choice ";
    goto flag;
}
void P2(char box[3][3],string player2)
{
    char pos;
    flag:
    cout<<endl<<player2<<" your turn ";
        cin>>pos;
    cout<<endl;
    for(int i=0;i<3;i++)
        for(int j=0;j<3;j++)
            if(box[i][j]==pos)
            {
                box[i][j]='Y';
                return;
            }
    cout<<endl<<"Enter a valid choice ";
    goto flag;
}

void display(char box[3][3])
{
    for(int i=0;i<3;i++)
    {
        cout<<"\t\t\t";
        for(int j=0;j<3;j++)
        {
            cout<<" "<<box[i][j]<<" ";
            if(j<=1)
                cout<<'|';
        }
        cout<<endl;
        if(i<=1)
        {
            cout<<"\t\t\t";
            for(int l=0;l<3;l++)
                cout<<"----";
        }
        cout<<endl;
    }
}

bool check1(char box[3][3])
{

    //row wise check
    if(box[0][0]=='X'&&box[0][1]=='X'&&box[0][2]=='X')
        return true;
    else if(box[1][0]=='X'&&box[1][1]=='X'&&box[1][2]=='X')
        return true;
    else if(box[2][0]=='X'&&box[2][1]=='X'&&box[2][2]=='X')
        return true;

    //coloumn wise check
    else if(box[0][0]=='X'&&box[1][0]=='X'&&box[2][0]=='X')
        return true;
    else if(box[0][1]=='X'&&box[1][1]=='X'&&box[2][1]=='X')
        return true;
    else if(box[0][2]=='X'&&box[1][2]=='X'&&box[2][2]=='X')
        return true;

    //diagonal check
    else if(box[0][0]=='X'&&box[1][1]=='X'&&box[2][2]=='X')
        return true;
    else if(box[2][0]=='X'&&box[1][1]=='X'&&box[0][2]=='X')
        return true;
                                                            //return false if non of if -else if block become true
    return false;



}

bool check2(char box[3][3])
{

       //row wise check
    if(box[0][0]=='Y'&&box[0][1]=='Y'&&box[0][2]=='Y')
        return true;
    else if(box[1][0]=='Y'&&box[1][1]=='Y'&&box[1][2]=='Y')
        return true;
    else if(box[2][0]=='Y'&&box[2][1]=='Y'&&box[2][2]=='Y')
        return true;
        
    //coloumn wise check
    else if(box[0][0]=='Y'&&box[1][0]=='Y'&&box[2][0]=='Y')
        return true;
    else if(box[0][1]=='Y'&&box[1][1]=='Y'&&box[2][1]=='Y')
        return true;
    else if(box[0][2]=='Y'&&box[1][2]=='Y'&&box[2][2]=='Y')
        return true;

    //diagonal check
    else if(box[0][0]=='Y'&&box[1][1]=='Y'&&box[2][2]=='Y')
        return true;
    else if(box[2][0]=='Y'&&box[1][1]=='Y'&&box[0][2]=='Y')
        return true;

                                                                //return false if non of if -else if block become true
    return false;

}

