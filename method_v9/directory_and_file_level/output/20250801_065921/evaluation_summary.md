# LLM Directory and File Level Evaluation Summary

## Directory Level Macro Metrics

- **Number of Processed Proposals**: 231
- **Number of Proposals with at least one correct directory (precision > 0)**: 207
- **Macro Precision**: 0.712
- **Macro Recall**: 0.650
- **Macro F1**: 0.622

## File Level Macro Metrics

- **Number of Processed Proposals**: 231
- **Number of Proposals with at least one correct file (precision > 0)**: 193
- **Macro Precision**: 0.465
- **Macro Recall**: 0.481
- **Macro F1**: 0.413

## File Level within Correct Directories Macro Metrics

- **Number of Processed Proposals**: 231
- **Number of Proposals with at least one correct file (precision > 0)**: 193
- **Macro Precision**: 0.559
- **Macro Recall**: 0.481
- **Macro F1**: 0.458


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
| 50.0% | 50.0% | 50.0% | 3/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/crypto/tls/handshake_server_test.go`
- `src/crypto/tls/handshake_server_tls13.go`
- `src/crypto/tls/handshake_test.go`

**Predicted Files (6):**
- ✅ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/defaults.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/tls.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 3/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #48801**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat`
- `src/cmd/vet`

**Predicted Directories (2):**
- ✅ `src/cmd/vet`
- ❌ `src/cmd/vet/testdata/timeformat`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`
- `src/cmd/vet/main.go`

**Predicted Files (4):**
- ❌ `src/cmd/vet/testdata/timeformat/doc.go`
- ❌ `src/cmd/vet/testdata/timeformat/timeformat.go`
- ❌ `src/cmd/vet/vet.go`
- ❌ `src/cmd/vet/vetflag.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/vet`


### 📊 **Proposal #34875**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/doc`

**Predicted Directories (2):**
- ❌ `src/cmd/doc`
- ❌ `src/go/doc/comment`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/go/doc/comment.go`

**Predicted Files (6):**
- ❌ `src/cmd/doc/doc.go`
- ❌ `src/cmd/doc/pkg.go`
- ❌ `src/go/doc/comment/doc.go`
- ❌ `src/go/doc/comment/markdown.go`
- ❌ `src/go/doc/comment/parse.go`
- ❌ `src/go/doc/comment/text.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


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

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 77.8% | 63.6% | 70.0% | 7/11 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #51777**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/netip`

**Predicted Directories (1):**
- ✅ `src/net/netip`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/netip/netip_test.go`

**Predicted Files (2):**
- ❌ `src/net/netip/netip.go`
- ✅ `src/net/netip/netip_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/hash/maphash`

**Predicted Directories (1):**
- ✅ `src/hash/maphash`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/hash/maphash/maphash.go`
- `src/hash/maphash/maphash_test.go`

**Predicted Files (4):**
- ❌ `src/hash/maphash/example_test.go`
- ✅ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_test.go`
- ❌ `src/hash/maphash/smhasher_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/hash/maphash`


### 📊 **Proposal #46259**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (7):**
- ❌ `src/cmd/internal/sys`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/internal/syscall/execenv`
- ❌ `src/internal/syscall/unix`
- ❌ `src/os/exec`
- ✅ `src/syscall`
- ❌ `src/vendor/golang.org/x/sys/unix`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 1.2% | 50.0% | 2.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/syscall/exec_freebsd.go`
- `src/syscall/exec_freebsd_test.go`

**Predicted Files (86):**
- ❌ `src/cmd/internal/sys/arch.go`
- ❌ `src/cmd/internal/sys/arch_test.go`
- ❌ `src/cmd/internal/sys/args.go`
- ❌ `src/cmd/link/internal/ld/outbuf_freebsd.go`
- ❌ `src/cmd/link/internal/ld/outbuf_test.go`
- ❌ `src/internal/syscall/execenv/execenv_default.go`
- ❌ `src/internal/syscall/execenv/execenv_windows.go`
- ❌ `src/internal/syscall/unix/at_sysnum_freebsd.go`
- ❌ `src/internal/syscall/unix/at_sysnum_linux.go`
- ❌ `src/internal/syscall/unix/at_sysnum_netbsd.go`
- ❌ `src/internal/syscall/unix/at_sysnum_openbsd.go`
- ❌ `src/internal/syscall/unix/at_sysnum_solaris.go`
- ❌ `src/internal/syscall/unix/at_sysnum_wasip1.go`
- ❌ `src/internal/syscall/unix/at_sysnum_windows.go`
- ❌ `src/internal/syscall/unix/constants.go`
- ❌ `src/internal/syscall/unix/faccessat_bsd.go`
- ❌ `src/internal/syscall/unix/faccessat_darwin.go`
- ❌ `src/internal/syscall/unix/faccessat_openbsd.go`
- ❌ `src/internal/syscall/unix/faccessat_solaris.go`
- ❌ `src/internal/syscall/unix/faccessat_syscall.go`
- ❌ `src/internal/syscall/unix/fcntl_js.go`
- ❌ `src/internal/syscall/unix/fcntl_unix.go`
- ❌ `src/internal/syscall/unix/fcntl_wasip1.go`
- ❌ `src/internal/syscall/unix/getrandom.go`
- ❌ `src/internal/syscall/unix/getrandom_dragonfly.go`
- ❌ `src/internal/syscall/unix/getrandom_freebsd.go`
- ❌ `src/internal/syscall/unix/getrandom_linux.go`
- ❌ `src/internal/syscall/unix/getrandom_linux_test.go`
- ❌ `src/internal/syscall/unix/getrandom_solaris.go`
- ❌ `src/internal/syscall/unix/ioctl_aix.go`
- ❌ `src/internal/syscall/unix/kernel_version_freebsd.go`
- ❌ `src/internal/syscall/unix/kernel_version_freebsd_test.go`
- ❌ `src/internal/syscall/unix/kernel_version_linux.go`
- ❌ `src/internal/syscall/unix/kernel_version_other.go`
- ❌ `src/internal/syscall/unix/kernel_version_solaris.go`
- ❌ `src/internal/syscall/unix/kernel_version_solaris_test.go`
- ❌ `src/internal/syscall/unix/net.go`
- ❌ `src/internal/syscall/unix/net_darwin.go`
- ❌ `src/internal/syscall/unix/net_js.go`
- ❌ `src/internal/syscall/unix/net_wasip1.go`
- ❌ `src/internal/syscall/unix/nofollow_bsd.go`
- ❌ `src/internal/syscall/unix/nofollow_netbsd.go`
- ❌ `src/internal/syscall/unix/nofollow_posix.go`
- ❌ `src/internal/syscall/unix/nonblocking_js.go`
- ❌ `src/internal/syscall/unix/nonblocking_unix.go`
- ❌ `src/internal/syscall/unix/nonblocking_wasip1.go`
- ❌ `src/internal/syscall/unix/pidfd_linux.go`
- ❌ `src/internal/syscall/unix/pty_darwin.go`
- ❌ `src/internal/syscall/unix/renameat2_sysnum_linux.go`
- ❌ `src/internal/syscall/unix/renameat_sysnum_linux.go`
- ❌ `src/internal/syscall/unix/siginfo_linux.go`
- ❌ `src/internal/syscall/unix/siginfo_linux_mipsx.go`
- ❌ `src/internal/syscall/unix/siginfo_linux_other.go`
- ❌ `src/internal/syscall/unix/siginfo_linux_test.go`
- ❌ `src/internal/syscall/unix/syscall.go`
- ❌ `src/internal/syscall/unix/sysnum_freebsd.go`
- ❌ `src/internal/syscall/unix/sysnum_linux_386.go`
- ❌ `src/internal/syscall/unix/sysnum_linux_amd64.go`
- ❌ `src/internal/syscall/unix/sysnum_linux_arm.go`
- ❌ `src/internal/syscall/unix/sysnum_linux_generic.go`
- ❌ `src/internal/syscall/unix/sysnum_linux_mips64x.go`
- ❌ `src/internal/syscall/unix/sysnum_linux_mipsx.go`
- ❌ `src/internal/syscall/unix/sysnum_linux_ppc64x.go`
- ❌ `src/internal/syscall/unix/sysnum_linux_s390x.go`
- ❌ `src/internal/syscall/unix/tcsetpgrp_bsd.go`
- ❌ `src/internal/syscall/unix/tcsetpgrp_linux.go`
- ❌ `src/internal/syscall/unix/user_darwin.go`
- ❌ `src/internal/syscall/unix/utimes.go`
- ❌ `src/internal/syscall/unix/utimes_wasip1.go`
- ❌ `src/internal/syscall/unix/waitid_linux.go`
- ❌ `src/os/exec/exec_unix.go`
- ❌ `src/os/exec/exec_unix_test.go`
- ❌ `src/syscall/exec_bsd.go`
- ✅ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/syscall_freebsd.go`
- ❌ `src/syscall/syscall_freebsd_386.go`
- ❌ `src/syscall/syscall_freebsd_amd64.go`
- ❌ `src/syscall/syscall_freebsd_arm.go`
- ❌ `src/syscall/syscall_freebsd_arm64.go`
- ❌ `src/syscall/syscall_freebsd_riscv64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/syscall_freebsd.go`
- ❌ `src/vendor/golang.org/x/sys/unix/syscall_freebsd_386.go`
- ❌ `src/vendor/golang.org/x/sys/unix/syscall_freebsd_amd64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/syscall_freebsd_arm.go`
- ❌ `src/vendor/golang.org/x/sys/unix/syscall_freebsd_arm64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/syscall_freebsd_riscv64.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 50.0% | 20.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall`


### 📊 **Proposal #47257**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 9.1% | 16.7% | 1/11 |

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

**Predicted Directories (1):**
- ✅ `src/cmd/dist`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 5.6% | 9.5% | 1/18 |

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

**Predicted Files (3):**
- ✅ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/build_test.go`
- ❌ `src/cmd/dist/main.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 5.6% | 9.5% | 1/18 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/dist`


### 📊 **Proposal #47216**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (1):**
- ❌ `src/runtime/metrics`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/runtime/metrics.go`
- `src/runtime/metrics_test.go`
- `src/runtime/mgc.go`
- `src/runtime/mgclimit.go`
- `src/runtime/mgcscavenge.go`
- `src/runtime/mheap.go`

**Predicted Files (3):**
- ❌ `src/runtime/metrics/description.go`
- ❌ `src/runtime/metrics/metrics.go`
- ❌ `src/runtime/metrics/metrics_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #53747**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (2):**
- ❌ `src/cmd/internal/objabi`
- ✅ `src/flag`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/flag/example_func_test.go`
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (4):**
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/archive/zip`

**Predicted Directories (1):**
- ✅ `src/archive/zip`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 100.0% | 44.4% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/archive/zip/writer.go`
- `src/archive/zip/writer_test.go`

**Predicted Files (7):**
- ❌ `src/archive/zip/reader.go`
- ❌ `src/archive/zip/reader_test.go`
- ❌ `src/archive/zip/register.go`
- ❌ `src/archive/zip/struct.go`
- ✅ `src/archive/zip/writer.go`
- ✅ `src/archive/zip/writer_test.go`
- ❌ `src/archive/zip/zip_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 100.0% | 44.4% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/archive/zip`


### 📊 **Proposal #34626**

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
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/benchmark.go`
- `src/testing/benchmark_test.go`

**Predicted Files (2):**
- ✅ `src/testing/benchmark.go`
- ✅ `src/testing/benchmark_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #48530**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (1):**
- ✅ `src/net`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 25.0% | 22.2% | 1/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/net/net.go`
- `src/net/tcpsock.go`
- `src/net/tcpsock_plan9.go`
- `src/net/tcpsock_posix.go`

**Predicted Files (5):**
- ❌ `src/net/splice_linux.go`
- ❌ `src/net/splice_linux_test.go`
- ❌ `src/net/splice_stub.go`
- ✅ `src/net/tcpsock.go`
- ❌ `src/net/tcpsock_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 25.0% | 22.2% | 1/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #50102**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/archive/tar`

**Predicted Directories (1):**
- ✅ `src/archive/tar`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/archive/tar/common.go`
- `src/archive/tar/stat_unix.go`
- `src/archive/tar/tar_test.go`

**Predicted Files (2):**
- ✅ `src/archive/tar/common.go`
- ✅ `src/archive/tar/stat_unix.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/go/internal/generate`

**Predicted Directories (1):**
- ✅ `src/cmd/go/internal/generate`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/cmd/go/internal/generate/generate.go`

**Predicted Files (2):**
- ✅ `src/cmd/go/internal/generate/generate.go`
- ❌ `src/cmd/go/internal/generate/generate_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/generate`


### 📊 **Proposal #50062**

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
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/time.go`
- `src/time/time_test.go`

**Predicted Files (3):**
- ✅ `src/time/time.go`
- ❌ `src/time/zoneinfo.go`
- ❌ `src/time/zoneinfo_read.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #46731**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 11.1% | 12.5% | 1/9 |

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

**Predicted Directories (7):**
- ❌ `src/cmd/cgo/internal/test`
- ❌ `src/cmd/cgo/internal/test/issue41761a`
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/internal/gccgoimporter/testdata`
- ❌ `src/internal/sys`
- ✅ `test/fixedbugs`
- ❌ `test/internal/runtime/sys`

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

**Predicted Files (16):**
- ❌ `src/cmd/cgo/internal/test/issue41761.go`
- ❌ `src/cmd/cgo/internal/test/issue41761a/a.go`
- ❌ `src/cmd/cgo/internal/test/test.go`
- ❌ `src/cmd/cgo/internal/test/test_unix.go`
- ❌ `src/cmd/cgo/internal/test/test_windows.go`
- ❌ `src/cmd/compile/internal/gc/compile.go`
- ❌ `src/cmd/compile/internal/gc/export.go`
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/gc/obj.go`
- ❌ `src/cmd/compile/internal/gc/util.go`
- ❌ `src/internal/gccgoimporter/testdata/notinheap.go`
- ❌ `src/internal/sys/nih.go`
- ❌ `test/fixedbugs/notinheap.go`
- ❌ `test/fixedbugs/notinheap2.go`
- ❌ `test/fixedbugs/notinheap3.go`
- ❌ `test/internal/runtime/sys/inlinegcpc.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/18 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `test/fixedbugs`


### 📊 **Proposal #33184**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/time`

**Predicted Directories (2):**
- ❌ `lib/time`
- ✅ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/time.go`
- `src/time/tick.go`
- `src/time/tick_test.go`

**Predicted Files (3):**
- ❌ `lib/time/mkzip.go`
- ✅ `src/time/tick.go`
- ✅ `src/time/tick_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #50489**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/math/big`

**Predicted Directories (1):**
- ✅ `src/math/big`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/math/big/ratconv.go`
- `src/math/big/ratconv_test.go`

**Predicted Files (6):**
- ❌ `src/math/big/rat.go`
- ❌ `src/math/big/rat_test.go`
- ✅ `src/math/big/ratconv.go`
- ✅ `src/math/big/ratconv_test.go`
- ❌ `src/math/big/ratmarsh.go`
- ❌ `src/math/big/ratmarsh_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/math/big`


### 📊 **Proposal #47342**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/dist`
- `src/hash/maphash`

**Predicted Directories (1):**
- ✅ `src/hash/maphash`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 75.0% | 75.0% | 3/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/cmd/dist/test.go`
- `src/hash/maphash/maphash.go`
- `src/hash/maphash/maphash_purego.go`
- `src/hash/maphash/maphash_runtime.go`

**Predicted Files (4):**
- ✅ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_purego.go`
- ✅ `src/hash/maphash/maphash_runtime.go`
- ❌ `src/hash/maphash/maphash_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 75.0% | 75.0% | 3/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/hash/maphash`


### 📊 **Proposal #37255**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os/signal`

**Predicted Directories (2):**
- ❌ `src/context`
- ✅ `src/os/signal`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 66.7% | 50.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/os/signal/example_unix_test.go`
- `src/os/signal/signal.go`
- `src/os/signal/signal_test.go`

**Predicted Files (5):**
- ❌ `src/context/context.go`
- ❌ `src/context/context_test.go`
- ❌ `src/os/signal/doc.go`
- ✅ `src/os/signal/signal.go`
- ✅ `src/os/signal/signal_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/os/signal`


### 📊 **Proposal #42502**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 33.3% | 33.3% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/runtime`
- `src/runtime/pprof`
- `src/runtime/testdata/testprogcgo`

**Predicted Directories (3):**
- ❌ `src/cmd/pprof`
- ❌ `src/net/http/pprof`
- ✅ `src/runtime/pprof`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 9.5% | 14.8% | 2/21 |

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

**Predicted Files (6):**
- ❌ `src/cmd/pprof/pprof.go`
- ❌ `src/cmd/pprof/pprof_test.go`
- ❌ `src/net/http/pprof/pprof.go`
- ❌ `src/net/http/pprof/pprof_test.go`
- ✅ `src/runtime/pprof/pprof.go`
- ✅ `src/runtime/pprof/pprof_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 9.5% | 17.4% | 2/21 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime/pprof`


### 📊 **Proposal #42782**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/visiblefields.go`
- `src/reflect/visiblefields_test.go`

**Predicted Files (3):**
- ❌ `src/reflect/type.go`
- ✅ `src/reflect/visiblefields.go`
- ✅ `src/reflect/visiblefields_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #38248**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 25.0% | 28.6% | 2/8 |

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

**Predicted Directories (6):**
- ❌ `cmd/compile/internal/wasm`
- ❌ `misc/wasm`
- ✅ `src/cmd/link/internal/wasm`
- ❌ `src/syscall`
- ✅ `src/syscall/js`
- ❌ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 20.0% | 16.7% | 2/10 |

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

**Predicted Files (14):**
- ❌ `cmd/compile/internal/wasm/ssa.go`
- ❌ `misc/wasm/wasm_exec.js`
- ✅ `src/cmd/link/internal/wasm/asm.go`
- ❌ `src/cmd/link/internal/wasm/obj.go`
- ❌ `src/syscall/fs_wasip1.go`
- ❌ `src/syscall/js/func.go`
- ❌ `src/syscall/js/js.go`
- ✅ `src/syscall/js/js_test.go`
- ❌ `src/syscall/net_wasip1.go`
- ❌ `src/syscall/os_wasip1.go`
- ❌ `src/syscall/syscall_js.go`
- ❌ `src/syscall/syscall_wasip1.go`
- ❌ `src/syscall/tables_wasip1.go`
- ❌ `src/time/zoneinfo_wasip1.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 20.0% | 26.7% | 2/10 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/link/internal/wasm`
- `src/syscall/js`


### 📊 **Proposal #46279**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/link/internal/ld`

