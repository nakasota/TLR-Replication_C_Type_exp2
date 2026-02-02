#ifndef SAMPLE_REPO_NET_TCP_CLIENT_H
#define SAMPLE_REPO_NET_TCP_CLIENT_H

typedef struct {
    const char *host;
    int port;
} TcpClientConfig;

int tcp_open(const TcpClientConfig *config);
int tcp_close(int handle);

#endif
