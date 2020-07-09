/**
 * @file
 * @brief string pattern search: brute force
 */

#include <iostream>
#ifdef _MSC_VER
#include <string>    /** use this for MS visual C++ */
#else 
#include <cstring>
#endif
#include <vector>

namespace string_search {
    /**
     * find a pattern in a string by comparing thepattern to every substring
     * @param text       any string that might contain the pattern
     * @param pattern    string that we are searching for
     * @return           index where the pattern starts in the text
     * @return           -1 if the pattern was not found.
     */
    int bruteforce(const std::string &text, const std::string &pattern) {
        size_t pat_l = pattern.length();
        size_t txt_l = text.length();
        int index = -1;
        if (pat_l <= txt_l) {
            for (size_t i = 0; i < txt_l - pat_l + 1; i++) {
                std::string s = text.substr(i, pat_l);
                if (s == pattern) {
                    index = i;
                    break;
                }
            }
        }
        return index;
    }
}    //namespace string_search

using string_search::bruteforce;

/** set of test cases */
const std::vector<std::vector<std::string>> test_set = {
    /** {text, pattern, expected output} */
    {"a", "aa", "-1"}, 
    {"a", "a", "0"}, 
    {"ba", "b", "0"}, 
    {"bba", "bb", "0"}, 
    {"bbca", "c", "2"}, 
    {"ab", "b", "1"}
};

int main() {
    for (size_t i = 0; i < test_set.size(); i++) {
        int output = bruteforce(test_set[i][0], test_set[i][1]);
        if (std::to_string(output) == test_set[i][2]){
            std::cout << "success\n";
        } else {
            std::cout << "failure\n";
        }
    }
    return 0;
}