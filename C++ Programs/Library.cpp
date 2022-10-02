#include <iostream>
#include <fstream>

using namespace std;

int flag123=0;
class Librarian {
    protected:
    unsigned int id=0,exp;
    string lname,qual;
    public:

    void gatherData(){
        cout << "\nLibrarian Name: ";
        cin >> lname;
        cout << "\nLibrarian Qualification: ";
        cin >> qual;
        cout << "\nLibrarian Work Experience(in years): ";
        cin >> exp;
        id++;
    }

    void write(){
        ofstream write;
        write.open("librarian.txt",ios::app);
        if(!write){
            cout << "\nFile could not be opened.";
        } else {
            cout << "\nWriting Data to File....";
            write << id << " " << lname << " " << qual << " " << exp << endl;
            cout << "\nData has been exported to file named librarian.txt";
        }
    }


    void displaydata(){
    fstream file;
	cout << "\nAll Librarian Data:";
	file.open("librarian.txt", ios::in);
	if (!file)
		cout << "\n\nFile Opening Error!";
	else {

		file >> id >> lname;
		file >> qual >> exp;
		while (!file.eof()) {
            cout << "\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=";
			cout << "\nID: " << id
				<< "\nLibrarian Name: " << lname
				<< "\nLibrarian Qualification: " << qual
				<< "\nLibrarian Experience: " << exp << "yrs"
				<< "\n";
                cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n";
        file >> id >> lname;
		file >> qual >> exp;
		}
		file.close();
	}
    }


    void specificData(int idc)
    {
        int flag=0;
        fstream read;
        read.open("librarian.txt",ios::in);
        if(!read){
            cout << "\n\nFile Opening Error!";
        } else {
            while(!read.eof()){
                read >> id;
                read >> lname;
                read >> qual;
                read >> exp;
                if(id==idc){
                    flag=1;
                 cout << "\nLibrarian Data: ";
			    cout << "\nID: " << id
				<< "\nLibrarian Name: " << lname
				<< "\nLibrarian Qualification: " << qual
				<< "\nLibrarian Experience: " << exp << "yrs"
				<< "\n";
                break;
                }
               

            }
            if (flag==0){
                cout << "\nLibrarian ID Not Found.";
            }

        }
    }



     void updateData() {
        unsigned int vid,flag=0,exp_c;
        string lname_c,qual_c;
        ofstream write;
        ifstream read;
        cout << "\n\nUpdate Vehicle Record";
        write.open("temp.txt", ios::app);
        read.open("librarian.txt");

        if(!read){
            cout << "\nFile could not be found or File could not be created.";
        } else {
            cout << "\nLibrarian ID: ";
            cin >> vid;
            
            while (!read.eof()){
                read >> id;
                read >> lname;
                read >> qual;
                read >> exp;
                if(vid != id){
                    write << id << " " << lname << " " << qual << " " << exp << endl;
                } else {
                cout << "\t\t\t\tUpdate Librarian Record";
	            cout << "\nNew Librarian Name : ";
	            cin >> lname_c;
	            cout << "\nNew Librarian Qualification: ";
	            cin >> qual_c;
	            cout << "\nNew Librarian Work Experience (in years): ";
	            cin >> exp_c;
                    write << id << " " << lname_c << " " << qual_c << " " << exp_c << endl;
                flag++;
                read >> id;
                read >> lname;
                read >> qual;
                read >> exp;
                } 
            }
            if(flag==0){
                    cout << "\nLibrarian ID not found.";
                }
        }

        cout << endl;
        write.close();
        read.close();
        remove("librarian.txt");
        rename("temp.txt", "librarian.txt");
    }



    void deleteData() {
    fstream file, file1;
    int found = 0;
    int CNum;
    cout << "\nDelete Librarian Details." << endl;

    file.open("librarian.txt", ios::in);
    if (!file)
    {
        cout << "\nFile Not Found.";
    }
    else
    {
        cout << "\nLibrarian ID:  ";
        cin >> CNum;
        file1.open("temp.txt", ios::app | ios::out);
        file >> id >> lname >> qual >> exp;
        while (!file.eof())
        {
            if (CNum != id)
            {
                     file1 << id << " " << lname << " " << qual << " " << exp << endl;
            }
            else
            {
                found++;
                cout << "\nLibrarian Record has been deleted successfully.";
            }
              file >> id >> lname >> qual >> exp;
        }
        if (found == 0)
        {
            cout << "\nStudent ID not found.";
        }
        file1.close();
        file.close();
        remove("student.txt");
        rename("temp.txt", "student.txt");
    }
}

};


