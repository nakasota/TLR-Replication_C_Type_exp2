#ifndef SAMPLE_REPO_STORAGE_DB_H
#define SAMPLE_REPO_STORAGE_DB_H

typedef struct {
    const char *path;
    int flags;
} DatabaseConfig;

int db_open(const DatabaseConfig *config);
int db_close(int handle);

#endif
