class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def rattrape(target:int,pos1,pos2,vi1,vi2:int)->bool:
            time1= (target-pos1)/vi1
            time2=(target-pos2)/vi2 
            if time1<=time2:
                return True
            return False
        stack=[]
        dic={}
        for i in range(len(position)):
            dic[position[i]]=speed[i]
        position.sort()
        stack.append(position[len(position)-1])
        for i in range(1,len(position)):
            j=stack[-1]
            if not rattrape(target,position[len(position)-1-i],j,dic[position[len(position)-1-i]],dic[j]):
                stack.append(position[len(position)-1-i])
        return len(stack)



            