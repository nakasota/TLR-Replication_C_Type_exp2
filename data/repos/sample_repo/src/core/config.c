#include "core/config.h"

AppConfig default_config(void) {
    AppConfig cfg;
    cfg.enable_cache = 1;
    cfg.max_connections = 16;
    cfg.log_level = 2;
    return cfg;
}
