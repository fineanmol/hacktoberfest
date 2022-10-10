import java.util.Scanner;

class make_call{
    double rate;
    int time;
    String code;
    


    }
class local extends make_call{

    double calculations(){
        rate=0.05;
        return rate;

    }
}

class std extends make_call{

   
        double calculations(int time,String code){
            if(time>=6 && time<=22){
                if(code.equals("011")){
                    rate=0.5;
                    return rate;
                }
                else if(code.equals("022")){
                    rate=0.75;
                    return rate;
                }
                else{
                    rate=0.375;
                    return rate;
                }
            }
            else if(time>22 && time<=24 || time>=1 && time<6){
                if(code.equals("011")){
                    rate=0.25;
                    return rate;
                }
                else if(code.equals("022")){
                    rate=0.25;
                    return rate;
                }
                else{
                    rate=0.2;
                    return rate;
                }
            }
            else{
                System.out.println("Wrong Input of Time,please try again entering correct time.");
                return 0;
            }
        
            }
    
}

class CallRate {
    public static void main(String args[]){
    local m=new local();
    std s=new std();
    Scanner sc= new Scanner(System.in);
    double tot_rate=0,cur_rate=0;
    int dur,time;
    String code;

    boolean callEnd=false;
    while(!callEnd){
        System.out.print("1.local \n 2.std \n 3.call end\n");
        int ch=sc.nextInt();
        switch(ch){
        case 1:
            System.out.print("Enter duration of call:");
            dur =sc.nextInt();
            tot_rate=tot_rate+(dur*m.calculations());
            System.out.println("last call price is :"+tot_rate);
            break;
        case 2:
            System.out.println("Enter duration of call:");
            dur =sc.nextInt();
            System.out.println("Enter time when call was made in hrs(from 1 to 24):");
            time =sc.nextInt();
            System.out.println("Enter code:");
            code =sc.next();
            cur_rate=(dur*s.calculations(time,code));
            tot_rate=tot_rate +cur_rate;
            System.out.println("last call price is:"+cur_rate);
            System.out.println("total call price is :"+tot_rate);
            break;
        case 3:
            callEnd=true;
            System.out.println("Final total call price is :"+tot_rate);
            




}
}

}
}