class Book {
    protected:
    unsigned int id=0,cop,flag404;
    string bname,auth,pub;
    public:

    void gatherData(){
        cout << "\nBook Name: ";
        cin >> bname;
        cout << "\nBook Author: ";
        cin >> auth;
        cout << "\nBook Publication: ";
        cin >> pub;
        cout << "\nNumber of Copies: ";
        cin >> cop;
        id++;
    }

    void write(){
        ofstream write;
        write.open("book.txt",ios::app);
        if(!write){
            cout << "\nFile could not be opened.";
        } else {
            cout << "\nWriting Data to File....";
            write << id << " " << bname << " " << auth << " " << pub << " " << cop << endl;
            cout << "\nData has been exported to file named book.txt";
        }
    }


    void displaydata(){
    fstream file;
	cout << "\nAll Book Data:";
	file.open("book.txt", ios::in);
	if (!file)
		cout << "\n\nFile Opening Error!";
	else {

		file >> id >> bname;
		file >> auth >> pub;
        file >> cop;
		while (!file.eof()) {
            cout << "\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=";
			cout << "\nID: " << id
				<< "\nBook Name: " << bname
				<< "\nAuthor: " << auth
				<< "\nPublication: " << pub
                << "\nNo. of Copies: " << cop
				<< "\n";
                cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n";
        file >> id >> bname;
		file >> auth >> pub;
        file >> cop;
		}
		file.close();
	}
    }


    void specificData(int idc)
    {
        int flag=0;
        fstream read;
        read.open("book.txt",ios::in);
        if(!read){
            cout << "\n\nFile Opening Error!";
        } else {
            while(!read.eof()){
                read >> id;
                read >> bname;
                read >> auth;
                read >> pub;
                read >> cop;
                if(id==idc){
                    flag=1;
                 cout << "\nBook Data: ";
			   cout << "\nID: " << id
				<< "\nBook Name: " << bname
				<< "\nAuthor: " << auth
				<< "\nPublication: " << pub
                << "\nNo. of Copies: " << cop
				<< "\n";
                break;
                }
               

            }
            if (flag==0){
                cout << "\nBook ID Not Found.";
            }

        }
    }



     void updateData() {
        unsigned int vid,cop_c,flag=0;
        string bname_c,auth_c,pub_c;
        ofstream write;
        ifstream read;
        cout << "\n\nUpdate Vehicle Record";
        write.open("temp.txt", ios::app);
        read.open("book.txt");

        if(!read){
            cout << "\nFile could not be found or File could not be created.";
        } else {
            cout << "\nBook ID: ";
            cin >> vid;
            
            while (!read.eof()){
                read >> id;
                read >> bname;
                read >> auth;
                read >> pub;
                read >> cop;
                if(vid != id){
                    write << id << " " << bname << " " << auth << " " << pub << " " << cop << endl;
                } else {
                cout << "\t\t\t\tUpdate Book Record";
	            cout << "\nNew Book Name : ";
	            cin >> bname_c;
	            cout << "\nNew Book Author: ";
	            cin >> auth_c;
	            cout << "\nNew Book Publication : ";
	            cin >> pub_c;
                cout << "\nNew no. of  copies: ";
	            cin >> cop_c;
                    write << id << " " << bname_c << " " << auth_c << " " << pub_c << " " << cop_c << endl;
                flag++;
                read >> id;
                read >> bname;
                read >> auth;
                read >> pub;
                read >> cop;
                } 
            }
            if(flag==0){
                    cout << "\nBook ID not found.";
                }
        }

        cout << endl;
        write.close();
        read.close();
        remove("book.txt");
        rename("temp.txt", "book.txt");
    }



