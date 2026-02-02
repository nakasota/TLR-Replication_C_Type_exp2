#include "../include/foo.h"
#include <assert.h>

int main(void) {
    assert(foo_init() == 0);
    foo_cleanup();
    return 0;
}
