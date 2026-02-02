#include "core/errors.h"

const char *error_message(ErrorCode code) {
    switch (code) {
        case ERR_OK:
            return "ok";
        case ERR_INVALID_ARGUMENT:
            return "invalid argument";
        case ERR_NOT_FOUND:
            return "not found";
        case ERR_IO:
            return "io error";
        case ERR_NO_MEMORY:
            return "no memory";
        default:
            return "unknown error";
    }
}