    void deleteData() {
    fstream file, file1;
    int found = 0;
    int CNum;
    cout << "\nDelete Book Details." << endl;

    file.open("book.txt", ios::in);
    if (!file)
    {
        cout << "\nFile Not Found.";
    }
    else
    {
        cout << "\nBook ID:  ";
        cin >> CNum;
        file1.open("temp.txt", ios::app | ios::out);
        file >> id >> bname >> auth >> pub >> cop;
        while (!file.eof())
        {
            if (CNum != id)
            {
                     file1 << id << " " << bname << " " << auth << " " << pub << " " << cop << endl;
            }
            else
            {
                found++;
                cout << "\nStudent Record has been deleted successfully.";
            }
            file >> id >> bname >> auth >> pub >> cop;
        }
        if (found == 0)
        {
            cout << "\nStudent ID not found.";
        }
        file1.close();
        file.close();
        remove("student.txt");
        rename("temp.txt", "student.txt");
    }
}


    int updateBook(int x){

        unsigned int vid,cop_c,flag=0;
        ofstream write;
        ifstream read;
        write.open("temp.txt", ios::app);
        read.open("book.txt");

        if(!read){
            cout << "\nFile could not be found or File could not be created.";
        } else {
            vid = x;
                 read >> id;
                read >> bname;
                read >> auth;
                read >> pub;
                read >> cop;
            while (!read.eof()){
                if(vid != id){
                write << id << " " << bname << " " << auth << " " << pub << " " << cop << endl;
                } else {
                flag=1;
                if(cop==0){
                    write << vid << " " << bname << " " << auth << " " << pub << " " << cop << endl;
                    remove("temp.txt");
                    return 404;
                } else {
                cop--;
                write <<  vid << " " << bname << " " << auth << " " << pub << " " << cop << endl;
                } 
                }
                read >> id;
                read >> bname;
                read >> auth;
                read >> pub;
                read >> cop;
                
            }
            if(flag==0){
                    cout << "\nBook ID not found.";
                }
        }

        cout << endl;
        write.close();
        read.close();
        remove("book.txt");
        rename("temp.txt", "book.txt");
    



}




int updateBookbug(int x){

        unsigned int vid,cop_c,flag=0;
        ofstream write;
        ifstream read;
        write.open("temp.txt", ios::app);
        read.open("book.txt");

        if(!read){
            cout << "\nFile could not be found or File could not be created.";
        } else {
            vid = x;
                 read >> id;
                read >> bname;
                read >> auth;
                read >> pub;
                read >> cop;
            while (!read.eof()){
                if(vid != id){
                write << id << " " << bname << " " << auth << " " << pub << " " << cop << endl;
                } else {
                flag=1;
                cop++;
                write << vid << " " << bname << " " << auth << " " << pub << " " << cop << endl;
                remove("temp.txt");
                return 1234; 
                }
                read >> id;
                read >> bname;
                read >> auth;
                read >> pub;
                read >> cop;
                
            }
            if(flag==0){
                    cout << "\nBook ID not found.";
                }
        }

        cout << endl;
        write.close();
        read.close();
        remove("book.txt");
        rename("temp.txt", "book.txt");
    



}









};



class Student: public Book{
    protected:
    int id=0;
    string sname,dept,grade,div,book1,book2,book3;
    public:

    void gatherData(){
        cout << "\nStudent Name: ";
        cin >> sname;
        cout << "\nStudent Department: ";
        cin >> dept;
        cout << "\nStudent grade: ";
        cin >> grade;
        cout << "\nStudent Division: ";
        cin >> div;
        book1 = "no-book";
        book2 = "no-book";
        book3 = "no-book";
        id++;
    }

    void write(){
        ofstream write;
        write.open("student.txt",ios::app);
        if(!write){
            cout << "\nFile could not be opened.";
        } else {
            cout << "\nWriting Data to File....";
            write << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << "\n";
            cout << "\nData has been exported to file named student.txt";
        }
    }


    void displaydata(){
    fstream file;
	cout << "\nAll Student Data:";
	file.open("student.txt", ios::in);
	if (!file)
		cout << "\n\nFile Opening Error!";
	else {

		file >> id >> sname;
		file >> dept >> grade;
        file >> div >> book1;
        file >> book2 >> book3;
		while (!file.eof()) {
            cout << "\n\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=";
			cout << "\nID: " << id
				<< "\nStudent Name: " << sname
				<< "\nStudent Dept: " << dept
				<< "\nStudent Grade: " << grade
                << "\nStudent Division: " << div
                << "\nBooks Issued: " << book1 << ", " << book2 << ", " << book3
				<< "\n";
                cout << "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n";
        file >> id >> sname;
		file >> dept >> grade;
        file >> div >> book1;
        file >> book2 >> book3;
		}
		file.close();
	}
    }


