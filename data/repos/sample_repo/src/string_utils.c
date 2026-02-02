#include "../include/string_utils.h"
#include <string.h>

int strlen_safe(const char* s) {
    return s ? strlen(s) : 0;
}

void strrev(char* s) {
    if (!s) return;
    int len = strlen(s);
    for (int i = 0; i < len / 2; ++i) {
        char tmp = s[i];
        s[i] = s[len - i - 1];
        s[len - i - 1] = tmp;
    }
}