**Predicted Directories (3):**
- ❌ `src/net`
- ❌ `src/syscall`
- ❌ `src/vendor/golang.org/x/sys/unix`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/link/internal/ld/ld_test.go`
- `src/cmd/link/internal/ld/lib.go`

**Predicted Files (12):**
- ❌ `src/net/fd_posix.go`
- ❌ `src/net/fd_posix_test.go`
- ❌ `src/net/fd_test.go`
- ❌ `src/net/fd_unix.go`
- ❌ `src/net/fd_unix_test.go`
- ❌ `src/net/rlimit_unix.go`
- ❌ `src/syscall/rlimit.go`
- ❌ `src/syscall/rlimit_darwin.go`
- ❌ `src/syscall/rlimit_stub.go`
- ❌ `src/syscall/rlimit_test.go`
- ❌ `src/vendor/golang.org/x/sys/unix/fdset.go`
- ❌ `src/vendor/golang.org/x/sys/unix/syscall.go`

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
| 44.4% | 8.9% | 14.8% | 4/45 |

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

**Predicted Directories (9):**
- ✅ `src/cmd/compile/internal/abi`
- ✅ `src/cmd/compile/internal/ssa`
- ✅ `src/cmd/compile/internal/ssagen`
- ✅ `src/cmd/internal/objabi`
- ❌ `src/cmd/link/internal/amd64`
- ❌ `src/cmd/link/internal/arm64`
- ❌ `src/cmd/link/internal/ppc64`
- ❌ `src/cmd/link/internal/riscv64`
- ❌ `src/cmd/link/internal/s390x`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 2.6% | 4.5% | 4/152 |

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

**Predicted Files (24):**
- ✅ `src/cmd/compile/internal/abi/abiutils.go`
- ✅ `src/cmd/compile/internal/ssa/expand_calls.go`
- ✅ `src/cmd/compile/internal/ssagen/abi.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ✅ `src/cmd/internal/objabi/funcid.go`
- ❌ `src/cmd/internal/objabi/symkind.go`
- ❌ `src/cmd/internal/objabi/symkind_string.go`
- ❌ `src/cmd/internal/objabi/util.go`
- ❌ `src/cmd/link/internal/amd64/asm.go`
- ❌ `src/cmd/link/internal/amd64/l.go`
- ❌ `src/cmd/link/internal/amd64/obj.go`
- ❌ `src/cmd/link/internal/arm64/asm.go`
- ❌ `src/cmd/link/internal/arm64/l.go`
- ❌ `src/cmd/link/internal/arm64/obj.go`
- ❌ `src/cmd/link/internal/ppc64/asm.go`
- ❌ `src/cmd/link/internal/ppc64/l.go`
- ❌ `src/cmd/link/internal/ppc64/obj.go`
- ❌ `src/cmd/link/internal/riscv64/asm.go`
- ❌ `src/cmd/link/internal/riscv64/l.go`
- ❌ `src/cmd/link/internal/riscv64/obj.go`
- ❌ `src/cmd/link/internal/s390x/asm.go`
- ❌ `src/cmd/link/internal/s390x/l.go`
- ❌ `src/cmd/link/internal/s390x/obj.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 44.4% | 2.6% | 5.0% | 4/152 |

##### Correct Directories Used for Evaluation

**Correct Directories (4):**
- `src/cmd/compile/internal/abi`
- `src/cmd/compile/internal/ssa`
- `src/cmd/compile/internal/ssagen`
- `src/cmd/internal/objabi`


### 📊 **Proposal #51914**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (2):**
- ❌ `src/net/http`
- ✅ `src/net/http/httputil`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/httputil/reverseproxy.go`
- `src/net/http/httputil/reverseproxy_test.go`

**Predicted Files (6):**
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/response_test.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/server_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http/httputil`


### 📊 **Proposal #40481**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 14.3% | 25.0% | 1/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/compile/internal/ir`
- `src/cmd/compile/internal/ssagen`
- `src/cmd/compile/internal/typecheck`
- `src/cmd/compile/internal/walk`
- `src/go/types`
- `src/unsafe`
- `test`

**Predicted Directories (1):**
- ✅ `src/unsafe`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 8.3% | 15.4% | 1/12 |

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

**Predicted Files (1):**
- ✅ `src/unsafe/unsafe.go`

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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/syscall`

**Predicted Directories (1):**
- ✅ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/syscall_windows.go`
- `src/runtime/syscall_windows_test.go`
- `src/syscall/dll_windows.go`

**Predicted Files (4):**
- ❌ `src/syscall/mksyscall_windows.go`
- ❌ `src/syscall/syscall.go`
- ❌ `src/syscall/syscall_windows.go`
- ❌ `src/syscall/syscall_windows_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall`


### 📊 **Proposal #33136**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (1):**
- ✅ `src/reflect/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

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
| 36.4% | 33.3% | 34.8% | 4/12 |

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

**Predicted Directories (11):**
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/cgo/test`
- ❌ `src/cmd/cgo/testsanitizers`
- ✅ `src/cmd/compile/internal/pkginit`
- ❌ `src/cmd/dist`
- ✅ `src/cmd/link/internal/ld`
- ❌ `src/internal/asan`
- ✅ `src/runtime`
- ❌ `src/runtime/asan`
- ❌ `src/runtime/msan`
- ✅ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.0% | 16.1% | 8.8% | 5/31 |

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

**Predicted Files (83):**
- ❌ `src/cmd/cgo/test/test.go`
- ❌ `src/cmd/cgo/test/test26213.go`
- ❌ `src/cmd/cgo/test/test_unix.go`
- ❌ `src/cmd/cgo/test/test_windows.go`
- ❌ `src/cmd/cgo/testsanitizers/asan_test.go`
- ❌ `src/cmd/cgo/testsanitizers/cc_test.go`
- ❌ `src/cmd/cgo/testsanitizers/cshared_test.go`
- ❌ `src/cmd/cgo/testsanitizers/empty_test.go`
- ❌ `src/cmd/cgo/testsanitizers/libfuzzer_test.go`
- ❌ `src/cmd/cgo/testsanitizers/lsan_test.go`
- ❌ `src/cmd/cgo/testsanitizers/msan_test.go`
- ❌ `src/cmd/cgo/testsanitizers/tsan_test.go`
- ❌ `src/cmd/cgo/testx.go`
- ✅ `src/cmd/compile/internal/pkginit/initAsanGlobals.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/dist/testjson.go`
- ❌ `src/cmd/dist/testjson_test.go`
- ✅ `src/cmd/link/internal/ld/config.go`
- ❌ `src/cmd/link/internal/ld/data.go`
- ❌ `src/cmd/link/internal/ld/data_test.go`
- ❌ `src/cmd/link/internal/ld/deadcode.go`
- ❌ `src/cmd/link/internal/ld/deadcode_test.go`
- ❌ `src/cmd/link/internal/ld/decodesym.go`
- ❌ `src/cmd/link/internal/ld/dwarf.go`
- ❌ `src/cmd/link/internal/ld/dwarf_test.go`
- ❌ `src/cmd/link/internal/ld/elf.go`
- ❌ `src/cmd/link/internal/ld/elf_test.go`
- ❌ `src/cmd/link/internal/ld/errors.go`
- ❌ `src/cmd/link/internal/ld/execarchive.go`
- ❌ `src/cmd/link/internal/ld/execarchive_noexec.go`
- ❌ `src/cmd/link/internal/ld/fips140.go`
- ❌ `src/cmd/link/internal/ld/go.go`
- ❌ `src/cmd/link/internal/ld/go_test.go`
- ❌ `src/cmd/link/internal/ld/heap.go`
- ❌ `src/cmd/link/internal/ld/heap_test.go`
- ❌ `src/cmd/link/internal/ld/inittask.go`
- ❌ `src/cmd/link/internal/ld/issue33808_test.go`
- ❌ `src/cmd/link/internal/ld/ld.go`
- ✅ `src/cmd/link/internal/ld/lib.go`
- ❌ `src/cmd/link/internal/ld/link.go`
- ❌ `src/cmd/link/internal/ld/macho.go`
- ❌ `src/cmd/link/internal/ld/macho_combine_dwarf.go`
- ❌ `src/cmd/link/internal/ld/macho_test.go`
- ❌ `src/cmd/link/internal/ld/macho_update_uuid.go`
- ❌ `src/cmd/link/internal/ld/main.go`
- ❌ `src/cmd/link/internal/ld/msync_darwin_libc.go`
- ❌ `src/cmd/link/internal/ld/nooptcgolink_test.go`
- ❌ `src/cmd/link/internal/ld/outbuf.go`
- ❌ `src/cmd/link/internal/ld/outbuf_darwin.go`
- ❌ `src/cmd/link/internal/ld/outbuf_freebsd.go`
- ❌ `src/cmd/link/internal/ld/outbuf_linux.go`
- ❌ `src/cmd/link/internal/ld/outbuf_mmap.go`
- ❌ `src/cmd/link/internal/ld/outbuf_nofallocate.go`
- ❌ `src/cmd/link/internal/ld/outbuf_nommap.go`
- ❌ `src/cmd/link/internal/ld/outbuf_notdarwin.go`
- ❌ `src/cmd/link/internal/ld/outbuf_test.go`
- ❌ `src/cmd/link/internal/ld/outbuf_windows.go`
- ❌ `src/cmd/link/internal/ld/pcln.go`
- ❌ `src/cmd/link/internal/ld/pe.go`
- ❌ `src/cmd/link/internal/ld/seh.go`
- ❌ `src/cmd/link/internal/ld/stackcheck.go`
- ❌ `src/cmd/link/internal/ld/stackcheck_test.go`
- ❌ `src/cmd/link/internal/ld/sym.go`
- ❌ `src/cmd/link/internal/ld/symtab.go`
- ❌ `src/cmd/link/internal/ld/target.go`
- ❌ `src/cmd/link/internal/ld/typelink.go`
- ❌ `src/cmd/link/internal/ld/util.go`
- ❌ `src/cmd/link/internal/ld/xcoff.go`
- ❌ `src/internal/asan/asan.go`
- ❌ `src/internal/asan/doc.go`
- ❌ `src/internal/asan/noasan.go`
- ❌ `src/runtime/asan/asan.go`
- ✅ `src/runtime/malloc.go`
- ❌ `src/runtime/msan/msan.go`
- ❌ `src/syscall/syscall.go`
- ❌ `src/syscall/syscall_linux.go`
- ❌ `src/syscall/syscall_linux_amd64.go`
- ❌ `src/syscall/syscall_linux_arm64.go`
- ❌ `src/syscall/syscall_linux_riscv64.go`
- ❌ `src/syscall/syscall_linux_s390x.go`
- ❌ `src/syscall/syscall_linux_test.go`
- ✅ `src/syscall/syscall_unix.go`
- ❌ `src/syscall/syscall_unix_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.1% | 16.1% | 10.8% | 5/31 |

##### Correct Directories Used for Evaluation

**Correct Directories (4):**
- `src/cmd/compile/internal/pkginit`
- `src/cmd/link/internal/ld`
- `src/runtime`
- `src/syscall`


### 📊 **Proposal #50599**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 20.0% | 33.3% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/go/internal/vcs`
- `src/cmd/go/internal/work`
- `src/cmd/internal/moddeps`
- `src/go/build`
- `src/os/exec`

**Predicted Directories (1):**
- ✅ `src/os/exec`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 25.0% | 40.0% | 3/12 |

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

**Predicted Files (3):**
- ✅ `src/os/exec/env_test.go`
- ✅ `src/os/exec/exec.go`
- ✅ `src/os/exec/exec_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 25.0% | 40.0% | 3/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/os/exec`


### 📊 **Proposal #42537**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 7.0% | 12.0% | 3/43 |

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

**Predicted Directories (7):**
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/modload`
- ✅ `src/mime`
- ✅ `src/runtime/testdata/testprog`
- ❌ `src/testing`
- ❌ `src/testing/fstest`
- ✅ `test`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 2.7% | 4.9% | 2/74 |

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

**Predicted Files (7):**
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/proxy_test.go`
- ✅ `src/mime/mediatype.go`
- ✅ `src/runtime/testdata/testprog/traceback_ancestors.go`
- ❌ `src/testing/benchmark.go`
- ❌ `src/testing/fstest/mapfs.go`
- ❌ `test/run.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 2.7% | 5.2% | 2/74 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/mime`
- `src/runtime/testdata/testprog`
- `test`


### 📊 **Proposal #40995**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 42.9% | 54.5% | 3/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/dist`
- `src/cmd/link/internal/mips64`
- `src/cmd/vendor/golang.org/x/sys/unix`
- `src/cmd/vendor/golang.org/x/sys/windows`
- `src/runtime`
- `src/syscall`
- `src/vendor/golang.org/x/sys/cpu`

**Predicted Directories (4):**
- ✅ `src/cmd/link/internal/mips64`
- ✅ `src/runtime`
- ✅ `src/syscall`
- ❌ `src/vendor/golang.org/x/sys/unix`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 35.3% | 15.8% | 21.8% | 6/38 |

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

**Predicted Files (17):**
- ❌ `src/cmd/link/internal/mips64/asm.go`
- ❌ `src/cmd/link/internal/mips64/l.go`
- ✅ `src/cmd/link/internal/mips64/obj.go`
- ✅ `src/runtime/defs_openbsd_mips64.go`
- ✅ `src/runtime/os_openbsd_mips64.go`
- ✅ `src/runtime/signal_openbsd_mips64.go`
- ✅ `src/syscall/syscall_openbsd_mips64.go`
- ❌ `src/syscall/zerrors_openbsd_mips64.go`
- ✅ `src/syscall/zsyscall_openbsd_mips64.go`
- ❌ `src/syscall/zsysnum_openbsd_mips64.go`
- ❌ `src/syscall/ztypes_openbsd_mips64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/syscall_openbsd_mips64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/zerrors_openbsd_mips64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/zsyscall_openbsd_mips64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/zsysctl_openbsd_mips64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/zsysnum_openbsd_mips64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/ztypes_openbsd_mips64.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 54.5% | 15.8% | 24.5% | 6/38 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/cmd/link/internal/mips64`
- `src/runtime`
- `src/syscall`


### 📊 **Proposal #39034**

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
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/format.go`
- `src/time/format_test.go`

**Predicted Files (3):**
- ❌ `lib/time/mkzip.go`
- ✅ `src/time/format.go`
- ❌ `src/time/time.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #45100**

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


### 📊 **Proposal #47005**

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


### 📊 **Proposal #53482**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (2):**
- ✅ `src/net`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 16.7% | 18.2% | 1/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/net/interface_aix.go`
- `src/net/interface_bsd.go`
- `src/net/interface_linux.go`
- `src/net/interface_plan9.go`
- `src/net/interface_solaris.go`
- `src/net/interface_windows.go`

**Predicted Files (5):**
- ❌ `src/net/interface.go`
- ✅ `src/net/interface_linux.go`
- ❌ `src/net/interface_linux_test.go`
- ❌ `src/net/interface_test.go`
- ❌ `src/syscall/zerrors_linux_amd64.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 16.7% | 20.0% | 1/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #37112**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/work`
- `src/runtime`
- `src/runtime/metrics`

**Predicted Directories (2):**
- ✅ `src/runtime`
- ✅ `src/runtime/metrics`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 55.6% | 45.5% | 50.0% | 5/11 |

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

**Predicted Files (9):**
- ✅ `src/runtime/metrics.go`
- ✅ `src/runtime/metrics/description.go`
- ❌ `src/runtime/metrics/description_test.go`
- ❌ `src/runtime/metrics/doc.go`
- ❌ `src/runtime/metrics/example_test.go`
- ❌ `src/runtime/metrics/histogram.go`
- ✅ `src/runtime/metrics/sample.go`
- ✅ `src/runtime/metrics/value.go`
- ✅ `src/runtime/metrics_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 55.6% | 45.5% | 50.0% | 5/11 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/runtime`
- `src/runtime/metrics`


### 📊 **Proposal #46771**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/mime/multipart`

**Predicted Directories (1):**
- ✅ `src/mime/multipart`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/mime/multipart/writer.go`
- `src/mime/multipart/writer_test.go`

**Predicted Files (2):**
- ❌ `src/mime/multipart/formdata.go`
- ✅ `src/mime/multipart/writer.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/mime/multipart`


### 📊 **Proposal #48424**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 14.3% | 25.0% | 1/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/syntax`
- `src/cmd/compile/internal/types2`
- `src/go/internal/gcimporter`
- `src/go/parser`
- `src/go/types`
- `test/typeparam`

**Predicted Directories (1):**
- ✅ `test/typeparam`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 5.3% | 10.0% | 1/19 |

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

**Predicted Files (1):**
- ✅ `test/typeparam/issue48424.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 5.3% | 10.0% | 1/19 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `test/typeparam`


### 📊 **Proposal #46485**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 20.0% | 28.6% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/cgo`
- `src/cmd/go/internal/load`
- `src/cmd/gofmt`
- `src/go/internal/srcimporter`
- `src/go/parser`

**Predicted Directories (2):**
- ❌ `src/cmd/compile/internal/syntax`
- ✅ `src/go/parser`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 14.3% | 14.3% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/cgo/ast.go`
- `src/cmd/go/internal/load/test.go`
- `src/cmd/gofmt/gofmt.go`
- `src/cmd/gofmt/simplify.go`
- `src/go/internal/srcimporter/srcimporter.go`
- `src/go/parser/parser.go`
- `src/go/parser/performance_test.go`

**Predicted Files (7):**
- ❌ `src/cmd/compile/internal/syntax/parser.go`
- ❌ `src/cmd/compile/internal/syntax/parser_test.go`
- ❌ `src/go/parser/interface.go`
- ✅ `src/go/parser/parser.go`
- ❌ `src/go/parser/parser_test.go`
- ❌ `src/go/parser/resolver.go`
- ❌ `src/go/parser/resolver_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 14.3% | 16.7% | 1/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/parser`


### 📊 **Proposal #34652**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/html/template`
- `src/text/template`
- `src/text/template/parse`

