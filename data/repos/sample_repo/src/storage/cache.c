#include "storage/cache.h"

static int cache_ready = 0;

int cache_init(const CacheConfig *config) {
    if (!config || config->capacity <= 0) {
        return -1;
    }
    cache_ready = 1;
    return 0;
}

int cache_shutdown(void) {
    if (!cache_ready) {
        return -1;
    }
    cache_ready = 0;
    return 0;
}