    void specificData(int idc)
    {
        int flag=0;
        fstream read;
        read.open("student.txt",ios::in);
        if(!read){
            cout << "\n\nFile Opening Error!";
        } else {
            while(!read.eof()){
                read >> id;
                read >> sname;
                read >> dept;
                read >> grade;
                read >> div;
                if(id==idc){
                    flag=1;
                 cout << "\nStudent Data: ";
			    cout << "\nID: " << id
				<< "\nStudent Name: " << sname
				<< "\nStudent Dept: " << dept
				<< "\nStudent Grade: " << grade
                << "\nStudent Division: " << div
				<< "\n";
                break;
                }
               

            }
            if (flag==0){
                cout << "\nStudent ID Not Found.";
            }

        }
    }



     void updateData() {
        unsigned int vid,flag=0;
        string sname_c,dept_c,grade_c,div_c,book;
        ofstream write;
        ifstream read;
        cout << "\n\nUpdate Student Record";
        write.open("temp.txt", ios::app);
        read.open("student.txt");

        if(!read){
            cout << "\nFile could not be found or File could not be created.";
        } else {
            cout << "\nStudent ID: ";
            cin >> vid;
            
            while (!read.eof()){
                read >> id;
                read >> sname;
                read >> dept;
                read >> grade;
                read >> div;
                read >> book1;
                read >> book2;
                read >> book3;
                if(vid != id){
                    write << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                } else {
                cout << "\t\t\t\tUpdate Student Record";
	            cout << "\nNew Student Name : ";
	            cin >> sname_c;
	            cout << "\nNew Student Department: ";
	            cin >> dept_c;
	            cout << "\nNew Student Grade : ";
	            cin >> grade_c;
                cout << "\nNew Student Division : ";
	            cin >> div_c;
               write << id << " " << sname_c << " " << dept_c << " " << grade_c << " " << div_c  << " " << book1 << " " << book2 << " " << book3 << endl;
                flag++;
                read >> id;
                read >> sname;
                read >> dept;
                read >> grade;
                read >> div;
                read >> book1;
                read >> book2;
                read >> book3;
                } 
            }
            if(flag==0){
                    cout << "\nStudent ID not found.";
                }
        }

        cout << endl;
        write.close();
        read.close();
        remove("student.txt");
        rename("temp.txt", "student.txt");
    }



    void deleteData() {
    fstream file, file1;
    int found = 0;
    int CNum;
    cout << "\nDelete Student Details." << endl;

    file.open("student.txt", ios::in);
    if (!file)
    {
        cout << "\nFile Not Found.";
    }
    else
    {
        cout << "\nStudent ID:  ";
        cin >> CNum;
        file1.open("temp.txt", ios::app | ios::out);
        file >> id >> sname >> dept >> grade >> div >> book1 >> book2 >> book3;
        while (!file.eof())
        {
            if (CNum != id)
            {
                     file1 << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
            }
            else
            {
                found++;
                cout << "\nStudent Record has been deleted successfully.";
            }
            file >> id >> sname >> dept >> grade >> div >> book1 >> book2 >> book3;
        }
        if (found == 0)
        {
            cout << "\nStudent ID not found.";
        }
        file1.close();
        file.close();
        remove("student.txt");
        rename("temp.txt", "student.txt");
    }
}

    string assignBookValue(int x){

        int flag=0;
        fstream read;
        read.open("book.txt",ios::in);
        if(!read){
            cout << "\n\nFile Opening Error!";
        } else {
            while(!read.eof()){
                read >> id;
                read >> bname;
                read >> auth;
                read >> pub;
                read >> cop;
                if(id==x){
                flag=1;
                return(bname);
                break;
                }
               

            }
            if (flag==0){
                cout << "\nBook ID Not Found.";
            }

        }
        
    }


    int checkStudent(int idc){
         int flag=0;
        fstream read;
        read.open("student.txt",ios::in);
        if(!read){
            cout << "\n\nFile Opening Error!";
        } else {
            while(!read.eof()){
                read >> id;
                read >> sname;
                read >> dept;
                read >> grade;
                read >> div;
                read >> book1;
                read >> book2;
                read >> book3;
                if(id==idc){
                    flag=1;
                    if(book1.compare("no-book")!=0 && book2.compare("no-book")!=0 && book3.compare("no-book")!=0){
                        return 123;
                        break;
                    }

                    
                }
               

            }
            if (flag==0){
                cout << "\nStudent ID Not Found.";
            }

        }


    }









