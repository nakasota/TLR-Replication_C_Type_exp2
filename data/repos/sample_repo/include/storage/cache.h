#ifndef SAMPLE_REPO_STORAGE_CACHE_H
#define SAMPLE_REPO_STORAGE_CACHE_H

typedef struct {
    int capacity;
    int ttl_seconds;
} CacheConfig;

int cache_init(const CacheConfig *config);
int cache_shutdown(void);

#endif
