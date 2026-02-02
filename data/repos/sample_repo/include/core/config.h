#ifndef SAMPLE_REPO_CORE_CONFIG_H
#define SAMPLE_REPO_CORE_CONFIG_H

#define APP_NAME "sample_repo"
#define APP_VERSION_MAJOR 1
#define APP_VERSION_MINOR 2

typedef struct {
    int enable_cache;
    int max_connections;
    int log_level;
} AppConfig;

AppConfig default_config(void);

#endif