    int updateStudent(int x,int y){


        unsigned int vid,flag=0;
        string book;
        ofstream write;
        ifstream read;
        write.open("temp.txt", ios::app);
        read.open("student.txt");
        

        if(!read){
            cout << "\nFile could not be found or File could not be created.";
        } else {
            vid = x;
                read >> id;
                read >> sname;
                read >> dept;
                read >> grade;
                read >> div;
                read >> book1;
                read >> book2;
                read >> book3;
            while (!read.eof()){
                if(vid != id){
                    write << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                } else {
                    if(book1.compare("no-book")==0){
                book1 = assignBookValue(y);
                if (flag404!=1){
                write << vid << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                flag=1;
                cout << "\nBook has been Issued.";
                }
                } else if(book2.compare("no-book")==0){
                book2 = assignBookValue(y);
                if (flag404!=1){
                write << vid << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                flag=1;
                cout << "\nBook has been Issued.";
                }
                }else if(book3.compare("no-book")==0){
                book3 = assignBookValue(y);
                if (flag404!=1){
                write << vid << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                flag=1;
                cout << "\nBook has been Issued.";
                }
                } else {
                if (flag404!=1){
                write << vid << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                flag=1;
                cout << "\nStudent already has max number of books.";
                return 123;
                }
                    flag=1;
                }
                }
                read >> id;
                read >> sname;
                read >> dept;
                read >> grade;
                read >> div;
                read >> book1;
                read >> book2;
                read >> book3;
            }
            if(flag==0){
                    cout << "\nStudent ID not found.";
                }
        }

        cout << endl;
        write.close();
        read.close();
        remove("student.txt");
        rename("temp.txt", "student.txt");


    }


    void testBook(string x){
        int bidd,flag;
        flag=0;
        fstream read;
        ofstream write;
        write.open("temp1.txt",ios::app);
        read.open("book.txt",ios::in);
        if(!read){
            cout << "\nFile Opening Error";

        } else{
                read >> bidd;
                read >> bname;
                read >> auth;
                read >> pub;
                read >> cop;
                while(!read.eof()){
                    if(bname.compare(x)==0){
                        flag=1;
                        cop++;
                        write <<  bidd << " " << bname << " " << auth << " " << pub << " " << cop << endl;
                        cout << "\nBook has been returned.";
                    } else {
                         write <<  bidd << " " << bname << " " << auth << " " << pub << " " << cop << endl;
                    }
                read >> bidd;
                read >> bname;
                read >> auth;
                read >> pub;
                read >> cop;
                }

                if(flag==0){
                    cout << "\nStudent does not have a book";
                }





                write.close();
                read.close();
                remove("book.txt");
                rename("temp1.txt","book.txt");


        }

        



    }


    void testStudent(int x)
    {
        int flag=0,choice;
        fstream read;
        ofstream write;
        write.open("temp.txt",ios::app);
        read.open("student.txt",ios::in);
        if(!read){
            cout << "\n\nFile Opening Error!";
        } else {
                read >> id;
                read >> sname;
                read >> dept;
                read >> grade;
                read >> div;
                read >> book1;
                read >> book2;
                read >> book3;
                while(!read.eof()){
                    if(id==x){
                        cout << "\nWhich book would you like to return?\n";
                        cout << book1 << " -----> (1)\n";
                        cout << book2 << " -----> (2)\n";
                        cout << book3 << " -----> (3)\n";
                        cout << "Enter your choice: ";
                        cin >> choice;
                        if(choice==1){
                        if(book1.compare("no-book")!=0){
                        flag=1;
                        testBook(book1);
                        book1 = "no-book";
                        write << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                    } else {
                        flag=1;
                        write << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                        cout << "\nStudent does not have a book.";
                    }
                    
                    
                    
                    }else if(choice==2){
                        if(book2.compare("no-book")!=0){
                        flag=1;
                        testBook(book2);
                        book2 = "no-book";
                        write << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                    }else {
                        flag=1;
                        write << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                        cout << "\nStudent does not have a book.";
                    }
                    
                    
                    
                    }else if(choice==3){
                      if(book3.compare("no-book")!=0){
                        flag=1;
                        testBook(book3);
                        book3 = "no-book";
                        write << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                    }else {
                        flag=1;
                        write << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                        cout << "\nStudent does not have a book.";
                    }
                    
                    
                    
                    } else {
                        cout << "\nInvalid Choice";

                    }
                    } else {
                         write << id << " " << sname << " " << dept << " " << grade << " " << div << " " << book1 << " " << book2 << " " << book3 << endl;
                    }
                read >> id;
                read >> sname;
                read >> dept;
                read >> grade;
                read >> div;
                read >> book1;
                read >> book2;
                read >> book3;
                }

                write.close();
                read.close();
                remove("student.txt");
                rename("temp.txt","student.txt");
            if (flag==0){
                cout << "\nStudent ID Not Found.";
            }

        }
    }


    
    











};




