**Predicted Directories (1):**
- ✅ `src/text/template/parse`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 62.5% | 76.9% | 5/8 |

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

**Predicted Files (5):**
- ✅ `src/text/template/parse/lex.go`
- ✅ `src/text/template/parse/lex_test.go`
- ✅ `src/text/template/parse/node.go`
- ✅ `src/text/template/parse/parse.go`
- ✅ `src/text/template/parse/parse_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 62.5% | 76.9% | 5/8 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/text/template/parse`


### 📊 **Proposal #42098**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (3):**
- ❌ `src/internal/syscall/windows`
- ❌ `src/os/exec`
- ✅ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/syscall/exec_windows.go`

**Predicted Files (7):**
- ❌ `src/internal/syscall/windows/exec_windows_test.go`
- ❌ `src/internal/syscall/windows/syscall_windows.go`
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
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/web`
- `src/io/ioutil`
- `src/testing`

**Predicted Directories (1):**
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/cmd/go/internal/web/file_test.go`
- `src/io/ioutil/tempfile_test.go`
- `src/testing/testing.go`
- `src/testing/testing_test.go`

**Predicted Files (2):**
- ✅ `src/testing/testing.go`
- ✅ `src/testing/testing_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
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
- ❌ `src/cmd/vet`
- ❌ `src/tools/go/analysis/passes/directive`
- ❌ `src/vet/testdata/directive`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/embed/embed.go`
- `src/embed/internal/embedtest/embed_test.go`

**Predicted Files (4):**
- ❌ `src/cmd/vet/vet.go`
- ❌ `src/cmd/vet/vetflag.go`
- ❌ `src/tools/go/analysis/passes/directive/directive.go`
- ❌ `src/vet/testdata/directive/directive.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (1):**
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
- ❌ `src/time/abs_test.go`
- ✅ `src/time/time.go`
- ✅ `src/time/time_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #37023**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/runtime/debug`

**Predicted Directories (2):**
- ✅ `src/runtime`
- ✅ `src/runtime/debug`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 33.3% | 44.4% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/runtime/debug/panic_test.go`
- `src/runtime/error.go`
- `src/runtime/os_plan9.go`
- `src/runtime/panic.go`
- `src/runtime/signal_unix.go`
- `src/runtime/signal_windows.go`

**Predicted Files (3):**
- ❌ `src/runtime/debug/stack.go`
- ✅ `src/runtime/panic.go`
- ✅ `src/runtime/signal_unix.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 33.3% | 44.4% | 2/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/runtime`
- `src/runtime/debug`


### 📊 **Proposal #46258**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (1):**
- ✅ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 50.0% | 30.8% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/syscall/exec_freebsd.go`
- `src/syscall/exec_pdeathsig_test.go`
- `src/syscall/syscall_freebsd_test.go`
- `src/syscall/syscall_linux_test.go`

**Predicted Files (9):**
- ✅ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/exec_freebsd_test.go`
- ❌ `src/syscall/syscall_freebsd.go`
- ❌ `src/syscall/syscall_freebsd_386.go`
- ❌ `src/syscall/syscall_freebsd_amd64.go`
- ❌ `src/syscall/syscall_freebsd_arm.go`
- ❌ `src/syscall/syscall_freebsd_arm64.go`
- ❌ `src/syscall/syscall_freebsd_riscv64.go`
- ✅ `src/syscall/syscall_freebsd_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 50.0% | 30.8% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall`


### 📊 **Proposal #51430**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 6.7% | 11.1% | 1/15 |

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

**Predicted Directories (3):**
- ✅ `src/cmd/covdata`
- ❌ `src/cmd/cover`
- ❌ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 38.9% | 24.1% | 29.8% | 7/29 |

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

**Predicted Files (18):**
- ✅ `src/cmd/covdata/argsmerge.go`
- ✅ `src/cmd/covdata/covdata.go`
- ❌ `src/cmd/covdata/doc.go`
- ✅ `src/cmd/covdata/dump.go`
- ❌ `src/cmd/covdata/export_test.go`
- ✅ `src/cmd/covdata/merge.go`
- ✅ `src/cmd/covdata/metamerge.go`
- ✅ `src/cmd/covdata/subtractintersect.go`
- ✅ `src/cmd/covdata/tool_test.go`
- ❌ `src/cmd/cover/cover.go`
- ❌ `src/cmd/cover/cover_test.go`
- ❌ `src/cmd/cover/doc.go`
- ❌ `src/cmd/cover/export_test.go`
- ❌ `src/cmd/cover/func.go`
- ❌ `src/cmd/cover/html.go`
- ❌ `src/cmd/cover/pkgname_test.go`
- ❌ `src/testing/cover.go`
- ❌ `src/testing/newcover.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 77.8% | 24.1% | 36.8% | 7/29 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/covdata`


### 📊 **Proposal #46308**

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
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/tls_test.go`

**Predicted Files (3):**
- ✅ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/common_string.go`
- ❌ `src/crypto/tls/tls.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #37033**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/link/internal/ld`
- `src/runtime/cgo`

**Predicted Directories (5):**
- ❌ `misc/cgo/gmp`
- ❌ `src/cmd/cgo/internal/cgotest`
- ❌ `src/cmd/cgo/internal/swig`
- ❌ `src/cmd/cgo/internal/test`
- ✅ `src/runtime/cgo`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.4% | 66.7% | 25.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/link/internal/ld/lib.go`
- `src/runtime/cgo/handle.go`
- `src/runtime/cgo/handle_test.go`

**Predicted Files (13):**
- ❌ `misc/cgo/gmp/fib.go`
- ❌ `misc/cgo/gmp/gmp.go`
- ❌ `misc/cgo/gmp/pi.go`
- ❌ `src/cmd/cgo/internal/cgotest/overlaydir.go`
- ❌ `src/cmd/cgo/internal/swig/swig_test.go`
- ❌ `src/cmd/cgo/internal/test/cgo_linux_test.go`
- ❌ `src/cmd/cgo/internal/test/cgo_stubs_android_test.go`
- ❌ `src/cmd/cgo/internal/test/cgo_stubs_ppc64x_internal_linking_test.go`
- ❌ `src/cmd/cgo/internal/test/cgo_test.go`
- ❌ `src/cmd/cgo/internal/test/cgo_thread_lock.go`
- ❌ `src/cmd/cgo/internal/test/cgo_unix_test.go`
- ✅ `src/runtime/cgo/handle.go`
- ✅ `src/runtime/cgo/handle_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime/cgo`


### 📊 **Proposal #51766**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/netip`

**Predicted Directories (1):**
- ✅ `src/net/netip`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/netip/netip_test.go`

**Predicted Files (1):**
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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/regexp/syntax`

**Predicted Directories (1):**
- ✅ `src/regexp/syntax`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/regexp/syntax/parse.go`

**Predicted Files (3):**
- ✅ `src/regexp/syntax/parse.go`
- ❌ `src/regexp/syntax/parse_test.go`
- ❌ `src/regexp/syntax/regexp.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/regexp/syntax`


### 📊 **Proposal #51896**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/unicode/utf16`

**Predicted Directories (1):**
- ✅ `src/unicode/utf16`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/unicode/utf16/utf16.go`
- `src/unicode/utf16/utf16_test.go`

**Predicted Files (2):**
- ✅ `src/unicode/utf16/utf16.go`
- ✅ `src/unicode/utf16/utf16_test.go`

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
| 33.3% | 33.3% | 33.3% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/run`
- `src/cmd/go/internal/work`

**Predicted Directories (3):**
- ❌ `src/cmd/go/internal/modload`
- ✅ `src/cmd/go/internal/run`
- ❌ `test/fixedbugs`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 33.3% | 16.7% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/run/run.go`
- `src/cmd/go/internal/work/build.go`

**Predicted Files (9):**
- ❌ `src/cmd/go/internal/modload/build.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ❌ `src/cmd/go/internal/modload/search.go`
- ❌ `src/cmd/go/internal/modload/stat_openfile.go`
- ❌ `src/cmd/go/internal/modload/stat_unix.go`
- ❌ `src/cmd/go/internal/modload/stat_windows.go`
- ✅ `src/cmd/go/internal/run/run.go`
- ❌ `test/fixedbugs/issue42076.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/run`


### 📊 **Proposal #19367**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (2):**
- ❌ `src/unsafe`
- ❌ `test`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/runtime/checkptr.go`
- `src/runtime/select.go`

**Predicted Files (5):**
- ❌ `src/unsafe/unsafe.go`
- ❌ `test/unsafe_slice_data.go`
- ❌ `test/unsafe_string.go`
- ❌ `test/unsafe_string_data.go`
- ❌ `test/unsafebuiltins.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #37168**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/rc4`
- `src/image`

**Predicted Directories (9):**
- ❌ `src/crypto/aes`
- ❌ `src/crypto/cipher`
- ❌ `src/crypto/elliptic`
- ❌ `src/crypto/sha1`
- ❌ `src/crypto/sha256`
- ❌ `src/crypto/sha3`
- ❌ `src/crypto/sha512`
- ❌ `src/crypto/x509`
- ❌ `src/math/big/internal/asmgen`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/rc4/rc4.go`
- `src/crypto/rc4/rc4_test.go`
- `src/image/image_test.go`

**Predicted Files (28):**
- ❌ `src/crypto/aes/aes.go`
- ❌ `src/crypto/cipher/gcm.go`
- ❌ `src/crypto/elliptic/elliptic.go`
- ❌ `src/crypto/sha1/sha1.go`
- ❌ `src/crypto/sha256/sha256.go`
- ❌ `src/crypto/sha3/sha3.go`
- ❌ `src/crypto/sha512/sha512.go`
- ❌ `src/crypto/x509/x509.go`
- ❌ `src/math/big/internal/asmgen/386.go`
- ❌ `src/math/big/internal/asmgen/add.go`
- ❌ `src/math/big/internal/asmgen/amd64.go`
- ❌ `src/math/big/internal/asmgen/arch.go`
- ❌ `src/math/big/internal/asmgen/arm.go`
- ❌ `src/math/big/internal/asmgen/arm64.go`
- ❌ `src/math/big/internal/asmgen/asm.go`
- ❌ `src/math/big/internal/asmgen/cheat.go`
- ❌ `src/math/big/internal/asmgen/func.go`
- ❌ `src/math/big/internal/asmgen/loong64.go`
- ❌ `src/math/big/internal/asmgen/main.go`
- ❌ `src/math/big/internal/asmgen/main_test.go`
- ❌ `src/math/big/internal/asmgen/mips.go`
- ❌ `src/math/big/internal/asmgen/mips64.go`
- ❌ `src/math/big/internal/asmgen/mul.go`
- ❌ `src/math/big/internal/asmgen/pipe.go`
- ❌ `src/math/big/internal/asmgen/ppc64.go`
- ❌ `src/math/big/internal/asmgen/riscv64.go`
- ❌ `src/math/big/internal/asmgen/s390x.go`
- ❌ `src/math/big/internal/asmgen/shift.go`

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
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/test`
- `src/cmd/objdump`
- `src/internal/testenv`

**Predicted Directories (2):**
- ✅ `src/cmd/go/internal/test`
- ❌ `src/cmd/test2json`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 33.3% | 20.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/test/test.go`
- `src/cmd/objdump/objdump_test.go`
- `src/internal/testenv/testenv.go`

**Predicted Files (7):**
- ❌ `src/cmd/go/internal/test/flagdefs.go`
- ❌ `src/cmd/go/internal/test/flagdefs_test.go`
- ❌ `src/cmd/go/internal/test/genflags.go`
- ✅ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/go/internal/test/testflag.go`
- ❌ `src/cmd/test2json/test2json.go`
- ❌ `src/cmd/test2json/test2json_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 33.3% | 25.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/test`


### 📊 **Proposal #43823**

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
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/time/format.go`

**Predicted Files (5):**
- ❌ `lib/time/mkzip.go`
- ✅ `src/time/format.go`
- ❌ `src/time/format_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`

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

**Predicted Directories (1):**
- ❌ `src/cmd/go/internal/test`

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

**Predicted Files (5):**
- ❌ `src/cmd/go/internal/test/flagdefs.go`
- ❌ `src/cmd/go/internal/test/flagdefs_test.go`
- ❌ `src/cmd/go/internal/test/genflags.go`
- ❌ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/go/internal/test/testflag.go`

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
- ✅ `src/encoding/json`
- ❌ `src/encoding/json/internal/jsonwire`
- ❌ `src/encoding/json/v2`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 33.3% | 22.2% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/encoding/json/decode.go`
- `src/encoding/json/stream.go`
- `src/encoding/json/stream_test.go`

**Predicted Files (6):**
- ✅ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ❌ `src/encoding/json/internal/jsonwire/decode.go`
- ❌ `src/encoding/json/internal/jsonwire/decode_test.go`
- ❌ `src/encoding/json/v2/intern.go`
- ❌ `src/encoding/json/v2/intern_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/json`


### 📊 **Proposal #46131**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/reflect/all_test.go`

**Predicted Files (2):**
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`

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

**Predicted Directories (1):**
- ❌ `src/cmd/compile/internal/gc`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/base/flag.go`
- `src/cmd/compile/internal/noder/import.go`
- `src/cmd/go/internal/work/gc.go`

**Predicted Files (5):**
- ❌ `src/cmd/compile/internal/gc/compile.go`
- ❌ `src/cmd/compile/internal/gc/export.go`
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/gc/obj.go`
- ❌ `src/cmd/compile/internal/gc/util.go`

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
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/io`
- `src/io/ioutil`
- `src/os`

**Predicted Directories (2):**
- ✅ `src/io`
- ✅ `src/io/ioutil`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 16.7% | 25.0% | 2/12 |

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

**Predicted Files (4):**
- ✅ `src/io/io.go`
- ❌ `src/io/io_test.go`
- ✅ `src/io/ioutil/ioutil.go`
- ❌ `src/io/ioutil/ioutil_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 16.7% | 25.0% | 2/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/io`
- `src/io/ioutil`


### 📊 **Proposal #47527**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/bufio`

**Predicted Directories (1):**
- ✅ `src/bufio`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/bufio/bufio.go`
- `src/bufio/bufio_test.go`
- `src/bufio/example_test.go`

**Predicted Files (2):**
- ✅ `src/bufio/bufio.go`
- ✅ `src/bufio/bufio_test.go`

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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/ast`

**Predicted Directories (2):**
- ❌ `src/cmd/go/internal/doc`
- ✅ `src/go/ast`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/ast/ast.go`
- `src/go/ast/ast_test.go`

**Predicted Files (3):**
- ❌ `src/cmd/go/internal/doc/doc.go`
- ✅ `src/go/ast/ast.go`
- ✅ `src/go/ast/ast_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/ast`


### 📊 **Proposal #37776**

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
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/net/url/example_test.go`
- `src/net/url/url.go`
- `src/net/url/url_test.go`

**Predicted Files (2):**
- ✅ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`

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
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/list`
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modload`

**Predicted Directories (3):**
- ❌ `src/cmd/go`
- ✅ `src/cmd/go/internal/modcmd`
- ✅ `src/cmd/go/internal/modload`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 13.6% | 60.0% | 22.2% | 3/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/go/internal/list/list.go`
- `src/cmd/go/internal/modcmd/download.go`
- `src/cmd/go/internal/modcmd/why.go`
- `src/cmd/go/internal/modload/build.go`
- `src/cmd/go/internal/modload/list.go`

**Predicted Files (22):**
- ❌ `src/cmd/go/go.go`
- ❌ `src/cmd/go/go_test.go`
- ✅ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modcmd/edit.go`
- ❌ `src/cmd/go/internal/modcmd/graph.go`
- ❌ `src/cmd/go/internal/modcmd/init.go`
- ❌ `src/cmd/go/internal/modcmd/tidy.go`
- ❌ `src/cmd/go/internal/modcmd/vendor.go`
- ❌ `src/cmd/go/internal/modcmd/verify.go`
- ✅ `src/cmd/go/internal/modcmd/why.go`
- ❌ `src/cmd/go/internal/modload/deprecate.go`
- ❌ `src/cmd/go/internal/modload/deprecate_test.go`
- ❌ `src/cmd/go/internal/modload/edit.go`
- ✅ `src/cmd/go/internal/modload/list.go`
- ❌ `src/cmd/go/internal/modload/list_test.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/modfile_test.go`
- ❌ `src/cmd/go/internal/modload/resolve.go`
- ❌ `src/cmd/go/internal/modload/resolve_test.go`
- ❌ `src/cmd/go/internal/modload/rewrite.go`
- ❌ `src/cmd/go/internal/modload/rewrite_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.0% | 60.0% | 24.0% | 3/5 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modload`


### 📊 **Proposal #39557**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (1):**
- ✅ `src/flag`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 3/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/flag/example_func_test.go`
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (3):**
- ✅ `src/flag/example_func_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 3/3 |

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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`

**Predicted Files (1):**
- ✅ `src/database/sql/sql.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/database/sql`


### 📊 **Proposal #53003**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 20.0% | 33.3% | 2/10 |

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

**Predicted Directories (2):**
- ✅ `src/unsafe`
- ✅ `test`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 17.6% | 28.6% | 3/17 |

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

**Predicted Files (4):**
- ✅ `src/unsafe/unsafe.go`
- ✅ `test/unsafe_slice_data.go`
- ✅ `test/unsafe_string.go`
- ❌ `test/unsafe_string_data.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 17.6% | 28.6% | 3/17 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/unsafe`
- `test`


### 📊 **Proposal #40281**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- `src/reflect`

**Predicted Directories (5):**
- ❌ `src/encoding/json`
- ❌ `src/encoding/xml`
- ✅ `src/reflect`
- ❌ `src/tools/go/analysis/passes/structtag`
- ❌ `src/vet/testdata/structtag`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 50.0% | 18.2% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- `src/reflect/type.go`

