using namespace std::
class Solution {
public:
    bool isIsomorphic(const std::string& s, const std::string& t) {
        if (s.size() != t.size()) {
            return false;
        }

        std::unordered_map<char, char> mapping;
        std::unordered_set<char> unique;

        for (size_t index = 0; index < s.size(); ++index) {
            char char_s = s[index];
            char char_t = t[index];

            if (mapping.find(char_s) != mapping.end()) {
                if (mapping[char_s] != char_t) {
                    return false;
                }
            } else {
                if (unique.find(char_t) != unique.end()) {
                    return false;
                }
                mapping[char_s] = char_t;
                unique.insert(char_t);
            }
        }

        return true;
    }
};