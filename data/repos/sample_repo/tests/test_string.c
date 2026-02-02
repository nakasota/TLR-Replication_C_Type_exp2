#include "../include/string_utils.h"
#include <assert.h>
#include <string.h>

int main() {
    char s[10] = "abc";
    strrev(s);
    assert(strcmp(s, "cba") == 0);
    assert(strlen_safe("hello") == 5);
    return 0;
}
