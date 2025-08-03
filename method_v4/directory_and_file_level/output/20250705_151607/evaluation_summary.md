# LLM Directory and File Level Evaluation Summary

## Directory and File Level Macro Metrics

- **Number of Processed Proposals**: 5
- **Number of Proposals with at least one correct link (precision > 0)**: 4
- **Macro Precision**: 0.249
- **Macro Recall**: 0.461
- **Macro F1**: 0.272


### 📊 **Proposal #45428**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 16.7% | 15.4% | 1/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/crypto/tls/handshake_server_test.go`
- `src/crypto/tls/handshake_server_tls13.go`
- `src/crypto/tls/handshake_test.go`

**Predicted Files (7):**
- ❌ `src/crypto/tls/defaults_boring.go`
- ❌ `src/crypto/tls/example_test.go`
- ❌ `src/crypto/tls/fipsonly/fipsonly.go`
- ❌ `src/crypto/tls/fipsonly/fipsonly_test.go`
- ❌ `src/crypto/tls/handshake_client_test.go`
- ✅ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/internal/fips140tls/fipstls.go`


### 📊 **Proposal #48801**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`
- `src/cmd/vet/main.go`

**Predicted Files (5):**
- ❌ `src/cmd/vet/doc.go`
- ✅ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/time/format_test.go`
- ❌ `src/time/time_test.go`


### 📊 **Proposal #34875**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 100.0% | 22.2% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/go/doc/comment.go`

**Predicted Files (8):**
- ❌ `src/cmd/doc/doc_test.go`
- ❌ `src/cmd/doc/main.go`
- ✅ `src/go/doc/comment.go`
- ❌ `src/go/doc/comment/comment.go`
- ❌ `src/go/doc/comment/html.go`
- ❌ `src/go/doc/comment/markdown.go`
- ❌ `src/go/doc/comment/print.go`
- ❌ `src/go/doc/comment/std_test.go`


### 📊 **Proposal #32716**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 77.8% | 63.6% | 70.0% | 7/11 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (11):**
- `src/crypto/tls/auth_test.go`
- `src/crypto/tls/cipher_suites.go`
- `src/crypto/tls/common.go`
- `src/crypto/tls/conn.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/crypto/tls/handshake_server_test.go`
- `src/crypto/tls/handshake_server_tls13.go`
- `src/crypto/tls/handshake_test.go`
- `src/crypto/tls/key_agreement.go`
- `src/crypto/tls/prf.go`

**Predicted Files (9):**
- ✅ `src/crypto/tls/auth_test.go`
- ✅ `src/crypto/tls/cipher_suites.go`
- ✅ `src/crypto/tls/common.go`
- ✅ `src/crypto/tls/conn.go`
- ✅ `src/crypto/tls/handshake_server_test.go`
- ✅ `src/crypto/tls/key_agreement.go`
- ✅ `src/crypto/tls/prf.go`
- ❌ `src/crypto/tls/prf_test.go`
- ❌ `src/crypto/tls/tls_test.go`


### 📊 **Proposal #51777**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/netip/netip_test.go`

**Predicted Files (1):**
- ❌ `src/net/netip/netip_pkg_test.go`
