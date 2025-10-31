//leetcode 1773
import java.util.List;
public class Item_Count {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {

        int count =0;
        for(int i=0;i<items.size();i++){
          
                if((ruleKey.equals("type") && ruleValue.equals(items.get(i).get(0)))||
                (ruleKey.equals("color") && ruleValue.equals(items.get(i).get(1))) ||
                (ruleKey.equals("name") && ruleValue.equals(items.get(i).get(2)))){
                    count++;
                }
            
        }

        return count;
        
    }
    
}