int main(){
    Student stud;
    Book book;
    Librarian lib;

    int cid,flag=0,sid,bid;
    int loop = 0,a,b,c,d,e,f;
    system("clear");
    while (loop == 0){
        cout << "\n=-=-=-=-=-=TSDL Assignment 3=-=-=-=-=-=";
        cout << "\nBook Database              ----->(1)";
        cout << "\nLibrarian Database         ----->(2)";
        cout << "\nStudent Database           ----->(3)";
        cout << "\nIssue a Book               ----->(4)";
        cout << "\nReturn a Book              ----->(5)";
        cout << "\nExit                       ----->(0)";
        cout << "\nWhat would you like to do?: ";
        cin >> a;
     if (a==1){
        cout << "\n=-=-=-=-=-=Book Database=-=-=-=-=-=";
        cout << "\nAdd Data    ----->(1)";
        cout << "\nView Data   ----->(2)";
        cout << "\nModify Data ----->(3)";
        cout << "\nDelete Data ----->(4)";
        cout << "\nExit        ----->(0)";
        cout << "\nWhat would you like to do?: ";
        cin >> b;
        if(b==1){
            book.gatherData();
            book.write();
        } else if(b==2){
            book.displaydata();
        } else if (b==3){
            book.updateData();
        } else if (b==4){
            book.deleteData();
        }
    } else if(a==2){
        cout << "\n=-=-=-=-=-=Librarian Database=-=-=-=-=-=";
        cout << "\nAdd Data    ----->(1)";
        cout << "\nView Data   ----->(2)";
        cout << "\nModify Data ----->(3)";
        cout << "\nDelete Data ----->(4)";
        cout << "\nExit        ----->(0)";
        cout << "\nWhat would you like to do?: ";
        cin >> b;
        if(b==1){
            lib.gatherData();
            lib.write();
        } else if(b==2){
            lib.displaydata();
        } else if (b==3){
            lib.updateData();
        } else if (b==4){
            lib.deleteData();
        }

    } else if(a==3){
        cout << "\n=-=-=-=-=-=Student Database=-=-=-=-=-=";
        cout << "\nAdd Data    ----->(1)";
        cout << "\nView Data   ----->(2)";
        cout << "\nModify Data ----->(3)";
        cout << "\nDelete Data ----->(4)";
        cout << "\nExit        ----->(0)";
        cout << "\nWhat would you like to do?: ";
        cin >> b;
        if(b==1){
            stud.gatherData();
            stud.write();
        } else if(b==2){
            stud.displaydata();
        } else if (b==3){
            stud.updateData();
        } else if (b==4){
            stud.deleteData();
        }
    } else if(a==4){

        cout << "\nEnter Student ID: ";
        cin >> sid;
        f = stud.checkStudent(sid);
        if(f==123){
             cout << "\nStudent already has max number of books.\n";
        } else { 
        if (f==123)
        cout << "\nBooks Available: ";
        book.displaydata();
        cout << "\nEnter the ID of the book you have to issue: ";
        cin >> bid;
        d = book.updateBook(bid);
        if(d==404){
            cout << "\nOut of copies.";
        } else {
        stud.updateStudent(sid,bid);
        }
        }
    } else if(a==5){
        cout << "\nEnter Student ID: ";
        cin >> sid;
        stud.testStudent(sid);
        }
    else if(a==0){
    break;
    } else {
        cout << "\nInvalid Input. Please Try again";
    }
    }


}   