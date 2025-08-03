# LLM Multi-Level Evaluation Summary

## Directory-Level Macro Metrics

- **Number of Processed Proposals**: 5
- **Number of Proposals with at least one correct link (precision > 0)**: 4
- **Macro Precision**: 0.533
- **Macro Recall**: 0.700
- **Macro F1**: 0.580

## File-Level Macro Metrics

- **Number of Processed Proposals**: 5
- **Number of Proposals with at least one correct link (precision > 0)**: 4
- **Macro Precision**: 0.505
- **Macro Recall**: 0.439
- **Macro F1**: 0.450

## Function-Level Macro Metrics

- **Number of Processed Proposals**: 5
- **Number of Proposals with at least one correct link (precision > 0)**: 4
- **Macro Precision**: 0.539
- **Macro Recall**: 0.370
- **Macro F1**: 0.419


### 📊 **Proposal #45428 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (3):**
- ✅ `src/crypto/tls`
- ❌ `src/crypto/tls/fipsonly`
- ❌ `src/crypto/tls/internal/fips140tls`


### 📊 **Proposal #45428 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 3/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/crypto/tls/handshake_server_test.go`
- `src/crypto/tls/handshake_server_tls13.go`
- `src/crypto/tls/handshake_test.go`

**Predicted Files (3):**
- ✅ `src/crypto/tls/common.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ✅ `src/crypto/tls/handshake_server.go`


### 📊 **Proposal #45428 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 54.5% | 40.0% | 46.2% | 6/15 |

##### Ground Truth vs Predicted Functions

**File: `src/crypto/tls/common.go`**
- Ground Truth Functions (5): SupportsCertificate, cipherSuites, maxSupportedVersion, mutualVersion, supportedVersions
- Predicted Functions (3):
  - ❌ `defaultConfig`
  - ❌ `minSupportedVersion`
  - ✅ `supportedVersions`

**File: `src/crypto/tls/handshake_client.go`**
- Ground Truth Functions (3): clientHandshake, makeClientHello, pickTLSVersion
- Predicted Functions (2):
  - ✅ `clientHandshake`
  - ✅ `pickTLSVersion`

**File: `src/crypto/tls/handshake_server.go`**
- Ground Truth Functions (3): pickCipherSuite, processClientHello, readClientHello
- Predicted Functions (6):
  - ❌ `cipherSuiteOk`
  - ❌ `handshake`
  - ✅ `pickCipherSuite`
  - ✅ `processClientHello`
  - ✅ `readClientHello`
  - ❌ `serverHandshake`

**File: `src/crypto/tls/handshake_server_test.go`**
- Ground Truth Functions (2): TestVersion, testCrossVersionResume
- Predicted Functions (0):
  - None

**File: `src/crypto/tls/handshake_server_tls13.go`**
- Ground Truth Functions (1): processClientHello
- Predicted Functions (0):
  - None

**File: `src/crypto/tls/handshake_test.go`**
- Ground Truth Functions (1): runMain
- Predicted Functions (0):
  - None


### 📊 **Proposal #48801 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat`
- `src/cmd/vet`

**Predicted Directories (3):**
- ✅ `src/cmd/vet`
- ❌ `src/go/types`
- ❌ `src/time`


### 📊 **Proposal #48801 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`
- `src/cmd/vet/main.go`

**Predicted Files (4):**
- ✅ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/timeformat.go`
- ❌ `src/cmd/vet/vet.go`
- ❌ `src/go/types/stdlib_test.go`


### 📊 **Proposal #48801 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Functions

**File: `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`**
- Ground Truth Functions (2): badFormatAt, run
- Predicted Functions (0):
  - None

**File: `src/cmd/vet/main.go`**
- Ground Truth Functions (1): main
- Predicted Functions (1):
  - ✅ `main`

**File: `src/go/types/stdlib_test.go`**
- Ground Truth Functions (0): None
- Predicted Functions (0):
  - None


### 📊 **Proposal #34875 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/doc`

**Predicted Directories (1):**
- ❌ `src/go/doc/comment`


### 📊 **Proposal #34875 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/go/doc/comment.go`

**Predicted Files (1):**
- ✅ `src/go/doc/comment.go`


### 📊 **Proposal #34875 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Functions

**File: `src/go/doc/comment.go`**
- Ground Truth Functions (2): ToHTML, ToText
- Predicted Functions (2):
  - ✅ `ToHTML`
  - ✅ `ToText`


