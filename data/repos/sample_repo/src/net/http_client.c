#include "net/http_client.h"

int http_get(const HttpClientConfig *config, const char *path, char *out_buffer, int out_size) {
    if (!config || !path || !out_buffer || out_size <= 0) {
        return -1;
    }
    int written = 0;
    while (path[written] != '\0' && written < out_size - 1) {
        out_buffer[written] = path[written];
        written++;
    }
    out_buffer[written] = '\0';
    return written;
}
