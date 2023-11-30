class Solution:
    def interpret(self, command: str) -> str:
        size=len(command)
        res=''
        for i in range(size):
            if command[i]=='G':
                res+='G'
            elif command[i]=='(' and command[i+1]==')':
                res+='o'
            elif command[i]=='(' and command[i+1]=='a':
                res+='al'
        return res