**Predicted Files (9):**
- ❌ `src/encoding/json/tags.go`
- ❌ `src/encoding/json/tags_test.go`
- ❌ `src/encoding/xml/marshal.go`
- ❌ `src/encoding/xml/marshal_test.go`
- ❌ `src/reflect/abi.go`
- ✅ `src/reflect/type.go`
- ❌ `src/reflect/value.go`
- ❌ `src/tools/go/analysis/passes/structtag/structtag.go`
- ❌ `src/vet/testdata/structtag/structtag.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

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
| 50.0% | 12.5% | 20.0% | 1/8 |

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

**Predicted Files (2):**
- ✅ `src/reflect/type.go`
- ❌ `src/reflect/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 12.5% | 20.0% | 1/8 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #46121**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/html/template`

**Predicted Directories (2):**
- ✅ `src/html/template`
- ❌ `src/text/template`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/html/template/template.go`

**Predicted Files (4):**
- ✅ `src/html/template/template.go`
- ❌ `src/html/template/template_test.go`
- ❌ `src/text/template/funcs.go`
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
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/dist`
- `src/os/exec`

**Predicted Directories (3):**
- ❌ `src/cmd/internal/pathcache`
- ✅ `src/os/exec`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 12.5% | 13.3% | 1/8 |

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

**Predicted Files (7):**
- ❌ `src/cmd/internal/pathcache/lookpath.go`
- ❌ `src/os/exec/exec_windows.go`
- ❌ `src/os/exec/exec_windows_test.go`
- ✅ `src/os/exec/lp_windows.go`
- ❌ `src/os/exec/lp_windows_test.go`
- ❌ `src/syscall/exec_windows.go`
- ❌ `src/syscall/exec_windows_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 12.5% | 16.7% | 1/8 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/os/exec`


### 📊 **Proposal #50860**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 25.0% | 28.6% | 1/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `src/cmd/compile/internal/escape`
- `src/cmd/compile/internal/test`
- `src/cmd/compile/internal/types`
- `src/sync/atomic`

**Predicted Directories (3):**
- ❌ `src/internal/abi`
- ❌ `src/runtime/atomic`
- ✅ `src/sync/atomic`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 40.0% | 26.7% | 2/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/compile/internal/escape/utils.go`
- `src/cmd/compile/internal/test/inl_test.go`
- `src/cmd/compile/internal/types/size.go`
- `src/sync/atomic/atomic_test.go`
- `src/sync/atomic/type.go`

**Predicted Files (10):**
- ❌ `src/internal/abi/types.go`
- ❌ `src/runtime/atomic/types.go`
- ✅ `src/sync/atomic/atomic_test.go`
- ❌ `src/sync/atomic/doc.go`
- ❌ `src/sync/atomic/doc_32.go`
- ❌ `src/sync/atomic/doc_64.go`
- ❌ `src/sync/atomic/example_test.go`
- ✅ `src/sync/atomic/type.go`
- ❌ `src/sync/atomic/value.go`
- ❌ `src/sync/atomic/value_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 40.0% | 30.8% | 2/5 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/sync/atomic`


### 📊 **Proposal #52444**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (1):**
- ✅ `src/crypto/x509`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (4):**
- ❌ `src/crypto/x509/parser.go`
- ❌ `src/crypto/x509/parser_test.go`
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #43724**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/syscall/windows`
- `src/syscall`

**Predicted Directories (3):**
- ❌ `src/os/exec`
- ❌ `src/os/exec/internal/fdtest`
- ✅ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/internal/syscall/windows/zsyscall_windows.go`
- `src/syscall/mksyscall_windows.go`

**Predicted Files (10):**
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/internal/fdtest/exists_plan9.go`
- ❌ `src/os/exec/internal/fdtest/exists_test.go`
- ❌ `src/os/exec/internal/fdtest/exists_unix.go`
- ❌ `src/os/exec/internal/fdtest/exists_windows.go`
- ❌ `src/syscall/exec_unix.go`
- ❌ `src/syscall/exec_unix_test.go`
- ❌ `src/syscall/exec_windows.go`
- ❌ `src/syscall/exec_windows_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall`


### 📊 **Proposal #41730**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 20.0% | 28.6% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/go`
- `src/cmd/go/internal/envcmd`
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modget`
- `src/cmd/go/internal/vcs`

**Predicted Directories (2):**
- ✅ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/vcweb`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 28.6% | 28.6% | 2/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/envcmd/env.go`
- `src/cmd/go/internal/modfetch/proxy.go`
- `src/cmd/go/internal/modget/get.go`
- `src/cmd/go/internal/vcs/vcs.go`
- `src/cmd/go/internal/vcs/vcs_test.go`
- `src/cmd/go/main.go`

**Predicted Files (7):**
- ✅ `src/cmd/go/internal/vcs/vcs.go`
- ✅ `src/cmd/go/internal/vcs/vcs_test.go`
- ❌ `src/cmd/go/internal/vcweb/bzr.go`
- ❌ `src/cmd/go/internal/vcweb/fossil.go`
- ❌ `src/cmd/go/internal/vcweb/git.go`
- ❌ `src/cmd/go/internal/vcweb/hg.go`
- ❌ `src/cmd/go/internal/vcweb/svn.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 28.6% | 44.4% | 2/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/vcs`


### 📊 **Proposal #51668**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/fmt`

**Predicted Directories (1):**
- ✅ `src/fmt`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/fmt/print.go`
- `src/fmt/state_test.go`

**Predicted Files (2):**
- ❌ `src/fmt/format.go`
- ✅ `src/fmt/print.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/fmt`


### 📊 **Proposal #41980**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/diff`
- `src/testing`

**Predicted Directories (1):**
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/internal/diff/diff_test.go`
- `src/testing/example.go`

**Predicted Files (1):**
- ❌ `src/testing/run_example.go`

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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (2):**
- ❌ `src/cmd/internal/objabi`
- ✅ `src/flag`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (4):**
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`

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
- ❌ `src/cmd/internal/sys`
- ❌ `src/cmd/link/internal/amd64`
- ❌ `src/internal/cpu`
- ❌ `src/internal/goarch`
- ❌ `src/vendor/golang.org/x/arch/x86/x86asm`

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

**Predicted Files (14):**
- ❌ `src/cmd/internal/sys/arch.go`
- ❌ `src/cmd/link/internal/amd64/asm.go`
- ❌ `src/cmd/link/internal/amd64/l.go`
- ❌ `src/cmd/link/internal/amd64/obj.go`
- ❌ `src/internal/cpu/cpu_x86.go`
- ❌ `src/internal/cpu/cpu_x86_test.go`
- ❌ `src/internal/goarch/goarch_amd64.go`
- ❌ `src/internal/goarch/zgoarch_amd64.go`
- ❌ `src/vendor/golang.org/x/arch/x86/x86asm/decode.go`
- ❌ `src/vendor/golang.org/x/arch/x86/x86asm/gnu.go`
- ❌ `src/vendor/golang.org/x/arch/x86/x86asm/inst.go`
- ❌ `src/vendor/golang.org/x/arch/x86/x86asm/intel.go`
- ❌ `src/vendor/golang.org/x/arch/x86/x86asm/plan9x.go`
- ❌ `src/vendor/golang.org/x/arch/x86/x86asm/tables.go`

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
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/work`

**Predicted Directories (2):**
- ❌ `src/cmd/go/internal/modget`
- ✅ `src/cmd/go/internal/modload`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.6% | 50.0% | 10.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modload/init.go`
- `src/cmd/go/internal/work/build.go`

**Predicted Files (18):**
- ❌ `src/cmd/go/internal/modget/get.go`
- ❌ `src/cmd/go/internal/modget/query.go`
- ❌ `src/cmd/go/internal/modload/build.go`
- ❌ `src/cmd/go/internal/modload/buildlist.go`
- ❌ `src/cmd/go/internal/modload/edit.go`
- ❌ `src/cmd/go/internal/modload/help.go`
- ❌ `src/cmd/go/internal/modload/import.go`
- ✅ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/modload/list.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/mvs.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ❌ `src/cmd/go/internal/modload/search.go`
- ❌ `src/cmd/go/internal/modload/stat_openfile.go`
- ❌ `src/cmd/go/internal/modload/stat_unix.go`
- ❌ `src/cmd/go/internal/modload/stat_windows.go`
- ❌ `src/cmd/go/internal/modload/vendor.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.2% | 50.0% | 11.1% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/modload`


### 📊 **Proposal #42322**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/embed/internal/embedtest`
- `src/io/fs`
- `src/testing/fstest`

**Predicted Directories (2):**
- ✅ `src/io/fs`
- ❌ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 28.6% | 30.8% | 2/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/embed/internal/embedtest/embed_test.go`
- `src/io/fs/readdir_test.go`
- `src/io/fs/readfile_test.go`
- `src/io/fs/sub.go`
- `src/io/fs/sub_test.go`
- `src/testing/fstest/mapfs.go`
- `src/testing/fstest/testfs.go`

**Predicted Files (6):**
- ❌ `src/io/fs/fs.go`
- ❌ `src/io/fs/fs_test.go`
- ✅ `src/io/fs/sub.go`
- ✅ `src/io/fs/sub_test.go`
- ❌ `src/net/http/fs.go`
- ❌ `src/net/http/fs_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 28.6% | 36.4% | 2/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io/fs`


### 📊 **Proposal #42100**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 25.0% | 33.3% | 1/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `misc/ios`
- `src/cmd/dist`
- `src/cmd/go/internal/work`
- `src/cmd/link/internal/ld`

**Predicted Directories (2):**
- ❌ `cmd/dist`
- ✅ `misc/ios`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 4.2% | 20.0% | 6.9% | 1/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `misc/ios/go_ios_exec.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/cmd/go/internal/work/init.go`
- `src/cmd/link/internal/ld/config.go`

**Predicted Files (24):**
- ❌ `cmd/dist/build.go`
- ❌ `cmd/dist/build_test.go`
- ❌ `cmd/dist/buildgo.go`
- ❌ `cmd/dist/buildruntime.go`
- ❌ `cmd/dist/buildtag.go`
- ❌ `cmd/dist/buildtag_test.go`
- ❌ `cmd/dist/buildtool.go`
- ❌ `cmd/dist/doc.go`
- ❌ `cmd/dist/exec.go`
- ❌ `cmd/dist/imports.go`
- ❌ `cmd/dist/main.go`
- ❌ `cmd/dist/notgo122.go`
- ❌ `cmd/dist/quoted.go`
- ❌ `cmd/dist/supported_test.go`
- ❌ `cmd/dist/sys_default.go`
- ❌ `cmd/dist/sys_windows.go`
- ❌ `cmd/dist/test.go`
- ❌ `cmd/dist/testjson.go`
- ❌ `cmd/dist/testjson_test.go`
- ❌ `cmd/dist/util.go`
- ❌ `cmd/dist/util_gc.go`
- ❌ `cmd/dist/util_gccgo.go`
- ❌ `misc/ios/detect.go`
- ✅ `misc/ios/go_ios_exec.go`

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
| 80.0% | 44.4% | 57.1% | 4/9 |

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

**Predicted Directories (5):**
- ✅ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ✅ `src/cmd/go/internal/version`
- ✅ `src/cmd/go/internal/work`
- ✅ `src/runtime/debug`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 15.4% | 21.1% | 2/13 |

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

**Predicted Files (6):**
- ✅ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/git.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ✅ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/runtime/debug/debug.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 15.4% | 23.5% | 2/13 |

##### Correct Directories Used for Evaluation

**Correct Directories (4):**
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/version`
- `src/cmd/go/internal/work`
- `src/runtime/debug`


### 📊 **Proposal #39567**

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
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/serve_test.go`
- `src/net/http/server.go`

**Predicted Files (3):**
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
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/image`
- `src/image/draw`

**Predicted Directories (2):**
- ✅ `src/image`
- ✅ `src/image/draw`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 57.1% | 72.7% | 4/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/image/draw/draw.go`
- `src/image/draw/draw_test.go`
- `src/image/geom.go`
- `src/image/image.go`
- `src/image/image_test.go`
- `src/image/names.go`
- `src/image/ycbcr.go`

**Predicted Files (4):**
- ✅ `src/image/draw/draw.go`
- ✅ `src/image/draw/draw_test.go`
- ✅ `src/image/image.go`
- ✅ `src/image/image_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 57.1% | 72.7% | 4/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/image`
- `src/image/draw`


### 📊 **Proposal #45754**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (1):**
- ✅ `src/flag`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/example_textvar_test.go`
- `src/flag/flag.go`

**Predicted Files (3):**
- ✅ `src/flag/example_textvar_test.go`
- ✅ `src/flag/flag.go`
- ❌ `src/flag/flag_test.go`

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
| 100.0% | 4.8% | 9.1% | 1/21 |

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

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 4.9% | 9.3% | 2/41 |

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

**Predicted Files (2):**
- ✅ `src/reflect/type.go`
- ✅ `src/reflect/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 4.9% | 9.3% | 2/41 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #48052**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/debug/plan9obj`

**Predicted Directories (1):**
- ✅ `src/debug/plan9obj`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/debug/plan9obj/file.go`

**Predicted Files (3):**
- ✅ `src/debug/plan9obj/file.go`
- ❌ `src/debug/plan9obj/file_test.go`
- ❌ `src/debug/plan9obj/plan9obj.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/debug/plan9obj`


### 📊 **Proposal #33920**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/io/ioutil`
- `src/os`

**Predicted Directories (2):**
- ✅ `src/io/ioutil`
- ✅ `src/os`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/io/ioutil/tempfile.go`
- `src/io/ioutil/tempfile_test.go`
- `src/os/os_test.go`

**Predicted Files (4):**
- ✅ `src/io/ioutil/tempfile.go`
- ✅ `src/io/ioutil/tempfile_test.go`
- ❌ `src/os/tempfile.go`
- ❌ `src/os/tempfile_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/io/ioutil`
- `src/os`


### 📊 **Proposal #47209**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/fsys`
- `src/io/fs`
- `src/path/filepath`

**Predicted Directories (1):**
- ✅ `src/path/filepath`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 25.0% | 28.6% | 1/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/cmd/go/internal/fsys/fsys_test.go`
- `src/io/fs/walk.go`
- `src/path/filepath/path.go`
- `src/path/filepath/path_test.go`

**Predicted Files (3):**
- ❌ `src/path/filepath/match.go`
- ✅ `src/path/filepath/path.go`
- ❌ `src/path/filepath/symlink.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 25.0% | 28.6% | 1/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/path/filepath`


### 📊 **Proposal #48152**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/tls`
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/net/http/transport_test.go`

**Predicted Files (4):**
- ❌ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/conn_test.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/crypto/tls/tls_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #41682**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (1):**
- ✅ `src/crypto/x509`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/x509/verify_test.go`
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (2):**
- ❌ `src/crypto/x509/verify.go`
- ✅ `src/crypto/x509/verify_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #53200**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/token`

**Predicted Directories (1):**
- ✅ `src/go/token`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/token/position.go`
- `src/go/token/position_test.go`

**Predicted Files (2):**
- ✅ `src/go/token/position.go`
- ❌ `src/go/token/token.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

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
| 33.3% | 66.7% | 44.4% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/database/sql/fakedb_test.go`
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`

**Predicted Files (6):**
- ❌ `src/database/sql/convert.go`
- ❌ `src/database/sql/convert_test.go`
- ❌ `src/database/sql/driver/types.go`
- ❌ `src/database/sql/driver/types_test.go`
- ✅ `src/database/sql/sql.go`
- ✅ `src/database/sql/sql_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

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

**Predicted Directories (4):**
- ❌ `src/cmd/go/test`
- ❌ `src/cmd/go/test/internal/genflags`
- ❌ `src/cmd/vet`
- ❌ `src/golang.org/x/tools/go/analysis/internal/analysisflags`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/test/testflag.go`
- `src/cmd/go/internal/work/exec.go`

**Predicted Files (6):**
- ❌ `src/cmd/go/test/internal/genflags/testflag.go`
- ❌ `src/cmd/go/test/internal/genflags/vetflag.go`
- ❌ `src/cmd/go/test/test.go`
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/golang.org/x/tools/go/analysis/internal/analysisflags/flags.go`

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
| 100.0% | 20.0% | 33.3% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/internal/fuzz`
- `src/internal/godebug`
- `src/net`
- `src/net/http`
- `src/net/netip`

**Predicted Directories (1):**
- ✅ `src/net/netip`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 17.6% | 30.0% | 3/17 |

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

**Predicted Files (3):**
- ✅ `src/net/netip/netip.go`
- ✅ `src/net/netip/netip_pkg_test.go`
- ✅ `src/net/netip/netip_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 17.6% | 30.0% | 3/17 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/netip`


### 📊 **Proposal #40337**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (2):**
- ❌ `src/crypto/dsa`
- ✅ `src/crypto/x509`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (4):**
- ❌ `src/crypto/dsa/dsa.go`
- ❌ `src/crypto/x509/parser.go`
- ❌ `src/crypto/x509/verify.go`
- ✅ `src/crypto/x509/x509.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #45973**

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
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/serve_test.go`
- `src/net/http/server.go`

**Predicted Files (3):**
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/request.go`
- ✅ `src/net/http/server.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http`


### 📊 **Proposal #49471**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (1):**
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

**Predicted Files (5):**
- ❌ `src/syscall/dll_windows.go`
- ❌ `src/syscall/env_windows.go`
- ❌ `src/syscall/security_windows.go`
- ❌ `src/syscall/syscall_windows.go`
- ❌ `src/syscall/syscall_windows_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #52746**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modfetch/codehost`
- `src/cmd/go/internal/vcs`

**Predicted Directories (2):**
- ❌ `lib/time`
- ❌ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modfetch/codehost/vcs.go`
- `src/cmd/go/internal/vcs/vcs.go`

**Predicted Files (4):**
- ❌ `lib/time/mkzip.go`
- ❌ `src/time/format.go`
- ❌ `src/time/format_rfc3339.go`
- ❌ `src/time/time.go`

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

**Predicted Directories (3):**
- ❌ `src/cmd`
- ❌ `src/cmd/go/internal/doc`
- ❌ `src/go/doc`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/doc/main.go`
- `src/cmd/doc/pkg.go`

