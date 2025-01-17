#include <stdbool.h>

bool doesValidArrayExist(int* derived, int derivedSize) {
    
    bool is_valid(int start_value) {
        int current = start_value;
        for (int i = 0; i < derivedSize - 1; i++) {
            current = derived[i] ^ current;
        }
        return (derived[derivedSize - 1] ^ current) == start_value;
    }
    

    return is_valid(0) || is_valid(1);
}
