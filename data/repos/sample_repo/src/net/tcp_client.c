#include "net/tcp_client.h"

int tcp_open(const TcpClientConfig *config) {
    if (!config || !config->host || config->port <= 0) {
        return -1;
    }
    return config->port;
}

int tcp_close(int handle) {
    if (handle <= 0) {
        return -1;
    }
    return 0;
}
