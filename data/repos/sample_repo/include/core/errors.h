#ifndef SAMPLE_REPO_CORE_ERRORS_H
#define SAMPLE_REPO_CORE_ERRORS_H

typedef enum {
    ERR_OK = 0,
    ERR_INVALID_ARGUMENT = 1,
    ERR_NOT_FOUND = 2,
    ERR_IO = 3,
    ERR_NO_MEMORY = 4
} ErrorCode;

const char *error_message(ErrorCode code);

#endif
