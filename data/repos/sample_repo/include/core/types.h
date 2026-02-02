#ifndef SAMPLE_REPO_CORE_TYPES_H
#define SAMPLE_REPO_CORE_TYPES_H

#include <stddef.h>

typedef struct {
    const char *data;
    size_t length;
} BufferView;

typedef struct {
    int id;
    const char *name;
} UserRecord;

#endif
