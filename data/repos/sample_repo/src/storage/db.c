#include "storage/db.h"

int db_open(const DatabaseConfig *config) {
    if (!config || !config->path) {
        return -1;
    }
    return 1;
}

int db_close(int handle) {
    if (handle <= 0) {
        return -1;
    }
    return 0;
}
