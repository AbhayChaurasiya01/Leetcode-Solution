class Solution {
public:
    bool isValid(string s) {
        stack<char> st;  // stack to store opening brackets
        
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);  // push opening brackets to the stack
            } else {
                // check if the stack is empty or if the closing bracket matches the top of the stack
                if (st.empty()) {
                    return false;
                }
                char top = st.top();
                st.pop();
                if ((c == ')' && top != '(') ||
                    (c == '}' && top != '{') ||
                    (c == ']' && top != '[')) {
                    return false;
                }
            }
        }
        
        // if stack is empty, all opening brackets have been matched, otherwise return false
        return st.empty();
    }
};