**Predicted Files (6):**
- ❌ `src/cmd/doc.go`
- ❌ `src/cmd/go/internal/doc/doc.go`
- ❌ `src/go/doc/comment.go`
- ❌ `src/go/doc/comment_test.go`
- ❌ `src/go/doc/doc.go`
- ❌ `src/go/doc/doc_test.go`

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
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/ed25519/ed25519.go`
- `src/crypto/ed25519/ed25519_test.go`

**Predicted Files (3):**
- ✅ `src/crypto/ed25519/ed25519.go`
- ✅ `src/crypto/ed25519/ed25519_test.go`
- ❌ `src/crypto/ed25519/ed25519vectors_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/ed25519`


### 📊 **Proposal #43744**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/runtime`
- `src/testing`
- `src/time`

**Predicted Directories (1):**
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/proc.go`
- `src/testing/benchmark_test.go`
- `src/time/sleep_test.go`

**Predicted Files (2):**
- ❌ `src/testing/benchmark.go`
- ✅ `src/testing/benchmark_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #47916**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/types2`
- `src/go/types`

**Predicted Directories (2):**
- ✅ `src/cmd/compile/internal/types2`
- ✅ `src/go/types`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.8% | 75.0% | 30.0% | 15/20 |

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

**Predicted Files (80):**
- ❌ `src/cmd/compile/internal/types2/alias.go`
- ❌ `src/cmd/compile/internal/types2/api.go`
- ❌ `src/cmd/compile/internal/types2/check.go`
- ❌ `src/cmd/compile/internal/types2/instantiate.go`
- ❌ `src/cmd/compile/internal/types2/interface.go`
- ❌ `src/cmd/compile/internal/types2/named.go`
- ❌ `src/cmd/compile/internal/types2/object.go`
- ✅ `src/cmd/compile/internal/types2/signature.go`
- ❌ `src/cmd/compile/internal/types2/type.go`
- ❌ `src/cmd/compile/internal/types2/typeparam.go`
- ❌ `src/go/types/alias.go`
- ❌ `src/go/types/api.go`
- ❌ `src/go/types/api_predicates.go`
- ❌ `src/go/types/array.go`
- ✅ `src/go/types/assignments.go`
- ❌ `src/go/types/basic.go`
- ❌ `src/go/types/builtins.go`
- ✅ `src/go/types/call.go`
- ❌ `src/go/types/chan.go`
- ✅ `src/go/types/check.go`
- ❌ `src/go/types/const.go`
- ✅ `src/go/types/context.go`
- ❌ `src/go/types/conversions.go`
- ✅ `src/go/types/decl.go`
- ❌ `src/go/types/errors.go`
- ❌ `src/go/types/eval.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/format.go`
- ❌ `src/go/types/gccgosizes.go`
- ❌ `src/go/types/gcsizes.go`
- ❌ `src/go/types/gotype.go`
- ✅ `src/go/types/index.go`
- ❌ `src/go/types/infer.go`
- ❌ `src/go/types/initorder.go`
- ✅ `src/go/types/instantiate.go`
- ❌ `src/go/types/interface.go`
- ❌ `src/go/types/iter.go`
- ❌ `src/go/types/labels.go`
- ❌ `src/go/types/literals.go`
- ✅ `src/go/types/lookup.go`
- ❌ `src/go/types/map.go`
- ❌ `src/go/types/methodset.go`
- ❌ `src/go/types/mono.go`
- ❌ `src/go/types/named.go`
- ✅ `src/go/types/object.go`
- ❌ `src/go/types/objset.go`
- ❌ `src/go/types/operand.go`
- ❌ `src/go/types/package.go`
- ❌ `src/go/types/pointer.go`
- ✅ `src/go/types/predicates.go`
- ❌ `src/go/types/range.go`
- ❌ `src/go/types/recording.go`
- ❌ `src/go/types/resolver.go`
- ❌ `src/go/types/return.go`
- ❌ `src/go/types/scope.go`
- ❌ `src/go/types/selection.go`
- ❌ `src/go/types/self_test.go`
- ✅ `src/go/types/signature.go`
- ❌ `src/go/types/sizes.go`
- ❌ `src/go/types/slice.go`
- ❌ `src/go/types/stmt.go`
- ❌ `src/go/types/struct.go`
- ✅ `src/go/types/subst.go`
- ❌ `src/go/types/termlist.go`
- ❌ `src/go/types/token_test.go`
- ❌ `src/go/types/tuple.go`
- ❌ `src/go/types/type.go`
- ✅ `src/go/types/typelists.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/go/types/typeset.go`
- ✅ `src/go/types/typestring.go`
- ❌ `src/go/types/typeterm.go`
- ❌ `src/go/types/typexpr.go`
- ❌ `src/go/types/under.go`
- ❌ `src/go/types/unify.go`
- ❌ `src/go/types/union.go`
- ❌ `src/go/types/universe.go`
- ❌ `src/go/types/util.go`
- ❌ `src/go/types/validtype.go`
- ❌ `src/go/types/version.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.8% | 75.0% | 30.0% | 15/20 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/compile/internal/types2`
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

**Predicted Directories (3):**
- ❌ `src/cmd/vet`
- ❌ `src/cmd/vet/testdata/stdmethods`
- ❌ `src/errors`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf/printf.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer/sigchanyzer.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods/stdmethods.go`

**Predicted Files (10):**
- ❌ `src/cmd/vet/testdata/stdmethods/doc.go`
- ❌ `src/cmd/vet/testdata/stdmethods/stdmethods.go`
- ❌ `src/cmd/vet/vet.go`
- ❌ `src/cmd/vet/vetflag.go`
- ❌ `src/errors/errors.go`
- ❌ `src/errors/errors_test.go`
- ❌ `src/errors/join.go`
- ❌ `src/errors/join_test.go`
- ❌ `src/errors/wrap.go`
- ❌ `src/errors/wrap_test.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (1):**
- ✅ `src/net/http/httputil`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/net/http/httputil/example_test.go`
- `src/net/http/httputil/reverseproxy.go`
- `src/net/http/httputil/reverseproxy_test.go`

**Predicted Files (2):**
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http/httputil`


### 📊 **Proposal #44196**

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
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/time.go`
- `src/time/time_test.go`

**Predicted Files (2):**
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
| 50.0% | 20.0% | 28.6% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/dist`
- `src/cmd/go`
- `src/cmd/go/internal/test`
- `src/cmd/go/internal/work`
- `src/cmd/link`

**Predicted Directories (2):**
- ✅ `src/cmd/go/internal/work`
- ❌ `src/cmd/link/internal/ld`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.6% | 14.3% | 8.0% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/test/test.go`
- `src/cmd/go/internal/test/testflag.go`
- `src/cmd/go/internal/work/build.go`
- `src/cmd/link/dwarf_test.go`

**Predicted Files (18):**
- ✅ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/build_test.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/exec_test.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`
- ❌ `src/cmd/go/internal/work/init.go`
- ❌ `src/cmd/go/internal/work/security.go`
- ❌ `src/cmd/go/internal/work/security_test.go`
- ❌ `src/cmd/go/internal/work/shell.go`
- ❌ `src/cmd/go/internal/work/shell_test.go`
- ❌ `src/cmd/link/internal/ld/go.go`
- ❌ `src/cmd/link/internal/ld/ld.go`
- ❌ `src/cmd/link/internal/ld/lib.go`
- ❌ `src/cmd/link/internal/ld/link.go`
- ❌ `src/cmd/link/internal/ld/main.go`
- ❌ `src/cmd/link/internal/ld/target.go`
- ❌ `src/cmd/link/internal/ld/util.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 14.3% | 11.1% | 1/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/work`


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
| 33.3% | 0.7% | 1.5% | 1/134 |

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

**Predicted Files (3):**
- ❌ `src/bytes/bytes.go`
- ✅ `src/strings/strings.go`
- ❌ `src/strings/strings_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 0.7% | 1.5% | 1/134 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/strings`


### 📊 **Proposal #44011**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/os`
- `src/os/exec`
- `src/syscall`

**Predicted Directories (1):**
- ✅ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 33.3% | 30.8% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/os/exec/exec_windows_test.go`
- `src/os/file_windows.go`
- `src/syscall/exec_windows.go`
- `src/syscall/exec_windows_test.go`
- `src/syscall/syscall_windows.go`
- `src/syscall/zsyscall_windows.go`

**Predicted Files (7):**
- ❌ `src/syscall/dll_windows.go`
- ❌ `src/syscall/env_windows.go`
- ❌ `src/syscall/security_windows.go`
- ✅ `src/syscall/syscall_windows.go`
- ❌ `src/syscall/syscall_windows_test.go`
- ❌ `src/syscall/zerrors_windows.go`
- ✅ `src/syscall/zsyscall_windows.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 33.3% | 30.8% | 2/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall`


### 📊 **Proposal #43620**

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
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/benchmark.go`
- `src/testing/benchmark_test.go`

**Predicted Files (2):**
- ✅ `src/testing/benchmark.go`
- ✅ `src/testing/benchmark_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #48256**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go`
- `src/cmd/go/internal/workcmd`

**Predicted Directories (1):**
- ✅ `src/cmd/go/internal/workcmd`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 66.7% | 44.4% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/workcmd/edit.go`
- `src/cmd/go/internal/workcmd/init.go`
- `src/cmd/go/main.go`

**Predicted Files (6):**
- ✅ `src/cmd/go/internal/workcmd/edit.go`
- ✅ `src/cmd/go/internal/workcmd/init.go`
- ❌ `src/cmd/go/internal/workcmd/sync.go`
- ❌ `src/cmd/go/internal/workcmd/use.go`
- ❌ `src/cmd/go/internal/workcmd/vendor.go`
- ❌ `src/cmd/go/internal/workcmd/work.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 66.7% | 44.4% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/workcmd`


### 📊 **Proposal #38017**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/time`
- `src/time/tzdata`

**Predicted Directories (3):**
- ❌ `lib/time`
- ✅ `src/time`
- ✅ `src/time/tzdata`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 50.0% | 57.1% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/time/export_test.go`
- `src/time/tzdata/tzdata.go`
- `src/time/tzdata_test.go`
- `src/time/zoneinfo_read.go`

**Predicted Files (3):**
- ❌ `lib/time/mkzip.go`
- ✅ `src/time/tzdata/tzdata.go`
- ✅ `src/time/tzdata_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/time`
- `src/time/tzdata`


### 📊 **Proposal #50601**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/binary`

**Predicted Directories (1):**
- ✅ `src/encoding/binary`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/binary/binary.go`
- `src/encoding/binary/binary_test.go`

**Predicted Files (2):**
- ✅ `src/encoding/binary/binary.go`
- ✅ `src/encoding/binary/binary_test.go`

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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (2):**
- ❌ `src/bytes`
- ✅ `src/io`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/io/io.go`
- `src/io/multi.go`
- `src/io/multi_test.go`

**Predicted Files (4):**
- ❌ `src/bytes/buffer.go`
- ❌ `src/bytes/reader.go`
- ✅ `src/io/multi.go`
- ✅ `src/io/multi_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io`


### 📊 **Proposal #41790**

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
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/database/sql/fakedb_test.go`
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`

**Predicted Files (3):**
- ❌ `src/database/sql/driver/driver.go`
- ✅ `src/database/sql/sql.go`
- ✅ `src/database/sql/sql_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/database/sql`


### 📊 **Proposal #5901**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/json`

**Predicted Directories (1):**
- ✅ `src/encoding/json`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/encoding/json/bench_test.go`
- `src/encoding/json/decode.go`
- `src/encoding/json/encode.go`
- `src/encoding/json/stream.go`

**Predicted Files (4):**
- ✅ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ✅ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encode_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/json`


### 📊 **Proposal #52792**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modload`

**Predicted Directories (1):**
- ❌ `src/cmd/go/internal/modinfo`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modfetch/fetch.go`
- `src/cmd/go/internal/modload/build.go`

**Predicted Files (1):**
- ❌ `src/cmd/go/internal/modinfo/info.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #28308**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 8.7% | 14.3% | 2/23 |

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

**Predicted Directories (5):**
- ✅ `src/cmd/vet`
- ✅ `src/cmd/vet/testdata/hostport`
- ❌ `src/fmt`
- ❌ `src/golang.org/x/tools/go/analysis/passes/hostport`
- ❌ `src/net`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 2.9% | 4.3% | 1/34 |

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

**Predicted Files (12):**
- ✅ `src/cmd/vet/testdata/hostport/hostport.go`
- ❌ `src/cmd/vet/vet.go`
- ❌ `src/cmd/vet/vetflag.go`
- ❌ `src/fmt/fmt_test.go`
- ❌ `src/fmt/format.go`
- ❌ `src/fmt/print.go`
- ❌ `src/fmt/scan.go`
- ❌ `src/golang.org/x/tools/go/analysis/passes/hostport/hostport.go`
- ❌ `src/net/dial.go`
- ❌ `src/net/dial_test.go`
- ❌ `src/net/net.go`
- ❌ `src/net/net_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 2.9% | 5.4% | 1/34 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/vet`
- `src/cmd/vet/testdata/hostport`


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
- ❌ `src/syscall/js/export_test.go`
- ❌ `src/syscall/js/func.go`
- ✅ `src/syscall/js/js.go`
- ❌ `src/syscall/js/js_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall/js`


### 📊 **Proposal #53021**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/cipher`
- `src/crypto/subtle`

**Predicted Directories (1):**
- ✅ `src/crypto/subtle`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 16.7% | 20.0% | 1/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/crypto/cipher/cbc.go`
- `src/crypto/cipher/cfb.go`
- `src/crypto/cipher/ctr.go`
- `src/crypto/cipher/ofb.go`
- `src/crypto/subtle/xor.go`
- `src/crypto/subtle/xor_test.go`

**Predicted Files (4):**
- ✅ `src/crypto/subtle/xor.go`
- ❌ `src/crypto/subtle/xor_asm.go`
- ❌ `src/crypto/subtle/xor_generic.go`
- ❌ `src/crypto/subtle/xor_loong64.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 16.7% | 20.0% | 1/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/subtle`


### 📊 **Proposal #49580**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 25.0% | 40.0% | 1/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `src/archive/tar`
- `src/io/fs`
- `src/os`
- `src/testing/fstest`

**Predicted Directories (1):**
- ✅ `src/io/fs`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 14.3% | 25.0% | 2/14 |

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

**Predicted Files (2):**
- ✅ `src/io/fs/readlink.go`
- ✅ `src/io/fs/readlink_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 14.3% | 25.0% | 2/14 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io/fs`


### 📊 **Proposal #53015**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/html/template`
- `src/text/template`
- `src/text/template/parse`

**Predicted Directories (1):**
- ✅ `src/text/template`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 14.3% | 20.0% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/html/template/escape.go`
- `src/html/template/escape_test.go`
- `src/text/template/exec.go`
- `src/text/template/parse/lex.go`
- `src/text/template/parse/lex_test.go`
- `src/text/template/parse/node.go`
- `src/text/template/parse/parse.go`

**Predicted Files (3):**
- ✅ `src/text/template/exec.go`
- ❌ `src/text/template/exec_test.go`
- ❌ `src/text/template/template.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 14.3% | 20.0% | 1/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/text/template`


### 📊 **Proposal #41048**

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
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/transport.go`
- `src/net/http/transport_test.go`

**Predicted Files (2):**
- ✅ `src/net/http/transport.go`
- ✅ `src/net/http/transport_test.go`

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
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/runtime`
- `src/runtime/debug`
- `src/runtime/testdata/testprog`

**Predicted Directories (1):**
- ✅ `src/runtime/debug`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 3.6% | 6.7% | 1/28 |

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

**Predicted Files (2):**
- ✅ `src/runtime/debug/garbage.go`
- ❌ `src/runtime/debug/garbage_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 3.6% | 6.7% | 1/28 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
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
| 100.0% | 33.3% | 50.0% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/time/format.go`
- `src/time/time.go`
- `src/time/time_test.go`
- `src/time/zoneinfo.go`
- `src/time/zoneinfo_read.go`
- `src/time/zoneinfo_test.go`

**Predicted Files (2):**
- ✅ `src/time/zoneinfo.go`
- ✅ `src/time/zoneinfo_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 2/6 |

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
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/match.go`
- `src/testing/match_test.go`

**Predicted Files (2):**
- ✅ `src/testing/match.go`
- ✅ `src/testing/match_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #42027**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 13.3% | 23.5% | 2/15 |

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

**Predicted Directories (2):**
- ✅ `src/io/fs`
- ✅ `src/path/filepath`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 22.2% | 25.0% | 4/18 |

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

**Predicted Files (14):**
- ✅ `src/io/fs/walk.go`
- ✅ `src/io/fs/walk_test.go`
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
| 28.6% | 22.2% | 25.0% | 4/18 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/io/fs`
- `src/path/filepath`


### 📊 **Proposal #27628**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/cache`
- `src/cmd/go/internal/work`

**Predicted Directories (2):**
- ✅ `src/cmd/go/internal/work`
- ❌ `src/cmd/link/internal/ld`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 21.1% | 80.0% | 33.3% | 4/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/go/internal/cache/hash.go`
- `src/cmd/go/internal/work/buildid.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/go/internal/work/gc.go`
- `src/cmd/go/internal/work/gccgo.go`

**Predicted Files (19):**
- ❌ `src/cmd/go/internal/work/action.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/build_test.go`
- ✅ `src/cmd/go/internal/work/buildid.go`
- ✅ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/exec_test.go`
- ✅ `src/cmd/go/internal/work/gc.go`
- ✅ `src/cmd/go/internal/work/gccgo.go`
- ❌ `src/cmd/go/internal/work/init.go`
- ❌ `src/cmd/go/internal/work/security.go`
- ❌ `src/cmd/go/internal/work/security_test.go`
- ❌ `src/cmd/go/internal/work/shell.go`
- ❌ `src/cmd/go/internal/work/shell_test.go`
- ❌ `src/cmd/link/internal/ld/go.go`
- ❌ `src/cmd/link/internal/ld/go_test.go`
- ❌ `src/cmd/link/internal/ld/ld.go`
- ❌ `src/cmd/link/internal/ld/ld_test.go`
- ❌ `src/cmd/link/internal/ld/link.go`
- ❌ `src/cmd/link/internal/ld/main.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.8% | 80.0% | 44.4% | 4/5 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/work`


