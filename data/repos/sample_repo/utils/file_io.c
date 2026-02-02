#include "utils/file_io.h"
#include <stdio.h>

int read_text_file(const char *path, char *buffer, size_t buffer_size) {
    if (!path || !buffer || buffer_size == 0) {
        return -1;
    }
    FILE *fp = fopen(path, "r");
    if (!fp) {
        return -1;
    }
    size_t nread = fread(buffer, 1, buffer_size - 1, fp);
    buffer[nread] = '\0';
    fclose(fp);
    return (int)nread;
}
