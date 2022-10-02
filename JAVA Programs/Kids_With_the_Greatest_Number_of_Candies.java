// Leetcode - 1431. Kids With the Greatest Number of Candies
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/



class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
         ArrayList<Boolean> list = new ArrayList<Boolean>();
        int max = Integer.MIN_VALUE;
        for(int i=0;i<candies.length;i++){
            if(max<candies[i]){
                max= candies[i];
            }
        }

        for(int i=0;i<candies.length;i++){
            if(candies[i]+extraCandies >= max){
                list.add(true);
            }else{
                list.add(false);
            }
        }
       
        return list;
    }
}