class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack=[]
        operands=["+","-","/","*"]
        for s in tokens:
            res=0
            if s in operands:
                num1=stack.pop()
                num2=stack.pop()
                
                if s=="+":
                    res=num2+num1
                if s=="-":
                    res=num2-num1
                if s=="*":
                    res=num2*num1
                if s=="/":
                    res=num2/num1
                stack.append(int(res))
            else:
                stack.append(int(s))
                print(stack)
        return int(stack.pop())