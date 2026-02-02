#include "core/config.h"
#include "core/errors.h"
#include "net/http_client.h"
#include "storage/cache.h"
#include "storage/db.h"

int main(void) {
    AppConfig cfg = default_config();
    CacheConfig cache_cfg = { cfg.max_connections, 60 };
    DatabaseConfig db_cfg = { "data.db", 0 };
    HttpClientConfig http_cfg = { "localhost", 8080, 1000 };
    char buffer[64];

    if (cache_init(&cache_cfg) != 0) {
        return ERR_IO;
    }
    if (db_open(&db_cfg) <= 0) {
        cache_shutdown();
        return ERR_IO;
    }
    http_get(&http_cfg, "/status", buffer, sizeof(buffer));
    db_close(1);
    cache_shutdown();
    return ERR_OK;
}
