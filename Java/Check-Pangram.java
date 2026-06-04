class Solution {
    public boolean checkIfPangram(String sentence) {
        boolean[] check= new boolean[26];
        int count=0;
        for(char c : sentence.toCharArray()){
            int index= c-'a';
            if(!check[index]){
                check[index]=true;
                count++;
            }
            if(count==26){
                return true;
            }
        }
        return false;
    }
}