#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    std::vector<std::string> stringMatching(std::vector<std::string>& words) {
        std::vector<std::string> result;
        
        
        std::sort(words.begin(), words.end(), [](const std::string& a, const std::string& b) {
            return a.size() < b.size();
        });
        
        
        for (int i = 0; i < words.size(); ++i) {
            for (int j = i + 1; j < words.size(); ++j) {
                if (words[j].find(words[i]) != std::string::npos) { 
                    result.push_back(words[i]);
                    break; 
                }
            }
        }
        
        return result;
    }
};
