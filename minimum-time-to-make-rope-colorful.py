def minCost(self, colors: str, neededTime: List[int]) -> int:
        result=0
        temp_max=0
        for i in range(len(colors)):
            if colors[i]==colors[i-1]:
                result+=min(neededTime[i],temp_max)
                temp_max=max(neededTime[i],temp_max)
            else:
                temp_max=neededTime[i]
        return result
     
