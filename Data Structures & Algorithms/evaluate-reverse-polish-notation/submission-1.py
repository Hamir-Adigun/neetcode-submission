class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        def sum(self,a:int ,b:int)->int:
            return a+b
        def mula(self,a:int,b:int)->int:
            return a*b
        def sous(self,a:int,b:int)->int:
            return a-b
        def div(self,a:int,b:int)->int:
            return int(a/b)
        dic={
            "+":sum,
            "*":mula,
            "-":sous,
            "/":div
        }
        stack=[]
        for i in tokens:
            if i in dic:
                p=stack.pop()
                j=stack.pop()
                stack.append(str(dic[i](self,int(j),int(p))))
            else:
                stack.append(i)
        return int(stack[0])





        