// LANGUAGE: Java
// AUTHOR: Naman Manjkhola
// GITHUB: https://github.com/NamanManjkhola

console.log('Hello, World!');
class RemoveWhitespaces {    
    public static void main(String[] args) {    
            
        String str1="Remove white spaces";    
            
        //Removes the white spaces  
        str1 = str1.replaceAll(" ", "");    
            
        System.out.println("String after removing all the white spaces : " + str1);    
    }    
}    