# Embedding-Based Localization Evaluation Summary (2025-07-12)

Processed Proposals: 231

## Directory-Level Macro Metrics (File Embeddings)

- Top-5: Precision=0.311, Recall=0.502, F1=0.338
- Top-10: Precision=0.212, Recall=0.577, F1=0.266
- Top-20: Precision=0.149, Recall=0.664, F1=0.208
- Top-30: Precision=0.114, Recall=0.697, F1=0.168
- Top-40: Precision=0.096, Recall=0.729, F1=0.146
- Top-50: Precision=0.083, Recall=0.746, F1=0.129

## File-Level Macro Metrics (File Embeddings)

- Top-5: Precision=0.133, Recall=0.188, F1=0.135
- Top-10: Precision=0.099, Recall=0.257, F1=0.122
- Top-20: Precision=0.066, Recall=0.334, F1=0.097
- Top-30: Precision=0.052, Recall=0.388, F1=0.081
- Top-40: Precision=0.044, Recall=0.435, F1=0.072
- Top-50: Precision=0.039, Recall=0.465, F1=0.065

## Directory-Level Macro Metrics (Function Embeddings)

- Top-5: Precision=0.439, Recall=0.585, F1=0.448
- Top-10: Precision=0.333, Recall=0.627, F1=0.377
- Top-20: Precision=0.248, Recall=0.688, F1=0.310
- Top-30: Precision=0.207, Recall=0.725, F1=0.268
- Top-40: Precision=0.172, Recall=0.750, F1=0.234
- Top-50: Precision=0.146, Recall=0.765, F1=0.207

## File-Level Macro Metrics (Function Embeddings)

- Top-5: Precision=0.309, Recall=0.332, F1=0.280
- Top-10: Precision=0.241, Recall=0.409, F1=0.263
- Top-20: Precision=0.183, Recall=0.501, F1=0.230
- Top-30: Precision=0.149, Recall=0.541, F1=0.198
- Top-40: Precision=0.126, Recall=0.573, F1=0.175
- Top-50: Precision=0.108, Recall=0.606, F1=0.158

## Function-Level Macro Metrics (Function Embeddings)

- Top-5: Precision=0.162, Recall=0.116, F1=0.107
- Top-10: Precision=0.123, Recall=0.170, F1=0.111
- Top-20: Precision=0.096, Recall=0.237, F1=0.107
- Top-30: Precision=0.078, Recall=0.277, F1=0.096
- Top-40: Precision=0.067, Recall=0.298, F1=0.086
- Top-50: Precision=0.059, Recall=0.323, F1=0.080

## Detailed Per-Proposal Comparisons

### 📊 Proposal #19367

#### File Embeddings - Directory Level
- ✅ `src/runtime`

#### File Embeddings - File Level
- ❌ `src/runtime/checkptr.go`
- ❌ `src/runtime/select.go`

#### Function Embeddings - Directory Level
- ✅ `src/runtime`

#### Function Embeddings - File Level
- ❌ `src/runtime/checkptr.go`
- ❌ `src/runtime/select.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/checkptr.go`, `checkptrAlignment`)
- ❌ (`src/runtime/checkptr.go`, `checkptrArithmetic`)
- ❌ (`src/runtime/select.go`, `selectgo`)

### 📊 Proposal #26535

#### File Embeddings - Directory Level
- ✅ `src/compress/lzw`

#### File Embeddings - File Level
- ✅ `src/compress/lzw/reader.go`
- ❌ `src/compress/lzw/reader_test.go`
- ❌ `src/compress/lzw/writer.go`
- ❌ `src/compress/lzw/writer_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/compress/lzw`

#### Function Embeddings - File Level
- ❌ `src/compress/lzw/reader.go`
- ❌ `src/compress/lzw/reader_test.go`
- ❌ `src/compress/lzw/writer.go`
- ❌ `src/compress/lzw/writer_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/compress/lzw/writer.go`, `Write`)
- ❌ (`src/compress/lzw/reader_test.go`, `TestReaderReset`)
- ❌ (`src/compress/lzw/reader_test.go`, `TestHiCodeDoesNotOverflow`)
- ❌ (`src/compress/lzw/reader_test.go`, `TestNoLongerSavingPriorExpansions`)
- ❌ (`src/compress/lzw/reader_test.go`, `BenchmarkDecoder`)
- ❌ (`src/compress/lzw/reader.go`, `readLSB`)
- ❌ (`src/compress/lzw/reader.go`, `readMSB`)
- ❌ (`src/compress/lzw/reader.go`, `Read`)
- ❌ (`src/compress/lzw/reader.go`, `decode`)
- ❌ (`src/compress/lzw/reader.go`, `Close`)
- ❌ (`src/compress/lzw/reader.go`, `Reset`)
- ❌ (`src/compress/lzw/reader.go`, `NewReader`)
- ❌ (`src/compress/lzw/reader.go`, `newReader`)
- ❌ (`src/compress/lzw/reader.go`, `init`)
- ❌ (`src/compress/lzw/writer.go`, `writeLSB`)
- ❌ (`src/compress/lzw/writer.go`, `writeMSB`)
- ❌ (`src/compress/lzw/writer.go`, `incHi`)
- ❌ (`src/compress/lzw/writer.go`, `Write`)
- ❌ (`src/compress/lzw/writer.go`, `Close`)
- ❌ (`src/compress/lzw/writer.go`, `Reset`)
- ❌ (`src/compress/lzw/writer.go`, `NewWriter`)
- ❌ (`src/compress/lzw/writer.go`, `newWriter`)
- ❌ (`src/compress/lzw/writer.go`, `init`)
- ❌ (`src/compress/lzw/writer_test.go`, `TestWriterReset`)
- ❌ (`src/compress/lzw/writer_test.go`, `BenchmarkEncoder`)

### 📊 Proposal #27628

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/cache`
- ❌ `src/cmd/go/internal/work`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/cache/hash.go`
- ❌ `src/cmd/go/internal/work/buildid.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/cache`
- ✅ `src/cmd/go/internal/work`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/cache/hash.go`
- ✅ `src/cmd/go/internal/work/buildid.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/work/buildid.go`, `useCache`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `showStdout`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `updateBuildID`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `link`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `useCache`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `showStdout`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `updateBuildID`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `useCache`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `flushOutput`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `updateBuildID`)
- ❌ (`src/cmd/go/internal/work/gccgo.go`, `asm`)
- ❌ (`src/cmd/go/internal/work/gccgo.go`, `pack`)
- ❌ (`src/cmd/go/internal/work/gccgo.go`, `link`)
- ❌ (`src/cmd/go/internal/work/gccgo.go`, `cc`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `asm`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `toolVerify`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `pack`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `ld`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `ldShared`)
- ❌ (`src/cmd/go/internal/cache/hash.go`, `Subkey`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `build`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `vet`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `link`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `getPkgConfigFlags`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `linkShared`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `cover`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `ld`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `gcc`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `gxx`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `gfortran`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `ccompile`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `gccld`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `cgo`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `dynimport`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `swig`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `swigOne`)

### 📊 Proposal #28089

#### File Embeddings - Directory Level
- ❌ `src/go/ast`

#### File Embeddings - File Level
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/issues_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/go/ast`

#### Function Embeddings - File Level
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/issues_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/ast/issues_test.go`, `TestIssue28089`)
- ❌ (`src/go/ast/ast.go`, `IsGenerated`)
- ❌ (`src/go/ast/ast.go`, `generator`)

### 📊 Proposal #28308

#### File Embeddings - Directory Level
- ❌ `src/cmd/vendor/golang.org/x/sys/unix`
- ❌ `src/cmd/vendor/golang.org/x/text/language`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/composite`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/copylock`
- ✅ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/hostport`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/lostcancel`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/nilfunc`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/unreachable`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/types/typeutil`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/analysisinternal`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/bisect`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typeparams`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typesinternal`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex`
- ❌ `src/cmd/vet`
- ✅ `src/cmd/vet/testdata/hostport`
- ❌ `src/net/http`
- ❌ `src/vendor/golang.org/x/crypto/cryptobyte`
- ❌ `src/vendor/golang.org/x/sys/cpu`

#### File Embeddings - File Level
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
- ❌ `src/cmd/vendor/golang.org/x/text/language/parse.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/composite/composite.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/copylock/copylock.go`
- ✅ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/hostport/hostport.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/lostcancel/lostcancel.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/nilfunc/nilfunc.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/testinggoroutine.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/util.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/unreachable/unreachable.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/types/typeutil/callee.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/analysisinternal/analysis.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil/clone.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil/comment.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor/cursor.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil/util.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/bisect/bisect.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typeparams/free.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typeparams/termlist.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/classify_call.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/types.go`
- ❌ `src/cmd/vet/main.go`
- ✅ `src/cmd/vet/testdata/hostport/hostport.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/net/http/h2_bundle.go`
- ❌ `src/vendor/golang.org/x/crypto/cryptobyte/asn1.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_linux_loong64.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_loong64.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/parse.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/vendor/golang.org/x/sys/unix`
- ❌ `src/cmd/vendor/golang.org/x/text/language`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/composite`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/copylock`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/hostport`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/lostcancel`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/nilfunc`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/unreachable`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/types/typeutil`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/analysisinternal`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/bisect`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typeparams`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typesinternal`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex`
- ❌ `src/cmd/vet`
- ✅ `src/cmd/vet/testdata/hostport`
- ❌ `src/net/http`
- ❌ `src/vendor/golang.org/x/crypto/cryptobyte`
- ❌ `src/vendor/golang.org/x/sys/cpu`

#### Function Embeddings - File Level
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
- ❌ `src/cmd/vendor/golang.org/x/text/language/parse.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/composite/composite.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/copylock/copylock.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/hostport/hostport.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/lostcancel/lostcancel.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/nilfunc/nilfunc.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/testinggoroutine.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/util.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/unreachable/unreachable.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/types/typeutil/callee.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/analysisinternal/analysis.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil/clone.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil/comment.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor/cursor.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/astutil/util.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/bisect/bisect.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typeparams/free.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typeparams/termlist.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/classify_call.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/types.go`
- ❌ `src/cmd/vet/main.go`
- ✅ `src/cmd/vet/testdata/hostport/hostport.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/net/http/h2_bundle.go`
- ❌ `src/vendor/golang.org/x/crypto/cryptobyte/asn1.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_linux_loong64.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_loong64.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/parse.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/vet/main.go`, `main`)
- ❌ (`src/cmd/vet/vet_test.go`, `TestVet`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`, `New`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`, `Uses`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`, `Used`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`, `Def`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`, `Package`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`, `Object`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`, `Selection`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`, `Calls`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/hostport/hostport.go`, `run`)
- ✅ (`src/cmd/vet/testdata/hostport/hostport.go`, `_`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/types/typeutil/callee.go`, `Callee`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/types/typeutil/callee.go`, `StaticCallee`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/types/typeutil/callee.go`, `usedIdent`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/types/typeutil/callee.go`, `interfaceMethod`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/comment.go`, `Deprecation`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/comment.go`, `isDirective`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/comment.go`, `Directives`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `Readv`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `Preadv`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `Writev`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `Pwritev`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `appendBytes`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `writevRacedetect`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `readvRacedetect`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `darwinMajorMinPatch`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `darwinKernelVersionMin`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`, `sockaddr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`, `sockaddr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`, `sockaddr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`, `sockaddr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`, `sockaddr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`, `anyToSockaddr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`, `readvRacedetect`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`, `writevRacedetect`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`, `isGroupMember`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`, `isCapDacOverrideSet`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/copylock/copylock.go`, `lockPath`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `readv`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `preadv`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `writev`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `pwritev`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_loong64.go`, `initOptions`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_loong64.go`, `get_cpucfg`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_loong64.go`, `cfgIsSet`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`, `checkCanonicalFieldTag`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`, `checkTagDuplicates`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/analysisinternal/analysis.go`, `AddImport`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/analysisinternal/analysis.go`, `FreshName`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/analysisinternal/analysis.go`, `Format`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/analysisinternal/analysis.go`, `validateFix`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/analysisinternal/analysis.go`, `IsStdPackage`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/classify_call.go`, `String`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/classify_call.go`, `ClassifyCall`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/classify_call.go`, `UsedIdent`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/classify_call.go`, `usedIdent`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/classify_call.go`, `interfaceMethod`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/nilfunc/nilfunc.go`, `run`)
- ❌ (`src/vendor/golang.org/x/crypto/cryptobyte/asn1.go`, `AddASN1`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/composite/composite.go`, `run`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/bisect/bisect.go`, `AppendMarker`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/bisect/bisect.go`, `fnvUint64`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/bisect/bisect.go`, `fnvUint32`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typeparams/free.go`, `Has`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor/cursor.go`, `At`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor/cursor.go`, `Inspect`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor/cursor.go`, `Enclosing`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor/cursor.go`, `FindNode`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor/cursor.go`, `FindByPos`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/util.go`, `RangeInStringLiteral`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/util.go`, `PosInStringLiteral`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/util.go`, `PreorderStack`)
- ❌ (`src/cmd/vendor/golang.org/x/text/language/parse.go`, `Parse`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/testinggoroutine.go`, `goAsyncCall`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/testinggoroutine.go`, `tRunAsyncCall`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typesinternal/types.go`, `NewTypesInfo`)
- ❌ (`src/net/http/h2_bundle.go`, `http2invalidHTTP1LookingFrameHeader`)
- ❌ (`src/net/http/h2_bundle.go`, `ReadFrame`)
- ❌ (`src/net/http/h2_bundle.go`, `serve`)
- ❌ (`src/net/http/h2_bundle.go`, `handlePingTimer`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `readv`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `preadv`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `writev`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `pwritev`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/typeparams/termlist.go`, `String`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/unreachable/unreachable.go`, `findDead`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/lostcancel/lostcancel.go`, `runFunc`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/util.go`, `isMethodNamed`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/util.go`, `funcLitInScope`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/clone.go`, `CloneNode`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/internal/astutil/clone.go`, `cloneNode`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/parse.go`, `parseRelease`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_linux_loong64.go`, `doinit`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_linux_loong64.go`, `hwcIsSet`)

### 📊 Proposal #29062

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/test`
- ❌ `src/cmd/objdump`
- ❌ `src/internal/testenv`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/objdump/objdump_test.go`
- ❌ `src/internal/testenv/testenv.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/test`
- ❌ `src/cmd/objdump`
- ❌ `src/internal/testenv`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/objdump/objdump_test.go`
- ❌ `src/internal/testenv/testenv.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/objdump/objdump_test.go`, `TestMain`)
- ❌ (`src/cmd/go/internal/test/test.go`, `Write`)
- ❌ (`src/cmd/objdump/objdump_test.go`, `TestMain`)
- ❌ (`src/cmd/go/internal/test/test.go`, `tryCache`)
- ❌ (`src/cmd/go/internal/test/test.go`, `tryCacheWithID`)
- ❌ (`src/internal/testenv/testenv.go`, `HasGoBuild`)

### 📊 Proposal #29770

#### File Embeddings - Directory Level
- ✅ `src/html/template`
- ❌ `src/text/template`
- ✅ `src/text/template/parse`

#### File Embeddings - File Level
- ❌ `src/html/template/exec_test.go`
- ❌ `src/text/template/exec_test.go`
- ✅ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/parse.go`

#### Function Embeddings - Directory Level
- ❌ `src/html/template`
- ❌ `src/text/template`
- ✅ `src/text/template/parse`

#### Function Embeddings - File Level
- ❌ `src/html/template/exec_test.go`
- ❌ `src/text/template/exec_test.go`
- ❌ `src/text/template/parse/lex.go`
- ✅ `src/text/template/parse/parse.go`

#### Function Embeddings - Function Level
- ❌ (`src/text/template/parse/lex.go`, `lex`)
- ❌ (`src/text/template/parse/lex.go`, `lexText`)
- ❌ (`src/text/template/parse/lex.go`, `atRightDelim`)
- ❌ (`src/text/template/parse/lex.go`, `lexLeftDelim`)
- ❌ (`src/text/template/parse/lex.go`, `lexRightDelim`)
- ❌ (`src/text/template/parse/lex.go`, `lexInsideAction`)
- ❌ (`src/text/template/parse/lex.go`, `lexSpace`)
- ❌ (`src/text/template/parse/lex.go`, `atTerminator`)
- ❌ (`src/text/template/parse/lex.go`, `isSpace`)
- ❌ (`src/text/template/parse/lex.go`, `hasLeftTrimMarker`)
- ❌ (`src/text/template/parse/lex.go`, `hasRightTrimMarker`)
- ❌ (`src/text/template/exec_test.go`, `TestUnterminatedStringError`)
- ❌ (`src/html/template/exec_test.go`, `TestUnterminatedStringError`)
- ❌ (`src/text/template/parse/parse.go`, `unexpected`)
- ❌ (`src/text/template/parse/parse.go`, `textOrAction`)
- ❌ (`src/text/template/parse/parse.go`, `clearActionLine`)
- ❌ (`src/text/template/parse/parse.go`, `action`)
- ✅ (`src/text/template/parse/parse.go`, `pipeline`)
- ❌ (`src/text/template/parse/parse.go`, `checkPipeline`)
- ❌ (`src/text/template/parse/parse.go`, `parseControl`)
- ❌ (`src/text/template/parse/parse.go`, `elseControl`)
- ❌ (`src/text/template/parse/parse.go`, `blockControl`)
- ✅ (`src/text/template/parse/parse.go`, `templateControl`)
- ❌ (`src/text/template/parse/parse.go`, `command`)
- ❌ (`src/text/template/parse/parse.go`, `term`)

### 📊 Proposal #30715

#### File Embeddings - Directory Level
- ❌ `src/net/http`

#### File Embeddings - File Level
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/serve_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/http`

#### Function Embeddings - File Level
- ❌ `src/net/http/request.go`
- ✅ `src/net/http/serve_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/http/request.go`, `MaxBytesReader`)
- ❌ (`src/net/http/request.go`, `Error`)
- ❌ (`src/net/http/request.go`, `Read`)
- ❌ (`src/net/http/serve_test.go`, `testRequestBodyLimit`)

### 📊 Proposal #31804

#### File Embeddings - Directory Level
- ✅ `src/crypto/ed25519`

#### File Embeddings - File Level
- ✅ `src/crypto/ed25519/ed25519.go`
- ✅ `src/crypto/ed25519/ed25519_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/ed25519`

#### Function Embeddings - File Level
- ✅ `src/crypto/ed25519/ed25519.go`
- ✅ `src/crypto/ed25519/ed25519_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/ed25519/ed25519.go`, `Sign`)
- ❌ (`src/crypto/ed25519/ed25519.go`, `newKeyFromSeed`)
- ❌ (`src/crypto/ed25519/ed25519.go`, `Sign`)
- ✅ (`src/crypto/ed25519/ed25519.go`, `sign`)
- ❌ (`src/crypto/ed25519/ed25519.go`, `Verify`)
- ❌ (`src/crypto/ed25519/ed25519.go`, `VerifyWithOptions`)
- ❌ (`src/crypto/ed25519/ed25519_test.go`, `TestSignVerifyHashed`)
- ❌ (`src/crypto/ed25519/ed25519_test.go`, `TestCryptoSigner`)
- ❌ (`src/crypto/ed25519/ed25519.go`, `Sign`)
- ❌ (`src/crypto/ed25519/ed25519.go`, `newKeyFromSeed`)
- ❌ (`src/crypto/ed25519/ed25519.go`, `Sign`)
- ✅ (`src/crypto/ed25519/ed25519.go`, `sign`)
- ❌ (`src/crypto/ed25519/ed25519.go`, `Verify`)
- ❌ (`src/crypto/ed25519/ed25519.go`, `VerifyWithOptions`)
- ❌ (`src/crypto/ed25519/ed25519_test.go`, `TestSignVerifyHashed`)
- ❌ (`src/crypto/ed25519/ed25519_test.go`, `TestSignVerifyContext`)

### 📊 Proposal #32406

#### File Embeddings - Directory Level
- ✅ `src/crypto/tls`
- ❌ `src/net/http`

#### File Embeddings - File Level
- ❌ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/conn.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ✅ `src/crypto/tls/handshake_client_test.go`
- ✅ `src/crypto/tls/handshake_client_tls13.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/handshake_server_tls13.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/net/http/transport_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/tls`
- ❌ `src/net/http`

#### Function Embeddings - File Level
- ❌ `src/crypto/tls/common.go`
- ✅ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_client_test.go`
- ❌ `src/crypto/tls/handshake_client_tls13.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ✅ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/handshake_server_tls13.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/net/http/transport_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/http/transport.go`, `addTLS`)
- ❌ (`src/net/http/transport.go`, `dialConn`)
- ❌ (`src/net/http/server.go`, `serve`)
- ❌ (`src/crypto/tls/common.go`, `Context`)
- ❌ (`src/crypto/tls/common.go`, `Context`)
- ❌ (`src/crypto/tls/handshake_server.go`, `clientHelloInfo`)
- ❌ (`src/crypto/tls/handshake_client.go`, `doFullHandshake`)
- ❌ (`src/crypto/tls/common.go`, `Context`)
- ❌ (`src/crypto/tls/common.go`, `Context`)
- ❌ (`src/crypto/tls/handshake_server.go`, `serverHandshake`)
- ❌ (`src/crypto/tls/handshake_server.go`, `handshake`)
- ❌ (`src/crypto/tls/handshake_server.go`, `readClientHello`)
- ❌ (`src/crypto/tls/handshake_server.go`, `processClientHello`)
- ❌ (`src/crypto/tls/handshake_server.go`, `processCertsFromClient`)
- ❌ (`src/crypto/tls/handshake_server.go`, `clientHelloInfo`)
- ❌ (`src/crypto/tls/conn.go`, `handleRenegotiation`)
- ✅ (`src/crypto/tls/conn.go`, `Handshake`)
- ❌ (`src/crypto/tls/conn.go`, `HandshakeContext`)
- ❌ (`src/crypto/tls/conn.go`, `handshakeContext`)
- ❌ (`src/crypto/tls/handshake_client.go`, `clientHandshake`)
- ❌ (`src/crypto/tls/handshake_client.go`, `doFullHandshake`)
- ❌ (`src/crypto/tls/handshake_client.go`, `certificateRequestInfoFromMsg`)
- ❌ (`src/crypto/tls/handshake_client_tls13.go`, `sendClientCertificate`)
- ❌ (`src/net/http/transport.go`, `addTLS`)
- ❌ (`src/net/http/transport.go`, `dialConn`)
- ✅ (`src/crypto/tls/handshake_server_test.go`, `testClientHelloFailure`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestSNIGivenOnFailure`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestServerHandshakeContextCancellation`)
- ❌ (`src/crypto/tls/handshake_client_test.go`, `TestClientHandshakeContextCancellation`)
- ❌ (`src/crypto/tls/tls.go`, `dial`)
- ❌ (`src/crypto/tls/tls.go`, `Dial`)
- ❌ (`src/crypto/tls/tls.go`, `Dial`)
- ❌ (`src/net/http/server.go`, `serve`)
- ❌ (`src/crypto/tls/handshake_server_tls13.go`, `pickCertificate`)
- ❌ (`src/net/http/transport_test.go`, `TestTransportDialTLSContext`)

### 📊 Proposal #32716

#### File Embeddings - Directory Level
- ✅ `src/crypto/tls`

#### File Embeddings - File Level
- ❌ `src/crypto/tls/auth_test.go`
- ❌ `src/crypto/tls/cipher_suites.go`
- ✅ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/handshake_server_tls13.go`
- ❌ `src/crypto/tls/handshake_test.go`
- ❌ `src/crypto/tls/key_agreement.go`
- ❌ `src/crypto/tls/prf.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/tls`

#### Function Embeddings - File Level
- ❌ `src/crypto/tls/auth_test.go`
- ✅ `src/crypto/tls/cipher_suites.go`
- ❌ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/conn.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/handshake_server_tls13.go`
- ❌ `src/crypto/tls/handshake_test.go`
- ❌ `src/crypto/tls/key_agreement.go`
- ❌ `src/crypto/tls/prf.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/tls/cipher_suites.go`, `macSHA1`)
- ❌ (`src/crypto/tls/cipher_suites.go`, `macSHA256`)
- ❌ (`src/crypto/tls/cipher_suites.go`, `newConstantTimeHash`)
- ❌ (`src/crypto/tls/cipher_suites.go`, `Size`)
- ❌ (`src/crypto/tls/common.go`, `supportedVersions`)
- ❌ (`src/crypto/tls/common.go`, `maxSupportedVersion`)
- ❌ (`src/crypto/tls/common.go`, `mutualVersion`)
- ❌ (`src/crypto/tls/handshake_server.go`, `readClientHello`)
- ❌ (`src/crypto/tls/handshake_server.go`, `processClientHello`)
- ❌ (`src/crypto/tls/handshake_server.go`, `pickCipherSuite`)
- ❌ (`src/crypto/tls/prf.go`, `prfAndHashForVersion`)
- ❌ (`src/crypto/tls/prf.go`, `prfForVersion`)
- ❌ (`src/crypto/tls/prf.go`, `keysFromMasterSecret`)
- ❌ (`src/crypto/tls/prf.go`, `newFinishedHash`)
- ❌ (`src/crypto/tls/prf.go`, `Write`)
- ❌ (`src/crypto/tls/prf.go`, `hashForClientCertificate`)
- ❌ (`src/crypto/tls/prf.go`, `discardHandshakeBuffer`)
- ❌ (`src/crypto/tls/prf.go`, `ekmFromMasterSecret`)
- ❌ (`src/crypto/tls/conn.go`, `roundUp`)
- ❌ (`src/crypto/tls/conn.go`, `decrypt`)
- ❌ (`src/crypto/tls/conn.go`, `Write`)
- ❌ (`src/crypto/tls/conn.go`, `handleRenegotiation`)
- ❌ (`src/crypto/tls/handshake_client.go`, `makeClientHello`)
- ❌ (`src/crypto/tls/handshake_client.go`, `pickTLSVersion`)
- ❌ (`src/crypto/tls/auth_test.go`, `TestSignatureSelection`)
- ❌ (`src/crypto/tls/handshake_test.go`, `checkOpenSSLVersion`)
- ❌ (`src/crypto/tls/handshake_test.go`, `runMain`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestRejectBadProtocolVersion`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestNoSuiteOverlap`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `runServerTestTLS13`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestHandshakeServerRSAAES`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestHandshakeServerAESGCM`)
- ❌ (`src/crypto/tls/key_agreement.go`, `processClientKeyExchange`)
- ❌ (`src/crypto/tls/handshake_server_tls13.go`, `processClientHello`)

### 📊 Proposal #32779

#### File Embeddings - Directory Level
- ✅ `src/encoding/json`

#### File Embeddings - File Level
- ✅ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/stream.go`
- ❌ `src/encoding/json/stream_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/encoding/json`

#### Function Embeddings - File Level
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/stream.go`
- ✅ `src/encoding/json/stream_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/encoding/json/stream.go`, `Token`)
- ❌ (`src/encoding/json/decode.go`, `objectInterface`)
- ❌ (`src/encoding/json/stream_test.go`, `TestDecoder`)
- ❌ (`src/encoding/json/stream_test.go`, `TestDecodeInStream`)

### 📊 Proposal #33136

#### File Embeddings - Directory Level
- ✅ `src/reflect`

#### File Embeddings - File Level
- ❌ `src/reflect/all_test.go`
- ✅ `src/reflect/value.go`

#### Function Embeddings - Directory Level
- ✅ `src/reflect`

#### Function Embeddings - File Level
- ✅ `src/reflect/all_test.go`
- ❌ `src/reflect/value.go`

#### Function Embeddings - Function Level
- ❌ (`src/reflect/value.go`, `pointer`)
- ❌ (`src/reflect/value.go`, `packEface`)
- ❌ (`src/reflect/value.go`, `Addr`)
- ❌ (`src/reflect/value.go`, `Bool`)
- ❌ (`src/reflect/value.go`, `Bytes`)
- ❌ (`src/reflect/value.go`, `runes`)
- ❌ (`src/reflect/value.go`, `call`)
- ❌ (`src/reflect/value.go`, `callReflect`)
- ❌ (`src/reflect/value.go`, `methodReceiver`)
- ❌ (`src/reflect/value.go`, `storeRcvr`)
- ❌ (`src/reflect/value.go`, `Cap`)
- ❌ (`src/reflect/value.go`, `Close`)
- ❌ (`src/reflect/value.go`, `Complex`)
- ❌ (`src/reflect/value.go`, `Elem`)
- ❌ (`src/reflect/value.go`, `Field`)
- ❌ (`src/reflect/value.go`, `Float`)
- ❌ (`src/reflect/value.go`, `Index`)
- ❌ (`src/reflect/value.go`, `Int`)
- ❌ (`src/reflect/value.go`, `Interface`)
- ❌ (`src/reflect/value.go`, `valueInterface`)
- ❌ (`src/reflect/value.go`, `InterfaceData`)
- ❌ (`src/reflect/value.go`, `IsNil`)
- ❌ (`src/reflect/value.go`, `Len`)
- ❌ (`src/reflect/value.go`, `Pointer`)
- ❌ (`src/reflect/value.go`, `send`)
- ❌ (`src/reflect/value.go`, `Set`)
- ❌ (`src/reflect/value.go`, `SetPointer`)
- ❌ (`src/reflect/value.go`, `Slice`)
- ❌ (`src/reflect/value.go`, `Slice3`)
- ❌ (`src/reflect/value.go`, `String`)
- ❌ (`src/reflect/value.go`, `Uint`)
- ❌ (`src/reflect/value.go`, `typesMustMatch`)
- ❌ (`src/reflect/value.go`, `Copy`)
- ❌ (`src/reflect/value.go`, `Select`)
- ❌ (`src/reflect/value.go`, `Zero`)
- ❌ (`src/reflect/value.go`, `Set`)
- ❌ (`src/reflect/value.go`, `Zero`)
- ❌ (`src/reflect/all_test.go`, `TestSmallZero`)
- ❌ (`src/reflect/all_test.go`, `TestZeroSet`)

### 📊 Proposal #33184

#### File Embeddings - Directory Level
- ❌ `src/runtime`
- ✅ `src/time`

#### File Embeddings - File Level
- ❌ `src/runtime/time.go`
- ✅ `src/time/tick.go`
- ❌ `src/time/tick_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/runtime`
- ✅ `src/time`

#### Function Embeddings - File Level
- ✅ `src/runtime/time.go`
- ✅ `src/time/tick.go`
- ✅ `src/time/tick_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/time/tick_test.go`, `TestTicker`)
- ❌ (`src/time/tick_test.go`, `BenchmarkTickerReset`)
- ❌ (`src/time/tick_test.go`, `BenchmarkTickerResetNaive`)
- ✅ (`src/time/tick.go`, `Reset`)
- ❌ (`src/time/tick_test.go`, `TestTicker`)
- ❌ (`src/time/tick_test.go`, `BenchmarkTickerReset`)
- ❌ (`src/time/tick_test.go`, `BenchmarkTickerResetNaive`)
- ✅ (`src/time/tick.go`, `Reset`)
- ❌ (`src/time/tick_test.go`, `TestTicker`)
- ❌ (`src/runtime/time.go`, `goroutineReady`)
- ❌ (`src/time/tick.go`, `Tick`)

### 📊 Proposal #33232

#### File Embeddings - Directory Level
- ❌ `src/archive/tar`
- ❌ `src/builtin`
- ❌ `src/bytes`
- ❌ `src/cmd/asm`
- ❌ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/importer/testdata`
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/syntax`
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/cmd/compile/internal/test/testdata`
- ❌ `src/cmd/compile/internal/types`
- ❌ `src/cmd/compile/internal/types2`
- ❌ `src/cmd/cover/testdata`
- ❌ `src/cmd/doc`
- ❌ `src/cmd/fix`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/cmdflag`
- ❌ `src/cmd/go/internal/list`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ❌ `src/cmd/go/internal/modget`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/mvs`
- ❌ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/internal/buildid`
- ❌ `src/cmd/internal/obj`
- ❌ `src/cmd/internal/test2json`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode`
- ❌ `src/cmd/link/internal/loadelf`
- ❌ `src/cmd/link/internal/loadmacho`
- ❌ `src/cmd/link/internal/loadxcoff`
- ❌ `src/cmd/pack`
- ❌ `src/container/list`
- ❌ `src/container/ring`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/database/sql`
- ❌ `src/debug/dwarf`
- ❌ `src/debug/pe`
- ❌ `src/embed/internal/embedtest`
- ❌ `src/encoding/asn1`
- ❌ `src/encoding/binary`
- ❌ `src/encoding/gob`
- ❌ `src/encoding/json`
- ❌ `src/encoding/xml`
- ❌ `src/errors`
- ❌ `src/expvar`
- ❌ `src/fmt`
- ❌ `src/go/ast`
- ❌ `src/go/doc/testdata`
- ❌ `src/go/internal/gcimporter/testdata`
- ❌ `src/go/token`
- ❌ `src/go/types`
- ❌ `src/html/template`
- ❌ `src/internal/fmtsort`
- ❌ `src/internal/reflectlite`
- ❌ `src/internal/singleflight`
- ❌ `src/math/big`
- ❌ `src/math/bits`
- ❌ `src/math/rand`
- ❌ `src/mime/quotedprintable`
- ❌ `src/net`
- ❌ `src/net/http`
- ❌ `src/net/http/httptrace`
- ❌ `src/net/rpc`
- ❌ `src/net/rpc/jsonrpc`
- ❌ `src/net/url`
- ❌ `src/os/user`
- ❌ `src/plugin`
- ❌ `src/reflect`
- ❌ `src/runtime`
- ❌ `src/runtime/cgo`
- ❌ `src/runtime/pprof`
- ❌ `src/runtime/race`
- ❌ `src/runtime/race/testdata`
- ❌ `src/strings`
- ❌ `src/sync`
- ❌ `src/sync/atomic`
- ❌ `src/syscall`
- ❌ `src/syscall/js`
- ❌ `src/testing`
- ❌ `src/testing/quick`
- ❌ `src/text/template`

#### File Embeddings - File Level
- ❌ `src/archive/tar/reader_test.go`
- ❌ `src/archive/tar/writer_test.go`
- ❌ `src/builtin/builtin.go`
- ❌ `src/bytes/reader_test.go`
- ❌ `src/cmd/asm/internal/asm/endtoend_test.go`
- ❌ `src/cmd/asm/internal/asm/parse.go`
- ❌ `src/cmd/asm/main.go`
- ❌ `src/cmd/cgo/gcc.go`
- ❌ `src/cmd/cgo/out.go`
- ❌ `src/cmd/compile/internal/base/timings.go`
- ❌ `src/cmd/compile/internal/importer/testdata/exports.go`
- ❌ `src/cmd/compile/internal/ir/sizeof_test.go`
- ❌ `src/cmd/compile/internal/ssa/copyelim_test.go`
- ❌ `src/cmd/compile/internal/ssa/sizeof_test.go`
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/compile/internal/syntax/printer.go`
- ❌ `src/cmd/compile/internal/test/iface_test.go`
- ❌ `src/cmd/compile/internal/test/shift_test.go`
- ❌ `src/cmd/compile/internal/test/testdata/compound_test.go`
- ❌ `src/cmd/compile/internal/types/sizeof_test.go`
- ❌ `src/cmd/compile/internal/types2/expr.go`
- ❌ `src/cmd/compile/internal/types2/sizeof_test.go`
- ❌ `src/cmd/compile/internal/types2/subst.go`
- ❌ `src/cmd/cover/testdata/test.go`
- ❌ `src/cmd/doc/pkg.go`
- ❌ `src/cmd/fix/cftype.go`
- ❌ `src/cmd/fix/fix.go`
- ❌ `src/cmd/fix/gotypes.go`
- ❌ `src/cmd/fix/netipv6zone.go`
- ❌ `src/cmd/fix/printerconfig.go`
- ❌ `src/cmd/fix/typecheck.go`
- ❌ `src/cmd/go/internal/cmdflag/flag.go`
- ❌ `src/cmd/go/internal/list/list.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modfetch/cache.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/git.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ❌ `src/cmd/go/internal/modfetch/coderepo.go`
- ❌ `src/cmd/go/internal/modfetch/fetch.go`
- ❌ `src/cmd/go/internal/modfetch/repo.go`
- ❌ `src/cmd/go/internal/modget/get.go`
- ❌ `src/cmd/go/internal/modload/buildlist.go`
- ❌ `src/cmd/go/internal/modload/import.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/vendor.go`
- ❌ `src/cmd/go/internal/mvs/mvs.go`
- ❌ `src/cmd/go/internal/vcs/vcs.go`
- ❌ `src/cmd/go/internal/work/build_test.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/proxy_test.go`
- ❌ `src/cmd/internal/buildid/buildid_test.go`
- ❌ `src/cmd/internal/obj/link.go`
- ❌ `src/cmd/internal/obj/pcln.go`
- ❌ `src/cmd/internal/obj/sizeof_test.go`
- ❌ `src/cmd/internal/test2json/test2json_test.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/reflectcall.go`
- ❌ `src/cmd/link/internal/loadelf/ldelf.go`
- ❌ `src/cmd/link/internal/loadmacho/ldmacho.go`
- ❌ `src/cmd/link/internal/loadxcoff/ldxcoff.go`
- ❌ `src/cmd/pack/pack_test.go`
- ❌ `src/container/list/list_test.go`
- ❌ `src/container/ring/example_test.go`
- ❌ `src/container/ring/ring_test.go`
- ❌ `src/crypto/tls/generate_cert.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_client_test.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/x509/name_constraints_test.go`
- ❌ `src/crypto/x509/verify.go`
- ❌ `src/crypto/x509/x509_test.go`
- ❌ `src/database/sql/convert.go`
- ❌ `src/database/sql/convert_test.go`
- ❌ `src/database/sql/fakedb_test.go`
- ❌ `src/database/sql/sql.go`
- ❌ `src/database/sql/sql_test.go`
- ❌ `src/debug/dwarf/entry.go`
- ❌ `src/debug/dwarf/entry_test.go`
- ❌ `src/debug/pe/file.go`
- ❌ `src/embed/internal/embedtest/embed_test.go`
- ❌ `src/encoding/asn1/asn1.go`
- ❌ `src/encoding/asn1/asn1_test.go`
- ❌ `src/encoding/asn1/marshal_test.go`
- ❌ `src/encoding/binary/binary_test.go`
- ❌ `src/encoding/binary/example_test.go`
- ❌ `src/encoding/gob/codec_test.go`
- ❌ `src/encoding/gob/encoder_test.go`
- ❌ `src/encoding/gob/timing_test.go`
- ❌ `src/encoding/gob/type_test.go`
- ❌ `src/encoding/json/bench_test.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encode_test.go`
- ❌ `src/encoding/json/example_test.go`
- ❌ `src/encoding/json/scanner_test.go`
- ❌ `src/encoding/json/stream.go`
- ❌ `src/encoding/json/stream_test.go`
- ❌ `src/encoding/json/tagkey_test.go`
- ❌ `src/encoding/xml/marshal_test.go`
- ❌ `src/errors/wrap.go`
- ❌ `src/errors/wrap_test.go`
- ❌ `src/expvar/expvar.go`
- ❌ `src/expvar/expvar_test.go`
- ❌ `src/fmt/fmt_test.go`
- ❌ `src/fmt/scan_test.go`
- ❌ `src/go/ast/print.go`
- ❌ `src/go/doc/testdata/benchmark.go`
- ❌ `src/go/doc/testdata/testing.go`
- ❌ `src/go/internal/gcimporter/testdata/exports.go`
- ❌ `src/go/token/serialize_test.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/sizeof_test.go`
- ❌ `src/go/types/subst.go`
- ❌ `src/html/template/content_test.go`
- ❌ `src/html/template/escape_test.go`
- ❌ `src/html/template/example_test.go`
- ❌ `src/html/template/exec_test.go`
- ❌ `src/html/template/js.go`
- ❌ `src/html/template/js_test.go`
- ❌ `src/html/template/url_test.go`
- ❌ `src/internal/fmtsort/sort_test.go`
- ❌ `src/internal/reflectlite/all_test.go`
- ❌ `src/internal/reflectlite/value.go`
- ❌ `src/internal/singleflight/singleflight_test.go`
- ❌ `src/math/big/floatconv_test.go`
- ❌ `src/math/bits/make_examples.go`
- ❌ `src/math/rand/example_test.go`
- ❌ `src/math/rand/regress_test.go`
- ❌ `src/mime/quotedprintable/reader_test.go`
- ❌ `src/net/http/clientserver_test.go`
- ❌ `src/net/http/h2_bundle.go`
- ❌ `src/net/http/httptrace/trace.go`
- ❌ `src/net/http/response_test.go`
- ❌ `src/net/http/roundtrip_js.go`
- ❌ `src/net/http/serve_test.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/net/http/transport_test.go`
- ❌ `src/net/lookup.go`
- ❌ `src/net/lookup_test.go`
- ❌ `src/net/rpc/debug.go`
- ❌ `src/net/rpc/jsonrpc/server.go`
- ❌ `src/net/url/url_test.go`
- ❌ `src/os/user/lookup_unix.go`
- ❌ `src/plugin/plugin_dlopen.go`
- ❌ `src/reflect/abi_test.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/example_test.go`
- ❌ `src/reflect/export_test.go`
- ❌ `src/reflect/set_test.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`
- ❌ `src/runtime/abi_test.go`
- ❌ `src/runtime/cgo/handle_test.go`
- ❌ `src/runtime/chan_test.go`
- ❌ `src/runtime/debugcall.go`
- ❌ `src/runtime/gcinfo_test.go`
- ❌ `src/runtime/iface_test.go`
- ❌ `src/runtime/malloc_test.go`
- ❌ `src/runtime/map_benchmark_test.go`
- ❌ `src/runtime/map_test.go`
- ❌ `src/runtime/mfinal_test.go`
- ❌ `src/runtime/mgcscavenge.go`
- ❌ `src/runtime/os_windows.go`
- ❌ `src/runtime/plugin.go`
- ❌ `src/runtime/pprof/pprof.go`
- ❌ `src/runtime/race/race_test.go`
- ❌ `src/runtime/race/testdata/issue12664_test.go`
- ❌ `src/runtime/race/testdata/mop_test.go`
- ❌ `src/runtime/race/testdata/pool_test.go`
- ❌ `src/runtime/sizeof_test.go`
- ❌ `src/strings/reader_test.go`
- ❌ `src/sync/atomic/value.go`
- ❌ `src/sync/atomic/value_test.go`
- ❌ `src/sync/map.go`
- ❌ `src/sync/map_reference_test.go`
- ❌ `src/sync/map_test.go`
- ❌ `src/sync/pool_test.go`
- ❌ `src/sync/poolqueue.go`
- ❌ `src/syscall/fs_js.go`
- ❌ `src/syscall/js/js.go`
- ❌ `src/syscall/js/js_test.go`
- ❌ `src/syscall/syscall_windows.go`
- ❌ `src/testing/quick/quick.go`
- ❌ `src/testing/testing.go`
- ❌ `src/text/template/exec_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/archive/tar`
- ❌ `src/builtin`
- ❌ `src/bytes`
- ❌ `src/cmd/asm`
- ❌ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/importer/testdata`
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/syntax`
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/cmd/compile/internal/test/testdata`
- ❌ `src/cmd/compile/internal/types`
- ✅ `src/cmd/compile/internal/types2`
- ❌ `src/cmd/cover/testdata`
- ❌ `src/cmd/doc`
- ❌ `src/cmd/fix`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/cmdflag`
- ❌ `src/cmd/go/internal/list`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ❌ `src/cmd/go/internal/modget`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/mvs`
- ❌ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/internal/buildid`
- ❌ `src/cmd/internal/obj`
- ❌ `src/cmd/internal/test2json`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode`
- ❌ `src/cmd/link/internal/loadelf`
- ❌ `src/cmd/link/internal/loadmacho`
- ❌ `src/cmd/link/internal/loadxcoff`
- ❌ `src/cmd/pack`
- ❌ `src/container/list`
- ❌ `src/container/ring`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/database/sql`
- ❌ `src/debug/dwarf`
- ❌ `src/debug/pe`
- ❌ `src/embed/internal/embedtest`
- ❌ `src/encoding/asn1`
- ❌ `src/encoding/binary`
- ❌ `src/encoding/gob`
- ❌ `src/encoding/json`
- ❌ `src/encoding/xml`
- ❌ `src/errors`
- ❌ `src/expvar`
- ❌ `src/fmt`
- ❌ `src/go/ast`
- ❌ `src/go/doc/testdata`
- ❌ `src/go/internal/gcimporter/testdata`
- ❌ `src/go/token`
- ✅ `src/go/types`
- ❌ `src/html/template`
- ❌ `src/internal/fmtsort`
- ❌ `src/internal/reflectlite`
- ❌ `src/internal/singleflight`
- ❌ `src/math/big`
- ❌ `src/math/bits`
- ❌ `src/math/rand`
- ❌ `src/mime/quotedprintable`
- ❌ `src/net`
- ❌ `src/net/http`
- ❌ `src/net/http/httptrace`
- ❌ `src/net/rpc`
- ❌ `src/net/rpc/jsonrpc`
- ❌ `src/net/url`
- ❌ `src/os/user`
- ❌ `src/plugin`
- ❌ `src/reflect`
- ❌ `src/runtime`
- ❌ `src/runtime/cgo`
- ❌ `src/runtime/pprof`
- ❌ `src/runtime/race`
- ❌ `src/runtime/race/testdata`
- ❌ `src/strings`
- ❌ `src/sync`
- ❌ `src/sync/atomic`
- ❌ `src/syscall`
- ❌ `src/syscall/js`
- ❌ `src/testing`
- ❌ `src/testing/quick`
- ❌ `src/text/template`

#### Function Embeddings - File Level
- ❌ `src/archive/tar/reader_test.go`
- ❌ `src/archive/tar/writer_test.go`
- ❌ `src/builtin/builtin.go`
- ❌ `src/bytes/reader_test.go`
- ❌ `src/cmd/asm/internal/asm/endtoend_test.go`
- ❌ `src/cmd/asm/internal/asm/parse.go`
- ❌ `src/cmd/asm/main.go`
- ❌ `src/cmd/cgo/gcc.go`
- ❌ `src/cmd/cgo/out.go`
- ❌ `src/cmd/compile/internal/base/timings.go`
- ❌ `src/cmd/compile/internal/importer/testdata/exports.go`
- ❌ `src/cmd/compile/internal/ir/sizeof_test.go`
- ❌ `src/cmd/compile/internal/ssa/copyelim_test.go`
- ❌ `src/cmd/compile/internal/ssa/sizeof_test.go`
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/compile/internal/syntax/printer.go`
- ❌ `src/cmd/compile/internal/test/iface_test.go`
- ❌ `src/cmd/compile/internal/test/shift_test.go`
- ❌ `src/cmd/compile/internal/test/testdata/compound_test.go`
- ❌ `src/cmd/compile/internal/types/sizeof_test.go`
- ❌ `src/cmd/compile/internal/types2/expr.go`
- ❌ `src/cmd/compile/internal/types2/sizeof_test.go`
- ❌ `src/cmd/compile/internal/types2/subst.go`
- ❌ `src/cmd/cover/testdata/test.go`
- ❌ `src/cmd/doc/pkg.go`
- ❌ `src/cmd/fix/cftype.go`
- ❌ `src/cmd/fix/fix.go`
- ❌ `src/cmd/fix/gotypes.go`
- ❌ `src/cmd/fix/netipv6zone.go`
- ❌ `src/cmd/fix/printerconfig.go`
- ❌ `src/cmd/fix/typecheck.go`
- ❌ `src/cmd/go/internal/cmdflag/flag.go`
- ❌ `src/cmd/go/internal/list/list.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modfetch/cache.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/git.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ❌ `src/cmd/go/internal/modfetch/coderepo.go`
- ❌ `src/cmd/go/internal/modfetch/fetch.go`
- ❌ `src/cmd/go/internal/modfetch/repo.go`
- ❌ `src/cmd/go/internal/modget/get.go`
- ❌ `src/cmd/go/internal/modload/buildlist.go`
- ❌ `src/cmd/go/internal/modload/import.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/vendor.go`
- ❌ `src/cmd/go/internal/mvs/mvs.go`
- ❌ `src/cmd/go/internal/vcs/vcs.go`
- ❌ `src/cmd/go/internal/work/build_test.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/proxy_test.go`
- ❌ `src/cmd/internal/buildid/buildid_test.go`
- ❌ `src/cmd/internal/obj/link.go`
- ❌ `src/cmd/internal/obj/pcln.go`
- ❌ `src/cmd/internal/obj/sizeof_test.go`
- ❌ `src/cmd/internal/test2json/test2json_test.go`
- ❌ `src/cmd/link/internal/ld/testdata/deadcode/reflectcall.go`
- ❌ `src/cmd/link/internal/loadelf/ldelf.go`
- ❌ `src/cmd/link/internal/loadmacho/ldmacho.go`
- ❌ `src/cmd/link/internal/loadxcoff/ldxcoff.go`
- ❌ `src/cmd/pack/pack_test.go`
- ❌ `src/container/list/list_test.go`
- ❌ `src/container/ring/example_test.go`
- ❌ `src/container/ring/ring_test.go`
- ❌ `src/crypto/tls/generate_cert.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_client_test.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/x509/name_constraints_test.go`
- ❌ `src/crypto/x509/verify.go`
- ❌ `src/crypto/x509/x509_test.go`
- ❌ `src/database/sql/convert.go`
- ❌ `src/database/sql/convert_test.go`
- ❌ `src/database/sql/fakedb_test.go`
- ❌ `src/database/sql/sql.go`
- ❌ `src/database/sql/sql_test.go`
- ❌ `src/debug/dwarf/entry.go`
- ❌ `src/debug/dwarf/entry_test.go`
- ❌ `src/debug/pe/file.go`
- ❌ `src/embed/internal/embedtest/embed_test.go`
- ❌ `src/encoding/asn1/asn1.go`
- ❌ `src/encoding/asn1/asn1_test.go`
- ❌ `src/encoding/asn1/marshal_test.go`
- ❌ `src/encoding/binary/binary_test.go`
- ❌ `src/encoding/binary/example_test.go`
- ❌ `src/encoding/gob/codec_test.go`
- ❌ `src/encoding/gob/encoder_test.go`
- ❌ `src/encoding/gob/timing_test.go`
- ❌ `src/encoding/gob/type_test.go`
- ❌ `src/encoding/json/bench_test.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encode_test.go`
- ❌ `src/encoding/json/example_test.go`
- ❌ `src/encoding/json/scanner_test.go`
- ❌ `src/encoding/json/stream.go`
- ❌ `src/encoding/json/stream_test.go`
- ❌ `src/encoding/json/tagkey_test.go`
- ❌ `src/encoding/xml/marshal_test.go`
- ❌ `src/errors/wrap.go`
- ❌ `src/errors/wrap_test.go`
- ❌ `src/expvar/expvar.go`
- ❌ `src/expvar/expvar_test.go`
- ❌ `src/fmt/fmt_test.go`
- ❌ `src/fmt/scan_test.go`
- ❌ `src/go/ast/print.go`
- ❌ `src/go/doc/testdata/benchmark.go`
- ❌ `src/go/doc/testdata/testing.go`
- ❌ `src/go/internal/gcimporter/testdata/exports.go`
- ❌ `src/go/token/serialize_test.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/sizeof_test.go`
- ❌ `src/go/types/subst.go`
- ❌ `src/html/template/content_test.go`
- ❌ `src/html/template/escape_test.go`
- ❌ `src/html/template/example_test.go`
- ❌ `src/html/template/exec_test.go`
- ❌ `src/html/template/js.go`
- ❌ `src/html/template/js_test.go`
- ❌ `src/html/template/url_test.go`
- ❌ `src/internal/fmtsort/sort_test.go`
- ❌ `src/internal/reflectlite/all_test.go`
- ❌ `src/internal/reflectlite/value.go`
- ❌ `src/internal/singleflight/singleflight_test.go`
- ❌ `src/math/big/floatconv_test.go`
- ❌ `src/math/bits/make_examples.go`
- ❌ `src/math/rand/example_test.go`
- ❌ `src/math/rand/regress_test.go`
- ❌ `src/mime/quotedprintable/reader_test.go`
- ❌ `src/net/http/clientserver_test.go`
- ❌ `src/net/http/h2_bundle.go`
- ❌ `src/net/http/httptrace/trace.go`
- ❌ `src/net/http/response_test.go`
- ❌ `src/net/http/roundtrip_js.go`
- ❌ `src/net/http/serve_test.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/net/http/transport_test.go`
- ❌ `src/net/lookup.go`
- ❌ `src/net/lookup_test.go`
- ❌ `src/net/rpc/debug.go`
- ❌ `src/net/rpc/jsonrpc/server.go`
- ❌ `src/net/url/url_test.go`
- ❌ `src/os/user/lookup_unix.go`
- ❌ `src/plugin/plugin_dlopen.go`
- ❌ `src/reflect/abi_test.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/example_test.go`
- ❌ `src/reflect/export_test.go`
- ❌ `src/reflect/set_test.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`
- ❌ `src/runtime/abi_test.go`
- ❌ `src/runtime/cgo/handle_test.go`
- ❌ `src/runtime/chan_test.go`
- ❌ `src/runtime/debugcall.go`
- ❌ `src/runtime/gcinfo_test.go`
- ❌ `src/runtime/iface_test.go`
- ❌ `src/runtime/malloc_test.go`
- ❌ `src/runtime/map_benchmark_test.go`
- ❌ `src/runtime/map_test.go`
- ❌ `src/runtime/mfinal_test.go`
- ❌ `src/runtime/mgcscavenge.go`
- ❌ `src/runtime/os_windows.go`
- ❌ `src/runtime/plugin.go`
- ❌ `src/runtime/pprof/pprof.go`
- ❌ `src/runtime/race/race_test.go`
- ❌ `src/runtime/race/testdata/issue12664_test.go`
- ❌ `src/runtime/race/testdata/mop_test.go`
- ❌ `src/runtime/race/testdata/pool_test.go`
- ❌ `src/runtime/sizeof_test.go`
- ❌ `src/strings/reader_test.go`
- ❌ `src/sync/atomic/value.go`
- ❌ `src/sync/atomic/value_test.go`
- ❌ `src/sync/map.go`
- ❌ `src/sync/map_reference_test.go`
- ❌ `src/sync/map_test.go`
- ❌ `src/sync/pool_test.go`
- ❌ `src/sync/poolqueue.go`
- ❌ `src/syscall/fs_js.go`
- ❌ `src/syscall/js/js.go`
- ❌ `src/syscall/js/js_test.go`
- ❌ `src/syscall/syscall_windows.go`
- ❌ `src/testing/quick/quick.go`
- ❌ `src/testing/testing.go`
- ❌ `src/text/template/exec_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/compile/internal/types2/subst.go`, `typ`)
- ❌ (`src/runtime/iface_test.go`, `BenchmarkAssertI2E`)
- ❌ (`src/runtime/iface_test.go`, `BenchmarkAssertI2E2`)
- ❌ (`src/runtime/iface_test.go`, `BenchmarkAssertI2E2Blank`)
- ❌ (`src/runtime/iface_test.go`, `BenchmarkAssertE2E2`)
- ❌ (`src/runtime/iface_test.go`, `BenchmarkAssertE2E2Blank`)
- ❌ (`src/runtime/iface_test.go`, `TestNonEscapingConvT2E`)
- ❌ (`src/os/user/lookup_unix.go`, `matchGroupIndexValue`)
- ❌ (`src/os/user/lookup_unix.go`, `matchUserIndexValue`)
- ❌ (`src/container/ring/ring_test.go`, `verify`)
- ❌ (`src/database/sql/convert_test.go`, `conversionTests`)
- ❌ (`src/database/sql/convert_test.go`, `TestConversions`)
- ❌ (`src/database/sql/convert_test.go`, `TestRawBytesAllocs`)
- ❌ (`src/database/sql/convert_test.go`, `TestDriverArgs`)
- ❌ (`src/database/sql/sql_test.go`, `TestRowsColumnTypes`)
- ❌ (`src/database/sql/sql_test.go`, `TestExec`)
- ❌ (`src/database/sql/sql_test.go`, `TestConnRaw`)
- ❌ (`src/database/sql/sql_test.go`, `TestInvalidNilValues`)
- ❌ (`src/database/sql/sql_test.go`, `TestConnIsValid`)
- ❌ (`src/database/sql/sql_test.go`, `TestNamedValueChecker`)
- ❌ (`src/encoding/json/stream_test.go`, `TestEncoderSetEscapeHTML`)
- ❌ (`src/encoding/json/stream_test.go`, `TestDecoder`)
- ❌ (`src/encoding/json/stream_test.go`, `TestBlocking`)
- ❌ (`src/encoding/json/stream_test.go`, `TestDecodeInStream`)
- ❌ (`src/cmd/go/proxy_test.go`, `proxyHandler`)
- ❌ (`src/cmd/go/proxy_test.go`, `readArchive`)
- ❌ (`src/runtime/plugin.go`, `plugin_lastmoduleinit`)
- ❌ (`src/cmd/internal/test2json/test2json_test.go`, `diffJSON`)
- ❌ (`src/syscall/fs_js.go`, `fsCall`)
- ❌ (`src/cmd/go/internal/cmdflag/flag.go`, `ParseOne`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `gc`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `asmArgs`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `toolVerify`)
- ❌ (`src/cmd/internal/obj/pcln.go`, `linkpcln`)
- ❌ (`src/crypto/tls/handshake_server.go`, `establishKeys`)
- ❌ (`src/sync/map.go`, `load`)
- ❌ (`src/sync/map.go`, `tryLoadOrStore`)
- ❌ (`src/sync/map.go`, `delete`)
- ❌ (`src/sync/map.go`, `dirtyLocked`)
- ❌ (`src/cmd/compile/internal/ssa/copyelim_test.go`, `benchmarkCopyElim`)
- ❌ (`src/net/rpc/jsonrpc/server.go`, `ReadRequestBody`)
- ❌ (`src/encoding/json/bench_test.go`, `BenchmarkDecoderStream`)
- ❌ (`src/cmd/cover/testdata/test.go`, `testTypeSwitch`)
- ❌ (`src/cmd/cover/testdata/test.go`, `testEmptySwitches`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `matchInModule`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `checkWildcardVersions`)
- ❌ (`src/errors/wrap_test.go`, `TestAs`)
- ❌ (`src/errors/wrap_test.go`, `TestAsValidation`)
- ❌ (`src/cmd/compile/internal/test/testdata/compound_test.go`, `interface_ssa`)
- ❌ (`src/cmd/compile/internal/test/testdata/compound_test.go`, `testInterface`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `Fatalf`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateSelfSignedCertificate`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestCRLCreation`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateCertificateRequest`)
- ❌ (`src/container/ring/example_test.go`, `ExampleRing_Do`)
- ❌ (`src/container/ring/example_test.go`, `ExampleRing_Move`)
- ❌ (`src/container/ring/example_test.go`, `ExampleRing_Link`)
- ❌ (`src/container/ring/example_test.go`, `ExampleRing_Unlink`)
- ❌ (`src/runtime/gcinfo_test.go`, `TestGCInfo`)
- ❌ (`src/cmd/compile/internal/syntax/printer.go`, `printRawNode`)
- ❌ (`src/testing/quick/quick.go`, `toInterfaces`)
- ❌ (`src/archive/tar/reader_test.go`, `TestFileReader`)
- ❌ (`src/embed/internal/embedtest/embed_test.go`, `TestAliases`)
- ❌ (`src/encoding/gob/type_test.go`, `TestRegistrationNaming`)
- ❌ (`src/encoding/gob/type_test.go`, `TestTypeRace`)
- ❌ (`src/crypto/tls/handshake_client.go`, `establishKeys`)
- ❌ (`src/internal/reflectlite/value.go`, `packEface`)
- ❌ (`src/internal/reflectlite/value.go`, `Elem`)
- ❌ (`src/internal/reflectlite/value.go`, `valueInterface`)
- ❌ (`src/internal/reflectlite/value.go`, `assignTo`)
- ❌ (`src/internal/reflectlite/value.go`, `ifaceE2I`)
- ❌ (`src/net/http/transport.go`, `logf`)
- ❌ (`src/cmd/go/internal/modfetch/fetch.go`, `Download`)
- ❌ (`src/cmd/go/internal/modfetch/fetch.go`, `DownloadZip`)
- ❌ (`src/net/http/httptrace/trace.go`, `WithClientTrace`)
- ❌ (`src/go/token/serialize_test.go`, `checkSerialize`)
- ❌ (`src/net/http/response_test.go`, `TestReadResponseCloseInMiddle`)
- ❌ (`src/net/http/response_test.go`, `TestReadResponseErrors`)
- ❌ (`src/encoding/gob/codec_test.go`, `encFuzzDec`)
- ❌ (`src/encoding/gob/codec_test.go`, `TestFuzz`)
- ❌ (`src/reflect/value.go`, `packEface`)
- ❌ (`src/reflect/value.go`, `Elem`)
- ❌ (`src/reflect/value.go`, `valueInterface`)
- ❌ (`src/reflect/value.go`, `assignTo`)
- ❌ (`src/reflect/value.go`, `cvtT2I`)
- ❌ (`src/reflect/value.go`, `ifaceE2I`)
- ❌ (`src/encoding/asn1/asn1_test.go`, `TestUnmarshalWithNilOrNonPointer`)
- ❌ (`src/encoding/asn1/asn1_test.go`, `TestMarshalNilValue`)
- ❌ (`src/math/big/floatconv_test.go`, `TestFloatFormat`)
- ❌ (`src/html/template/url_test.go`, `TestURLFilters`)
- ❌ (`src/cmd/fix/netipv6zone.go`, `netipv6zone`)
- ❌ (`src/net/http/h2_bundle.go`, `ServeConn`)
- ❌ (`src/net/http/h2_bundle.go`, `http2h1ServerKeepAlivesDisabled`)
- ❌ (`src/internal/reflectlite/all_test.go`, `TestInterfaceValue`)
- ❌ (`src/internal/reflectlite/all_test.go`, `TestFunctionValue`)
- ❌ (`src/internal/reflectlite/all_test.go`, `TestIsNil`)
- ❌ (`src/internal/reflectlite/all_test.go`, `TestImportPath`)
- ❌ (`src/internal/reflectlite/all_test.go`, `TestAllocations`)
- ❌ (`src/internal/reflectlite/all_test.go`, `TestInvalid`)
- ❌ (`src/runtime/race/testdata/mop_test.go`, `TestRaceCaseType`)
- ❌ (`src/runtime/race/testdata/mop_test.go`, `TestRaceCaseTypeBody`)
- ❌ (`src/runtime/race/testdata/mop_test.go`, `TestRaceCaseTypeIssue5890`)
- ❌ (`src/runtime/race/testdata/mop_test.go`, `TestRaceEfaceWW`)
- ❌ (`src/runtime/race/testdata/mop_test.go`, `TestRaceEfaceConv`)
- ❌ (`src/runtime/race/testdata/mop_test.go`, `TestRaceEmptyInterface1`)
- ❌ (`src/runtime/race/testdata/mop_test.go`, `TestRaceEmptyInterface2`)
- ❌ (`src/runtime/race/testdata/mop_test.go`, `TestRaceTypeAssert`)
- ❌ (`src/encoding/json/example_test.go`, `ExampleRawMessage_unmarshal`)
- ❌ (`src/reflect/type.go`, `ptrTo`)
- ❌ (`src/reflect/type.go`, `ChanOf`)
- ❌ (`src/reflect/type.go`, `FuncOf`)
- ❌ (`src/reflect/type.go`, `SliceOf`)
- ❌ (`src/reflect/type.go`, `StructOf`)
- ❌ (`src/reflect/type.go`, `ArrayOf`)
- ❌ (`src/reflect/type.go`, `funcLayout`)
- ❌ (`src/cmd/go/internal/modfetch/codehost/git.go`, `Stat`)
- ❌ (`src/testing/testing.go`, `tRunner`)
- ❌ (`src/cmd/compile/internal/test/iface_test.go`, `TestEfaceConv1`)
- ❌ (`src/cmd/compile/internal/test/iface_test.go`, `TestEfaceConv2`)
- ❌ (`src/cmd/compile/internal/test/iface_test.go`, `TestIfaceConv1`)
- ❌ (`src/cmd/compile/internal/test/iface_test.go`, `TestIfaceConv2`)
- ❌ (`src/encoding/asn1/marshal_test.go`, `TestIssue11130`)
- ❌ (`src/encoding/asn1/marshal_test.go`, `BenchmarkUnmarshal`)
- ❌ (`src/math/rand/example_test.go`, `Example_rand`)
- ❌ (`src/encoding/json/tagkey_test.go`, `TestStructTagObjectKey`)
- ❌ (`src/cmd/go/internal/work/build_test.go`, `TestRespectSetgidDir`)
- ❌ (`src/text/template/exec_test.go`, `TestEvalFieldErrors`)
- ❌ (`src/text/template/exec_test.go`, `TestInterfaceValues`)
- ❌ (`src/text/template/exec_test.go`, `TestExecutePanicDuringCall`)
- ❌ (`src/net/url/url_test.go`, `ufmt`)
- ❌ (`src/cmd/compile/internal/ssa/sizeof_test.go`, `TestSizeof`)
- ❌ (`src/cmd/go/internal/mvs/mvs.go`, `buildList`)
- ❌ (`src/builtin/builtin.go`, `panic`)
- ❌ (`src/builtin/builtin.go`, `recover`)
- ❌ (`src/cmd/link/internal/loadelf/ldelf.go`, `Load`)
- ❌ (`src/reflect/example_test.go`, `ExampleKind`)
- ❌ (`src/reflect/example_test.go`, `ExampleMakeFunc`)
- ❌ (`src/encoding/json/encode.go`, `newEncodeState`)
- ❌ (`src/runtime/chan_test.go`, `TestChanSendInterface`)
- ❌ (`src/cmd/go/internal/modload/load.go`, `pkg`)
- ❌ (`src/database/sql/convert.go`, `convertAssignRows`)
- ❌ (`src/sync/poolqueue.go`, `pushHead`)
- ❌ (`src/sync/poolqueue.go`, `popHead`)
- ❌ (`src/sync/poolqueue.go`, `popTail`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `gccld`)
- ❌ (`src/cmd/internal/obj/sizeof_test.go`, `TestSizeof`)
- ❌ (`src/mime/quotedprintable/reader_test.go`, `TestReader`)
- ❌ (`src/mime/quotedprintable/reader_test.go`, `TestExhaustive`)
- ❌ (`src/expvar/expvar.go`, `Init`)
- ❌ (`src/go/ast/print.go`, `fprint`)
- ❌ (`src/fmt/scan_test.go`, `testScanfMulti`)
- ❌ (`src/sync/map_reference_test.go`, `Store`)
- ❌ (`src/sync/map_reference_test.go`, `LoadOrStore`)
- ❌ (`src/sync/map_reference_test.go`, `Range`)
- ❌ (`src/sync/map_reference_test.go`, `Load`)
- ❌ (`src/sync/map_reference_test.go`, `LoadOrStore`)
- ❌ (`src/sync/map_reference_test.go`, `Range`)
- ❌ (`src/sync/map_reference_test.go`, `dirty`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestTLS12OnlyCipherSuites`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestTLSPointFormats`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `connFromCommand`)
- ❌ (`src/cmd/fix/cftype.go`, `typefix`)
- ❌ (`src/go/types/subst.go`, `typ`)
- ❌ (`src/runtime/os_windows.go`, `monitorSuspendResume`)
- ❌ (`src/runtime/os_windows.go`, `goenvs`)
- ❌ (`src/encoding/json/scanner_test.go`, `genArray`)
- ❌ (`src/encoding/json/scanner_test.go`, `genMap`)
- ❌ (`src/net/http/server.go`, `ServeHTTP`)
- ❌ (`src/cmd/go/internal/modload/modfile.go`, `rawGoModSummary`)
- ❌ (`src/cmd/go/internal/modload/modfile.go`, `queryLatestVersionIgnoringRetractions`)
- ❌ (`src/cmd/link/internal/loadmacho/ldmacho.go`, `Load`)
- ❌ (`src/cmd/compile/internal/test/shift_test.go`, `TestShiftGeneric`)
- ❌ (`src/reflect/set_test.go`, `TestImplicitMapConversion`)
- ❌ (`src/debug/dwarf/entry.go`, `entry`)
- ❌ (`src/sync/map_test.go`, `applyCalls`)
- ❌ (`src/sync/map_test.go`, `TestConcurrentRange`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `metaImportsForPrefix`)
- ❌ (`src/cmd/go/internal/modfetch/codehost/vcs.go`, `NewRepo`)
- ❌ (`src/runtime/mgcscavenge.go`, `bgscavenge`)
- ❌ (`src/syscall/js/js.go`, `ValueOf`)
- ❌ (`src/bytes/reader_test.go`, `TestReaderAt`)
- ❌ (`src/runtime/race/testdata/issue12664_test.go`, `TestRaceIssue12664_3`)
- ❌ (`src/html/template/js_test.go`, `TestJSValEscaper`)
- ❌ (`src/html/template/js_test.go`, `TestJSStrEscaper`)
- ❌ (`src/html/template/js_test.go`, `TestJSRegexpEscaper`)
- ❌ (`src/html/template/js_test.go`, `TestEscapersOnLower7AndSelectHighCodepoints`)
- ❌ (`src/container/list/list_test.go`, `TestExtending`)
- ❌ (`src/container/list/list_test.go`, `TestZeroList`)
- ❌ (`src/container/list/list_test.go`, `TestInsertBeforeUnknownMark`)
- ❌ (`src/container/list/list_test.go`, `TestInsertAfterUnknownMark`)
- ❌ (`src/container/list/list_test.go`, `TestMoveUnknownMark`)
- ❌ (`src/runtime/map_benchmark_test.go`, `BenchmarkMapInterfaceString`)
- ❌ (`src/runtime/map_benchmark_test.go`, `BenchmarkMapInterfacePtr`)
- ❌ (`src/database/sql/sql.go`, `rowsColumnInfoSetupConnLocked`)
- ❌ (`src/crypto/tls/generate_cert.go`, `main`)
- ❌ (`src/runtime/mfinal_test.go`, `TestFinalizerType`)
- ❌ (`src/runtime/mfinal_test.go`, `TestFinalizerInterfaceBig`)
- ❌ (`src/cmd/compile/internal/types2/expr.go`, `exprInternal`)
- ❌ (`src/encoding/json/decode_test.go`, `TestUnmarshalMarshal`)
- ❌ (`src/encoding/json/decode_test.go`, `TestUnmarshalInterface`)
- ❌ (`src/encoding/json/decode_test.go`, `TestInterfaceSet`)
- ❌ (`src/encoding/json/decode_test.go`, `TestUnmarshalSyntax`)
- ❌ (`src/encoding/json/decode_test.go`, `TestSkipArrayObjects`)
- ❌ (`src/encoding/json/decode_test.go`, `TestPrefilled`)
- ❌ (`src/encoding/json/decode_test.go`, `TestInvalidStringOption`)
- ❌ (`src/encoding/json/decode_test.go`, `TestUnmarshalEmbeddedUnexported`)
- ❌ (`src/encoding/json/decode_test.go`, `TestUnmarshalErrorAfterMultipleJSON`)
- ❌ (`src/encoding/json/decode_test.go`, `TestUnmarshalRecursivePointer`)
- ❌ (`src/encoding/json/decode_test.go`, `TestUnmarshalMaxDepth`)
- ❌ (`src/cmd/asm/internal/asm/endtoend_test.go`, `testEndToEnd`)
- ❌ (`src/cmd/asm/internal/asm/endtoend_test.go`, `testErrors`)
- ❌ (`src/cmd/internal/obj/link.go`, `NewFuncInfo`)
- ❌ (`src/cmd/internal/obj/link.go`, `NewFileInfo`)
- ❌ (`src/errors/wrap.go`, `As`)
- ❌ (`src/html/template/exec_test.go`, `TestEvalFieldErrors`)
- ❌ (`src/html/template/exec_test.go`, `TestInterfaceValues`)
- ❌ (`src/html/template/exec_test.go`, `TestExecutePanicDuringCall`)
- ❌ (`src/html/template/exec_test.go`, `TestTemplateFuncsAfterClone`)
- ❌ (`src/net/http/serve_test.go`, `TestRequestBodyTimeoutClosesConnection`)
- ❌ (`src/net/http/serve_test.go`, `testTransportAndServerSharedBodyRace`)
- ❌ (`src/net/http/serve_test.go`, `testServerContext_LocalAddrContextKey`)
- ❌ (`src/net/http/serve_test.go`, `testContentEncodingNoSniffing`)
- ❌ (`src/debug/dwarf/entry_test.go`, `TestUnitIteration`)
- ❌ (`src/encoding/json/stream.go`, `Token`)
- ❌ (`src/cmd/fix/printerconfig.go`, `printerconfig`)
- ❌ (`src/strings/reader_test.go`, `TestReaderAt`)
- ❌ (`src/cmd/fix/typecheck.go`, `typecheck`)
- ❌ (`src/cmd/fix/typecheck.go`, `typecheck1`)
- ❌ (`src/net/http/transport_test.go`, `TestTransportServerClosingUnexpectedly`)
- ❌ (`src/net/http/transport_test.go`, `TestRetryRequestsOnError`)
- ❌ (`src/net/http/transport_test.go`, `testTransportEventTrace`)
- ❌ (`src/net/http/transport_test.go`, `TestTransportEventTraceTLSVerify`)
- ❌ (`src/net/http/transport_test.go`, `TestTransportEventTraceRealDNS`)
- ❌ (`src/cmd/link/internal/loadxcoff/ldxcoff.go`, `Load`)
- ❌ (`src/crypto/tls/handshake_client_test.go`, `connFromCommand`)
- ❌ (`src/cmd/fix/gotypes.go`, `fixGoExact`)
- ❌ (`src/runtime/map_test.go`, `TestDeferDeleteSlow`)
- ❌ (`src/runtime/map_test.go`, `TestMapInterfaceKey`)
- ❌ (`src/cmd/compile/internal/types/sizeof_test.go`, `TestSizeof`)
- ❌ (`src/expvar/expvar_test.go`, `TestMapCounter`)
- ❌ (`src/expvar/expvar_test.go`, `TestFunc`)
- ❌ (`src/cmd/asm/main.go`, `main`)
- ❌ (`src/encoding/xml/marshal_test.go`, `TestStructPointerMarshal`)
- ❌ (`src/encoding/xml/marshal_test.go`, `TestEncodeToken`)
- ❌ (`src/encoding/binary/example_test.go`, `ExampleWrite_multi`)
- ❌ (`src/runtime/debugcall.go`, `debugCallPanicked`)
- ❌ (`src/cmd/go/internal/modload/buildlist.go`, `readModGraph`)
- ❌ (`src/go/internal/gcimporter/testdata/exports.go`, `F5`)
- ❌ (`src/cmd/cgo/gcc.go`, `mangle`)
- ❌ (`src/cmd/cgo/gcc.go`, `loadType`)
- ❌ (`src/encoding/json/encode_test.go`, `TestOmitEmpty`)
- ❌ (`src/encoding/json/encode_test.go`, `init`)
- ❌ (`src/encoding/json/encode_test.go`, `TestAnonymousFields`)
- ❌ (`src/encoding/json/encode_test.go`, `TestNilMarshal`)
- ❌ (`src/encoding/json/encode_test.go`, `TestEncodeBytekind`)
- ❌ (`src/encoding/json/encode_test.go`, `TestMarshalFloat`)
- ❌ (`src/encoding/json/encode_test.go`, `TestMarshalRawMessageValue`)
- ❌ (`src/crypto/x509/verify.go`, `checkNameConstraints`)
- ❌ (`src/crypto/x509/verify.go`, `isValid`)
- ❌ (`src/archive/tar/writer_test.go`, `TestWriter`)
- ❌ (`src/archive/tar/writer_test.go`, `TestFileWriter`)
- ❌ (`src/net/lookup_test.go`, `TestLookupIPAddrPreservesContextValues`)
- ❌ (`src/go/types/sizeof_test.go`, `TestSizeof`)
- ❌ (`src/runtime/pprof/pprof.go`, `NewProfile`)
- ❌ (`src/go/types/expr.go`, `exprInternal`)
- ❌ (`src/encoding/gob/encoder_test.go`, `TestBasicEncoderDecoder`)
- ❌ (`src/encoding/gob/encoder_test.go`, `TestNestedInterfaces`)
- ❌ (`src/encoding/gob/encoder_test.go`, `TestGobMapInterfaceEncode`)
- ❌ (`src/encoding/gob/encoder_test.go`, `TestPtrToMapOfMap`)
- ❌ (`src/encoding/gob/encoder_test.go`, `TestNilPointerPanics`)
- ❌ (`src/encoding/gob/encoder_test.go`, `TestNilPointerInsideInterface`)
- ❌ (`src/encoding/gob/encoder_test.go`, `Test29ElementSlice`)
- ❌ (`src/cmd/go/internal/list/list.go`, `runList`)
- ❌ (`src/cmd/go/internal/modload/vendor.go`, `checkVendorConsistency`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestSizeStructCache`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestReadErrorMsg`)
- ❌ (`src/encoding/binary/binary_test.go`, `testReadInvalidDestination`)
- ❌ (`src/net/http/clientserver_test.go`, `TestH12_AutoGzip_Disabled`)
- ❌ (`src/net/http/clientserver_test.go`, `TestBidiStreamReverseProxy`)
- ❌ (`src/net/http/roundtrip_js.go`, `RoundTrip`)
- ❌ (`src/net/http/roundtrip_js.go`, `Read`)
- ❌ (`src/net/http/roundtrip_js.go`, `Read`)
- ❌ (`src/cmd/go/internal/modfetch/cache.go`, `Versions`)
- ❌ (`src/cmd/go/internal/modfetch/cache.go`, `Stat`)
- ❌ (`src/cmd/go/internal/modfetch/cache.go`, `Latest`)
- ❌ (`src/cmd/go/internal/modfetch/cache.go`, `GoMod`)
- ❌ (`src/plugin/plugin_dlopen.go`, `open`)
- ❌ (`src/plugin/plugin_dlopen.go`, `lastmoduleinit`)
- ❌ (`src/html/template/content_test.go`, `TestTypedContent`)
- ❌ (`src/html/template/content_test.go`, `TestEscapingNilNonemptyInterfaces`)
- ❌ (`src/html/template/js.go`, `jsValEscaper`)
- ❌ (`src/sync/pool_test.go`, `TestPoolNew`)
- ❌ (`src/sync/pool_test.go`, `TestPoolStress`)
- ❌ (`src/sync/pool_test.go`, `BenchmarkPoolSTW`)
- ❌ (`src/sync/pool_test.go`, `BenchmarkPoolExpensiveNew`)
- ❌ (`src/sync/atomic/value.go`, `CompareAndSwap`)
- ❌ (`src/crypto/x509/name_constraints_test.go`, `TestConstraintCases`)
- ❌ (`src/cmd/compile/internal/base/timings.go`, `add`)
- ❌ (`src/cmd/asm/internal/asm/parse.go`, `errorf`)
- ❌ (`src/cmd/fix/fix.go`, `renameTop`)
- ❌ (`src/net/lookup.go`, `lookupIPAddr`)
- ❌ (`src/net/lookup.go`, `ipAddrsEface`)
- ❌ (`src/cmd/compile/internal/importer/testdata/exports.go`, `F5`)
- ❌ (`src/runtime/race/testdata/pool_test.go`, `TestRacePool`)
- ❌ (`src/runtime/race/testdata/pool_test.go`, `TestNoRacePool`)
- ❌ (`src/internal/fmtsort/sort_test.go`, `TestInterface`)
- ❌ (`src/runtime/abi_test.go`, `TestFinalizerRegisterABI`)
- ❌ (`src/encoding/asn1/asn1.go`, `parseField`)
- ❌ (`src/cmd/doc/pkg.go`, `emit`)
- ❌ (`src/cmd/internal/buildid/buildid_test.go`, `TestFindAndHash`)
- ❌ (`src/runtime/cgo/handle_test.go`, `TestHandle`)
- ❌ (`src/math/rand/regress_test.go`, `TestRegress`)
- ❌ (`src/go/doc/testdata/testing.go`, `RunTests`)
- ❌ (`src/sync/atomic/value_test.go`, `TestValueConcurrent`)
- ❌ (`src/reflect/export_test.go`, `gcbits`)
- ❌ (`src/encoding/gob/timing_test.go`, `BenchmarkEndToEndPipe`)
- ❌ (`src/encoding/gob/timing_test.go`, `BenchmarkEndToEndByteBuffer`)
- ❌ (`src/encoding/gob/timing_test.go`, `BenchmarkEndToEndSliceByteBuffer`)
- ❌ (`src/encoding/gob/timing_test.go`, `BenchmarkEncodeInterfaceSlice`)
- ❌ (`src/encoding/gob/timing_test.go`, `BenchmarkDecodeInterfaceSlice`)
- ❌ (`src/go/doc/testdata/benchmark.go`, `RunBenchmarks`)
- ❌ (`src/go/doc/testdata/benchmark.go`, `Benchmark`)
- ❌ (`src/syscall/js/js_test.go`, `TestFuncOf`)
- ❌ (`src/syscall/js/js_test.go`, `TestInvokeFunction`)
- ❌ (`src/syscall/js/js_test.go`, `TestInterleavedFunctions`)
- ❌ (`src/syscall/js/js_test.go`, `ExampleFuncOf`)
- ❌ (`src/syscall/js/js_test.go`, `TestGlobal`)
- ❌ (`src/syscall/syscall_windows.go`, `compileCallback`)
- ❌ (`src/cmd/go/internal/modfetch/coderepo.go`, `convert`)
- ❌ (`src/html/template/escape_test.go`, `TestEscape`)
- ❌ (`src/html/template/escape_test.go`, `TestEscapeSet`)
- ❌ (`src/html/template/escape_test.go`, `TestRedundantFuncs`)
- ❌ (`src/html/template/example_test.go`, `Example_escape`)
- ❌ (`src/cmd/pack/pack_test.go`, `TestLargeDefs`)
- ❌ (`src/runtime/sizeof_test.go`, `TestSizeof`)
- ❌ (`src/fmt/fmt_test.go`, `TestFmtInterface`)
- ❌ (`src/fmt/fmt_test.go`, `BenchmarkSprintfTruncateBytes`)
- ❌ (`src/fmt/fmt_test.go`, `BenchmarkSprintfStructure`)
- ❌ (`src/fmt/fmt_test.go`, `BenchmarkFprintIntNoAlloc`)
- ❌ (`src/encoding/json/decode.go`, `arrayInterface`)
- ❌ (`src/encoding/json/decode.go`, `objectInterface`)
- ❌ (`src/cmd/go/internal/modload/import.go`, `dirInModule`)
- ❌ (`src/runtime/malloc_test.go`, `TestMemStats`)
- ❌ (`src/runtime/race/race_test.go`, `TestIssue8102`)
- ❌ (`src/reflect/abi_test.go`, `TestMethodValueCallABI`)
- ❌ (`src/cmd/cgo/out.go`, `writeExports`)
- ❌ (`src/cmd/link/internal/ld/testdata/deadcode/reflectcall.go`, `main`)
- ❌ (`src/math/bits/make_examples.go`, `main`)
- ❌ (`src/cmd/compile/internal/ir/sizeof_test.go`, `TestSizeof`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `loadPackageData`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `isDir`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `goModPath`)
- ❌ (`src/database/sql/fakedb_test.go`, `prepareInsert`)
- ❌ (`src/database/sql/fakedb_test.go`, `execInsert`)
- ❌ (`src/database/sql/fakedb_test.go`, `QueryContext`)
- ❌ (`src/database/sql/fakedb_test.go`, `colTypeToReflectType`)
- ❌ (`src/cmd/compile/internal/types2/sizeof_test.go`, `TestSizeof`)
- ❌ (`src/reflect/all_test.go`, `TestMapIterSet`)
- ❌ (`src/reflect/all_test.go`, `TestInterfaceGet`)
- ❌ (`src/reflect/all_test.go`, `TestInterfaceValue`)
- ❌ (`src/reflect/all_test.go`, `TestFunctionValue`)
- ❌ (`src/reflect/all_test.go`, `init`)
- ❌ (`src/reflect/all_test.go`, `TestIsNil`)
- ❌ (`src/reflect/all_test.go`, `TestIsZero`)
- ❌ (`src/reflect/all_test.go`, `TestInterfaceExtraction`)
- ❌ (`src/reflect/all_test.go`, `TestMethod5`)
- ❌ (`src/reflect/all_test.go`, `TestInterfaceSet`)
- ❌ (`src/reflect/all_test.go`, `TestImportPath`)
- ❌ (`src/reflect/all_test.go`, `TestPtrToGC`)
- ❌ (`src/reflect/all_test.go`, `TestAllocations`)
- ❌ (`src/reflect/all_test.go`, `TestVariadic`)
- ❌ (`src/reflect/all_test.go`, `TestArrayOf`)
- ❌ (`src/reflect/all_test.go`, `TestArrayOfGC`)
- ❌ (`src/reflect/all_test.go`, `TestSliceOfGC`)
- ❌ (`src/reflect/all_test.go`, `TestStructOf`)
- ❌ (`src/reflect/all_test.go`, `TestStructOfGC`)
- ❌ (`src/reflect/all_test.go`, `TestStructOfWithInterface`)
- ❌ (`src/reflect/all_test.go`, `TestChanOfGC`)
- ❌ (`src/reflect/all_test.go`, `TestMapOfGCKeys`)
- ❌ (`src/reflect/all_test.go`, `TestMapOfGCValues`)
- ❌ (`src/reflect/all_test.go`, `TestFuncOf`)
- ❌ (`src/reflect/all_test.go`, `TestInvalid`)
- ❌ (`src/reflect/all_test.go`, `TestFuncLayout`)
- ❌ (`src/reflect/all_test.go`, `TestGCBits`)
- ❌ (`src/reflect/all_test.go`, `TestExported`)
- ❌ (`src/reflect/all_test.go`, `TestSwapper`)
- ❌ (`src/cmd/go/internal/modfetch/repo.go`, `Lookup`)
- ❌ (`src/internal/singleflight/singleflight_test.go`, `TestDo`)
- ❌ (`src/internal/singleflight/singleflight_test.go`, `TestDoErr`)
- ❌ (`src/internal/singleflight/singleflight_test.go`, `TestDoDupSuppress`)
- ❌ (`src/net/rpc/debug.go`, `ServeHTTP`)
- ❌ (`src/debug/pe/file.go`, `readOptionalHeader`)

### 📊 Proposal #33920

#### File Embeddings - Directory Level
- ✅ `src/io/ioutil`
- ❌ `src/os`

#### File Embeddings - File Level
- ✅ `src/io/ioutil/tempfile.go`
- ✅ `src/io/ioutil/tempfile_test.go`
- ❌ `src/os/os_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/io/ioutil`
- ❌ `src/os`

#### Function Embeddings - File Level
- ❌ `src/io/ioutil/tempfile.go`
- ✅ `src/io/ioutil/tempfile_test.go`
- ❌ `src/os/os_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/os/os_test.go`, `TestStatDirWithTrailingSlash`)
- ❌ (`src/io/ioutil/tempfile_test.go`, `TestTempFile_BadPattern`)
- ❌ (`src/io/ioutil/tempfile_test.go`, `TestTempDir_BadPattern`)
- ❌ (`src/io/ioutil/tempfile.go`, `TempFile`)
- ❌ (`src/io/ioutil/tempfile.go`, `TempDir`)

### 📊 Proposal #34293

#### File Embeddings - Directory Level
- ❌ `src/cmd/doc`

#### File Embeddings - File Level
- ❌ `src/cmd/doc/main.go`
- ❌ `src/cmd/doc/pkg.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/doc`

#### Function Embeddings - File Level
- ❌ `src/cmd/doc/main.go`
- ❌ `src/cmd/doc/pkg.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/doc/pkg.go`, `packageDoc`)
- ❌ (`src/cmd/doc/main.go`, `do`)

### 📊 Proposal #34527

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/go/internal/clean`
- ❌ `src/cmd/go/internal/envcmd`
- ❌ `src/cmd/go/internal/modfetch`
- ✅ `src/cmd/go/internal/modfetch/codehost`
- ✅ `src/cmd/go/internal/modload`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/go/internal/clean/clean.go`
- ❌ `src/cmd/go/internal/envcmd/env.go`
- ❌ `src/cmd/go/internal/modfetch/cache.go`
- ✅ `src/cmd/go/internal/modfetch/codehost/codehost.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/git_test.go`
- ✅ `src/cmd/go/internal/modfetch/codehost/shell.go`
- ❌ `src/cmd/go/internal/modfetch/coderepo_test.go`
- ❌ `src/cmd/go/internal/modfetch/fetch.go`
- ❌ `src/cmd/go/internal/modfetch/sumdb.go`
- ✅ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/modload/query_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/go/internal/clean`
- ❌ `src/cmd/go/internal/envcmd`
- ✅ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ❌ `src/cmd/go/internal/modload`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/go/internal/clean/clean.go`
- ❌ `src/cmd/go/internal/envcmd/env.go`
- ✅ `src/cmd/go/internal/modfetch/cache.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/codehost.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/git_test.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/shell.go`
- ❌ `src/cmd/go/internal/modfetch/coderepo_test.go`
- ✅ `src/cmd/go/internal/modfetch/fetch.go`
- ❌ `src/cmd/go/internal/modfetch/sumdb.go`
- ❌ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/modload/query_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/modfetch/codehost/codehost.go`, `WorkDir`)
- ❌ (`src/cmd/go/internal/envcmd/env.go`, `MkEnv`)
- ❌ (`src/cmd/go/internal/modfetch/codehost/shell.go`, `main`)
- ❌ (`src/cmd/go/internal/clean/clean.go`, `runClean`)
- ❌ (`src/cmd/go/internal/modfetch/codehost/git_test.go`, `testMain`)
- ❌ (`src/cmd/go/internal/cfg/cfg.go`, `gopathDir`)
- ❌ (`src/cmd/go/internal/modfetch/coderepo_test.go`, `testMain`)
- ❌ (`src/cmd/go/internal/modfetch/sumdb.go`, `ReadConfig`)
- ❌ (`src/cmd/go/internal/modfetch/sumdb.go`, `WriteConfig`)
- ❌ (`src/cmd/go/internal/modfetch/sumdb.go`, `ReadCache`)
- ❌ (`src/cmd/go/internal/modfetch/sumdb.go`, `WriteCache`)
- ✅ (`src/cmd/go/internal/modfetch/cache.go`, `cacheDir`)
- ❌ (`src/cmd/go/internal/modfetch/cache.go`, `DownloadDir`)
- ❌ (`src/cmd/go/internal/modfetch/cache.go`, `SideLock`)
- ❌ (`src/cmd/go/internal/modfetch/cache.go`, `readDiskStatByHash`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `Init`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `WillBeEnabled`)
- ❌ (`src/cmd/go/internal/modload/query_test.go`, `testMain`)
- ✅ (`src/cmd/go/internal/modfetch/fetch.go`, `Download`)
- ❌ (`src/cmd/go/internal/modfetch/fetch.go`, `checkMod`)
- ❌ (`src/cmd/go/internal/modfetch/fetch.go`, `Sum`)

### 📊 Proposal #34626

#### File Embeddings - Directory Level
- ❌ `src/testing`

#### File Embeddings - File Level
- ❌ `src/testing/benchmark.go`
- ❌ `src/testing/benchmark_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/testing`

#### Function Embeddings - File Level
- ❌ `src/testing/benchmark.go`
- ❌ `src/testing/benchmark_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/testing/benchmark.go`, `launch`)
- ❌ (`src/testing/benchmark.go`, `String`)
- ❌ (`src/testing/benchmark.go`, `prettyPrint`)
- ❌ (`src/testing/benchmark_test.go`, `TestPrettyPrint`)
- ❌ (`src/testing/benchmark_test.go`, `TestResultString`)
- ❌ (`src/testing/benchmark.go`, `prettyPrint`)
- ❌ (`src/testing/benchmark_test.go`, `TestResultString`)
- ❌ (`src/testing/benchmark_test.go`, `TestReportMetric`)

### 📊 Proposal #34652

#### File Embeddings - Directory Level
- ❌ `src/html/template`
- ❌ `src/text/template`
- ✅ `src/text/template/parse`

#### File Embeddings - File Level
- ❌ `src/html/template/escape.go`
- ❌ `src/html/template/template_test.go`
- ❌ `src/text/template/exec.go`
- ❌ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/lex_test.go`
- ❌ `src/text/template/parse/node.go`
- ✅ `src/text/template/parse/parse.go`
- ❌ `src/text/template/parse/parse_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/html/template`
- ❌ `src/text/template`
- ✅ `src/text/template/parse`

#### Function Embeddings - File Level
- ❌ `src/html/template/escape.go`
- ✅ `src/html/template/template_test.go`
- ❌ `src/text/template/exec.go`
- ✅ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/lex_test.go`
- ❌ `src/text/template/parse/node.go`
- ❌ `src/text/template/parse/parse.go`
- ✅ `src/text/template/parse/parse_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/html/template/escape.go`, `escape`)
- ✅ (`src/text/template/parse/parse_test.go`, `TestParseWithComments`)
- ❌ (`src/text/template/parse/lex_test.go`, `collect`)
- ❌ (`src/text/template/parse/node.go`, `newComment`)
- ❌ (`src/text/template/parse/node.go`, `String`)
- ❌ (`src/text/template/parse/node.go`, `writeTo`)
- ❌ (`src/text/template/parse/node.go`, `tree`)
- ❌ (`src/text/template/parse/node.go`, `Copy`)
- ❌ (`src/text/template/parse/lex.go`, `lex`)
- ✅ (`src/text/template/parse/lex.go`, `lexComment`)
- ✅ (`src/html/template/template_test.go`, `TestSkipEscapeComments`)
- ❌ (`src/text/template/exec.go`, `walk`)
- ❌ (`src/text/template/parse/parse.go`, `Parse`)
- ❌ (`src/text/template/parse/parse.go`, `add`)
- ❌ (`src/text/template/parse/parse.go`, `IsEmptyTree`)
- ❌ (`src/text/template/parse/parse.go`, `parse`)
- ❌ (`src/text/template/parse/parse.go`, `itemList`)
- ❌ (`src/text/template/parse/parse.go`, `textOrAction`)
- ❌ (`src/text/template/parse/parse.go`, `blockControl`)
- ❌ (`src/text/template/parse/parse.go`, `term`)
- ❌ (`src/text/template/parse/parse_test.go`, `TestSkipFuncCheck`)
- ❌ (`src/text/template/parse/parse.go`, `term`)

### 📊 Proposal #34875

#### File Embeddings - Directory Level
- ❌ `src/go/doc`

#### File Embeddings - File Level
- ❌ `src/go/doc/comment.go`

#### Function Embeddings - Directory Level
- ✅ `src/go/doc`

#### Function Embeddings - File Level
- ❌ `src/go/doc/comment.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/doc/comment.go`, `ToHTML`)
- ❌ (`src/go/doc/comment.go`, `ToText`)

### 📊 Proposal #34974

#### File Embeddings - Directory Level
- ✅ `src/archive/zip`

#### File Embeddings - File Level
- ✅ `src/archive/zip/writer.go`
- ❌ `src/archive/zip/writer_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/archive/zip`

#### Function Embeddings - File Level
- ✅ `src/archive/zip/writer.go`
- ✅ `src/archive/zip/writer_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/archive/zip/writer_test.go`, `TestWriterDirAttributes`)
- ❌ (`src/archive/zip/writer_test.go`, `testCreate`)
- ❌ (`src/archive/zip/writer.go`, `CreateHeader`)
- ❌ (`src/archive/zip/writer.go`, `Write`)
- ❌ (`src/archive/zip/writer.go`, `Write`)
- ✅ (`src/archive/zip/writer.go`, `close`)

### 📊 Proposal #35044

#### File Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### File Embeddings - File Level
- ✅ `src/crypto/x509/cert_pool.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### Function Embeddings - File Level
- ✅ `src/crypto/x509/cert_pool.go`

#### Function Embeddings - Function Level
- ✅ (`src/crypto/x509/cert_pool.go`, `SystemCertPool`)

### 📊 Proposal #35567

#### File Embeddings - Directory Level
- ❌ `src/go/build`
- ❌ `src/runtime/debug`
- ❌ `src/testing`

#### File Embeddings - File Level
- ❌ `src/go/build/deps_test.go`
- ❌ `src/runtime/debug/stack_test.go`
- ❌ `src/testing/benchmark.go`
- ❌ `src/testing/example.go`
- ❌ `src/testing/testing.go`

#### Function Embeddings - Directory Level
- ❌ `src/go/build`
- ❌ `src/runtime/debug`
- ❌ `src/testing`

#### Function Embeddings - File Level
- ❌ `src/go/build/deps_test.go`
- ❌ `src/runtime/debug/stack_test.go`
- ❌ `src/testing/benchmark.go`
- ❌ `src/testing/example.go`
- ❌ `src/testing/testing.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/debug/stack_test.go`, `TestStack`)
- ❌ (`src/testing/benchmark.go`, `RunBenchmarks`)
- ❌ (`src/go/build/deps_test.go`, `findImports`)
- ❌ (`src/testing/example.go`, `RunExamples`)
- ❌ (`src/testing/testing.go`, `CoverMode`)
- ❌ (`src/testing/testing.go`, `Main`)
- ❌ (`src/testing/testing.go`, `MainStart`)
- ❌ (`src/testing/testing.go`, `Run`)
- ❌ (`src/testing/testing.go`, `listTests`)
- ❌ (`src/testing/testing.go`, `RunTests`)
- ❌ (`src/testing/testing.go`, `before`)
- ❌ (`src/testing/testing.go`, `after`)
- ❌ (`src/testing/testing.go`, `writeProfiles`)
- ❌ (`src/testing/testing.go`, `toOutputDir`)
- ❌ (`src/testing/testing.go`, `startAlarm`)
- ❌ (`src/testing/testing.go`, `stopAlarm`)

### 📊 Proposal #35804

#### File Embeddings - Directory Level
- ✅ `src/database/sql`

#### File Embeddings - File Level
- ❌ `src/database/sql/sql.go`
- ❌ `src/database/sql/sql_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/database/sql`

#### Function Embeddings - File Level
- ✅ `src/database/sql/sql.go`
- ✅ `src/database/sql/sql_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/database/sql/sql_test.go`, `TestRowErr`)
- ❌ (`src/database/sql/sql.go`, `Err`)

### 📊 Proposal #35833

#### File Embeddings - Directory Level
- ❌ `src/crypto/elliptic`
- ❌ `src/crypto/rand`
- ❌ `src/crypto/rsa`
- ❌ `src/crypto/x509`
- ✅ `src/math/big`

#### File Embeddings - File Level
- ❌ `src/crypto/elliptic/elliptic.go`
- ❌ `src/crypto/rand/util.go`
- ❌ `src/crypto/rsa/pkcs1v15.go`
- ❌ `src/crypto/x509/sec1.go`
- ❌ `src/math/big/int.go`
- ❌ `src/math/big/int_test.go`
- ❌ `src/math/big/nat.go`

#### Function Embeddings - Directory Level
- ❌ `src/crypto/elliptic`
- ✅ `src/crypto/rand`
- ❌ `src/crypto/rsa`
- ❌ `src/crypto/x509`
- ✅ `src/math/big`

#### Function Embeddings - File Level
- ❌ `src/crypto/elliptic/elliptic.go`
- ✅ `src/crypto/rand/util.go`
- ❌ `src/crypto/rsa/pkcs1v15.go`
- ❌ `src/crypto/x509/sec1.go`
- ✅ `src/math/big/int.go`
- ❌ `src/math/big/int_test.go`
- ❌ `src/math/big/nat.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/elliptic/elliptic.go`, `GenerateKey`)
- ✅ (`src/crypto/rand/util.go`, `Int`)
- ❌ (`src/math/big/int.go`, `FillBytes`)
- ❌ (`src/crypto/elliptic/elliptic.go`, `GenerateKey`)
- ❌ (`src/crypto/elliptic/elliptic.go`, `Marshal`)
- ❌ (`src/crypto/elliptic/elliptic.go`, `Unmarshal`)
- ❌ (`src/math/big/nat.go`, `bytes`)
- ❌ (`src/crypto/x509/sec1.go`, `marshalECPrivateKeyWithOID`)
- ❌ (`src/math/big/int_test.go`, `TestFillBytes`)
- ❌ (`src/crypto/rsa/pkcs1v15.go`, `EncryptPKCS1v15`)
- ❌ (`src/crypto/rsa/pkcs1v15.go`, `decryptPKCS1v15`)

### 📊 Proposal #35998

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/web`
- ✅ `src/io/ioutil`
- ❌ `src/testing`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/web/file_test.go`
- ✅ `src/io/ioutil/tempfile_test.go`
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/web`
- ❌ `src/io/ioutil`
- ✅ `src/testing`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/web/file_test.go`
- ❌ `src/io/ioutil/tempfile_test.go`
- ✅ `src/testing/testing.go`
- ✅ `src/testing/testing_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/web/file_test.go`, `TestGetFileURL`)
- ❌ (`src/io/ioutil/tempfile_test.go`, `TestTempFile_BadPattern`)
- ❌ (`src/io/ioutil/tempfile_test.go`, `TestTempDir_BadPattern`)
- ✅ (`src/testing/testing.go`, `TempDir`)
- ❌ (`src/testing/testing_test.go`, `TestTempDir`)

### 📊 Proposal #36771

#### File Embeddings - Directory Level
- ✅ `src/strconv`

#### File Embeddings - File Level
- ✅ `src/strconv/atoc.go`
- ✅ `src/strconv/atoc_test.go`
- ✅ `src/strconv/ctoa.go`

#### Function Embeddings - Directory Level
- ✅ `src/strconv`

#### Function Embeddings - File Level
- ✅ `src/strconv/atoc.go`
- ❌ `src/strconv/atoc_test.go`
- ✅ `src/strconv/ctoa.go`

#### Function Embeddings - Function Level
- ❌ (`src/strconv/atoc.go`, `convErr`)
- ✅ (`src/strconv/atoc.go`, `ParseComplex`)
- ❌ (`src/strconv/atoc_test.go`, `TestParseComplex`)
- ✅ (`src/strconv/ctoa.go`, `FormatComplex`)

### 📊 Proposal #37023

#### File Embeddings - Directory Level
- ✅ `src/runtime`
- ❌ `src/runtime/debug`

#### File Embeddings - File Level
- ❌ `src/runtime/debug/panic_test.go`
- ❌ `src/runtime/error.go`
- ❌ `src/runtime/os_plan9.go`
- ✅ `src/runtime/panic.go`
- ❌ `src/runtime/signal_unix.go`
- ❌ `src/runtime/signal_windows.go`

#### Function Embeddings - Directory Level
- ✅ `src/runtime`
- ✅ `src/runtime/debug`

#### Function Embeddings - File Level
- ✅ `src/runtime/debug/panic_test.go`
- ❌ `src/runtime/error.go`
- ❌ `src/runtime/os_plan9.go`
- ✅ `src/runtime/panic.go`
- ❌ `src/runtime/signal_unix.go`
- ❌ `src/runtime/signal_windows.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/error.go`, `Error`)
- ❌ (`src/runtime/error.go`, `Addr`)
- ❌ (`src/runtime/signal_windows.go`, `sigpanic`)
- ✅ (`src/runtime/panic.go`, `panicmemAddr`)
- ✅ (`src/runtime/debug/panic_test.go`, `TestPanicOnFault`)
- ❌ (`src/runtime/signal_unix.go`, `sigpanic`)
- ❌ (`src/runtime/os_plan9.go`, `sigpanic`)

### 📊 Proposal #37033

#### File Embeddings - Directory Level
- ❌ `src/cmd/link/internal/ld`
- ✅ `src/runtime/cgo`

#### File Embeddings - File Level
- ❌ `src/cmd/link/internal/ld/lib.go`
- ✅ `src/runtime/cgo/handle.go`
- ❌ `src/runtime/cgo/handle_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/runtime/cgo`

#### Function Embeddings - File Level
- ❌ `src/cmd/link/internal/ld/lib.go`
- ❌ `src/runtime/cgo/handle.go`
- ❌ `src/runtime/cgo/handle_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/link/internal/ld/lib.go`, `loadlib`)
- ❌ (`src/runtime/cgo/handle.go`, `NewHandle`)
- ❌ (`src/runtime/cgo/handle.go`, `Delete`)
- ❌ (`src/runtime/cgo/handle.go`, `Value`)
- ❌ (`src/runtime/cgo/handle_test.go`, `BenchmarkHandle`)
- ❌ (`src/cmd/link/internal/ld/lib.go`, `loadlib`)
- ❌ (`src/runtime/cgo/handle.go`, `NewHandle`)
- ❌ (`src/runtime/cgo/handle.go`, `Value`)
- ❌ (`src/runtime/cgo/handle.go`, `Delete`)
- ❌ (`src/runtime/cgo/handle_test.go`, `TestHandle`)
- ❌ (`src/runtime/cgo/handle_test.go`, `TestInvalidHandle`)
- ❌ (`src/runtime/cgo/handle_test.go`, `BenchmarkHandle`)

### 📊 Proposal #37112

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/work`
- ✅ `src/runtime`
- ✅ `src/runtime/metrics`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/runtime/export_test.go`
- ❌ `src/runtime/histogram.go`
- ❌ `src/runtime/histogram_test.go`
- ✅ `src/runtime/metrics.go`
- ❌ `src/runtime/metrics/description.go`
- ✅ `src/runtime/metrics/sample.go`
- ❌ `src/runtime/metrics/value.go`
- ✅ `src/runtime/metrics_test.go`
- ❌ `src/runtime/mgc.go`
- ✅ `src/runtime/mstats.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/work`
- ✅ `src/runtime`
- ❌ `src/runtime/metrics`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/work/gc.go`
- ✅ `src/runtime/export_test.go`
- ❌ `src/runtime/histogram.go`
- ❌ `src/runtime/histogram_test.go`
- ✅ `src/runtime/metrics.go`
- ❌ `src/runtime/metrics/description.go`
- ❌ `src/runtime/metrics/sample.go`
- ❌ `src/runtime/metrics/value.go`
- ✅ `src/runtime/metrics_test.go`
- ❌ `src/runtime/mgc.go`
- ❌ `src/runtime/mstats.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/metrics/sample.go`, `Read`)
- ❌ (`src/runtime/metrics/description.go`, `All`)
- ❌ (`src/runtime/metrics/value.go`, `Kind`)
- ❌ (`src/runtime/metrics/value.go`, `Uint64`)
- ❌ (`src/runtime/metrics/value.go`, `Float64`)
- ❌ (`src/runtime/metrics/value.go`, `Float64Histogram`)
- ❌ (`src/runtime/metrics/sample.go`, `runtime_readMetrics`)
- ❌ (`src/runtime/metrics/sample.go`, `Read`)
- ❌ (`src/runtime/metrics_test.go`, `prepareAllMetricsSamples`)
- ✅ (`src/runtime/metrics_test.go`, `TestReadMetrics`)
- ✅ (`src/runtime/metrics_test.go`, `TestReadMetricsConsistency`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `gc`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)
- ❌ (`src/runtime/metrics.go`, `makeStatDepSet`)
- ❌ (`src/runtime/metrics.go`, `difference`)
- ❌ (`src/runtime/metrics.go`, `union`)
- ❌ (`src/runtime/metrics.go`, `empty`)
- ❌ (`src/runtime/metrics.go`, `has`)
- ❌ (`src/runtime/metrics.go`, `compute`)
- ❌ (`src/runtime/metrics.go`, `compute`)
- ❌ (`src/runtime/metrics.go`, `ensure`)
- ❌ (`src/runtime/metrics.go`, `readMetrics`)
- ✅ (`src/runtime/export_test.go`, `ReadMetricsSlow`)
- ✅ (`src/runtime/metrics_test.go`, `TestReadMetrics`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)
- ❌ (`src/runtime/metrics.go`, `compute`)
- ✅ (`src/runtime/metrics_test.go`, `TestReadMetrics`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)
- ❌ (`src/runtime/metrics.go`, `compute`)
- ✅ (`src/runtime/metrics_test.go`, `TestReadMetricsConsistency`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)
- ❌ (`src/runtime/metrics.go`, `float64HistOrInit`)
- ❌ (`src/runtime/histogram_test.go`, `TestTimeHistogram`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)
- ❌ (`src/runtime/histogram.go`, `record`)
- ❌ (`src/runtime/histogram.go`, `timeHistogramMetricsBuckets`)
- ❌ (`src/runtime/export_test.go`, `Count`)
- ❌ (`src/runtime/export_test.go`, `Record`)
- ✅ (`src/runtime/metrics_test.go`, `TestReadMetricsConsistency`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)
- ❌ (`src/runtime/mgc.go`, `gcStart`)
- ❌ (`src/runtime/mgc.go`, `gcMarkDone`)
- ❌ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ❌ (`src/runtime/mstats.go`, `init`)
- ✅ (`src/runtime/metrics_test.go`, `TestReadMetricsConsistency`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)

### 📊 Proposal #37168

#### File Embeddings - Directory Level
- ❌ `src/crypto/rc4`
- ❌ `src/image`

#### File Embeddings - File Level
- ❌ `src/crypto/rc4/rc4.go`
- ❌ `src/crypto/rc4/rc4_test.go`
- ❌ `src/image/image_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/crypto/rc4`
- ❌ `src/image`

#### Function Embeddings - File Level
- ❌ `src/crypto/rc4/rc4.go`
- ❌ `src/crypto/rc4/rc4_test.go`
- ❌ `src/image/image_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/rc4/rc4_test.go`, `TestBlock`)
- ❌ (`src/crypto/rc4/rc4_test.go`, `benchmark`)
- ❌ (`src/crypto/rc4/rc4.go`, `XORKeyStream`)
- ❌ (`src/image/image_test.go`, `TestImage`)
- ❌ (`src/image/image_test.go`, `BenchmarkAt`)
- ❌ (`src/image/image_test.go`, `BenchmarkSet`)
- ❌ (`src/image/image_test.go`, `BenchmarkRGBAAt`)
- ❌ (`src/image/image_test.go`, `BenchmarkRGBASetRGBA`)
- ❌ (`src/image/image_test.go`, `BenchmarkRGBA64At`)
- ❌ (`src/image/image_test.go`, `BenchmarkRGBA64SetRGBA64`)
- ❌ (`src/image/image_test.go`, `BenchmarkNRGBAAt`)
- ❌ (`src/image/image_test.go`, `BenchmarkNRGBASetNRGBA`)
- ❌ (`src/image/image_test.go`, `BenchmarkNRGBA64At`)
- ❌ (`src/image/image_test.go`, `BenchmarkNRGBA64SetNRGBA64`)
- ❌ (`src/image/image_test.go`, `BenchmarkAlphaAt`)
- ❌ (`src/image/image_test.go`, `BenchmarkAlphaSetAlpha`)
- ❌ (`src/image/image_test.go`, `BenchmarkAlpha16At`)
- ❌ (`src/image/image_test.go`, `BenchmarkAlphaSetAlpha16`)
- ❌ (`src/image/image_test.go`, `BenchmarkGrayAt`)
- ❌ (`src/image/image_test.go`, `BenchmarkGraySetGray`)
- ❌ (`src/image/image_test.go`, `BenchmarkGray16At`)
- ❌ (`src/image/image_test.go`, `BenchmarkGraySetGray16`)

### 📊 Proposal #37196

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/typecheck/_builtin`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/runtime`
- ✅ `src/time`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/compile/internal/typecheck/_builtin/runtime.go`
- ❌ `src/cmd/compile/internal/walk/builtin.go`
- ❌ `src/runtime/chan.go`
- ❌ `src/runtime/time.go`
- ❌ `src/time/sleep.go`
- ❌ `src/time/tick_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/typecheck/_builtin`
- ❌ `src/cmd/compile/internal/walk`
- ✅ `src/runtime`
- ❌ `src/time`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/compile/internal/typecheck/_builtin/runtime.go`
- ❌ `src/cmd/compile/internal/walk/builtin.go`
- ❌ `src/runtime/chan.go`
- ✅ `src/runtime/time.go`
- ❌ `src/time/sleep.go`
- ❌ `src/time/tick_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/time/sleep.go`, `syncTimer`)
- ❌ (`src/time/sleep.go`, `NewTimer`)
- ❌ (`src/time/tick_test.go`, `TestChan`)
- ❌ (`src/time/tick_test.go`, `Stop`)
- ❌ (`src/time/tick_test.go`, `Reset`)
- ❌ (`src/time/tick_test.go`, `testTimerChan`)
- ❌ (`src/runtime/time.go`, `trace`)
- ❌ (`src/runtime/time.go`, `trace1`)
- ❌ (`src/runtime/time.go`, `hchan`)
- ❌ (`src/runtime/time.go`, `newTimer`)
- ❌ (`src/runtime/time.go`, `addHeap`)
- ✅ (`src/runtime/time.go`, `maybeRunAsync`)
- ✅ (`src/runtime/time.go`, `stop`)
- ❌ (`src/runtime/time.go`, `modify`)
- ❌ (`src/runtime/time.go`, `unlockAndRun`)
- ❌ (`src/runtime/chan.go`, `timerchandrain`)
- ❌ (`src/runtime/chan.go`, `chanlen`)
- ❌ (`src/runtime/chan.go`, `chancap`)
- ❌ (`src/cmd/compile/internal/typecheck/_builtin/runtime.go`, `chancap`)
- ❌ (`src/runtime/chan.go`, `chancap`)
- ❌ (`src/runtime/chan.go`, `reflectlite_chanlen`)
- ❌ (`src/runtime/chan.go`, `reflect_chancap`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `referenceTypeBuiltin`)
- ❌ (`src/cmd/compile/internal/walk/builtin.go`, `walkLenCap`)
- ❌ (`src/cmd/compile/internal/walk/builtin.go`, `isByteCount`)
- ❌ (`src/cmd/compile/internal/walk/builtin.go`, `isChanLenCap`)

### 📊 Proposal #37255

#### File Embeddings - Directory Level
- ✅ `src/os/signal`

#### File Embeddings - File Level
- ✅ `src/os/signal/example_unix_test.go`
- ❌ `src/os/signal/signal.go`
- ❌ `src/os/signal/signal_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/os/signal`

#### Function Embeddings - File Level
- ✅ `src/os/signal/example_unix_test.go`
- ✅ `src/os/signal/signal.go`
- ✅ `src/os/signal/signal_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/os/signal/signal_test.go`, `TestNotifyContextStop`)
- ❌ (`src/os/signal/signal_test.go`, `TestNotifyContextCancelParent`)
- ❌ (`src/os/signal/signal_test.go`, `TestNotifyContextPrematureCancelParent`)
- ❌ (`src/os/signal/signal_test.go`, `TestNotifyContextSimultaneousStop`)
- ❌ (`src/os/signal/signal_test.go`, `TestNotifyContextStringer`)
- ✅ (`src/os/signal/example_unix_test.go`, `ExampleNotifyContext`)
- ✅ (`src/os/signal/signal.go`, `NotifyContext`)
- ❌ (`src/os/signal/signal.go`, `stop`)
- ❌ (`src/os/signal/signal.go`, `String`)

### 📊 Proposal #37475

#### File Embeddings - Directory Level
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modload`
- ✅ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/version`
- ✅ `src/cmd/go/internal/work`
- ✅ `src/debug/buildinfo`
- ❌ `src/encoding/binary`
- ❌ `src/runtime/debug`

#### File Embeddings - File Level
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/load/flag.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modload/build.go`
- ✅ `src/cmd/go/internal/vcs/vcs.go`
- ❌ `src/cmd/go/internal/vcs/vcs_test.go`
- ❌ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ✅ `src/debug/buildinfo/buildinfo.go`
- ❌ `src/debug/buildinfo/buildinfo_test.go`
- ❌ `src/encoding/binary/binary_test.go`
- ❌ `src/encoding/binary/varint_test.go`
- ❌ `src/runtime/debug/mod.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/version`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/debug/buildinfo`
- ❌ `src/encoding/binary`
- ❌ `src/runtime/debug`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/load/flag.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modload/build.go`
- ❌ `src/cmd/go/internal/vcs/vcs.go`
- ❌ `src/cmd/go/internal/vcs/vcs_test.go`
- ❌ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/debug/buildinfo/buildinfo.go`
- ❌ `src/debug/buildinfo/buildinfo_test.go`
- ❌ `src/encoding/binary/binary_test.go`
- ❌ `src/encoding/binary/varint_test.go`
- ❌ `src/runtime/debug/mod.go`

#### Function Embeddings - Function Level
- ❌ (`src/encoding/binary/varint_test.go`, `testConstant`)
- ❌ (`src/encoding/binary/varint_test.go`, `TestConstants`)
- ❌ (`src/encoding/binary/varint_test.go`, `testVarint`)
- ❌ (`src/encoding/binary/varint_test.go`, `testUvarint`)
- ❌ (`src/encoding/binary/varint_test.go`, `TestBufferTooSmall`)
- ❌ (`src/encoding/binary/varint_test.go`, `TestBufferTooBigWithOverflow`)
- ❌ (`src/encoding/binary/varint_test.go`, `testOverflow`)
- ❌ (`src/encoding/binary/varint_test.go`, `TestOverflow`)
- ❌ (`src/encoding/binary/varint_test.go`, `TestNonCanonicalZero`)
- ❌ (`src/encoding/binary/varint_test.go`, `BenchmarkPutUvarint32`)
- ❌ (`src/encoding/binary/varint_test.go`, `BenchmarkPutUvarint64`)
- ❌ (`src/encoding/binary/binary_test.go`, `testRead`)
- ❌ (`src/encoding/binary/binary_test.go`, `testWrite`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestReadSlice`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestWriteSlice`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestReadBool`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestReadBoolSlice`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestSliceRoundTrip`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestWriteT`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestBlankFields`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestSizeStructCache`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestUnexportedRead`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestReadErrorMsg`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestReadTruncated`)
- ❌ (`src/encoding/binary/binary_test.go`, `testUint64SmallSliceLengthPanics`)
- ❌ (`src/encoding/binary/binary_test.go`, `testPutUint64SmallSliceLengthPanics`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestEarlyBoundsChecks`)
- ❌ (`src/encoding/binary/binary_test.go`, `TestReadInvalidDestination`)
- ❌ (`src/encoding/binary/binary_test.go`, `testReadInvalidDestination`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkReadSlice1000Int32s`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkReadStruct`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkWriteStruct`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkReadInts`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkWriteInts`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkWriteSlice1000Int32s`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkPutUint16`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkPutUint32`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkPutUint64`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkLittleEndianPutUint16`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkLittleEndianPutUint32`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkLittleEndianPutUint64`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkReadFloats`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkWriteFloats`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkReadSlice1000Float32s`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkWriteSlice1000Float32s`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkReadSlice1000Uint8s`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkWriteSlice1000Uint8s`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `load`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `setBuildInfo`)
- ❌ (`src/cmd/go/internal/modload/build.go`, `findModule`)
- ❌ (`src/cmd/go/internal/modload/build.go`, `ModInfoProg`)
- ❌ (`src/debug/buildinfo/buildinfo_test.go`, `TestReadFile`)
- ❌ (`src/runtime/debug/mod.go`, `ReadBuildInfo`)
- ❌ (`src/debug/buildinfo/buildinfo.go`, `ReadFile`)
- ❌ (`src/debug/buildinfo/buildinfo.go`, `Read`)
- ❌ (`src/debug/buildinfo/buildinfo.go`, `readRawBuildInfo`)
- ❌ (`src/debug/buildinfo/buildinfo.go`, `readString`)
- ❌ (`src/debug/buildinfo/buildinfo.go`, `DataStart`)
- ❌ (`src/debug/buildinfo/buildinfo.go`, `imageBase`)
- ❌ (`src/debug/buildinfo/buildinfo.go`, `DataStart`)
- ❌ (`src/debug/buildinfo/buildinfo.go`, `DataStart`)
- ❌ (`src/debug/buildinfo/buildinfo.go`, `DataStart`)
- ❌ (`src/debug/buildinfo/buildinfo_test.go`, `TestReadFile`)
- ❌ (`src/runtime/debug/mod.go`, `ReadBuildInfo`)
- ❌ (`src/debug/buildinfo/buildinfo.go`, `Read`)
- ❌ (`src/cmd/go/internal/version/version.go`, `scanFile`)
- ❌ (`src/cmd/go/internal/vcs/vcs_test.go`, `TestFromDir`)
- ❌ (`src/cmd/go/internal/work/build.go`, `AddBuildFlags`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `setBuildInfo`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `hgStatus`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `gitStatus`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `runOutputVerboseOnly`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `TagSync`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `FromDir`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `Error`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `Is`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `parseGOVCS`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `repoRootFromVCSPaths`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `repoRootForImportDynamic`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `setBuildInfo`)
- ❌ (`src/cmd/go/go_test.go`, `TestLdFlagsLongArgumentsIssue42295`)
- ❌ (`src/cmd/go/internal/work/build.go`, `AddBuildFlags`)
- ❌ (`src/cmd/go/internal/load/flag.go`, `set`)

### 📊 Proposal #37519

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/modget`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/modfetch/repo.go`
- ❌ `src/cmd/go/internal/modfetch/sumdb.go`
- ❌ `src/cmd/go/internal/modget/get.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/modget`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/modfetch/repo.go`
- ❌ `src/cmd/go/internal/modfetch/sumdb.go`
- ❌ `src/cmd/go/internal/modget/get.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/modget/get.go`, `runGet`)
- ❌ (`src/cmd/go/internal/modfetch/repo.go`, `lookupDirect`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `runGet`)
- ❌ (`src/cmd/go/internal/modfetch/sumdb.go`, `useSumDB`)

### 📊 Proposal #37533

#### File Embeddings - Directory Level
- ❌ `src/flag`

#### File Embeddings - File Level
- ❌ `src/flag/flag.go`
- ❌ `src/flag/flag_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/flag`

#### Function Embeddings - File Level
- ❌ `src/flag/flag.go`
- ❌ `src/flag/flag_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/flag/flag.go`, `Parse`)
- ❌ (`src/flag/flag_test.go`, `TestExitCode`)
- ❌ (`src/flag/flag_test.go`, `TestExitCode`)

### 📊 Proposal #37776

#### File Embeddings - Directory Level
- ✅ `src/net/url`

#### File Embeddings - File Level
- ✅ `src/net/url/example_test.go`
- ❌ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/url`

#### Function Embeddings - File Level
- ✅ `src/net/url/example_test.go`
- ✅ `src/net/url/url.go`
- ❌ `src/net/url/url_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/url/url.go`, `Parse`)
- ❌ (`src/net/url/url.go`, `EscapedPath`)
- ❌ (`src/net/url/url.go`, `validEncoded`)
- ✅ (`src/net/url/url.go`, `setFragment`)
- ✅ (`src/net/url/url.go`, `EscapedFragment`)
- ❌ (`src/net/url/url.go`, `String`)
- ✅ (`src/net/url/url.go`, `ResolveReference`)
- ❌ (`src/net/url/url_test.go`, `ufmt`)
- ❌ (`src/net/url/example_test.go`, `ExampleURL_EscapedPath`)
- ✅ (`src/net/url/example_test.go`, `ExampleURL_EscapedFragment`)

### 📊 Proposal #37974

#### File Embeddings - Directory Level
- ❌ `src/go/ast`

#### File Embeddings - File Level
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/go/ast`

#### Function Embeddings - File Level
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/ast/ast.go`, `Text`)
- ❌ (`src/go/ast/ast.go`, `isDirective`)
- ❌ (`src/go/ast/ast_test.go`, `TestIsDirective`)

### 📊 Proposal #38017

#### File Embeddings - Directory Level
- ✅ `src/time`
- ✅ `src/time/tzdata`

#### File Embeddings - File Level
- ❌ `src/time/export_test.go`
- ✅ `src/time/tzdata/tzdata.go`
- ❌ `src/time/tzdata_test.go`
- ✅ `src/time/zoneinfo_read.go`

#### Function Embeddings - Directory Level
- ✅ `src/time`
- ✅ `src/time/tzdata`

#### Function Embeddings - File Level
- ❌ `src/time/export_test.go`
- ✅ `src/time/tzdata/tzdata.go`
- ❌ `src/time/tzdata_test.go`
- ❌ `src/time/zoneinfo_read.go`

#### Function Embeddings - Function Level
- ❌ (`src/time/zoneinfo_read.go`, `registerLoadFromEmbeddedTZData`)
- ❌ (`src/time/zoneinfo_read.go`, `loadLocation`)
- ❌ (`src/time/tzdata/tzdata.go`, `registerLoadFromEmbeddedTZData`)
- ❌ (`src/time/tzdata/tzdata.go`, `init`)
- ❌ (`src/time/tzdata/tzdata.go`, `get4s`)
- ❌ (`src/time/tzdata/tzdata.go`, `get2s`)
- ✅ (`src/time/tzdata/tzdata.go`, `loadFromEmbeddedTZData`)
- ❌ (`src/time/tzdata_test.go`, `TestEmbeddedTZData`)
- ❌ (`src/time/tzdata_test.go`, `equal`)
- ❌ (`src/time/zoneinfo_read.go`, `registerLoadFromEmbeddedTZData`)
- ❌ (`src/time/zoneinfo_read.go`, `loadLocation`)
- ❌ (`src/time/tzdata/tzdata.go`, `registerLoadFromEmbeddedTZData`)
- ❌ (`src/time/tzdata/tzdata.go`, `init`)
- ❌ (`src/time/tzdata/tzdata.go`, `get4s`)
- ❌ (`src/time/tzdata/tzdata.go`, `get2s`)
- ✅ (`src/time/tzdata/tzdata.go`, `loadFromEmbeddedTZData`)
- ❌ (`src/time/export_test.go`, `LoadFromEmbeddedTZData`)
- ❌ (`src/time/zoneinfo_read.go`, `Error`)
- ❌ (`src/time/zoneinfo_read.go`, `readFile`)

### 📊 Proposal #38079

#### File Embeddings - Directory Level
- ❌ `src/net/http/httputil`

#### File Embeddings - File Level
- ❌ `src/net/http/httputil/reverseproxy.go`
- ❌ `src/net/http/httputil/reverseproxy_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/net/http/httputil`

#### Function Embeddings - File Level
- ❌ `src/net/http/httputil/reverseproxy.go`
- ❌ `src/net/http/httputil/reverseproxy_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/http/httputil/reverseproxy_test.go`, `TestXForwardedFor_Omit`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `ServeHTTP`)

### 📊 Proposal #38248

#### File Embeddings - Directory Level
- ✅ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/internal/obj`
- ✅ `src/cmd/internal/obj/wasm`
- ✅ `src/cmd/link/internal/wasm`
- ❌ `src/syscall/js`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/gc/compile.go`
- ❌ `src/cmd/compile/internal/ir/sizeof_test.go`
- ❌ `src/cmd/compile/internal/noder/noder.go`
- ❌ `src/cmd/compile/internal/ssagen/abi.go`
- ❌ `src/cmd/internal/obj/objfile.go`
- ❌ `src/cmd/internal/obj/plist.go`
- ❌ `src/cmd/internal/obj/sym.go`
- ❌ `src/cmd/internal/obj/wasm/wasmobj.go`
- ✅ `src/cmd/link/internal/wasm/asm.go`
- ❌ `src/syscall/js/js_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/internal/obj`
- ✅ `src/cmd/internal/obj/wasm`
- ✅ `src/cmd/link/internal/wasm`
- ❌ `src/syscall/js`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/gc/compile.go`
- ❌ `src/cmd/compile/internal/ir/sizeof_test.go`
- ❌ `src/cmd/compile/internal/noder/noder.go`
- ❌ `src/cmd/compile/internal/ssagen/abi.go`
- ❌ `src/cmd/internal/obj/objfile.go`
- ❌ `src/cmd/internal/obj/plist.go`
- ❌ `src/cmd/internal/obj/sym.go`
- ✅ `src/cmd/internal/obj/wasm/wasmobj.go`
- ✅ `src/cmd/link/internal/wasm/asm.go`
- ❌ `src/syscall/js/js_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `instinit`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `preprocess`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `assemble`)
- ✅ (`src/cmd/link/internal/wasm/asm.go`, `asmb2`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `writeTypeSec`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `writeImportSec`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `fieldsToTypes`)
- ❌ (`src/cmd/internal/obj/objfile.go`, `Aux`)
- ❌ (`src/cmd/internal/obj/objfile.go`, `nAuxSym`)
- ❌ (`src/cmd/internal/obj/objfile.go`, `genFuncInfoSyms`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `preprocess`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `assemble`)
- ❌ (`src/cmd/internal/obj/sym.go`, `traverseFuncAux`)
- ❌ (`src/syscall/js/js_test.go`, `testAdd`)
- ❌ (`src/syscall/js/js_test.go`, `TestWasmImport`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `readWasmImport`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `assignAddress`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `asmb`)
- ✅ (`src/cmd/link/internal/wasm/asm.go`, `asmb2`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `writeSecHeader`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `writeImportSec`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `fieldsToTypes`)
- ❌ (`src/cmd/internal/obj/objfile.go`, `Aux`)
- ❌ (`src/cmd/internal/obj/objfile.go`, `nAuxSym`)
- ❌ (`src/cmd/internal/obj/objfile.go`, `genFuncInfoSyms`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `preprocess`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `assemble`)
- ❌ (`src/cmd/internal/obj/sym.go`, `traverseFuncAux`)
- ❌ (`src/syscall/js/js_test.go`, `testAdd`)
- ❌ (`src/syscall/js/js_test.go`, `TestWasmImport`)
- ❌ (`src/cmd/internal/obj/plist.go`, `InitTextSym`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `readWasmImport`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `assignAddress`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `asmb`)
- ✅ (`src/cmd/link/internal/wasm/asm.go`, `asmb2`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `lookupType`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `writeImportSec`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `fieldsToTypes`)
- ❌ (`src/cmd/internal/obj/objfile.go`, `Aux`)
- ❌ (`src/cmd/internal/obj/objfile.go`, `nAuxSym`)
- ❌ (`src/cmd/internal/obj/objfile.go`, `genFuncInfoSyms`)
- ❌ (`src/cmd/compile/internal/ir/sizeof_test.go`, `TestSizeof`)
- ❌ (`src/cmd/compile/internal/gc/compile.go`, `enqueueFunc`)
- ❌ (`src/cmd/compile/internal/noder/noder.go`, `pragma`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `preprocess`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `assemble`)
- ❌ (`src/cmd/compile/internal/ssagen/abi.go`, `CreateWasmImportWrapper`)
- ❌ (`src/cmd/internal/obj/sym.go`, `traverseFuncAux`)
- ❌ (`src/syscall/js/js_test.go`, `testAdd`)
- ❌ (`src/syscall/js/js_test.go`, `TestWasmImport`)
- ❌ (`src/cmd/internal/obj/plist.go`, `Flushplist`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `readWasmImport`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `assignAddress`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `asmb`)
- ✅ (`src/cmd/link/internal/wasm/asm.go`, `asmb2`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `writeSecHeader`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `writeImportSec`)
- ❌ (`src/cmd/link/internal/wasm/asm.go`, `fieldsToTypes`)

### 📊 Proposal #38627

#### File Embeddings - Directory Level
- ❌ `src/text/template/parse`

#### File Embeddings - File Level
- ❌ `src/text/template/parse/parse.go`

#### Function Embeddings - Directory Level
- ✅ `src/text/template/parse`

#### Function Embeddings - File Level
- ❌ `src/text/template/parse/parse.go`

#### Function Embeddings - Function Level
- ❌ (`src/text/template/parse/parse.go`, `term`)

### 📊 Proposal #38687

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/generate`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/generate/generate.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/generate`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/generate/generate.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/generate/generate.go`, `init`)
- ❌ (`src/cmd/go/internal/generate/generate.go`, `runGenerate`)
- ❌ (`src/cmd/go/internal/generate/generate.go`, `run`)

### 📊 Proposal #38776

#### File Embeddings - Directory Level
- ❌ `src/crypto/internal/boring`
- ❌ `src/crypto/md5`
- ❌ `src/crypto/sha1`
- ❌ `src/crypto/sha256`
- ❌ `src/crypto/sha512`
- ❌ `src/hash/crc32`
- ❌ `src/hash/crc64`
- ❌ `src/hash/fnv`

#### File Embeddings - File Level
- ❌ `src/crypto/internal/boring/sha.go`
- ❌ `src/crypto/md5/md5_test.go`
- ❌ `src/crypto/sha1/sha1.go`
- ❌ `src/crypto/sha1/sha1_test.go`
- ❌ `src/crypto/sha1/sha1block_amd64.go`
- ❌ `src/crypto/sha1/sha1block_arm64.go`
- ❌ `src/crypto/sha1/sha1block_decl.go`
- ❌ `src/crypto/sha256/sha256_test.go`
- ❌ `src/crypto/sha512/sha512_test.go`
- ❌ `src/hash/crc32/crc32_test.go`
- ❌ `src/hash/crc64/crc64_test.go`
- ❌ `src/hash/fnv/fnv_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/crypto/internal/boring`
- ❌ `src/crypto/md5`
- ❌ `src/crypto/sha1`
- ❌ `src/crypto/sha256`
- ❌ `src/crypto/sha512`
- ❌ `src/hash/crc32`
- ❌ `src/hash/crc64`
- ❌ `src/hash/fnv`

#### Function Embeddings - File Level
- ❌ `src/crypto/internal/boring/sha.go`
- ❌ `src/crypto/md5/md5_test.go`
- ❌ `src/crypto/sha1/sha1.go`
- ❌ `src/crypto/sha1/sha1_test.go`
- ❌ `src/crypto/sha1/sha1block_amd64.go`
- ❌ `src/crypto/sha1/sha1block_arm64.go`
- ❌ `src/crypto/sha1/sha1block_decl.go`
- ❌ `src/crypto/sha256/sha256_test.go`
- ❌ `src/crypto/sha512/sha512_test.go`
- ❌ `src/hash/crc32/crc32_test.go`
- ❌ `src/hash/crc64/crc64_test.go`
- ❌ `src/hash/fnv/fnv_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/md5/md5_test.go`, `benchmarkSize`)
- ❌ (`src/crypto/md5/md5_test.go`, `BenchmarkHash8Bytes`)
- ❌ (`src/crypto/md5/md5_test.go`, `BenchmarkHash1K`)
- ❌ (`src/crypto/md5/md5_test.go`, `BenchmarkHash8K`)
- ❌ (`src/crypto/md5/md5_test.go`, `BenchmarkHash8BytesUnaligned`)
- ❌ (`src/crypto/md5/md5_test.go`, `BenchmarkHash1KUnaligned`)
- ❌ (`src/crypto/md5/md5_test.go`, `BenchmarkHash8KUnaligned`)
- ❌ (`src/hash/crc32/crc32_test.go`, `testGoldenCastagnoli`)
- ❌ (`src/hash/crc32/crc32_test.go`, `TestSimple`)
- ❌ (`src/hash/crc32/crc32_test.go`, `TestSlicing`)
- ❌ (`src/hash/crc32/crc32_test.go`, `TestGolden`)
- ❌ (`src/hash/fnv/fnv_test.go`, `testGolden`)
- ❌ (`src/hash/fnv/fnv_test.go`, `testIntegrity`)
- ❌ (`src/hash/crc64/crc64_test.go`, `bench`)
- ❌ (`src/hash/crc64/crc64_test.go`, `BenchmarkCrc64`)
- ❌ (`src/crypto/sha256/sha256_test.go`, `TestGolden`)
- ❌ (`src/crypto/sha256/sha256_test.go`, `TestLargeHashes`)
- ❌ (`src/crypto/sha256/sha256_test.go`, `TestAllocations`)
- ❌ (`src/crypto/sha1/sha1block_amd64.go`, `blockAVX2`)
- ❌ (`src/crypto/sha1/sha1block_amd64.go`, `block`)
- ❌ (`src/crypto/sha1/sha1_test.go`, `TestGolden`)
- ❌ (`src/crypto/sha1/sha1_test.go`, `TestLargeHashes`)
- ❌ (`src/crypto/sha1/sha1_test.go`, `TestAllocations`)
- ❌ (`src/crypto/sha1/sha1block_arm64.go`, `sha1block`)
- ❌ (`src/crypto/sha1/sha1block_arm64.go`, `block`)
- ❌ (`src/crypto/sha1/sha1block_decl.go`, `block`)
- ❌ (`src/crypto/sha1/sha1.go`, `Write`)
- ❌ (`src/crypto/sha512/sha512_test.go`, `testHash`)
- ❌ (`src/crypto/sha512/sha512_test.go`, `TestLargeHashes`)
- ❌ (`src/crypto/sha512/sha512_test.go`, `TestAllocations`)
- ❌ (`src/crypto/internal/boring/sha.go`, `sum`)
- ❌ (`src/crypto/internal/boring/sha.go`, `NewSHA512`)
- ❌ (`src/crypto/internal/boring/sha.go`, `MarshalBinary`)
- ❌ (`src/crypto/sha512/sha512_test.go`, `TestGolden`)
- ❌ (`src/crypto/sha512/sha512_test.go`, `TestAllocations`)
- ❌ (`src/crypto/sha512/sha512_test.go`, `benchmarkSize`)
- ❌ (`src/crypto/internal/boring/sha.go`, `sum`)
- ❌ (`src/crypto/sha256/sha256_test.go`, `TestGolden`)
- ❌ (`src/crypto/sha256/sha256_test.go`, `TestAllocations`)
- ❌ (`src/crypto/sha256/sha256_test.go`, `TestCgo`)
- ❌ (`src/crypto/sha256/sha256_test.go`, `benchmarkSize`)

### 📊 Proposal #38781

#### File Embeddings - Directory Level
- ❌ `src/net/http`
- ✅ `src/testing/iotest`

#### File Embeddings - File Level
- ❌ `src/net/http/transport_test.go`
- ✅ `src/testing/iotest/example_test.go`
- ❌ `src/testing/iotest/logger_test.go`
- ❌ `src/testing/iotest/reader.go`
- ✅ `src/testing/iotest/reader_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/net/http`
- ✅ `src/testing/iotest`

#### Function Embeddings - File Level
- ❌ `src/net/http/transport_test.go`
- ❌ `src/testing/iotest/example_test.go`
- ❌ `src/testing/iotest/logger_test.go`
- ✅ `src/testing/iotest/reader.go`
- ✅ `src/testing/iotest/reader_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/testing/iotest/reader.go`, `ErrReader`)
- ❌ (`src/testing/iotest/reader.go`, `Read`)
- ❌ (`src/testing/iotest/logger_test.go`, `TestReadLogger`)
- ❌ (`src/testing/iotest/logger_test.go`, `TestReadLogger_errorOnRead`)
- ✅ (`src/testing/iotest/reader_test.go`, `TestErrReader`)
- ❌ (`src/testing/iotest/example_test.go`, `ExampleErrReader`)
- ✅ (`src/testing/iotest/reader.go`, `ErrReader`)
- ❌ (`src/testing/iotest/reader.go`, `Read`)
- ❌ (`src/testing/iotest/logger_test.go`, `TestReadLogger_errorOnRead`)
- ✅ (`src/testing/iotest/reader_test.go`, `TestErrReader`)
- ❌ (`src/net/http/transport_test.go`, `TestTransportClosesBodyOnError`)

### 📊 Proposal #39034

#### File Embeddings - Directory Level
- ✅ `src/time`

#### File Embeddings - File Level
- ❌ `src/time/format.go`
- ❌ `src/time/format_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/time`

#### Function Embeddings - File Level
- ❌ `src/time/format.go`
- ❌ `src/time/format_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/time/format.go`, `GoString`)
- ❌ (`src/time/format.go`, `AppendFormat`)
- ❌ (`src/time/format.go`, `quote`)
- ❌ (`src/time/format_test.go`, `TestGoString`)
- ❌ (`src/time/format_test.go`, `TestParseYday`)
- ❌ (`src/time/format_test.go`, `TestQuote`)

### 📊 Proposal #39057

#### File Embeddings - Directory Level
- ✅ `src/log`

#### File Embeddings - File Level
- ❌ `src/log/log_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/log`

#### Function Embeddings - File Level
- ❌ `src/log/log_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/log/log_test.go`, `TestDefault`)

### 📊 Proposal #39178

#### File Embeddings - Directory Level
- ✅ `src/net`

#### File Embeddings - File Level
- ❌ `src/net/lookup.go`
- ❌ `src/net/lookup_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net`

#### Function Embeddings - File Level
- ❌ `src/net/lookup.go`
- ✅ `src/net/lookup_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/lookup_test.go`, `TestLookupContextCancel`)
- ✅ (`src/net/lookup_test.go`, `TestDNSTimeout`)
- ❌ (`src/net/lookup.go`, `lookupIPAddr`)

### 📊 Proposal #39214

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/types`
- ❌ `src/cmd/internal/obj`
- ❌ `src/cmd/internal/obj/x86`
- ✅ `src/internal/cpu`
- ❌ `src/strconv`
- ❌ `src/strings`
- ❌ `src/testing`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/types/pkg.go`
- ❌ `src/cmd/internal/obj/sym.go`
- ❌ `src/cmd/internal/obj/x86/obj6.go`
- ❌ `src/internal/cpu/cpu_no_name.go`
- ❌ `src/internal/cpu/cpu_x86.go`
- ❌ `src/strconv/atof.go`
- ❌ `src/strconv/atof_test.go`
- ❌ `src/strconv/internal_test.go`
- ❌ `src/strings/strings.go`
- ❌ `src/strings/strings_test.go`
- ❌ `src/testing/benchmark.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/types`
- ❌ `src/cmd/internal/obj`
- ❌ `src/cmd/internal/obj/x86`
- ❌ `src/internal/cpu`
- ❌ `src/strconv`
- ❌ `src/strings`
- ✅ `src/testing`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/types/pkg.go`
- ❌ `src/cmd/internal/obj/sym.go`
- ❌ `src/cmd/internal/obj/x86/obj6.go`
- ❌ `src/internal/cpu/cpu_no_name.go`
- ❌ `src/internal/cpu/cpu_x86.go`
- ❌ `src/strconv/atof.go`
- ❌ `src/strconv/atof_test.go`
- ❌ `src/strconv/internal_test.go`
- ❌ `src/strings/strings.go`
- ❌ `src/strings/strings_test.go`
- ✅ `src/testing/benchmark.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/internal/obj/x86/obj6.go`, `preprocess`)
- ❌ (`src/cmd/internal/obj/x86/obj6.go`, `stacksplit`)
- ❌ (`src/strconv/atof_test.go`, `TestParseFloatPrefix`)
- ❌ (`src/strconv/internal_test.go`, `ParseFloatPrefix`)
- ❌ (`src/strconv/atof.go`, `commonPrefixLenIgnoreCase`)
- ❌ (`src/strconv/atof.go`, `special`)
- ❌ (`src/strconv/atof.go`, `set`)
- ❌ (`src/strconv/atof.go`, `readFloat`)
- ❌ (`src/strconv/atof.go`, `atof32`)
- ❌ (`src/strconv/atof.go`, `atof64`)
- ❌ (`src/strconv/atof.go`, `ParseFloat`)
- ❌ (`src/strconv/atof.go`, `parseFloatPrefix`)
- ❌ (`src/internal/cpu/cpu_x86.go`, `doinit`)
- ❌ (`src/internal/cpu/cpu_x86.go`, `appendBytes`)
- ✅ (`src/testing/benchmark.go`, `run`)
- ❌ (`src/testing/benchmark.go`, `Run`)
- ❌ (`src/internal/cpu/cpu_x86.go`, `doinit`)
- ❌ (`src/internal/cpu/cpu_x86.go`, `Name`)
- ❌ (`src/internal/cpu/cpu_x86.go`, `appendBytes`)
- ✅ (`src/testing/benchmark.go`, `run`)
- ❌ (`src/testing/benchmark.go`, `Run`)
- ❌ (`src/internal/cpu/cpu_no_name.go`, `Name`)
- ❌ (`src/cmd/compile/internal/gc/main.go`, `Main`)
- ❌ (`src/cmd/compile/internal/types/pkg.go`, `InternString`)
- ❌ (`src/cmd/internal/obj/sym.go`, `LookupInit`)
- ❌ (`src/strings/strings.go`, `ToLower`)
- ❌ (`src/strings/strings_test.go`, `BenchmarkToLower`)

### 📊 Proposal #39351

#### File Embeddings - Directory Level
- ❌ `src/expvar`
- ✅ `src/sync/atomic`

#### File Embeddings - File Level
- ❌ `src/expvar/expvar.go`
- ❌ `src/expvar/expvar_test.go`
- ❌ `src/sync/atomic/value.go`
- ❌ `src/sync/atomic/value_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/expvar`
- ✅ `src/sync/atomic`

#### Function Embeddings - File Level
- ❌ `src/expvar/expvar.go`
- ❌ `src/expvar/expvar_test.go`
- ❌ `src/sync/atomic/value.go`
- ❌ `src/sync/atomic/value_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/sync/atomic/value_test.go`, `TestValue_Swap`)
- ❌ (`src/sync/atomic/value_test.go`, `TestValueSwapConcurrent`)
- ❌ (`src/sync/atomic/value_test.go`, `TestValue_CompareAndSwap`)
- ❌ (`src/sync/atomic/value_test.go`, `TestValueCompareAndSwapConcurrent`)
- ❌ (`src/sync/atomic/value.go`, `Load`)
- ❌ (`src/sync/atomic/value.go`, `Store`)
- ❌ (`src/sync/atomic/value.go`, `Swap`)
- ❌ (`src/sync/atomic/value.go`, `CompareAndSwap`)
- ❌ (`src/expvar/expvar.go`, `String`)
- ❌ (`src/expvar/expvar.go`, `addKey`)
- ❌ (`src/expvar/expvar.go`, `Get`)
- ❌ (`src/expvar/expvar.go`, `Set`)
- ❌ (`src/expvar/expvar.go`, `Add`)
- ❌ (`src/expvar/expvar.go`, `AddFloat`)
- ❌ (`src/expvar/expvar.go`, `Do`)
- ❌ (`src/expvar/expvar.go`, `Value`)
- ❌ (`src/expvar/expvar.go`, `String`)
- ❌ (`src/expvar/expvar.go`, `Set`)
- ❌ (`src/expvar/expvar.go`, `Publish`)
- ❌ (`src/expvar/expvar.go`, `Get`)
- ❌ (`src/expvar/expvar.go`, `NewFloat`)
- ❌ (`src/expvar/expvar.go`, `NewMap`)
- ❌ (`src/expvar/expvar.go`, `NewString`)
- ❌ (`src/expvar/expvar.go`, `Do`)
- ❌ (`src/expvar/expvar.go`, `memstats`)
- ❌ (`src/expvar/expvar_test.go`, `RemoveAll`)
- ❌ (`src/expvar/expvar_test.go`, `TestString`)

### 📊 Proposal #39444

#### File Embeddings - Directory Level
- ✅ `src/os`

#### File Embeddings - File Level
- ❌ `src/os/exec_unix.go`
- ❌ `src/os/exec_unix_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/os`

#### Function Embeddings - File Level
- ✅ `src/os/exec_unix.go`
- ❌ `src/os/exec_unix_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/os/exec_unix.go`, `signal`)
- ❌ (`src/os/exec_unix_test.go`, `TestErrProcessDone`)

### 📊 Proposal #39557

#### File Embeddings - Directory Level
- ✅ `src/flag`

#### File Embeddings - File Level
- ❌ `src/flag/example_func_test.go`
- ✅ `src/flag/flag.go`
- ❌ `src/flag/flag_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/flag`

#### Function Embeddings - File Level
- ❌ `src/flag/example_func_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/flag/flag.go`, `Func`)
- ❌ (`src/flag/flag.go`, `Func`)
- ❌ (`src/flag/flag_test.go`, `TestEverything`)
- ❌ (`src/flag/flag_test.go`, `TestUserDefinedFunc`)
- ❌ (`src/flag/example_func_test.go`, `ExampleFunc`)

### 📊 Proposal #39567

#### File Embeddings - Directory Level
- ✅ `src/net/http`

#### File Embeddings - File Level
- ❌ `src/net/http/serve_test.go`
- ❌ `src/net/http/server.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/http`

#### Function Embeddings - File Level
- ✅ `src/net/http/serve_test.go`
- ❌ `src/net/http/server.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/http/server.go`, `serve`)
- ❌ (`src/net/http/serve_test.go`, `TestMaxBytesHandler`)
- ❌ (`src/net/http/serve_test.go`, `testMaxBytesHandler`)
- ❌ (`src/net/http/server.go`, `MaxBytesHandler`)

### 📊 Proposal #39904

#### File Embeddings - Directory Level
- ❌ `src/testing`

#### File Embeddings - File Level
- ❌ `src/testing/match.go`
- ❌ `src/testing/match_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/testing`

#### Function Embeddings - File Level
- ✅ `src/testing/match.go`
- ✅ `src/testing/match_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/testing/match_test.go`, `TestSplitRegexp`)
- ❌ (`src/testing/match_test.go`, `TestMatcher`)
- ❌ (`src/testing/match.go`, `newMatcher`)
- ❌ (`src/testing/match.go`, `fullName`)
- ✅ (`src/testing/match.go`, `splitRegexp`)
- ✅ (`src/testing/match_test.go`, `TestSplitRegexp`)
- ❌ (`src/testing/match_test.go`, `TestMatcher`)
- ❌ (`src/testing/match_test.go`, `GoString`)
- ❌ (`src/testing/match.go`, `newMatcher`)
- ❌ (`src/testing/match.go`, `fullName`)
- ❌ (`src/testing/match.go`, `matches`)
- ❌ (`src/testing/match.go`, `verify`)
- ❌ (`src/testing/match.go`, `matches`)
- ❌ (`src/testing/match.go`, `verify`)
- ✅ (`src/testing/match.go`, `splitRegexp`)

### 📊 Proposal #40025

#### File Embeddings - Directory Level
- ✅ `src/io`
- ✅ `src/io/ioutil`
- ❌ `src/os`

#### File Embeddings - File Level
- ✅ `src/io/example_test.go`
- ❌ `src/io/io.go`
- ✅ `src/io/ioutil/example_test.go`
- ✅ `src/io/ioutil/ioutil.go`
- ❌ `src/os/dir.go`
- ❌ `src/os/example_test.go`
- ❌ `src/os/file.go`
- ❌ `src/os/os_test.go`
- ❌ `src/os/read_test.go`
- ❌ `src/os/removeall_test.go`
- ❌ `src/os/tempfile.go`
- ❌ `src/os/tempfile_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/io`
- ✅ `src/io/ioutil`
- ✅ `src/os`

#### Function Embeddings - File Level
- ❌ `src/io/example_test.go`
- ✅ `src/io/io.go`
- ❌ `src/io/ioutil/example_test.go`
- ❌ `src/io/ioutil/ioutil.go`
- ❌ `src/os/dir.go`
- ❌ `src/os/example_test.go`
- ❌ `src/os/file.go`
- ❌ `src/os/os_test.go`
- ❌ `src/os/read_test.go`
- ❌ `src/os/removeall_test.go`
- ❌ `src/os/tempfile.go`
- ❌ `src/os/tempfile_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/io/ioutil/ioutil.go`, `ReadAll`)
- ❌ (`src/io/ioutil/ioutil.go`, `ReadFile`)
- ❌ (`src/io/io.go`, `NopCloser`)
- ❌ (`src/io/io.go`, `Write`)
- ❌ (`src/io/io.go`, `WriteString`)
- ❌ (`src/io/io.go`, `ReadFrom`)
- ❌ (`src/io/ioutil/ioutil.go`, `ReadAll`)
- ❌ (`src/io/ioutil/ioutil.go`, `ReadFile`)
- ❌ (`src/io/ioutil/ioutil.go`, `WriteFile`)
- ❌ (`src/io/ioutil/ioutil.go`, `ReadDir`)
- ❌ (`src/io/example_test.go`, `ExampleReadAll`)
- ❌ (`src/io/ioutil/example_test.go`, `ExampleReadDir`)
- ❌ (`src/io/ioutil/example_test.go`, `ExampleTempDir`)
- ❌ (`src/io/io.go`, `Write`)
- ❌ (`src/io/io.go`, `ReadAll`)
- ❌ (`src/io/ioutil/ioutil.go`, `ReadAll`)
- ❌ (`src/io/ioutil/ioutil.go`, `ReadFile`)
- ❌ (`src/io/ioutil/ioutil.go`, `NopCloser`)
- ❌ (`src/io/example_test.go`, `ExampleReadAll`)
- ❌ (`src/io/io.go`, `CopyBuffer`)
- ❌ (`src/io/io.go`, `Write`)
- ❌ (`src/io/io.go`, `WriteString`)
- ❌ (`src/io/io.go`, `ReadFrom`)
- ❌ (`src/io/io.go`, `NopCloser`)
- ❌ (`src/io/io.go`, `ReadAll`)
- ❌ (`src/io/ioutil/ioutil.go`, `ReadFile`)
- ❌ (`src/io/ioutil/ioutil.go`, `WriteFile`)
- ❌ (`src/io/ioutil/ioutil.go`, `ReadDir`)
- ❌ (`src/io/ioutil/ioutil.go`, `NopCloser`)
- ❌ (`src/os/os_test.go`, `checkSize`)
- ❌ (`src/os/os_test.go`, `TestReadFileProc`)
- ❌ (`src/os/example_test.go`, `ExampleReadDir`)
- ❌ (`src/os/example_test.go`, `ExampleMkdirTemp`)
- ❌ (`src/os/example_test.go`, `ExampleMkdirTemp_suffix`)
- ❌ (`src/os/example_test.go`, `ExampleCreateTemp`)
- ❌ (`src/os/example_test.go`, `ExampleCreateTemp_suffix`)
- ❌ (`src/os/example_test.go`, `ExampleReadFile`)
- ❌ (`src/os/example_test.go`, `ExampleWriteFile`)
- ❌ (`src/os/tempfile.go`, `nextRandom`)
- ❌ (`src/os/tempfile.go`, `CreateTemp`)
- ❌ (`src/os/tempfile.go`, `prefixAndSuffix`)
- ❌ (`src/os/tempfile.go`, `MkdirTemp`)
- ❌ (`src/os/tempfile.go`, `joinPath`)
- ❌ (`src/os/read_test.go`, `checkNamedSize`)
- ❌ (`src/os/read_test.go`, `TestReadFile`)
- ❌ (`src/os/read_test.go`, `TestWriteFile`)
- ❌ (`src/os/read_test.go`, `TestReadOnlyWriteFile`)
- ❌ (`src/os/read_test.go`, `TestReadDir`)
- ❌ (`src/os/dir.go`, `ReadDir`)
- ❌ (`src/os/tempfile_test.go`, `TestCreateTemp`)
- ❌ (`src/os/tempfile_test.go`, `TestCreateTempPattern`)
- ❌ (`src/os/tempfile_test.go`, `TestCreateTempBadPattern`)
- ❌ (`src/os/tempfile_test.go`, `TestMkdirTemp`)
- ❌ (`src/os/tempfile_test.go`, `TestMkdirTempBadDir`)
- ❌ (`src/os/tempfile_test.go`, `TestMkdirTempBadPattern`)
- ❌ (`src/os/file.go`, `ReadFile`)
- ❌ (`src/os/file.go`, `WriteFile`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveAllButReadOnlyAndPathError`)

### 📊 Proposal #40034

#### File Embeddings - Directory Level
- ✅ `src/net/smtp`

#### File Embeddings - File Level
- ✅ `src/net/smtp/smtp.go`
- ✅ `src/net/smtp/smtp_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/smtp`

#### Function Embeddings - File Level
- ✅ `src/net/smtp/smtp.go`
- ✅ `src/net/smtp/smtp_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/smtp/smtp_test.go`, `TestNewClient`)
- ❌ (`src/net/smtp/smtp_test.go`, `TestNewClientWithTLS`)
- ❌ (`src/net/smtp/smtp_test.go`, `TestSendMail`)
- ❌ (`src/net/smtp/smtp_test.go`, `TestSendMailWithAuth`)
- ❌ (`src/net/smtp/smtp_test.go`, `TestTLSConnState`)
- ❌ (`src/net/smtp/smtp.go`, `NewClient`)
- ✅ (`src/net/smtp/smtp.go`, `SendMail`)
- ❌ (`src/net/smtp/smtp.go`, `StartTLS`)
- ❌ (`src/net/smtp/smtp.go`, `Auth`)
- ❌ (`src/net/smtp/smtp.go`, `Mail`)
- ❌ (`src/net/smtp/smtp.go`, `Rcpt`)
- ❌ (`src/net/smtp/smtp.go`, `Close`)
- ✅ (`src/net/smtp/smtp.go`, `SendMail`)

### 📊 Proposal #40082

#### File Embeddings - Directory Level
- ✅ `src/database/sql`

#### File Embeddings - File Level
- ❌ `src/database/sql/fakedb_test.go`
- ❌ `src/database/sql/sql.go`
- ❌ `src/database/sql/sql_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/database/sql`

#### Function Embeddings - File Level
- ❌ `src/database/sql/fakedb_test.go`
- ✅ `src/database/sql/sql.go`
- ✅ `src/database/sql/sql_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/database/sql/sql.go`, `Scan`)
- ✅ (`src/database/sql/sql.go`, `Value`)
- ❌ (`src/database/sql/fakedb_test.go`, `converterForType`)
- ❌ (`src/database/sql/fakedb_test.go`, `colTypeToReflectType`)
- ✅ (`src/database/sql/sql_test.go`, `TestNullInt16Param`)
- ❌ (`src/database/sql/sql_test.go`, `TestNullByteParam`)
- ❌ (`src/database/sql/sql.go`, `Scan`)
- ✅ (`src/database/sql/sql.go`, `Value`)
- ❌ (`src/database/sql/sql.go`, `Scan`)
- ✅ (`src/database/sql/sql.go`, `Value`)
- ❌ (`src/database/sql/fakedb_test.go`, `converterForType`)
- ❌ (`src/database/sql/sql_test.go`, `TestNullByteParam`)
- ❌ (`src/database/sql/sql.go`, `Scan`)
- ✅ (`src/database/sql/sql.go`, `Value`)

### 📊 Proposal #40127

#### File Embeddings - Directory Level
- ❌ `src/encoding/json`

#### File Embeddings - File Level
- ❌ `src/encoding/json/indent.go`
- ❌ `src/encoding/json/stream.go`

#### Function Embeddings - Directory Level
- ✅ `src/encoding/json`

#### Function Embeddings - File Level
- ❌ `src/encoding/json/indent.go`
- ✅ `src/encoding/json/stream.go`

#### Function Embeddings - Function Level
- ❌ (`src/encoding/json/indent.go`, `Indent`)
- ❌ (`src/encoding/json/stream.go`, `Encode`)
- ❌ (`src/encoding/json/stream.go`, `tokenError`)

### 📊 Proposal #40255

#### File Embeddings - Directory Level
- ❌ `src/cmd/asm/internal/asm`
- ✅ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/compile/internal/x86`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/reflect`
- ✅ `src/runtime`
- ❌ `test/codegen`

#### File Embeddings - File Level
- ❌ `src/cmd/asm/internal/asm/endtoend_test.go`
- ❌ `src/cmd/compile/internal/ssa/regalloc.go`
- ❌ `src/cmd/compile/internal/ssa/rewrite386.go`
- ❌ `src/cmd/compile/internal/x86/galign.go`
- ❌ `src/cmd/compile/internal/x86/ssa.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/util_gc.go`
- ❌ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/runtime/mkpreempt.go`
- ❌ `test/codegen/arithmetic.go`
- ❌ `test/codegen/floats.go`
- ❌ `test/codegen/math.go`
- ❌ `test/codegen/memops.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/asm/internal/asm`
- ✅ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/compile/internal/x86`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/reflect`
- ❌ `src/runtime`
- ❌ `test/codegen`

#### Function Embeddings - File Level
- ❌ `src/cmd/asm/internal/asm/endtoend_test.go`
- ❌ `src/cmd/compile/internal/ssa/regalloc.go`
- ❌ `src/cmd/compile/internal/ssa/rewrite386.go`
- ❌ `src/cmd/compile/internal/x86/galign.go`
- ❌ `src/cmd/compile/internal/x86/ssa.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/util_gc.go`
- ❌ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/runtime/mkpreempt.go`
- ❌ `test/codegen/arithmetic.go`
- ❌ `test/codegen/floats.go`
- ❌ `test/codegen/math.go`
- ❌ `test/codegen/memops.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/compile/internal/x86/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/go/internal/cfg/cfg.go`, `GetArchEnv`)
- ❌ (`test/codegen/memops.go`, `idxFloat32`)
- ❌ (`test/codegen/memops.go`, `idxFloat64`)
- ❌ (`src/cmd/compile/internal/x86/galign.go`, `Init`)
- ❌ (`src/cmd/dist/util_gc.go`, `useVFPv1`)
- ❌ (`src/reflect/all_test.go`, `TestConvertNaNs`)
- ❌ (`test/codegen/floats.go`, `Mul2`)
- ❌ (`test/codegen/floats.go`, `DivPow2`)
- ❌ (`test/codegen/floats.go`, `indexStore`)
- ❌ (`src/cmd/asm/internal/asm/endtoend_test.go`, `Test386EndToEnd`)
- ❌ (`src/cmd/asm/internal/asm/endtoend_test.go`, `TestARMEndToEnd`)
- ❌ (`src/cmd/compile/internal/ssa/regalloc.go`, `init`)
- ❌ (`src/cmd/compile/internal/ssa/regalloc.go`, `regalloc`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_Op386ADDSD`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_Op386ADDSS`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_Op386DIVSD`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_Op386DIVSS`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_Op386MULSD`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_Op386MULSS`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_Op386SUBSD`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_Op386SUBSDload`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_Op386SUBSS`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_Op386SUBSSload`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_OpNeg64F`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_OpNeq16`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_OpNeq32`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_OpNeq32F`)
- ❌ (`src/cmd/compile/internal/ssa/rewrite386.go`, `rewriteValue386_OpNeq64F`)
- ❌ (`test/codegen/arithmetic.go`, `MulMemSrc`)
- ❌ (`test/codegen/arithmetic.go`, `DivMemSrc`)
- ❌ (`test/codegen/arithmetic.go`, `FloatDivs`)
- ❌ (`src/cmd/dist/build.go`, `xinit`)
- ❌ (`src/cmd/dist/build.go`, `cmdenv`)
- ❌ (`test/codegen/math.go`, `sqrt`)
- ❌ (`src/runtime/mkpreempt.go`, `gen386`)
- ❌ (`src/runtime/mkpreempt.go`, `genAMD64`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `buildActionID`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `printLinkerConfig`)

### 📊 Proposal #40276

#### File Embeddings - Directory Level
- ✅ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/work`

#### File Embeddings - File Level
- ✅ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/work/build.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/go/internal/modload`
- ✅ `src/cmd/go/internal/work`

#### Function Embeddings - File Level
- ✅ `src/cmd/go/internal/modload/init.go`
- ✅ `src/cmd/go/internal/work/build.go`

#### Function Embeddings - Function Level
- ✅ (`src/cmd/go/internal/work/build.go`, `runInstall`)
- ❌ (`src/cmd/go/internal/work/build.go`, `installOutsideModule`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `BinDir`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `Init`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `WillBeEnabled`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `Enabled`)

### 📊 Proposal #40281

#### File Embeddings - Directory Level
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- ❌ `src/reflect`

#### File Embeddings - File Level
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- ❌ `src/reflect/type.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- ❌ `src/reflect`

#### Function Embeddings - File Level
- ✅ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- ❌ `src/reflect/type.go`

#### Function Embeddings - Function Level
- ❌ (`src/reflect/type.go`, `Lookup`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`, `validateStructTag`)

### 📊 Proposal #40337

#### File Embeddings - Directory Level
- ❌ `src/crypto/x509`

#### File Embeddings - File Level
- ❌ `src/crypto/x509/x509.go`
- ❌ `src/crypto/x509/x509_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/crypto/x509`

#### Function Embeddings - File Level
- ❌ `src/crypto/x509/x509.go`
- ❌ `src/crypto/x509/x509_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/x509/x509_test.go`, `TestVerifyCertificateWithDSASignature`)
- ❌ (`src/crypto/x509/x509.go`, `checkSignature`)
- ❌ (`src/crypto/x509/x509.go`, `CheckCRLSignature`)

### 📊 Proposal #40356

#### File Embeddings - Directory Level
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods`

#### File Embeddings - File Level
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf/printf.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer/sigchanyzer.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods/stdmethods.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods`

#### Function Embeddings - File Level
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf/printf.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer/sigchanyzer.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods/stdmethods.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf/printf.go`, `checkPrintf`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer/sigchanyzer.go`, `run`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods/stdmethods.go`, `canonicalMethod`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods/stdmethods.go`, `implementsError`)

### 📊 Proposal #40357

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/list`
- ❌ `src/cmd/go/internal/modcmd`
- ❌ `src/cmd/go/internal/modload`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/list/list.go`
- ❌ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modcmd/why.go`
- ❌ `src/cmd/go/internal/modload/build.go`
- ❌ `src/cmd/go/internal/modload/list.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/list`
- ❌ `src/cmd/go/internal/modcmd`
- ✅ `src/cmd/go/internal/modload`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/list/list.go`
- ❌ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modcmd/why.go`
- ❌ `src/cmd/go/internal/modload/build.go`
- ❌ `src/cmd/go/internal/modload/list.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/modcmd/download.go`, `runDownload`)
- ❌ (`src/cmd/go/internal/modcmd/why.go`, `runWhy`)
- ❌ (`src/cmd/go/internal/modload/list.go`, `ListModules`)
- ❌ (`src/cmd/go/internal/modload/list.go`, `listModules`)
- ❌ (`src/cmd/go/internal/modload/build.go`, `PackageModuleInfo`)
- ❌ (`src/cmd/go/internal/modload/build.go`, `ModuleInfo`)
- ❌ (`src/cmd/go/internal/modload/build.go`, `moduleInfo`)
- ❌ (`src/cmd/go/internal/list/list.go`, `runList`)

### 📊 Proposal #40481

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/go/types`
- ❌ `src/unsafe`
- ✅ `test`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/ir/expr.go`
- ❌ `src/cmd/compile/internal/ir/fmt.go`
- ❌ `src/cmd/compile/internal/ir/op_string.go`
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/compile/internal/typecheck/builtin.go`
- ❌ `src/cmd/compile/internal/typecheck/func.go`
- ❌ `src/cmd/compile/internal/typecheck/typecheck.go`
- ❌ `src/cmd/compile/internal/walk/builtin.go`
- ❌ `src/cmd/compile/internal/walk/expr.go`
- ❌ `src/go/types/builtins.go`
- ❌ `src/unsafe/unsafe.go`
- ✅ `test/unsafebuiltins.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/go/types`
- ❌ `src/unsafe`
- ✅ `test`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/ir/expr.go`
- ❌ `src/cmd/compile/internal/ir/fmt.go`
- ❌ `src/cmd/compile/internal/ir/op_string.go`
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/compile/internal/typecheck/builtin.go`
- ❌ `src/cmd/compile/internal/typecheck/func.go`
- ❌ `src/cmd/compile/internal/typecheck/typecheck.go`
- ❌ `src/cmd/compile/internal/walk/builtin.go`
- ❌ `src/cmd/compile/internal/walk/expr.go`
- ❌ `src/go/types/builtins.go`
- ❌ `src/unsafe/unsafe.go`
- ✅ `test/unsafebuiltins.go`

#### Function Embeddings - Function Level
- ❌ (`src/unsafe/unsafe.go`, `Add`)
- ❌ (`src/unsafe/unsafe.go`, `Slice`)
- ❌ (`src/go/types/builtins.go`, `builtin`)
- ✅ (`test/unsafebuiltins.go`, `main`)
- ❌ (`test/unsafebuiltins.go`, `assert`)
- ❌ (`test/unsafebuiltins.go`, `mustPanic`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `expr`)
- ❌ (`src/cmd/compile/internal/typecheck/typecheck.go`, `typecheck1`)
- ❌ (`src/cmd/compile/internal/walk/expr.go`, `walkExpr1`)
- ❌ (`src/cmd/compile/internal/ir/op_string.go`, `_`)
- ❌ (`src/cmd/compile/internal/typecheck/builtin.go`, `runtimeTypes`)
- ❌ (`src/cmd/compile/internal/ir/fmt.go`, `exprFmt`)
- ❌ (`src/cmd/compile/internal/ir/expr.go`, `SetOp`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcCall`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcUnsafeAdd`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcUnsafeSlice`)
- ❌ (`src/cmd/compile/internal/walk/builtin.go`, `walkUnsafeSlice`)

### 📊 Proposal #40592

#### File Embeddings - Directory Level
- ❌ `src/encoding/json`
- ❌ `src/reflect`

#### File Embeddings - File Level
- ❌ `src/encoding/json/encode.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/deepequal.go`
- ❌ `src/reflect/set_test.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`

#### Function Embeddings - Directory Level
- ❌ `src/encoding/json`
- ✅ `src/reflect`

#### Function Embeddings - File Level
- ❌ `src/encoding/json/encode.go`
- ✅ `src/reflect/all_test.go`
- ❌ `src/reflect/deepequal.go`
- ❌ `src/reflect/set_test.go`
- ❌ `src/reflect/type.go`
- ✅ `src/reflect/value.go`

#### Function Embeddings - Function Level
- ❌ (`src/reflect/set_test.go`, `TestImplicitMapConversion`)
- ❌ (`src/reflect/deepequal.go`, `deepValueEqual`)
- ❌ (`src/reflect/type.go`, `StructOf`)
- ❌ (`src/reflect/value.go`, `Pointer`)
- ❌ (`src/reflect/value.go`, `Recv`)
- ❌ (`src/reflect/value.go`, `recv`)
- ✅ (`src/reflect/value.go`, `UnsafePointer`)
- ❌ (`src/reflect/all_test.go`, `TestNestedMethods`)
- ❌ (`src/reflect/all_test.go`, `TestEmbeddedMethods`)
- ❌ (`src/reflect/all_test.go`, `TestSlice`)
- ❌ (`src/reflect/all_test.go`, `TestSlice3`)
- ❌ (`src/reflect/all_test.go`, `verifyGCBitsSlice`)
- ❌ (`src/reflect/all_test.go`, `TestMethodValue`)
- ❌ (`src/encoding/json/encode.go`, `encode`)
- ❌ (`src/encoding/json/encode.go`, `encode`)

### 📊 Proposal #40724

#### File Embeddings - Directory Level
- ❌ `src/cmd/asm`
- ❌ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/abi`
- ❌ `src/cmd/compile/internal/amd64`
- ❌ `src/cmd/compile/internal/arm`
- ❌ `src/cmd/compile/internal/arm64`
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/liveness`
- ❌ `src/cmd/compile/internal/mips`
- ❌ `src/cmd/compile/internal/mips64`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/ppc64`
- ❌ `src/cmd/compile/internal/reflectdata`
- ❌ `src/cmd/compile/internal/riscv64`
- ❌ `src/cmd/compile/internal/s390x`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/cmd/compile/internal/wasm`
- ❌ `src/cmd/compile/internal/x86`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/internal/obj`
- ❌ `src/cmd/internal/obj/wasm`
- ❌ `src/cmd/internal/obj/x86`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/cmd/link/internal/loadelf`
- ❌ `src/cmd/link/internal/loader`
- ❌ `src/cmd/link/internal/loadmacho`
- ❌ `src/cmd/link/internal/loadpe`
- ❌ `src/cmd/link/internal/loadxcoff`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl`
- ❌ `src/internal/abi`
- ❌ `src/internal/abi/testdata`
- ❌ `src/math`
- ❌ `src/reflect`
- ❌ `src/runtime`
- ❌ `src/runtime/cgo`
- ❌ `test`
- ✅ `test/codegen`

#### File Embeddings - File Level
- ❌ `src/cmd/asm/internal/asm/asm.go`
- ❌ `src/cmd/asm/internal/asm/endtoend_test.go`
- ❌ `src/cmd/asm/internal/asm/expr_test.go`
- ❌ `src/cmd/asm/internal/asm/line_test.go`
- ❌ `src/cmd/asm/internal/asm/operand_test.go`
- ❌ `src/cmd/asm/internal/asm/parse.go`
- ❌ `src/cmd/asm/internal/asm/pseudo_test.go`
- ❌ `src/cmd/asm/main.go`
- ❌ `src/cmd/cgo/out.go`
- ❌ `src/cmd/compile/internal/abi/abiutils.go`
- ❌ `src/cmd/compile/internal/amd64/ssa.go`
- ❌ `src/cmd/compile/internal/arm/ssa.go`
- ❌ `src/cmd/compile/internal/arm64/ssa.go`
- ❌ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/gc/compile.go`
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/gc/obj.go`
- ❌ `src/cmd/compile/internal/ir/expr.go`
- ❌ `src/cmd/compile/internal/ir/fmt.go`
- ❌ `src/cmd/compile/internal/ir/func.go`
- ❌ `src/cmd/compile/internal/ir/sizeof_test.go`
- ❌ `src/cmd/compile/internal/liveness/plive.go`
- ❌ `src/cmd/compile/internal/mips/ssa.go`
- ❌ `src/cmd/compile/internal/mips64/ssa.go`
- ❌ `src/cmd/compile/internal/noder/lex.go`
- ❌ `src/cmd/compile/internal/ppc64/ssa.go`
- ❌ `src/cmd/compile/internal/reflectdata/alg.go`
- ❌ `src/cmd/compile/internal/reflectdata/reflect.go`
- ❌ `src/cmd/compile/internal/riscv64/ssa.go`
- ❌ `src/cmd/compile/internal/s390x/ssa.go`
- ❌ `src/cmd/compile/internal/ssa/config.go`
- ❌ `src/cmd/compile/internal/ssa/decompose.go`
- ❌ `src/cmd/compile/internal/ssa/expand_calls.go`
- ❌ `src/cmd/compile/internal/ssa/export_test.go`
- ❌ `src/cmd/compile/internal/ssa/func.go`
- ❌ `src/cmd/compile/internal/ssa/location.go`
- ❌ `src/cmd/compile/internal/ssa/op.go`
- ❌ `src/cmd/compile/internal/ssa/regalloc.go`
- ❌ `src/cmd/compile/internal/ssa/rewriteAMD64.go`
- ❌ `src/cmd/compile/internal/ssa/rewritedec64.go`
- ❌ `src/cmd/compile/internal/ssa/stackalloc.go`
- ❌ `src/cmd/compile/internal/ssagen/abi.go`
- ❌ `src/cmd/compile/internal/ssagen/nowb.go`
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/compile/internal/test/clobberdead_test.go`
- ❌ `src/cmd/compile/internal/walk/closure.go`
- ❌ `src/cmd/compile/internal/walk/expr.go`
- ❌ `src/cmd/compile/internal/walk/order.go`
- ❌ `src/cmd/compile/internal/wasm/ssa.go`
- ❌ `src/cmd/compile/internal/x86/ssa.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/internal/obj/link.go`
- ❌ `src/cmd/internal/obj/plist.go`
- ❌ `src/cmd/internal/obj/util.go`
- ❌ `src/cmd/internal/obj/wasm/wasmobj.go`
- ❌ `src/cmd/internal/obj/x86/obj6.go`
- ❌ `src/cmd/internal/objabi/funcid.go`
- ❌ `src/cmd/link/internal/ld/deadcode_test.go`
- ❌ `src/cmd/link/internal/ld/go.go`
- ❌ `src/cmd/link/internal/ld/lib.go`
- ❌ `src/cmd/link/internal/ld/macho.go`
- ❌ `src/cmd/link/internal/ld/main.go`
- ❌ `src/cmd/link/internal/ld/pe.go`
- ❌ `src/cmd/link/internal/ld/symtab.go`
- ❌ `src/cmd/link/internal/loadelf/ldelf.go`
- ❌ `src/cmd/link/internal/loader/loader.go`
- ❌ `src/cmd/link/internal/loadmacho/ldmacho.go`
- ❌ `src/cmd/link/internal/loadpe/ldpe.go`
- ❌ `src/cmd/link/internal/loadxcoff/ldxcoff.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl/asmdecl.go`
- ❌ `src/internal/abi/abi.go`
- ❌ `src/internal/abi/abi_test.go`
- ❌ `src/internal/abi/export_test.go`
- ❌ `src/internal/abi/testdata/x.go`
- ❌ `src/math/acosh.go`
- ❌ `src/math/arith_s390x.go`
- ❌ `src/math/asin.go`
- ❌ `src/math/asinh.go`
- ❌ `src/math/atan.go`
- ❌ `src/math/atan2.go`
- ❌ `src/math/atanh.go`
- ❌ `src/math/cbrt.go`
- ❌ `src/math/dim.go`
- ❌ `src/math/dim_asm.go`
- ❌ `src/math/dim_noasm.go`
- ❌ `src/math/erf.go`
- ❌ `src/math/exp.go`
- ❌ `src/math/exp2_asm.go`
- ❌ `src/math/exp2_noasm.go`
- ❌ `src/math/exp_asm.go`
- ❌ `src/math/exp_noasm.go`
- ❌ `src/math/expm1.go`
- ❌ `src/math/floor.go`
- ❌ `src/math/floor_asm.go`
- ❌ `src/math/floor_noasm.go`
- ❌ `src/math/frexp.go`
- ❌ `src/math/hypot.go`
- ❌ `src/math/hypot_asm.go`
- ❌ `src/math/hypot_noasm.go`
- ❌ `src/math/ldexp.go`
- ❌ `src/math/log.go`
- ❌ `src/math/log10.go`
- ❌ `src/math/log1p.go`
- ❌ `src/math/log_asm.go`
- ❌ `src/math/log_stub.go`
- ❌ `src/math/mod.go`
- ❌ `src/math/modf.go`
- ❌ `src/math/modf_asm.go`
- ❌ `src/math/modf_noasm.go`
- ❌ `src/math/pow.go`
- ❌ `src/math/remainder.go`
- ❌ `src/math/sin.go`
- ❌ `src/math/sinh.go`
- ❌ `src/math/sqrt.go`
- ❌ `src/math/stubs.go`
- ❌ `src/math/tan.go`
- ❌ `src/math/tanh.go`
- ❌ `src/reflect/abi.go`
- ❌ `src/reflect/abi_test.go`
- ❌ `src/reflect/export_test.go`
- ❌ `src/reflect/makefunc.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`
- ❌ `src/runtime/cgo/callbacks.go`
- ❌ `src/runtime/cgocall.go`
- ❌ `src/runtime/debug_test.go`
- ❌ `src/runtime/debugcall.go`
- ❌ `src/runtime/export_debug_test.go`
- ❌ `src/runtime/export_test.go`
- ❌ `src/runtime/gc_test.go`
- ❌ `src/runtime/mbarrier.go`
- ❌ `src/runtime/mgc.go`
- ❌ `src/runtime/mgcmark.go`
- ❌ `src/runtime/mgcscavenge.go`
- ❌ `src/runtime/mgcsweep.go`
- ❌ `src/runtime/mheap.go`
- ❌ `src/runtime/mkduff.go`
- ❌ `src/runtime/mkpreempt.go`
- ❌ `src/runtime/os_netbsd.go`
- ❌ `src/runtime/panic.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/stubs.go`
- ❌ `src/runtime/stubs_amd64.go`
- ❌ `src/runtime/syscall_windows.go`
- ❌ `src/runtime/syscall_windows_test.go`
- ❌ `src/runtime/traceback.go`
- ❌ `src/runtime/traceback_test.go`
- ❌ `test/codegen/clobberdead.go`
- ❌ `test/codegen/clobberdeadreg.go`
- ❌ `test/codegen/structs.go`
- ❌ `test/nosplit.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/asm`
- ❌ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/abi`
- ❌ `src/cmd/compile/internal/amd64`
- ❌ `src/cmd/compile/internal/arm`
- ❌ `src/cmd/compile/internal/arm64`
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/liveness`
- ❌ `src/cmd/compile/internal/mips`
- ❌ `src/cmd/compile/internal/mips64`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/ppc64`
- ❌ `src/cmd/compile/internal/reflectdata`
- ❌ `src/cmd/compile/internal/riscv64`
- ❌ `src/cmd/compile/internal/s390x`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/cmd/compile/internal/wasm`
- ❌ `src/cmd/compile/internal/x86`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/internal/obj`
- ❌ `src/cmd/internal/obj/wasm`
- ❌ `src/cmd/internal/obj/x86`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/cmd/link/internal/loadelf`
- ❌ `src/cmd/link/internal/loader`
- ❌ `src/cmd/link/internal/loadmacho`
- ❌ `src/cmd/link/internal/loadpe`
- ❌ `src/cmd/link/internal/loadxcoff`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl`
- ❌ `src/internal/abi`
- ❌ `src/internal/abi/testdata`
- ❌ `src/math`
- ❌ `src/reflect`
- ❌ `src/runtime`
- ❌ `src/runtime/cgo`
- ❌ `test`
- ❌ `test/codegen`

#### Function Embeddings - File Level
- ❌ `src/cmd/asm/internal/asm/asm.go`
- ❌ `src/cmd/asm/internal/asm/endtoend_test.go`
- ❌ `src/cmd/asm/internal/asm/expr_test.go`
- ❌ `src/cmd/asm/internal/asm/line_test.go`
- ❌ `src/cmd/asm/internal/asm/operand_test.go`
- ❌ `src/cmd/asm/internal/asm/parse.go`
- ❌ `src/cmd/asm/internal/asm/pseudo_test.go`
- ❌ `src/cmd/asm/main.go`
- ❌ `src/cmd/cgo/out.go`
- ❌ `src/cmd/compile/internal/abi/abiutils.go`
- ❌ `src/cmd/compile/internal/amd64/ssa.go`
- ❌ `src/cmd/compile/internal/arm/ssa.go`
- ❌ `src/cmd/compile/internal/arm64/ssa.go`
- ❌ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/gc/compile.go`
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/gc/obj.go`
- ❌ `src/cmd/compile/internal/ir/expr.go`
- ❌ `src/cmd/compile/internal/ir/fmt.go`
- ❌ `src/cmd/compile/internal/ir/func.go`
- ❌ `src/cmd/compile/internal/ir/sizeof_test.go`
- ❌ `src/cmd/compile/internal/liveness/plive.go`
- ❌ `src/cmd/compile/internal/mips/ssa.go`
- ❌ `src/cmd/compile/internal/mips64/ssa.go`
- ❌ `src/cmd/compile/internal/noder/lex.go`
- ❌ `src/cmd/compile/internal/ppc64/ssa.go`
- ❌ `src/cmd/compile/internal/reflectdata/alg.go`
- ❌ `src/cmd/compile/internal/reflectdata/reflect.go`
- ❌ `src/cmd/compile/internal/riscv64/ssa.go`
- ❌ `src/cmd/compile/internal/s390x/ssa.go`
- ❌ `src/cmd/compile/internal/ssa/config.go`
- ❌ `src/cmd/compile/internal/ssa/decompose.go`
- ❌ `src/cmd/compile/internal/ssa/expand_calls.go`
- ❌ `src/cmd/compile/internal/ssa/export_test.go`
- ❌ `src/cmd/compile/internal/ssa/func.go`
- ❌ `src/cmd/compile/internal/ssa/location.go`
- ❌ `src/cmd/compile/internal/ssa/op.go`
- ❌ `src/cmd/compile/internal/ssa/regalloc.go`
- ❌ `src/cmd/compile/internal/ssa/rewriteAMD64.go`
- ❌ `src/cmd/compile/internal/ssa/rewritedec64.go`
- ❌ `src/cmd/compile/internal/ssa/stackalloc.go`
- ❌ `src/cmd/compile/internal/ssagen/abi.go`
- ❌ `src/cmd/compile/internal/ssagen/nowb.go`
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/compile/internal/test/clobberdead_test.go`
- ❌ `src/cmd/compile/internal/walk/closure.go`
- ❌ `src/cmd/compile/internal/walk/expr.go`
- ❌ `src/cmd/compile/internal/walk/order.go`
- ❌ `src/cmd/compile/internal/wasm/ssa.go`
- ❌ `src/cmd/compile/internal/x86/ssa.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/internal/obj/link.go`
- ❌ `src/cmd/internal/obj/plist.go`
- ❌ `src/cmd/internal/obj/util.go`
- ❌ `src/cmd/internal/obj/wasm/wasmobj.go`
- ❌ `src/cmd/internal/obj/x86/obj6.go`
- ❌ `src/cmd/internal/objabi/funcid.go`
- ❌ `src/cmd/link/internal/ld/deadcode_test.go`
- ❌ `src/cmd/link/internal/ld/go.go`
- ❌ `src/cmd/link/internal/ld/lib.go`
- ❌ `src/cmd/link/internal/ld/macho.go`
- ❌ `src/cmd/link/internal/ld/main.go`
- ❌ `src/cmd/link/internal/ld/pe.go`
- ❌ `src/cmd/link/internal/ld/symtab.go`
- ❌ `src/cmd/link/internal/loadelf/ldelf.go`
- ❌ `src/cmd/link/internal/loader/loader.go`
- ❌ `src/cmd/link/internal/loadmacho/ldmacho.go`
- ❌ `src/cmd/link/internal/loadpe/ldpe.go`
- ❌ `src/cmd/link/internal/loadxcoff/ldxcoff.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl/asmdecl.go`
- ❌ `src/internal/abi/abi.go`
- ❌ `src/internal/abi/abi_test.go`
- ❌ `src/internal/abi/export_test.go`
- ❌ `src/internal/abi/testdata/x.go`
- ❌ `src/math/acosh.go`
- ❌ `src/math/arith_s390x.go`
- ❌ `src/math/asin.go`
- ❌ `src/math/asinh.go`
- ❌ `src/math/atan.go`
- ❌ `src/math/atan2.go`
- ❌ `src/math/atanh.go`
- ❌ `src/math/cbrt.go`
- ❌ `src/math/dim.go`
- ❌ `src/math/dim_asm.go`
- ❌ `src/math/dim_noasm.go`
- ❌ `src/math/erf.go`
- ❌ `src/math/exp.go`
- ❌ `src/math/exp2_asm.go`
- ❌ `src/math/exp2_noasm.go`
- ❌ `src/math/exp_asm.go`
- ❌ `src/math/exp_noasm.go`
- ❌ `src/math/expm1.go`
- ❌ `src/math/floor.go`
- ❌ `src/math/floor_asm.go`
- ❌ `src/math/floor_noasm.go`
- ❌ `src/math/frexp.go`
- ❌ `src/math/hypot.go`
- ❌ `src/math/hypot_asm.go`
- ❌ `src/math/hypot_noasm.go`
- ❌ `src/math/ldexp.go`
- ❌ `src/math/log.go`
- ❌ `src/math/log10.go`
- ❌ `src/math/log1p.go`
- ❌ `src/math/log_asm.go`
- ❌ `src/math/log_stub.go`
- ❌ `src/math/mod.go`
- ❌ `src/math/modf.go`
- ❌ `src/math/modf_asm.go`
- ❌ `src/math/modf_noasm.go`
- ❌ `src/math/pow.go`
- ❌ `src/math/remainder.go`
- ❌ `src/math/sin.go`
- ❌ `src/math/sinh.go`
- ❌ `src/math/sqrt.go`
- ❌ `src/math/stubs.go`
- ❌ `src/math/tan.go`
- ❌ `src/math/tanh.go`
- ❌ `src/reflect/abi.go`
- ❌ `src/reflect/abi_test.go`
- ❌ `src/reflect/export_test.go`
- ❌ `src/reflect/makefunc.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`
- ❌ `src/runtime/cgo/callbacks.go`
- ❌ `src/runtime/cgocall.go`
- ❌ `src/runtime/debug_test.go`
- ❌ `src/runtime/debugcall.go`
- ❌ `src/runtime/export_debug_test.go`
- ❌ `src/runtime/export_test.go`
- ❌ `src/runtime/gc_test.go`
- ❌ `src/runtime/mbarrier.go`
- ❌ `src/runtime/mgc.go`
- ❌ `src/runtime/mgcmark.go`
- ❌ `src/runtime/mgcscavenge.go`
- ❌ `src/runtime/mgcsweep.go`
- ❌ `src/runtime/mheap.go`
- ❌ `src/runtime/mkduff.go`
- ❌ `src/runtime/mkpreempt.go`
- ❌ `src/runtime/os_netbsd.go`
- ❌ `src/runtime/panic.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/stubs.go`
- ❌ `src/runtime/stubs_amd64.go`
- ❌ `src/runtime/syscall_windows.go`
- ❌ `src/runtime/syscall_windows_test.go`
- ❌ `src/runtime/traceback.go`
- ❌ `src/runtime/traceback_test.go`
- ❌ `test/codegen/clobberdead.go`
- ❌ `test/codegen/clobberdeadreg.go`
- ❌ `test/codegen/structs.go`
- ❌ `test/nosplit.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpLsh16x64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpLsh32x64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpLsh64x16`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpLsh64x32`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpLsh64x64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpLsh64x8`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpLsh8x64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpOr32`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh16Ux64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh16x64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh32Ux64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh32x64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh64Ux16`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh64Ux32`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh64Ux64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh64Ux8`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh64x16`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh64x32`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh64x64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh64x8`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh8Ux64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpRsh8x64`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpTrunc64to16`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpTrunc64to32`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpTrunc64to8`)
- ❌ (`src/cmd/compile/internal/ssa/expand_calls.go`, `expandCalls`)
- ❌ (`src/cmd/compile/internal/ssa/decompose.go`, `decomposeBuiltIn`)
- ❌ (`src/cmd/compile/internal/ssa/decompose.go`, `decomposeUserArrayInto`)
- ❌ (`src/cmd/compile/internal/ssa/decompose.go`, `decomposeUserStructInto`)
- ❌ (`src/cmd/compile/internal/ssa/decompose.go`, `deleteNamedVals`)
- ❌ (`src/cmd/compile/internal/ssa/export_test.go`, `SplitSlot`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `asmArgs`)
- ❌ (`src/runtime/stubs.go`, `reflectcall`)
- ❌ (`src/runtime/panic.go`, `gopanic`)
- ❌ (`src/reflect/type.go`, `funcLayout`)
- ❌ (`src/reflect/makefunc.go`, `MakeFunc`)
- ❌ (`src/reflect/makefunc.go`, `makeMethodValue`)
- ❌ (`src/reflect/value.go`, `call`)
- ❌ (`src/reflect/value.go`, `callMethod`)
- ❌ (`src/reflect/value.go`, `makeFloat`)
- ❌ (`src/reflect/value.go`, `call`)
- ❌ (`src/reflect/export_test.go`, `FuncLayout`)
- ❌ (`src/runtime/syscall_windows.go`, `callbackWrap`)
- ❌ (`src/runtime/stubs.go`, `cgocallback`)
- ❌ (`src/runtime/proc.go`, `sigprof`)
- ❌ (`src/runtime/cgo/callbacks.go`, `_cgo_panic`)
- ❌ (`src/cmd/internal/objabi/funcid.go`, `GetFuncID`)
- ❌ (`src/runtime/syscall_windows.go`, `compileCallback`)
- ❌ (`src/runtime/syscall_windows.go`, `callbackWrap`)
- ❌ (`src/runtime/cgocall.go`, `cgocallbackg`)
- ❌ (`src/runtime/cgocall.go`, `cgocallbackg1`)
- ❌ (`src/runtime/cgocall.go`, `unwindm`)
- ❌ (`src/runtime/cgocall.go`, `badcgocallback`)
- ❌ (`src/runtime/cgocall.go`, `cgounimpl`)
- ❌ (`src/cmd/cgo/out.go`, `writeDefs`)
- ❌ (`src/cmd/cgo/out.go`, `writeExports`)
- ❌ (`src/cmd/cgo/out.go`, `writeGccgoExports`)
- ❌ (`src/cmd/compile/internal/gc/main.go`, `Main`)
- ❌ (`src/cmd/link/internal/ld/main.go`, `Main`)
- ❌ (`src/cmd/link/internal/ld/symtab.go`, `putelfsym`)
- ❌ (`src/cmd/internal/obj/x86/obj6.go`, `preprocess`)
- ❌ (`src/cmd/internal/obj/plist.go`, `Flushplist`)
- ❌ (`src/cmd/internal/obj/plist.go`, `InitTextSym`)
- ❌ (`test/nosplit.go`, `main`)
- ❌ (`src/cmd/asm/internal/asm/endtoend_test.go`, `testEndToEnd`)
- ❌ (`src/cmd/asm/internal/asm/endtoend_test.go`, `testErrors`)
- ❌ (`src/cmd/asm/internal/asm/expr_test.go`, `TestExpr`)
- ❌ (`src/cmd/asm/internal/asm/expr_test.go`, `runBadTest`)
- ❌ (`src/cmd/internal/obj/link.go`, `ParseABI`)
- ❌ (`src/cmd/internal/obj/util.go`, `Dconv`)
- ❌ (`src/cmd/internal/obj/util.go`, `DconvWithABIDetail`)
- ❌ (`src/cmd/internal/obj/util.go`, `WriteDconv`)
- ❌ (`src/cmd/internal/obj/util.go`, `writeDconv`)
- ❌ (`src/cmd/internal/obj/util.go`, `WriteNameTo`)
- ❌ (`src/cmd/internal/obj/util.go`, `writeNameTo`)
- ❌ (`src/cmd/internal/obj/util.go`, `abiDecorate`)
- ❌ (`src/cmd/asm/internal/asm/line_test.go`, `testBadInstParser`)
- ❌ (`src/cmd/asm/internal/asm/parse.go`, `NewParser`)
- ❌ (`src/cmd/asm/internal/asm/parse.go`, `symDefRef`)
- ❌ (`src/cmd/asm/internal/asm/parse.go`, `symbolReference`)
- ❌ (`src/cmd/asm/internal/asm/parse.go`, `symRefAttrs`)
- ❌ (`src/cmd/asm/internal/asm/parse.go`, `funcAddress`)
- ❌ (`src/cmd/asm/internal/asm/operand_test.go`, `newParser`)
- ❌ (`src/cmd/asm/internal/asm/operand_test.go`, `testOperandParser`)
- ❌ (`src/cmd/asm/internal/asm/operand_test.go`, `TestAMD64OperandParser`)
- ❌ (`src/cmd/asm/internal/asm/operand_test.go`, `TestFuncAddress`)
- ❌ (`src/cmd/asm/main.go`, `main`)
- ❌ (`src/cmd/asm/internal/asm/pseudo_test.go`, `TestErroneous`)
- ❌ (`src/cmd/compile/internal/ssa/op.go`, `StaticAuxCall`)
- ❌ (`src/cmd/compile/internal/ssa/op.go`, `InterfaceAuxCall`)
- ❌ (`src/cmd/compile/internal/ssa/op.go`, `ClosureAuxCall`)
- ❌ (`src/cmd/compile/internal/ssa/config.go`, `NewConfig`)
- ❌ (`src/cmd/compile/internal/ssa/rewritedec64.go`, `rewriteValuedec64_OpArg`)
- ❌ (`src/cmd/compile/internal/ssa/stackalloc.go`, `stackalloc`)
- ❌ (`src/cmd/compile/internal/ssa/expand_calls.go`, `expandCalls`)
- ❌ (`src/cmd/dist/build.go`, `runInstall`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `asmArgs`)
- ❌ (`src/cmd/asm/main.go`, `main`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl/asmdecl.go`, `run`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `instinit`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `preprocess`)
- ❌ (`src/runtime/mkpreempt.go`, `header`)
- ❌ (`src/runtime/syscall_windows_test.go`, `cSrc`)
- ❌ (`src/runtime/syscall_windows_test.go`, `makeSrc`)
- ❌ (`src/runtime/syscall_windows.go`, `tryMerge`)
- ❌ (`src/runtime/syscall_windows.go`, `compileCallback`)
- ❌ (`src/runtime/syscall_windows.go`, `callbackWrap`)
- ❌ (`src/cmd/link/internal/ld/main.go`, `Main`)
- ❌ (`src/cmd/link/internal/ld/symtab.go`, `putelfsym`)
- ❌ (`src/cmd/internal/obj/x86/obj6.go`, `preprocess`)
- ❌ (`src/cmd/compile/internal/base/flag.go`, `ParseFlags`)
- ❌ (`src/cmd/internal/obj/plist.go`, `Flushplist`)
- ❌ (`src/cmd/internal/obj/plist.go`, `InitTextSym`)
- ❌ (`test/nosplit.go`, `main`)
- ❌ (`src/runtime/stubs.go`, `reflectcall`)
- ❌ (`src/runtime/panic.go`, `gopanic`)
- ❌ (`src/reflect/type.go`, `funcLayout`)
- ❌ (`src/reflect/type.go`, `append`)
- ❌ (`src/reflect/type.go`, `addTypeBits`)
- ❌ (`src/reflect/makefunc.go`, `MakeFunc`)
- ❌ (`src/reflect/makefunc.go`, `makeMethodValue`)
- ❌ (`src/reflect/value.go`, `call`)
- ❌ (`src/reflect/value.go`, `callReflect`)
- ❌ (`src/reflect/value.go`, `callMethod`)
- ❌ (`src/reflect/value.go`, `cvtIntString`)
- ❌ (`src/reflect/value.go`, `call`)
- ❌ (`src/reflect/export_test.go`, `FuncLayout`)
- ❌ (`src/runtime/mbarrier.go`, `reflectcallmove`)
- ❌ (`src/runtime/syscall_windows.go`, `callbackWrap`)
- ❌ (`src/reflect/abi.go`, `dump`)
- ❌ (`src/reflect/abi.go`, `stepsForValue`)
- ❌ (`src/reflect/abi.go`, `addArg`)
- ❌ (`src/reflect/abi.go`, `addRcvr`)
- ❌ (`src/reflect/abi.go`, `regAssign`)
- ❌ (`src/reflect/abi.go`, `assignIntN`)
- ❌ (`src/reflect/abi.go`, `assignFloatN`)
- ❌ (`src/reflect/abi.go`, `stackAssign`)
- ❌ (`src/reflect/abi.go`, `dump`)
- ❌ (`src/reflect/abi.go`, `newAbiDesc`)
- ❌ (`src/internal/abi/abi.go`, `Set`)
- ❌ (`src/internal/abi/abi.go`, `Get`)
- ❌ (`src/cmd/compile/internal/ssa/func.go`, `spSb`)
- ❌ (`src/cmd/compile/internal/ssa/op.go`, `OwnAuxCall`)
- ❌ (`src/cmd/compile/internal/ssa/expand_calls.go`, `isBlockMultiValueExit`)
- ❌ (`src/cmd/compile/internal/ssa/expand_calls.go`, `expandCalls`)
- ❌ (`src/cmd/compile/internal/ir/fmt.go`, `dumpNode`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `buildssa`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `exit`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `canSSA`)
- ❌ (`src/cmd/internal/obj/link.go`, `SpillRegisterArgs`)
- ❌ (`src/cmd/internal/obj/link.go`, `UnspillRegisterArgs`)
- ❌ (`src/cmd/compile/internal/ssa/location.go`, `String`)
- ❌ (`src/cmd/internal/obj/x86/obj6.go`, `stacksplit`)
- ❌ (`src/cmd/compile/internal/noder/lex.go`, `pragmaFlag`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `buildssa`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `call`)
- ❌ (`src/runtime/mkduff.go`, `zeroAMD64`)
- ❌ (`src/runtime/mkduff.go`, `copyAMD64`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `buildssa`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `genssa`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64MOVQstoreconst`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpZero`)
- ❌ (`test/codegen/structs.go`, `Zero1`)
- ❌ (`test/codegen/structs.go`, `Zero2`)
- ❌ (`src/cmd/compile/internal/ssa/op.go`, `OwnAuxCall`)
- ❌ (`src/cmd/compile/internal/amd64/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/amd64/ssa.go`, `ssaGenBlock`)
- ❌ (`src/cmd/compile/internal/ssagen/abi.go`, `makeABIWrapper`)
- ❌ (`src/cmd/compile/internal/ssa/config.go`, `NewConfig`)
- ❌ (`src/cmd/compile/internal/amd64/ssa.go`, `getgFromTLS`)
- ❌ (`src/cmd/compile/internal/amd64/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/amd64/ssa.go`, `ssaGenBlock`)
- ❌ (`src/cmd/compile/internal/ssa/config.go`, `NewConfig`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpGetG`)
- ❌ (`src/cmd/link/internal/ld/lib.go`, `ldshlibsyms`)
- ❌ (`src/runtime/mgcscavenge.go`, `bgscavenge`)
- ❌ (`src/cmd/compile/internal/walk/closure.go`, `directClosureCall`)
- ❌ (`src/runtime/mgcsweep.go`, `bgsweep`)
- ❌ (`src/runtime/export_test.go`, `RunSchedLocalQueueEmptyTest`)
- ❌ (`src/cmd/compile/internal/walk/order.go`, `stmt`)
- ❌ (`src/runtime/mgc.go`, `gcenable`)
- ❌ (`src/runtime/stubs_amd64.go`, `spillArgs`)
- ❌ (`src/runtime/stubs_amd64.go`, `unspillArgs`)
- ❌ (`src/reflect/makefunc.go`, `MakeFunc`)
- ❌ (`src/reflect/makefunc.go`, `makeMethodValue`)
- ❌ (`src/reflect/makefunc.go`, `moveMakeFuncArgPtrs`)
- ❌ (`src/reflect/value.go`, `callReflect`)
- ❌ (`src/reflect/value.go`, `methodReceiver`)
- ❌ (`src/reflect/value.go`, `storeRcvr`)
- ❌ (`src/reflect/value.go`, `callMethod`)
- ❌ (`src/reflect/abi_test.go`, `TestMethodValueCallABI`)
- ❌ (`src/reflect/abi_test.go`, `AllRegsCall`)
- ❌ (`src/reflect/abi_test.go`, `RegsAndStackCall`)
- ❌ (`src/reflect/abi_test.go`, `SpillStructCall`)
- ❌ (`src/reflect/abi_test.go`, `TestReflectCallABI`)
- ❌ (`src/reflect/abi_test.go`, `TestReflectMakeFuncCallABI`)
- ❌ (`src/reflect/abi_test.go`, `callArgsNone`)
- ❌ (`src/reflect/abi_test.go`, `callArgsInt`)
- ❌ (`src/reflect/abi_test.go`, `callArgsInt8`)
- ❌ (`src/reflect/abi_test.go`, `callArgsInt16`)
- ❌ (`src/reflect/abi_test.go`, `callArgsInt32`)
- ❌ (`src/reflect/abi_test.go`, `callArgsInt64`)
- ❌ (`src/reflect/abi_test.go`, `callArgsUint`)
- ❌ (`src/reflect/abi_test.go`, `callArgsUint8`)
- ❌ (`src/reflect/abi_test.go`, `callArgsUint16`)
- ❌ (`src/reflect/abi_test.go`, `callArgsUint32`)
- ❌ (`src/reflect/abi_test.go`, `callArgsUint64`)
- ❌ (`src/reflect/abi_test.go`, `callArgsFloat32`)
- ❌ (`src/reflect/abi_test.go`, `callArgsFloat64`)
- ❌ (`src/reflect/abi_test.go`, `callArgsComplex64`)
- ❌ (`src/reflect/abi_test.go`, `callArgsComplex128`)
- ❌ (`src/reflect/abi_test.go`, `callArgsArray1`)
- ❌ (`src/reflect/abi_test.go`, `callArgsArray`)
- ❌ (`src/reflect/abi_test.go`, `callArgsArray1Mix`)
- ❌ (`src/reflect/abi_test.go`, `callArgsString`)
- ❌ (`src/reflect/abi_test.go`, `callArgsSlice`)
- ❌ (`src/reflect/abi_test.go`, `callArgsPointer`)
- ❌ (`src/reflect/abi_test.go`, `callArgsManyInt`)
- ❌ (`src/reflect/abi_test.go`, `callArgsManyFloat64`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct1`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct2`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct3`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct4`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct5`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct6`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct7`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct8`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct9`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct10`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct11`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct12`)
- ❌ (`src/reflect/abi_test.go`, `callArgsStruct13`)
- ❌ (`src/reflect/abi_test.go`, `callArgs2Struct1`)
- ❌ (`src/reflect/abi_test.go`, `callArgsEmptyStruct`)
- ❌ (`src/reflect/abi.go`, `newAbiDesc`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum2`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum3`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum4`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum5`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum6`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum7`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum8`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum9`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum10`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum9uint8`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum9uint16`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum9int8`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum5mix`)
- ❌ (`src/runtime/syscall_windows_test.go`, `sum5andPair`)
- ❌ (`src/runtime/syscall_windows_test.go`, `getCallbackTestFuncs`)
- ❌ (`src/runtime/syscall_windows_test.go`, `makeSrc`)
- ❌ (`src/runtime/syscall_windows_test.go`, `TestStdcallAndCDeclCallbacks`)
- ❌ (`src/runtime/syscall_windows.go`, `tryMerge`)
- ❌ (`src/runtime/syscall_windows.go`, `assignArg`)
- ❌ (`src/runtime/syscall_windows.go`, `tryRegAssignArg`)
- ❌ (`src/runtime/syscall_windows.go`, `assignReg`)
- ❌ (`src/runtime/syscall_windows.go`, `compileCallback`)
- ❌ (`src/runtime/syscall_windows.go`, `callbackWrap`)
- ❌ (`src/runtime/export_test.go`, `SetIntArgRegs`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `newliveness`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `epilogue`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `compact`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `enableClobber`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `clobber`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `clobber`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `clobberVar`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `clobberWalk`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `clobberPtr`)
- ❌ (`src/cmd/compile/internal/test/clobberdead_test.go`, `TestClobberDead`)
- ❌ (`test/codegen/clobberdead.go`, `F`)
- ❌ (`src/cmd/compile/internal/abi/abiutils.go`, `FrameOffset`)
- ❌ (`src/cmd/compile/internal/abi/abiutils.go`, `updateOffset`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `WriteFuncMap`)
- ❌ (`src/cmd/compile/internal/gc/compile.go`, `enqueueFunc`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `emitOpenDeferInfo`)
- ❌ (`src/cmd/compile/internal/mips64/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/x86/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/ppc64/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/s390x/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/test/clobberdead_test.go`, `TestClobberDead`)
- ❌ (`src/cmd/compile/internal/test/clobberdead_test.go`, `TestClobberDeadReg`)
- ❌ (`src/cmd/compile/internal/test/clobberdead_test.go`, `runHello`)
- ❌ (`src/cmd/compile/internal/ssa/regalloc.go`, `clobberRegs`)
- ❌ (`src/cmd/compile/internal/ssa/regalloc.go`, `init`)
- ❌ (`src/cmd/compile/internal/ssa/regalloc.go`, `regalloc`)
- ❌ (`src/cmd/compile/internal/wasm/ssa.go`, `ssaGenValue`)
- ❌ (`test/codegen/clobberdeadreg.go`, `F`)
- ❌ (`src/cmd/compile/internal/arm/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/mips/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/amd64/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/riscv64/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/arm64/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/internal/obj/x86/obj6.go`, `preprocess`)
- ❌ (`src/internal/abi/abi_test.go`, `TestFuncPC`)
- ❌ (`src/internal/abi/abi_test.go`, `TestFuncPCCompileError`)
- ❌ (`src/internal/abi/testdata/x.go`, `Fn0`)
- ❌ (`src/internal/abi/testdata/x.go`, `test`)
- ❌ (`src/runtime/proc.go`, `oneNewExtraM`)
- ❌ (`src/runtime/proc.go`, `newproc1`)
- ❌ (`src/cmd/compile/internal/walk/expr.go`, `walkCall`)
- ❌ (`src/internal/abi/export_test.go`, `FuncPCTestFn`)
- ❌ (`src/internal/abi/export_test.go`, `FuncPCTest`)
- ❌ (`src/cmd/compile/internal/walk/order.go`, `call`)
- ❌ (`src/cmd/link/internal/ld/symtab.go`, `putelfsym`)
- ❌ (`src/cmd/link/internal/ld/symtab.go`, `mangleABIName`)
- ❌ (`src/cmd/link/internal/ld/pe.go`, `writeSymbols`)
- ❌ (`src/cmd/link/internal/ld/deadcode_test.go`, `TestDeadcode`)
- ❌ (`src/runtime/traceback_test.go`, `TestTracebackArgs`)
- ❌ (`src/runtime/traceback_test.go`, `testTracebackArgs1`)
- ❌ (`src/runtime/traceback_test.go`, `testTracebackArgs2`)
- ❌ (`src/runtime/traceback_test.go`, `testTracebackArgs3`)
- ❌ (`src/runtime/traceback_test.go`, `testTracebackArgs4`)
- ❌ (`src/runtime/traceback_test.go`, `testTracebackArgs5`)
- ❌ (`src/cmd/compile/internal/gc/obj.go`, `addGCLocals`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `emitArgInfo`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `genssa`)
- ❌ (`src/runtime/traceback.go`, `printArgs`)
- ❌ (`src/cmd/compile/internal/walk/expr.go`, `walkExpr1`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `openDeferRecord`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `call`)
- ❌ (`src/cmd/compile/internal/walk/order.go`, `stmt`)
- ❌ (`src/cmd/compile/internal/reflectdata/reflect.go`, `methodWrapper`)
- ❌ (`src/cmd/compile/internal/ir/expr.go`, `FuncName`)
- ❌ (`src/cmd/compile/internal/reflectdata/alg.go`, `hashfor`)
- ❌ (`src/cmd/compile/internal/reflectdata/alg.go`, `hashmem`)
- ❌ (`src/cmd/compile/internal/gc/main.go`, `Main`)
- ❌ (`src/cmd/compile/internal/ssagen/nowb.go`, `newNowritebarrierrecChecker`)
- ❌ (`src/cmd/internal/obj/link.go`, `ABISetOf`)
- ❌ (`src/cmd/internal/obj/link.go`, `Set`)
- ❌ (`src/cmd/internal/obj/link.go`, `Get`)
- ❌ (`src/cmd/internal/obj/link.go`, `String`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `stmt`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `call`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `callTargetLSym`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `deferstruct`)
- ❌ (`src/cmd/compile/internal/ir/func.go`, `NewFunc`)
- ❌ (`src/cmd/compile/internal/ir/sizeof_test.go`, `TestSizeof`)
- ❌ (`src/cmd/internal/obj/wasm/wasmobj.go`, `instinit`)
- ❌ (`src/cmd/compile/internal/ssagen/abi.go`, `NewSymABIs`)
- ❌ (`src/cmd/compile/internal/ssagen/abi.go`, `canonicalize`)
- ❌ (`src/cmd/compile/internal/ssagen/abi.go`, `ReadSymABIs`)
- ❌ (`src/cmd/compile/internal/ssagen/abi.go`, `GenABIWrappers`)
- ❌ (`src/cmd/compile/internal/ssagen/abi.go`, `forEachWrapperABI`)
- ❌ (`src/cmd/compile/internal/ssagen/abi.go`, `makeABIWrapper`)
- ❌ (`src/runtime/mheap.go`, `init`)
- ❌ (`src/runtime/mheap.go`, `freeSpecial`)
- ❌ (`src/runtime/mgcsweep.go`, `sweep`)
- ❌ (`src/runtime/gc_test.go`, `TestGCTestMoveStackOnNextCall`)
- ❌ (`src/runtime/gc_test.go`, `moveStackCheck`)
- ❌ (`src/runtime/gc_test.go`, `TestGCTestIsReachable`)
- ❌ (`src/runtime/gc_test.go`, `TestGCTestPointerClass`)
- ❌ (`src/runtime/mgc.go`, `gcTestMoveStackOnNextCall`)
- ❌ (`src/runtime/mgc.go`, `gcTestIsReachable`)
- ❌ (`src/runtime/mgc.go`, `gcTestPointerClass`)
- ❌ (`src/runtime/export_test.go`, `GCTestIsReachable`)
- ❌ (`src/runtime/export_test.go`, `GCTestPointerClass`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `openDeferRecord`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `call`)
- ❌ (`src/runtime/os_netbsd.go`, `netbsdMstart`)
- ❌ (`src/runtime/os_netbsd.go`, `netbsdMstart0`)
- ❌ (`src/runtime/proc.go`, `newproc`)
- ❌ (`src/runtime/panic.go`, `deferproc`)
- ❌ (`src/runtime/panic.go`, `deferprocStack`)
- ❌ (`src/runtime/panic.go`, `Goexit`)
- ❌ (`src/runtime/panic.go`, `gopanic`)
- ❌ (`src/cmd/compile/internal/amd64/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/ssagen/abi.go`, `GenABIWrappers`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpGetG`)
- ❌ (`src/cmd/link/internal/ld/macho.go`, `machosymtab`)
- ❌ (`src/cmd/compile/internal/reflectdata/reflect.go`, `methodWrapper`)
- ❌ (`src/runtime/debug_test.go`, `TestDebugCall`)
- ❌ (`src/runtime/debug_test.go`, `TestDebugCallLarge`)
- ❌ (`src/runtime/debug_test.go`, `TestDebugCallGC`)
- ❌ (`src/runtime/debug_test.go`, `TestDebugCallGrowStack`)
- ❌ (`src/runtime/debug_test.go`, `debugCallUnsafePointWorker`)
- ❌ (`src/runtime/debug_test.go`, `TestDebugCallUnsafePoint`)
- ❌ (`src/runtime/debug_test.go`, `TestDebugCallPanic`)
- ❌ (`src/runtime/export_debug_test.go`, `InjectDebugCall`)
- ❌ (`src/runtime/export_debug_test.go`, `inject`)
- ❌ (`src/runtime/export_debug_test.go`, `handle`)
- ❌ (`src/runtime/debugcall.go`, `debugCallV2`)
- ❌ (`src/runtime/debugcall.go`, `debugCallWrap`)
- ❌ (`src/runtime/debugcall.go`, `debugCallWrap1`)
- ❌ (`src/runtime/mgcmark.go`, `scanframeworker`)
- ❌ (`src/cmd/link/internal/ld/macho.go`, `domacho`)
- ❌ (`src/cmd/link/internal/loadpe/ldpe.go`, `Load`)
- ❌ (`src/cmd/link/internal/loadelf/ldelf.go`, `Load`)
- ❌ (`src/cmd/link/internal/ld/symtab.go`, `mangleABIName`)
- ❌ (`src/cmd/link/internal/loader/loader.go`, `AddCgoExport`)
- ❌ (`src/cmd/link/internal/loader/loader.go`, `LookupOrCreateCgoExport`)
- ❌ (`src/cmd/compile/internal/ssagen/abi.go`, `GenABIWrappers`)
- ❌ (`src/cmd/link/internal/loadxcoff/ldxcoff.go`, `Load`)
- ❌ (`src/cmd/link/internal/loadmacho/ldmacho.go`, `Load`)
- ❌ (`src/cmd/link/internal/ld/go.go`, `setCgoAttr`)
- ❌ (`src/cmd/link/internal/ld/go.go`, `addexport`)
- ❌ (`src/cmd/asm/internal/asm/asm.go`, `asmText`)
- ❌ (`src/cmd/asm/internal/asm/pseudo_test.go`, `TestErroneous`)
- ❌ (`src/cmd/internal/obj/plist.go`, `Flushplist`)
- ❌ (`src/math/ldexp.go`, `Ldexp`)
- ❌ (`src/math/hypot_noasm.go`, `archHypot`)
- ❌ (`src/math/modf_asm.go`, `archModf`)
- ❌ (`src/math/asin.go`, `Asin`)
- ❌ (`src/math/asin.go`, `Acos`)
- ❌ (`src/math/dim_asm.go`, `archMax`)
- ❌ (`src/math/dim_asm.go`, `archMin`)
- ❌ (`src/math/exp2_asm.go`, `archExp2`)
- ❌ (`src/math/stubs.go`, `archAcos`)
- ❌ (`src/math/stubs.go`, `archAcosh`)
- ❌ (`src/math/stubs.go`, `archAsin`)
- ❌ (`src/math/stubs.go`, `archAsinh`)
- ❌ (`src/math/stubs.go`, `archAtan`)
- ❌ (`src/math/stubs.go`, `archAtan2`)
- ❌ (`src/math/stubs.go`, `archAtanh`)
- ❌ (`src/math/stubs.go`, `archCbrt`)
- ❌ (`src/math/stubs.go`, `archCos`)
- ❌ (`src/math/stubs.go`, `archCosh`)
- ❌ (`src/math/stubs.go`, `archErf`)
- ❌ (`src/math/stubs.go`, `archErfc`)
- ❌ (`src/math/stubs.go`, `archExpm1`)
- ❌ (`src/math/stubs.go`, `archFrexp`)
- ❌ (`src/math/stubs.go`, `archLdexp`)
- ❌ (`src/math/stubs.go`, `archLog10`)
- ❌ (`src/math/stubs.go`, `archLog2`)
- ❌ (`src/math/stubs.go`, `archLog1p`)
- ❌ (`src/math/stubs.go`, `archMod`)
- ❌ (`src/math/stubs.go`, `archPow`)
- ❌ (`src/math/stubs.go`, `archRemainder`)
- ❌ (`src/math/stubs.go`, `archSin`)
- ❌ (`src/math/stubs.go`, `archSinh`)
- ❌ (`src/math/stubs.go`, `archTan`)
- ❌ (`src/math/stubs.go`, `archTanh`)
- ❌ (`src/math/hypot.go`, `Hypot`)
- ❌ (`src/math/expm1.go`, `Expm1`)
- ❌ (`src/math/tan.go`, `Tan`)
- ❌ (`src/math/floor_asm.go`, `archFloor`)
- ❌ (`src/math/floor_asm.go`, `archCeil`)
- ❌ (`src/math/floor_asm.go`, `archTrunc`)
- ❌ (`src/math/log.go`, `Log`)
- ❌ (`src/math/exp2_noasm.go`, `archExp2`)
- ❌ (`src/math/exp.go`, `Exp`)
- ❌ (`src/math/exp.go`, `Exp2`)
- ❌ (`src/math/sin.go`, `Cos`)
- ❌ (`src/math/sin.go`, `Sin`)
- ❌ (`src/math/erf.go`, `Erf`)
- ❌ (`src/math/erf.go`, `Erfc`)
- ❌ (`src/math/sqrt.go`, `Sqrt`)
- ❌ (`src/math/frexp.go`, `Frexp`)
- ❌ (`src/math/log1p.go`, `Log1p`)
- ❌ (`src/math/atan.go`, `Atan`)
- ❌ (`src/math/hypot_asm.go`, `archHypot`)
- ❌ (`src/math/atan2.go`, `Atan2`)
- ❌ (`src/math/exp_noasm.go`, `archExp`)
- ❌ (`src/math/mod.go`, `Mod`)
- ❌ (`src/math/acosh.go`, `Acosh`)
- ❌ (`src/math/floor.go`, `Floor`)
- ❌ (`src/math/floor.go`, `Ceil`)
- ❌ (`src/math/floor.go`, `Trunc`)
- ❌ (`src/math/tanh.go`, `Tanh`)
- ❌ (`src/math/dim_noasm.go`, `archMax`)
- ❌ (`src/math/dim_noasm.go`, `archMin`)
- ❌ (`src/math/modf.go`, `Modf`)
- ❌ (`src/math/floor_noasm.go`, `archFloor`)
- ❌ (`src/math/floor_noasm.go`, `archCeil`)
- ❌ (`src/math/floor_noasm.go`, `archTrunc`)
- ❌ (`src/math/atanh.go`, `Atanh`)
- ❌ (`src/math/remainder.go`, `Remainder`)
- ❌ (`src/math/modf_noasm.go`, `archModf`)
- ❌ (`src/math/sinh.go`, `Sinh`)
- ❌ (`src/math/sinh.go`, `Cosh`)
- ❌ (`src/math/exp_asm.go`, `archExp`)
- ❌ (`src/math/log10.go`, `Log10`)
- ❌ (`src/math/log10.go`, `log10`)
- ❌ (`src/math/log10.go`, `Log2`)
- ❌ (`src/math/log_stub.go`, `archLog`)
- ❌ (`src/math/cbrt.go`, `Cbrt`)
- ❌ (`src/math/asinh.go`, `Asinh`)
- ❌ (`src/math/log_asm.go`, `archLog`)
- ❌ (`src/math/arith_s390x.go`, `expTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `expAsm`)
- ❌ (`src/math/arith_s390x.go`, `logTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `logAsm`)
- ❌ (`src/math/arith_s390x.go`, `archLog10`)
- ❌ (`src/math/arith_s390x.go`, `log10TrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `log10Asm`)
- ❌ (`src/math/arith_s390x.go`, `archCos`)
- ❌ (`src/math/arith_s390x.go`, `cosTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `cosAsm`)
- ❌ (`src/math/arith_s390x.go`, `archCosh`)
- ❌ (`src/math/arith_s390x.go`, `coshTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `coshAsm`)
- ❌ (`src/math/arith_s390x.go`, `archSin`)
- ❌ (`src/math/arith_s390x.go`, `sinTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `sinAsm`)
- ❌ (`src/math/arith_s390x.go`, `archSinh`)
- ❌ (`src/math/arith_s390x.go`, `sinhTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `sinhAsm`)
- ❌ (`src/math/arith_s390x.go`, `archTanh`)
- ❌ (`src/math/arith_s390x.go`, `tanhTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `tanhAsm`)
- ❌ (`src/math/arith_s390x.go`, `archLog1p`)
- ❌ (`src/math/arith_s390x.go`, `log1pTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `log1pAsm`)
- ❌ (`src/math/arith_s390x.go`, `archAtanh`)
- ❌ (`src/math/arith_s390x.go`, `atanhTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `atanhAsm`)
- ❌ (`src/math/arith_s390x.go`, `archAcos`)
- ❌ (`src/math/arith_s390x.go`, `acosTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `acosAsm`)
- ❌ (`src/math/arith_s390x.go`, `archAcosh`)
- ❌ (`src/math/arith_s390x.go`, `acoshTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `acoshAsm`)
- ❌ (`src/math/arith_s390x.go`, `archAsin`)
- ❌ (`src/math/arith_s390x.go`, `asinTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `asinAsm`)
- ❌ (`src/math/arith_s390x.go`, `archAsinh`)
- ❌ (`src/math/arith_s390x.go`, `asinhTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `asinhAsm`)
- ❌ (`src/math/arith_s390x.go`, `archErf`)
- ❌ (`src/math/arith_s390x.go`, `erfTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `erfAsm`)
- ❌ (`src/math/arith_s390x.go`, `archErfc`)
- ❌ (`src/math/arith_s390x.go`, `erfcTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `erfcAsm`)
- ❌ (`src/math/arith_s390x.go`, `archAtan`)
- ❌ (`src/math/arith_s390x.go`, `atanTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `atanAsm`)
- ❌ (`src/math/arith_s390x.go`, `archAtan2`)
- ❌ (`src/math/arith_s390x.go`, `atan2TrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `atan2Asm`)
- ❌ (`src/math/arith_s390x.go`, `archCbrt`)
- ❌ (`src/math/arith_s390x.go`, `cbrtTrampolineSetup`)
- ❌ (`src/math/arith_s390x.go`, `cbrtAsm`)
- ❌ (`src/math/arith_s390x.go`, `archTan`)
- ❌ (`src/math/arith_s390x.go`, `archExpm1`)
- ❌ (`src/math/arith_s390x.go`, `archPow`)
- ❌ (`src/math/arith_s390x.go`, `archFrexp`)
- ❌ (`src/math/arith_s390x.go`, `archLdexp`)
- ❌ (`src/math/arith_s390x.go`, `archLog2`)
- ❌ (`src/math/arith_s390x.go`, `archMod`)
- ❌ (`src/math/arith_s390x.go`, `archRemainder`)
- ❌ (`src/math/dim.go`, `Max`)
- ❌ (`src/math/dim.go`, `Min`)
- ❌ (`src/math/pow.go`, `Pow`)

### 📊 Proposal #40728

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/base`
- ❌ `src/cmd/go/internal/fmtcmd`
- ❌ `src/cmd/go/internal/list`
- ❌ `src/cmd/go/internal/modcmd`
- ❌ `src/cmd/go/internal/modget`
- ✅ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/work`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/base/flag.go`
- ❌ `src/cmd/go/internal/fmtcmd/fmt.go`
- ❌ `src/cmd/go/internal/list/list.go`
- ❌ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modcmd/edit.go`
- ❌ `src/cmd/go/internal/modcmd/graph.go`
- ❌ `src/cmd/go/internal/modcmd/init.go`
- ❌ `src/cmd/go/internal/modcmd/tidy.go`
- ❌ `src/cmd/go/internal/modcmd/vendor.go`
- ❌ `src/cmd/go/internal/modcmd/verify.go`
- ❌ `src/cmd/go/internal/modcmd/why.go`
- ❌ `src/cmd/go/internal/modget/get.go`
- ❌ `src/cmd/go/internal/modget/query.go`
- ❌ `src/cmd/go/internal/modload/buildlist.go`
- ❌ `src/cmd/go/internal/modload/import.go`
- ✅ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/mvs.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ❌ `src/cmd/go/internal/modload/query_test.go`
- ❌ `src/cmd/go/internal/modload/search.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/init.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/base`
- ❌ `src/cmd/go/internal/fmtcmd`
- ❌ `src/cmd/go/internal/list`
- ❌ `src/cmd/go/internal/modcmd`
- ✅ `src/cmd/go/internal/modget`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/work`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/base/flag.go`
- ❌ `src/cmd/go/internal/fmtcmd/fmt.go`
- ❌ `src/cmd/go/internal/list/list.go`
- ❌ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modcmd/edit.go`
- ❌ `src/cmd/go/internal/modcmd/graph.go`
- ❌ `src/cmd/go/internal/modcmd/init.go`
- ❌ `src/cmd/go/internal/modcmd/tidy.go`
- ❌ `src/cmd/go/internal/modcmd/vendor.go`
- ❌ `src/cmd/go/internal/modcmd/verify.go`
- ❌ `src/cmd/go/internal/modcmd/why.go`
- ✅ `src/cmd/go/internal/modget/get.go`
- ❌ `src/cmd/go/internal/modget/query.go`
- ❌ `src/cmd/go/internal/modload/buildlist.go`
- ❌ `src/cmd/go/internal/modload/import.go`
- ❌ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/mvs.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ❌ `src/cmd/go/internal/modload/query_test.go`
- ❌ `src/cmd/go/internal/modload/search.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/init.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/list/list.go`, `runList`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `setDefaultBuildMod`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `WriteGoMod`)
- ❌ (`src/cmd/go/internal/modcmd/download.go`, `init`)
- ❌ (`src/cmd/go/internal/modcmd/why.go`, `init`)
- ❌ (`src/cmd/go/internal/modcmd/init.go`, `init`)
- ❌ (`src/cmd/go/internal/work/init.go`, `buildModeInit`)
- ❌ (`src/cmd/go/internal/work/build.go`, `AddBuildFlags`)
- ❌ (`src/cmd/go/internal/work/build.go`, `Set`)
- ❌ (`src/cmd/go/internal/base/flag.go`, `String`)
- ❌ (`src/cmd/go/internal/base/flag.go`, `Set`)
- ❌ (`src/cmd/go/internal/base/flag.go`, `AddModFlag`)
- ❌ (`src/cmd/go/internal/base/flag.go`, `AddModCommonFlags`)
- ❌ (`src/cmd/go/internal/modcmd/vendor.go`, `init`)
- ❌ (`src/cmd/go/internal/fmtcmd/fmt.go`, `init`)
- ❌ (`src/cmd/go/internal/modcmd/edit.go`, `init`)
- ❌ (`src/cmd/go/internal/modcmd/graph.go`, `init`)
- ❌ (`src/cmd/go/internal/modcmd/tidy.go`, `init`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `setDefaultBuildMod`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `WriteGoMod`)
- ❌ (`src/cmd/go/internal/modcmd/verify.go`, `init`)
- ❌ (`src/cmd/go/internal/modload/import.go`, `ImportPath`)
- ❌ (`src/cmd/go/internal/modload/import.go`, `Error`)
- ❌ (`src/cmd/go/internal/modload/import.go`, `Unwrap`)
- ❌ (`src/cmd/go/internal/modload/import.go`, `queryImport`)
- ❌ (`src/cmd/go/internal/modload/import.go`, `Error`)
- ❌ (`src/cmd/go/internal/modload/import.go`, `queryImport`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `queryProxy`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `IsRevisionQuery`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `newQueryMatcher`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `allowsVersion`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `filterVersions`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `lookupRepo`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `Versions`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `Stat`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `Latest`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `replacementStat`)
- ❌ (`src/cmd/go/internal/modload/modfile.go`, `Error`)
- ❌ (`src/cmd/go/internal/modload/modfile.go`, `Unwrap`)
- ❌ (`src/cmd/go/internal/modload/modfile.go`, `indexModFile`)
- ❌ (`src/cmd/go/internal/modload/query_test.go`, `TestQuery`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `queryProxy`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `newQueryMatcher`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `QueryPattern`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `queryPrefixModules`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `Error`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `Error`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `Error`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `newQuery`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `validate`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `ResolvedString`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `isWildcard`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `matchesPath`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `canMatchInModule`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `pathOnce`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `reportError`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `reportConflict`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `Error`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `versionOkForMainModule`)
- ❌ (`src/cmd/go/internal/modload/search.go`, `matchPackages`)
- ❌ (`src/cmd/go/internal/modload/search.go`, `MatchInModule`)
- ❌ (`src/cmd/go/internal/modload/mvs.go`, `Previous`)
- ❌ (`src/cmd/go/internal/modload/load.go`, `load`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `Set`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `init`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `runGet`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `parseArgs`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `newResolver`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `initialSelected`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `selected`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `noneForPath`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `queryModule`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `queryPackages`)
- ✅ (`src/cmd/go/internal/modget/get.go`, `queryPattern`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `checkAllowedOr`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `matchInModule`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `queryNone`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `performLocalQueries`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `performWildcardQueries`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `queryWildcard`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `tryWildcard`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `findMissingWildcards`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `checkWildcardVersions`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `performPathQueries`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `queryPath`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `performPatternAllQueries`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `findAndUpgradeImports`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `loadPackages`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `disambiguate`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `chooseArbitrarily`)
- ✅ (`src/cmd/go/internal/modget/get.go`, `reportChanges`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `resolve`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `updateBuildList`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `isNoSuchModuleVersion`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `isNoSuchPackageVersion`)
- ❌ (`src/cmd/go/internal/modload/buildlist.go`, `EditBuildList`)
- ❌ (`src/cmd/go/internal/modload/buildlist.go`, `Error`)

### 📊 Proposal #40995

#### File Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ❌ `src/cmd/link/internal/mips64`
- ✅ `src/cmd/vendor/golang.org/x/sys/unix`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows`
- ✅ `src/runtime`
- ✅ `src/syscall`
- ❌ `src/vendor/golang.org/x/sys/cpu`

#### File Embeddings - File Level
- ❌ `src/cmd/dist/main.go`
- ❌ `src/cmd/link/internal/mips64/obj.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/sockcmsg_unix_other.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_aix.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_bsd.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin_amd64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin_arm64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_dragonfly.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_freebsd.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_netbsd.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_openbsd.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_solaris.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_dragonfly_amd64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows/syscall.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows/syscall_windows.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`
- ❌ `src/runtime/defs_openbsd_mips64.go`
- ❌ `src/runtime/mheap.go`
- ❌ `src/runtime/os_openbsd.go`
- ❌ `src/runtime/os_openbsd_mips64.go`
- ❌ `src/runtime/signal_openbsd_mips64.go`
- ❌ `src/runtime/stack.go`
- ❌ `src/syscall/exec_bsd.go`
- ❌ `src/syscall/exec_unix_test.go`
- ❌ `src/syscall/syscall_openbsd_mips64.go`
- ❌ `src/syscall/zsyscall_openbsd_mips64.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_arm64.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_linux_s390x.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_netbsd_arm64.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_other_mips64x.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_s390x.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_x86.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_zos.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_zos_s390x.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ❌ `src/cmd/link/internal/mips64`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows`
- ✅ `src/runtime`
- ❌ `src/syscall`
- ❌ `src/vendor/golang.org/x/sys/cpu`

#### Function Embeddings - File Level
- ❌ `src/cmd/dist/main.go`
- ❌ `src/cmd/link/internal/mips64/obj.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/sockcmsg_unix_other.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_aix.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_bsd.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin_amd64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin_arm64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_dragonfly.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_freebsd.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_netbsd.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_openbsd.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall_solaris.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_dragonfly_amd64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows/syscall.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows/syscall_windows.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`
- ❌ `src/runtime/defs_openbsd_mips64.go`
- ❌ `src/runtime/mheap.go`
- ✅ `src/runtime/os_openbsd.go`
- ❌ `src/runtime/os_openbsd_mips64.go`
- ✅ `src/runtime/signal_openbsd_mips64.go`
- ❌ `src/runtime/stack.go`
- ❌ `src/syscall/exec_bsd.go`
- ❌ `src/syscall/exec_unix_test.go`
- ❌ `src/syscall/syscall_openbsd_mips64.go`
- ❌ `src/syscall/zsyscall_openbsd_mips64.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_arm64.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_linux_s390x.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_netbsd_arm64.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_other_mips64x.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_s390x.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_x86.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_zos.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_zos_s390x.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/stack.go`, `stackpoolalloc`)
- ❌ (`src/runtime/stack.go`, `stackpoolfree`)
- ❌ (`src/runtime/stack.go`, `stackalloc`)
- ❌ (`src/runtime/stack.go`, `stackfree`)
- ❌ (`src/runtime/stack.go`, `freeStackSpans`)
- ❌ (`src/runtime/os_openbsd.go`, `osStackAlloc`)
- ❌ (`src/runtime/os_openbsd.go`, `osStackFree`)
- ❌ (`src/runtime/os_openbsd.go`, `osStackRemap`)
- ❌ (`src/runtime/defs_openbsd_mips64.go`, `setNsec`)
- ❌ (`src/runtime/defs_openbsd_mips64.go`, `set_usec`)
- ❌ (`src/runtime/os_openbsd_mips64.go`, `cputicks`)
- ❌ (`src/runtime/signal_openbsd_mips64.go`, `regs`)
- ❌ (`src/runtime/signal_openbsd_mips64.go`, `sigaddr`)
- ❌ (`src/runtime/signal_openbsd_mips64.go`, `set_sigaddr`)
- ❌ (`src/runtime/os_openbsd.go`, `mpreinit`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `getgroups`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `setgroups`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `wait4`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `accept`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `bind`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `connect`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `socket`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `getsockopt`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `setsockopt`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `getpeername`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `getsockname`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Shutdown`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `socketpair`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `recvfrom`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `sendto`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `recvmsg`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `sendmsg`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `kevent`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `utimes`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `futimes`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `fcntl`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `accept4`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `getdents`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Access`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Adjtime`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Chdir`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Chflags`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Chmod`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Chown`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Chroot`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Close`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Dup`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Dup2`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Fchdir`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Fchflags`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Fchmod`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Fchown`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Flock`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Fpathconf`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Fstat`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Fstatfs`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Fsync`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Ftruncate`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getegid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Geteuid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getgid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getpgid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getpgrp`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getpid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getppid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getpriority`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getrlimit`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getrusage`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getsid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Gettimeofday`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Getuid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Issetugid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Kill`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Kqueue`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Lchown`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Link`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Listen`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Lstat`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Mkdir`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Mkfifo`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Mknod`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Nanosleep`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Open`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Pathconf`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `read`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Readlink`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Rename`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Revoke`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Rmdir`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Seek`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Select`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Setegid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Seteuid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Setgid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Setlogin`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Setpgid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Setpriority`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Setregid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Setreuid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Setsid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Settimeofday`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Setuid`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Stat`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Statfs`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Symlink`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Sync`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Truncate`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Umask`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Unlink`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `Unmount`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `write`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `mmap`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `munmap`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `readlen`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `utimensat`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `getcwd`)
- ❌ (`src/syscall/zsyscall_openbsd_mips64.go`, `sysctl`)
- ❌ (`src/syscall/syscall_openbsd_mips64.go`, `setTimespec`)
- ❌ (`src/syscall/syscall_openbsd_mips64.go`, `setTimeval`)
- ❌ (`src/syscall/syscall_openbsd_mips64.go`, `SetKevent`)
- ❌ (`src/syscall/syscall_openbsd_mips64.go`, `SetLen`)
- ❌ (`src/syscall/syscall_openbsd_mips64.go`, `SetControllen`)
- ❌ (`src/syscall/syscall_openbsd_mips64.go`, `SetLen`)
- ❌ (`src/cmd/link/internal/mips64/obj.go`, `Init`)
- ❌ (`src/cmd/link/internal/mips64/obj.go`, `archinit`)
- ❌ (`src/cmd/dist/main.go`, `main`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_bsd.go`, `Getwd`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_bsd.go`, `anyToSockaddr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `errnoErr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `AdjustTokenGroups`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `AdjustTokenPrivileges`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `AllocateAndInitializeSid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `buildSecurityDescriptor`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ChangeServiceConfig2`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ChangeServiceConfig`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `checkTokenMembership`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CloseServiceHandle`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ControlService`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `convertSecurityDescriptorToStringSecurityDescriptor`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ConvertSidToStringSid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `convertStringSecurityDescriptorToSecurityDescriptor`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `_convertStringSecurityDescriptorToSecurityDescriptor`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ConvertStringSidToSid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CopySid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateService`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `createWellKnownSid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CryptAcquireContext`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CryptGenRandom`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CryptReleaseContext`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DeleteService`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DeregisterEventSource`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DuplicateTokenEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `EnumServicesStatusEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `EqualSid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FreeSid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetLengthSid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getNamedSecurityInfo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `_getNamedSecurityInfo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSecurityDescriptorControl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSecurityDescriptorDacl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSecurityDescriptorGroup`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSecurityDescriptorLength`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSecurityDescriptorOwner`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSecurityDescriptorRMControl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSecurityDescriptorSacl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSecurityInfo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSidIdentifierAuthority`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSidSubAuthority`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSidSubAuthorityCount`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetTokenInformation`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ImpersonateSelf`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `initializeSecurityDescriptor`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `InitiateSystemShutdownEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `isValidSecurityDescriptor`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `isValidSid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `isWellKnownSid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `LookupAccountName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `LookupAccountSid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `LookupPrivilegeValue`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `makeAbsoluteSD`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `makeSelfRelativeSD`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `NotifyServiceStatusChange`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `OpenProcessToken`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `OpenSCManager`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `OpenService`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `OpenThreadToken`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `QueryServiceConfig2`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `QueryServiceConfig`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `QueryServiceLockStatus`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `QueryServiceStatus`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `QueryServiceStatusEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `RegCloseKey`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `RegEnumKeyEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `RegOpenKeyEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `RegQueryInfoKey`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `RegQueryValueEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `RegisterEventSource`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ReportEvent`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `RevertToSelf`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `setEntriesInAcl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetNamedSecurityInfo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `_SetNamedSecurityInfo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `setSecurityDescriptorControl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `setSecurityDescriptorDacl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `setSecurityDescriptorGroup`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `setSecurityDescriptorOwner`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `setSecurityDescriptorRMControl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `setSecurityDescriptorSacl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetSecurityInfo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetServiceStatus`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetThreadToken`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetTokenInformation`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `StartServiceCtrlDispatcher`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `StartService`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CertAddCertificateContextToStore`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CertCloseStore`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CertCreateCertificateContext`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CertEnumCertificatesInStore`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CertFreeCertificateChain`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CertFreeCertificateContext`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CertGetCertificateChain`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CertOpenStore`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CertOpenSystemStore`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CertVerifyCertificateChainPolicy`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DnsNameCompare`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DnsQuery`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `_DnsQuery`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DnsRecordListFree`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetAdaptersAddresses`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetAdaptersInfo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetIfEntry`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `AssignProcessToJobObject`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CancelIo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CancelIoEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CloseHandle`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateDirectory`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateEventEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateEvent`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateFileMapping`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateFile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateHardLink`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateIoCompletionPort`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateJobObject`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateMutexEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateMutex`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreatePipe`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateProcess`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateSymbolicLink`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateToolhelp32Snapshot`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DefineDosDevice`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DeleteFile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DeleteVolumeMountPoint`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DeviceIoControl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DuplicateHandle`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ExitProcess`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FindClose`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `findFirstFile1`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FindFirstVolumeMountPoint`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FindFirstVolume`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `findNextFile1`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FindNextVolumeMountPoint`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FindNextVolume`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FindVolumeClose`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FindVolumeMountPointClose`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FlushFileBuffers`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FlushViewOfFile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FormatMessage`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FreeEnvironmentStrings`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FreeLibrary`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GenerateConsoleCtrlEvent`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetACP`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetCommandLine`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetComputerNameEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetComputerName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetConsoleMode`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetConsoleScreenBufferInfo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetCurrentDirectory`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetCurrentProcessId`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetCurrentThreadId`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetDiskFreeSpaceEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetDriveType`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetEnvironmentStrings`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetEnvironmentVariable`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetExitCodeProcess`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetFileAttributesEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetFileAttributes`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetFileInformationByHandle`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetFileInformationByHandleEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetFileType`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetFullPathName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetLastError`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetLogicalDriveStrings`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetLogicalDrives`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetLongPathName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetModuleFileName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetModuleHandleEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetOverlappedResult`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetPriorityClass`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetProcAddress`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `_GetProcAddress`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetProcessId`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getProcessPreferredUILanguages`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetProcessShutdownParameters`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetProcessTimes`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetProcessWorkingSetSizeEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetQueuedCompletionStatus`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetShortPathName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetStdHandle`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSystemDirectory`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSystemPreferredUILanguages`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetSystemTimeAsFileTime`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetSystemTimePreciseAsFileTime`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getSystemWindowsDirectory`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetTempPath`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getThreadPreferredUILanguages`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getTickCount64`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetTimeZoneInformation`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getUserPreferredUILanguages`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetVersion`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetVolumeInformationByHandle`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetVolumeInformation`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetVolumeNameForVolumeMountPoint`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetVolumePathName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetVolumePathNamesForVolumeName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getWindowsDirectory`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `IsWow64Process`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `LoadLibraryEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `_LoadLibraryEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `LoadLibrary`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `_LoadLibrary`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `LocalFree`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `LockFileEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `MapViewOfFile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `MoveFileEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `MoveFile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `MultiByteToWideChar`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `OpenEvent`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `OpenMutex`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `OpenProcess`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `OpenThread`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `PostQueuedCompletionStatus`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `Process32First`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `Process32Next`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ProcessIdToSessionId`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `PulseEvent`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `QueryDosDevice`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `QueryInformationJobObject`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ReadConsole`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ReadDirectoryChanges`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ReleaseMutex`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `RemoveDirectory`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ResetEvent`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ResumeThread`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetConsoleMode`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetCurrentDirectory`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetEndOfFile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetEnvironmentVariable`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetErrorMode`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetEvent`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetFileAttributes`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetFileCompletionNotificationModes`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetFilePointer`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetFileTime`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetHandleInformation`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetInformationJobObject`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetPriorityClass`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetProcessPriorityBoost`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetProcessShutdownParameters`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetProcessWorkingSetSizeEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetStdHandle`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetVolumeLabel`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SetVolumeMountPoint`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `SleepEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `TerminateJobObject`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `TerminateProcess`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `Thread32First`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `Thread32Next`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `UnlockFileEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `UnmapViewOfFile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `VirtualAlloc`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `VirtualFree`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `VirtualLock`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `VirtualProtect`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `VirtualUnlock`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `waitForMultipleObjects`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WaitForSingleObject`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WriteConsole`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `AcceptEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetAcceptExSockaddrs`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `TransmitFile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `NetApiBufferFree`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `NetGetJoinInformation`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `NetUserGetInfo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `rtlGetNtVersionNumbers`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `rtlGetVersion`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `clsidFromString`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `coCreateGuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CoTaskMemFree`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `stringFromGUID2`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetUserNameEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `TranslateName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `shGetKnownFolderPath`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ShellExecute`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `ExitWindowsEx`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `MessageBox`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `CreateEnvironmentBlock`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `DestroyEnvironmentBlock`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetUserProfileDirectory`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `FreeAddrInfoW`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetAddrInfoW`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WSACleanup`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WSAEnumProtocols`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WSAIoctl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WSARecv`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WSARecvFrom`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WSASend`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WSASendTo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WSAStartup`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `bind`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `Closesocket`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `connect`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetHostByName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `_GetHostByName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getpeername`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetProtoByName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `_GetProtoByName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `GetServByName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `_GetServByName`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `getsockname`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `Getsockopt`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `listen`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `Ntohs`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `recvfrom`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `sendto`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `Setsockopt`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `shutdown`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `socket`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WTSEnumerateSessions`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WTSFreeMemory`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`, `WTSQueryUserToken`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_openbsd.go`, `anyToSockaddrGOOS`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_openbsd.go`, `Getdirentries`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_openbsd.go`, `Sendfile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_openbsd.go`, `sendfile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `sockaddr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `anyToSockaddrGOOS`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `direntReclen`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `Pipe`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `Getfsstat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `xattrPointer`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `Getxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `Lgetxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `IoctlCtlInfo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `IoctlGetIfreqMTU`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`, `IoctlSetIfreqMTU`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_netbsd.go`, `anyToSockaddrGOOS`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_netbsd.go`, `Getdirentries`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_netbsd.go`, `sendfile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_aix.go`, `Access`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_aix.go`, `Chmod`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_aix.go`, `Chown`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_aix.go`, `Creat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `pipe`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getcwd`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fstat`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_s390x.go`, `initOptions`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_s390x.go`, `bitIsSet`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_s390x.go`, `Has`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_s390x.go`, `Has`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_s390x.go`, `doinit`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_x86.go`, `initOptions`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_x86.go`, `archInit`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/syscall_windows.go`, `UTF16ToString`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/syscall_windows.go`, `GetProcAddressByOrdinal`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/syscall_windows.go`, `WSASendMsg`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/syscall_windows.go`, `WSARecvMsg`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_dragonfly.go`, `anyToSockaddrGOOS`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_dragonfly.go`, `Accept4`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_dragonfly.go`, `Getfsstat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_dragonfly_amd64.go`, `utimes`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_dragonfly_amd64.go`, `sysctl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin_amd64.go`, `setTimespec`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_zos_s390x.go`, `initS390Xbase`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/sockcmsg_unix_other.go`, `cmsgAlignOf`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `pipe`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getcwd`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_linux_s390x.go`, `initS390Xbase`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_freebsd.go`, `anyToSockaddrGOOS`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_freebsd.go`, `Accept4`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_freebsd.go`, `Getfsstat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin_arm64.go`, `setTimespec`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall.go`, `ByteSliceToString`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall.go`, `BytePtrToString`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_zos.go`, `archInit`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall_solaris.go`, `IoctlSetTermio`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_netbsd_arm64.go`, `sysctl`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_netbsd_arm64.go`, `sysctlNodes`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_netbsd_arm64.go`, `nametomib`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_netbsd_arm64.go`, `sysctlCPUID`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_netbsd_arm64.go`, `doinit`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/syscall.go`, `ByteSliceFromString`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/syscall.go`, `ByteSliceToString`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/syscall.go`, `BytePtrToString`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_arm64.go`, `archInit`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_arm64.go`, `setMinimalFeatures`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_arm64.go`, `readARM64Registers`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_arm64.go`, `parseARM64SystemRegisters`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu_other_mips64x.go`, `archInit`)
- ❌ (`src/runtime/mheap.go`, `allocSpan`)
- ❌ (`src/syscall/exec_unix_test.go`, `TestForeground`)
- ❌ (`src/syscall/exec_bsd.go`, `forkAndExecInChild`)

### 📊 Proposal #41048

#### File Embeddings - Directory Level
- ✅ `src/net/http`

#### File Embeddings - File Level
- ❌ `src/net/http/transport.go`
- ❌ `src/net/http/transport_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/http`

#### Function Embeddings - File Level
- ❌ `src/net/http/transport.go`
- ✅ `src/net/http/transport_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/http/transport.go`, `Clone`)
- ❌ (`src/net/http/transport.go`, `dialConn`)
- ❌ (`src/net/http/transport_test.go`, `TestTransportProxyGetConnectHeader`)
- ❌ (`src/net/http/transport_test.go`, `TestTransportClone`)

### 📊 Proposal #41066

#### File Embeddings - Directory Level
- ✅ `src/crypto/tls`

#### File Embeddings - File Level
- ❌ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/tls_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/tls`

#### Function Embeddings - File Level
- ❌ `src/crypto/tls/conn.go`
- ✅ `src/crypto/tls/tls_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/tls/conn.go`, `Write`)
- ❌ (`src/crypto/tls/conn.go`, `Close`)
- ✅ (`src/crypto/tls/tls_test.go`, `TestConnCloseBreakingWrite`)

### 📊 Proposal #41184

#### File Embeddings - Directory Level
- ❌ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/asm/internal/lex`
- ✅ `src/cmd/fix`
- ❌ `src/cmd/go/internal/fix`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/loopclosure`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/unitchecker`
- ❌ `src/cmd/vet`
- ❌ `src/go/build`
- ❌ `src/go/build/constraint`
- ❌ `src/go/printer`
- ❌ `src/runtime`
- ❌ `src/runtime/pprof`

#### File Embeddings - File Level
- ❌ `src/cmd/asm/internal/asm/endtoend_test.go`
- ❌ `src/cmd/asm/internal/asm/parse.go`
- ❌ `src/cmd/asm/internal/lex/input.go`
- ❌ `src/cmd/asm/internal/lex/lex_test.go`
- ❌ `src/cmd/asm/internal/lex/tokenizer.go`
- ✅ `src/cmd/fix/buildtag.go`
- ❌ `src/cmd/fix/buildtag_test.go`
- ❌ `src/cmd/fix/fix.go`
- ❌ `src/cmd/fix/main.go`
- ❌ `src/cmd/fix/main_test.go`
- ❌ `src/cmd/go/internal/fix/fix.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/loopclosure/loopclosure.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/unitchecker/unitchecker.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/go/build/constraint/expr.go`
- ❌ `src/go/build/constraint/expr_test.go`
- ❌ `src/go/printer/gobuild.go`
- ❌ `src/go/printer/printer.go`
- ❌ `src/runtime/auxv_none.go`
- ❌ `src/runtime/mkduff.go`
- ❌ `src/runtime/mkpreempt.go`
- ❌ `src/runtime/pprof/mprof_test.go`
- ❌ `src/runtime/wincallback.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/asm/internal/lex`
- ✅ `src/cmd/fix`
- ❌ `src/cmd/go/internal/fix`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix`
- ✅ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/loopclosure`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/unitchecker`
- ❌ `src/cmd/vet`
- ✅ `src/go/build`
- ❌ `src/go/build/constraint`
- ❌ `src/go/printer`
- ❌ `src/runtime`
- ❌ `src/runtime/pprof`

#### Function Embeddings - File Level
- ❌ `src/cmd/asm/internal/asm/endtoend_test.go`
- ❌ `src/cmd/asm/internal/asm/parse.go`
- ❌ `src/cmd/asm/internal/lex/input.go`
- ❌ `src/cmd/asm/internal/lex/lex_test.go`
- ❌ `src/cmd/asm/internal/lex/tokenizer.go`
- ✅ `src/cmd/fix/buildtag.go`
- ❌ `src/cmd/fix/buildtag_test.go`
- ❌ `src/cmd/fix/fix.go`
- ❌ `src/cmd/fix/main.go`
- ❌ `src/cmd/fix/main_test.go`
- ❌ `src/cmd/go/internal/fix/fix.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
- ✅ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/loopclosure/loopclosure.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/unitchecker/unitchecker.go`
- ❌ `src/cmd/vet/vet_test.go`
- ✅ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/go/build/constraint/expr.go`
- ❌ `src/go/build/constraint/expr_test.go`
- ❌ `src/go/printer/gobuild.go`
- ❌ `src/go/printer/printer.go`
- ❌ `src/runtime/auxv_none.go`
- ❌ `src/runtime/mkduff.go`
- ❌ `src/runtime/mkpreempt.go`
- ❌ `src/runtime/pprof/mprof_test.go`
- ❌ `src/runtime/wincallback.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/load/pkg.go`, `AllFiles`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `copyBuild`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `buildVetConfig`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/unitchecker/unitchecker.go`, `run`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `runBuildTag`)
- ❌ (`src/go/build/build.go`, `matchFile`)
- ❌ (`src/go/build/build.go`, `ImportDir`)
- ❌ (`src/go/build/build.go`, `isGoBuildComment`)
- ✅ (`src/go/build/build.go`, `shouldBuild`)
- ❌ (`src/go/build/build.go`, `parseFileHeader`)
- ❌ (`src/go/build/build_test.go`, `TestShouldBuild`)
- ❌ (`src/cmd/asm/internal/lex/lex_test.go`, `drain`)
- ❌ (`src/cmd/asm/internal/asm/endtoend_test.go`, `testErrors`)
- ❌ (`src/cmd/asm/internal/asm/endtoend_test.go`, `TestGoBuildErrors`)
- ❌ (`src/cmd/asm/internal/lex/tokenizer.go`, `Next`)
- ❌ (`src/cmd/asm/internal/asm/parse.go`, `nextToken`)
- ❌ (`src/cmd/asm/internal/asm/parse.go`, `line`)
- ❌ (`src/cmd/asm/internal/lex/input.go`, `Next`)
- ❌ (`src/go/build/constraint/expr.go`, `Eval`)
- ❌ (`src/go/build/constraint/expr.go`, `String`)
- ❌ (`src/go/build/constraint/expr.go`, `Eval`)
- ❌ (`src/go/build/constraint/expr.go`, `String`)
- ❌ (`src/go/build/constraint/expr.go`, `Eval`)
- ❌ (`src/go/build/constraint/expr.go`, `String`)
- ❌ (`src/go/build/constraint/expr.go`, `andArg`)
- ❌ (`src/go/build/constraint/expr.go`, `and`)
- ❌ (`src/go/build/constraint/expr.go`, `Eval`)
- ❌ (`src/go/build/constraint/expr.go`, `String`)
- ❌ (`src/go/build/constraint/expr.go`, `orArg`)
- ❌ (`src/go/build/constraint/expr.go`, `or`)
- ❌ (`src/go/build/constraint/expr.go`, `Error`)
- ❌ (`src/go/build/constraint/expr.go`, `Parse`)
- ❌ (`src/go/build/constraint/expr.go`, `IsGoBuild`)
- ❌ (`src/go/build/constraint/expr.go`, `splitGoBuild`)
- ❌ (`src/go/build/constraint/expr.go`, `parseExpr`)
- ❌ (`src/go/build/constraint/expr.go`, `or`)
- ❌ (`src/go/build/constraint/expr.go`, `and`)
- ❌ (`src/go/build/constraint/expr.go`, `not`)
- ❌ (`src/go/build/constraint/expr.go`, `atom`)
- ❌ (`src/go/build/constraint/expr.go`, `lex`)
- ❌ (`src/go/build/constraint/expr.go`, `IsPlusBuild`)
- ❌ (`src/go/build/constraint/expr.go`, `splitPlusBuild`)
- ❌ (`src/go/build/constraint/expr.go`, `parsePlusBuildExpr`)
- ❌ (`src/go/build/constraint/expr.go`, `isValidTag`)
- ❌ (`src/go/build/constraint/expr.go`, `PlusBuildLines`)
- ❌ (`src/go/build/constraint/expr.go`, `pushNot`)
- ❌ (`src/go/build/constraint/expr.go`, `appendSplitAnd`)
- ❌ (`src/go/build/constraint/expr.go`, `appendSplitOr`)
- ❌ (`src/go/build/constraint/expr_test.go`, `TestExprString`)
- ❌ (`src/go/build/constraint/expr_test.go`, `TestLex`)
- ❌ (`src/go/build/constraint/expr_test.go`, `lexHelp`)
- ❌ (`src/go/build/constraint/expr_test.go`, `TestParseExpr`)
- ❌ (`src/go/build/constraint/expr_test.go`, `TestParseError`)
- ❌ (`src/go/build/constraint/expr_test.go`, `TestExprEval`)
- ❌ (`src/go/build/constraint/expr_test.go`, `TestParsePlusBuildExpr`)
- ❌ (`src/go/build/constraint/expr_test.go`, `TestParse`)
- ❌ (`src/go/build/constraint/expr_test.go`, `TestPlusBuildLines`)
- ❌ (`src/go/build/build_test.go`, `TestMatch`)
- ❌ (`src/go/build/build.go`, `matchFile`)
- ✅ (`src/go/build/build.go`, `shouldBuild`)
- ❌ (`src/go/build/build.go`, `parseFileHeader`)
- ❌ (`src/go/build/build.go`, `saveCgo`)
- ❌ (`src/go/build/build.go`, `matchAuto`)
- ❌ (`src/go/build/build.go`, `eval`)
- ❌ (`src/go/build/build.go`, `matchTag`)
- ❌ (`src/go/build/build.go`, `goodOSArchFile`)
- ❌ (`src/go/build/build_test.go`, `TestMatch`)
- ❌ (`src/go/printer/gobuild.go`, `fixGoBuildLines`)
- ❌ (`src/go/printer/gobuild.go`, `appendLines`)
- ❌ (`src/go/printer/gobuild.go`, `lineAt`)
- ❌ (`src/go/printer/gobuild.go`, `commentTextAt`)
- ❌ (`src/go/printer/gobuild.go`, `isNL`)
- ❌ (`src/go/printer/printer.go`, `writeComment`)
- ❌ (`src/go/printer/printer.go`, `printNode`)
- ❌ (`src/go/printer/printer.go`, `fprint`)
- ❌ (`src/cmd/vet/vet_test.go`, `wantedErrors`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/loopclosure/loopclosure.go`, `run`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/unitchecker/unitchecker.go`, `Main`)
- ✅ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `checkGoFile`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `checkOtherFile`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `init`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `file`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `comment`)
- ✅ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `goBuildLine`)
- ✅ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `plusBuildLine`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `finish`)
- ❌ (`src/cmd/go/internal/fix/fix.go`, `init`)
- ❌ (`src/cmd/go/internal/fix/fix.go`, `runFix`)
- ❌ (`src/cmd/fix/main_test.go`, `TestRewrite`)
- ❌ (`src/cmd/fix/buildtag.go`, `init`)
- ✅ (`src/cmd/fix/buildtag.go`, `buildtag`)
- ❌ (`src/cmd/fix/fix.go`, `walkBeforeAfter`)
- ❌ (`src/cmd/fix/buildtag_test.go`, `init`)
- ❌ (`src/cmd/fix/main.go`, `main`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/unitchecker/unitchecker.go`, `run`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `runBuildTag`)
- ❌ (`src/runtime/auxv_none.go`, `sysargs`)
- ❌ (`src/runtime/pprof/mprof_test.go`, `TestMemoryProfiler`)
- ❌ (`src/runtime/wincallback.go`, `genasm386Amd64`)
- ❌ (`src/runtime/mkduff.go`, `tagsPPC64x`)
- ❌ (`src/runtime/mkduff.go`, `tagsMIPS64x`)
- ❌ (`src/runtime/mkpreempt.go`, `header`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `getgroups`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `setgroups`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `wait4`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `accept`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `bind`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `connect`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `socket`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `getsockopt`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `setsockopt`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `getpeername`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `getsockname`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Shutdown`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `socketpair`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `recvfrom`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `sendto`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `recvmsg`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `sendmsg`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `kevent`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `utimes`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `futimes`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `poll`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Madvise`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Mlock`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Mlockall`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Mprotect`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Msync`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Munlock`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Munlockall`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `pipe`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `getxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `fgetxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `setxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `fsetxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `removexattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `fremovexattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `listxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `flistxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `fcntl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `kill`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `ioctl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `sysctl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `sendfile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Access`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Adjtime`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Chdir`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Chflags`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Chmod`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Chown`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Chroot`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `ClockGettime`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Close`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Clonefile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Clonefileat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Dup`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Dup2`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Exchangedata`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Exit`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Faccessat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fchdir`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fchflags`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fchmod`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fchmodat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fchown`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fchownat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fclonefileat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Flock`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fpathconf`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fsync`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Ftruncate`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getcwd`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getdtablesize`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getegid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Geteuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getgid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getpgid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getpgrp`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getpid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getppid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getpriority`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getrlimit`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getrusage`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getsid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Gettimeofday`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Getuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Issetugid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Kqueue`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Lchown`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Link`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Linkat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Listen`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Mkdir`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Mkdirat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Mkfifo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Mknod`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Open`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Openat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Pathconf`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `read`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Readlink`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Readlinkat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Rename`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Renameat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Revoke`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Rmdir`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Seek`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Select`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Setegid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Seteuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Setgid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Setlogin`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Setpgid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Setpriority`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Setprivexec`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Setregid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Setreuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Setsid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Settimeofday`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Setuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Symlink`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Symlinkat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Sync`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Truncate`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Umask`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Undelete`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Unlink`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Unlinkat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Unmount`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `write`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `mmap`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `munmap`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fstat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fstatat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Fstatfs`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `getfsstat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Lstat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `ptrace1`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Stat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`, `Statfs`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `getgroups`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `setgroups`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `wait4`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `accept`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `bind`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `connect`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `socket`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `getsockopt`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `setsockopt`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `getpeername`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `getsockname`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Shutdown`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `socketpair`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `recvfrom`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `sendto`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `recvmsg`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `sendmsg`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `kevent`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `utimes`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `futimes`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `poll`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Madvise`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Mlock`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Mlockall`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Mprotect`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Msync`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Munlock`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Munlockall`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `pipe`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `getxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `fgetxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `setxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `fsetxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `removexattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `fremovexattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `listxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `flistxattr`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `fcntl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `kill`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `ioctl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `sysctl`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `sendfile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Access`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Adjtime`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Chdir`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Chflags`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Chmod`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Chown`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Chroot`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `ClockGettime`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Close`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Clonefile`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Clonefileat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Dup`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Dup2`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Exchangedata`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Exit`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Faccessat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fchdir`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fchflags`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fchmod`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fchmodat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fchown`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fchownat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fclonefileat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Flock`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fpathconf`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fsync`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Ftruncate`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getcwd`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getdtablesize`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getegid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Geteuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getgid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getpgid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getpgrp`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getpid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getppid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getpriority`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getrlimit`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getrusage`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getsid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Gettimeofday`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Getuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Issetugid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Kqueue`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Lchown`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Link`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Linkat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Listen`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Mkdir`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Mkdirat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Mkfifo`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Mknod`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Open`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Openat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Pathconf`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `read`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Readlink`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Readlinkat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Rename`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Renameat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Revoke`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Rmdir`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Seek`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Select`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Setegid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Seteuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Setgid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Setlogin`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Setpgid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Setpriority`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Setprivexec`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Setregid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Setreuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Setsid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Settimeofday`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Setuid`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Symlink`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Symlinkat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Sync`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Truncate`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Umask`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Undelete`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Unlink`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Unlinkat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Unmount`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `write`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `mmap`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `munmap`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fstat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fstatat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Fstatfs`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `getfsstat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Lstat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `ptrace1`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Stat`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`, `Statfs`)

### 📊 Proposal #41260

#### File Embeddings - Directory Level
- ❌ `src/testing`

#### File Embeddings - File Level
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/testing`

#### Function Embeddings - File Level
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/testing/testing.go`, `Setenv`)
- ❌ (`src/testing/testing.go`, `Parallel`)
- ❌ (`src/testing/testing.go`, `Setenv`)
- ❌ (`src/testing/testing_test.go`, `TestSetenv`)

### 📊 Proposal #41563

#### File Embeddings - Directory Level
- ❌ `src/encoding/asn1`
- ❌ `src/encoding/json`
- ❌ `src/encoding/xml`
- ❌ `src/net/rpc`
- ✅ `src/reflect`
- ❌ `src/text/template`

#### File Embeddings - File Level
- ❌ `src/encoding/asn1/asn1.go`
- ❌ `src/encoding/asn1/marshal.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/xml/typeinfo.go`
- ❌ `src/net/rpc/server.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/type.go`
- ❌ `src/text/template/exec.go`

#### Function Embeddings - Directory Level
- ✅ `src/encoding/asn1`
- ❌ `src/encoding/json`
- ❌ `src/encoding/xml`
- ❌ `src/net/rpc`
- ✅ `src/reflect`
- ❌ `src/text/template`

#### Function Embeddings - File Level
- ❌ `src/encoding/asn1/asn1.go`
- ❌ `src/encoding/asn1/marshal.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/xml/typeinfo.go`
- ❌ `src/net/rpc/server.go`
- ✅ `src/reflect/all_test.go`
- ✅ `src/reflect/type.go`
- ❌ `src/text/template/exec.go`

#### Function Embeddings - Function Level
- ❌ (`src/encoding/json/encode.go`, `typeFields`)
- ❌ (`src/net/rpc/server.go`, `suitableMethods`)
- ✅ (`src/reflect/type.go`, `IsExported`)
- ✅ (`src/reflect/type.go`, `IsExported`)
- ❌ (`src/reflect/type.go`, `StructOf`)
- ❌ (`src/reflect/type.go`, `runtimeStructField`)
- ❌ (`src/encoding/asn1/asn1.go`, `parseField`)
- ✅ (`src/reflect/all_test.go`, `TestFieldPkgPath`)
- ❌ (`src/reflect/all_test.go`, `TestMethodPkgPath`)
- ❌ (`src/text/template/exec.go`, `evalField`)
- ❌ (`src/encoding/xml/typeinfo.go`, `getTypeInfo`)
- ❌ (`src/encoding/asn1/marshal.go`, `makeBody`)

### 📊 Proposal #41682

#### File Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### File Embeddings - File Level
- ❌ `src/crypto/x509/verify_test.go`
- ❌ `src/crypto/x509/x509.go`
- ❌ `src/crypto/x509/x509_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### Function Embeddings - File Level
- ❌ `src/crypto/x509/verify_test.go`
- ❌ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateSelfSignedCertificate`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateCertificateRequest`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestInsecureAlgorithmErrorString`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestSHA1`)
- ❌ (`src/crypto/x509/x509_test.go`, `Public`)
- ❌ (`src/crypto/x509/x509_test.go`, `Sign`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateCertificateBrokenSigner`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateCertificateLegacy`)
- ❌ (`src/crypto/x509/x509_test.go`, `BenchmarkParseCertificate`)
- ❌ (`src/crypto/x509/verify_test.go`, `TestGoVerify`)
- ❌ (`src/crypto/x509/x509.go`, `Error`)
- ❌ (`src/crypto/x509/x509.go`, `checkSignature`)
- ❌ (`src/crypto/x509/x509.go`, `CreateCertificate`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateCertificateLegacy`)
- ❌ (`src/crypto/x509/x509_test.go`, `mustCert`)
- ❌ (`src/crypto/x509/x509_test.go`, `allCerts`)
- ✅ (`src/crypto/x509/x509_test.go`, `TestDisableSHA1ForCertOnly`)
- ❌ (`src/crypto/x509/x509.go`, `CheckSignatureFrom`)
- ❌ (`src/crypto/x509/x509.go`, `CheckSignature`)
- ❌ (`src/crypto/x509/x509.go`, `checkSignature`)
- ❌ (`src/crypto/x509/x509.go`, `CreateCertificate`)
- ❌ (`src/crypto/x509/x509.go`, `CheckSignature`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateCertificateLegacy`)
- ❌ (`src/crypto/x509/x509_test.go`, `mustCert`)
- ❌ (`src/crypto/x509/x509_test.go`, `allCerts`)
- ✅ (`src/crypto/x509/x509_test.go`, `TestDisableSHA1ForCertOnly`)
- ❌ (`src/crypto/x509/x509.go`, `CheckSignatureFrom`)
- ❌ (`src/crypto/x509/x509.go`, `CheckSignature`)
- ❌ (`src/crypto/x509/x509.go`, `checkSignature`)
- ❌ (`src/crypto/x509/x509.go`, `CreateCertificate`)
- ❌ (`src/crypto/x509/x509.go`, `CheckSignature`)

### 📊 Proposal #41696

#### File Embeddings - Directory Level
- ✅ `src/cmd/dist`
- ✅ `src/cmd/go`
- ❌ `src/cmd/go/internal/test`
- ✅ `src/cmd/go/internal/work`
- ❌ `src/cmd/link`

#### File Embeddings - File Level
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/go/internal/test/testflag.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/link/dwarf_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/dist`
- ✅ `src/cmd/go`
- ❌ `src/cmd/go/internal/test`
- ✅ `src/cmd/go/internal/work`
- ❌ `src/cmd/link`

#### Function Embeddings - File Level
- ✅ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/test.go`
- ✅ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/go/internal/test/testflag.go`
- ✅ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/link/dwarf_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/work/build.go`, `runBuild`)
- ✅ (`src/cmd/go/internal/work/build.go`, `runInstall`)
- ❌ (`src/cmd/go/internal/test/test.go`, `runTest`)
- ❌ (`src/cmd/link/dwarf_test.go`, `TestMain`)
- ❌ (`src/cmd/link/dwarf_test.go`, `testDWARF`)
- ❌ (`src/cmd/dist/test.go`, `run`)
- ❌ (`src/cmd/go/internal/work/build.go`, `init`)
- ❌ (`src/cmd/go/internal/work/build.go`, `runBuild`)
- ✅ (`src/cmd/go/internal/work/build.go`, `runInstall`)
- ❌ (`src/cmd/go/internal/work/build.go`, `omitTestOnly`)
- ❌ (`src/cmd/go/internal/work/build.go`, `InstallPackages`)
- ❌ (`src/cmd/go/internal/test/test.go`, `runTest`)
- ❌ (`src/cmd/go/go_test.go`, `TestNewReleaseRebuildsStalePackagesInGOPATH`)
- ❌ (`src/cmd/go/go_test.go`, `TestInstallWithTags`)
- ❌ (`src/cmd/go/go_test.go`, `TestParallelTest`)
- ❌ (`src/cmd/go/go_test.go`, `TestImportPath`)
- ❌ (`src/cmd/dist/build.go`, `cmdbootstrap`)
- ❌ (`src/cmd/go/internal/test/testflag.go`, `init`)
- ❌ (`src/cmd/go/internal/test/testflag.go`, `testFlags`)

### 📊 Proposal #41730

#### File Embeddings - Directory Level
- ✅ `src/cmd/go`
- ❌ `src/cmd/go/internal/envcmd`
- ❌ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/modget`
- ✅ `src/cmd/go/internal/vcs`

#### File Embeddings - File Level
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/envcmd/env.go`
- ❌ `src/cmd/go/internal/modfetch/proxy.go`
- ❌ `src/cmd/go/internal/modget/get.go`
- ✅ `src/cmd/go/internal/vcs/vcs.go`
- ✅ `src/cmd/go/internal/vcs/vcs_test.go`
- ❌ `src/cmd/go/main.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/envcmd`
- ❌ `src/cmd/go/internal/modfetch`
- ✅ `src/cmd/go/internal/modget`
- ✅ `src/cmd/go/internal/vcs`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/envcmd/env.go`
- ❌ `src/cmd/go/internal/modfetch/proxy.go`
- ✅ `src/cmd/go/internal/modget/get.go`
- ✅ `src/cmd/go/internal/vcs/vcs.go`
- ❌ `src/cmd/go/internal/vcs/vcs_test.go`
- ❌ `src/cmd/go/main.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/envcmd/env.go`, `MkEnv`)
- ❌ (`src/cmd/go/internal/vcs/vcs_test.go`, `init`)
- ❌ (`src/cmd/go/internal/vcs/vcs_test.go`, `TestGOVCS`)
- ❌ (`src/cmd/go/internal/vcs/vcs_test.go`, `TestGOVCSErrors`)
- ❌ (`src/cmd/go/main.go`, `init`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `FromDir`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `parseGOVCS`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `allow`)
- ✅ (`src/cmd/go/internal/vcs/vcs.go`, `checkGOVCS`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `repoRootFromVCSPaths`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `repoRootForImportDynamic`)
- ❌ (`src/cmd/go/internal/envcmd/env.go`, `MkEnv`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `Set`)
- ❌ (`src/cmd/go/internal/modget/get.go`, `init`)
- ❌ (`src/cmd/go/internal/vcs/vcs_test.go`, `TestRepoRootForImportPath`)
- ❌ (`src/cmd/go/main.go`, `init`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `FromDir`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `httpPrefix`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `RepoRootForImportPath`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `repoRootFromVCSPaths`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `validateRepoRoot`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `matchGoImport`)
- ❌ (`src/cmd/go/internal/envcmd/env.go`, `MkEnv`)
- ❌ (`src/cmd/go/internal/vcs/vcs_test.go`, `init`)
- ❌ (`src/cmd/go/internal/vcs/vcs_test.go`, `TestGOVCS`)
- ❌ (`src/cmd/go/internal/vcs/vcs_test.go`, `TestGOVCSErrors`)
- ❌ (`src/cmd/go/main.go`, `init`)
- ❌ (`src/cmd/go/go_test.go`, `init`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `FromDir`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `parseGOVCS`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `allow`)
- ✅ (`src/cmd/go/internal/vcs/vcs.go`, `checkGOVCS`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `repoRootFromVCSPaths`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `repoRootForImportDynamic`)
- ❌ (`src/cmd/go/internal/modfetch/proxy.go`, `proxyList`)

### 📊 Proposal #41773

#### File Embeddings - Directory Level
- ❌ `src/net/http`

#### File Embeddings - File Level
- ❌ `src/net/http/serve_test.go`
- ❌ `src/net/http/server.go`

#### Function Embeddings - Directory Level
- ❌ `src/net/http`

#### Function Embeddings - File Level
- ❌ `src/net/http/serve_test.go`
- ❌ `src/net/http/server.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/http/serve_test.go`, `TestOptionsHandler`)
- ❌ (`src/net/http/server.go`, `ServeHTTP`)
- ❌ (`src/net/http/serve_test.go`, `TestOptionsHandler`)
- ❌ (`src/net/http/server.go`, `ServeHTTP`)

### 📊 Proposal #41790

#### File Embeddings - Directory Level
- ✅ `src/database/sql`

#### File Embeddings - File Level
- ❌ `src/database/sql/fakedb_test.go`
- ❌ `src/database/sql/sql.go`
- ✅ `src/database/sql/sql_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/database/sql`

#### Function Embeddings - File Level
- ❌ `src/database/sql/fakedb_test.go`
- ✅ `src/database/sql/sql.go`
- ❌ `src/database/sql/sql_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/database/sql/fakedb_test.go`, `Close`)
- ❌ (`src/database/sql/sql_test.go`, `TestOpenConnector`)
- ❌ (`src/database/sql/sql.go`, `Close`)

### 📊 Proposal #41792

#### File Embeddings - Directory Level
- ✅ `src/flag`

#### File Embeddings - File Level
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/flag`

#### Function Embeddings - File Level
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/flag/flag.go`, `Var`)
- ❌ (`src/flag/flag.go`, `Var`)
- ❌ (`src/flag/flag.go`, `sprintf`)
- ❌ (`src/flag/flag.go`, `failf`)
- ❌ (`src/flag/flag_test.go`, `mustPanic`)
- ✅ (`src/flag/flag_test.go`, `TestInvalidFlags`)
- ❌ (`src/flag/flag_test.go`, `TestRedefinedFlags`)

### 📊 Proposal #41980

#### File Embeddings - Directory Level
- ❌ `src/internal/diff`
- ❌ `src/testing`

#### File Embeddings - File Level
- ❌ `src/internal/diff/diff_test.go`
- ❌ `src/testing/example.go`

#### Function Embeddings - Directory Level
- ❌ `src/internal/diff`
- ❌ `src/testing`

#### Function Embeddings - File Level
- ❌ `src/internal/diff/diff_test.go`
- ❌ `src/testing/example.go`

#### Function Embeddings - Function Level
- ❌ (`src/testing/example.go`, `processRunResult`)
- ❌ (`src/internal/diff/diff_test.go`, `Test`)

### 📊 Proposal #42026

#### File Embeddings - Directory Level
- ❌ `src/archive/tar`
- ❌ `src/archive/zip`
- ❌ `src/cmd/addr2line`
- ❌ `src/cmd/cover`
- ❌ `src/cmd/fix`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/bug`
- ❌ `src/cmd/go/internal/cache`
- ❌ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/go/internal/clean`
- ❌ `src/cmd/go/internal/envcmd`
- ❌ `src/cmd/go/internal/fsys`
- ❌ `src/cmd/go/internal/generate`
- ❌ `src/cmd/go/internal/imports`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/lockedfile`
- ❌ `src/cmd/go/internal/lockedfile/internal/filelock`
- ❌ `src/cmd/go/internal/modcmd`
- ❌ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ❌ `src/cmd/go/internal/modfetch/zip_sum_test`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/test`
- ❌ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/web`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/go/testdata`
- ❌ `src/cmd/gofmt`
- ❌ `src/cmd/nm`
- ❌ `src/cmd/objdump`
- ❌ `src/cmd/pack`
- ❌ `src/cmd/vet`
- ❌ `src/compress/bzip2`
- ❌ `src/compress/flate`
- ❌ `src/compress/lzw`
- ❌ `src/compress/zlib`
- ❌ `src/crypto/md5`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/debug/dwarf`
- ❌ `src/debug/gosym`
- ❌ `src/debug/pe`
- ❌ `src/embed/internal/embedtest`
- ❌ `src/go/build`
- ❌ `src/go/doc`
- ❌ `src/go/format`
- ❌ `src/go/importer`
- ❌ `src/go/internal/gccgoimporter`
- ❌ `src/go/internal/gcimporter`
- ❌ `src/go/internal/srcimporter`
- ❌ `src/go/parser`
- ❌ `src/go/printer`
- ❌ `src/go/types`
- ❌ `src/hash/crc32`
- ❌ `src/html/template`
- ❌ `src/image/color/palette`
- ❌ `src/image/gif`
- ❌ `src/image/internal/imageutil`
- ❌ `src/image/jpeg`
- ❌ `src/image/png`
- ❌ `src/index/suffixarray`
- ❌ `src/internal/cpu`
- ❌ `src/internal/obscuretestdata`
- ❌ `src/internal/poll`
- ❌ `src/internal/trace`
- ✅ `src/io/ioutil`
- ❌ `src/log/syslog`
- ❌ `src/math/big`
- ❌ `src/math/bits`
- ❌ `src/mime/multipart`
- ❌ `src/net`
- ❌ `src/net/http`
- ✅ `src/os`
- ❌ `src/os/exec`
- ❌ `src/os/signal`
- ❌ `src/os/user`
- ❌ `src/path/filepath`
- ❌ `src/runtime`
- ❌ `src/runtime/debug`
- ❌ `src/runtime/pprof`
- ❌ `src/runtime/race`
- ❌ `src/runtime/race/testdata`
- ❌ `src/runtime/testdata/testprog`
- ❌ `src/runtime/testdata/testprogcgo`
- ❌ `src/runtime/trace`
- ❌ `src/strconv`
- ❌ `src/syscall`
- ❌ `src/testing`
- ❌ `src/text/template`
- ❌ `src/time`

#### File Embeddings - File Level
- ❌ `src/archive/tar/reader_test.go`
- ❌ `src/archive/tar/tar_test.go`
- ❌ `src/archive/tar/writer_test.go`
- ❌ `src/archive/zip/reader_test.go`
- ❌ `src/archive/zip/writer_test.go`
- ❌ `src/cmd/addr2line/addr2line_test.go`
- ❌ `src/cmd/cover/cover.go`
- ❌ `src/cmd/cover/cover_test.go`
- ❌ `src/cmd/cover/html.go`
- ❌ `src/cmd/fix/main.go`
- ❌ `src/cmd/fix/typecheck.go`
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/go_windows_test.go`
- ❌ `src/cmd/go/help_test.go`
- ❌ `src/cmd/go/internal/bug/bug.go`
- ❌ `src/cmd/go/internal/cache/cache.go`
- ❌ `src/cmd/go/internal/cache/cache_test.go`
- ❌ `src/cmd/go/internal/cache/default.go`
- ❌ `src/cmd/go/internal/cache/hash_test.go`
- ❌ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/go/internal/clean/clean.go`
- ❌ `src/cmd/go/internal/envcmd/env.go`
- ❌ `src/cmd/go/internal/fsys/fsys.go`
- ❌ `src/cmd/go/internal/fsys/fsys_test.go`
- ❌ `src/cmd/go/internal/generate/generate.go`
- ❌ `src/cmd/go/internal/imports/scan_test.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/lockedfile/internal/filelock/filelock_test.go`
- ❌ `src/cmd/go/internal/lockedfile/lockedfile_test.go`
- ❌ `src/cmd/go/internal/modcmd/vendor.go`
- ❌ `src/cmd/go/internal/modcmd/verify.go`
- ❌ `src/cmd/go/internal/modfetch/cache.go`
- ❌ `src/cmd/go/internal/modfetch/cache_test.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/codehost.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/git_test.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/shell.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ❌ `src/cmd/go/internal/modfetch/coderepo.go`
- ❌ `src/cmd/go/internal/modfetch/coderepo_test.go`
- ❌ `src/cmd/go/internal/modfetch/fetch.go`
- ❌ `src/cmd/go/internal/modfetch/zip_sum_test/zip_sum_test.go`
- ❌ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/modload/query_test.go`
- ❌ `src/cmd/go/internal/modload/vendor.go`
- ❌ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/go/internal/vcs/vcs_test.go`
- ❌ `src/cmd/go/internal/web/file_test.go`
- ❌ `src/cmd/go/internal/work/build_test.go`
- ❌ `src/cmd/go/internal/work/buildid.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`
- ❌ `src/cmd/go/proxy_test.go`
- ❌ `src/cmd/go/testdata/addmod.go`
- ❌ `src/cmd/go/testdata/savedir.go`
- ❌ `src/cmd/gofmt/gofmt.go`
- ❌ `src/cmd/gofmt/gofmt_test.go`
- ❌ `src/cmd/nm/nm_test.go`
- ❌ `src/cmd/objdump/objdump_test.go`
- ❌ `src/cmd/pack/pack_test.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/compress/bzip2/bzip2_test.go`
- ❌ `src/compress/flate/deflate_test.go`
- ❌ `src/compress/flate/huffman_bit_writer_test.go`
- ❌ `src/compress/flate/reader_test.go`
- ❌ `src/compress/lzw/reader_test.go`
- ❌ `src/compress/lzw/writer_test.go`
- ❌ `src/compress/zlib/writer_test.go`
- ❌ `src/crypto/md5/gen.go`
- ❌ `src/crypto/tls/handshake_test.go`
- ❌ `src/crypto/tls/link_test.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/crypto/x509/name_constraints_test.go`
- ❌ `src/crypto/x509/root_plan9.go`
- ❌ `src/crypto/x509/root_unix.go`
- ❌ `src/crypto/x509/root_unix_test.go`
- ❌ `src/debug/dwarf/dwarf5ranges_test.go`
- ❌ `src/debug/gosym/pclntab_test.go`
- ❌ `src/debug/pe/file_test.go`
- ❌ `src/embed/internal/embedtest/embedx_test.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/go/build/deps_test.go`
- ❌ `src/go/doc/doc_test.go`
- ❌ `src/go/format/benchmark_test.go`
- ❌ `src/go/format/format_test.go`
- ❌ `src/go/importer/importer_test.go`
- ❌ `src/go/internal/gccgoimporter/importer_test.go`
- ❌ `src/go/internal/gcimporter/gcimporter_test.go`
- ❌ `src/go/internal/srcimporter/srcimporter.go`
- ❌ `src/go/internal/srcimporter/srcimporter_test.go`
- ❌ `src/go/parser/error_test.go`
- ❌ `src/go/parser/interface.go`
- ❌ `src/go/parser/performance_test.go`
- ❌ `src/go/printer/performance_test.go`
- ❌ `src/go/printer/printer_test.go`
- ❌ `src/go/types/check_test.go`
- ❌ `src/go/types/hilbert_test.go`
- ❌ `src/go/types/stdlib_test.go`
- ❌ `src/hash/crc32/gen_const_ppc64le.go`
- ❌ `src/html/template/examplefiles_test.go`
- ❌ `src/html/template/template.go`
- ❌ `src/image/color/palette/gen.go`
- ❌ `src/image/gif/reader_test.go`
- ❌ `src/image/internal/imageutil/gen.go`
- ❌ `src/image/jpeg/reader_test.go`
- ❌ `src/image/png/reader_test.go`
- ❌ `src/index/suffixarray/gen.go`
- ❌ `src/index/suffixarray/suffixarray_test.go`
- ❌ `src/internal/cpu/cpu_s390x_test.go`
- ❌ `src/internal/obscuretestdata/obscuretestdata.go`
- ❌ `src/internal/poll/read_test.go`
- ❌ `src/internal/trace/gc_test.go`
- ❌ `src/io/ioutil/ioutil.go`
- ❌ `src/io/ioutil/tempfile.go`
- ❌ `src/io/ioutil/tempfile_test.go`
- ❌ `src/log/syslog/syslog_test.go`
- ❌ `src/math/big/link_test.go`
- ❌ `src/math/bits/make_examples.go`
- ❌ `src/math/bits/make_tables.go`
- ❌ `src/mime/multipart/formdata.go`
- ❌ `src/net/dnsclient_unix_test.go`
- ❌ `src/net/error_test.go`
- ❌ `src/net/http/filetransport_test.go`
- ❌ `src/net/http/fs_test.go`
- ❌ `src/net/http/request_test.go`
- ❌ `src/net/http/transfer_test.go`
- ❌ `src/net/http/transport_test.go`
- ❌ `src/net/mockserver_test.go`
- ❌ `src/net/net_windows_test.go`
- ❌ `src/net/unixsock_test.go`
- ✅ `src/os/dir.go`
- ❌ `src/os/error_test.go`
- ❌ `src/os/example_test.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/lp_unix_test.go`
- ❌ `src/os/exec/lp_windows_test.go`
- ❌ `src/os/fifo_test.go`
- ❌ `src/os/file.go`
- ❌ `src/os/file_plan9.go`
- ❌ `src/os/os_test.go`
- ❌ `src/os/os_unix_test.go`
- ❌ `src/os/os_windows_test.go`
- ❌ `src/os/path_test.go`
- ❌ `src/os/path_windows_test.go`
- ❌ `src/os/pipe_test.go`
- ❌ `src/os/read_test.go`
- ❌ `src/os/removeall_test.go`
- ❌ `src/os/signal/signal_test.go`
- ❌ `src/os/signal/signal_windows_test.go`
- ❌ `src/os/stat_test.go`
- ❌ `src/os/tempfile.go`
- ❌ `src/os/tempfile_test.go`
- ❌ `src/os/timeout_test.go`
- ❌ `src/os/user/lookup_plan9.go`
- ❌ `src/path/filepath/example_unix_walk_test.go`
- ❌ `src/path/filepath/match_test.go`
- ❌ `src/path/filepath/path_test.go`
- ❌ `src/path/filepath/path_windows_test.go`
- ❌ `src/runtime/crash_test.go`
- ❌ `src/runtime/crash_unix_test.go`
- ❌ `src/runtime/debug/heapdump_test.go`
- ❌ `src/runtime/debug_test.go`
- ❌ `src/runtime/memmove_linux_amd64_test.go`
- ❌ `src/runtime/mkduff.go`
- ❌ `src/runtime/mkfastlog2table.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/proto_test.go`
- ❌ `src/runtime/race/output_test.go`
- ❌ `src/runtime/race/testdata/io_test.go`
- ❌ `src/runtime/runtime-gdb_test.go`
- ❌ `src/runtime/runtime-lldb_test.go`
- ❌ `src/runtime/signal_windows_test.go`
- ❌ `src/runtime/syscall_windows_test.go`
- ❌ `src/runtime/testdata/testprog/memprof.go`
- ❌ `src/runtime/testdata/testprog/syscalls_linux.go`
- ❌ `src/runtime/testdata/testprog/timeprof.go`
- ❌ `src/runtime/testdata/testprog/vdso.go`
- ❌ `src/runtime/testdata/testprogcgo/pprof.go`
- ❌ `src/runtime/testdata/testprogcgo/threadpprof.go`
- ❌ `src/runtime/trace/trace_test.go`
- ❌ `src/runtime/wincallback.go`
- ❌ `src/strconv/makeisprint.go`
- ❌ `src/syscall/dirent_test.go`
- ❌ `src/syscall/exec_linux_test.go`
- ❌ `src/syscall/getdirentries_test.go`
- ❌ `src/syscall/syscall_linux_test.go`
- ❌ `src/syscall/syscall_unix_test.go`
- ❌ `src/syscall/syscall_windows_test.go`
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`
- ❌ `src/text/template/examplefiles_test.go`
- ❌ `src/text/template/helper.go`
- ❌ `src/text/template/link_test.go`
- ❌ `src/time/genzabbrs.go`

#### Function Embeddings - Directory Level
- ❌ `src/archive/tar`
- ❌ `src/archive/zip`
- ❌ `src/cmd/addr2line`
- ❌ `src/cmd/cover`
- ❌ `src/cmd/fix`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/bug`
- ❌ `src/cmd/go/internal/cache`
- ❌ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/go/internal/clean`
- ❌ `src/cmd/go/internal/envcmd`
- ✅ `src/cmd/go/internal/fsys`
- ❌ `src/cmd/go/internal/generate`
- ❌ `src/cmd/go/internal/imports`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/lockedfile`
- ❌ `src/cmd/go/internal/lockedfile/internal/filelock`
- ❌ `src/cmd/go/internal/modcmd`
- ❌ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ❌ `src/cmd/go/internal/modfetch/zip_sum_test`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/test`
- ❌ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/web`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/go/testdata`
- ❌ `src/cmd/gofmt`
- ❌ `src/cmd/nm`
- ❌ `src/cmd/objdump`
- ❌ `src/cmd/pack`
- ❌ `src/cmd/vet`
- ❌ `src/compress/bzip2`
- ❌ `src/compress/flate`
- ❌ `src/compress/lzw`
- ❌ `src/compress/zlib`
- ❌ `src/crypto/md5`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/debug/dwarf`
- ❌ `src/debug/gosym`
- ❌ `src/debug/pe`
- ❌ `src/embed/internal/embedtest`
- ❌ `src/go/build`
- ❌ `src/go/doc`
- ❌ `src/go/format`
- ❌ `src/go/importer`
- ❌ `src/go/internal/gccgoimporter`
- ❌ `src/go/internal/gcimporter`
- ❌ `src/go/internal/srcimporter`
- ❌ `src/go/parser`
- ❌ `src/go/printer`
- ❌ `src/go/types`
- ❌ `src/hash/crc32`
- ❌ `src/html/template`
- ❌ `src/image/color/palette`
- ❌ `src/image/gif`
- ❌ `src/image/internal/imageutil`
- ❌ `src/image/jpeg`
- ❌ `src/image/png`
- ❌ `src/index/suffixarray`
- ❌ `src/internal/cpu`
- ❌ `src/internal/obscuretestdata`
- ❌ `src/internal/poll`
- ❌ `src/internal/trace`
- ✅ `src/io/ioutil`
- ❌ `src/log/syslog`
- ❌ `src/math/big`
- ❌ `src/math/bits`
- ❌ `src/mime/multipart`
- ❌ `src/net`
- ❌ `src/net/http`
- ✅ `src/os`
- ❌ `src/os/exec`
- ❌ `src/os/signal`
- ❌ `src/os/user`
- ❌ `src/path/filepath`
- ❌ `src/runtime`
- ❌ `src/runtime/debug`
- ❌ `src/runtime/pprof`
- ❌ `src/runtime/race`
- ❌ `src/runtime/race/testdata`
- ❌ `src/runtime/testdata/testprog`
- ❌ `src/runtime/testdata/testprogcgo`
- ❌ `src/runtime/trace`
- ❌ `src/strconv`
- ❌ `src/syscall`
- ❌ `src/testing`
- ❌ `src/text/template`
- ❌ `src/time`

#### Function Embeddings - File Level
- ❌ `src/archive/tar/reader_test.go`
- ❌ `src/archive/tar/tar_test.go`
- ❌ `src/archive/tar/writer_test.go`
- ❌ `src/archive/zip/reader_test.go`
- ❌ `src/archive/zip/writer_test.go`
- ❌ `src/cmd/addr2line/addr2line_test.go`
- ❌ `src/cmd/cover/cover.go`
- ❌ `src/cmd/cover/cover_test.go`
- ❌ `src/cmd/cover/html.go`
- ❌ `src/cmd/fix/main.go`
- ❌ `src/cmd/fix/typecheck.go`
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/go_windows_test.go`
- ❌ `src/cmd/go/help_test.go`
- ❌ `src/cmd/go/internal/bug/bug.go`
- ❌ `src/cmd/go/internal/cache/cache.go`
- ❌ `src/cmd/go/internal/cache/cache_test.go`
- ❌ `src/cmd/go/internal/cache/default.go`
- ❌ `src/cmd/go/internal/cache/hash_test.go`
- ❌ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/go/internal/clean/clean.go`
- ❌ `src/cmd/go/internal/envcmd/env.go`
- ❌ `src/cmd/go/internal/fsys/fsys.go`
- ✅ `src/cmd/go/internal/fsys/fsys_test.go`
- ❌ `src/cmd/go/internal/generate/generate.go`
- ❌ `src/cmd/go/internal/imports/scan_test.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/lockedfile/internal/filelock/filelock_test.go`
- ❌ `src/cmd/go/internal/lockedfile/lockedfile_test.go`
- ❌ `src/cmd/go/internal/modcmd/vendor.go`
- ❌ `src/cmd/go/internal/modcmd/verify.go`
- ❌ `src/cmd/go/internal/modfetch/cache.go`
- ❌ `src/cmd/go/internal/modfetch/cache_test.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/codehost.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/git_test.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/shell.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ❌ `src/cmd/go/internal/modfetch/coderepo.go`
- ❌ `src/cmd/go/internal/modfetch/coderepo_test.go`
- ❌ `src/cmd/go/internal/modfetch/fetch.go`
- ❌ `src/cmd/go/internal/modfetch/zip_sum_test/zip_sum_test.go`
- ❌ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/modload/query_test.go`
- ❌ `src/cmd/go/internal/modload/vendor.go`
- ❌ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/go/internal/vcs/vcs_test.go`
- ❌ `src/cmd/go/internal/web/file_test.go`
- ❌ `src/cmd/go/internal/work/build_test.go`
- ❌ `src/cmd/go/internal/work/buildid.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`
- ❌ `src/cmd/go/proxy_test.go`
- ❌ `src/cmd/go/testdata/addmod.go`
- ❌ `src/cmd/go/testdata/savedir.go`
- ❌ `src/cmd/gofmt/gofmt.go`
- ❌ `src/cmd/gofmt/gofmt_test.go`
- ❌ `src/cmd/nm/nm_test.go`
- ❌ `src/cmd/objdump/objdump_test.go`
- ❌ `src/cmd/pack/pack_test.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/compress/bzip2/bzip2_test.go`
- ❌ `src/compress/flate/deflate_test.go`
- ❌ `src/compress/flate/huffman_bit_writer_test.go`
- ❌ `src/compress/flate/reader_test.go`
- ❌ `src/compress/lzw/reader_test.go`
- ❌ `src/compress/lzw/writer_test.go`
- ❌ `src/compress/zlib/writer_test.go`
- ❌ `src/crypto/md5/gen.go`
- ❌ `src/crypto/tls/handshake_test.go`
- ❌ `src/crypto/tls/link_test.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/crypto/x509/name_constraints_test.go`
- ❌ `src/crypto/x509/root_plan9.go`
- ❌ `src/crypto/x509/root_unix.go`
- ❌ `src/crypto/x509/root_unix_test.go`
- ❌ `src/debug/dwarf/dwarf5ranges_test.go`
- ❌ `src/debug/gosym/pclntab_test.go`
- ❌ `src/debug/pe/file_test.go`
- ❌ `src/embed/internal/embedtest/embedx_test.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/go/build/deps_test.go`
- ❌ `src/go/doc/doc_test.go`
- ❌ `src/go/format/benchmark_test.go`
- ❌ `src/go/format/format_test.go`
- ❌ `src/go/importer/importer_test.go`
- ❌ `src/go/internal/gccgoimporter/importer_test.go`
- ❌ `src/go/internal/gcimporter/gcimporter_test.go`
- ❌ `src/go/internal/srcimporter/srcimporter.go`
- ❌ `src/go/internal/srcimporter/srcimporter_test.go`
- ❌ `src/go/parser/error_test.go`
- ❌ `src/go/parser/interface.go`
- ❌ `src/go/parser/performance_test.go`
- ❌ `src/go/printer/performance_test.go`
- ❌ `src/go/printer/printer_test.go`
- ❌ `src/go/types/check_test.go`
- ❌ `src/go/types/hilbert_test.go`
- ❌ `src/go/types/stdlib_test.go`
- ❌ `src/hash/crc32/gen_const_ppc64le.go`
- ❌ `src/html/template/examplefiles_test.go`
- ❌ `src/html/template/template.go`
- ❌ `src/image/color/palette/gen.go`
- ❌ `src/image/gif/reader_test.go`
- ❌ `src/image/internal/imageutil/gen.go`
- ❌ `src/image/jpeg/reader_test.go`
- ❌ `src/image/png/reader_test.go`
- ❌ `src/index/suffixarray/gen.go`
- ❌ `src/index/suffixarray/suffixarray_test.go`
- ❌ `src/internal/cpu/cpu_s390x_test.go`
- ❌ `src/internal/obscuretestdata/obscuretestdata.go`
- ❌ `src/internal/poll/read_test.go`
- ❌ `src/internal/trace/gc_test.go`
- ❌ `src/io/ioutil/ioutil.go`
- ❌ `src/io/ioutil/tempfile.go`
- ❌ `src/io/ioutil/tempfile_test.go`
- ❌ `src/log/syslog/syslog_test.go`
- ❌ `src/math/big/link_test.go`
- ❌ `src/math/bits/make_examples.go`
- ❌ `src/math/bits/make_tables.go`
- ❌ `src/mime/multipart/formdata.go`
- ❌ `src/net/dnsclient_unix_test.go`
- ❌ `src/net/error_test.go`
- ❌ `src/net/http/filetransport_test.go`
- ❌ `src/net/http/fs_test.go`
- ❌ `src/net/http/request_test.go`
- ❌ `src/net/http/transfer_test.go`
- ❌ `src/net/http/transport_test.go`
- ❌ `src/net/mockserver_test.go`
- ❌ `src/net/net_windows_test.go`
- ❌ `src/net/unixsock_test.go`
- ❌ `src/os/dir.go`
- ❌ `src/os/error_test.go`
- ❌ `src/os/example_test.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/lp_unix_test.go`
- ❌ `src/os/exec/lp_windows_test.go`
- ❌ `src/os/fifo_test.go`
- ❌ `src/os/file.go`
- ❌ `src/os/file_plan9.go`
- ❌ `src/os/os_test.go`
- ❌ `src/os/os_unix_test.go`
- ❌ `src/os/os_windows_test.go`
- ❌ `src/os/path_test.go`
- ❌ `src/os/path_windows_test.go`
- ❌ `src/os/pipe_test.go`
- ❌ `src/os/read_test.go`
- ❌ `src/os/removeall_test.go`
- ❌ `src/os/signal/signal_test.go`
- ❌ `src/os/signal/signal_windows_test.go`
- ❌ `src/os/stat_test.go`
- ❌ `src/os/tempfile.go`
- ❌ `src/os/tempfile_test.go`
- ❌ `src/os/timeout_test.go`
- ❌ `src/os/user/lookup_plan9.go`
- ❌ `src/path/filepath/example_unix_walk_test.go`
- ❌ `src/path/filepath/match_test.go`
- ❌ `src/path/filepath/path_test.go`
- ❌ `src/path/filepath/path_windows_test.go`
- ❌ `src/runtime/crash_test.go`
- ❌ `src/runtime/crash_unix_test.go`
- ❌ `src/runtime/debug/heapdump_test.go`
- ❌ `src/runtime/debug_test.go`
- ❌ `src/runtime/memmove_linux_amd64_test.go`
- ❌ `src/runtime/mkduff.go`
- ❌ `src/runtime/mkfastlog2table.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/proto_test.go`
- ❌ `src/runtime/race/output_test.go`
- ❌ `src/runtime/race/testdata/io_test.go`
- ❌ `src/runtime/runtime-gdb_test.go`
- ❌ `src/runtime/runtime-lldb_test.go`
- ❌ `src/runtime/signal_windows_test.go`
- ❌ `src/runtime/syscall_windows_test.go`
- ❌ `src/runtime/testdata/testprog/memprof.go`
- ❌ `src/runtime/testdata/testprog/syscalls_linux.go`
- ❌ `src/runtime/testdata/testprog/timeprof.go`
- ❌ `src/runtime/testdata/testprog/vdso.go`
- ❌ `src/runtime/testdata/testprogcgo/pprof.go`
- ❌ `src/runtime/testdata/testprogcgo/threadpprof.go`
- ❌ `src/runtime/trace/trace_test.go`
- ❌ `src/runtime/wincallback.go`
- ❌ `src/strconv/makeisprint.go`
- ❌ `src/syscall/dirent_test.go`
- ❌ `src/syscall/exec_linux_test.go`
- ❌ `src/syscall/getdirentries_test.go`
- ❌ `src/syscall/syscall_linux_test.go`
- ❌ `src/syscall/syscall_unix_test.go`
- ❌ `src/syscall/syscall_windows_test.go`
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`
- ❌ `src/text/template/examplefiles_test.go`
- ❌ `src/text/template/helper.go`
- ❌ `src/text/template/link_test.go`
- ❌ `src/time/genzabbrs.go`

#### Function Embeddings - Function Level
- ❌ (`src/io/ioutil/ioutil.go`, `ReadFile`)
- ❌ (`src/io/ioutil/ioutil.go`, `WriteFile`)
- ❌ (`src/io/ioutil/ioutil.go`, `ReadDir`)
- ❌ (`src/io/ioutil/ioutil.go`, `NopCloser`)
- ❌ (`src/os/os_test.go`, `checkSize`)
- ❌ (`src/os/os_test.go`, `TestReadFileProc`)
- ❌ (`src/os/example_test.go`, `ExampleReadDir`)
- ❌ (`src/os/example_test.go`, `ExampleMkdirTemp`)
- ❌ (`src/os/example_test.go`, `ExampleMkdirTemp_suffix`)
- ❌ (`src/os/example_test.go`, `ExampleCreateTemp`)
- ❌ (`src/os/example_test.go`, `ExampleCreateTemp_suffix`)
- ❌ (`src/os/example_test.go`, `ExampleReadFile`)
- ❌ (`src/os/example_test.go`, `ExampleWriteFile`)
- ❌ (`src/os/tempfile.go`, `nextRandom`)
- ❌ (`src/os/tempfile.go`, `CreateTemp`)
- ❌ (`src/os/tempfile.go`, `prefixAndSuffix`)
- ❌ (`src/os/tempfile.go`, `MkdirTemp`)
- ❌ (`src/os/tempfile.go`, `joinPath`)
- ❌ (`src/os/read_test.go`, `checkNamedSize`)
- ❌ (`src/os/read_test.go`, `TestReadFile`)
- ❌ (`src/os/read_test.go`, `TestWriteFile`)
- ❌ (`src/os/read_test.go`, `TestReadOnlyWriteFile`)
- ❌ (`src/os/read_test.go`, `TestReadDir`)
- ❌ (`src/os/dir.go`, `ReadDir`)
- ❌ (`src/os/tempfile_test.go`, `TestCreateTemp`)
- ❌ (`src/os/tempfile_test.go`, `TestCreateTempPattern`)
- ❌ (`src/os/tempfile_test.go`, `TestCreateTempBadPattern`)
- ❌ (`src/os/tempfile_test.go`, `TestMkdirTemp`)
- ❌ (`src/os/tempfile_test.go`, `TestMkdirTempBadDir`)
- ❌ (`src/os/tempfile_test.go`, `TestMkdirTempBadPattern`)
- ❌ (`src/os/file.go`, `ReadFile`)
- ❌ (`src/os/file.go`, `WriteFile`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveAllButReadOnlyAndPathError`)
- ❌ (`src/cmd/go/internal/imports/scan_test.go`, `TestScanDir`)
- ❌ (`src/index/suffixarray/gen.go`, `main`)
- ❌ (`src/cmd/go/internal/fsys/fsys.go`, `Init`)
- ❌ (`src/cmd/nm/nm_test.go`, `testGoExec`)
- ❌ (`src/cmd/nm/nm_test.go`, `testGoLib`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestAtomicLoadStore64`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestTracebackAll`)
- ❌ (`src/syscall/syscall_windows_test.go`, `TestWin32finddata`)
- ❌ (`src/cmd/go/internal/vcs/vcs_test.go`, `TestFromDir`)
- ❌ (`src/compress/flate/huffman_bit_writer_test.go`, `testBlockHuff`)
- ❌ (`src/compress/flate/huffman_bit_writer_test.go`, `testBlock`)
- ❌ (`src/compress/flate/huffman_bit_writer_test.go`, `testWriterEOF`)
- ❌ (`src/crypto/x509/root_unix_test.go`, `TestLoadSystemCertsLoadColonSeparatedDirs`)
- ❌ (`src/cmd/go/internal/work/gccgo.go`, `link`)
- ❌ (`src/crypto/tls/tls.go`, `LoadX509KeyPair`)
- ❌ (`src/runtime/race/testdata/io_test.go`, `TestNoRaceIOFile`)
- ❌ (`src/cmd/cover/cover_test.go`, `TestMain`)
- ❌ (`src/cmd/cover/cover_test.go`, `TestCover`)
- ❌ (`src/cmd/cover/cover_test.go`, `TestDirectives`)
- ❌ (`src/net/http/filetransport_test.go`, `TestFileTransport`)
- ❌ (`src/cmd/go/internal/envcmd/env.go`, `updateEnvFile`)
- ❌ (`src/crypto/x509/root_unix.go`, `loadSystemRoots`)
- ❌ (`src/log/syslog/syslog_test.go`, `startServer`)
- ❌ (`src/go/parser/interface.go`, `readSource`)
- ❌ (`src/path/filepath/path_test.go`, `testWalk`)
- ❌ (`src/path/filepath/path_test.go`, `TestWalkSkipDirOnFile`)
- ❌ (`src/path/filepath/path_test.go`, `TestWalkFileError`)
- ❌ (`src/path/filepath/path_test.go`, `TestEvalSymlinks`)
- ❌ (`src/path/filepath/path_test.go`, `TestIssue13582`)
- ❌ (`src/path/filepath/path_test.go`, `TestAbs`)
- ❌ (`src/path/filepath/path_test.go`, `TestAbsEmptyString`)
- ❌ (`src/path/filepath/path_test.go`, `testWalkSymlink`)
- ❌ (`src/path/filepath/path_test.go`, `TestIssue29372`)
- ❌ (`src/path/filepath/path_test.go`, `TestEvalSymlinksAboveRoot`)
- ❌ (`src/path/filepath/path_test.go`, `TestEvalSymlinksAboveRootChdir`)
- ❌ (`src/net/mockserver_test.go`, `testUnixAddr`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `toolVerify`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `pluginPath`)
- ❌ (`src/archive/tar/tar_test.go`, `TestFileInfoHeaderSymlink`)
- ❌ (`src/os/os_test.go`, `newFile`)
- ❌ (`src/os/os_test.go`, `TestReaddirNValues`)
- ❌ (`src/os/os_test.go`, `TestReaddirStatFailures`)
- ❌ (`src/os/os_test.go`, `TestReaddirOfFile`)
- ❌ (`src/os/os_test.go`, `TestRenameOverwriteDest`)
- ❌ (`src/os/os_test.go`, `testChtimes`)
- ❌ (`src/os/os_test.go`, `TestChdirAndGetwd`)
- ❌ (`src/os/os_test.go`, `TestProgWideChdir`)
- ❌ (`src/os/os_test.go`, `TestSeek`)
- ❌ (`src/os/os_test.go`, `TestWriteAt`)
- ❌ (`src/os/os_test.go`, `writeFile`)
- ❌ (`src/os/os_test.go`, `TestStatDirWithTrailingSlash`)
- ❌ (`src/os/os_test.go`, `TestStatDirModeExec`)
- ❌ (`src/os/os_test.go`, `TestStatRelativeSymlink`)
- ❌ (`src/os/os_test.go`, `TestLongPath`)
- ❌ (`src/os/os_test.go`, `TestRemoveAllRace`)
- ❌ (`src/runtime/crash_unix_test.go`, `TestCrashDumpsAllThreads`)
- ❌ (`src/runtime/testdata/testprog/memprof.go`, `MemProf`)
- ❌ (`src/go/internal/gccgoimporter/importer_test.go`, `TestObjImporter`)
- ❌ (`src/runtime/runtime-lldb_test.go`, `TestLldbPython`)
- ❌ (`src/internal/trace/gc_test.go`, `TestMMUTrace`)
- ❌ (`src/compress/bzip2/bzip2_test.go`, `mustLoadFile`)
- ❌ (`src/cmd/fix/typecheck.go`, `typecheck`)
- ❌ (`src/cmd/cover/cover.go`, `annotate`)
- ❌ (`src/os/os_windows_test.go`, `TestSameWindowsFile`)
- ❌ (`src/os/os_windows_test.go`, `testDirLinks`)
- ❌ (`src/os/os_windows_test.go`, `TestNetworkSymbolicLink`)
- ❌ (`src/os/os_windows_test.go`, `TestOpenVolumeName`)
- ❌ (`src/os/os_windows_test.go`, `TestDeleteReadOnly`)
- ❌ (`src/os/os_windows_test.go`, `TestCmdArgs`)
- ❌ (`src/os/os_windows_test.go`, `TestSymlinkCreation`)
- ❌ (`src/net/http/transport_test.go`, `TestTransportRequestWriteRoundTrip`)
- ❌ (`src/image/color/palette/gen.go`, `main`)
- ❌ (`src/html/template/template.go`, `readFileOS`)
- ❌ (`src/runtime/testdata/testprogcgo/pprof.go`, `CgoPprof`)
- ❌ (`src/net/net_windows_test.go`, `runCmd`)
- ❌ (`src/runtime/trace/trace_test.go`, `saveTrace`)
- ❌ (`src/math/big/link_test.go`, `TestLinkerGC`)
- ❌ (`src/go/parser/performance_test.go`, `readFile`)
- ❌ (`src/runtime/memmove_linux_amd64_test.go`, `TestMemmoveOverflow`)
- ❌ (`src/syscall/syscall_unix_test.go`, `TestFcntlFlock`)
- ❌ (`src/syscall/syscall_unix_test.go`, `TestPassFD`)
- ❌ (`src/syscall/syscall_unix_test.go`, `passFDChild`)
- ❌ (`src/os/exec/lp_windows_test.go`, `TestCommand`)
- ❌ (`src/cmd/cover/html.go`, `htmlOutput`)
- ❌ (`src/runtime/testdata/testprogcgo/threadpprof.go`, `pprofThread`)
- ❌ (`src/cmd/go/internal/modfetch/zip_sum_test/zip_sum_test.go`, `TestZipSums`)
- ❌ (`src/go/doc/doc_test.go`, `test`)
- ❌ (`src/cmd/go/internal/modfetch/codehost/shell.go`, `main`)
- ❌ (`src/strconv/makeisprint.go`, `main`)
- ❌ (`src/compress/lzw/reader_test.go`, `BenchmarkDecoder`)
- ❌ (`src/archive/tar/reader_test.go`, `TestReadTruncation`)
- ❌ (`src/image/internal/imageutil/gen.go`, `main`)
- ❌ (`src/runtime/syscall_windows_test.go`, `TestStdcallAndCDeclCallbacks`)
- ❌ (`src/runtime/syscall_windows_test.go`, `TestReturnAfterStackGrowInCallback`)
- ❌ (`src/runtime/syscall_windows_test.go`, `TestFloatArgs`)
- ❌ (`src/runtime/syscall_windows_test.go`, `TestFloatReturn`)
- ❌ (`src/runtime/syscall_windows_test.go`, `TestDLLPreloadMitigation`)
- ❌ (`src/runtime/syscall_windows_test.go`, `TestBigStackCallbackSyscall`)
- ❌ (`src/runtime/syscall_windows_test.go`, `BenchmarkRunningGoProgram`)
- ❌ (`src/cmd/gofmt/gofmt_test.go`, `runTest`)
- ❌ (`src/cmd/gofmt/gofmt_test.go`, `TestCRLF`)
- ❌ (`src/cmd/gofmt/gofmt_test.go`, `TestBackupFile`)
- ❌ (`src/net/http/fs_test.go`, `TestServeFile`)
- ❌ (`src/net/http/fs_test.go`, `TestFileServerImplicitLeadingSlash`)
- ❌ (`src/net/http/fs_test.go`, `TestLinuxSendfile`)
- ❌ (`src/cmd/go/internal/modfetch/cache_test.go`, `TestWriteDiskCache`)
- ❌ (`src/cmd/go/internal/lockedfile/internal/filelock/filelock_test.go`, `mustTempFile`)
- ❌ (`src/runtime/testdata/testprog/vdso.go`, `signalInVDSO`)
- ❌ (`src/syscall/dirent_test.go`, `TestDirent`)
- ❌ (`src/syscall/dirent_test.go`, `TestDirentRepeat`)
- ❌ (`src/runtime/debug_test.go`, `skipUnderDebugger`)
- ❌ (`src/runtime/testdata/testprog/timeprof.go`, `TimeProf`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `findModulePath`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `findImportComment`)
- ❌ (`src/image/jpeg/reader_test.go`, `TestDecodeEOF`)
- ❌ (`src/image/jpeg/reader_test.go`, `TestTruncatedSOSDataDoesntPanic`)
- ❌ (`src/image/jpeg/reader_test.go`, `benchmarkDecode`)
- ❌ (`src/cmd/go/testdata/addmod.go`, `main`)
- ❌ (`src/cmd/go/internal/modfetch/fetch.go`, `download`)
- ❌ (`src/cmd/go/internal/modfetch/fetch.go`, `downloadZip`)
- ❌ (`src/os/exec/lp_unix_test.go`, `TestLookPathUnixEmptyPath`)
- ❌ (`src/archive/tar/writer_test.go`, `TestWriter`)
- ❌ (`src/go/format/benchmark_test.go`, `BenchmarkFormat`)
- ❌ (`src/internal/cpu/cpu_s390x_test.go`, `getFeatureList`)
- ❌ (`src/go/format/format_test.go`, `TestNode`)
- ❌ (`src/go/format/format_test.go`, `TestSource`)
- ❌ (`src/runtime/wincallback.go`, `genasm386Amd64`)
- ❌ (`src/runtime/wincallback.go`, `genasmArm`)
- ❌ (`src/runtime/wincallback.go`, `gengo`)
- ❌ (`src/cmd/go/internal/generate/generate.go`, `generate`)
- ❌ (`src/cmd/go/go_windows_test.go`, `TestAbsolutePath`)
- ❌ (`src/cmd/go/internal/bug/bug.go`, `printOSDetails`)
- ❌ (`src/cmd/go/internal/bug/bug.go`, `printGlibcVersion`)
- ❌ (`src/text/template/link_test.go`, `TestLinkerGC`)
- ❌ (`src/runtime/signal_windows_test.go`, `TestVectoredHandlerDontCrashOnLibrary`)
- ❌ (`src/runtime/signal_windows_test.go`, `TestLibraryCtrlHandler`)
- ❌ (`src/runtime/crash_test.go`, `buildTestProg`)
- ❌ (`src/compress/flate/reader_test.go`, `doBench`)
- ❌ (`src/runtime/mkduff.go`, `gen`)
- ❌ (`src/cmd/vet/vet_test.go`, `wantedErrors`)
- ❌ (`src/syscall/getdirentries_test.go`, `testGetdirentries`)
- ❌ (`src/image/gif/reader_test.go`, `BenchmarkDecode`)
- ❌ (`src/cmd/go/internal/modcmd/vendor.go`, `runVendor`)
- ❌ (`src/cmd/go/internal/modload/vendor.go`, `readVendorList`)
- ❌ (`src/runtime/mkfastlog2table.go`, `main`)
- ❌ (`src/compress/flate/deflate_test.go`, `TestDeflateInflateString`)
- ❌ (`src/testing/testing.go`, `TempDir`)
- ❌ (`src/runtime/testdata/testprog/syscalls_linux.go`, `tidExists`)
- ❌ (`src/net/unixsock_test.go`, `TestUnixUnlink`)
- ❌ (`src/cmd/go/internal/modload/query_test.go`, `testMain`)
- ❌ (`src/cmd/fix/main.go`, `processFile`)
- ❌ (`src/internal/obscuretestdata/obscuretestdata.go`, `DecodeToTempFile`)
- ❌ (`src/crypto/x509/name_constraints_test.go`, `writePEMsToTempFile`)
- ❌ (`src/cmd/go/internal/test/test.go`, `builderTest`)
- ❌ (`src/cmd/go/internal/test/test.go`, `saveOutput`)
- ❌ (`src/go/types/hilbert_test.go`, `TestHilbert`)
- ❌ (`src/internal/poll/read_test.go`, `TestRead`)
- ❌ (`src/cmd/go/go_test.go`, `TestMain`)
- ❌ (`src/cmd/go/go_test.go`, `makeTempdir`)
- ❌ (`src/cmd/go/go_test.go`, `tempFile`)
- ❌ (`src/cmd/go/go_test.go`, `TestNewReleaseRebuildsStalePackagesInGOPATH`)
- ❌ (`src/cmd/go/go_test.go`, `TestTwoPkgConfigs`)
- ❌ (`src/html/template/examplefiles_test.go`, `createTestDir`)
- ❌ (`src/go/internal/srcimporter/srcimporter.go`, `cgo`)
- ❌ (`src/cmd/go/internal/cache/default.go`, `initDefaultCache`)
- ❌ (`src/cmd/go/internal/work/build_test.go`, `TestSharedLibName`)
- ❌ (`src/cmd/go/internal/work/build_test.go`, `TestRespectSetgidDir`)
- ❌ (`src/os/error_test.go`, `TestErrIsExist`)
- ❌ (`src/os/error_test.go`, `TestErrIsNotExist`)
- ❌ (`src/os/error_test.go`, `TestErrPathNUL`)
- ❌ (`src/index/suffixarray/suffixarray_test.go`, `makeText`)
- ❌ (`src/os/user/lookup_plan9.go`, `current`)
- ❌ (`src/cmd/go/internal/lockedfile/lockedfile_test.go`, `TestCanLockExistingFile`)
- ❌ (`src/cmd/go/internal/lockedfile/lockedfile_test.go`, `TestSpuriousEDEADLK`)
- ❌ (`src/cmd/go/internal/web/file_test.go`, `TestGetFileURL`)
- ❌ (`src/net/http/transfer_test.go`, `TestTransferWriterWriteBodyReaderTypes`)
- ❌ (`src/go/importer/importer_test.go`, `TestForCompiler`)
- ❌ (`src/go/build/build_test.go`, `TestImportDirNotExist`)
- ❌ (`src/go/build/build_test.go`, `TestImportPackageOutsideModule`)
- ❌ (`src/go/build/build_test.go`, `TestMissingImportErrorRepetition`)
- ❌ (`src/os/stat_test.go`, `TestDirAndSymlinkStats`)
- ❌ (`src/os/stat_test.go`, `TestFileAndSymlinkStats`)
- ❌ (`src/os/stat_test.go`, `TestSymlinkWithTrailingSlash`)
- ❌ (`src/path/filepath/path_windows_test.go`, `testWinSplitListTestIsValid`)
- ❌ (`src/path/filepath/path_windows_test.go`, `TestWindowsEvalSymlinks`)
- ❌ (`src/path/filepath/path_windows_test.go`, `TestEvalSymlinksCanonicalNames`)
- ❌ (`src/path/filepath/path_windows_test.go`, `TestToNorm`)
- ❌ (`src/path/filepath/path_windows_test.go`, `TestNTNamespaceSymlink`)
- ❌ (`src/mime/multipart/formdata.go`, `readForm`)
- ❌ (`src/crypto/md5/gen.go`, `main`)
- ❌ (`src/compress/zlib/writer_test.go`, `testFileLevelDictReset`)
- ❌ (`src/cmd/go/internal/modcmd/verify.go`, `verifyMod`)
- ❌ (`src/runtime/debug/heapdump_test.go`, `TestWriteHeapDumpNonempty`)
- ❌ (`src/runtime/debug/heapdump_test.go`, `TestWriteHeapDumpFinalizers`)
- ❌ (`src/path/filepath/example_unix_walk_test.go`, `prepareTestDirTree`)
- ❌ (`src/runtime/runtime-gdb_test.go`, `testGdbPython`)
- ❌ (`src/runtime/runtime-gdb_test.go`, `TestGdbBacktrace`)
- ❌ (`src/runtime/runtime-gdb_test.go`, `TestGdbAutotmpTypes`)
- ❌ (`src/runtime/runtime-gdb_test.go`, `TestGdbConst`)
- ❌ (`src/runtime/runtime-gdb_test.go`, `TestGdbPanic`)
- ❌ (`src/runtime/runtime-gdb_test.go`, `TestGdbInfCallstack`)
- ❌ (`src/os/os_unix_test.go`, `TestReaddirRemoveRace`)
- ❌ (`src/path/filepath/match_test.go`, `TestGlobSymlink`)
- ❌ (`src/path/filepath/match_test.go`, `TestWindowsGlob`)
- ❌ (`src/debug/gosym/pclntab_test.go`, `dotest`)
- ❌ (`src/debug/gosym/pclntab_test.go`, `Test115PclnParsing`)
- ❌ (`src/debug/dwarf/dwarf5ranges_test.go`, `TestDwarf5Ranges`)
- ❌ (`src/go/printer/printer_test.go`, `runcheck`)
- ❌ (`src/go/printer/printer_test.go`, `TestBaseIndent`)
- ❌ (`src/go/printer/printer_test.go`, `TestWriteErrors`)
- ❌ (`src/cmd/go/help_test.go`, `TestDocsUpToDate`)
- ❌ (`src/os/fifo_test.go`, `TestFifoEOF`)
- ❌ (`src/os/pipe_test.go`, `testClosedPipeRace`)
- ❌ (`src/cmd/go/internal/modfetch/codehost/git_test.go`, `testMain`)
- ❌ (`src/crypto/tls/handshake_test.go`, `tempFile`)
- ❌ (`src/go/internal/gcimporter/gcimporter_test.go`, `mktmpdir`)
- ❌ (`src/go/internal/gcimporter/gcimporter_test.go`, `TestVersionHandling`)
- ❌ (`src/cmd/go/internal/modfetch/coderepo.go`, `Zip`)
- ❌ (`src/go/printer/performance_test.go`, `initialize`)
- ❌ (`src/archive/zip/writer_test.go`, `TestWriterTime`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `Do`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `build`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `installShlibname`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `gccSupportsFlag`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `cgo`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `swigDoIntSize`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `passLongArgsInResponseFiles`)
- ❌ (`src/cmd/go/internal/cache/cache.go`, `GetBytes`)
- ❌ (`src/cmd/go/internal/cache/cache.go`, `putIndexEntry`)
- ❌ (`src/cmd/objdump/objdump_test.go`, `TestGoobjFileNumber`)
- ❌ (`src/cmd/pack/pack_test.go`, `TestExtract`)
- ❌ (`src/cmd/pack/pack_test.go`, `TestHello`)
- ❌ (`src/cmd/pack/pack_test.go`, `TestLargeDefs`)
- ❌ (`src/cmd/pack/pack_test.go`, `TestIssue21703`)
- ❌ (`src/syscall/exec_linux_test.go`, `TestUnshare`)
- ❌ (`src/syscall/exec_linux_test.go`, `TestUnshareMountNameSpace`)
- ❌ (`src/syscall/exec_linux_test.go`, `TestUnshareMountNameSpaceChroot`)
- ❌ (`src/syscall/exec_linux_test.go`, `testAmbientCaps`)
- ❌ (`src/math/bits/make_tables.go`, `main`)
- ❌ (`src/hash/crc32/gen_const_ppc64le.go`, `main`)
- ❌ (`src/debug/pe/file_test.go`, `testDWARF`)
- ❌ (`src/debug/pe/file_test.go`, `TestBSSHasZeros`)
- ❌ (`src/debug/pe/file_test.go`, `TestBuildingWindowsGUI`)
- ❌ (`src/debug/pe/file_test.go`, `TestImportedSymbolsNoPanicMissingOptionalHeader`)
- ❌ (`src/compress/lzw/writer_test.go`, `BenchmarkEncoder`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveAll`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveAllLarge`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveAllLongPath`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveAllDot`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveAllDotDot`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveReadOnlyDir`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveAllButReadOnlyAndPathError`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveUnreadableDir`)
- ❌ (`src/os/removeall_test.go`, `TestRemoveAllWithMoreErrorThanReqSize`)
- ❌ (`src/crypto/x509/root_plan9.go`, `loadSystemRoots`)
- ❌ (`src/cmd/go/internal/cache/hash_test.go`, `TestHashFile`)
- ❌ (`src/cmd/gofmt/gofmt.go`, `processFile`)
- ❌ (`src/cmd/gofmt/gofmt.go`, `backupFile`)
- ❌ (`src/runtime/race/output_test.go`, `TestOutput`)
- ❌ (`src/net/dnsclient_unix_test.go`, `newResolvConfTest`)
- ❌ (`src/embed/internal/embedtest/embedx_test.go`, `TestXGlobal`)
- ❌ (`src/net/http/request_test.go`, `benchmarkFileAndServer`)
- ❌ (`src/cmd/go/internal/modfetch/codehost/codehost.go`, `WorkDir`)
- ❌ (`src/os/signal/signal_windows_test.go`, `TestCtrlBreak`)
- ❌ (`src/text/template/helper.go`, `readFileOS`)
- ❌ (`src/os/path_test.go`, `TestMkdirAllWithSymlink`)
- ❌ (`src/math/bits/make_examples.go`, `main`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `goModPath`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `load`)
- ❌ (`src/cmd/go/internal/modfetch/coderepo_test.go`, `testMain`)
- ❌ (`src/cmd/go/internal/modfetch/coderepo_test.go`, `TestCodeRepo`)
- ❌ (`src/cmd/go/internal/modfetch/coderepo_test.go`, `TestCodeRepoVersions`)
- ❌ (`src/cmd/go/internal/modfetch/coderepo_test.go`, `TestLatest`)
- ❌ (`src/os/signal/signal_test.go`, `TestDetectNohup`)
- ❌ (`src/cmd/go/internal/cfg/cfg.go`, `initEnvCache`)
- ❌ (`src/cmd/addr2line/addr2line_test.go`, `testAddr2Line`)
- ❌ (`src/cmd/addr2line/addr2line_test.go`, `TestAddr2Line`)
- ❌ (`src/cmd/go/internal/modfetch/codehost/vcs.go`, `ReadZip`)
- ❌ (`src/crypto/tls/link_test.go`, `TestLinkerGC`)
- ❌ (`src/text/template/examplefiles_test.go`, `createTestDir`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `gccgoBuildIDFile`)
- ❌ (`src/syscall/syscall_linux_test.go`, `TestSyscallNoError`)
- ❌ (`src/syscall/syscall_linux_test.go`, `compareStatus`)
- ❌ (`src/runtime/pprof/proto_test.go`, `testPCs`)
- ❌ (`src/os/exec/exec_test.go`, `TestExtraFiles`)
- ❌ (`src/os/path_windows_test.go`, `TestMkdirAllExtendedLength`)
- ❌ (`src/os/timeout_test.go`, `TestNonpollableDeadline`)
- ❌ (`src/net/error_test.go`, `TestFileError`)
- ❌ (`src/image/png/reader_test.go`, `benchmarkDecode`)
- ✅ (`src/cmd/go/internal/fsys/fsys_test.go`, `initOverlay`)
- ❌ (`src/time/genzabbrs.go`, `main`)
- ❌ (`src/cmd/go/testdata/savedir.go`, `main`)
- ❌ (`src/cmd/go/internal/cache/cache_test.go`, `TestBasic`)
- ❌ (`src/cmd/go/internal/cache/cache_test.go`, `TestGrowth`)
- ❌ (`src/cmd/go/internal/cache/cache_test.go`, `TestVerifyPanic`)
- ❌ (`src/cmd/go/internal/cache/cache_test.go`, `TestCacheTrim`)
- ❌ (`src/archive/zip/reader_test.go`, `readTestFile`)
- ❌ (`src/archive/zip/reader_test.go`, `messWith`)
- ❌ (`src/cmd/go/internal/imports/scan_test.go`, `TestScanDir`)
- ❌ (`src/os/exec/exec_test.go`, `TestPipeLookPathLeak`)
- ❌ (`src/cmd/go/internal/test/test.go`, `hashOpen`)
- ❌ (`src/cmd/go/internal/modcmd/vendor.go`, `matchMetadata`)
- ❌ (`src/cmd/go/internal/modcmd/vendor.go`, `matchPotentialSourceFile`)
- ❌ (`src/cmd/go/internal/modcmd/vendor.go`, `copyDir`)
- ❌ (`src/crypto/x509/root_unix.go`, `readUniqueDirectoryEntries`)
- ❌ (`src/crypto/x509/root_unix.go`, `isSameDirSymlink`)
- ❌ (`src/cmd/go/internal/clean/clean.go`, `clean`)
- ❌ (`src/go/types/check_test.go`, `testDir`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `hasGoFiles`)
- ❌ (`src/go/internal/gcimporter/gcimporter_test.go`, `TestVersionHandling`)
- ❌ (`src/go/parser/interface.go`, `ParseDir`)
- ❌ (`src/go/types/stdlib_test.go`, `testTestDir`)
- ❌ (`src/go/types/stdlib_test.go`, `walk`)
- ❌ (`src/go/internal/srcimporter/srcimporter_test.go`, `walkDir`)
- ❌ (`src/go/build/deps_test.go`, `findImports`)
- ❌ (`src/testing/testing_test.go`, `testTempDir`)
- ❌ (`src/cmd/go/internal/modfetch/cache.go`, `rewriteVersionList`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `CreateModFile`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `findModulePath`)
- ❌ (`src/cmd/go/proxy_test.go`, `readModList`)
- ❌ (`src/go/parser/error_test.go`, `TestErrors`)
- ❌ (`src/os/tempfile.go`, `prefixAndSuffix`)
- ❌ (`src/os/file_plan9.go`, `rename`)
- ❌ (`src/io/ioutil/tempfile_test.go`, `TestTempFile_BadPattern`)
- ❌ (`src/io/ioutil/tempfile_test.go`, `TestTempDir_BadPattern`)
- ❌ (`src/io/ioutil/tempfile.go`, `TempFile`)
- ❌ (`src/io/ioutil/tempfile.go`, `TempDir`)

### 📊 Proposal #42027

#### File Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ❌ `src/cmd/fix`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/version`
- ❌ `src/cmd/go/testdata`
- ❌ `src/cmd/gofmt`
- ❌ `src/cmd/internal/moddeps`
- ❌ `src/compress/gzip`
- ❌ `src/go/build`
- ❌ `src/go/doc`
- ❌ `src/index/suffixarray`
- ✅ `src/io/fs`
- ✅ `src/path/filepath`
- ❌ `test`

#### File Embeddings - File Level
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/fix/main.go`
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/modfetch/fetch.go`
- ❌ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/go/testdata/addmod.go`
- ❌ `src/cmd/go/testdata/savedir.go`
- ❌ `src/cmd/gofmt/long_test.go`
- ❌ `src/cmd/internal/moddeps/moddeps_test.go`
- ❌ `src/compress/gzip/issue14937_test.go`
- ❌ `src/go/build/deps_test.go`
- ❌ `src/go/doc/headscan.go`
- ❌ `src/index/suffixarray/suffixarray_test.go`
- ❌ `src/io/fs/walk.go`
- ❌ `src/io/fs/walk_test.go`
- ❌ `src/path/filepath/path.go`
- ❌ `src/path/filepath/path_test.go`
- ❌ `test/winbatch.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ❌ `src/cmd/fix`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/version`
- ❌ `src/cmd/go/testdata`
- ❌ `src/cmd/gofmt`
- ❌ `src/cmd/internal/moddeps`
- ❌ `src/compress/gzip`
- ❌ `src/go/build`
- ❌ `src/go/doc`
- ❌ `src/index/suffixarray`
- ✅ `src/io/fs`
- ✅ `src/path/filepath`
- ❌ `test`

#### Function Embeddings - File Level
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/fix/main.go`
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/modfetch/fetch.go`
- ❌ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/go/testdata/addmod.go`
- ❌ `src/cmd/go/testdata/savedir.go`
- ❌ `src/cmd/gofmt/long_test.go`
- ❌ `src/cmd/internal/moddeps/moddeps_test.go`
- ❌ `src/compress/gzip/issue14937_test.go`
- ❌ `src/go/build/deps_test.go`
- ❌ `src/go/doc/headscan.go`
- ❌ `src/index/suffixarray/suffixarray_test.go`
- ✅ `src/io/fs/walk.go`
- ❌ `src/io/fs/walk_test.go`
- ✅ `src/path/filepath/path.go`
- ✅ `src/path/filepath/path_test.go`
- ❌ `test/winbatch.go`

#### Function Embeddings - Function Level
- ✅ (`src/path/filepath/path.go`, `walkDir`)
- ✅ (`src/path/filepath/path.go`, `walk`)
- ❌ (`src/path/filepath/path.go`, `WalkDir`)
- ❌ (`src/path/filepath/path.go`, `Walk`)
- ❌ (`src/path/filepath/path.go`, `readDirNames`)
- ❌ (`src/io/fs/walk_test.go`, `walkTree`)
- ❌ (`src/io/fs/walk_test.go`, `makeTree`)
- ❌ (`src/io/fs/walk_test.go`, `mark`)
- ❌ (`src/io/fs/walk_test.go`, `TestWalkDir`)
- ✅ (`src/io/fs/walk.go`, `walkDir`)
- ❌ (`src/io/fs/walk.go`, `WalkDir`)
- ❌ (`src/path/filepath/path_test.go`, `TestWalk`)
- ✅ (`src/path/filepath/path.go`, `walkDir`)
- ❌ (`src/path/filepath/path.go`, `WalkDir`)
- ❌ (`src/path/filepath/path.go`, `Walk`)
- ❌ (`src/path/filepath/path_test.go`, `mark`)
- ❌ (`src/path/filepath/path_test.go`, `TestWalk`)
- ❌ (`src/path/filepath/path_test.go`, `TestWalkDir`)
- ❌ (`src/path/filepath/path_test.go`, `testWalk`)
- ❌ (`src/path/filepath/path_test.go`, `touch`)
- ✅ (`src/path/filepath/path_test.go`, `TestWalkSkipDirOnFile`)
- ❌ (`src/go/doc/headscan.go`, `main`)
- ❌ (`src/cmd/dist/test.go`, `makeGOROOTUnwritable`)
- ❌ (`src/cmd/go/internal/version/version.go`, `scanDir`)
- ❌ (`src/compress/gzip/issue14937_test.go`, `TestGZIPFilesHaveZeroMTimes`)
- ❌ (`src/cmd/internal/moddeps/moddeps_test.go`, `findGorootModules`)
- ❌ (`src/cmd/gofmt/long_test.go`, `genFilenames`)
- ❌ (`src/cmd/go/go_test.go`, `removeAll`)
- ❌ (`src/cmd/go/go_test.go`, `TestNewReleaseRebuildsStalePackagesInGOPATH`)
- ❌ (`src/go/build/deps_test.go`, `listStdPkgs`)
- ❌ (`src/cmd/go/testdata/savedir.go`, `main`)
- ❌ (`test/winbatch.go`, `main`)
- ❌ (`src/cmd/fix/main.go`, `walkDir`)
- ❌ (`src/cmd/go/internal/modfetch/fetch.go`, `makeDirsReadOnly`)
- ❌ (`src/cmd/go/internal/modfetch/fetch.go`, `RemoveAll`)
- ❌ (`src/cmd/go/testdata/addmod.go`, `main`)
- ❌ (`src/index/suffixarray/suffixarray_test.go`, `makeText`)
- ✅ (`src/path/filepath/path.go`, `walk`)
- ❌ (`src/path/filepath/path.go`, `Walk`)
- ❌ (`src/path/filepath/path.go`, `readDirNames`)
- ❌ (`src/path/filepath/path.go`, `Base`)
- ❌ (`src/path/filepath/path_test.go`, `mark`)
- ❌ (`src/path/filepath/path_test.go`, `TestWalk`)
- ❌ (`src/path/filepath/path_test.go`, `touch`)
- ✅ (`src/path/filepath/path_test.go`, `TestWalkSkipDirOnFile`)
- ❌ (`src/path/filepath/path_test.go`, `TestWalkFileError`)
- ✅ (`src/path/filepath/path.go`, `walkDir`)
- ❌ (`src/path/filepath/path.go`, `WalkDir`)
- ❌ (`src/path/filepath/path.go`, `Walk`)
- ❌ (`src/path/filepath/path_test.go`, `mark`)
- ❌ (`src/path/filepath/path_test.go`, `TestWalk`)
- ❌ (`src/path/filepath/path_test.go`, `TestWalkDir`)
- ❌ (`src/path/filepath/path_test.go`, `testWalk`)
- ❌ (`src/path/filepath/path_test.go`, `touch`)
- ✅ (`src/path/filepath/path_test.go`, `TestWalkSkipDirOnFile`)

### 📊 Proposal #42088

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/run`
- ❌ `src/cmd/go/internal/work`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/run/run.go`
- ❌ `src/cmd/go/internal/work/build.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/run`
- ✅ `src/cmd/go/internal/work`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/run/run.go`
- ❌ `src/cmd/go/internal/work/build.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/run/run.go`, `runRun`)
- ❌ (`src/cmd/go/internal/run/run.go`, `shouldUseOutsideModuleMode`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `PackagesAndErrors`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `mainPackagesOnly`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `PackagesAndErrorsOutsideModule`)
- ❌ (`src/cmd/go/internal/work/build.go`, `installOutsideModule`)
- ❌ (`src/cmd/go/internal/work/build.go`, `FindExecCmd`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `mainPackagesOnly`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `Error`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `ImportPath`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `GoFilesPackage`)
- ❌ (`src/cmd/go/internal/run/run.go`, `runRun`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `mainPackagesOnly`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `AllFiles`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `copyBuild`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `PackagesAndErrors`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `mainPackagesOnly`)

### 📊 Proposal #42098

#### File Embeddings - Directory Level
- ✅ `src/syscall`

#### File Embeddings - File Level
- ❌ `src/syscall/exec_windows.go`

#### Function Embeddings - Directory Level
- ✅ `src/syscall`

#### Function Embeddings - File Level
- ❌ `src/syscall/exec_windows.go`

#### Function Embeddings - Function Level
- ❌ (`src/syscall/exec_windows.go`, `StartProcess`)

### 📊 Proposal #42100

#### File Embeddings - Directory Level
- ❌ `misc/ios`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/link/internal/ld`

#### File Embeddings - File Level
- ❌ `misc/ios/go_ios_exec.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/go/internal/work/init.go`
- ❌ `src/cmd/link/internal/ld/config.go`

#### Function Embeddings - Directory Level
- ❌ `misc/ios`
- ✅ `src/cmd/dist`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/link/internal/ld`

#### Function Embeddings - File Level
- ❌ `misc/ios/go_ios_exec.go`
- ❌ `src/cmd/dist/build.go`
- ✅ `src/cmd/dist/test.go`
- ❌ `src/cmd/go/internal/work/init.go`
- ❌ `src/cmd/link/internal/ld/config.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/dist/build.go`, `wrapperPathFor`)
- ❌ (`misc/ios/go_ios_exec.go`, `main`)
- ❌ (`misc/ios/go_ios_exec.go`, `runMain`)
- ❌ (`misc/ios/go_ios_exec.go`, `runOnSimulator`)
- ❌ (`misc/ios/go_ios_exec.go`, `assembleApp`)
- ❌ (`misc/ios/go_ios_exec.go`, `installSimulator`)
- ❌ (`misc/ios/go_ios_exec.go`, `runSimulator`)
- ❌ (`misc/ios/go_ios_exec.go`, `infoPlist`)
- ❌ (`misc/ios/go_ios_exec.go`, `entitlementsPlist`)
- ❌ (`src/cmd/link/internal/ld/config.go`, `Set`)
- ❌ (`src/cmd/go/internal/work/init.go`, `buildModeInit`)
- ❌ (`src/cmd/dist/test.go`, `registerTests`)

### 📊 Proposal #42102

#### File Embeddings - Directory Level
- ✅ `src/time`

#### File Embeddings - File Level
- ❌ `src/time/format.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`
- ✅ `src/time/zoneinfo.go`
- ❌ `src/time/zoneinfo_read.go`
- ❌ `src/time/zoneinfo_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/time`

#### Function Embeddings - File Level
- ❌ `src/time/format.go`
- ✅ `src/time/time.go`
- ✅ `src/time/time_test.go`
- ✅ `src/time/zoneinfo.go`
- ❌ `src/time/zoneinfo_read.go`
- ❌ `src/time/zoneinfo_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/time/zoneinfo_read.go`, `LoadLocationFromTZData`)
- ❌ (`src/time/zoneinfo_test.go`, `TestTzset`)
- ❌ (`src/time/format.go`, `parse`)
- ❌ (`src/time/time.go`, `locabs`)
- ❌ (`src/time/time.go`, `Zone`)
- ❌ (`src/time/time.go`, `UnmarshalBinary`)
- ❌ (`src/time/time.go`, `IsDST`)
- ❌ (`src/time/time.go`, `Date`)
- ✅ (`src/time/time_test.go`, `TestTimeIsDST`)
- ❌ (`src/time/zoneinfo.go`, `lookup`)
- ❌ (`src/time/zoneinfo.go`, `tzset`)
- ❌ (`src/time/zoneinfo.go`, `lookupName`)
- ❌ (`src/time/zoneinfo_read.go`, `LoadLocationFromTZData`)
- ❌ (`src/time/zoneinfo_test.go`, `TestTzset`)
- ❌ (`src/time/format.go`, `parse`)
- ❌ (`src/time/time.go`, `locabs`)
- ❌ (`src/time/time.go`, `Zone`)
- ❌ (`src/time/time.go`, `UnmarshalBinary`)
- ❌ (`src/time/time.go`, `IsDST`)
- ❌ (`src/time/time.go`, `Date`)
- ✅ (`src/time/time_test.go`, `TestTimeIsDST`)
- ❌ (`src/time/zoneinfo.go`, `lookup`)
- ❌ (`src/time/zoneinfo.go`, `tzset`)
- ❌ (`src/time/zoneinfo.go`, `lookupName`)

### 📊 Proposal #42322

#### File Embeddings - Directory Level
- ❌ `src/embed/internal/embedtest`
- ❌ `src/io/fs`
- ❌ `src/testing/fstest`

#### File Embeddings - File Level
- ❌ `src/embed/internal/embedtest/embed_test.go`
- ❌ `src/io/fs/readdir_test.go`
- ❌ `src/io/fs/readfile_test.go`
- ❌ `src/io/fs/sub.go`
- ❌ `src/io/fs/sub_test.go`
- ❌ `src/testing/fstest/mapfs.go`
- ❌ `src/testing/fstest/testfs.go`

#### Function Embeddings - Directory Level
- ❌ `src/embed/internal/embedtest`
- ❌ `src/io/fs`
- ❌ `src/testing/fstest`

#### Function Embeddings - File Level
- ❌ `src/embed/internal/embedtest/embed_test.go`
- ❌ `src/io/fs/readdir_test.go`
- ❌ `src/io/fs/readfile_test.go`
- ❌ `src/io/fs/sub.go`
- ❌ `src/io/fs/sub_test.go`
- ❌ `src/testing/fstest/mapfs.go`
- ❌ `src/testing/fstest/testfs.go`

#### Function Embeddings - Function Level
- ❌ (`src/io/fs/readfile_test.go`, `TestReadFile`)
- ❌ (`src/io/fs/readdir_test.go`, `TestReadDir`)
- ❌ (`src/io/fs/sub_test.go`, `TestSub`)
- ❌ (`src/testing/fstest/mapfs.go`, `Sub`)
- ❌ (`src/io/fs/sub.go`, `Sub`)
- ❌ (`src/io/fs/sub.go`, `fullName`)
- ❌ (`src/io/fs/sub.go`, `shorten`)
- ❌ (`src/io/fs/sub.go`, `fixErr`)
- ❌ (`src/io/fs/sub.go`, `Open`)
- ❌ (`src/io/fs/sub.go`, `ReadDir`)
- ❌ (`src/io/fs/sub.go`, `ReadFile`)
- ❌ (`src/io/fs/sub.go`, `Glob`)
- ❌ (`src/embed/internal/embedtest/embed_test.go`, `TestGlobal`)
- ❌ (`src/testing/fstest/testfs.go`, `TestFS`)
- ❌ (`src/testing/fstest/testfs.go`, `testFS`)

### 📊 Proposal #42387

#### File Embeddings - Directory Level
- ✅ `src/io/fs`

#### File Embeddings - File Level
- ✅ `src/io/fs/readdir.go`
- ❌ `src/io/fs/readdir_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/io/fs`

#### Function Embeddings - File Level
- ✅ `src/io/fs/readdir.go`
- ❌ `src/io/fs/readdir_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/io/fs/readdir.go`, `IsDir`)
- ❌ (`src/io/fs/readdir.go`, `Type`)
- ❌ (`src/io/fs/readdir.go`, `Info`)
- ❌ (`src/io/fs/readdir.go`, `Name`)
- ✅ (`src/io/fs/readdir.go`, `FileInfoToDirEntry`)
- ❌ (`src/io/fs/readdir_test.go`, `TestFileInfoToDirEntry`)

### 📊 Proposal #42502

#### File Embeddings - Directory Level
- ✅ `src/runtime`
- ✅ `src/runtime/pprof`
- ❌ `src/runtime/testdata/testprogcgo`

#### File Embeddings - File Level
- ❌ `src/runtime/cgocall.go`
- ❌ `src/runtime/cpuprof.go`
- ❌ `src/runtime/os3_plan9.go`
- ❌ `src/runtime/os3_solaris.go`
- ❌ `src/runtime/os_aix.go`
- ❌ `src/runtime/os_darwin.go`
- ❌ `src/runtime/os_dragonfly.go`
- ❌ `src/runtime/os_freebsd.go`
- ❌ `src/runtime/os_linux.go`
- ❌ `src/runtime/os_netbsd.go`
- ❌ `src/runtime/os_openbsd.go`
- ❌ `src/runtime/os_windows.go`
- ✅ `src/runtime/pprof/pprof.go`
- ✅ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/proto.go`
- ❌ `src/runtime/pprof/proto_test.go`
- ❌ `src/runtime/pprof/protomem.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/signal_unix.go`
- ❌ `src/runtime/testdata/testprogcgo/threadpprof.go`
- ❌ `src/runtime/testdata/testprogcgo/tracebackctxt.go`

#### Function Embeddings - Directory Level
- ✅ `src/runtime`
- ✅ `src/runtime/pprof`
- ❌ `src/runtime/testdata/testprogcgo`

#### Function Embeddings - File Level
- ❌ `src/runtime/cgocall.go`
- ✅ `src/runtime/cpuprof.go`
- ❌ `src/runtime/os3_plan9.go`
- ❌ `src/runtime/os3_solaris.go`
- ❌ `src/runtime/os_aix.go`
- ❌ `src/runtime/os_darwin.go`
- ❌ `src/runtime/os_dragonfly.go`
- ❌ `src/runtime/os_freebsd.go`
- ❌ `src/runtime/os_linux.go`
- ❌ `src/runtime/os_netbsd.go`
- ❌ `src/runtime/os_openbsd.go`
- ❌ `src/runtime/os_windows.go`
- ✅ `src/runtime/pprof/pprof.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/proto.go`
- ❌ `src/runtime/pprof/proto_test.go`
- ❌ `src/runtime/pprof/protomem.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/signal_unix.go`
- ❌ `src/runtime/testdata/testprogcgo/threadpprof.go`
- ❌ `src/runtime/testdata/testprogcgo/tracebackctxt.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/pprof/pprof.go`, `StartCPUProfile`)
- ❌ (`src/runtime/pprof/pprof.go`, `StartCPUProfile`)
- ❌ (`src/runtime/os3_solaris.go`, `setProcessCPUProfiler`)
- ❌ (`src/runtime/os3_solaris.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/os3_plan9.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/os_netbsd.go`, `setProcessCPUProfiler`)
- ❌ (`src/runtime/os_netbsd.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/os_darwin.go`, `setProcessCPUProfiler`)
- ❌ (`src/runtime/os_darwin.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/os_windows.go`, `stdcall`)
- ❌ (`src/runtime/os_windows.go`, `profileLoop`)
- ❌ (`src/runtime/os_windows.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/signal_unix.go`, `sigprofNonGo`)
- ❌ (`src/runtime/signal_unix.go`, `sigprofNonGoPC`)
- ❌ (`src/runtime/os_dragonfly.go`, `setProcessCPUProfiler`)
- ❌ (`src/runtime/os_dragonfly.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/proc.go`, `execute`)
- ❌ (`src/runtime/proc.go`, `sigprof`)
- ❌ (`src/runtime/proc.go`, `setcpuprofilerate`)
- ✅ (`src/runtime/cpuprof.go`, `SetCPUProfileRate`)
- ❌ (`src/runtime/cpuprof.go`, `add`)
- ❌ (`src/runtime/cgocall.go`, `cgocallbackg1`)
- ❌ (`src/runtime/os_aix.go`, `setProcessCPUProfiler`)
- ❌ (`src/runtime/os_aix.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/os_linux.go`, `setProcessCPUProfiler`)
- ❌ (`src/runtime/os_linux.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/os_openbsd.go`, `setProcessCPUProfiler`)
- ❌ (`src/runtime/os_openbsd.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/os_freebsd.go`, `setProcessCPUProfiler`)
- ❌ (`src/runtime/os_freebsd.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/pprof/protomem.go`, `writeHeapProto`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `avoidFunctions`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestCPUProfile`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestCPUProfileMultithreaded`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestCPUProfileMultithreadMagnitude`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestCPUProfileInlining`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestCPUProfileRecursion`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `recursionChainTop`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `testCPUProfile`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestGoroutineSwitch`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestMathBigDivide`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestMorestack`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `BenchmarkGoroutine`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestCPUProfileLabel`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestLabelRace`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestGoroutineProfileLabelRace`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestLabelSystemstack`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestTryAdd`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `TestTimeVDSO`)
- ❌ (`src/runtime/pprof/proto_test.go`, `translateCPUProfile`)
- ❌ (`src/runtime/signal_unix.go`, `sigtrampgo`)
- ❌ (`src/runtime/signal_unix.go`, `sighandler`)
- ❌ (`src/runtime/pprof/proto.go`, `newProfileBuilder`)
- ❌ (`src/runtime/pprof/proto.go`, `addCPUData`)
- ❌ (`src/runtime/pprof/proto.go`, `build`)
- ✅ (`src/runtime/cpuprof.go`, `SetCPUProfileRate`)
- ❌ (`src/runtime/testdata/testprogcgo/threadpprof.go`, `pprofThread`)
- ❌ (`src/runtime/pprof/pprof.go`, `printCountCycleProfile`)
- ❌ (`src/runtime/pprof/pprof.go`, `printCountProfile`)
- ❌ (`src/runtime/pprof/pprof.go`, `StartCPUProfile`)
- ❌ (`src/runtime/pprof/pprof.go`, `profileWriter`)
- ✅ (`src/runtime/pprof/pprof.go`, `StopCPUProfile`)
- ❌ (`src/runtime/testdata/testprogcgo/tracebackctxt.go`, `TracebackContextPreemptionGoFunction`)
- ❌ (`src/runtime/os_linux.go`, `osinit`)
- ❌ (`src/runtime/os_linux.go`, `validSIGPROF`)
- ❌ (`src/runtime/os_linux.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/os_linux.go`, `setProcessCPUProfiler`)
- ❌ (`src/runtime/proc.go`, `sigprof`)
- ❌ (`src/runtime/os_linux.go`, `validSIGPROF`)
- ❌ (`src/runtime/os_linux.go`, `setThreadCPUProfiler`)
- ❌ (`src/runtime/os_windows.go`, `profilem`)
- ❌ (`src/runtime/signal_unix.go`, `sighandler`)

### 📊 Proposal #42537

#### File Embeddings - Directory Level
- ❌ `src/archive/tar`
- ❌ `src/archive/zip`
- ❌ `src/bytes`
- ❌ `src/cmd/doc`
- ❌ `src/cmd/fix`
- ❌ `src/cmd/go/internal/clean`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/vet`
- ❌ `src/crypto/ecdsa`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/encoding/asn1`
- ❌ `src/encoding/json`
- ❌ `src/encoding/pem`
- ❌ `src/encoding/xml`
- ❌ `src/go/build`
- ❌ `src/go/constant`
- ❌ `src/go/doc`
- ❌ `src/go/importer`
- ❌ `src/go/printer`
- ❌ `src/go/types`
- ❌ `src/html/template`
- ❌ `src/mime`
- ❌ `src/net`
- ❌ `src/net/http`
- ❌ `src/net/http/cgi`
- ❌ `src/net/http/internal`
- ❌ `src/net/mail`
- ❌ `src/net/smtp`
- ❌ `src/net/textproto`
- ❌ `src/net/url`
- ❌ `src/os`
- ❌ `src/os/exec`
- ❌ `src/os/user`
- ❌ `src/regexp`
- ❌ `src/regexp/syntax`
- ❌ `src/runtime`
- ❌ `src/runtime/pprof`
- ❌ `src/runtime/testdata/testprog`
- ❌ `src/strconv`
- ❌ `src/strings`
- ❌ `src/text/template`
- ❌ `test`

#### File Embeddings - File Level
- ❌ `src/archive/tar/strconv.go`
- ❌ `src/archive/tar/writer_test.go`
- ❌ `src/archive/zip/writer_test.go`
- ❌ `src/bytes/bytes.go`
- ❌ `src/bytes/bytes_test.go`
- ❌ `src/cmd/doc/dirs.go`
- ❌ `src/cmd/doc/pkg.go`
- ❌ `src/cmd/fix/typecheck.go`
- ❌ `src/cmd/go/internal/clean/clean.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/crypto/ecdsa/ecdsa_test.go`
- ❌ `src/crypto/tls/handshake_client_test.go`
- ❌ `src/crypto/tls/handshake_test.go`
- ❌ `src/crypto/x509/pem_decrypt.go`
- ❌ `src/encoding/asn1/common.go`
- ❌ `src/encoding/json/tags.go`
- ❌ `src/encoding/pem/pem.go`
- ❌ `src/encoding/xml/typeinfo.go`
- ❌ `src/encoding/xml/xml.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/go/build/read.go`
- ❌ `src/go/build/read_test.go`
- ❌ `src/go/constant/value_test.go`
- ❌ `src/go/doc/headscan.go`
- ❌ `src/go/importer/importer_test.go`
- ❌ `src/go/printer/comment.go`
- ❌ `src/go/printer/nodes.go`
- ❌ `src/go/printer/printer.go`
- ❌ `src/go/types/eval_test.go`
- ❌ `src/html/template/attr.go`
- ❌ `src/html/template/js.go`
- ❌ `src/html/template/url.go`
- ❌ `src/mime/encodedword.go`
- ❌ `src/mime/mediatype.go`
- ❌ `src/net/http/cgi/child.go`
- ❌ `src/net/http/cgi/host.go`
- ❌ `src/net/http/cgi/host_test.go`
- ❌ `src/net/http/client_test.go`
- ❌ `src/net/http/cookie.go`
- ❌ `src/net/http/fs.go`
- ❌ `src/net/http/internal/chunked.go`
- ❌ `src/net/http/main_test.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/net/mail/message.go`
- ❌ `src/net/main_posix_test.go`
- ❌ `src/net/main_test.go`
- ❌ `src/net/platform_test.go`
- ❌ `src/net/smtp/smtp.go`
- ❌ `src/net/textproto/reader.go`
- ❌ `src/net/url/url.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/os_test.go`
- ❌ `src/os/user/cgo_lookup_unix.go`
- ❌ `src/os/user/lookup_unix.go`
- ❌ `src/regexp/exec_test.go`
- ❌ `src/regexp/regexp.go`
- ❌ `src/regexp/syntax/parse.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/proto.go`
- ❌ `src/runtime/pprof/proto_test.go`
- ❌ `src/runtime/runtime-gdb_test.go`
- ❌ `src/runtime/testdata/testprog/numcpu_freebsd.go`
- ❌ `src/runtime/testdata/testprog/traceback_ancestors.go`
- ❌ `src/strconv/fp_test.go`
- ❌ `src/strings/strings.go`
- ❌ `src/strings/strings_test.go`
- ❌ `src/text/template/option.go`
- ❌ `test/zerodivide.go`

#### Function Embeddings - Directory Level
- ❌ `src/archive/tar`
- ❌ `src/archive/zip`
- ❌ `src/bytes`
- ❌ `src/cmd/doc`
- ❌ `src/cmd/fix`
- ❌ `src/cmd/go/internal/clean`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/vet`
- ❌ `src/crypto/ecdsa`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/encoding/asn1`
- ❌ `src/encoding/json`
- ❌ `src/encoding/pem`
- ❌ `src/encoding/xml`
- ❌ `src/go/build`
- ❌ `src/go/constant`
- ❌ `src/go/doc`
- ❌ `src/go/importer`
- ❌ `src/go/printer`
- ❌ `src/go/types`
- ❌ `src/html/template`
- ❌ `src/mime`
- ❌ `src/net`
- ❌ `src/net/http`
- ❌ `src/net/http/cgi`
- ❌ `src/net/http/internal`
- ❌ `src/net/mail`
- ❌ `src/net/smtp`
- ❌ `src/net/textproto`
- ❌ `src/net/url`
- ❌ `src/os`
- ❌ `src/os/exec`
- ❌ `src/os/user`
- ❌ `src/regexp`
- ❌ `src/regexp/syntax`
- ❌ `src/runtime`
- ❌ `src/runtime/pprof`
- ❌ `src/runtime/testdata/testprog`
- ❌ `src/strconv`
- ❌ `src/strings`
- ❌ `src/text/template`
- ❌ `test`

#### Function Embeddings - File Level
- ❌ `src/archive/tar/strconv.go`
- ❌ `src/archive/tar/writer_test.go`
- ❌ `src/archive/zip/writer_test.go`
- ❌ `src/bytes/bytes.go`
- ❌ `src/bytes/bytes_test.go`
- ❌ `src/cmd/doc/dirs.go`
- ❌ `src/cmd/doc/pkg.go`
- ❌ `src/cmd/fix/typecheck.go`
- ❌ `src/cmd/go/internal/clean/clean.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/crypto/ecdsa/ecdsa_test.go`
- ❌ `src/crypto/tls/handshake_client_test.go`
- ❌ `src/crypto/tls/handshake_test.go`
- ❌ `src/crypto/x509/pem_decrypt.go`
- ❌ `src/encoding/asn1/common.go`
- ❌ `src/encoding/json/tags.go`
- ❌ `src/encoding/pem/pem.go`
- ❌ `src/encoding/xml/typeinfo.go`
- ❌ `src/encoding/xml/xml.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/go/build/read.go`
- ❌ `src/go/build/read_test.go`
- ❌ `src/go/constant/value_test.go`
- ❌ `src/go/doc/headscan.go`
- ❌ `src/go/importer/importer_test.go`
- ❌ `src/go/printer/comment.go`
- ❌ `src/go/printer/nodes.go`
- ❌ `src/go/printer/printer.go`
- ❌ `src/go/types/eval_test.go`
- ❌ `src/html/template/attr.go`
- ❌ `src/html/template/js.go`
- ❌ `src/html/template/url.go`
- ❌ `src/mime/encodedword.go`
- ❌ `src/mime/mediatype.go`
- ❌ `src/net/http/cgi/child.go`
- ❌ `src/net/http/cgi/host.go`
- ❌ `src/net/http/cgi/host_test.go`
- ❌ `src/net/http/client_test.go`
- ❌ `src/net/http/cookie.go`
- ❌ `src/net/http/fs.go`
- ❌ `src/net/http/internal/chunked.go`
- ❌ `src/net/http/main_test.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/net/mail/message.go`
- ❌ `src/net/main_posix_test.go`
- ❌ `src/net/main_test.go`
- ❌ `src/net/platform_test.go`
- ❌ `src/net/smtp/smtp.go`
- ❌ `src/net/textproto/reader.go`
- ❌ `src/net/url/url.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/os_test.go`
- ❌ `src/os/user/cgo_lookup_unix.go`
- ❌ `src/os/user/lookup_unix.go`
- ❌ `src/regexp/exec_test.go`
- ❌ `src/regexp/regexp.go`
- ❌ `src/regexp/syntax/parse.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/proto.go`
- ❌ `src/runtime/pprof/proto_test.go`
- ❌ `src/runtime/runtime-gdb_test.go`
- ❌ `src/runtime/testdata/testprog/numcpu_freebsd.go`
- ❌ `src/runtime/testdata/testprog/traceback_ancestors.go`
- ❌ `src/strconv/fp_test.go`
- ❌ `src/strings/strings.go`
- ❌ `src/strings/strings_test.go`
- ❌ `src/text/template/option.go`
- ❌ `test/zerodivide.go`

#### Function Embeddings - Function Level
- ❌ (`src/html/template/js.go`, `isJSType`)
- ❌ (`src/net/http/client_test.go`, `testRedirectsByMethod`)
- ❌ (`src/encoding/json/tags.go`, `parseTag`)
- ❌ (`src/encoding/json/tags.go`, `Contains`)
- ❌ (`src/regexp/syntax/parse.go`, `Parse`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `containsInOrder`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `stackContainsLabeled`)
- ❌ (`src/net/main_posix_test.go`, `disableSocketConnect`)
- ❌ (`test/zerodivide.go`, `main`)
- ❌ (`src/os/user/lookup_unix.go`, `matchUserIndexValue`)
- ❌ (`src/net/platform_test.go`, `testableNetwork`)
- ❌ (`src/net/platform_test.go`, `testableAddress`)
- ❌ (`src/net/platform_test.go`, `testableListenArgs`)
- ❌ (`src/net/http/cgi/child.go`, `envMap`)
- ❌ (`src/archive/tar/strconv.go`, `hasNUL`)
- ❌ (`src/archive/tar/strconv.go`, `parsePAXTime`)
- ❌ (`src/archive/tar/strconv.go`, `parsePAXRecord`)
- ❌ (`src/archive/tar/strconv.go`, `formatPAXRecord`)
- ❌ (`src/archive/tar/strconv.go`, `validPAXRecord`)
- ❌ (`src/net/http/internal/chunked.go`, `removeChunkExtension`)
- ❌ (`src/go/types/eval_test.go`, `split`)
- ❌ (`src/html/template/attr.go`, `attrType`)
- ❌ (`src/go/doc/headscan.go`, `appendHeadings`)
- ❌ (`src/go/doc/headscan.go`, `main`)
- ❌ (`src/net/main_test.go`, `runningGoroutines`)
- ❌ (`src/go/importer/importer_test.go`, `TestForCompiler`)
- ❌ (`src/go/build/build_test.go`, `TestMissingImportErrorRepetition`)
- ❌ (`src/net/http/transport.go`, `dialConn`)
- ❌ (`src/os/exec/exec.go`, `dedupEnvCase`)
- ❌ (`src/os/exec/exec.go`, `addCriticalEnv`)
- ❌ (`src/net/http/server.go`, `stripHostPort`)
- ❌ (`src/net/http/cookie.go`, `readSetCookies`)
- ❌ (`src/net/http/cookie.go`, `readCookies`)
- ❌ (`src/net/http/cookie.go`, `sanitizeCookieValue`)
- ❌ (`src/cmd/doc/pkg.go`, `oneLineNodeDepth`)
- ❌ (`src/regexp/regexp.go`, `expand`)
- ❌ (`src/regexp/regexp.go`, `extract`)
- ❌ (`src/go/constant/value_test.go`, `testNumbers`)
- ❌ (`src/go/constant/value_test.go`, `val`)
- ❌ (`src/go/printer/nodes.go`, `normalizedNumber`)
- ❌ (`src/os/os_test.go`, `TestHostname`)
- ❌ (`src/regexp/exec_test.go`, `parseResult`)
- ❌ (`src/regexp/exec_test.go`, `testFowler`)
- ❌ (`src/net/textproto/reader.go`, `ReadMIMEHeader`)
- ❌ (`src/encoding/pem/pem.go`, `Decode`)
- ❌ (`src/encoding/asn1/common.go`, `parseFieldParameters`)
- ❌ (`src/archive/tar/writer_test.go`, `TestIssue12594`)
- ❌ (`src/encoding/xml/typeinfo.go`, `structFieldInfo`)
- ❌ (`src/runtime/runtime-gdb_test.go`, `testGdbPython`)
- ❌ (`src/os/user/cgo_lookup_unix.go`, `buildUser`)
- ❌ (`src/runtime/pprof/proto.go`, `parseProcSelfMaps`)
- ❌ (`src/go/build/read.go`, `parseGoEmbed`)
- ❌ (`src/net/http/request.go`, `BasicAuth`)
- ❌ (`src/net/http/request.go`, `parseBasicAuth`)
- ❌ (`src/net/http/request.go`, `parseRequestLine`)
- ❌ (`src/cmd/doc/dirs.go`, `findCodeRoots`)
- ❌ (`src/cmd/fix/typecheck.go`, `typecheck1`)
- ❌ (`src/crypto/ecdsa/ecdsa_test.go`, `TestVectors`)
- ❌ (`src/net/http/cgi/host_test.go`, `runResponseChecks`)
- ❌ (`src/crypto/x509/pem_decrypt.go`, `DecryptPEMBlock`)
- ❌ (`src/runtime/testdata/testprog/numcpu_freebsd.go`, `getList`)
- ❌ (`src/mime/encodedword.go`, `Decode`)
- ❌ (`src/net/url/url.go`, `Parse`)
- ❌ (`src/net/url/url.go`, `parse`)
- ❌ (`src/net/url/url.go`, `parseAuthority`)
- ❌ (`src/net/url/url.go`, `String`)
- ❌ (`src/net/url/url.go`, `parseQuery`)
- ❌ (`src/net/url/url.go`, `resolvePath`)
- ❌ (`src/net/url/url.go`, `Parse`)
- ❌ (`src/cmd/vet/vet_test.go`, `errorCheck`)
- ❌ (`src/go/build/read_test.go`, `testRead`)
- ❌ (`src/net/http/fs.go`, `parseRange`)
- ❌ (`src/mime/mediatype.go`, `FormatMediaType`)
- ❌ (`src/mime/mediatype.go`, `ParseMediaType`)
- ❌ (`src/runtime/pprof/proto_test.go`, `TestProcSelfMaps`)
- ❌ (`src/strconv/fp_test.go`, `myatof64`)
- ❌ (`src/strconv/fp_test.go`, `myatof32`)
- ❌ (`src/os/exec/exec_test.go`, `TestCatGoodAndBadFile`)
- ❌ (`src/go/build/build.go`, `findImportComment`)
- ❌ (`src/go/build/build.go`, `saveCgo`)
- ❌ (`src/go/build/build.go`, `goodOSArchFile`)
- ❌ (`src/encoding/xml/xml.go`, `nsname`)
- ❌ (`src/encoding/xml/xml.go`, `emitCDATA`)
- ❌ (`src/encoding/xml/xml.go`, `procInst`)
- ❌ (`src/net/http/main_test.go`, `interestingGoroutines`)
- ❌ (`src/html/template/url.go`, `isSafeURL`)
- ❌ (`src/crypto/tls/handshake_test.go`, `parseTestData`)
- ❌ (`src/runtime/testdata/testprog/traceback_ancestors.go`, `printStack`)
- ❌ (`src/runtime/testdata/testprog/traceback_ancestors.go`, `goroutineID`)
- ❌ (`src/text/template/option.go`, `setOption`)
- ❌ (`src/net/http/response.go`, `ReadResponse`)
- ❌ (`src/crypto/tls/handshake_client_test.go`, `Write`)
- ❌ (`src/archive/zip/writer_test.go`, `TestWriterDirAttributes`)
- ❌ (`src/go/printer/printer.go`, `stripCommonPrefix`)
- ❌ (`src/net/http/cgi/host.go`, `ServeHTTP`)
- ❌ (`src/net/mail/message.go`, `ParseDate`)
- ❌ (`src/net/smtp/smtp.go`, `ehlo`)
- ❌ (`src/strings/strings.go`, `CutPrefix`)
- ❌ (`src/strings/strings.go`, `CutSuffix`)
- ❌ (`src/bytes/bytes_test.go`, `TestCutPrefix`)
- ❌ (`src/bytes/bytes_test.go`, `TestCutSuffix`)
- ❌ (`src/bytes/bytes.go`, `CutPrefix`)
- ❌ (`src/bytes/bytes.go`, `CutSuffix`)
- ❌ (`src/strings/strings_test.go`, `TestCutPrefix`)
- ❌ (`src/strings/strings_test.go`, `TestCutSuffix`)
- ❌ (`src/go/build/build.go`, `hasSubdir`)
- ❌ (`src/go/printer/comment.go`, `formatDocComment`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `PackagesAndErrorsOutsideModule`)
- ❌ (`src/cmd/go/internal/clean/clean.go`, `clean`)

### 📊 Proposal #42681

#### File Embeddings - Directory Level
- ❌ `src/cmd/asm/internal/lex`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/runtime`

#### File Embeddings - File Level
- ❌ `src/cmd/asm/internal/lex/input.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/buildruntime.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/link/internal/ld/main.go`
- ❌ `src/runtime/heapdump.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/asm/internal/lex`
- ✅ `src/cmd/dist`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/runtime`

#### Function Embeddings - File Level
- ❌ `src/cmd/asm/internal/lex/input.go`
- ✅ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/buildruntime.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/link/internal/ld/main.go`
- ❌ `src/runtime/heapdump.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/dist/buildruntime.go`, `mkzversion`)
- ❌ (`src/cmd/link/internal/ld/main.go`, `Main`)
- ❌ (`src/cmd/dist/build.go`, `xinit`)
- ❌ (`src/cmd/dist/build.go`, `runInstall`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `asmArgs`)
- ❌ (`src/cmd/asm/internal/lex/input.go`, `predefine`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `buildActionID`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `printLinkerConfig`)
- ❌ (`src/cmd/dist/buildruntime.go`, `mkzversion`)
- ❌ (`src/cmd/link/internal/ld/main.go`, `Main`)
- ❌ (`src/cmd/asm/internal/lex/input.go`, `predefine`)
- ❌ (`src/cmd/dist/build.go`, `xinit`)
- ❌ (`src/cmd/dist/build.go`, `runInstall`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `asmArgs`)
- ❌ (`src/runtime/heapdump.go`, `dumpparams`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `buildActionID`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `printLinkerConfig`)

### 📊 Proposal #42710

#### File Embeddings - Directory Level
- ✅ `src/hash/maphash`

#### File Embeddings - File Level
- ❌ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/hash/maphash`

#### Function Embeddings - File Level
- ❌ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/hash/maphash/maphash_test.go`, `TestHashGrouping`)
- ❌ (`src/hash/maphash/maphash.go`, `WriteByte`)
- ❌ (`src/hash/maphash/maphash.go`, `Write`)
- ❌ (`src/hash/maphash/maphash.go`, `WriteString`)
- ❌ (`src/hash/maphash/maphash.go`, `flush`)
- ❌ (`src/hash/maphash/maphash.go`, `Sum64`)
- ❌ (`src/hash/maphash/maphash.go`, `initSeed`)
- ❌ (`src/hash/maphash/maphash.go`, `SetSeed`)
- ❌ (`src/hash/maphash/maphash_test.go`, `TestHashGrouping`)
- ✅ (`src/hash/maphash/maphash_test.go`, `benchmarkSize`)
- ❌ (`src/hash/maphash/maphash_test.go`, `BenchmarkHash`)
- ❌ (`src/hash/maphash/maphash.go`, `Bytes`)
- ❌ (`src/hash/maphash/maphash.go`, `String`)

### 📊 Proposal #42782

#### File Embeddings - Directory Level
- ✅ `src/reflect`

#### File Embeddings - File Level
- ✅ `src/reflect/visiblefields.go`
- ✅ `src/reflect/visiblefields_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/reflect`

#### Function Embeddings - File Level
- ✅ `src/reflect/visiblefields.go`
- ❌ `src/reflect/visiblefields_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/reflect/visiblefields.go`, `VisibleFields`)
- ❌ (`src/reflect/visiblefields.go`, `walk`)
- ❌ (`src/reflect/visiblefields_test.go`, `TestFields`)

### 📊 Proposal #43401

#### File Embeddings - Directory Level
- ✅ `src/encoding/csv`

#### File Embeddings - File Level
- ❌ `src/encoding/csv/reader.go`
- ✅ `src/encoding/csv/reader_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/encoding/csv`

#### Function Embeddings - File Level
- ✅ `src/encoding/csv/reader.go`
- ✅ `src/encoding/csv/reader_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/encoding/csv/reader.go`, `InputOffset`)
- ✅ (`src/encoding/csv/reader.go`, `readLine`)
- ❌ (`src/encoding/csv/reader_test.go`, `TestRead`)

### 📊 Proposal #43620

#### File Embeddings - Directory Level
- ✅ `src/testing`

#### File Embeddings - File Level
- ✅ `src/testing/benchmark.go`
- ❌ `src/testing/benchmark_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/testing`

#### Function Embeddings - File Level
- ✅ `src/testing/benchmark.go`
- ❌ `src/testing/benchmark_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/testing/benchmark.go`, `Elapsed`)
- ❌ (`src/testing/benchmark_test.go`, `ExampleB_ReportMetric`)

### 📊 Proposal #43698

#### File Embeddings - Directory Level
- ✅ `src/embed`
- ❌ `src/embed/internal/embedtest`

#### File Embeddings - File Level
- ✅ `src/embed/embed.go`
- ❌ `src/embed/internal/embedtest/embed_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/embed`
- ✅ `src/embed/internal/embedtest`

#### Function Embeddings - File Level
- ❌ `src/embed/embed.go`
- ✅ `src/embed/internal/embedtest/embed_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/embed/embed.go`, `lookup`)
- ❌ (`src/embed/embed.go`, `readDir`)
- ✅ (`src/embed/internal/embedtest/embed_test.go`, `TestUninitialized`)

### 📊 Proposal #43724

#### File Embeddings - Directory Level
- ❌ `src/internal/syscall/windows`
- ❌ `src/syscall`

#### File Embeddings - File Level
- ❌ `src/internal/syscall/windows/zsyscall_windows.go`
- ❌ `src/syscall/mksyscall_windows.go`

#### Function Embeddings - Directory Level
- ❌ `src/internal/syscall/windows`
- ❌ `src/syscall`

#### Function Embeddings - File Level
- ❌ `src/internal/syscall/windows/zsyscall_windows.go`
- ❌ `src/syscall/mksyscall_windows.go`

#### Function Embeddings - Function Level
- ❌ (`src/syscall/mksyscall_windows.go`, `main`)
- ❌ (`src/internal/syscall/windows/zsyscall_windows.go`, `GetComputerNameEx`)
- ❌ (`src/internal/syscall/windows/zsyscall_windows.go`, `SetFileInformationByHandle`)

### 📊 Proposal #43744

#### File Embeddings - Directory Level
- ❌ `src/runtime`
- ✅ `src/testing`
- ❌ `src/time`

#### File Embeddings - File Level
- ❌ `src/runtime/proc.go`
- ❌ `src/testing/benchmark_test.go`
- ❌ `src/time/sleep_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/runtime`
- ✅ `src/testing`
- ❌ `src/time`

#### Function Embeddings - File Level
- ❌ `src/runtime/proc.go`
- ❌ `src/testing/benchmark_test.go`
- ❌ `src/time/sleep_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/proc.go`, `handoffp`)
- ❌ (`src/runtime/proc.go`, `wakeNetPoller`)
- ❌ (`src/runtime/proc.go`, `procresize`)
- ❌ (`src/runtime/proc.go`, `sysmon`)
- ❌ (`src/time/sleep_test.go`, `BenchmarkParallelTimerLatency`)
- ❌ (`src/time/sleep_test.go`, `BenchmarkStaggeredTickerLatency`)
- ❌ (`src/time/sleep_test.go`, `warmupScheduler`)
- ❌ (`src/time/sleep_test.go`, `doWork`)
- ❌ (`src/testing/benchmark_test.go`, `ExampleB_ReportMetric`)

### 📊 Proposal #43823

#### File Embeddings - Directory Level
- ✅ `src/time`

#### File Embeddings - File Level
- ❌ `src/time/format.go`

#### Function Embeddings - Directory Level
- ✅ `src/time`

#### Function Embeddings - File Level
- ✅ `src/time/format.go`

#### Function Embeddings - Function Level
- ❌ (`src/time/format.go`, `nextStdChunk`)
- ❌ (`src/time/format.go`, `parse`)
- ❌ (`src/time/format.go`, `commaOrPeriod`)
- ❌ (`src/time/format.go`, `parseNanoseconds`)

### 📊 Proposal #43931

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/staticdata`
- ❌ `src/cmd/dist`
- ❌ `src/embed/internal/embedtest`
- ❌ `src/go/types`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/noder/noder.go`
- ❌ `src/cmd/compile/internal/staticdata/embed.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/embed/internal/embedtest/embed_test.go`
- ❌ `src/go/types/stdlib_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/staticdata`
- ❌ `src/cmd/dist`
- ❌ `src/embed/internal/embedtest`
- ❌ `src/go/types`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/noder/noder.go`
- ❌ `src/cmd/compile/internal/staticdata/embed.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/embed/internal/embedtest/embed_test.go`
- ❌ `src/go/types/stdlib_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/types/stdlib_test.go`, `TestStdTest`)
- ❌ (`src/embed/internal/embedtest/embed_test.go`, `TestDir`)
- ❌ (`src/embed/internal/embedtest/embed_test.go`, `TestHidden`)
- ❌ (`src/embed/internal/embedtest/embed_test.go`, `TestUninitialized`)
- ❌ (`src/cmd/compile/internal/staticdata/embed.go`, `embedFileList`)
- ❌ (`src/cmd/compile/internal/staticdata/embed.go`, `embedKind`)
- ❌ (`src/cmd/compile/internal/staticdata/embed.go`, `embedFileNameSplit`)
- ❌ (`src/cmd/compile/internal/staticdata/embed.go`, `embedFileLess`)
- ❌ (`src/cmd/compile/internal/staticdata/embed.go`, `WriteEmbed`)
- ❌ (`src/cmd/compile/internal/gc/main.go`, `Main`)
- ❌ (`src/cmd/dist/test.go`, `registerStdTest`)
- ❌ (`src/cmd/dist/test.go`, `registerTests`)
- ❌ (`src/cmd/compile/internal/noder/noder.go`, `LoadPackage`)

### 📊 Proposal #43947

#### File Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ✅ `src/os/exec`

#### File Embeddings - File Level
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/dist/util.go`
- ❌ `src/os/exec/dot_test.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/lp_plan9.go`
- ❌ `src/os/exec/lp_unix.go`
- ❌ `src/os/exec/lp_windows.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ✅ `src/os/exec`

#### Function Embeddings - File Level
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/dist/util.go`
- ❌ `src/os/exec/dot_test.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/lp_plan9.go`
- ❌ `src/os/exec/lp_unix.go`
- ✅ `src/os/exec/lp_windows.go`

#### Function Embeddings - Function Level
- ❌ (`src/os/exec/dot_test.go`, `TestLookPath`)
- ❌ (`src/os/exec/lp_unix.go`, `LookPath`)
- ❌ (`src/cmd/dist/test.go`, `run`)
- ❌ (`src/cmd/dist/test.go`, `registerStdTest`)
- ❌ (`src/cmd/dist/test.go`, `registerRaceBenchTest`)
- ❌ (`src/cmd/dist/test.go`, `registerTests`)
- ❌ (`src/cmd/dist/test.go`, `flattenCmdline`)
- ❌ (`src/cmd/dist/util.go`, `run`)
- ❌ (`src/os/exec/exec.go`, `Command`)
- ❌ (`src/os/exec/exec.go`, `String`)
- ❌ (`src/os/exec/exec.go`, `writerDescriptor`)
- ❌ (`src/os/exec/exec.go`, `Start`)
- ❌ (`src/os/exec/lp_plan9.go`, `LookPath`)
- ❌ (`src/cmd/dist/build.go`, `xinit`)
- ❌ (`src/os/exec/lp_windows.go`, `LookPath`)
- ❌ (`src/os/exec/lp_unix.go`, `LookPath`)
- ❌ (`src/cmd/dist/test.go`, `run`)
- ❌ (`src/cmd/dist/test.go`, `registerStdTest`)
- ❌ (`src/cmd/dist/test.go`, `registerRaceBenchTest`)
- ❌ (`src/cmd/dist/test.go`, `registerTests`)
- ❌ (`src/cmd/dist/test.go`, `flattenCmdline`)
- ❌ (`src/cmd/dist/util.go`, `run`)
- ❌ (`src/os/exec/exec.go`, `Error`)
- ❌ (`src/os/exec/exec.go`, `Command`)
- ❌ (`src/os/exec/exec.go`, `String`)
- ❌ (`src/os/exec/exec.go`, `Start`)
- ❌ (`src/os/exec/lp_plan9.go`, `LookPath`)
- ❌ (`src/cmd/dist/build.go`, `xinit`)
- ❌ (`src/os/exec/lp_windows.go`, `LookPath`)
- ❌ (`src/os/exec/exec.go`, `Command`)

### 📊 Proposal #43993

#### File Embeddings - Directory Level
- ❌ `src/reflect`
- ❌ `src/text/template`

#### File Embeddings - File Level
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/value.go`
- ❌ `src/text/template/exec.go`
- ❌ `src/text/template/funcs.go`

#### Function Embeddings - Directory Level
- ✅ `src/reflect`
- ✅ `src/text/template`

#### Function Embeddings - File Level
- ✅ `src/reflect/all_test.go`
- ❌ `src/reflect/value.go`
- ✅ `src/text/template/exec.go`
- ❌ `src/text/template/funcs.go`

#### Function Embeddings - Function Level
- ❌ (`src/reflect/value.go`, `Set`)
- ❌ (`src/reflect/value.go`, `Zero`)
- ❌ (`src/reflect/all_test.go`, `TestSmallZero`)
- ❌ (`src/reflect/all_test.go`, `TestZeroSet`)
- ❌ (`src/text/template/exec.go`, `isMissing`)
- ❌ (`src/text/template/exec.go`, `evalPipeline`)
- ❌ (`src/text/template/exec.go`, `notAFunction`)
- ❌ (`src/text/template/exec.go`, `evalField`)
- ❌ (`src/text/template/exec.go`, `evalCall`)
- ❌ (`src/text/template/funcs.go`, `isNil`)

### 📊 Proposal #44006

#### File Embeddings - Directory Level
- ❌ `src/syscall/js`

#### File Embeddings - File Level
- ❌ `src/syscall/js/js.go`

#### Function Embeddings - Directory Level
- ✅ `src/syscall/js`

#### Function Embeddings - File Level
- ✅ `src/syscall/js/js.go`

#### Function Embeddings - Function Level
- ❌ (`src/syscall/js/js.go`, `makeValue`)
- ❌ (`src/syscall/js/js.go`, `ValueOf`)

### 📊 Proposal #44011

#### File Embeddings - Directory Level
- ✅ `src/os`
- ❌ `src/os/exec`
- ✅ `src/syscall`

#### File Embeddings - File Level
- ❌ `src/os/exec/exec_windows_test.go`
- ❌ `src/os/file_windows.go`
- ❌ `src/syscall/exec_windows.go`
- ❌ `src/syscall/exec_windows_test.go`
- ❌ `src/syscall/syscall_windows.go`
- ❌ `src/syscall/zsyscall_windows.go`

#### Function Embeddings - Directory Level
- ❌ `src/os`
- ❌ `src/os/exec`
- ✅ `src/syscall`

#### Function Embeddings - File Level
- ❌ `src/os/exec/exec_windows_test.go`
- ❌ `src/os/file_windows.go`
- ❌ `src/syscall/exec_windows.go`
- ❌ `src/syscall/exec_windows_test.go`
- ✅ `src/syscall/syscall_windows.go`
- ✅ `src/syscall/zsyscall_windows.go`

#### Function Embeddings - Function Level
- ❌ (`src/syscall/zsyscall_windows.go`, `deleteProcThreadAttributeList`)
- ❌ (`src/syscall/zsyscall_windows.go`, `initializeProcThreadAttributeList`)
- ❌ (`src/syscall/zsyscall_windows.go`, `updateProcThreadAttribute`)
- ❌ (`src/syscall/syscall_windows.go`, `newProcThreadAttributeList`)
- ❌ (`src/syscall/exec_windows.go`, `StartProcess`)
- ❌ (`src/syscall/exec_windows.go`, `StartProcess`)
- ❌ (`src/os/file_windows.go`, `Pipe`)
- ❌ (`src/os/exec/exec_windows_test.go`, `TestPipePassing`)
- ❌ (`src/syscall/exec_windows_test.go`, `TestChangingProcessParent`)
- ❌ (`src/syscall/exec_windows.go`, `StartProcess`)

### 📊 Proposal #44143

#### File Embeddings - Directory Level
- ❌ `src/net/http`

#### File Embeddings - File Level
- ❌ `src/net/http/socks_bundle.go`

#### Function Embeddings - Directory Level
- ❌ `src/net/http`

#### Function Embeddings - File Level
- ❌ `src/net/http/socks_bundle.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/http/socks_bundle.go`, `Dial`)

### 📊 Proposal #44167

#### File Embeddings - Directory Level
- ✅ `src/runtime`

#### File Embeddings - File Level
- ❌ `src/runtime/export_test.go`
- ❌ `src/runtime/mcache.go`
- ❌ `src/runtime/metrics.go`
- ✅ `src/runtime/mgc.go`
- ❌ `src/runtime/mgcmark.go`
- ✅ `src/runtime/mgcpacer.go`
- ✅ `src/runtime/mgcpacer_test.go`
- ❌ `src/runtime/mgcscavenge.go`
- ❌ `src/runtime/mgcsweep.go`
- ❌ `src/runtime/mgcwork.go`
- ❌ `src/runtime/mstats.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/stack.go`
- ❌ `src/runtime/symtab.go`

#### Function Embeddings - Directory Level
- ✅ `src/runtime`

#### Function Embeddings - File Level
- ❌ `src/runtime/export_test.go`
- ❌ `src/runtime/mcache.go`
- ❌ `src/runtime/metrics.go`
- ✅ `src/runtime/mgc.go`
- ❌ `src/runtime/mgcmark.go`
- ✅ `src/runtime/mgcpacer.go`
- ✅ `src/runtime/mgcpacer_test.go`
- ❌ `src/runtime/mgcscavenge.go`
- ❌ `src/runtime/mgcsweep.go`
- ❌ `src/runtime/mgcwork.go`
- ❌ `src/runtime/mstats.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/stack.go`
- ❌ `src/runtime/symtab.go`

#### Function Embeddings - Function Level
- ✅ (`src/runtime/mgcpacer.go`, `startCycle`)
- ✅ (`src/runtime/mgcpacer.go`, `revise`)
- ❌ (`src/runtime/mgcpacer.go`, `endCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `enlistWorker`)
- ❌ (`src/runtime/mgcpacer.go`, `findRunnableGCWorker`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgc.go`, `gcinit`)
- ❌ (`src/runtime/mgc.go`, `setGCPhase`)
- ❌ (`src/runtime/mgc.go`, `GC`)
- ❌ (`src/runtime/mgc.go`, `gcWaitOnMark`)
- ❌ (`src/runtime/mgc.go`, `test`)
- ❌ (`src/runtime/mgc.go`, `gcStart`)
- ❌ (`src/runtime/mgc.go`, `gcMarkDone`)
- ✅ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ✅ (`src/runtime/mgcpacer.go`, `revise`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgc.go`, `gcinit`)
- ❌ (`src/runtime/mgc.go`, `test`)
- ❌ (`src/runtime/mcache.go`, `refill`)
- ❌ (`src/runtime/mcache.go`, `allocLarge`)
- ❌ (`src/runtime/mcache.go`, `releaseAll`)
- ❌ (`src/runtime/mgcpacer.go`, `init`)
- ✅ (`src/runtime/mgcpacer.go`, `startCycle`)
- ✅ (`src/runtime/mgcpacer.go`, `revise`)
- ❌ (`src/runtime/mgcpacer.go`, `endCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `enlistWorker`)
- ❌ (`src/runtime/mgcpacer.go`, `findRunnableGCWorker`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgcsweep.go`, `deductSweepCredit`)
- ❌ (`src/runtime/mgc.go`, `gcinit`)
- ❌ (`src/runtime/mgc.go`, `test`)
- ❌ (`src/runtime/mgc.go`, `gcStart`)
- ✅ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ❌ (`src/runtime/mgc.go`, `gcMark`)
- ❌ (`src/runtime/mgc.go`, `gcResetMarkState`)
- ❌ (`src/runtime/mstats.go`, `readmemstats_m`)
- ❌ (`src/runtime/mgcpacer.go`, `commit`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ✅ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ❌ (`src/runtime/mgcpacer.go`, `init`)
- ✅ (`src/runtime/mgcpacer.go`, `revise`)
- ❌ (`src/runtime/mgcpacer.go`, `commit`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgc.go`, `gcinit`)
- ❌ (`src/runtime/mgc.go`, `test`)
- ❌ (`src/runtime/mgcpacer.go`, `init`)
- ❌ (`src/runtime/mgc.go`, `gcinit`)
- ❌ (`src/runtime/mgcpacer.go`, `init`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgcscavenge.go`, `gcPaceScavenger`)
- ❌ (`src/runtime/metrics.go`, `compute`)
- ✅ (`src/runtime/mgcpacer.go`, `startCycle`)
- ✅ (`src/runtime/mgcpacer.go`, `revise`)
- ❌ (`src/runtime/mgcpacer.go`, `commit`)
- ❌ (`src/runtime/mgc.go`, `gcStart`)
- ✅ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ❌ (`src/runtime/mstats.go`, `readmemstats_m`)
- ❌ (`src/runtime/mgcpacer.go`, `endCycle`)
- ❌ (`src/runtime/mgc.go`, `gcMarkDone`)
- ❌ (`src/runtime/mgcpacer.go`, `endCycle`)
- ✅ (`src/runtime/mgcpacer.go`, `revise`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgc.go`, `test`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgcsweep.go`, `gcPaceSweeper`)
- ✅ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ✅ (`src/runtime/mgcpacer.go`, `startCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `endCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `resetLive`)
- ❌ (`src/runtime/mgc.go`, `gcStart`)
- ✅ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ❌ (`src/runtime/mgc.go`, `gcBgMarkWorker`)
- ❌ (`src/runtime/mgc.go`, `gcMark`)
- ❌ (`src/runtime/mgc.go`, `gcSweep`)
- ❌ (`src/runtime/mcache.go`, `refill`)
- ❌ (`src/runtime/mcache.go`, `allocLarge`)
- ❌ (`src/runtime/mcache.go`, `releaseAll`)
- ❌ (`src/runtime/mcache.go`, `prepareForSweep`)
- ❌ (`src/runtime/mgcpacer.go`, `update`)
- ❌ (`src/runtime/stack.go`, `copystack`)
- ❌ (`src/runtime/proc.go`, `goexit0`)
- ❌ (`src/runtime/proc.go`, `newproc1`)
- ✅ (`src/runtime/mgcpacer.go`, `startCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `addScannableStack`)
- ❌ (`src/runtime/mgcpacer.go`, `addGlobals`)
- ❌ (`src/runtime/symtab.go`, `modulesinit`)
- ❌ (`src/runtime/mgcwork.go`, `dispose`)
- ✅ (`src/runtime/mgcpacer_test.go`, `TestGcPacer`)
- ❌ (`src/runtime/mgcpacer.go`, `init`)
- ✅ (`src/runtime/mgcpacer.go`, `startCycle`)
- ✅ (`src/runtime/mgcpacer.go`, `revise`)
- ❌ (`src/runtime/mgcpacer.go`, `endCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `resetLive`)
- ❌ (`src/runtime/mgcpacer.go`, `update`)
- ❌ (`src/runtime/mgcpacer.go`, `commit`)
- ✅ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ❌ (`src/runtime/mgcmark.go`, `markroot`)
- ❌ (`src/runtime/mgcmark.go`, `markrootBlock`)
- ❌ (`src/runtime/mgcmark.go`, `gcFlushBgCredit`)
- ❌ (`src/runtime/mgcmark.go`, `scanstack`)
- ❌ (`src/runtime/mgcmark.go`, `gcDrain`)
- ❌ (`src/runtime/mgcmark.go`, `gcDrainN`)
- ❌ (`src/runtime/mgcmark.go`, `scanobject`)
- ❌ (`src/runtime/mgcmark.go`, `gcDumpObject`)
- ❌ (`src/runtime/mgcmark.go`, `gcmarknewobject`)
- ❌ (`src/runtime/export_test.go`, `Revise`)
- ✅ (`src/runtime/mgcpacer.go`, `startCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `endCycle`)
- ❌ (`src/runtime/mgc.go`, `gcStart`)
- ❌ (`src/runtime/mgc.go`, `gcMarkDone`)
- ✅ (`src/runtime/mgcpacer_test.go`, `TestGcPacer`)
- ❌ (`src/runtime/mgcpacer_test.go`, `next`)
- ❌ (`src/runtime/mgcpacer_test.go`, `check`)
- ❌ (`src/runtime/mgcpacer_test.go`, `goalRatio`)
- ❌ (`src/runtime/mgcpacer_test.go`, `String`)
- ❌ (`src/runtime/mgcpacer_test.go`, `assertInEpsilon`)
- ❌ (`src/runtime/mgcpacer_test.go`, `assertInRange`)
- ❌ (`src/runtime/mgcpacer_test.go`, `constant`)
- ❌ (`src/runtime/mgcpacer_test.go`, `unit`)
- ❌ (`src/runtime/mgcpacer_test.go`, `oscillate`)
- ❌ (`src/runtime/mgcpacer_test.go`, `ramp`)
- ❌ (`src/runtime/mgcpacer_test.go`, `random`)
- ❌ (`src/runtime/mgcpacer_test.go`, `delay`)
- ❌ (`src/runtime/mgcpacer_test.go`, `scale`)
- ❌ (`src/runtime/mgcpacer_test.go`, `offset`)
- ❌ (`src/runtime/mgcpacer_test.go`, `sum`)
- ❌ (`src/runtime/mgcpacer_test.go`, `quantize`)
- ❌ (`src/runtime/mgcpacer_test.go`, `min`)
- ❌ (`src/runtime/mgcpacer_test.go`, `max`)
- ❌ (`src/runtime/mgcpacer_test.go`, `limit`)
- ❌ (`src/runtime/export_test.go`, `NewGCController`)
- ❌ (`src/runtime/export_test.go`, `StartCycle`)
- ❌ (`src/runtime/export_test.go`, `AssistWorkPerByte`)
- ❌ (`src/runtime/export_test.go`, `HeapGoal`)
- ❌ (`src/runtime/export_test.go`, `HeapLive`)
- ❌ (`src/runtime/export_test.go`, `HeapMarked`)
- ❌ (`src/runtime/export_test.go`, `Revise`)
- ❌ (`src/runtime/export_test.go`, `EndCycle`)

### 📊 Proposal #44196

#### File Embeddings - Directory Level
- ❌ `src/time`

#### File Embeddings - File Level
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/time`

#### Function Embeddings - File Level
- ✅ `src/time/time.go`
- ✅ `src/time/time_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/time/time.go`, `UnixMilli`)
- ❌ (`src/time/time.go`, `UnixMicro`)
- ✅ (`src/time/time.go`, `UnixMilli`)
- ❌ (`src/time/time.go`, `UnixMicro`)
- ❌ (`src/time/time_test.go`, `TestUnixMilli`)
- ❌ (`src/time/time_test.go`, `TestUnixMicro`)
- ❌ (`src/time/time_test.go`, `BenchmarkNowUnixMilli`)
- ❌ (`src/time/time_test.go`, `BenchmarkNowUnixMicro`)

### 📊 Proposal #44221

#### File Embeddings - Directory Level
- ✅ `src/encoding/csv`

#### File Embeddings - File Level
- ❌ `src/encoding/csv/reader.go`
- ❌ `src/encoding/csv/reader_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/encoding/csv`

#### Function Embeddings - File Level
- ✅ `src/encoding/csv/reader.go`
- ❌ `src/encoding/csv/reader_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/encoding/csv/reader.go`, `FieldPos`)
- ✅ (`src/encoding/csv/reader.go`, `readLine`)
- ❌ (`src/encoding/csv/reader.go`, `nextRune`)
- ✅ (`src/encoding/csv/reader.go`, `readRecord`)
- ❌ (`src/encoding/csv/reader_test.go`, `TestRead`)
- ❌ (`src/encoding/csv/reader_test.go`, `firstError`)
- ❌ (`src/encoding/csv/reader_test.go`, `errorWithPosition`)
- ❌ (`src/encoding/csv/reader_test.go`, `makePositions`)
- ❌ (`src/encoding/csv/reader.go`, `FieldPos`)
- ✅ (`src/encoding/csv/reader.go`, `readLine`)
- ❌ (`src/encoding/csv/reader.go`, `nextRune`)
- ✅ (`src/encoding/csv/reader.go`, `readRecord`)
- ❌ (`src/encoding/csv/reader_test.go`, `TestRead`)
- ❌ (`src/encoding/csv/reader_test.go`, `firstError`)
- ❌ (`src/encoding/csv/reader_test.go`, `errorWithPosition`)
- ❌ (`src/encoding/csv/reader_test.go`, `makePositions`)

### 📊 Proposal #44435

#### File Embeddings - Directory Level
- ✅ `src/cmd/go/internal/modcmd`
- ✅ `src/cmd/go/internal/modload`

#### File Embeddings - File Level
- ✅ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/go/internal/modcmd`
- ✅ `src/cmd/go/internal/modload`

#### Function Embeddings - File Level
- ✅ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/modcmd/download.go`, `runDownload`)
- ❌ (`src/cmd/go/internal/modload/modfile.go`, `pruningForGoVersion`)

### 📊 Proposal #44505

#### File Embeddings - Directory Level
- ❌ `src/cmd/asm/internal/lex`
- ✅ `src/cmd/dist`
- ❌ `src/sort`

#### File Embeddings - File Level
- ❌ `src/cmd/asm/internal/lex/tokenizer.go`
- ❌ `src/cmd/dist/build.go`
- ✅ `src/cmd/dist/buildtool.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/dist/util.go`
- ❌ `src/sort/slice.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/asm/internal/lex`
- ✅ `src/cmd/dist`
- ❌ `src/sort`

#### Function Embeddings - File Level
- ❌ `src/cmd/asm/internal/lex/tokenizer.go`
- ✅ `src/cmd/dist/build.go`
- ✅ `src/cmd/dist/buildtool.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/dist/util.go`
- ❌ `src/sort/slice.go`

#### Function Embeddings - Function Level
- ✅ (`src/cmd/dist/buildtool.go`, `bootstrapBuildTools`)
- ❌ (`src/cmd/dist/build.go`, `findgoversion`)
- ❌ (`src/cmd/dist/build.go`, `cmdbootstrap`)
- ❌ (`src/cmd/dist/test.go`, `makeGOROOTUnwritable`)
- ❌ (`src/cmd/dist/util.go`, `run`)
- ❌ (`src/sort/slice.go`, `Slice`)
- ❌ (`src/sort/slice.go`, `SliceStable`)
- ❌ (`src/sort/slice.go`, `SliceIsSorted`)
- ✅ (`src/cmd/dist/buildtool.go`, `bootstrapBuildTools`)
- ✅ (`src/cmd/dist/buildtool.go`, `bootstrapBuildTools`)
- ✅ (`src/cmd/dist/buildtool.go`, `bootstrapBuildTools`)
- ❌ (`src/cmd/asm/internal/lex/tokenizer.go`, `Next`)

### 📊 Proposal #44808

#### File Embeddings - Directory Level
- ❌ `src/image`
- ✅ `src/image/draw`

#### File Embeddings - File Level
- ✅ `src/image/draw/draw.go`
- ✅ `src/image/draw/draw_test.go`
- ❌ `src/image/geom.go`
- ❌ `src/image/image.go`
- ❌ `src/image/image_test.go`
- ❌ `src/image/names.go`
- ❌ `src/image/ycbcr.go`

#### Function Embeddings - Directory Level
- ❌ `src/image`
- ✅ `src/image/draw`

#### Function Embeddings - File Level
- ❌ `src/image/draw/draw.go`
- ✅ `src/image/draw/draw_test.go`
- ❌ `src/image/geom.go`
- ❌ `src/image/image.go`
- ❌ `src/image/image_test.go`
- ❌ `src/image/names.go`
- ❌ `src/image/ycbcr.go`

#### Function Embeddings - Function Level
- ❌ (`src/image/image_test.go`, `TestRGBA64Image`)
- ❌ (`src/image/ycbcr.go`, `RGBA64At`)
- ❌ (`src/image/ycbcr.go`, `RGBA64At`)
- ❌ (`src/image/image.go`, `RGBA64At`)
- ❌ (`src/image/image.go`, `SetRGBA64`)
- ❌ (`src/image/image.go`, `RGBA64At`)
- ❌ (`src/image/image.go`, `SetRGBA64`)
- ❌ (`src/image/image.go`, `RGBA64At`)
- ❌ (`src/image/image.go`, `SetRGBA64`)
- ❌ (`src/image/image.go`, `RGBA64At`)
- ❌ (`src/image/image.go`, `SetRGBA64`)
- ❌ (`src/image/image.go`, `RGBA64At`)
- ❌ (`src/image/image.go`, `SetRGBA64`)
- ❌ (`src/image/image.go`, `RGBA64At`)
- ❌ (`src/image/image.go`, `SetRGBA64`)
- ❌ (`src/image/image.go`, `RGBA64At`)
- ❌ (`src/image/image.go`, `SetRGBA64`)
- ❌ (`src/image/image.go`, `RGBA64At`)
- ❌ (`src/image/image.go`, `SetRGBA64`)
- ❌ (`src/image/image.go`, `RGBA64At`)
- ❌ (`src/image/image.go`, `SetRGBA64`)
- ❌ (`src/image/geom.go`, `RGBA64At`)
- ❌ (`src/image/image_test.go`, `TestRGBA64Image`)
- ❌ (`src/image/names.go`, `RGBA64At`)
- ❌ (`src/image/draw/draw_test.go`, `At`)
- ❌ (`src/image/draw/draw_test.go`, `RGBA64At`)
- ❌ (`src/image/draw/draw_test.go`, `Set`)
- ❌ (`src/image/draw/draw_test.go`, `PixOffset`)
- ❌ (`src/image/draw/draw_test.go`, `init`)
- ❌ (`src/image/draw/draw_test.go`, `At`)
- ❌ (`src/image/draw/draw_test.go`, `RGBA64At`)
- ❌ (`src/image/draw/draw_test.go`, `Set`)
- ❌ (`src/image/draw/draw_test.go`, `SetRGBA64`)
- ❌ (`src/image/draw/draw_test.go`, `PixOffset`)
- ❌ (`src/image/draw/draw_test.go`, `init`)
- ❌ (`src/image/draw/draw_test.go`, `TestDraw`)
- ❌ (`src/image/draw/draw.go`, `DrawMask`)
- ❌ (`src/image/draw/draw_test.go`, `convertToSlowestRGBA`)
- ✅ (`src/image/draw/draw_test.go`, `convertToSlowerRGBA`)
- ❌ (`src/image/draw/draw_test.go`, `makeGolden`)
- ❌ (`src/image/draw/draw_test.go`, `TestDraw`)
- ❌ (`src/image/draw/draw.go`, `DrawMask`)
- ❌ (`src/image/draw/draw.go`, `drawRGBA`)

### 📊 Proposal #44815

#### File Embeddings - Directory Level
- ✅ `src/bufio`

#### File Embeddings - File Level
- ✅ `src/bufio/bufio.go`
- ❌ `src/bufio/bufio_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/bufio`

#### Function Embeddings - File Level
- ✅ `src/bufio/bufio.go`
- ❌ `src/bufio/bufio_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/bufio/bufio_test.go`, `Write`)
- ❌ (`src/bufio/bufio_test.go`, `ReadFrom`)
- ❌ (`src/bufio/bufio_test.go`, `TestWriterReadFromWithBufferedData`)
- ✅ (`src/bufio/bufio.go`, `ReadFrom`)

### 📊 Proposal #44853

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/pkginit`
- ❌ `src/cmd/compile/internal/reflectdata`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/link/internal/ld`
- ✅ `src/runtime`
- ❌ `src/syscall`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/gc/obj.go`
- ❌ `src/cmd/compile/internal/noder/import.go`
- ❌ `src/cmd/compile/internal/noder/reader.go`
- ❌ `src/cmd/compile/internal/pkginit/initAsanGlobals.go`
- ❌ `src/cmd/compile/internal/reflectdata/reflect.go`
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/init.go`
- ❌ `src/cmd/link/internal/ld/config.go`
- ❌ `src/cmd/link/internal/ld/lib.go`
- ❌ `src/runtime/asan.go`
- ❌ `src/runtime/cgo_sigaction.go`
- ❌ `src/runtime/iface.go`
- ❌ `src/runtime/malloc.go`
- ❌ `src/runtime/mbarrier.go`
- ❌ `src/runtime/mgcsweep.go`
- ❌ `src/runtime/mheap.go`
- ❌ `src/runtime/mprof.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/select.go`
- ❌ `src/runtime/slice.go`
- ❌ `src/runtime/stack.go`
- ❌ `src/runtime/string.go`
- ❌ `src/runtime/traceback.go`
- ❌ `src/syscall/syscall_unix.go`
- ❌ `src/syscall/syscall_windows.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/pkginit`
- ❌ `src/cmd/compile/internal/reflectdata`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/link/internal/ld`
- ✅ `src/runtime`
- ❌ `src/syscall`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/gc/obj.go`
- ❌ `src/cmd/compile/internal/noder/import.go`
- ❌ `src/cmd/compile/internal/noder/reader.go`
- ❌ `src/cmd/compile/internal/pkginit/initAsanGlobals.go`
- ❌ `src/cmd/compile/internal/reflectdata/reflect.go`
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/init.go`
- ❌ `src/cmd/link/internal/ld/config.go`
- ❌ `src/cmd/link/internal/ld/lib.go`
- ❌ `src/runtime/asan.go`
- ✅ `src/runtime/cgo_sigaction.go`
- ❌ `src/runtime/iface.go`
- ❌ `src/runtime/malloc.go`
- ❌ `src/runtime/mbarrier.go`
- ❌ `src/runtime/mgcsweep.go`
- ❌ `src/runtime/mheap.go`
- ❌ `src/runtime/mprof.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/select.go`
- ❌ `src/runtime/slice.go`
- ❌ `src/runtime/stack.go`
- ❌ `src/runtime/string.go`
- ❌ `src/runtime/traceback.go`
- ❌ `src/syscall/syscall_unix.go`
- ❌ `src/syscall/syscall_windows.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/link/internal/ld/lib.go`, `libinit`)
- ❌ (`src/cmd/link/internal/ld/lib.go`, `loadlib`)
- ❌ (`src/cmd/link/internal/ld/config.go`, `mustLinkExternal`)
- ❌ (`src/cmd/compile/internal/gc/main.go`, `Main`)
- ❌ (`src/cmd/compile/internal/noder/import.go`, `openPackage`)
- ❌ (`src/cmd/compile/internal/reflectdata/reflect.go`, `WriteBasicTypes`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `InitConfig`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `instrumentFields`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `instrument2`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `exprCheckPtr`)
- ❌ (`src/cmd/compile/internal/base/flag.go`, `ParseFlags`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `LinkerDeps`)
- ❌ (`src/cmd/go/go_test.go`, `TestMain`)
- ❌ (`src/cmd/go/internal/work/init.go`, `instrumentInit`)
- ❌ (`src/cmd/go/internal/work/build.go`, `AddBuildFlags`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `cgo`)
- ❌ (`src/runtime/asan.go`, `ASanRead`)
- ❌ (`src/runtime/asan.go`, `ASanWrite`)
- ❌ (`src/runtime/asan.go`, `asanread`)
- ❌ (`src/runtime/asan.go`, `asanwrite`)
- ❌ (`src/runtime/asan.go`, `asanunpoison`)
- ❌ (`src/runtime/asan.go`, `asanpoison`)
- ❌ (`src/runtime/malloc.go`, `mallocgc`)
- ❌ (`src/runtime/select.go`, `selectgo`)
- ❌ (`src/runtime/iface.go`, `convT`)
- ❌ (`src/runtime/iface.go`, `convTnoptr`)
- ❌ (`src/runtime/mgcsweep.go`, `sweep`)
- ✅ (`src/runtime/cgo_sigaction.go`, `sigaction`)
- ❌ (`src/runtime/traceback.go`, `callCgoSymbolizer`)
- ❌ (`src/runtime/traceback.go`, `cgoContextPCs`)
- ❌ (`src/syscall/syscall_windows.go`, `Read`)
- ❌ (`src/syscall/syscall_windows.go`, `Write`)
- ❌ (`src/runtime/stack.go`, `stackalloc`)
- ❌ (`src/runtime/stack.go`, `stackfree`)
- ❌ (`src/runtime/mbarrier.go`, `reflect_typedmemmove`)
- ❌ (`src/runtime/mbarrier.go`, `typedslicecopy`)
- ❌ (`src/runtime/proc.go`, `newm1`)
- ❌ (`src/runtime/proc.go`, `gfget`)
- ❌ (`src/runtime/slice.go`, `makeslicecopy`)
- ❌ (`src/runtime/slice.go`, `growslice`)
- ❌ (`src/runtime/slice.go`, `slicecopy`)
- ❌ (`src/runtime/mheap.go`, `freeSpan`)
- ❌ (`src/runtime/mprof.go`, `BlockProfile`)
- ❌ (`src/runtime/string.go`, `slicebytetostring`)
- ❌ (`src/runtime/string.go`, `slicebytetostringtmp`)
- ❌ (`src/runtime/string.go`, `slicerunetostring`)
- ❌ (`src/syscall/syscall_unix.go`, `Read`)
- ❌ (`src/syscall/syscall_unix.go`, `Write`)
- ❌ (`src/cmd/go/internal/work/init.go`, `instrumentInit`)
- ❌ (`src/cmd/go/internal/work/init.go`, `compilerRequiredAsanVersion`)
- ❌ (`src/cmd/compile/internal/pkginit/initAsanGlobals.go`, `instrumentGlobals`)
- ❌ (`src/cmd/compile/internal/pkginit/initAsanGlobals.go`, `createtypes`)
- ❌ (`src/cmd/compile/internal/pkginit/initAsanGlobals.go`, `GetRedzoneSizeForGlobal`)
- ❌ (`src/cmd/compile/internal/pkginit/initAsanGlobals.go`, `canInstrumentGlobal`)
- ❌ (`src/runtime/asan.go`, `asanregisterglobals`)
- ❌ (`src/cmd/compile/internal/noder/reader.go`, `objIdx`)
- ❌ (`src/cmd/compile/internal/gc/obj.go`, `ggloblnod`)

### 📊 Proposal #44940

#### File Embeddings - Directory Level
- ✅ `src/unicode/utf16`

#### File Embeddings - File Level
- ❌ `src/unicode/utf16/utf16.go`
- ✅ `src/unicode/utf16/utf16_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/unicode/utf16`

#### Function Embeddings - File Level
- ✅ `src/unicode/utf16/utf16.go`
- ❌ `src/unicode/utf16/utf16_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/unicode/utf16/utf16_test.go`, `TestRuneLen`)
- ✅ (`src/unicode/utf16/utf16.go`, `RuneLen`)
- ❌ (`src/unicode/utf16/utf16_test.go`, `TestRuneLen`)
- ✅ (`src/unicode/utf16/utf16.go`, `RuneLen`)
- ❌ (`src/unicode/utf16/utf16.go`, `Encode`)

### 📊 Proposal #45033

#### File Embeddings - Directory Level
- ✅ `src/strconv`

#### File Embeddings - File Level
- ❌ `src/strconv/bytealg.go`
- ❌ `src/strconv/bytealg_bootstrap.go`
- ✅ `src/strconv/quote.go`
- ❌ `src/strconv/quote_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/strconv`

#### Function Embeddings - File Level
- ❌ `src/strconv/bytealg.go`
- ❌ `src/strconv/bytealg_bootstrap.go`
- ✅ `src/strconv/quote.go`
- ✅ `src/strconv/quote_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/strconv/quote.go`, `contains`)
- ✅ (`src/strconv/quote.go`, `QuotedPrefix`)
- ✅ (`src/strconv/quote.go`, `Unquote`)
- ✅ (`src/strconv/quote.go`, `unquote`)
- ❌ (`src/strconv/bytealg.go`, `index`)
- ❌ (`src/strconv/bytealg_bootstrap.go`, `index`)
- ❌ (`src/strconv/quote_test.go`, `TestUnquote`)
- ❌ (`src/strconv/quote_test.go`, `TestUnquoteInvalidUTF8`)
- ✅ (`src/strconv/quote_test.go`, `testUnquote`)

### 📊 Proposal #45100

#### File Embeddings - Directory Level
- ❌ `src/net/url`

#### File Embeddings - File Level
- ❌ `src/net/url/url.go`
- ❌ `src/net/url/url_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/net/url`

#### Function Embeddings - File Level
- ❌ `src/net/url/url.go`
- ❌ `src/net/url/url_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/url/url.go`, `Has`)
- ❌ (`src/net/url/url_test.go`, `TestQueryValues`)

### 📊 Proposal #45428

#### File Embeddings - Directory Level
- ✅ `src/crypto/tls`

#### File Embeddings - File Level
- ❌ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/handshake_server_tls13.go`
- ❌ `src/crypto/tls/handshake_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/tls`

#### Function Embeddings - File Level
- ❌ `src/crypto/tls/common.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/handshake_server_tls13.go`
- ❌ `src/crypto/tls/handshake_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/tls/handshake_test.go`, `runMain`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestVersion`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `testCrossVersionResume`)
- ❌ (`src/crypto/tls/common.go`, `cipherSuites`)
- ❌ (`src/crypto/tls/common.go`, `supportedVersions`)
- ❌ (`src/crypto/tls/common.go`, `maxSupportedVersion`)
- ❌ (`src/crypto/tls/common.go`, `mutualVersion`)
- ❌ (`src/crypto/tls/common.go`, `SupportsCertificate`)
- ❌ (`src/crypto/tls/handshake_server.go`, `readClientHello`)
- ❌ (`src/crypto/tls/handshake_server.go`, `processClientHello`)
- ❌ (`src/crypto/tls/handshake_server.go`, `pickCipherSuite`)
- ❌ (`src/crypto/tls/handshake_server_tls13.go`, `processClientHello`)
- ❌ (`src/crypto/tls/handshake_client.go`, `makeClientHello`)
- ❌ (`src/crypto/tls/handshake_client.go`, `clientHandshake`)
- ❌ (`src/crypto/tls/handshake_client.go`, `pickTLSVersion`)

### 📊 Proposal #45430

#### File Embeddings - Directory Level
- ✅ `src/crypto/tls`

#### File Embeddings - File Level
- ✅ `src/crypto/tls/cipher_suites.go`
- ❌ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ✅ `src/crypto/tls/handshake_server_tls13.go`
- ❌ `src/crypto/tls/handshake_test.go`
- ❌ `src/crypto/tls/tls_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/tls`

#### Function Embeddings - File Level
- ✅ `src/crypto/tls/cipher_suites.go`
- ❌ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ✅ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/handshake_server_tls13.go`
- ❌ `src/crypto/tls/handshake_test.go`
- ✅ `src/crypto/tls/tls_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/tls/cipher_suites.go`, `CipherSuites`)
- ✅ (`src/crypto/tls/cipher_suites.go`, `InsecureCipherSuites`)
- ❌ (`src/crypto/tls/cipher_suites.go`, `selectCipherSuite`)
- ❌ (`src/crypto/tls/common.go`, `cipherSuites`)
- ❌ (`src/crypto/tls/common.go`, `unexpectedMessageError`)
- ❌ (`src/crypto/tls/common.go`, `isSupportedSignatureAlgorithm`)
- ✅ (`src/crypto/tls/handshake_server_test.go`, `TestCipherSuitePreference`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestServerResumption`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestHandshakeServerExportKeyingMaterial`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestHandshakeServerRSAPSS`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestAESCipherReordering`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestAESCipherReorderingTLS13`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestServerHandshakeContextCancellation`)
- ❌ (`src/crypto/tls/handshake_client.go`, `makeClientHello`)
- ❌ (`src/crypto/tls/handshake_server.go`, `pickCipherSuite`)
- ❌ (`src/crypto/tls/handshake_server_tls13.go`, `processClientHello`)
- ❌ (`src/crypto/tls/handshake_test.go`, `runMain`)
- ✅ (`src/crypto/tls/tls_test.go`, `TestCipherSuites`)
- ❌ (`src/crypto/tls/tls_test.go`, `http2isBadCipher`)

### 📊 Proposal #45435

#### File Embeddings - Directory Level
- ✅ `src/sync`

#### File Embeddings - File Level
- ✅ `src/sync/mutex.go`
- ❌ `src/sync/mutex_test.go`
- ❌ `src/sync/rwmutex.go`
- ❌ `src/sync/rwmutex_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/sync`

#### Function Embeddings - File Level
- ✅ `src/sync/mutex.go`
- ❌ `src/sync/mutex_test.go`
- ❌ `src/sync/rwmutex.go`
- ✅ `src/sync/rwmutex_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/sync/rwmutex_test.go`, `TestRWMutex`)
- ❌ (`src/sync/mutex_test.go`, `HammerMutex`)
- ❌ (`src/sync/mutex_test.go`, `TestMutex`)
- ❌ (`src/sync/rwmutex.go`, `TryRLock`)
- ❌ (`src/sync/rwmutex.go`, `TryLock`)
- ✅ (`src/sync/mutex.go`, `TryLock`)

### 📊 Proposal #45453

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/amd64`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/internal/buildcfg`
- ❌ `test/codegen`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/amd64/ssa.go`
- ❌ `src/cmd/compile/internal/amd64/versions_test.go`
- ❌ `src/cmd/compile/internal/ssa/rewriteAMD64.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/buildruntime.go`
- ❌ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/internal/buildcfg/cfg.go`
- ❌ `src/internal/buildcfg/cfg_test.go`
- ❌ `test/codegen/bmi.go`
- ❌ `test/codegen/mathbits.go`
- ❌ `test/codegen/memcombine.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/amd64`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/dist`
- ✅ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/go/internal/work`
- ✅ `src/internal/buildcfg`
- ❌ `test/codegen`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/amd64/ssa.go`
- ❌ `src/cmd/compile/internal/amd64/versions_test.go`
- ❌ `src/cmd/compile/internal/ssa/rewriteAMD64.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/buildruntime.go`
- ✅ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ✅ `src/internal/buildcfg/cfg.go`
- ❌ `src/internal/buildcfg/cfg_test.go`
- ❌ `test/codegen/bmi.go`
- ❌ `test/codegen/mathbits.go`
- ❌ `test/codegen/memcombine.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/cfg/cfg.go`, `GetArchEnv`)
- ❌ (`src/internal/buildcfg/cfg.go`, `goamd64`)
- ❌ (`src/cmd/dist/buildruntime.go`, `mkbuildcfg`)
- ❌ (`src/internal/buildcfg/cfg_test.go`, `TestConfigFlags`)
- ❌ (`src/cmd/dist/build.go`, `xinit`)
- ❌ (`src/cmd/dist/build.go`, `cmdenv`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `asmArgs`)
- ❌ (`test/codegen/bmi.go`, `andn64`)
- ❌ (`test/codegen/bmi.go`, `andn32`)
- ❌ (`test/codegen/bmi.go`, `blsi64`)
- ❌ (`test/codegen/bmi.go`, `blsi32`)
- ❌ (`test/codegen/bmi.go`, `blsmsk64`)
- ❌ (`test/codegen/bmi.go`, `blsmsk32`)
- ❌ (`test/codegen/bmi.go`, `blsr64`)
- ❌ (`test/codegen/bmi.go`, `blsr32`)
- ❌ (`src/cmd/compile/internal/amd64/ssa.go`, `ssaGenValue`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64ANDL`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64ANDNL`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64ANDNQ`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64ANDQ`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64XORL`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64XORQ`)
- ❌ (`src/cmd/compile/internal/amd64/ssa.go`, `ssaGenValue`)
- ❌ (`test/codegen/mathbits.go`, `TrailingZeros`)
- ❌ (`test/codegen/mathbits.go`, `TrailingZeros64`)
- ❌ (`test/codegen/mathbits.go`, `TrailingZeros32`)
- ❌ (`test/codegen/mathbits.go`, `IterateBits`)
- ❌ (`test/codegen/mathbits.go`, `IterateBits64`)
- ❌ (`test/codegen/mathbits.go`, `IterateBits32`)
- ❌ (`test/codegen/mathbits.go`, `IterateBits16`)
- ❌ (`test/codegen/mathbits.go`, `IterateBits8`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpCtz16NonZero`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpCtz32`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpCtz32NonZero`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpCtz64`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpCtz64NonZero`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpCtz8NonZero`)
- ❌ (`src/cmd/compile/internal/amd64/ssa.go`, `ssaGenValue`)
- ❌ (`test/codegen/memcombine.go`, `load_be64`)
- ❌ (`test/codegen/memcombine.go`, `load_be64_idx`)
- ❌ (`test/codegen/memcombine.go`, `load_be32`)
- ❌ (`test/codegen/memcombine.go`, `load_be32_idx`)
- ❌ (`test/codegen/memcombine.go`, `load_be_byte4_uint32_inv`)
- ❌ (`test/codegen/memcombine.go`, `load_be_byte8_uint64`)
- ❌ (`test/codegen/memcombine.go`, `load_be_byte8_uint64_inv`)
- ❌ (`test/codegen/memcombine.go`, `store_le16_idx`)
- ❌ (`test/codegen/memcombine.go`, `store_be64`)
- ❌ (`test/codegen/memcombine.go`, `store_be64_idx`)
- ❌ (`test/codegen/memcombine.go`, `store_be32`)
- ❌ (`test/codegen/memcombine.go`, `store_be32_idx`)
- ❌ (`test/codegen/memcombine.go`, `store_be_byte_2`)
- ❌ (`test/codegen/memcombine.go`, `store_be_byte_4`)
- ❌ (`test/codegen/memcombine.go`, `store_be_byte_8`)
- ❌ (`src/cmd/compile/internal/amd64/versions_test.go`, `TestGoAMD64v1`)
- ❌ (`src/cmd/compile/internal/amd64/versions_test.go`, `setOf`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64BSWAPL`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64BSWAPQ`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64MOVBELstore`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64MOVBEQstore`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64MOVLstore`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64MOVQstore`)
- ❌ (`src/cmd/compile/internal/ssa/rewriteAMD64.go`, `rewriteValueAMD64_OpAMD64ORQ`)

### 📊 Proposal #45454

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/cfg`
- ✅ `src/go/build`
- ✅ `src/internal/buildcfg`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/cfg/cfg.go`
- ✅ `src/go/build/build.go`
- ✅ `src/internal/buildcfg/cfg.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/go/internal/cfg`
- ✅ `src/go/build`
- ❌ `src/internal/buildcfg`

#### Function Embeddings - File Level
- ✅ `src/cmd/go/internal/cfg/cfg.go`
- ✅ `src/go/build/build.go`
- ❌ `src/internal/buildcfg/cfg.go`

#### Function Embeddings - Function Level
- ✅ (`src/cmd/go/internal/cfg/cfg.go`, `defaultContext`)
- ❌ (`src/internal/buildcfg/cfg.go`, `toolTags`)
- ❌ (`src/internal/buildcfg/cfg.go`, `experimentTags`)
- ❌ (`src/internal/buildcfg/cfg.go`, `gogoarchTags`)
- ✅ (`src/go/build/build.go`, `defaultContext`)
- ❌ (`src/cmd/go/internal/cfg/cfg.go`, `init`)

### 📊 Proposal #45460

#### File Embeddings - Directory Level
- ❌ `src/net/http`

#### File Embeddings - File Level
- ❌ `src/net/http/transport.go`

#### Function Embeddings - Directory Level
- ❌ `src/net/http`

#### Function Embeddings - File Level
- ❌ `src/net/http/transport.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/http/transport.go`, `dialConn`)

### 📊 Proposal #45628

#### File Embeddings - Directory Level
- ❌ `src/encoding/xml`

#### File Embeddings - File Level
- ❌ `src/encoding/xml/xml.go`
- ❌ `src/encoding/xml/xml_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/encoding/xml`

#### Function Embeddings - File Level
- ❌ `src/encoding/xml/xml.go`
- ✅ `src/encoding/xml/xml_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/encoding/xml/xml_test.go`, `TestInputLinePos`)
- ❌ (`src/encoding/xml/xml.go`, `getc`)
- ❌ (`src/encoding/xml/xml.go`, `InputPos`)

### 📊 Proposal #45754

#### File Embeddings - Directory Level
- ✅ `src/flag`

#### File Embeddings - File Level
- ❌ `src/flag/example_textvar_test.go`
- ✅ `src/flag/flag.go`

#### Function Embeddings - Directory Level
- ✅ `src/flag`

#### Function Embeddings - File Level
- ❌ `src/flag/example_textvar_test.go`
- ✅ `src/flag/flag.go`

#### Function Embeddings - Function Level
- ❌ (`src/flag/example_textvar_test.go`, `ExampleTextVar`)
- ❌ (`src/flag/flag.go`, `newTextValue`)
- ❌ (`src/flag/flag.go`, `Set`)
- ❌ (`src/flag/flag.go`, `Get`)
- ❌ (`src/flag/flag.go`, `String`)
- ✅ (`src/flag/flag.go`, `TextVar`)
- ✅ (`src/flag/flag.go`, `TextVar`)

### 📊 Proposal #45899

#### File Embeddings - Directory Level
- ❌ `src/io`

#### File Embeddings - File Level
- ❌ `src/io/io.go`
- ❌ `src/io/io_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/io`

#### Function Embeddings - File Level
- ✅ `src/io/io.go`
- ❌ `src/io/io_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/io/io_test.go`, `TestOffsetWriter_Seek`)
- ❌ (`src/io/io_test.go`, `TestOffsetWriter_WriteAt`)
- ❌ (`src/io/io_test.go`, `TestOffsetWriter_Write`)
- ❌ (`src/io/io.go`, `NewOffsetWriter`)
- ❌ (`src/io/io.go`, `Write`)
- ❌ (`src/io/io.go`, `WriteAt`)
- ❌ (`src/io/io.go`, `Seek`)

### 📊 Proposal #45963

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/test`
- ❌ `src/cmd/go/internal/work`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/test/testflag.go`
- ❌ `src/cmd/go/internal/work/exec.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/test`
- ❌ `src/cmd/go/internal/work`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/test/testflag.go`
- ❌ `src/cmd/go/internal/work/exec.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/work/exec.go`, `buildVetConfig`)
- ❌ (`src/cmd/go/internal/test/testflag.go`, `String`)
- ❌ (`src/cmd/go/internal/test/testflag.go`, `Set`)

### 📊 Proposal #45964

#### File Embeddings - Directory Level
- ❌ `src/syscall`

#### File Embeddings - File Level
- ❌ `src/syscall/exec_linux.go`
- ❌ `src/syscall/syscall_linux.go`
- ❌ `src/syscall/syscall_linux_amd64.go`
- ❌ `src/syscall/syscall_linux_arm.go`
- ❌ `src/syscall/syscall_linux_mips64x.go`
- ❌ `src/syscall/syscall_linux_mipsx.go`
- ❌ `src/syscall/syscall_linux_ppc64x.go`
- ❌ `src/syscall/syscall_linux_riscv64.go`
- ❌ `src/syscall/syscall_linux_s390x.go`
- ❌ `src/syscall/zsyscall_linux_386.go`
- ❌ `src/syscall/zsyscall_linux_amd64.go`
- ❌ `src/syscall/zsyscall_linux_arm.go`
- ❌ `src/syscall/zsyscall_linux_arm64.go`
- ❌ `src/syscall/zsyscall_linux_mips.go`
- ❌ `src/syscall/zsyscall_linux_mips64.go`
- ❌ `src/syscall/zsyscall_linux_mips64le.go`
- ❌ `src/syscall/zsyscall_linux_mipsle.go`
- ❌ `src/syscall/zsyscall_linux_ppc64.go`
- ❌ `src/syscall/zsyscall_linux_ppc64le.go`
- ❌ `src/syscall/zsyscall_linux_riscv64.go`
- ❌ `src/syscall/zsyscall_linux_s390x.go`

#### Function Embeddings - Directory Level
- ❌ `src/syscall`

#### Function Embeddings - File Level
- ❌ `src/syscall/exec_linux.go`
- ❌ `src/syscall/syscall_linux.go`
- ❌ `src/syscall/syscall_linux_amd64.go`
- ❌ `src/syscall/syscall_linux_arm.go`
- ❌ `src/syscall/syscall_linux_mips64x.go`
- ❌ `src/syscall/syscall_linux_mipsx.go`
- ❌ `src/syscall/syscall_linux_ppc64x.go`
- ❌ `src/syscall/syscall_linux_riscv64.go`
- ❌ `src/syscall/syscall_linux_s390x.go`
- ❌ `src/syscall/zsyscall_linux_386.go`
- ❌ `src/syscall/zsyscall_linux_amd64.go`
- ❌ `src/syscall/zsyscall_linux_arm.go`
- ❌ `src/syscall/zsyscall_linux_arm64.go`
- ❌ `src/syscall/zsyscall_linux_mips.go`
- ❌ `src/syscall/zsyscall_linux_mips64.go`
- ❌ `src/syscall/zsyscall_linux_mips64le.go`
- ❌ `src/syscall/zsyscall_linux_mipsle.go`
- ❌ `src/syscall/zsyscall_linux_ppc64.go`
- ❌ `src/syscall/zsyscall_linux_ppc64le.go`
- ❌ `src/syscall/zsyscall_linux_riscv64.go`
- ❌ `src/syscall/zsyscall_linux_s390x.go`

#### Function Embeddings - Function Level
- ❌ (`src/syscall/exec_linux.go`, `formatIDMappings`)
- ❌ (`src/syscall/exec_linux.go`, `writeIDMappings`)
- ❌ (`src/syscall/syscall_linux.go`, `UtimesNano`)
- ❌ (`src/syscall/syscall_linux.go`, `Futimesat`)
- ❌ (`src/syscall/syscall_linux.go`, `Futimes`)
- ❌ (`src/syscall/syscall_linux.go`, `Accept`)
- ❌ (`src/syscall/exec_linux.go`, `forkAndExecInChild1`)
- ❌ (`src/syscall/zsyscall_linux_arm.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_arm.go`, `Munlockall`)
- ❌ (`src/syscall/zsyscall_linux_ppc64.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_ppc64.go`, `utimes`)
- ❌ (`src/syscall/zsyscall_linux_mips64le.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_mips64le.go`, `utimes`)
- ❌ (`src/syscall/syscall_linux_riscv64.go`, `SetLen`)
- ❌ (`src/syscall/syscall_linux_riscv64.go`, `SetControllen`)
- ❌ (`src/syscall/syscall_linux_riscv64.go`, `SetLen`)
- ❌ (`src/syscall/syscall_linux_riscv64.go`, `InotifyInit`)
- ❌ (`src/syscall/zsyscall_linux_amd64.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_amd64.go`, `utimes`)
- ❌ (`src/syscall/syscall_linux_mips64x.go`, `Ioperm`)
- ❌ (`src/syscall/syscall_linux_mips64x.go`, `Iopl`)
- ❌ (`src/syscall/zsyscall_linux_mips.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_mips.go`, `EpollWait`)
- ❌ (`src/syscall/zsyscall_linux_mips.go`, `mmap2`)
- ❌ (`src/syscall/syscall_linux_s390x.go`, `mmap`)
- ❌ (`src/syscall/zsyscall_linux_riscv64.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_riscv64.go`, `Gettimeofday`)
- ❌ (`src/syscall/zsyscall_linux_arm64.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_arm64.go`, `Gettimeofday`)
- ❌ (`src/syscall/zsyscall_linux_ppc64le.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_ppc64le.go`, `utimes`)
- ❌ (`src/syscall/syscall_linux.go`, `Pipe`)
- ❌ (`src/syscall/syscall_linux.go`, `Pipe2`)
- ❌ (`src/syscall/syscall_linux_arm.go`, `seek`)
- ❌ (`src/syscall/syscall_linux_arm.go`, `Seek`)
- ❌ (`src/syscall/zsyscall_linux_mips64.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_mips64.go`, `utimes`)
- ❌ (`src/syscall/syscall_linux_ppc64x.go`, `SetLen`)
- ❌ (`src/syscall/syscall_linux_ppc64x.go`, `SetControllen`)
- ❌ (`src/syscall/syscall_linux_ppc64x.go`, `SetLen`)
- ❌ (`src/syscall/syscall_linux_ppc64x.go`, `SyncFileRange`)
- ❌ (`src/syscall/zsyscall_linux_386.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_386.go`, `Munlockall`)
- ❌ (`src/syscall/zsyscall_linux_386.go`, `Dup2`)
- ❌ (`src/syscall/syscall_linux_mipsx.go`, `mmap`)
- ❌ (`src/syscall/zsyscall_linux_s390x.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_s390x.go`, `utimes`)
- ❌ (`src/syscall/syscall_linux_amd64.go`, `SetLen`)
- ❌ (`src/syscall/syscall_linux_amd64.go`, `SetControllen`)
- ❌ (`src/syscall/syscall_linux_amd64.go`, `SetLen`)
- ❌ (`src/syscall/zsyscall_linux_mipsle.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_linux_mipsle.go`, `EpollWait`)
- ❌ (`src/syscall/zsyscall_linux_mipsle.go`, `mmap2`)

### 📊 Proposal #45973

#### File Embeddings - Directory Level
- ✅ `src/net/http`

#### File Embeddings - File Level
- ❌ `src/net/http/serve_test.go`
- ❌ `src/net/http/server.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/http`

#### Function Embeddings - File Level
- ✅ `src/net/http/serve_test.go`
- ✅ `src/net/http/server.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/http/serve_test.go`, `TestQuerySemicolon`)
- ❌ (`src/net/http/serve_test.go`, `testQuerySemicolon`)
- ❌ (`src/net/http/server.go`, `ServeHTTP`)
- ✅ (`src/net/http/server.go`, `AllowQuerySemicolons`)

### 📊 Proposal #46057

#### File Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### File Embeddings - File Level
- ✅ `src/crypto/x509/cert_pool.go`
- ✅ `src/crypto/x509/cert_pool_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### Function Embeddings - File Level
- ✅ `src/crypto/x509/cert_pool.go`
- ✅ `src/crypto/x509/cert_pool_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/crypto/x509/cert_pool.go`, `Equal`)
- ✅ (`src/crypto/x509/cert_pool_test.go`, `TestCertPoolEqual`)

### 📊 Proposal #46059

#### File Embeddings - Directory Level
- ❌ `src/net/url`

#### File Embeddings - File Level
- ❌ `src/net/url/url.go`
- ❌ `src/net/url/url_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/net/url`

#### Function Embeddings - File Level
- ❌ `src/net/url/url.go`
- ❌ `src/net/url/url_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/url/url.go`, `parse`)
- ❌ (`src/net/url/url.go`, `String`)
- ❌ (`src/net/url/url_test.go`, `ufmt`)

### 📊 Proposal #46121

#### File Embeddings - Directory Level
- ❌ `src/html/template`

#### File Embeddings - File Level
- ❌ `src/html/template/template.go`

#### Function Embeddings - Directory Level
- ✅ `src/html/template`

#### Function Embeddings - File Level
- ✅ `src/html/template/template.go`

#### Function Embeddings - Function Level
- ❌ (`src/html/template/template.go`, `Funcs`)

### 📊 Proposal #46131

#### File Embeddings - Directory Level
- ❌ `src/reflect`

#### File Embeddings - File Level
- ❌ `src/reflect/all_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/reflect`

#### Function Embeddings - File Level
- ❌ `src/reflect/all_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/reflect/all_test.go`, `TestMapIterSet`)

### 📊 Proposal #46258

#### File Embeddings - Directory Level
- ✅ `src/syscall`

#### File Embeddings - File Level
- ❌ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/exec_pdeathsig_test.go`
- ❌ `src/syscall/syscall_freebsd_test.go`
- ❌ `src/syscall/syscall_linux_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/syscall`

#### Function Embeddings - File Level
- ❌ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/exec_pdeathsig_test.go`
- ❌ `src/syscall/syscall_freebsd_test.go`
- ❌ `src/syscall/syscall_linux_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/syscall/exec_freebsd.go`, `runtime_BeforeFork`)
- ❌ (`src/syscall/exec_freebsd.go`, `runtime_AfterFork`)
- ❌ (`src/syscall/exec_freebsd.go`, `runtime_AfterForkInChild`)
- ❌ (`src/syscall/exec_freebsd.go`, `forkAndExecInChild`)
- ❌ (`src/syscall/exec_freebsd.go`, `forkAndExecInChild`)
- ❌ (`src/syscall/syscall_linux_test.go`, `TestParseNetlinkMessage`)
- ❌ (`src/syscall/syscall_linux_test.go`, `TestSyscallNoError`)
- ❌ (`src/syscall/exec_pdeathsig_test.go`, `deathSignalParent`)
- ❌ (`src/syscall/exec_pdeathsig_test.go`, `deathSignalChild`)
- ❌ (`src/syscall/syscall_freebsd_test.go`, `TestMain`)

### 📊 Proposal #46259

#### File Embeddings - Directory Level
- ✅ `src/syscall`

#### File Embeddings - File Level
- ✅ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/exec_freebsd_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/syscall`

#### Function Embeddings - File Level
- ✅ `src/syscall/exec_freebsd.go`
- ✅ `src/syscall/exec_freebsd_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/syscall/exec_freebsd.go`, `runtime_BeforeFork`)
- ❌ (`src/syscall/exec_freebsd.go`, `runtime_AfterFork`)
- ❌ (`src/syscall/exec_freebsd.go`, `runtime_AfterForkInChild`)
- ✅ (`src/syscall/exec_freebsd.go`, `forkAndExecInChild`)
- ✅ (`src/syscall/exec_freebsd.go`, `forkAndExecInChild`)
- ❌ (`src/syscall/exec_freebsd_test.go`, `prepareJail`)
- ✅ (`src/syscall/exec_freebsd_test.go`, `TestJailAttach`)

### 📊 Proposal #46279

#### File Embeddings - Directory Level
- ❌ `src/cmd/link/internal/ld`

#### File Embeddings - File Level
- ❌ `src/cmd/link/internal/ld/ld_test.go`
- ❌ `src/cmd/link/internal/ld/lib.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/link/internal/ld`

#### Function Embeddings - File Level
- ❌ `src/cmd/link/internal/ld/ld_test.go`
- ❌ `src/cmd/link/internal/ld/lib.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/link/internal/ld/lib.go`, `linksetup`)
- ❌ (`src/cmd/link/internal/ld/ld_test.go`, `TestMemProfileCheck`)

### 📊 Proposal #46287

#### File Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ✅ `src/crypto/x509`
- ❌ `src/crypto/x509/internal/macos`
- ❌ `src/runtime`

#### File Embeddings - File Level
- ❌ `src/cmd/dist/test.go`
- ❌ `src/crypto/x509/cert_pool.go`
- ❌ `src/crypto/x509/hybrid_pool_test.go`
- ❌ `src/crypto/x509/internal/macos/corefoundation.go`
- ❌ `src/crypto/x509/internal/macos/security.go`
- ✅ `src/crypto/x509/root_darwin.go`
- ✅ `src/crypto/x509/root_windows.go`
- ❌ `src/crypto/x509/verify.go`
- ❌ `src/crypto/x509/verify_test.go`
- ❌ `src/crypto/x509/x509_test.go`
- ❌ `src/runtime/sys_darwin.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ✅ `src/crypto/x509`
- ❌ `src/crypto/x509/internal/macos`
- ❌ `src/runtime`

#### Function Embeddings - File Level
- ❌ `src/cmd/dist/test.go`
- ❌ `src/crypto/x509/cert_pool.go`
- ❌ `src/crypto/x509/hybrid_pool_test.go`
- ❌ `src/crypto/x509/internal/macos/corefoundation.go`
- ❌ `src/crypto/x509/internal/macos/security.go`
- ✅ `src/crypto/x509/root_darwin.go`
- ❌ `src/crypto/x509/root_windows.go`
- ❌ `src/crypto/x509/verify.go`
- ✅ `src/crypto/x509/verify_test.go`
- ❌ `src/crypto/x509/x509_test.go`
- ❌ `src/runtime/sys_darwin.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/sys_darwin.go`, `crypto_x509_syscall`)
- ❌ (`src/crypto/x509/cert_pool.go`, `SystemCertPool`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `CFStringToString`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `TimeToCFDateRef`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `BytesToCFData`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `x509_CFDataCreate_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `CFArrayCreateMutable`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `x509_CFArrayCreateMutable_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `CFArrayAppendValue`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `x509_CFArrayAppendValue_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `CFDateCreate`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `x509_CFDateCreate_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `CFErrorCopyDescription`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `x509_CFErrorCopyDescription_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `CFStringCreateExternalRepresentation`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `x509_CFStringCreateExternalRepresentation_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/corefoundation.go`, `ReleaseCFArray`)
- ❌ (`src/crypto/x509/verify_test.go`, `TestSystemRootsError`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestSystemCertPool`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `SecTrustCreateWithCertificates`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `x509_SecTrustCreateWithCertificates_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `SecCertificateCreateWithData`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `x509_SecCertificateCreateWithData_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `SecPolicyCreateSSL`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `x509_SecPolicyCreateSSL_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `SecTrustSetVerifyDate`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `x509_SecTrustSetVerifyDate_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `SecTrustEvaluate`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `x509_SecTrustEvaluate_trampoline`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `SecTrustEvaluateWithError`)
- ❌ (`src/crypto/x509/internal/macos/security.go`, `x509_SecTrustEvaluateWithError_trampoline`)
- ✅ (`src/crypto/x509/root_darwin.go`, `systemVerify`)
- ❌ (`src/crypto/x509/root_darwin.go`, `exportCertificate`)
- ❌ (`src/crypto/x509/root_darwin.go`, `loadSystemRoots`)
- ❌ (`src/crypto/x509/verify.go`, `Verify`)
- ❌ (`src/crypto/x509/cert_pool.go`, `SystemCertPool`)
- ❌ (`src/crypto/x509/verify_test.go`, `TestSystemRootsError`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestSystemCertPool`)
- ❌ (`src/cmd/dist/test.go`, `registerTests`)
- ❌ (`src/crypto/x509/verify.go`, `Verify`)
- ❌ (`src/crypto/x509/cert_pool.go`, `SystemCertPool`)
- ❌ (`src/crypto/x509/root_windows.go`, `loadSystemRoots`)
- ❌ (`src/crypto/x509/root_windows.go`, `systemVerify`)
- ❌ (`src/crypto/x509/root_darwin.go`, `loadSystemRoots`)
- ❌ (`src/crypto/x509/verify.go`, `Verify`)
- ❌ (`src/crypto/x509/hybrid_pool_test.go`, `TestHybridPool`)

### 📊 Proposal #46293

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/test`
- ✅ `src/reflect`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/test/inl_test.go`
- ❌ `src/reflect/all_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/test`
- ✅ `src/reflect`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/test/inl_test.go`
- ❌ `src/reflect/all_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/reflect/all_test.go`, `TestMapIterSet`)
- ❌ (`src/reflect/all_test.go`, `TestMapIterReset`)
- ❌ (`src/cmd/compile/internal/test/inl_test.go`, `TestIntendedInlining`)
- ❌ (`src/reflect/all_test.go`, `TestMapIterSet`)

### 📊 Proposal #46308

#### File Embeddings - Directory Level
- ✅ `src/crypto/tls`

#### File Embeddings - File Level
- ❌ `src/crypto/tls/common.go`
- ✅ `src/crypto/tls/tls_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/tls`

#### Function Embeddings - File Level
- ❌ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/tls_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/tls/common.go`, `VersionName`)
- ❌ (`src/crypto/tls/tls_test.go`, `TestVersionName`)
- ❌ (`src/crypto/tls/common.go`, `VersionName`)
- ❌ (`src/crypto/tls/tls_test.go`, `TestVersionName`)

### 📊 Proposal #46336

#### File Embeddings - Directory Level
- ❌ `src/archive/tar`
- ❌ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/asm/internal/lex`
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/liveness`
- ❌ `src/cmd/compile/internal/logopt`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/doc`
- ❌ `src/cmd/fix`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/base`
- ❌ `src/cmd/go/internal/cache`
- ❌ `src/cmd/go/internal/cmdflag`
- ❌ `src/cmd/go/internal/envcmd`
- ❌ `src/cmd/go/internal/imports`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modcmd`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ❌ `src/cmd/go/internal/modget`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/mvs`
- ❌ `src/cmd/go/internal/search`
- ❌ `src/cmd/go/internal/test`
- ❌ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/vet`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/go/testdata`
- ❌ `src/cmd/gofmt`
- ❌ `src/cmd/internal/obj`
- ❌ `src/cmd/internal/test2json`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/binutils`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/driver`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/report`
- ❌ `src/cmd/vendor/github.com/google/pprof/profile`
- ❌ `src/cmd/vendor/golang.org/x/arch/ppc64/ppc64asm`
- ❌ `src/cmd/vendor/golang.org/x/mod/modfile`
- ❌ `src/cmd/vendor/golang.org/x/mod/module`
- ❌ `src/cmd/vendor/golang.org/x/mod/sumdb`
- ❌ `src/cmd/vendor/golang.org/x/mod/sumdb/note`
- ❌ `src/cmd/vendor/golang.org/x/sys/plan9`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/framepointer`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- ❌ `src/cmd/vet`
- ❌ `src/crypto/ecdsa`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/encoding/asn1`
- ❌ `src/encoding/json`
- ❌ `src/encoding/xml`
- ❌ `src/fmt`
- ❌ `src/go/build`
- ❌ `src/go/constant`
- ❌ `src/go/doc`
- ❌ `src/go/importer`
- ❌ `src/go/printer`
- ❌ `src/go/types`
- ❌ `src/html/template`
- ❌ `src/internal/goroot`
- ❌ `src/math/big`
- ❌ `src/mime`
- ❌ `src/net`
- ❌ `src/net/http`
- ❌ `src/net/http/cgi`
- ❌ `src/net/mail`
- ❌ `src/net/smtp`
- ❌ `src/net/url`
- ❌ `src/os`
- ❌ `src/os/exec`
- ❌ `src/os/user`
- ❌ `src/regexp`
- ❌ `src/regexp/syntax`
- ❌ `src/runtime/pprof`
- ❌ `src/strconv`
- ❌ `src/strings`
- ❌ `src/testing/fstest`
- ❌ `src/vendor/golang.org/x/net/http/httpguts`
- ❌ `src/vendor/golang.org/x/net/idna`
- ❌ `src/vendor/golang.org/x/sys/cpu`

#### File Embeddings - File Level
- ❌ `src/archive/tar/strconv.go`
- ❌ `src/archive/tar/writer_test.go`
- ❌ `src/cmd/asm/internal/asm/operand_test.go`
- ❌ `src/cmd/asm/internal/lex/input.go`
- ❌ `src/cmd/cgo/gcc.go`
- ❌ `src/cmd/cgo/godefs.go`
- ❌ `src/cmd/cgo/out.go`
- ❌ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/liveness/plive.go`
- ❌ `src/cmd/compile/internal/logopt/log_opts.go`
- ❌ `src/cmd/compile/internal/noder/noder.go`
- ❌ `src/cmd/compile/internal/ssa/debug_test.go`
- ❌ `src/cmd/compile/internal/ssa/html.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/imports.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/doc/dirs.go`
- ❌ `src/cmd/doc/pkg.go`
- ❌ `src/cmd/fix/typecheck.go`
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/base/base.go`
- ❌ `src/cmd/go/internal/base/goflags.go`
- ❌ `src/cmd/go/internal/cache/hash.go`
- ❌ `src/cmd/go/internal/cmdflag/flag.go`
- ❌ `src/cmd/go/internal/envcmd/env.go`
- ❌ `src/cmd/go/internal/imports/build.go`
- ❌ `src/cmd/go/internal/imports/read_test.go`
- ❌ `src/cmd/go/internal/load/flag.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modcmd/edit.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ❌ `src/cmd/go/internal/modget/query.go`
- ❌ `src/cmd/go/internal/modload/build.go`
- ❌ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/modload/list.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ❌ `src/cmd/go/internal/mvs/mvs_test.go`
- ❌ `src/cmd/go/internal/search/search.go`
- ❌ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/go/internal/vcs/vcs.go`
- ❌ `src/cmd/go/internal/vet/vetflag.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/buildid.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`
- ❌ `src/cmd/go/proxy_test.go`
- ❌ `src/cmd/go/testdata/addmod.go`
- ❌ `src/cmd/gofmt/gofmt_test.go`
- ❌ `src/cmd/internal/obj/stringer.go`
- ❌ `src/cmd/internal/test2json/test2json.go`
- ❌ `src/cmd/link/internal/ld/data.go`
- ❌ `src/cmd/link/internal/ld/dwarf.go`
- ❌ `src/cmd/link/internal/ld/go.go`
- ❌ `src/cmd/link/internal/ld/ld.go`
- ❌ `src/cmd/link/internal/ld/main.go`
- ❌ `src/cmd/link/internal/ld/pe.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/binutils/addr2liner.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/binutils/binutils.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/driver/commands.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/driver/driver_focus.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/driver/interactive.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/report/source.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/profile/legacy_profile.go`
- ❌ `src/cmd/vendor/golang.org/x/arch/ppc64/ppc64asm/plan9.go`
- ❌ `src/cmd/vendor/golang.org/x/mod/modfile/rule.go`
- ❌ `src/cmd/vendor/golang.org/x/mod/module/module.go`
- ❌ `src/cmd/vendor/golang.org/x/mod/sumdb/note/note.go`
- ❌ `src/cmd/vendor/golang.org/x/mod/sumdb/server.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/plan9/syscall.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/xattr_bsd.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows/syscall.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl/asmdecl.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/framepointer/framepointer.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/crypto/ecdsa/ecdsa_test.go`
- ❌ `src/crypto/tls/handshake_test.go`
- ❌ `src/crypto/x509/pem_decrypt.go`
- ❌ `src/encoding/asn1/common.go`
- ❌ `src/encoding/json/tags.go`
- ❌ `src/encoding/xml/typeinfo.go`
- ❌ `src/encoding/xml/xml.go`
- ❌ `src/fmt/fmt_test.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/go/build/read.go`
- ❌ `src/go/build/read_test.go`
- ❌ `src/go/constant/value_test.go`
- ❌ `src/go/doc/headscan.go`
- ❌ `src/go/importer/importer_test.go`
- ❌ `src/go/printer/nodes.go`
- ❌ `src/go/printer/printer.go`
- ❌ `src/go/types/eval_test.go`
- ❌ `src/html/template/attr.go`
- ❌ `src/html/template/js.go`
- ❌ `src/html/template/url.go`
- ❌ `src/internal/goroot/gc.go`
- ❌ `src/math/big/ratconv.go`
- ❌ `src/mime/encodedword.go`
- ❌ `src/mime/mediatype.go`
- ❌ `src/net/http/cgi/child.go`
- ❌ `src/net/http/cgi/host.go`
- ❌ `src/net/http/cgi/host_test.go`
- ❌ `src/net/http/client_test.go`
- ❌ `src/net/http/cookie.go`
- ❌ `src/net/http/fs.go`
- ❌ `src/net/http/main_test.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/net/mail/message.go`
- ❌ `src/net/main_test.go`
- ❌ `src/net/smtp/smtp.go`
- ❌ `src/net/url/url.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/os_test.go`
- ❌ `src/os/user/cgo_lookup_unix.go`
- ❌ `src/os/user/lookup_unix.go`
- ❌ `src/regexp/exec_test.go`
- ❌ `src/regexp/syntax/parse.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/proto_test.go`
- ❌ `src/strconv/fp_test.go`
- ❌ `src/strings/strings.go`
- ❌ `src/testing/fstest/mapfs.go`
- ❌ `src/testing/fstest/testfs.go`
- ❌ `src/vendor/golang.org/x/net/http/httpguts/httplex.go`
- ❌ `src/vendor/golang.org/x/net/idna/idna10.0.0.go`
- ❌ `src/vendor/golang.org/x/net/idna/idna9.0.0.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu.go`

#### Function Embeddings - Directory Level
- ❌ `src/archive/tar`
- ❌ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/asm/internal/lex`
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/liveness`
- ❌ `src/cmd/compile/internal/logopt`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/doc`
- ❌ `src/cmd/fix`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/base`
- ❌ `src/cmd/go/internal/cache`
- ❌ `src/cmd/go/internal/cmdflag`
- ❌ `src/cmd/go/internal/envcmd`
- ❌ `src/cmd/go/internal/imports`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modcmd`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ❌ `src/cmd/go/internal/modget`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/go/internal/mvs`
- ❌ `src/cmd/go/internal/search`
- ❌ `src/cmd/go/internal/test`
- ❌ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/vet`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/go/testdata`
- ❌ `src/cmd/gofmt`
- ❌ `src/cmd/internal/obj`
- ❌ `src/cmd/internal/test2json`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/binutils`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/driver`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/report`
- ❌ `src/cmd/vendor/github.com/google/pprof/profile`
- ❌ `src/cmd/vendor/golang.org/x/arch/ppc64/ppc64asm`
- ❌ `src/cmd/vendor/golang.org/x/mod/modfile`
- ❌ `src/cmd/vendor/golang.org/x/mod/module`
- ❌ `src/cmd/vendor/golang.org/x/mod/sumdb`
- ❌ `src/cmd/vendor/golang.org/x/mod/sumdb/note`
- ❌ `src/cmd/vendor/golang.org/x/sys/plan9`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/framepointer`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- ❌ `src/cmd/vet`
- ❌ `src/crypto/ecdsa`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/encoding/asn1`
- ❌ `src/encoding/json`
- ❌ `src/encoding/xml`
- ❌ `src/fmt`
- ❌ `src/go/build`
- ❌ `src/go/constant`
- ❌ `src/go/doc`
- ❌ `src/go/importer`
- ❌ `src/go/printer`
- ❌ `src/go/types`
- ❌ `src/html/template`
- ❌ `src/internal/goroot`
- ❌ `src/math/big`
- ❌ `src/mime`
- ❌ `src/net`
- ❌ `src/net/http`
- ❌ `src/net/http/cgi`
- ❌ `src/net/mail`
- ❌ `src/net/smtp`
- ❌ `src/net/url`
- ❌ `src/os`
- ❌ `src/os/exec`
- ❌ `src/os/user`
- ❌ `src/regexp`
- ❌ `src/regexp/syntax`
- ❌ `src/runtime/pprof`
- ❌ `src/strconv`
- ✅ `src/strings`
- ❌ `src/testing/fstest`
- ❌ `src/vendor/golang.org/x/net/http/httpguts`
- ❌ `src/vendor/golang.org/x/net/idna`
- ❌ `src/vendor/golang.org/x/sys/cpu`

#### Function Embeddings - File Level
- ❌ `src/archive/tar/strconv.go`
- ❌ `src/archive/tar/writer_test.go`
- ❌ `src/cmd/asm/internal/asm/operand_test.go`
- ❌ `src/cmd/asm/internal/lex/input.go`
- ❌ `src/cmd/cgo/gcc.go`
- ❌ `src/cmd/cgo/godefs.go`
- ❌ `src/cmd/cgo/out.go`
- ❌ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/liveness/plive.go`
- ❌ `src/cmd/compile/internal/logopt/log_opts.go`
- ❌ `src/cmd/compile/internal/noder/noder.go`
- ❌ `src/cmd/compile/internal/ssa/debug_test.go`
- ❌ `src/cmd/compile/internal/ssa/html.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/imports.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/doc/dirs.go`
- ❌ `src/cmd/doc/pkg.go`
- ❌ `src/cmd/fix/typecheck.go`
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/base/base.go`
- ❌ `src/cmd/go/internal/base/goflags.go`
- ❌ `src/cmd/go/internal/cache/hash.go`
- ❌ `src/cmd/go/internal/cmdflag/flag.go`
- ❌ `src/cmd/go/internal/envcmd/env.go`
- ❌ `src/cmd/go/internal/imports/build.go`
- ❌ `src/cmd/go/internal/imports/read_test.go`
- ❌ `src/cmd/go/internal/load/flag.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modcmd/edit.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ❌ `src/cmd/go/internal/modget/query.go`
- ❌ `src/cmd/go/internal/modload/build.go`
- ❌ `src/cmd/go/internal/modload/init.go`
- ❌ `src/cmd/go/internal/modload/list.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ❌ `src/cmd/go/internal/mvs/mvs_test.go`
- ❌ `src/cmd/go/internal/search/search.go`
- ❌ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/go/internal/vcs/vcs.go`
- ❌ `src/cmd/go/internal/vet/vetflag.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/buildid.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`
- ❌ `src/cmd/go/proxy_test.go`
- ❌ `src/cmd/go/testdata/addmod.go`
- ❌ `src/cmd/gofmt/gofmt_test.go`
- ❌ `src/cmd/internal/obj/stringer.go`
- ❌ `src/cmd/internal/test2json/test2json.go`
- ❌ `src/cmd/link/internal/ld/data.go`
- ❌ `src/cmd/link/internal/ld/dwarf.go`
- ❌ `src/cmd/link/internal/ld/go.go`
- ❌ `src/cmd/link/internal/ld/ld.go`
- ❌ `src/cmd/link/internal/ld/main.go`
- ❌ `src/cmd/link/internal/ld/pe.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/binutils/addr2liner.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/binutils/binutils.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/driver/commands.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/driver/driver_focus.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/driver/interactive.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/internal/report/source.go`
- ❌ `src/cmd/vendor/github.com/google/pprof/profile/legacy_profile.go`
- ❌ `src/cmd/vendor/golang.org/x/arch/ppc64/ppc64asm/plan9.go`
- ❌ `src/cmd/vendor/golang.org/x/mod/modfile/rule.go`
- ❌ `src/cmd/vendor/golang.org/x/mod/module/module.go`
- ❌ `src/cmd/vendor/golang.org/x/mod/sumdb/note/note.go`
- ❌ `src/cmd/vendor/golang.org/x/mod/sumdb/server.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/plan9/syscall.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/syscall.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/unix/xattr_bsd.go`
- ❌ `src/cmd/vendor/golang.org/x/sys/windows/syscall.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl/asmdecl.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/framepointer/framepointer.go`
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/crypto/ecdsa/ecdsa_test.go`
- ❌ `src/crypto/tls/handshake_test.go`
- ❌ `src/crypto/x509/pem_decrypt.go`
- ❌ `src/encoding/asn1/common.go`
- ❌ `src/encoding/json/tags.go`
- ❌ `src/encoding/xml/typeinfo.go`
- ❌ `src/encoding/xml/xml.go`
- ❌ `src/fmt/fmt_test.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/go/build/read.go`
- ❌ `src/go/build/read_test.go`
- ❌ `src/go/constant/value_test.go`
- ❌ `src/go/doc/headscan.go`
- ❌ `src/go/importer/importer_test.go`
- ❌ `src/go/printer/nodes.go`
- ❌ `src/go/printer/printer.go`
- ❌ `src/go/types/eval_test.go`
- ❌ `src/html/template/attr.go`
- ❌ `src/html/template/js.go`
- ❌ `src/html/template/url.go`
- ❌ `src/internal/goroot/gc.go`
- ❌ `src/math/big/ratconv.go`
- ❌ `src/mime/encodedword.go`
- ❌ `src/mime/mediatype.go`
- ❌ `src/net/http/cgi/child.go`
- ❌ `src/net/http/cgi/host.go`
- ❌ `src/net/http/cgi/host_test.go`
- ❌ `src/net/http/client_test.go`
- ❌ `src/net/http/cookie.go`
- ❌ `src/net/http/fs.go`
- ❌ `src/net/http/main_test.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/net/mail/message.go`
- ❌ `src/net/main_test.go`
- ❌ `src/net/smtp/smtp.go`
- ❌ `src/net/url/url.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/os_test.go`
- ❌ `src/os/user/cgo_lookup_unix.go`
- ❌ `src/os/user/lookup_unix.go`
- ❌ `src/regexp/exec_test.go`
- ❌ `src/regexp/syntax/parse.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/proto_test.go`
- ❌ `src/strconv/fp_test.go`
- ❌ `src/strings/strings.go`
- ❌ `src/testing/fstest/mapfs.go`
- ❌ `src/testing/fstest/testfs.go`
- ❌ `src/vendor/golang.org/x/net/http/httpguts/httplex.go`
- ❌ `src/vendor/golang.org/x/net/idna/idna10.0.0.go`
- ❌ `src/vendor/golang.org/x/net/idna/idna9.0.0.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu.go`

#### Function Embeddings - Function Level
- ❌ (`src/strings/strings.go`, `Cut`)
- ❌ (`src/cmd/compile/internal/ssa/debug_test.go`, `read`)
- ❌ (`src/cmd/compile/internal/ssa/debug_test.go`, `canonFileName`)
- ❌ (`src/cmd/compile/internal/ssa/debug_test.go`, `printVariableAndNormalize`)
- ❌ (`src/cmd/compile/internal/ssa/debug_test.go`, `varsToPrint`)
- ❌ (`src/cmd/compile/internal/ssa/debug_test.go`, `quit`)
- ❌ (`src/html/template/js.go`, `isJSType`)
- ❌ (`src/cmd/compile/internal/logopt/log_opts.go`, `parseLogFlag`)
- ❌ (`src/net/http/client_test.go`, `removeCommonLines`)
- ❌ (`src/regexp/syntax/parse.go`, `Parse`)
- ❌ (`src/regexp/syntax/parse.go`, `parsePerlFlags`)
- ❌ (`src/regexp/syntax/parse.go`, `parseUnicodeClass`)
- ❌ (`src/cmd/vendor/golang.org/x/mod/sumdb/note/note.go`, `NewVerifier`)
- ❌ (`src/cmd/vendor/golang.org/x/mod/sumdb/note/note.go`, `NewSigner`)
- ❌ (`src/cmd/vendor/golang.org/x/mod/sumdb/note/note.go`, `Open`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `containsInOrder`)
- ❌ (`src/runtime/pprof/pprof_test.go`, `stackContainsLabeled`)
- ❌ (`src/cmd/go/internal/test/test.go`, `tryCacheWithID`)
- ❌ (`src/cmd/go/internal/test/test.go`, `computeTestInputsID`)
- ❌ (`src/os/user/lookup_unix.go`, `matchUserIndexValue`)
- ❌ (`src/cmd/compile/internal/base/flag.go`, `readImportCfg`)
- ❌ (`src/cmd/vendor/golang.org/x/arch/ppc64/ppc64asm/plan9.go`, `GoSyntax`)
- ❌ (`src/cmd/go/internal/work/gccgo.go`, `buildImportcfgSymlinks`)
- ❌ (`src/cmd/compile/internal/noder/noder.go`, `pragma`)
- ❌ (`src/cmd/compile/internal/noder/noder.go`, `parseGoEmbed`)
- ❌ (`src/net/http/cgi/child.go`, `envMap`)
- ❌ (`src/archive/tar/strconv.go`, `hasNUL`)
- ❌ (`src/archive/tar/strconv.go`, `parsePAXTime`)
- ❌ (`src/archive/tar/strconv.go`, `parsePAXRecord`)
- ❌ (`src/archive/tar/strconv.go`, `validPAXRecord`)
- ❌ (`src/cmd/go/go_test.go`, `parallel`)
- ❌ (`src/cmd/go/go_test.go`, `isStale`)
- ❌ (`src/cmd/link/internal/ld/go.go`, `ldpkg`)
- ❌ (`src/cmd/link/internal/ld/go.go`, `loadcgo`)
- ❌ (`src/cmd/link/internal/ld/go.go`, `setCgoAttr`)
- ❌ (`src/go/types/eval_test.go`, `split`)
- ❌ (`src/cmd/go/proxy_test.go`, `proxyHandler`)
- ❌ (`src/html/template/attr.go`, `attrType`)
- ❌ (`src/cmd/go/internal/envcmd/env.go`, `argKey`)
- ❌ (`src/cmd/go/internal/envcmd/env.go`, `runEnv`)
- ❌ (`src/cmd/go/internal/envcmd/env.go`, `PrintEnv`)
- ❌ (`src/cmd/go/internal/envcmd/env.go`, `lineToKey`)
- ❌ (`src/vendor/golang.org/x/net/http/httpguts/httplex.go`, `headerValueContainsToken`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`, `checkTagDuplicates`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`, `validateStructTag`)
- ❌ (`src/cmd/link/internal/ld/data.go`, `addstrdata1`)
- ❌ (`src/go/build/build_test.go`, `TestMissingImportErrorRepetition`)
- ❌ (`src/go/importer/importer_test.go`, `TestForCompiler`)
- ❌ (`src/os/exec/exec.go`, `dedupEnvCase`)
- ❌ (`src/os/exec/exec.go`, `addCriticalEnv`)
- ❌ (`src/cmd/go/internal/cmdflag/flag.go`, `ParseOne`)
- ❌ (`src/cmd/dist/build.go`, `shouldbuild`)
- ❌ (`src/cmd/dist/build.go`, `timelog`)
- ❌ (`src/cmd/doc/pkg.go`, `oneLineNodeDepth`)
- ❌ (`src/go/constant/value_test.go`, `testNumbers`)
- ❌ (`src/go/constant/value_test.go`, `val`)
- ❌ (`src/cmd/link/internal/ld/dwarf.go`, `writeDirFileTables`)
- ❌ (`src/go/printer/nodes.go`, `normalizedNumber`)
- ❌ (`src/os/os_test.go`, `TestHostname`)
- ❌ (`src/cmd/go/internal/base/base.go`, `LongName`)
- ❌ (`src/encoding/asn1/common.go`, `parseFieldParameters`)
- ❌ (`src/math/big/ratconv.go`, `SetString`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `QueryPattern`)
- ❌ (`src/cmd/compile/internal/liveness/plive.go`, `showlive`)
- ❌ (`src/net/http/request.go`, `ParseHTTPVersion`)
- ❌ (`src/net/http/request.go`, `parseBasicAuth`)
- ❌ (`src/net/http/request.go`, `parseRequestLine`)
- ❌ (`src/vendor/golang.org/x/sys/cpu/cpu.go`, `processOptions`)
- ❌ (`src/cmd/doc/dirs.go`, `findCodeRoots`)
- ❌ (`src/cmd/go/internal/mvs/mvs_test.go`, `Test`)
- ❌ (`src/cmd/fix/typecheck.go`, `typecheck1`)
- ❌ (`src/crypto/ecdsa/ecdsa_test.go`, `TestVectors`)
- ❌ (`src/crypto/x509/pem_decrypt.go`, `DecryptPEMBlock`)
- ❌ (`src/cmd/vendor/golang.org/x/mod/module/module.go`, `CheckPath`)
- ❌ (`src/cmd/vendor/golang.org/x/mod/module/module.go`, `checkElem`)
- ❌ (`src/cmd/vendor/golang.org/x/mod/module/module.go`, `MatchPrefixPatterns`)
- ❌ (`src/net/url/url.go`, `Parse`)
- ❌ (`src/net/url/url.go`, `parse`)
- ❌ (`src/net/url/url.go`, `parseAuthority`)
- ❌ (`src/net/url/url.go`, `parseHost`)
- ❌ (`src/net/url/url.go`, `String`)
- ❌ (`src/net/url/url.go`, `parseQuery`)
- ❌ (`src/net/url/url.go`, `resolvePath`)
- ❌ (`src/mime/encodedword.go`, `Decode`)
- ❌ (`src/mime/encodedword.go`, `DecodeHeader`)
- ❌ (`src/mime/encodedword.go`, `decode`)
- ❌ (`src/mime/encodedword.go`, `convert`)
- ❌ (`src/cmd/link/internal/ld/main.go`, `Main`)
- ❌ (`src/cmd/go/internal/search/search.go`, `MatchDirs`)
- ❌ (`src/cmd/go/internal/search/search.go`, `CleanPatterns`)
- ❌ (`src/cmd/go/internal/search/search.go`, `IsStandardImportPath`)
- ❌ (`src/cmd/go/internal/search/search.go`, `IsRelativePath`)
- ❌ (`src/cmd/cgo/godefs.go`, `godefs`)
- ❌ (`src/cmd/link/internal/ld/pe.go`, `initdynimport`)
- ❌ (`src/cmd/dist/imports.go`, `resolveVendor`)
- ❌ (`src/net/http/fs.go`, `parseRange`)
- ❌ (`src/strconv/fp_test.go`, `myatof64`)
- ❌ (`src/strconv/fp_test.go`, `myatof32`)
- ❌ (`src/cmd/go/internal/cache/hash.go`, `stripExperiment`)
- ❌ (`src/cmd/go/internal/work/build.go`, `installOutsideModule`)
- ❌ (`src/cmd/go/internal/load/flag.go`, `set`)
- ❌ (`src/encoding/xml/xml.go`, `nsname`)
- ❌ (`src/encoding/xml/xml.go`, `procInst`)
- ❌ (`src/net/http/main_test.go`, `interestingGoroutines`)
- ❌ (`src/cmd/vendor/github.com/google/pprof/internal/driver/commands.go`, `usage`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/syscall.go`, `ByteSliceFromString`)
- ❌ (`src/crypto/tls/handshake_test.go`, `parseTestData`)
- ❌ (`src/cmd/go/internal/modcmd/edit.go`, `parsePathVersion`)
- ❌ (`src/cmd/go/internal/modcmd/edit.go`, `parsePathVersionOptional`)
- ❌ (`src/cmd/go/internal/modcmd/edit.go`, `parseVersionInterval`)
- ❌ (`src/cmd/go/internal/modcmd/edit.go`, `flagReplace`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/unix/xattr_bsd.go`, `xattrnamespace`)
- ❌ (`src/net/http/cgi/host.go`, `ServeHTTP`)
- ❌ (`src/go/printer/printer.go`, `stripCommonPrefix`)
- ❌ (`src/net/smtp/smtp.go`, `ehlo`)
- ❌ (`src/encoding/json/tags.go`, `parseTag`)
- ❌ (`src/encoding/json/tags.go`, `Contains`)
- ❌ (`src/cmd/go/internal/modload/build.go`, `ModuleInfo`)
- ❌ (`src/cmd/go/internal/imports/build.go`, `MatchFile`)
- ❌ (`src/cmd/go/internal/modget/query.go`, `newQuery`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/framepointer/framepointer.go`, `run`)
- ❌ (`src/cmd/internal/obj/stringer.go`, `main`)
- ❌ (`src/testing/fstest/mapfs.go`, `Open`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `file`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `goBuildLine`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`, `plusBuildLine`)
- ❌ (`src/fmt/fmt_test.go`, `presentInMap`)
- ❌ (`src/cmd/internal/test2json/test2json.go`, `handleInputLine`)
- ❌ (`src/internal/goroot/gc.go`, `isStandard`)
- ❌ (`src/cmd/vendor/github.com/google/pprof/internal/binutils/binutils.go`, `initTools`)
- ❌ (`src/cmd/go/internal/modload/list.go`, `listModules`)
- ❌ (`src/cmd/gofmt/gofmt_test.go`, `runTest`)
- ❌ (`src/go/doc/headscan.go`, `appendHeadings`)
- ❌ (`src/go/doc/headscan.go`, `main`)
- ❌ (`src/cmd/asm/internal/asm/operand_test.go`, `TestFuncAddress`)
- ❌ (`src/cmd/dist/test.go`, `flattenCmdline`)
- ❌ (`src/cmd/vendor/golang.org/x/mod/sumdb/server.go`, `ServeHTTP`)
- ❌ (`src/net/main_test.go`, `runningGoroutines`)
- ❌ (`src/vendor/golang.org/x/net/idna/idna9.0.0.go`, `label`)
- ❌ (`src/vendor/golang.org/x/net/idna/idna9.0.0.go`, `validateLabel`)
- ❌ (`src/net/http/transport.go`, `dialConn`)
- ❌ (`src/cmd/vendor/github.com/google/pprof/internal/driver/driver_focus.go`, `compileTagFilter`)
- ❌ (`src/net/http/server.go`, `stripHostPort`)
- ❌ (`src/net/http/cookie.go`, `readSetCookies`)
- ❌ (`src/net/http/cookie.go`, `readCookies`)
- ❌ (`src/net/http/cookie.go`, `sanitizeCookieValue`)
- ❌ (`src/cmd/cgo/out.go`, `checkImportSymName`)
- ❌ (`src/cmd/cgo/gcc.go`, `loadDefines`)
- ❌ (`src/cmd/cgo/gcc.go`, `guessKinds`)
- ❌ (`src/cmd/cgo/gcc.go`, `badCFType`)
- ❌ (`src/cmd/go/internal/modload/modfile.go`, `ShortMessage`)
- ❌ (`src/cmd/go/internal/modload/init.go`, `fixVersion`)
- ❌ (`src/cmd/go/testdata/addmod.go`, `main`)
- ❌ (`src/cmd/go/internal/vet/vetflag.go`, `parseVettoolFlag`)
- ❌ (`src/regexp/exec_test.go`, `parseResult`)
- ❌ (`src/regexp/exec_test.go`, `testFowler`)
- ❌ (`src/vendor/golang.org/x/net/idna/idna10.0.0.go`, `label`)
- ❌ (`src/vendor/golang.org/x/net/idna/idna10.0.0.go`, `validateLabel`)
- ❌ (`src/cmd/compile/internal/ssa/html.go`, `WriteAST`)
- ❌ (`src/archive/tar/writer_test.go`, `TestIssue12594`)
- ❌ (`src/encoding/xml/typeinfo.go`, `structFieldInfo`)
- ❌ (`src/cmd/link/internal/ld/ld.go`, `readImportCfg`)
- ❌ (`src/testing/fstest/testfs.go`, `checkBadPath`)
- ❌ (`src/os/user/cgo_lookup_unix.go`, `buildUser`)
- ❌ (`src/cmd/vendor/github.com/google/pprof/internal/report/source.go`, `trimPath`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `PackagesAndErrorsOutsideModule`)
- ❌ (`src/go/build/read.go`, `parseGoEmbed`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `bzrResolveRepo`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `svnRemoteRepo`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `parseGOVCS`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl/asmdecl.go`, `run`)
- ❌ (`src/cmd/go/internal/modfetch/codehost/vcs.go`, `bzrParseStat`)
- ❌ (`src/cmd/go/internal/imports/read_test.go`, `testRead`)
- ❌ (`src/net/http/cgi/host_test.go`, `runResponseChecks`)
- ❌ (`src/cmd/vet/vet_test.go`, `errorCheck`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `actionID`)
- ❌ (`src/cmd/go/internal/work/buildid.go`, `contentID`)
- ❌ (`src/cmd/vendor/github.com/google/pprof/internal/binutils/addr2liner.go`, `readFrame`)
- ❌ (`src/go/build/read_test.go`, `testRead`)
- ❌ (`src/mime/mediatype.go`, `FormatMediaType`)
- ❌ (`src/mime/mediatype.go`, `ParseMediaType`)
- ❌ (`src/cmd/vendor/github.com/google/pprof/profile/legacy_profile.go`, `parseContention`)
- ❌ (`src/cmd/vendor/github.com/google/pprof/profile/legacy_profile.go`, `parseProcMapsFromScanner`)
- ❌ (`src/runtime/pprof/proto_test.go`, `TestProcSelfMaps`)
- ❌ (`src/os/exec/exec_test.go`, `TestCatGoodAndBadFile`)
- ❌ (`src/go/build/build.go`, `saveCgo`)
- ❌ (`src/go/build/build.go`, `goodOSArchFile`)
- ❌ (`src/cmd/vendor/golang.org/x/mod/modfile/rule.go`, `setIndirect`)
- ❌ (`src/cmd/asm/internal/lex/input.go`, `predefine`)
- ❌ (`src/html/template/url.go`, `isSafeURL`)
- ❌ (`src/cmd/vendor/github.com/google/pprof/internal/driver/interactive.go`, `interactive`)
- ❌ (`src/net/http/response.go`, `ReadResponse`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/windows/syscall.go`, `ByteSliceFromString`)
- ❌ (`src/net/mail/message.go`, `ParseDate`)
- ❌ (`src/cmd/go/internal/base/goflags.go`, `InitGOFLAGS`)
- ❌ (`src/cmd/go/internal/base/goflags.go`, `SetFromGOFLAGS`)
- ❌ (`src/cmd/go/internal/base/goflags.go`, `InGOFLAGS`)
- ❌ (`src/cmd/vendor/golang.org/x/sys/plan9/syscall.go`, `ByteSliceFromString`)

### 📊 Proposal #46485

#### File Embeddings - Directory Level
- ✅ `src/cmd/cgo`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/gofmt`
- ❌ `src/go/internal/srcimporter`
- ❌ `src/go/parser`

#### File Embeddings - File Level
- ✅ `src/cmd/cgo/ast.go`
- ❌ `src/cmd/go/internal/load/test.go`
- ❌ `src/cmd/gofmt/gofmt.go`
- ❌ `src/cmd/gofmt/simplify.go`
- ❌ `src/go/internal/srcimporter/srcimporter.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/performance_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/gofmt`
- ❌ `src/go/internal/srcimporter`
- ❌ `src/go/parser`

#### Function Embeddings - File Level
- ❌ `src/cmd/cgo/ast.go`
- ❌ `src/cmd/go/internal/load/test.go`
- ❌ `src/cmd/gofmt/gofmt.go`
- ❌ `src/cmd/gofmt/simplify.go`
- ❌ `src/go/internal/srcimporter/srcimporter.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/performance_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/parser/performance_test.go`, `BenchmarkParseOnly`)
- ❌ (`src/go/parser/performance_test.go`, `BenchmarkResolve`)
- ❌ (`src/go/parser/parser.go`, `parseFile`)
- ❌ (`src/cmd/gofmt/gofmt.go`, `initParserMode`)
- ❌ (`src/go/internal/srcimporter/srcimporter.go`, `parseFiles`)
- ❌ (`src/go/internal/srcimporter/srcimporter.go`, `cgo`)
- ❌ (`src/cmd/cgo/ast.go`, `ParseGo`)
- ❌ (`src/cmd/go/internal/load/test.go`, `load`)
- ❌ (`src/cmd/gofmt/gofmt.go`, `initParserMode`)
- ❌ (`src/cmd/gofmt/simplify.go`, `Visit`)

### 📊 Proposal #46505

#### File Embeddings - Directory Level
- ❌ `src/crypto/sha256`
- ❌ `src/crypto/sha512`

#### File Embeddings - File Level
- ❌ `src/crypto/sha256/sha256.go`
- ❌ `src/crypto/sha512/sha512.go`

#### Function Embeddings - Directory Level
- ❌ `src/crypto/sha256`
- ❌ `src/crypto/sha512`

#### Function Embeddings - File Level
- ❌ `src/crypto/sha256/sha256.go`
- ❌ `src/crypto/sha512/sha512.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/sha256/sha256.go`, `Sum224`)
- ❌ (`src/crypto/sha512/sha512.go`, `Sum384`)
- ❌ (`src/crypto/sha512/sha512.go`, `Sum512_224`)
- ❌ (`src/crypto/sha512/sha512.go`, `Sum512_256`)

### 📊 Proposal #46518

#### File Embeddings - Directory Level
- ❌ `src/internal/fuzz`
- ❌ `src/internal/godebug`
- ✅ `src/net`
- ❌ `src/net/http`
- ✅ `src/net/netip`

#### File Embeddings - File Level
- ❌ `src/internal/fuzz/fuzz.go`
- ❌ `src/internal/godebug/godebug_test.go`
- ❌ `src/net/conf.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/net/lookup.go`
- ❌ `src/net/netip/export_test.go`
- ❌ `src/net/netip/inlining_test.go`
- ✅ `src/net/netip/netip.go`
- ❌ `src/net/netip/netip_pkg_test.go`
- ❌ `src/net/netip/netip_test.go`
- ❌ `src/net/netip/slow_test.go`
- ❌ `src/net/netip/uint128.go`
- ❌ `src/net/netip/uint128_test.go`
- ❌ `src/net/parse_test.go`
- ❌ `src/net/tcpsock.go`
- ❌ `src/net/udpsock.go`

#### Function Embeddings - Directory Level
- ❌ `src/internal/fuzz`
- ❌ `src/internal/godebug`
- ✅ `src/net`
- ❌ `src/net/http`
- ❌ `src/net/netip`

#### Function Embeddings - File Level
- ❌ `src/internal/fuzz/fuzz.go`
- ❌ `src/internal/godebug/godebug_test.go`
- ❌ `src/net/conf.go`
- ❌ `src/net/http/server.go`
- ❌ `src/net/http/transport.go`
- ❌ `src/net/lookup.go`
- ❌ `src/net/netip/export_test.go`
- ❌ `src/net/netip/inlining_test.go`
- ❌ `src/net/netip/netip.go`
- ❌ `src/net/netip/netip_pkg_test.go`
- ❌ `src/net/netip/netip_test.go`
- ❌ `src/net/netip/slow_test.go`
- ❌ `src/net/netip/uint128.go`
- ❌ `src/net/netip/uint128_test.go`
- ❌ `src/net/parse_test.go`
- ❌ `src/net/tcpsock.go`
- ❌ `src/net/udpsock.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/netip/netip_test.go`, `TestParseAddr`)
- ❌ (`src/net/netip/netip_test.go`, `TestIPv4Constructors`)
- ❌ (`src/net/netip/netip_test.go`, `TestAddrMarshalUnmarshalBinary`)
- ❌ (`src/net/netip/netip_test.go`, `TestAddrMarshalUnmarshal`)
- ❌ (`src/net/netip/netip_test.go`, `TestAddrFrom16`)
- ❌ (`src/net/netip/netip_test.go`, `TestIPProperties`)
- ❌ (`src/net/netip/netip_test.go`, `TestAddrWellKnown`)
- ❌ (`src/net/netip/netip_test.go`, `TestIPStringExpanded`)
- ❌ (`src/net/netip/netip_test.go`, `TestPrefixMasking`)
- ❌ (`src/net/netip/netip_test.go`, `TestPrefixMarshalUnmarshal`)
- ❌ (`src/net/netip/netip_test.go`, `TestPrefixUnmarshalTextNonZero`)
- ❌ (`src/net/netip/netip_test.go`, `TestIs4AndIs6`)
- ❌ (`src/net/netip/netip_test.go`, `TestIs4In6`)
- ❌ (`src/net/netip/netip_test.go`, `TestPrefixMasked`)
- ❌ (`src/net/netip/netip_test.go`, `TestPrefix`)
- ❌ (`src/net/netip/netip_test.go`, `TestPrefixFromInvalidBits`)
- ❌ (`src/net/netip/netip_test.go`, `TestParsePrefixAllocs`)
- ❌ (`src/net/netip/netip_test.go`, `TestParsePrefixError`)
- ❌ (`src/net/netip/netip_test.go`, `TestPrefixIsSingleIP`)
- ❌ (`src/net/netip/netip_test.go`, `mustIPs`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkBinaryMarshalRoundTrip`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkStdIPv4`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkIPv4`)
- ❌ (`src/net/netip/netip_test.go`, `newip4i_v4`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkIPv4_inline`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkStdIPv6`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkIPv6`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkIPv4Contains`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkIPv6Contains`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkParseAddr`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkStdParseIP`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkIPStringExpanded`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkAddrPortString`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkAddrPortMarshalText`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkPrefixMasking`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkPrefixMarshalText`)
- ❌ (`src/net/netip/netip_test.go`, `BenchmarkParseAddrPort`)
- ❌ (`src/net/netip/netip_test.go`, `TestAs4`)
- ❌ (`src/net/netip/netip_test.go`, `TestPrefixOverlaps`)
- ❌ (`src/net/netip/netip_test.go`, `TestNoAllocs`)
- ❌ (`src/net/netip/netip_test.go`, `TestPrefixString`)
- ❌ (`src/net/netip/uint128.go`, `mask6`)
- ❌ (`src/net/netip/uint128.go`, `and`)
- ❌ (`src/net/netip/uint128.go`, `xor`)
- ❌ (`src/net/netip/uint128.go`, `or`)
- ❌ (`src/net/netip/uint128.go`, `not`)
- ❌ (`src/net/netip/uint128.go`, `subOne`)
- ❌ (`src/net/netip/uint128.go`, `addOne`)
- ❌ (`src/net/netip/uint128.go`, `halves`)
- ❌ (`src/net/netip/uint128.go`, `bitsSetFrom`)
- ❌ (`src/net/netip/uint128.go`, `bitsClearedFrom`)
- ❌ (`src/net/netip/uint128_test.go`, `TestUint128AddSub`)
- ❌ (`src/net/netip/uint128_test.go`, `TestBitsSetFrom`)
- ❌ (`src/net/netip/uint128_test.go`, `TestBitsClearedFrom`)
- ❌ (`src/net/parse_test.go`, `TestDtoi`)
- ❌ (`src/internal/godebug/godebug_test.go`, `TestGet`)
- ❌ (`src/net/netip/inlining_test.go`, `TestInlining`)
- ❌ (`src/net/udpsock.go`, `AddrPort`)
- ❌ (`src/net/udpsock.go`, `UDPAddrFromAddrPort`)
- ❌ (`src/net/udpsock.go`, `ReadMsgUDPAddrPort`)
- ❌ (`src/net/udpsock.go`, `WriteToUDPAddrPort`)
- ❌ (`src/net/udpsock.go`, `WriteMsgUDPAddrPort`)
- ❌ (`src/net/netip/netip.go`, `AddrFrom4`)
- ❌ (`src/net/netip/netip.go`, `AddrFrom16`)
- ❌ (`src/net/netip/netip.go`, `ParseAddr`)
- ❌ (`src/net/netip/netip.go`, `MustParseAddr`)
- ❌ (`src/net/netip/netip.go`, `Error`)
- ❌ (`src/net/netip/netip.go`, `parseIPv4`)
- ❌ (`src/net/netip/netip.go`, `parseIPv6`)
- ❌ (`src/net/netip/netip.go`, `AddrFromSlice`)
- ❌ (`src/net/netip/netip.go`, `v4`)
- ❌ (`src/net/netip/netip.go`, `v6`)
- ❌ (`src/net/netip/netip.go`, `v6u16`)
- ❌ (`src/net/netip/netip.go`, `isZero`)
- ❌ (`src/net/netip/netip.go`, `BitLen`)
- ❌ (`src/net/netip/netip.go`, `Zone`)
- ❌ (`src/net/netip/netip.go`, `Compare`)
- ❌ (`src/net/netip/netip.go`, `Is4`)
- ❌ (`src/net/netip/netip.go`, `Is4In6`)
- ❌ (`src/net/netip/netip.go`, `Is6`)
- ❌ (`src/net/netip/netip.go`, `Unmap`)
- ❌ (`src/net/netip/netip.go`, `WithZone`)
- ❌ (`src/net/netip/netip.go`, `withoutZone`)
- ❌ (`src/net/netip/netip.go`, `hasZone`)
- ❌ (`src/net/netip/netip.go`, `IsLinkLocalUnicast`)
- ❌ (`src/net/netip/netip.go`, `IsLoopback`)
- ❌ (`src/net/netip/netip.go`, `IsMulticast`)
- ❌ (`src/net/netip/netip.go`, `IsInterfaceLocalMulticast`)
- ❌ (`src/net/netip/netip.go`, `IsLinkLocalMulticast`)
- ❌ (`src/net/netip/netip.go`, `IsGlobalUnicast`)
- ❌ (`src/net/netip/netip.go`, `IsPrivate`)
- ❌ (`src/net/netip/netip.go`, `IsUnspecified`)
- ❌ (`src/net/netip/netip.go`, `Prefix`)
- ❌ (`src/net/netip/netip.go`, `As16`)
- ❌ (`src/net/netip/netip.go`, `As4`)
- ❌ (`src/net/netip/netip.go`, `Next`)
- ❌ (`src/net/netip/netip.go`, `Prev`)
- ❌ (`src/net/netip/netip.go`, `String`)
- ❌ (`src/net/netip/netip.go`, `AppendTo`)
- ❌ (`src/net/netip/netip.go`, `appendDecimal`)
- ❌ (`src/net/netip/netip.go`, `appendHex`)
- ❌ (`src/net/netip/netip.go`, `appendHexPad`)
- ❌ (`src/net/netip/netip.go`, `string4`)
- ❌ (`src/net/netip/netip.go`, `appendTo4`)
- ❌ (`src/net/netip/netip.go`, `string6`)
- ❌ (`src/net/netip/netip.go`, `appendTo6`)
- ❌ (`src/net/netip/netip.go`, `StringExpanded`)
- ❌ (`src/net/netip/netip.go`, `MarshalText`)
- ❌ (`src/net/netip/netip.go`, `UnmarshalText`)
- ❌ (`src/net/netip/netip.go`, `MarshalBinary`)
- ❌ (`src/net/netip/netip.go`, `UnmarshalBinary`)
- ❌ (`src/net/netip/netip.go`, `splitAddrPort`)
- ❌ (`src/net/netip/netip.go`, `ParseAddrPort`)
- ❌ (`src/net/netip/netip.go`, `MustParseAddrPort`)
- ❌ (`src/net/netip/netip.go`, `String`)
- ❌ (`src/net/netip/netip.go`, `AppendTo`)
- ❌ (`src/net/netip/netip.go`, `MarshalText`)
- ❌ (`src/net/netip/netip.go`, `UnmarshalText`)
- ❌ (`src/net/netip/netip.go`, `PrefixFrom`)
- ❌ (`src/net/netip/netip.go`, `ParsePrefix`)
- ❌ (`src/net/netip/netip.go`, `MustParsePrefix`)
- ❌ (`src/net/netip/netip.go`, `Masked`)
- ❌ (`src/net/netip/netip.go`, `Contains`)
- ❌ (`src/net/netip/netip.go`, `Overlaps`)
- ❌ (`src/net/netip/netip.go`, `AppendTo`)
- ❌ (`src/net/netip/netip.go`, `MarshalText`)
- ❌ (`src/net/netip/netip.go`, `UnmarshalText`)
- ❌ (`src/net/netip/netip.go`, `String`)
- ❌ (`src/net/lookup.go`, `LookupNetIP`)
- ❌ (`src/net/tcpsock.go`, `AddrPort`)
- ❌ (`src/internal/fuzz/fuzz.go`, `shouldPrintDebugInfo`)
- ❌ (`src/net/netip/export_test.go`, `Mk128`)
- ❌ (`src/net/netip/export_test.go`, `MkAddr`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `TestPrefixValid`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `TestIPNextPrev`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `BenchmarkIPNextPrev`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `doNextPrev`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `TestIPBitLen`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `TestPrefixContains`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `TestParseIPError`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `TestParseAddrPort`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `TestAddrPortMarshalUnmarshal`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `testAppendToMarshal`)
- ❌ (`src/net/netip/netip_pkg_test.go`, `TestIPv6Accessor`)
- ❌ (`src/net/conf.go`, `goDebugNetDNS`)
- ❌ (`src/net/http/transport.go`, `onceSetNextProtoDefaults`)
- ❌ (`src/net/netip/slow_test.go`, `parseIPSlow`)
- ❌ (`src/net/netip/slow_test.go`, `normalizeIPv6Slow`)
- ❌ (`src/net/netip/slow_test.go`, `parseIPv4Slow`)
- ❌ (`src/net/netip/slow_test.go`, `parseWord`)
- ❌ (`src/net/http/server.go`, `onceSetNextProtoDefaults`)

### 📊 Proposal #46552

#### File Embeddings - Directory Level
- ❌ `src/runtime`
- ✅ `src/syscall`

#### File Embeddings - File Level
- ❌ `src/runtime/syscall_windows.go`
- ❌ `src/runtime/syscall_windows_test.go`
- ❌ `src/syscall/dll_windows.go`

#### Function Embeddings - Directory Level
- ✅ `src/runtime`
- ❌ `src/syscall`

#### Function Embeddings - File Level
- ❌ `src/runtime/syscall_windows.go`
- ✅ `src/runtime/syscall_windows_test.go`
- ❌ `src/syscall/dll_windows.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/syscall_windows_test.go`, `TestSyscallN`)
- ❌ (`src/runtime/syscall_windows.go`, `syscall_Syscall`)
- ❌ (`src/runtime/syscall_windows.go`, `syscall_Syscall6`)
- ❌ (`src/runtime/syscall_windows.go`, `syscall_Syscall9`)
- ❌ (`src/runtime/syscall_windows.go`, `syscall_Syscall12`)
- ❌ (`src/runtime/syscall_windows.go`, `syscall_Syscall15`)
- ❌ (`src/runtime/syscall_windows.go`, `syscall_Syscall18`)
- ❌ (`src/runtime/syscall_windows.go`, `syscall_SyscallN`)
- ❌ (`src/syscall/dll_windows.go`, `SyscallN`)
- ❌ (`src/syscall/dll_windows.go`, `Call`)
- ❌ (`src/syscall/dll_windows.go`, `Load`)

### 📊 Proposal #46648

#### File Embeddings - Directory Level
- ✅ `src/go/types`

#### File Embeddings - File Level
- ❌ `src/go/types/check.go`
- ❌ `src/go/types/check_test.go`
- ❌ `src/go/types/stdlib_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/go/types`

#### Function Embeddings - File Level
- ❌ `src/go/types/check.go`
- ❌ `src/go/types/check_test.go`
- ❌ `src/go/types/stdlib_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/types/stdlib_test.go`, `testTestDir`)
- ❌ (`src/go/types/check.go`, `NewChecker`)
- ❌ (`src/go/types/check_test.go`, `testFiles`)

### 📊 Proposal #46731

#### File Embeddings - Directory Level
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/typebits`
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/compile/internal/types`
- ❌ `src/reflect`
- ❌ `src/runtime`
- ❌ `test`
- ✅ `test/fixedbugs`

#### File Embeddings - File Level
- ❌ `src/cmd/cgo/gcc.go`
- ❌ `src/cmd/cgo/out.go`
- ❌ `src/cmd/compile/internal/noder/noder.go`
- ❌ `src/cmd/compile/internal/noder/reader.go`
- ❌ `src/cmd/compile/internal/noder/writer.go`
- ❌ `src/cmd/compile/internal/typebits/typebits.go`
- ❌ `src/cmd/compile/internal/typecheck/func.go`
- ❌ `src/cmd/compile/internal/types/size.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/deepequal.go`
- ❌ `src/reflect/nih_test.go`
- ❌ `src/reflect/value.go`
- ❌ `src/runtime/debuglog.go`
- ❌ `src/runtime/malloc.go`
- ❌ `src/runtime/mcheckmark.go`
- ❌ `src/runtime/mheap.go`
- ❌ `test/directive.go`
- ❌ `test/fixedbugs/issue40954.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/typebits`
- ❌ `src/cmd/compile/internal/typecheck`
- ✅ `src/cmd/compile/internal/types`
- ❌ `src/reflect`
- ❌ `src/runtime`
- ❌ `test`
- ❌ `test/fixedbugs`

#### Function Embeddings - File Level
- ❌ `src/cmd/cgo/gcc.go`
- ❌ `src/cmd/cgo/out.go`
- ❌ `src/cmd/compile/internal/noder/noder.go`
- ❌ `src/cmd/compile/internal/noder/reader.go`
- ❌ `src/cmd/compile/internal/noder/writer.go`
- ❌ `src/cmd/compile/internal/typebits/typebits.go`
- ❌ `src/cmd/compile/internal/typecheck/func.go`
- ❌ `src/cmd/compile/internal/types/size.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/deepequal.go`
- ❌ `src/reflect/nih_test.go`
- ❌ `src/reflect/value.go`
- ❌ `src/runtime/debuglog.go`
- ❌ `src/runtime/malloc.go`
- ❌ `src/runtime/mcheckmark.go`
- ❌ `src/runtime/mheap.go`
- ❌ `test/directive.go`
- ❌ `test/fixedbugs/issue40954.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/compile/internal/types/size.go`, `CalcSize`)
- ❌ (`src/runtime/malloc.go`, `add`)
- ❌ (`src/runtime/mcheckmark.go`, `startCheckmarks`)
- ❌ (`src/runtime/mcheckmark.go`, `setCheckmark`)
- ❌ (`src/runtime/debuglog.go`, `ensure`)
- ❌ (`src/runtime/debuglog.go`, `writeFrameAt`)
- ❌ (`src/runtime/debuglog.go`, `byte`)
- ❌ (`src/runtime/debuglog.go`, `bytes`)
- ❌ (`src/runtime/debuglog.go`, `readUint16LEAt`)
- ❌ (`src/runtime/debuglog.go`, `readUint64LEAt`)
- ❌ (`src/runtime/debuglog.go`, `peek`)
- ❌ (`src/runtime/debuglog.go`, `uvarint`)
- ❌ (`src/runtime/debuglog.go`, `printVal`)
- ❌ (`src/runtime/mheap.go`, `bytep`)
- ❌ (`src/cmd/cgo/out.go`, `writeDefs`)
- ❌ (`src/cmd/cgo/gcc.go`, `loadType`)
- ❌ (`src/cmd/cgo/gcc.go`, `badPointerTypedef`)
- ❌ (`src/cmd/compile/internal/noder/noder.go`, `pragma`)
- ❌ (`src/cmd/compile/internal/noder/reader.go`, `expr`)
- ❌ (`src/runtime/mcheckmark.go`, `startCheckmarks`)
- ❌ (`src/runtime/mcheckmark.go`, `setCheckmark`)
- ❌ (`src/runtime/debuglog.go`, `ensure`)
- ❌ (`src/runtime/debuglog.go`, `writeFrameAt`)
- ❌ (`src/runtime/debuglog.go`, `byte`)
- ❌ (`src/runtime/debuglog.go`, `bytes`)
- ❌ (`src/runtime/debuglog.go`, `readUint16LEAt`)
- ❌ (`src/runtime/debuglog.go`, `readUint64LEAt`)
- ❌ (`src/runtime/debuglog.go`, `peek`)
- ❌ (`src/runtime/debuglog.go`, `uvarint`)
- ❌ (`src/runtime/debuglog.go`, `printVal`)
- ❌ (`src/runtime/mheap.go`, `bytep`)
- ❌ (`src/cmd/cgo/out.go`, `writeDefs`)
- ❌ (`src/cmd/cgo/gcc.go`, `Init`)
- ❌ (`src/cmd/cgo/gcc.go`, `loadType`)
- ❌ (`src/cmd/cgo/gcc.go`, `badPointerTypedef`)
- ❌ (`src/cmd/cgo/gcc.go`, `badVoidPointerTypedef`)
- ❌ (`src/reflect/nih_test.go`, `TestNotInHeapDeref`)
- ❌ (`src/reflect/deepequal.go`, `deepValueEqual`)
- ❌ (`src/reflect/value.go`, `New`)
- ❌ (`src/reflect/all_test.go`, `TestMethodCallValueCodePtr`)
- ❌ (`src/reflect/all_test.go`, `TestIssue50208`)
- ❌ (`test/fixedbugs/issue40954.go`, `main`)
- ❌ (`src/cmd/compile/internal/noder/noder.go`, `pragma`)
- ❌ (`test/directive.go`, `f`)
- ❌ (`src/cmd/compile/internal/noder/noder.go`, `pragma`)
- ❌ (`src/cmd/compile/internal/typebits/typebits.go`, `Set`)
- ❌ (`src/cmd/compile/internal/noder/writer.go`, `Visit`)
- ❌ (`src/cmd/compile/internal/noder/reader.go`, `typeExt`)
- ❌ (`src/cmd/compile/internal/noder/reader.go`, `expr`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcUnsafeSlice`)

### 📊 Proposal #46742

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/runtime`
- ❌ `src/runtime/testdata/testprog`
- ✅ `test`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/typecheck/builtin.go`
- ❌ `src/cmd/compile/internal/typecheck/func.go`
- ❌ `src/cmd/compile/internal/walk/builtin.go`
- ❌ `src/runtime/checkptr.go`
- ❌ `src/runtime/checkptr_test.go`
- ❌ `src/runtime/testdata/testprog/checkptr.go`
- ✅ `test/unsafebuiltins.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/runtime`
- ❌ `src/runtime/testdata/testprog`
- ✅ `test`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/typecheck/builtin.go`
- ❌ `src/cmd/compile/internal/typecheck/func.go`
- ❌ `src/cmd/compile/internal/walk/builtin.go`
- ❌ `src/runtime/checkptr.go`
- ❌ `src/runtime/checkptr_test.go`
- ❌ `src/runtime/testdata/testprog/checkptr.go`
- ✅ `test/unsafebuiltins.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/testdata/testprog/checkptr.go`, `init`)
- ❌ (`src/runtime/testdata/testprog/checkptr.go`, `CheckPtrSliceOK`)
- ❌ (`src/runtime/testdata/testprog/checkptr.go`, `CheckPtrSliceFail`)
- ❌ (`src/runtime/checkptr.go`, `checkptrAlignment`)
- ❌ (`src/runtime/checkptr.go`, `checkptrStraddles`)
- ✅ (`test/unsafebuiltins.go`, `main`)
- ❌ (`src/cmd/compile/internal/typecheck/builtin.go`, `runtimeTypes`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcUnsafeSlice`)
- ❌ (`src/cmd/compile/internal/walk/builtin.go`, `walkUnsafeSlice`)
- ❌ (`src/runtime/checkptr_test.go`, `TestCheckPtr`)

### 📊 Proposal #46746

#### File Embeddings - Directory Level
- ❌ `src/reflect`

#### File Embeddings - File Level
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/value.go`

#### Function Embeddings - Directory Level
- ✅ `src/reflect`

#### Function Embeddings - File Level
- ❌ `src/reflect/all_test.go`
- ✅ `src/reflect/value.go`

#### Function Embeddings - Function Level
- ❌ (`src/reflect/value.go`, `CanConvert`)
- ❌ (`src/reflect/all_test.go`, `TestConvert`)
- ❌ (`src/reflect/all_test.go`, `TestConvertPanic`)
- ❌ (`src/reflect/value.go`, `Comparable`)
- ❌ (`src/reflect/value.go`, `Equal`)
- ❌ (`src/reflect/all_test.go`, `TestValue_Comparable`)
- ❌ (`src/reflect/all_test.go`, `TestValue_Equal`)

### 📊 Proposal #46771

#### File Embeddings - Directory Level
- ✅ `src/mime/multipart`

#### File Embeddings - File Level
- ✅ `src/mime/multipart/writer.go`
- ✅ `src/mime/multipart/writer_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/mime/multipart`

#### Function Embeddings - File Level
- ✅ `src/mime/multipart/writer.go`
- ✅ `src/mime/multipart/writer_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/mime/multipart/writer.go`, `CreateFormFile`)
- ✅ (`src/mime/multipart/writer.go`, `CreateFormFile`)
- ✅ (`src/mime/multipart/writer.go`, `FileContentDisposition`)
- ✅ (`src/mime/multipart/writer_test.go`, `TestFileContentDisposition`)

### 📊 Proposal #47005

#### File Embeddings - Directory Level
- ✅ `src/net/url`

#### File Embeddings - File Level
- ❌ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/url`

#### Function Embeddings - File Level
- ✅ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/net/url/url.go`, `JoinPath`)
- ✅ (`src/net/url/url.go`, `JoinPath`)
- ✅ (`src/net/url/url_test.go`, `TestJoinPath`)
- ✅ (`src/net/url/url.go`, `JoinPath`)
- ✅ (`src/net/url/url.go`, `JoinPath`)
- ✅ (`src/net/url/url_test.go`, `TestJoinPath`)

### 📊 Proposal #47066

#### File Embeddings - Directory Level
- ✅ `src/reflect`

#### File Embeddings - File Level
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/value.go`

#### Function Embeddings - Directory Level
- ✅ `src/reflect`

#### Function Embeddings - File Level
- ✅ `src/reflect/all_test.go`
- ✅ `src/reflect/value.go`

#### Function Embeddings - Function Level
- ❌ (`src/reflect/value.go`, `Bytes`)
- ❌ (`src/reflect/all_test.go`, `TestBytes`)

### 📊 Proposal #47142

#### File Embeddings - Directory Level
- ❌ `src/database/sql`

#### File Embeddings - File Level
- ❌ `src/database/sql/fakedb_test.go`
- ❌ `src/database/sql/sql.go`
- ❌ `src/database/sql/sql_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/database/sql`

#### Function Embeddings - File Level
- ✅ `src/database/sql/fakedb_test.go`
- ✅ `src/database/sql/sql.go`
- ❌ `src/database/sql/sql_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/database/sql/fakedb_test.go`, `Error`)
- ❌ (`src/database/sql/fakedb_test.go`, `Unwrap`)
- ❌ (`src/database/sql/fakedb_test.go`, `isDirtyAndMark`)
- ❌ (`src/database/sql/fakedb_test.go`, `Begin`)
- ❌ (`src/database/sql/fakedb_test.go`, `ResetSession`)
- ❌ (`src/database/sql/fakedb_test.go`, `PrepareContext`)
- ❌ (`src/database/sql/fakedb_test.go`, `ExecContext`)
- ❌ (`src/database/sql/fakedb_test.go`, `Query`)
- ✅ (`src/database/sql/fakedb_test.go`, `QueryContext`)
- ❌ (`src/database/sql/fakedb_test.go`, `NumInput`)
- ❌ (`src/database/sql/fakedb_test.go`, `Commit`)
- ❌ (`src/database/sql/fakedb_test.go`, `Rollback`)
- ❌ (`src/database/sql/sql_test.go`, `TestTxEndBadConn`)
- ❌ (`src/database/sql/sql.go`, `PingContext`)
- ❌ (`src/database/sql/sql.go`, `conn`)
- ✅ (`src/database/sql/sql.go`, `putConn`)
- ❌ (`src/database/sql/sql.go`, `PrepareContext`)
- ❌ (`src/database/sql/sql.go`, `ExecContext`)
- ❌ (`src/database/sql/sql.go`, `QueryContext`)
- ❌ (`src/database/sql/sql.go`, `BeginTx`)
- ✅ (`src/database/sql/sql.go`, `Conn`)
- ❌ (`src/database/sql/sql.go`, `PrepareContext`)
- ❌ (`src/database/sql/sql.go`, `BeginTx`)
- ❌ (`src/database/sql/sql.go`, `closemuRUnlockCondReleaseConn`)
- ❌ (`src/database/sql/sql.go`, `Commit`)
- ❌ (`src/database/sql/sql.go`, `rollback`)
- ❌ (`src/database/sql/sql.go`, `ExecContext`)
- ❌ (`src/database/sql/sql.go`, `QueryContext`)

### 📊 Proposal #47164

#### File Embeddings - Directory Level
- ❌ `src/log`

#### File Embeddings - File Level
- ❌ `src/log/log.go`
- ❌ `src/log/log_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/log`

#### Function Embeddings - File Level
- ❌ `src/log/log.go`
- ❌ `src/log/log_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/log/log_test.go`, `TestDiscard`)
- ❌ (`src/log/log.go`, `New`)
- ❌ (`src/log/log.go`, `SetOutput`)
- ❌ (`src/log/log.go`, `Output`)
- ❌ (`src/log/log.go`, `Printf`)
- ❌ (`src/log/log.go`, `Print`)
- ❌ (`src/log/log.go`, `Println`)
- ❌ (`src/log/log.go`, `Prefix`)
- ❌ (`src/log/log.go`, `SetOutput`)
- ❌ (`src/log/log.go`, `Print`)
- ❌ (`src/log/log.go`, `Printf`)
- ❌ (`src/log/log.go`, `Println`)

### 📊 Proposal #47209

#### File Embeddings - Directory Level
- ✅ `src/cmd/go/internal/fsys`
- ✅ `src/io/fs`
- ✅ `src/path/filepath`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/fsys/fsys_test.go`
- ✅ `src/io/fs/walk.go`
- ❌ `src/path/filepath/path.go`
- ❌ `src/path/filepath/path_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/go/internal/fsys`
- ✅ `src/io/fs`
- ✅ `src/path/filepath`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/fsys/fsys_test.go`
- ✅ `src/io/fs/walk.go`
- ✅ `src/path/filepath/path.go`
- ✅ `src/path/filepath/path_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/path/filepath/path.go`, `walk`)
- ❌ (`src/path/filepath/path.go`, `WalkDir`)
- ❌ (`src/path/filepath/path.go`, `Walk`)
- ❌ (`src/cmd/go/internal/fsys/fsys_test.go`, `TestWalkSkipAll`)
- ❌ (`src/io/fs/walk.go`, `WalkDir`)
- ❌ (`src/path/filepath/path_test.go`, `TestWalkSkipAllOnFile`)

### 📊 Proposal #47216

#### File Embeddings - Directory Level
- ✅ `src/runtime`

#### File Embeddings - File Level
- ❌ `src/runtime/metrics.go`
- ❌ `src/runtime/metrics_test.go`
- ❌ `src/runtime/mgc.go`
- ❌ `src/runtime/mgclimit.go`
- ❌ `src/runtime/mgcscavenge.go`
- ❌ `src/runtime/mheap.go`

#### Function Embeddings - Directory Level
- ✅ `src/runtime`

#### Function Embeddings - File Level
- ❌ `src/runtime/metrics.go`
- ✅ `src/runtime/metrics_test.go`
- ❌ `src/runtime/mgc.go`
- ❌ `src/runtime/mgclimit.go`
- ❌ `src/runtime/mgcscavenge.go`
- ❌ `src/runtime/mheap.go`

#### Function Embeddings - Function Level
- ✅ (`src/runtime/metrics_test.go`, `TestReadMetricsConsistency`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)
- ❌ (`src/runtime/metrics_test.go`, `TestReadMetrics`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)
- ✅ (`src/runtime/metrics_test.go`, `TestReadMetricsConsistency`)
- ❌ (`src/runtime/metrics_test.go`, `withinEpsilon`)
- ❌ (`src/runtime/mgcscavenge.go`, `init`)
- ❌ (`src/runtime/mheap.go`, `allocSpan`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)
- ❌ (`src/runtime/metrics.go`, `compute`)
- ❌ (`src/runtime/metrics.go`, `nsToSec`)
- ❌ (`src/runtime/metrics.go`, `ensure`)
- ❌ (`src/runtime/mgclimit.go`, `stop`)
- ❌ (`src/runtime/mgc.go`, `gcMarkTermination`)

### 📊 Proposal #47257

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/importer`
- ❌ `src/cmd/compile/internal/types2`
- ✅ `src/cmd/dist`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modindex`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/link`
- ❌ `src/go/build`
- ❌ `src/go/internal/gcimporter`
- ✅ `src/runtime`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/importer/gcimporter_test.go`
- ❌ `src/cmd/compile/internal/types2/issues_test.go`
- ❌ `src/cmd/compile/internal/types2/self_test.go`
- ❌ `src/cmd/compile/internal/types2/sizes_test.go`
- ❌ `src/cmd/compile/internal/types2/typestring_test.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modindex/index_test.go`
- ❌ `src/cmd/go/internal/modindex/read.go`
- ❌ `src/cmd/go/internal/work/action.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/link/link_test.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/internal/gcimporter/gcimporter_test.go`
- ❌ `src/runtime/sys_darwin.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/importer`
- ❌ `src/cmd/compile/internal/types2`
- ❌ `src/cmd/dist`
- ✅ `src/cmd/go`
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modindex`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/link`
- ❌ `src/go/build`
- ❌ `src/go/internal/gcimporter`
- ❌ `src/runtime`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/importer/gcimporter_test.go`
- ❌ `src/cmd/compile/internal/types2/issues_test.go`
- ❌ `src/cmd/compile/internal/types2/self_test.go`
- ❌ `src/cmd/compile/internal/types2/sizes_test.go`
- ❌ `src/cmd/compile/internal/types2/typestring_test.go`
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/test.go`
- ✅ `src/cmd/go/go_test.go`
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modindex/index_test.go`
- ❌ `src/cmd/go/internal/modindex/read.go`
- ❌ `src/cmd/go/internal/work/action.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/link/link_test.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/internal/gcimporter/gcimporter_test.go`
- ❌ `src/runtime/sys_darwin.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/sys_darwin.go`, `crypto_x509_syscall`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `buildActionID`)
- ❌ (`src/cmd/go/internal/modindex/index_test.go`, `TestIndex`)
- ❌ (`src/cmd/dist/test.go`, `run`)
- ❌ (`src/cmd/go/internal/work/build.go`, `InstallPackages`)
- ❌ (`src/go/build/build.go`, `Import`)
- ❌ (`src/cmd/link/link_test.go`, `TestUnlinkableObj`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `copyBuild`)
- ❌ (`src/cmd/go/internal/load/pkg.go`, `load`)
- ✅ (`src/cmd/go/go_test.go`, `TestGoInstallPkgdir`)
- ❌ (`src/cmd/go/internal/modindex/read.go`, `Import`)
- ❌ (`src/cmd/go/internal/work/action.go`, `CompileAction`)
- ❌ (`src/cmd/go/internal/work/action.go`, `linkSharedAction`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `installShlibname`)
- ❌ (`src/cmd/dist/build.go`, `setup`)
- ❌ (`src/cmd/dist/build.go`, `runInstall`)
- ❌ (`src/cmd/dist/build.go`, `packagefile`)
- ❌ (`src/go/internal/gcimporter/gcimporter_test.go`, `TestImportTestdata`)
- ❌ (`src/go/internal/gcimporter/gcimporter_test.go`, `TestImportTypeparamTests`)
- ❌ (`src/cmd/compile/internal/importer/gcimporter_test.go`, `TestImportTestdata`)
- ❌ (`src/cmd/compile/internal/types2/sizes_test.go`, `TestAtomicAlign`)
- ❌ (`src/cmd/compile/internal/types2/issues_test.go`, `TestIssue43124`)
- ❌ (`src/cmd/compile/internal/types2/self_test.go`, `TestSelf`)
- ❌ (`src/cmd/compile/internal/types2/self_test.go`, `BenchmarkCheck`)
- ❌ (`src/cmd/compile/internal/types2/typestring_test.go`, `TestTypeString`)

### 📊 Proposal #47342

#### File Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ✅ `src/hash/maphash`

#### File Embeddings - File Level
- ❌ `src/cmd/dist/test.go`
- ❌ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_purego.go`
- ✅ `src/hash/maphash/maphash_runtime.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ✅ `src/hash/maphash`

#### Function Embeddings - File Level
- ❌ `src/cmd/dist/test.go`
- ❌ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_purego.go`
- ✅ `src/hash/maphash/maphash_runtime.go`

#### Function Embeddings - Function Level
- ✅ (`src/hash/maphash/maphash_purego.go`, `rthash`)
- ❌ (`src/hash/maphash/maphash_purego.go`, `rthashString`)
- ❌ (`src/hash/maphash/maphash_purego.go`, `randUint64`)
- ❌ (`src/hash/maphash/maphash_purego.go`, `wyhash`)
- ✅ (`src/hash/maphash/maphash_purego.go`, `r3`)
- ❌ (`src/hash/maphash/maphash_purego.go`, `r4`)
- ❌ (`src/hash/maphash/maphash_purego.go`, `r8`)
- ❌ (`src/hash/maphash/maphash_purego.go`, `mix`)
- ❌ (`src/cmd/dist/test.go`, `registerTests`)
- ❌ (`src/hash/maphash/maphash_runtime.go`, `runtime_memhash`)
- ✅ (`src/hash/maphash/maphash_runtime.go`, `rthash`)
- ❌ (`src/hash/maphash/maphash_runtime.go`, `rthashString`)
- ❌ (`src/hash/maphash/maphash_runtime.go`, `randUint64`)
- ❌ (`src/hash/maphash/maphash.go`, `Bytes`)
- ❌ (`src/hash/maphash/maphash.go`, `String`)
- ❌ (`src/hash/maphash/maphash.go`, `Write`)
- ❌ (`src/hash/maphash/maphash.go`, `WriteString`)
- ❌ (`src/hash/maphash/maphash.go`, `flush`)
- ❌ (`src/hash/maphash/maphash.go`, `Sum64`)
- ❌ (`src/hash/maphash/maphash.go`, `MakeSeed`)
- ❌ (`src/hash/maphash/maphash.go`, `Sum`)

### 📊 Proposal #47527

#### File Embeddings - Directory Level
- ✅ `src/bufio`

#### File Embeddings - File Level
- ✅ `src/bufio/bufio.go`
- ❌ `src/bufio/bufio_test.go`
- ✅ `src/bufio/example_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/bufio`

#### Function Embeddings - File Level
- ✅ `src/bufio/bufio.go`
- ❌ `src/bufio/bufio_test.go`
- ❌ `src/bufio/example_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/bufio/bufio_test.go`, `TestWriterAppend`)
- ❌ (`src/bufio/example_test.go`, `ExampleWriter_AvailableBuffer`)
- ✅ (`src/bufio/bufio.go`, `AvailableBuffer`)

### 📊 Proposal #47609

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/test`
- ✅ `src/unicode/utf8`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/test/inl_test.go`
- ✅ `src/unicode/utf8/utf8.go`
- ❌ `src/unicode/utf8/utf8_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/unicode/utf8`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/test/inl_test.go`
- ❌ `src/unicode/utf8/utf8.go`
- ❌ `src/unicode/utf8/utf8_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/unicode/utf8/utf8.go`, `AppendRune`)
- ❌ (`src/unicode/utf8/utf8.go`, `appendRuneNonASCII`)
- ❌ (`src/unicode/utf8/utf8_test.go`, `TestAppendRune`)
- ❌ (`src/unicode/utf8/utf8_test.go`, `BenchmarkAppendASCIIRune`)
- ❌ (`src/unicode/utf8/utf8_test.go`, `BenchmarkAppendJapaneseRune`)
- ❌ (`src/cmd/compile/internal/test/inl_test.go`, `TestIntendedInlining`)

### 📊 Proposal #47651

#### File Embeddings - Directory Level
- ❌ `src/cmd/fix`
- ❌ `src/cmd/gofmt`
- ❌ `src/database/sql`
- ❌ `src/database/sql/driver`
- ❌ `src/encoding/asn1`
- ❌ `src/encoding/binary`
- ❌ `src/encoding/gob`
- ❌ `src/encoding/json`
- ❌ `src/encoding/xml`
- ❌ `src/flag`
- ❌ `src/fmt`
- ❌ `src/go/ast`
- ❌ `src/html/template`
- ❌ `src/internal/fmtsort`
- ❌ `src/internal/reflectlite`
- ❌ `src/net/rpc`
- ❌ `src/reflect`
- ❌ `src/testing/quick`
- ❌ `src/text/template`
- ✅ `test`
- ❌ `test/fixedbugs/issue32901.dir`

#### File Embeddings - File Level
- ❌ `src/cmd/fix/cftype.go`
- ❌ `src/cmd/fix/typecheck.go`
- ❌ `src/cmd/gofmt/rewrite.go`
- ❌ `src/database/sql/convert.go`
- ❌ `src/database/sql/driver/types.go`
- ❌ `src/encoding/asn1/asn1.go`
- ❌ `src/encoding/binary/binary.go`
- ❌ `src/encoding/gob/decode.go`
- ❌ `src/encoding/gob/decoder.go`
- ❌ `src/encoding/gob/encode.go`
- ❌ `src/encoding/gob/encoder.go`
- ❌ `src/encoding/gob/type.go`
- ❌ `src/encoding/gob/type_test.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/xml/marshal.go`
- ❌ `src/encoding/xml/read.go`
- ❌ `src/encoding/xml/typeinfo.go`
- ❌ `src/flag/flag.go`
- ❌ `src/fmt/print.go`
- ❌ `src/fmt/scan.go`
- ❌ `src/fmt/scan_test.go`
- ❌ `src/go/ast/print.go`
- ❌ `src/html/template/content.go`
- ❌ `src/html/template/js.go`
- ❌ `src/internal/fmtsort/sort.go`
- ❌ `src/internal/reflectlite/tostring_test.go`
- ❌ `src/internal/reflectlite/value.go`
- ❌ `src/net/rpc/server.go`
- ❌ `src/reflect/abi.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/deepequal.go`
- ❌ `src/reflect/tostring_test.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`
- ❌ `src/reflect/visiblefields.go`
- ❌ `src/testing/quick/quick.go`
- ❌ `src/text/template/exec.go`
- ❌ `test/fixedbugs/issue32901.dir/main.go`
- ✅ `test/reflectmethod7.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/fix`
- ❌ `src/cmd/gofmt`
- ❌ `src/database/sql`
- ❌ `src/database/sql/driver`
- ❌ `src/encoding/asn1`
- ❌ `src/encoding/binary`
- ❌ `src/encoding/gob`
- ❌ `src/encoding/json`
- ❌ `src/encoding/xml`
- ❌ `src/flag`
- ❌ `src/fmt`
- ❌ `src/go/ast`
- ❌ `src/html/template`
- ❌ `src/internal/fmtsort`
- ✅ `src/internal/reflectlite`
- ❌ `src/net/rpc`
- ✅ `src/reflect`
- ❌ `src/testing/quick`
- ❌ `src/text/template`
- ❌ `test`
- ❌ `test/fixedbugs/issue32901.dir`

#### Function Embeddings - File Level
- ❌ `src/cmd/fix/cftype.go`
- ❌ `src/cmd/fix/typecheck.go`
- ❌ `src/cmd/gofmt/rewrite.go`
- ❌ `src/database/sql/convert.go`
- ❌ `src/database/sql/driver/types.go`
- ❌ `src/encoding/asn1/asn1.go`
- ❌ `src/encoding/binary/binary.go`
- ❌ `src/encoding/gob/decode.go`
- ❌ `src/encoding/gob/decoder.go`
- ❌ `src/encoding/gob/encode.go`
- ❌ `src/encoding/gob/encoder.go`
- ❌ `src/encoding/gob/type.go`
- ❌ `src/encoding/gob/type_test.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/xml/marshal.go`
- ❌ `src/encoding/xml/read.go`
- ❌ `src/encoding/xml/typeinfo.go`
- ❌ `src/flag/flag.go`
- ❌ `src/fmt/print.go`
- ❌ `src/fmt/scan.go`
- ❌ `src/fmt/scan_test.go`
- ❌ `src/go/ast/print.go`
- ❌ `src/html/template/content.go`
- ❌ `src/html/template/js.go`
- ❌ `src/internal/fmtsort/sort.go`
- ❌ `src/internal/reflectlite/tostring_test.go`
- ✅ `src/internal/reflectlite/value.go`
- ❌ `src/net/rpc/server.go`
- ❌ `src/reflect/abi.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/deepequal.go`
- ❌ `src/reflect/tostring_test.go`
- ✅ `src/reflect/type.go`
- ❌ `src/reflect/value.go`
- ❌ `src/reflect/visiblefields.go`
- ❌ `src/testing/quick/quick.go`
- ❌ `src/text/template/exec.go`
- ❌ `test/fixedbugs/issue32901.dir/main.go`
- ❌ `test/reflectmethod7.go`

#### Function Embeddings - Function Level
- ❌ (`src/internal/reflectlite/value.go`, `Elem`)
- ❌ (`src/internal/reflectlite/value.go`, `IsNil`)
- ❌ (`src/reflect/type.go`, `uncommon`)
- ❌ (`src/reflect/type.go`, `Elem`)
- ❌ (`src/reflect/type.go`, `FieldByIndex`)
- ❌ (`src/reflect/type.go`, `FieldByNameFunc`)
- ❌ (`src/reflect/type.go`, `TypeOf`)
- ❌ (`src/reflect/type.go`, `haveIdenticalUnderlyingType`)
- ❌ (`src/reflect/type.go`, `funcStr`)
- ❌ (`src/reflect/type.go`, `isReflexive`)
- ❌ (`src/reflect/type.go`, `needKeyUpdate`)
- ❌ (`src/reflect/type.go`, `StructOf`)
- ❌ (`src/reflect/type.go`, `append`)
- ❌ (`src/reflect/type.go`, `addTypeBits`)
- ❌ (`src/flag/flag.go`, `isZeroValue`)
- ❌ (`src/html/template/js.go`, `indirectToJSONMarshaler`)
- ❌ (`src/go/ast/print.go`, `NotNilFilter`)
- ❌ (`src/go/ast/print.go`, `print`)
- ❌ (`src/fmt/scan_test.go`, `testScan`)
- ❌ (`src/fmt/scan_test.go`, `TestScanf`)
- ❌ (`src/reflect/value.go`, `Addr`)
- ❌ (`src/reflect/value.go`, `Elem`)
- ❌ (`src/reflect/value.go`, `FieldByIndex`)
- ❌ (`src/reflect/value.go`, `Index`)
- ❌ (`src/reflect/value.go`, `IsNil`)
- ❌ (`src/reflect/value.go`, `IsZero`)
- ❌ (`src/reflect/value.go`, `Pointer`)
- ❌ (`src/reflect/value.go`, `UnsafePointer`)
- ❌ (`src/reflect/value.go`, `Indirect`)
- ❌ (`src/reflect/value.go`, `New`)
- ❌ (`src/reflect/value.go`, `NewAt`)
- ❌ (`src/reflect/value.go`, `CanConvert`)
- ❌ (`src/reflect/value.go`, `convertOp`)
- ❌ (`src/reflect/value.go`, `cvtSliceArrayPtr`)
- ❌ (`src/encoding/gob/type.go`, `validUserType`)
- ❌ (`src/encoding/gob/type.go`, `implementsInterface`)
- ❌ (`src/encoding/gob/type.go`, `isSent`)
- ❌ (`src/encoding/gob/type.go`, `Register`)
- ❌ (`src/cmd/gofmt/rewrite.go`, `subst`)
- ❌ (`src/fmt/scan.go`, `scanOne`)
- ❌ (`src/encoding/xml/typeinfo.go`, `getTypeInfo`)
- ❌ (`src/encoding/xml/typeinfo.go`, `lookupXMLName`)
- ❌ (`src/encoding/xml/typeinfo.go`, `value`)
- ❌ (`test/fixedbugs/issue32901.dir/main.go`, `main`)
- ❌ (`test/reflectmethod7.go`, `main`)
- ❌ (`src/testing/quick/quick.go`, `sizedValue`)
- ❌ (`src/database/sql/driver/types.go`, `callValuerValue`)
- ❌ (`src/database/sql/driver/types.go`, `ConvertValue`)
- ❌ (`src/encoding/json/encode.go`, `isEmptyValue`)
- ❌ (`src/encoding/json/encode.go`, `newTypeEncoder`)
- ❌ (`src/encoding/json/encode.go`, `marshalerEncoder`)
- ❌ (`src/encoding/json/encode.go`, `textMarshalerEncoder`)
- ❌ (`src/encoding/json/encode.go`, `encode`)
- ❌ (`src/encoding/json/encode.go`, `newSliceEncoder`)
- ❌ (`src/encoding/json/encode.go`, `typeByIndex`)
- ❌ (`src/encoding/json/encode.go`, `typeFields`)
- ❌ (`src/internal/fmtsort/sort.go`, `compare`)
- ❌ (`src/encoding/json/decode.go`, `Error`)
- ❌ (`src/encoding/json/decode.go`, `unmarshal`)
- ❌ (`src/encoding/json/decode.go`, `indirect`)
- ❌ (`src/encoding/json/decode.go`, `object`)
- ❌ (`src/encoding/json/decode.go`, `literalStore`)
- ❌ (`src/encoding/gob/encoder.go`, `EncodeValue`)
- ❌ (`src/encoding/gob/type_test.go`, `TestRegistrationNaming`)
- ❌ (`src/cmd/fix/typecheck.go`, `typecheck1`)
- ❌ (`src/reflect/all_test.go`, `TestCanSetField`)
- ❌ (`src/reflect/all_test.go`, `TestIsZero`)
- ❌ (`src/reflect/all_test.go`, `TestPtrTo`)
- ❌ (`src/reflect/all_test.go`, `TestPtrToGC`)
- ❌ (`src/reflect/all_test.go`, `TestArrayOfDirectIface`)
- ❌ (`src/reflect/all_test.go`, `TestStructOfWithInterface`)
- ❌ (`src/reflect/all_test.go`, `TestGCBits`)
- ❌ (`src/reflect/all_test.go`, `TestTypeOfTypeOf`)
- ❌ (`src/cmd/fix/cftype.go`, `typefix`)
- ❌ (`src/encoding/json/decode_test.go`, `TestUnmarshal`)
- ❌ (`src/fmt/print.go`, `fmtPointer`)
- ❌ (`src/fmt/print.go`, `catchPanic`)
- ❌ (`src/fmt/print.go`, `printValue`)
- ❌ (`src/reflect/visiblefields.go`, `walk`)
- ❌ (`src/database/sql/convert.go`, `convertAssignRows`)
- ❌ (`src/database/sql/convert.go`, `callValuerValue`)
- ❌ (`src/reflect/deepequal.go`, `deepValueEqual`)
- ❌ (`src/encoding/asn1/asn1.go`, `Error`)
- ❌ (`src/encoding/asn1/asn1.go`, `UnmarshalWithParams`)
- ❌ (`src/reflect/tostring_test.go`, `valueToString`)
- ❌ (`src/text/template/exec.go`, `isTrue`)
- ❌ (`src/text/template/exec.go`, `evalField`)
- ❌ (`src/text/template/exec.go`, `canBeNil`)
- ❌ (`src/text/template/exec.go`, `validateType`)
- ❌ (`src/text/template/exec.go`, `indirect`)
- ❌ (`src/text/template/exec.go`, `printableValue`)
- ❌ (`src/encoding/gob/encode.go`, `valid`)
- ❌ (`src/encoding/gob/encode.go`, `encodeInterface`)
- ❌ (`src/encoding/gob/encode.go`, `gobEncodeOpFor`)
- ❌ (`src/encoding/xml/read.go`, `DecodeElement`)
- ❌ (`src/encoding/xml/read.go`, `unmarshalAttr`)
- ❌ (`src/encoding/xml/read.go`, `unmarshal`)
- ❌ (`src/encoding/xml/read.go`, `copyValue`)
- ❌ (`src/encoding/xml/marshal.go`, `marshalValue`)
- ❌ (`src/encoding/xml/marshal.go`, `marshalAttr`)
- ❌ (`src/encoding/xml/marshal.go`, `indirect`)
- ❌ (`src/encoding/xml/marshal.go`, `marshalStruct`)
- ❌ (`src/encoding/xml/marshal.go`, `isEmptyValue`)
- ❌ (`src/html/template/content.go`, `indirect`)
- ❌ (`src/html/template/content.go`, `indirectToStringerOrError`)
- ❌ (`src/encoding/binary/binary.go`, `Read`)
- ❌ (`src/net/rpc/server.go`, `isExportedOrBuiltinType`)
- ❌ (`src/net/rpc/server.go`, `register`)
- ❌ (`src/net/rpc/server.go`, `suitableMethods`)
- ❌ (`src/net/rpc/server.go`, `readRequest`)
- ❌ (`src/encoding/gob/decode.go`, `decAlloc`)
- ❌ (`src/encoding/gob/decode.go`, `decodeStruct`)
- ❌ (`src/encoding/gob/decode.go`, `decodeArrayHelper`)
- ❌ (`src/encoding/gob/decode.go`, `decodeMap`)
- ❌ (`src/encoding/gob/decode.go`, `gobDecodeOpFor`)
- ❌ (`src/reflect/abi.go`, `regAssign`)
- ❌ (`src/internal/reflectlite/tostring_test.go`, `valueToStringImpl`)
- ❌ (`src/encoding/gob/decoder.go`, `Decode`)
- ❌ (`src/encoding/gob/decoder.go`, `DecodeValue`)

### 📊 Proposal #47658

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/reflect`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/test/inl_test.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/value.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/reflect`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/test/inl_test.go`
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/value.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/compile/internal/test/inl_test.go`, `TestIntendedInlining`)
- ❌ (`src/reflect/value.go`, `CanComplex`)
- ❌ (`src/reflect/value.go`, `CanFloat`)
- ❌ (`src/reflect/value.go`, `CanInt`)
- ❌ (`src/reflect/value.go`, `CanUint`)
- ❌ (`src/reflect/all_test.go`, `TestCanIntUintFloatComplex`)

### 📊 Proposal #47781

#### File Embeddings - Directory Level
- ✅ `src/cmd/cgo`
- ❌ `src/go/ast`
- ❌ `src/go/parser`
- ❌ `src/go/printer`
- ✅ `src/go/types`

#### File Embeddings - File Level
- ❌ `src/cmd/cgo/ast.go`
- ❌ `src/cmd/cgo/ast_go1.go`
- ✅ `src/cmd/cgo/ast_go118.go`
- ❌ `src/cmd/cgo/gcc.go`
- ❌ `src/go/ast/walk.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/resolver.go`
- ❌ `src/go/printer/nodes.go`
- ❌ `src/go/types/call.go`
- ❌ `src/go/types/decl.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/exprstring.go`
- ❌ `src/go/types/interface.go`
- ❌ `src/go/types/resolver.go`
- ❌ `src/go/types/signature.go`
- ❌ `src/go/types/struct.go`
- ❌ `src/go/types/typexpr.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/cgo`
- ❌ `src/go/ast`
- ❌ `src/go/parser`
- ❌ `src/go/printer`
- ✅ `src/go/types`

#### Function Embeddings - File Level
- ❌ `src/cmd/cgo/ast.go`
- ❌ `src/cmd/cgo/ast_go1.go`
- ❌ `src/cmd/cgo/ast_go118.go`
- ❌ `src/cmd/cgo/gcc.go`
- ❌ `src/go/ast/walk.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/resolver.go`
- ❌ `src/go/printer/nodes.go`
- ❌ `src/go/types/call.go`
- ❌ `src/go/types/decl.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/exprstring.go`
- ❌ `src/go/types/interface.go`
- ❌ `src/go/types/resolver.go`
- ❌ `src/go/types/signature.go`
- ❌ `src/go/types/struct.go`
- ❌ `src/go/types/typexpr.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/parser/resolver.go`, `Visit`)
- ❌ (`src/go/parser/resolver.go`, `walkFuncType`)
- ❌ (`src/go/printer/nodes.go`, `signature`)
- ❌ (`src/go/printer/nodes.go`, `spec`)
- ❌ (`src/go/ast/walk.go`, `Walk`)
- ❌ (`src/go/types/decl.go`, `typeDecl`)
- ❌ (`src/go/types/decl.go`, `funcDecl`)
- ❌ (`src/go/types/signature.go`, `funcType`)
- ❌ (`src/go/types/interface.go`, `interfaceType`)
- ❌ (`src/go/parser/parser.go`, `parseMethodSpec`)
- ❌ (`src/go/parser/parser.go`, `parseGenericType`)
- ❌ (`src/go/parser/parser.go`, `parseFuncDecl`)
- ❌ (`src/go/types/resolver.go`, `collectObjects`)
- ❌ (`src/go/printer/nodes.go`, `expr1`)
- ❌ (`src/go/types/struct.go`, `embeddedFieldIdent`)
- ❌ (`src/go/types/expr.go`, `exprInternal`)
- ❌ (`src/go/types/resolver.go`, `unpackRecv`)
- ❌ (`src/go/types/exprstring.go`, `WriteExpr`)
- ❌ (`src/go/ast/walk.go`, `Walk`)
- ❌ (`src/go/types/typexpr.go`, `typInternal`)
- ❌ (`src/go/types/call.go`, `arguments`)
- ❌ (`src/go/parser/parser.go`, `parsePrimaryExpr`)
- ❌ (`src/cmd/cgo/ast_go1.go`, `walkUnexpected`)
- ❌ (`src/cmd/cgo/gcc.go`, `rewriteName`)
- ❌ (`src/cmd/cgo/ast_go118.go`, `walkUnexpected`)
- ❌ (`src/cmd/cgo/ast.go`, `walk`)

### 📊 Proposal #47916

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/noder`
- ✅ `src/cmd/compile/internal/types2`
- ✅ `src/go/types`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/noder/writer.go`
- ❌ `src/cmd/compile/internal/types2/call.go`
- ❌ `src/cmd/compile/internal/types2/lookup.go`
- ❌ `src/cmd/compile/internal/types2/signature.go`
- ❌ `src/go/types/api_test.go`
- ❌ `src/go/types/assignments.go`
- ❌ `src/go/types/call.go`
- ❌ `src/go/types/check.go`
- ❌ `src/go/types/context.go`
- ❌ `src/go/types/decl.go`
- ❌ `src/go/types/index.go`
- ✅ `src/go/types/instantiate.go`
- ❌ `src/go/types/instantiate_test.go`
- ❌ `src/go/types/lookup.go`
- ❌ `src/go/types/object.go`
- ❌ `src/go/types/predicates.go`
- ❌ `src/go/types/signature.go`
- ❌ `src/go/types/subst.go`
- ❌ `src/go/types/typelists.go`
- ❌ `src/go/types/typestring.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/noder`
- ✅ `src/cmd/compile/internal/types2`
- ✅ `src/go/types`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/noder/writer.go`
- ✅ `src/cmd/compile/internal/types2/call.go`
- ❌ `src/cmd/compile/internal/types2/lookup.go`
- ❌ `src/cmd/compile/internal/types2/signature.go`
- ✅ `src/go/types/api_test.go`
- ❌ `src/go/types/assignments.go`
- ❌ `src/go/types/call.go`
- ❌ `src/go/types/check.go`
- ❌ `src/go/types/context.go`
- ❌ `src/go/types/decl.go`
- ❌ `src/go/types/index.go`
- ❌ `src/go/types/instantiate.go`
- ❌ `src/go/types/instantiate_test.go`
- ❌ `src/go/types/lookup.go`
- ❌ `src/go/types/object.go`
- ❌ `src/go/types/predicates.go`
- ❌ `src/go/types/signature.go`
- ❌ `src/go/types/subst.go`
- ❌ `src/go/types/typelists.go`
- ❌ `src/go/types/typestring.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/types/subst.go`, `typ`)
- ❌ (`src/go/types/index.go`, `indexExpr`)
- ❌ (`src/go/types/decl.go`, `typeDecl`)
- ❌ (`src/go/types/typelists.go`, `bindTParams`)
- ❌ (`src/go/types/object.go`, `writeObject`)
- ❌ (`src/go/types/predicates.go`, `isGeneric`)
- ❌ (`src/go/types/predicates.go`, `identical`)
- ❌ (`src/go/types/lookup.go`, `missingMethod`)
- ❌ (`src/go/types/assignments.go`, `assignment`)
- ❌ (`src/go/types/typestring.go`, `typ`)
- ❌ (`src/go/types/typestring.go`, `signature`)
- ❌ (`src/go/types/instantiate.go`, `Instantiate`)
- ❌ (`src/go/types/instantiate.go`, `instance`)
- ❌ (`src/go/types/api_test.go`, `TestInstantiate`)
- ❌ (`src/go/types/signature.go`, `funcType`)
- ❌ (`src/go/types/call.go`, `funcInst`)
- ❌ (`src/go/types/call.go`, `callExpr`)
- ❌ (`src/go/types/call.go`, `arguments`)
- ❌ (`src/cmd/compile/internal/types2/signature.go`, `funcType`)
- ❌ (`src/go/types/signature.go`, `funcType`)
- ❌ (`src/cmd/compile/internal/noder/writer.go`, `method`)
- ❌ (`src/cmd/compile/internal/noder/writer.go`, `pkgDecl`)
- ❌ (`src/cmd/compile/internal/noder/writer.go`, `objTypeParams`)
- ❌ (`src/go/types/call.go`, `selector`)
- ❌ (`src/cmd/compile/internal/types2/call.go`, `selector`)
- ❌ (`src/go/types/lookup.go`, `missingMethod`)
- ❌ (`src/cmd/compile/internal/types2/lookup.go`, `missingMethod`)
- ❌ (`src/go/types/subst.go`, `subst`)
- ❌ (`src/go/types/subst.go`, `typ`)
- ❌ (`src/go/types/instantiate.go`, `Instantiate`)
- ❌ (`src/go/types/instantiate.go`, `instance`)
- ❌ (`src/go/types/instantiate_test.go`, `TestInstantiateEquality`)
- ❌ (`src/go/types/instantiate_test.go`, `TestInstantiateNonEquality`)
- ❌ (`src/go/types/context.go`, `NewContext`)
- ❌ (`src/go/types/typestring.go`, `newTypeHasher`)
- ❌ (`src/go/types/typestring.go`, `error`)
- ❌ (`src/go/types/typestring.go`, `typ`)
- ❌ (`src/go/types/typestring.go`, `tuple`)
- ❌ (`src/go/types/typestring.go`, `signature`)
- ❌ (`src/go/types/check.go`, `NewChecker`)

### 📊 Proposal #48052

#### File Embeddings - Directory Level
- ❌ `src/debug/plan9obj`

#### File Embeddings - File Level
- ❌ `src/debug/plan9obj/file.go`

#### Function Embeddings - Directory Level
- ✅ `src/debug/plan9obj`

#### Function Embeddings - File Level
- ✅ `src/debug/plan9obj/file.go`

#### Function Embeddings - Function Level
- ✅ (`src/debug/plan9obj/file.go`, `Symbols`)

### 📊 Proposal #48152

#### File Embeddings - Directory Level
- ✅ `src/crypto/tls`
- ❌ `src/net/http`

#### File Embeddings - File Level
- ❌ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ❌ `src/net/http/transport_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/tls`
- ❌ `src/net/http`

#### Function Embeddings - File Level
- ✅ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ❌ `src/net/http/transport_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/crypto/tls/common.go`, `Error`)
- ❌ (`src/crypto/tls/common.go`, `Unwrap`)
- ✅ (`src/crypto/tls/handshake_server.go`, `processCertsFromClient`)
- ❌ (`src/net/http/transport_test.go`, `testTransportEventTraceTLSVerify`)
- ❌ (`src/crypto/tls/handshake_client.go`, `verifyServerCertificate`)

### 📊 Proposal #48157

#### File Embeddings - Directory Level
- ❌ `src/internal/fuzz`
- ❌ `src/internal/testenv`
- ✅ `src/runtime`

#### File Embeddings - File Level
- ❌ `src/internal/fuzz/minimize_test.go`
- ❌ `src/internal/fuzz/worker.go`
- ❌ `src/internal/fuzz/worker_test.go`
- ❌ `src/internal/testenv/testenv.go`
- ❌ `src/runtime/crash_test.go`
- ❌ `src/runtime/runtime-gdb_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/internal/fuzz`
- ❌ `src/internal/testenv`
- ❌ `src/runtime`

#### Function Embeddings - File Level
- ❌ `src/internal/fuzz/minimize_test.go`
- ❌ `src/internal/fuzz/worker.go`
- ❌ `src/internal/fuzz/worker_test.go`
- ❌ `src/internal/testenv/testenv.go`
- ❌ `src/runtime/crash_test.go`
- ❌ `src/runtime/runtime-gdb_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/internal/fuzz/worker_test.go`, `BenchmarkWorkerFuzzOverhead`)
- ❌ (`src/internal/fuzz/minimize_test.go`, `TestMinimizeInput`)
- ❌ (`src/internal/fuzz/minimize_test.go`, `TestMinimizeFlaky`)
- ❌ (`src/internal/fuzz/worker.go`, `coordinate`)
- ❌ (`src/internal/fuzz/worker.go`, `minimize`)
- ❌ (`src/internal/fuzz/worker.go`, `RunFuzzWorker`)
- ❌ (`src/internal/fuzz/worker.go`, `fuzz`)
- ❌ (`src/internal/fuzz/worker.go`, `minimizeInput`)
- ❌ (`src/internal/testenv/testenv.go`, `WriteImportcfg`)
- ❌ (`src/runtime/crash_test.go`, `runBuiltTestProg`)
- ❌ (`src/runtime/runtime-gdb_test.go`, `TestGdbBacktrace`)

### 📊 Proposal #48187

#### File Embeddings - Directory Level
- ✅ `src/cmd/go/internal/version`
- ❌ `src/debug/buildinfo`

#### File Embeddings - File Level
- ✅ `src/cmd/go/internal/version/version.go`
- ❌ `src/debug/buildinfo/buildinfo_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/version`
- ❌ `src/debug/buildinfo`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/version/version.go`
- ❌ `src/debug/buildinfo/buildinfo_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/debug/buildinfo/buildinfo_test.go`, `TestReadFile`)
- ❌ (`src/cmd/go/internal/version/version.go`, `scanDir`)
- ❌ (`src/cmd/go/internal/version/version.go`, `isGoBinaryCandidate`)
- ❌ (`src/cmd/go/internal/version/version.go`, `scanFile`)

### 📊 Proposal #48218

#### File Embeddings - Directory Level
- ✅ `src/reflect`

#### File Embeddings - File Level
- ✅ `src/reflect/value.go`
- ❌ `src/reflect/visiblefields_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/reflect`

#### Function Embeddings - File Level
- ✅ `src/reflect/value.go`
- ❌ `src/reflect/visiblefields_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/reflect/visiblefields_test.go`, `TestFieldByIndexErr`)
- ✅ (`src/reflect/value.go`, `FieldByIndexErr`)

### 📊 Proposal #48256

#### File Embeddings - Directory Level
- ✅ `src/cmd/go`
- ✅ `src/cmd/go/internal/workcmd`

#### File Embeddings - File Level
- ✅ `src/cmd/go/internal/workcmd/edit.go`
- ✅ `src/cmd/go/internal/workcmd/init.go`
- ✅ `src/cmd/go/main.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go`
- ✅ `src/cmd/go/internal/workcmd`

#### Function Embeddings - File Level
- ✅ `src/cmd/go/internal/workcmd/edit.go`
- ✅ `src/cmd/go/internal/workcmd/init.go`
- ❌ `src/cmd/go/main.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/main.go`, `init`)
- ❌ (`src/cmd/go/internal/workcmd/edit.go`, `init`)
- ❌ (`src/cmd/go/internal/workcmd/edit.go`, `runEditwork`)
- ❌ (`src/cmd/go/internal/workcmd/edit.go`, `allowedVersionArg`)
- ❌ (`src/cmd/go/internal/workcmd/edit.go`, `parsePathVersionOptional`)
- ❌ (`src/cmd/go/internal/workcmd/edit.go`, `flagEditworkReplace`)
- ❌ (`src/cmd/go/internal/workcmd/init.go`, `init`)

### 📊 Proposal #48257

#### File Embeddings - Directory Level
- ✅ `src/cmd/go/internal/workcmd`

#### File Embeddings - File Level
- ✅ `src/cmd/go/internal/workcmd/use.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/go/internal/workcmd`

#### Function Embeddings - File Level
- ✅ `src/cmd/go/internal/workcmd/use.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/workcmd/use.go`, `init`)
- ✅ (`src/cmd/go/internal/workcmd/use.go`, `runUse`)
- ✅ (`src/cmd/go/internal/workcmd/use.go`, `runUse`)

### 📊 Proposal #48294

#### File Embeddings - Directory Level
- ❌ `src/reflect`

#### File Embeddings - File Level
- ❌ `src/reflect/all_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/reflect`

#### Function Embeddings - File Level
- ✅ `src/reflect/all_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/reflect/all_test.go`, `TestMapIterSet`)
- ❌ (`src/reflect/all_test.go`, `TestMapIterReset`)
- ❌ (`src/reflect/all_test.go`, `TestSetIter`)

### 📊 Proposal #48409

#### File Embeddings - Directory Level
- ✅ `src/runtime`
- ❌ `src/runtime/debug`
- ❌ `src/runtime/testdata/testprog`

#### File Embeddings - File Level
- ❌ `src/runtime/debug/garbage.go`
- ❌ `src/runtime/debug/stubs.go`
- ❌ `src/runtime/debuglog.go`
- ❌ `src/runtime/export_test.go`
- ❌ `src/runtime/gc_test.go`
- ❌ `src/runtime/malloc.go`
- ❌ `src/runtime/mcache.go`
- ❌ `src/runtime/mem.go`
- ❌ `src/runtime/metrics.go`
- ❌ `src/runtime/mgc.go`
- ❌ `src/runtime/mgclimit.go`
- ❌ `src/runtime/mgclimit_test.go`
- ❌ `src/runtime/mgcmark.go`
- ❌ `src/runtime/mgcpacer.go`
- ❌ `src/runtime/mgcpacer_test.go`
- ❌ `src/runtime/mgcscavenge.go`
- ❌ `src/runtime/mgcscavenge_test.go`
- ❌ `src/runtime/mgcsweep.go`
- ❌ `src/runtime/mheap.go`
- ❌ `src/runtime/mpagealloc.go`
- ❌ `src/runtime/mpagealloc_32bit.go`
- ❌ `src/runtime/mpagealloc_64bit.go`
- ❌ `src/runtime/mranges.go`
- ❌ `src/runtime/mstats.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/string.go`
- ❌ `src/runtime/string_test.go`
- ❌ `src/runtime/testdata/testprog/gc.go`

#### Function Embeddings - Directory Level
- ✅ `src/runtime`
- ❌ `src/runtime/debug`
- ✅ `src/runtime/testdata/testprog`

#### Function Embeddings - File Level
- ❌ `src/runtime/debug/garbage.go`
- ❌ `src/runtime/debug/stubs.go`
- ❌ `src/runtime/debuglog.go`
- ✅ `src/runtime/export_test.go`
- ❌ `src/runtime/gc_test.go`
- ❌ `src/runtime/malloc.go`
- ❌ `src/runtime/mcache.go`
- ❌ `src/runtime/mem.go`
- ❌ `src/runtime/metrics.go`
- ❌ `src/runtime/mgc.go`
- ❌ `src/runtime/mgclimit.go`
- ❌ `src/runtime/mgclimit_test.go`
- ❌ `src/runtime/mgcmark.go`
- ❌ `src/runtime/mgcpacer.go`
- ❌ `src/runtime/mgcpacer_test.go`
- ❌ `src/runtime/mgcscavenge.go`
- ❌ `src/runtime/mgcscavenge_test.go`
- ❌ `src/runtime/mgcsweep.go`
- ❌ `src/runtime/mheap.go`
- ❌ `src/runtime/mpagealloc.go`
- ❌ `src/runtime/mpagealloc_32bit.go`
- ❌ `src/runtime/mpagealloc_64bit.go`
- ❌ `src/runtime/mranges.go`
- ❌ `src/runtime/mstats.go`
- ❌ `src/runtime/proc.go`
- ❌ `src/runtime/string.go`
- ❌ `src/runtime/string_test.go`
- ✅ `src/runtime/testdata/testprog/gc.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/mgclimit_test.go`, `TestGCCPULimiter`)
- ❌ (`src/runtime/proc.go`, `findRunnable`)
- ❌ (`src/runtime/proc.go`, `procresize`)
- ❌ (`src/runtime/mgcpacer.go`, `startCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `endCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `enlistWorker`)
- ❌ (`src/runtime/mgcpacer.go`, `findRunnableGCWorker`)
- ❌ (`src/runtime/mgclimit.go`, `limiting`)
- ❌ (`src/runtime/mgclimit.go`, `startGCTransition`)
- ❌ (`src/runtime/mgclimit.go`, `finishGCTransition`)
- ❌ (`src/runtime/mgclimit.go`, `needUpdate`)
- ❌ (`src/runtime/mgclimit.go`, `update`)
- ❌ (`src/runtime/mgclimit.go`, `updateLocked`)
- ❌ (`src/runtime/mgclimit.go`, `accumulate`)
- ❌ (`src/runtime/mgclimit.go`, `tryLock`)
- ❌ (`src/runtime/mgclimit.go`, `unlock`)
- ❌ (`src/runtime/mgclimit.go`, `resetCapacity`)
- ❌ (`src/runtime/mgc.go`, `gcStart`)
- ❌ (`src/runtime/mgc.go`, `gcMarkDone`)
- ❌ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ❌ (`src/runtime/mgcmark.go`, `gcAssistAlloc`)
- ❌ (`src/runtime/mgcmark.go`, `gcAssistAlloc1`)
- ❌ (`src/runtime/export_test.go`, `EndCycle`)
- ❌ (`src/runtime/export_test.go`, `NewGCCPULimiter`)
- ❌ (`src/runtime/export_test.go`, `Fill`)
- ❌ (`src/runtime/export_test.go`, `Capacity`)
- ❌ (`src/runtime/export_test.go`, `Overflow`)
- ❌ (`src/runtime/export_test.go`, `Limiting`)
- ❌ (`src/runtime/export_test.go`, `NeedUpdate`)
- ❌ (`src/runtime/export_test.go`, `StartGCTransition`)
- ❌ (`src/runtime/export_test.go`, `FinishGCTransition`)
- ❌ (`src/runtime/export_test.go`, `Update`)
- ❌ (`src/runtime/export_test.go`, `ResetCapacity`)
- ❌ (`src/runtime/string_test.go`, `TestParseByteCount`)
- ❌ (`src/runtime/string.go`, `parseByteCount`)
- ❌ (`src/runtime/debug/stubs.go`, `setMemoryLimit`)
- ❌ (`src/runtime/mgcpacer.go`, `init`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgcpacer.go`, `setMemoryLimit`)
- ❌ (`src/runtime/mgcpacer.go`, `setMemoryLimit`)
- ❌ (`src/runtime/mgcpacer.go`, `readGOMEMLIMIT`)
- ❌ (`src/runtime/mgc.go`, `gcinit`)
- ❌ (`src/runtime/export_test.go`, `NewGCController`)
- ❌ (`src/runtime/malloc.go`, `sysAlloc`)
- ❌ (`src/runtime/malloc.go`, `sysReserveAligned`)
- ❌ (`src/runtime/malloc.go`, `alloc`)
- ❌ (`src/runtime/debuglog.go`, `dlog`)
- ❌ (`src/runtime/debuglog.go`, `printDebugLog`)
- ❌ (`src/runtime/mheap.go`, `allocSpan`)
- ❌ (`src/runtime/mpagealloc.go`, `init`)
- ❌ (`src/runtime/mem.go`, `sysAlloc`)
- ❌ (`src/runtime/mem.go`, `sysUnused`)
- ❌ (`src/runtime/mem.go`, `sysUsed`)
- ❌ (`src/runtime/mem.go`, `sysFree`)
- ❌ (`src/runtime/mem.go`, `sysFault`)
- ❌ (`src/runtime/mpagealloc_32bit.go`, `sysInit`)
- ❌ (`src/runtime/mpagealloc_64bit.go`, `sysGrow`)
- ❌ (`src/runtime/mstats.go`, `readmemstats_m`)
- ❌ (`src/runtime/export_test.go`, `NewAddrRanges`)
- ❌ (`src/runtime/export_test.go`, `MakeAddrRanges`)
- ❌ (`src/runtime/export_test.go`, `NewPageAlloc`)
- ❌ (`src/runtime/export_test.go`, `FreePageAlloc`)
- ❌ (`src/runtime/mcache.go`, `refill`)
- ❌ (`src/runtime/mcache.go`, `allocLarge`)
- ❌ (`src/runtime/mcache.go`, `releaseAll`)
- ❌ (`src/runtime/mgcsweep.go`, `sweep`)
- ❌ (`src/runtime/mstats.go`, `readmemstats_m`)
- ❌ (`src/runtime/mgcpacer_test.go`, `TestGcPacer`)
- ❌ (`src/runtime/mgcpacer_test.go`, `triggerRatio`)
- ❌ (`src/runtime/mgcpacer_test.go`, `TestIdleMarkWorkerCount`)
- ❌ (`src/runtime/mgcpacer.go`, `init`)
- ❌ (`src/runtime/mgcpacer.go`, `heapGoalInternal`)
- ❌ (`src/runtime/mgcpacer.go`, `memoryLimitHeapGoal`)
- ❌ (`src/runtime/mgcpacer.go`, `trigger`)
- ❌ (`src/runtime/mgcpacer.go`, `commit`)
- ❌ (`src/runtime/mgcpacer.go`, `gcControllerCommit`)
- ❌ (`src/runtime/export_test.go`, `NewGCController`)
- ❌ (`src/runtime/export_test.go`, `StartCycle`)
- ❌ (`src/runtime/mgcpacer_test.go`, `TestGcPacer`)
- ❌ (`src/runtime/metrics.go`, `compute`)
- ❌ (`src/runtime/mgcpacer.go`, `init`)
- ❌ (`src/runtime/mgcpacer.go`, `startCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `revise`)
- ❌ (`src/runtime/mgcpacer.go`, `endCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `resetLive`)
- ❌ (`src/runtime/mgcpacer.go`, `addScannableStack`)
- ❌ (`src/runtime/mgcpacer.go`, `addGlobals`)
- ❌ (`src/runtime/mgcpacer.go`, `heapGoal`)
- ❌ (`src/runtime/mgcpacer.go`, `heapGoalInternal`)
- ❌ (`src/runtime/mgcpacer.go`, `trigger`)
- ❌ (`src/runtime/mgcpacer.go`, `commit`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgcpacer.go`, `setGCPercent`)
- ❌ (`src/runtime/mgcpacer.go`, `setMemoryLimit`)
- ❌ (`src/runtime/mgcpacer.go`, `gcControllerCommit`)
- ❌ (`src/runtime/mgc.go`, `test`)
- ❌ (`src/runtime/mgc.go`, `gcStart`)
- ❌ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ❌ (`src/runtime/mstats.go`, `readmemstats_m`)
- ❌ (`src/runtime/export_test.go`, `StartCycle`)
- ❌ (`src/runtime/export_test.go`, `HeapGoal`)
- ❌ (`src/runtime/export_test.go`, `Triggered`)
- ❌ (`src/runtime/export_test.go`, `EndCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `trigger`)
- ❌ (`src/runtime/mgcscavenge.go`, `wake`)
- ❌ (`src/runtime/proc.go`, `empty`)
- ❌ (`src/runtime/proc.go`, `findRunnable`)
- ❌ (`src/runtime/proc.go`, `sysmon`)
- ❌ (`src/runtime/mgcsweep.go`, `sweepone`)
- ❌ (`src/runtime/mgc.go`, `gcenable`)
- ❌ (`src/runtime/mgc.go`, `test`)
- ❌ (`src/runtime/mgc.go`, `gcStart`)
- ❌ (`src/runtime/mgcscavenge.go`, `gcPaceScavenger`)
- ❌ (`src/runtime/mgcscavenge.go`, `init`)
- ❌ (`src/runtime/mheap.go`, `allocSpan`)
- ❌ (`src/runtime/mgcpacer.go`, `gcControllerCommit`)
- ❌ (`src/runtime/mgcmark.go`, `gcAssistAlloc1`)
- ❌ (`src/runtime/testdata/testprog/gc.go`, `init`)
- ❌ (`src/runtime/testdata/testprog/gc.go`, `GCMemoryLimit`)
- ❌ (`src/runtime/testdata/testprog/gc.go`, `GCMemoryLimitNoGCPercent`)
- ❌ (`src/runtime/testdata/testprog/gc.go`, `gcMemoryLimit`)
- ❌ (`src/runtime/debug/garbage.go`, `SetMemoryLimit`)
- ❌ (`src/runtime/gc_test.go`, `TestMemoryLimit`)
- ❌ (`src/runtime/gc_test.go`, `TestMemoryLimitNoGCPercent`)
- ❌ (`src/runtime/mgc.go`, `gcinit`)
- ❌ (`src/runtime/mgcscavenge.go`, `heapRetained`)
- ❌ (`src/runtime/mgcscavenge.go`, `gcPaceScavenger`)
- ❌ (`src/runtime/mgcscavenge.go`, `printScavTrace`)
- ❌ (`src/runtime/malloc.go`, `sysAlloc`)
- ❌ (`src/runtime/mheap.go`, `allocSpan`)
- ❌ (`src/runtime/mheap.go`, `grow`)
- ❌ (`src/runtime/mheap.go`, `freeSpanLocked`)
- ❌ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ❌ (`src/runtime/mstats.go`, `readmemstats_m`)
- ❌ (`src/runtime/mgcscavenge.go`, `heapRetained`)
- ❌ (`src/runtime/mgcscavenge.go`, `printScavTrace`)
- ❌ (`src/runtime/malloc.go`, `sysAlloc`)
- ❌ (`src/runtime/mcache.go`, `refill`)
- ❌ (`src/runtime/mcache.go`, `allocLarge`)
- ❌ (`src/runtime/mcache.go`, `releaseAll`)
- ❌ (`src/runtime/mheap.go`, `allocSpan`)
- ❌ (`src/runtime/mheap.go`, `grow`)
- ❌ (`src/runtime/mheap.go`, `freeSpanLocked`)
- ❌ (`src/runtime/mem.go`, `sysAlloc`)
- ❌ (`src/runtime/mem.go`, `sysUnused`)
- ❌ (`src/runtime/mem.go`, `sysUsed`)
- ❌ (`src/runtime/mem.go`, `sysFree`)
- ❌ (`src/runtime/mem.go`, `sysFault`)
- ❌ (`src/runtime/mgcsweep.go`, `sweep`)
- ❌ (`src/runtime/mgc.go`, `gcMarkTermination`)
- ❌ (`src/runtime/mstats.go`, `readmemstats_m`)
- ❌ (`src/runtime/export_test.go`, `FreePageAlloc`)
- ❌ (`src/runtime/mheap.go`, `allocSpan`)
- ❌ (`src/runtime/mgcsweep.go`, `sweep`)
- ❌ (`src/runtime/mgcpacer_test.go`, `TestGcPacer`)
- ❌ (`src/runtime/mgcpacer_test.go`, `runway`)
- ❌ (`src/runtime/mgcpacer_test.go`, `triggerRatio`)
- ❌ (`src/runtime/mgcpacer.go`, `commit`)
- ❌ (`src/runtime/mgcpacer.go`, `init`)
- ❌ (`src/runtime/mgcpacer.go`, `startCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `endCycle`)
- ❌ (`src/runtime/mgcpacer.go`, `enlistWorker`)
- ❌ (`src/runtime/mgcscavenge.go`, `heapRetained`)
- ❌ (`src/runtime/mgcscavenge.go`, `scavenge`)
- ❌ (`src/runtime/mgcscavenge.go`, `printScavTrace`)
- ❌ (`src/runtime/mgcscavenge.go`, `scavengeOne`)
- ❌ (`src/runtime/mgcscavenge.go`, `fillAligned`)
- ❌ (`src/runtime/mgcscavenge.go`, `findScavengeCandidate`)
- ❌ (`src/runtime/mgcscavenge.go`, `find`)
- ❌ (`src/runtime/mheap.go`, `scavengeAll`)
- ❌ (`src/runtime/mheap.go`, `runtime_debug_freeOSMemory`)
- ❌ (`src/runtime/mpagealloc.go`, `grow`)
- ❌ (`src/runtime/mpagealloc.go`, `free`)
- ❌ (`src/runtime/mgcscavenge_test.go`, `TestScavengeIndex`)
- ❌ (`src/runtime/mpagealloc_32bit.go`, `sysInit`)
- ❌ (`src/runtime/mgcsweep.go`, `sweepone`)
- ❌ (`src/runtime/mpagealloc_64bit.go`, `sysInit`)
- ❌ (`src/runtime/mpagealloc_64bit.go`, `sysGrow`)
- ❌ (`src/runtime/mranges.go`, `Clear`)
- ❌ (`src/runtime/mranges.go`, `StoreMin`)
- ❌ (`src/runtime/mranges.go`, `StoreUnmark`)
- ❌ (`src/runtime/mranges.go`, `StoreMarked`)
- ❌ (`src/runtime/mranges.go`, `Load`)
- ❌ (`src/runtime/export_test.go`, `NewPageAlloc`)
- ❌ (`src/runtime/export_test.go`, `FreePageAlloc`)
- ❌ (`src/runtime/export_test.go`, `NewScavengeIndex`)
- ❌ (`src/runtime/export_test.go`, `Find`)
- ❌ (`src/runtime/metrics.go`, `initMetrics`)
- ❌ (`src/runtime/mgclimit.go`, `accumulate`)
- ❌ (`src/runtime/mgclimit.go`, `resetCapacity`)

### 📊 Proposal #48424

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/syntax`
- ❌ `src/cmd/compile/internal/types2`
- ❌ `src/go/internal/gcimporter`
- ❌ `src/go/parser`
- ❌ `src/go/types`
- ✅ `test/typeparam`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/noder/noder.go`
- ❌ `src/cmd/compile/internal/syntax/error_test.go`
- ❌ `src/cmd/compile/internal/syntax/parser.go`
- ❌ `src/cmd/compile/internal/syntax/parser_test.go`
- ❌ `src/cmd/compile/internal/syntax/printer_test.go`
- ❌ `src/cmd/compile/internal/types2/check_test.go`
- ❌ `src/cmd/compile/internal/types2/decl.go`
- ❌ `src/cmd/compile/internal/types2/interface.go`
- ❌ `src/cmd/compile/internal/types2/typeparam.go`
- ❌ `src/cmd/compile/internal/types2/typestring.go`
- ❌ `src/cmd/compile/internal/types2/universe.go`
- ❌ `src/go/internal/gcimporter/gcimporter_test.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/types/decl.go`
- ❌ `src/go/types/interface.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/go/types/typestring.go`
- ❌ `src/go/types/universe.go`
- ❌ `test/typeparam/issue48424.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/syntax`
- ✅ `src/cmd/compile/internal/types2`
- ❌ `src/go/internal/gcimporter`
- ❌ `src/go/parser`
- ✅ `src/go/types`
- ✅ `test/typeparam`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/noder/noder.go`
- ❌ `src/cmd/compile/internal/syntax/error_test.go`
- ❌ `src/cmd/compile/internal/syntax/parser.go`
- ❌ `src/cmd/compile/internal/syntax/parser_test.go`
- ❌ `src/cmd/compile/internal/syntax/printer_test.go`
- ❌ `src/cmd/compile/internal/types2/check_test.go`
- ❌ `src/cmd/compile/internal/types2/decl.go`
- ❌ `src/cmd/compile/internal/types2/interface.go`
- ✅ `src/cmd/compile/internal/types2/typeparam.go`
- ❌ `src/cmd/compile/internal/types2/typestring.go`
- ❌ `src/cmd/compile/internal/types2/universe.go`
- ❌ `src/go/internal/gcimporter/gcimporter_test.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/types/decl.go`
- ❌ `src/go/types/interface.go`
- ✅ `src/go/types/typeparam.go`
- ❌ `src/go/types/typestring.go`
- ❌ `src/go/types/universe.go`
- ❌ `test/typeparam/issue48424.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `typeDecl`)
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `funcDeclOrNil`)
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `interfaceType`)
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `fieldDecl`)
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `methodDecl`)
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `paramDeclOrNil`)
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `paramList`)
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `nameList`)
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `qualifiedName`)
- ❌ (`src/cmd/compile/internal/syntax/parser_test.go`, `TestParse`)
- ❌ (`src/cmd/compile/internal/syntax/parser_test.go`, `TestVerify`)
- ❌ (`src/cmd/compile/internal/syntax/error_test.go`, `testSyntaxErrors`)
- ❌ (`src/cmd/compile/internal/syntax/printer_test.go`, `TestPrintString`)
- ❌ (`src/cmd/compile/internal/types2/decl.go`, `collectTypeParams`)
- ❌ (`src/cmd/compile/internal/types2/decl.go`, `bound`)
- ❌ (`src/cmd/compile/internal/types2/check_test.go`, `testFiles`)
- ❌ (`src/cmd/compile/internal/types2/typeparam.go`, `SetConstraint`)
- ✅ (`src/cmd/compile/internal/types2/typeparam.go`, `iface`)
- ❌ (`src/go/internal/gcimporter/gcimporter_test.go`, `TestImportTypeparamTests`)
- ❌ (`src/cmd/compile/internal/noder/noder.go`, `LoadPackage`)
- ❌ (`test/typeparam/issue48424.go`, `identity`)
- ❌ (`test/typeparam/issue48424.go`, `min`)
- ❌ (`test/typeparam/issue48424.go`, `max`)
- ❌ (`test/typeparam/issue48424.go`, `main`)
- ❌ (`src/cmd/compile/internal/types2/decl.go`, `bound`)
- ❌ (`src/cmd/compile/internal/types2/universe.go`, `defPredeclaredTypes`)
- ❌ (`src/cmd/compile/internal/types2/typestring.go`, `typ`)
- ✅ (`src/cmd/compile/internal/types2/typeparam.go`, `iface`)
- ❌ (`src/cmd/compile/internal/types2/interface.go`, `interfaceType`)
- ❌ (`src/go/parser/parser.go`, `parseQualifiedIdent`)
- ❌ (`src/go/parser/parser.go`, `parseArrayFieldOrTypeInstance`)
- ❌ (`src/go/parser/parser.go`, `parseParamDecl`)
- ❌ (`src/go/parser/parser.go`, `parseParameterList`)
- ❌ (`src/go/parser/parser.go`, `parseParameters`)
- ❌ (`src/go/parser/parser.go`, `parseFuncType`)
- ❌ (`src/go/parser/parser.go`, `parseMethodSpec`)
- ❌ (`src/go/parser/parser.go`, `embeddedElem`)
- ❌ (`src/go/parser/parser.go`, `embeddedTerm`)
- ❌ (`src/go/parser/parser.go`, `parseInterfaceType`)
- ❌ (`src/go/parser/parser.go`, `parseMapType`)
- ❌ (`src/go/parser/parser.go`, `parseTypeInstance`)
- ❌ (`src/go/parser/parser.go`, `tryIdentOrType`)
- ❌ (`src/go/parser/parser.go`, `parseIndexOrSliceOrInstance`)
- ❌ (`src/go/parser/parser.go`, `parseValueSpec`)
- ❌ (`src/go/parser/parser.go`, `parseGenericType`)
- ❌ (`src/go/parser/parser.go`, `parseTypeSpec`)
- ❌ (`src/cmd/compile/internal/types2/decl.go`, `collectTypeParams`)
- ❌ (`src/go/types/decl.go`, `collectTypeParams`)
- ❌ (`src/go/types/decl.go`, `bound`)
- ❌ (`src/go/types/typeparam.go`, `SetConstraint`)
- ✅ (`src/go/types/typeparam.go`, `iface`)
- ❌ (`src/go/internal/gcimporter/gcimporter_test.go`, `TestImportTypeparamTests`)
- ❌ (`src/go/types/decl.go`, `bound`)
- ❌ (`src/go/types/interface.go`, `interfaceType`)
- ❌ (`src/go/types/typestring.go`, `typ`)
- ✅ (`src/go/types/typeparam.go`, `iface`)
- ❌ (`src/go/types/universe.go`, `defPredeclaredTypes`)
- ❌ (`src/cmd/compile/internal/types2/check_test.go`, `testFiles`)
- ❌ (`src/cmd/compile/internal/noder/noder.go`, `LoadPackage`)
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `paramDeclOrNil`)
- ❌ (`src/cmd/compile/internal/syntax/parser_test.go`, `TestParse`)
- ❌ (`src/cmd/compile/internal/syntax/parser_test.go`, `TestVerify`)
- ❌ (`src/cmd/compile/internal/syntax/error_test.go`, `testSyntaxErrors`)
- ❌ (`src/cmd/compile/internal/syntax/printer_test.go`, `TestPrintString`)

### 📊 Proposal #48530

#### File Embeddings - Directory Level
- ✅ `src/net`

#### File Embeddings - File Level
- ❌ `src/net/net.go`
- ❌ `src/net/tcpsock.go`
- ❌ `src/net/tcpsock_plan9.go`
- ❌ `src/net/tcpsock_posix.go`

#### Function Embeddings - Directory Level
- ✅ `src/net`

#### Function Embeddings - File Level
- ❌ `src/net/net.go`
- ✅ `src/net/tcpsock.go`
- ❌ `src/net/tcpsock_plan9.go`
- ✅ `src/net/tcpsock_posix.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/tcpsock_plan9.go`, `writeTo`)
- ✅ (`src/net/tcpsock_posix.go`, `writeTo`)
- ❌ (`src/net/net.go`, `genericWriteTo`)
- ✅ (`src/net/tcpsock.go`, `WriteTo`)

### 📊 Proposal #48801

#### File Embeddings - Directory Level
- ✅ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat`
- ❌ `src/cmd/vet`

#### File Embeddings - File Level
- ✅ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`
- ❌ `src/cmd/vet/main.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat`
- ❌ `src/cmd/vet`

#### Function Embeddings - File Level
- ❌ `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`
- ❌ `src/cmd/vet/main.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/vet/main.go`, `main`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`, `run`)
- ❌ (`src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`, `badFormatAt`)

### 📊 Proposal #48866

#### File Embeddings - Directory Level
- ✅ `src/mime`

#### File Embeddings - File Level
- ❌ `src/mime/mediatype.go`
- ❌ `src/mime/mediatype_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/mime`

#### Function Embeddings - File Level
- ✅ `src/mime/mediatype.go`
- ❌ `src/mime/mediatype_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/mime/mediatype.go`, `ParseMediaType`)
- ❌ (`src/mime/mediatype_test.go`, `TestParseMediaType`)

### 📊 Proposal #49097

#### File Embeddings - Directory Level
- ✅ `src/net`

#### File Embeddings - File Level
- ❌ `src/net/dial.go`
- ❌ `src/net/iprawsock.go`
- ❌ `src/net/net.go`
- ❌ `src/net/tcpsock.go`
- ❌ `src/net/udpsock.go`
- ❌ `src/net/unixsock.go`

#### Function Embeddings - Directory Level
- ✅ `src/net`

#### Function Embeddings - File Level
- ✅ `src/net/dial.go`
- ✅ `src/net/iprawsock.go`
- ❌ `src/net/net.go`
- ✅ `src/net/tcpsock.go`
- ✅ `src/net/udpsock.go`
- ✅ `src/net/unixsock.go`

#### Function Embeddings - Function Level
- ✅ (`src/net/unixsock.go`, `DialUnix`)
- ❌ (`src/net/net.go`, `Error`)
- ❌ (`src/net/dial.go`, `DialContext`)
- ✅ (`src/net/iprawsock.go`, `DialIP`)
- ✅ (`src/net/unixsock.go`, `DialUnix`)
- ✅ (`src/net/tcpsock.go`, `DialTCP`)
- ✅ (`src/net/udpsock.go`, `DialUDP`)

### 📊 Proposal #49390

#### File Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ❌ `src/internal/testenv`

#### File Embeddings - File Level
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/internal/testenv/noopt.go`
- ❌ `src/internal/testenv/opt.go`
- ❌ `src/internal/testenv/testenv.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/dist`
- ✅ `src/internal/testenv`

#### Function Embeddings - File Level
- ❌ `src/cmd/dist/build.go`
- ✅ `src/cmd/dist/test.go`
- ❌ `src/internal/testenv/noopt.go`
- ❌ `src/internal/testenv/opt.go`
- ❌ `src/internal/testenv/testenv.go`

#### Function Embeddings - Function Level
- ❌ (`src/internal/testenv/noopt.go`, `OptimizationOff`)
- ❌ (`src/cmd/dist/build.go`, `cmdbootstrap`)
- ❌ (`src/cmd/dist/build.go`, `goCmd`)
- ❌ (`src/cmd/dist/build.go`, `checkNotStale`)
- ❌ (`src/cmd/dist/build.go`, `setNoOpt`)
- ❌ (`src/cmd/dist/test.go`, `cmdtest`)
- ❌ (`src/internal/testenv/opt.go`, `OptimizationOff`)
- ❌ (`src/internal/testenv/testenv.go`, `SkipIfOptimizationOff`)

### 📊 Proposal #49471

#### File Embeddings - Directory Level
- ✅ `src/runtime`

#### File Embeddings - File Level
- ❌ `src/runtime/os_windows.go`
- ❌ `src/runtime/panic.go`
- ❌ `src/runtime/signal_windows.go`

#### Function Embeddings - Directory Level
- ✅ `src/runtime`

#### Function Embeddings - File Level
- ✅ `src/runtime/os_windows.go`
- ❌ `src/runtime/panic.go`
- ❌ `src/runtime/signal_windows.go`

#### Function Embeddings - Function Level
- ❌ (`src/runtime/signal_windows.go`, `exceptionhandler`)
- ❌ (`src/runtime/signal_windows.go`, `lastcontinuehandler`)
- ❌ (`src/runtime/signal_windows.go`, `winthrow`)
- ❌ (`src/runtime/signal_windows.go`, `initsig`)
- ❌ (`src/runtime/signal_windows.go`, `sigenable`)
- ❌ (`src/runtime/signal_windows.go`, `crash`)
- ❌ (`src/runtime/panic.go`, `fatalthrow`)
- ❌ (`src/runtime/panic.go`, `fatalpanic`)
- ❌ (`src/runtime/os_windows.go`, `loadOptionalSyscalls`)
- ❌ (`src/runtime/signal_windows.go`, `lastcontinuetramp`)
- ❌ (`src/runtime/signal_windows.go`, `initExceptionHandler`)
- ❌ (`src/runtime/signal_windows.go`, `isAbort`)
- ❌ (`src/runtime/signal_windows.go`, `exceptionhandler`)
- ❌ (`src/runtime/signal_windows.go`, `winthrow`)
- ❌ (`src/runtime/signal_windows.go`, `crash`)
- ❌ (`src/runtime/panic.go`, `fatalthrow`)
- ❌ (`src/runtime/panic.go`, `fatalpanic`)
- ❌ (`src/runtime/os_windows.go`, `loadOptionalSyscalls`)

### 📊 Proposal #49580

#### File Embeddings - Directory Level
- ❌ `src/archive/tar`
- ✅ `src/io/fs`
- ❌ `src/os`
- ✅ `src/testing/fstest`

#### File Embeddings - File Level
- ❌ `src/archive/tar/writer.go`
- ❌ `src/archive/tar/writer_test.go`
- ✅ `src/io/fs/readlink.go`
- ✅ `src/io/fs/readlink_test.go`
- ❌ `src/io/fs/sub.go`
- ❌ `src/io/fs/walk_test.go`
- ❌ `src/os/dir.go`
- ❌ `src/os/file.go`
- ❌ `src/os/file_test.go`
- ❌ `src/os/os_test.go`
- ❌ `src/testing/fstest/mapfs.go`
- ❌ `src/testing/fstest/mapfs_test.go`
- ✅ `src/testing/fstest/testfs.go`
- ❌ `src/testing/fstest/testfs_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/archive/tar`
- ✅ `src/io/fs`
- ❌ `src/os`
- ❌ `src/testing/fstest`

#### Function Embeddings - File Level
- ❌ `src/archive/tar/writer.go`
- ❌ `src/archive/tar/writer_test.go`
- ✅ `src/io/fs/readlink.go`
- ✅ `src/io/fs/readlink_test.go`
- ✅ `src/io/fs/sub.go`
- ❌ `src/io/fs/walk_test.go`
- ❌ `src/os/dir.go`
- ❌ `src/os/file.go`
- ❌ `src/os/file_test.go`
- ❌ `src/os/os_test.go`
- ❌ `src/testing/fstest/mapfs.go`
- ❌ `src/testing/fstest/mapfs_test.go`
- ❌ `src/testing/fstest/testfs.go`
- ❌ `src/testing/fstest/testfs_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/os/os_test.go`, `TestCopyFSWithSymlinks`)
- ❌ (`src/testing/fstest/testfs_test.go`, `TestSymlink`)
- ✅ (`src/io/fs/readlink.go`, `ReadLink`)
- ❌ (`src/io/fs/readlink.go`, `Lstat`)
- ❌ (`src/os/file_test.go`, `TestDirFSReadLink`)
- ❌ (`src/os/file_test.go`, `TestDirFSLstat`)
- ❌ (`src/os/file_test.go`, `TestDirFSWalkDir`)
- ✅ (`src/io/fs/sub.go`, `ReadLink`)
- ❌ (`src/io/fs/sub.go`, `Lstat`)
- ❌ (`src/archive/tar/writer_test.go`, `TestWriterAddFS`)
- ❌ (`src/testing/fstest/testfs.go`, `checkDir`)
- ❌ (`src/testing/fstest/testfs.go`, `checkStat`)
- ❌ (`src/io/fs/walk_test.go`, `TestWalkDirSymlink`)
- ❌ (`src/os/dir.go`, `CopyFS`)
- ❌ (`src/testing/fstest/mapfs.go`, `Open`)
- ❌ (`src/testing/fstest/mapfs.go`, `resolveSymlinks`)
- ❌ (`src/testing/fstest/mapfs.go`, `ReadLink`)
- ❌ (`src/testing/fstest/mapfs.go`, `Lstat`)
- ❌ (`src/testing/fstest/mapfs.go`, `lstat`)
- ✅ (`src/io/fs/readlink_test.go`, `TestReadLink`)
- ❌ (`src/io/fs/readlink_test.go`, `TestLstat`)
- ❌ (`src/testing/fstest/mapfs_test.go`, `TestMapFSSymlink`)
- ❌ (`src/os/file.go`, `Lstat`)
- ❌ (`src/os/file.go`, `ReadLink`)
- ❌ (`src/archive/tar/writer.go`, `AddFS`)

### 📊 Proposal #50062

#### File Embeddings - Directory Level
- ✅ `src/time`

#### File Embeddings - File Level
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/time`

#### Function Embeddings - File Level
- ✅ `src/time/time.go`
- ✅ `src/time/time_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/time/time.go`, `ZoneBounds`)
- ✅ (`src/time/time_test.go`, `TestZoneBounds`)

### 📊 Proposal #50101

#### File Embeddings - Directory Level
- ❌ `src/internal/syscall/unix`
- ✅ `src/net`

#### File Embeddings - File Level
- ❌ `src/internal/syscall/unix/net_darwin.go`
- ❌ `src/net/cgo_unix.go`
- ❌ `src/net/cgo_unix_cgo_res.go`
- ❌ `src/net/cgo_unix_cgo_resn.go`
- ❌ `src/net/cgo_unix_syscall.go`
- ❌ `src/net/conf.go`
- ❌ `src/net/dnsclient.go`
- ❌ `src/net/dnsclient_unix.go`
- ❌ `src/net/dnsclient_unix_test.go`
- ❌ `src/net/lookup.go`
- ❌ `src/net/lookup_plan9.go`
- ❌ `src/net/lookup_unix.go`
- ✅ `src/net/lookup_windows.go`

#### Function Embeddings - Directory Level
- ❌ `src/internal/syscall/unix`
- ✅ `src/net`

#### Function Embeddings - File Level
- ❌ `src/internal/syscall/unix/net_darwin.go`
- ❌ `src/net/cgo_unix.go`
- ❌ `src/net/cgo_unix_cgo_res.go`
- ❌ `src/net/cgo_unix_cgo_resn.go`
- ❌ `src/net/cgo_unix_syscall.go`
- ❌ `src/net/conf.go`
- ❌ `src/net/dnsclient.go`
- ❌ `src/net/dnsclient_unix.go`
- ❌ `src/net/dnsclient_unix_test.go`
- ❌ `src/net/lookup.go`
- ❌ `src/net/lookup_plan9.go`
- ❌ `src/net/lookup_unix.go`
- ✅ `src/net/lookup_windows.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/conf.go`, `initConfVal`)
- ❌ (`src/net/cgo_unix_cgo_res.go`, `_C_res_ninit`)
- ❌ (`src/net/cgo_unix_cgo_res.go`, `_C_res_nclose`)
- ❌ (`src/net/cgo_unix_cgo_res.go`, `_C_res_nsearch`)
- ❌ (`src/net/cgo_unix_syscall.go`, `_C_res_ninit`)
- ❌ (`src/net/cgo_unix_syscall.go`, `_C_res_nsearch`)
- ❌ (`src/net/cgo_unix_syscall.go`, `_C_res_nclose`)
- ❌ (`src/net/dnsclient_unix_test.go`, `TestLongDNSNames`)
- ❌ (`src/net/cgo_unix.go`, `cgoLookupIP`)
- ❌ (`src/net/cgo_unix.go`, `cgoLookupCNAME`)
- ❌ (`src/net/cgo_unix.go`, `resSearch`)
- ❌ (`src/net/lookup.go`, `parseCNAMEFromResources`)
- ❌ (`src/net/cgo_unix_cgo_resn.go`, `_C_res_ninit`)
- ❌ (`src/net/cgo_unix_cgo_resn.go`, `_C_res_nclose`)
- ❌ (`src/net/cgo_unix_cgo_resn.go`, `_C_res_nsearch`)
- ❌ (`src/internal/syscall/unix/net_darwin.go`, `libresolv_res_9_ninit_trampoline`)
- ❌ (`src/internal/syscall/unix/net_darwin.go`, `ResNinit`)
- ❌ (`src/internal/syscall/unix/net_darwin.go`, `libresolv_res_9_nclose_trampoline`)
- ❌ (`src/internal/syscall/unix/net_darwin.go`, `ResNclose`)
- ❌ (`src/internal/syscall/unix/net_darwin.go`, `libresolv_res_9_nsearch_trampoline`)
- ❌ (`src/internal/syscall/unix/net_darwin.go`, `ResNsearch`)
- ❌ (`src/net/dnsclient_unix.go`, `goLookupIPCNAMEOrder`)
- ❌ (`src/net/dnsclient_unix.go`, `goLookupCNAME`)
- ❌ (`src/net/cgo_unix.go`, `cgoLookupCNAME`)
- ✅ (`src/net/lookup_windows.go`, `lookupCNAME`)
- ❌ (`src/net/cgo_unix_cgo_resn.go`, `_C_res_nsearch`)
- ❌ (`src/net/lookup_plan9.go`, `lookupCNAME`)
- ❌ (`src/net/cgo_unix_cgo_res.go`, `_C_res_nsearch`)
- ❌ (`src/net/cgo_unix_syscall.go`, `_C_res_nsearch`)
- ❌ (`src/net/dnsclient_unix_test.go`, `TestStrictErrorsLookupTXT`)
- ❌ (`src/net/cgo_unix.go`, `cgoLookupHostIP`)
- ❌ (`src/net/cgo_unix.go`, `cgoLookupIP`)
- ❌ (`src/net/cgo_unix.go`, `cgoSockaddr`)
- ❌ (`src/net/cgo_unix.go`, `cgoLookupCNAME`)
- ❌ (`src/net/cgo_unix.go`, `resSearch`)
- ❌ (`src/net/cgo_unix.go`, `cgoResSearch`)
- ❌ (`src/net/lookup_unix.go`, `lookupCNAME`)
- ❌ (`src/net/lookup.go`, `goLookupSRV`)
- ❌ (`src/net/lookup.go`, `goLookupMX`)
- ❌ (`src/net/lookup.go`, `goLookupNS`)
- ❌ (`src/net/lookup.go`, `goLookupTXT`)
- ❌ (`src/net/dnsclient.go`, `equalASCIIName`)
- ❌ (`src/net/dnsclient_unix.go`, `checkResponse`)
- ❌ (`src/net/dnsclient_unix.go`, `tryOneName`)
- ❌ (`src/net/dnsclient_unix.go`, `lookup`)
- ❌ (`src/net/dnsclient_unix.go`, `goLookupIPCNAMEOrder`)
- ❌ (`src/net/dnsclient_unix.go`, `goLookupCNAME`)
- ❌ (`src/net/dnsclient_unix.go`, `goLookupPTR`)

### 📊 Proposal #50102

#### File Embeddings - Directory Level
- ✅ `src/archive/tar`

#### File Embeddings - File Level
- ✅ `src/archive/tar/common.go`
- ❌ `src/archive/tar/stat_unix.go`
- ❌ `src/archive/tar/tar_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/archive/tar`

#### Function Embeddings - File Level
- ✅ `src/archive/tar/common.go`
- ❌ `src/archive/tar/stat_unix.go`
- ✅ `src/archive/tar/tar_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/archive/tar/common.go`, `FileInfoHeader`)
- ❌ (`src/archive/tar/stat_unix.go`, `init`)
- ❌ (`src/archive/tar/stat_unix.go`, `statUnix`)
- ✅ (`src/archive/tar/common.go`, `FileInfoHeader`)
- ❌ (`src/archive/tar/tar_test.go`, `Name`)
- ❌ (`src/archive/tar/tar_test.go`, `Size`)
- ❌ (`src/archive/tar/tar_test.go`, `Mode`)
- ❌ (`src/archive/tar/tar_test.go`, `ModTime`)
- ✅ (`src/archive/tar/tar_test.go`, `IsDir`)
- ❌ (`src/archive/tar/tar_test.go`, `Sys`)
- ❌ (`src/archive/tar/tar_test.go`, `Uname`)
- ❌ (`src/archive/tar/tar_test.go`, `Gname`)
- ❌ (`src/archive/tar/tar_test.go`, `TestFileInfoHeaderUseFileInfoNames`)
- ❌ (`src/archive/tar/stat_unix.go`, `init`)
- ✅ (`src/archive/tar/common.go`, `FileInfoHeader`)
- ❌ (`src/archive/tar/tar_test.go`, `Sys`)
- ❌ (`src/archive/tar/tar_test.go`, `Uname`)
- ❌ (`src/archive/tar/tar_test.go`, `Gname`)
- ❌ (`src/archive/tar/tar_test.go`, `TestFileInfoHeaderUseFileInfoNames`)
- ✅ (`src/archive/tar/common.go`, `FileInfoHeader`)
- ❌ (`src/archive/tar/common.go`, `isHeaderOnlyType`)

### 📊 Proposal #50332

#### File Embeddings - Directory Level
- ✅ `src/cmd/doc`
- ✅ `src/cmd/go`
- ❌ `src/cmd/go/internal/base`
- ❌ `src/cmd/go/internal/bug`
- ❌ `src/cmd/go/internal/envcmd`
- ❌ `src/cmd/go/internal/fmtcmd`
- ❌ `src/cmd/go/internal/modcmd`
- ❌ `src/cmd/go/internal/tool`
- ❌ `src/cmd/go/internal/version`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/go/internal/workcmd`

#### File Embeddings - File Level
- ❌ `src/cmd/doc/main.go`
- ✅ `src/cmd/go/chdir_test.go`
- ❌ `src/cmd/go/internal/base/flag.go`
- ❌ `src/cmd/go/internal/bug/bug.go`
- ❌ `src/cmd/go/internal/envcmd/env.go`
- ❌ `src/cmd/go/internal/fmtcmd/fmt.go`
- ❌ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modcmd/edit.go`
- ❌ `src/cmd/go/internal/modcmd/graph.go`
- ❌ `src/cmd/go/internal/modcmd/init.go`
- ❌ `src/cmd/go/internal/modcmd/tidy.go`
- ❌ `src/cmd/go/internal/modcmd/vendor.go`
- ❌ `src/cmd/go/internal/modcmd/verify.go`
- ❌ `src/cmd/go/internal/modcmd/why.go`
- ❌ `src/cmd/go/internal/tool/tool.go`
- ❌ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/workcmd/edit.go`
- ❌ `src/cmd/go/internal/workcmd/init.go`
- ❌ `src/cmd/go/internal/workcmd/sync.go`
- ❌ `src/cmd/go/internal/workcmd/use.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/doc`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/base`
- ❌ `src/cmd/go/internal/bug`
- ❌ `src/cmd/go/internal/envcmd`
- ❌ `src/cmd/go/internal/fmtcmd`
- ✅ `src/cmd/go/internal/modcmd`
- ❌ `src/cmd/go/internal/tool`
- ❌ `src/cmd/go/internal/version`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/go/internal/workcmd`

#### Function Embeddings - File Level
- ❌ `src/cmd/doc/main.go`
- ❌ `src/cmd/go/chdir_test.go`
- ❌ `src/cmd/go/internal/base/flag.go`
- ❌ `src/cmd/go/internal/bug/bug.go`
- ❌ `src/cmd/go/internal/envcmd/env.go`
- ❌ `src/cmd/go/internal/fmtcmd/fmt.go`
- ❌ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modcmd/edit.go`
- ❌ `src/cmd/go/internal/modcmd/graph.go`
- ❌ `src/cmd/go/internal/modcmd/init.go`
- ✅ `src/cmd/go/internal/modcmd/tidy.go`
- ❌ `src/cmd/go/internal/modcmd/vendor.go`
- ❌ `src/cmd/go/internal/modcmd/verify.go`
- ❌ `src/cmd/go/internal/modcmd/why.go`
- ❌ `src/cmd/go/internal/tool/tool.go`
- ❌ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/workcmd/edit.go`
- ❌ `src/cmd/go/internal/workcmd/init.go`
- ❌ `src/cmd/go/internal/workcmd/sync.go`
- ❌ `src/cmd/go/internal/workcmd/use.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/modcmd/download.go`, `init`)
- ❌ (`src/cmd/go/internal/tool/tool.go`, `init`)
- ❌ (`src/cmd/go/internal/workcmd/init.go`, `init`)
- ❌ (`src/cmd/go/internal/fmtcmd/fmt.go`, `init`)
- ❌ (`src/cmd/go/internal/modcmd/graph.go`, `init`)
- ❌ (`src/cmd/go/internal/bug/bug.go`, `init`)
- ❌ (`src/cmd/go/internal/workcmd/use.go`, `init`)
- ❌ (`src/cmd/go/chdir_test.go`, `TestChdir`)
- ❌ (`src/cmd/go/internal/modcmd/why.go`, `init`)
- ❌ (`src/cmd/go/internal/envcmd/env.go`, `init`)
- ❌ (`src/cmd/go/internal/modcmd/init.go`, `init`)
- ❌ (`src/cmd/go/internal/version/version.go`, `init`)
- ❌ (`src/cmd/go/internal/work/build.go`, `AddBuildFlags`)
- ❌ (`src/cmd/go/internal/base/flag.go`, `AddChdirFlag`)
- ❌ (`src/cmd/go/internal/modcmd/vendor.go`, `init`)
- ❌ (`src/cmd/go/internal/workcmd/edit.go`, `init`)
- ❌ (`src/cmd/go/internal/modcmd/edit.go`, `init`)
- ❌ (`src/cmd/go/internal/modcmd/tidy.go`, `init`)
- ❌ (`src/cmd/doc/main.go`, `do`)
- ❌ (`src/cmd/go/internal/modcmd/verify.go`, `init`)
- ❌ (`src/cmd/go/internal/workcmd/sync.go`, `init`)

### 📊 Proposal #50429

#### File Embeddings - Directory Level
- ❌ `src/go/parser`

#### File Embeddings - File Level
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/parser_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/go/parser`

#### Function Embeddings - File Level
- ❌ `src/go/parser/parser.go`
- ✅ `src/go/parser/parser_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/go/parser/parser_test.go`, `TestRangePos`)
- ❌ (`src/go/parser/parser.go`, `parseForStmt`)

### 📊 Proposal #50436

#### File Embeddings - Directory Level
- ❌ `src/os/exec`

#### File Embeddings - File Level
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/os/exec`

#### Function Embeddings - File Level
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/os/exec/exec.go`, `interfaceEqual`)
- ❌ (`src/os/exec/exec.go`, `argv`)
- ❌ (`src/os/exec/exec.go`, `childStdin`)
- ❌ (`src/os/exec/exec.go`, `childStdout`)
- ❌ (`src/os/exec/exec.go`, `childStderr`)
- ❌ (`src/os/exec/exec.go`, `writerDescriptor`)
- ❌ (`src/os/exec/exec.go`, `Start`)
- ❌ (`src/os/exec/exec.go`, `Wait`)
- ❌ (`src/os/exec/exec.go`, `CombinedOutput`)
- ❌ (`src/os/exec/exec.go`, `StdinPipe`)
- ❌ (`src/os/exec/exec.go`, `StdoutPipe`)
- ❌ (`src/os/exec/exec.go`, `StderrPipe`)
- ❌ (`src/os/exec/exec.go`, `CommandContext`)
- ❌ (`src/os/exec/exec.go`, `Start`)
- ❌ (`src/os/exec/exec.go`, `watchCtx`)
- ❌ (`src/os/exec/exec.go`, `Wait`)
- ❌ (`src/os/exec/exec.go`, `awaitGoroutines`)
- ❌ (`src/os/exec/exec_test.go`, `cmdHang`)
- ❌ (`src/os/exec/exec_test.go`, `newTickReader`)
- ❌ (`src/os/exec/exec_test.go`, `Read`)
- ❌ (`src/os/exec/exec_test.go`, `startHang`)
- ❌ (`src/os/exec/exec_test.go`, `TestWaitInterrupt`)
- ❌ (`src/os/exec/exec_test.go`, `TestCancelErrors`)
- ❌ (`src/os/exec/exec.go`, `childStdin`)
- ❌ (`src/os/exec/exec.go`, `writerDescriptor`)
- ❌ (`src/os/exec/exec.go`, `Start`)
- ❌ (`src/os/exec/exec.go`, `Wait`)
- ❌ (`src/os/exec/exec.go`, `StdinPipe`)
- ❌ (`src/os/exec/exec.go`, `StdoutPipe`)
- ❌ (`src/os/exec/exec.go`, `StderrPipe`)
- ❌ (`src/os/exec/exec.go`, `CommandContext`)
- ❌ (`src/os/exec/exec.go`, `Start`)
- ❌ (`src/os/exec/exec.go`, `watchCtx`)
- ❌ (`src/os/exec/exec.go`, `Error`)
- ❌ (`src/os/exec/exec.go`, `Unwrap`)
- ❌ (`src/os/exec/exec.go`, `Start`)
- ❌ (`src/os/exec/exec.go`, `Wait`)
- ❌ (`src/os/exec/exec.go`, `watchCtx`)

### 📊 Proposal #50465

#### File Embeddings - Directory Level
- ✅ `src/net/http/httputil`

#### File Embeddings - File Level
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/http/httputil`

#### Function Embeddings - File Level
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/http/httputil/reverseproxy_test.go`, `TestReverseProxy`)
- ✅ (`src/net/http/httputil/reverseproxy_test.go`, `TestXForwardedFor`)
- ✅ (`src/net/http/httputil/reverseproxy_test.go`, `TestXForwardedFor_Omit`)
- ❌ (`src/net/http/httputil/reverseproxy_test.go`, `TestServeHTTPDeepCopy`)
- ❌ (`src/net/http/httputil/reverseproxy_test.go`, `TestClonesRequestHeaders`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `ServeHTTP`)
- ❌ (`src/net/http/httputil/reverseproxy_test.go`, `TestReverseProxy`)
- ✅ (`src/net/http/httputil/reverseproxy_test.go`, `TestXForwardedFor`)
- ✅ (`src/net/http/httputil/reverseproxy_test.go`, `TestXForwardedFor_Omit`)
- ✅ (`src/net/http/httputil/reverseproxy_test.go`, `TestReverseProxyRewriteStripsForwarded`)
- ❌ (`src/net/http/httputil/reverseproxy_test.go`, `TestModifyResponseClosesBody`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `ServeHTTP`)

### 📊 Proposal #50489

#### File Embeddings - Directory Level
- ✅ `src/math/big`

#### File Embeddings - File Level
- ❌ `src/math/big/ratconv.go`
- ❌ `src/math/big/ratconv_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/math/big`

#### Function Embeddings - File Level
- ❌ `src/math/big/ratconv.go`
- ❌ `src/math/big/ratconv_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/math/big/ratconv_test.go`, `TestFloatPrec`)
- ❌ (`src/math/big/ratconv_test.go`, `BenchmarkFloatPrecExact`)
- ❌ (`src/math/big/ratconv_test.go`, `BenchmarkFloatPrecInexact`)
- ❌ (`src/math/big/ratconv.go`, `FloatPrec`)

### 📊 Proposal #50599

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/internal/moddeps`
- ❌ `src/go/build`
- ✅ `src/os/exec`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/vcs/vcs.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/internal/moddeps/moddeps_test.go`
- ❌ `src/go/build/build.go`
- ❌ `src/os/exec/env_test.go`
- ❌ `src/os/exec/example_test.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_linux_test.go`
- ❌ `src/os/exec/exec_posix_test.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/exec_windows_test.go`
- ❌ `src/os/exec/lp_windows_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/work`
- ❌ `src/cmd/internal/moddeps`
- ❌ `src/go/build`
- ✅ `src/os/exec`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/vcs/vcs.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/internal/moddeps/moddeps_test.go`
- ❌ `src/go/build/build.go`
- ❌ `src/os/exec/env_test.go`
- ❌ `src/os/exec/example_test.go`
- ✅ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_linux_test.go`
- ✅ `src/os/exec/exec_posix_test.go`
- ✅ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/exec_windows_test.go`
- ❌ `src/os/exec/lp_windows_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/build/build.go`, `importGo`)
- ❌ (`src/os/exec/env_test.go`, `TestDedupEnv`)
- ❌ (`src/os/exec/exec.go`, `dedupEnvCase`)
- ❌ (`src/os/exec/example_test.go`, `ExampleCmd_Environ`)
- ❌ (`src/os/exec/exec.go`, `argv`)
- ❌ (`src/os/exec/exec.go`, `Start`)
- ✅ (`src/os/exec/exec.go`, `environ`)
- ❌ (`src/os/exec/exec.go`, `Environ`)
- ❌ (`src/os/exec/exec_posix_test.go`, `TestImplicitPWD`)
- ✅ (`src/os/exec/exec_posix_test.go`, `TestExplicitPWD`)
- ❌ (`src/os/exec/exec_test.go`, `helperCommandContext`)
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `run1`)
- ❌ (`src/cmd/go/internal/work/exec.go`, `gccSupportsFlag`)
- ❌ (`src/go/build/build.go`, `importGo`)
- ❌ (`src/os/exec/exec_posix_test.go`, `init`)
- ❌ (`src/os/exec/exec_posix_test.go`, `cmdPwd`)
- ❌ (`src/os/exec/exec_posix_test.go`, `TestCredentialNoSetGroups`)
- ❌ (`src/os/exec/exec_posix_test.go`, `TestWaitid`)
- ❌ (`src/os/exec/exec_posix_test.go`, `TestImplicitPWD`)
- ✅ (`src/os/exec/exec_posix_test.go`, `TestExplicitPWD`)
- ❌ (`src/os/exec/exec_linux_test.go`, `init`)
- ❌ (`src/os/exec/exec_windows_test.go`, `init`)
- ❌ (`src/os/exec/exec_windows_test.go`, `cmdPipeHandle`)
- ❌ (`src/os/exec/exec_windows_test.go`, `TestChildCriticalEnv`)
- ❌ (`src/os/exec/exec_test.go`, `init`)
- ❌ (`src/os/exec/exec_test.go`, `TestMain`)
- ❌ (`src/os/exec/exec_test.go`, `registerHelperCommand`)
- ❌ (`src/os/exec/exec_test.go`, `maySkipHelperCommand`)
- ❌ (`src/os/exec/exec_test.go`, `helperCommand`)
- ❌ (`src/os/exec/exec_test.go`, `helperCommandContext`)
- ❌ (`src/os/exec/exec_test.go`, `cmdEcho`)
- ❌ (`src/os/exec/exec_test.go`, `cmdEchoEnv`)
- ❌ (`src/os/exec/exec_test.go`, `cmdCat`)
- ❌ (`src/os/exec/exec_test.go`, `cmdPipeTest`)
- ❌ (`src/os/exec/exec_test.go`, `cmdStdinClose`)
- ❌ (`src/os/exec/exec_test.go`, `cmdExit`)
- ❌ (`src/os/exec/exec_test.go`, `cmdDescribeFiles`)
- ❌ (`src/os/exec/exec_test.go`, `cmdStderrFail`)
- ❌ (`src/os/exec/exec_test.go`, `cmdYes`)
- ✅ (`src/os/exec/exec_test.go`, `TestCommandRelativeName`)
- ❌ (`src/os/exec/exec_test.go`, `TestCatGoodAndBadFile`)
- ❌ (`src/os/exec/exec_test.go`, `TestExtraFiles`)
- ❌ (`src/os/exec/exec_test.go`, `TestExtraFilesRace`)
- ❌ (`src/os/exec/exec_test.go`, `Read`)
- ❌ (`src/os/exec/exec_test.go`, `TestClosePipeOnCopyError`)
- ❌ (`src/os/exec/exec_test.go`, `TestContextCancel`)
- ❌ (`src/os/exec/exec_test.go`, `TestDedupEnvEcho`)
- ❌ (`src/os/exec/exec_test.go`, `TestString`)
- ❌ (`src/os/exec/lp_windows_test.go`, `init`)
- ❌ (`src/os/exec/lp_windows_test.go`, `installBat`)
- ❌ (`src/cmd/internal/moddeps/moddeps_test.go`, `TestAllDependencies`)
- ❌ (`src/cmd/internal/moddeps/moddeps_test.go`, `makeGOROOTCopy`)
- ❌ (`src/cmd/internal/moddeps/moddeps_test.go`, `run`)
- ❌ (`src/cmd/internal/moddeps/moddeps_test.go`, `findGorootModules`)

### 📊 Proposal #50601

#### File Embeddings - Directory Level
- ❌ `src/encoding/binary`

#### File Embeddings - File Level
- ❌ `src/encoding/binary/binary.go`
- ❌ `src/encoding/binary/binary_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/encoding/binary`

#### Function Embeddings - File Level
- ✅ `src/encoding/binary/binary.go`
- ✅ `src/encoding/binary/binary_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/encoding/binary/binary.go`, `AppendUint16`)
- ✅ (`src/encoding/binary/binary.go`, `AppendUint32`)
- ✅ (`src/encoding/binary/binary.go`, `AppendUint64`)
- ✅ (`src/encoding/binary/binary.go`, `AppendUint16`)
- ✅ (`src/encoding/binary/binary.go`, `AppendUint32`)
- ✅ (`src/encoding/binary/binary.go`, `AppendUint64`)
- ✅ (`src/encoding/binary/binary_test.go`, `TestByteOrder`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkReadInts`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkWriteInts`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkPutUint16`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkAppendUint16`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkPutUint32`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkAppendUint32`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkPutUint64`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkAppendUint64`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkLittleEndianPutUint16`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkLittleEndianAppendUint16`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkLittleEndianPutUint32`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkLittleEndianAppendUint32`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkLittleEndianPutUint64`)
- ❌ (`src/encoding/binary/binary_test.go`, `BenchmarkLittleEndianAppendUint64`)

### 📊 Proposal #50674

#### File Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### File Embeddings - File Level
- ❌ `src/crypto/x509/parser.go`
- ✅ `src/crypto/x509/x509.go`
- ❌ `src/crypto/x509/x509_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### Function Embeddings - File Level
- ❌ `src/crypto/x509/parser.go`
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateRevocationList`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestParseRevocationList`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestRevocationListCheckSignatureFrom`)
- ✅ (`src/crypto/x509/x509.go`, `ParseDERCRL`)
- ❌ (`src/crypto/x509/x509.go`, `CheckSignatureFrom`)
- ❌ (`src/crypto/x509/parser.go`, `parseTime`)
- ❌ (`src/crypto/x509/parser.go`, `parseValidity`)
- ❌ (`src/crypto/x509/parser.go`, `parseExtension`)
- ❌ (`src/crypto/x509/parser.go`, `ParseRevocationList`)

### 📊 Proposal #50770

#### File Embeddings - Directory Level
- ✅ `src/time`

#### File Embeddings - File Level
- ❌ `src/time/mono_test.go`
- ❌ `src/time/time.go`

#### Function Embeddings - Directory Level
- ✅ `src/time`

#### Function Embeddings - File Level
- ❌ `src/time/mono_test.go`
- ✅ `src/time/time.go`

#### Function Embeddings - Function Level
- ❌ (`src/time/mono_test.go`, `TestMonotonicAdd`)
- ❌ (`src/time/mono_test.go`, `TestMonotonicSub`)
- ❌ (`src/time/mono_test.go`, `TestMonotonicOverflow`)
- ❌ (`src/time/time.go`, `Compare`)

### 📊 Proposal #50842

#### File Embeddings - Directory Level
- ✅ `src/io`

#### File Embeddings - File Level
- ❌ `src/io/io.go`
- ✅ `src/io/multi.go`
- ❌ `src/io/multi_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/io`

#### Function Embeddings - File Level
- ❌ `src/io/io.go`
- ❌ `src/io/multi.go`
- ❌ `src/io/multi_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/io/multi.go`, `WriteTo`)
- ❌ (`src/io/multi_test.go`, `TestMultiReaderAsWriterTo`)
- ❌ (`src/io/multi.go`, `WriteTo`)
- ❌ (`src/io/multi.go`, `writeToWithBuffer`)
- ❌ (`src/io/io.go`, `Copy`)
- ❌ (`src/io/io.go`, `CopyBuffer`)
- ❌ (`src/io/io.go`, `copyBuffer`)
- ❌ (`src/io/multi_test.go`, `TestMultiReaderAsWriterTo`)
- ❌ (`src/io/multi.go`, `WriteTo`)
- ❌ (`src/io/multi.go`, `writeToWithBuffer`)

### 📊 Proposal #50859

#### File Embeddings - Directory Level
- ✅ `src/sync`

#### File Embeddings - File Level
- ✅ `src/sync/cond.go`

#### Function Embeddings - Directory Level
- ❌ `src/sync`

#### Function Embeddings - File Level
- ❌ `src/sync/cond.go`

#### Function Embeddings - Function Level
- ❌ (`src/sync/cond.go`, `check`)

### 📊 Proposal #50860

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/escape`
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/cmd/compile/internal/types`
- ✅ `src/sync/atomic`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/escape/utils.go`
- ❌ `src/cmd/compile/internal/test/inl_test.go`
- ❌ `src/cmd/compile/internal/types/size.go`
- ❌ `src/sync/atomic/atomic_test.go`
- ✅ `src/sync/atomic/type.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/escape`
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/cmd/compile/internal/types`
- ✅ `src/sync/atomic`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/escape/utils.go`
- ❌ `src/cmd/compile/internal/test/inl_test.go`
- ❌ `src/cmd/compile/internal/types/size.go`
- ✅ `src/sync/atomic/atomic_test.go`
- ❌ `src/sync/atomic/type.go`

#### Function Embeddings - Function Level
- ❌ (`src/sync/atomic/type.go`, `CompareAndSwap`)
- ❌ (`src/sync/atomic/type.go`, `b32`)
- ❌ (`src/sync/atomic/type.go`, `CompareAndSwap`)
- ❌ (`src/sync/atomic/type.go`, `CompareAndSwap`)
- ❌ (`src/sync/atomic/type.go`, `CompareAndSwap`)
- ❌ (`src/sync/atomic/type.go`, `CompareAndSwap`)
- ❌ (`src/sync/atomic/type.go`, `CompareAndSwap`)
- ❌ (`src/sync/atomic/type.go`, `CompareAndSwap`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestSwapInt32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestSwapUint32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestSwapInt64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestSwapInt64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestSwapUint64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestSwapUint64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestSwapUintptrMethod`)
- ❌ (`src/sync/atomic/atomic_test.go`, `testPointers`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestSwapPointerMethod`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestAddInt32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestAddUint32`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestAddUint32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestAddInt64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestAddInt64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestAddUint64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestAddUint64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestAddUintptrMethod`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestCompareAndSwapInt32`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestCompareAndSwapInt32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestCompareAndSwapUint32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestCompareAndSwapInt64`)
- ✅ (`src/sync/atomic/atomic_test.go`, `TestCompareAndSwapInt64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `testCompareAndSwapUint64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestCompareAndSwapUint64Method`)
- ✅ (`src/sync/atomic/atomic_test.go`, `TestCompareAndSwapUintptrMethod`)
- ✅ (`src/sync/atomic/atomic_test.go`, `TestCompareAndSwapPointerMethod`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestLoadInt32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestLoadUint32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestLoadInt64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestLoadInt64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestLoadUint64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestLoadUint64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestLoadUintptrMethod`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestLoadPointer`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestLoadPointerMethod`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestStoreInt32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestStoreUint32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestStoreInt64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestStoreInt64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestStoreUint64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestStoreUint64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestStoreUintptrMethod`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestStorePointerMethod`)
- ❌ (`src/sync/atomic/atomic_test.go`, `init`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerSwapInt32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerSwapUint32Method`)
- ✅ (`src/sync/atomic/atomic_test.go`, `hammerSwapUintptr32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerAddInt32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerAddUint32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerAddUintptr32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerCompareAndSwapInt32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerCompareAndSwapUint32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerCompareAndSwapUintptr32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerSwapInt64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerSwapUint64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerSwapUintptr64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerAddInt64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerAddUint64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerAddUintptr64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerCompareAndSwapInt64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerCompareAndSwapUint64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerCompareAndSwapUintptr64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerStoreLoadInt32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerStoreLoadUint32Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerStoreLoadInt64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerStoreLoadUint64Method`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerStoreLoadUintptrMethod`)
- ❌ (`src/sync/atomic/atomic_test.go`, `hammerStoreLoadPointerMethod`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestHammerStoreLoad`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestUnaligned64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestAutoAligned64`)
- ❌ (`src/sync/atomic/atomic_test.go`, `TestNilDeref`)
- ❌ (`src/cmd/compile/internal/test/inl_test.go`, `TestIntendedInlining`)
- ❌ (`src/cmd/compile/internal/types/size.go`, `calcStructOffset`)
- ❌ (`src/cmd/compile/internal/escape/utils.go`, `HeapAllocReason`)
- ❌ (`src/cmd/compile/internal/test/inl_test.go`, `TestIntendedInlining`)

### 📊 Proposal #51082

#### File Embeddings - Directory Level
- ❌ `misc/cgo/gmp`
- ❌ `src/archive/zip`
- ❌ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/importer`
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/compile/internal/syntax`
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/compile/internal/types`
- ❌ `src/cmd/compile/internal/types2`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/cmd/cover`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/doc`
- ❌ `src/cmd/go/internal/cache`
- ❌ `src/cmd/go/internal/imports`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/internal/obj/riscv`
- ❌ `src/cmd/internal/obj/x86`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/cmd/link/internal/loader`
- ❌ `src/container/ring`
- ❌ `src/debug/dwarf`
- ❌ `src/debug/gosym`
- ❌ `src/encoding/ascii85`
- ❌ `src/encoding/binary`
- ❌ `src/encoding/json`
- ❌ `src/go/ast`
- ❌ `src/go/build`
- ❌ `src/go/constant`
- ❌ `src/go/doc`
- ✅ `src/go/doc/comment`
- ❌ `src/go/format`
- ❌ `src/go/internal/gccgoimporter`
- ❌ `src/go/internal/gcimporter`
- ❌ `src/go/parser`
- ✅ `src/go/printer`
- ❌ `src/go/printer/testdata`
- ❌ `src/go/scanner`
- ❌ `src/go/token`
- ❌ `src/go/types`
- ❌ `src/html/template`
- ❌ `src/index/suffixarray`
- ❌ `src/internal/fmtsort`
- ❌ `src/math/big`
- ❌ `src/math/rand`
- ❌ `src/net/http`
- ❌ `src/net/textproto`
- ❌ `src/path`
- ❌ `src/path/filepath`
- ❌ `src/reflect`
- ❌ `src/regexp`
- ❌ `src/regexp/syntax`
- ❌ `src/runtime`
- ❌ `src/runtime/pprof`
- ❌ `src/runtime/trace`
- ❌ `src/sort`
- ❌ `src/strconv`
- ❌ `src/sync`
- ❌ `src/testing/fstest`
- ❌ `src/text/tabwriter`
- ❌ `src/text/template`
- ❌ `src/unicode`

#### File Embeddings - File Level
- ❌ `misc/cgo/gmp/gmp.go`
- ❌ `src/archive/zip/reader_test.go`
- ❌ `src/cmd/asm/internal/asm/parse.go`
- ❌ `src/cmd/cgo/gcc.go`
- ❌ `src/cmd/compile/internal/importer/gcimporter.go`
- ❌ `src/cmd/compile/internal/ir/fmt.go`
- ❌ `src/cmd/compile/internal/ssa/block.go`
- ❌ `src/cmd/compile/internal/ssa/compile.go`
- ❌ `src/cmd/compile/internal/ssa/debug.go`
- ❌ `src/cmd/compile/internal/ssa/debug_test.go`
- ❌ `src/cmd/compile/internal/syntax/parser.go`
- ❌ `src/cmd/compile/internal/syntax/syntax.go`
- ❌ `src/cmd/compile/internal/test/zerorange_test.go`
- ❌ `src/cmd/compile/internal/typecheck/mkbuiltin.go`
- ❌ `src/cmd/compile/internal/types/fmt.go`
- ❌ `src/cmd/compile/internal/types2/api.go`
- ❌ `src/cmd/compile/internal/types2/builtins.go`
- ❌ `src/cmd/compile/internal/types2/expr.go`
- ❌ `src/cmd/compile/internal/types2/lookup.go`
- ❌ `src/cmd/compile/internal/types2/operand.go`
- ❌ `src/cmd/compile/internal/types2/selection.go`
- ❌ `src/cmd/compile/internal/types2/typexpr.go`
- ❌ `src/cmd/compile/internal/types2/universe.go`
- ❌ `src/cmd/compile/internal/walk/builtin.go`
- ❌ `src/cmd/compile/internal/walk/order.go`
- ❌ `src/cmd/cover/cover_test.go`
- ❌ `src/cmd/dist/buildruntime.go`
- ❌ `src/cmd/doc/pkg.go`
- ❌ `src/cmd/go/internal/cache/cache.go`
- ❌ `src/cmd/go/internal/imports/build.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ❌ `src/cmd/internal/obj/riscv/obj.go`
- ❌ `src/cmd/internal/obj/x86/asm6.go`
- ❌ `src/cmd/link/internal/ld/dwarf_test.go`
- ❌ `src/cmd/link/internal/loader/loader.go`
- ❌ `src/container/ring/ring.go`
- ❌ `src/debug/dwarf/entry.go`
- ❌ `src/debug/gosym/pclntab_test.go`
- ❌ `src/encoding/ascii85/ascii85.go`
- ❌ `src/encoding/binary/varint.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/commentmap.go`
- ❌ `src/go/ast/filter.go`
- ❌ `src/go/ast/resolve.go`
- ❌ `src/go/ast/scope.go`
- ❌ `src/go/ast/walk.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/constant/value.go`
- ❌ `src/go/doc/comment.go`
- ❌ `src/go/doc/comment/html.go`
- ❌ `src/go/doc/comment/markdown.go`
- ❌ `src/go/doc/comment/parse.go`
- ✅ `src/go/doc/comment/print.go`
- ❌ `src/go/doc/comment/std_test.go`
- ❌ `src/go/doc/comment/testdata_test.go`
- ❌ `src/go/doc/comment/text.go`
- ❌ `src/go/doc/comment_test.go`
- ❌ `src/go/doc/doc.go`
- ❌ `src/go/doc/doc_test.go`
- ❌ `src/go/doc/example.go`
- ❌ `src/go/doc/exports.go`
- ❌ `src/go/doc/filter.go`
- ❌ `src/go/doc/reader.go`
- ❌ `src/go/doc/synopsis.go`
- ❌ `src/go/doc/synopsis_test.go`
- ❌ `src/go/format/benchmark_test.go`
- ❌ `src/go/format/format.go`
- ❌ `src/go/internal/gccgoimporter/parser.go`
- ❌ `src/go/internal/gcimporter/gcimporter.go`
- ❌ `src/go/parser/error_test.go`
- ❌ `src/go/parser/interface.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/resolver.go`
- ✅ `src/go/printer/comment.go`
- ✅ `src/go/printer/nodes.go`
- ❌ `src/go/printer/printer.go`
- ❌ `src/go/printer/printer_test.go`
- ❌ `src/go/printer/testdata/parser.go`
- ❌ `src/go/scanner/errors.go`
- ❌ `src/go/scanner/scanner.go`
- ❌ `src/go/token/position.go`
- ❌ `src/go/token/token.go`
- ❌ `src/go/types/api.go`
- ❌ `src/go/types/builtins.go`
- ❌ `src/go/types/eval.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/lookup.go`
- ❌ `src/go/types/operand.go`
- ❌ `src/go/types/selection.go`
- ❌ `src/go/types/typexpr.go`
- ❌ `src/go/types/universe.go`
- ❌ `src/html/template/template.go`
- ❌ `src/index/suffixarray/suffixarray.go`
- ❌ `src/internal/fmtsort/sort.go`
- ❌ `src/math/big/float.go`
- ❌ `src/math/big/floatconv.go`
- ❌ `src/math/big/int.go`
- ❌ `src/math/big/intconv.go`
- ❌ `src/math/big/natconv.go`
- ❌ `src/math/big/rat.go`
- ❌ `src/math/rand/exp.go`
- ❌ `src/math/rand/normal.go`
- ❌ `src/net/http/fs.go`
- ❌ `src/net/textproto/reader.go`
- ❌ `src/net/textproto/textproto.go`
- ❌ `src/path/filepath/match.go`
- ❌ `src/path/match.go`
- ❌ `src/reflect/makefunc.go`
- ❌ `src/regexp/exec_test.go`
- ❌ `src/regexp/syntax/parse.go`
- ❌ `src/runtime/chan.go`
- ❌ `src/runtime/pprof/pprof.go`
- ❌ `src/runtime/trace/annotation.go`
- ❌ `src/sort/search.go`
- ❌ `src/sort/search_test.go`
- ❌ `src/strconv/itoa.go`
- ❌ `src/sync/cond.go`
- ❌ `src/sync/once.go`
- ❌ `src/testing/fstest/testfs.go`
- ❌ `src/text/tabwriter/tabwriter.go`
- ❌ `src/text/template/option.go`
- ❌ `src/unicode/letter.go`

#### Function Embeddings - Directory Level
- ❌ `misc/cgo/gmp`
- ❌ `src/archive/zip`
- ❌ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/importer`
- ❌ `src/cmd/compile/internal/ir`
- ✅ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/compile/internal/syntax`
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/compile/internal/types`
- ❌ `src/cmd/compile/internal/types2`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/cmd/cover`
- ❌ `src/cmd/dist`
- ❌ `src/cmd/doc`
- ❌ `src/cmd/go/internal/cache`
- ❌ `src/cmd/go/internal/imports`
- ❌ `src/cmd/go/internal/modload`
- ❌ `src/cmd/internal/obj/riscv`
- ❌ `src/cmd/internal/obj/x86`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/cmd/link/internal/loader`
- ❌ `src/container/ring`
- ❌ `src/debug/dwarf`
- ❌ `src/debug/gosym`
- ❌ `src/encoding/ascii85`
- ❌ `src/encoding/binary`
- ❌ `src/encoding/json`
- ❌ `src/go/ast`
- ❌ `src/go/build`
- ❌ `src/go/constant`
- ❌ `src/go/doc`
- ✅ `src/go/doc/comment`
- ❌ `src/go/format`
- ❌ `src/go/internal/gccgoimporter`
- ❌ `src/go/internal/gcimporter`
- ❌ `src/go/parser`
- ✅ `src/go/printer`
- ❌ `src/go/printer/testdata`
- ❌ `src/go/scanner`
- ❌ `src/go/token`
- ❌ `src/go/types`
- ❌ `src/html/template`
- ❌ `src/index/suffixarray`
- ❌ `src/internal/fmtsort`
- ❌ `src/math/big`
- ❌ `src/math/rand`
- ❌ `src/net/http`
- ❌ `src/net/textproto`
- ❌ `src/path`
- ❌ `src/path/filepath`
- ❌ `src/reflect`
- ❌ `src/regexp`
- ❌ `src/regexp/syntax`
- ❌ `src/runtime`
- ❌ `src/runtime/pprof`
- ❌ `src/runtime/trace`
- ❌ `src/sort`
- ❌ `src/strconv`
- ❌ `src/sync`
- ❌ `src/testing/fstest`
- ❌ `src/text/tabwriter`
- ❌ `src/text/template`
- ❌ `src/unicode`

#### Function Embeddings - File Level
- ❌ `misc/cgo/gmp/gmp.go`
- ❌ `src/archive/zip/reader_test.go`
- ❌ `src/cmd/asm/internal/asm/parse.go`
- ❌ `src/cmd/cgo/gcc.go`
- ❌ `src/cmd/compile/internal/importer/gcimporter.go`
- ❌ `src/cmd/compile/internal/ir/fmt.go`
- ❌ `src/cmd/compile/internal/ssa/block.go`
- ❌ `src/cmd/compile/internal/ssa/compile.go`
- ❌ `src/cmd/compile/internal/ssa/debug.go`
- ❌ `src/cmd/compile/internal/ssa/debug_test.go`
- ❌ `src/cmd/compile/internal/syntax/parser.go`
- ❌ `src/cmd/compile/internal/syntax/syntax.go`
- ❌ `src/cmd/compile/internal/test/zerorange_test.go`
- ❌ `src/cmd/compile/internal/typecheck/mkbuiltin.go`
- ❌ `src/cmd/compile/internal/types/fmt.go`
- ❌ `src/cmd/compile/internal/types2/api.go`
- ❌ `src/cmd/compile/internal/types2/builtins.go`
- ❌ `src/cmd/compile/internal/types2/expr.go`
- ❌ `src/cmd/compile/internal/types2/lookup.go`
- ❌ `src/cmd/compile/internal/types2/operand.go`
- ❌ `src/cmd/compile/internal/types2/selection.go`
- ❌ `src/cmd/compile/internal/types2/typexpr.go`
- ❌ `src/cmd/compile/internal/types2/universe.go`
- ❌ `src/cmd/compile/internal/walk/builtin.go`
- ❌ `src/cmd/compile/internal/walk/order.go`
- ❌ `src/cmd/cover/cover_test.go`
- ❌ `src/cmd/dist/buildruntime.go`
- ❌ `src/cmd/doc/pkg.go`
- ❌ `src/cmd/go/internal/cache/cache.go`
- ❌ `src/cmd/go/internal/imports/build.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ❌ `src/cmd/internal/obj/riscv/obj.go`
- ❌ `src/cmd/internal/obj/x86/asm6.go`
- ❌ `src/cmd/link/internal/ld/dwarf_test.go`
- ❌ `src/cmd/link/internal/loader/loader.go`
- ❌ `src/container/ring/ring.go`
- ❌ `src/debug/dwarf/entry.go`
- ❌ `src/debug/gosym/pclntab_test.go`
- ❌ `src/encoding/ascii85/ascii85.go`
- ❌ `src/encoding/binary/varint.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/commentmap.go`
- ❌ `src/go/ast/filter.go`
- ❌ `src/go/ast/resolve.go`
- ❌ `src/go/ast/scope.go`
- ❌ `src/go/ast/walk.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/constant/value.go`
- ❌ `src/go/doc/comment.go`
- ✅ `src/go/doc/comment/html.go`
- ❌ `src/go/doc/comment/markdown.go`
- ❌ `src/go/doc/comment/parse.go`
- ✅ `src/go/doc/comment/print.go`
- ❌ `src/go/doc/comment/std_test.go`
- ❌ `src/go/doc/comment/testdata_test.go`
- ❌ `src/go/doc/comment/text.go`
- ❌ `src/go/doc/comment_test.go`
- ❌ `src/go/doc/doc.go`
- ❌ `src/go/doc/doc_test.go`
- ❌ `src/go/doc/example.go`
- ❌ `src/go/doc/exports.go`
- ❌ `src/go/doc/filter.go`
- ❌ `src/go/doc/reader.go`
- ❌ `src/go/doc/synopsis.go`
- ❌ `src/go/doc/synopsis_test.go`
- ❌ `src/go/format/benchmark_test.go`
- ❌ `src/go/format/format.go`
- ❌ `src/go/internal/gccgoimporter/parser.go`
- ❌ `src/go/internal/gcimporter/gcimporter.go`
- ❌ `src/go/parser/error_test.go`
- ❌ `src/go/parser/interface.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/resolver.go`
- ✅ `src/go/printer/comment.go`
- ❌ `src/go/printer/nodes.go`
- ✅ `src/go/printer/printer.go`
- ❌ `src/go/printer/printer_test.go`
- ❌ `src/go/printer/testdata/parser.go`
- ❌ `src/go/scanner/errors.go`
- ❌ `src/go/scanner/scanner.go`
- ❌ `src/go/token/position.go`
- ❌ `src/go/token/token.go`
- ❌ `src/go/types/api.go`
- ❌ `src/go/types/builtins.go`
- ❌ `src/go/types/eval.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/lookup.go`
- ❌ `src/go/types/operand.go`
- ❌ `src/go/types/selection.go`
- ❌ `src/go/types/typexpr.go`
- ❌ `src/go/types/universe.go`
- ❌ `src/html/template/template.go`
- ❌ `src/index/suffixarray/suffixarray.go`
- ❌ `src/internal/fmtsort/sort.go`
- ❌ `src/math/big/float.go`
- ❌ `src/math/big/floatconv.go`
- ❌ `src/math/big/int.go`
- ❌ `src/math/big/intconv.go`
- ❌ `src/math/big/natconv.go`
- ❌ `src/math/big/rat.go`
- ❌ `src/math/rand/exp.go`
- ❌ `src/math/rand/normal.go`
- ❌ `src/net/http/fs.go`
- ❌ `src/net/textproto/reader.go`
- ❌ `src/net/textproto/textproto.go`
- ❌ `src/path/filepath/match.go`
- ❌ `src/path/match.go`
- ❌ `src/reflect/makefunc.go`
- ❌ `src/regexp/exec_test.go`
- ❌ `src/regexp/syntax/parse.go`
- ❌ `src/runtime/chan.go`
- ❌ `src/runtime/pprof/pprof.go`
- ❌ `src/runtime/trace/annotation.go`
- ❌ `src/sort/search.go`
- ❌ `src/sort/search_test.go`
- ❌ `src/strconv/itoa.go`
- ❌ `src/sync/cond.go`
- ❌ `src/sync/once.go`
- ❌ `src/testing/fstest/testfs.go`
- ❌ `src/text/tabwriter/tabwriter.go`
- ❌ `src/text/template/option.go`
- ❌ `src/unicode/letter.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/internal/obj/riscv/obj.go`, `stackOffset`)
- ❌ (`src/debug/gosym/pclntab_test.go`, `read115Executable`)
- ❌ (`src/math/big/int.go`, `Sign`)
- ❌ (`src/math/big/int.go`, `QuoRem`)
- ❌ (`src/math/big/int.go`, `DivMod`)
- ❌ (`src/math/big/int.go`, `Cmp`)
- ❌ (`src/cmd/compile/internal/ssa/debug_test.go`, `TestNexting`)
- ❌ (`src/cmd/link/internal/ld/dwarf_test.go`, `processParams`)
- ❌ (`src/regexp/syntax/parse.go`, `factor`)
- ❌ (`src/go/internal/gccgoimporter/parser.go`, `getPkg`)
- ❌ (`src/go/internal/gccgoimporter/parser.go`, `parseType`)
- ❌ (`src/go/types/lookup.go`, `LookupFieldOrMethod`)
- ❌ (`src/go/types/lookup.go`, `MissingMethod`)
- ❌ (`src/container/ring/ring.go`, `Move`)
- ❌ (`src/container/ring/ring.go`, `Link`)
- ❌ (`src/container/ring/ring.go`, `Unlink`)
- ❌ (`src/container/ring/ring.go`, `Len`)
- ❌ (`src/go/ast/filter.go`, `FileExports`)
- ❌ (`src/go/ast/filter.go`, `PackageExports`)
- ❌ (`src/go/ast/filter.go`, `fieldName`)
- ❌ (`src/go/ast/filter.go`, `filterFile`)
- ❌ (`src/go/ast/filter.go`, `filterPackage`)
- ❌ (`src/go/ast/filter.go`, `nameOf`)
- ❌ (`src/go/ast/filter.go`, `MergePackageFiles`)
- ❌ (`src/sync/cond.go`, `Wait`)
- ❌ (`src/go/scanner/scanner.go`, `Init`)
- ❌ (`src/go/scanner/scanner.go`, `Scan`)
- ❌ (`src/go/doc/reader.go`, `recvString`)
- ❌ (`src/go/doc/reader.go`, `set`)
- ❌ (`src/go/doc/reader.go`, `add`)
- ❌ (`src/go/doc/reader.go`, `baseTypeName`)
- ❌ (`src/go/doc/reader.go`, `lookupType`)
- ❌ (`src/go/doc/reader.go`, `recordAnonymousField`)
- ❌ (`src/go/doc/reader.go`, `readValue`)
- ❌ (`src/go/doc/reader.go`, `fields`)
- ❌ (`src/go/doc/reader.go`, `readType`)
- ❌ (`src/go/doc/reader.go`, `readFunc`)
- ❌ (`src/go/doc/reader.go`, `readNote`)
- ❌ (`src/go/doc/reader.go`, `readNotes`)
- ❌ (`src/go/doc/reader.go`, `readFile`)
- ❌ (`src/go/doc/reader.go`, `collectEmbeddedMethods`)
- ❌ (`src/go/doc/reader.go`, `computeMethodSets`)
- ❌ (`src/go/doc/reader.go`, `cleanupTypes`)
- ❌ (`src/go/doc/reader.go`, `sortedValues`)
- ❌ (`src/internal/fmtsort/sort.go`, `Sort`)
- ❌ (`src/math/big/natconv.go`, `scan`)
- ❌ (`src/math/big/natconv.go`, `convertWords`)
- ❌ (`src/path/filepath/match.go`, `Match`)
- ❌ (`src/cmd/asm/internal/asm/parse.go`, `symRefAttrs`)
- ❌ (`src/cmd/compile/internal/types2/expr.go`, `rawExpr`)
- ❌ (`src/cmd/compile/internal/types2/expr.go`, `exprInternal`)
- ❌ (`src/cmd/compile/internal/types2/expr.go`, `expr`)
- ❌ (`src/cmd/compile/internal/types2/expr.go`, `exprWithHint`)
- ❌ (`src/cmd/cover/cover_test.go`, `TestCover`)
- ❌ (`src/go/token/position.go`, `String`)
- ❌ (`src/go/token/position.go`, `IsValid`)
- ❌ (`src/go/token/position.go`, `AddLine`)
- ❌ (`src/go/token/position.go`, `MergeLine`)
- ❌ (`src/go/token/position.go`, `SetLines`)
- ❌ (`src/go/token/position.go`, `Offset`)
- ❌ (`src/go/token/position.go`, `unpack`)
- ❌ (`src/go/token/position.go`, `Base`)
- ❌ (`src/go/token/position.go`, `AddFile`)
- ❌ (`src/go/token/position.go`, `file`)
- ❌ (`src/go/token/position.go`, `searchInts`)
- ❌ (`src/go/types/builtins.go`, `builtin`)
- ❌ (`src/go/ast/scope.go`, `Lookup`)
- ❌ (`src/go/ast/scope.go`, `Insert`)
- ❌ (`src/cmd/compile/internal/walk/builtin.go`, `walkCopy`)
- ❌ (`src/go/format/format.go`, `Node`)
- ❌ (`src/go/format/format.go`, `Source`)
- ❌ (`src/go/types/eval.go`, `CheckExpr`)
- ❌ (`src/go/ast/resolve.go`, `NewPackage`)
- ❌ (`src/sync/once.go`, `Do`)
- ❌ (`src/go/doc/exports.go`, `filterIdentList`)
- ❌ (`src/go/doc/exports.go`, `hasExportedName`)
- ❌ (`src/go/doc/exports.go`, `filterFieldList`)
- ❌ (`src/go/doc/exports.go`, `filterParamList`)
- ❌ (`src/go/doc/exports.go`, `filterType`)
- ❌ (`src/go/doc/exports.go`, `copyConstType`)
- ❌ (`src/go/doc/exports.go`, `fileExports`)
- ❌ (`src/go/parser/interface.go`, `readSource`)
- ❌ (`src/go/parser/interface.go`, `ParseFile`)
- ❌ (`src/go/parser/interface.go`, `ParseDir`)
- ❌ (`src/go/parser/interface.go`, `ParseExprFrom`)
- ❌ (`src/runtime/trace/annotation.go`, `StartRegion`)
- ❌ (`src/cmd/compile/internal/types2/universe.go`, `def`)
- ❌ (`src/index/suffixarray/suffixarray.go`, `Bytes`)
- ❌ (`src/index/suffixarray/suffixarray.go`, `Lookup`)
- ❌ (`src/index/suffixarray/suffixarray.go`, `FindAllIndex`)
- ❌ (`src/cmd/compile/internal/ir/fmt.go`, `Format`)
- ❌ (`src/cmd/compile/internal/ir/fmt.go`, `fmtNode`)
- ❌ (`src/cmd/compile/internal/ir/fmt.go`, `Format`)
- ❌ (`src/go/printer/nodes.go`, `linebreak`)
- ❌ (`src/go/printer/nodes.go`, `binaryExpr`)
- ❌ (`src/go/printer/nodes.go`, `indentList`)
- ❌ (`src/go/printer/nodes.go`, `keepTypeColumn`)
- ❌ (`src/go/printer/nodes.go`, `spec`)
- ❌ (`src/go/printer/nodes.go`, `nodeSize`)
- ❌ (`src/go/printer/nodes.go`, `funcBody`)
- ❌ (`src/path/match.go`, `Match`)
- ❌ (`src/net/textproto/reader.go`, `ReadContinuedLine`)
- ❌ (`src/net/textproto/reader.go`, `ReadCodeLine`)
- ❌ (`src/net/textproto/reader.go`, `ReadResponse`)
- ❌ (`src/net/textproto/reader.go`, `ReadMIMEHeader`)
- ❌ (`src/cmd/link/internal/loader/loader.go`, `Errorf`)
- ❌ (`src/reflect/makefunc.go`, `MakeFunc`)
- ❌ (`src/go/types/api.go`, `TypeOf`)
- ❌ (`src/go/types/api.go`, `ObjectOf`)
- ❌ (`src/cmd/compile/internal/ssa/debug.go`, `PopulateABIInRegArgOps`)
- ❌ (`src/encoding/json/encode.go`, `Marshal`)
- ❌ (`src/cmd/internal/obj/x86/asm6.go`, `regIndex`)
- ❌ (`src/html/template/template.go`, `Option`)
- ❌ (`src/cmd/go/internal/modload/load.go`, `stackText`)
- ❌ (`src/go/printer/printer_test.go`, `TestLineComments`)
- ❌ (`src/net/http/fs.go`, `FileServer`)
- ❌ (`src/encoding/ascii85/ascii85.go`, `Decode`)
- ❌ (`src/math/big/rat.go`, `Sign`)
- ❌ (`src/math/big/rat.go`, `Cmp`)
- ❌ (`src/cmd/compile/internal/types2/lookup.go`, `LookupFieldOrMethod`)
- ❌ (`src/cmd/compile/internal/types2/lookup.go`, `MissingMethod`)
- ❌ (`src/go/types/universe.go`, `def`)
- ❌ (`src/go/internal/gcimporter/gcimporter.go`, `Import`)
- ❌ (`src/cmd/compile/internal/syntax/syntax.go`, `Parse`)
- ❌ (`src/go/printer/printer.go`, `commentBefore`)
- ❌ (`src/go/printer/printer.go`, `commentSizeBefore`)
- ❌ (`src/go/printer/printer.go`, `writeString`)
- ❌ (`src/go/printer/printer.go`, `writeCommentPrefix`)
- ❌ (`src/go/printer/printer.go`, `isBlank`)
- ❌ (`src/go/printer/printer.go`, `stripCommonPrefix`)
- ❌ (`src/go/printer/printer.go`, `writeCommentSuffix`)
- ✅ (`src/go/printer/printer.go`, `intersperseComments`)
- ❌ (`src/go/printer/printer.go`, `print`)
- ❌ (`src/math/big/float.go`, `Sign`)
- ❌ (`src/math/big/float.go`, `Cmp`)
- ❌ (`src/math/big/float.go`, `ord`)
- ❌ (`src/cmd/compile/internal/types2/selection.go`, `SelectionString`)
- ❌ (`src/cmd/go/internal/cache/cache.go`, `Open`)
- ❌ (`src/go/doc/doc.go`, `New`)
- ❌ (`src/go/doc/doc.go`, `NewFromFiles`)
- ❌ (`src/go/constant/value.go`, `Val`)
- ❌ (`src/go/constant/value.go`, `Make`)
- ❌ (`src/go/constant/value.go`, `UnaryOp`)
- ❌ (`src/go/constant/value.go`, `match`)
- ❌ (`src/go/constant/value.go`, `BinaryOp`)
- ❌ (`src/go/constant/value.go`, `Shift`)
- ❌ (`src/go/constant/value.go`, `Compare`)
- ❌ (`src/go/types/selection.go`, `SelectionString`)
- ❌ (`src/cmd/go/internal/imports/build.go`, `ShouldBuild`)
- ❌ (`src/math/rand/normal.go`, `NormFloat64`)
- ❌ (`src/cmd/compile/internal/types2/typexpr.go`, `ident`)
- ❌ (`src/cmd/compile/internal/types2/typexpr.go`, `definedType`)
- ❌ (`src/cmd/compile/internal/types2/typexpr.go`, `typInternal`)
- ❌ (`src/go/types/typexpr.go`, `ident`)
- ❌ (`src/go/types/typexpr.go`, `definedType`)
- ❌ (`src/go/types/typexpr.go`, `typInternal`)
- ❌ (`src/encoding/json/decode.go`, `Unmarshal`)
- ❌ (`src/cmd/compile/internal/importer/gcimporter.go`, `Import`)
- ❌ (`src/go/token/token.go`, `String`)
- ❌ (`src/go/token/token.go`, `Precedence`)
- ❌ (`src/go/token/token.go`, `Lookup`)
- ❌ (`src/go/token/token.go`, `IsOperator`)
- ❌ (`src/go/token/token.go`, `IsKeyword`)
- ❌ (`src/go/token/token.go`, `IsIdentifier`)
- ❌ (`src/go/doc/example.go`, `classifyExamples`)
- ❌ (`src/unicode/letter.go`, `SimpleFold`)
- ❌ (`src/cmd/internal/obj/riscv/obj.go`, `stackOffset`)
- ❌ (`src/go/ast/commentmap.go`, `sortComments`)
- ❌ (`src/go/ast/commentmap.go`, `nodeList`)
- ❌ (`src/go/ast/commentmap.go`, `push`)
- ❌ (`src/go/ast/commentmap.go`, `pop`)
- ❌ (`src/go/ast/commentmap.go`, `NewCommentMap`)
- ❌ (`src/go/ast/commentmap.go`, `summary`)
- ❌ (`src/go/ast/walk.go`, `Walk`)
- ❌ (`src/go/ast/walk.go`, `Inspect`)
- ❌ (`src/go/scanner/errors.go`, `PrintError`)
- ❌ (`src/cmd/cgo/gcc.go`, `splitQuoted`)
- ❌ (`src/go/doc/filter.go`, `Filter`)
- ❌ (`src/go/parser/parser.go`, `consumeCommentGroup`)
- ❌ (`src/go/parser/parser.go`, `next`)
- ❌ (`src/go/parser/parser.go`, `expectClosing`)
- ❌ (`src/go/parser/parser.go`, `safePos`)
- ❌ (`src/go/parser/parser.go`, `parseOperand`)
- ❌ (`src/strconv/itoa.go`, `formatBits`)
- ❌ (`src/go/parser/error_test.go`, `expectedErrors`)
- ❌ (`src/go/parser/error_test.go`, `compareErrors`)
- ❌ (`src/go/parser/resolver.go`, `resolve`)
- ❌ (`src/cmd/compile/internal/types2/builtins.go`, `builtin`)
- ❌ (`src/regexp/exec_test.go`, `TestRE2Search`)
- ❌ (`src/go/doc/synopsis.go`, `Synopsis`)
- ❌ (`src/cmd/compile/internal/ssa/compile.go`, `PhaseOption`)
- ❌ (`src/debug/dwarf/entry.go`, `Val`)
- ❌ (`src/go/format/benchmark_test.go`, `array1`)
- ❌ (`src/cmd/compile/internal/test/zerorange_test.go`, `TestZerorange45372`)
- ❌ (`src/sort/search.go`, `Search`)
- ❌ (`src/sort/search.go`, `SearchInts`)
- ❌ (`src/testing/fstest/testfs.go`, `TestFS`)
- ❌ (`src/encoding/binary/varint.go`, `Uvarint`)
- ❌ (`src/encoding/binary/varint.go`, `Varint`)
- ❌ (`src/math/big/floatconv.go`, `Parse`)
- ❌ (`src/go/printer/testdata/parser.go`, `consumeCommentGroup`)
- ❌ (`src/go/printer/testdata/parser.go`, `next`)
- ❌ (`src/go/printer/testdata/parser.go`, `parseOperand`)
- ❌ (`src/go/printer/testdata/parser.go`, `checkExprOrType`)
- ❌ (`src/text/tabwriter/tabwriter.go`, `Init`)
- ❌ (`src/text/tabwriter/tabwriter.go`, `format`)
- ❌ (`src/text/tabwriter/tabwriter.go`, `startEscape`)
- ❌ (`src/text/tabwriter/tabwriter.go`, `endEscape`)
- ❌ (`src/text/tabwriter/tabwriter.go`, `Write`)
- ❌ (`src/math/big/intconv.go`, `Format`)
- ❌ (`src/math/big/intconv.go`, `scan`)
- ❌ (`src/runtime/pprof/pprof.go`, `Add`)
- ❌ (`src/cmd/dist/buildruntime.go`, `mkzversion`)
- ❌ (`src/cmd/dist/buildruntime.go`, `mkobjabi`)
- ❌ (`src/net/textproto/textproto.go`, `Cmd`)
- ❌ (`src/go/ast/ast.go`, `String`)
- ❌ (`src/go/ast/ast.go`, `End`)
- ❌ (`src/sort/search_test.go`, `log2`)
- ❌ (`src/runtime/chan.go`, `selectnbsend`)
- ❌ (`src/runtime/chan.go`, `selectnbrecv`)
- ❌ (`src/go/build/build.go`, `Import`)
- ❌ (`src/go/build/build.go`, `splitQuoted`)
- ❌ (`src/go/types/expr.go`, `rawExpr`)
- ❌ (`src/go/types/expr.go`, `exprInternal`)
- ❌ (`src/go/types/expr.go`, `expr`)
- ❌ (`src/go/types/expr.go`, `exprWithHint`)
- ❌ (`src/cmd/compile/internal/types2/api.go`, `TypeOf`)
- ❌ (`src/cmd/compile/internal/types2/api.go`, `ObjectOf`)
- ❌ (`src/cmd/compile/internal/syntax/parser.go`, `list`)
- ❌ (`src/text/template/option.go`, `Option`)
- ❌ (`src/go/types/operand.go`, `Pos`)
- ❌ (`src/go/types/operand.go`, `operandString`)
- ❌ (`src/archive/zip/reader_test.go`, `biggestZipBytes`)
- ❌ (`src/cmd/compile/internal/types2/operand.go`, `Pos`)
- ❌ (`src/cmd/compile/internal/types2/operand.go`, `operandString`)
- ❌ (`src/cmd/compile/internal/types/fmt.go`, `Format`)
- ❌ (`src/cmd/compile/internal/types/fmt.go`, `Format`)
- ❌ (`src/math/rand/exp.go`, `ExpFloat64`)
- ❌ (`src/cmd/compile/internal/typecheck/mkbuiltin.go`, `mkbuiltin`)
- ❌ (`src/go/doc/comment/text.go`, `writeNL`)
- ❌ (`src/go/doc/comment/text.go`, `Text`)
- ❌ (`src/go/doc/comment/text.go`, `block`)
- ❌ (`src/go/doc/comment/text.go`, `text`)
- ❌ (`src/go/doc/comment/text.go`, `oneLongLine`)
- ❌ (`src/go/doc/comment/text.go`, `wrap`)
- ❌ (`src/go/doc/comment/markdown.go`, `Markdown`)
- ❌ (`src/go/doc/comment/markdown.go`, `block`)
- ❌ (`src/go/doc/comment/markdown.go`, `text`)
- ❌ (`src/go/doc/comment/markdown.go`, `rawText`)
- ❌ (`src/go/doc/comment/markdown.go`, `escape`)
- ❌ (`src/go/doc/comment/std_test.go`, `TestStd`)
- ❌ (`src/go/doc/comment/print.go`, `headingLevel`)
- ❌ (`src/go/doc/comment/print.go`, `headingID`)
- ❌ (`src/go/doc/comment/print.go`, `docLinkURL`)
- ❌ (`src/go/doc/comment/print.go`, `DefaultURL`)
- ❌ (`src/go/doc/comment/print.go`, `DefaultID`)
- ❌ (`src/go/doc/comment/print.go`, `Comment`)
- ❌ (`src/go/doc/comment/print.go`, `blankBefore`)
- ❌ (`src/go/doc/comment/print.go`, `block`)
- ✅ (`src/go/doc/comment/print.go`, `text`)
- ❌ (`src/go/doc/comment/print.go`, `indent`)
- ❌ (`src/go/doc/comment/html.go`, `HTML`)
- ❌ (`src/go/doc/comment/html.go`, `block`)
- ❌ (`src/go/doc/comment/html.go`, `inc`)
- ✅ (`src/go/doc/comment/html.go`, `text`)
- ❌ (`src/go/doc/comment/html.go`, `escape`)
- ❌ (`src/go/doc/comment/parse.go`, `BlankBefore`)
- ❌ (`src/go/doc/comment/parse.go`, `BlankBetween`)
- ❌ (`src/go/doc/comment/parse.go`, `lookupPkg`)
- ❌ (`src/go/doc/comment/parse.go`, `isStdPkg`)
- ❌ (`src/go/doc/comment/parse.go`, `DefaultLookupPackage`)
- ❌ (`src/go/doc/comment/parse.go`, `Parse`)
- ❌ (`src/go/doc/comment/parse.go`, `unindent`)
- ❌ (`src/go/doc/comment/parse.go`, `isBlank`)
- ❌ (`src/go/doc/comment/parse.go`, `commonPrefix`)
- ❌ (`src/go/doc/comment/parse.go`, `leadingSpace`)
- ❌ (`src/go/doc/comment/parse.go`, `isOldHeading`)
- ❌ (`src/go/doc/comment/parse.go`, `oldHeading`)
- ❌ (`src/go/doc/comment/parse.go`, `isHeading`)
- ❌ (`src/go/doc/comment/parse.go`, `heading`)
- ❌ (`src/go/doc/comment/parse.go`, `indented`)
- ❌ (`src/go/doc/comment/parse.go`, `code`)
- ❌ (`src/go/doc/comment/parse.go`, `paragraph`)
- ❌ (`src/go/doc/comment/parse.go`, `parseLink`)
- ❌ (`src/go/doc/comment/parse.go`, `isList`)
- ❌ (`src/go/doc/comment/parse.go`, `listMarker`)
- ❌ (`src/go/doc/comment/parse.go`, `list`)
- ❌ (`src/go/doc/comment/parse.go`, `parseLinkedText`)
- ❌ (`src/go/doc/comment/parse.go`, `docLink`)
- ❌ (`src/go/doc/comment/parse.go`, `splitDocName`)
- ❌ (`src/go/doc/comment/parse.go`, `isName`)
- ❌ (`src/go/doc/comment/parse.go`, `parseText`)
- ❌ (`src/go/doc/comment/parse.go`, `autoURL`)
- ❌ (`src/go/doc/comment/parse.go`, `isScheme`)
- ❌ (`src/go/doc/comment/parse.go`, `isHost`)
- ❌ (`src/go/doc/comment/parse.go`, `isPunct`)
- ❌ (`src/go/doc/comment/parse.go`, `isPath`)
- ❌ (`src/go/doc/comment/parse.go`, `isIdentASCII`)
- ❌ (`src/go/doc/comment/parse.go`, `ident`)
- ❌ (`src/go/doc/comment/testdata_test.go`, `TestTestdata`)
- ❌ (`src/go/doc/comment/testdata_test.go`, `dump`)
- ❌ (`src/go/doc/comment/testdata_test.go`, `dumpTo`)
- ❌ (`src/go/doc/comment/testdata_test.go`, `dumpNL`)
- ❌ (`src/go/printer/printer_test.go`, `checkEqual`)
- ✅ (`src/go/printer/printer.go`, `intersperseComments`)
- ✅ (`src/go/printer/comment.go`, `formatDocComment`)
- ❌ (`src/go/printer/comment.go`, `isDirective`)
- ❌ (`src/go/printer/comment.go`, `allStars`)
- ❌ (`src/go/doc/doc.go`, `New`)
- ❌ (`src/go/doc/doc.go`, `collectValues`)
- ❌ (`src/go/doc/doc.go`, `collectTypes`)
- ❌ (`src/go/doc/doc.go`, `collectFuncs`)
- ❌ (`src/go/doc/doc.go`, `lookupSym`)
- ❌ (`src/go/doc/doc.go`, `lookupPackage`)
- ❌ (`src/go/doc/doc.go`, `Parser`)
- ❌ (`src/go/doc/doc.go`, `Printer`)
- ❌ (`src/go/doc/doc.go`, `HTML`)
- ❌ (`src/go/doc/doc.go`, `Markdown`)
- ❌ (`src/go/doc/doc.go`, `Text`)
- ❌ (`src/go/doc/comment.go`, `ToHTML`)
- ❌ (`src/go/doc/comment.go`, `ToText`)
- ❌ (`src/go/doc/synopsis.go`, `firstSentence`)
- ❌ (`src/go/doc/synopsis.go`, `Synopsis`)
- ❌ (`src/go/doc/synopsis.go`, `Synopsis`)
- ❌ (`src/go/doc/comment_test.go`, `TestComment`)
- ❌ (`src/go/doc/doc_test.go`, `TestFuncs`)
- ❌ (`src/go/doc/synopsis_test.go`, `TestSynopsis`)
- ❌ (`src/go/doc/reader.go`, `clean`)
- ❌ (`src/go/doc/reader.go`, `readNote`)
- ❌ (`src/go/doc/reader.go`, `readNotes`)
- ❌ (`src/go/doc/reader.go`, `readFile`)
- ❌ (`src/go/doc/reader.go`, `readPackage`)
- ❌ (`src/go/doc/reader.go`, `assumedPackageName`)
- ❌ (`src/cmd/doc/pkg.go`, `ToText`)
- ❌ (`src/cmd/doc/pkg.go`, `emit`)
- ❌ (`src/cmd/doc/pkg.go`, `joinStrings`)
- ❌ (`src/cmd/doc/pkg.go`, `packageDoc`)
- ❌ (`src/cmd/doc/pkg.go`, `printFieldDoc`)
- ❌ (`src/math/big/int.go`, `Jacobi`)
- ❌ (`src/math/big/int.go`, `modSqrt3Mod4Prime`)
- ❌ (`src/cmd/compile/internal/ssa/block.go`, `String`)
- ❌ (`src/go/constant/value.go`, `Val`)
- ❌ (`src/go/constant/value.go`, `Make`)
- ❌ (`misc/cgo/gmp/gmp.go`, `CmpInt`)
- ❌ (`src/cmd/cgo/gcc.go`, `checkIndex`)
- ❌ (`src/cmd/compile/internal/walk/order.go`, `orderBlock`)
- ❌ (`src/cmd/compile/internal/walk/order.go`, `exprInPlace`)
- ❌ (`src/cmd/compile/internal/walk/order.go`, `exprNoLHS`)
- ❌ (`src/cmd/go/internal/modload/query.go`, `allowsVersion`)

### 📊 Proposal #51115

#### File Embeddings - Directory Level
- ❌ `src/io`

#### File Embeddings - File Level
- ❌ `src/io/io.go`

#### Function Embeddings - Directory Level
- ❌ `src/io`

#### Function Embeddings - File Level
- ❌ `src/io/io.go`

#### Function Embeddings - Function Level
- ❌ (`src/io/io.go`, `Read`)
- ❌ (`src/io/io.go`, `Read`)

### 📊 Proposal #51225

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/noder`
- ✅ `src/cmd/go/internal/work`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/noder/import.go`
- ❌ `src/cmd/go/internal/work/gc.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/noder`
- ✅ `src/cmd/go/internal/work`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/noder/import.go`
- ❌ `src/cmd/go/internal/work/gc.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/compile/internal/base/flag.go`, `ParseFlags`)
- ❌ (`src/cmd/compile/internal/base/flag.go`, `readImportCfg`)
- ❌ (`src/cmd/compile/internal/noder/import.go`, `openPackage`)
- ❌ (`src/cmd/go/internal/work/gc.go`, `gc`)

### 📊 Proposal #51414

#### File Embeddings - Directory Level
- ✅ `src/time`

#### File Embeddings - File Level
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/time`

#### Function Embeddings - File Level
- ✅ `src/time/time.go`
- ✅ `src/time/time_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/time/time.go`, `Abs`)
- ❌ (`src/time/time_test.go`, `TestDurationAbs`)

### 📊 Proposal #51428

#### File Embeddings - Directory Level
- ❌ `src/net`

#### File Embeddings - File Level
- ❌ `src/net/error_test.go`
- ❌ `src/net/net.go`

#### Function Embeddings - Directory Level
- ❌ `src/net`

#### Function Embeddings - File Level
- ❌ `src/net/error_test.go`
- ❌ `src/net/net.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/net.go`, `Is`)
- ❌ (`src/net/error_test.go`, `TestContextError`)

### 📊 Proposal #51430

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/coverage`
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/covdata`
- ❌ `src/cmd/covdata/testdata`
- ❌ `src/cmd/internal/cov`
- ❌ `src/internal/coverage/calloc`
- ❌ `src/internal/coverage/cformat`
- ❌ `src/internal/coverage/cmerge`
- ❌ `src/internal/coverage/decodecounter`
- ❌ `src/internal/coverage/encodecounter`
- ❌ `src/internal/coverage/pods`
- ❌ `src/internal/coverage/stringtab`
- ❌ `src/internal/coverage/test`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/coverage/cover.go`
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/typecheck/builtin.go`
- ❌ `src/cmd/compile/internal/typecheck/mkbuiltin.go`
- ❌ `src/cmd/compile/internal/typecheck/syms.go`
- ❌ `src/cmd/covdata/argsmerge.go`
- ❌ `src/cmd/covdata/covdata.go`
- ❌ `src/cmd/covdata/dump.go`
- ❌ `src/cmd/covdata/merge.go`
- ❌ `src/cmd/covdata/metamerge.go`
- ❌ `src/cmd/covdata/subtractintersect.go`
- ❌ `src/cmd/covdata/testdata/dep.go`
- ❌ `src/cmd/covdata/testdata/prog1.go`
- ❌ `src/cmd/covdata/testdata/prog2.go`
- ❌ `src/cmd/covdata/tool_test.go`
- ❌ `src/cmd/internal/cov/mreader.go`
- ❌ `src/cmd/internal/cov/readcovdata.go`
- ❌ `src/internal/coverage/calloc/batchcounteralloc.go`
- ❌ `src/internal/coverage/cformat/fmt_test.go`
- ❌ `src/internal/coverage/cformat/format.go`
- ❌ `src/internal/coverage/cmerge/merge.go`
- ❌ `src/internal/coverage/cmerge/merge_test.go`
- ❌ `src/internal/coverage/decodecounter/decodecounterfile.go`
- ❌ `src/internal/coverage/encodecounter/encode.go`
- ❌ `src/internal/coverage/pods/pods.go`
- ❌ `src/internal/coverage/pods/pods_test.go`
- ❌ `src/internal/coverage/stringtab/stringtab.go`
- ❌ `src/internal/coverage/test/counter_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/coverage`
- ❌ `src/cmd/compile/internal/gc`
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/covdata`
- ❌ `src/cmd/covdata/testdata`
- ❌ `src/cmd/internal/cov`
- ❌ `src/internal/coverage/calloc`
- ❌ `src/internal/coverage/cformat`
- ❌ `src/internal/coverage/cmerge`
- ❌ `src/internal/coverage/decodecounter`
- ❌ `src/internal/coverage/encodecounter`
- ❌ `src/internal/coverage/pods`
- ❌ `src/internal/coverage/stringtab`
- ❌ `src/internal/coverage/test`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/coverage/cover.go`
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/internal/typecheck/builtin.go`
- ❌ `src/cmd/compile/internal/typecheck/mkbuiltin.go`
- ❌ `src/cmd/compile/internal/typecheck/syms.go`
- ❌ `src/cmd/covdata/argsmerge.go`
- ❌ `src/cmd/covdata/covdata.go`
- ❌ `src/cmd/covdata/dump.go`
- ❌ `src/cmd/covdata/merge.go`
- ❌ `src/cmd/covdata/metamerge.go`
- ❌ `src/cmd/covdata/subtractintersect.go`
- ❌ `src/cmd/covdata/testdata/dep.go`
- ❌ `src/cmd/covdata/testdata/prog1.go`
- ❌ `src/cmd/covdata/testdata/prog2.go`
- ❌ `src/cmd/covdata/tool_test.go`
- ❌ `src/cmd/internal/cov/mreader.go`
- ❌ `src/cmd/internal/cov/readcovdata.go`
- ❌ `src/internal/coverage/calloc/batchcounteralloc.go`
- ❌ `src/internal/coverage/cformat/fmt_test.go`
- ❌ `src/internal/coverage/cformat/format.go`
- ❌ `src/internal/coverage/cmerge/merge.go`
- ❌ `src/internal/coverage/cmerge/merge_test.go`
- ❌ `src/internal/coverage/decodecounter/decodecounterfile.go`
- ❌ `src/internal/coverage/encodecounter/encode.go`
- ❌ `src/internal/coverage/pods/pods.go`
- ❌ `src/internal/coverage/pods/pods_test.go`
- ❌ `src/internal/coverage/stringtab/stringtab.go`
- ❌ `src/internal/coverage/test/counter_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/internal/coverage/pods/pods_test.go`, `TestPodCollection`)
- ❌ (`src/cmd/covdata/argsmerge.go`, `Merge`)
- ❌ (`src/cmd/covdata/argsmerge.go`, `ArgsSummary`)
- ❌ (`src/cmd/covdata/dump.go`, `makeDumpOp`)
- ❌ (`src/cmd/covdata/dump.go`, `Usage`)
- ❌ (`src/cmd/covdata/dump.go`, `Setup`)
- ❌ (`src/cmd/covdata/dump.go`, `BeginPod`)
- ❌ (`src/cmd/covdata/dump.go`, `EndPod`)
- ❌ (`src/cmd/covdata/dump.go`, `BeginCounterDataFile`)
- ❌ (`src/cmd/covdata/dump.go`, `VisitFuncCounterData`)
- ❌ (`src/cmd/covdata/dump.go`, `VisitMetaDataFile`)
- ❌ (`src/cmd/covdata/dump.go`, `BeginPackage`)
- ❌ (`src/cmd/covdata/dump.go`, `VisitFunc`)
- ❌ (`src/cmd/covdata/dump.go`, `Finish`)
- ❌ (`src/cmd/covdata/metamerge.go`, `newMetaMerge`)
- ❌ (`src/cmd/covdata/metamerge.go`, `visitMetaDataFile`)
- ❌ (`src/cmd/covdata/metamerge.go`, `beginCounterDataFile`)
- ❌ (`src/cmd/covdata/metamerge.go`, `copyMetaDataFile`)
- ❌ (`src/cmd/covdata/metamerge.go`, `beginPod`)
- ❌ (`src/cmd/covdata/metamerge.go`, `endPod`)
- ❌ (`src/cmd/covdata/metamerge.go`, `emitMeta`)
- ❌ (`src/cmd/covdata/metamerge.go`, `emitCounters`)
- ❌ (`src/cmd/covdata/metamerge.go`, `VisitFuncs`)
- ❌ (`src/cmd/covdata/metamerge.go`, `visitPackage`)
- ❌ (`src/cmd/covdata/metamerge.go`, `visitFuncCounterData`)
- ❌ (`src/cmd/covdata/metamerge.go`, `visitFunc`)
- ❌ (`src/cmd/covdata/tool_test.go`, `gobuild`)
- ❌ (`src/cmd/covdata/tool_test.go`, `emitFile`)
- ❌ (`src/cmd/covdata/tool_test.go`, `buildProg`)
- ❌ (`src/cmd/covdata/tool_test.go`, `TestCovTool`)
- ❌ (`src/cmd/covdata/tool_test.go`, `runToolOp`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testDump`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testPercent`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testPkgList`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testTextfmt`)
- ❌ (`src/cmd/covdata/tool_test.go`, `dumplines`)
- ❌ (`src/cmd/covdata/tool_test.go`, `runDumpChecks`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testMergeSimple`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testMergeSelect`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testMergeCombinePrograms`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testSubtract`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testIntersect`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testCounterClash`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testEmpty`)
- ❌ (`src/cmd/covdata/tool_test.go`, `testCommandLineErrors`)
- ❌ (`src/cmd/covdata/testdata/prog2.go`, `fifth`)
- ❌ (`src/cmd/covdata/testdata/prog2.go`, `sixth`)
- ❌ (`src/cmd/covdata/testdata/prog2.go`, `main`)
- ❌ (`src/cmd/covdata/testdata/prog1.go`, `first`)
- ❌ (`src/cmd/covdata/testdata/prog1.go`, `second`)
- ❌ (`src/cmd/covdata/testdata/prog1.go`, `third`)
- ❌ (`src/cmd/covdata/testdata/prog1.go`, `fourth`)
- ❌ (`src/cmd/covdata/testdata/prog1.go`, `main`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `makeSubtractIntersectOp`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `Usage`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `Setup`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `BeginPod`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `EndPod`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `EndCounters`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `pruneCounters`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `BeginCounterDataFile`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `VisitFuncCounterData`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `VisitMetaDataFile`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `BeginPackage`)
- ❌ (`src/cmd/covdata/subtractintersect.go`, `VisitFunc`)
- ❌ (`src/cmd/covdata/covdata.go`, `atExit`)
- ❌ (`src/cmd/covdata/covdata.go`, `Exit`)
- ❌ (`src/cmd/covdata/covdata.go`, `dbgtrace`)
- ❌ (`src/cmd/covdata/covdata.go`, `warn`)
- ❌ (`src/cmd/covdata/covdata.go`, `fatal`)
- ❌ (`src/cmd/covdata/covdata.go`, `usage`)
- ❌ (`src/cmd/covdata/covdata.go`, `main`)
- ❌ (`src/cmd/internal/cov/mreader.go`, `NewMreader`)
- ❌ (`src/cmd/internal/cov/mreader.go`, `Read`)
- ❌ (`src/cmd/internal/cov/mreader.go`, `ReadByte`)
- ❌ (`src/cmd/internal/cov/mreader.go`, `Seek`)
- ❌ (`src/cmd/covdata/testdata/dep.go`, `Dep1`)
- ❌ (`src/cmd/covdata/testdata/dep.go`, `PDep`)
- ❌ (`src/internal/coverage/cformat/fmt_test.go`, `TestBasics`)
- ❌ (`src/internal/coverage/cmerge/merge.go`, `MergeCounters`)
- ❌ (`src/internal/coverage/cmerge/merge.go`, `SaturatingAdd`)
- ❌ (`src/internal/coverage/cmerge/merge.go`, `SaturatingAdd`)
- ❌ (`src/internal/coverage/cmerge/merge.go`, `SetModeAndGranularity`)
- ❌ (`src/internal/coverage/cmerge/merge.go`, `ResetModeAndGranularity`)
- ❌ (`src/internal/coverage/cmerge/merge.go`, `Mode`)
- ❌ (`src/internal/coverage/cmerge/merge.go`, `Granularity`)
- ❌ (`src/internal/coverage/cformat/format.go`, `NewFormatter`)
- ❌ (`src/internal/coverage/cformat/format.go`, `SetPackage`)
- ❌ (`src/internal/coverage/cformat/format.go`, `AddUnit`)
- ❌ (`src/internal/coverage/cformat/format.go`, `sortUnits`)
- ❌ (`src/internal/coverage/cformat/format.go`, `EmitTextual`)
- ❌ (`src/internal/coverage/cformat/format.go`, `EmitPercent`)
- ❌ (`src/internal/coverage/cformat/format.go`, `EmitFuncs`)
- ❌ (`src/cmd/covdata/merge.go`, `makeMergeOp`)
- ❌ (`src/cmd/covdata/merge.go`, `Usage`)
- ❌ (`src/cmd/covdata/merge.go`, `Setup`)
- ❌ (`src/cmd/covdata/merge.go`, `BeginPod`)
- ❌ (`src/cmd/covdata/merge.go`, `EndPod`)
- ❌ (`src/cmd/covdata/merge.go`, `BeginCounterDataFile`)
- ❌ (`src/cmd/covdata/merge.go`, `VisitFuncCounterData`)
- ❌ (`src/cmd/covdata/merge.go`, `VisitMetaDataFile`)
- ❌ (`src/cmd/covdata/merge.go`, `BeginPackage`)
- ❌ (`src/cmd/covdata/merge.go`, `VisitFunc`)
- ❌ (`src/cmd/covdata/merge.go`, `Finish`)
- ❌ (`src/internal/coverage/calloc/batchcounteralloc.go`, `AllocateCounters`)
- ❌ (`src/cmd/internal/cov/readcovdata.go`, `MakeCovDataReader`)
- ❌ (`src/cmd/internal/cov/readcovdata.go`, `Visit`)
- ❌ (`src/cmd/internal/cov/readcovdata.go`, `verb`)
- ❌ (`src/cmd/internal/cov/readcovdata.go`, `warn`)
- ❌ (`src/cmd/internal/cov/readcovdata.go`, `fatal`)
- ❌ (`src/cmd/internal/cov/readcovdata.go`, `visitPod`)
- ❌ (`src/cmd/internal/cov/readcovdata.go`, `processPackage`)
- ❌ (`src/internal/coverage/pods/pods.go`, `CollectPods`)
- ❌ (`src/internal/coverage/pods/pods.go`, `CollectPodsFromFiles`)
- ❌ (`src/internal/coverage/pods/pods.go`, `collectPodsImpl`)
- ❌ (`src/internal/coverage/pods/pods.go`, `warning`)
- ❌ (`src/internal/coverage/cmerge/merge_test.go`, `TestClash`)
- ❌ (`src/internal/coverage/cmerge/merge_test.go`, `TestBasic`)
- ❌ (`src/internal/coverage/stringtab/stringtab.go`, `Lookup`)
- ❌ (`src/internal/coverage/stringtab/stringtab.go`, `Freeze`)
- ❌ (`src/internal/coverage/stringtab/stringtab.go`, `NewReader`)
- ❌ (`src/internal/coverage/stringtab/stringtab.go`, `Entries`)
- ❌ (`src/internal/coverage/stringtab/stringtab.go`, `Get`)
- ❌ (`src/internal/coverage/test/counter_test.go`, `VisitFuncs`)
- ❌ (`src/internal/coverage/test/counter_test.go`, `mkfunc`)
- ❌ (`src/internal/coverage/test/counter_test.go`, `TestCounterDataWriterReader`)
- ❌ (`src/internal/coverage/test/counter_test.go`, `TestCounterDataAppendSegment`)
- ❌ (`src/internal/coverage/encodecounter/encode.go`, `NewCoverageDataWriter`)
- ❌ (`src/internal/coverage/encodecounter/encode.go`, `Write`)
- ❌ (`src/internal/coverage/encodecounter/encode.go`, `padToFourByteBoundary`)
- ❌ (`src/internal/coverage/encodecounter/encode.go`, `writeSegmentPreamble`)
- ❌ (`src/internal/coverage/encodecounter/encode.go`, `AppendSegment`)
- ❌ (`src/internal/coverage/encodecounter/encode.go`, `writeHeader`)
- ❌ (`src/internal/coverage/encodecounter/encode.go`, `writeBytes`)
- ❌ (`src/internal/coverage/encodecounter/encode.go`, `writeCounters`)
- ❌ (`src/internal/coverage/encodecounter/encode.go`, `writeFooter`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `NewCounterDataReader`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `checkMagic`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `readFooter`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `readSegmentPreamble`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `readStringTable`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `readArgs`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `OsArgs`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `Goos`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `Goarch`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `NumSegments`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `BeginNextSegment`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `NumFunctionsInSegment`)
- ❌ (`src/internal/coverage/decodecounter/decodecounterfile.go`, `NextFunc`)
- ❌ (`src/cmd/compile/internal/gc/main.go`, `Main`)
- ❌ (`src/cmd/compile/internal/typecheck/mkbuiltin.go`, `main`)
- ❌ (`src/cmd/compile/internal/typecheck/mkbuiltin.go`, `mkbuiltin`)
- ❌ (`src/cmd/compile/internal/base/flag.go`, `ParseFlags`)
- ❌ (`src/cmd/compile/internal/base/flag.go`, `readCoverageCfg`)
- ❌ (`src/cmd/compile/internal/typecheck/syms.go`, `InitCoverage`)
- ❌ (`src/cmd/compile/internal/typecheck/syms.go`, `LookupCoverage`)
- ❌ (`src/cmd/compile/internal/coverage/cover.go`, `Fixup`)
- ❌ (`src/cmd/compile/internal/coverage/cover.go`, `metaHashAndLen`)
- ❌ (`src/cmd/compile/internal/coverage/cover.go`, `registerMeta`)
- ❌ (`src/cmd/compile/internal/coverage/cover.go`, `addInitHookCall`)
- ❌ (`src/cmd/compile/internal/typecheck/builtin.go`, `newSig`)
- ❌ (`src/cmd/compile/internal/typecheck/builtin.go`, `params`)
- ❌ (`src/cmd/compile/internal/typecheck/builtin.go`, `runtimeTypes`)
- ❌ (`src/cmd/compile/internal/typecheck/builtin.go`, `coverageTypes`)

### 📊 Proposal #51566

#### File Embeddings - Directory Level
- ✅ `src/io`
- ❌ `src/net/http`

#### File Embeddings - File Level
- ❌ `src/io/io.go`
- ✅ `src/io/io_test.go`
- ❌ `src/net/http/transfer.go`

#### Function Embeddings - Directory Level
- ✅ `src/io`
- ❌ `src/net/http`

#### Function Embeddings - File Level
- ❌ `src/io/io.go`
- ✅ `src/io/io_test.go`
- ❌ `src/net/http/transfer.go`

#### Function Embeddings - Function Level
- ❌ (`src/io/io_test.go`, `TestNopCloserWriterToForwarding`)
- ❌ (`src/net/http/transfer.go`, `unwrapBody`)
- ❌ (`src/net/http/transfer.go`, `unwrapNopCloser`)
- ❌ (`src/net/http/transfer.go`, `isKnownInMemoryReader`)
- ❌ (`src/io/io.go`, `NopCloser`)
- ❌ (`src/io/io.go`, `WriteTo`)

### 📊 Proposal #51572

#### File Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ✅ `src/cmd/go/internal/imports`
- ✅ `src/go/build`

#### File Embeddings - File Level
- ❌ `src/cmd/dist/build.go`
- ✅ `src/cmd/go/internal/imports/build.go`
- ✅ `src/go/build/build.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/dist`
- ❌ `src/cmd/go/internal/imports`
- ✅ `src/go/build`

#### Function Embeddings - File Level
- ❌ `src/cmd/dist/build.go`
- ❌ `src/cmd/go/internal/imports/build.go`
- ✅ `src/go/build/build.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/dist/build.go`, `matchtag`)
- ❌ (`src/go/build/build.go`, `matchTag`)
- ❌ (`src/cmd/go/internal/imports/build.go`, `matchTag`)
- ❌ (`src/cmd/go/internal/imports/build.go`, `matchTag`)

### 📊 Proposal #51644

#### File Embeddings - Directory Level
- ✅ `src/encoding/binary`

#### File Embeddings - File Level
- ✅ `src/encoding/binary/varint.go`
- ❌ `src/encoding/binary/varint_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/encoding/binary`

#### Function Embeddings - File Level
- ✅ `src/encoding/binary/varint.go`
- ❌ `src/encoding/binary/varint_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/encoding/binary/varint.go`, `AppendUvarint`)
- ✅ (`src/encoding/binary/varint.go`, `AppendVarint`)
- ❌ (`src/encoding/binary/varint_test.go`, `testVarint`)
- ❌ (`src/encoding/binary/varint_test.go`, `testUvarint`)

### 📊 Proposal #51668

#### File Embeddings - Directory Level
- ✅ `src/fmt`

#### File Embeddings - File Level
- ❌ `src/fmt/print.go`
- ❌ `src/fmt/state_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/fmt`

#### Function Embeddings - File Level
- ✅ `src/fmt/print.go`
- ❌ `src/fmt/state_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/fmt/state_test.go`, `Write`)
- ❌ (`src/fmt/state_test.go`, `Width`)
- ❌ (`src/fmt/state_test.go`, `Precision`)
- ❌ (`src/fmt/state_test.go`, `Flag`)
- ❌ (`src/fmt/state_test.go`, `mkState`)
- ❌ (`src/fmt/state_test.go`, `TestFormatString`)
- ✅ (`src/fmt/print.go`, `FormatString`)

### 📊 Proposal #51682

#### File Embeddings - Directory Level
- ✅ `src/cmd/compile/internal/types2`
- ❌ `src/go/types`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/types2/api_test.go`
- ✅ `src/cmd/compile/internal/types2/object.go`
- ❌ `src/cmd/compile/internal/types2/sizeof_test.go`
- ❌ `src/cmd/compile/internal/types2/subst.go`
- ❌ `src/go/types/api_test.go`
- ❌ `src/go/types/object.go`
- ❌ `src/go/types/sizeof_test.go`
- ❌ `src/go/types/subst.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/compile/internal/types2`
- ✅ `src/go/types`

#### Function Embeddings - File Level
- ✅ `src/cmd/compile/internal/types2/api_test.go`
- ✅ `src/cmd/compile/internal/types2/object.go`
- ❌ `src/cmd/compile/internal/types2/sizeof_test.go`
- ❌ `src/cmd/compile/internal/types2/subst.go`
- ❌ `src/go/types/api_test.go`
- ❌ `src/go/types/object.go`
- ❌ `src/go/types/sizeof_test.go`
- ❌ `src/go/types/subst.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/types/subst.go`, `func_`)
- ❌ (`src/go/types/subst.go`, `replaceRecvType`)
- ✅ (`src/cmd/compile/internal/types2/object.go`, `Origin`)
- ❌ (`src/cmd/compile/internal/types2/object.go`, `NewFunc`)
- ✅ (`src/cmd/compile/internal/types2/object.go`, `Origin`)
- ❌ (`src/cmd/compile/internal/types2/subst.go`, `func_`)
- ❌ (`src/cmd/compile/internal/types2/subst.go`, `replaceRecvType`)
- ❌ (`src/go/types/api_test.go`, `TestUsesInfo`)
- ❌ (`src/go/types/api_test.go`, `TestInstantiatedObjects`)
- ❌ (`src/go/types/api_test.go`, `originObject`)
- ❌ (`src/go/types/object.go`, `Origin`)
- ❌ (`src/go/types/object.go`, `NewFunc`)
- ❌ (`src/go/types/object.go`, `Origin`)
- ❌ (`src/cmd/compile/internal/types2/sizeof_test.go`, `TestSizeof`)
- ❌ (`src/go/types/sizeof_test.go`, `TestSizeof`)
- ✅ (`src/cmd/compile/internal/types2/api_test.go`, `TestInstantiatedObjects`)
- ❌ (`src/cmd/compile/internal/types2/api_test.go`, `originObject`)

### 📊 Proposal #51684

#### File Embeddings - Directory Level
- ✅ `src/regexp/syntax`

#### File Embeddings - File Level
- ✅ `src/regexp/syntax/parse.go`

#### Function Embeddings - Directory Level
- ✅ `src/regexp/syntax`

#### Function Embeddings - File Level
- ✅ `src/regexp/syntax/parse.go`

#### Function Embeddings - Function Level
- ❌ (`src/regexp/syntax/parse.go`, `checkHeight`)
- ❌ (`src/regexp/syntax/parse.go`, `parse`)
- ❌ (`src/regexp/syntax/parse.go`, `checkHeight`)
- ❌ (`src/regexp/syntax/parse.go`, `parse`)

### 📊 Proposal #51766

#### File Embeddings - Directory Level
- ✅ `src/net/netip`

#### File Embeddings - File Level
- ❌ `src/net/netip/netip_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/netip`

#### Function Embeddings - File Level
- ✅ `src/net/netip/netip_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/net/netip/netip_test.go`, `TestAddrWellKnown`)
- ❌ (`src/net/netip/netip_test.go`, `TestNoAllocs`)

### 📊 Proposal #51777

#### File Embeddings - Directory Level
- ✅ `src/net/netip`

#### File Embeddings - File Level
- ❌ `src/net/netip/netip_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/netip`

#### Function Embeddings - File Level
- ❌ `src/net/netip/netip_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/netip/netip_test.go`, `TestAddrWellKnown`)
- ❌ (`src/net/netip/netip_test.go`, `TestNoAllocs`)

### 📊 Proposal #51868

#### File Embeddings - Directory Level
- ✅ `src/debug/pe`

#### File Embeddings - File Level
- ✅ `src/debug/pe/symbol.go`
- ❌ `src/debug/pe/symbols_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/debug/pe`

#### Function Embeddings - File Level
- ✅ `src/debug/pe/symbol.go`
- ❌ `src/debug/pe/symbols_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/debug/pe/symbols_test.go`, `TestReadCOFFSymbolAuxInfo`)
- ❌ (`src/debug/pe/symbol.go`, `COFFSymbolReadSectionDefAux`)

### 📊 Proposal #51896

#### File Embeddings - Directory Level
- ✅ `src/unicode/utf16`

#### File Embeddings - File Level
- ✅ `src/unicode/utf16/utf16.go`
- ✅ `src/unicode/utf16/utf16_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/unicode/utf16`

#### Function Embeddings - File Level
- ✅ `src/unicode/utf16/utf16.go`
- ❌ `src/unicode/utf16/utf16_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/unicode/utf16/utf16_test.go`, `TestAppendRune`)
- ❌ (`src/unicode/utf16/utf16_test.go`, `BenchmarkAppendRuneValidASCII`)
- ❌ (`src/unicode/utf16/utf16_test.go`, `BenchmarkAppendRuneValidJapaneseChars`)
- ✅ (`src/unicode/utf16/utf16.go`, `AppendRune`)

### 📊 Proposal #51914

#### File Embeddings - Directory Level
- ❌ `src/net/http/httputil`

#### File Embeddings - File Level
- ❌ `src/net/http/httputil/reverseproxy.go`
- ❌ `src/net/http/httputil/reverseproxy_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/http/httputil`

#### Function Embeddings - File Level
- ❌ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/net/http/httputil/reverseproxy_test.go`, `Test1xxResponses`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `ServeHTTP`)

### 📊 Proposal #51972

#### File Embeddings - Directory Level
- ✅ `src/sync`

#### File Embeddings - File Level
- ❌ `src/sync/map.go`
- ✅ `src/sync/map_reference_test.go`
- ✅ `src/sync/map_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/sync`

#### Function Embeddings - File Level
- ✅ `src/sync/map.go`
- ❌ `src/sync/map_reference_test.go`
- ✅ `src/sync/map_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/sync/map_test.go`, `apply`)
- ❌ (`src/sync/map_test.go`, `TestCompareAndSwap_NonExistingKey`)
- ❌ (`src/sync/map_reference_test.go`, `Swap`)
- ❌ (`src/sync/map_reference_test.go`, `CompareAndSwap`)
- ❌ (`src/sync/map_reference_test.go`, `CompareAndDelete`)
- ❌ (`src/sync/map_reference_test.go`, `Swap`)
- ❌ (`src/sync/map_reference_test.go`, `CompareAndSwap`)
- ❌ (`src/sync/map_reference_test.go`, `CompareAndDelete`)
- ❌ (`src/sync/map.go`, `Store`)
- ❌ (`src/sync/map.go`, `tryCompareAndSwap`)
- ❌ (`src/sync/map.go`, `unexpungeLocked`)
- ❌ (`src/sync/map.go`, `swapLocked`)
- ✅ (`src/sync/map.go`, `LoadOrStore`)
- ✅ (`src/sync/map.go`, `trySwap`)
- ✅ (`src/sync/map.go`, `Swap`)
- ✅ (`src/sync/map.go`, `CompareAndSwap`)
- ❌ (`src/sync/map.go`, `CompareAndDelete`)

### 📊 Proposal #52221

#### File Embeddings - Directory Level
- ✅ `src/crypto/ecdh`
- ✅ `src/crypto/ecdsa`
- ✅ `src/crypto/elliptic`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`

#### File Embeddings - File Level
- ✅ `src/crypto/ecdh/ecdh.go`
- ❌ `src/crypto/ecdh/ecdh_test.go`
- ✅ `src/crypto/ecdh/nist.go`
- ❌ `src/crypto/ecdh/x25519.go`
- ❌ `src/crypto/ecdsa/ecdsa.go`
- ✅ `src/crypto/elliptic/elliptic.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_client_tls13.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/handshake_server_tls13.go`
- ❌ `src/crypto/tls/key_agreement.go`
- ❌ `src/crypto/tls/key_schedule.go`
- ❌ `src/crypto/x509/pkcs8.go`
- ❌ `src/crypto/x509/pkcs8_test.go`
- ❌ `src/crypto/x509/sec1.go`
- ❌ `src/crypto/x509/x509.go`

#### Function Embeddings - Directory Level
- ❌ `src/crypto/ecdh`
- ✅ `src/crypto/ecdsa`
- ❌ `src/crypto/elliptic`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`

#### Function Embeddings - File Level
- ❌ `src/crypto/ecdh/ecdh.go`
- ❌ `src/crypto/ecdh/ecdh_test.go`
- ❌ `src/crypto/ecdh/nist.go`
- ❌ `src/crypto/ecdh/x25519.go`
- ✅ `src/crypto/ecdsa/ecdsa.go`
- ❌ `src/crypto/elliptic/elliptic.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_client_tls13.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/handshake_server_tls13.go`
- ❌ `src/crypto/tls/key_agreement.go`
- ❌ `src/crypto/tls/key_schedule.go`
- ❌ `src/crypto/x509/pkcs8.go`
- ❌ `src/crypto/x509/pkcs8_test.go`
- ❌ `src/crypto/x509/sec1.go`
- ❌ `src/crypto/x509/x509.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/tls/handshake_client_tls13.go`, `handshake`)
- ❌ (`src/crypto/tls/handshake_client_tls13.go`, `processHelloRetryRequest`)
- ❌ (`src/crypto/tls/handshake_client_tls13.go`, `processServerHello`)
- ❌ (`src/crypto/tls/handshake_client_tls13.go`, `establishHandshakeKeys`)
- ❌ (`src/crypto/tls/handshake_server_test.go`, `TestAESCipherReorderingTLS13`)
- ❌ (`src/crypto/ecdh/x25519.go`, `String`)
- ❌ (`src/crypto/ecdh/x25519.go`, `GenerateKey`)
- ❌ (`src/crypto/ecdh/x25519.go`, `NewPrivateKey`)
- ❌ (`src/crypto/ecdh/x25519.go`, `NewPublicKey`)
- ❌ (`src/crypto/ecdh/x25519.go`, `x25519ScalarMult`)
- ❌ (`src/crypto/tls/handshake_server_tls13.go`, `processClientHello`)
- ❌ (`src/crypto/tls/handshake_client.go`, `makeClientHello`)
- ❌ (`src/crypto/tls/handshake_client.go`, `clientHandshake`)
- ❌ (`src/crypto/ecdh/ecdh.go`, `Bytes`)
- ❌ (`src/crypto/ecdh/ecdh.go`, `Equal`)
- ❌ (`src/crypto/ecdh/ecdh.go`, `Curve`)
- ❌ (`src/crypto/ecdh/ecdh.go`, `Bytes`)
- ❌ (`src/crypto/ecdh/ecdh.go`, `Equal`)
- ❌ (`src/crypto/ecdh/ecdh.go`, `Curve`)
- ❌ (`src/crypto/ecdh/ecdh.go`, `PublicKey`)
- ❌ (`src/crypto/ecdh/ecdh.go`, `Public`)
- ❌ (`src/crypto/tls/key_agreement.go`, `generateServerKeyExchange`)
- ❌ (`src/crypto/tls/key_agreement.go`, `processClientKeyExchange`)
- ❌ (`src/crypto/tls/key_agreement.go`, `processServerKeyExchange`)
- ❌ (`src/crypto/tls/key_schedule.go`, `generateECDHEKey`)
- ❌ (`src/crypto/tls/key_schedule.go`, `curveForCurveID`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `TestECDH`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `Read`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `TestGenerateKey`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `TestVectors`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `hexDecode`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `TestString`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `testAllCurves`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `BenchmarkECDH`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `benchmarkAllCurves`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `Read`)
- ❌ (`src/crypto/ecdh/nist.go`, `String`)
- ❌ (`src/crypto/ecdh/nist.go`, `GenerateKey`)
- ❌ (`src/crypto/ecdh/nist.go`, `NewPrivateKey`)
- ❌ (`src/crypto/ecdh/nist.go`, `NewPublicKey`)
- ❌ (`src/crypto/ecdh/ecdh_test.go`, `TestLinker`)
- ❌ (`src/crypto/x509/pkcs8.go`, `MarshalPKCS8PrivateKey`)
- ❌ (`src/crypto/x509/sec1.go`, `marshalECDHPrivateKey`)
- ❌ (`src/crypto/x509/x509.go`, `marshalPublicKey`)
- ❌ (`src/crypto/x509/x509.go`, `oidFromECDHCurve`)
- ✅ (`src/crypto/ecdsa/ecdsa.go`, `ECDH`)
- ✅ (`src/crypto/ecdsa/ecdsa.go`, `ECDH`)
- ❌ (`src/crypto/ecdsa/ecdsa.go`, `curveToECDH`)
- ❌ (`src/crypto/x509/pkcs8_test.go`, `TestPKCS8`)
- ❌ (`src/crypto/elliptic/elliptic.go`, `GenerateKey`)
- ❌ (`src/crypto/elliptic/elliptic.go`, `Marshal`)
- ❌ (`src/crypto/elliptic/elliptic.go`, `Unmarshal`)

### 📊 Proposal #52376

#### File Embeddings - Directory Level
- ✅ `src/reflect`

#### File Embeddings - File Level
- ❌ `src/reflect/all_test.go`
- ❌ `src/reflect/value.go`

#### Function Embeddings - Directory Level
- ✅ `src/reflect`

#### Function Embeddings - File Level
- ❌ `src/reflect/all_test.go`
- ✅ `src/reflect/value.go`

#### Function Embeddings - Function Level
- ✅ (`src/reflect/value.go`, `IsZero`)
- ✅ (`src/reflect/value.go`, `SetZero`)
- ❌ (`src/reflect/all_test.go`, `TestIsZero`)

### 📊 Proposal #52444

#### File Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### File Embeddings - File Level
- ✅ `src/crypto/x509/x509.go`
- ❌ `src/crypto/x509/x509_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### Function Embeddings - File Level
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/crypto/x509/x509.go`, `CreateCertificate`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestParseNegativeSerial`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateNegativeSerial`)
- ✅ (`src/crypto/x509/x509.go`, `CreateCertificate`)

### 📊 Proposal #52463

#### File Embeddings - Directory Level
- ❌ `src/cmd/gofmt`

#### File Embeddings - File Level
- ❌ `src/cmd/gofmt/gofmt.go`
- ❌ `src/cmd/gofmt/simplify.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/gofmt`

#### Function Embeddings - File Level
- ❌ `src/cmd/gofmt/gofmt.go`
- ❌ `src/cmd/gofmt/simplify.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/gofmt/gofmt.go`, `initParserMode`)
- ❌ (`src/cmd/gofmt/simplify.go`, `Visit`)

### 📊 Proposal #52746

#### File Embeddings - Directory Level
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ❌ `src/cmd/go/internal/vcs`

#### File Embeddings - File Level
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ❌ `src/cmd/go/internal/vcs/vcs.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ❌ `src/cmd/go/internal/vcs`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ❌ `src/cmd/go/internal/vcs/vcs.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/vcs/vcs.go`, `fossilStatus`)
- ❌ (`src/cmd/go/internal/modfetch/codehost/vcs.go`, `fossilParseStat`)

### 📊 Proposal #52792

#### File Embeddings - Directory Level
- ✅ `src/cmd/go/internal/modfetch`
- ✅ `src/cmd/go/internal/modload`

#### File Embeddings - File Level
- ✅ `src/cmd/go/internal/modfetch/fetch.go`
- ❌ `src/cmd/go/internal/modload/build.go`

#### Function Embeddings - Directory Level
- ✅ `src/cmd/go/internal/modfetch`
- ✅ `src/cmd/go/internal/modload`

#### Function Embeddings - File Level
- ❌ `src/cmd/go/internal/modfetch/fetch.go`
- ❌ `src/cmd/go/internal/modload/build.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/go/internal/modload/build.go`, `moduleInfo`)
- ❌ (`src/cmd/go/internal/modload/build.go`, `moduleInfo`)
- ❌ (`src/cmd/go/internal/modfetch/fetch.go`, `RecordedSum`)

### 📊 Proposal #53002

#### File Embeddings - Directory Level
- ✅ `src/net/http/httputil`

#### File Embeddings - File Level
- ❌ `src/net/http/httputil/example_test.go`
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/net/http/httputil`

#### Function Embeddings - File Level
- ✅ `src/net/http/httputil/example_test.go`
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`

#### Function Embeddings - Function Level
- ✅ (`src/net/http/httputil/reverseproxy_test.go`, `TestReverseProxyRewriteStripsForwarded`)
- ❌ (`src/net/http/httputil/reverseproxy_test.go`, `TestSetURL`)
- ✅ (`src/net/http/httputil/reverseproxy_test.go`, `TestReverseProxyRewriteReplacesOut`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `SetURL`)
- ✅ (`src/net/http/httputil/reverseproxy.go`, `SetXForwarded`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `NewSingleHostReverseProxy`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `rewriteRequestURL`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `copyHeader`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `getErrorHandler`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `modifyResponse`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `ServeHTTP`)
- ❌ (`src/net/http/httputil/reverseproxy.go`, `removeHopByHopHeaders`)
- ✅ (`src/net/http/httputil/example_test.go`, `ExampleReverseProxy`)

### 📊 Proposal #53003

#### File Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/escape`
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/compile/internal/types2`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/go/types`
- ❌ `src/unsafe`
- ✅ `test`

#### File Embeddings - File Level
- ❌ `src/cmd/compile/internal/escape/expr.go`
- ❌ `src/cmd/compile/internal/ir/expr.go`
- ❌ `src/cmd/compile/internal/ir/op_string.go`
- ❌ `src/cmd/compile/internal/noder/reader.go`
- ❌ `src/cmd/compile/internal/noder/writer.go`
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/compile/internal/typecheck/const.go`
- ❌ `src/cmd/compile/internal/typecheck/func.go`
- ❌ `src/cmd/compile/internal/typecheck/typecheck.go`
- ❌ `src/cmd/compile/internal/types2/builtins.go`
- ❌ `src/cmd/compile/internal/walk/builtin.go`
- ❌ `src/cmd/compile/internal/walk/expr.go`
- ❌ `src/go/types/builtins.go`
- ❌ `src/unsafe/unsafe.go`
- ✅ `test/unsafe_slice_data.go`
- ❌ `test/unsafe_string.go`
- ❌ `test/unsafebuiltins.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/compile/internal/escape`
- ❌ `src/cmd/compile/internal/ir`
- ❌ `src/cmd/compile/internal/noder`
- ❌ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/compile/internal/types2`
- ❌ `src/cmd/compile/internal/walk`
- ❌ `src/go/types`
- ❌ `src/unsafe`
- ✅ `test`

#### Function Embeddings - File Level
- ❌ `src/cmd/compile/internal/escape/expr.go`
- ❌ `src/cmd/compile/internal/ir/expr.go`
- ❌ `src/cmd/compile/internal/ir/op_string.go`
- ❌ `src/cmd/compile/internal/noder/reader.go`
- ❌ `src/cmd/compile/internal/noder/writer.go`
- ❌ `src/cmd/compile/internal/ssagen/ssa.go`
- ❌ `src/cmd/compile/internal/typecheck/const.go`
- ❌ `src/cmd/compile/internal/typecheck/func.go`
- ❌ `src/cmd/compile/internal/typecheck/typecheck.go`
- ❌ `src/cmd/compile/internal/types2/builtins.go`
- ❌ `src/cmd/compile/internal/walk/builtin.go`
- ❌ `src/cmd/compile/internal/walk/expr.go`
- ❌ `src/go/types/builtins.go`
- ❌ `src/unsafe/unsafe.go`
- ✅ `test/unsafe_slice_data.go`
- ❌ `test/unsafe_string.go`
- ❌ `test/unsafebuiltins.go`

#### Function Embeddings - Function Level
- ❌ (`src/cmd/compile/internal/types2/builtins.go`, `builtin`)
- ❌ (`test/unsafebuiltins.go`, `main`)
- ❌ (`src/cmd/compile/internal/noder/writer.go`, `expr`)
- ❌ (`test/unsafe_string.go`, `main`)
- ❌ (`src/cmd/compile/internal/escape/expr.go`, `exprSkipInit`)
- ❌ (`src/cmd/compile/internal/walk/builtin.go`, `walkUnsafeString`)
- ❌ (`src/cmd/compile/internal/typecheck/const.go`, `callOrChan`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `stmt`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `softfloatInit`)
- ❌ (`src/cmd/compile/internal/typecheck/typecheck.go`, `typecheck1`)
- ❌ (`src/cmd/compile/internal/walk/expr.go`, `walkExpr1`)
- ❌ (`src/cmd/compile/internal/ir/op_string.go`, `_`)
- ❌ (`src/cmd/compile/internal/ir/expr.go`, `SetOp`)
- ❌ (`src/unsafe/unsafe.go`, `String`)
- ❌ (`src/cmd/compile/internal/noder/reader.go`, `expr`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcCall`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcUnsafeString`)
- ❌ (`src/go/types/builtins.go`, `builtin`)
- ❌ (`src/cmd/compile/internal/types2/builtins.go`, `builtin`)
- ❌ (`test/unsafebuiltins.go`, `main`)
- ❌ (`src/cmd/compile/internal/typecheck/const.go`, `callOrChan`)
- ❌ (`src/cmd/compile/internal/typecheck/typecheck.go`, `typecheck1`)
- ❌ (`src/cmd/compile/internal/walk/expr.go`, `walkExpr1`)
- ❌ (`src/cmd/compile/internal/ir/op_string.go`, `_`)
- ❌ (`src/cmd/compile/internal/ir/expr.go`, `SetOp`)
- ❌ (`src/unsafe/unsafe.go`, `StringData`)
- ❌ (`src/cmd/compile/internal/escape/expr.go`, `exprSkipInit`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcCall`)
- ❌ (`src/go/types/builtins.go`, `builtin`)
- ❌ (`src/cmd/compile/internal/types2/builtins.go`, `builtin`)
- ❌ (`src/cmd/compile/internal/typecheck/const.go`, `callOrChan`)
- ❌ (`src/cmd/compile/internal/typecheck/typecheck.go`, `typecheck1`)
- ❌ (`src/cmd/compile/internal/walk/expr.go`, `walkExpr1`)
- ❌ (`src/cmd/compile/internal/ir/op_string.go`, `_`)
- ✅ (`test/unsafe_slice_data.go`, `main`)
- ❌ (`src/cmd/compile/internal/ir/expr.go`, `SetOp`)
- ❌ (`src/unsafe/unsafe.go`, `SliceData`)
- ❌ (`src/cmd/compile/internal/escape/expr.go`, `exprSkipInit`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcCall`)
- ❌ (`src/go/types/builtins.go`, `builtin`)
- ❌ (`src/cmd/compile/internal/typecheck/const.go`, `callOrChan`)
- ❌ (`src/cmd/compile/internal/noder/writer.go`, `expr`)
- ❌ (`src/cmd/compile/internal/ssagen/ssa.go`, `stmt`)
- ❌ (`src/cmd/compile/internal/typecheck/typecheck.go`, `typecheck1`)
- ❌ (`src/cmd/compile/internal/walk/expr.go`, `walkExpr1`)
- ❌ (`src/cmd/compile/internal/ir/op_string.go`, `_`)
- ❌ (`src/cmd/compile/internal/ir/expr.go`, `SetOp`)
- ❌ (`src/cmd/compile/internal/ir/expr.go`, `SetOp`)
- ❌ (`src/cmd/compile/internal/noder/reader.go`, `expr`)
- ❌ (`src/cmd/compile/internal/escape/expr.go`, `exprSkipInit`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcCall`)
- ❌ (`src/cmd/compile/internal/typecheck/func.go`, `tcUnsafeString`)
- ❌ (`src/cmd/compile/internal/walk/builtin.go`, `walkUnsafeString`)
- ❌ (`src/cmd/compile/internal/types2/builtins.go`, `builtin`)
- ❌ (`src/unsafe/unsafe.go`, `SliceData`)
- ❌ (`src/unsafe/unsafe.go`, `String`)
- ❌ (`src/unsafe/unsafe.go`, `StringData`)
- ❌ (`src/go/types/builtins.go`, `builtin`)
- ❌ (`src/cmd/compile/internal/types2/builtins.go`, `builtin`)
- ❌ (`src/go/types/builtins.go`, `builtin`)

### 📊 Proposal #53015

#### File Embeddings - Directory Level
- ❌ `src/html/template`
- ✅ `src/text/template`
- ❌ `src/text/template/parse`

#### File Embeddings - File Level
- ❌ `src/html/template/escape.go`
- ❌ `src/html/template/escape_test.go`
- ✅ `src/text/template/exec.go`
- ❌ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/lex_test.go`
- ❌ `src/text/template/parse/node.go`
- ❌ `src/text/template/parse/parse.go`

#### Function Embeddings - Directory Level
- ✅ `src/html/template`
- ✅ `src/text/template`
- ❌ `src/text/template/parse`

#### Function Embeddings - File Level
- ❌ `src/html/template/escape.go`
- ❌ `src/html/template/escape_test.go`
- ✅ `src/text/template/exec.go`
- ❌ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/lex_test.go`
- ❌ `src/text/template/parse/node.go`
- ❌ `src/text/template/parse/parse.go`

#### Function Embeddings - Function Level
- ❌ (`src/html/template/escape.go`, `escape`)
- ❌ (`src/html/template/escape.go`, `joinRange`)
- ❌ (`src/text/template/parse/lex_test.go`, `collect`)
- ❌ (`src/text/template/parse/node.go`, `Copy`)
- ❌ (`src/text/template/parse/lex.go`, `lexIdentifier`)
- ❌ (`src/html/template/escape_test.go`, `TestErrors`)
- ❌ (`src/text/template/exec.go`, `execute`)
- ❌ (`src/text/template/exec.go`, `walk`)
- ❌ (`src/text/template/exec.go`, `walkTemplate`)
- ❌ (`src/text/template/parse/parse.go`, `startParse`)
- ❌ (`src/text/template/parse/parse.go`, `action`)

### 📊 Proposal #53021

#### File Embeddings - Directory Level
- ❌ `src/crypto/cipher`
- ✅ `src/crypto/subtle`

#### File Embeddings - File Level
- ❌ `src/crypto/cipher/cbc.go`
- ❌ `src/crypto/cipher/cfb.go`
- ❌ `src/crypto/cipher/ctr.go`
- ❌ `src/crypto/cipher/ofb.go`
- ✅ `src/crypto/subtle/xor.go`
- ❌ `src/crypto/subtle/xor_test.go`

#### Function Embeddings - Directory Level
- ❌ `src/crypto/cipher`
- ✅ `src/crypto/subtle`

#### Function Embeddings - File Level
- ❌ `src/crypto/cipher/cbc.go`
- ❌ `src/crypto/cipher/cfb.go`
- ❌ `src/crypto/cipher/ctr.go`
- ❌ `src/crypto/cipher/ofb.go`
- ❌ `src/crypto/subtle/xor.go`
- ✅ `src/crypto/subtle/xor_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/cipher/ofb.go`, `XORKeyStream`)
- ❌ (`src/crypto/subtle/xor_test.go`, `TestXORBytes`)
- ✅ (`src/crypto/subtle/xor_test.go`, `TestXorBytesPanic`)
- ❌ (`src/crypto/subtle/xor_test.go`, `BenchmarkXORBytes`)
- ❌ (`src/crypto/subtle/xor_test.go`, `mustPanic`)
- ❌ (`src/crypto/cipher/cfb.go`, `XORKeyStream`)
- ❌ (`src/crypto/cipher/cbc.go`, `CryptBlocks`)
- ❌ (`src/crypto/cipher/cbc.go`, `CryptBlocks`)
- ❌ (`src/crypto/subtle/xor.go`, `XORBytes`)
- ❌ (`src/crypto/cipher/ctr.go`, `XORKeyStream`)

### 📊 Proposal #53200

#### File Embeddings - Directory Level
- ✅ `src/go/token`

#### File Embeddings - File Level
- ✅ `src/go/token/position.go`
- ❌ `src/go/token/position_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/go/token`

#### Function Embeddings - File Level
- ✅ `src/go/token/position.go`
- ❌ `src/go/token/position_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/go/token/position.go`, `RemoveFile`)
- ❌ (`src/go/token/position_test.go`, `TestRemoveFile`)

### 📊 Proposal #53346

#### File Embeddings - Directory Level
- ✅ `src/encoding/xml`

#### File Embeddings - File Level
- ❌ `src/encoding/xml/marshal.go`
- ❌ `src/encoding/xml/marshal_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/encoding/xml`

#### Function Embeddings - File Level
- ✅ `src/encoding/xml/marshal.go`
- ✅ `src/encoding/xml/marshal_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/encoding/xml/marshal.go`, `Marshal`)
- ❌ (`src/encoding/xml/marshal.go`, `MarshalIndent`)
- ❌ (`src/encoding/xml/marshal.go`, `NewEncoder`)
- ❌ (`src/encoding/xml/marshal.go`, `Encode`)
- ❌ (`src/encoding/xml/marshal.go`, `EncodeElement`)
- ✅ (`src/encoding/xml/marshal.go`, `EncodeToken`)
- ❌ (`src/encoding/xml/marshal.go`, `isValidDirective`)
- ❌ (`src/encoding/xml/marshal.go`, `Flush`)
- ❌ (`src/encoding/xml/marshal.go`, `Close`)
- ❌ (`src/encoding/xml/marshal.go`, `Write`)
- ❌ (`src/encoding/xml/marshal.go`, `WriteString`)
- ❌ (`src/encoding/xml/marshal.go`, `WriteByte`)
- ❌ (`src/encoding/xml/marshal.go`, `Close`)
- ❌ (`src/encoding/xml/marshal_test.go`, `TestClose`)

### 📊 Proposal #53466

#### File Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ❌ `src/cmd/link`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/cmd/link/internal/riscv64`
- ✅ `src/runtime`
- ❌ `src/syscall`

#### File Embeddings - File Level
- ❌ `src/cmd/dist/main.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/link/elf_test.go`
- ❌ `src/cmd/link/internal/ld/lib.go`
- ❌ `src/cmd/link/internal/riscv64/obj.go`
- ❌ `src/cmd/link/link_test.go`
- ❌ `src/runtime/defs_freebsd_riscv64.go`
- ❌ `src/runtime/vdso_freebsd_riscv64.go`
- ❌ `src/syscall/syscall_freebsd_riscv64.go`
- ❌ `src/syscall/zsyscall_freebsd_riscv64.go`

#### Function Embeddings - Directory Level
- ❌ `src/cmd/dist`
- ❌ `src/cmd/link`
- ❌ `src/cmd/link/internal/ld`
- ❌ `src/cmd/link/internal/riscv64`
- ✅ `src/runtime`
- ❌ `src/syscall`

#### Function Embeddings - File Level
- ❌ `src/cmd/dist/main.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/link/elf_test.go`
- ❌ `src/cmd/link/internal/ld/lib.go`
- ❌ `src/cmd/link/internal/riscv64/obj.go`
- ❌ `src/cmd/link/link_test.go`
- ❌ `src/runtime/defs_freebsd_riscv64.go`
- ❌ `src/runtime/vdso_freebsd_riscv64.go`
- ❌ `src/syscall/syscall_freebsd_riscv64.go`
- ❌ `src/syscall/zsyscall_freebsd_riscv64.go`

#### Function Embeddings - Function Level
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `getgroups`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `setgroups`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `wait4`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `accept`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `bind`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `connect`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `socket`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `getsockopt`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `setsockopt`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `getpeername`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `getsockname`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Shutdown`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `socketpair`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `recvfrom`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `sendto`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `recvmsg`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `sendmsg`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `kevent`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `sysctl`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `utimes`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `futimes`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `fcntl`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `pipe2`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Access`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Adjtime`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Chdir`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Chflags`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Chmod`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Chown`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Chroot`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Close`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Dup`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Dup2`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Fchdir`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Fchflags`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Fchmod`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Fchown`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Flock`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Fpathconf`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Fstat`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Fstatat`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Fstatfs`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Fsync`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Ftruncate`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `getdirentries`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getdtablesize`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getegid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Geteuid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getgid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getpgid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getpgrp`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getpid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getppid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getpriority`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getrlimit`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getrusage`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getsid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Gettimeofday`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Getuid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Issetugid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Kill`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Kqueue`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Lchown`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Link`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Listen`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Mkdir`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Mkfifo`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `mknodat`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Nanosleep`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Open`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Pathconf`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `pread`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `pwrite`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `read`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Readlink`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Rename`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Revoke`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Rmdir`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Seek`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Select`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Setegid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Seteuid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Setgid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Setlogin`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Setpgid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Setpriority`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Setregid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Setreuid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Setsid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Settimeofday`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Setuid`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Statfs`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Symlink`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Sync`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Truncate`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Umask`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Undelete`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Unlink`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `Unmount`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `write`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `mmap`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `munmap`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `readlen`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `accept4`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `utimensat`)
- ❌ (`src/syscall/zsyscall_freebsd_riscv64.go`, `getcwd`)
- ❌ (`src/syscall/syscall_freebsd_riscv64.go`, `setTimespec`)
- ❌ (`src/syscall/syscall_freebsd_riscv64.go`, `setTimeval`)
- ❌ (`src/syscall/syscall_freebsd_riscv64.go`, `SetKevent`)
- ❌ (`src/syscall/syscall_freebsd_riscv64.go`, `SetLen`)
- ❌ (`src/syscall/syscall_freebsd_riscv64.go`, `SetControllen`)
- ❌ (`src/syscall/syscall_freebsd_riscv64.go`, `SetLen`)
- ❌ (`src/syscall/syscall_freebsd_riscv64.go`, `sendfile`)
- ❌ (`src/syscall/syscall_freebsd_riscv64.go`, `Syscall9`)
- ❌ (`src/runtime/defs_freebsd_riscv64.go`, `setNsec`)
- ❌ (`src/runtime/defs_freebsd_riscv64.go`, `set_usec`)
- ❌ (`src/runtime/vdso_freebsd_riscv64.go`, `getTimecounter`)
- ❌ (`src/cmd/dist/test.go`, `extLink`)
- ❌ (`src/cmd/dist/main.go`, `main`)
- ❌ (`src/cmd/link/internal/riscv64/obj.go`, `Init`)
- ❌ (`src/cmd/link/internal/riscv64/obj.go`, `archinit`)
- ❌ (`src/cmd/link/elf_test.go`, `TestMinusRSymsWithSameName`)
- ❌ (`src/cmd/link/link_test.go`, `TestIssue33979`)
- ❌ (`src/cmd/link/internal/ld/lib.go`, `extld`)

### 📊 Proposal #53482

#### File Embeddings - Directory Level
- ✅ `src/net`

#### File Embeddings - File Level
- ❌ `src/net/interface_aix.go`
- ❌ `src/net/interface_bsd.go`
- ✅ `src/net/interface_linux.go`
- ❌ `src/net/interface_plan9.go`
- ✅ `src/net/interface_solaris.go`
- ❌ `src/net/interface_windows.go`

#### Function Embeddings - Directory Level
- ✅ `src/net`

#### Function Embeddings - File Level
- ❌ `src/net/interface_aix.go`
- ✅ `src/net/interface_bsd.go`
- ❌ `src/net/interface_linux.go`
- ❌ `src/net/interface_plan9.go`
- ❌ `src/net/interface_solaris.go`
- ✅ `src/net/interface_windows.go`

#### Function Embeddings - Function Level
- ❌ (`src/net/interface_solaris.go`, `linkFlags`)
- ❌ (`src/net/interface_windows.go`, `interfaceTable`)
- ❌ (`src/net/interface_plan9.go`, `readInterface`)
- ❌ (`src/net/interface_linux.go`, `linkFlags`)
- ❌ (`src/net/interface_aix.go`, `linkFlags`)
- ❌ (`src/net/interface_bsd.go`, `linkFlags`)

### 📊 Proposal #53573

#### File Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### File Embeddings - File Level
- ✅ `src/crypto/x509/parser.go`
- ❌ `src/crypto/x509/x509.go`
- ❌ `src/crypto/x509/x509_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/crypto/x509`

#### Function Embeddings - File Level
- ❌ `src/crypto/x509/parser.go`
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/crypto/x509/x509_test.go`, `TestCreateRevocationList`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestParseUniqueID`)
- ❌ (`src/crypto/x509/x509_test.go`, `TestParseRevocationList`)
- ❌ (`src/crypto/x509/x509.go`, `CreateRevocationList`)
- ❌ (`src/crypto/x509/parser.go`, `ParseRevocationList`)

### 📊 Proposal #53747

#### File Embeddings - Directory Level
- ✅ `src/flag`

#### File Embeddings - File Level
- ❌ `src/flag/example_func_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`

#### Function Embeddings - Directory Level
- ✅ `src/flag`

#### Function Embeddings - File Level
- ❌ `src/flag/example_func_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`

#### Function Embeddings - Function Level
- ❌ (`src/flag/flag.go`, `UnquoteUsage`)
- ❌ (`src/flag/flag.go`, `TextVar`)
- ❌ (`src/flag/flag.go`, `Func`)
- ✅ (`src/flag/flag.go`, `BoolFunc`)
- ✅ (`src/flag/flag.go`, `BoolFunc`)
- ❌ (`src/flag/flag_test.go`, `TestEverything`)
- ❌ (`src/flag/flag_test.go`, `TestUserDefinedBoolFunc`)
- ❌ (`src/flag/example_func_test.go`, `ExampleBoolFunc`)
- ✅ (`src/flag/flag.go`, `BoolFunc`)
- ✅ (`src/flag/flag.go`, `BoolFunc`)
- ❌ (`src/flag/flag_test.go`, `TestEverything`)
- ❌ (`src/flag/flag_test.go`, `TestUserDefinedBoolFunc`)
- ❌ (`src/flag/example_func_test.go`, `ExampleBoolFunc`)

### 📊 Proposal #5901

#### File Embeddings - Directory Level
- ❌ `src/encoding/json`

#### File Embeddings - File Level
- ❌ `src/encoding/json/bench_test.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/stream.go`

#### Function Embeddings - Directory Level
- ✅ `src/encoding/json`

#### Function Embeddings - File Level
- ❌ `src/encoding/json/bench_test.go`
- ❌ `src/encoding/json/decode.go`
- ✅ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/stream.go`

#### Function Embeddings - Function Level
- ❌ (`src/encoding/json/bench_test.go`, `BenchmarkTypeFieldsCache`)
- ❌ (`src/encoding/json/encode.go`, `newEncodeState`)
- ❌ (`src/encoding/json/encode.go`, `isEmptyValue`)
- ❌ (`src/encoding/json/encode.go`, `reflectValue`)
- ❌ (`src/encoding/json/encode.go`, `valueEncoder`)
- ❌ (`src/encoding/json/encode.go`, `typeEncoder`)
- ❌ (`src/encoding/json/encode.go`, `newTypeEncoder`)
- ❌ (`src/encoding/json/encode.go`, `isValidNumber`)
- ❌ (`src/encoding/json/encode.go`, `encode`)
- ❌ (`src/encoding/json/encode.go`, `newStructEncoder`)
- ❌ (`src/encoding/json/encode.go`, `encode`)
- ❌ (`src/encoding/json/encode.go`, `newMapEncoder`)
- ❌ (`src/encoding/json/encode.go`, `encodeByteSlice`)
- ❌ (`src/encoding/json/encode.go`, `encode`)
- ❌ (`src/encoding/json/encode.go`, `newSliceEncoder`)
- ❌ (`src/encoding/json/encode.go`, `newArrayEncoder`)
- ❌ (`src/encoding/json/encode.go`, `newPtrEncoder`)
- ❌ (`src/encoding/json/encode.go`, `typeFields`)
- ❌ (`src/encoding/json/encode.go`, `cachedTypeFields`)
- ❌ (`src/encoding/json/stream.go`, `Encode`)
- ❌ (`src/encoding/json/decode.go`, `indirect`)
- ❌ (`src/encoding/json/decode.go`, `array`)
- ❌ (`src/encoding/json/decode.go`, `object`)
- ❌ (`src/encoding/json/decode.go`, `literalStore`)
