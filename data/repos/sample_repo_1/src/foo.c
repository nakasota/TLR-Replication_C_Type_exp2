#include "../include/foo.h"

static int initialized = 0;

int foo_init(void) {
    initialized = 1;
    return 0;
}

void foo_cleanup(void) {
    initialized = 0;
}
