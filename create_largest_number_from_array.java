class Solution {
    public String largestNumber(int[] nums) 
    {
        for(int i=0;i<nums.length-1;i++)
        {
            for(int j=i+1;j<nums.length;j++)
            {
                if((nums[i]+""+nums[j]).compareTo(nums[j]+""+nums[i])<0)
                {
                    int c=nums[i];
                    nums[i]=nums[j];
                    nums[j]=c;
                }

            }
        }

        String s="";
        for(int i=0;i<nums.length;i++)
            s=s+""+nums[i];

        int i=0;
        while(i<s.length()-1)
        {
            if(s.charAt(i)!='0')
                break;
            i++;
        }

        s=s.substring(i);

        return s;
    }
}
