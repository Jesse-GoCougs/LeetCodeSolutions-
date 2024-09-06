class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size();
        int m = needle.size();

        for(int i = 0; i <n; i++){
            if(haystack[i] == needle[0]){
                if(n -i >= m && findNeedle(needle, haystack.substr(i, m))){
                    return i;
                }
            }
        }
        return -1;

    }
    bool findNeedle(string needle, string hayStack){
        for(int i =0; i <needle.size(); i++){
            if(hayStack[i] != needle[i]){
                return false;
            }
        } 
        return true;
    }
};