### 📊 **Proposal #32716 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`


### 📊 **Proposal #32716 (File Level)**

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


### 📊 **Proposal #32716 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.8% | 11.8% | 13.1% | 4/34 |

##### Ground Truth vs Predicted Functions

**File: `src/crypto/tls/auth_test.go`**
- Ground Truth Functions (1): TestSignatureSelection
- Predicted Functions (1):
  - ❌ `TestLegacyTypeAndHash`

**File: `src/crypto/tls/cipher_suites.go`**
- Ground Truth Functions (4): Size, macSHA1, macSHA256, newConstantTimeHash
- Predicted Functions (2):
  - ❌ `CipherSuites`
  - ❌ `InsecureCipherSuites`

**File: `src/crypto/tls/common.go`**
- Ground Truth Functions (3): maxSupportedVersion, mutualVersion, supportedVersions
- Predicted Functions (5):
  - ❌ `VersionName`
  - ❌ `minOrMaxVersion`
  - ❌ `supportedVersion`
  - ✅ `supportedVersions`
  - ❌ `supportedVersionsFromMax`

**File: `src/crypto/tls/conn.go`**
- Ground Truth Functions (4): Write, decrypt, handleRenegotiation, roundUp
- Predicted Functions (6):
  - ❌ `readChangeCipherSpec`
  - ❌ `readRecord`
  - ❌ `readRecordOrCCS`
  - ❌ `writeChangeCipherRecord`
  - ❌ `writeHandshakeRecord`
  - ❌ `writeRecordLocked`

**File: `src/crypto/tls/handshake_client.go`**
- Ground Truth Functions (2): makeClientHello, pickTLSVersion
- Predicted Functions (0):
  - None

**File: `src/crypto/tls/handshake_server.go`**
- Ground Truth Functions (3): pickCipherSuite, processClientHello, readClientHello
- Predicted Functions (0):
  - None

**File: `src/crypto/tls/handshake_server_test.go`**
- Ground Truth Functions (5): TestHandshakeServerAESGCM, TestHandshakeServerRSAAES, TestNoSuiteOverlap, TestRejectBadProtocolVersion, runServerTestTLS13
- Predicted Functions (2):
  - ✅ `TestRejectBadProtocolVersion`
  - ❌ `runServerTestForVersion`

**File: `src/crypto/tls/handshake_server_tls13.go`**
- Ground Truth Functions (1): processClientHello
- Predicted Functions (0):
  - None

**File: `src/crypto/tls/handshake_test.go`**
- Ground Truth Functions (2): checkOpenSSLVersion, runMain
- Predicted Functions (0):
  - None

**File: `src/crypto/tls/key_agreement.go`**
- Ground Truth Functions (1): processClientKeyExchange
- Predicted Functions (3):
  - ❌ `5SHA1Hash`
  - ❌ `a1Hash`
  - ❌ `shForServerKeyExchange`

**File: `src/crypto/tls/prf.go`**
- Ground Truth Functions (8): Write, discardHandshakeBuffer, ekmFromMasterSecret, hashForClientCertificate, keysFromMasterSecret, newFinishedHash, prfAndHashForVersion, prfForVersion
- Predicted Functions (4):
  - ❌ `prf10`
  - ❌ `prf12`
  - ✅ `prfAndHashForVersion`
  - ✅ `prfForVersion`

**File: `src/crypto/tls/prf_test.go`**
- Ground Truth Functions (0): None
- Predicted Functions (2):
  - ❌ `TestKeysFromPreMasterSecret`
  - ❌ `TestSplitPreMasterSecret`

**File: `src/crypto/tls/tls_test.go`**
- Ground Truth Functions (0): None
- Predicted Functions (2):
  - ❌ `stCipherSuites`
  - ❌ `stVersionName`


### 📊 **Proposal #51777 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/netip`

**Predicted Directories (1):**
- ✅ `src/net/netip`


### 📊 **Proposal #51777 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/netip/netip_test.go`

**Predicted Files (1):**
- ❌ `src/net/netip/netip.go`


### 📊 **Proposal #51777 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions

**File: `src/net/netip/netip.go`**
- Ground Truth Functions (0): None
- Predicted Functions (2):
  - ❌ `AddrFrom16`
  - ❌ `IPv6Loopback`

**File: `src/net/netip/netip_test.go`**
- Ground Truth Functions (2): TestAddrWellKnown, TestNoAllocs
- Predicted Functions (0):
  - None