### 📊 **Proposal #51868**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/debug/pe`

**Predicted Directories (1):**
- ✅ `src/debug/pe`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/debug/pe/symbol.go`
- `src/debug/pe/symbols_test.go`

**Predicted Files (4):**
- ❌ `src/debug/pe/file.go`
- ❌ `src/debug/pe/pe.go`
- ❌ `src/debug/pe/section.go`
- ✅ `src/debug/pe/symbol.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/ast`

**Predicted Directories (1):**
- ✅ `src/go/ast`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/ast/ast.go`
- `src/go/ast/issues_test.go`

**Predicted Files (2):**
- ✅ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`

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
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/x509/parser.go`
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (3):**
- ✅ `src/crypto/x509/parser.go`
- ❌ `src/crypto/x509/pkix/pkix.go`
- ✅ `src/crypto/x509/x509.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

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
| 64.3% | 42.9% | 51.4% | 9/21 |

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

**Predicted Files (14):**
- ❌ `src/internal/poll/sock_cloexec.go`
- ❌ `src/runtime/internal/atomic/sys_linux_arm.s`
- ✅ `src/syscall/exec_linux.go`
- ✅ `src/syscall/syscall_linux.go`
- ❌ `src/syscall/syscall_linux_386.go`
- ✅ `src/syscall/syscall_linux_amd64.go`
- ✅ `src/syscall/syscall_linux_arm.go`
- ❌ `src/syscall/syscall_linux_arm64.go`
- ❌ `src/syscall/syscall_linux_loong64.go`
- ✅ `src/syscall/syscall_linux_mips64x.go`
- ✅ `src/syscall/syscall_linux_mipsx.go`
- ✅ `src/syscall/syscall_linux_ppc64x.go`
- ✅ `src/syscall/syscall_linux_riscv64.go`
- ✅ `src/syscall/syscall_linux_s390x.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 42.9% | 54.5% | 9/21 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/syscall`


### 📊 **Proposal #39444**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os`

**Predicted Directories (2):**
- ✅ `src/os`
- ❌ `src/os/exec`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/os/exec_unix.go`
- `src/os/exec_unix_test.go`

**Predicted Files (3):**
- ❌ `src/os/exec/exec_unix.go`
- ✅ `src/os/exec_unix.go`
- ✅ `src/os/exec_unix_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/os`


### 📊 **Proposal #45430**

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
| 66.7% | 25.0% | 36.4% | 2/8 |

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

**Predicted Files (3):**
- ✅ `src/crypto/tls/cipher_suites.go`
- ✅ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/tls.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 25.0% | 36.4% | 2/8 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #37533**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (3):**
- ❌ `src/cmd/gofmt`
- ❌ `src/cmd/internal/objabi`
- ✅ `src/flag`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (6):**
- ❌ `src/cmd/gofmt/gofmt.go`
- ❌ `src/cmd/gofmt/gofmt_test.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`

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
| 50.0% | 20.0% | 28.6% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/cgo`
- `src/go/ast`
- `src/go/parser`
- `src/go/printer`
- `src/go/types`

**Predicted Directories (2):**
- ✅ `src/go/ast`
- ❌ `src/go/token`

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

**Predicted Files (4):**
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`
- ❌ `src/go/token/token.go`
- ❌ `src/go/token/token_test.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (1):**
- ✅ `src/crypto/x509`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/cert_pool.go`
- `src/crypto/x509/cert_pool_test.go`

**Predicted Files (2):**
- ✅ `src/crypto/x509/cert_pool.go`
- ✅ `src/crypto/x509/cert_pool_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #43401**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/csv`

**Predicted Directories (1):**
- ✅ `src/encoding/csv`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/csv/reader.go`
- `src/encoding/csv/reader_test.go`

**Predicted Files (2):**
- ✅ `src/encoding/csv/reader.go`
- ✅ `src/encoding/csv/reader_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/csv`


### 📊 **Proposal #40728**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 14.3% | 25.0% | 1/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/go/internal/base`
- `src/cmd/go/internal/fmtcmd`
- `src/cmd/go/internal/list`
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modget`
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/work`

**Predicted Directories (1):**
- ✅ `src/cmd/go/internal/modload`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 63.6% | 29.2% | 40.0% | 7/24 |

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

**Predicted Files (11):**
- ✅ `src/cmd/go/internal/modload/import.go`
- ❌ `src/cmd/go/internal/modload/import_test.go`
- ❌ `src/cmd/go/internal/modload/list.go`
- ✅ `src/cmd/go/internal/modload/load.go`
- ✅ `src/cmd/go/internal/modload/modfile.go`
- ✅ `src/cmd/go/internal/modload/mvs.go`
- ❌ `src/cmd/go/internal/modload/mvs_test.go`
- ✅ `src/cmd/go/internal/modload/query.go`
- ✅ `src/cmd/go/internal/modload/query_test.go`
- ✅ `src/cmd/go/internal/modload/search.go`
- ❌ `src/cmd/go/internal/modload/vendor.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 63.6% | 29.2% | 40.0% | 7/24 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/modload`


### 📊 **Proposal #43993**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/reflect`
- `src/text/template`

**Predicted Directories (2):**
- ❌ `src/cmd/vet`
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 25.0% | 18.2% | 1/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`
- `src/text/template/exec.go`
- `src/text/template/funcs.go`

**Predicted Files (7):**
- ❌ `src/cmd/vet/doc.go`
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/vet.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/cmd/vet/vetflag.go`
- ❌ `src/reflect/deepequal.go`
- ✅ `src/reflect/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 25.0% | 33.3% | 1/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #50770**

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
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/mono_test.go`
- `src/time/time.go`

**Predicted Files (3):**
- ❌ `lib/time/mkzip.go`
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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/csv`

**Predicted Directories (1):**
- ✅ `src/encoding/csv`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/csv/reader.go`
- `src/encoding/csv/reader_test.go`

**Predicted Files (2):**
- ✅ `src/encoding/csv/reader.go`
- ✅ `src/encoding/csv/reader_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

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

**Predicted Directories (0):**

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/http/socks_bundle.go`

**Predicted Files (0):**

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
| 66.7% | 33.3% | 44.4% | 2/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/cmd/compile/internal/gc`
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/staticdata`
- `src/cmd/dist`
- `src/embed/internal/embedtest`
- `src/go/types`

**Predicted Directories (3):**
- ✅ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/types2`
- ✅ `src/go/types`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 4.2% | 16.7% | 6.7% | 1/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/cmd/compile/internal/gc/main.go`
- `src/cmd/compile/internal/noder/noder.go`
- `src/cmd/compile/internal/staticdata/embed.go`
- `src/cmd/dist/test.go`
- `src/embed/internal/embedtest/embed_test.go`
- `src/go/types/stdlib_test.go`

**Predicted Files (24):**
- ❌ `src/cmd/compile/internal/gc/compile.go`
- ❌ `src/cmd/compile/internal/gc/export.go`
- ✅ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/gc/obj.go`
- ❌ `src/cmd/compile/internal/gc/util.go`
- ❌ `src/cmd/compile/internal/types2/typeparam.go`
- ❌ `src/cmd/compile/internal/types2/typeset.go`
- ❌ `src/cmd/compile/internal/types2/typeset_test.go`
- ❌ `src/cmd/compile/internal/types2/typestring.go`
- ❌ `src/cmd/compile/internal/types2/typestring_test.go`
- ❌ `src/cmd/compile/internal/types2/typeterm.go`
- ❌ `src/cmd/compile/internal/types2/typeterm_test.go`
- ❌ `src/cmd/compile/internal/types2/typexpr.go`
- ❌ `src/cmd/compile/internal/types2/unify.go`
- ❌ `src/cmd/compile/internal/types2/union.go`
- ❌ `src/cmd/compile/internal/types2/universe.go`
- ❌ `src/cmd/compile/internal/types2/util.go`
- ❌ `src/cmd/compile/internal/types2/util_test.go`
- ❌ `src/cmd/compile/internal/types2/validtype.go`
- ❌ `src/cmd/compile/internal/types2/version.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/go/types/types.go`
- ❌ `src/go/types/types_test.go`
- ❌ `src/go/types/typexpr.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 16.7% | 13.3% | 1/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/compile/internal/gc`
- `src/go/types`


### 📊 **Proposal #48294**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/reflect/all_test.go`

**Predicted Files (3):**
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`
- ❌ `src/reflect/value.go`

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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (2):**
- ✅ `src/net`
- ❌ `src/syscall`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/error_test.go`
- `src/net/net.go`

**Predicted Files (2):**
- ✅ `src/net/net.go`
- ❌ `src/syscall/net.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #52463**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/gofmt`

**Predicted Directories (3):**
- ❌ `src/cmd/go`
- ✅ `src/cmd/gofmt`
- ❌ `src/go/ast`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 100.0% | 44.4% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/gofmt/gofmt.go`
- `src/cmd/gofmt/simplify.go`

**Predicted Files (7):**
- ❌ `src/cmd/go/ast.go`
- ✅ `src/cmd/gofmt/gofmt.go`
- ❌ `src/cmd/gofmt/rewrite.go`
- ✅ `src/cmd/gofmt/simplify.go`
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`
- ❌ `src/go/ast/scope.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/gofmt`


### 📊 **Proposal #51115**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (3):**
- ❌ `src/bytes`
- ✅ `src/io`
- ❌ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/io/io.go`

**Predicted Files (6):**
- ❌ `src/bytes/reader.go`
- ❌ `src/bytes/reader_test.go`
- ✅ `src/io/io.go`
- ❌ `src/io/io_test.go`
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
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/go/build`
- `src/runtime/debug`
- `src/testing`

**Predicted Directories (2):**
- ✅ `src/testing`
- ❌ `src/testing/internal/testdeps`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 60.0% | 66.7% | 3/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/go/build/deps_test.go`
- `src/runtime/debug/stack_test.go`
- `src/testing/benchmark.go`
- `src/testing/example.go`
- `src/testing/testing.go`

**Predicted Files (4):**
- ✅ `src/testing/benchmark.go`
- ✅ `src/testing/example.go`
- ❌ `src/testing/internal/testdeps/deps.go`
- ✅ `src/testing/testing.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 60.0% | 75.0% | 3/5 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing`


### 📊 **Proposal #40255**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 22.2% | 30.8% | 2/9 |

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

**Predicted Directories (4):**
- ✅ `src/cmd/compile/internal/ssa`
- ✅ `src/cmd/compile/internal/x86`
- ❌ `src/cmd/internal/sys`
- ❌ `src/cmd/link/internal/ld`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 6.7% | 7.4% | 1/15 |

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

**Predicted Files (12):**
- ✅ `src/cmd/compile/internal/ssa/rewrite386.go`
- ❌ `src/cmd/compile/internal/ssa/rewrite386splitload.go`
- ❌ `src/cmd/compile/internal/ssa/softfloat.go`
- ❌ `src/cmd/compile/internal/x86/asm6.go`
- ❌ `src/cmd/internal/sys/arch.go`
- ❌ `src/cmd/link/internal/ld/config.go`
- ❌ `src/cmd/link/internal/ld/ld.go`
- ❌ `src/cmd/link/internal/ld/lib.go`
- ❌ `src/cmd/link/internal/ld/link.go`
- ❌ `src/cmd/link/internal/ld/sym.go`
- ❌ `src/cmd/link/internal/ld/symtab.go`
- ❌ `src/cmd/link/internal/ld/target.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 6.7% | 10.5% | 1/15 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/compile/internal/ssa`
- `src/cmd/compile/internal/x86`


### 📊 **Proposal #46648**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/types`

**Predicted Directories (2):**
- ❌ `src/cmd/compile/internal/types2`
- ✅ `src/go/types`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.7% | 66.7% | 7.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/go/types/check.go`
- `src/go/types/check_test.go`
- `src/go/types/stdlib_test.go`

**Predicted Files (54):**
- ❌ `src/cmd/compile/internal/types2/check.go`
- ❌ `src/cmd/compile/internal/types2/version.go`
- ❌ `src/go/types/api.go`
- ✅ `src/go/types/check.go`
- ✅ `src/go/types/check_test.go`
- ❌ `src/go/types/context.go`
- ❌ `src/go/types/context_test.go`
- ❌ `src/go/types/errors.go`
- ❌ `src/go/types/errors_test.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/exprstring.go`
- ❌ `src/go/types/exprstring_test.go`
- ❌ `src/go/types/format.go`
- ❌ `src/go/types/gotype.go`
- ❌ `src/go/types/instantiate.go`
- ❌ `src/go/types/instantiate_test.go`
- ❌ `src/go/types/interface.go`
- ❌ `src/go/types/lookup.go`
- ❌ `src/go/types/lookup_test.go`
- ❌ `src/go/types/object.go`
- ❌ `src/go/types/object_test.go`
- ❌ `src/go/types/operand.go`
- ❌ `src/go/types/package.go`
- ❌ `src/go/types/predicates.go`
- ❌ `src/go/types/recording.go`
- ❌ `src/go/types/selection.go`
- ❌ `src/go/types/signature.go`
- ❌ `src/go/types/sizes.go`
- ❌ `src/go/types/sizes_test.go`
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

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.8% | 66.7% | 7.3% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/go/types`


### 📊 **Proposal #53346**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/xml`

**Predicted Directories (1):**
- ✅ `src/encoding/xml`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/xml/marshal.go`
- `src/encoding/xml/marshal_test.go`

**Predicted Files (2):**
- ❌ `src/encoding/xml/xml.go`
- ❌ `src/encoding/xml/xml_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/xml`


### 📊 **Proposal #40127**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/json`

**Predicted Directories (1):**
- ✅ `src/encoding/json`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/json/indent.go`
- `src/encoding/json/stream.go`

**Predicted Files (4):**
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encode_test.go`
- ✅ `src/encoding/json/stream.go`
- ❌ `src/encoding/json/stream_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/json`


### 📊 **Proposal #51082**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 3.1% | 5.6% | 2/65 |

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

**Predicted Directories (6):**
- ❌ `src/cmd`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/doc`
- ❌ `src/cmd/gofmt`
- ✅ `src/go/doc/comment`
- ✅ `src/go/printer`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 5.6% | 10.1% | 7/125 |

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

**Predicted Files (14):**
- ❌ `src/cmd/doc.go`
- ❌ `src/cmd/go/doc.go`
- ❌ `src/cmd/go/internal/doc/doc.go`
- ❌ `src/cmd/gofmt/doc.go`
- ❌ `src/cmd/gofmt/gofmt.go`
- ❌ `src/go/doc/comment/doc.go`
- ✅ `src/go/doc/comment/html.go`
- ✅ `src/go/doc/comment/markdown.go`
- ✅ `src/go/doc/comment/parse.go`
- ❌ `src/go/doc/comment/parse_test.go`
- ✅ `src/go/doc/comment/print.go`
- ✅ `src/go/printer/comment.go`
- ✅ `src/go/printer/printer.go`
- ✅ `src/go/printer/printer_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 77.8% | 5.6% | 10.4% | 7/125 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/go/doc/comment`
- `src/go/printer`


### 📊 **Proposal #35833**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 20.0% | 33.3% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/crypto/elliptic`
- `src/crypto/rand`
- `src/crypto/rsa`
- `src/crypto/x509`
- `src/math/big`

**Predicted Directories (1):**
- ✅ `src/math/big`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 28.6% | 44.4% | 2/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/crypto/elliptic/elliptic.go`
- `src/crypto/rand/util.go`
- `src/crypto/rsa/pkcs1v15.go`
- `src/crypto/x509/sec1.go`
- `src/math/big/int.go`
- `src/math/big/int_test.go`
- `src/math/big/nat.go`

**Predicted Files (2):**
- ✅ `src/math/big/int.go`
- ✅ `src/math/big/int_test.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/http/transport.go`

**Predicted Files (1):**
- ✅ `src/net/http/transport.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http`


### 📊 **Proposal #42387**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io/fs`

**Predicted Directories (1):**
- ✅ `src/io/fs`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/io/fs/readdir.go`
- `src/io/fs/readdir_test.go`

**Predicted Files (4):**
- ❌ `src/io/fs/fs.go`
- ❌ `src/io/fs/fs_test.go`
- ✅ `src/io/fs/readdir.go`
- ✅ `src/io/fs/readdir_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/io/fs`


### 📊 **Proposal #45454**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/cfg`
- `src/go/build`
- `src/internal/buildcfg`

**Predicted Directories (4):**
- ❌ `src/cmd/asm/internal/arch`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/sys`
- ❌ `src/internal/goarch`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/cfg/cfg.go`
- `src/go/build/build.go`
- `src/internal/buildcfg/cfg.go`

**Predicted Files (27):**
- ❌ `src/cmd/asm/internal/arch/amd64.go`
- ❌ `src/cmd/asm/internal/arch/arm.go`
- ❌ `src/cmd/asm/internal/arch/arm64.go`
- ❌ `src/cmd/asm/internal/arch/loong64.go`
- ❌ `src/cmd/asm/internal/arch/mips.go`
- ❌ `src/cmd/asm/internal/arch/ppc64.go`
- ❌ `src/cmd/asm/internal/arch/riscv64.go`
- ❌ `src/cmd/asm/internal/arch/s390x.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ❌ `src/cmd/internal/sys/arch.go`
- ❌ `src/cmd/internal/sys/arch_test.go`
- ❌ `src/internal/goarch/goarch.go`
- ❌ `src/internal/goarch/goarch_386.go`
- ❌ `src/internal/goarch/goarch_amd64.go`
- ❌ `src/internal/goarch/goarch_arm.go`
- ❌ `src/internal/goarch/goarch_arm64.go`
- ❌ `src/internal/goarch/goarch_loong64.go`
- ❌ `src/internal/goarch/goarch_mips.go`
- ❌ `src/internal/goarch/goarch_mips64.go`
- ❌ `src/internal/goarch/goarch_mips64le.go`
- ❌ `src/internal/goarch/goarch_mipsle.go`
- ❌ `src/internal/goarch/goarch_ppc64.go`
- ❌ `src/internal/goarch/goarch_ppc64le.go`
- ❌ `src/internal/goarch/goarch_riscv64.go`
- ❌ `src/internal/goarch/goarch_s390x.go`
- ❌ `src/internal/goarch/goarch_wasm.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


