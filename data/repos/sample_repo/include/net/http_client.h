#ifndef SAMPLE_REPO_NET_HTTP_CLIENT_H
#define SAMPLE_REPO_NET_HTTP_CLIENT_H

typedef struct {
    const char *host;
    int port;
    int timeout_ms;
} HttpClientConfig;

int http_get(const HttpClientConfig *config, const char *path, char *out_buffer, int out_size);

#endif
