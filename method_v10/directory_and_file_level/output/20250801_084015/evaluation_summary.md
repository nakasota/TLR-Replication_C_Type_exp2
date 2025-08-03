# LLM Directory and File Level Evaluation Summary

## Directory Level Macro Metrics

- **Number of Processed Proposals**: 231
- **Number of Proposals with at least one correct directory (precision > 0)**: 196
- **Macro Precision**: 0.338
- **Macro Recall**: 0.645
- **Macro F1**: 0.377

## File Level Macro Metrics

- **Number of Processed Proposals**: 231
- **Number of Proposals with at least one correct file (precision > 0)**: 170
- **Macro Precision**: 0.204
- **Macro Recall**: 0.425
- **Macro F1**: 0.230

## File Level within Correct Directories Macro Metrics

- **Number of Processed Proposals**: 231
- **Number of Proposals with at least one correct file (precision > 0)**: 170
- **Macro Precision**: 0.444
- **Macro Recall**: 0.425
- **Macro F1**: 0.385


### 📊 **Proposal #45428**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 3/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/crypto/tls/handshake_server_test.go`
- `src/crypto/tls/handshake_server_tls13.go`
- `src/crypto/tls/handshake_test.go`

**Predicted Files (9):**
- ❌ `src/crypto/tls/alert.go`
- ❌ `src/crypto/tls/auth.go`
- ❌ `src/crypto/tls/cipher_suites.go`
- ✅ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/defaults.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/tls.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 3/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #48801**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat`
- `src/cmd/vet`

**Predicted Directories (3):**
- ❌ `src/time`
- ❌ `src/vet`
- ❌ `test`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`
- `src/cmd/vet/main.go`

**Predicted Files (8):**
- ❌ `src/time/format.go`
- ❌ `src/time/format_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`
- ❌ `src/vet/doc.go`
- ❌ `src/vet/main.go`
- ❌ `src/vet/vet_test.go`
- ❌ `test/issue24801.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #34875**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/doc`

**Predicted Directories (2):**
- ✅ `src/go/doc`
- ❌ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/go/doc/comment.go`

**Predicted Files (4):**
- ✅ `src/go/doc/comment.go`
- ❌ `src/go/doc/doc.go`
- ❌ `src/go/doc/markdown.go`
- ❌ `src/net/http/doc.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/doc`


### 📊 **Proposal #32716**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 72.7% | 72.7% | 72.7% | 8/11 |

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

**Predicted Files (11):**
- ✅ `src/crypto/tls/auth_test.go`
- ✅ `src/crypto/tls/cipher_suites.go`
- ✅ `src/crypto/tls/common.go`
- ✅ `src/crypto/tls/conn.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ✅ `src/crypto/tls/handshake_server_test.go`
- ✅ `src/crypto/tls/key_agreement.go`
- ✅ `src/crypto/tls/prf.go`
- ❌ `src/crypto/tls/prf_test.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/crypto/tls/tls_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 72.7% | 72.7% | 72.7% | 8/11 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #51777**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/netip`

**Predicted Directories (5):**
- ❌ `src`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16317.dir`
- ❌ `src/issue16616.dir`
- ✅ `src/net/netip`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/netip/netip_test.go`

**Predicted Files (10):**
- ❌ `src/issue15920.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16317.dir/a.go`
- ❌ `src/issue16317.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/net.go`
- ❌ `src/net/netip/netip.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/netip`


### 📊 **Proposal #47164**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/log`

**Predicted Directories (1):**
- ✅ `src/log`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/log/log.go`
- `src/log/log_test.go`

**Predicted Files (2):**
- ✅ `src/log/log.go`
- ✅ `src/log/log_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/log`


### 📊 **Proposal #42710**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/hash/maphash`

**Predicted Directories (3):**
- ✅ `src/hash/maphash`
- ❌ `src/runtime/hash/maphash`
- ❌ `src/runtime/maps`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 100.0% | 36.4% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/hash/maphash/maphash.go`
- `src/hash/maphash/maphash_test.go`

**Predicted Files (9):**
- ❌ `map.go`
- ❌ `mapimp.go`
- ❌ `maps.go`
- ❌ `mapsimp.go`
- ✅ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_test.go`
- ❌ `src/runtime/hash/maphash/maphash.go`
- ❌ `src/runtime/maps/map.go`
- ❌ `src/runtime/maps/map_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/hash/maphash`


### 📊 **Proposal #46259**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.7% | 100.0% | 12.5% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (15):**
- ❌ `internal/runtime/sys`
- ❌ `src/cgo/internal/test/testdata/issue24161arg`
- ❌ `src/cgo/internal/test/testdata/issue24161e0`
- ❌ `src/cgo/internal/test/testdata/issue24161e1`
- ❌ `src/cgo/internal/test/testdata/issue24161e2`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16317.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/internal`
- ❌ `src/goos`
- ❌ `src/os/exec`
- ❌ `src/runtime`
- ❌ `src/sys`
- ✅ `src/syscall`
- ❌ `syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.1% | 50.0% | 5.9% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/syscall/exec_freebsd.go`
- `src/syscall/exec_freebsd_test.go`

**Predicted Files (32):**
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `src/cgo/internal/test/testdata/issue24161arg/def.go`
- ❌ `src/cgo/internal/test/testdata/issue24161arg/use.go`
- ❌ `src/cgo/internal/test/testdata/issue24161e0/main.go`
- ❌ `src/cgo/internal/test/testdata/issue24161e1/main.go`
- ❌ `src/cgo/internal/test/testdata/issue24161e2/main.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16317.dir/a.go`
- ❌ `src/fixedbugs/issue16317.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/go/internal/exec.go`
- ❌ `src/go/internal/exec_stub.go`
- ❌ `src/goos/gengoos.go`
- ❌ `src/goos/goos.go`
- ❌ `src/goos/zgoos_freebsd.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_freebsd.go`
- ❌ `src/runtime/sys_freebsd.go`
- ❌ `src/runtime/sys_freebsd_amd64.go`
- ❌ `src/runtime/sys_freebsd_arm.go`
- ❌ `src/runtime/sys_freebsd_arm64.go`
- ❌ `src/runtime/sys_freebsd_riscv64.go`
- ❌ `src/sys/syscall_freebsd.go`
- ❌ `src/syscall/exec_bsd.go`
- ✅ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/syscall_freebsd.go`
- ❌ `src/syscall/syscall_freebsd_test.go`
- ❌ `src/syscall/sysnum_freebsd.go`
- ❌ `syscall/exec_bsd.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall`


### 📊 **Proposal #47257**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 18.2% | 20.0% | 2/11 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (11):**
- `src/cmd/compile/internal/importer`
- `src/cmd/compile/internal/types2`
- `src/cmd/dist`
- `src/cmd/go`
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/modindex`
- `src/cmd/go/internal/work`
- `src/cmd/link`
- `src/go/build`
- `src/go/internal/gcimporter`
- `src/runtime`

**Predicted Directories (9):**
- ✅ `src/cmd/dist`
- ❌ `src/net/http`
- ❌ `src/net/http/cookiejar`
- ❌ `src/net/http/httptest`
- ❌ `src/net/http/httptrace`
- ❌ `src/net/http/httputil`
- ❌ `src/net/http/pprof`
- ✅ `src/runtime`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 11.1% | 10.0% | 2/18 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (18):**
- `src/cmd/compile/internal/importer/gcimporter_test.go`
- `src/cmd/compile/internal/types2/issues_test.go`
- `src/cmd/compile/internal/types2/self_test.go`
- `src/cmd/compile/internal/types2/sizes_test.go`
- `src/cmd/compile/internal/types2/typestring_test.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/modindex/index_test.go`
- `src/cmd/go/internal/modindex/read.go`
- `src/cmd/go/internal/work/action.go`
- `src/cmd/go/internal/work/build.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/link/link_test.go`
- `src/go/build/build.go`
- `src/go/internal/gcimporter/gcimporter_test.go`
- `src/runtime/sys_darwin.go`

**Predicted Files (22):**
- ✅ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/build_test.go`
- ❌ `src/cmd/dist/buildgo.go`
- ❌ `src/cmd/dist/buildruntime.go`
- ❌ `src/cmd/dist/buildtag.go`
- ❌ `src/cmd/dist/buildtag_test.go`
- ✅ `src/cmd/dist/test.go`
- ❌ `src/net/http/client.go`
- ❌ `src/net/http/cookie.go`
- ❌ `src/net/http/cookiejar/jar.go`
- ❌ `src/net/http/httptest/httptest.go`
- ❌ `src/net/http/httptrace/httptrace.go`
- ❌ `src/net/http/httputil/httputil.go`
- ❌ `src/net/http/pprof/pprof.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/responsecontroller.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/runtime/cgo.go`
- ❌ `src/runtime/net.go`
- ❌ `src/syscall/net.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 11.1% | 14.8% | 2/18 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/dist`
- `src/runtime`


### 📊 **Proposal #47216**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (6):**
- ❌ `internal/runtime`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/fixedbugs/issue47201.dir`
- ✅ `src/runtime`
- ❌ `src/runtime/metrics`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 33.3% | 15.4% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/runtime/metrics.go`
- `src/runtime/metrics_test.go`
- `src/runtime/mgc.go`
- `src/runtime/mgclimit.go`
- `src/runtime/mgcscavenge.go`
- `src/runtime/mheap.go`

**Predicted Files (20):**
- ❌ `internal/runtime/metrics.go`
- ❌ `src/fixedbugs/issue16133.dir/a.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16133.dir/main.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/fixedbugs/issue47201.dir/a.go`
- ❌ `src/fixedbugs/issue47201.dir/b.go`
- ✅ `src/runtime/metrics.go`
- ❌ `src/runtime/metrics/description.go`
- ❌ `src/runtime/metrics/description_test.go`
- ❌ `src/runtime/metrics/doc.go`
- ❌ `src/runtime/metrics/example.go`
- ❌ `src/runtime/metrics/histogram.go`
- ❌ `src/runtime/metrics/sample.go`
- ❌ `src/runtime/metrics/value.go`
- ✅ `src/runtime/metrics_test.go`
- ❌ `src/runtime/runtime.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 33.3% | 44.4% | 2/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime`


### 📊 **Proposal #53747**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (5):**
- ❌ `src/compile/internal/base`
- ❌ `src/fixedbugs/issue16133.dir`
- ✅ `src/flag`
- ❌ `src/go/internal/cmdflag`
- ❌ `testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 66.7% | 33.3% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/flag/example_func_test.go`
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (9):**
- ❌ `src/compile/internal/base/flag.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`
- ❌ `src/go/internal/cmdflag/flag.go`
- ❌ `testing/flag_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/flag`


### 📊 **Proposal #34974**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/archive/zip`

**Predicted Directories (2):**
- ✅ `src/archive/zip`
- ❌ `src/compress/zip`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/archive/zip/writer.go`
- `src/archive/zip/writer_test.go`

**Predicted Files (4):**
- ❌ `src/archive/zip/reader.go`
- ✅ `src/archive/zip/writer.go`
- ❌ `src/archive/zip/zip_test.go`
- ❌ `src/compress/zip/zip.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/archive/zip`


### 📊 **Proposal #34626**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (7):**
- ❌ `src/cmd/internal/objfile`
- ❌ `src/issue15646.dir`
- ❌ `src/issue15920.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`
- ❌ `src/runtime`
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.5% | 100.0% | 19.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/benchmark.go`
- `src/testing/benchmark_test.go`

**Predicted Files (19):**
- ❌ `src/cmd/internal/objfile/bench.go`
- ❌ `src/cmd/internal/objfile/bench_test.go`
- ❌ `src/issue15646.dir/a.go`
- ❌ `src/issue15646.dir/b.go`
- ❌ `src/issue15920.dir/a.go`
- ❌ `src/issue15920.dir/b.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/runtime/bench_test.go`
- ❌ `src/testing/bench_test.go`
- ✅ `src/testing/benchmark.go`
- ✅ `src/testing/benchmark_test.go`
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #48530**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (4):**
- ❌ `src`
- ❌ `src/issue16133.dir`
- ✅ `src/net`
- ❌ `src/net/poll`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 25.0% | 12.5% | 1/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/net/net.go`
- `src/net/tcpsock.go`
- `src/net/tcpsock_plan9.go`
- `src/net/tcpsock_posix.go`

**Predicted Files (12):**
- ❌ `src/issue15920.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/net.go`
- ✅ `src/net/net.go`
- ❌ `src/net/poll/splice_linux.go`
- ❌ `src/net/poll/splice_linux_test.go`
- ❌ `src/net/splice_linux.go`
- ❌ `src/net/tcp.go`
- ❌ `src/net/tcpconn.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 25.0% | 25.0% | 1/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #50102**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/archive/tar`

**Predicted Directories (2):**
- ✅ `src/archive/tar`
- ❌ `src/internal/archive`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/archive/tar/common.go`
- `src/archive/tar/stat_unix.go`
- `src/archive/tar/tar_test.go`

**Predicted Files (4):**
- ✅ `src/archive/tar/common.go`
- ✅ `src/archive/tar/stat_unix.go`
- ❌ `src/internal/archive/archive.go`
- ❌ `src/internal/archive/archive_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/archive/tar`


### 📊 **Proposal #38687**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/go/internal/generate`

**Predicted Directories (3):**
- ❌ `src/cmd/go/generate`
- ❌ `src/fixedbugs`
- ❌ `src/fixedbugs/issue16133.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/cmd/go/internal/generate/generate.go`

**Predicted Files (9):**
- ❌ `cmd/`
- ❌ `src/cmd/go/generate/generate.go`
- ❌ `src/cmd/go/generate/generate_test.go`
- ❌ `src/fixedbugs/issue16016.go`
- ❌ `src/fixedbugs/issue16037_run.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #50062**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (3):**
- ❌ `lib/time`
- ❌ `src/runtime`
- ✅ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/time.go`
- `src/time/time_test.go`

**Predicted Files (5):**
- ❌ `lib/time/mkzip.go`
- ❌ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ✅ `src/time/time.go`
- ❌ `src/time/zoneinfo.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #46731**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 22.2% | 17.4% | 2/9 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (9):**
- `src/cmd/cgo`
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/typebits`
- `src/cmd/compile/internal/typecheck`
- `src/cmd/compile/internal/types`
- `src/reflect`
- `src/runtime`
- `test`
- `test/fixedbugs`

**Predicted Directories (14):**
- ❌ `cmd/cgo/internal/test`
- ❌ `cmd/cgo/internal/test/issue41761a`
- ❌ `cmd/compile/internal/gc`
- ❌ `internal/runtime/sys`
- ❌ `runtime/internal/sys`
- ❌ `src/cmd/compile/internal/objabi`
- ❌ `src/cmd/compile/internal/objfile`
- ❌ `src/go/internal/mmap`
- ❌ `src/internal/gccgoimporter/testdata`
- ✅ `src/runtime`
- ❌ `src/runtime/cgo`
- ❌ `src/runtime/internal/sys`
- ❌ `src/runtime/sys`
- ✅ `test`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/18 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (18):**
- `src/cmd/cgo/gcc.go`
- `src/cmd/cgo/out.go`
- `src/cmd/compile/internal/noder/noder.go`
- `src/cmd/compile/internal/noder/reader.go`
- `src/cmd/compile/internal/noder/writer.go`
- `src/cmd/compile/internal/typebits/typebits.go`
- `src/cmd/compile/internal/typecheck/func.go`
- `src/cmd/compile/internal/types/size.go`
- `src/reflect/all_test.go`
- `src/reflect/deepequal.go`
- `src/reflect/nih_test.go`
- `src/reflect/value.go`
- `src/runtime/debuglog.go`
- `src/runtime/malloc.go`
- `src/runtime/mcheckmark.go`
- `src/runtime/mheap.go`
- `test/directive.go`
- `test/fixedbugs/issue40954.go`

**Predicted Files (41):**
- ❌ `cmd/cgo/internal/test/issue41761.go`
- ❌ `cmd/cgo/internal/test/issue41761a/a.go`
- ❌ `cmd/cgo/internal/test/issue41761a/b.go`
- ❌ `cmd/compile/internal/gc/compile.go`
- ❌ `cmd/compile/internal/gc/export.go`
- ❌ `cmd/compile/internal/gc/main.go`
- ❌ `cmd/compile/internal/gc/util.go`
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `runtime/internal/sys/notinheap.go`
- ❌ `src/cmd/compile/internal/objabi/autotype.go`
- ❌ `src/cmd/compile/internal/objfile/elf.go`
- ❌ `src/cmd/compile/internal/objfile/elf_test.go`
- ❌ `src/cmd/compile/internal/objfile/goobj.go`
- ❌ `src/cmd/compile/internal/objfile/goobj_test.go`
- ❌ `src/cmd/compile/internal/objfile/macho.go`
- ❌ `src/cmd/compile/internal/objfile/macho_test.go`
- ❌ `src/cmd/compile/internal/objfile/objfile.go`
- ❌ `src/cmd/compile/internal/objfile/pe.go`
- ❌ `src/cmd/compile/internal/objfile/pe_test.go`
- ❌ `src/cmd/compile/internal/objfile/plan9obj.go`
- ❌ `src/cmd/compile/internal/objfile/plan9obj_test.go`
- ❌ `src/cmd/compile/internal/objfile/reloctype.go`
- ❌ `src/cmd/compile/internal/objfile/reloctype_string.go`
- ❌ `src/cmd/compile/internal/objfile/stack.go`
- ❌ `src/cmd/compile/internal/objfile/symkind.go`
- ❌ `src/cmd/compile/internal/objfile/symkind_string.go`
- ❌ `src/cmd/compile/internal/objfile/symkind_test.go`
- ❌ `src/cmd/compile/internal/objfile/util.go`
- ❌ `src/cmd/compile/internal/objfile/xcoff.go`
- ❌ `src/cmd/compile/internal/objfile/xcoff_test.go`
- ❌ `src/go/internal/mmap/mmap.go`
- ❌ `src/go/internal/mmap/mmap_test.go`
- ❌ `src/internal/gccgoimporter/testdata/notinheap.go`
- ❌ `src/runtime/cgo.go`
- ❌ `src/runtime/cgo/cgo.go`
- ❌ `src/runtime/internal/sys/sys.go`
- ❌ `src/runtime/mmap.go`
- ❌ `src/runtime/runtime.go`
- ❌ `src/runtime/runtime_test.go`
- ❌ `src/runtime/sys/nih.go`
- ❌ `test/notinheap.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/18 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/runtime`
- `test`


### 📊 **Proposal #33184**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/time`

**Predicted Directories (3):**
- ❌ `lib/time`
- ❌ `src`
- ✅ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 66.7% | 40.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/time.go`
- `src/time/tick.go`
- `src/time/tick_test.go`

**Predicted Files (7):**
- ❌ `lib/time/mkzip.go`
- ❌ `src/time.go`
- ✅ `src/time/tick.go`
- ✅ `src/time/tick_test.go`
- ❌ `src/time/ticker.go`
- ❌ `src/time/ticker_test.go`
- ❌ `src/time_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #50489**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/math/big`

**Predicted Directories (2):**
- ❌ `src/math`
- ✅ `src/math/big`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/math/big/ratconv.go`
- `src/math/big/ratconv_test.go`

**Predicted Files (4):**
- ❌ `src/math/big/rat.go`
- ❌ `src/math/big/rat_test.go`
- ❌ `src/math/math.go`
- ❌ `src/math/math_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/math/big`


### 📊 **Proposal #47342**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/dist`
- `src/hash/maphash`

**Predicted Directories (6):**
- ❌ `src/go/internal/hash`
- ✅ `src/hash/maphash`
- ❌ `src/issue15920.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.1% | 50.0% | 10.8% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/cmd/dist/test.go`
- `src/hash/maphash/maphash.go`
- `src/hash/maphash/maphash_purego.go`
- `src/hash/maphash/maphash_runtime.go`

**Predicted Files (33):**
- ❌ `escape_hash_maphash.go`
- ❌ `map.go`
- ❌ `mapimp.go`
- ❌ `maps.go`
- ❌ `mapsimp.go`
- ❌ `src/go/internal/hash/hash.go`
- ✅ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_purego.go`
- ❌ `src/hash/maphash/maphash_test.go`
- ❌ `src/issue15920.dir/a.go`
- ❌ `src/issue15920.dir/b.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/runtime/hash32.go`
- ❌ `src/runtime/hash64.go`
- ❌ `src/runtime/hash_test.go`
- ❌ `src/runtime/map_benchmark_test.go`
- ❌ `src/runtime/map_fast32_noswiss.go`
- ❌ `src/runtime/map_fast32_swiss.go`
- ❌ `src/runtime/map_fast64_noswiss.go`
- ❌ `src/runtime/map_fast64_swiss.go`
- ❌ `src/runtime/map_faststr_noswiss.go`
- ❌ `src/runtime/map_faststr_swiss.go`
- ❌ `src/runtime/map_noswiss.go`
- ❌ `src/runtime/map_noswiss_test.go`
- ❌ `src/runtime/map_swiss.go`
- ❌ `src/runtime/map_swiss_test.go`
- ❌ `src/runtime/map_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 50.0% | 57.1% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/hash/maphash`


### 📊 **Proposal #37255**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os/signal`

**Predicted Directories (4):**
- ❌ `src/context`
- ❌ `src/go/internal/base`
- ✅ `src/os/signal`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 33.3% | 20.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/os/signal/example_unix_test.go`
- `src/os/signal/signal.go`
- `src/os/signal/signal_test.go`

**Predicted Files (7):**
- ❌ `src/context/context.go`
- ❌ `src/context/context_test.go`
- ❌ `src/go/internal/base/signal.go`
- ❌ `src/go/internal/base/signal_notunix.go`
- ❌ `src/go/internal/base/signal_unix.go`
- ✅ `src/os/signal/signal.go`
- ❌ `src/syscall/syscall.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/os/signal`


### 📊 **Proposal #42502**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/runtime`
- `src/runtime/pprof`
- `src/runtime/testdata/testprogcgo`

**Predicted Directories (1):**
- ✅ `src/runtime/pprof`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 9.5% | 16.0% | 2/21 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (21):**
- `src/runtime/cgocall.go`
- `src/runtime/cpuprof.go`
- `src/runtime/os3_plan9.go`
- `src/runtime/os3_solaris.go`
- `src/runtime/os_aix.go`
- `src/runtime/os_darwin.go`
- `src/runtime/os_dragonfly.go`
- `src/runtime/os_freebsd.go`
- `src/runtime/os_linux.go`
- `src/runtime/os_netbsd.go`
- `src/runtime/os_openbsd.go`
- `src/runtime/os_windows.go`
- `src/runtime/pprof/pprof.go`
- `src/runtime/pprof/pprof_test.go`
- `src/runtime/pprof/proto.go`
- `src/runtime/pprof/proto_test.go`
- `src/runtime/pprof/protomem.go`
- `src/runtime/proc.go`
- `src/runtime/signal_unix.go`
- `src/runtime/testdata/testprogcgo/threadpprof.go`
- `src/runtime/testdata/testprogcgo/tracebackctxt.go`

**Predicted Files (4):**
- ❌ `src/runtime/pprof/mprof_test.go`
- ✅ `src/runtime/pprof/pprof.go`
- ✅ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/profile.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 9.5% | 16.0% | 2/21 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime/pprof`


### 📊 **Proposal #42782**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (4):**
- ❌ `interface`
- ❌ `src/issue16616.dir`
- ✅ `src/reflect`
- ❌ `src/reflectlite`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 100.0% | 22.2% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/visiblefields.go`
- `src/reflect/visiblefields_test.go`

**Predicted Files (16):**
- ❌ `interface/struct.go`
- ❌ `reflectmethod1.go`
- ❌ `reflectmethod2.go`
- ❌ `reflectmethod3.go`
- ❌ `reflectmethod4.go`
- ❌ `reflectmethod5.go`
- ❌ `reflectmethod6.go`
- ❌ `reflectmethod7.go`
- ❌ `reflectmethod8.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/reflect/reflect.go`
- ❌ `src/reflect/type.go`
- ✅ `src/reflect/visiblefields.go`
- ✅ `src/reflect/visiblefields_test.go`
- ❌ `src/reflectlite/type.go`
- ❌ `src/reflectlite/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #38248**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 12.5% | 12.5% | 1/8 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (8):**
- `src/cmd/compile/internal/gc`
- `src/cmd/compile/internal/ir`
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/ssagen`
- `src/cmd/internal/obj`
- `src/cmd/internal/obj/wasm`
- `src/cmd/link/internal/wasm`
- `src/syscall/js`

**Predicted Directories (8):**
- ❌ `src/cmd/compile`
- ❌ `src/cmd/compile/internal/wasm`
- ❌ `src/runtime`
- ❌ `src/runtime/wasitest`
- ❌ `src/syscall/execenv`
- ✅ `src/syscall/js`
- ❌ `src/syscall/unix`
- ❌ `wasm`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/10 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (10):**
- `src/cmd/compile/internal/gc/compile.go`
- `src/cmd/compile/internal/ir/sizeof_test.go`
- `src/cmd/compile/internal/noder/noder.go`
- `src/cmd/compile/internal/ssagen/abi.go`
- `src/cmd/internal/obj/objfile.go`
- `src/cmd/internal/obj/plist.go`
- `src/cmd/internal/obj/sym.go`
- `src/cmd/internal/obj/wasm/wasmobj.go`
- `src/cmd/link/internal/wasm/asm.go`
- `src/syscall/js/js_test.go`

**Predicted Files (19):**
- ❌ `src/cmd/compile/compile.go`
- ❌ `src/cmd/compile/internal/wasm/asm.go`
- ❌ `src/cmd/compile/internal/wasm/obj.go`
- ❌ `src/cmd/compile/wasm.go`
- ❌ `src/runtime/runtime.go`
- ❌ `src/runtime/wasitest/host_test.go`
- ❌ `src/runtime/wasitest/nonblock_test.go`
- ❌ `src/runtime/wasitest/tcpecho_test.go`
- ❌ `src/syscall/execenv/execenv_js.go`
- ❌ `src/syscall/js/fs_js.go`
- ❌ `src/syscall/js/net_js.go`
- ❌ `src/syscall/js/syscall_js.go`
- ❌ `src/syscall/unix/at_js.go`
- ❌ `src/syscall/unix/net_js.go`
- ❌ `src/syscall/unix/nonblocking_js.go`
- ❌ `wasm/ssa.go`
- ❌ `wasmexport.go`
- ❌ `wasmexport2.go`
- ❌ `wasmmemsize.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/10 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall/js`


### 📊 **Proposal #46279**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/link/internal/ld`

**Predicted Directories (9):**
- ❌ `internal/runtime/sys`
- ❌ `src/go/internal`
- ❌ `src/internal/unix`
- ❌ `src/runtime`
- ❌ `src/runtime/cgo`
- ❌ `src/runtime/sys`
- ❌ `src/sys`
- ❌ `src/sys/unix`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/link/internal/ld/ld_test.go`
- `src/cmd/link/internal/ld/lib.go`

**Predicted Files (20):**
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `select.go`
- ❌ `src/go/internal/limit.go`
- ❌ `src/go/internal/signal_notunix.go`
- ❌ `src/go/internal/signal_unix.go`
- ❌ `src/internal/unix/unix.go`
- ❌ `src/internal/unix/unix_test.go`
- ❌ `src/runtime/cgo/callbacks.go`
- ❌ `src/runtime/cgo/callbacks_aix.go`
- ❌ `src/runtime/cgo/callbacks_traceback.go`
- ❌ `src/runtime/cgo/cgo.go`
- ❌ `src/runtime/cgo/linux.go`
- ❌ `src/runtime/select.go`
- ❌ `src/runtime/sys/syscall_linux.go`
- ❌ `src/runtime/sys/syscall_linux_test.go`
- ❌ `src/sys/syscall.go`
- ❌ `src/sys/unix/syscall_linux.go`
- ❌ `src/sys/unix/syscall_unix.go`
- ❌ `src/syscall/rlimit.go`
- ❌ `src/syscall/rlimit_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #40724**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 6.7% | 11.5% | 3/45 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (45):**
- `src/cmd/asm`
- `src/cmd/asm/internal/asm`
- `src/cmd/cgo`
- `src/cmd/compile/internal/abi`
- `src/cmd/compile/internal/amd64`
- `src/cmd/compile/internal/arm`
- `src/cmd/compile/internal/arm64`
- `src/cmd/compile/internal/base`
- `src/cmd/compile/internal/gc`
- `src/cmd/compile/internal/ir`
- `src/cmd/compile/internal/liveness`
- `src/cmd/compile/internal/mips`
- `src/cmd/compile/internal/mips64`
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/ppc64`
- `src/cmd/compile/internal/reflectdata`
- `src/cmd/compile/internal/riscv64`
- `src/cmd/compile/internal/s390x`
- `src/cmd/compile/internal/ssa`
- `src/cmd/compile/internal/ssagen`
- `src/cmd/compile/internal/test`
- `src/cmd/compile/internal/walk`
- `src/cmd/compile/internal/wasm`
- `src/cmd/compile/internal/x86`
- `src/cmd/dist`
- `src/cmd/go/internal/work`
- `src/cmd/internal/obj`
- `src/cmd/internal/obj/wasm`
- `src/cmd/internal/obj/x86`
- `src/cmd/internal/objabi`
- `src/cmd/link/internal/ld`
- `src/cmd/link/internal/loadelf`
- `src/cmd/link/internal/loader`
- `src/cmd/link/internal/loadmacho`
- `src/cmd/link/internal/loadpe`
- `src/cmd/link/internal/loadxcoff`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl`
- `src/internal/abi`
- `src/internal/abi/testdata`
- `src/math`
- `src/reflect`
- `src/runtime`
- `src/runtime/cgo`
- `test`
- `test/codegen`

**Predicted Directories (7):**
- ❌ `cmd/compile/internal/abi`
- ❌ `src`
- ✅ `src/cmd/asm`
- ❌ `src/cmd/compile`
- ✅ `src/internal/abi`
- ✅ `src/runtime`
- ❌ `test/abi`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.8% | 1.3% | 2.0% | 2/152 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (152):**
- `src/cmd/asm/internal/asm/asm.go`
- `src/cmd/asm/internal/asm/endtoend_test.go`
- `src/cmd/asm/internal/asm/expr_test.go`
- `src/cmd/asm/internal/asm/line_test.go`
- `src/cmd/asm/internal/asm/operand_test.go`
- `src/cmd/asm/internal/asm/parse.go`
- `src/cmd/asm/internal/asm/pseudo_test.go`
- `src/cmd/asm/main.go`
- `src/cmd/cgo/out.go`
- `src/cmd/compile/internal/abi/abiutils.go`
- `src/cmd/compile/internal/amd64/ssa.go`
- `src/cmd/compile/internal/arm/ssa.go`
- `src/cmd/compile/internal/arm64/ssa.go`
- `src/cmd/compile/internal/base/flag.go`
- `src/cmd/compile/internal/gc/compile.go`
- `src/cmd/compile/internal/gc/main.go`
- `src/cmd/compile/internal/gc/obj.go`
- `src/cmd/compile/internal/ir/expr.go`
- `src/cmd/compile/internal/ir/fmt.go`
- `src/cmd/compile/internal/ir/func.go`
- `src/cmd/compile/internal/ir/sizeof_test.go`
- `src/cmd/compile/internal/liveness/plive.go`
- `src/cmd/compile/internal/mips/ssa.go`
- `src/cmd/compile/internal/mips64/ssa.go`
- `src/cmd/compile/internal/noder/lex.go`
- `src/cmd/compile/internal/ppc64/ssa.go`
- `src/cmd/compile/internal/reflectdata/alg.go`
- `src/cmd/compile/internal/reflectdata/reflect.go`
- `src/cmd/compile/internal/riscv64/ssa.go`
- `src/cmd/compile/internal/s390x/ssa.go`
- `src/cmd/compile/internal/ssa/config.go`
- `src/cmd/compile/internal/ssa/decompose.go`
- `src/cmd/compile/internal/ssa/expand_calls.go`
- `src/cmd/compile/internal/ssa/export_test.go`
- `src/cmd/compile/internal/ssa/func.go`
- `src/cmd/compile/internal/ssa/location.go`
- `src/cmd/compile/internal/ssa/op.go`
- `src/cmd/compile/internal/ssa/regalloc.go`
- `src/cmd/compile/internal/ssa/rewriteAMD64.go`
- `src/cmd/compile/internal/ssa/rewritedec64.go`
- `src/cmd/compile/internal/ssa/stackalloc.go`
- `src/cmd/compile/internal/ssagen/abi.go`
- `src/cmd/compile/internal/ssagen/nowb.go`
- `src/cmd/compile/internal/ssagen/ssa.go`
- `src/cmd/compile/internal/test/clobberdead_test.go`
- `src/cmd/compile/internal/walk/closure.go`
- `src/cmd/compile/internal/walk/expr.go`
- `src/cmd/compile/internal/walk/order.go`
- `src/cmd/compile/internal/wasm/ssa.go`
- `src/cmd/compile/internal/x86/ssa.go`
- `src/cmd/dist/build.go`
- `src/cmd/go/internal/work/gc.go`
- `src/cmd/internal/obj/link.go`
- `src/cmd/internal/obj/plist.go`
- `src/cmd/internal/obj/util.go`
- `src/cmd/internal/obj/wasm/wasmobj.go`
- `src/cmd/internal/obj/x86/obj6.go`
- `src/cmd/internal/objabi/funcid.go`
- `src/cmd/link/internal/ld/deadcode_test.go`
- `src/cmd/link/internal/ld/go.go`
- `src/cmd/link/internal/ld/lib.go`
- `src/cmd/link/internal/ld/macho.go`
- `src/cmd/link/internal/ld/main.go`
- `src/cmd/link/internal/ld/pe.go`
- `src/cmd/link/internal/ld/symtab.go`
- `src/cmd/link/internal/loadelf/ldelf.go`
- `src/cmd/link/internal/loader/loader.go`
- `src/cmd/link/internal/loadmacho/ldmacho.go`
- `src/cmd/link/internal/loadpe/ldpe.go`
- `src/cmd/link/internal/loadxcoff/ldxcoff.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl/asmdecl.go`
- `src/internal/abi/abi.go`
- `src/internal/abi/abi_test.go`
- `src/internal/abi/export_test.go`
- `src/internal/abi/testdata/x.go`
- `src/math/acosh.go`
- `src/math/arith_s390x.go`
- `src/math/asin.go`
- `src/math/asinh.go`
- `src/math/atan.go`
- `src/math/atan2.go`
- `src/math/atanh.go`
- `src/math/cbrt.go`
- `src/math/dim.go`
- `src/math/dim_asm.go`
- `src/math/dim_noasm.go`
- `src/math/erf.go`
- `src/math/exp.go`
- `src/math/exp2_asm.go`
- `src/math/exp2_noasm.go`
- `src/math/exp_asm.go`
- `src/math/exp_noasm.go`
- `src/math/expm1.go`
- `src/math/floor.go`
- `src/math/floor_asm.go`
- `src/math/floor_noasm.go`
- `src/math/frexp.go`
- `src/math/hypot.go`
- `src/math/hypot_asm.go`
- `src/math/hypot_noasm.go`
- `src/math/ldexp.go`
- `src/math/log.go`
- `src/math/log10.go`
- `src/math/log1p.go`
- `src/math/log_asm.go`
- `src/math/log_stub.go`
- `src/math/mod.go`
- `src/math/modf.go`
- `src/math/modf_asm.go`
- `src/math/modf_noasm.go`
- `src/math/pow.go`
- `src/math/remainder.go`
- `src/math/sin.go`
- `src/math/sinh.go`
- `src/math/sqrt.go`
- `src/math/stubs.go`
- `src/math/tan.go`
- `src/math/tanh.go`
- `src/reflect/abi.go`
- `src/reflect/abi_test.go`
- `src/reflect/export_test.go`
- `src/reflect/makefunc.go`
- `src/reflect/type.go`
- `src/reflect/value.go`
- `src/runtime/cgo/callbacks.go`
- `src/runtime/cgocall.go`
- `src/runtime/debug_test.go`
- `src/runtime/debugcall.go`
- `src/runtime/export_debug_test.go`
- `src/runtime/export_test.go`
- `src/runtime/gc_test.go`
- `src/runtime/mbarrier.go`
- `src/runtime/mgc.go`
- `src/runtime/mgcmark.go`
- `src/runtime/mgcscavenge.go`
- `src/runtime/mgcsweep.go`
- `src/runtime/mheap.go`
- `src/runtime/mkduff.go`
- `src/runtime/mkpreempt.go`
- `src/runtime/os_netbsd.go`
- `src/runtime/panic.go`
- `src/runtime/proc.go`
- `src/runtime/stubs.go`
- `src/runtime/stubs_amd64.go`
- `src/runtime/syscall_windows.go`
- `src/runtime/syscall_windows_test.go`
- `src/runtime/traceback.go`
- `src/runtime/traceback_test.go`
- `test/codegen/clobberdead.go`
- `test/codegen/clobberdeadreg.go`
- `test/codegen/structs.go`
- `test/nosplit.go`

**Predicted Files (52):**
- ❌ `cmd/compile/internal/abi/abi.go`
- ❌ `cmd/compile/internal/abi/abi_test.go`
- ❌ `cmd/compile/internal/abi/abiutils.go`
- ❌ `cmd/compile/internal/abi/abiutils_test.go`
- ❌ `cmd/compile/internal/abi/abiutilsaux_test.go`
- ❌ `src/cmd/asm/asm.go`
- ❌ `src/cmd/compile/abi.go`
- ❌ `src/cmd/compile/abi_string.go`
- ❌ `src/cmd/compile/abi_test.go`
- ❌ `src/cmd/compile/asm.go`
- ❌ `src/cmd/compile/compile.go`
- ❌ `src/cmd/compile/internal-abi.md`
- ❌ `src/cmd/compile/ir.go`
- ❌ `src/cmd/compile/objfile.go`
- ❌ `src/cmd/compile/ssa.go`
- ❌ `src/cmd/compile/ssa_test.go`
- ❌ `src/cmd/compile/stack.go`
- ❌ `src/cmd/compile/stack_test.go`
- ✅ `src/internal/abi/abi.go`
- ❌ `src/internal/abi/abi_amd64.go`
- ❌ `src/internal/abi/abi_arm64.go`
- ❌ `src/internal/abi/abi_generic.go`
- ❌ `src/internal/abi/abi_loong64.go`
- ❌ `src/internal/abi/abi_ppc64x.go`
- ❌ `src/internal/abi/abi_riscv64.go`
- ❌ `src/runtime/`
- ❌ `src/runtime/abi_test.go`
- ❌ `src/runtime/cgo.go`
- ❌ `src/runtime/cgo_ppc64x.go`
- ❌ `src/runtime/cgo_sigaction.go`
- ✅ `src/runtime/cgocall.go`
- ❌ `src/runtime/cgocallback.go`
- ❌ `src/runtime/cgocheck.go`
- ❌ `src/runtime/trace.go`
- ❌ `src/runtime/trace_test.go`
- ❌ `test/abi/bad_internal_offsets.go`
- ❌ `test/abi/convF_criteria.go`
- ❌ `test/abi/convT64_criteria.go`
- ❌ `test/abi/defer_aggregate.go`
- ❌ `test/abi/defer_recover_results.go`
- ❌ `test/abi/double_nested_addressed_struct.go`
- ❌ `test/abi/double_nested_struct.go`
- ❌ `test/abi/f_ret_z_not.go`
- ❌ `test/abi/fibish.go`
- ❌ `test/abi/fibish_closure.go`
- ❌ `test/abi/map.go`
- ❌ `test/abi/method_wrapper.go`
- ❌ `test/abi/return_stuff.go`
- ❌ `test/abi/spills3.go`
- ❌ `test/abi/spills4.go`
- ❌ `test/abi/store_reg_args.go`
- ❌ `test/abi/struct_lower_1.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.8% | 1.3% | 2.4% | 2/152 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/cmd/asm`
- `src/internal/abi`
- `src/runtime`


### 📊 **Proposal #51914**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (3):**
- ❌ `src/net/http`
- ❌ `src/net/http/httptest`
- ✅ `src/net/http/httputil`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 50.0% | 14.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/httputil/reverseproxy.go`
- `src/net/http/httputil/reverseproxy_test.go`

**Predicted Files (12):**
- ❌ `issue16133.go`
- ❌ `issue16616.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/httptest/httptest.go`
- ❌ `src/net/http/httptest/recorder.go`
- ❌ `src/net/http/httptest/server.go`
- ❌ `src/net/http/httputil/httptest.go`
- ❌ `src/net/http/httputil/httputil.go`
- ✅ `src/net/http/httputil/reverseproxy.go`
- ❌ `src/net/http/net.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/server.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http/httputil`


### 📊 **Proposal #40481**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 14.3% | 18.2% | 1/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/compile/internal/ir`
- `src/cmd/compile/internal/ssagen`
- `src/cmd/compile/internal/typecheck`
- `src/cmd/compile/internal/walk`
- `src/go/types`
- `src/unsafe`
- `test`

**Predicted Directories (4):**
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/runtime`
- ✅ `src/unsafe`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.0% | 8.3% | 6.2% | 1/12 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (12):**
- `src/cmd/compile/internal/ir/expr.go`
- `src/cmd/compile/internal/ir/fmt.go`
- `src/cmd/compile/internal/ir/op_string.go`
- `src/cmd/compile/internal/ssagen/ssa.go`
- `src/cmd/compile/internal/typecheck/builtin.go`
- `src/cmd/compile/internal/typecheck/func.go`
- `src/cmd/compile/internal/typecheck/typecheck.go`
- `src/cmd/compile/internal/walk/builtin.go`
- `src/cmd/compile/internal/walk/expr.go`
- `src/go/types/builtins.go`
- `src/unsafe/unsafe.go`
- `test/unsafebuiltins.go`

**Predicted Files (20):**
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/elf_test.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/goobj_test.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/macho_test.go`
- ❌ `src/cmd/internal/objfile/objfile.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/pe_test.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/plan9obj_test.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/cmd/internal/objfile/xcoff_test.go`
- ❌ `src/runtime/unsafe.go`
- ✅ `src/unsafe/unsafe.go`
- ❌ `unsafe_slice_data.go`
- ❌ `unsafe_string.go`
- ❌ `unsafe_string_data.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 8.3% | 15.4% | 1/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/unsafe`


### 📊 **Proposal #46552**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/syscall`

**Predicted Directories (6):**
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16317.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/runtime`
- ❌ `src/sys`
- ✅ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 66.7% | 19.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/syscall_windows.go`
- `src/runtime/syscall_windows_test.go`
- `src/syscall/dll_windows.go`

**Predicted Files (18):**
- ❌ `src/fixedbugs/issue16133.dir/a.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16317.dir/a.go`
- ❌ `src/fixedbugs/issue16317.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/runtime/sys_windows.go`
- ✅ `src/runtime/syscall_windows.go`
- ✅ `src/runtime/syscall_windows_test.go`
- ❌ `src/sys/mksyscall.go`
- ❌ `src/sys/syscall.go`
- ❌ `src/sys/syscall_windows.go`
- ❌ `src/syscall/mksyscall.go`
- ❌ `src/syscall/mksyscall_windows.go`
- ❌ `src/syscall/syscall_windows.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 66.7% | 44.4% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/runtime`
- `src/syscall`


### 📊 **Proposal #33136**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (5):**
- ❌ `src/encoding/json`
- ❌ `src/encoding/json/internal/jsonwire`
- ✅ `src/reflect`
- ❌ `src/reflectlite`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.3% | 50.0% | 9.5% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (19):**
- ❌ `reflectmethod1.go`
- ❌ `reflectmethod2.go`
- ❌ `reflectmethod3.go`
- ❌ `reflectmethod4.go`
- ❌ `reflectmethod5.go`
- ❌ `reflectmethod6.go`
- ❌ `reflectmethod7.go`
- ❌ `reflectmethod8.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encode_test.go`
- ❌ `src/encoding/json/internal/jsonwire/decode.go`
- ❌ `src/encoding/json/internal/jsonwire/decode_test.go`
- ❌ `src/reflect/reflect.go`
- ❌ `src/reflect/type.go`
- ✅ `src/reflect/value.go`
- ❌ `src/reflectlite/value.go`
- ❌ `src/runtime/reflect_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #52221**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 20.0% | 33.3% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/crypto/ecdh`
- `src/crypto/ecdsa`
- `src/crypto/elliptic`
- `src/crypto/tls`
- `src/crypto/x509`

**Predicted Directories (1):**
- ✅ `src/crypto/ecdh`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 25.0% | 40.0% | 4/16 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (16):**
- `src/crypto/ecdh/ecdh.go`
- `src/crypto/ecdh/ecdh_test.go`
- `src/crypto/ecdh/nist.go`
- `src/crypto/ecdh/x25519.go`
- `src/crypto/ecdsa/ecdsa.go`
- `src/crypto/elliptic/elliptic.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_client_tls13.go`
- `src/crypto/tls/handshake_server_test.go`
- `src/crypto/tls/handshake_server_tls13.go`
- `src/crypto/tls/key_agreement.go`
- `src/crypto/tls/key_schedule.go`
- `src/crypto/x509/pkcs8.go`
- `src/crypto/x509/pkcs8_test.go`
- `src/crypto/x509/sec1.go`
- `src/crypto/x509/x509.go`

**Predicted Files (4):**
- ✅ `src/crypto/ecdh/ecdh.go`
- ✅ `src/crypto/ecdh/ecdh_test.go`
- ✅ `src/crypto/ecdh/nist.go`
- ✅ `src/crypto/ecdh/x25519.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 25.0% | 40.0% | 4/16 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/ecdh`


### 📊 **Proposal #44853**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 8.3% | 9.5% | 1/12 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (12):**
- `src/cmd/compile/internal/base`
- `src/cmd/compile/internal/gc`
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/pkginit`
- `src/cmd/compile/internal/reflectdata`
- `src/cmd/compile/internal/ssagen`
- `src/cmd/go`
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/work`
- `src/cmd/link/internal/ld`
- `src/runtime`
- `src/syscall`

**Predicted Directories (9):**
- ❌ `cmd/dist: add asan tests in misc/cgo`
- ❌ `internal/runtime/sys`
- ❌ `src/crypto`
- ❌ `src/internal/asan`
- ✅ `src/runtime`
- ❌ `src/runtime/asan`
- ❌ `src/runtime/atomic`
- ❌ `src/runtime/msan`
- ❌ `testsanitizers`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 6.5% | 7.8% | 2/31 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (31):**
- `src/cmd/compile/internal/base/flag.go`
- `src/cmd/compile/internal/gc/main.go`
- `src/cmd/compile/internal/gc/obj.go`
- `src/cmd/compile/internal/noder/import.go`
- `src/cmd/compile/internal/noder/reader.go`
- `src/cmd/compile/internal/pkginit/initAsanGlobals.go`
- `src/cmd/compile/internal/reflectdata/reflect.go`
- `src/cmd/compile/internal/ssagen/ssa.go`
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/work/build.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/go/internal/work/init.go`
- `src/cmd/link/internal/ld/config.go`
- `src/cmd/link/internal/ld/lib.go`
- `src/runtime/asan.go`
- `src/runtime/cgo_sigaction.go`
- `src/runtime/iface.go`
- `src/runtime/malloc.go`
- `src/runtime/mbarrier.go`
- `src/runtime/mgcsweep.go`
- `src/runtime/mheap.go`
- `src/runtime/mprof.go`
- `src/runtime/proc.go`
- `src/runtime/select.go`
- `src/runtime/slice.go`
- `src/runtime/stack.go`
- `src/runtime/string.go`
- `src/runtime/traceback.go`
- `src/syscall/syscall_unix.go`
- `src/syscall/syscall_windows.go`

**Predicted Files (20):**
- ❌ `cmd/dist: add asan tests in misc/cgo/testsanitizers package`
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `src/crypto/asan.go`
- ❌ `src/internal/asan/asan.go`
- ✅ `src/runtime/asan.go`
- ❌ `src/runtime/asan/asan.go`
- ❌ `src/runtime/atomic/atomic.go`
- ❌ `src/runtime/atomic/atomic_test.go`
- ✅ `src/runtime/malloc.go`
- ❌ `src/runtime/msan/msan.go`
- ❌ `testsanitizers/asan_global1_fail.go`
- ❌ `testsanitizers/asan_global2_fail.go`
- ❌ `testsanitizers/asan_global3_fail.go`
- ❌ `testsanitizers/asan_global4_fail.go`
- ❌ `testsanitizers/asan_global5.go`
- ❌ `testsanitizers/asan_test.go`
- ❌ `testsanitizers/asan_unsafe_fail1.go`
- ❌ `testsanitizers/asan_unsafe_fail2.go`
- ❌ `testsanitizers/asan_unsafe_fail3.go`
- ❌ `testsanitizers/asan_useAfterReturn.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 6.5% | 12.1% | 2/31 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime`


### 📊 **Proposal #50599**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 20.0% | 22.2% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/go/internal/vcs`
- `src/cmd/go/internal/work`
- `src/cmd/internal/moddeps`
- `src/go/build`
- `src/os/exec`

**Predicted Directories (4):**
- ✅ `src/os/exec`
- ❌ `src/syscall`
- ❌ `src/syscall/execenv`
- ❌ `src/toolchain`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 16.7% | 19.0% | 2/12 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (12):**
- `src/cmd/go/internal/vcs/vcs.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/internal/moddeps/moddeps_test.go`
- `src/go/build/build.go`
- `src/os/exec/env_test.go`
- `src/os/exec/example_test.go`
- `src/os/exec/exec.go`
- `src/os/exec/exec_linux_test.go`
- `src/os/exec/exec_posix_test.go`
- `src/os/exec/exec_test.go`
- `src/os/exec/exec_windows_test.go`
- `src/os/exec/lp_windows_test.go`

**Predicted Files (9):**
- ✅ `src/os/exec/exec.go`
- ✅ `src/os/exec/exec_test.go`
- ❌ `src/syscall/exec_linux.go`
- ❌ `src/syscall/exec_linux_test.go`
- ❌ `src/syscall/exec_unix.go`
- ❌ `src/syscall/exec_unix_test.go`
- ❌ `src/syscall/execenv/execenv_default.go`
- ❌ `src/syscall/execenv/execenv_windows.go`
- ❌ `src/toolchain/exec.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 16.7% | 28.6% | 2/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/os/exec`


### 📊 **Proposal #42537**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 37.5% | 7.0% | 11.8% | 3/43 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (43):**
- `src/archive/tar`
- `src/archive/zip`
- `src/bytes`
- `src/cmd/doc`
- `src/cmd/fix`
- `src/cmd/go/internal/clean`
- `src/cmd/go/internal/load`
- `src/cmd/vet`
- `src/crypto/ecdsa`
- `src/crypto/tls`
- `src/crypto/x509`
- `src/encoding/asn1`
- `src/encoding/json`
- `src/encoding/pem`
- `src/encoding/xml`
- `src/go/build`
- `src/go/constant`
- `src/go/doc`
- `src/go/importer`
- `src/go/printer`
- `src/go/types`
- `src/html/template`
- `src/mime`
- `src/net`
- `src/net/http`
- `src/net/http/cgi`
- `src/net/http/internal`
- `src/net/mail`
- `src/net/smtp`
- `src/net/textproto`
- `src/net/url`
- `src/os`
- `src/os/exec`
- `src/os/user`
- `src/regexp`
- `src/regexp/syntax`
- `src/runtime`
- `src/runtime/pprof`
- `src/runtime/testdata/testprog`
- `src/strconv`
- `src/strings`
- `src/text/template`
- `test`

**Predicted Directories (8):**
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/modload`
- ✅ `src/mime`
- ✅ `src/strings`
- ❌ `src/test`
- ❌ `src/testing`
- ❌ `src/testing/fstest`
- ✅ `test`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 2.7% | 4.7% | 2/74 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (74):**
- `src/archive/tar/strconv.go`
- `src/archive/tar/writer_test.go`
- `src/archive/zip/writer_test.go`
- `src/bytes/bytes.go`
- `src/bytes/bytes_test.go`
- `src/cmd/doc/dirs.go`
- `src/cmd/doc/pkg.go`
- `src/cmd/fix/typecheck.go`
- `src/cmd/go/internal/clean/clean.go`
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/vet/vet_test.go`
- `src/crypto/ecdsa/ecdsa_test.go`
- `src/crypto/tls/handshake_client_test.go`
- `src/crypto/tls/handshake_test.go`
- `src/crypto/x509/pem_decrypt.go`
- `src/encoding/asn1/common.go`
- `src/encoding/json/tags.go`
- `src/encoding/pem/pem.go`
- `src/encoding/xml/typeinfo.go`
- `src/encoding/xml/xml.go`
- `src/go/build/build.go`
- `src/go/build/build_test.go`
- `src/go/build/read.go`
- `src/go/build/read_test.go`
- `src/go/constant/value_test.go`
- `src/go/doc/headscan.go`
- `src/go/importer/importer_test.go`
- `src/go/printer/comment.go`
- `src/go/printer/nodes.go`
- `src/go/printer/printer.go`
- `src/go/types/eval_test.go`
- `src/html/template/attr.go`
- `src/html/template/js.go`
- `src/html/template/url.go`
- `src/mime/encodedword.go`
- `src/mime/mediatype.go`
- `src/net/http/cgi/child.go`
- `src/net/http/cgi/host.go`
- `src/net/http/cgi/host_test.go`
- `src/net/http/client_test.go`
- `src/net/http/cookie.go`
- `src/net/http/fs.go`
- `src/net/http/internal/chunked.go`
- `src/net/http/main_test.go`
- `src/net/http/request.go`
- `src/net/http/response.go`
- `src/net/http/server.go`
- `src/net/http/transport.go`
- `src/net/mail/message.go`
- `src/net/main_posix_test.go`
- `src/net/main_test.go`
- `src/net/platform_test.go`
- `src/net/smtp/smtp.go`
- `src/net/textproto/reader.go`
- `src/net/url/url.go`
- `src/os/exec/exec.go`
- `src/os/exec/exec_test.go`
- `src/os/os_test.go`
- `src/os/user/cgo_lookup_unix.go`
- `src/os/user/lookup_unix.go`
- `src/regexp/exec_test.go`
- `src/regexp/regexp.go`
- `src/regexp/syntax/parse.go`
- `src/runtime/pprof/pprof_test.go`
- `src/runtime/pprof/proto.go`
- `src/runtime/pprof/proto_test.go`
- `src/runtime/runtime-gdb_test.go`
- `src/runtime/testdata/testprog/numcpu_freebsd.go`
- `src/runtime/testdata/testprog/traceback_ancestors.go`
- `src/strconv/fp_test.go`
- `src/strings/strings.go`
- `src/strings/strings_test.go`
- `src/text/template/option.go`
- `test/zerodivide.go`

**Predicted Files (12):**
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/proxy_test.go`
- ✅ `src/mime/mediatype.go`
- ❌ `src/strings/compare.go`
- ❌ `src/strings/replace.go`
- ✅ `src/strings/strings.go`
- ❌ `src/test/run.go`
- ❌ `src/testing/benchmark.go`
- ❌ `src/testing/benchmark_test.go`
- ❌ `src/testing/fstest/mapfs.go`
- ❌ `src/testing/fstest/mapfs_test.go`
- ❌ `test/run.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 2.7% | 5.1% | 2/74 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/mime`
- `src/strings`
- `test`


### 📊 **Proposal #40995**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 17.6% | 42.9% | 25.0% | 3/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/dist`
- `src/cmd/link/internal/mips64`
- `src/cmd/vendor/golang.org/x/sys/unix`
- `src/cmd/vendor/golang.org/x/sys/windows`
- `src/runtime`
- `src/syscall`
- `src/vendor/golang.org/x/sys/cpu`

**Predicted Directories (17):**
- ✅ `src/cmd/dist`
- ❌ `src/cmd/dist/cmd`
- ❌ `src/compile/internal/abi`
- ❌ `src/compile/internal/mips/mips64`
- ❌ `src/internal/cpu`
- ❌ `src/internal/goos`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`
- ❌ `src/net`
- ❌ `src/os`
- ✅ `src/runtime`
- ❌ `src/runtime/atomic`
- ❌ `src/sys`
- ❌ `src/sys/unix`
- ✅ `src/syscall`
- ❌ `src/syscall/unix`
- ❌ `src/sysinfo`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.8% | 10.5% | 10.7% | 4/38 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (38):**
- `src/cmd/dist/main.go`
- `src/cmd/link/internal/mips64/obj.go`
- `src/cmd/vendor/golang.org/x/sys/unix/sockcmsg_unix_other.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_aix.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_bsd.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin_amd64.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin_arm64.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_dragonfly.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_freebsd.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_netbsd.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_openbsd.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_solaris.go`
- `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
- `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
- `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_dragonfly_amd64.go`
- `src/cmd/vendor/golang.org/x/sys/windows/syscall.go`
- `src/cmd/vendor/golang.org/x/sys/windows/syscall_windows.go`
- `src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`
- `src/runtime/defs_openbsd_mips64.go`
- `src/runtime/mheap.go`
- `src/runtime/os_openbsd.go`
- `src/runtime/os_openbsd_mips64.go`
- `src/runtime/signal_openbsd_mips64.go`
- `src/runtime/stack.go`
- `src/syscall/exec_bsd.go`
- `src/syscall/exec_unix_test.go`
- `src/syscall/syscall_openbsd_mips64.go`
- `src/syscall/zsyscall_openbsd_mips64.go`
- `src/vendor/golang.org/x/sys/cpu/cpu_arm64.go`
- `src/vendor/golang.org/x/sys/cpu/cpu_linux_s390x.go`
- `src/vendor/golang.org/x/sys/cpu/cpu_netbsd_arm64.go`
- `src/vendor/golang.org/x/sys/cpu/cpu_other_mips64x.go`
- `src/vendor/golang.org/x/sys/cpu/cpu_s390x.go`
- `src/vendor/golang.org/x/sys/cpu/cpu_x86.go`
- `src/vendor/golang.org/x/sys/cpu/cpu_zos.go`
- `src/vendor/golang.org/x/sys/cpu/cpu_zos_s390x.go`

**Predicted Files (37):**
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/build_test.go`
- ❌ `src/cmd/dist/buildruntime.go`
- ❌ `src/cmd/dist/cmd/dist.go`
- ❌ `src/cmd/dist/sys_default.go`
- ❌ `src/cmd/dist/sys_windows.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/dist/util.go`
- ❌ `src/compile/internal/abi/abi.go`
- ❌ `src/compile/internal/mips/mips64/galign.go`
- ❌ `src/compile/internal/mips/mips64/ggen.go`
- ❌ `src/compile/internal/mips/mips64/ssa.go`
- ❌ `src/internal/cpu/cpu_mips.go`
- ❌ `src/internal/cpu/cpu_mips64.go`
- ❌ `src/internal/goos/zgoos_openbsd.go`
- ❌ `src/issue16133.dir/a.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16133.dir/main.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/net/cgo_openbsd.go`
- ❌ `src/net/tcpsockopt_openbsd.go`
- ❌ `src/os/dirent_openbsd.go`
- ❌ `src/runtime/atomic/atomic_mips64x.go`
- ✅ `src/runtime/defs_openbsd_mips64.go`
- ✅ `src/runtime/os_openbsd_mips64.go`
- ✅ `src/runtime/signal_openbsd_mips64.go`
- ❌ `src/sys/arch.go`
- ❌ `src/sys/syscall_openbsd_mips64.go`
- ❌ `src/sys/unix/syscall_openbsd_mips64.go`
- ❌ `src/syscall/defs_linux_mips64x.go`
- ✅ `src/syscall/syscall_openbsd_mips64.go`
- ❌ `src/syscall/sysnum_linux_mips64x.go`
- ❌ `src/syscall/unix/at_openbsd.go`
- ❌ `src/syscall/unix/tcsetpgrp_bsd.go`
- ❌ `src/sysinfo/cpuinfo_bsd.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.8% | 10.5% | 15.7% | 4/38 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/cmd/dist`
- `src/runtime`
- `src/syscall`


### 📊 **Proposal #39034**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (4):**
- ❌ `lib/time`
- ❌ `src/fmt`
- ❌ `src/runtime`
- ✅ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/format.go`
- `src/time/format_test.go`

**Predicted Files (7):**
- ❌ `lib/time/mkzip.go`
- ❌ `src/fmt/format.go`
- ❌ `src/fmt/print.go`
- ❌ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #45100**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (2):**
- ✅ `src/net/url`
- ❌ `src/web`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/url/url.go`
- `src/net/url/url_test.go`

**Predicted Files (8):**
- ❌ `issue15646.go`
- ❌ `issue15920.go`
- ❌ `issue16133.go`
- ❌ `issue16317.go`
- ✅ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`
- ❌ `src/web/url.go`
- ❌ `src/web/url_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/url`


### 📊 **Proposal #47005**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (3):**
- ❌ `src/net`
- ✅ `src/net/url`
- ❌ `src/web`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/url/url.go`
- `src/net/url/url_test.go`

**Predicted Files (5):**
- ❌ `src/net/url.go`
- ✅ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`
- ❌ `src/web/url.go`
- ❌ `src/web/url_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/url`


### 📊 **Proposal #53482**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (6):**
- ❌ `interface`
- ❌ `net`
- ❌ `src`
- ✅ `src/net`
- ❌ `src/syscall`
- ❌ `syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 16.7% | 14.3% | 1/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/net/interface_aix.go`
- `src/net/interface_bsd.go`
- `src/net/interface_linux.go`
- `src/net/interface_plan9.go`
- `src/net/interface_solaris.go`
- `src/net/interface_windows.go`

**Predicted Files (8):**
- ❌ `interface/struct.go`
- ❌ `net/interface_linux.go`
- ❌ `src/net.go`
- ❌ `src/net/interface.go`
- ✅ `src/net/interface_linux.go`
- ❌ `src/syscall/netlink_linux.go`
- ❌ `src/syscall/zerrors_linux_amd64.go`
- ❌ `syscall/zerrors_linux_amd64.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 16.7% | 25.0% | 1/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #37112**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/work`
- `src/runtime`
- `src/runtime/metrics`

**Predicted Directories (4):**
- ❌ `internal/runtime`
- ❌ `src/expvar`
- ✅ `src/runtime`
- ✅ `src/runtime/metrics`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 38.5% | 45.5% | 41.7% | 5/11 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (11):**
- `src/cmd/go/internal/work/gc.go`
- `src/runtime/export_test.go`
- `src/runtime/histogram.go`
- `src/runtime/histogram_test.go`
- `src/runtime/metrics.go`
- `src/runtime/metrics/description.go`
- `src/runtime/metrics/sample.go`
- `src/runtime/metrics/value.go`
- `src/runtime/metrics_test.go`
- `src/runtime/mgc.go`
- `src/runtime/mstats.go`

**Predicted Files (13):**
- ❌ `internal/runtime/metrics.go`
- ❌ `src/expvar/expvar.go`
- ❌ `src/expvar/expvar_test.go`
- ✅ `src/runtime/metrics.go`
- ✅ `src/runtime/metrics/description.go`
- ❌ `src/runtime/metrics/description_test.go`
- ❌ `src/runtime/metrics/doc.go`
- ❌ `src/runtime/metrics/example_test.go`
- ❌ `src/runtime/metrics/histogram.go`
- ✅ `src/runtime/metrics/sample.go`
- ✅ `src/runtime/metrics/value.go`
- ✅ `src/runtime/metrics_test.go`
- ❌ `src/runtime/runtime.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 45.5% | 47.6% | 5/11 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/runtime`
- `src/runtime/metrics`


### 📊 **Proposal #46771**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/mime/multipart`

**Predicted Directories (2):**
- ❌ `src/fixedbugs/issue16133.dir`
- ✅ `src/mime/multipart`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 50.0% | 22.2% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/mime/multipart/writer.go`
- `src/mime/multipart/writer_test.go`

**Predicted Files (7):**
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/mime/multipart/formdata.go`
- ❌ `src/mime/multipart/multipart.go`
- ✅ `src/mime/multipart/writer.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/mime/multipart`


### 📊 **Proposal #48424**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/syntax`
- `src/cmd/compile/internal/types2`
- `src/go/internal/gcimporter`
- `src/go/parser`
- `src/go/types`
- `test/typeparam`

**Predicted Directories (3):**
- ❌ `src/maps`
- ❌ `src/types`
- ❌ `typeparam`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/19 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (19):**
- `src/cmd/compile/internal/noder/noder.go`
- `src/cmd/compile/internal/syntax/error_test.go`
- `src/cmd/compile/internal/syntax/parser.go`
- `src/cmd/compile/internal/syntax/parser_test.go`
- `src/cmd/compile/internal/syntax/printer_test.go`
- `src/cmd/compile/internal/types2/check_test.go`
- `src/cmd/compile/internal/types2/decl.go`
- `src/cmd/compile/internal/types2/interface.go`
- `src/cmd/compile/internal/types2/typeparam.go`
- `src/cmd/compile/internal/types2/typestring.go`
- `src/cmd/compile/internal/types2/universe.go`
- `src/go/internal/gcimporter/gcimporter_test.go`
- `src/go/parser/parser.go`
- `src/go/types/decl.go`
- `src/go/types/interface.go`
- `src/go/types/typeparam.go`
- `src/go/types/typestring.go`
- `src/go/types/universe.go`
- `test/typeparam/issue48424.go`

**Predicted Files (6):**
- ❌ `src/maps/maps.go`
- ❌ `src/maps/maps_test.go`
- ❌ `src/types/typeparam.go`
- ❌ `src/types/typeset.go`
- ❌ `src/types/typeset_test.go`
- ❌ `typeparam/issue48424.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/19 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #46485**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 20.0% | 25.0% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/cgo`
- `src/cmd/go/internal/load`
- `src/cmd/gofmt`
- `src/go/internal/srcimporter`
- `src/go/parser`

**Predicted Directories (3):**
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/go/parser`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 14.3% | 12.5% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/cgo/ast.go`
- `src/cmd/go/internal/load/test.go`
- `src/cmd/gofmt/gofmt.go`
- `src/cmd/gofmt/simplify.go`
- `src/go/internal/srcimporter/srcimporter.go`
- `src/go/parser/parser.go`
- `src/go/parser/performance_test.go`

**Predicted Files (9):**
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ✅ `src/go/parser/parser.go`
- ❌ `src/go/parser/parser_test.go`
- ❌ `src/go/parser/resolver.go`
- ❌ `src/go/parser/resolver_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 14.3% | 18.2% | 1/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/parser`


### 📊 **Proposal #34652**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 3/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/html/template`
- `src/text/template`
- `src/text/template/parse`

**Predicted Directories (9):**
- ❌ `src`
- ✅ `src/html/template`
- ❌ `src/issue15646.dir`
- ❌ `src/issue15920.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16317.dir`
- ❌ `src/issue16616.dir`
- ✅ `src/text/template`
- ✅ `src/text/template/parse`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 21.4% | 75.0% | 33.3% | 6/8 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (8):**
- `src/html/template/escape.go`
- `src/html/template/template_test.go`
- `src/text/template/exec.go`
- `src/text/template/parse/lex.go`
- `src/text/template/parse/lex_test.go`
- `src/text/template/parse/node.go`
- `src/text/template/parse/parse.go`
- `src/text/template/parse/parse_test.go`

**Predicted Files (28):**
- ❌ `src/html/template/template.go`
- ✅ `src/html/template/template_test.go`
- ❌ `src/issue15646.dir/a.go`
- ❌ `src/issue15646.dir/b.go`
- ❌ `src/issue15920.dir/a.go`
- ❌ `src/issue15920.dir/b.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16317.dir/a.go`
- ❌ `src/issue16317.dir/b.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/issue229398.go`
- ❌ `src/issue25357.go`
- ❌ `src/issue301493.go`
- ❌ `src/issue311569.go`
- ❌ `src/issue317269.go`
- ❌ `src/issue36911.go`
- ❌ `src/issue38627.go`
- ❌ `src/text/template/parse.go`
- ✅ `src/text/template/parse/lex.go`
- ✅ `src/text/template/parse/lex_test.go`
- ✅ `src/text/template/parse/node.go`
- ✅ `src/text/template/parse/parse.go`
- ✅ `src/text/template/parse/parse_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 75.0% | 75.0% | 6/8 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/html/template`
- `src/text/template`
- `src/text/template/parse`


### 📊 **Proposal #42098**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (2):**
- ❌ `src/os/exec`
- ✅ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/syscall/exec_windows.go`

**Predicted Files (5):**
- ❌ `src/os/exec/exec_windows.go`
- ❌ `src/os/exec/exec_windows_test.go`
- ✅ `src/syscall/exec_windows.go`
- ❌ `src/syscall/syscall_windows.go`
- ❌ `src/syscall/syscall_windows_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall`


### 📊 **Proposal #35998**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/web`
- `src/io/ioutil`
- `src/testing`

**Predicted Directories (2):**
- ✅ `src/io/ioutil`
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 75.0% | 75.0% | 3/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/cmd/go/internal/web/file_test.go`
- `src/io/ioutil/tempfile_test.go`
- `src/testing/testing.go`
- `src/testing/testing_test.go`

**Predicted Files (4):**
- ❌ `src/io/ioutil/tempfile.go`
- ✅ `src/io/ioutil/tempfile_test.go`
- ✅ `src/testing/testing.go`
- ✅ `src/testing/testing_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 75.0% | 75.0% | 3/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/io/ioutil`
- `src/testing`


### 📊 **Proposal #43698**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/embed`
- `src/embed/internal/embedtest`

**Predicted Directories (3):**
- ❌ `interface`
- ❌ `src/cmd/vet`
- ❌ `src/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/embed/embed.go`
- `src/embed/internal/embedtest/embed_test.go`

**Predicted Files (12):**
- ❌ `interface/embed.go`
- ❌ `interface/embed1.go`
- ❌ `interface/embed2.go`
- ❌ `interface/embed3.go`
- ❌ `interface/explicit.go`
- ❌ `src/cmd/vet/doc.go`
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/vet.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/cmd/vet/vetflag.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #51414**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (3):**
- ❌ `lib/time`
- ❌ `src/runtime`
- ✅ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/time.go`
- `src/time/time_test.go`

**Predicted Files (5):**
- ❌ `lib/time/mkzip.go`
- ❌ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ✅ `src/time/time.go`
- ✅ `src/time/time_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #37023**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/runtime/debug`

**Predicted Directories (3):**
- ❌ `internal/runtime/sys`
- ✅ `src/runtime`
- ✅ `src/runtime/debug`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.0% | 50.0% | 37.5% | 3/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/runtime/debug/panic_test.go`
- `src/runtime/error.go`
- `src/runtime/os_plan9.go`
- `src/runtime/panic.go`
- `src/runtime/signal_unix.go`
- `src/runtime/signal_windows.go`

**Predicted Files (10):**
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `recover.go`
- ❌ `src/runtime/debug/garbage.go`
- ❌ `src/runtime/debug/garbage_test.go`
- ✅ `src/runtime/debug/panic_test.go`
- ❌ `src/runtime/debug/stack.go`
- ✅ `src/runtime/panic.go`
- ❌ `src/runtime/runtime.go`
- ❌ `src/runtime/runtime_test.go`
- ✅ `src/runtime/signal_unix.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 37.5% | 50.0% | 42.9% | 3/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/runtime`
- `src/runtime/debug`


### 📊 **Proposal #46258**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.7% | 100.0% | 14.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (13):**
- ❌ `src/fixedbugs/issue15646.dir`
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/internal/base`
- ❌ `src/internal/goos`
- ❌ `src/os`
- ❌ `src/os/exec`
- ❌ `src/os/signal`
- ❌ `src/runtime`
- ❌ `src/sys`
- ✅ `src/syscall`
- ❌ `src/syscall/unix`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.6% | 50.0% | 10.0% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/syscall/exec_freebsd.go`
- `src/syscall/exec_pdeathsig_test.go`
- `src/syscall/syscall_freebsd_test.go`
- `src/syscall/syscall_linux_test.go`

**Predicted Files (36):**
- ❌ `issue47258.go`
- ❌ `src/fixedbugs/issue15646.dir/issue15646.go`
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/go/internal/base/signal.go`
- ❌ `src/go/internal/base/signal_notunix.go`
- ❌ `src/go/internal/base/signal_unix.go`
- ❌ `src/internal/goos/goos_freebsd.go`
- ❌ `src/os/dirent_freebsd.go`
- ❌ `src/os/dirent_test.go`
- ❌ `src/os/dirent_unix.go`
- ❌ `src/os/exec/exec_freebsd.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/exec_unix.go`
- ❌ `src/os/signal/signal_freebsd.go`
- ❌ `src/os/signal/signal_test.go`
- ❌ `src/os/signal/signal_unix.go`
- ❌ `src/runtime/os_freebsd.go`
- ❌ `src/runtime/sys_freebsd.go`
- ❌ `src/runtime/syscall_freebsd.go`
- ❌ `src/sys/syscall_freebsd.go`
- ❌ `src/sys/syscall_freebsd_amd64.go`
- ❌ `src/sys/syscall_freebsd_arm.go`
- ❌ `src/sys/syscall_freebsd_arm64.go`
- ❌ `src/sys/syscall_freebsd_riscv64.go`
- ✅ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/syscall_freebsd.go`
- ✅ `src/syscall/syscall_freebsd_test.go`
- ❌ `src/syscall/unix/at_sysnum_freebsd.go`
- ❌ `src/syscall/unix/at_sysnum_fstatat64_linux.go`
- ❌ `src/syscall/unix/sysnum_freebsd.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 50.0% | 57.1% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall`


### 📊 **Proposal #51430**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/15 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (15):**
- `src/cmd/compile/internal/base`
- `src/cmd/compile/internal/coverage`
- `src/cmd/compile/internal/gc`
- `src/cmd/compile/internal/typecheck`
- `src/cmd/covdata`
- `src/cmd/covdata/testdata`
- `src/cmd/internal/cov`
- `src/internal/coverage/calloc`
- `src/internal/coverage/cformat`
- `src/internal/coverage/cmerge`
- `src/internal/coverage/decodecounter`
- `src/internal/coverage/encodecounter`
- `src/internal/coverage/pods`
- `src/internal/coverage/stringtab`
- `src/internal/coverage/test`

**Predicted Directories (11):**
- ❌ `src/cmd/cover`
- ❌ `src/cmd/cover/testdata/html`
- ❌ `src/cmd/cover/testdata/pkgcfg/a`
- ❌ `src/cmd/cover/testdata/pkgcfg/noFuncsNoTests`
- ❌ `src/cmd/cover/testdata/pkgcfg/yesFuncsNoTests`
- ❌ `src/compile/internal/coverage`
- ❌ `src/internal/coverage`
- ❌ `src/runtime`
- ❌ `src/runtime/coverage`
- ❌ `src/runtime/profile`
- ❌ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/29 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (29):**
- `src/cmd/compile/internal/base/flag.go`
- `src/cmd/compile/internal/coverage/cover.go`
- `src/cmd/compile/internal/gc/main.go`
- `src/cmd/compile/internal/typecheck/builtin.go`
- `src/cmd/compile/internal/typecheck/mkbuiltin.go`
- `src/cmd/compile/internal/typecheck/syms.go`
- `src/cmd/covdata/argsmerge.go`
- `src/cmd/covdata/covdata.go`
- `src/cmd/covdata/dump.go`
- `src/cmd/covdata/merge.go`
- `src/cmd/covdata/metamerge.go`
- `src/cmd/covdata/subtractintersect.go`
- `src/cmd/covdata/testdata/dep.go`
- `src/cmd/covdata/testdata/prog1.go`
- `src/cmd/covdata/testdata/prog2.go`
- `src/cmd/covdata/tool_test.go`
- `src/cmd/internal/cov/mreader.go`
- `src/cmd/internal/cov/readcovdata.go`
- `src/internal/coverage/calloc/batchcounteralloc.go`
- `src/internal/coverage/cformat/fmt_test.go`
- `src/internal/coverage/cformat/format.go`
- `src/internal/coverage/cmerge/merge.go`
- `src/internal/coverage/cmerge/merge_test.go`
- `src/internal/coverage/decodecounter/decodecounterfile.go`
- `src/internal/coverage/encodecounter/encode.go`
- `src/internal/coverage/pods/pods.go`
- `src/internal/coverage/pods/pods_test.go`
- `src/internal/coverage/stringtab/stringtab.go`
- `src/internal/coverage/test/counter_test.go`

**Predicted Files (31):**
- ❌ `src/cmd/cover/cover.go`
- ❌ `src/cmd/cover/cover_test.go`
- ❌ `src/cmd/cover/doc.go`
- ❌ `src/cmd/cover/func.go`
- ❌ `src/cmd/cover/html.go`
- ❌ `src/cmd/cover/pkgname_test.go`
- ❌ `src/cmd/cover/profile.go`
- ❌ `src/cmd/cover/test.go`
- ❌ `src/cmd/cover/testdata/html/html.go`
- ❌ `src/cmd/cover/testdata/html/html_test.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/a/a.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/a/a2.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/a/a_test.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/noFuncsNoTests/nfnt.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/yesFuncsNoTests/yfnt.go`
- ❌ `src/compile/internal/coverage/cover.go`
- ❌ `src/internal/coverage/decode.go`
- ❌ `src/internal/coverage/emit.go`
- ❌ `src/internal/coverage/encode.go`
- ❌ `src/internal/coverage/merge.go`
- ❌ `src/internal/coverage/rtcove.go`
- ❌ `src/internal/coverage/testsupport.go`
- ❌ `src/runtime/coverage/coverage.go`
- ❌ `src/runtime/covercounter.go`
- ❌ `src/runtime/covermeta.go`
- ❌ `src/runtime/profile/merge.go`
- ❌ `src/runtime/profile/profile.go`
- ❌ `src/runtime/profile/proto.go`
- ❌ `src/runtime/profile/prune.go`
- ❌ `src/testing/cover.go`
- ❌ `src/testing/cover_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/29 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #46308**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 100.0% | 22.2% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (8):**
- ❌ `src`
- ✅ `src/crypto/tls`
- ❌ `src/go/internal/crypto/tls`
- ❌ `src/issue15646.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16317.dir`
- ❌ `src/issue16616.dir`
- ❌ `src/testtls`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.7% | 50.0% | 11.8% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/tls_test.go`

**Predicted Files (15):**
- ❌ `src/crypto/tls/tls.go`
- ✅ `src/crypto/tls/tls_test.go`
- ❌ `src/go/internal/crypto/tls/tls.go`
- ❌ `src/issue15646.dir/issue15646.go`
- ❌ `src/issue15920.go`
- ❌ `src/issue16133.dir/a.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16317.dir/a.go`
- ❌ `src/issue16317.dir/b.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/testtls/tls.go`
- ❌ `src/testtls/tls_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #37033**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/link/internal/ld`
- `src/runtime/cgo`

**Predicted Directories (3):**
- ❌ `src/go/internal/modload`
- ❌ `src/runtime`
- ✅ `src/runtime/cgo`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 66.7% | 28.6% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/link/internal/ld/lib.go`
- `src/runtime/cgo/handle.go`
- `src/runtime/cgo/handle_test.go`

**Predicted Files (11):**
- ❌ `runtime.go`
- ❌ `src/go/internal/modload/build.go`
- ❌ `src/go/internal/modload/import.go`
- ❌ `src/go/internal/modload/load.go`
- ❌ `src/runtime/cgo.go`
- ❌ `src/runtime/cgo/cgo.go`
- ✅ `src/runtime/cgo/handle.go`
- ✅ `src/runtime/cgo/handle_test.go`
- ❌ `src/runtime/cgo/runtime.go`
- ❌ `src/runtime/cgocallback.go`
- ❌ `src/runtime/cgocheck.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime/cgo`


### 📊 **Proposal #51766**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/netip`

**Predicted Directories (2):**
- ❌ `src/net`
- ✅ `src/net/netip`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/netip/netip_test.go`

**Predicted Files (3):**
- ❌ `src/net/net.go`
- ❌ `src/net/netip/addr.go`
- ❌ `src/net/netip/netip.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/netip`


### 📊 **Proposal #51684**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/regexp/syntax`

**Predicted Directories (5):**
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/regexp`
- ✅ `src/regexp/syntax`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 100.0% | 20.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/regexp/syntax/parse.go`

**Predicted Files (9):**
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/regexp/regexp.go`
- ✅ `src/regexp/syntax/parse.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/regexp/syntax`


### 📊 **Proposal #51896**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/unicode/utf16`

**Predicted Directories (3):**
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`
- ✅ `src/unicode/utf16`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 100.0% | 30.8% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/unicode/utf16/utf16.go`
- `src/unicode/utf16/utf16_test.go`

**Predicted Files (11):**
- ❌ `append.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ✅ `src/unicode/utf16/utf16.go`
- ✅ `src/unicode/utf16/utf16_test.go`
- ❌ `utf.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/unicode/utf16`


### 📊 **Proposal #42088**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/run`
- `src/cmd/go/internal/work`

**Predicted Directories (0):**

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/run/run.go`
- `src/cmd/go/internal/work/build.go`

**Predicted Files (0):**

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #19367**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (2):**
- ✅ `src/runtime`
- ❌ `src/unsafe`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/runtime/checkptr.go`
- `src/runtime/select.go`

**Predicted Files (7):**
- ❌ `src/runtime/slice.go`
- ❌ `src/runtime/slice_test.go`
- ❌ `src/runtime/unsafe.go`
- ❌ `src/unsafe/unsafe.go`
- ❌ `unsafe_slice_data.go`
- ❌ `unsafe_string.go`
- ❌ `unsafe_string_data.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime`


### 📊 **Proposal #37168**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/rc4`
- `src/image`

**Predicted Directories (19):**
- ❌ `src/crypto/aes`
- ❌ `src/crypto/cipher`
- ❌ `src/crypto/des`
- ❌ `src/crypto/dsa`
- ❌ `src/crypto/ecdsa`
- ❌ `src/crypto/ed25519`
- ❌ `src/crypto/elliptic`
- ❌ `src/crypto/hmac`
- ❌ `src/crypto/rsa`
- ❌ `src/crypto/sha1`
- ❌ `src/crypto/sha256`
- ❌ `src/crypto/sha512`
- ❌ `src/math/big`
- ❌ `src/math/big/internal/asmgen`
- ❌ `vendor/golang.org/x/crypto/chacha20`
- ❌ `vendor/golang.org/x/crypto/chacha20poly1305`
- ❌ `vendor/golang.org/x/crypto/cryptobyte`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/asn1`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/rc4/rc4.go`
- `src/crypto/rc4/rc4_test.go`
- `src/image/image_test.go`

**Predicted Files (52):**
- ❌ `src/crypto/aes/aes.go`
- ❌ `src/crypto/cipher/cbc.go`
- ❌ `src/crypto/cipher/ctr.go`
- ❌ `src/crypto/cipher/gcm.go`
- ❌ `src/crypto/des/block.go`
- ❌ `src/crypto/dsa/dsa.go`
- ❌ `src/crypto/ecdsa/ecdsa.go`
- ❌ `src/crypto/ed25519/ed25519.go`
- ❌ `src/crypto/elliptic/elliptic.go`
- ❌ `src/crypto/hmac/hmac.go`
- ❌ `src/crypto/rsa/rsa.go`
- ❌ `src/crypto/sha1/sha1.go`
- ❌ `src/crypto/sha256/sha256.go`
- ❌ `src/crypto/sha512/sha512.go`
- ❌ `src/math/big/arith_amd64.go`
- ❌ `src/math/big/float.go`
- ❌ `src/math/big/float_test.go`
- ❌ `src/math/big/int.go`
- ❌ `src/math/big/int_test.go`
- ❌ `src/math/big/internal/asmgen/amd64.go`
- ❌ `src/math/big/internal/asmgen/arm.go`
- ❌ `src/math/big/internal/asmgen/arm64.go`
- ❌ `src/math/big/internal/asmgen/mips.go`
- ❌ `src/math/big/internal/asmgen/mips64.go`
- ❌ `src/math/big/internal/asmgen/ppc64.go`
- ❌ `src/math/big/internal/asmgen/riscv64.go`
- ❌ `src/math/big/internal/asmgen/s390x.go`
- ❌ `src/math/big/nat.go`
- ❌ `src/math/big/nat_test.go`
- ❌ `src/math/big/rat.go`
- ❌ `src/math/big/rat_test.go`
- ❌ `src/math/big/sqrt.go`
- ❌ `src/math/big/sqrt_test.go`
- ❌ `vendor/golang.org/x/crypto/chacha20/chacha_arm64.go`
- ❌ `vendor/golang.org/x/crypto/chacha20/chacha_generic.go`
- ❌ `vendor/golang.org/x/crypto/chacha20/chacha_noasm.go`
- ❌ `vendor/golang.org/x/crypto/chacha20/chacha_ppc64x.go`
- ❌ `vendor/golang.org/x/crypto/chacha20/chacha_s390x.go`
- ❌ `vendor/golang.org/x/crypto/chacha20poly1305/chacha20poly1305.go`
- ❌ `vendor/golang.org/x/crypto/chacha20poly1305/chacha20poly1305_amd64.go`
- ❌ `vendor/golang.org/x/crypto/chacha20poly1305/chacha20poly1305_generic.go`
- ❌ `vendor/golang.org/x/crypto/chacha20poly1305/chacha20poly1305_noasm.go`
- ❌ `vendor/golang.org/x/crypto/chacha20poly1305/xchacha20poly1305.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/asn1.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/asn1/asn1.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/builder.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/string.go`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305/mac_noasm.go`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305/poly1305.go`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305/sum_asm.go`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305/sum_generic.go`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305/sum_s390x.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #29062**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/test`
- `src/cmd/objdump`
- `src/internal/testenv`

**Predicted Directories (1):**
- ❌ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/test/test.go`
- `src/cmd/objdump/objdump_test.go`
- `src/internal/testenv/testenv.go`

**Predicted Files (2):**
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #43823**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (4):**
- ❌ `src`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 100.0% | 16.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/time/format.go`

**Predicted Files (11):**
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/time.go`
- ✅ `src/time/format.go`
- ❌ `src/time/format_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`
- ❌ `src/time_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #48157**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/internal/fuzz`
- `src/internal/testenv`
- `src/runtime`

**Predicted Directories (2):**
- ❌ `src/cmd/go`
- ❌ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/internal/fuzz/minimize_test.go`
- `src/internal/fuzz/worker.go`
- `src/internal/fuzz/worker_test.go`
- `src/internal/testenv/testenv.go`
- `src/runtime/crash_test.go`
- `src/runtime/runtime-gdb_test.go`

**Predicted Files (4):**
- ❌ `src/cmd/go/test.go`
- ❌ `src/cmd/go/test_test.go`
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #32779**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/json`

**Predicted Directories (3):**
- ❌ `src/dist`
- ❌ `src/encoding`
- ✅ `src/encoding/json`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.7% | 33.3% | 11.1% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/encoding/json/decode.go`
- `src/encoding/json/stream.go`
- `src/encoding/json/stream_test.go`

**Predicted Files (15):**
- ❌ `src/dist/testjson.go`
- ❌ `src/dist/testjson_test.go`
- ❌ `src/encoding/json`
- ✅ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ❌ `src/encoding/json/decoder.go`
- ❌ `src/encoding/json/decoder_test.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encode_test.go`
- ❌ `src/encoding/json/encoder.go`
- ❌ `src/encoding/json/encoder_test.go`
- ❌ `src/encoding/json/internal.go`
- ❌ `src/encoding/json/json.go`
- ❌ `src/encoding/json/marshal.go`
- ❌ `src/encoding/json/unmarshal.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 33.3% | 13.3% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/json`


### 📊 **Proposal #46131**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (7):**
- ❌ `src/fixedbugs/issue47131.dir`
- ✅ `src/reflect`
- ❌ `src/runtime`
- ❌ `src/runtime/maps`
- ❌ `src/sync`
- ❌ `src/types`
- ❌ `test`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/reflect/all_test.go`

**Predicted Files (23):**
- ❌ `map.go`
- ❌ `mapimp.go`
- ❌ `maps.go`
- ❌ `mapsimp.go`
- ❌ `src/fixedbugs/issue47131.dir/a.go`
- ❌ `src/fixedbugs/issue47131.dir/b.go`
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`
- ❌ `src/reflect/map_noswiss.go`
- ❌ `src/reflect/map_noswiss_test.go`
- ❌ `src/reflect/map_swiss.go`
- ❌ `src/reflect/map_swiss_test.go`
- ❌ `src/reflect/reflect.go`
- ❌ `src/runtime/map.go`
- ❌ `src/runtime/map_benchmark_test.go`
- ❌ `src/runtime/map_test.go`
- ❌ `src/runtime/maps/map.go`
- ❌ `src/runtime/maps/map_test.go`
- ❌ `src/sync/map.go`
- ❌ `src/sync/map_bench_test.go`
- ❌ `src/sync/map_test.go`
- ❌ `src/types/map.go`
- ❌ `test/map.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #51225**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/compile/internal/base`
- `src/cmd/compile/internal/noder`
- `src/cmd/go/internal/work`

**Predicted Directories (10):**
- ❌ `cmd/compile`
- ❌ `cmd/compile/internal/importer`
- ❌ `src/cmd/compile`
- ❌ `src/cmd/compile/internal`
- ❌ `src/cmd/compile/internal/objabi`
- ❌ `src/cmd/go`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/build`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/base/flag.go`
- `src/cmd/compile/internal/noder/import.go`
- `src/cmd/go/internal/work/gc.go`

**Predicted Files (25):**
- ❌ `cmd/compile/compile.go`
- ❌ `cmd/compile/internal/importer/gcimporter.go`
- ❌ `cmd/compile/internal/importer/gcimporter_test.go`
- ❌ `import.go`
- ❌ `import1.go`
- ❌ `import2.go`
- ❌ `import4.go`
- ❌ `import5.go`
- ❌ `import6.go`
- ❌ `src/cmd/compile/compile.go`
- ❌ `src/cmd/compile/internal/flag.go`
- ❌ `src/cmd/compile/internal/flag_test.go`
- ❌ `src/cmd/compile/internal/objabi/flag.go`
- ❌ `src/cmd/compile/internal/objabi/flag_test.go`
- ❌ `src/cmd/go/go.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16133.dir/main.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/runtime/compiler.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #40025**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/io`
- `src/io/ioutil`
- `src/os`

**Predicted Directories (3):**
- ✅ `src/io`
- ✅ `src/io/ioutil`
- ❌ `src/issue16133.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 16.7% | 22.2% | 2/12 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (12):**
- `src/io/example_test.go`
- `src/io/io.go`
- `src/io/ioutil/example_test.go`
- `src/io/ioutil/ioutil.go`
- `src/os/dir.go`
- `src/os/example_test.go`
- `src/os/file.go`
- `src/os/os_test.go`
- `src/os/read_test.go`
- `src/os/removeall_test.go`
- `src/os/tempfile.go`
- `src/os/tempfile_test.go`

**Predicted Files (6):**
- ✅ `src/io/io.go`
- ✅ `src/io/ioutil/ioutil.go`
- ❌ `src/io/ioutil/ioutil_test.go`
- ❌ `src/issue16133.dir/a.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/main.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 16.7% | 26.7% | 2/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/io`
- `src/io/ioutil`


### 📊 **Proposal #47527**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/bufio`

**Predicted Directories (3):**
- ❌ `src/bio`
- ✅ `src/bufio`
- ❌ `src/strconv`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 66.7% | 50.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/bufio/bufio.go`
- `src/bufio/bufio_test.go`
- `src/bufio/example_test.go`

**Predicted Files (5):**
- ❌ `src/bio/buf.go`
- ✅ `src/bufio/bufio.go`
- ✅ `src/bufio/bufio_test.go`
- ❌ `src/strconv/strconv.go`
- ❌ `src/strconv/strconv_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/bufio`


### 📊 **Proposal #37974**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/ast`

**Predicted Directories (7):**
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/go`
- ❌ `src/go/doc`
- ❌ `src/go/internal/doc`
- ❌ `src/net/http`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/ast/ast.go`
- `src/go/ast/ast_test.go`

**Predicted Files (38):**
- ❌ `directive.go`
- ❌ `directive2.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/funcid.go`
- ❌ `src/cmd/internal/objabi/head.go`
- ❌ `src/cmd/internal/objabi/line.go`
- ❌ `src/cmd/internal/objabi/path.go`
- ❌ `src/cmd/internal/objabi/reloctype.go`
- ❌ `src/cmd/internal/objabi/reloctype_string.go`
- ❌ `src/cmd/internal/objabi/stack.go`
- ❌ `src/cmd/internal/objabi/symkind.go`
- ❌ `src/cmd/internal/objabi/symkind_string.go`
- ❌ `src/cmd/internal/objabi/util.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/flag_test.go`
- ❌ `src/cmd/internal/objfile/funcid_test.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/head_test.go`
- ❌ `src/cmd/internal/objfile/line.go`
- ❌ `src/cmd/internal/objfile/line_test.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/objfile.go`
- ❌ `src/cmd/internal/objfile/path_test.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/reloctype_string_test.go`
- ❌ `src/cmd/internal/objfile/reloctype_test.go`
- ❌ `src/cmd/internal/objfile/stack_test.go`
- ❌ `src/cmd/internal/objfile/symkind_string_test.go`
- ❌ `src/cmd/internal/objfile/symkind_test.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/go/doc.go`
- ❌ `src/go/doc/comment.go`
- ❌ `src/go/doc/comment_test.go`
- ❌ `src/go/doc/doc.go`
- ❌ `src/go/internal/doc/doc.go`
- ❌ `src/net/http/doc.go`
- ❌ `src/runtime/doc.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #37776**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (6):**
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/net`
- ✅ `src/net/url`
- ❌ `src/web`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 66.7% | 33.3% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/net/url/example_test.go`
- `src/net/url/url.go`
- `src/net/url/url_test.go`

**Predicted Files (9):**
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/issue16133.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/net/url.go`
- ✅ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`
- ❌ `src/web/url.go`
- ❌ `src/web/url_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/url`


### 📊 **Proposal #40357**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/list`
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modload`

**Predicted Directories (3):**
- ❌ `src/cmd/go/internal/modfile`
- ❌ `src/go/internal/modcmd`
- ❌ `src/go/internal/modload`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/go/internal/list/list.go`
- `src/cmd/go/internal/modcmd/download.go`
- `src/cmd/go/internal/modcmd/why.go`
- `src/cmd/go/internal/modload/build.go`
- `src/cmd/go/internal/modload/list.go`

**Predicted Files (7):**
- ❌ `src/cmd/go/internal/modfile/print.go`
- ❌ `src/cmd/go/internal/modfile/read.go`
- ❌ `src/go/internal/modcmd/edit.go`
- ❌ `src/go/internal/modcmd/get.go`
- ❌ `src/go/internal/modload/list.go`
- ❌ `src/go/internal/modload/load.go`
- ❌ `src/go/internal/modload/modfile.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #39557**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (7):**
- ❌ `src/cmd/internal/objabi`
- ✅ `src/flag`
- ❌ `src/go/internal/cmdflag`
- ❌ `src/go/internal/load`
- ❌ `src/net/http`
- ❌ `src/net/http/httptest`
- ❌ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 3/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/flag/example_func_test.go`
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (15):**
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/flag/example_flagset_test.go`
- ✅ `src/flag/example_func_test.go`
- ❌ `src/flag/example_test.go`
- ❌ `src/flag/example_textvar_test.go`
- ❌ `src/flag/example_value_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`
- ❌ `src/go/internal/cmdflag/flag.go`
- ❌ `src/go/internal/load/flag.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/httptest/httptest.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ❌ `src/testing/flag_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 100.0% | 60.0% | 3/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/flag`


### 📊 **Proposal #35804**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/database/sql`

**Predicted Directories (1):**
- ✅ `src/database/sql`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`

**Predicted Files (2):**
- ✅ `src/database/sql/sql.go`
- ✅ `src/database/sql/sql_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/database/sql`


### 📊 **Proposal #53003**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 10.0% | 15.4% | 1/10 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (10):**
- `src/cmd/compile/internal/escape`
- `src/cmd/compile/internal/ir`
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/ssagen`
- `src/cmd/compile/internal/typecheck`
- `src/cmd/compile/internal/types2`
- `src/cmd/compile/internal/walk`
- `src/go/types`
- `src/unsafe`
- `test`

**Predicted Directories (3):**
- ❌ `src`
- ❌ `src/runtime`
- ✅ `src/unsafe`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 5.9% | 8.0% | 1/17 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (17):**
- `src/cmd/compile/internal/escape/expr.go`
- `src/cmd/compile/internal/ir/expr.go`
- `src/cmd/compile/internal/ir/op_string.go`
- `src/cmd/compile/internal/noder/reader.go`
- `src/cmd/compile/internal/noder/writer.go`
- `src/cmd/compile/internal/ssagen/ssa.go`
- `src/cmd/compile/internal/typecheck/const.go`
- `src/cmd/compile/internal/typecheck/func.go`
- `src/cmd/compile/internal/typecheck/typecheck.go`
- `src/cmd/compile/internal/types2/builtins.go`
- `src/cmd/compile/internal/walk/builtin.go`
- `src/cmd/compile/internal/walk/expr.go`
- `src/go/types/builtins.go`
- `src/unsafe/unsafe.go`
- `test/unsafe_slice_data.go`
- `test/unsafe_string.go`
- `test/unsafebuiltins.go`

**Predicted Files (8):**
- ❌ `src/runtime/slice.go`
- ❌ `src/runtime/string.go`
- ❌ `src/runtime/unsafe.go`
- ❌ `src/unsafe.go`
- ✅ `src/unsafe/unsafe.go`
- ❌ `unsafe_slice_data.go`
- ❌ `unsafe_string.go`
- ❌ `unsafe_string_data.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 5.9% | 11.1% | 1/17 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/unsafe`


### 📊 **Proposal #40281**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 50.0% | 22.2% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- `src/reflect`

**Predicted Directories (7):**
- ❌ `interface`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/encoding/json`
- ✅ `src/reflect`
- ❌ `src/reflectlite`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- `src/reflect/type.go`

**Predicted Files (23):**
- ❌ `interface/struct.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/elf_test.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/goobj_test.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/macho_test.go`
- ❌ `src/cmd/internal/objfile/objfile.go`
- ❌ `src/cmd/internal/objfile/objfile_test.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/pe_test.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/plan9obj_test.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/cmd/internal/objfile/xcoff_test.go`
- ❌ `src/encoding/json/tags.go`
- ❌ `src/encoding/json/tags_test.go`
- ❌ `src/reflect/reflect.go`
- ❌ `src/reflectlite/type.go`
- ❌ `src/reflectlite/value.go`
- ❌ `src/runtime/reflect_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #41563**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 16.7% | 28.6% | 1/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/encoding/asn1`
- `src/encoding/json`
- `src/encoding/xml`
- `src/net/rpc`
- `src/reflect`
- `src/text/template`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 12.5% | 10.0% | 1/8 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (8):**
- `src/encoding/asn1/asn1.go`
- `src/encoding/asn1/marshal.go`
- `src/encoding/json/encode.go`
- `src/encoding/xml/typeinfo.go`
- `src/net/rpc/server.go`
- `src/reflect/all_test.go`
- `src/reflect/type.go`
- `src/text/template/exec.go`

**Predicted Files (12):**
- ❌ `method.go`
- ❌ `reflectmethod1.go`
- ❌ `reflectmethod2.go`
- ❌ `reflectmethod3.go`
- ❌ `reflectmethod4.go`
- ❌ `reflectmethod5.go`
- ❌ `reflectmethod6.go`
- ❌ `reflectmethod7.go`
- ❌ `reflectmethod8.go`
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/type.go`
- ❌ `src/reflect/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 12.5% | 18.2% | 1/8 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #46121**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/html/template`

**Predicted Directories (3):**
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/html/template`
- ❌ `src/text/template`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/html/template/template.go`

**Predicted Files (5):**
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ✅ `src/html/template/template.go`
- ❌ `src/html/template/template_test.go`
- ❌ `src/text/template/exec.go`
- ❌ `src/text/template/template.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/html/template`


### 📊 **Proposal #43947**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 50.0% | 18.2% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/dist`
- `src/os/exec`

**Predicted Directories (9):**
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/os`
- ✅ `src/os/exec`
- ❌ `src/syscall`
- ❌ `src/syscall/execenv`
- ❌ `src/syscall/windows`
- ❌ `src/toolchain`
- ❌ `src/work`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/8 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (8):**
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/cmd/dist/util.go`
- `src/os/exec/dot_test.go`
- `src/os/exec/exec.go`
- `src/os/exec/lp_plan9.go`
- `src/os/exec/lp_unix.go`
- `src/os/exec/lp_windows.go`

**Predicted Files (21):**
- ❌ `src/cmd/internal/objabi/exec_windows.go`
- ❌ `src/cmd/internal/objabi/os_windows.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/objfile.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/os/exec/exec_windows.go`
- ❌ `src/os/exec/exec_windows_test.go`
- ❌ `src/os/os_windows.go`
- ❌ `src/os/os_windows_arm.go`
- ❌ `src/os/os_windows_arm64.go`
- ❌ `src/syscall/exec_windows.go`
- ❌ `src/syscall/exec_windows_test.go`
- ❌ `src/syscall/execenv/execenv_windows.go`
- ❌ `src/syscall/windows/exec_windows_test.go`
- ❌ `src/toolchain/exec.go`
- ❌ `src/toolchain/path_windows.go`
- ❌ `src/work/exec.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/8 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/os/exec`


### 📊 **Proposal #50860**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 25.0% | 33.3% | 1/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `src/cmd/compile/internal/escape`
- `src/cmd/compile/internal/test`
- `src/cmd/compile/internal/types`
- `src/sync/atomic`

**Predicted Directories (2):**
- ❌ `src/runtime/atomic`
- ✅ `src/sync/atomic`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 40.0% | 25.0% | 2/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/compile/internal/escape/utils.go`
- `src/cmd/compile/internal/test/inl_test.go`
- `src/cmd/compile/internal/types/size.go`
- `src/sync/atomic/atomic_test.go`
- `src/sync/atomic/type.go`

**Predicted Files (11):**
- ❌ `atomicload.go`
- ❌ `escape_runtime_atomic.go`
- ❌ `intrinsic_atomic.go`
- ❌ `src/runtime/atomic/atomic_test.go`
- ❌ `src/runtime/atomic/types.go`
- ❌ `src/sync/atomic/atomic.go`
- ✅ `src/sync/atomic/atomic_test.go`
- ❌ `src/sync/atomic/doc.go`
- ✅ `src/sync/atomic/type.go`
- ❌ `src/sync/atomic/value.go`
- ❌ `src/sync/atomic/value_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 40.0% | 36.4% | 2/5 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/sync/atomic`


### 📊 **Proposal #52444**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (5):**
- ❌ `src`
- ✅ `src/crypto/x509`
- ❌ `src/issue15646.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.4% | 100.0% | 26.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (13):**
- ❌ `src/crypto/x509/parser.go`
- ❌ `src/crypto/x509/parser_test.go`
- ❌ `src/crypto/x509/pem_decrypt.go`
- ❌ `src/crypto/x509/pem_decrypt_test.go`
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`
- ❌ `src/issue15646.dir/issue15646.go`
- ❌ `src/issue15920.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16616.dir/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #43724**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/syscall/windows`
- `src/syscall`

**Predicted Directories (4):**
- ❌ `src/cmd/internal/pathcache`
- ❌ `src/go/internal/exec`
- ❌ `src/os`
- ❌ `src/os/exec`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/internal/syscall/windows/zsyscall_windows.go`
- `src/syscall/mksyscall_windows.go`

**Predicted Files (8):**
- ❌ `src/cmd/internal/pathcache/lookpath.go`
- ❌ `src/go/internal/exec/exec.go`
- ❌ `src/go/internal/exec/exec_test.go`
- ❌ `src/os/exec.go`
- ❌ `src/os/exec/dot_test.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/exec_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #41730**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 40.0% | 57.1% | 2/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/go`
- `src/cmd/go/internal/envcmd`
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modget`
- `src/cmd/go/internal/vcs`

**Predicted Directories (2):**
- ✅ `src/cmd/go/internal/modfetch`
- ✅ `src/cmd/go/internal/vcs`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/envcmd/env.go`
- `src/cmd/go/internal/modfetch/proxy.go`
- `src/cmd/go/internal/modget/get.go`
- `src/cmd/go/internal/vcs/vcs.go`
- `src/cmd/go/internal/vcs/vcs_test.go`
- `src/cmd/go/main.go`

**Predicted Files (4):**
- ❌ `src/cmd/go/internal/modfetch/git.go`
- ❌ `src/cmd/go/internal/modfetch/svn.go`
- ❌ `src/cmd/go/internal/vcs/git.go`
- ❌ `src/cmd/go/internal/vcs/svn.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/vcs`


### 📊 **Proposal #51668**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/fmt`

**Predicted Directories (3):**
- ✅ `src/fmt`
- ❌ `src/go/internal/fmtcmd`
- ❌ `src/types`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/fmt/print.go`
- `src/fmt/state_test.go`

**Predicted Files (5):**
- ❌ `src/fmt/format.go`
- ✅ `src/fmt/print.go`
- ✅ `src/fmt/state_test.go`
- ❌ `src/go/internal/fmtcmd/fmt.go`
- ❌ `src/types/fmt.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/fmt`


### 📊 **Proposal #41980**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/diff`
- `src/testing`

**Predicted Directories (3):**
- ❌ `src/cmp`
- ✅ `src/testing`
- ❌ `test/interface`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/internal/diff/diff_test.go`
- `src/testing/example.go`

**Predicted Files (9):**
- ❌ `src/cmp/cmp.go`
- ❌ `src/testing/example_test.go`
- ❌ `src/testing/run_example.go`
- ❌ `test/interface/assertinline.go`
- ❌ `test/interface/convert.go`
- ❌ `test/interface/convert1.go`
- ❌ `test/interface/convert2.go`
- ❌ `test/interface/convert3.go`
- ❌ `test/interface/convert4.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #41792**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (6):**
- ❌ `src/cmd/internal/objabi`
- ❌ `src/compile/internal/base`
- ✅ `src/flag`
- ❌ `src/go/internal/base`
- ❌ `src/go/internal/load`
- ❌ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (8):**
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ❌ `src/compile/internal/base/flag.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`
- ❌ `src/go/internal/base/flag.go`
- ❌ `src/go/internal/load/flag.go`
- ❌ `src/testing/flag_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/flag`


### 📊 **Proposal #45453**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/compile/internal/amd64`
- `src/cmd/compile/internal/ssa`
- `src/cmd/dist`
- `src/cmd/go/internal/cfg`
- `src/cmd/go/internal/work`
- `src/internal/buildcfg`
- `test/codegen`

**Predicted Directories (5):**
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/runtime/asan`
- ❌ `src/runtime/race`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/12 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (12):**
- `src/cmd/compile/internal/amd64/ssa.go`
- `src/cmd/compile/internal/amd64/versions_test.go`
- `src/cmd/compile/internal/ssa/rewriteAMD64.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/buildruntime.go`
- `src/cmd/go/internal/cfg/cfg.go`
- `src/cmd/go/internal/work/gc.go`
- `src/internal/buildcfg/cfg.go`
- `src/internal/buildcfg/cfg_test.go`
- `test/codegen/bmi.go`
- `test/codegen/mathbits.go`
- `test/codegen/memcombine.go`

**Predicted Files (13):**
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/runtime/asan/asan.go`
- ❌ `src/runtime/race/race.go`
- ❌ `src/runtime/race/race_darwin_amd64.go`
- ❌ `src/runtime/race/race_v3_amd64.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/12 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #40276**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/work`

**Predicted Directories (0):**

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modload/init.go`
- `src/cmd/go/internal/work/build.go`

**Predicted Files (0):**

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #42322**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 33.3% | 33.3% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/embed/internal/embedtest`
- `src/io/fs`
- `src/testing/fstest`

**Predicted Directories (3):**
- ❌ `src/embed`
- ✅ `src/io/fs`
- ❌ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 28.6% | 28.6% | 2/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/embed/internal/embedtest/embed_test.go`
- `src/io/fs/readdir_test.go`
- `src/io/fs/readfile_test.go`
- `src/io/fs/sub.go`
- `src/io/fs/sub_test.go`
- `src/testing/fstest/mapfs.go`
- `src/testing/fstest/testfs.go`

**Predicted Files (7):**
- ❌ `src/embed/embed.go`
- ❌ `src/embed/example_test.go`
- ❌ `src/io/fs/fs.go`
- ✅ `src/io/fs/sub.go`
- ✅ `src/io/fs/sub_test.go`
- ❌ `src/net/http/fs.go`
- ❌ `src/net/http/http.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 28.6% | 40.0% | 2/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io/fs`


### 📊 **Proposal #42100**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 25.0% | 20.0% | 1/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `misc/ios`
- `src/cmd/dist`
- `src/cmd/go/internal/work`
- `src/cmd/link/internal/ld`

**Predicted Directories (6):**
- ✅ `misc/ios`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/go/goos`
- ❌ `src/runtime`
- ❌ `src/runtime/cgo`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.1% | 20.0% | 5.4% | 1/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `misc/ios/go_ios_exec.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/cmd/go/internal/work/init.go`
- `src/cmd/link/internal/ld/config.go`

**Predicted Files (32):**
- ❌ `misc/ios/detect.go`
- ✅ `misc/ios/go_ios_exec.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/elf_test.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/goobj_test.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/macho_test.go`
- ❌ `src/cmd/internal/objfile/objfile.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/pe_test.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/plan9obj_test.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/cmd/internal/objfile/xcoff_test.go`
- ❌ `src/go/goos/zgoos_ios.go`
- ❌ `src/runtime/cgo/handle_ios_arm64.go`
- ❌ `src/runtime/defs_darwin.go`
- ❌ `src/runtime/defs_darwin_amd64.go`
- ❌ `src/runtime/os_darwin.go`
- ❌ `src/runtime/os_darwin_amd64.go`
- ❌ `src/runtime/signal_darwin_amd64.go`
- ❌ `src/runtime/syscall_darwin.go`
- ❌ `src/runtime/syscall_darwin_amd64.go`
- ❌ `src/runtime/syscall_darwin_arm64.go`
- ❌ `src/syscall/rlimit_darwin.go`
- ❌ `src/syscall/route_darwin.go`
- ❌ `src/syscall/syscall_darwin_amd64.go`
- ❌ `src/syscall/syscall_darwin_arm64.go`
- ❌ `src/syscall/types_darwin.go`
- ❌ `src/syscall/zsysnum_darwin_amd64.go`
- ❌ `src/syscall/zsysnum_darwin_arm64.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 20.0% | 28.6% | 1/5 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `misc/ios`


### 📊 **Proposal #37475**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 27.3% | 33.3% | 30.0% | 3/9 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (9):**
- `src/cmd/go`
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/vcs`
- `src/cmd/go/internal/version`
- `src/cmd/go/internal/work`
- `src/debug/buildinfo`
- `src/encoding/binary`
- `src/runtime/debug`

**Predicted Directories (11):**
- ❌ `cmd/go/internal/load`
- ❌ `cmd/go/internal/work`
- ❌ `runtime/debug`
- ❌ `src/cmd/go/internal`
- ✅ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ✅ `src/cmd/go/internal/work`
- ❌ `src/go/internal/load`
- ❌ `src/go/internal/work`
- ❌ `src/runtime`
- ✅ `src/runtime/debug`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.1% | 7.7% | 7.4% | 1/13 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (13):**
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/load/flag.go`
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/modload/build.go`
- `src/cmd/go/internal/vcs/vcs.go`
- `src/cmd/go/internal/vcs/vcs_test.go`
- `src/cmd/go/internal/version/version.go`
- `src/cmd/go/internal/work/build.go`
- `src/debug/buildinfo/buildinfo.go`
- `src/debug/buildinfo/buildinfo_test.go`
- `src/encoding/binary/binary_test.go`
- `src/encoding/binary/varint_test.go`
- `src/runtime/debug/mod.go`

**Predicted Files (14):**
- ❌ `cmd/go/internal/load/pkg.go`
- ❌ `cmd/go/internal/work/exec.go`
- ❌ `runtime/debug/debug.go`
- ✅ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/git.go`
- ❌ `src/cmd/go/internal/version.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/go/internal/load/pkg.go`
- ❌ `src/go/internal/work/exec.go`
- ❌ `src/runtime/debug.go`
- ❌ `src/runtime/debug/buildinfo.go`
- ❌ `src/runtime/debug/debug.go`
- ❌ `src/runtime/debug/readbuildinfo.go`
- ❌ `src/runtime/debug_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 7.7% | 11.1% | 1/13 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/work`
- `src/runtime/debug`


### 📊 **Proposal #39567**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (3):**
- ❌ `src/issue16317.dir`
- ❌ `src/issue16616.dir`
- ✅ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/serve_test.go`
- `src/net/http/server.go`

**Predicted Files (6):**
- ❌ `src/issue16317.dir/a.go`
- ❌ `src/issue16317.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ✅ `src/net/http/server.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http`


### 📊 **Proposal #44808**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/image`
- `src/image/draw`

**Predicted Directories (3):**
- ✅ `src/image`
- ❌ `src/image/color`
- ✅ `src/image/draw`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 28.6% | 40.0% | 2/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/image/draw/draw.go`
- `src/image/draw/draw_test.go`
- `src/image/geom.go`
- `src/image/image.go`
- `src/image/image_test.go`
- `src/image/names.go`
- `src/image/ycbcr.go`

**Predicted Files (3):**
- ❌ `src/image/color/color.go`
- ✅ `src/image/draw/draw.go`
- ✅ `src/image/image.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 28.6% | 44.4% | 2/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/image`
- `src/image/draw`


### 📊 **Proposal #45754**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 100.0% | 20.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (9):**
- ❌ `src/compile/base`
- ❌ `src/encoding`
- ✅ `src/flag`
- ❌ `src/go/internal/cmdflag`
- ❌ `src/go/internal/load`
- ❌ `src/math/big`
- ❌ `src/net`
- ❌ `src/testing`
- ❌ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/example_textvar_test.go`
- `src/flag/flag.go`

**Predicted Files (14):**
- ❌ `src/compile/base/flag.go`
- ❌ `src/encoding/text.go`
- ✅ `src/flag/example_textvar_test.go`
- ✅ `src/flag/flag.go`
- ❌ `src/flag/flag_test.go`
- ❌ `src/go/internal/cmdflag/flag.go`
- ❌ `src/go/internal/load/flag.go`
- ❌ `src/math/big/float.go`
- ❌ `src/math/big/int.go`
- ❌ `src/math/big/rat.go`
- ❌ `src/net/ip.go`
- ❌ `src/testing/flag_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/flag`


### 📊 **Proposal #47651**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 4.8% | 6.2% | 1/21 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (21):**
- `src/cmd/fix`
- `src/cmd/gofmt`
- `src/database/sql`
- `src/database/sql/driver`
- `src/encoding/asn1`
- `src/encoding/binary`
- `src/encoding/gob`
- `src/encoding/json`
- `src/encoding/xml`
- `src/flag`
- `src/fmt`
- `src/go/ast`
- `src/html/template`
- `src/internal/fmtsort`
- `src/internal/reflectlite`
- `src/net/rpc`
- `src/reflect`
- `src/testing/quick`
- `src/text/template`
- `test`
- `test/fixedbugs/issue32901.dir`

**Predicted Directories (11):**
- ❌ `interface`
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/reflect`
- ❌ `src/reflectdata`
- ❌ `src/reflectlite`
- ❌ `src/runtime`
- ❌ `src/types`
- ❌ `src/unsafe`
- ❌ `src/weak`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 7.3% | 8.5% | 3/41 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (41):**
- `src/cmd/fix/cftype.go`
- `src/cmd/fix/typecheck.go`
- `src/cmd/gofmt/rewrite.go`
- `src/database/sql/convert.go`
- `src/database/sql/driver/types.go`
- `src/encoding/asn1/asn1.go`
- `src/encoding/binary/binary.go`
- `src/encoding/gob/decode.go`
- `src/encoding/gob/decoder.go`
- `src/encoding/gob/encode.go`
- `src/encoding/gob/encoder.go`
- `src/encoding/gob/type.go`
- `src/encoding/gob/type_test.go`
- `src/encoding/json/decode.go`
- `src/encoding/json/decode_test.go`
- `src/encoding/json/encode.go`
- `src/encoding/xml/marshal.go`
- `src/encoding/xml/read.go`
- `src/encoding/xml/typeinfo.go`
- `src/flag/flag.go`
- `src/fmt/print.go`
- `src/fmt/scan.go`
- `src/fmt/scan_test.go`
- `src/go/ast/print.go`
- `src/html/template/content.go`
- `src/html/template/js.go`
- `src/internal/fmtsort/sort.go`
- `src/internal/reflectlite/tostring_test.go`
- `src/internal/reflectlite/value.go`
- `src/net/rpc/server.go`
- `src/reflect/abi.go`
- `src/reflect/all_test.go`
- `src/reflect/deepequal.go`
- `src/reflect/tostring_test.go`
- `src/reflect/type.go`
- `src/reflect/value.go`
- `src/reflect/visiblefields.go`
- `src/testing/quick/quick.go`
- `src/text/template/exec.go`
- `test/fixedbugs/issue32901.dir/main.go`
- `test/reflectmethod7.go`

**Predicted Files (30):**
- ❌ `interface/pointer.go`
- ❌ `reflectmethod1.go`
- ❌ `reflectmethod2.go`
- ❌ `reflectmethod3.go`
- ❌ `reflectmethod4.go`
- ❌ `reflectmethod5.go`
- ❌ `reflectmethod6.go`
- ❌ `reflectmethod7.go`
- ❌ `reflectmethod8.go`
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ✅ `src/reflect/abi.go`
- ❌ `src/reflect/iter.go`
- ✅ `src/reflect/type.go`
- ✅ `src/reflect/value.go`
- ❌ `src/reflectdata/reflect.go`
- ❌ `src/reflectlite/type.go`
- ❌ `src/reflectlite/value.go`
- ❌ `src/runtime/reflect_test.go`
- ❌ `src/types/pointer.go`
- ❌ `src/unsafe/unsafe.go`
- ❌ `src/weak/pointer.go`
- ❌ `src/weak/pointer_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 7.3% | 13.3% | 3/41 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #48052**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/debug/plan9obj`

**Predicted Directories (3):**
- ❌ `src/debug/elf`
- ✅ `src/debug/plan9obj`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/debug/plan9obj/file.go`

**Predicted Files (3):**
- ❌ `src/debug/elf/elf.go`
- ✅ `src/debug/plan9obj/file.go`
- ❌ `src/syscall/syscall_plan9.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/debug/plan9obj`


### 📊 **Proposal #33920**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/io/ioutil`
- `src/os`

**Predicted Directories (1):**
- ✅ `src/io/ioutil`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/io/ioutil/tempfile.go`
- `src/io/ioutil/tempfile_test.go`
- `src/os/os_test.go`

**Predicted Files (2):**
- ✅ `src/io/ioutil/tempfile.go`
- ✅ `src/io/ioutil/tempfile_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io/ioutil`


### 📊 **Proposal #47209**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/fsys`
- `src/io/fs`
- `src/path/filepath`

**Predicted Directories (3):**
- ❌ `src/fixedbugs/issue4370.dir`
- ✅ `src/io/fs`
- ✅ `src/path/filepath`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 75.0% | 24.0% | 3/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/cmd/go/internal/fsys/fsys_test.go`
- `src/io/fs/walk.go`
- `src/path/filepath/path.go`
- `src/path/filepath/path_test.go`

**Predicted Files (21):**
- ❌ `src/fixedbugs/issue4370.dir/p1.go`
- ❌ `src/fixedbugs/issue4370.dir/p2.go`
- ❌ `src/fixedbugs/issue4370.dir/p3.go`
- ✅ `src/io/fs/walk.go`
- ❌ `src/io/fs/walk_test.go`
- ❌ `src/path/filepath/example_test.go`
- ❌ `src/path/filepath/example_unix_test.go`
- ❌ `src/path/filepath/example_unix_walk_test.go`
- ❌ `src/path/filepath/export_test.go`
- ❌ `src/path/filepath/match.go`
- ❌ `src/path/filepath/match_test.go`
- ✅ `src/path/filepath/path.go`
- ❌ `src/path/filepath/path_plan9.go`
- ✅ `src/path/filepath/path_test.go`
- ❌ `src/path/filepath/path_unix.go`
- ❌ `src/path/filepath/path_windows.go`
- ❌ `src/path/filepath/path_windows_test.go`
- ❌ `src/path/filepath/symlink.go`
- ❌ `src/path/filepath/symlink_plan9.go`
- ❌ `src/path/filepath/symlink_unix.go`
- ❌ `src/path/filepath/symlink_windows.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 75.0% | 27.3% | 3/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/io/fs`
- `src/path/filepath`


### 📊 **Proposal #48152**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/tls`
- `src/net/http`

**Predicted Directories (2):**
- ✅ `src/crypto/tls`
- ❌ `src/crypto/x509`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.4% | 50.0% | 23.5% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/net/http/transport_test.go`

**Predicted Files (13):**
- ✅ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_client_test.go`
- ❌ `src/crypto/tls/handshake_messages.go`
- ❌ `src/crypto/tls/handshake_messages_test.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/crypto/tls/tls_test.go`
- ❌ `src/crypto/tls/verify.go`
- ❌ `src/crypto/x509/verify.go`
- ❌ `src/crypto/x509/verify_test.go`
- ❌ `src/crypto/x509/x509.go`
- ❌ `src/crypto/x509/x509_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 50.0% | 30.8% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #41682**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (7):**
- ✅ `src/crypto/x509`
- ❌ `src/issue15646.dir`
- ❌ `src/issue15838.dir`
- ❌ `src/issue15920.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16317.dir`
- ❌ `src/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.0% | 100.0% | 26.1% | 3/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/x509/verify_test.go`
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (20):**
- ❌ `src/crypto/x509/parser.go`
- ❌ `src/crypto/x509/parser_test.go`
- ❌ `src/crypto/x509/verify.go`
- ✅ `src/crypto/x509/verify_test.go`
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`
- ❌ `src/issue15646.dir/issue15646.go`
- ❌ `src/issue15838.dir/a.go`
- ❌ `src/issue15838.dir/b.go`
- ❌ `src/issue15920.dir/a.go`
- ❌ `src/issue15920.dir/b.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16317.dir/a.go`
- ❌ `src/issue16317.dir/b.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 3/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #53200**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/token`

**Predicted Directories (3):**
- ❌ `src/go/internal/modload`
- ✅ `src/go/token`
- ❌ `test/fixedbugs`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/token/position.go`
- `src/go/token/position_test.go`

**Predicted Files (12):**
- ❌ `src/go/internal/modload/build.go`
- ❌ `src/go/internal/modload/import.go`
- ❌ `src/go/internal/modload/load.go`
- ❌ `src/go/token/file.go`
- ❌ `src/go/token/file_test.go`
- ❌ `src/go/token/pos.go`
- ❌ `src/go/token/pos_test.go`
- ✅ `src/go/token/position.go`
- ✅ `src/go/token/position_test.go`
- ❌ `src/go/token/token.go`
- ❌ `src/go/token/token_test.go`
- ❌ `test/fixedbugs/issue53200.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/token`


### 📊 **Proposal #40082**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/database/sql`

**Predicted Directories (2):**
- ✅ `src/database/sql`
- ❌ `src/database/sql/driver`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 66.7% | 50.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/database/sql/fakedb_test.go`
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`

**Predicted Files (5):**
- ❌ `src/database/sql/driver/driver.go`
- ❌ `src/database/sql/driver/types.go`
- ❌ `src/database/sql/driver/types_test.go`
- ✅ `src/database/sql/sql.go`
- ✅ `src/database/sql/sql_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/database/sql`


### 📊 **Proposal #45963**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/test`
- `src/cmd/go/internal/work`

**Predicted Directories (6):**
- ❌ `src/cmd/go/analysis`
- ❌ `src/cmd/go/analysis/internal/analysisflags`
- ❌ `src/cmd/go/analysis/unitchecker`
- ❌ `src/cmd/go/vet`
- ❌ `src/cmd/vet`
- ❌ `src/fixedbugs/issue4590.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/test/testflag.go`
- `src/cmd/go/internal/work/exec.go`

**Predicted Files (13):**
- ❌ `src/cmd/go/analysis/analysis.go`
- ❌ `src/cmd/go/analysis/diagnostic.go`
- ❌ `src/cmd/go/analysis/internal/analysisflags/flags.go`
- ❌ `src/cmd/go/analysis/unitchecker/unitchecker.go`
- ❌ `src/cmd/go/vet/vet.go`
- ❌ `src/cmd/go/vet/vetflag.go`
- ❌ `src/cmd/vet/doc.go`
- ❌ `src/cmd/vet/main.go`
- ❌ `src/fixedbugs/issue4590.dir/main.go`
- ❌ `src/fixedbugs/issue4590.dir/pkg1.go`
- ❌ `src/fixedbugs/issue4590.dir/pkg2.go`
- ❌ `src/fixedbugs/issue4590.dir/prog.go`
- ❌ `src/fixedbugs/issue4590.dir/test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #46518**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 40.0% | 57.1% | 2/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/internal/fuzz`
- `src/internal/godebug`
- `src/net`
- `src/net/http`
- `src/net/netip`

**Predicted Directories (2):**
- ✅ `src/net`
- ✅ `src/net/netip`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 17.6% | 28.6% | 3/17 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (17):**
- `src/internal/fuzz/fuzz.go`
- `src/internal/godebug/godebug_test.go`
- `src/net/conf.go`
- `src/net/http/server.go`
- `src/net/http/transport.go`
- `src/net/lookup.go`
- `src/net/netip/export_test.go`
- `src/net/netip/inlining_test.go`
- `src/net/netip/netip.go`
- `src/net/netip/netip_pkg_test.go`
- `src/net/netip/netip_test.go`
- `src/net/netip/slow_test.go`
- `src/net/netip/uint128.go`
- `src/net/netip/uint128_test.go`
- `src/net/parse_test.go`
- `src/net/tcpsock.go`
- `src/net/udpsock.go`

**Predicted Files (4):**
- ❌ `src/net/net.go`
- ✅ `src/net/netip/export_test.go`
- ✅ `src/net/netip/netip.go`
- ✅ `src/net/netip/netip_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 17.6% | 28.6% | 3/17 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/net`
- `src/net/netip`


### 📊 **Proposal #40337**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (5):**
- ❌ `src/crypto/dsa`
- ✅ `src/crypto/x509`
- ❌ `src/golang.org/x/crypto/ssh`
- ❌ `vendor/golang.org/x/crypto/ssh`
- ❌ `vendor/golang.org/x/crypto/x509`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 100.0% | 36.4% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (9):**
- ❌ `issue17596.go`
- ❌ `src/crypto/dsa/dsa.go`
- ❌ `src/crypto/x509/parser.go`
- ❌ `src/crypto/x509/verify.go`
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`
- ❌ `src/golang.org/x/crypto/ssh/keys.go`
- ❌ `vendor/golang.org/x/crypto/ssh/keys.go`
- ❌ `vendor/golang.org/x/crypto/x509/x509.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #45973**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (4):**
- ❌ `src/fixedbugs/issue25192.dir`
- ✅ `src/net/http`
- ❌ `vendor/golang.org/x/net/http/httpguts`
- ❌ `vendor/golang.org/x/net/http/httpproxy`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 50.0% | 16.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/serve_test.go`
- `src/net/http/server.go`

**Predicted Files (10):**
- ❌ `src/fixedbugs/issue25192.dir/a.go`
- ❌ `src/fixedbugs/issue25192.dir/b.go`
- ❌ `src/fixedbugs/issue25192.dir/c.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ✅ `src/net/http/server.go`
- ❌ `src/net/http/url.go`
- ❌ `vendor/golang.org/x/net/http/httpguts/guts.go`
- ❌ `vendor/golang.org/x/net/http/httpproxy/proxy.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http`


### 📊 **Proposal #49471**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (7):**
- ❌ `internal/runtime/sys`
- ❌ `src/go/internal/obj/x86`
- ✅ `src/runtime`
- ❌ `src/runtime/debug`
- ❌ `src/runtime/syscall`
- ❌ `src/runtime/syscall/windows/registry`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/os_windows.go`
- `src/runtime/panic.go`
- `src/runtime/signal_windows.go`

**Predicted Files (27):**
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `runtime.go`
- ❌ `src/go/internal/obj/x86/a.out.go`
- ❌ `src/go/internal/obj/x86/anames.go`
- ❌ `src/go/internal/obj/x86/asm6.go`
- ❌ `src/go/internal/obj/x86/asm_test.go`
- ❌ `src/go/internal/obj/x86/avx_optabs.go`
- ❌ `src/go/internal/obj/x86/evex.go`
- ❌ `src/go/internal/obj/x86/obj6.go`
- ❌ `src/go/internal/obj/x86/objfile.go`
- ❌ `src/go/internal/obj/x86/objfile_test.go`
- ❌ `src/go/internal/obj/x86/pcrelative_test.go`
- ❌ `src/go/internal/obj/x86/ytab.go`
- ❌ `src/runtime/crash.go`
- ❌ `src/runtime/crashdump.go`
- ❌ `src/runtime/debug/stack.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/runtime.go`
- ❌ `src/runtime/stack.go`
- ❌ `src/runtime/syscall/syscall_windows.go`
- ❌ `src/runtime/syscall/windows/registry/key.go`
- ❌ `src/runtime/syscall/windows/registry/syscall.go`
- ❌ `src/runtime/syscall_windows.go`
- ❌ `src/runtime/trace.go`
- ❌ `src/runtime/trace_test.go`
- ❌ `src/syscall/security_windows.go`
- ❌ `src/syscall/syscall_windows.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime`


### 📊 **Proposal #52746**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modfetch/codehost`
- `src/cmd/go/internal/vcs`

**Predicted Directories (3):**
- ❌ `lib/time`
- ❌ `src/runtime`
- ❌ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modfetch/codehost/vcs.go`
- `src/cmd/go/internal/vcs/vcs.go`

**Predicted Files (7):**
- ❌ `lib/time/mkzip.go`
- ❌ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ❌ `src/time/format.go`
- ❌ `src/time/format_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #34293**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/doc`

**Predicted Directories (11):**
- ❌ `cmd/go`
- ❌ `go/doc`
- ❌ `internal/lsp/cmd`
- ❌ `internal/lsp/source`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/doc`
- ❌ `src/cmd/go/internal/modcmd`
- ❌ `src/go/doc`
- ❌ `src/go/internal/doc`
- ❌ `src/net/http`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/doc/main.go`
- `src/cmd/doc/pkg.go`

**Predicted Files (17):**
- ❌ `cmd/go/doc.go`
- ❌ `go/doc/doc.go`
- ❌ `internal/lsp/cmd/definition.go`
- ❌ `internal/lsp/source/comment.go`
- ❌ `src/cmd/go/doc.go`
- ❌ `src/cmd/go/internal/doc/comment.go`
- ❌ `src/cmd/go/internal/doc/doc.go`
- ❌ `src/cmd/go/internal/modcmd/editModuleJSON.go`
- ❌ `src/go/doc/comment.go`
- ❌ `src/go/doc/comment_test.go`
- ❌ `src/go/doc/doc.go`
- ❌ `src/go/doc/exports.go`
- ❌ `src/go/doc/package.go`
- ❌ `src/go/doc/synopsis.go`
- ❌ `src/go/internal/doc/doc.go`
- ❌ `src/net/http/doc.go`
- ❌ `src/runtime/doc.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #31804**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/ed25519`

**Predicted Directories (1):**
- ✅ `src/crypto/ed25519`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/ed25519/ed25519.go`
- `src/crypto/ed25519/ed25519_test.go`

**Predicted Files (2):**
- ✅ `src/crypto/ed25519/ed25519.go`
- ✅ `src/crypto/ed25519/ed25519_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/ed25519`


### 📊 **Proposal #43744**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 33.3% | 28.6% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/runtime`
- `src/testing`
- `src/time`

**Predicted Directories (4):**
- ❌ `src/encoding/json`
- ❌ `src/encoding/json/v2`
- ✅ `src/testing`
- ❌ `src/testing/benchstat`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 33.3% | 20.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/proc.go`
- `src/testing/benchmark_test.go`
- `src/time/sleep_test.go`

**Predicted Files (7):**
- ❌ `src/encoding/json/bench_test.go`
- ❌ `src/encoding/json/v2/bench_test.go`
- ❌ `src/testing/benchmark.go`
- ✅ `src/testing/benchmark_test.go`
- ❌ `src/testing/benchstat/bench.go`
- ❌ `src/testing/benchstat/bench_test.go`
- ❌ `src/testing/testing.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 33.3% | 33.3% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #47916**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 33.3% | 25.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/types2`
- `src/go/types`

**Predicted Directories (5):**
- ✅ `src/go/types`
- ❌ `src/types`
- ❌ `src/types/testdata`
- ❌ `src/types2`
- ❌ `typeparam`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.2% | 80.0% | 19.6% | 16/20 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (20):**
- `src/cmd/compile/internal/noder/writer.go`
- `src/cmd/compile/internal/types2/call.go`
- `src/cmd/compile/internal/types2/lookup.go`
- `src/cmd/compile/internal/types2/signature.go`
- `src/go/types/api_test.go`
- `src/go/types/assignments.go`
- `src/go/types/call.go`
- `src/go/types/check.go`
- `src/go/types/context.go`
- `src/go/types/decl.go`
- `src/go/types/index.go`
- `src/go/types/instantiate.go`
- `src/go/types/instantiate_test.go`
- `src/go/types/lookup.go`
- `src/go/types/object.go`
- `src/go/types/predicates.go`
- `src/go/types/signature.go`
- `src/go/types/subst.go`
- `src/go/types/typelists.go`
- `src/go/types/typestring.go`

**Predicted Files (143):**
- ❌ `src/go/types/alias.go`
- ❌ `src/go/types/api.go`
- ✅ `src/go/types/api_test.go`
- ❌ `src/go/types/array.go`
- ✅ `src/go/types/assignments.go`
- ❌ `src/go/types/badlinkname.go`
- ❌ `src/go/types/basic.go`
- ❌ `src/go/types/builtins.go`
- ❌ `src/go/types/builtins_test.go`
- ✅ `src/go/types/call.go`
- ❌ `src/go/types/chan.go`
- ✅ `src/go/types/check.go`
- ❌ `src/go/types/check_test.go`
- ❌ `src/go/types/commentMap_test.go`
- ❌ `src/go/types/const.go`
- ✅ `src/go/types/context.go`
- ❌ `src/go/types/context_test.go`
- ❌ `src/go/types/conversions.go`
- ✅ `src/go/types/decl.go`
- ❌ `src/go/types/errorcalls_test.go`
- ❌ `src/go/types/errors.go`
- ❌ `src/go/types/errors_test.go`
- ❌ `src/go/types/errsupport.go`
- ❌ `src/go/types/eval.go`
- ❌ `src/go/types/eval_test.go`
- ❌ `src/go/types/example_test.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/exprstring.go`
- ❌ `src/go/types/exprstring_test.go`
- ❌ `src/go/types/format.go`
- ❌ `src/go/types/gccgosizes.go`
- ❌ `src/go/types/gcsizes.go`
- ❌ `src/go/types/generate.go`
- ❌ `src/go/types/generate_test.go`
- ❌ `src/go/types/gotype.go`
- ❌ `src/go/types/hilbert_test.go`
- ✅ `src/go/types/index.go`
- ❌ `src/go/types/infer.go`
- ❌ `src/go/types/initorder.go`
- ✅ `src/go/types/instantiate.go`
- ✅ `src/go/types/instantiate_test.go`
- ❌ `src/go/types/interface.go`
- ❌ `src/go/types/issues_test.go`
- ❌ `src/go/types/iter.go`
- ❌ `src/go/types/labels.go`
- ❌ `src/go/types/literals.go`
- ✅ `src/go/types/lookup.go`
- ❌ `src/go/types/lookup_test.go`
- ❌ `src/go/types/main_test.go`
- ❌ `src/go/types/map.go`
- ❌ `src/go/types/methodset.go`
- ❌ `src/go/types/methodset_test.go`
- ❌ `src/go/types/mono.go`
- ❌ `src/go/types/mono_test.go`
- ❌ `src/go/types/named.go`
- ❌ `src/go/types/named_test.go`
- ✅ `src/go/types/object.go`
- ❌ `src/go/types/object_test.go`
- ❌ `src/go/types/objset.go`
- ❌ `src/go/types/operand.go`
- ❌ `src/go/types/package.go`
- ❌ `src/go/types/pointer.go`
- ✅ `src/go/types/predicates.go`
- ❌ `src/go/types/range.go`
- ❌ `src/go/types/recording.go`
- ❌ `src/go/types/resolver.go`
- ❌ `src/go/types/resolver_test.go`
- ❌ `src/go/types/return.go`
- ❌ `src/go/types/scope.go`
- ❌ `src/go/types/scope2.go`
- ❌ `src/go/types/scope2_test.go`
- ❌ `src/go/types/selection.go`
- ❌ `src/go/types/self_test.go`
- ✅ `src/go/types/signature.go`
- ❌ `src/go/types/sized_test.go`
- ❌ `src/go/types/sizes.go`
- ❌ `src/go/types/sizes_test.go`
- ❌ `src/go/types/slice.go`
- ❌ `src/go/types/stdlib_test.go`
- ❌ `src/go/types/stmt.go`
- ❌ `src/go/types/struct.go`
- ✅ `src/go/types/subst.go`
- ❌ `src/go/types/termlist.go`
- ❌ `src/go/types/termlist_test.go`
- ❌ `src/go/types/token_test.go`
- ❌ `src/go/types/tuple.go`
- ❌ `src/go/types/type.go`
- ✅ `src/go/types/typelists.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/go/types/typeset.go`
- ❌ `src/go/types/typeset_test.go`
- ✅ `src/go/types/typestring.go`
- ❌ `src/go/types/typestring_test.go`
- ❌ `src/go/types/typeterm.go`
- ❌ `src/go/types/typeterm_test.go`
- ❌ `src/go/types/typexpr.go`
- ❌ `src/go/types/under.go`
- ❌ `src/go/types/unify.go`
- ❌ `src/go/types/union.go`
- ❌ `src/go/types/universe.go`
- ❌ `src/go/types/util.go`
- ❌ `src/go/types/util_test.go`
- ❌ `src/go/types/validtype.go`
- ❌ `src/go/types/version.go`
- ❌ `src/go/types/version_test.go`
- ❌ `src/types/testdata/typeparams.go`
- ❌ `src/types/type.go`
- ❌ `src/types/type_test.go`
- ❌ `src/types2/typeparam.go`
- ❌ `typeparam/absdiffimp.go`
- ❌ `typeparam/aliasimp.go`
- ❌ `typeparam/chansimp.go`
- ❌ `typeparam/factimp.go`
- ❌ `typeparam/gencrawler.go`
- ❌ `typeparam/geninline.go`
- ❌ `typeparam/issue46461.go`
- ❌ `typeparam/issue47514.go`
- ❌ `typeparam/issue47892.go`
- ❌ `typeparam/issue48185a.go`
- ❌ `typeparam/issue48185b.go`
- ❌ `typeparam/issue48280.go`
- ❌ `typeparam/issue48306.go`
- ❌ `typeparam/issue48337a.go`
- ❌ `typeparam/issue48337b.go`
- ❌ `typeparam/issue48454.go`
- ❌ `typeparam/issue48462.go`
- ❌ `typeparam/issue50121.go`
- ❌ `typeparam/issue50121b.go`
- ❌ `typeparam/issue50481b.go`
- ❌ `typeparam/issue50481c.go`
- ❌ `typeparam/issue50552.go`
- ❌ `typeparam/issue50561.go`
- ❌ `typeparam/issue51219.go`
- ❌ `typeparam/issue51219b.go`
- ❌ `typeparam/issue51836.go`
- ❌ `typeparam/issue52117.go`
- ❌ `typeparam/issue54302.go`
- ❌ `typeparam/listimp.go`
- ❌ `typeparam/mapimp.go`
- ❌ `typeparam/mutualimp.go`
- ❌ `typeparam/orderedmapsimp.go`
- ❌ `typeparam/structinit.go`
- ❌ `typeparam/valimp.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.2% | 80.0% | 25.6% | 16/20 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/types`


### 📊 **Proposal #40356**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods`

**Predicted Directories (34):**
- ❌ `src/cmd/vet`
- ❌ `src/cmd/vet/testdata/appends`
- ❌ `src/cmd/vet/testdata/assign`
- ❌ `src/cmd/vet/testdata/atomic`
- ❌ `src/cmd/vet/testdata/bool`
- ❌ `src/cmd/vet/testdata/buildtag`
- ❌ `src/cmd/vet/testdata/cgo`
- ❌ `src/cmd/vet/testdata/composite`
- ❌ `src/cmd/vet/testdata/copylock`
- ❌ `src/cmd/vet/testdata/deadcode`
- ❌ `src/cmd/vet/testdata/directive`
- ❌ `src/cmd/vet/testdata/hostport`
- ❌ `src/cmd/vet/testdata/httpresponse`
- ❌ `src/cmd/vet/testdata/lostcancel`
- ❌ `src/cmd/vet/testdata/method`
- ❌ `src/cmd/vet/testdata/nilfunc`
- ❌ `src/cmd/vet/testdata/print`
- ❌ `src/cmd/vet/testdata/rangeloop`
- ❌ `src/cmd/vet/testdata/shift`
- ❌ `src/cmd/vet/testdata/slog`
- ❌ `src/cmd/vet/testdata/stdversion`
- ❌ `src/cmd/vet/testdata/structtag`
- ❌ `src/cmd/vet/testdata/tagtest`
- ❌ `src/cmd/vet/testdata/testingpkg`
- ❌ `src/cmd/vet/testdata/unmarshal`
- ❌ `src/cmd/vet/testdata/unsafeptr`
- ❌ `src/cmd/vet/testdata/unused`
- ❌ `src/cmd/vet/testdata/waitgroup`
- ❌ `src/errors`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/runtime`
- ❌ `src/types`
- ❌ `src/types/errors`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf/printf.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer/sigchanyzer.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods/stdmethods.go`

**Predicted Files (42):**
- ❌ `src/cmd/vet/doc.go`
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/testdata/appends/appends.go`
- ❌ `src/cmd/vet/testdata/assign/assign.go`
- ❌ `src/cmd/vet/testdata/atomic/atomic.go`
- ❌ `src/cmd/vet/testdata/bool/bool.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag.go`
- ❌ `src/cmd/vet/testdata/cgo/cgo.go`
- ❌ `src/cmd/vet/testdata/composite/composite.go`
- ❌ `src/cmd/vet/testdata/copylock/copylock.go`
- ❌ `src/cmd/vet/testdata/deadcode/deadcode.go`
- ❌ `src/cmd/vet/testdata/directive/directive.go`
- ❌ `src/cmd/vet/testdata/hostport/hostport.go`
- ❌ `src/cmd/vet/testdata/httpresponse/httpresponse.go`
- ❌ `src/cmd/vet/testdata/lostcancel/lostcancel.go`
- ❌ `src/cmd/vet/testdata/method/method.go`
- ❌ `src/cmd/vet/testdata/nilfunc/nilfunc.go`
- ❌ `src/cmd/vet/testdata/print/print.go`
- ❌ `src/cmd/vet/testdata/rangeloop/rangeloop.go`
- ❌ `src/cmd/vet/testdata/shift/shift.go`
- ❌ `src/cmd/vet/testdata/slog/slog.go`
- ❌ `src/cmd/vet/testdata/stdversion/stdversion.go`
- ❌ `src/cmd/vet/testdata/structtag/structtag.go`
- ❌ `src/cmd/vet/testdata/tagtest/file1.go`
- ❌ `src/cmd/vet/testdata/tagtest/file2.go`
- ❌ `src/cmd/vet/testdata/testingpkg/tests.go`
- ❌ `src/cmd/vet/testdata/unmarshal/unmarshal.go`
- ❌ `src/cmd/vet/testdata/unsafeptr/unsafeptr.go`
- ❌ `src/cmd/vet/testdata/unused/unused.go`
- ❌ `src/cmd/vet/testdata/waitgroup/waitgroup.go`
- ❌ `src/cmd/vet/vet.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/errors/errors.go`
- ❌ `src/errors/errors_test.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/runtime/error.go`
- ❌ `src/types/errors.go`
- ❌ `src/types/errors/codes.go`
- ❌ `src/types/errors/codes_test.go`
- ❌ `src/types/errors_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #40034**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/smtp`

**Predicted Directories (1):**
- ✅ `src/net/smtp`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/smtp/smtp.go`
- `src/net/smtp/smtp_test.go`

**Predicted Files (2):**
- ✅ `src/net/smtp/smtp.go`
- ✅ `src/net/smtp/smtp_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/smtp`


### 📊 **Proposal #53002**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (2):**
- ❌ `src/go/internal`
- ✅ `src/net/http/httputil`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/net/http/httputil/example_test.go`
- `src/net/http/httputil/reverseproxy.go`
- `src/net/http/httputil/reverseproxy_test.go`

**Predicted Files (4):**
- ❌ `src/go/internal/httputils.go`
- ❌ `src/net/http/httputil/httputil.go`
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http/httputil`


### 📊 **Proposal #44196**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (2):**
- ❌ `lib/time`
- ✅ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/time.go`
- `src/time/time_test.go`

**Predicted Files (3):**
- ❌ `lib/time/mkzip.go`
- ✅ `src/time/time.go`
- ✅ `src/time/time_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #50465**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (1):**
- ✅ `src/net/http/httputil`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/httputil/reverseproxy.go`
- `src/net/http/httputil/reverseproxy_test.go`

**Predicted Files (2):**
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http/httputil`


### 📊 **Proposal #41696**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/dist`
- `src/cmd/go`
- `src/cmd/go/internal/test`
- `src/cmd/go/internal/work`
- `src/cmd/link`

**Predicted Directories (7):**
- ❌ `cmd`
- ❌ `cmd/go/buildid`
- ❌ `cmd/go/cgo/internal/test`
- ❌ `src/cmd/go/internal/modcmd`
- ❌ `src/cmd/go/internal/objabi`
- ❌ `src/cmd/go/internal/objfile`
- ❌ `src/go/build`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/test/test.go`
- `src/cmd/go/internal/test/testflag.go`
- `src/cmd/go/internal/work/build.go`
- `src/cmd/link/dwarf_test.go`

**Predicted Files (36):**
- ❌ `cmd/go`
- ❌ `cmd/go/buildid/buildid.go`
- ❌ `cmd/go/cgo/internal/test/cgo_test.go`
- ❌ `cmd/go/cgo/internal/test/test.go`
- ❌ `src/cmd/go/internal/modcmd/edit.go`
- ❌ `src/cmd/go/internal/modcmd/init.go`
- ❌ `src/cmd/go/internal/modcmd/sync.go`
- ❌ `src/cmd/go/internal/modcmd/use.go`
- ❌ `src/cmd/go/internal/modcmd/vendor.go`
- ❌ `src/cmd/go/internal/modcmd/work.go`
- ❌ `src/cmd/go/internal/objabi/autotype.go`
- ❌ `src/cmd/go/internal/objabi/flag.go`
- ❌ `src/cmd/go/internal/objabi/flag_test.go`
- ❌ `src/cmd/go/internal/objabi/funcid.go`
- ❌ `src/cmd/go/internal/objabi/head.go`
- ❌ `src/cmd/go/internal/objabi/line.go`
- ❌ `src/cmd/go/internal/objabi/path.go`
- ❌ `src/cmd/go/internal/objabi/reloctype.go`
- ❌ `src/cmd/go/internal/objabi/reloctype_string.go`
- ❌ `src/cmd/go/internal/objabi/stack.go`
- ❌ `src/cmd/go/internal/objabi/symkind.go`
- ❌ `src/cmd/go/internal/objabi/symkind_string.go`
- ❌ `src/cmd/go/internal/objabi/util.go`
- ❌ `src/cmd/go/internal/objfile/elf.go`
- ❌ `src/cmd/go/internal/objfile/elf_test.go`
- ❌ `src/cmd/go/internal/objfile/macho.go`
- ❌ `src/cmd/go/internal/objfile/macho_test.go`
- ❌ `src/cmd/go/internal/objfile/objfile.go`
- ❌ `src/cmd/go/internal/objfile/pe.go`
- ❌ `src/cmd/go/internal/objfile/pe_test.go`
- ❌ `src/cmd/go/internal/objfile/plan9obj.go`
- ❌ `src/cmd/go/internal/objfile/plan9obj_test.go`
- ❌ `src/cmd/go/internal/objfile/xcoff.go`
- ❌ `src/cmd/go/internal/objfile/xcoff_test.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #46336**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 1.2% | 2.3% | 1/86 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (86):**
- `src/archive/tar`
- `src/cmd/asm/internal/asm`
- `src/cmd/asm/internal/lex`
- `src/cmd/cgo`
- `src/cmd/compile/internal/base`
- `src/cmd/compile/internal/liveness`
- `src/cmd/compile/internal/logopt`
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/ssa`
- `src/cmd/dist`
- `src/cmd/doc`
- `src/cmd/fix`
- `src/cmd/go`
- `src/cmd/go/internal/base`
- `src/cmd/go/internal/cache`
- `src/cmd/go/internal/cmdflag`
- `src/cmd/go/internal/envcmd`
- `src/cmd/go/internal/imports`
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modfetch/codehost`
- `src/cmd/go/internal/modget`
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/mvs`
- `src/cmd/go/internal/search`
- `src/cmd/go/internal/test`
- `src/cmd/go/internal/vcs`
- `src/cmd/go/internal/vet`
- `src/cmd/go/internal/work`
- `src/cmd/go/testdata`
- `src/cmd/gofmt`
- `src/cmd/internal/obj`
- `src/cmd/internal/test2json`
- `src/cmd/link/internal/ld`
- `src/cmd/vendor/github.com/google/pprof/internal/binutils`
- `src/cmd/vendor/github.com/google/pprof/internal/driver`
- `src/cmd/vendor/github.com/google/pprof/internal/report`
- `src/cmd/vendor/github.com/google/pprof/profile`
- `src/cmd/vendor/golang.org/x/arch/ppc64/ppc64asm`
- `src/cmd/vendor/golang.org/x/mod/modfile`
- `src/cmd/vendor/golang.org/x/mod/module`
- `src/cmd/vendor/golang.org/x/mod/sumdb`
- `src/cmd/vendor/golang.org/x/mod/sumdb/note`
- `src/cmd/vendor/golang.org/x/sys/plan9`
- `src/cmd/vendor/golang.org/x/sys/unix`
- `src/cmd/vendor/golang.org/x/sys/windows`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/framepointer`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- `src/cmd/vet`
- `src/crypto/ecdsa`
- `src/crypto/tls`
- `src/crypto/x509`
- `src/encoding/asn1`
- `src/encoding/json`
- `src/encoding/xml`
- `src/fmt`
- `src/go/build`
- `src/go/constant`
- `src/go/doc`
- `src/go/importer`
- `src/go/printer`
- `src/go/types`
- `src/html/template`
- `src/internal/goroot`
- `src/math/big`
- `src/mime`
- `src/net`
- `src/net/http`
- `src/net/http/cgi`
- `src/net/mail`
- `src/net/smtp`
- `src/net/url`
- `src/os`
- `src/os/exec`
- `src/os/user`
- `src/regexp`
- `src/regexp/syntax`
- `src/runtime/pprof`
- `src/strconv`
- `src/strings`
- `src/testing/fstest`
- `src/vendor/golang.org/x/net/http/httpguts`
- `src/vendor/golang.org/x/net/idna`
- `src/vendor/golang.org/x/sys/cpu`

**Predicted Directories (2):**
- ❌ `src/bytes`
- ✅ `src/strings`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 0.7% | 1.4% | 1/134 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (134):**
- `src/archive/tar/strconv.go`
- `src/archive/tar/writer_test.go`
- `src/cmd/asm/internal/asm/operand_test.go`
- `src/cmd/asm/internal/lex/input.go`
- `src/cmd/cgo/gcc.go`
- `src/cmd/cgo/godefs.go`
- `src/cmd/cgo/out.go`
- `src/cmd/compile/internal/base/flag.go`
- `src/cmd/compile/internal/liveness/plive.go`
- `src/cmd/compile/internal/logopt/log_opts.go`
- `src/cmd/compile/internal/noder/noder.go`
- `src/cmd/compile/internal/ssa/debug_test.go`
- `src/cmd/compile/internal/ssa/html.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/imports.go`
- `src/cmd/dist/test.go`
- `src/cmd/doc/dirs.go`
- `src/cmd/doc/pkg.go`
- `src/cmd/fix/typecheck.go`
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/base/base.go`
- `src/cmd/go/internal/base/goflags.go`
- `src/cmd/go/internal/cache/hash.go`
- `src/cmd/go/internal/cmdflag/flag.go`
- `src/cmd/go/internal/envcmd/env.go`
- `src/cmd/go/internal/imports/build.go`
- `src/cmd/go/internal/imports/read_test.go`
- `src/cmd/go/internal/load/flag.go`
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/modcmd/edit.go`
- `src/cmd/go/internal/modfetch/codehost/vcs.go`
- `src/cmd/go/internal/modget/query.go`
- `src/cmd/go/internal/modload/build.go`
- `src/cmd/go/internal/modload/init.go`
- `src/cmd/go/internal/modload/list.go`
- `src/cmd/go/internal/modload/modfile.go`
- `src/cmd/go/internal/modload/query.go`
- `src/cmd/go/internal/mvs/mvs_test.go`
- `src/cmd/go/internal/search/search.go`
- `src/cmd/go/internal/test/test.go`
- `src/cmd/go/internal/vcs/vcs.go`
- `src/cmd/go/internal/vet/vetflag.go`
- `src/cmd/go/internal/work/build.go`
- `src/cmd/go/internal/work/buildid.go`
- `src/cmd/go/internal/work/gccgo.go`
- `src/cmd/go/proxy_test.go`
- `src/cmd/go/testdata/addmod.go`
- `src/cmd/gofmt/gofmt_test.go`
- `src/cmd/internal/obj/stringer.go`
- `src/cmd/internal/test2json/test2json.go`
- `src/cmd/link/internal/ld/data.go`
- `src/cmd/link/internal/ld/dwarf.go`
- `src/cmd/link/internal/ld/go.go`
- `src/cmd/link/internal/ld/ld.go`
- `src/cmd/link/internal/ld/main.go`
- `src/cmd/link/internal/ld/pe.go`
- `src/cmd/vendor/github.com/google/pprof/internal/binutils/addr2liner.go`
- `src/cmd/vendor/github.com/google/pprof/internal/binutils/binutils.go`
- `src/cmd/vendor/github.com/google/pprof/internal/driver/commands.go`
- `src/cmd/vendor/github.com/google/pprof/internal/driver/driver_focus.go`
- `src/cmd/vendor/github.com/google/pprof/internal/driver/interactive.go`
- `src/cmd/vendor/github.com/google/pprof/internal/report/source.go`
- `src/cmd/vendor/github.com/google/pprof/profile/legacy_profile.go`
- `src/cmd/vendor/golang.org/x/arch/ppc64/ppc64asm/plan9.go`
- `src/cmd/vendor/golang.org/x/mod/modfile/rule.go`
- `src/cmd/vendor/golang.org/x/mod/module/module.go`
- `src/cmd/vendor/golang.org/x/mod/sumdb/note/note.go`
- `src/cmd/vendor/golang.org/x/mod/sumdb/server.go`
- `src/cmd/vendor/golang.org/x/sys/plan9/syscall.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall.go`
- `src/cmd/vendor/golang.org/x/sys/unix/xattr_bsd.go`
- `src/cmd/vendor/golang.org/x/sys/windows/syscall.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl/asmdecl.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/framepointer/framepointer.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- `src/cmd/vet/vet_test.go`
- `src/crypto/ecdsa/ecdsa_test.go`
- `src/crypto/tls/handshake_test.go`
- `src/crypto/x509/pem_decrypt.go`
- `src/encoding/asn1/common.go`
- `src/encoding/json/tags.go`
- `src/encoding/xml/typeinfo.go`
- `src/encoding/xml/xml.go`
- `src/fmt/fmt_test.go`
- `src/go/build/build.go`
- `src/go/build/build_test.go`
- `src/go/build/read.go`
- `src/go/build/read_test.go`
- `src/go/constant/value_test.go`
- `src/go/doc/headscan.go`
- `src/go/importer/importer_test.go`
- `src/go/printer/nodes.go`
- `src/go/printer/printer.go`
- `src/go/types/eval_test.go`
- `src/html/template/attr.go`
- `src/html/template/js.go`
- `src/html/template/url.go`
- `src/internal/goroot/gc.go`
- `src/math/big/ratconv.go`
- `src/mime/encodedword.go`
- `src/mime/mediatype.go`
- `src/net/http/cgi/child.go`
- `src/net/http/cgi/host.go`
- `src/net/http/cgi/host_test.go`
- `src/net/http/client_test.go`
- `src/net/http/cookie.go`
- `src/net/http/fs.go`
- `src/net/http/main_test.go`
- `src/net/http/request.go`
- `src/net/http/response.go`
- `src/net/http/server.go`
- `src/net/http/transport.go`
- `src/net/mail/message.go`
- `src/net/main_test.go`
- `src/net/smtp/smtp.go`
- `src/net/url/url.go`
- `src/os/exec/exec.go`
- `src/os/exec/exec_test.go`
- `src/os/os_test.go`
- `src/os/user/cgo_lookup_unix.go`
- `src/os/user/lookup_unix.go`
- `src/regexp/exec_test.go`
- `src/regexp/syntax/parse.go`
- `src/runtime/pprof/pprof_test.go`
- `src/runtime/pprof/proto_test.go`
- `src/strconv/fp_test.go`
- `src/strings/strings.go`
- `src/testing/fstest/mapfs.go`
- `src/testing/fstest/testfs.go`
- `src/vendor/golang.org/x/net/http/httpguts/httplex.go`
- `src/vendor/golang.org/x/net/idna/idna10.0.0.go`
- `src/vendor/golang.org/x/net/idna/idna9.0.0.go`
- `src/vendor/golang.org/x/sys/cpu/cpu.go`

**Predicted Files (6):**
- ❌ `src/bytes/bytes.go`
- ❌ `src/strings/builder.go`
- ❌ `src/strings/compare.go`
- ❌ `src/strings/replace.go`
- ❌ `src/strings/search.go`
- ✅ `src/strings/strings.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 0.7% | 1.4% | 1/134 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/strings`


### 📊 **Proposal #44011**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 66.7% | 33.3% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/os`
- `src/os/exec`
- `src/syscall`

**Predicted Directories (9):**
- ❌ `src/internal/lockedfile`
- ❌ `src/internal/lockedfile/internal/filelock`
- ✅ `src/os/exec`
- ❌ `src/os/exec/internal/fdtest`
- ❌ `src/runtime`
- ❌ `src/sys`
- ✅ `src/syscall`
- ❌ `src/syscall/execenv`
- ❌ `src/syscall/windows`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 33.3% | 15.4% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/os/exec/exec_windows_test.go`
- `src/os/file_windows.go`
- `src/syscall/exec_windows.go`
- `src/syscall/exec_windows_test.go`
- `src/syscall/syscall_windows.go`
- `src/syscall/zsyscall_windows.go`

**Predicted Files (20):**
- ❌ `src/internal/lockedfile/internal/filelock/filelock.go`
- ❌ `src/internal/lockedfile/internal/filelock/filelock_windows.go`
- ❌ `src/internal/lockedfile/lockedfile.go`
- ❌ `src/internal/lockedfile/lockedfile_filelock.go`
- ❌ `src/internal/lockedfile/lockedfile_plan9.go`
- ❌ `src/internal/lockedfile/lockedfile_test.go`
- ❌ `src/internal/lockedfile/lockedfile_windows.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/exec_windows.go`
- ❌ `src/os/exec/internal/fdtest/exists_plan9.go`
- ❌ `src/os/exec/internal/fdtest/exists_test.go`
- ❌ `src/os/exec/internal/fdtest/exists_unix.go`
- ❌ `src/os/exec/internal/fdtest/exists_windows.go`
- ❌ `src/runtime/syscall_windows.go`
- ❌ `src/sys/syscall_windows.go`
- ✅ `src/syscall/exec_windows.go`
- ❌ `src/syscall/execenv/execenv_windows.go`
- ❌ `src/syscall/syscall.go`
- ✅ `src/syscall/syscall_windows.go`
- ❌ `src/syscall/windows/syscall_windows.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 33.3% | 36.4% | 2/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/os/exec`
- `src/syscall`


### 📊 **Proposal #43620**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (2):**
- ❌ `src/runtime`
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/benchmark.go`
- `src/testing/benchmark_test.go`

**Predicted Files (5):**
- ❌ `src/runtime/testing.go`
- ❌ `src/testing/bench.go`
- ❌ `src/testing/bench_test.go`
- ✅ `src/testing/benchmark.go`
- ✅ `src/testing/benchmark_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #48256**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go`
- `src/cmd/go/internal/workcmd`

**Predicted Directories (6):**
- ❌ `src/cmd/internal/script`
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/internal/modcmd`
- ❌ `src/go/internal/workcmd`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/workcmd/edit.go`
- `src/cmd/go/internal/workcmd/init.go`
- `src/cmd/go/main.go`

**Predicted Files (16):**
- ❌ `src/cmd/internal/script/cmds.go`
- ❌ `src/cmd/internal/script/cmds_nonunix.go`
- ❌ `src/cmd/internal/script/cmds_unix.go`
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/go/internal/modcmd/edit.go`
- ❌ `src/go/internal/modcmd/init.go`
- ❌ `src/go/internal/workcmd/edit.go`
- ❌ `src/go/internal/workcmd/init.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #38017**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/time`
- `src/time/tzdata`

**Predicted Directories (3):**
- ❌ `lib/time`
- ❌ `src/runtime`
- ✅ `src/time/tzdata`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 25.0% | 22.2% | 1/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/time/export_test.go`
- `src/time/tzdata/tzdata.go`
- `src/time/tzdata_test.go`
- `src/time/zoneinfo_read.go`

**Predicted Files (5):**
- ❌ `lib/time/mkzip.go`
- ❌ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ✅ `src/time/tzdata/tzdata.go`
- ❌ `src/time/tzdata/tzdata_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 25.0% | 33.3% | 1/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time/tzdata`


### 📊 **Proposal #50601**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/binary`

**Predicted Directories (4):**
- ✅ `src/encoding/binary`
- ❌ `src/issue15646.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 100.0% | 30.8% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/binary/binary.go`
- `src/encoding/binary/binary_test.go`

**Predicted Files (11):**
- ✅ `src/encoding/binary/binary.go`
- ✅ `src/encoding/binary/binary_test.go`
- ❌ `src/issue15646.dir/a.go`
- ❌ `src/issue15646.dir/b.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/binary`


### 📊 **Proposal #50842**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (4):**
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/io`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 66.7% | 30.8% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/io/io.go`
- `src/io/multi.go`
- `src/io/multi_test.go`

**Predicted Files (10):**
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ✅ `src/io/multi.go`
- ❌ `src/io/multi_reader.go`
- ✅ `src/io/multi_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io`


### 📊 **Proposal #41790**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/database/sql`

**Predicted Directories (6):**
- ❌ `src/database`
- ✅ `src/database/sql`
- ❌ `src/database/sql/driver`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16317.dir`
- ❌ `src/fixedbugs/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 33.3% | 13.3% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/database/sql/fakedb_test.go`
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`

**Predicted Files (12):**
- ❌ `src/database/sql/`
- ❌ `src/database/sql/driver/driver.go`
- ✅ `src/database/sql/sql.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16317.dir/a.go`
- ❌ `src/fixedbugs/issue16317.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/database/sql`


### 📊 **Proposal #5901**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/json`

**Predicted Directories (5):**
- ❌ `src/archive/tar`
- ❌ `src/archive/zip`
- ✅ `src/encoding/json`
- ❌ `src/encoding/json/jsontext`
- ❌ `src/syscall/js`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.4% | 50.0% | 23.5% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/encoding/json/bench_test.go`
- `src/encoding/json/decode.go`
- `src/encoding/json/encode.go`
- `src/encoding/json/stream.go`

**Predicted Files (13):**
- ❌ `src/archive/tar/reader.go`
- ❌ `src/archive/tar/writer.go`
- ❌ `src/archive/zip/reader.go`
- ❌ `src/archive/zip/writer.go`
- ✅ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decoder.go`
- ✅ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encoder.go`
- ❌ `src/encoding/json/internal.go`
- ❌ `src/encoding/json/jsontext/decode.go`
- ❌ `src/encoding/json/jsontext/encode.go`
- ❌ `src/syscall/js/js.go`
- ❌ `src/syscall/js/js_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 50.0% | 44.4% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/json`


### 📊 **Proposal #52792**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modload`

**Predicted Directories (2):**
- ❌ `src/cmd/go/internal/modinfo`
- ✅ `src/cmd/go/internal/modload`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modfetch/fetch.go`
- `src/cmd/go/internal/modload/build.go`

**Predicted Files (2):**
- ❌ `src/cmd/go/internal/modinfo/info.go`
- ❌ `src/cmd/go/internal/modload/list.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/modload`


### 📊 **Proposal #28308**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 4.3% | 7.4% | 1/23 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (23):**
- `src/cmd/vendor/golang.org/x/sys/unix`
- `src/cmd/vendor/golang.org/x/text/language`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/composite`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/copylock`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/hostport`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/lostcancel`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/nilfunc`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/unreachable`
- `src/cmd/vendor/golang.org/x/tools/go/types/typeutil`
- `src/cmd/vendor/golang.org/x/tools/internal/analysisinternal`
- `src/cmd/vendor/golang.org/x/tools/internal/astutil`
- `src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor`
- `src/cmd/vendor/golang.org/x/tools/internal/bisect`
- `src/cmd/vendor/golang.org/x/tools/internal/typeparams`
- `src/cmd/vendor/golang.org/x/tools/internal/typesinternal`
- `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex`
- `src/cmd/vet`
- `src/cmd/vet/testdata/hostport`
- `src/net/http`
- `src/vendor/golang.org/x/crypto/cryptobyte`
- `src/vendor/golang.org/x/sys/cpu`

**Predicted Directories (4):**
- ❌ `src`
- ✅ `src/cmd/vet`
- ❌ `src/cmd/vet/hostport`
- ❌ `src/net`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/34 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (34):**
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`
- `src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`
- `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
- `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
- `src/cmd/vendor/golang.org/x/text/language/parse.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/composite/composite.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/copylock/copylock.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/hostport/hostport.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/lostcancel/lostcancel.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/nilfunc/nilfunc.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/testinggoroutine.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/util.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/unreachable/unreachable.go`
- `src/cmd/vendor/golang.org/x/tools/go/types/typeutil/callee.go`
- `src/cmd/vendor/golang.org/x/tools/internal/analysisinternal/analysis.go`
- `src/cmd/vendor/golang.org/x/tools/internal/astutil/clone.go`
- `src/cmd/vendor/golang.org/x/tools/internal/astutil/comment.go`
- `src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor/cursor.go`
- `src/cmd/vendor/golang.org/x/tools/internal/astutil/util.go`
- `src/cmd/vendor/golang.org/x/tools/internal/bisect/bisect.go`
- `src/cmd/vendor/golang.org/x/tools/internal/typeparams/free.go`
- `src/cmd/vendor/golang.org/x/tools/internal/typeparams/termlist.go`
- `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/classify_call.go`
- `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`
- `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/types.go`
- `src/cmd/vet/main.go`
- `src/cmd/vet/testdata/hostport/hostport.go`
- `src/cmd/vet/vet_test.go`
- `src/net/http/h2_bundle.go`
- `src/vendor/golang.org/x/crypto/cryptobyte/asn1.go`
- `src/vendor/golang.org/x/sys/cpu/cpu_linux_loong64.go`
- `src/vendor/golang.org/x/sys/cpu/cpu_loong64.go`
- `src/vendor/golang.org/x/sys/cpu/parse.go`

**Predicted Files (5):**
- ❌ `src/cmd/vet/hostport/hostport.go`
- ❌ `src/cmd/vet/vet.go`
- ❌ `src/net.go`
- ❌ `src/net/dial.go`
- ❌ `src/net/net.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/34 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/vet`


### 📊 **Proposal #44006**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall/js`

**Predicted Directories (1):**
- ✅ `src/syscall/js`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/syscall/js/js.go`

**Predicted Files (4):**
- ✅ `src/syscall/js/js.go`
- ❌ `wasmexport.go`
- ❌ `wasmexport2.go`
- ❌ `wasmmemsize.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall/js`


### 📊 **Proposal #53021**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/cipher`
- `src/crypto/subtle`

**Predicted Directories (3):**
- ❌ `src/bytes`
- ✅ `src/crypto/cipher`
- ✅ `src/crypto/subtle`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 16.7% | 18.2% | 1/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/crypto/cipher/cbc.go`
- `src/crypto/cipher/cfb.go`
- `src/crypto/cipher/ctr.go`
- `src/crypto/cipher/ofb.go`
- `src/crypto/subtle/xor.go`
- `src/crypto/subtle/xor_test.go`

**Predicted Files (5):**
- ❌ `src/bytes/bytes.go`
- ❌ `src/crypto/cipher/xor.go`
- ❌ `src/crypto/cipher/xor_generic.go`
- ✅ `src/crypto/subtle/xor.go`
- ❌ `src/crypto/subtle/xor_generic.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 16.7% | 20.0% | 1/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/crypto/cipher`
- `src/crypto/subtle`


### 📊 **Proposal #49580**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 25.0% | 25.0% | 1/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `src/archive/tar`
- `src/io/fs`
- `src/os`
- `src/testing/fstest`

**Predicted Directories (4):**
- ❌ `src/archive/zip`
- ❌ `src/go/internal/fsys`
- ✅ `src/io/fs`
- ❌ `src/path/filepath`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 14.3% | 16.7% | 2/14 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (14):**
- `src/archive/tar/writer.go`
- `src/archive/tar/writer_test.go`
- `src/io/fs/readlink.go`
- `src/io/fs/readlink_test.go`
- `src/io/fs/sub.go`
- `src/io/fs/walk_test.go`
- `src/os/dir.go`
- `src/os/file.go`
- `src/os/file_test.go`
- `src/os/os_test.go`
- `src/testing/fstest/mapfs.go`
- `src/testing/fstest/mapfs_test.go`
- `src/testing/fstest/testfs.go`
- `src/testing/fstest/testfs_test.go`

**Predicted Files (10):**
- ❌ `src/archive/zip/reader.go`
- ❌ `src/archive/zip/writer.go`
- ❌ `src/go/internal/fsys/fsys.go`
- ❌ `src/go/internal/fsys/fsys_test.go`
- ❌ `src/io/fs/fs.go`
- ✅ `src/io/fs/readlink.go`
- ✅ `src/io/fs/readlink_test.go`
- ❌ `src/path/filepath/symlink.go`
- ❌ `src/path/filepath/symlink_unix.go`
- ❌ `src/path/filepath/symlink_windows.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 14.3% | 23.5% | 2/14 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io/fs`


### 📊 **Proposal #53015**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/html/template`
- `src/text/template`
- `src/text/template/parse`

**Predicted Directories (2):**
- ✅ `src/html/template`
- ✅ `src/text/template`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 14.3% | 15.4% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/html/template/escape.go`
- `src/html/template/escape_test.go`
- `src/text/template/exec.go`
- `src/text/template/parse/lex.go`
- `src/text/template/parse/lex_test.go`
- `src/text/template/parse/node.go`
- `src/text/template/parse/parse.go`

**Predicted Files (6):**
- ❌ `return.go`
- ❌ `src/html/template/template.go`
- ❌ `src/html/template/template_test.go`
- ✅ `src/text/template/exec.go`
- ❌ `src/text/template/exec_test.go`
- ❌ `src/text/template/template.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 14.3% | 16.7% | 1/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/html/template`
- `src/text/template`


### 📊 **Proposal #41048**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (5):**
- ❌ `src/issue15920.dir`
- ❌ `src/issue16616.dir`
- ✅ `src/net/http`
- ❌ `vendor/golang.org/x/net/http/httpguts`
- ❌ `vendor/golang.org/x/net/http/httpproxy`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 100.0% | 36.4% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/transport.go`
- `src/net/http/transport_test.go`

**Predicted Files (9):**
- ❌ `src/issue15920.dir/a.go`
- ❌ `src/issue15920.dir/b.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ✅ `src/net/http/transport.go`
- ✅ `src/net/http/transport_test.go`
- ❌ `vendor/golang.org/x/net/http/httpguts/guts.go`
- ❌ `vendor/golang.org/x/net/http/httpproxy/proxy.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http`


### 📊 **Proposal #48409**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/runtime`
- `src/runtime/debug`
- `src/runtime/testdata/testprog`

**Predicted Directories (3):**
- ❌ `internal/runtime/sys`
- ✅ `src/runtime`
- ✅ `src/runtime/debug`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 46.7% | 25.0% | 32.6% | 7/28 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (28):**
- `src/runtime/debug/garbage.go`
- `src/runtime/debug/stubs.go`
- `src/runtime/debuglog.go`
- `src/runtime/export_test.go`
- `src/runtime/gc_test.go`
- `src/runtime/malloc.go`
- `src/runtime/mcache.go`
- `src/runtime/mem.go`
- `src/runtime/metrics.go`
- `src/runtime/mgc.go`
- `src/runtime/mgclimit.go`
- `src/runtime/mgclimit_test.go`
- `src/runtime/mgcmark.go`
- `src/runtime/mgcpacer.go`
- `src/runtime/mgcpacer_test.go`
- `src/runtime/mgcscavenge.go`
- `src/runtime/mgcscavenge_test.go`
- `src/runtime/mgcsweep.go`
- `src/runtime/mheap.go`
- `src/runtime/mpagealloc.go`
- `src/runtime/mpagealloc_32bit.go`
- `src/runtime/mpagealloc_64bit.go`
- `src/runtime/mranges.go`
- `src/runtime/mstats.go`
- `src/runtime/proc.go`
- `src/runtime/string.go`
- `src/runtime/string_test.go`
- `src/runtime/testdata/testprog/gc.go`

**Predicted Files (15):**
- ❌ `gc.go`
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `runtime.go`
- ❌ `src/runtime/debug.go`
- ❌ `src/runtime/debug/debug.go`
- ❌ `src/runtime/debug/doc.go`
- ✅ `src/runtime/debug/garbage.go`
- ❌ `src/runtime/debug/garbage_test.go`
- ❌ `src/runtime/debug/runtime.go`
- ✅ `src/runtime/mgc.go`
- ✅ `src/runtime/mgclimit.go`
- ✅ `src/runtime/mgcmark.go`
- ✅ `src/runtime/mgcpacer.go`
- ✅ `src/runtime/mgcscavenge.go`
- ✅ `src/runtime/mheap.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 58.3% | 25.0% | 35.0% | 7/28 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/runtime`
- `src/runtime/debug`


### 📊 **Proposal #42102**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (1):**
- ✅ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 3/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/time/format.go`
- `src/time/time.go`
- `src/time/time_test.go`
- `src/time/zoneinfo.go`
- `src/time/zoneinfo_read.go`
- `src/time/zoneinfo_test.go`

**Predicted Files (3):**
- ✅ `src/time/time.go`
- ✅ `src/time/time_test.go`
- ✅ `src/time/zoneinfo.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 3/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #39904**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (1):**
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/match.go`
- `src/testing/match_test.go`

**Predicted Files (4):**
- ✅ `src/testing/match.go`
- ✅ `src/testing/match_test.go`
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #42027**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 13.3% | 22.2% | 2/15 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (15):**
- `src/cmd/dist`
- `src/cmd/fix`
- `src/cmd/go`
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/version`
- `src/cmd/go/testdata`
- `src/cmd/gofmt`
- `src/cmd/internal/moddeps`
- `src/compress/gzip`
- `src/go/build`
- `src/go/doc`
- `src/index/suffixarray`
- `src/io/fs`
- `src/path/filepath`
- `test`

**Predicted Directories (3):**
- ❌ `src/go/internal/fsys`
- ✅ `src/io/fs`
- ✅ `src/path/filepath`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.8% | 16.7% | 16.2% | 3/18 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (18):**
- `src/cmd/dist/test.go`
- `src/cmd/fix/main.go`
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/modfetch/fetch.go`
- `src/cmd/go/internal/version/version.go`
- `src/cmd/go/testdata/addmod.go`
- `src/cmd/go/testdata/savedir.go`
- `src/cmd/gofmt/long_test.go`
- `src/cmd/internal/moddeps/moddeps_test.go`
- `src/compress/gzip/issue14937_test.go`
- `src/go/build/deps_test.go`
- `src/go/doc/headscan.go`
- `src/index/suffixarray/suffixarray_test.go`
- `src/io/fs/walk.go`
- `src/io/fs/walk_test.go`
- `src/path/filepath/path.go`
- `src/path/filepath/path_test.go`
- `test/winbatch.go`

**Predicted Files (19):**
- ❌ `src/go/internal/fsys/walk.go`
- ✅ `src/io/fs/walk.go`
- ❌ `src/path/filepath/example_test.go`
- ❌ `src/path/filepath/example_unix_test.go`
- ❌ `src/path/filepath/example_unix_walk_test.go`
- ❌ `src/path/filepath/export_test.go`
- ❌ `src/path/filepath/export_windows_test.go`
- ❌ `src/path/filepath/match.go`
- ❌ `src/path/filepath/match_test.go`
- ✅ `src/path/filepath/path.go`
- ❌ `src/path/filepath/path_plan9.go`
- ✅ `src/path/filepath/path_test.go`
- ❌ `src/path/filepath/path_unix.go`
- ❌ `src/path/filepath/path_windows.go`
- ❌ `src/path/filepath/path_windows_test.go`
- ❌ `src/path/filepath/symlink.go`
- ❌ `src/path/filepath/symlink_plan9.go`
- ❌ `src/path/filepath/symlink_unix.go`
- ❌ `src/path/filepath/symlink_windows.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 16.7% | 16.7% | 3/18 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/io/fs`
- `src/path/filepath`


### 📊 **Proposal #27628**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/cache`
- `src/cmd/go/internal/work`

**Predicted Directories (0):**

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/go/internal/cache/hash.go`
- `src/cmd/go/internal/work/buildid.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/go/internal/work/gc.go`
- `src/cmd/go/internal/work/gccgo.go`

**Predicted Files (0):**

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #51868**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/debug/pe`

**Predicted Directories (3):**
- ✅ `src/debug/pe`
- ❌ `src/issue16616.dir`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/debug/pe/symbol.go`
- `src/debug/pe/symbols_test.go`

**Predicted Files (6):**
- ❌ `src/debug/pe/file.go`
- ❌ `src/debug/pe/pe.go`
- ❌ `src/debug/pe/section.go`
- ✅ `src/debug/pe/symbol.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/runtime/pe.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/debug/pe`


### 📊 **Proposal #28089**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/ast`

**Predicted Directories (3):**
- ✅ `src/go/ast`
- ❌ `src/go/internal/ast`
- ❌ `src/go/parser`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/ast/ast.go`
- `src/go/ast/issues_test.go`

**Predicted Files (5):**
- ✅ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`
- ❌ `src/go/internal/ast/ast.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/parser_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/ast`


### 📊 **Proposal #41773**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/serve_test.go`
- `src/net/http/server.go`

**Predicted Files (1):**
- ✅ `src/net/http/server.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http`


### 📊 **Proposal #50674**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 100.0% | 20.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (9):**
- ❌ `crypto`
- ❌ `src`
- ✅ `src/crypto/x509`
- ❌ `src/crypto/x509/pkix`
- ❌ `src/go/internal/auth`
- ❌ `src/go/internal/cache`
- ❌ `vendor/golang.org/x/crypto/cryptobyte`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/asn1`
- ❌ `vendor/golang.org/x/crypto/x509`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.7% | 33.3% | 6.7% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/x509/parser.go`
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (27):**
- ❌ `crypto/x509`
- ❌ `src/crypto/x509/pkix/pkix.go`
- ✅ `src/crypto/x509/x509.go`
- ❌ `src/go/internal/auth/auth.go`
- ❌ `src/go/internal/auth/auth_test.go`
- ❌ `src/go/internal/auth/gitauth.go`
- ❌ `src/go/internal/auth/gitauth_test.go`
- ❌ `src/go/internal/auth/httputils.go`
- ❌ `src/go/internal/auth/netrc.go`
- ❌ `src/go/internal/auth/netrc_test.go`
- ❌ `src/go/internal/auth/userauth.go`
- ❌ `src/go/internal/auth/userauth_test.go`
- ❌ `src/go/internal/cache/cache.go`
- ❌ `src/go/internal/cache/cache_test.go`
- ❌ `src/go/internal/cache/default.go`
- ❌ `src/go/internal/cache/hash.go`
- ❌ `src/go/internal/cache/hash_test.go`
- ❌ `src/go/internal/cache/prog.go`
- ❌ `src/issue15646.go`
- ❌ `src/issue15920.go`
- ❌ `src/issue16133.go`
- ❌ `src/issue16317.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/asn1.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/asn1/asn1.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/builder.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/string.go`
- ❌ `vendor/golang.org/x/crypto/x509/x509.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #26535**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/compress/lzw`

**Predicted Directories (1):**
- ✅ `src/compress/lzw`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 4/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/compress/lzw/reader.go`
- `src/compress/lzw/reader_test.go`
- `src/compress/lzw/writer.go`
- `src/compress/lzw/writer_test.go`

**Predicted Files (4):**
- ✅ `src/compress/lzw/reader.go`
- ✅ `src/compress/lzw/reader_test.go`
- ✅ `src/compress/lzw/writer.go`
- ✅ `src/compress/lzw/writer_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 4/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/compress/lzw`


### 📊 **Proposal #45964**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (3):**
- ❌ `src/internal/poll`
- ❌ `src/runtime/internal/atomic`
- ✅ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 9.5% | 13.8% | 2/21 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (21):**
- `src/syscall/exec_linux.go`
- `src/syscall/syscall_linux.go`
- `src/syscall/syscall_linux_amd64.go`
- `src/syscall/syscall_linux_arm.go`
- `src/syscall/syscall_linux_mips64x.go`
- `src/syscall/syscall_linux_mipsx.go`
- `src/syscall/syscall_linux_ppc64x.go`
- `src/syscall/syscall_linux_riscv64.go`
- `src/syscall/syscall_linux_s390x.go`
- `src/syscall/zsyscall_linux_386.go`
- `src/syscall/zsyscall_linux_amd64.go`
- `src/syscall/zsyscall_linux_arm.go`
- `src/syscall/zsyscall_linux_arm64.go`
- `src/syscall/zsyscall_linux_mips.go`
- `src/syscall/zsyscall_linux_mips64.go`
- `src/syscall/zsyscall_linux_mips64le.go`
- `src/syscall/zsyscall_linux_mipsle.go`
- `src/syscall/zsyscall_linux_ppc64.go`
- `src/syscall/zsyscall_linux_ppc64le.go`
- `src/syscall/zsyscall_linux_riscv64.go`
- `src/syscall/zsyscall_linux_s390x.go`

**Predicted Files (8):**
- ❌ `src/internal/poll/sock_cloexec.go`
- ❌ `src/internal/poll/sockopt_linux.go`
- ❌ `src/internal/poll/splice_linux.go`
- ❌ `src/runtime/internal/atomic/sys_linux_arm.s`
- ❌ `src/syscall/defs_linux.go`
- ✅ `src/syscall/exec_linux.go`
- ✅ `src/syscall/syscall_linux.go`
- ❌ `src/syscall/syscall_linux_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 9.5% | 16.0% | 2/21 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall`


### 📊 **Proposal #39444**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os`

**Predicted Directories (4):**
- ✅ `src/os`
- ❌ `src/os/exec`
- ❌ `src/os/signal`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 50.0% | 22.2% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/os/exec_unix.go`
- `src/os/exec_unix_test.go`

**Predicted Files (7):**
- ❌ `src/os/exec/exec_unix.go`
- ✅ `src/os/exec_unix.go`
- ❌ `src/os/os_darwin.go`
- ❌ `src/os/os_linux.go`
- ❌ `src/os/signal/signal_unix.go`
- ❌ `src/os/signal_unix.go`
- ❌ `src/syscall/syscall_unix.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/os`


### 📊 **Proposal #45430**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (4):**
- ✅ `src/crypto/tls`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`
- ❌ `src/testtls`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 23.1% | 37.5% | 28.6% | 3/8 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (8):**
- `src/crypto/tls/cipher_suites.go`
- `src/crypto/tls/common.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/crypto/tls/handshake_server_test.go`
- `src/crypto/tls/handshake_server_tls13.go`
- `src/crypto/tls/handshake_test.go`
- `src/crypto/tls/tls_test.go`

**Predicted Files (13):**
- ✅ `src/crypto/tls/cipher_suites.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/testtls/tls.go`
- ❌ `src/testtls/tls_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 37.5% | 50.0% | 3/8 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #37533**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 100.0% | 20.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (9):**
- ❌ `compile/internal/base`
- ❌ `src/cmd/internal/objabi`
- ✅ `src/flag`
- ❌ `src/go/internal`
- ❌ `src/os/exec`
- ❌ `src/runtime`
- ❌ `src/terminal/pkgbits`
- ❌ `test/fixedbugs`
- ❌ `testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.4% | 100.0% | 26.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (13):**
- ❌ `compile/internal/base/flag.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`
- ❌ `src/go/internal/flag.go`
- ❌ `src/go/internal/flag_test.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/runtime/flag.go`
- ❌ `src/terminal/pkgbits/flags.go`
- ❌ `test/fixedbugs/issue8011.go`
- ❌ `testing/flag_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/flag`


### 📊 **Proposal #47781**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 20.0% | 16.7% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/cgo`
- `src/go/ast`
- `src/go/parser`
- `src/go/printer`
- `src/go/types`

**Predicted Directories (7):**
- ❌ `src/compile/internal/ir`
- ❌ `src/compile/internal/types`
- ✅ `src/go/ast`
- ❌ `src/go/internal/ast`
- ❌ `src/go/internal/token`
- ❌ `src/go/token`
- ❌ `src/types`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/17 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (17):**
- `src/cmd/cgo/ast.go`
- `src/cmd/cgo/ast_go1.go`
- `src/cmd/cgo/ast_go118.go`
- `src/cmd/cgo/gcc.go`
- `src/go/ast/walk.go`
- `src/go/parser/parser.go`
- `src/go/parser/resolver.go`
- `src/go/printer/nodes.go`
- `src/go/types/call.go`
- `src/go/types/decl.go`
- `src/go/types/expr.go`
- `src/go/types/exprstring.go`
- `src/go/types/interface.go`
- `src/go/types/resolver.go`
- `src/go/types/signature.go`
- `src/go/types/struct.go`
- `src/go/types/typexpr.go`

**Predicted Files (10):**
- ❌ `src/compile/internal/ir/type.go`
- ❌ `src/compile/internal/types/typeparam.go`
- ❌ `src/compile/internal/types/typeset.go`
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`
- ❌ `src/go/internal/ast/ast.go`
- ❌ `src/go/internal/token/token.go`
- ❌ `src/go/token/token.go`
- ❌ `src/go/token/token_test.go`
- ❌ `src/types/typeparams.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/17 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/ast`


### 📊 **Proposal #46057**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (5):**
- ✅ `src/crypto/x509`
- ❌ `src/issue15646.dir`
- ❌ `src/issue15920.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/cert_pool.go`
- `src/crypto/x509/cert_pool_test.go`

**Predicted Files (14):**
- ✅ `src/crypto/x509/cert_pool.go`
- ✅ `src/crypto/x509/cert_pool_test.go`
- ❌ `src/crypto/x509/example_test.go`
- ❌ `src/issue15646.dir/a.go`
- ❌ `src/issue15646.dir/b.go`
- ❌ `src/issue15920.dir/a.go`
- ❌ `src/issue15920.dir/b.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #43401**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/csv`

**Predicted Directories (7):**
- ✅ `src/encoding/csv`
- ❌ `src/issue15646.dir`
- ❌ `src/issue15838.dir`
- ❌ `src/issue15920.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16317.dir`
- ❌ `src/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/csv/reader.go`
- `src/encoding/csv/reader_test.go`

**Predicted Files (10):**
- ✅ `src/encoding/csv/reader.go`
- ✅ `src/encoding/csv/reader_test.go`
- ❌ `src/encoding/csv/writer.go`
- ❌ `src/encoding/csv/writer_test.go`
- ❌ `src/issue15646.dir/issue15646.go`
- ❌ `src/issue15838.dir/issue15838.go`
- ❌ `src/issue15920.dir/issue15920.go`
- ❌ `src/issue16133.dir/issue16133.go`
- ❌ `src/issue16317.dir/issue16317.go`
- ❌ `src/issue16616.dir/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/csv`


### 📊 **Proposal #40728**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 28.6% | 28.6% | 2/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/go/internal/base`
- `src/cmd/go/internal/fmtcmd`
- `src/cmd/go/internal/list`
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modget`
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/work`

**Predicted Directories (7):**
- ❌ `cmd/go/internal/modget`
- ❌ `cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/modfile`
- ✅ `src/cmd/go/internal/modget`
- ✅ `src/cmd/go/internal/modload`
- ❌ `src/go/internal/modcmd`
- ❌ `src/go/internal/modload`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.9% | 4.2% | 4.9% | 1/24 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (24):**
- `src/cmd/go/internal/base/flag.go`
- `src/cmd/go/internal/fmtcmd/fmt.go`
- `src/cmd/go/internal/list/list.go`
- `src/cmd/go/internal/modcmd/download.go`
- `src/cmd/go/internal/modcmd/edit.go`
- `src/cmd/go/internal/modcmd/graph.go`
- `src/cmd/go/internal/modcmd/init.go`
- `src/cmd/go/internal/modcmd/tidy.go`
- `src/cmd/go/internal/modcmd/vendor.go`
- `src/cmd/go/internal/modcmd/verify.go`
- `src/cmd/go/internal/modcmd/why.go`
- `src/cmd/go/internal/modget/get.go`
- `src/cmd/go/internal/modget/query.go`
- `src/cmd/go/internal/modload/buildlist.go`
- `src/cmd/go/internal/modload/import.go`
- `src/cmd/go/internal/modload/init.go`
- `src/cmd/go/internal/modload/load.go`
- `src/cmd/go/internal/modload/modfile.go`
- `src/cmd/go/internal/modload/mvs.go`
- `src/cmd/go/internal/modload/query.go`
- `src/cmd/go/internal/modload/query_test.go`
- `src/cmd/go/internal/modload/search.go`
- `src/cmd/go/internal/work/build.go`
- `src/cmd/go/internal/work/init.go`

**Predicted Files (17):**
- ❌ `cmd/go/internal/modget/README.md`
- ❌ `cmd/go/internal/modget/get.go`
- ❌ `cmd/go/internal/modload/README.md`
- ❌ `cmd/go/internal/modload/resolve.go`
- ❌ `src/cmd/go/internal/modfile/modfile.go`
- ✅ `src/cmd/go/internal/modget/get.go`
- ❌ `src/cmd/go/internal/modload/modload.go`
- ❌ `src/go/internal/modcmd/download.go`
- ❌ `src/go/internal/modcmd/edit.go`
- ❌ `src/go/internal/modcmd/graph.go`
- ❌ `src/go/internal/modcmd/init.go`
- ❌ `src/go/internal/modcmd/mod.go`
- ❌ `src/go/internal/modcmd/tidy.go`
- ❌ `src/go/internal/modcmd/vendor.go`
- ❌ `src/go/internal/modcmd/verify.go`
- ❌ `src/go/internal/modcmd/why.go`
- ❌ `src/go/internal/modload/modfile.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 4.2% | 7.7% | 1/24 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/go/internal/modget`
- `src/cmd/go/internal/modload`


### 📊 **Proposal #43993**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/reflect`
- `src/text/template`

**Predicted Directories (4):**
- ❌ `interface`
- ✅ `src/reflect`
- ❌ `src/reflectlite`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`
- `src/text/template/exec.go`
- `src/text/template/funcs.go`

**Predicted Files (4):**
- ❌ `interface/equal.go`
- ❌ `src/reflect/deepequal.go`
- ❌ `src/reflectlite/value.go`
- ❌ `src/runtime/reflect_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #50770**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (4):**
- ❌ `lib/time`
- ❌ `src/issue16133.dir`
- ❌ `src/runtime`
- ✅ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 50.0% | 18.2% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/mono_test.go`
- `src/time/time.go`

**Predicted Files (9):**
- ❌ `lib/time/mkzip.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ✅ `src/time/time.go`
- ❌ `src/time/time_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #44221**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 100.0% | 22.2% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/csv`

**Predicted Directories (8):**
- ❌ `src/cgroup`
- ❌ `src/encoding`
- ✅ `src/encoding/csv`
- ❌ `src/go/internal/cov`
- ❌ `src/go/internal/cov/covcmd`
- ❌ `src/go/internal/cov/testdata`
- ❌ `src/runtime/pprof`
- ❌ `src/runtime/trace`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.8% | 100.0% | 21.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/csv/reader.go`
- `src/encoding/csv/reader_test.go`

**Predicted Files (17):**
- ❌ `src/cgroup/line_reader.go`
- ❌ `src/encoding/csv`
- ❌ `src/encoding/csv/csv.go`
- ❌ `src/encoding/csv/csv_test.go`
- ✅ `src/encoding/csv/reader.go`
- ✅ `src/encoding/csv/reader_test.go`
- ❌ `src/encoding/csv/writer.go`
- ❌ `src/encoding/csv/writer_test.go`
- ❌ `src/go/internal/cov/covcmd/cmddefs.go`
- ❌ `src/go/internal/cov/mreader.go`
- ❌ `src/go/internal/cov/read_test.go`
- ❌ `src/go/internal/cov/readcovdata.go`
- ❌ `src/go/internal/cov/testdata/small.go`
- ❌ `src/runtime/pprof/pprof.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/trace/trace.go`
- ❌ `src/runtime/trace/trace_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/csv`


### 📊 **Proposal #44143**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (2):**
- ❌ `src`
- ❌ `src/context`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/http/socks_bundle.go`

**Predicted Files (4):**
- ❌ `src/context.go`
- ❌ `src/context/context.go`
- ❌ `src/context/context_test.go`
- ❌ `src/context_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #43931**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 16.7% | 13.3% | 1/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/cmd/compile/internal/gc`
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/staticdata`
- `src/cmd/dist`
- `src/embed/internal/embedtest`
- `src/go/types`

**Predicted Directories (9):**
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/cmd/internal/objfile/testdata`
- ❌ `src/cmd/internal/objfile/testdata/deadcode`
- ❌ `src/cmd/internal/objfile/testdata/testfilenum`
- ❌ `src/compile/internal/types2`
- ✅ `src/go/types`
- ❌ `src/types/testdata`
- ❌ `typeparam`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/cmd/compile/internal/gc/main.go`
- `src/cmd/compile/internal/noder/noder.go`
- `src/cmd/compile/internal/staticdata/embed.go`
- `src/cmd/dist/test.go`
- `src/embed/internal/embedtest/embed_test.go`
- `src/go/types/stdlib_test.go`

**Predicted Files (91):**
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/elf_test.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/goobj_test.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/macho_test.go`
- ❌ `src/cmd/internal/objfile/objfile.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/pe_test.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/plan9obj_test.go`
- ❌ `src/cmd/internal/objfile/reloctype.go`
- ❌ `src/cmd/internal/objfile/reloctype_string.go`
- ❌ `src/cmd/internal/objfile/testdata/deadcode/globalmap.go`
- ❌ `src/cmd/internal/objfile/testdata/deadcode/ifacemethod.go`
- ❌ `src/cmd/internal/objfile/testdata/deadcode/ifacemethod2.go`
- ❌ `src/cmd/internal/objfile/testdata/deadcode/ifacemethod3.go`
- ❌ `src/cmd/internal/objfile/testdata/deadcode/ifacemethod4.go`
- ❌ `src/cmd/internal/objfile/testdata/deadcode/ifacemethod5.go`
- ❌ `src/cmd/internal/objfile/testdata/deadcode/ifacemethod6.go`
- ❌ `src/cmd/internal/objfile/testdata/deadcode/reflectcall.go`
- ❌ `src/cmd/internal/objfile/testdata/deadcode/structof_funcof.go`
- ❌ `src/cmd/internal/objfile/testdata/deadcode/typedesc.go`
- ❌ `src/cmd/internal/objfile/testdata/fmthello.go`
- ❌ `src/cmd/internal/objfile/testdata/fmthellocgo.go`
- ❌ `src/cmd/internal/objfile/testdata/testfilenum/a.go`
- ❌ `src/cmd/internal/objfile/testdata/testfilenum/b.go`
- ❌ `src/cmd/internal/objfile/testdata/testfilenum/c.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/cmd/internal/objfile/xcoff_test.go`
- ❌ `src/compile/internal/types2/typeparam.go`
- ❌ `src/compile/internal/types2/typeset.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/types/testdata/typeparams.go`
- ❌ `typeparam/absdiff.go`
- ❌ `typeparam/absdiff2.go`
- ❌ `typeparam/absdiff3.go`
- ❌ `typeparam/absdiffimp.go`
- ❌ `typeparam/absdiffimp2.go`
- ❌ `typeparam/aliasimp.go`
- ❌ `typeparam/chansimp.go`
- ❌ `typeparam/dedup.go`
- ❌ `typeparam/fact.go`
- ❌ `typeparam/factimp.go`
- ❌ `typeparam/gencrawler.go`
- ❌ `typeparam/genembed.go`
- ❌ `typeparam/geninline.go`
- ❌ `typeparam/issue46461.go`
- ❌ `typeparam/issue48094.go`
- ❌ `typeparam/issue48185a.go`
- ❌ `typeparam/issue48185b.go`
- ❌ `typeparam/issue48280.go`
- ❌ `typeparam/issue48306.go`
- ❌ `typeparam/issue48337a.go`
- ❌ `typeparam/issue48337b.go`
- ❌ `typeparam/issue48454.go`
- ❌ `typeparam/issue48537.go`
- ❌ `typeparam/issue48602.go`
- ❌ `typeparam/issue48716.go`
- ❌ `typeparam/issue48962.go`
- ❌ `typeparam/issue49027.go`
- ❌ `typeparam/issue49241.go`
- ❌ `typeparam/issue49246.go`
- ❌ `typeparam/issue49497.go`
- ❌ `typeparam/issue49524.go`
- ❌ `typeparam/issue49536.go`
- ❌ `typeparam/issue50121.go`
- ❌ `typeparam/issue50121b.go`
- ❌ `typeparam/issue50437.go`
- ❌ `typeparam/issue50481b.go`
- ❌ `typeparam/issue50481c.go`
- ❌ `typeparam/issue50552.go`
- ❌ `typeparam/issue50561.go`
- ❌ `typeparam/issue51219.go`
- ❌ `typeparam/issue51219b.go`
- ❌ `typeparam/issue51836.go`
- ❌ `typeparam/issue52117.go`
- ❌ `typeparam/listimp.go`
- ❌ `typeparam/mapimp.go`
- ❌ `typeparam/mutualimp.go`
- ❌ `typeparam/orderedmapsimp.go`
- ❌ `typeparam/pairimp.go`
- ❌ `typeparam/recoverimp.go`
- ❌ `typeparam/select.go`
- ❌ `typeparam/sliceimp.go`
- ❌ `typeparam/stringerimp.go`
- ❌ `typeparam/structinit.go`
- ❌ `typeparam/valimp.go`
- ❌ `typeparam/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/types`


### 📊 **Proposal #48294**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (5):**
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/reflect`
- ❌ `src/reflectlite`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/reflect/all_test.go`

**Predicted Files (21):**
- ❌ `reflectmethod1.go`
- ❌ `reflectmethod2.go`
- ❌ `reflectmethod3.go`
- ❌ `reflectmethod4.go`
- ❌ `reflectmethod5.go`
- ❌ `reflectmethod6.go`
- ❌ `reflectmethod7.go`
- ❌ `reflectmethod8.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`
- ❌ `src/reflect/value.go`
- ❌ `src/reflectlite/value.go`
- ❌ `src/runtime/map_test.go`
- ❌ `src/runtime/reflect_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #51428**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (4):**
- ❌ `src/context`
- ❌ `src/fix`
- ✅ `src/net`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 50.0% | 20.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/error_test.go`
- `src/net/net.go`

**Predicted Files (8):**
- ❌ `src/context/context.go`
- ❌ `src/context/context_test.go`
- ❌ `src/fix/context.go`
- ❌ `src/fix/context_test.go`
- ❌ `src/net/dial.go`
- ✅ `src/net/net.go`
- ❌ `src/net/net_test.go`
- ❌ `src/syscall/net.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #52463**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/gofmt`

**Predicted Directories (4):**
- ❌ `src`
- ❌ `src/go/ast`
- ❌ `src/go/parser`
- ❌ `src/go/types`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/gofmt/gofmt.go`
- `src/cmd/gofmt/simplify.go`

**Predicted Files (16):**
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`
- ❌ `src/go/ast/filter.go`
- ❌ `src/go/ast/import.go`
- ❌ `src/go/ast/print.go`
- ❌ `src/go/ast/resolve.go`
- ❌ `src/go/ast/scope.go`
- ❌ `src/go/ast/walk.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/types/types.go`
- ❌ `src/issue15646.go`
- ❌ `src/issue15838.go`
- ❌ `src/issue15920.go`
- ❌ `src/issue16133.go`
- ❌ `src/issue16317.go`
- ❌ `src/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #51115**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (2):**
- ✅ `src/io`
- ❌ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/io/io.go`

**Predicted Files (5):**
- ✅ `src/io/io.go`
- ❌ `src/io/io_test.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io`


### 📊 **Proposal #35567**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/go/build`
- `src/runtime/debug`
- `src/testing`

**Predicted Directories (1):**
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 20.0% | 25.0% | 1/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/go/build/deps_test.go`
- `src/runtime/debug/stack_test.go`
- `src/testing/benchmark.go`
- `src/testing/example.go`
- `src/testing/testing.go`

**Predicted Files (3):**
- ❌ `src/testing/internal`
- ✅ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 20.0% | 25.0% | 1/5 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #40255**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 11.1% | 11.8% | 1/9 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (9):**
- `src/cmd/asm/internal/asm`
- `src/cmd/compile/internal/ssa`
- `src/cmd/compile/internal/x86`
- `src/cmd/dist`
- `src/cmd/go/internal/cfg`
- `src/cmd/go/internal/work`
- `src/reflect`
- `src/runtime`
- `test/codegen`

**Predicted Directories (8):**
- ❌ `src/compile/internal`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/go`
- ❌ `src/go/goarch`
- ❌ `src/go/internal/modload`
- ✅ `src/runtime`
- ❌ `src/runtime/atomic`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/15 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (15):**
- `src/cmd/asm/internal/asm/endtoend_test.go`
- `src/cmd/compile/internal/ssa/regalloc.go`
- `src/cmd/compile/internal/ssa/rewrite386.go`
- `src/cmd/compile/internal/x86/galign.go`
- `src/cmd/compile/internal/x86/ssa.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/util_gc.go`
- `src/cmd/go/internal/cfg/cfg.go`
- `src/cmd/go/internal/work/exec.go`
- `src/reflect/all_test.go`
- `src/runtime/mkpreempt.go`
- `test/codegen/arithmetic.go`
- `test/codegen/floats.go`
- `test/codegen/math.go`
- `test/codegen/memops.go`

**Predicted Files (76):**
- ❌ `src/compile/internal/softfloat.go`
- ❌ `src/fixedbugs/issue16133.dir/a.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/go/build.go`
- ❌ `src/go/gccgo.go`
- ❌ `src/go/goarch/goarch_386.go`
- ❌ `src/go/goarch/goarch_amd64.go`
- ❌ `src/go/internal/modload/build.go`
- ❌ `src/go/internal/modload/edit.go`
- ❌ `src/go/internal/modload/help.go`
- ❌ `src/go/internal/modload/import.go`
- ❌ `src/go/internal/modload/init.go`
- ❌ `src/go/internal/modload/list.go`
- ❌ `src/go/internal/modload/load.go`
- ❌ `src/go/internal/modload/modfile.go`
- ❌ `src/go/internal/modload/mvs.go`
- ❌ `src/go/internal/modload/query.go`
- ❌ `src/go/internal/modload/search.go`
- ❌ `src/go/internal/modload/stat_openfile.go`
- ❌ `src/go/internal/modload/vendor.go`
- ❌ `src/runtime/atomic/atomic_386.go`
- ❌ `src/runtime/defs1_linux.go`
- ❌ `src/runtime/defs1_netbsd_386.go`
- ❌ `src/runtime/defs1_netbsd_amd64.go`
- ❌ `src/runtime/defs1_netbsd_arm.go`
- ❌ `src/runtime/defs1_netbsd_arm64.go`
- ❌ `src/runtime/defs1_solaris_amd64.go`
- ❌ `src/runtime/defs_linux.go`
- ❌ `src/runtime/defs_linux_386.go`
- ❌ `src/runtime/defs_linux_amd64.go`
- ❌ `src/runtime/defs_linux_arm.go`
- ❌ `src/runtime/defs_linux_arm64.go`
- ❌ `src/runtime/defs_linux_loong64.go`
- ❌ `src/runtime/defs_linux_mips64x.go`
- ❌ `src/runtime/defs_linux_mipsx.go`
- ❌ `src/runtime/defs_linux_ppc64.go`
- ❌ `src/runtime/defs_linux_ppc64le.go`
- ❌ `src/runtime/defs_linux_riscv64.go`
- ❌ `src/runtime/defs_linux_s390x.go`
- ❌ `src/runtime/defs_netbsd.go`
- ❌ `src/runtime/defs_netbsd_386.go`
- ❌ `src/runtime/defs_netbsd_amd64.go`
- ❌ `src/runtime/defs_netbsd_arm.go`
- ❌ `src/runtime/defs_openbsd.go`
- ❌ `src/runtime/defs_openbsd_386.go`
- ❌ `src/runtime/defs_openbsd_amd64.go`
- ❌ `src/runtime/defs_openbsd_arm.go`
- ❌ `src/runtime/defs_openbsd_arm64.go`
- ❌ `src/runtime/defs_openbsd_mips64.go`
- ❌ `src/runtime/defs_openbsd_ppc64.go`
- ❌ `src/runtime/defs_openbsd_riscv64.go`
- ❌ `src/runtime/defs_plan9_386.go`
- ❌ `src/runtime/defs_plan9_amd64.go`
- ❌ `src/runtime/defs_plan9_arm.go`
- ❌ `src/runtime/defs_solaris.go`
- ❌ `src/runtime/defs_solaris_amd64.go`
- ❌ `src/runtime/defs_windows.go`
- ❌ `src/runtime/defs_windows_386.go`
- ❌ `src/runtime/defs_windows_amd64.go`
- ❌ `src/runtime/defs_windows_arm.go`
- ❌ `src/runtime/defs_windows_arm64.go`
- ❌ `src/runtime/signal_386.go`
- ❌ `src/runtime/signal_freebsd_386.go`
- ❌ `src/runtime/signal_linux_386.go`
- ❌ `src/runtime/signal_netbsd_386.go`
- ❌ `src/runtime/signal_openbsd_386.go`
- ❌ `src/syscall/defs_linux_386.go`
- ❌ `src/syscall/syscall_freebsd_386.go`
- ❌ `src/syscall/syscall_linux_386.go`
- ❌ `src/syscall/syscall_openbsd_386.go`
- ❌ `src/syscall/syscall_plan9_386.go`
- ❌ `src/syscall/types_windows_386.go`
- ❌ `src/syscall/zerrors_linux_386.go`
- ❌ `src/syscall/zsysnum_linux_386.go`
- ❌ `src/syscall/ztypes_linux_386.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/15 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime`


### 📊 **Proposal #46648**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.7% | 100.0% | 14.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/types`

**Predicted Directories (13):**
- ❌ `src/cmd/internal/types2`
- ❌ `src/go/internal/fix`
- ✅ `src/go/types`
- ❌ `src/types`
- ❌ `src/types/errors`
- ❌ `src/types/spec`
- ❌ `src/types/testdata`
- ❌ `src/types/testdata/check/decls2`
- ❌ `src/types/testdata/importdecl0`
- ❌ `src/types/testdata/importdecl1`
- ❌ `src/types/testdata/issue25008`
- ❌ `src/types/types2`
- ❌ `syntax`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 1.4% | 100.0% | 2.7% | 3/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/go/types/check.go`
- `src/go/types/check_test.go`
- `src/go/types/stdlib_test.go`

**Predicted Files (220):**
- ❌ `src/cmd/internal/types2/types.go`
- ❌ `src/go/internal/fix/gotypes.go`
- ❌ `src/go/types/alias.go`
- ❌ `src/go/types/api.go`
- ❌ `src/go/types/api_test.go`
- ❌ `src/go/types/array.go`
- ❌ `src/go/types/assignments.go`
- ❌ `src/go/types/badlinkname.go`
- ❌ `src/go/types/basic.go`
- ❌ `src/go/types/builtins.go`
- ❌ `src/go/types/builtins_test.go`
- ❌ `src/go/types/call.go`
- ❌ `src/go/types/chan.go`
- ✅ `src/go/types/check.go`
- ✅ `src/go/types/check_test.go`
- ❌ `src/go/types/commentMap_test.go`
- ❌ `src/go/types/const.go`
- ❌ `src/go/types/context.go`
- ❌ `src/go/types/context_test.go`
- ❌ `src/go/types/conversions.go`
- ❌ `src/go/types/decl.go`
- ❌ `src/go/types/errorcalls_test.go`
- ❌ `src/go/types/errors.go`
- ❌ `src/go/types/errors_test.go`
- ❌ `src/go/types/errsupport.go`
- ❌ `src/go/types/eval.go`
- ❌ `src/go/types/eval_test.go`
- ❌ `src/go/types/example_test.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/exprstring.go`
- ❌ `src/go/types/exprstring_test.go`
- ❌ `src/go/types/format.go`
- ❌ `src/go/types/gccgosizes.go`
- ❌ `src/go/types/gcsizes.go`
- ❌ `src/go/types/generate.go`
- ❌ `src/go/types/generate_test.go`
- ❌ `src/go/types/gotype.go`
- ❌ `src/go/types/hilbert_test.go`
- ❌ `src/go/types/index.go`
- ❌ `src/go/types/infer.go`
- ❌ `src/go/types/initorder.go`
- ❌ `src/go/types/instantiate.go`
- ❌ `src/go/types/instantiate_test.go`
- ❌ `src/go/types/interface.go`
- ❌ `src/go/types/issues_test.go`
- ❌ `src/go/types/iter.go`
- ❌ `src/go/types/labels.go`
- ❌ `src/go/types/literals.go`
- ❌ `src/go/types/lookup.go`
- ❌ `src/go/types/lookup_test.go`
- ❌ `src/go/types/main_test.go`
- ❌ `src/go/types/map.go`
- ❌ `src/go/types/methodset.go`
- ❌ `src/go/types/methodset_test.go`
- ❌ `src/go/types/mono.go`
- ❌ `src/go/types/mono_test.go`
- ❌ `src/go/types/named.go`
- ❌ `src/go/types/named_test.go`
- ❌ `src/go/types/object.go`
- ❌ `src/go/types/object_test.go`
- ❌ `src/go/types/objset.go`
- ❌ `src/go/types/operand.go`
- ❌ `src/go/types/package.go`
- ❌ `src/go/types/pointer.go`
- ❌ `src/go/types/predicates.go`
- ❌ `src/go/types/range.go`
- ❌ `src/go/types/recording.go`
- ❌ `src/go/types/resolver.go`
- ❌ `src/go/types/resolver_test.go`
- ❌ `src/go/types/return.go`
- ❌ `src/go/types/scope.go`
- ❌ `src/go/types/scope2.go`
- ❌ `src/go/types/scope2_test.go`
- ❌ `src/go/types/selection.go`
- ❌ `src/go/types/self_test.go`
- ❌ `src/go/types/signature.go`
- ❌ `src/go/types/sizeof_test.go`
- ❌ `src/go/types/sizes.go`
- ❌ `src/go/types/sizes_test.go`
- ❌ `src/go/types/slice.go`
- ✅ `src/go/types/stdlib_test.go`
- ❌ `src/go/types/stmt.go`
- ❌ `src/go/types/struct.go`
- ❌ `src/go/types/subst.go`
- ❌ `src/go/types/termlist.go`
- ❌ `src/go/types/termlist_test.go`
- ❌ `src/go/types/token_test.go`
- ❌ `src/go/types/tuple.go`
- ❌ `src/go/types/type.go`
- ❌ `src/go/types/typelists.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/go/types/typeset.go`
- ❌ `src/go/types/typeset_test.go`
- ❌ `src/go/types/typestring.go`
- ❌ `src/go/types/typestring_test.go`
- ❌ `src/go/types/typeterm.go`
- ❌ `src/go/types/typeterm_test.go`
- ❌ `src/go/types/typexpr.go`
- ❌ `src/go/types/under.go`
- ❌ `src/go/types/unify.go`
- ❌ `src/go/types/union.go`
- ❌ `src/go/types/universe.go`
- ❌ `src/go/types/util.go`
- ❌ `src/go/types/util_test.go`
- ❌ `src/go/types/validtype.go`
- ❌ `src/go/types/version.go`
- ❌ `src/go/types/version_test.go`
- ❌ `src/types/errors/codes.go`
- ❌ `src/types/errors/codes_test.go`
- ❌ `src/types/goversion.go`
- ❌ `src/types/spec/assignability.go`
- ❌ `src/types/spec/comparable.go`
- ❌ `src/types/spec/comparable1.19.go`
- ❌ `src/types/spec/comparisons.go`
- ❌ `src/types/spec/conversions.go`
- ❌ `src/types/spec/range.go`
- ❌ `src/types/spec/range_int.go`
- ❌ `src/types/spec/receivers.go`
- ❌ `src/types/spec/typeAliases1.22.go`
- ❌ `src/types/spec/typeAliases1.23a.go`
- ❌ `src/types/spec/typeAliases1.23b.go`
- ❌ `src/types/spec/typeAliases1.8.go`
- ❌ `src/types/testdata/blank.go`
- ❌ `src/types/testdata/builtins0.go`
- ❌ `src/types/testdata/builtins1.go`
- ❌ `src/types/testdata/chans.go`
- ❌ `src/types/testdata/check/decls2/decls2a.go`
- ❌ `src/types/testdata/check/decls2/decls2b.go`
- ❌ `src/types/testdata/compliterals.go`
- ❌ `src/types/testdata/const0.go`
- ❌ `src/types/testdata/const1.go`
- ❌ `src/types/testdata/constdecl.go`
- ❌ `src/types/testdata/conversions0.go`
- ❌ `src/types/testdata/conversions1.go`
- ❌ `src/types/testdata/cycles0.go`
- ❌ `src/types/testdata/cycles1.go`
- ❌ `src/types/testdata/cycles2.go`
- ❌ `src/types/testdata/cycles3.go`
- ❌ `src/types/testdata/cycles4.go`
- ❌ `src/types/testdata/cycles5.go`
- ❌ `src/types/testdata/cycles5a.go`
- ❌ `src/types/testdata/decls0.go`
- ❌ `src/types/testdata/decls1.go`
- ❌ `src/types/testdata/decls3.go`
- ❌ `src/types/testdata/decls4.go`
- ❌ `src/types/testdata/decls5.go`
- ❌ `src/types/testdata/doubled_labels.go`
- ❌ `src/types/testdata/errors.go`
- ❌ `src/types/testdata/expr0.go`
- ❌ `src/types/testdata/expr1.go`
- ❌ `src/types/testdata/expr2.go`
- ❌ `src/types/testdata/expr3.go`
- ❌ `src/types/testdata/funcinference.go`
- ❌ `src/types/testdata/go1_12.go`
- ❌ `src/types/testdata/go1_13.go`
- ❌ `src/types/testdata/go1_16.go`
- ❌ `src/types/testdata/go1_19.go`
- ❌ `src/types/testdata/go1_19_20.go`
- ❌ `src/types/testdata/go1_20_19.go`
- ❌ `src/types/testdata/go1_21_19.go`
- ❌ `src/types/testdata/go1_21_22.go`
- ❌ `src/types/testdata/go1_22_21.go`
- ❌ `src/types/testdata/go1_8.go`
- ❌ `src/types/testdata/go1_xx_19.go`
- ❌ `src/types/testdata/gotos.go`
- ❌ `src/types/testdata/importC.go`
- ❌ `src/types/testdata/importdecl0/importdecl0a.go`
- ❌ `src/types/testdata/importdecl0/importdecl0b.go`
- ❌ `src/types/testdata/importdecl1/importdecl1a.go`
- ❌ `src/types/testdata/importdecl1/importdecl1b.go`
- ❌ `src/types/testdata/init0.go`
- ❌ `src/types/testdata/init1.go`
- ❌ `src/types/testdata/init2.go`
- ❌ `src/types/testdata/issue25008/issue25008a.go`
- ❌ `src/types/testdata/issue25008/issue25008b.go`
- ❌ `src/types/testdata/issue70974.go`
- ❌ `src/types/testdata/issues0.go`
- ❌ `src/types/testdata/issues1.go`
- ❌ `src/types/testdata/labels.go`
- ❌ `src/types/testdata/linalg.go`
- ❌ `src/types/testdata/literals.go`
- ❌ `src/types/testdata/lookup1.go`
- ❌ `src/types/testdata/lookup2.go`
- ❌ `src/types/testdata/main0.go`
- ❌ `src/types/testdata/main1.go`
- ❌ `src/types/testdata/map0.go`
- ❌ `src/types/testdata/map1.go`
- ❌ `src/types/testdata/methodsets.go`
- ❌ `src/types/testdata/shifts.go`
- ❌ `src/types/testdata/slices.go`
- ❌ `src/types/testdata/stmt0.go`
- ❌ `src/types/testdata/stmt1.go`
- ❌ `src/types/testdata/typeinference.go`
- ❌ `src/types/testdata/typeinst0.go`
- ❌ `src/types/testdata/typeinst1.go`
- ❌ `src/types/testdata/typeinstcycles.go`
- ❌ `src/types/testdata/typeparams.go`
- ❌ `src/types/testdata/unions.go`
- ❌ `src/types/testdata/vardecl.go`
- ❌ `src/types/types.go`
- ❌ `src/types/types2/api.go`
- ❌ `syntax/chan.go`
- ❌ `syntax/chan1.go`
- ❌ `syntax/composite.go`
- ❌ `syntax/ddd.go`
- ❌ `syntax/else.go`
- ❌ `syntax/if.go`
- ❌ `syntax/import.go`
- ❌ `syntax/initvar.go`
- ❌ `syntax/semi1.go`
- ❌ `syntax/semi2.go`
- ❌ `syntax/semi3.go`
- ❌ `syntax/semi4.go`
- ❌ `syntax/semi5.go`
- ❌ `syntax/semi6.go`
- ❌ `syntax/semi7.go`
- ❌ `syntax/texpr.go`
- ❌ `syntax/typesw.go`
- ❌ `syntax/vareq.go`
- ❌ `syntax/vareq1.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 2.9% | 100.0% | 5.6% | 3/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/types`


### 📊 **Proposal #53346**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/xml`

**Predicted Directories (2):**
- ✅ `src/encoding/xml`
- ❌ `src/terminal/pkgbits`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/xml/marshal.go`
- `src/encoding/xml/marshal_test.go`

**Predicted Files (6):**
- ❌ `src/encoding/xml/encoder.go`
- ❌ `src/encoding/xml/encoder_test.go`
- ✅ `src/encoding/xml/marshal.go`
- ✅ `src/encoding/xml/marshal_test.go`
- ❌ `src/encoding/xml/xml.go`
- ❌ `src/terminal/pkgbits/encoder.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/xml`


### 📊 **Proposal #40127**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 100.0% | 22.2% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/json`

**Predicted Directories (8):**
- ✅ `src/encoding/json`
- ❌ `src/encoding/json/internal/jsonflags`
- ❌ `src/encoding/json/internal/jsonopts`
- ❌ `src/encoding/json/internal/jsontest`
- ❌ `src/encoding/json/internal/jsonwire`
- ❌ `src/encoding/json/jsontext`
- ❌ `src/encoding/json/v2`
- ❌ `src/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/json/indent.go`
- `src/encoding/json/stream.go`

**Predicted Files (21):**
- ❌ `src/encoding/json/decoder.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encode_test.go`
- ❌ `src/encoding/json/encoder.go`
- ❌ `src/encoding/json/internal/jsonflags/flags.go`
- ❌ `src/encoding/json/internal/jsonopts/options.go`
- ❌ `src/encoding/json/internal/jsontest/testcase.go`
- ❌ `src/encoding/json/internal/jsontest/testdata.go`
- ❌ `src/encoding/json/internal/jsonwire/decode.go`
- ❌ `src/encoding/json/internal/jsonwire/decode_test.go`
- ❌ `src/encoding/json/internal/jsonwire/encode.go`
- ❌ `src/encoding/json/internal/jsonwire/encode_test.go`
- ❌ `src/encoding/json/internal/jsonwire/wire.go`
- ❌ `src/encoding/json/internal/jsonwire/wire_test.go`
- ❌ `src/encoding/json/jsontext/encode.go`
- ❌ `src/encoding/json/jsontext/encode_test.go`
- ❌ `src/encoding/json/jsontext/token.go`
- ❌ `src/encoding/json/jsontext/token_test.go`
- ❌ `src/encoding/json/v2/v2_encode.go`
- ❌ `src/encoding/json/v2/v2_encode_test.go`
- ❌ `src/issue16616.dir/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/json`


### 📊 **Proposal #51082**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 57.1% | 12.3% | 20.3% | 8/65 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (65):**
- `misc/cgo/gmp`
- `src/archive/zip`
- `src/cmd/asm/internal/asm`
- `src/cmd/cgo`
- `src/cmd/compile/internal/importer`
- `src/cmd/compile/internal/ir`
- `src/cmd/compile/internal/ssa`
- `src/cmd/compile/internal/syntax`
- `src/cmd/compile/internal/test`
- `src/cmd/compile/internal/typecheck`
- `src/cmd/compile/internal/types`
- `src/cmd/compile/internal/types2`
- `src/cmd/compile/internal/walk`
- `src/cmd/cover`
- `src/cmd/dist`
- `src/cmd/doc`
- `src/cmd/go/internal/cache`
- `src/cmd/go/internal/imports`
- `src/cmd/go/internal/modload`
- `src/cmd/internal/obj/riscv`
- `src/cmd/internal/obj/x86`
- `src/cmd/link/internal/ld`
- `src/cmd/link/internal/loader`
- `src/container/ring`
- `src/debug/dwarf`
- `src/debug/gosym`
- `src/encoding/ascii85`
- `src/encoding/binary`
- `src/encoding/json`
- `src/go/ast`
- `src/go/build`
- `src/go/constant`
- `src/go/doc`
- `src/go/doc/comment`
- `src/go/format`
- `src/go/internal/gccgoimporter`
- `src/go/internal/gcimporter`
- `src/go/parser`
- `src/go/printer`
- `src/go/printer/testdata`
- `src/go/scanner`
- `src/go/token`
- `src/go/types`
- `src/html/template`
- `src/index/suffixarray`
- `src/internal/fmtsort`
- `src/math/big`
- `src/math/rand`
- `src/net/http`
- `src/net/textproto`
- `src/path`
- `src/path/filepath`
- `src/reflect`
- `src/regexp`
- `src/regexp/syntax`
- `src/runtime`
- `src/runtime/pprof`
- `src/runtime/trace`
- `src/sort`
- `src/strconv`
- `src/sync`
- `src/testing/fstest`
- `src/text/tabwriter`
- `src/text/template`
- `src/unicode`

**Predicted Directories (14):**
- ❌ `internal/runtime/sys`
- ❌ `src/cmd/internal/objfile`
- ✅ `src/go/doc`
- ✅ `src/go/doc/comment`
- ✅ `src/go/printer`
- ✅ `src/net/http`
- ✅ `src/runtime/pprof`
- ✅ `src/runtime/trace`
- ✅ `src/strconv`
- ❌ `src/strings`
- ✅ `src/sync`
- ❌ `src/sync/atomic`
- ❌ `src/trace`
- ❌ `src/trace/raw`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.3% | 5.6% | 7.7% | 7/125 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (125):**
- `misc/cgo/gmp/gmp.go`
- `src/archive/zip/reader_test.go`
- `src/cmd/asm/internal/asm/parse.go`
- `src/cmd/cgo/gcc.go`
- `src/cmd/compile/internal/importer/gcimporter.go`
- `src/cmd/compile/internal/ir/fmt.go`
- `src/cmd/compile/internal/ssa/block.go`
- `src/cmd/compile/internal/ssa/compile.go`
- `src/cmd/compile/internal/ssa/debug.go`
- `src/cmd/compile/internal/ssa/debug_test.go`
- `src/cmd/compile/internal/syntax/parser.go`
- `src/cmd/compile/internal/syntax/syntax.go`
- `src/cmd/compile/internal/test/zerorange_test.go`
- `src/cmd/compile/internal/typecheck/mkbuiltin.go`
- `src/cmd/compile/internal/types/fmt.go`
- `src/cmd/compile/internal/types2/api.go`
- `src/cmd/compile/internal/types2/builtins.go`
- `src/cmd/compile/internal/types2/expr.go`
- `src/cmd/compile/internal/types2/lookup.go`
- `src/cmd/compile/internal/types2/operand.go`
- `src/cmd/compile/internal/types2/selection.go`
- `src/cmd/compile/internal/types2/typexpr.go`
- `src/cmd/compile/internal/types2/universe.go`
- `src/cmd/compile/internal/walk/builtin.go`
- `src/cmd/compile/internal/walk/order.go`
- `src/cmd/cover/cover_test.go`
- `src/cmd/dist/buildruntime.go`
- `src/cmd/doc/pkg.go`
- `src/cmd/go/internal/cache/cache.go`
- `src/cmd/go/internal/imports/build.go`
- `src/cmd/go/internal/modload/load.go`
- `src/cmd/go/internal/modload/query.go`
- `src/cmd/internal/obj/riscv/obj.go`
- `src/cmd/internal/obj/x86/asm6.go`
- `src/cmd/link/internal/ld/dwarf_test.go`
- `src/cmd/link/internal/loader/loader.go`
- `src/container/ring/ring.go`
- `src/debug/dwarf/entry.go`
- `src/debug/gosym/pclntab_test.go`
- `src/encoding/ascii85/ascii85.go`
- `src/encoding/binary/varint.go`
- `src/encoding/json/decode.go`
- `src/encoding/json/encode.go`
- `src/go/ast/ast.go`
- `src/go/ast/commentmap.go`
- `src/go/ast/filter.go`
- `src/go/ast/resolve.go`
- `src/go/ast/scope.go`
- `src/go/ast/walk.go`
- `src/go/build/build.go`
- `src/go/constant/value.go`
- `src/go/doc/comment.go`
- `src/go/doc/comment/html.go`
- `src/go/doc/comment/markdown.go`
- `src/go/doc/comment/parse.go`
- `src/go/doc/comment/print.go`
- `src/go/doc/comment/std_test.go`
- `src/go/doc/comment/testdata_test.go`
- `src/go/doc/comment/text.go`
- `src/go/doc/comment_test.go`
- `src/go/doc/doc.go`
- `src/go/doc/doc_test.go`
- `src/go/doc/example.go`
- `src/go/doc/exports.go`
- `src/go/doc/filter.go`
- `src/go/doc/reader.go`
- `src/go/doc/synopsis.go`
- `src/go/doc/synopsis_test.go`
- `src/go/format/benchmark_test.go`
- `src/go/format/format.go`
- `src/go/internal/gccgoimporter/parser.go`
- `src/go/internal/gcimporter/gcimporter.go`
- `src/go/parser/error_test.go`
- `src/go/parser/interface.go`
- `src/go/parser/parser.go`
- `src/go/parser/resolver.go`
- `src/go/printer/comment.go`
- `src/go/printer/nodes.go`
- `src/go/printer/printer.go`
- `src/go/printer/printer_test.go`
- `src/go/printer/testdata/parser.go`
- `src/go/scanner/errors.go`
- `src/go/scanner/scanner.go`
- `src/go/token/position.go`
- `src/go/token/token.go`
- `src/go/types/api.go`
- `src/go/types/builtins.go`
- `src/go/types/eval.go`
- `src/go/types/expr.go`
- `src/go/types/lookup.go`
- `src/go/types/operand.go`
- `src/go/types/selection.go`
- `src/go/types/typexpr.go`
- `src/go/types/universe.go`
- `src/html/template/template.go`
- `src/index/suffixarray/suffixarray.go`
- `src/internal/fmtsort/sort.go`
- `src/math/big/float.go`
- `src/math/big/floatconv.go`
- `src/math/big/int.go`
- `src/math/big/intconv.go`
- `src/math/big/natconv.go`
- `src/math/big/rat.go`
- `src/math/rand/exp.go`
- `src/math/rand/normal.go`
- `src/net/http/fs.go`
- `src/net/textproto/reader.go`
- `src/net/textproto/textproto.go`
- `src/path/filepath/match.go`
- `src/path/match.go`
- `src/reflect/makefunc.go`
- `src/regexp/exec_test.go`
- `src/regexp/syntax/parse.go`
- `src/runtime/chan.go`
- `src/runtime/pprof/pprof.go`
- `src/runtime/trace/annotation.go`
- `src/sort/search.go`
- `src/sort/search_test.go`
- `src/strconv/itoa.go`
- `src/sync/cond.go`
- `src/sync/once.go`
- `src/testing/fstest/testfs.go`
- `src/text/tabwriter/tabwriter.go`
- `src/text/template/option.go`
- `src/unicode/letter.go`

**Predicted Files (57):**
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `src/cmd/internal/objfile/doc.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/elf_test.go`
- ❌ `src/cmd/internal/objfile/flag.go`
- ❌ `src/cmd/internal/objfile/flag_test.go`
- ❌ `src/cmd/internal/objfile/funcid.go`
- ❌ `src/cmd/internal/objfile/funcid_test.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/head.go`
- ❌ `src/cmd/internal/objfile/head_test.go`
- ❌ `src/cmd/internal/objfile/line.go`
- ❌ `src/cmd/internal/objfile/line_test.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/macho_test.go`
- ❌ `src/cmd/internal/objfile/path.go`
- ❌ `src/cmd/internal/objfile/path_test.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/pe_test.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/plan9obj_test.go`
- ❌ `src/cmd/internal/objfile/reloctype.go`
- ❌ `src/cmd/internal/objfile/reloctype_string.go`
- ❌ `src/cmd/internal/objfile/reloctype_test.go`
- ❌ `src/cmd/internal/objfile/stack.go`
- ❌ `src/cmd/internal/objfile/stack_test.go`
- ❌ `src/cmd/internal/objfile/symkind.go`
- ❌ `src/cmd/internal/objfile/symkind_string.go`
- ❌ `src/cmd/internal/objfile/symkind_test.go`
- ❌ `src/cmd/internal/objfile/util.go`
- ❌ `src/cmd/internal/objfile/util_test.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/cmd/internal/objfile/xcoff_test.go`
- ❌ `src/go/doc/comment/comment.go`
- ❌ `src/go/doc/comment/doc.go`
- ✅ `src/go/doc/comment/markdown.go`
- ✅ `src/go/doc/comment/parse.go`
- ✅ `src/go/doc/comment/print.go`
- ✅ `src/go/doc/doc.go`
- ❌ `src/go/printer/doc.go`
- ✅ `src/go/printer/printer.go`
- ❌ `src/go/printer/printerconfig.go`
- ❌ `src/net/http/doc.go`
- ✅ `src/runtime/pprof/pprof.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/trace/trace.go`
- ❌ `src/runtime/trace/trace_test.go`
- ❌ `src/strconv/doc.go`
- ❌ `src/strconv/strconv_test.go`
- ❌ `src/strings/strings.go`
- ❌ `src/strings/strings_test.go`
- ❌ `src/sync/atomic/atomic_test.go`
- ❌ `src/sync/atomic/doc.go`
- ✅ `src/sync/cond.go`
- ❌ `src/sync/cond_test.go`
- ❌ `src/trace/raw/doc.go`
- ❌ `src/trace/trace.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 38.9% | 5.6% | 9.8% | 7/125 |

##### Correct Directories Used for Evaluation

**Correct Directories (8):**
- `src/go/doc`
- `src/go/doc/comment`
- `src/go/printer`
- `src/net/http`
- `src/runtime/pprof`
- `src/runtime/trace`
- `src/strconv`
- `src/sync`


### 📊 **Proposal #35833**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 20.0% | 28.6% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/crypto/elliptic`
- `src/crypto/rand`
- `src/crypto/rsa`
- `src/crypto/x509`
- `src/math/big`

**Predicted Directories (2):**
- ❌ `src/math`
- ✅ `src/math/big`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 28.6% | 36.4% | 2/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/crypto/elliptic/elliptic.go`
- `src/crypto/rand/util.go`
- `src/crypto/rsa/pkcs1v15.go`
- `src/crypto/x509/sec1.go`
- `src/math/big/int.go`
- `src/math/big/int_test.go`
- `src/math/big/nat.go`

**Predicted Files (4):**
- ✅ `src/math/big/int.go`
- ✅ `src/math/big/int_test.go`
- ❌ `src/math/math.go`
- ❌ `src/math/math_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 28.6% | 44.4% | 2/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/math/big`


### 📊 **Proposal #45460**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/http/transport.go`

**Predicted Files (2):**
- ❌ `src/net/http/request.go`
- ✅ `src/net/http/transport.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http`


### 📊 **Proposal #42387**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io/fs`

**Predicted Directories (5):**
- ❌ `src`
- ❌ `src/go/internal/fsys`
- ✅ `src/io/fs`
- ❌ `src/issue16133.dir`
- ❌ `src/os`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 50.0% | 15.4% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/io/fs/readdir.go`
- `src/io/fs/readdir_test.go`

**Predicted Files (11):**
- ❌ `src/go/internal/fsys/fsys.go`
- ❌ `src/io/fs/fs.go`
- ✅ `src/io/fs/readdir.go`
- ❌ `src/io/fs/stat.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16616.go`
- ❌ `src/os/dir.go`
- ❌ `src/os/file.go`
- ❌ `src/os/os.go`
- ❌ `src/os/stat.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io/fs`


### 📊 **Proposal #45454**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.6% | 33.3% | 6.5% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/cfg`
- `src/go/build`
- `src/internal/buildcfg`

**Predicted Directories (28):**
- ❌ `issue48454.dir`
- ❌ `issue48462.dir`
- ❌ `src/asm/internal/arch`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/cmd/internal/sys`
- ❌ `src/cmd/internal/telemetry`
- ❌ `src/cmd/link/internal/amd64`
- ❌ `src/cmd/link/internal/arm`
- ❌ `src/cmd/link/internal/arm64`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode`
- ❌ `src/cmd/link/internal/ppc64`
- ❌ `src/cmd/link/internal/riscv64`
- ❌ `src/cmd/link/internal/s390x`
- ❌ `src/cmd/link/internal/wasm`
- ❌ `src/cmd/link/internal/x86`
- ❌ `src/compile/internal`
- ❌ `src/compile/internal/arm`
- ❌ `src/compile/internal/arm64`
- ❌ `src/compile/internal/ppc64`
- ❌ `src/compile/internal/riscv64`
- ❌ `src/compile/internal/s390x`
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/go/build`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 1.2% | 33.3% | 2.3% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/cfg/cfg.go`
- `src/go/build/build.go`
- `src/internal/buildcfg/cfg.go`

**Predicted Files (85):**
- ❌ `issue48454.dir/a.go`
- ❌ `issue48454.dir/b.go`
- ❌ `issue48462.dir/a.go`
- ❌ `issue48462.dir/main.go`
- ❌ `src/asm/internal/arch/arm.go`
- ❌ `src/asm/internal/arch/arm64.go`
- ❌ `src/asm/internal/arch/ppc64.go`
- ❌ `src/asm/internal/arch/riscv64.go`
- ❌ `src/asm/internal/arch/s390x.go`
- ❌ `src/cmd/dist/buildtag.go`
- ❌ `src/cmd/dist/buildtag_test.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ❌ `src/cmd/internal/objabi/util.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/cmd/internal/sys/arch.go`
- ❌ `src/cmd/internal/sys/args.go`
- ❌ `src/cmd/internal/telemetry/telemetry.go`
- ❌ `src/cmd/internal/telemetry/telemetry_bootstrap.go`
- ❌ `src/cmd/link/internal/amd64/asm.go`
- ❌ `src/cmd/link/internal/amd64/ld.go`
- ❌ `src/cmd/link/internal/arm/asm.go`
- ❌ `src/cmd/link/internal/arm/ld.go`
- ❌ `src/cmd/link/internal/arm64/asm.go`
- ❌ `src/cmd/link/internal/arm64/ld.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/globalmap.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/ifacemethod.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/ifacemethod2.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/ifacemethod3.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/ifacemethod4.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/ifacemethod5.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/ifacemethod6.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/reflectcall.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/structof_funcof.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/typedesc.go`
- ❌ `src/cmd/link/internal/ppc64/asm.go`
- ❌ `src/cmd/link/internal/ppc64/ld.go`
- ❌ `src/cmd/link/internal/riscv64/asm.go`
- ❌ `src/cmd/link/internal/riscv64/ld.go`
- ❌ `src/cmd/link/internal/s390x/asm.go`
- ❌ `src/cmd/link/internal/s390x/ld.go`
- ❌ `src/cmd/link/internal/wasm/ld.go`
- ❌ `src/cmd/link/internal/x86/asm.go`
- ❌ `src/cmd/link/internal/x86/ld.go`
- ❌ `src/compile/internal/arm/galign.go`
- ❌ `src/compile/internal/arm64/galign.go`
- ❌ `src/compile/internal/ppc64/galign.go`
- ❌ `src/compile/internal/riscv64/galign.go`
- ❌ `src/compile/internal/s390x/galign.go`
- ❌ `src/compile/internal/softfloat.go`
- ❌ `src/fixedbugs/issue15920.dir/issue15920.go`
- ❌ `src/fixedbugs/issue16133.dir/issue16133.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ✅ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/runtime/defs_darwin_amd64.go`
- ❌ `src/runtime/defs_darwin_arm64.go`
- ❌ `src/runtime/defs_freebsd_amd64.go`
- ❌ `src/runtime/defs_freebsd_arm.go`
- ❌ `src/runtime/defs_freebsd_arm64.go`
- ❌ `src/runtime/defs_linux_amd64.go`
- ❌ `src/runtime/defs_linux_arm.go`
- ❌ `src/runtime/defs_linux_arm64.go`
- ❌ `src/runtime/defs_linux_ppc64.go`
- ❌ `src/runtime/defs_linux_ppc64le.go`
- ❌ `src/runtime/defs_linux_riscv64.go`
- ❌ `src/runtime/defs_netbsd_amd64.go`
- ❌ `src/runtime/defs_netbsd_arm.go`
- ❌ `src/runtime/defs_netbsd_arm64.go`
- ❌ `src/runtime/defs_openbsd_amd64.go`
- ❌ `src/runtime/defs_openbsd_arm.go`
- ❌ `src/runtime/defs_openbsd_arm64.go`
- ❌ `src/runtime/defs_plan9_amd64.go`
- ❌ `src/runtime/defs_plan9_arm.go`
- ❌ `src/runtime/defs_plan9_arm64.go`
- ❌ `src/runtime/defs_solaris_amd64.go`
- ❌ `src/runtime/defs_solaris_arm.go`
- ❌ `src/runtime/defs_solaris_arm64.go`
- ❌ `src/runtime/defs_windows_amd64.go`
- ❌ `src/runtime/defs_windows_arm.go`
- ❌ `src/runtime/defs_windows_arm64.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/build`


### 📊 **Proposal #50436**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os/exec`

**Predicted Directories (4):**
- ❌ `src/cmd/go`
- ❌ `src/internal/testenv`
- ❌ `src/os`
- ✅ `src/os/exec`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/os/exec/exec.go`
- `src/os/exec/exec_test.go`

**Predicted Files (10):**
- ❌ `src/cmd/go/script_test.go`
- ❌ `src/internal/testenv/testenv.go`
- ✅ `src/os/exec/exec.go`
- ✅ `src/os/exec/exec_test.go`
- ❌ `src/os/exec_linux.go`
- ❌ `src/os/exec_linux_test.go`
- ❌ `src/os/exec_unix.go`
- ❌ `src/os/exec_unix_test.go`
- ❌ `src/os/exec_windows.go`
- ❌ `src/os/exec_windows_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/os/exec`


### 📊 **Proposal #44167**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (4):**
- ❌ `internal/runtime/sys`
- ✅ `src/runtime`
- ❌ `src/runtime/debug`
- ❌ `src/runtime/gc`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 28.6% | 30.8% | 4/14 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (14):**
- `src/runtime/export_test.go`
- `src/runtime/mcache.go`
- `src/runtime/metrics.go`
- `src/runtime/mgc.go`
- `src/runtime/mgcmark.go`
- `src/runtime/mgcpacer.go`
- `src/runtime/mgcpacer_test.go`
- `src/runtime/mgcscavenge.go`
- `src/runtime/mgcsweep.go`
- `src/runtime/mgcwork.go`
- `src/runtime/mstats.go`
- `src/runtime/proc.go`
- `src/runtime/stack.go`
- `src/runtime/symtab.go`

**Predicted Files (12):**
- ❌ `gc.go`
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `runtime.go`
- ❌ `src/runtime/debug/garbage.go`
- ❌ `src/runtime/debug/garbage_test.go`
- ❌ `src/runtime/gc.go`
- ❌ `src/runtime/gc/malloc.go`
- ❌ `src/runtime/gc/scan.go`
- ✅ `src/runtime/mgc.go`
- ✅ `src/runtime/mgcpacer.go`
- ✅ `src/runtime/mgcpacer_test.go`
- ✅ `src/runtime/proc.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 80.0% | 28.6% | 42.1% | 4/14 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime`


### 📊 **Proposal #39178**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (2):**
- ✅ `src/net`
- ❌ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/lookup.go`
- `src/net/lookup_test.go`

**Predicted Files (3):**
- ❌ `src/net/http/client.go`
- ❌ `src/net/http/transport.go`
- ✅ `src/net/lookup.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #46287**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 2/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `src/cmd/dist`
- `src/crypto/x509`
- `src/crypto/x509/internal/macos`
- `src/runtime`

**Predicted Directories (2):**
- ✅ `src/crypto/x509`
- ✅ `src/crypto/x509/internal/macos`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 54.5% | 60.0% | 6/11 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (11):**
- `src/cmd/dist/test.go`
- `src/crypto/x509/cert_pool.go`
- `src/crypto/x509/hybrid_pool_test.go`
- `src/crypto/x509/internal/macos/corefoundation.go`
- `src/crypto/x509/internal/macos/security.go`
- `src/crypto/x509/root_darwin.go`
- `src/crypto/x509/root_windows.go`
- `src/crypto/x509/verify.go`
- `src/crypto/x509/verify_test.go`
- `src/crypto/x509/x509_test.go`
- `src/runtime/sys_darwin.go`

**Predicted Files (9):**
- ✅ `src/crypto/x509/cert_pool.go`
- ❌ `src/crypto/x509/cert_pool_test.go`
- ❌ `src/crypto/x509/example_test.go`
- ✅ `src/crypto/x509/internal/macos/corefoundation.go`
- ✅ `src/crypto/x509/internal/macos/security.go`
- ✅ `src/crypto/x509/verify.go`
- ✅ `src/crypto/x509/verify_test.go`
- ❌ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 54.5% | 60.0% | 6/11 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/crypto/x509`
- `src/crypto/x509/internal/macos`


### 📊 **Proposal #48257**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/go/internal/workcmd`

**Predicted Directories (1):**
- ❌ `src/go/work/workcmd`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/cmd/go/internal/workcmd/use.go`

**Predicted Files (1):**
- ❌ `src/go/work/workcmd/use.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #46293**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 50.0% | 22.2% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/reflect`

**Predicted Directories (7):**
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/reflect`
- ❌ `src/runtime`
- ❌ `src/runtime/maps`
- ❌ `src/types`
- ❌ `test`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/reflect/all_test.go`

**Predicted Files (17):**
- ❌ `map.go`
- ❌ `mapimp.go`
- ❌ `maps.go`
- ❌ `mapsimp.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/map_noswiss.go`
- ❌ `src/reflect/map_swiss.go`
- ❌ `src/reflect/reflect.go`
- ❌ `src/runtime/map.go`
- ❌ `src/runtime/map_test.go`
- ❌ `src/runtime/maps/map.go`
- ❌ `src/runtime/maps/map_test.go`
- ❌ `src/types/map.go`
- ❌ `test/map.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #42026**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 3.3% | 6.4% | 3/90 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (90):**
- `src/archive/tar`
- `src/archive/zip`
- `src/cmd/addr2line`
- `src/cmd/cover`
- `src/cmd/fix`
- `src/cmd/go`
- `src/cmd/go/internal/bug`
- `src/cmd/go/internal/cache`
- `src/cmd/go/internal/cfg`
- `src/cmd/go/internal/clean`
- `src/cmd/go/internal/envcmd`
- `src/cmd/go/internal/fsys`
- `src/cmd/go/internal/generate`
- `src/cmd/go/internal/imports`
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/lockedfile`
- `src/cmd/go/internal/lockedfile/internal/filelock`
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modfetch/codehost`
- `src/cmd/go/internal/modfetch/zip_sum_test`
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/test`
- `src/cmd/go/internal/vcs`
- `src/cmd/go/internal/web`
- `src/cmd/go/internal/work`
- `src/cmd/go/testdata`
- `src/cmd/gofmt`
- `src/cmd/nm`
- `src/cmd/objdump`
- `src/cmd/pack`
- `src/cmd/vet`
- `src/compress/bzip2`
- `src/compress/flate`
- `src/compress/lzw`
- `src/compress/zlib`
- `src/crypto/md5`
- `src/crypto/tls`
- `src/crypto/x509`
- `src/debug/dwarf`
- `src/debug/gosym`
- `src/debug/pe`
- `src/embed/internal/embedtest`
- `src/go/build`
- `src/go/doc`
- `src/go/format`
- `src/go/importer`
- `src/go/internal/gccgoimporter`
- `src/go/internal/gcimporter`
- `src/go/internal/srcimporter`
- `src/go/parser`
- `src/go/printer`
- `src/go/types`
- `src/hash/crc32`
- `src/html/template`
- `src/image/color/palette`
- `src/image/gif`
- `src/image/internal/imageutil`
- `src/image/jpeg`
- `src/image/png`
- `src/index/suffixarray`
- `src/internal/cpu`
- `src/internal/obscuretestdata`
- `src/internal/poll`
- `src/internal/trace`
- `src/io/ioutil`
- `src/log/syslog`
- `src/math/big`
- `src/math/bits`
- `src/mime/multipart`
- `src/net`
- `src/net/http`
- `src/os`
- `src/os/exec`
- `src/os/signal`
- `src/os/user`
- `src/path/filepath`
- `src/runtime`
- `src/runtime/debug`
- `src/runtime/pprof`
- `src/runtime/race`
- `src/runtime/race/testdata`
- `src/runtime/testdata/testprog`
- `src/runtime/testdata/testprogcgo`
- `src/runtime/trace`
- `src/strconv`
- `src/syscall`
- `src/testing`
- `src/text/template`
- `src/time`

**Predicted Directories (4):**
- ❌ `src/io/fs`
- ✅ `src/io/ioutil`
- ✅ `src/os`
- ✅ `src/os/exec`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 53.8% | 3.6% | 6.8% | 7/194 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (194):**
- `src/archive/tar/reader_test.go`
- `src/archive/tar/tar_test.go`
- `src/archive/tar/writer_test.go`
- `src/archive/zip/reader_test.go`
- `src/archive/zip/writer_test.go`
- `src/cmd/addr2line/addr2line_test.go`
- `src/cmd/cover/cover.go`
- `src/cmd/cover/cover_test.go`
- `src/cmd/cover/html.go`
- `src/cmd/fix/main.go`
- `src/cmd/fix/typecheck.go`
- `src/cmd/go/go_test.go`
- `src/cmd/go/go_windows_test.go`
- `src/cmd/go/help_test.go`
- `src/cmd/go/internal/bug/bug.go`
- `src/cmd/go/internal/cache/cache.go`
- `src/cmd/go/internal/cache/cache_test.go`
- `src/cmd/go/internal/cache/default.go`
- `src/cmd/go/internal/cache/hash_test.go`
- `src/cmd/go/internal/cfg/cfg.go`
- `src/cmd/go/internal/clean/clean.go`
- `src/cmd/go/internal/envcmd/env.go`
- `src/cmd/go/internal/fsys/fsys.go`
- `src/cmd/go/internal/fsys/fsys_test.go`
- `src/cmd/go/internal/generate/generate.go`
- `src/cmd/go/internal/imports/scan_test.go`
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/lockedfile/internal/filelock/filelock_test.go`
- `src/cmd/go/internal/lockedfile/lockedfile_test.go`
- `src/cmd/go/internal/modcmd/vendor.go`
- `src/cmd/go/internal/modcmd/verify.go`
- `src/cmd/go/internal/modfetch/cache.go`
- `src/cmd/go/internal/modfetch/cache_test.go`
- `src/cmd/go/internal/modfetch/codehost/codehost.go`
- `src/cmd/go/internal/modfetch/codehost/git_test.go`
- `src/cmd/go/internal/modfetch/codehost/shell.go`
- `src/cmd/go/internal/modfetch/codehost/vcs.go`
- `src/cmd/go/internal/modfetch/coderepo.go`
- `src/cmd/go/internal/modfetch/coderepo_test.go`
- `src/cmd/go/internal/modfetch/fetch.go`
- `src/cmd/go/internal/modfetch/zip_sum_test/zip_sum_test.go`
- `src/cmd/go/internal/modload/init.go`
- `src/cmd/go/internal/modload/query_test.go`
- `src/cmd/go/internal/modload/vendor.go`
- `src/cmd/go/internal/test/test.go`
- `src/cmd/go/internal/vcs/vcs_test.go`
- `src/cmd/go/internal/web/file_test.go`
- `src/cmd/go/internal/work/build_test.go`
- `src/cmd/go/internal/work/buildid.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/go/internal/work/gc.go`
- `src/cmd/go/internal/work/gccgo.go`
- `src/cmd/go/proxy_test.go`
- `src/cmd/go/testdata/addmod.go`
- `src/cmd/go/testdata/savedir.go`
- `src/cmd/gofmt/gofmt.go`
- `src/cmd/gofmt/gofmt_test.go`
- `src/cmd/nm/nm_test.go`
- `src/cmd/objdump/objdump_test.go`
- `src/cmd/pack/pack_test.go`
- `src/cmd/vet/vet_test.go`
- `src/compress/bzip2/bzip2_test.go`
- `src/compress/flate/deflate_test.go`
- `src/compress/flate/huffman_bit_writer_test.go`
- `src/compress/flate/reader_test.go`
- `src/compress/lzw/reader_test.go`
- `src/compress/lzw/writer_test.go`
- `src/compress/zlib/writer_test.go`
- `src/crypto/md5/gen.go`
- `src/crypto/tls/handshake_test.go`
- `src/crypto/tls/link_test.go`
- `src/crypto/tls/tls.go`
- `src/crypto/x509/name_constraints_test.go`
- `src/crypto/x509/root_plan9.go`
- `src/crypto/x509/root_unix.go`
- `src/crypto/x509/root_unix_test.go`
- `src/debug/dwarf/dwarf5ranges_test.go`
- `src/debug/gosym/pclntab_test.go`
- `src/debug/pe/file_test.go`
- `src/embed/internal/embedtest/embedx_test.go`
- `src/go/build/build_test.go`
- `src/go/build/deps_test.go`
- `src/go/doc/doc_test.go`
- `src/go/format/benchmark_test.go`
- `src/go/format/format_test.go`
- `src/go/importer/importer_test.go`
- `src/go/internal/gccgoimporter/importer_test.go`
- `src/go/internal/gcimporter/gcimporter_test.go`
- `src/go/internal/srcimporter/srcimporter.go`
- `src/go/internal/srcimporter/srcimporter_test.go`
- `src/go/parser/error_test.go`
- `src/go/parser/interface.go`
- `src/go/parser/performance_test.go`
- `src/go/printer/performance_test.go`
- `src/go/printer/printer_test.go`
- `src/go/types/check_test.go`
- `src/go/types/hilbert_test.go`
- `src/go/types/stdlib_test.go`
- `src/hash/crc32/gen_const_ppc64le.go`
- `src/html/template/examplefiles_test.go`
- `src/html/template/template.go`
- `src/image/color/palette/gen.go`
- `src/image/gif/reader_test.go`
- `src/image/internal/imageutil/gen.go`
- `src/image/jpeg/reader_test.go`
- `src/image/png/reader_test.go`
- `src/index/suffixarray/gen.go`
- `src/index/suffixarray/suffixarray_test.go`
- `src/internal/cpu/cpu_s390x_test.go`
- `src/internal/obscuretestdata/obscuretestdata.go`
- `src/internal/poll/read_test.go`
- `src/internal/trace/gc_test.go`
- `src/io/ioutil/ioutil.go`
- `src/io/ioutil/tempfile.go`
- `src/io/ioutil/tempfile_test.go`
- `src/log/syslog/syslog_test.go`
- `src/math/big/link_test.go`
- `src/math/bits/make_examples.go`
- `src/math/bits/make_tables.go`
- `src/mime/multipart/formdata.go`
- `src/net/dnsclient_unix_test.go`
- `src/net/error_test.go`
- `src/net/http/filetransport_test.go`
- `src/net/http/fs_test.go`
- `src/net/http/request_test.go`
- `src/net/http/transfer_test.go`
- `src/net/http/transport_test.go`
- `src/net/mockserver_test.go`
- `src/net/net_windows_test.go`
- `src/net/unixsock_test.go`
- `src/os/dir.go`
- `src/os/error_test.go`
- `src/os/example_test.go`
- `src/os/exec/exec_test.go`
- `src/os/exec/lp_unix_test.go`
- `src/os/exec/lp_windows_test.go`
- `src/os/fifo_test.go`
- `src/os/file.go`
- `src/os/file_plan9.go`
- `src/os/os_test.go`
- `src/os/os_unix_test.go`
- `src/os/os_windows_test.go`
- `src/os/path_test.go`
- `src/os/path_windows_test.go`
- `src/os/pipe_test.go`
- `src/os/read_test.go`
- `src/os/removeall_test.go`
- `src/os/signal/signal_test.go`
- `src/os/signal/signal_windows_test.go`
- `src/os/stat_test.go`
- `src/os/tempfile.go`
- `src/os/tempfile_test.go`
- `src/os/timeout_test.go`
- `src/os/user/lookup_plan9.go`
- `src/path/filepath/example_unix_walk_test.go`
- `src/path/filepath/match_test.go`
- `src/path/filepath/path_test.go`
- `src/path/filepath/path_windows_test.go`
- `src/runtime/crash_test.go`
- `src/runtime/crash_unix_test.go`
- `src/runtime/debug/heapdump_test.go`
- `src/runtime/debug_test.go`
- `src/runtime/memmove_linux_amd64_test.go`
- `src/runtime/mkduff.go`
- `src/runtime/mkfastlog2table.go`
- `src/runtime/pprof/pprof_test.go`
- `src/runtime/pprof/proto_test.go`
- `src/runtime/race/output_test.go`
- `src/runtime/race/testdata/io_test.go`
- `src/runtime/runtime-gdb_test.go`
- `src/runtime/runtime-lldb_test.go`
- `src/runtime/signal_windows_test.go`
- `src/runtime/syscall_windows_test.go`
- `src/runtime/testdata/testprog/memprof.go`
- `src/runtime/testdata/testprog/syscalls_linux.go`
- `src/runtime/testdata/testprog/timeprof.go`
- `src/runtime/testdata/testprog/vdso.go`
- `src/runtime/testdata/testprogcgo/pprof.go`
- `src/runtime/testdata/testprogcgo/threadpprof.go`
- `src/runtime/trace/trace_test.go`
- `src/runtime/wincallback.go`
- `src/strconv/makeisprint.go`
- `src/syscall/dirent_test.go`
- `src/syscall/exec_linux_test.go`
- `src/syscall/getdirentries_test.go`
- `src/syscall/syscall_linux_test.go`
- `src/syscall/syscall_unix_test.go`
- `src/syscall/syscall_windows_test.go`
- `src/testing/testing.go`
- `src/testing/testing_test.go`
- `src/text/template/examplefiles_test.go`
- `src/text/template/helper.go`
- `src/text/template/link_test.go`
- `src/time/genzabbrs.go`

**Predicted Files (13):**
- ❌ `src/io/fs/readdir.go`
- ❌ `src/io/fs/readfile.go`
- ❌ `src/io/fs/stat.go`
- ✅ `src/io/ioutil/ioutil.go`
- ✅ `src/io/ioutil/tempfile.go`
- ❌ `src/os/exec/exec.go`
- ✅ `src/os/exec/exec_test.go`
- ✅ `src/os/file.go`
- ❌ `src/os/file_test.go`
- ❌ `src/os/os.go`
- ✅ `src/os/os_test.go`
- ✅ `src/os/tempfile.go`
- ✅ `src/os/tempfile_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 70.0% | 3.6% | 6.9% | 7/194 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/io/ioutil`
- `src/os`
- `src/os/exec`


### 📊 **Proposal #45435**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/sync`

**Predicted Directories (6):**
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/internal/lockedfile`
- ❌ `src/net/http`
- ❌ `src/net/http2/hpack`
- ✅ `src/sync`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 23.5% | 100.0% | 38.1% | 4/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/sync/mutex.go`
- `src/sync/mutex_test.go`
- `src/sync/rwmutex.go`
- `src/sync/rwmutex_test.go`

**Predicted Files (17):**
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/go/internal/lockedfile/lockedfile.go`
- ❌ `src/go/internal/lockedfile/mutex.go`
- ❌ `src/net/http/h2_bundle.go`
- ❌ `src/net/http2/hpack/encode.go`
- ❌ `src/net/http2/hpack/hpack.go`
- ❌ `src/net/http2/hpack/huffman.go`
- ❌ `src/net/http2/hpack/static_table.go`
- ❌ `src/net/http2/hpack/tables.go`
- ✅ `src/sync/mutex.go`
- ✅ `src/sync/mutex_test.go`
- ✅ `src/sync/rwmutex.go`
- ✅ `src/sync/rwmutex_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 4/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/sync`


### 📊 **Proposal #48187**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 13.3% | 100.0% | 23.5% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/version`
- `src/debug/buildinfo`

**Predicted Directories (15):**
- ❌ `cmd/link/internal/ld`
- ❌ `debug`
- ❌ `internal/runtime/sys`
- ❌ `src/cgo/internal/testcarchive`
- ❌ `src/cgo/internal/testcshared`
- ❌ `src/cgo/internal/testcshared/testdata/go2c2go/go`
- ❌ `src/cgo/internal/testcshared/testdata/go2c2go/m1`
- ❌ `src/cgo/internal/testcshared/testdata/go2c2go/m2`
- ✅ `src/cmd/go/internal/version`
- ❌ `src/cmd/link/internal/ld`
- ✅ `src/debug/buildinfo`
- ❌ `src/go/internal/archive`
- ❌ `src/go/internal/gover`
- ❌ `src/go/version`
- ❌ `test`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 100.0% | 16.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/version/version.go`
- `src/debug/buildinfo/buildinfo_test.go`

**Predicted Files (22):**
- ❌ `cmd/link/internal/ld/ar.go`
- ❌ `debug/buildinfo.go`
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `src/cgo/internal/testcarchive/carchive_test.go`
- ❌ `src/cgo/internal/testcshared/cshared_test.go`
- ❌ `src/cgo/internal/testcshared/testdata/go2c2go/go/shlib.go`
- ❌ `src/cgo/internal/testcshared/testdata/go2c2go/m1/main.go`
- ❌ `src/cgo/internal/testcshared/testdata/go2c2go/m2/main.go`
- ✅ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/link/internal/ld/ar.go`
- ❌ `src/debug/buildinfo/buildinfo.go`
- ✅ `src/debug/buildinfo/buildinfo_test.go`
- ❌ `src/go/internal/archive/archive.go`
- ❌ `src/go/internal/archive/archive_test.go`
- ❌ `src/go/internal/gover/version.go`
- ❌ `src/go/version/version.go`
- ❌ `test/issue45242.go`
- ❌ `test/issue45258.go`
- ❌ `test/issue4529.go`
- ❌ `test/issue45323.go`
- ❌ `test/issue45344.go`
- ❌ `test/issue45359.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/go/internal/version`
- `src/debug/buildinfo`


### 📊 **Proposal #37519**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 50.0% | 22.2% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modget`

**Predicted Directories (7):**
- ❌ `cmd/go/internal/get`
- ❌ `cmd/go/internal/modget`
- ❌ `src/cmd/go/internal/get`
- ✅ `src/cmd/go/internal/modget`
- ❌ `src/go/internal/modcmd`
- ❌ `src/go/internal/modget`
- ❌ `src/go/internal/vcweb`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/modfetch/repo.go`
- `src/cmd/go/internal/modfetch/sumdb.go`
- `src/cmd/go/internal/modget/get.go`

**Predicted Files (16):**
- ❌ `cmd/go/internal/get/get.go`
- ❌ `cmd/go/internal/modget/modget.go`
- ❌ `src/cmd/go/internal/get/get.go`
- ❌ `src/cmd/go/internal/modget/modget.go`
- ❌ `src/go/internal/modcmd/download.go`
- ❌ `src/go/internal/modcmd/edit.go`
- ❌ `src/go/internal/modcmd/graph.go`
- ❌ `src/go/internal/modcmd/init.go`
- ❌ `src/go/internal/modcmd/mod.go`
- ❌ `src/go/internal/modcmd/tidy.go`
- ❌ `src/go/internal/modcmd/vendor.go`
- ❌ `src/go/internal/modcmd/verify.go`
- ❌ `src/go/internal/modcmd/why.go`
- ❌ `src/go/internal/modget/get.go`
- ❌ `src/go/internal/modget/query.go`
- ❌ `src/go/internal/vcweb/insecure.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/modget`


### 📊 **Proposal #38627**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/text/template/parse`

**Predicted Directories (2):**
- ❌ `src/html/template`
- ✅ `src/text/template/parse`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/text/template/parse/parse.go`

**Predicted Files (6):**
- ❌ `src/html/template/template.go`
- ❌ `src/html/template/template_test.go`
- ❌ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/lex_test.go`
- ✅ `src/text/template/parse/parse.go`
- ❌ `src/text/template/parse/parse_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/text/template/parse`


### 📊 **Proposal #41260**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (2):**
- ❌ `src/os`
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/testing.go`
- `src/testing/testing_test.go`

**Predicted Files (4):**
- ❌ `src/os/env_test.go`
- ❌ `src/os/exec_test.go`
- ✅ `src/testing/testing.go`
- ✅ `src/testing/testing_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #44505**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/asm/internal/lex`
- `src/cmd/dist`
- `src/sort`

**Predicted Directories (4):**
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/internal/modfetch`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/cmd/asm/internal/lex/tokenizer.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/buildtool.go`
- `src/cmd/dist/test.go`
- `src/cmd/dist/util.go`
- `src/sort/slice.go`

**Predicted Files (9):**
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/go/internal/modfetch/bootstrap.go`
- ❌ `src/go/internal/modfetch/toolchain.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #50429**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/parser`

**Predicted Directories (2):**
- ❌ `ken`
- ❌ `src/go/ast`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/parser/parser.go`
- `src/go/parser/parser_test.go`

**Predicted Files (5):**
- ❌ `ken/range.go`
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_go1.go`
- ❌ `src/go/ast/ast_go118.go`
- ❌ `src/go/ast/ast_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #53573**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (2):**
- ✅ `src/crypto/x509`
- ❌ `src/crypto/x509/pkix`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/x509/parser.go`
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (2):**
- ❌ `src/crypto/x509/pkix/pkix.go`
- ✅ `src/crypto/x509/x509.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #46059**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (1):**
- ✅ `src/net/url`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/url/url.go`
- `src/net/url/url_test.go`

**Predicted Files (2):**
- ✅ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/url`


### 📊 **Proposal #42681**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 20.0% | 13.3% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/asm/internal/lex`
- `src/cmd/dist`
- `src/cmd/go/internal/work`
- `src/cmd/link/internal/ld`
- `src/runtime`

**Predicted Directories (10):**
- ❌ `cmd`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/fixedbugs/issue15646.dir`
- ❌ `src/fixedbugs/issue15838.dir`
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/goexperiment`
- ❌ `src/go/internal/modload`
- ✅ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/asm/internal/lex/input.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/buildruntime.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/go/internal/work/gc.go`
- `src/cmd/link/internal/ld/main.go`
- `src/runtime/heapdump.go`

**Predicted Files (35):**
- ❌ `cmd/compile`
- ❌ `cmd/go`
- ❌ `src/cmd/internal/objabi/util.go`
- ❌ `src/fixedbugs/issue15646.dir/a.go`
- ❌ `src/fixedbugs/issue15646.dir/b.go`
- ❌ `src/fixedbugs/issue15838.dir/a.go`
- ❌ `src/fixedbugs/issue15838.dir/b.go`
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/go/goexperiment/flags.go`
- ❌ `src/go/internal/modload/build.go`
- ❌ `src/go/internal/modload/edit.go`
- ❌ `src/go/internal/modload/help.go`
- ❌ `src/go/internal/modload/import.go`
- ❌ `src/go/internal/modload/init.go`
- ❌ `src/go/internal/modload/list.go`
- ❌ `src/go/internal/modload/load.go`
- ❌ `src/go/internal/modload/modfile.go`
- ❌ `src/go/internal/modload/mvs.go`
- ❌ `src/go/internal/modload/query.go`
- ❌ `src/go/internal/modload/search.go`
- ❌ `src/go/internal/modload/vendor.go`
- ❌ `src/runtime/defs_darwin.go`
- ❌ `src/runtime/defs_darwin_amd64.go`
- ❌ `src/runtime/defs_darwin_arm64.go`
- ❌ `src/runtime/race.go`
- ❌ `src/runtime/runtime.go`
- ❌ `src/runtime/runtime_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime`


### 📊 **Proposal #40592**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/encoding/json`
- `src/reflect`

**Predicted Directories (3):**
- ❌ `interface`
- ✅ `src/reflect`
- ❌ `src/reflectlite`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 33.3% | 14.3% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/encoding/json/encode.go`
- `src/reflect/all_test.go`
- `src/reflect/deepequal.go`
- `src/reflect/set_test.go`
- `src/reflect/type.go`
- `src/reflect/value.go`

**Predicted Files (22):**
- ❌ `interface/convert.go`
- ❌ `interface/convert1.go`
- ❌ `interface/convert2.go`
- ❌ `interface/convert3.go`
- ❌ `interface/convert4.go`
- ❌ `interface/convert5.go`
- ❌ `interface/convert6.go`
- ❌ `interface/convert7.go`
- ❌ `interface/convert8.go`
- ❌ `interface/pointer.go`
- ❌ `interface/struct.go`
- ❌ `reflectmethod1.go`
- ❌ `reflectmethod2.go`
- ❌ `reflectmethod3.go`
- ❌ `reflectmethod4.go`
- ❌ `reflectmethod5.go`
- ❌ `reflectmethod6.go`
- ❌ `reflectmethod7.go`
- ❌ `reflectmethod8.go`
- ✅ `src/reflect/type.go`
- ✅ `src/reflect/value.go`
- ❌ `src/reflectlite/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 2/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #51644**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/binary`

**Predicted Directories (5):**
- ❌ `src`
- ✅ `src/encoding/binary`
- ❌ `src/issue15646.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/binary/varint.go`
- `src/encoding/binary/varint_test.go`

**Predicted Files (12):**
- ❌ `src/encoding/binary/binary.go`
- ❌ `src/encoding/binary/binary_test.go`
- ✅ `src/encoding/binary/varint.go`
- ✅ `src/encoding/binary/varint_test.go`
- ❌ `src/issue15646.dir/issue15646.go`
- ❌ `src/issue15838.go`
- ❌ `src/issue15920.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16616.dir/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/binary`


### 📊 **Proposal #34527**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/cmd/go/internal/cfg`
- `src/cmd/go/internal/clean`
- `src/cmd/go/internal/envcmd`
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modfetch/codehost`
- `src/cmd/go/internal/modload`

**Predicted Directories (2):**
- ❌ `src/go/internal/modcmd`
- ❌ `src/go/internal/modfetch`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/12 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (12):**
- `src/cmd/go/internal/cfg/cfg.go`
- `src/cmd/go/internal/clean/clean.go`
- `src/cmd/go/internal/envcmd/env.go`
- `src/cmd/go/internal/modfetch/cache.go`
- `src/cmd/go/internal/modfetch/codehost/codehost.go`
- `src/cmd/go/internal/modfetch/codehost/git_test.go`
- `src/cmd/go/internal/modfetch/codehost/shell.go`
- `src/cmd/go/internal/modfetch/coderepo_test.go`
- `src/cmd/go/internal/modfetch/fetch.go`
- `src/cmd/go/internal/modfetch/sumdb.go`
- `src/cmd/go/internal/modload/init.go`
- `src/cmd/go/internal/modload/query_test.go`

**Predicted Files (4):**
- ❌ `src/go/internal/modcmd/download.go`
- ❌ `src/go/internal/modfetch/cache.go`
- ❌ `src/go/internal/modfetch/proxy.go`
- ❌ `src/go/internal/modfetch/sumdb.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/12 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #45628**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/xml`

**Predicted Directories (4):**
- ❌ `encoding/xml`
- ❌ `src/encoding`
- ✅ `src/encoding/xml`
- ❌ `src/runtime/pprof`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/xml/xml.go`
- `src/encoding/xml/xml_test.go`

**Predicted Files (6):**
- ❌ `encoding/xml/xml.go`
- ❌ `src/encoding/xml`
- ✅ `src/encoding/xml/xml.go`
- ✅ `src/encoding/xml/xml_test.go`
- ❌ `src/runtime/pprof/pprof.go`
- ❌ `src/runtime/pprof/pprof_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/xml`


### 📊 **Proposal #46746**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (4):**
- ❌ `interface`
- ✅ `src/reflect`
- ❌ `src/reflectlite`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.8% | 50.0% | 7.1% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (26):**
- ❌ `interface/convert.go`
- ❌ `interface/convert1.go`
- ❌ `interface/convert2.go`
- ❌ `interface/convert3.go`
- ❌ `interface/convert4.go`
- ❌ `interface/embed.go`
- ❌ `interface/embed1.go`
- ❌ `interface/embed2.go`
- ❌ `interface/embed3.go`
- ❌ `interface/explicit.go`
- ❌ `interface/fail.go`
- ❌ `interface/fake.go`
- ❌ `interface/noeq.go`
- ❌ `interface/pointer.go`
- ❌ `interface/private.go`
- ❌ `interface/receiver.go`
- ❌ `interface/receiver1.go`
- ❌ `interface/recursive.go`
- ❌ `interface/recursive1.go`
- ❌ `interface/recursive2.go`
- ❌ `interface/struct.go`
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/value.go`
- ❌ `src/reflectlite/type.go`
- ❌ `src/reflectlite/value.go`
- ❌ `src/runtime/reflect_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #44940**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/unicode/utf16`

**Predicted Directories (5):**
- ❌ `src`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16317.dir`
- ❌ `src/issue16616.dir`
- ✅ `src/unicode/utf16`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 100.0% | 30.8% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/unicode/utf16/utf16.go`
- `src/unicode/utf16/utf16_test.go`

**Predicted Files (11):**
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16317.dir/a.go`
- ❌ `src/issue16317.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ✅ `src/unicode/utf16/utf16.go`
- ✅ `src/unicode/utf16/utf16_test.go`
- ❌ `src/utf8.go`
- ❌ `utf.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/unicode/utf16`


### 📊 **Proposal #41066**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (6):**
- ✅ `src/crypto/tls`
- ❌ `src/issue16616.dir`
- ❌ `src/net`
- ❌ `src/net/http`
- ❌ `src/testtls`
- ❌ `vendor/golang.org/x/net`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.2% | 50.0% | 11.1% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/tls/conn.go`
- `src/crypto/tls/tls_test.go`

**Predicted Files (16):**
- ❌ `src/crypto/tls/alert.go`
- ❌ `src/crypto/tls/auth.go`
- ❌ `src/crypto/tls/cache.go`
- ❌ `src/crypto/tls/cipher_suites.go`
- ❌ `src/crypto/tls/common.go`
- ✅ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/defaults.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/net.go`
- ❌ `src/testtls/tls.go`
- ❌ `src/testtls/tls_test.go`
- ❌ `vendor/golang.org/x/net/net.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 50.0% | 16.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #41184**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.8% | 25.0% | 27.6% | 4/16 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (16):**
- `src/cmd/asm/internal/asm`
- `src/cmd/asm/internal/lex`
- `src/cmd/fix`
- `src/cmd/go/internal/fix`
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/work`
- `src/cmd/vendor/golang.org/x/sys/unix`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/loopclosure`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/unitchecker`
- `src/cmd/vet`
- `src/go/build`
- `src/go/build/constraint`
- `src/go/printer`
- `src/runtime`
- `src/runtime/pprof`

**Predicted Directories (13):**
- ❌ `cmd`
- ❌ `go`
- ❌ `src/cmd/dist`
- ✅ `src/cmd/fix`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/vet`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16317.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/go/build`
- ✅ `src/go/build/constraint`
- ❌ `src/go/internal/modload`
- ✅ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 13.3% | 20.0% | 16.0% | 6/30 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (30):**
- `src/cmd/asm/internal/asm/endtoend_test.go`
- `src/cmd/asm/internal/asm/parse.go`
- `src/cmd/asm/internal/lex/input.go`
- `src/cmd/asm/internal/lex/lex_test.go`
- `src/cmd/asm/internal/lex/tokenizer.go`
- `src/cmd/fix/buildtag.go`
- `src/cmd/fix/buildtag_test.go`
- `src/cmd/fix/fix.go`
- `src/cmd/fix/main.go`
- `src/cmd/fix/main_test.go`
- `src/cmd/go/internal/fix/fix.go`
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
- `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/loopclosure/loopclosure.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/unitchecker/unitchecker.go`
- `src/cmd/vet/vet_test.go`
- `src/go/build/build.go`
- `src/go/build/build_test.go`
- `src/go/build/constraint/expr.go`
- `src/go/build/constraint/expr_test.go`
- `src/go/printer/gobuild.go`
- `src/go/printer/printer.go`
- `src/runtime/auxv_none.go`
- `src/runtime/mkduff.go`
- `src/runtime/mkpreempt.go`
- `src/runtime/pprof/mprof_test.go`
- `src/runtime/wincallback.go`

**Predicted Files (45):**
- ❌ `cmd/compile`
- ❌ `cmd/go`
- ❌ `go/build`
- ❌ `src/cmd/dist/buildtag.go`
- ❌ `src/cmd/dist/buildtag_test.go`
- ✅ `src/cmd/fix/buildtag.go`
- ✅ `src/cmd/fix/buildtag_test.go`
- ❌ `src/cmd/go/build.go`
- ❌ `src/cmd/go/parse.go`
- ❌ `src/cmd/go/vet.go`
- ❌ `src/cmd/go/vet/buildtag.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16317.dir/a.go`
- ❌ `src/fixedbugs/issue16317.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ✅ `src/go/build/build.go`
- ✅ `src/go/build/build_test.go`
- ❌ `src/go/build/constraint.go`
- ✅ `src/go/build/constraint/expr.go`
- ✅ `src/go/build/constraint/expr_test.go`
- ❌ `src/go/build/constraint/vers.go`
- ❌ `src/go/build/constraint/vers_test.go`
- ❌ `src/go/internal/modload/build.go`
- ❌ `src/go/internal/modload/build_test.go`
- ❌ `src/runtime/defs_darwin.go`
- ❌ `src/runtime/defs_darwin_amd64.go`
- ❌ `src/runtime/defs_darwin_arm64.go`
- ❌ `src/runtime/defs_linux.go`
- ❌ `src/runtime/defs_linux_amd64.go`
- ❌ `src/runtime/defs_linux_arm64.go`
- ❌ `src/runtime/defs_windows.go`
- ❌ `src/runtime/defs_windows_amd64.go`
- ❌ `src/runtime/defs_windows_arm64.go`
- ❌ `src/runtime/race.go`
- ❌ `src/runtime/race_darwin_amd64.go`
- ❌ `src/runtime/race_darwin_arm64.go`
- ❌ `src/runtime/race_linux_test.go`
- ❌ `src/runtime/race_test.go`
- ❌ `src/runtime/race_unix_test.go`
- ❌ `src/runtime/race_windows_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 24.0% | 20.0% | 21.8% | 6/30 |

##### Correct Directories Used for Evaluation

**Correct Directories (4):**
- `src/cmd/fix`
- `src/go/build`
- `src/go/build/constraint`
- `src/runtime`


### 📊 **Proposal #48866**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 100.0% | 20.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/mime`

**Predicted Directories (9):**
- ❌ `bytes`
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16317.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/internal/obj`
- ✅ `src/mime`
- ❌ `src/net/http`
- ❌ `src/terminal/pkgbits`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.5% | 100.0% | 17.4% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/mime/mediatype.go`
- `src/mime/mediatype_test.go`

**Predicted Files (21):**
- ❌ `bytes/boundary_test.go`
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16317.dir/a.go`
- ❌ `src/fixedbugs/issue16317.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/go/internal/obj/objfile.go`
- ❌ `src/go/internal/obj/objfile_test.go`
- ✅ `src/mime/mediatype.go`
- ✅ `src/mime/mediatype_test.go`
- ❌ `src/mime/mime.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/http_test.go`
- ❌ `src/terminal/pkgbits/decoder.go`
- ❌ `src/terminal/pkgbits/encoder.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/mime`


### 📊 **Proposal #50332**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/11 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (11):**
- `src/cmd/doc`
- `src/cmd/go`
- `src/cmd/go/internal/base`
- `src/cmd/go/internal/bug`
- `src/cmd/go/internal/envcmd`
- `src/cmd/go/internal/fmtcmd`
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/tool`
- `src/cmd/go/internal/version`
- `src/cmd/go/internal/work`
- `src/cmd/go/internal/workcmd`

**Predicted Directories (0):**

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/21 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (21):**
- `src/cmd/doc/main.go`
- `src/cmd/go/chdir_test.go`
- `src/cmd/go/internal/base/flag.go`
- `src/cmd/go/internal/bug/bug.go`
- `src/cmd/go/internal/envcmd/env.go`
- `src/cmd/go/internal/fmtcmd/fmt.go`
- `src/cmd/go/internal/modcmd/download.go`
- `src/cmd/go/internal/modcmd/edit.go`
- `src/cmd/go/internal/modcmd/graph.go`
- `src/cmd/go/internal/modcmd/init.go`
- `src/cmd/go/internal/modcmd/tidy.go`
- `src/cmd/go/internal/modcmd/vendor.go`
- `src/cmd/go/internal/modcmd/verify.go`
- `src/cmd/go/internal/modcmd/why.go`
- `src/cmd/go/internal/tool/tool.go`
- `src/cmd/go/internal/version/version.go`
- `src/cmd/go/internal/work/build.go`
- `src/cmd/go/internal/workcmd/edit.go`
- `src/cmd/go/internal/workcmd/init.go`
- `src/cmd/go/internal/workcmd/sync.go`
- `src/cmd/go/internal/workcmd/use.go`

**Predicted Files (0):**

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/21 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #53466**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 33.3% | 18.2% | 2/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/cmd/dist`
- `src/cmd/link`
- `src/cmd/link/internal/ld`
- `src/cmd/link/internal/riscv64`
- `src/runtime`
- `src/syscall`

**Predicted Directories (16):**
- ❌ `src/asm/internal/arch`
- ❌ `src/compile/internal/abi`
- ❌ `src/compile/internal/arch/riscv64`
- ❌ `src/internal/goarch`
- ❌ `src/internal/goos`
- ❌ `src/issue15646.dir`
- ❌ `src/issue15838.dir`
- ❌ `src/issue15920.dir`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`
- ❌ `src/os`
- ✅ `src/runtime`
- ❌ `src/runtime/cgo`
- ❌ `src/runtime/riscv`
- ❌ `src/sys`
- ✅ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.1% | 40.0% | 18.6% | 4/10 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (10):**
- `src/cmd/dist/main.go`
- `src/cmd/dist/test.go`
- `src/cmd/link/elf_test.go`
- `src/cmd/link/internal/ld/lib.go`
- `src/cmd/link/internal/riscv64/obj.go`
- `src/cmd/link/link_test.go`
- `src/runtime/defs_freebsd_riscv64.go`
- `src/runtime/vdso_freebsd_riscv64.go`
- `src/syscall/syscall_freebsd_riscv64.go`
- `src/syscall/zsyscall_freebsd_riscv64.go`

**Predicted Files (33):**
- ❌ `src/asm/internal/arch/riscv64.go`
- ❌ `src/compile/internal/abi/abi.go`
- ❌ `src/compile/internal/abi/abiutils.go`
- ❌ `src/compile/internal/abi/abiutils_test.go`
- ❌ `src/compile/internal/arch/riscv64/galign.go`
- ❌ `src/compile/internal/arch/riscv64/ggen.go`
- ❌ `src/compile/internal/arch/riscv64/rewriteRISCV64.go`
- ❌ `src/compile/internal/arch/riscv64/rewriteRISCV64latelower.go`
- ❌ `src/compile/internal/arch/riscv64/ssa.go`
- ❌ `src/internal/goarch/goarch_riscv64.go`
- ❌ `src/internal/goos/zgoos_freebsd.go`
- ❌ `src/issue15646.dir/issue15646.go`
- ❌ `src/issue15838.dir/issue15838.go`
- ❌ `src/issue15920.dir/issue15920.go`
- ❌ `src/issue16133.dir/issue16133.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/os/dirent_freebsd.go`
- ❌ `src/os/stat_freebsd.go`
- ❌ `src/runtime/cgo/freebsd.go`
- ✅ `src/runtime/defs_freebsd_riscv64.go`
- ❌ `src/runtime/os_freebsd_riscv64.go`
- ❌ `src/runtime/riscv/riscv.go`
- ❌ `src/runtime/riscv/syscall.go`
- ❌ `src/runtime/signal_freebsd_riscv64.go`
- ✅ `src/runtime/vdso_freebsd_riscv64.go`
- ❌ `src/sys/syscall_freebsd_riscv64.go`
- ❌ `src/syscall/defs_linux_riscv64.go`
- ✅ `src/syscall/syscall_freebsd_riscv64.go`
- ❌ `src/syscall/sysnum_freebsd.go`
- ❌ `src/syscall/sysnum_freebsd_riscv64.go`
- ❌ `src/syscall/types_freebsd_riscv64.go`
- ❌ `src/syscall/zerrors_freebsd_riscv64.go`
- ✅ `src/syscall/zsyscall_freebsd_riscv64.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 36.4% | 40.0% | 38.1% | 4/10 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/runtime`
- `src/syscall`


### 📊 **Proposal #49097**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (2):**
- ✅ `src/net`
- ❌ `src/net/netip`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 33.3% | 33.3% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/net/dial.go`
- `src/net/iprawsock.go`
- `src/net/net.go`
- `src/net/tcpsock.go`
- `src/net/udpsock.go`
- `src/net/unixsock.go`

**Predicted Files (6):**
- ✅ `src/net/dial.go`
- ❌ `src/net/ip.go`
- ✅ `src/net/net.go`
- ❌ `src/net/netip/netip.go`
- ❌ `src/net/tcp.go`
- ❌ `src/net/udp.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 33.3% | 36.4% | 2/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #49390**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/dist`
- `src/internal/testenv`

**Predicted Directories (6):**
- ❌ `cmd/compile/internal/flags`
- ❌ `src/cmd/compile`
- ❌ `src/runtime`
- ❌ `src/runtime/atomic`
- ❌ `src/runtime/sys`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/internal/testenv/noopt.go`
- `src/internal/testenv/opt.go`
- `src/internal/testenv/testenv.go`

**Predicted Files (12):**
- ❌ `cmd/compile/internal/flags/flags.go`
- ❌ `cmd/compile/internal/flags/flags_test.go`
- ❌ `src/cmd/compile/doc.go`
- ❌ `src/runtime/atomic/atomic.go`
- ❌ `src/runtime/atomic/atomic_test.go`
- ❌ `src/runtime/runtime.go`
- ❌ `src/runtime/runtime_test.go`
- ❌ `src/runtime/sys/sys.go`
- ❌ `src/runtime/sys/sys_test.go`
- ❌ `src/syscall/net.go`
- ❌ `src/syscall/syscall.go`
- ❌ `src/syscall/syscall_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #39351**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/expvar`
- `src/sync/atomic`

**Predicted Directories (2):**
- ❌ `src/runtime/atomic`
- ✅ `src/sync/atomic`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 25.0% | 25.0% | 1/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/expvar/expvar.go`
- `src/expvar/expvar_test.go`
- `src/sync/atomic/value.go`
- `src/sync/atomic/value_test.go`

**Predicted Files (4):**
- ❌ `src/runtime/atomic/atomic.go`
- ❌ `src/sync/atomic/atomic.go`
- ❌ `src/sync/atomic/atomic_test.go`
- ✅ `src/sync/atomic/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 25.0% | 28.6% | 1/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/sync/atomic`


### 📊 **Proposal #47142**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/database/sql`

**Predicted Directories (6):**
- ✅ `src/database/sql`
- ❌ `src/database/sql/driver`
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16317.dir`
- ❌ `src/fixedbugs/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.1% | 33.3% | 11.8% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/database/sql/fakedb_test.go`
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`

**Predicted Files (14):**
- ❌ `src/database/sql/driver.go`
- ❌ `src/database/sql/driver/driver.go`
- ✅ `src/database/sql/sql.go`
- ❌ `src/fixedbugs/issue15920.dir/a.go`
- ❌ `src/fixedbugs/issue15920.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16317.dir/a.go`
- ❌ `src/fixedbugs/issue16317.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/database/sql`


### 📊 **Proposal #46742**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 20.0% | 14.3% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/compile/internal/typecheck`
- `src/cmd/compile/internal/walk`
- `src/runtime`
- `src/runtime/testdata/testprog`
- `test`

**Predicted Directories (9):**
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/internal/unsafe`
- ✅ `src/runtime`
- ❌ `src/runtime/asan`
- ❌ `src/runtime/debug`
- ❌ `src/unsafe`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/compile/internal/typecheck/builtin.go`
- `src/cmd/compile/internal/typecheck/func.go`
- `src/cmd/compile/internal/walk/builtin.go`
- `src/runtime/checkptr.go`
- `src/runtime/checkptr_test.go`
- `src/runtime/testdata/testprog/checkptr.go`
- `test/unsafebuiltins.go`

**Predicted Files (34):**
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/flag_test.go`
- ❌ `src/cmd/internal/objfile/line.go`
- ❌ `src/cmd/internal/objfile/line_test.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/objfile.go`
- ❌ `src/cmd/internal/objfile/path_test.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/reloctype.go`
- ❌ `src/cmd/internal/objfile/reloctype_string.go`
- ❌ `src/cmd/internal/objfile/reloctype_test.go`
- ❌ `src/cmd/internal/objfile/stack.go`
- ❌ `src/cmd/internal/objfile/stack_test.go`
- ❌ `src/cmd/internal/objfile/symkind.go`
- ❌ `src/cmd/internal/objfile/symkind_string.go`
- ❌ `src/cmd/internal/objfile/symkind_test.go`
- ❌ `src/cmd/internal/objfile/util.go`
- ❌ `src/cmd/internal/objfile/util_test.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/go/internal/unsafe/unsafe.go`
- ❌ `src/runtime/asan/asan.go`
- ❌ `src/runtime/debug/garbage.go`
- ❌ `src/runtime/slice.go`
- ❌ `src/runtime/slice_test.go`
- ❌ `src/runtime/unsafe.go`
- ❌ `src/unsafe/unsafe.go`
- ❌ `unsafe_slice_data.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime`


### 📊 **Proposal #46505**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/sha256`
- `src/crypto/sha512`

**Predicted Directories (3):**
- ❌ `interface`
- ❌ `ken`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/sha256/sha256.go`
- `src/crypto/sha512/sha512.go`

**Predicted Files (8):**
- ❌ `interface/convert.go`
- ❌ `interface/convert1.go`
- ❌ `interface/convert2.go`
- ❌ `interface/convert3.go`
- ❌ `interface/convert4.go`
- ❌ `ken/convert.go`
- ❌ `src/runtime/slice.go`
- ❌ `src/runtime/slice_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #52376**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (3):**
- ✅ `src/reflect`
- ❌ `src/reflectlite`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (5):**
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/value.go`
- ❌ `src/reflectlite/set_test.go`
- ❌ `src/reflectlite/value.go`
- ❌ `src/runtime/reflect_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #44815**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/bufio`

**Predicted Directories (5):**
- ❌ `src/bio`
- ✅ `src/bufio`
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`
- ❌ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/bufio/bufio.go`
- `src/bufio/bufio_test.go`

**Predicted Files (14):**
- ❌ `src/bio/buf.go`
- ✅ `src/bufio/bufio.go`
- ✅ `src/bufio/bufio_test.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/transfer.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/bufio`


### 📊 **Proposal #45033**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/strconv`

**Predicted Directories (6):**
- ❌ `src/bufio`
- ❌ `src/fmt`
- ❌ `src/reflect`
- ✅ `src/strconv`
- ❌ `src/strconv/quoted`
- ❌ `src/text/template/parse`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 50.0% | 22.2% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/strconv/bytealg.go`
- `src/strconv/bytealg_bootstrap.go`
- `src/strconv/quote.go`
- `src/strconv/quote_test.go`

**Predicted Files (14):**
- ❌ `src/bufio/scan.go`
- ❌ `src/fmt/scan.go`
- ❌ `src/reflect/type.go`
- ❌ `src/strconv/atoi.go`
- ❌ `src/strconv/atoi_test.go`
- ✅ `src/strconv/quote.go`
- ✅ `src/strconv/quote_test.go`
- ❌ `src/strconv/quoted.go`
- ❌ `src/strconv/quoted/quoted.go`
- ❌ `src/strconv/quoted/quoted_test.go`
- ❌ `src/strconv/strconv.go`
- ❌ `src/strconv/strconv_test.go`
- ❌ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/lex_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 50.0% | 36.4% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/strconv`


### 📊 **Proposal #48218**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (2):**
- ✅ `src/reflect`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/value.go`
- `src/reflect/visiblefields_test.go`

**Predicted Files (2):**
- ✅ `src/reflect/value.go`
- ❌ `src/runtime/reflect_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #47066**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (4):**
- ✅ `src/reflect`
- ❌ `src/reflectlite`
- ❌ `src/runtime`
- ❌ `src/runtime/race/testdata`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (5):**
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/value.go`
- ❌ `src/reflectlite/value.go`
- ❌ `src/runtime/race/testdata/reflect_test.go`
- ❌ `src/runtime/reflect_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #51572**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.7% | 100.0% | 19.4% | 3/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/dist`
- `src/cmd/go/internal/imports`
- `src/go/build`

**Predicted Directories (28):**
- ❌ `cgo`
- ❌ `src/archive/tar`
- ✅ `src/cmd/dist`
- ✅ `src/cmd/go/internal/imports`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/telemetrystats`
- ❌ `src/cmd/go/internal/toolchain`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/fixedbugs/issue15920.dir`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/go/build`
- ❌ `src/go/build/constraint`
- ❌ `src/go/build/testdata/alltags`
- ❌ `src/go/build/testdata/cgo_disabled`
- ❌ `src/go/build/testdata/directives`
- ❌ `src/go/build/testdata/multi`
- ❌ `src/go/build/testdata/non_source_tags`
- ❌ `src/go/build/testdata/other`
- ❌ `src/go/build/testdata/other/file`
- ❌ `src/net/http`
- ❌ `src/net/http/httptest`
- ❌ `src/net/http/httputil`
- ❌ `src/runtime`
- ❌ `src/sys/unix`
- ❌ `src/syscall`
- ❌ `src/syscall/unix`
- ❌ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 1.4% | 33.3% | 2.7% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/dist/build.go`
- `src/cmd/go/internal/imports/build.go`
- `src/go/build/build.go`

**Predicted Files (70):**
- ❌ `cgo/cgo_unix_test.go`
- ❌ `cgo/test_unix.go`
- ❌ `src/archive/tar/stat_unix.go`
- ❌ `src/cmd/dist/buildtag.go`
- ❌ `src/cmd/dist/buildtag_test.go`
- ❌ `src/cmd/go/internal/imports/tags.go`
- ❌ `src/cmd/go/internal/modload/stat_unix.go`
- ❌ `src/cmd/go/internal/telemetrystats/version_unix.go`
- ❌ `src/cmd/go/internal/toolchain/path_unix.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/build_test.go`
- ❌ `src/fixedbugs/issue15920.dir/issue15920.go`
- ❌ `src/fixedbugs/issue16133.dir/issue16133.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ✅ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/go/build/constraint/expr.go`
- ❌ `src/go/build/constraint/expr_test.go`
- ❌ `src/go/build/testdata/alltags/alltags.go`
- ❌ `src/go/build/testdata/alltags/x_netbsd_arm.go`
- ❌ `src/go/build/testdata/cgo_disabled/cgo_disabled.go`
- ❌ `src/go/build/testdata/cgo_disabled/empty.go`
- ❌ `src/go/build/testdata/directives/a.go`
- ❌ `src/go/build/testdata/directives/a_test.go`
- ❌ `src/go/build/testdata/directives/b_test.go`
- ❌ `src/go/build/testdata/directives/c_test.go`
- ❌ `src/go/build/testdata/directives/d_test.go`
- ❌ `src/go/build/testdata/directives/e.go`
- ❌ `src/go/build/testdata/multi/file.go`
- ❌ `src/go/build/testdata/multi/file_appengine.go`
- ❌ `src/go/build/testdata/non_source_tags/non_source_tags.go`
- ❌ `src/go/build/testdata/other/file/file.go`
- ❌ `src/go/build/testdata/other/main.go`
- ❌ `src/net/http/client.go`
- ❌ `src/net/http/client_test.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/http_test.go`
- ❌ `src/net/http/httptest/httptest.go`
- ❌ `src/net/http/httputil/httputil.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/server_test.go`
- ❌ `src/runtime/os_unix.go`
- ❌ `src/runtime/sys_aix.go`
- ❌ `src/runtime/sys_dragonfly.go`
- ❌ `src/runtime/sys_freebsd.go`
- ❌ `src/runtime/sys_linux.go`
- ❌ `src/runtime/sys_netbsd.go`
- ❌ `src/runtime/sys_openbsd.go`
- ❌ `src/runtime/sys_solaris.go`
- ❌ `src/runtime/sys_unix.go`
- ❌ `src/sys/unix/syscall_darwin.go`
- ❌ `src/sys/unix/syscall_freebsd.go`
- ❌ `src/sys/unix/syscall_linux.go`
- ❌ `src/sys/unix/syscall_netbsd.go`
- ❌ `src/sys/unix/syscall_openbsd.go`
- ❌ `src/sys/unix/syscall_unix.go`
- ❌ `src/syscall/env_unix.go`
- ❌ `src/syscall/exec_unix.go`
- ❌ `src/syscall/exec_unix_test.go`
- ❌ `src/syscall/sockcmsg_unix.go`
- ❌ `src/syscall/sockcmsg_unix_other.go`
- ❌ `src/syscall/syscall_unix.go`
- ❌ `src/syscall/syscall_unix_test.go`
- ❌ `src/syscall/unix/errno_unix.go`
- ❌ `src/syscall/unix/fcntl_unix.go`
- ❌ `src/syscall/unix/nonblocking_unix.go`
- ❌ `src/syscall/unix/syscall.go`
- ❌ `src/time/sys_unix.go`
- ❌ `src/time/zoneinfo_unix.go`
- ❌ `src/time/zoneinfo_unix_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 33.3% | 25.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/cmd/dist`
- `src/cmd/go/internal/imports`
- `src/go/build`


### 📊 **Proposal #39057**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/log`

**Predicted Directories (1):**
- ✅ `src/log`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/log/log_test.go`

**Predicted Files (1):**
- ❌ `src/log/log.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/log`


### 📊 **Proposal #38781**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/net/http`
- `src/testing/iotest`

**Predicted Directories (2):**
- ❌ `src/io`
- ✅ `src/testing/iotest`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 40.0% | 40.0% | 2/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/net/http/transport_test.go`
- `src/testing/iotest/example_test.go`
- `src/testing/iotest/logger_test.go`
- `src/testing/iotest/reader.go`
- `src/testing/iotest/reader_test.go`

**Predicted Files (5):**
- ❌ `src/io/io.go`
- ❌ `src/io/io_test.go`
- ❌ `src/testing/iotest/iotest.go`
- ✅ `src/testing/iotest/reader.go`
- ✅ `src/testing/iotest/reader_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 40.0% | 50.0% | 2/5 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing/iotest`


### 📊 **Proposal #36771**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/strconv`

**Predicted Directories (3):**
- ❌ `src/archive/tar`
- ❌ `src/fmt`
- ✅ `src/strconv`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 66.7% | 16.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/strconv/atoc.go`
- `src/strconv/atoc_test.go`
- `src/strconv/ctoa.go`

**Predicted Files (22):**
- ❌ `cmplx.go`
- ❌ `convert.go`
- ❌ `src/archive/tar/strconv.go`
- ❌ `src/archive/tar/strconv_test.go`
- ❌ `src/fmt/print.go`
- ❌ `src/fmt/scan.go`
- ❌ `src/strconv/atob.go`
- ❌ `src/strconv/atob_test.go`
- ✅ `src/strconv/atoc.go`
- ✅ `src/strconv/atoc_test.go`
- ❌ `src/strconv/atof.go`
- ❌ `src/strconv/atof_test.go`
- ❌ `src/strconv/atoi.go`
- ❌ `src/strconv/atoi_test.go`
- ❌ `src/strconv/ftoa.go`
- ❌ `src/strconv/ftoa_test.go`
- ❌ `src/strconv/internal_test.go`
- ❌ `src/strconv/itoa.go`
- ❌ `src/strconv/itoa_test.go`
- ❌ `src/strconv/quote.go`
- ❌ `src/strconv/quote_test.go`
- ❌ `src/strconv/strconv_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 66.7% | 21.1% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/strconv`


### 📊 **Proposal #44435**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modload`

**Predicted Directories (3):**
- ❌ `src/go/modcmd`
- ❌ `src/go/modfetch`
- ❌ `src/go/modload`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modcmd/download.go`
- `src/cmd/go/internal/modload/modfile.go`

**Predicted Files (4):**
- ❌ `src/go/modcmd/download.go`
- ❌ `src/go/modfetch/cache.go`
- ❌ `src/go/modfetch/fetch.go`
- ❌ `src/go/modload/modfile.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #50101**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/syscall/unix`
- `src/net`

**Predicted Directories (2):**
- ❌ `src`
- ✅ `src/net`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 23.1% | 35.3% | 3/13 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (13):**
- `src/internal/syscall/unix/net_darwin.go`
- `src/net/cgo_unix.go`
- `src/net/cgo_unix_cgo_res.go`
- `src/net/cgo_unix_cgo_resn.go`
- `src/net/cgo_unix_syscall.go`
- `src/net/conf.go`
- `src/net/dnsclient.go`
- `src/net/dnsclient_unix.go`
- `src/net/dnsclient_unix_test.go`
- `src/net/lookup.go`
- `src/net/lookup_plan9.go`
- `src/net/lookup_unix.go`
- `src/net/lookup_windows.go`

**Predicted Files (4):**
- ❌ `src/net.go`
- ✅ `src/net/lookup.go`
- ✅ `src/net/lookup_unix.go`
- ✅ `src/net/lookup_windows.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 23.1% | 37.5% | 3/13 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #29770**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/html/template`
- `src/text/template`
- `src/text/template/parse`

**Predicted Directories (2):**
- ✅ `src/html/template`
- ✅ `src/text/template/parse`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/html/template/exec_test.go`
- `src/text/template/exec_test.go`
- `src/text/template/parse/lex.go`
- `src/text/template/parse/parse.go`

**Predicted Files (6):**
- ❌ `src/html/template/template.go`
- ❌ `src/html/template/template_test.go`
- ✅ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/lex_test.go`
- ✅ `src/text/template/parse/parse.go`
- ❌ `src/text/template/parse/parse_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/html/template`
- `src/text/template/parse`


### 📊 **Proposal #51566**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/io`
- `src/net/http`

**Predicted Directories (4):**
- ❌ `src/bytes`
- ✅ `src/io`
- ❌ `src/runtime/pprof`
- ❌ `src/runtime/pprof/testdata/mappingtest`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 66.7% | 33.3% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/io/io.go`
- `src/io/io_test.go`
- `src/net/http/transfer.go`

**Predicted Files (9):**
- ❌ `src/bytes/bytes.go`
- ❌ `src/bytes/bytes_test.go`
- ❌ `src/bytes/reader.go`
- ❌ `src/bytes/reader_test.go`
- ✅ `src/io/io.go`
- ✅ `src/io/io_test.go`
- ❌ `src/runtime/pprof/pprof.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/testdata/mappingtest/main.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io`


### 📊 **Proposal #37196**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 20.0% | 20.0% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/compile/internal/ssagen`
- `src/cmd/compile/internal/typecheck/_builtin`
- `src/cmd/compile/internal/walk`
- `src/runtime`
- `src/time`

**Predicted Directories (5):**
- ❌ `internal/runtime/sys`
- ❌ `lib`
- ❌ `src`
- ✅ `src/time`
- ❌ `time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 14.3% | 12.5% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/compile/internal/ssagen/ssa.go`
- `src/cmd/compile/internal/typecheck/_builtin/runtime.go`
- `src/cmd/compile/internal/walk/builtin.go`
- `src/runtime/chan.go`
- `src/runtime/time.go`
- `src/time/sleep.go`
- `src/time/tick_test.go`

**Predicted Files (9):**
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `lib/time/`
- ❌ `src/time.go`
- ✅ `src/time/sleep.go`
- ❌ `src/time/tick.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`
- ❌ `src/time_test.go`
- ❌ `time/sleep.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 14.3% | 18.2% | 1/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #38079**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (2):**
- ✅ `src/net/http/httputil`
- ❌ `test/fixedbugs`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/httputil/reverseproxy.go`
- `src/net/http/httputil/reverseproxy_test.go`

**Predicted Files (3):**
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`
- ❌ `test/fixedbugs/issue38079.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http/httputil`


### 📊 **Proposal #51682**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/types2`
- `src/go/types`

**Predicted Directories (6):**
- ❌ `src/go/internal`
- ✅ `src/go/types`
- ❌ `src/go/types/objectpath`
- ❌ `src/go/types/typeutil`
- ❌ `src/types`
- ❌ `src/types/errors`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 4.0% | 12.5% | 6.1% | 1/8 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (8):**
- `src/cmd/compile/internal/types2/api_test.go`
- `src/cmd/compile/internal/types2/object.go`
- `src/cmd/compile/internal/types2/sizeof_test.go`
- `src/cmd/compile/internal/types2/subst.go`
- `src/go/types/api_test.go`
- `src/go/types/object.go`
- `src/go/types/sizeof_test.go`
- `src/go/types/subst.go`

**Predicted Files (25):**
- ❌ `src/go/internal/gotypes.go`
- ❌ `src/go/internal/gotypes_test.go`
- ❌ `src/go/types/alias.go`
- ❌ `src/go/types/api.go`
- ❌ `src/go/types/api_predicates.go`
- ❌ `src/go/types/builtins.go`
- ❌ `src/go/types/decl.go`
- ❌ `src/go/types/errors.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/func.go`
- ❌ `src/go/types/gotype.go`
- ❌ `src/go/types/interface.go`
- ❌ `src/go/types/named.go`
- ✅ `src/go/types/object.go`
- ❌ `src/go/types/objectpath/objectpath.go`
- ❌ `src/go/types/scope.go`
- ❌ `src/go/types/signature.go`
- ❌ `src/go/types/type.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/go/types/typeutil/map.go`
- ❌ `src/go/types/var.go`
- ❌ `src/types/errors/codes.go`
- ❌ `src/types/errors/codes_test.go`
- ❌ `src/types/object.go`
- ❌ `src/types/types.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.9% | 12.5% | 8.0% | 1/8 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/types`


### 📊 **Proposal #39214**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 12.5% | 10.0% | 1/8 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (8):**
- `src/cmd/compile/internal/gc`
- `src/cmd/compile/internal/types`
- `src/cmd/internal/obj`
- `src/cmd/internal/obj/x86`
- `src/internal/cpu`
- `src/strconv`
- `src/strings`
- `src/testing`

**Predicted Directories (12):**
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16317.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/internal/cpu`
- ✅ `src/internal/cpu`
- ❌ `src/runtime`
- ❌ `src/runtime/cgo`
- ❌ `src/runtime/debug`
- ❌ `src/sys`
- ❌ `src/sys/cpu`
- ❌ `src/syscall`
- ❌ `src/sysinfo`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 1.9% | 8.3% | 3.1% | 1/12 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (12):**
- `src/cmd/compile/internal/gc/main.go`
- `src/cmd/compile/internal/types/pkg.go`
- `src/cmd/internal/obj/sym.go`
- `src/cmd/internal/obj/x86/obj6.go`
- `src/internal/cpu/cpu_no_name.go`
- `src/internal/cpu/cpu_x86.go`
- `src/strconv/atof.go`
- `src/strconv/atof_test.go`
- `src/strconv/internal_test.go`
- `src/strings/strings.go`
- `src/strings/strings_test.go`
- `src/testing/benchmark.go`

**Predicted Files (52):**
- ❌ `src/fixedbugs/issue16133.dir/a.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16133.dir/main.go`
- ❌ `src/fixedbugs/issue16317.dir/a.go`
- ❌ `src/fixedbugs/issue16317.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/go/internal/cpu/cpu.go`
- ❌ `src/internal/cpu/cpu.go`
- ❌ `src/internal/cpu/cpu_arm.go`
- ❌ `src/internal/cpu/cpu_arm64.go`
- ❌ `src/internal/cpu/cpu_loong64.go`
- ❌ `src/internal/cpu/cpu_mips.go`
- ❌ `src/internal/cpu/cpu_ppc64x.go`
- ❌ `src/internal/cpu/cpu_riscv64.go`
- ❌ `src/internal/cpu/cpu_s390x.go`
- ✅ `src/internal/cpu/cpu_x86.go`
- ❌ `src/internal/cpu/cpu_x86_64.go`
- ❌ `src/runtime/cgo/cgo.go`
- ❌ `src/runtime/cpuflags.go`
- ❌ `src/runtime/cpuflags_amd64.go`
- ❌ `src/runtime/cpuflags_arm64.go`
- ❌ `src/runtime/debug/example_monitor_test.go`
- ❌ `src/runtime/defs_linux.go`
- ❌ `src/runtime/defs_linux_amd64.go`
- ❌ `src/runtime/defs_linux_arm.go`
- ❌ `src/runtime/defs_linux_arm64.go`
- ❌ `src/runtime/defs_linux_ppc64.go`
- ❌ `src/runtime/defs_linux_ppc64le.go`
- ❌ `src/runtime/defs_linux_riscv64.go`
- ❌ `src/runtime/defs_linux_s390x.go`
- ❌ `src/runtime/os_linux.go`
- ❌ `src/runtime/os_linux_arm.go`
- ❌ `src/runtime/os_linux_arm64.go`
- ❌ `src/runtime/os_linux_ppc64x.go`
- ❌ `src/runtime/os_linux_riscv64.go`
- ❌ `src/runtime/os_linux_x86.go`
- ❌ `src/sys/cpu/cpu_linux.go`
- ❌ `src/sys/cpu/proc_cpuinfo_linux.go`
- ❌ `src/sys/cpu/runtime_auxv.go`
- ❌ `src/sys/syscall_linux.go`
- ❌ `src/syscall/syscall_linux.go`
- ❌ `src/syscall/syscall_linux_amd64.go`
- ❌ `src/syscall/syscall_linux_arm.go`
- ❌ `src/syscall/syscall_linux_arm64.go`
- ❌ `src/syscall/syscall_linux_ppc64x.go`
- ❌ `src/syscall/syscall_linux_riscv64.go`
- ❌ `src/syscall/syscall_linux_s390x.go`
- ❌ `src/sysinfo/cpuinfo_bsd.go`
- ❌ `src/sysinfo/cpuinfo_linux.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 8.3% | 9.1% | 1/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/internal/cpu`


### 📊 **Proposal #30715**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/request.go`
- `src/net/http/serve_test.go`

**Predicted Files (2):**
- ✅ `src/net/http/request.go`
- ❌ `src/net/http/request_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http`


### 📊 **Proposal #51972**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/sync`

**Predicted Directories (3):**
- ❌ `src/issue16133.dir`
- ❌ `src/issue16616.dir`
- ✅ `src/sync`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 13.3% | 66.7% | 22.2% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/sync/map.go`
- `src/sync/map_reference_test.go`
- `src/sync/map_test.go`

**Predicted Files (15):**
- ❌ `map.go`
- ❌ `maps.go`
- ❌ `src/issue16133.dir/a1.go`
- ❌ `src/issue16133.dir/a2.go`
- ❌ `src/issue16133.dir/b.go`
- ❌ `src/issue16133.dir/c.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/sync/export_test.go`
- ❌ `src/sync/hashtriemap.go`
- ❌ `src/sync/hashtriemap_test.go`
- ✅ `src/sync/map.go`
- ✅ `src/sync/map_test.go`
- ❌ `src/sync/mutex.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 66.7% | 44.4% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/sync`


### 📊 **Proposal #50859**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/sync`

**Predicted Directories (14):**
- ❌ `internal/runtime/sys`
- ❌ `src/compile/internal/abi`
- ❌ `src/compile/internal/ir`
- ❌ `src/compile/internal/ssa`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16317.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ❌ `src/go/internal/obj`
- ❌ `src/runtime`
- ❌ `src/runtime/atomic`
- ❌ `src/runtime/race`
- ❌ `src/runtime/sync`
- ❌ `src/runtime/sync/atomic`
- ❌ `src/sync/atomic`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/sync/cond.go`

**Predicted Files (32):**
- ❌ `escape_sync_atomic.go`
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `intrinsic_atomic.go`
- ❌ `src/compile/internal/abi/abiutils.go`
- ❌ `src/compile/internal/abi/abiutils_test.go`
- ❌ `src/compile/internal/ir/ir.go`
- ❌ `src/compile/internal/ir/ir_test.go`
- ❌ `src/compile/internal/ssa/ssa.go`
- ❌ `src/compile/internal/ssa/ssa_test.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16317.dir/a.go`
- ❌ `src/fixedbugs/issue16317.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/go/internal/obj/obj.go`
- ❌ `src/go/internal/obj/obj_test.go`
- ❌ `src/runtime/atomic/atomic.go`
- ❌ `src/runtime/atomic/doc.go`
- ❌ `src/runtime/race/race.go`
- ❌ `src/runtime/race/race_test.go`
- ❌ `src/runtime/runtime.go`
- ❌ `src/runtime/runtime_test.go`
- ❌ `src/runtime/sync/atomic.go`
- ❌ `src/runtime/sync/atomic/atomic_test.go`
- ❌ `src/runtime/sync/atomic/doc.go`
- ❌ `src/runtime/sync/atomic/type.go`
- ❌ `src/runtime/sync/atomic/value.go`
- ❌ `src/runtime/sync/doc.go`
- ❌ `src/sync/atomic/atomic.go`
- ❌ `src/sync/atomic/atomic_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #32406**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/tls`
- `src/net/http`

**Predicted Directories (3):**
- ✅ `src/crypto/tls`
- ✅ `src/net/http`
- ❌ `src/testtls`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 25.0% | 31.6% | 3/12 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (12):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/conn.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_client_test.go`
- `src/crypto/tls/handshake_client_tls13.go`
- `src/crypto/tls/handshake_server.go`
- `src/crypto/tls/handshake_server_test.go`
- `src/crypto/tls/handshake_server_tls13.go`
- `src/crypto/tls/tls.go`
- `src/net/http/server.go`
- `src/net/http/transport.go`
- `src/net/http/transport_test.go`

**Predicted Files (7):**
- ✅ `src/crypto/tls/conn.go`
- ✅ `src/crypto/tls/tls.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ✅ `src/net/http/server.go`
- ❌ `src/testtls/tls.go`
- ❌ `src/testtls/tls_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 25.0% | 35.3% | 3/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/crypto/tls`
- `src/net/http`


### 📊 **Proposal #35044**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (3):**
- ✅ `src/crypto/x509`
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/crypto/x509/cert_pool.go`

**Predicted Files (7):**
- ✅ `src/crypto/x509/cert_pool.go`
- ❌ `src/crypto/x509/cert_pool_test.go`
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #45899**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (2):**
- ✅ `src/io`
- ❌ `src/io/fs`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/io/io.go`
- `src/io/io_test.go`

**Predicted Files (2):**
- ❌ `src/io/fs/fs.go`
- ✅ `src/io/io.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io`


### 📊 **Proposal #33232**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/89 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (89):**
- `src/archive/tar`
- `src/builtin`
- `src/bytes`
- `src/cmd/asm`
- `src/cmd/asm/internal/asm`
- `src/cmd/cgo`
- `src/cmd/compile/internal/base`
- `src/cmd/compile/internal/importer/testdata`
- `src/cmd/compile/internal/ir`
- `src/cmd/compile/internal/ssa`
- `src/cmd/compile/internal/ssagen`
- `src/cmd/compile/internal/syntax`
- `src/cmd/compile/internal/test`
- `src/cmd/compile/internal/test/testdata`
- `src/cmd/compile/internal/types`
- `src/cmd/compile/internal/types2`
- `src/cmd/cover/testdata`
- `src/cmd/doc`
- `src/cmd/fix`
- `src/cmd/go`
- `src/cmd/go/internal/cmdflag`
- `src/cmd/go/internal/list`
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modfetch/codehost`
- `src/cmd/go/internal/modget`
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/mvs`
- `src/cmd/go/internal/vcs`
- `src/cmd/go/internal/work`
- `src/cmd/internal/buildid`
- `src/cmd/internal/obj`
- `src/cmd/internal/test2json`
- `src/cmd/link/internal/ld/testdata/deadcode`
- `src/cmd/link/internal/loadelf`
- `src/cmd/link/internal/loadmacho`
- `src/cmd/link/internal/loadxcoff`
- `src/cmd/pack`
- `src/container/list`
- `src/container/ring`
- `src/crypto/tls`
- `src/crypto/x509`
- `src/database/sql`
- `src/debug/dwarf`
- `src/debug/pe`
- `src/embed/internal/embedtest`
- `src/encoding/asn1`
- `src/encoding/binary`
- `src/encoding/gob`
- `src/encoding/json`
- `src/encoding/xml`
- `src/errors`
- `src/expvar`
- `src/fmt`
- `src/go/ast`
- `src/go/doc/testdata`
- `src/go/internal/gcimporter/testdata`
- `src/go/token`
- `src/go/types`
- `src/html/template`
- `src/internal/fmtsort`
- `src/internal/reflectlite`
- `src/internal/singleflight`
- `src/math/big`
- `src/math/bits`
- `src/math/rand`
- `src/mime/quotedprintable`
- `src/net`
- `src/net/http`
- `src/net/http/httptrace`
- `src/net/rpc`
- `src/net/rpc/jsonrpc`
- `src/net/url`
- `src/os/user`
- `src/plugin`
- `src/reflect`
- `src/runtime`
- `src/runtime/cgo`
- `src/runtime/pprof`
- `src/runtime/race`
- `src/runtime/race/testdata`
- `src/strings`
- `src/sync`
- `src/sync/atomic`
- `src/syscall`
- `src/syscall/js`
- `src/testing`
- `src/testing/quick`
- `src/text/template`

**Predicted Directories (2):**
- ❌ `src/encoding/json/v2`
- ❌ `src/types`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/189 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (189):**
- `src/archive/tar/reader_test.go`
- `src/archive/tar/writer_test.go`
- `src/builtin/builtin.go`
- `src/bytes/reader_test.go`
- `src/cmd/asm/internal/asm/endtoend_test.go`
- `src/cmd/asm/internal/asm/parse.go`
- `src/cmd/asm/main.go`
- `src/cmd/cgo/gcc.go`
- `src/cmd/cgo/out.go`
- `src/cmd/compile/internal/base/timings.go`
- `src/cmd/compile/internal/importer/testdata/exports.go`
- `src/cmd/compile/internal/ir/sizeof_test.go`
- `src/cmd/compile/internal/ssa/copyelim_test.go`
- `src/cmd/compile/internal/ssa/sizeof_test.go`
- `src/cmd/compile/internal/ssagen/ssa.go`
- `src/cmd/compile/internal/syntax/printer.go`
- `src/cmd/compile/internal/test/iface_test.go`
- `src/cmd/compile/internal/test/shift_test.go`
- `src/cmd/compile/internal/test/testdata/compound_test.go`
- `src/cmd/compile/internal/types/sizeof_test.go`
- `src/cmd/compile/internal/types2/expr.go`
- `src/cmd/compile/internal/types2/sizeof_test.go`
- `src/cmd/compile/internal/types2/subst.go`
- `src/cmd/cover/testdata/test.go`
- `src/cmd/doc/pkg.go`
- `src/cmd/fix/cftype.go`
- `src/cmd/fix/fix.go`
- `src/cmd/fix/gotypes.go`
- `src/cmd/fix/netipv6zone.go`
- `src/cmd/fix/printerconfig.go`
- `src/cmd/fix/typecheck.go`
- `src/cmd/go/internal/cmdflag/flag.go`
- `src/cmd/go/internal/list/list.go`
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/modfetch/cache.go`
- `src/cmd/go/internal/modfetch/codehost/git.go`
- `src/cmd/go/internal/modfetch/codehost/vcs.go`
- `src/cmd/go/internal/modfetch/coderepo.go`
- `src/cmd/go/internal/modfetch/fetch.go`
- `src/cmd/go/internal/modfetch/repo.go`
- `src/cmd/go/internal/modget/get.go`
- `src/cmd/go/internal/modload/buildlist.go`
- `src/cmd/go/internal/modload/import.go`
- `src/cmd/go/internal/modload/load.go`
- `src/cmd/go/internal/modload/modfile.go`
- `src/cmd/go/internal/modload/vendor.go`
- `src/cmd/go/internal/mvs/mvs.go`
- `src/cmd/go/internal/vcs/vcs.go`
- `src/cmd/go/internal/work/build_test.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/go/internal/work/gc.go`
- `src/cmd/go/proxy_test.go`
- `src/cmd/internal/buildid/buildid_test.go`
- `src/cmd/internal/obj/link.go`
- `src/cmd/internal/obj/pcln.go`
- `src/cmd/internal/obj/sizeof_test.go`
- `src/cmd/internal/test2json/test2json_test.go`
- `src/cmd/link/internal/ld/testdata/deadcode/reflectcall.go`
- `src/cmd/link/internal/loadelf/ldelf.go`
- `src/cmd/link/internal/loadmacho/ldmacho.go`
- `src/cmd/link/internal/loadxcoff/ldxcoff.go`
- `src/cmd/pack/pack_test.go`
- `src/container/list/list_test.go`
- `src/container/ring/example_test.go`
- `src/container/ring/ring_test.go`
- `src/crypto/tls/generate_cert.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_client_test.go`
- `src/crypto/tls/handshake_server.go`
- `src/crypto/tls/handshake_server_test.go`
- `src/crypto/x509/name_constraints_test.go`
- `src/crypto/x509/verify.go`
- `src/crypto/x509/x509_test.go`
- `src/database/sql/convert.go`
- `src/database/sql/convert_test.go`
- `src/database/sql/fakedb_test.go`
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`
- `src/debug/dwarf/entry.go`
- `src/debug/dwarf/entry_test.go`
- `src/debug/pe/file.go`
- `src/embed/internal/embedtest/embed_test.go`
- `src/encoding/asn1/asn1.go`
- `src/encoding/asn1/asn1_test.go`
- `src/encoding/asn1/marshal_test.go`
- `src/encoding/binary/binary_test.go`
- `src/encoding/binary/example_test.go`
- `src/encoding/gob/codec_test.go`
- `src/encoding/gob/encoder_test.go`
- `src/encoding/gob/timing_test.go`
- `src/encoding/gob/type_test.go`
- `src/encoding/json/bench_test.go`
- `src/encoding/json/decode.go`
- `src/encoding/json/decode_test.go`
- `src/encoding/json/encode.go`
- `src/encoding/json/encode_test.go`
- `src/encoding/json/example_test.go`
- `src/encoding/json/scanner_test.go`
- `src/encoding/json/stream.go`
- `src/encoding/json/stream_test.go`
- `src/encoding/json/tagkey_test.go`
- `src/encoding/xml/marshal_test.go`
- `src/errors/wrap.go`
- `src/errors/wrap_test.go`
- `src/expvar/expvar.go`
- `src/expvar/expvar_test.go`
- `src/fmt/fmt_test.go`
- `src/fmt/scan_test.go`
- `src/go/ast/print.go`
- `src/go/doc/testdata/benchmark.go`
- `src/go/doc/testdata/testing.go`
- `src/go/internal/gcimporter/testdata/exports.go`
- `src/go/token/serialize_test.go`
- `src/go/types/expr.go`
- `src/go/types/sizeof_test.go`
- `src/go/types/subst.go`
- `src/html/template/content_test.go`
- `src/html/template/escape_test.go`
- `src/html/template/example_test.go`
- `src/html/template/exec_test.go`
- `src/html/template/js.go`
- `src/html/template/js_test.go`
- `src/html/template/url_test.go`
- `src/internal/fmtsort/sort_test.go`
- `src/internal/reflectlite/all_test.go`
- `src/internal/reflectlite/value.go`
- `src/internal/singleflight/singleflight_test.go`
- `src/math/big/floatconv_test.go`
- `src/math/bits/make_examples.go`
- `src/math/rand/example_test.go`
- `src/math/rand/regress_test.go`
- `src/mime/quotedprintable/reader_test.go`
- `src/net/http/clientserver_test.go`
- `src/net/http/h2_bundle.go`
- `src/net/http/httptrace/trace.go`
- `src/net/http/response_test.go`
- `src/net/http/roundtrip_js.go`
- `src/net/http/serve_test.go`
- `src/net/http/server.go`
- `src/net/http/transport.go`
- `src/net/http/transport_test.go`
- `src/net/lookup.go`
- `src/net/lookup_test.go`
- `src/net/rpc/debug.go`
- `src/net/rpc/jsonrpc/server.go`
- `src/net/url/url_test.go`
- `src/os/user/lookup_unix.go`
- `src/plugin/plugin_dlopen.go`
- `src/reflect/abi_test.go`
- `src/reflect/all_test.go`
- `src/reflect/example_test.go`
- `src/reflect/export_test.go`
- `src/reflect/set_test.go`
- `src/reflect/type.go`
- `src/reflect/value.go`
- `src/runtime/abi_test.go`
- `src/runtime/cgo/handle_test.go`
- `src/runtime/chan_test.go`
- `src/runtime/debugcall.go`
- `src/runtime/gcinfo_test.go`
- `src/runtime/iface_test.go`
- `src/runtime/malloc_test.go`
- `src/runtime/map_benchmark_test.go`
- `src/runtime/map_test.go`
- `src/runtime/mfinal_test.go`
- `src/runtime/mgcscavenge.go`
- `src/runtime/os_windows.go`
- `src/runtime/plugin.go`
- `src/runtime/pprof/pprof.go`
- `src/runtime/race/race_test.go`
- `src/runtime/race/testdata/issue12664_test.go`
- `src/runtime/race/testdata/mop_test.go`
- `src/runtime/race/testdata/pool_test.go`
- `src/runtime/sizeof_test.go`
- `src/strings/reader_test.go`
- `src/sync/atomic/value.go`
- `src/sync/atomic/value_test.go`
- `src/sync/map.go`
- `src/sync/map_reference_test.go`
- `src/sync/map_test.go`
- `src/sync/pool_test.go`
- `src/sync/poolqueue.go`
- `src/syscall/fs_js.go`
- `src/syscall/js/js.go`
- `src/syscall/js/js_test.go`
- `src/syscall/syscall_windows.go`
- `src/testing/quick/quick.go`
- `src/testing/testing.go`
- `src/text/template/exec_test.go`

**Predicted Files (2):**
- ❌ `src/encoding/json/v2/arshal_any.go`
- ❌ `src/types/interface.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/189 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #47658**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/reflect`

**Predicted Directories (5):**
- ❌ `src/fixedbugs/issue16133.dir`
- ❌ `src/fixedbugs/issue16616.dir`
- ✅ `src/reflect`
- ❌ `src/reflectlite`
- ❌ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 33.3% | 13.3% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (12):**
- ❌ `src/fixedbugs/issue16133.dir/a1.go`
- ❌ `src/fixedbugs/issue16133.dir/a2.go`
- ❌ `src/fixedbugs/issue16133.dir/b.go`
- ❌ `src/fixedbugs/issue16133.dir/c.go`
- ❌ `src/fixedbugs/issue16616.dir/a.go`
- ❌ `src/fixedbugs/issue16616.dir/b.go`
- ❌ `src/fixedbugs/issue16616.dir/issue16616.go`
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/value.go`
- ❌ `src/reflectlite/type.go`
- ❌ `src/reflectlite/value.go`
- ❌ `src/runtime/reflect_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #47609**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/unicode/utf8`

**Predicted Directories (3):**
- ❌ `src/issue16616.dir`
- ❌ `src/unicode`
- ✅ `src/unicode/utf8`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 66.7% | 36.4% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/unicode/utf8/utf8.go`
- `src/unicode/utf8/utf8_test.go`

**Predicted Files (8):**
- ❌ `append.go`
- ❌ `src/issue16616.dir/a.go`
- ❌ `src/issue16616.dir/b.go`
- ❌ `src/issue16616.dir/issue16616.go`
- ❌ `src/unicode/utf8.go`
- ✅ `src/unicode/utf8/utf8.go`
- ✅ `src/unicode/utf8/utf8_test.go`
- ❌ `utf.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/unicode/utf8`


### 📊 **Proposal #38776**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 36.8% | 87.5% | 51.9% | 7/8 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (8):**
- `src/crypto/internal/boring`
- `src/crypto/md5`
- `src/crypto/sha1`
- `src/crypto/sha256`
- `src/crypto/sha512`
- `src/hash/crc32`
- `src/hash/crc64`
- `src/hash/fnv`

**Predicted Directories (19):**
- ❌ `src/crypto/adler32`
- ❌ `src/crypto/crc32`
- ❌ `src/crypto/crc64`
- ❌ `src/crypto/fnv`
- ❌ `src/crypto/hmac`
- ✅ `src/crypto/md5`
- ❌ `src/crypto/rand`
- ❌ `src/crypto/rsa`
- ✅ `src/crypto/sha1`
- ✅ `src/crypto/sha256`
- ❌ `src/crypto/sha3`
- ✅ `src/crypto/sha512`
- ❌ `src/go/internal/hash`
- ❌ `src/hash/adler32`
- ✅ `src/hash/crc32`
- ✅ `src/hash/crc64`
- ✅ `src/hash/fnv`
- ❌ `src/hash/maphash`
- ❌ `src/testhash`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.1% | 41.7% | 23.3% | 5/12 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (12):**
- `src/crypto/internal/boring/sha.go`
- `src/crypto/md5/md5_test.go`
- `src/crypto/sha1/sha1.go`
- `src/crypto/sha1/sha1_test.go`
- `src/crypto/sha1/sha1block_amd64.go`
- `src/crypto/sha1/sha1block_arm64.go`
- `src/crypto/sha1/sha1block_decl.go`
- `src/crypto/sha256/sha256_test.go`
- `src/crypto/sha512/sha512_test.go`
- `src/hash/crc32/crc32_test.go`
- `src/hash/crc64/crc64_test.go`
- `src/hash/fnv/fnv_test.go`

**Predicted Files (31):**
- ❌ `src/crypto/adler32/adler32.go`
- ❌ `src/crypto/adler32/adler32_test.go`
- ❌ `src/crypto/crc32/crc32.go`
- ❌ `src/crypto/crc32/crc32_test.go`
- ❌ `src/crypto/crc64/crc64.go`
- ❌ `src/crypto/crc64/crc64_test.go`
- ❌ `src/crypto/fnv/fnv.go`
- ❌ `src/crypto/fnv/fnv_test.go`
- ❌ `src/crypto/hmac/hmac.go`
- ❌ `src/crypto/hmac/hmac_test.go`
- ❌ `src/crypto/md5/md5.go`
- ✅ `src/crypto/md5/md5_test.go`
- ❌ `src/crypto/rand/rand.go`
- ❌ `src/crypto/rand/rand_test.go`
- ❌ `src/crypto/rsa/rsa.go`
- ❌ `src/crypto/rsa/rsa_test.go`
- ✅ `src/crypto/sha1/sha1.go`
- ✅ `src/crypto/sha1/sha1_test.go`
- ❌ `src/crypto/sha256/sha256.go`
- ✅ `src/crypto/sha256/sha256_test.go`
- ❌ `src/crypto/sha3/sha3.go`
- ❌ `src/crypto/sha3/sha3_test.go`
- ❌ `src/crypto/sha512/sha512.go`
- ✅ `src/crypto/sha512/sha512_test.go`
- ❌ `src/go/internal/hash/hash.go`
- ❌ `src/hash/adler32/adler32.go`
- ❌ `src/hash/crc32/crc32.go`
- ❌ `src/hash/crc64/crc64.go`
- ❌ `src/hash/fnv/fnv.go`
- ❌ `src/hash/maphash/maphash.go`
- ❌ `src/testhash/hash.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 45.5% | 41.7% | 43.5% | 5/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (7):**
- `src/crypto/md5`
- `src/crypto/sha1`
- `src/crypto/sha256`
- `src/crypto/sha512`
- `src/hash/crc32`
- `src/hash/crc64`
- `src/hash/fnv`
