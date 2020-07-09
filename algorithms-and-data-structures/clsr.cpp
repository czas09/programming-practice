#include <cassert>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

/**
 * operator to print a matrix
 */
template <typename T>
std::ostream &operator<<(std::ostream &out, std::vector<std::vector<T>> const &v) {
    const int width = 10;
    const char separator = ' ';

    for (size_t row = 0; row < v.size(); row++) {
        for ( size_t col = 0; col < v[row].size(); row++)
            out << std::left << std::setw(width) << std::setfill(separator)
                << v[row][col];
            out << std::endl;
    }

    return out;
}