### 📊 **Proposal #50436**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os/exec`

**Predicted Directories (2):**
- ❌ `src/cmd/go`
- ✅ `src/os/exec`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/os/exec/exec.go`
- `src/os/exec/exec_test.go`

**Predicted Files (5):**
- ❌ `src/cmd/go/script_test.go`
- ✅ `src/os/exec/exec.go`
- ✅ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/exec_unix.go`
- ❌ `src/os/exec/exec_windows.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/os/exec`


### 📊 **Proposal #44167**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (1):**
- ✅ `src/runtime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 42.9% | 60.0% | 6/14 |

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

**Predicted Files (6):**
- ✅ `src/runtime/mgc.go`
- ✅ `src/runtime/mgcmark.go`
- ✅ `src/runtime/mgcpacer.go`
- ✅ `src/runtime/mgcpacer_test.go`
- ✅ `src/runtime/mgcsweep.go`
- ✅ `src/runtime/mgcwork.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 42.9% | 60.0% | 6/14 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/runtime`


### 📊 **Proposal #39178**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (1):**
- ✅ `src/net`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/lookup.go`
- `src/net/lookup_test.go`

**Predicted Files (2):**
- ✅ `src/net/lookup.go`
- ✅ `src/net/lookup_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #46287**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 25.0% | 40.0% | 1/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `src/cmd/dist`
- `src/crypto/x509`
- `src/crypto/x509/internal/macos`
- `src/runtime`

**Predicted Directories (1):**
- ✅ `src/crypto/x509`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 80.0% | 36.4% | 50.0% | 4/11 |

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

**Predicted Files (5):**
- ✅ `src/crypto/x509/cert_pool.go`
- ✅ `src/crypto/x509/root_darwin.go`
- ❌ `src/crypto/x509/root_unix.go`
- ✅ `src/crypto/x509/root_windows.go`
- ✅ `src/crypto/x509/verify.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 80.0% | 36.4% | 50.0% | 4/11 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/x509`


### 📊 **Proposal #48257**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/go/internal/workcmd`

**Predicted Directories (1):**
- ✅ `src/cmd/go/internal/workcmd`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/cmd/go/internal/workcmd/use.go`

**Predicted Files (1):**
- ✅ `src/cmd/go/internal/workcmd/use.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/workcmd`


### 📊 **Proposal #46293**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/reflect/all_test.go`

**Predicted Files (2):**
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`

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
| 66.7% | 2.2% | 4.3% | 2/90 |

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

**Predicted Directories (3):**
- ❌ `src/io/fs`
- ✅ `src/io/ioutil`
- ✅ `src/os`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 54.5% | 3.1% | 5.9% | 6/194 |

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

**Predicted Files (11):**
- ❌ `src/io/fs/readdir.go`
- ❌ `src/io/fs/readdir_test.go`
- ❌ `src/io/fs/readfile.go`
- ❌ `src/io/fs/readfile_test.go`
- ✅ `src/io/ioutil/ioutil.go`
- ❌ `src/io/ioutil/ioutil_test.go`
- ✅ `src/io/ioutil/tempfile.go`
- ✅ `src/io/ioutil/tempfile_test.go`
- ✅ `src/os/dir.go`
- ✅ `src/os/file.go`
- ✅ `src/os/tempfile.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 85.7% | 3.1% | 6.0% | 6/194 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/io/ioutil`
- `src/os`


### 📊 **Proposal #45435**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/sync`

**Predicted Directories (3):**
- ❌ `src/internal/sync`
- ❌ `src/net/http`
- ✅ `src/sync`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/sync/mutex.go`
- `src/sync/mutex_test.go`
- `src/sync/rwmutex.go`
- `src/sync/rwmutex_test.go`

**Predicted Files (4):**
- ❌ `src/internal/sync/mutex.go`
- ❌ `src/net/http/h2_bundle.go`
- ✅ `src/sync/mutex.go`
- ✅ `src/sync/mutex_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/sync`


### 📊 **Proposal #48187**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/version`
- `src/debug/buildinfo`

**Predicted Directories (2):**
- ✅ `src/cmd/go/internal/version`
- ✅ `src/debug/buildinfo`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/version/version.go`
- `src/debug/buildinfo/buildinfo_test.go`

**Predicted Files (4):**
- ✅ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/go/internal/version/version_test.go`
- ❌ `src/debug/buildinfo/buildinfo.go`
- ✅ `src/debug/buildinfo/buildinfo_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/go/internal/version`
- `src/debug/buildinfo`


### 📊 **Proposal #37519**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modget`

**Predicted Directories (2):**
- ❌ `src/cmd/go/internal/get`
- ✅ `src/cmd/go/internal/modget`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/modfetch/repo.go`
- `src/cmd/go/internal/modfetch/sumdb.go`
- `src/cmd/go/internal/modget/get.go`

**Predicted Files (2):**
- ❌ `src/cmd/go/internal/get/get.go`
- ✅ `src/cmd/go/internal/modget/get.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/modget`


### 📊 **Proposal #38627**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/text/template/parse`

**Predicted Directories (1):**
- ✅ `src/text/template/parse`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/text/template/parse/parse.go`

**Predicted Files (2):**
- ✅ `src/text/template/parse/parse.go`
- ❌ `src/text/template/parse/parse_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/text/template/parse`


### 📊 **Proposal #41260**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (3):**
- ❌ `src/os`
- ❌ `src/os/exec`
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/testing.go`
- `src/testing/testing_test.go`

**Predicted Files (5):**
- ❌ `src/os/env.go`
- ❌ `src/os/env_test.go`
- ❌ `src/os/exec/env_test.go`
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
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/asm/internal/lex`
- `src/cmd/dist`
- `src/sort`

**Predicted Directories (1):**
- ✅ `src/cmd/dist`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 66.7% | 28.6% | 4/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/cmd/asm/internal/lex/tokenizer.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/buildtool.go`
- `src/cmd/dist/test.go`
- `src/cmd/dist/util.go`
- `src/sort/slice.go`

**Predicted Files (22):**
- ✅ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/build_test.go`
- ❌ `src/cmd/dist/buildgo.go`
- ❌ `src/cmd/dist/buildruntime.go`
- ❌ `src/cmd/dist/buildtag.go`
- ❌ `src/cmd/dist/buildtag_test.go`
- ✅ `src/cmd/dist/buildtool.go`
- ❌ `src/cmd/dist/doc.go`
- ❌ `src/cmd/dist/exec.go`
- ❌ `src/cmd/dist/imports.go`
- ❌ `src/cmd/dist/main.go`
- ❌ `src/cmd/dist/notgo122.go`
- ❌ `src/cmd/dist/quoted.go`
- ❌ `src/cmd/dist/supported_test.go`
- ❌ `src/cmd/dist/sys_default.go`
- ❌ `src/cmd/dist/sys_windows.go`
- ✅ `src/cmd/dist/test.go`
- ❌ `src/cmd/dist/testjson.go`
- ❌ `src/cmd/dist/testjson_test.go`
- ✅ `src/cmd/dist/util.go`
- ❌ `src/cmd/dist/util_gc.go`
- ❌ `src/cmd/dist/util_gccgo.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 66.7% | 28.6% | 4/6 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/dist`


### 📊 **Proposal #50429**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/parser`

**Predicted Directories (2):**
- ❌ `src/cmd/compile/internal/syntax`
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
- ❌ `src/cmd/compile/internal/syntax/nodes.go`
- ❌ `src/cmd/compile/internal/syntax/parser.go`
- ❌ `src/cmd/compile/internal/syntax/positions.go`
- ❌ `src/go/ast/ast.go`
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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (2):**
- ❌ `src/net/http`
- ✅ `src/net/url`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/url/url.go`
- `src/net/url/url_test.go`

**Predicted Files (5):**
- ❌ `src/net/http/url.go`
- ❌ `src/net/http/url_test.go`
- ❌ `src/net/url/example_test.go`
- ✅ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/url`


### 📊 **Proposal #42681**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 20.0% | 25.0% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/asm/internal/lex`
- `src/cmd/dist`
- `src/cmd/go/internal/work`
- `src/cmd/link/internal/ld`
- `src/runtime`

**Predicted Directories (3):**
- ✅ `src/cmd/go/internal/work`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/internal/goexperiment`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.9% | 14.3% | 8.3% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/asm/internal/lex/input.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/buildruntime.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/go/internal/work/gc.go`
- `src/cmd/link/internal/ld/main.go`
- `src/runtime/heapdump.go`

**Predicted Files (17):**
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/build_test.go`
- ✅ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`
- ❌ `src/cmd/go/internal/work/init.go`
- ❌ `src/cmd/internal/objabi/util.go`
- ❌ `src/internal/goexperiment/exp_fieldtrack_off.go`
- ❌ `src/internal/goexperiment/exp_fieldtrack_on.go`
- ❌ `src/internal/goexperiment/exp_preemptibleloops_off.go`
- ❌ `src/internal/goexperiment/exp_preemptibleloops_on.go`
- ❌ `src/internal/goexperiment/exp_regabiargs_off.go`
- ❌ `src/internal/goexperiment/exp_regabiargs_on.go`
- ❌ `src/internal/goexperiment/exp_regabiwrappers_off.go`
- ❌ `src/internal/goexperiment/exp_regabiwrappers_on.go`
- ❌ `src/internal/goexperiment/exp_staticlockranking_off.go`
- ❌ `src/internal/goexperiment/exp_staticlockranking_on.go`
- ❌ `src/internal/goexperiment/flags.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 14.3% | 16.7% | 1/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/cmd/go/internal/work`


### 📊 **Proposal #40592**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/encoding/json`
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/encoding/json/encode.go`
- `src/reflect/all_test.go`
- `src/reflect/deepequal.go`
- `src/reflect/set_test.go`
- `src/reflect/type.go`
- `src/reflect/value.go`

**Predicted Files (2):**
- ✅ `src/reflect/type.go`
- ✅ `src/reflect/value.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/binary`

**Predicted Directories (1):**
- ✅ `src/encoding/binary`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/binary/varint.go`
- `src/encoding/binary/varint_test.go`

**Predicted Files (2):**
- ❌ `src/encoding/binary/binary.go`
- ✅ `src/encoding/binary/varint.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

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

**Predicted Directories (0):**

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

**Predicted Files (0):**

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/xml`

**Predicted Directories (1):**
- ✅ `src/encoding/xml`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/xml/xml.go`
- `src/encoding/xml/xml_test.go`

**Predicted Files (4):**
- ❌ `src/encoding/xml/read.go`
- ❌ `src/encoding/xml/read_test.go`
- ✅ `src/encoding/xml/xml.go`
- ✅ `src/encoding/xml/xml_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/encoding/xml`


### 📊 **Proposal #46746**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (1):**
- ✅ `src/reflect/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #44940**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/unicode/utf16`

**Predicted Directories (1):**
- ✅ `src/unicode/utf16`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/unicode/utf16/utf16.go`
- `src/unicode/utf16/utf16_test.go`

**Predicted Files (2):**
- ✅ `src/unicode/utf16/utf16.go`
- ✅ `src/unicode/utf16/utf16_test.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/tls/conn.go`
- `src/crypto/tls/tls_test.go`

**Predicted Files (2):**
- ✅ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/tls.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #41184**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 25.0% | 33.3% | 4/16 |

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

**Predicted Directories (8):**
- ❌ `src/cmd/go/internal/imports`
- ✅ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modload`
- ✅ `src/cmd/go/internal/work`
- ❌ `src/cmd/vet/testdata/buildtag`
- ❌ `src/cmd/vet/testdata/tagtest`
- ✅ `src/go/build`
- ✅ `src/go/build/constraint`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 13.6% | 20.0% | 16.2% | 6/30 |

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

**Predicted Files (44):**
- ❌ `src/cmd/go/internal/imports/tags.go`
- ✅ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/load/pkg_test.go`
- ❌ `src/cmd/go/internal/load/test.go`
- ❌ `src/cmd/go/internal/modload/build.go`
- ❌ `src/cmd/go/internal/modload/buildlist.go`
- ❌ `src/cmd/go/internal/modload/import.go`
- ❌ `src/cmd/go/internal/modload/import_test.go`
- ❌ `src/cmd/go/internal/modload/list.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/mvs.go`
- ❌ `src/cmd/go/internal/modload/mvs_test.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ❌ `src/cmd/go/internal/modload/query_test.go`
- ❌ `src/cmd/go/internal/modload/search.go`
- ❌ `src/cmd/go/internal/modload/stat_openfile.go`
- ❌ `src/cmd/go/internal/modload/stat_unix.go`
- ❌ `src/cmd/go/internal/modload/stat_windows.go`
- ❌ `src/cmd/go/internal/modload/vendor.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/build_test.go`
- ✅ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/exec_test.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`
- ❌ `src/cmd/go/internal/work/init.go`
- ❌ `src/cmd/go/internal/work/security.go`
- ❌ `src/cmd/go/internal/work/security_test.go`
- ❌ `src/cmd/go/internal/work/shell.go`
- ❌ `src/cmd/go/internal/work/shell_test.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag2.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag3.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag4.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag5.go`
- ❌ `src/cmd/vet/testdata/tagtest/file1.go`
- ❌ `src/cmd/vet/testdata/tagtest/file2.go`
- ✅ `src/go/build/build.go`
- ✅ `src/go/build/build_test.go`
- ✅ `src/go/build/constraint/expr.go`
- ✅ `src/go/build/constraint/expr_test.go`
- ❌ `src/go/build/constraint/vers.go`
- ❌ `src/go/build/constraint/vers_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.0% | 20.0% | 24.0% | 6/30 |

##### Correct Directories Used for Evaluation

**Correct Directories (4):**
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/work`
- `src/go/build`
- `src/go/build/constraint`


### 📊 **Proposal #48866**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/mime`

**Predicted Directories (1):**
- ✅ `src/mime`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/mime/mediatype.go`
- `src/mime/mediatype_test.go`

**Predicted Files (2):**
- ✅ `src/mime/mediatype.go`
- ✅ `src/mime/mediatype_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/mime`


### 📊 **Proposal #50332**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 27.3% | 37.5% | 3/11 |

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

**Predicted Directories (5):**
- ✅ `src/cmd/go`
- ✅ `src/cmd/go/internal/base`
- ❌ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/go/internal/load`
- ✅ `src/cmd/go/internal/work`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 9.5% | 12.1% | 2/21 |

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

**Predicted Files (12):**
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/base/base.go`
- ✅ `src/cmd/go/internal/base/flag.go`
- ❌ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/go/internal/load/flag.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ✅ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/init.go`
- ❌ `src/cmd/go/internal/work/shell.go`
- ❌ `src/cmd/go/internal/work/work.go`
- ❌ `src/cmd/go/main.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 9.5% | 13.3% | 2/21 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/cmd/go`
- `src/cmd/go/internal/base`
- `src/cmd/go/internal/work`


### 📊 **Proposal #53466**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.0% | 50.0% | 37.5% | 3/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/cmd/dist`
- `src/cmd/link`
- `src/cmd/link/internal/ld`
- `src/cmd/link/internal/riscv64`
- `src/runtime`
- `src/syscall`

**Predicted Directories (10):**
- ❌ `src/cmd/asm/internal/arch`
- ❌ `src/cmd/compile/internal/riscv64`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/compile/internal/ssa/_gen`
- ✅ `src/cmd/link/internal/riscv64`
- ❌ `src/internal/abi`
- ❌ `src/internal/cpu`
- ✅ `src/runtime`
- ✅ `src/syscall`
- ❌ `src/vendor/golang.org/x/sys/unix`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 17.2% | 50.0% | 25.6% | 5/10 |

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

**Predicted Files (29):**
- ❌ `src/cmd/asm/internal/arch/riscv64.go`
- ❌ `src/cmd/compile/internal/riscv64/galign.go`
- ❌ `src/cmd/compile/internal/riscv64/ggen.go`
- ❌ `src/cmd/compile/internal/riscv64/gsubr.go`
- ❌ `src/cmd/compile/internal/riscv64/ssa.go`
- ❌ `src/cmd/compile/internal/ssa/_gen/RISCV64Ops.go`
- ❌ `src/cmd/compile/internal/ssa/rewriteRISCV64.go`
- ❌ `src/cmd/compile/internal/ssa/rewriteRISCV64latelower.go`
- ❌ `src/cmd/link/internal/riscv64/asm.go`
- ❌ `src/cmd/link/internal/riscv64/l.go`
- ✅ `src/cmd/link/internal/riscv64/obj.go`
- ❌ `src/internal/abi/abi_riscv64.go`
- ❌ `src/internal/cpu/cpu_riscv64.go`
- ❌ `src/internal/cpu/cpu_riscv64_linux.go`
- ❌ `src/internal/cpu/cpu_riscv64_other.go`
- ✅ `src/runtime/defs_freebsd_riscv64.go`
- ❌ `src/runtime/os_freebsd_riscv64.go`
- ❌ `src/runtime/signal_freebsd_riscv64.go`
- ✅ `src/runtime/vdso_freebsd_riscv64.go`
- ✅ `src/syscall/syscall_freebsd_riscv64.go`
- ❌ `src/syscall/zerrors_freebsd_riscv64.go`
- ✅ `src/syscall/zsyscall_freebsd_riscv64.go`
- ❌ `src/syscall/zsysnum_freebsd_riscv64.go`
- ❌ `src/syscall/ztypes_freebsd_riscv64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/syscall_freebsd_riscv64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/zerrors_freebsd_riscv64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/zsyscall_freebsd_riscv64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/zsysnum_freebsd_riscv64.go`
- ❌ `src/vendor/golang.org/x/sys/unix/ztypes_freebsd_riscv64.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 41.7% | 50.0% | 45.5% | 5/10 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/cmd/link/internal/riscv64`
- `src/runtime`
- `src/syscall`


### 📊 **Proposal #49097**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (1):**
- ✅ `src/net`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 80.0% | 66.7% | 72.7% | 4/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/net/dial.go`
- `src/net/iprawsock.go`
- `src/net/net.go`
- `src/net/tcpsock.go`
- `src/net/udpsock.go`
- `src/net/unixsock.go`

