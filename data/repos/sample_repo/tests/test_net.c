#include "net/http_client.h"
#include "net/tcp_client.h"

int test_http_get(void) {
    HttpClientConfig cfg = { "example.com", 80, 1000 };
    char buffer[16];
    return http_get(&cfg, "/ping", buffer, sizeof(buffer)) >= 0;
}

int test_tcp_open_close(void) {
    TcpClientConfig cfg = { "127.0.0.1", 9000 };
    int handle = tcp_open(&cfg);
    if (handle <= 0) {
        return 0;
    }
    return tcp_close(handle) == 0;
}
