class Solution {
public:
    bool isValid(string s) {
        stack <char> p;
        for(int i=0; i<s.length(); i++){
            if(s[i]=='(' || s[i]=='{' || s[i]=='['){
             p.push(s[i]); 
            }
            else if(s[i]==')' || s[i]=='}' || s[i]==']'){
            if(p.empty())
                return false;
            else if(s[i] == ')' && p.top() != '(')
                return false;
             else if(s[i] == '}' && p.top() != '{')
                return false;
             else if(s[i] == ']' && p.top() != '[')
                return false;
                else
                    p.pop();
            }  
        }
        if(p.empty())
            return true;
        else
            return false;
    }
};
