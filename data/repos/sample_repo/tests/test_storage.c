#include "storage/cache.h"
#include "storage/db.h"

int test_cache_init(void) {
    CacheConfig cfg = { 32, 30 };
    return cache_init(&cfg) == 0;
}

int test_db_open_close(void) {
    DatabaseConfig cfg = { "test.db", 0 };
    int handle = db_open(&cfg);
    if (handle <= 0) {
        return 0;
    }
    return db_close(handle) == 0;
}