**Predicted Files (5):**
- ✅ `src/net/dial.go`
- ❌ `src/net/dial_test.go`
- ✅ `src/net/tcpsock.go`
- ✅ `src/net/udpsock.go`
- ✅ `src/net/unixsock.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 80.0% | 66.7% | 72.7% | 4/6 |

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

**Predicted Directories (0):**

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

**Predicted Files (0):**

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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/expvar`
- `src/sync/atomic`

**Predicted Directories (1):**
- ✅ `src/sync/atomic`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/expvar/expvar.go`
- `src/expvar/expvar_test.go`
- `src/sync/atomic/value.go`
- `src/sync/atomic/value_test.go`

**Predicted Files (2):**
- ✅ `src/sync/atomic/value.go`
- ✅ `src/sync/atomic/value_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/sync/atomic`


### 📊 **Proposal #47142**

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
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/database/sql/fakedb_test.go`
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`

**Predicted Files (2):**
- ❌ `src/database/sql/driver/driver.go`
- ✅ `src/database/sql/sql.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/database/sql`


### 📊 **Proposal #46742**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 20.0% | 33.3% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/compile/internal/typecheck`
- `src/cmd/compile/internal/walk`
- `src/runtime`
- `src/runtime/testdata/testprog`
- `test`

**Predicted Directories (1):**
- ✅ `src/runtime`

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

**Predicted Files (3):**
- ❌ `src/runtime/slice.go`
- ❌ `src/runtime/slice_test.go`
- ❌ `src/runtime/unsafe.go`

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

**Predicted Directories (0):**

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/sha256/sha256.go`
- `src/crypto/sha512/sha512.go`

**Predicted Files (0):**

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (1):**
- ✅ `src/reflect/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #44815**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/bufio`

**Predicted Directories (2):**
- ✅ `src/bufio`
- ❌ `src/net/http`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/bufio/bufio.go`
- `src/bufio/bufio_test.go`

**Predicted Files (6):**
- ✅ `src/bufio/bufio.go`
- ✅ `src/bufio/bufio_test.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/request_test.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/response_test.go`

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
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/strconv`

**Predicted Directories (4):**
- ❌ `src/cmd/internal/quoted`
- ❌ `src/fmt`
- ✅ `src/strconv`
- ❌ `src/text/template/parse`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/strconv/bytealg.go`
- `src/strconv/bytealg_bootstrap.go`
- `src/strconv/quote.go`
- `src/strconv/quote_test.go`

**Predicted Files (6):**
- ❌ `src/cmd/internal/quoted/quoted.go`
- ❌ `src/cmd/internal/quoted/quoted_test.go`
- ❌ `src/fmt/scan.go`
- ✅ `src/strconv/quote.go`
- ✅ `src/strconv/quote_test.go`
- ❌ `src/text/template/parse/lex.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/strconv`


### 📊 **Proposal #48218**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/value.go`
- `src/reflect/visiblefields_test.go`

**Predicted Files (1):**
- ✅ `src/reflect/value.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (1):**
- ✅ `src/reflect/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #51572**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/dist`
- `src/cmd/go/internal/imports`
- `src/go/build`

**Predicted Directories (13):**
- ❌ `src/cmd/internal/osinfo`
- ❌ `src/cmd/script`
- ❌ `src/cmd/test2json`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/go/internal/base`
- ❌ `src/internal/goos`
- ❌ `src/syscall`
- ❌ `src/time`
- ❌ `src/vendor/golang.org/x/net/nettest`
- ❌ `src/vendor/golang.org/x/sys/unix`
- ❌ `src/vendor/golang.org/x/telemetry/internal/mmap`
- ❌ `src/vendor/golang.org/x/term`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/dist/build.go`
- `src/cmd/go/internal/imports/build.go`
- `src/go/build/build.go`

**Predicted Files (41):**
- ❌ `src/cmd/internal/osinfo/os_uname.go`
- ❌ `src/cmd/internal/osinfo/version_unix_test.go`
- ❌ `src/cmd/script/cmds_unix.go`
- ❌ `src/cmd/test2json/signal_unix.go`
- ❌ `src/crypto/tls/bogo_shim_unix_test.go`
- ❌ `src/crypto/tls/handshake_unix_test.go`
- ❌ `src/crypto/x509/root_unix.go`
- ❌ `src/crypto/x509/root_unix_test.go`
- ❌ `src/go/internal/base/env.go`
- ❌ `src/go/internal/base/error.go`
- ❌ `src/go/internal/base/error_notunix.go`
- ❌ `src/go/internal/base/error_unix.go`
- ❌ `src/go/internal/base/flag.go`
- ❌ `src/go/internal/base/goflags.go`
- ❌ `src/go/internal/base/limit.go`
- ❌ `src/go/internal/base/path.go`
- ❌ `src/go/internal/base/signal.go`
- ❌ `src/go/internal/base/signal_notunix.go`
- ❌ `src/go/internal/base/signal_unix.go`
- ❌ `src/go/internal/base/tool.go`
- ❌ `src/internal/goos/unix.go`
- ❌ `src/syscall/exec_unix.go`
- ❌ `src/syscall/exec_unix_test.go`
- ❌ `src/syscall/linkname_unix.go`
- ❌ `src/syscall/mmap_unix_test.go`
- ❌ `src/syscall/sockcmsg_unix.go`
- ❌ `src/syscall/sockcmsg_unix_other.go`
- ❌ `src/syscall/syscall_unix.go`
- ❌ `src/syscall/syscall_unix_test.go`
- ❌ `src/time/sys_unix.go`
- ❌ `src/time/zoneinfo_unix.go`
- ❌ `src/time/zoneinfo_unix_test.go`
- ❌ `src/vendor/golang.org/x/net/nettest/nettest_unix.go`
- ❌ `src/vendor/golang.org/x/sys/unix/env_unix.go`
- ❌ `src/vendor/golang.org/x/sys/unix/pagesize_unix.go`
- ❌ `src/vendor/golang.org/x/sys/unix/sysvshm_unix.go`
- ❌ `src/vendor/golang.org/x/sys/unix/sysvshm_unix_other.go`
- ❌ `src/vendor/golang.org/x/telemetry/internal/mmap/mmap_unix.go`
- ❌ `src/vendor/golang.org/x/term/term_unix.go`
- ❌ `src/vendor/golang.org/x/term/term_unix_bsd.go`
- ❌ `src/vendor/golang.org/x/term/term_unix_other.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Correct Directories Used for Evaluation

**No correct directories found** - This proposal had no correctly predicted directories, so file-level evaluation within correct directories is not applicable.


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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/log/log_test.go`

**Predicted Files (2):**
- ❌ `src/log/log.go`
- ✅ `src/log/log_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/log`


### 📊 **Proposal #38781**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/net/http`
- `src/testing/iotest`

**Predicted Directories (1):**
- ✅ `src/testing/iotest`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 40.0% | 57.1% | 2/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/net/http/transport_test.go`
- `src/testing/iotest/example_test.go`
- `src/testing/iotest/logger_test.go`
- `src/testing/iotest/reader.go`
- `src/testing/iotest/reader_test.go`

**Predicted Files (2):**
- ✅ `src/testing/iotest/reader.go`
- ✅ `src/testing/iotest/reader_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 40.0% | 57.1% | 2/5 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/testing/iotest`


### 📊 **Proposal #36771**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/strconv`

**Predicted Directories (2):**
- ❌ `src/fmt`
- ✅ `src/strconv`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 66.7% | 44.4% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/strconv/atoc.go`
- `src/strconv/atoc_test.go`
- `src/strconv/ctoa.go`

**Predicted Files (6):**
- ❌ `src/fmt/scan.go`
- ❌ `src/fmt/scan_test.go`
- ✅ `src/strconv/atoc.go`
- ✅ `src/strconv/atoc_test.go`
- ❌ `src/strconv/atoi.go`
- ❌ `src/strconv/atoi_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/strconv`


### 📊 **Proposal #44435**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modload`

**Predicted Directories (2):**
- ✅ `src/cmd/go/internal/modcmd`
- ✅ `src/cmd/go/internal/modload`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.8% | 100.0% | 21.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modcmd/download.go`
- `src/cmd/go/internal/modload/modfile.go`

**Predicted Files (17):**
- ✅ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modcmd/mod.go`
- ❌ `src/cmd/go/internal/modcmd/verify.go`
- ❌ `src/cmd/go/internal/modcmd/why.go`
- ❌ `src/cmd/go/internal/modload/build.go`
- ❌ `src/cmd/go/internal/modload/buildlist.go`
- ❌ `src/cmd/go/internal/modload/edit.go`
- ❌ `src/cmd/go/internal/modload/help.go`
- ❌ `src/cmd/go/internal/modload/import.go`
- ❌ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/modload/list.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ✅ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/mvs.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ❌ `src/cmd/go/internal/modload/search.go`
- ❌ `src/cmd/go/internal/modload/vendor.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.8% | 100.0% | 21.1% | 2/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modload`


### 📊 **Proposal #50101**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/syscall/unix`
- `src/net`

**Predicted Directories (1):**
- ✅ `src/net`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 23.1% | 33.3% | 3/13 |

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

**Predicted Files (5):**
- ✅ `src/net/lookup.go`
- ❌ `src/net/lookup_test.go`
- ✅ `src/net/lookup_unix.go`
- ✅ `src/net/lookup_windows.go`
- ❌ `src/net/lookup_windows_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 23.1% | 33.3% | 3/13 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net`


### 📊 **Proposal #29770**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/html/template`
- `src/text/template`
- `src/text/template/parse`

**Predicted Directories (1):**
- ✅ `src/text/template/parse`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/html/template/exec_test.go`
- `src/text/template/exec_test.go`
- `src/text/template/parse/lex.go`
- `src/text/template/parse/parse.go`

**Predicted Files (4):**
- ✅ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/lex_test.go`
- ✅ `src/text/template/parse/parse.go`
- ❌ `src/text/template/parse/parse_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 2/4 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/text/template/parse`


### 📊 **Proposal #51566**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/io`
- `src/net/http`

**Predicted Directories (2):**
- ❌ `src/bytes`
- ✅ `src/io`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/io/io.go`
- `src/io/io_test.go`
- `src/net/http/transfer.go`

**Predicted Files (4):**
- ❌ `src/bytes/reader.go`
- ❌ `src/bytes/reader_test.go`
- ✅ `src/io/io.go`
- ✅ `src/io/io_test.go`

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
| 100.0% | 20.0% | 33.3% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/compile/internal/ssagen`
- `src/cmd/compile/internal/typecheck/_builtin`
- `src/cmd/compile/internal/walk`
- `src/runtime`
- `src/time`

**Predicted Directories (1):**
- ✅ `src/time`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 28.6% | 30.8% | 2/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/compile/internal/ssagen/ssa.go`
- `src/cmd/compile/internal/typecheck/_builtin/runtime.go`
- `src/cmd/compile/internal/walk/builtin.go`
- `src/runtime/chan.go`
- `src/runtime/time.go`
- `src/time/sleep.go`
- `src/time/tick_test.go`

**Predicted Files (6):**
- ✅ `src/time/sleep.go`
- ❌ `src/time/sleep_test.go`
- ❌ `src/time/tick.go`
- ✅ `src/time/tick_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 28.6% | 30.8% | 2/7 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/time`


### 📊 **Proposal #38079**

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


### 📊 **Proposal #51682**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/types2`
- `src/go/types`

**Predicted Directories (3):**
- ❌ `src/cmd/compile/internal/types`
- ✅ `src/cmd/compile/internal/types2`
- ✅ `src/go/types`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 25.0% | 25.0% | 2/8 |

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

**Predicted Files (8):**
- ❌ `src/cmd/compile/internal/types/type.go`
- ❌ `src/cmd/compile/internal/types/type_test.go`
- ✅ `src/cmd/compile/internal/types2/object.go`
- ❌ `src/cmd/compile/internal/types2/object_test.go`
- ❌ `src/go/types/func.go`
- ✅ `src/go/types/object.go`
- ❌ `src/go/types/object_test.go`
- ❌ `src/go/types/var.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 25.0% | 28.6% | 2/8 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/cmd/compile/internal/types2`
- `src/go/types`


### 📊 **Proposal #39214**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 25.0% | 36.4% | 2/8 |

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

**Predicted Directories (3):**
- ✅ `src/internal/cpu`
- ❌ `src/runtime`
- ✅ `src/testing`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.6% | 25.0% | 12.8% | 3/12 |

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

**Predicted Files (35):**
- ❌ `src/internal/cpu/cpu.go`
- ❌ `src/internal/cpu/cpu_arm.go`
- ❌ `src/internal/cpu/cpu_arm64.go`
- ❌ `src/internal/cpu/cpu_arm64_android.go`
- ❌ `src/internal/cpu/cpu_arm64_darwin.go`
- ❌ `src/internal/cpu/cpu_arm64_freebsd.go`
- ❌ `src/internal/cpu/cpu_arm64_hwcap.go`
- ❌ `src/internal/cpu/cpu_arm64_linux.go`
- ❌ `src/internal/cpu/cpu_arm64_openbsd.go`
- ❌ `src/internal/cpu/cpu_arm64_other.go`
- ❌ `src/internal/cpu/cpu_loong64.go`
- ❌ `src/internal/cpu/cpu_loong64_hwcap.go`
- ❌ `src/internal/cpu/cpu_loong64_linux.go`
- ❌ `src/internal/cpu/cpu_mips.go`
- ❌ `src/internal/cpu/cpu_mips64x.go`
- ❌ `src/internal/cpu/cpu_mipsle.go`
- ✅ `src/internal/cpu/cpu_no_name.go`
- ❌ `src/internal/cpu/cpu_ppc64x.go`
- ❌ `src/internal/cpu/cpu_ppc64x_aix.go`
- ❌ `src/internal/cpu/cpu_ppc64x_linux.go`
- ❌ `src/internal/cpu/cpu_ppc64x_other.go`
- ❌ `src/internal/cpu/cpu_riscv64.go`
- ❌ `src/internal/cpu/cpu_riscv64_linux.go`
- ❌ `src/internal/cpu/cpu_riscv64_other.go`
- ❌ `src/internal/cpu/cpu_s390x.go`
- ❌ `src/internal/cpu/cpu_s390x_test.go`
- ❌ `src/internal/cpu/cpu_test.go`
- ❌ `src/internal/cpu/cpu_wasm.go`
- ✅ `src/internal/cpu/cpu_x86.go`
- ❌ `src/internal/cpu/cpu_x86_test.go`
- ❌ `src/runtime/cpuflags.go`
- ❌ `src/runtime/cpuflags_amd64.go`
- ❌ `src/runtime/cpuflags_arm64.go`
- ✅ `src/testing/benchmark.go`
- ❌ `src/testing/benchmark_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.4% | 25.0% | 13.6% | 3/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (2):**
- `src/internal/cpu`
- `src/testing`


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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/request.go`
- `src/net/http/serve_test.go`

**Predicted Files (1):**
- ✅ `src/net/http/request.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/net/http`


### 📊 **Proposal #51972**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/sync`

**Predicted Directories (1):**
- ✅ `src/sync`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/sync/map.go`
- `src/sync/map_reference_test.go`
- `src/sync/map_test.go`

**Predicted Files (2):**
- ✅ `src/sync/map.go`
- ✅ `src/sync/map_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

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

**Predicted Directories (2):**
- ❌ `src/runtime/race`
- ❌ `src/sync/atomic`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/sync/cond.go`

**Predicted Files (5):**
- ❌ `src/runtime/race/doc.go`
- ❌ `src/runtime/race/race.go`
- ❌ `src/sync/atomic/doc.go`
- ❌ `src/sync/atomic/type.go`
- ❌ `src/sync/atomic/value.go`

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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/tls`
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 85.7% | 50.0% | 63.2% | 6/12 |

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
- ✅ `src/crypto/tls/handshake_client.go`
- ✅ `src/crypto/tls/handshake_client_test.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ✅ `src/crypto/tls/handshake_server_test.go`
- ✅ `src/crypto/tls/tls.go`
- ❌ `src/crypto/tls/tls_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 85.7% | 50.0% | 63.2% | 6/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/crypto/tls`


### 📊 **Proposal #35044**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (1):**
- ✅ `src/crypto/x509`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/crypto/x509/cert_pool.go`

**Predicted Files (2):**
- ✅ `src/crypto/x509/cert_pool.go`
- ❌ `src/crypto/x509/cert_pool_test.go`

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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (1):**
- ✅ `src/io`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/io/io.go`
- `src/io/io_test.go`

**Predicted Files (2):**
- ✅ `src/io/io.go`
- ✅ `src/io/io_test.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

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

**Predicted Directories (0):**

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

**Predicted Files (0):**

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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (1):**
- ✅ `src/reflect/value.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Correct Directories Used for Evaluation

**Correct Directories (1):**
- `src/reflect`


### 📊 **Proposal #47609**

#### Directory Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/unicode/utf8`

**Predicted Directories (1):**
- ✅ `src/unicode/utf8`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/unicode/utf8/utf8.go`
- `src/unicode/utf8/utf8_test.go`

**Predicted Files (2):**
- ✅ `src/unicode/utf8/utf8.go`
- ✅ `src/unicode/utf8/utf8_test.go`

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
| 75.0% | 37.5% | 50.0% | 3/8 |

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

**Predicted Directories (4):**
- ❌ `src/hash/adler32`
- ✅ `src/hash/crc32`
- ✅ `src/hash/crc64`
- ✅ `src/hash/fnv`

#### File Level Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/12 |

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

**Predicted Files (4):**
- ❌ `src/hash/adler32/adler32.go`
- ❌ `src/hash/crc32/crc32.go`
- ❌ `src/hash/crc64/crc64.go`
- ❌ `src/hash/fnv/fnv.go`

#### File Level within Correct Directories Results

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/12 |

##### Correct Directories Used for Evaluation

**Correct Directories (3):**
- `src/hash/crc32`
- `src/hash/crc64`
- `src/hash/fnv`
