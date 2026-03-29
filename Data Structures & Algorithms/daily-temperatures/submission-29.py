class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i in range(len(temperatures)-1):
            if temperatures[i]>= temperatures[i+1]:
                stack.append(i)
            else:
                result[i]=1
                while len(stack)!=0 and temperatures[stack[-1]]<temperatures[i+1]:
                    j=stack.pop()
                    result[j]=i+1-j
        while len(stack)>0:
            j=stack.pop()
            result[j]=0
        return result