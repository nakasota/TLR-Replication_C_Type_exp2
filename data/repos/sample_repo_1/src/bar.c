#include "../include/bar.h"

static const char* name = "bar";

int bar_compute(int x, int y) {
    return x + y;
}

const char* bar_name(void) {
    return name;
}
