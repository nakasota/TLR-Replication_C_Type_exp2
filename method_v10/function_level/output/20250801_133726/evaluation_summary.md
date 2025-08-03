# LLM Directory, File & Function-Level Evaluation Summary

## Directory-Level Macro Metrics

- **Number of Processed Proposals**: 231
- **Number of Proposals with at least one correct link (precision > 0)**: 188
- **Macro Precision**: 0.464
- **Macro Recall**: 0.622
- **Macro F1**: 0.473

## File-Level Macro Metrics

- **Number of Processed Proposals**: 231
- **Number of Proposals with at least one correct link (precision > 0)**: 165
- **Macro Precision**: 0.278
- **Macro Recall**: 0.400
- **Macro F1**: 0.284

## Function-Level Macro Metrics

- **Number of Processed Proposals**: 231
- **Number of Proposals with at least one correct link (precision > 0)**: 159
- **Macro Precision**: 0.214
- **Macro Recall**: 0.279
- **Macro F1**: 0.195


### 📊 **Proposal #53200 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/go/token/position.go`
    - Ground Truth Functions (1):
        - `RemoveFile`
    - Predicted Functions (5):
        - ❌ `AddFile`
        - ❌ `File`
        - ❌ `Position`
        - ❌ `PositionFor`
        - ✅ `RemoveFile`

- **File:** `src/go/token/position_test.go`
    - Ground Truth Functions (1):
        - `TestRemoveFile`
    - Predicted Functions (2):
        - ❌ `TestFileSet_AddExistingFiles`
        - ✅ `TestRemoveFile`

- **File:** `src/go/token/token.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `RemoveFile`

- **File:** `src/go/token/token_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #32716 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.1% | 20.6% | 15.2% | 7/34 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/auth_test.go`
    - Ground Truth Functions (1):
        - `TestSignatureSelection`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/cipher_suites.go`
    - Ground Truth Functions (4):
        - `Size`
        - `macSHA1`
        - `macSHA256`
        - `newConstantTimeHash`
    - Predicted Functions (8):
        - ❌ `CipherSuites`
        - ❌ `InsecureCipherSuites`
        - ❌ `cipher3DES`
        - ❌ `cipherAES`
        - ❌ `cipherRC4`
        - ❌ `cipherSuiteByID`
        - ❌ `mutualCipherSuite`
        - ❌ `selectCipherSuite`

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (3):
        - `maxSupportedVersion`
        - `mutualVersion`
        - `supportedVersions`
    - Predicted Functions (3):
        - ✅ `maxSupportedVersion`
        - ✅ `supportedVersions`
        - ❌ `supportedVersionsFromMax`

- **File:** `src/crypto/tls/conn.go`
    - Ground Truth Functions (4):
        - `Write`
        - `decrypt`
        - `handleRenegotiation`
        - `roundUp`
    - Predicted Functions (8):
        - ❌ `Handshake`
        - ❌ `HandshakeContext`
        - ❌ `connectionStateLocked`
        - ❌ `readHandshake`
        - ❌ `readRecord`
        - ❌ `sendAlert`
        - ❌ `writeHandshakeRecord`
        - ❌ `writeRecordLocked`

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (2):
        - `makeClientHello`
        - `pickTLSVersion`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server.go`
    - Ground Truth Functions (3):
        - `pickCipherSuite`
        - `processClientHello`
        - `readClientHello`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server_test.go`
    - Ground Truth Functions (5):
        - `TestHandshakeServerAESGCM`
        - `TestHandshakeServerRSAAES`
        - `TestNoSuiteOverlap`
        - `TestRejectBadProtocolVersion`
        - `runServerTestTLS13`
    - Predicted Functions (30):
        - ❌ `TestFallbackSCSV`
        - ❌ `TestHandshakeServerAES128SHA256`
        - ❌ `TestHandshakeServerAES256GCMSHA384`
        - ❌ `TestHandshakeServerAES256SHA384`
        - ✅ `TestHandshakeServerAESGCM`
        - ❌ `TestHandshakeServerALPN`
        - ❌ `TestHandshakeServerALPNFallback`
        - ❌ `TestHandshakeServerALPNNoMatch`
        - ❌ `TestHandshakeServerALPNNotConfigured`
        - ❌ `TestHandshakeServerCHACHA20SHA256`
        - ❌ `TestHandshakeServerECDHEECDSAAES`
        - ❌ `TestHandshakeServerEd25519`
        - ❌ `TestHandshakeServerEmptyCertificates`
        - ❌ `TestHandshakeServerExportKeyingMaterial`
        - ❌ `TestHandshakeServerGetCertificateExtensions`
        - ❌ `TestHandshakeServerHelloRetryRequest`
        - ❌ `TestHandshakeServerKeySharePreference`
        - ❌ `TestHandshakeServerP256`
        - ❌ `TestHandshakeServerRSA3DES`
        - ✅ `TestHandshakeServerRSAAES`
        - ❌ `TestHandshakeServerRSAPKCS1v15`
        - ❌ `TestHandshakeServerRSAPSS`
        - ❌ `TestHandshakeServerRSARC4`
        - ❌ `TestHandshakeServerSNI`
        - ❌ `TestHandshakeServerSNIGetCertificate`
        - ❌ `TestHandshakeServerSNIGetCertificateError`
        - ❌ `TestHandshakeServerSNIGetCertificateNotFound`
        - ❌ `TestHandshakeServerX25519`
        - ❌ `TestServerResumption`
        - ❌ `TestServerResumptionDisabled`

- **File:** `src/crypto/tls/handshake_server_tls13.go`
    - Ground Truth Functions (1):
        - `processClientHello`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_test.go`
    - Ground Truth Functions (2):
        - `checkOpenSSLVersion`
        - `runMain`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/key_agreement.go`
    - Ground Truth Functions (1):
        - `processClientKeyExchange`
    - Predicted Functions (4):
        - ❌ `generateClientKeyExchange`
        - ❌ `generateServerKeyExchange`
        - ✅ `processClientKeyExchange`
        - ❌ `processServerKeyExchange`

- **File:** `src/crypto/tls/prf.go`
    - Ground Truth Functions (8):
        - `Write`
        - `discardHandshakeBuffer`
        - `ekmFromMasterSecret`
        - `hashForClientCertificate`
        - `keysFromMasterSecret`
        - `newFinishedHash`
        - `prfAndHashForVersion`
        - `prfForVersion`
    - Predicted Functions (2):
        - ✅ `prfAndHashForVersion`
        - ✅ `prfForVersion`

- **File:** `src/crypto/tls/prf_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestKeysFromPreMasterSecret`

- **File:** `src/crypto/tls/tls_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestCipherSuites`
        - ❌ `TestVersionName`


### 📊 **Proposal #40724 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.3% | 0.8% | 1.5% | 4/481 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/asm/internal/asm/asm.go`
    - Ground Truth Functions (1):
        - `asmText`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/asm/endtoend_test.go`
    - Ground Truth Functions (2):
        - `testEndToEnd`
        - `testErrors`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/asm/expr_test.go`
    - Ground Truth Functions (2):
        - `TestExpr`
        - `runBadTest`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/asm/line_test.go`
    - Ground Truth Functions (1):
        - `testBadInstParser`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/asm/operand_test.go`
    - Ground Truth Functions (4):
        - `TestAMD64OperandParser`
        - `TestFuncAddress`
        - `newParser`
        - `testOperandParser`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/asm/parse.go`
    - Ground Truth Functions (5):
        - `NewParser`
        - `funcAddress`
        - `symDefRef`
        - `symRefAttrs`
        - `symbolReference`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/asm/pseudo_test.go`
    - Ground Truth Functions (1):
        - `TestErroneous`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/out.go`
    - Ground Truth Functions (3):
        - `writeDefs`
        - `writeExports`
        - `writeGccgoExports`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/abi/abiutils.go`
    - Ground Truth Functions (2):
        - `FrameOffset`
        - `updateOffset`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/amd64/ssa.go`
    - Ground Truth Functions (3):
        - `getgFromTLS`
        - `ssaGenBlock`
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/arm/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/arm64/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/base/flag.go`
    - Ground Truth Functions (1):
        - `ParseFlags`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/gc/compile.go`
    - Ground Truth Functions (1):
        - `enqueueFunc`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/gc/main.go`
    - Ground Truth Functions (1):
        - `Main`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/gc/obj.go`
    - Ground Truth Functions (1):
        - `addGCLocals`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/expr.go`
    - Ground Truth Functions (1):
        - `FuncName`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/fmt.go`
    - Ground Truth Functions (1):
        - `dumpNode`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/func.go`
    - Ground Truth Functions (1):
        - `NewFunc`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/liveness/plive.go`
    - Ground Truth Functions (9):
        - `WriteFuncMap`
        - `clobber`
        - `clobberPtr`
        - `clobberVar`
        - `clobberWalk`
        - `compact`
        - `enableClobber`
        - `epilogue`
        - `newliveness`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/mips/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/mips64/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/lex.go`
    - Ground Truth Functions (1):
        - `pragmaFlag`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ppc64/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/reflectdata/alg.go`
    - Ground Truth Functions (2):
        - `hashfor`
        - `hashmem`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/reflectdata/reflect.go`
    - Ground Truth Functions (1):
        - `methodWrapper`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/riscv64/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/s390x/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/config.go`
    - Ground Truth Functions (1):
        - `NewConfig`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/decompose.go`
    - Ground Truth Functions (4):
        - `decomposeBuiltIn`
        - `decomposeUserArrayInto`
        - `decomposeUserStructInto`
        - `deleteNamedVals`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/expand_calls.go`
    - Ground Truth Functions (2):
        - `expandCalls`
        - `isBlockMultiValueExit`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/export_test.go`
    - Ground Truth Functions (1):
        - `SplitSlot`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/func.go`
    - Ground Truth Functions (1):
        - `spSb`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/location.go`
    - Ground Truth Functions (1):
        - `String`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/op.go`
    - Ground Truth Functions (4):
        - `ClosureAuxCall`
        - `InterfaceAuxCall`
        - `OwnAuxCall`
        - `StaticAuxCall`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/regalloc.go`
    - Ground Truth Functions (3):
        - `clobberRegs`
        - `init`
        - `regalloc`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/rewriteAMD64.go`
    - Ground Truth Functions (4):
        - `rewriteValueAMD64`
        - `rewriteValueAMD64_OpAMD64MOVQstoreconst`
        - `rewriteValueAMD64_OpGetG`
        - `rewriteValueAMD64_OpZero`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/rewritedec64.go`
    - Ground Truth Functions (27):
        - `rewriteValuedec64`
        - `rewriteValuedec64_OpArg`
        - `rewriteValuedec64_OpLsh16x64`
        - `rewriteValuedec64_OpLsh32x64`
        - `rewriteValuedec64_OpLsh64x16`
        - `rewriteValuedec64_OpLsh64x32`
        - `rewriteValuedec64_OpLsh64x64`
        - `rewriteValuedec64_OpLsh64x8`
        - `rewriteValuedec64_OpLsh8x64`
        - `rewriteValuedec64_OpOr32`
        - `rewriteValuedec64_OpRsh16Ux64`
        - `rewriteValuedec64_OpRsh16x64`
        - `rewriteValuedec64_OpRsh32Ux64`
        - `rewriteValuedec64_OpRsh32x64`
        - `rewriteValuedec64_OpRsh64Ux16`
        - `rewriteValuedec64_OpRsh64Ux32`
        - `rewriteValuedec64_OpRsh64Ux64`
        - `rewriteValuedec64_OpRsh64Ux8`
        - `rewriteValuedec64_OpRsh64x16`
        - `rewriteValuedec64_OpRsh64x32`
        - `rewriteValuedec64_OpRsh64x64`
        - `rewriteValuedec64_OpRsh64x8`
        - `rewriteValuedec64_OpRsh8Ux64`
        - `rewriteValuedec64_OpRsh8x64`
        - `rewriteValuedec64_OpTrunc64to16`
        - `rewriteValuedec64_OpTrunc64to32`
        - `rewriteValuedec64_OpTrunc64to8`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/stackalloc.go`
    - Ground Truth Functions (1):
        - `stackalloc`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssagen/abi.go`
    - Ground Truth Functions (6):
        - `GenABIWrappers`
        - `NewSymABIs`
        - `ReadSymABIs`
        - `canonicalize`
        - `forEachWrapperABI`
        - `makeABIWrapper`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssagen/nowb.go`
    - Ground Truth Functions (1):
        - `newNowritebarrierrecChecker`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssagen/ssa.go`
    - Ground Truth Functions (11):
        - `buildssa`
        - `call`
        - `callTargetLSym`
        - `canSSA`
        - `deferstruct`
        - `emitArgInfo`
        - `emitOpenDeferInfo`
        - `exit`
        - `genssa`
        - `openDeferRecord`
        - `stmt`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/test/clobberdead_test.go`
    - Ground Truth Functions (3):
        - `TestClobberDead`
        - `TestClobberDeadReg`
        - `runHello`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/closure.go`
    - Ground Truth Functions (1):
        - `directClosureCall`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/expr.go`
    - Ground Truth Functions (2):
        - `walkCall`
        - `walkExpr1`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/order.go`
    - Ground Truth Functions (2):
        - `call`
        - `stmt`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/wasm/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/x86/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (1):
        - `runInstall`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (1):
        - `asmArgs`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/link.go`
    - Ground Truth Functions (7):
        - `ABISetOf`
        - `Get`
        - `ParseABI`
        - `Set`
        - `SpillRegisterArgs`
        - `String`
        - `UnspillRegisterArgs`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/plist.go`
    - Ground Truth Functions (2):
        - `Flushplist`
        - `InitTextSym`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/util.go`
    - Ground Truth Functions (7):
        - `Dconv`
        - `DconvWithABIDetail`
        - `WriteDconv`
        - `WriteNameTo`
        - `abiDecorate`
        - `writeDconv`
        - `writeNameTo`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/wasm/wasmobj.go`
    - Ground Truth Functions (2):
        - `instinit`
        - `preprocess`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/x86/obj6.go`
    - Ground Truth Functions (2):
        - `preprocess`
        - `stacksplit`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/funcid.go`
    - Ground Truth Functions (1):
        - `GetFuncID`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/deadcode_test.go`
    - Ground Truth Functions (1):
        - `TestDeadcode`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/go.go`
    - Ground Truth Functions (2):
        - `addexport`
        - `setCgoAttr`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/lib.go`
    - Ground Truth Functions (1):
        - `ldshlibsyms`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/macho.go`
    - Ground Truth Functions (2):
        - `domacho`
        - `machosymtab`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/main.go`
    - Ground Truth Functions (1):
        - `Main`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/pe.go`
    - Ground Truth Functions (1):
        - `writeSymbols`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/symtab.go`
    - Ground Truth Functions (2):
        - `mangleABIName`
        - `putelfsym`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/loadelf/ldelf.go`
    - Ground Truth Functions (1):
        - `Load`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/loader/loader.go`
    - Ground Truth Functions (2):
        - `AddCgoExport`
        - `LookupOrCreateCgoExport`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/loadmacho/ldmacho.go`
    - Ground Truth Functions (1):
        - `Load`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/loadpe/ldpe.go`
    - Ground Truth Functions (1):
        - `Load`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/loadxcoff/ldxcoff.go`
    - Ground Truth Functions (1):
        - `Load`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl/asmdecl.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/internal/abi/abi.go`
    - Ground Truth Functions (2):
        - `Get`
        - `Set`
    - Predicted Functions (4):
        - ❌ `Dump`
        - ✅ `Get`
        - ❌ `IntRegArgAddr`
        - ✅ `Set`

- **File:** `src/internal/abi/abi_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `ABI0`
        - ❌ `ABIInternal`
        - ❌ `ABIWrapper`
        - ❌ `RegEntry`
        - ❌ `RegEntryAlign`
        - ❌ `RegEntryName`
        - ❌ `RegEntryOffset`
        - ❌ `RegEntrySize`
        - ❌ `RegEntryTmp`
        - ❌ `RegEntryType`

- **File:** `src/internal/abi/abi_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `ABI0`
        - ❌ `ABIInternal`
        - ❌ `ABIWrapper`
        - ❌ `RegEntryTmp`

- **File:** `src/internal/abi/abi_generic.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/abi/abi_loong64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/abi/abi_ppc64x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/abi/abi_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/abi/abi_test.go`
    - Ground Truth Functions (2):
        - `TestFuncPC`
        - `TestFuncPCCompileError`
    - Predicted Functions (2):
        - ✅ `TestFuncPC`
        - ✅ `TestFuncPCCompileError`

- **File:** `src/internal/abi/export_test.go`
    - Ground Truth Functions (2):
        - `FuncPCTest`
        - `FuncPCTestFn`
    - Predicted Functions (0):

- **File:** `src/internal/abi/testdata/x.go`
    - Ground Truth Functions (2):
        - `Fn0`
        - `test`
    - Predicted Functions (0):

- **File:** `src/math/acosh.go`
    - Ground Truth Functions (1):
        - `Acosh`
    - Predicted Functions (0):

- **File:** `src/math/arith_s390x.go`
    - Ground Truth Functions (63):
        - `acosAsm`
        - `acosTrampolineSetup`
        - `acoshAsm`
        - `acoshTrampolineSetup`
        - `archAcos`
        - `archAcosh`
        - `archAsin`
        - `archAsinh`
        - `archAtan`
        - `archAtan2`
        - `archAtanh`
        - `archCbrt`
        - `archCos`
        - `archCosh`
        - `archErf`
        - `archErfc`
        - `archExpm1`
        - `archFrexp`
        - `archLdexp`
        - `archLog10`
        - `archLog1p`
        - `archLog2`
        - `archMod`
        - `archPow`
        - `archRemainder`
        - `archSin`
        - `archSinh`
        - `archTan`
        - `archTanh`
        - `asinAsm`
        - `asinTrampolineSetup`
        - `asinhAsm`
        - `asinhTrampolineSetup`
        - `atan2Asm`
        - `atan2TrampolineSetup`
        - `atanAsm`
        - `atanTrampolineSetup`
        - `atanhAsm`
        - `atanhTrampolineSetup`
        - `cbrtAsm`
        - `cbrtTrampolineSetup`
        - `cosAsm`
        - `cosTrampolineSetup`
        - `coshAsm`
        - `coshTrampolineSetup`
        - `erfAsm`
        - `erfTrampolineSetup`
        - `erfcAsm`
        - `erfcTrampolineSetup`
        - `expAsm`
        - `expTrampolineSetup`
        - `log10Asm`
        - `log10TrampolineSetup`
        - `log1pAsm`
        - `log1pTrampolineSetup`
        - `logAsm`
        - `logTrampolineSetup`
        - `sinAsm`
        - `sinTrampolineSetup`
        - `sinhAsm`
        - `sinhTrampolineSetup`
        - `tanhAsm`
        - `tanhTrampolineSetup`
    - Predicted Functions (0):

- **File:** `src/math/asin.go`
    - Ground Truth Functions (2):
        - `Acos`
        - `Asin`
    - Predicted Functions (0):

- **File:** `src/math/asinh.go`
    - Ground Truth Functions (1):
        - `Asinh`
    - Predicted Functions (0):

- **File:** `src/math/atan.go`
    - Ground Truth Functions (1):
        - `Atan`
    - Predicted Functions (0):

- **File:** `src/math/atan2.go`
    - Ground Truth Functions (1):
        - `Atan2`
    - Predicted Functions (0):

- **File:** `src/math/atanh.go`
    - Ground Truth Functions (1):
        - `Atanh`
    - Predicted Functions (0):

- **File:** `src/math/cbrt.go`
    - Ground Truth Functions (1):
        - `Cbrt`
    - Predicted Functions (0):

- **File:** `src/math/dim.go`
    - Ground Truth Functions (2):
        - `Max`
        - `Min`
    - Predicted Functions (0):

- **File:** `src/math/dim_asm.go`
    - Ground Truth Functions (2):
        - `archMax`
        - `archMin`
    - Predicted Functions (0):

- **File:** `src/math/dim_noasm.go`
    - Ground Truth Functions (2):
        - `archMax`
        - `archMin`
    - Predicted Functions (0):

- **File:** `src/math/erf.go`
    - Ground Truth Functions (2):
        - `Erf`
        - `Erfc`
    - Predicted Functions (0):

- **File:** `src/math/exp.go`
    - Ground Truth Functions (2):
        - `Exp`
        - `Exp2`
    - Predicted Functions (0):

- **File:** `src/math/exp2_asm.go`
    - Ground Truth Functions (1):
        - `archExp2`
    - Predicted Functions (0):

- **File:** `src/math/exp2_noasm.go`
    - Ground Truth Functions (1):
        - `archExp2`
    - Predicted Functions (0):

- **File:** `src/math/exp_asm.go`
    - Ground Truth Functions (1):
        - `archExp`
    - Predicted Functions (0):

- **File:** `src/math/exp_noasm.go`
    - Ground Truth Functions (1):
        - `archExp`
    - Predicted Functions (0):

- **File:** `src/math/expm1.go`
    - Ground Truth Functions (1):
        - `Expm1`
    - Predicted Functions (0):

- **File:** `src/math/floor.go`
    - Ground Truth Functions (3):
        - `Ceil`
        - `Floor`
        - `Trunc`
    - Predicted Functions (0):

- **File:** `src/math/floor_asm.go`
    - Ground Truth Functions (3):
        - `archCeil`
        - `archFloor`
        - `archTrunc`
    - Predicted Functions (0):

- **File:** `src/math/floor_noasm.go`
    - Ground Truth Functions (3):
        - `archCeil`
        - `archFloor`
        - `archTrunc`
    - Predicted Functions (0):

- **File:** `src/math/frexp.go`
    - Ground Truth Functions (1):
        - `Frexp`
    - Predicted Functions (0):

- **File:** `src/math/hypot.go`
    - Ground Truth Functions (1):
        - `Hypot`
    - Predicted Functions (0):

- **File:** `src/math/hypot_asm.go`
    - Ground Truth Functions (1):
        - `archHypot`
    - Predicted Functions (0):

- **File:** `src/math/hypot_noasm.go`
    - Ground Truth Functions (1):
        - `archHypot`
    - Predicted Functions (0):

- **File:** `src/math/ldexp.go`
    - Ground Truth Functions (1):
        - `Ldexp`
    - Predicted Functions (0):

- **File:** `src/math/log.go`
    - Ground Truth Functions (1):
        - `Log`
    - Predicted Functions (0):

- **File:** `src/math/log10.go`
    - Ground Truth Functions (3):
        - `Log10`
        - `Log2`
        - `log10`
    - Predicted Functions (0):

- **File:** `src/math/log1p.go`
    - Ground Truth Functions (1):
        - `Log1p`
    - Predicted Functions (0):

- **File:** `src/math/log_asm.go`
    - Ground Truth Functions (1):
        - `archLog`
    - Predicted Functions (0):

- **File:** `src/math/log_stub.go`
    - Ground Truth Functions (1):
        - `archLog`
    - Predicted Functions (0):

- **File:** `src/math/mod.go`
    - Ground Truth Functions (1):
        - `Mod`
    - Predicted Functions (0):

- **File:** `src/math/modf.go`
    - Ground Truth Functions (1):
        - `Modf`
    - Predicted Functions (0):

- **File:** `src/math/modf_asm.go`
    - Ground Truth Functions (1):
        - `archModf`
    - Predicted Functions (0):

- **File:** `src/math/modf_noasm.go`
    - Ground Truth Functions (1):
        - `archModf`
    - Predicted Functions (0):

- **File:** `src/math/pow.go`
    - Ground Truth Functions (1):
        - `Pow`
    - Predicted Functions (0):

- **File:** `src/math/remainder.go`
    - Ground Truth Functions (1):
        - `Remainder`
    - Predicted Functions (0):

- **File:** `src/math/sin.go`
    - Ground Truth Functions (2):
        - `Cos`
        - `Sin`
    - Predicted Functions (0):

- **File:** `src/math/sinh.go`
    - Ground Truth Functions (2):
        - `Cosh`
        - `Sinh`
    - Predicted Functions (0):

- **File:** `src/math/sqrt.go`
    - Ground Truth Functions (1):
        - `Sqrt`
    - Predicted Functions (0):

- **File:** `src/math/stubs.go`
    - Ground Truth Functions (25):
        - `archAcos`
        - `archAcosh`
        - `archAsin`
        - `archAsinh`
        - `archAtan`
        - `archAtan2`
        - `archAtanh`
        - `archCbrt`
        - `archCos`
        - `archCosh`
        - `archErf`
        - `archErfc`
        - `archExpm1`
        - `archFrexp`
        - `archLdexp`
        - `archLog10`
        - `archLog1p`
        - `archLog2`
        - `archMod`
        - `archPow`
        - `archRemainder`
        - `archSin`
        - `archSinh`
        - `archTan`
        - `archTanh`
    - Predicted Functions (0):

- **File:** `src/math/tan.go`
    - Ground Truth Functions (1):
        - `Tan`
    - Predicted Functions (0):

- **File:** `src/math/tanh.go`
    - Ground Truth Functions (1):
        - `Tanh`
    - Predicted Functions (0):

- **File:** `src/reflect/abi.go`
    - Ground Truth Functions (9):
        - `addArg`
        - `addRcvr`
        - `assignFloatN`
        - `assignIntN`
        - `dump`
        - `newAbiDesc`
        - `regAssign`
        - `stackAssign`
        - `stepsForValue`
    - Predicted Functions (0):

- **File:** `src/reflect/abi_test.go`
    - Ground Truth Functions (44):
        - `AllRegsCall`
        - `RegsAndStackCall`
        - `SpillStructCall`
        - `TestMethodValueCallABI`
        - `TestReflectCallABI`
        - `TestReflectMakeFuncCallABI`
        - `callArgs2Struct1`
        - `callArgsArray`
        - `callArgsArray1`
        - `callArgsArray1Mix`
        - `callArgsComplex128`
        - `callArgsComplex64`
        - `callArgsEmptyStruct`
        - `callArgsFloat32`
        - `callArgsFloat64`
        - `callArgsInt`
        - `callArgsInt16`
        - `callArgsInt32`
        - `callArgsInt64`
        - `callArgsInt8`
        - `callArgsManyFloat64`
        - `callArgsManyInt`
        - `callArgsNone`
        - `callArgsPointer`
        - `callArgsSlice`
        - `callArgsString`
        - `callArgsStruct1`
        - `callArgsStruct10`
        - `callArgsStruct11`
        - `callArgsStruct12`
        - `callArgsStruct13`
        - `callArgsStruct2`
        - `callArgsStruct3`
        - `callArgsStruct4`
        - `callArgsStruct5`
        - `callArgsStruct6`
        - `callArgsStruct7`
        - `callArgsStruct8`
        - `callArgsStruct9`
        - `callArgsUint`
        - `callArgsUint16`
        - `callArgsUint32`
        - `callArgsUint64`
        - `callArgsUint8`
    - Predicted Functions (0):

- **File:** `src/reflect/export_test.go`
    - Ground Truth Functions (1):
        - `FuncLayout`
    - Predicted Functions (0):

- **File:** `src/reflect/makefunc.go`
    - Ground Truth Functions (3):
        - `MakeFunc`
        - `makeMethodValue`
        - `moveMakeFuncArgPtrs`
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (3):
        - `addTypeBits`
        - `append`
        - `funcLayout`
    - Predicted Functions (0):

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (7):
        - `call`
        - `callMethod`
        - `callReflect`
        - `cvtIntString`
        - `makeFloat`
        - `methodReceiver`
        - `storeRcvr`
    - Predicted Functions (0):

- **File:** `src/runtime/cgo/callbacks.go`
    - Ground Truth Functions (1):
        - `_cgo_panic`
    - Predicted Functions (0):

- **File:** `src/runtime/cgocall.go`
    - Ground Truth Functions (5):
        - `badcgocallback`
        - `cgocallbackg`
        - `cgocallbackg1`
        - `cgounimpl`
        - `unwindm`
    - Predicted Functions (0):

- **File:** `src/runtime/debug_test.go`
    - Ground Truth Functions (7):
        - `TestDebugCall`
        - `TestDebugCallGC`
        - `TestDebugCallGrowStack`
        - `TestDebugCallLarge`
        - `TestDebugCallPanic`
        - `TestDebugCallUnsafePoint`
        - `debugCallUnsafePointWorker`
    - Predicted Functions (0):

- **File:** `src/runtime/debugcall.go`
    - Ground Truth Functions (3):
        - `debugCallV2`
        - `debugCallWrap`
        - `debugCallWrap1`
    - Predicted Functions (0):

- **File:** `src/runtime/export_debug_test.go`
    - Ground Truth Functions (3):
        - `InjectDebugCall`
        - `handle`
        - `inject`
    - Predicted Functions (0):

- **File:** `src/runtime/export_test.go`
    - Ground Truth Functions (4):
        - `GCTestIsReachable`
        - `GCTestPointerClass`
        - `RunSchedLocalQueueEmptyTest`
        - `SetIntArgRegs`
    - Predicted Functions (0):

- **File:** `src/runtime/gc_test.go`
    - Ground Truth Functions (4):
        - `TestGCTestIsReachable`
        - `TestGCTestMoveStackOnNextCall`
        - `TestGCTestPointerClass`
        - `moveStackCheck`
    - Predicted Functions (0):

- **File:** `src/runtime/mbarrier.go`
    - Ground Truth Functions (1):
        - `reflectcallmove`
    - Predicted Functions (0):

- **File:** `src/runtime/mgc.go`
    - Ground Truth Functions (4):
        - `gcTestIsReachable`
        - `gcTestMoveStackOnNextCall`
        - `gcTestPointerClass`
        - `gcenable`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcmark.go`
    - Ground Truth Functions (1):
        - `scanframeworker`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcscavenge.go`
    - Ground Truth Functions (1):
        - `bgscavenge`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcsweep.go`
    - Ground Truth Functions (2):
        - `bgsweep`
        - `sweep`
    - Predicted Functions (0):

- **File:** `src/runtime/mheap.go`
    - Ground Truth Functions (2):
        - `freeSpecial`
        - `init`
    - Predicted Functions (0):

- **File:** `src/runtime/mkduff.go`
    - Ground Truth Functions (2):
        - `copyAMD64`
        - `zeroAMD64`
    - Predicted Functions (0):

- **File:** `src/runtime/mkpreempt.go`
    - Ground Truth Functions (1):
        - `header`
    - Predicted Functions (0):

- **File:** `src/runtime/os_netbsd.go`
    - Ground Truth Functions (2):
        - `netbsdMstart`
        - `netbsdMstart0`
    - Predicted Functions (0):

- **File:** `src/runtime/panic.go`
    - Ground Truth Functions (4):
        - `Goexit`
        - `deferproc`
        - `deferprocStack`
        - `gopanic`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/defs_darwin.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/defs_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/defs_darwin_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/pprof.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `StartCPUProfile`
        - ❌ `StopCPUProfile`
        - ❌ `WriteHeapProfile`
        - ❌ `writeBlock`
        - ❌ `writeGoroutine`
        - ❌ `writeMutex`
        - ❌ `writeProfileInternal`
        - ❌ `writeThreadCreate`

- **File:** `src/runtime/pprof/pprof_norusage.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/pprof_rusage.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/pprof_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (12):
        - ❌ `TestBlockProfile`
        - ❌ `TestCPUProfile`
        - ❌ `TestCPUProfileInlining`
        - ❌ `TestCPUProfileMultithreaded`
        - ❌ `TestCPUProfileRecursion`
        - ❌ `TestGoroutineProfileConcurrency`
        - ❌ `TestGoroutineProfileCoro`
        - ❌ `TestLabelSystemstack`
        - ❌ `TestMorestack`
        - ❌ `TestMutexProfile`
        - ❌ `growstack`
        - ❌ `growstack1`

- **File:** `src/runtime/pprof/pprof_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/proto.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/proto_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/protobuf.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/protomem.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/protomem_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/proc.go`
    - Ground Truth Functions (4):
        - `newproc`
        - `newproc1`
        - `oneNewExtraM`
        - `sigprof`
    - Predicted Functions (0):

- **File:** `src/runtime/runtime.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/stubs.go`
    - Ground Truth Functions (2):
        - `cgocallback`
        - `reflectcall`
    - Predicted Functions (0):

- **File:** `src/runtime/stubs_amd64.go`
    - Ground Truth Functions (2):
        - `spillArgs`
        - `unspillArgs`
    - Predicted Functions (0):

- **File:** `src/runtime/syscall_windows.go`
    - Ground Truth Functions (6):
        - `assignArg`
        - `assignReg`
        - `callbackWrap`
        - `compileCallback`
        - `tryMerge`
        - `tryRegAssignArg`
    - Predicted Functions (0):

- **File:** `src/runtime/syscall_windows_test.go`
    - Ground Truth Functions (18):
        - `TestStdcallAndCDeclCallbacks`
        - `cSrc`
        - `getCallbackTestFuncs`
        - `makeSrc`
        - `sum10`
        - `sum2`
        - `sum3`
        - `sum4`
        - `sum5`
        - `sum5andPair`
        - `sum5mix`
        - `sum6`
        - `sum7`
        - `sum8`
        - `sum9`
        - `sum9int8`
        - `sum9uint16`
        - `sum9uint8`
    - Predicted Functions (0):

- **File:** `src/runtime/trace.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/traceback.go`
    - Ground Truth Functions (1):
        - `printArgs`
    - Predicted Functions (0):

- **File:** `src/runtime/traceback_test.go`
    - Ground Truth Functions (6):
        - `TestTracebackArgs`
        - `testTracebackArgs1`
        - `testTracebackArgs2`
        - `testTracebackArgs3`
        - `testTracebackArgs4`
        - `testTracebackArgs5`
    - Predicted Functions (0):

- **File:** `test/abi/bad_internal_offsets.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `NoteFailure`
        - ❌ `NoteFailureElem`
        - ❌ `Test0`

- **File:** `test/abi/convF_criteria.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/abi/convT64_criteria.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/abi/defer_aggregate.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `callee`
        - ❌ `main`

- **File:** `test/abi/defer_recover_results.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/abi/double_nested_addressed_struct.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/abi/double_nested_struct.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `G`
        - ❌ `H`
        - ❌ `gotVsWant`
        - ❌ `main`

- **File:** `test/abi/f_ret_z_not.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/abi/fibish.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/abi/fibish_closure.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/abi/reg_not_ssa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `F`
        - ❌ `g`
        - ❌ `h`
        - ❌ `main`

- **File:** `test/abi/result_live.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/abi/result_regalloc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/abi/return_stuff.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/abi/spills3.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `F`
        - ❌ `main`
        - ❌ `spills`

- **File:** `test/abi/spills4.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `F`
        - ❌ `main`
        - ❌ `spills`

- **File:** `test/abi/store_reg_args.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `F`
        - ❌ `main`

- **File:** `test/abi/struct_lower_1.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `main`
        - ❌ `passStruct6`

- **File:** `test/codegen/clobberdead.go`
    - Ground Truth Functions (1):
        - `F`
    - Predicted Functions (0):

- **File:** `test/codegen/clobberdeadreg.go`
    - Ground Truth Functions (1):
        - `F`
    - Predicted Functions (0):

- **File:** `test/codegen/structs.go`
    - Ground Truth Functions (2):
        - `Zero1`
        - `Zero2`
    - Predicted Functions (0):

- **File:** `test/nosplit.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #40337 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/dsa/dsa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `GenerateKey`
        - ❌ `GenerateParameters`
        - ❌ `Sign`
        - ❌ `Verify`

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (2):
        - `CheckCRLSignature`
        - `checkSignature`
    - Predicted Functions (5):
        - ❌ `CheckSignature`
        - ❌ `CheckSignatureFrom`
        - ❌ `CreateCertificate`
        - ❌ `CreateCertificateRequest`
        - ❌ `ParsePKIXPublicKey`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (1):
        - `TestVerifyCertificateWithDSASignature`
    - Predicted Functions (0):


### 📊 **Proposal #44940 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/unicode/utf16/utf16.go`
    - Ground Truth Functions (2):
        - `Encode`
        - `RuneLen`
    - Predicted Functions (1):
        - ✅ `RuneLen`

- **File:** `src/unicode/utf16/utf16_test.go`
    - Ground Truth Functions (1):
        - `TestRuneLen`
    - Predicted Functions (1):
        - ✅ `TestRuneLen`


### 📊 **Proposal #52221 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.7% | 36.2% | 45.3% | 17/47 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/ecdh/ecdh.go`
    - Ground Truth Functions (5):
        - `Bytes`
        - `Curve`
        - `Equal`
        - `Public`
        - `PublicKey`
    - Predicted Functions (6):
        - ✅ `Bytes`
        - ✅ `Curve`
        - ❌ `ECDH`
        - ✅ `Equal`
        - ✅ `Public`
        - ✅ `PublicKey`

- **File:** `src/crypto/ecdh/ecdh_test.go`
    - Ground Truth Functions (10):
        - `BenchmarkECDH`
        - `Read`
        - `TestECDH`
        - `TestGenerateKey`
        - `TestLinker`
        - `TestString`
        - `TestVectors`
        - `benchmarkAllCurves`
        - `hexDecode`
        - `testAllCurves`
    - Predicted Functions (10):
        - ✅ `BenchmarkECDH`
        - ✅ `TestECDH`
        - ✅ `TestGenerateKey`
        - ❌ `TestNewPrivateKey`
        - ❌ `TestNewPublicKey`
        - ✅ `TestVectors`
        - ❌ `TestX25519Failure`
        - ✅ `benchmarkAllCurves`
        - ✅ `testAllCurves`
        - ❌ `testX25519Failure`

- **File:** `src/crypto/ecdh/nist.go`
    - Ground Truth Functions (4):
        - `GenerateKey`
        - `NewPrivateKey`
        - `NewPublicKey`
        - `String`
    - Predicted Functions (7):
        - ✅ `GenerateKey`
        - ✅ `NewPrivateKey`
        - ✅ `NewPublicKey`
        - ❌ `P256`
        - ❌ `P384`
        - ❌ `P521`
        - ❌ `ecdh`

- **File:** `src/crypto/ecdh/x25519.go`
    - Ground Truth Functions (5):
        - `GenerateKey`
        - `NewPrivateKey`
        - `NewPublicKey`
        - `String`
        - `x25519ScalarMult`
    - Predicted Functions (5):
        - ✅ `GenerateKey`
        - ✅ `NewPrivateKey`
        - ✅ `NewPublicKey`
        - ❌ `X25519`
        - ❌ `ecdh`

- **File:** `src/crypto/ecdsa/ecdsa.go`
    - Ground Truth Functions (2):
        - `ECDH`
        - `curveToECDH`
    - Predicted Functions (0):

- **File:** `src/crypto/elliptic/elliptic.go`
    - Ground Truth Functions (3):
        - `GenerateKey`
        - `Marshal`
        - `Unmarshal`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (2):
        - `clientHandshake`
        - `makeClientHello`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_client_tls13.go`
    - Ground Truth Functions (4):
        - `establishHandshakeKeys`
        - `handshake`
        - `processHelloRetryRequest`
        - `processServerHello`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server_test.go`
    - Ground Truth Functions (1):
        - `TestAESCipherReorderingTLS13`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server_tls13.go`
    - Ground Truth Functions (1):
        - `processClientHello`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/key_agreement.go`
    - Ground Truth Functions (3):
        - `generateServerKeyExchange`
        - `processClientKeyExchange`
        - `processServerKeyExchange`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/key_schedule.go`
    - Ground Truth Functions (2):
        - `curveForCurveID`
        - `generateECDHEKey`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/pkcs8.go`
    - Ground Truth Functions (1):
        - `MarshalPKCS8PrivateKey`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/pkcs8_test.go`
    - Ground Truth Functions (1):
        - `TestPKCS8`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/sec1.go`
    - Ground Truth Functions (1):
        - `marshalECDHPrivateKey`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (2):
        - `marshalPublicKey`
        - `oidFromECDHCurve`
    - Predicted Functions (0):


### 📊 **Proposal #45033 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 35.7% | 55.6% | 43.5% | 5/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/bufio/scan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/fmt/scan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `quotedString`

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `QuotedPrefix`
        - ❌ `QuotedPrefixLen`

- **File:** `src/strconv/atoi.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strconv/atoi_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strconv/bytealg.go`
    - Ground Truth Functions (1):
        - `index`
    - Predicted Functions (0):

- **File:** `src/strconv/bytealg_bootstrap.go`
    - Ground Truth Functions (1):
        - `index`
    - Predicted Functions (0):

- **File:** `src/strconv/quote.go`
    - Ground Truth Functions (4):
        - `QuotedPrefix`
        - `Unquote`
        - `contains`
        - `unquote`
    - Predicted Functions (2):
        - ✅ `QuotedPrefix`
        - ✅ `Unquote`

- **File:** `src/strconv/quote_test.go`
    - Ground Truth Functions (3):
        - `TestUnquote`
        - `TestUnquoteInvalidUTF8`
        - `testUnquote`
    - Predicted Functions (4):
        - ✅ `TestUnquote`
        - ✅ `TestUnquoteInvalidUTF8`
        - ❌ `Unquote`
        - ✅ `testUnquote`

- **File:** `src/strconv/strconv_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `QuotedPrefix`
        - ❌ `Unquote`

- **File:** `src/text/template/parse/lex.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `lexQuote`
        - ❌ `lexRawQuote`

- **File:** `src/text/template/parse/lex_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestLex`


### 📊 **Proposal #50102 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 15.4% | 26.7% | 2/13 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/common.go`
    - Ground Truth Functions (2):
        - `FileInfoHeader`
        - `isHeaderOnlyType`
    - Predicted Functions (1):
        - ✅ `FileInfoHeader`

- **File:** `src/archive/tar/stat_unix.go`
    - Ground Truth Functions (2):
        - `init`
        - `statUnix`
    - Predicted Functions (1):
        - ✅ `statUnix`

- **File:** `src/archive/tar/tar_test.go`
    - Ground Truth Functions (9):
        - `Gname`
        - `IsDir`
        - `ModTime`
        - `Mode`
        - `Name`
        - `Size`
        - `Sys`
        - `TestFileInfoHeaderUseFileInfoNames`
        - `Uname`
    - Predicted Functions (0):


### 📊 **Proposal #26535 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 90.9% | 41.7% | 57.1% | 10/24 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/compress/lzw/reader.go`
    - Ground Truth Functions (9):
        - `Close`
        - `NewReader`
        - `Read`
        - `Reset`
        - `decode`
        - `init`
        - `newReader`
        - `readLSB`
        - `readMSB`
    - Predicted Functions (4):
        - ✅ `Close`
        - ✅ `NewReader`
        - ✅ `Read`
        - ✅ `Reset`

- **File:** `src/compress/lzw/reader_test.go`
    - Ground Truth Functions (4):
        - `BenchmarkDecoder`
        - `TestHiCodeDoesNotOverflow`
        - `TestNoLongerSavingPriorExpansions`
        - `TestReaderReset`
    - Predicted Functions (1):
        - ✅ `TestReaderReset`

- **File:** `src/compress/lzw/writer.go`
    - Ground Truth Functions (9):
        - `Close`
        - `NewWriter`
        - `Reset`
        - `Write`
        - `incHi`
        - `init`
        - `newWriter`
        - `writeLSB`
        - `writeMSB`
    - Predicted Functions (4):
        - ✅ `Close`
        - ✅ `NewWriter`
        - ✅ `Reset`
        - ✅ `Write`

- **File:** `src/compress/lzw/writer_test.go`
    - Ground Truth Functions (2):
        - `BenchmarkEncoder`
        - `TestWriterReset`
    - Predicted Functions (2):
        - ✅ `TestWriterReset`
        - ❌ `TestWriterReturnValues`


### 📊 **Proposal #19367 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/checkptr.go`
    - Ground Truth Functions (2):
        - `checkptrAlignment`
        - `checkptrArithmetic`
    - Predicted Functions (0):

- **File:** `src/runtime/select.go`
    - Ground Truth Functions (1):
        - `selectgo`
    - Predicted Functions (0):

- **File:** `src/unsafe/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Slice`
        - ❌ `String`


### 📊 **Proposal #50465 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 50.0% | 57.1% | 4/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/httputil/reverseproxy.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (2):
        - ✅ `ServeHTTP`
        - ❌ `SetXForwarded`

- **File:** `src/net/http/httputil/reverseproxy_test.go`
    - Ground Truth Functions (7):
        - `TestClonesRequestHeaders`
        - `TestModifyResponseClosesBody`
        - `TestReverseProxy`
        - `TestReverseProxyRewriteStripsForwarded`
        - `TestServeHTTPDeepCopy`
        - `TestXForwardedFor`
        - `TestXForwardedFor_Omit`
    - Predicted Functions (4):
        - ❌ `TestReverseProxyModifyResponse`
        - ✅ `TestReverseProxyRewriteStripsForwarded`
        - ✅ `TestXForwardedFor`
        - ✅ `TestXForwardedFor_Omit`


### 📊 **Proposal #30715 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 25.0% | 15.4% | 1/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/request.go`
    - Ground Truth Functions (3):
        - `Error`
        - `MaxBytesReader`
        - `Read`
    - Predicted Functions (6):
        - ❌ `MaxBytesError`
        - ✅ `MaxBytesReader`
        - ❌ `Request.ParseForm`
        - ❌ `maxBytesReader.Close`
        - ❌ `maxBytesReader.Read`
        - ❌ `parsePostForm`

- **File:** `src/net/http/request_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestIssue10884_MaxBytesEOF`
        - ❌ `TestMaxBytesReaderDifferentLimits`
        - ❌ `TestMaxBytesReaderStickyError`

- **File:** `src/net/http/serve_test.go`
    - Ground Truth Functions (1):
        - `testRequestBodyLimit`
    - Predicted Functions (0):

- **File:** `test/fixedbugs/issue41440.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #45453 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/61 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/amd64/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/amd64/versions_test.go`
    - Ground Truth Functions (2):
        - `TestGoAMD64v1`
        - `setOf`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/rewriteAMD64.go`
    - Ground Truth Functions (20):
        - `rewriteValueAMD64`
        - `rewriteValueAMD64_OpAMD64ANDL`
        - `rewriteValueAMD64_OpAMD64ANDNL`
        - `rewriteValueAMD64_OpAMD64ANDNQ`
        - `rewriteValueAMD64_OpAMD64ANDQ`
        - `rewriteValueAMD64_OpAMD64BSWAPL`
        - `rewriteValueAMD64_OpAMD64BSWAPQ`
        - `rewriteValueAMD64_OpAMD64MOVBELstore`
        - `rewriteValueAMD64_OpAMD64MOVBEQstore`
        - `rewriteValueAMD64_OpAMD64MOVLstore`
        - `rewriteValueAMD64_OpAMD64MOVQstore`
        - `rewriteValueAMD64_OpAMD64ORQ`
        - `rewriteValueAMD64_OpAMD64XORL`
        - `rewriteValueAMD64_OpAMD64XORQ`
        - `rewriteValueAMD64_OpCtz16NonZero`
        - `rewriteValueAMD64_OpCtz32`
        - `rewriteValueAMD64_OpCtz32NonZero`
        - `rewriteValueAMD64_OpCtz64`
        - `rewriteValueAMD64_OpCtz64NonZero`
        - `rewriteValueAMD64_OpCtz8NonZero`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (2):
        - `cmdenv`
        - `xinit`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/buildruntime.go`
    - Ground Truth Functions (1):
        - `mkbuildcfg`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cfg/cfg.go`
    - Ground Truth Functions (1):
        - `GetArchEnv`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (1):
        - `asmArgs`
    - Predicted Functions (0):

- **File:** `src/internal/buildcfg/cfg.go`
    - Ground Truth Functions (1):
        - `goamd64`
    - Predicted Functions (0):

- **File:** `src/internal/buildcfg/cfg_test.go`
    - Ground Truth Functions (1):
        - `TestConfigFlags`
    - Predicted Functions (0):

- **File:** `test/codegen/bmi.go`
    - Ground Truth Functions (8):
        - `andn32`
        - `andn64`
        - `blsi32`
        - `blsi64`
        - `blsmsk32`
        - `blsmsk64`
        - `blsr32`
        - `blsr64`
    - Predicted Functions (0):

- **File:** `test/codegen/mathbits.go`
    - Ground Truth Functions (8):
        - `IterateBits`
        - `IterateBits16`
        - `IterateBits32`
        - `IterateBits64`
        - `IterateBits8`
        - `TrailingZeros`
        - `TrailingZeros32`
        - `TrailingZeros64`
    - Predicted Functions (0):

- **File:** `test/codegen/memcombine.go`
    - Ground Truth Functions (15):
        - `load_be32`
        - `load_be32_idx`
        - `load_be64`
        - `load_be64_idx`
        - `load_be_byte4_uint32_inv`
        - `load_be_byte8_uint64`
        - `load_be_byte8_uint64_inv`
        - `store_be32`
        - `store_be32_idx`
        - `store_be64`
        - `store_be64_idx`
        - `store_be_byte_2`
        - `store_be_byte_4`
        - `store_be_byte_8`
        - `store_le16_idx`
    - Predicted Functions (0):


### 📊 **Proposal #45963 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/test/testflag.go`
    - Ground Truth Functions (2):
        - `Set`
        - `String`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (1):
        - `buildVetConfig`
    - Predicted Functions (0):


### 📊 **Proposal #53015 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 18.2% | 17.4% | 2/11 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/html/template/escape.go`
    - Ground Truth Functions (2):
        - `escape`
        - `joinRange`
    - Predicted Functions (0):

- **File:** `src/html/template/escape_test.go`
    - Ground Truth Functions (1):
        - `TestErrors`
    - Predicted Functions (0):

- **File:** `src/html/template/template.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Execute`
        - ❌ `ExecuteTemplate`
        - ❌ `Funcs`

- **File:** `src/html/template/template_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `mustExecute`

- **File:** `src/text/template/exec.go`
    - Ground Truth Functions (3):
        - `execute`
        - `walk`
        - `walkTemplate`
    - Predicted Functions (5):
        - ❌ `Execute`
        - ❌ `ExecuteTemplate`
        - ✅ `execute`
        - ❌ `walkIfOrWith`
        - ✅ `walkTemplate`

- **File:** `src/text/template/parse/lex.go`
    - Ground Truth Functions (1):
        - `lexIdentifier`
    - Predicted Functions (0):

- **File:** `src/text/template/parse/lex_test.go`
    - Ground Truth Functions (1):
        - `collect`
    - Predicted Functions (0):

- **File:** `src/text/template/parse/node.go`
    - Ground Truth Functions (1):
        - `Copy`
    - Predicted Functions (0):

- **File:** `src/text/template/parse/parse.go`
    - Ground Truth Functions (2):
        - `action`
        - `startParse`
    - Predicted Functions (0):

- **File:** `src/text/template/template.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Execute`
        - ❌ `Funcs`
        - ❌ `Parse`


### 📊 **Proposal #35833 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 20.0% | 25.0% | 2/10 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/elliptic/elliptic.go`
    - Ground Truth Functions (3):
        - `GenerateKey`
        - `Marshal`
        - `Unmarshal`
    - Predicted Functions (0):

- **File:** `src/crypto/rand/util.go`
    - Ground Truth Functions (1):
        - `Int`
    - Predicted Functions (0):

- **File:** `src/crypto/rsa/pkcs1v15.go`
    - Ground Truth Functions (2):
        - `EncryptPKCS1v15`
        - `decryptPKCS1v15`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/sec1.go`
    - Ground Truth Functions (1):
        - `marshalECPrivateKeyWithOID`
    - Predicted Functions (0):

- **File:** `src/math/big/int.go`
    - Ground Truth Functions (1):
        - `FillBytes`
    - Predicted Functions (3):
        - ❌ `Bytes`
        - ✅ `FillBytes`
        - ❌ `SetBytes`

- **File:** `src/math/big/int_test.go`
    - Ground Truth Functions (1):
        - `TestFillBytes`
    - Predicted Functions (3):
        - ❌ `Bytes`
        - ❌ `FillBytes`
        - ✅ `TestFillBytes`

- **File:** `src/math/big/nat.go`
    - Ground Truth Functions (1):
        - `bytes`
    - Predicted Functions (0):


### 📊 **Proposal #40255 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/39 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/asm/internal/asm/endtoend_test.go`
    - Ground Truth Functions (2):
        - `Test386EndToEnd`
        - `TestARMEndToEnd`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/regalloc.go`
    - Ground Truth Functions (2):
        - `init`
        - `regalloc`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/rewrite386.go`
    - Ground Truth Functions (15):
        - `rewriteValue386_Op386ADDSD`
        - `rewriteValue386_Op386ADDSS`
        - `rewriteValue386_Op386DIVSD`
        - `rewriteValue386_Op386DIVSS`
        - `rewriteValue386_Op386MULSD`
        - `rewriteValue386_Op386MULSS`
        - `rewriteValue386_Op386SUBSD`
        - `rewriteValue386_Op386SUBSDload`
        - `rewriteValue386_Op386SUBSS`
        - `rewriteValue386_Op386SUBSSload`
        - `rewriteValue386_OpNeg64F`
        - `rewriteValue386_OpNeq16`
        - `rewriteValue386_OpNeq32`
        - `rewriteValue386_OpNeq32F`
        - `rewriteValue386_OpNeq64F`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/x86/galign.go`
    - Ground Truth Functions (1):
        - `Init`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/x86/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (2):
        - `cmdenv`
        - `xinit`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/util_gc.go`
    - Ground Truth Functions (1):
        - `useVFPv1`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cfg/cfg.go`
    - Ground Truth Functions (1):
        - `GetArchEnv`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (2):
        - `buildActionID`
        - `printLinkerConfig`
    - Predicted Functions (0):

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (1):
        - `TestConvertNaNs`
    - Predicted Functions (0):

- **File:** `src/runtime/mkpreempt.go`
    - Ground Truth Functions (2):
        - `gen386`
        - `genAMD64`
    - Predicted Functions (0):

- **File:** `src/runtime/signal_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `dumpregs`
        - ❌ `fault`
        - ❌ `preparePanic`
        - ❌ `pushCall`
        - ❌ `siglr`
        - ❌ `sigpc`
        - ❌ `sigsp`

- **File:** `src/runtime/stubs_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_freebsd_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_openbsd_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/types_windows_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_linux_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/codegen/arithmetic.go`
    - Ground Truth Functions (3):
        - `DivMemSrc`
        - `FloatDivs`
        - `MulMemSrc`
    - Predicted Functions (0):

- **File:** `test/codegen/floats.go`
    - Ground Truth Functions (3):
        - `DivPow2`
        - `Mul2`
        - `indexStore`
    - Predicted Functions (0):

- **File:** `test/codegen/math.go`
    - Ground Truth Functions (1):
        - `sqrt`
    - Predicted Functions (0):

- **File:** `test/codegen/memops.go`
    - Ground Truth Functions (2):
        - `idxFloat32`
        - `idxFloat64`
    - Predicted Functions (0):


### 📊 **Proposal #45628 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 37.5% | 100.0% | 54.5% | 3/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/xml/xml.go`
    - Ground Truth Functions (2):
        - `InputPos`
        - `getc`
    - Predicted Functions (6):
        - ❌ `InputOffset`
        - ✅ `InputPos`
        - ❌ `NewDecoder`
        - ❌ `Token`
        - ✅ `getc`
        - ❌ `ungetc`

- **File:** `src/encoding/xml/xml_test.go`
    - Ground Truth Functions (1):
        - `TestInputLinePos`
    - Predicted Functions (2):
        - ✅ `TestInputLinePos`
        - ❌ `TestSyntaxErrorLineNum`


### 📊 **Proposal #52376 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 33.3% | 25.0% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/abi.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/abi_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (1):
        - `TestIsZero`
    - Predicted Functions (0):

- **File:** `src/reflect/iter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/iter_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (2):
        - `IsZero`
        - `SetZero`
    - Predicted Functions (5):
        - ❌ `Clear`
        - ❌ `IsNil`
        - ❌ `Set`
        - ✅ `SetZero`
        - ❌ `Zero`


### 📊 **Proposal #51777 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/net.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `IPv6Loopback`

- **File:** `src/net/netip/netip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `AddrFrom16`
        - ❌ `IPv6Loopback`
        - ❌ `IsLoopback`

- **File:** `src/net/netip/netip_test.go`
    - Ground Truth Functions (2):
        - `TestAddrWellKnown`
        - `TestNoAllocs`
    - Predicted Functions (0):


### 📊 **Proposal #40127 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `(*encodeState) ClosingToken`
        - ❌ `(*encodeState) EncodeToken`
        - ❌ `(*encodeState) error`
        - ❌ `(*encodeState) marshal`
        - ❌ `(*encodeState) reflectValue`
        - ❌ `newEncodeState`

- **File:** `src/encoding/json/encode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `ClosingToken`
        - ❌ `EncodeToken`
        - ❌ `MarshalJSON`

- **File:** `src/encoding/json/indent.go`
    - Ground Truth Functions (1):
        - `Indent`
    - Predicted Functions (0):

- **File:** `src/encoding/json/internal/jsonflags/flags.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/json/internal/jsonopts/options.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/json/internal/jsontest/testcase.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/json/internal/jsontest/testdata.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `MarshalJSON`
        - ❌ `UnmarshalJSON`

- **File:** `src/encoding/json/internal/jsonwire/decode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `ConsumeLiteral`
        - ❌ `ConsumeNumber`
        - ❌ `ConsumeSimpleNumber`
        - ❌ `ConsumeString`

- **File:** `src/encoding/json/internal/jsonwire/decode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/json/internal/jsonwire/encode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/json/internal/jsonwire/wire.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/json/internal/jsonwire/wire_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/json/jsontext/encode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `NewEncoder`
        - ❌ `WriteToken`
        - ❌ `WriteValue`

- **File:** `src/encoding/json/jsontext/encode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `TestEncoder`
        - ❌ `TestEncoderErrors`
        - ❌ `TestFaultyEncoder`
        - ❌ `testEncoder`
        - ❌ `testEncoderErrors`
        - ❌ `testFaultyEncoder`

- **File:** `src/encoding/json/jsontext/token.go`
    - Ground Truth Functions (0):
    - Predicted Functions (12):
        - ❌ `Bool`
        - ❌ `Float`
        - ❌ `Int`
        - ❌ `String`
        - ❌ `Token.Bool`
        - ❌ `Token.Clone`
        - ❌ `Token.Float`
        - ❌ `Token.Int`
        - ❌ `Token.Kind`
        - ❌ `Token.String`
        - ❌ `Token.Uint`
        - ❌ `Uint`

- **File:** `src/encoding/json/jsontext/token_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/json/stream.go`
    - Ground Truth Functions (2):
        - `Encode`
        - `tokenError`
    - Predicted Functions (0):


### 📊 **Proposal #51225 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/base/flag.go`
    - Ground Truth Functions (2):
        - `ParseFlags`
        - `readImportCfg`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/import.go`
    - Ground Truth Functions (1):
        - `openPackage`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (1):
        - `gc`
    - Predicted Functions (0):

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Import`
        - ❌ `ImportDir`
        - ❌ `matchFile`
        - ❌ `shouldBuild`

- **File:** `src/go/build/build_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestImportCmd`


### 📊 **Proposal #29062 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/test/test.go`
    - Ground Truth Functions (3):
        - `Write`
        - `tryCache`
        - `tryCacheWithID`
    - Predicted Functions (0):

- **File:** `src/cmd/objdump/objdump_test.go`
    - Ground Truth Functions (1):
        - `TestMain`
    - Predicted Functions (0):

- **File:** `src/internal/testenv/testenv.go`
    - Ground Truth Functions (1):
        - `HasGoBuild`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestExit`
        - ❌ `TestExitCode`
        - ❌ `TestExitStatus`

- **File:** `src/os/os_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestExit`
        - ❌ `TestMain`

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (0):
    - Predicted Functions (11):
        - ❌ `(*M) Run`
        - ❌ `(*T) Error`
        - ❌ `(*T) Errorf`
        - ❌ `(*T) Fatal`
        - ❌ `(*T) Fatalf`
        - ❌ `(*T) Run`
        - ❌ `(*T) SetPanicOnExit0`
        - ❌ `(*T) Skip`
        - ❌ `(*T) Skipf`
        - ❌ `Main`
        - ❌ `MainStart`

- **File:** `src/testing/testing_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestMain`
        - ❌ `TestRunningTests`
        - ❌ `TestRunningTestsInCleanup`


### 📊 **Proposal #40276 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/modload/init.go`
    - Ground Truth Functions (4):
        - `BinDir`
        - `Enabled`
        - `Init`
        - `WillBeEnabled`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (2):
        - `installOutsideModule`
        - `runInstall`
    - Predicted Functions (0):


### 📊 **Proposal #39567 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 25.0% | 16.7% | 1/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/request.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `MaxBytesReader`

- **File:** `src/net/http/response.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/serve_test.go`
    - Ground Truth Functions (2):
        - `TestMaxBytesHandler`
        - `testMaxBytesHandler`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (2):
        - `MaxBytesHandler`
        - `serve`
    - Predicted Functions (7):
        - ❌ `(*Server) ListenAndServe`
        - ❌ `(*Server) Serve`
        - ❌ `(*Server) ServeTLS`
        - ❌ `(*Server) Shutdown`
        - ❌ `(*Server) initialReadLimitSize`
        - ❌ `(*Server) maxHeaderBytes`
        - ✅ `MaxBytesHandler`


### 📊 **Proposal #48294 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (3):
        - `TestMapIterReset`
        - `TestMapIterSet`
        - `TestSetIter`
    - Predicted Functions (0):

- **File:** `src/reflect/iter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `SetIterKey`
        - ❌ `SetIterValue`
        - ❌ `SetKey`
        - ❌ `SetValue`

- **File:** `src/reflect/iter_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #46057 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/cert_pool.go`
    - Ground Truth Functions (1):
        - `Equal`
    - Predicted Functions (4):
        - ❌ `AddCert`
        - ❌ `AppendCertsFromPEM`
        - ✅ `Equal`
        - ❌ `Subjects`

- **File:** `src/crypto/x509/cert_pool_test.go`
    - Ground Truth Functions (1):
        - `TestCertPoolEqual`
    - Predicted Functions (1):
        - ✅ `TestCertPoolEqual`

- **File:** `src/crypto/x509/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/deepequal.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `DeepEqual`


### 📊 **Proposal #35044 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/cert_pool.go`
    - Ground Truth Functions (1):
        - `SystemCertPool`
    - Predicted Functions (4):
        - ❌ `AddCert`
        - ❌ `AppendCertsFromPEM`
        - ❌ `Clone`
        - ❌ `Equal`

- **File:** `src/crypto/x509/cert_pool_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestCertPoolEqual`

- **File:** `src/crypto/x509/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/clone.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #28308 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/91 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`
    - Ground Truth Functions (9):
        - `Preadv`
        - `Pwritev`
        - `Readv`
        - `Writev`
        - `appendBytes`
        - `darwinKernelVersionMin`
        - `darwinMajorMinPatch`
        - `readvRacedetect`
        - `writevRacedetect`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_linux.go`
    - Ground Truth Functions (6):
        - `anyToSockaddr`
        - `isCapDacOverrideSet`
        - `isGroupMember`
        - `readvRacedetect`
        - `sockaddr`
        - `writevRacedetect`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
    - Ground Truth Functions (4):
        - `preadv`
        - `pwritev`
        - `readv`
        - `writev`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
    - Ground Truth Functions (4):
        - `preadv`
        - `pwritev`
        - `readv`
        - `writev`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/text/language/parse.go`
    - Ground Truth Functions (1):
        - `Parse`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/composite/composite.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/copylock/copylock.go`
    - Ground Truth Functions (1):
        - `lockPath`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/hostport/hostport.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/lostcancel/lostcancel.go`
    - Ground Truth Functions (1):
        - `runFunc`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/nilfunc/nilfunc.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
    - Ground Truth Functions (2):
        - `checkCanonicalFieldTag`
        - `checkTagDuplicates`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/testinggoroutine.go`
    - Ground Truth Functions (2):
        - `goAsyncCall`
        - `tRunAsyncCall`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/testinggoroutine/util.go`
    - Ground Truth Functions (2):
        - `funcLitInScope`
        - `isMethodNamed`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/unreachable/unreachable.go`
    - Ground Truth Functions (1):
        - `findDead`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/types/typeutil/callee.go`
    - Ground Truth Functions (4):
        - `Callee`
        - `StaticCallee`
        - `interfaceMethod`
        - `usedIdent`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/analysisinternal/analysis.go`
    - Ground Truth Functions (5):
        - `AddImport`
        - `Format`
        - `FreshName`
        - `IsStdPackage`
        - `validateFix`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/astutil/clone.go`
    - Ground Truth Functions (2):
        - `CloneNode`
        - `cloneNode`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/astutil/comment.go`
    - Ground Truth Functions (3):
        - `Deprecation`
        - `Directives`
        - `isDirective`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/astutil/cursor/cursor.go`
    - Ground Truth Functions (5):
        - `At`
        - `Enclosing`
        - `FindByPos`
        - `FindNode`
        - `Inspect`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/astutil/util.go`
    - Ground Truth Functions (3):
        - `PosInStringLiteral`
        - `PreorderStack`
        - `RangeInStringLiteral`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/bisect/bisect.go`
    - Ground Truth Functions (3):
        - `AppendMarker`
        - `fnvUint32`
        - `fnvUint64`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/typeparams/free.go`
    - Ground Truth Functions (1):
        - `Has`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/typeparams/termlist.go`
    - Ground Truth Functions (1):
        - `String`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/classify_call.go`
    - Ground Truth Functions (5):
        - `ClassifyCall`
        - `String`
        - `UsedIdent`
        - `interfaceMethod`
        - `usedIdent`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/typeindex/typeindex.go`
    - Ground Truth Functions (8):
        - `Calls`
        - `Def`
        - `New`
        - `Object`
        - `Package`
        - `Selection`
        - `Used`
        - `Uses`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/internal/typesinternal/types.go`
    - Ground Truth Functions (1):
        - `NewTypesInfo`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/testdata/hostport/hostport.go`
    - Ground Truth Functions (1):
        - `_`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (1):
        - `TestVet`
    - Predicted Functions (0):

- **File:** `src/net/dial.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Dial`
        - ❌ `DialTimeout`
        - ❌ `Dialer.Dial`
        - ❌ `Dialer.DialContext`

- **File:** `src/net/http/h2_bundle.go`
    - Ground Truth Functions (4):
        - `ReadFrame`
        - `handlePingTimer`
        - `http2invalidHTTP1LookingFrameHeader`
        - `serve`
    - Predicted Functions (0):

- **File:** `src/net/net.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Dial`
        - ❌ `JoinHostPort`
        - ❌ `SplitHostPort`

- **File:** `src/vendor/golang.org/x/crypto/cryptobyte/asn1.go`
    - Ground Truth Functions (1):
        - `AddASN1`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_linux_loong64.go`
    - Ground Truth Functions (2):
        - `doinit`
        - `hwcIsSet`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_loong64.go`
    - Ground Truth Functions (3):
        - `cfgIsSet`
        - `get_cpucfg`
        - `initOptions`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/parse.go`
    - Ground Truth Functions (1):
        - `parseRelease`
    - Predicted Functions (0):


### 📊 **Proposal #43698 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/vet/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Check`
        - ❌ `CheckComment`
        - ❌ `CheckFile`
        - ❌ `Vet`

- **File:** `src/cmd/vet/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestVet`
        - ❌ `errorCheck`

- **File:** `src/embed/embed.go`
    - Ground Truth Functions (2):
        - `lookup`
        - `readDir`
    - Predicted Functions (0):

- **File:** `src/embed/internal/embedtest/embed_test.go`
    - Ground Truth Functions (1):
        - `TestUninitialized`
    - Predicted Functions (0):


### 📊 **Proposal #48256 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/workcmd/edit.go`
    - Ground Truth Functions (5):
        - `allowedVersionArg`
        - `flagEditworkReplace`
        - `init`
        - `parsePathVersionOptional`
        - `runEditwork`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/workcmd/init.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/main.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):


### 📊 **Proposal #51868 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/debug/pe/file.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `COFFSymbolReadSectionDefAux`

- **File:** `src/debug/pe/pe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `COFFSymbolReadSectionDefAux`

- **File:** `src/debug/pe/section.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `COFFSymbolReadSectionDefAux`

- **File:** `src/debug/pe/symbol.go`
    - Ground Truth Functions (1):
        - `COFFSymbolReadSectionDefAux`
    - Predicted Functions (1):
        - ✅ `COFFSymbolReadSectionDefAux`

- **File:** `src/debug/pe/symbols_test.go`
    - Ground Truth Functions (1):
        - `TestReadCOFFSymbolAuxInfo`
    - Predicted Functions (0):


### 📊 **Proposal #52444 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 3/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/pem_decrypt.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/x509/pem_decrypt_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (1):
        - `CreateCertificate`
    - Predicted Functions (7):
        - ❌ `(*Certificate) CheckSignature`
        - ❌ `(*Certificate) CheckSignatureFrom`
        - ❌ `(*Certificate) CreateCRL`
        - ❌ `(*Certificate) Equal`
        - ✅ `CreateCertificate`
        - ❌ `CreateCertificateRequest`
        - ❌ `CreateRevocationList`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (2):
        - `TestCreateNegativeSerial`
        - `TestParseNegativeSerial`
    - Predicted Functions (2):
        - ✅ `TestCreateNegativeSerial`
        - ✅ `TestParseNegativeSerial`


### 📊 **Proposal #38776 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 2.2% | 2.7% | 2.4% | 1/37 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/internal/boring/sha.go`
    - Ground Truth Functions (3):
        - `MarshalBinary`
        - `NewSHA512`
        - `sum`
    - Predicted Functions (0):

- **File:** `src/crypto/md5/md5_test.go`
    - Ground Truth Functions (7):
        - `BenchmarkHash1K`
        - `BenchmarkHash1KUnaligned`
        - `BenchmarkHash8Bytes`
        - `BenchmarkHash8BytesUnaligned`
        - `BenchmarkHash8K`
        - `BenchmarkHash8KUnaligned`
        - `benchmarkSize`
    - Predicted Functions (0):

- **File:** `src/crypto/sha1/sha1.go`
    - Ground Truth Functions (1):
        - `Write`
    - Predicted Functions (3):
        - ❌ `BlockSize`
        - ❌ `Size`
        - ✅ `Write`

- **File:** `src/crypto/sha1/sha1_test.go`
    - Ground Truth Functions (3):
        - `TestAllocations`
        - `TestGolden`
        - `TestLargeHashes`
    - Predicted Functions (1):
        - ❌ `TestExtraMethods`

- **File:** `src/crypto/sha1/sha1block_amd64.go`
    - Ground Truth Functions (2):
        - `block`
        - `blockAVX2`
    - Predicted Functions (0):

- **File:** `src/crypto/sha1/sha1block_arm64.go`
    - Ground Truth Functions (2):
        - `block`
        - `sha1block`
    - Predicted Functions (0):

- **File:** `src/crypto/sha1/sha1block_decl.go`
    - Ground Truth Functions (1):
        - `block`
    - Predicted Functions (0):

- **File:** `src/crypto/sha256/sha256.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `New`
        - ❌ `New224`
        - ❌ `Sum224`
        - ❌ `Sum256`

- **File:** `src/crypto/sha256/sha256_test.go`
    - Ground Truth Functions (5):
        - `TestAllocations`
        - `TestCgo`
        - `TestGolden`
        - `TestLargeHashes`
        - `benchmarkSize`
    - Predicted Functions (1):
        - ❌ `TestExtraMethods`

- **File:** `src/crypto/sha3/sha3.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `BlockSize`
        - ❌ `Reset`
        - ❌ `Size`
        - ❌ `Sum`
        - ❌ `Write`

- **File:** `src/crypto/sha3/sha3_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/sha512/sha512.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `New`
        - ❌ `Sum384`
        - ❌ `Sum512`
        - ❌ `Sum512_224`
        - ❌ `Sum512_256`

- **File:** `src/crypto/sha512/sha512_test.go`
    - Ground Truth Functions (5):
        - `TestAllocations`
        - `TestGolden`
        - `TestLargeHashes`
        - `benchmarkSize`
        - `testHash`
    - Predicted Functions (1):
        - ❌ `TestExtraMethods`

- **File:** `src/hash/adler32/adler32.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `BlockSize`
        - ❌ `Reset`
        - ❌ `Size`
        - ❌ `Sum`
        - ❌ `Sum32`
        - ❌ `Write`

- **File:** `src/hash/crc32/crc32.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Sum`
        - ❌ `Sum32`
        - ❌ `Write`

- **File:** `src/hash/crc32/crc32_test.go`
    - Ground Truth Functions (4):
        - `TestGolden`
        - `TestSimple`
        - `TestSlicing`
        - `testGoldenCastagnoli`
    - Predicted Functions (0):

- **File:** `src/hash/crc64/crc64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `(*digest) BlockSize`
        - ❌ `(*digest) Reset`
        - ❌ `(*digest) Size`
        - ❌ `(*digest) Sum64`
        - ❌ `(*digest) Write`
        - ❌ `New`

- **File:** `src/hash/crc64/crc64_test.go`
    - Ground Truth Functions (2):
        - `BenchmarkCrc64`
        - `bench`
    - Predicted Functions (0):

- **File:** `src/hash/fnv/fnv.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `New128`
        - ❌ `New128a`
        - ❌ `New32`
        - ❌ `New32a`
        - ❌ `New64`
        - ❌ `New64a`
        - ❌ `Write`

- **File:** `src/hash/fnv/fnv_test.go`
    - Ground Truth Functions (2):
        - `testGolden`
        - `testIntegrity`
    - Predicted Functions (0):

- **File:** `src/hash/hash.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Write`
        - ❌ `WriteByte`
        - ❌ `WriteString`


### 📊 **Proposal #45460 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/request.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `NewRequest`
        - ❌ `NewRequestWithContext`
        - ❌ `ReadRequest`
        - ❌ `WriteProxy`

- **File:** `src/net/http/transport.go`
    - Ground Truth Functions (1):
        - `dialConn`
    - Predicted Functions (5):
        - ❌ `ProxyFromEnvironment`
        - ❌ `ProxyURL`
        - ❌ `connectMethodForRequest`
        - ❌ `customDialTLS`
        - ❌ `proxyAuth`


### 📊 **Proposal #46258 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.8% | 11.1% | 5.7% | 1/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Command`
        - ❌ `CommandContext`
        - ❌ `Run`
        - ❌ `Start`

- **File:** `src/os/exec/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Pdeathsig`
        - ❌ `Start`
        - ❌ `StartProcess`

- **File:** `src/os/signal/signal.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Notify`
        - ❌ `NotifyContext`

- **File:** `src/os/signal/signal_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (12):
        - ❌ `disableSignal`
        - ❌ `enableSignal`
        - ❌ `ignoreSignal`
        - ❌ `init`
        - ❌ `loop`
        - ❌ `signalIgnored`
        - ❌ `signal_disable`
        - ❌ `signal_enable`
        - ❌ `signal_ignore`
        - ❌ `signal_ignored`
        - ❌ `signal_recv`
        - ❌ `signum`

- **File:** `src/syscall/exec_freebsd.go`
    - Ground Truth Functions (4):
        - `forkAndExecInChild`
        - `runtime_AfterFork`
        - `runtime_AfterForkInChild`
        - `runtime_BeforeFork`
    - Predicted Functions (1):
        - ✅ `forkAndExecInChild`

- **File:** `src/syscall/exec_pdeathsig_test.go`
    - Ground Truth Functions (2):
        - `deathSignalChild`
        - `deathSignalParent`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_freebsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `RawSyscall`
        - ❌ `RawSyscall6`
        - ❌ `Syscall`
        - ❌ `Syscall6`

- **File:** `src/syscall/syscall_freebsd_test.go`
    - Ground Truth Functions (1):
        - `TestMain`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_test.go`
    - Ground Truth Functions (2):
        - `TestParseNetlinkMessage`
        - `TestSyscallNoError`
    - Predicted Functions (0):


### 📊 **Proposal #32406 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 7.7% | 9.5% | 2/26 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (1):
        - `Context`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/conn.go`
    - Ground Truth Functions (4):
        - `Handshake`
        - `HandshakeContext`
        - `handleRenegotiation`
        - `handshakeContext`
    - Predicted Functions (3):
        - ❌ `ConnectionState`
        - ✅ `Handshake`
        - ✅ `HandshakeContext`

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (3):
        - `certificateRequestInfoFromMsg`
        - `clientHandshake`
        - `doFullHandshake`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_client_test.go`
    - Ground Truth Functions (1):
        - `TestClientHandshakeContextCancellation`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_client_tls13.go`
    - Ground Truth Functions (1):
        - `sendClientCertificate`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server.go`
    - Ground Truth Functions (6):
        - `clientHelloInfo`
        - `handshake`
        - `processCertsFromClient`
        - `processClientHello`
        - `readClientHello`
        - `serverHandshake`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server_test.go`
    - Ground Truth Functions (3):
        - `TestSNIGivenOnFailure`
        - `TestServerHandshakeContextCancellation`
        - `testClientHelloFailure`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server_tls13.go`
    - Ground Truth Functions (1):
        - `pickCertificate`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/tls.go`
    - Ground Truth Functions (2):
        - `Dial`
        - `dial`
    - Predicted Functions (2):
        - ❌ `DialContext`
        - ❌ `HandshakeContext`

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (1):
        - `serve`
    - Predicted Functions (11):
        - ❌ `(*Server).Serve`
        - ❌ `(*Server).ServeTLS`
        - ❌ `(*Server).newConn`
        - ❌ `(*conn).close`
        - ❌ `(*conn).closeWriteAndWait`
        - ❌ `(*conn).finalFlush`
        - ❌ `(*conn).getState`
        - ❌ `(*conn).readRequest`
        - ❌ `(*conn).serve`
        - ❌ `(*conn).setState`
        - ❌ `(*conn).tlsHandshakeTimeout`

- **File:** `src/net/http/transport.go`
    - Ground Truth Functions (2):
        - `addTLS`
        - `dialConn`
    - Predicted Functions (0):

- **File:** `src/net/http/transport_test.go`
    - Ground Truth Functions (1):
        - `TestTransportDialTLSContext`
    - Predicted Functions (0):


### 📊 **Proposal #41980 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmp/cmp.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Compare`

- **File:** `src/cmp/cmp_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `ExampleCompare`
        - ❌ `ExampleLess`
        - ❌ `ExampleOr`

- **File:** `src/internal/diff/diff_test.go`
    - Ground Truth Functions (1):
        - `Test`
    - Predicted Functions (0):

- **File:** `src/testing/example.go`
    - Ground Truth Functions (1):
        - `processRunResult`
    - Predicted Functions (0):

- **File:** `src/testing/run_example.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `runExample`


### 📊 **Proposal #42782 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 27.3% | 100.0% | 42.9% | 3/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Field`
        - ❌ `FieldByIndex`
        - ❌ `FieldByName`
        - ❌ `FieldByNameFunc`
        - ❌ `NumField`
        - ❌ `StructOf`
        - ❌ `embeddedIfaceMethStub`

- **File:** `src/reflect/visiblefields.go`
    - Ground Truth Functions (2):
        - `VisibleFields`
        - `walk`
    - Predicted Functions (2):
        - ✅ `VisibleFields`
        - ✅ `walk`

- **File:** `src/reflect/visiblefields_test.go`
    - Ground Truth Functions (1):
        - `TestFields`
    - Predicted Functions (2):
        - ❌ `TestFieldByIndexErr`
        - ✅ `TestFields`


### 📊 **Proposal #42100 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 16.7% | 19.0% | 2/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `misc/ios/detect.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `misc/ios/go_ios_exec.go`
    - Ground Truth Functions (8):
        - `assembleApp`
        - `entitlementsPlist`
        - `infoPlist`
        - `installSimulator`
        - `main`
        - `runMain`
        - `runOnSimulator`
        - `runSimulator`
    - Predicted Functions (2):
        - ✅ `runOnSimulator`
        - ✅ `runSimulator`

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (1):
        - `wrapperPathFor`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `registerTests`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/init.go`
    - Ground Truth Functions (1):
        - `buildModeInit`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/elf.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `goarch`

- **File:** `src/cmd/internal/objfile/goobj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `goarch`
        - ❌ `goobjName`
        - ❌ `loadAddress`

- **File:** `src/cmd/internal/objfile/macho.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `goarch`
        - ❌ `openMacho`

- **File:** `src/cmd/internal/objfile/objfile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `GOARCH`

- **File:** `src/cmd/internal/objfile/pe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/plan9obj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/xcoff.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/config.go`
    - Ground Truth Functions (1):
        - `Set`
    - Predicted Functions (0):

- **File:** `src/runtime/defs_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/signal_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/rlimit_darwin.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/route_darwin.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_darwin_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zsysnum_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/ztypes_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/ztypes_darwin_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #51896 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 44.4% | 100.0% | 61.5% | 4/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/unicode/utf16/utf16.go`
    - Ground Truth Functions (1):
        - `AppendRune`
    - Predicted Functions (3):
        - ✅ `AppendRune`
        - ❌ `Count`
        - ❌ `EncodeInto`

- **File:** `src/unicode/utf16/utf16_test.go`
    - Ground Truth Functions (3):
        - `BenchmarkAppendRuneValidASCII`
        - `BenchmarkAppendRuneValidJapaneseChars`
        - `TestAppendRune`
    - Predicted Functions (6):
        - ❌ `AppendRune`
        - ✅ `BenchmarkAppendRuneValidASCII`
        - ✅ `BenchmarkAppendRuneValidJapaneseChars`
        - ❌ `Count`
        - ❌ `EncodeInto`
        - ✅ `TestAppendRune`


### 📊 **Proposal #52792 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/modfetch/fetch.go`
    - Ground Truth Functions (1):
        - `RecordedSum`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modinfo/info.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `String`
        - ❌ `UnmarshalJSON`

- **File:** `src/cmd/go/internal/modload/build.go`
    - Ground Truth Functions (1):
        - `moduleInfo`
    - Predicted Functions (0):


### 📊 **Proposal #46259 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 33.3% | 30.8% | 2/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/syscall/exec_bsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `forkAndExecInChild`

- **File:** `src/syscall/exec_freebsd.go`
    - Ground Truth Functions (4):
        - `forkAndExecInChild`
        - `runtime_AfterFork`
        - `runtime_AfterForkInChild`
        - `runtime_BeforeFork`
    - Predicted Functions (2):
        - ✅ `forkAndExecInChild`
        - ✅ `runtime_AfterForkInChild`

- **File:** `src/syscall/exec_freebsd_test.go`
    - Ground Truth Functions (2):
        - `TestJailAttach`
        - `prepareJail`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_freebsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `RawSyscall`
        - ❌ `RawSyscall6`
        - ❌ `Syscall`
        - ❌ `Syscall6`

- **File:** `src/syscall/syscall_freebsd_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #46505 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/sha256/sha256.go`
    - Ground Truth Functions (1):
        - `Sum224`
    - Predicted Functions (0):

- **File:** `src/crypto/sha512/sha512.go`
    - Ground Truth Functions (3):
        - `Sum384`
        - `Sum512_224`
        - `Sum512_256`
    - Predicted Functions (0):


### 📊 **Proposal #31804 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 62.5% | 76.9% | 5/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/ed25519/ed25519.go`
    - Ground Truth Functions (5):
        - `Sign`
        - `Verify`
        - `VerifyWithOptions`
        - `newKeyFromSeed`
        - `sign`
    - Predicted Functions (3):
        - ✅ `Sign`
        - ✅ `Verify`
        - ✅ `VerifyWithOptions`

- **File:** `src/crypto/ed25519/ed25519_test.go`
    - Ground Truth Functions (3):
        - `TestCryptoSigner`
        - `TestSignVerifyContext`
        - `TestSignVerifyHashed`
    - Predicted Functions (2):
        - ✅ `TestSignVerifyContext`
        - ✅ `TestSignVerifyHashed`


### 📊 **Proposal #40356 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf/printf.go`
    - Ground Truth Functions (1):
        - `checkPrintf`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer/sigchanyzer.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods/stdmethods.go`
    - Ground Truth Functions (2):
        - `canonicalMethod`
        - `implementsError`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `checkAsMethod`
        - ❌ `checkErrorMethods`
        - ❌ `checkIsMethod`
        - ❌ `checkUnwrapMethod`

- **File:** `src/cmd/vet/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `checkAsMethod`
        - ❌ `checkErrorMethods`
        - ❌ `checkIsMethod`
        - ❌ `checkUnwrapMethod`

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `errorCheck`

- **File:** `src/errors/errors.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `As`
        - ❌ `Is`
        - ❌ `Unwrap`

- **File:** `src/errors/errors_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestErrorMethod`

- **File:** `src/errors/join.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Unwrap`

- **File:** `src/errors/join_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestJoinErrorMethod`

- **File:** `src/errors/wrap.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `As`
        - ❌ `Is`
        - ❌ `Unwrap`

- **File:** `src/errors/wrap_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `As`
        - ❌ `Error`
        - ❌ `Is`
        - ❌ `Unwrap`

- **File:** `src/fmt/errors.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Unwrap`

- **File:** `src/fmt/errors_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Error`


### 📊 **Proposal #46552 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 27.3% | 27.3% | 27.3% | 3/11 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/syscall_windows.go`
    - Ground Truth Functions (7):
        - `syscall_Syscall`
        - `syscall_Syscall12`
        - `syscall_Syscall15`
        - `syscall_Syscall18`
        - `syscall_Syscall6`
        - `syscall_Syscall9`
        - `syscall_SyscallN`
    - Predicted Functions (3):
        - ✅ `syscall_Syscall18`
        - ✅ `syscall_SyscallN`
        - ❌ `syscall_syscalln`

- **File:** `src/runtime/syscall_windows_test.go`
    - Ground Truth Functions (1):
        - `TestSyscallN`
    - Predicted Functions (1):
        - ✅ `TestSyscallN`

- **File:** `src/syscall/dll_windows.go`
    - Ground Truth Functions (3):
        - `Call`
        - `Load`
        - `SyscallN`
    - Predicted Functions (0):

- **File:** `src/syscall/mksyscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Syscall`
        - ❌ `Syscall21`
        - ❌ `Syscall24`
        - ❌ `SyscallN`

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Syscall21`
        - ❌ `Syscall24`
        - ❌ `SyscallN`


### 📊 **Proposal #48409 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 1.7% | 3.0% | 2/121 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/debug/garbage.go`
    - Ground Truth Functions (1):
        - `SetMemoryLimit`
    - Predicted Functions (3):
        - ❌ `FreeOSMemory`
        - ❌ `SetGCPercent`
        - ✅ `SetMemoryLimit`

- **File:** `src/runtime/debug/garbage_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestFreeOSMemory`
        - ❌ `TestSetGCPercent`

- **File:** `src/runtime/debug/heapdump_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestWriteHeapDumpFinalizers`
        - ❌ `TestWriteHeapDumpNonempty`
        - ❌ `TestWriteHeapDumpTypeName`

- **File:** `src/runtime/debug/mod.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `SetMemoryLimit`

- **File:** `src/runtime/debug/mod_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `SetMemoryLimit`

- **File:** `src/runtime/debug/panic_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/debug/stack.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `SetMemoryLimit`

- **File:** `src/runtime/debug/stack_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestSetCrashOutput`

- **File:** `src/runtime/debug/stubs.go`
    - Ground Truth Functions (1):
        - `setMemoryLimit`
    - Predicted Functions (2):
        - ❌ `setGCPercent`
        - ✅ `setMemoryLimit`

- **File:** `src/runtime/debuglog.go`
    - Ground Truth Functions (2):
        - `dlog`
        - `printDebugLog`
    - Predicted Functions (0):

- **File:** `src/runtime/export_test.go`
    - Ground Truth Functions (21):
        - `Capacity`
        - `EndCycle`
        - `Fill`
        - `Find`
        - `FinishGCTransition`
        - `FreePageAlloc`
        - `HeapGoal`
        - `Limiting`
        - `MakeAddrRanges`
        - `NeedUpdate`
        - `NewAddrRanges`
        - `NewGCCPULimiter`
        - `NewGCController`
        - `NewPageAlloc`
        - `NewScavengeIndex`
        - `Overflow`
        - `ResetCapacity`
        - `StartCycle`
        - `StartGCTransition`
        - `Triggered`
        - `Update`
    - Predicted Functions (0):

- **File:** `src/runtime/gc_test.go`
    - Ground Truth Functions (2):
        - `TestMemoryLimit`
        - `TestMemoryLimitNoGCPercent`
    - Predicted Functions (0):

- **File:** `src/runtime/malloc.go`
    - Ground Truth Functions (3):
        - `alloc`
        - `sysAlloc`
        - `sysReserveAligned`
    - Predicted Functions (0):

- **File:** `src/runtime/mcache.go`
    - Ground Truth Functions (3):
        - `allocLarge`
        - `refill`
        - `releaseAll`
    - Predicted Functions (0):

- **File:** `src/runtime/mem.go`
    - Ground Truth Functions (5):
        - `sysAlloc`
        - `sysFault`
        - `sysFree`
        - `sysUnused`
        - `sysUsed`
    - Predicted Functions (0):

- **File:** `src/runtime/metrics.go`
    - Ground Truth Functions (2):
        - `compute`
        - `initMetrics`
    - Predicted Functions (0):

- **File:** `src/runtime/mgc.go`
    - Ground Truth Functions (6):
        - `gcMarkDone`
        - `gcMarkTermination`
        - `gcStart`
        - `gcenable`
        - `gcinit`
        - `test`
    - Predicted Functions (0):

- **File:** `src/runtime/mgclimit.go`
    - Ground Truth Functions (10):
        - `accumulate`
        - `finishGCTransition`
        - `limiting`
        - `needUpdate`
        - `resetCapacity`
        - `startGCTransition`
        - `tryLock`
        - `unlock`
        - `update`
        - `updateLocked`
    - Predicted Functions (0):

- **File:** `src/runtime/mgclimit_test.go`
    - Ground Truth Functions (1):
        - `TestGCCPULimiter`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcmark.go`
    - Ground Truth Functions (2):
        - `gcAssistAlloc`
        - `gcAssistAlloc1`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcpacer.go`
    - Ground Truth Functions (18):
        - `addGlobals`
        - `addScannableStack`
        - `commit`
        - `endCycle`
        - `enlistWorker`
        - `findRunnableGCWorker`
        - `gcControllerCommit`
        - `heapGoal`
        - `heapGoalInternal`
        - `init`
        - `memoryLimitHeapGoal`
        - `readGOMEMLIMIT`
        - `resetLive`
        - `revise`
        - `setGCPercent`
        - `setMemoryLimit`
        - `startCycle`
        - `trigger`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcpacer_test.go`
    - Ground Truth Functions (4):
        - `TestGcPacer`
        - `TestIdleMarkWorkerCount`
        - `runway`
        - `triggerRatio`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcscavenge.go`
    - Ground Truth Functions (10):
        - `fillAligned`
        - `find`
        - `findScavengeCandidate`
        - `gcPaceScavenger`
        - `heapRetained`
        - `init`
        - `printScavTrace`
        - `scavenge`
        - `scavengeOne`
        - `wake`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcscavenge_test.go`
    - Ground Truth Functions (1):
        - `TestScavengeIndex`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcsweep.go`
    - Ground Truth Functions (2):
        - `sweep`
        - `sweepone`
    - Predicted Functions (0):

- **File:** `src/runtime/mheap.go`
    - Ground Truth Functions (5):
        - `allocSpan`
        - `freeSpanLocked`
        - `grow`
        - `runtime_debug_freeOSMemory`
        - `scavengeAll`
    - Predicted Functions (0):

- **File:** `src/runtime/mpagealloc.go`
    - Ground Truth Functions (3):
        - `free`
        - `grow`
        - `init`
    - Predicted Functions (0):

- **File:** `src/runtime/mpagealloc_32bit.go`
    - Ground Truth Functions (1):
        - `sysInit`
    - Predicted Functions (0):

- **File:** `src/runtime/mpagealloc_64bit.go`
    - Ground Truth Functions (2):
        - `sysGrow`
        - `sysInit`
    - Predicted Functions (0):

- **File:** `src/runtime/mranges.go`
    - Ground Truth Functions (5):
        - `Clear`
        - `Load`
        - `StoreMarked`
        - `StoreMin`
        - `StoreUnmark`
    - Predicted Functions (0):

- **File:** `src/runtime/mstats.go`
    - Ground Truth Functions (1):
        - `readmemstats_m`
    - Predicted Functions (0):

- **File:** `src/runtime/proc.go`
    - Ground Truth Functions (4):
        - `empty`
        - `findRunnable`
        - `procresize`
        - `sysmon`
    - Predicted Functions (0):

- **File:** `src/runtime/string.go`
    - Ground Truth Functions (1):
        - `parseByteCount`
    - Predicted Functions (0):

- **File:** `src/runtime/string_test.go`
    - Ground Truth Functions (1):
        - `TestParseByteCount`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprog/gc.go`
    - Ground Truth Functions (4):
        - `GCMemoryLimit`
        - `GCMemoryLimitNoGCPercent`
        - `gcMemoryLimit`
        - `init`
    - Predicted Functions (0):


### 📊 **Proposal #40034 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 6/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/smtp/auth.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `CRAMMD5Auth`
        - ❌ `PlainAuth`

- **File:** `src/net/smtp/smtp.go`
    - Ground Truth Functions (7):
        - `Auth`
        - `Close`
        - `Mail`
        - `NewClient`
        - `Rcpt`
        - `SendMail`
        - `StartTLS`
    - Predicted Functions (5):
        - ❌ `Client.SendMail`
        - ❌ `Dial`
        - ✅ `NewClient`
        - ✅ `SendMail`
        - ✅ `StartTLS`

- **File:** `src/net/smtp/smtp_test.go`
    - Ground Truth Functions (5):
        - `TestNewClient`
        - `TestNewClientWithTLS`
        - `TestSendMail`
        - `TestSendMailWithAuth`
        - `TestTLSConnState`
    - Predicted Functions (5):
        - ❌ `Client.SendMail`
        - ❌ `Client.StartTLS`
        - ✅ `TestNewClientWithTLS`
        - ✅ `TestSendMail`
        - ✅ `TestSendMailWithAuth`


### 📊 **Proposal #51572 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (1):
        - `matchtag`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/imports/build.go`
    - Ground Truth Functions (1):
        - `matchTag`
    - Predicted Functions (0):

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (1):
        - `matchTag`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/os_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestChown`
        - ❌ `TestFileChown`
        - ❌ `TestLchown`

- **File:** `src/syscall/env_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Clearenv`
        - ❌ `Environ`
        - ❌ `Getenv`
        - ❌ `Setenv`
        - ❌ `Unsetenv`

- **File:** `src/syscall/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Exec`
        - ❌ `ForkExec`
        - ❌ `StartProcess`

- **File:** `src/syscall/exec_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestExec`
        - ❌ `TestForkExecNilArgv`
        - ❌ `TestInvalidExec`

- **File:** `src/syscall/linkname_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/mmap_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestMmap`

- **File:** `src/syscall/sockcmsg_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ParseUnixRights`
        - ❌ `UnixRights`

- **File:** `src/syscall/sockcmsg_unix_other.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Bind`
        - ❌ `Connect`
        - ❌ `Getpeername`
        - ❌ `Recvfrom`
        - ❌ `Sendto`
        - ❌ `Socket`

- **File:** `src/syscall/syscall_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestUnixRightsRoundtrip`

- **File:** `src/time/sys_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `closefd`
        - ❌ `interrupt`
        - ❌ `open`
        - ❌ `preadn`
        - ❌ `read`

- **File:** `src/time/zoneinfo_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `initLocal`

- **File:** `src/time/zoneinfo_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #41048 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 25.0% | 22.2% | 1/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/transport.go`
    - Ground Truth Functions (2):
        - `Clone`
        - `dialConn`
    - Predicted Functions (3):
        - ❌ `GetProxyConnectHeader`
        - ❌ `ProxyConnectHeader`
        - ❌ `roundTrip`

- **File:** `src/net/http/transport_test.go`
    - Ground Truth Functions (2):
        - `TestTransportClone`
        - `TestTransportProxyGetConnectHeader`
    - Predicted Functions (2):
        - ❌ `TestTransportProxyConnectHeader`
        - ✅ `TestTransportProxyGetConnectHeader`


### 📊 **Proposal #40357 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/list/list.go`
    - Ground Truth Functions (1):
        - `runList`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/download.go`
    - Ground Truth Functions (1):
        - `runDownload`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/why.go`
    - Ground Truth Functions (1):
        - `runWhy`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/build.go`
    - Ground Truth Functions (3):
        - `ModuleInfo`
        - `PackageModuleInfo`
        - `moduleInfo`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/list.go`
    - Ground Truth Functions (2):
        - `ListModules`
        - `listModules`
    - Predicted Functions (0):


### 📊 **Proposal #39178 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.0% | 33.3% | 8.7% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/client.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `(*Client) Do`
        - ❌ `(*Client) Get`
        - ❌ `Do`
        - ❌ `Get`

- **File:** `src/net/lookup.go`
    - Ground Truth Functions (1):
        - `lookupIPAddr`
    - Predicted Functions (10):
        - ❌ `LookupAddr`
        - ❌ `LookupCNAME`
        - ❌ `LookupHost`
        - ❌ `LookupIP`
        - ❌ `LookupIPAddr`
        - ❌ `LookupMX`
        - ❌ `LookupNS`
        - ❌ `LookupSRV`
        - ❌ `LookupTXT`
        - ✅ `lookupIPAddr`

- **File:** `src/net/lookup_test.go`
    - Ground Truth Functions (2):
        - `TestDNSTimeout`
        - `TestLookupContextCancel`
    - Predicted Functions (0):

- **File:** `src/net/net.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `(*DNSError) Error`
        - ❌ `(*DNSError) Temporary`
        - ❌ `(*DNSError) Timeout`
        - ❌ `(*OpError) Temporary`
        - ❌ `(*OpError) Timeout`
        - ❌ `newDNSError`


### 📊 **Proposal #46287 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 10.3% | 11.9% | 4/39 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `registerTests`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/cert_pool.go`
    - Ground Truth Functions (1):
        - `SystemCertPool`
    - Predicted Functions (4):
        - ❌ `AddCertWithConstraint`
        - ❌ `Equal`
        - ❌ `Subjects`
        - ✅ `SystemCertPool`

- **File:** `src/crypto/x509/cert_pool_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestCertPoolEqual`

- **File:** `src/crypto/x509/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ExampleCertificate_Verify`
        - ❌ `ExampleParsePKIXPublicKey`

- **File:** `src/crypto/x509/hybrid_pool_test.go`
    - Ground Truth Functions (1):
        - `TestHybridPool`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/internal/macos/corefoundation.go`
    - Ground Truth Functions (15):
        - `BytesToCFData`
        - `CFArrayAppendValue`
        - `CFArrayCreateMutable`
        - `CFDateCreate`
        - `CFErrorCopyDescription`
        - `CFStringCreateExternalRepresentation`
        - `CFStringToString`
        - `ReleaseCFArray`
        - `TimeToCFDateRef`
        - `x509_CFArrayAppendValue_trampoline`
        - `x509_CFArrayCreateMutable_trampoline`
        - `x509_CFDataCreate_trampoline`
        - `x509_CFDateCreate_trampoline`
        - `x509_CFErrorCopyDescription_trampoline`
        - `x509_CFStringCreateExternalRepresentation_trampoline`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/internal/macos/security.go`
    - Ground Truth Functions (12):
        - `SecCertificateCreateWithData`
        - `SecPolicyCreateSSL`
        - `SecTrustCreateWithCertificates`
        - `SecTrustEvaluate`
        - `SecTrustEvaluateWithError`
        - `SecTrustSetVerifyDate`
        - `x509_SecCertificateCreateWithData_trampoline`
        - `x509_SecPolicyCreateSSL_trampoline`
        - `x509_SecTrustCreateWithCertificates_trampoline`
        - `x509_SecTrustEvaluateWithError_trampoline`
        - `x509_SecTrustEvaluate_trampoline`
        - `x509_SecTrustSetVerifyDate_trampoline`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/root_darwin.go`
    - Ground Truth Functions (3):
        - `exportCertificate`
        - `loadSystemRoots`
        - `systemVerify`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/root_windows.go`
    - Ground Truth Functions (2):
        - `loadSystemRoots`
        - `systemVerify`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/verify.go`
    - Ground Truth Functions (1):
        - `Verify`
    - Predicted Functions (3):
        - ✅ `Verify`
        - ❌ `VerifyHostname`
        - ❌ `buildChains`

- **File:** `src/crypto/x509/verify_test.go`
    - Ground Truth Functions (1):
        - `TestSystemRootsError`
    - Predicted Functions (5):
        - ❌ `TestEKUEnforcement`
        - ❌ `TestNameConstraints`
        - ✅ `TestSystemRootsError`
        - ❌ `TestSystemVerify`
        - ❌ `TestVerify`

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `CheckCRLSignature`
        - ❌ `CheckSignature`
        - ❌ `CheckSignatureFrom`
        - ❌ `CreateCertificate`
        - ❌ `CreateCertificateRequest`
        - ❌ `CreateRevocationList`
        - ❌ `SystemCertPool`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (1):
        - `TestSystemCertPool`
    - Predicted Functions (6):
        - ❌ `TestCertificateEqualOnNil`
        - ❌ `TestEmptyNameConstraints`
        - ❌ `TestMatchHostnames`
        - ❌ `TestMatchIP`
        - ✅ `TestSystemCertPool`
        - ❌ `TestVerifyCertificateWithDSASignature`

- **File:** `src/runtime/sys_darwin.go`
    - Ground Truth Functions (1):
        - `crypto_x509_syscall`
    - Predicted Functions (0):


### 📊 **Proposal #50101 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 5.1% | 7.5% | 2/39 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/internal/syscall/unix/net_darwin.go`
    - Ground Truth Functions (6):
        - `ResNclose`
        - `ResNinit`
        - `ResNsearch`
        - `libresolv_res_9_nclose_trampoline`
        - `libresolv_res_9_ninit_trampoline`
        - `libresolv_res_9_nsearch_trampoline`
    - Predicted Functions (0):

- **File:** `src/net/cgo_unix.go`
    - Ground Truth Functions (6):
        - `cgoLookupCNAME`
        - `cgoLookupHostIP`
        - `cgoLookupIP`
        - `cgoResSearch`
        - `cgoSockaddr`
        - `resSearch`
    - Predicted Functions (0):

- **File:** `src/net/cgo_unix_cgo_res.go`
    - Ground Truth Functions (3):
        - `_C_res_nclose`
        - `_C_res_ninit`
        - `_C_res_nsearch`
    - Predicted Functions (0):

- **File:** `src/net/cgo_unix_cgo_resn.go`
    - Ground Truth Functions (3):
        - `_C_res_nclose`
        - `_C_res_ninit`
        - `_C_res_nsearch`
    - Predicted Functions (0):

- **File:** `src/net/cgo_unix_syscall.go`
    - Ground Truth Functions (3):
        - `_C_res_nclose`
        - `_C_res_ninit`
        - `_C_res_nsearch`
    - Predicted Functions (0):

- **File:** `src/net/conf.go`
    - Ground Truth Functions (1):
        - `initConfVal`
    - Predicted Functions (0):

- **File:** `src/net/dnsclient.go`
    - Ground Truth Functions (1):
        - `equalASCIIName`
    - Predicted Functions (0):

- **File:** `src/net/dnsclient_unix.go`
    - Ground Truth Functions (6):
        - `checkResponse`
        - `goLookupCNAME`
        - `goLookupIPCNAMEOrder`
        - `goLookupPTR`
        - `lookup`
        - `tryOneName`
    - Predicted Functions (0):

- **File:** `src/net/dnsclient_unix_test.go`
    - Ground Truth Functions (2):
        - `TestLongDNSNames`
        - `TestStrictErrorsLookupTXT`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `Handle`
        - ❌ `HandleFunc`
        - ❌ `ListenAndServe`
        - ❌ `ListenAndServeTLS`
        - ❌ `NewServeMux`
        - ❌ `Redirect`
        - ❌ `Serve`
        - ❌ `ServeHTTP`
        - ❌ `ServeTLS`
        - ❌ `StripPrefix`

- **File:** `src/net/lookup.go`
    - Ground Truth Functions (5):
        - `goLookupMX`
        - `goLookupNS`
        - `goLookupSRV`
        - `goLookupTXT`
        - `parseCNAMEFromResources`
    - Predicted Functions (1):
        - ❌ `LookupCNAME`

- **File:** `src/net/lookup_plan9.go`
    - Ground Truth Functions (1):
        - `lookupCNAME`
    - Predicted Functions (0):

- **File:** `src/net/lookup_unix.go`
    - Ground Truth Functions (1):
        - `lookupCNAME`
    - Predicted Functions (1):
        - ✅ `lookupCNAME`

- **File:** `src/net/lookup_windows.go`
    - Ground Truth Functions (1):
        - `lookupCNAME`
    - Predicted Functions (2):
        - ✅ `lookupCNAME`
        - ❌ `resolveCNAME`


### 📊 **Proposal #41184 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 65.0% | 3.6% | 6.8% | 13/364 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/asm/internal/asm/endtoend_test.go`
    - Ground Truth Functions (2):
        - `TestGoBuildErrors`
        - `testErrors`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/asm/parse.go`
    - Ground Truth Functions (2):
        - `line`
        - `nextToken`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/lex/input.go`
    - Ground Truth Functions (1):
        - `Next`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/lex/lex_test.go`
    - Ground Truth Functions (1):
        - `drain`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/lex/tokenizer.go`
    - Ground Truth Functions (1):
        - `Next`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/buildtag.go`
    - Ground Truth Functions (2):
        - `buildtag`
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/buildtag_test.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/fix.go`
    - Ground Truth Functions (1):
        - `walkBeforeAfter`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/main_test.go`
    - Ground Truth Functions (1):
        - `TestRewrite`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/fix/fix.go`
    - Ground Truth Functions (2):
        - `init`
        - `runFix`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/pkg.go`
    - Ground Truth Functions (2):
        - `AllFiles`
        - `copyBuild`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (1):
        - `buildVetConfig`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
    - Ground Truth Functions (138):
        - `Access`
        - `Adjtime`
        - `Chdir`
        - `Chflags`
        - `Chmod`
        - `Chown`
        - `Chroot`
        - `ClockGettime`
        - `Clonefile`
        - `Clonefileat`
        - `Close`
        - `Dup`
        - `Dup2`
        - `Exchangedata`
        - `Exit`
        - `Faccessat`
        - `Fchdir`
        - `Fchflags`
        - `Fchmod`
        - `Fchmodat`
        - `Fchown`
        - `Fchownat`
        - `Fclonefileat`
        - `Flock`
        - `Fpathconf`
        - `Fstat`
        - `Fstatat`
        - `Fstatfs`
        - `Fsync`
        - `Ftruncate`
        - `Getcwd`
        - `Getdtablesize`
        - `Getegid`
        - `Geteuid`
        - `Getgid`
        - `Getpgid`
        - `Getpgrp`
        - `Getpid`
        - `Getppid`
        - `Getpriority`
        - `Getrlimit`
        - `Getrusage`
        - `Getsid`
        - `Gettimeofday`
        - `Getuid`
        - `Issetugid`
        - `Kqueue`
        - `Lchown`
        - `Link`
        - `Linkat`
        - `Listen`
        - `Lstat`
        - `Madvise`
        - `Mkdir`
        - `Mkdirat`
        - `Mkfifo`
        - `Mknod`
        - `Mlock`
        - `Mlockall`
        - `Mprotect`
        - `Msync`
        - `Munlock`
        - `Munlockall`
        - `Open`
        - `Openat`
        - `Pathconf`
        - `Readlink`
        - `Readlinkat`
        - `Rename`
        - `Renameat`
        - `Revoke`
        - `Rmdir`
        - `Seek`
        - `Select`
        - `Setegid`
        - `Seteuid`
        - `Setgid`
        - `Setlogin`
        - `Setpgid`
        - `Setpriority`
        - `Setprivexec`
        - `Setregid`
        - `Setreuid`
        - `Setsid`
        - `Settimeofday`
        - `Setuid`
        - `Shutdown`
        - `Stat`
        - `Statfs`
        - `Symlink`
        - `Symlinkat`
        - `Sync`
        - `Truncate`
        - `Umask`
        - `Undelete`
        - `Unlink`
        - `Unlinkat`
        - `Unmount`
        - `accept`
        - `bind`
        - `connect`
        - `fcntl`
        - `fgetxattr`
        - `flistxattr`
        - `fremovexattr`
        - `fsetxattr`
        - `futimes`
        - `getfsstat`
        - `getgroups`
        - `getpeername`
        - `getsockname`
        - `getsockopt`
        - `getxattr`
        - `ioctl`
        - `kevent`
        - `kill`
        - `listxattr`
        - `mmap`
        - `munmap`
        - `pipe`
        - `poll`
        - `ptrace1`
        - `read`
        - `recvfrom`
        - `recvmsg`
        - `removexattr`
        - `sendfile`
        - `sendmsg`
        - `sendto`
        - `setgroups`
        - `setsockopt`
        - `setxattr`
        - `socket`
        - `socketpair`
        - `sysctl`
        - `utimes`
        - `wait4`
        - `write`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
    - Ground Truth Functions (138):
        - `Access`
        - `Adjtime`
        - `Chdir`
        - `Chflags`
        - `Chmod`
        - `Chown`
        - `Chroot`
        - `ClockGettime`
        - `Clonefile`
        - `Clonefileat`
        - `Close`
        - `Dup`
        - `Dup2`
        - `Exchangedata`
        - `Exit`
        - `Faccessat`
        - `Fchdir`
        - `Fchflags`
        - `Fchmod`
        - `Fchmodat`
        - `Fchown`
        - `Fchownat`
        - `Fclonefileat`
        - `Flock`
        - `Fpathconf`
        - `Fstat`
        - `Fstatat`
        - `Fstatfs`
        - `Fsync`
        - `Ftruncate`
        - `Getcwd`
        - `Getdtablesize`
        - `Getegid`
        - `Geteuid`
        - `Getgid`
        - `Getpgid`
        - `Getpgrp`
        - `Getpid`
        - `Getppid`
        - `Getpriority`
        - `Getrlimit`
        - `Getrusage`
        - `Getsid`
        - `Gettimeofday`
        - `Getuid`
        - `Issetugid`
        - `Kqueue`
        - `Lchown`
        - `Link`
        - `Linkat`
        - `Listen`
        - `Lstat`
        - `Madvise`
        - `Mkdir`
        - `Mkdirat`
        - `Mkfifo`
        - `Mknod`
        - `Mlock`
        - `Mlockall`
        - `Mprotect`
        - `Msync`
        - `Munlock`
        - `Munlockall`
        - `Open`
        - `Openat`
        - `Pathconf`
        - `Readlink`
        - `Readlinkat`
        - `Rename`
        - `Renameat`
        - `Revoke`
        - `Rmdir`
        - `Seek`
        - `Select`
        - `Setegid`
        - `Seteuid`
        - `Setgid`
        - `Setlogin`
        - `Setpgid`
        - `Setpriority`
        - `Setprivexec`
        - `Setregid`
        - `Setreuid`
        - `Setsid`
        - `Settimeofday`
        - `Setuid`
        - `Shutdown`
        - `Stat`
        - `Statfs`
        - `Symlink`
        - `Symlinkat`
        - `Sync`
        - `Truncate`
        - `Umask`
        - `Undelete`
        - `Unlink`
        - `Unlinkat`
        - `Unmount`
        - `accept`
        - `bind`
        - `connect`
        - `fcntl`
        - `fgetxattr`
        - `flistxattr`
        - `fremovexattr`
        - `fsetxattr`
        - `futimes`
        - `getfsstat`
        - `getgroups`
        - `getpeername`
        - `getsockname`
        - `getsockopt`
        - `getxattr`
        - `ioctl`
        - `kevent`
        - `kill`
        - `listxattr`
        - `mmap`
        - `munmap`
        - `pipe`
        - `poll`
        - `ptrace1`
        - `read`
        - `recvfrom`
        - `recvmsg`
        - `removexattr`
        - `sendfile`
        - `sendmsg`
        - `sendto`
        - `setgroups`
        - `setsockopt`
        - `setxattr`
        - `socket`
        - `socketpair`
        - `sysctl`
        - `utimes`
        - `wait4`
        - `write`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`
    - Ground Truth Functions (9):
        - `checkGoFile`
        - `checkOtherFile`
        - `comment`
        - `file`
        - `finish`
        - `goBuildLine`
        - `init`
        - `plusBuildLine`
        - `runBuildTag`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/loopclosure/loopclosure.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/unitchecker/unitchecker.go`
    - Ground Truth Functions (2):
        - `Main`
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (1):
        - `wantedErrors`
    - Predicted Functions (0):

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (10):
        - `ImportDir`
        - `eval`
        - `goodOSArchFile`
        - `isGoBuildComment`
        - `matchAuto`
        - `matchFile`
        - `matchTag`
        - `parseFileHeader`
        - `saveCgo`
        - `shouldBuild`
    - Predicted Functions (3):
        - ✅ `isGoBuildComment`
        - ✅ `matchTag`
        - ✅ `shouldBuild`

- **File:** `src/go/build/build_test.go`
    - Ground Truth Functions (2):
        - `TestMatch`
        - `TestShouldBuild`
    - Predicted Functions (3):
        - ❌ `TestAllTags`
        - ❌ `TestDirectives`
        - ✅ `TestShouldBuild`

- **File:** `src/go/build/constraint/expr.go`
    - Ground Truth Functions (22):
        - `Error`
        - `Eval`
        - `IsGoBuild`
        - `IsPlusBuild`
        - `Parse`
        - `PlusBuildLines`
        - `String`
        - `and`
        - `andArg`
        - `appendSplitAnd`
        - `appendSplitOr`
        - `atom`
        - `isValidTag`
        - `lex`
        - `not`
        - `or`
        - `orArg`
        - `parseExpr`
        - `parsePlusBuildExpr`
        - `pushNot`
        - `splitGoBuild`
        - `splitPlusBuild`
    - Predicted Functions (7):
        - ✅ `IsGoBuild`
        - ✅ `Parse`
        - ✅ `PlusBuildLines`
        - ✅ `isValidTag`
        - ✅ `parseExpr`
        - ✅ `parsePlusBuildExpr`
        - ✅ `splitGoBuild`

- **File:** `src/go/build/constraint/expr_test.go`
    - Ground Truth Functions (9):
        - `TestExprEval`
        - `TestExprString`
        - `TestLex`
        - `TestParse`
        - `TestParseError`
        - `TestParseExpr`
        - `TestParsePlusBuildExpr`
        - `TestPlusBuildLines`
        - `lexHelp`
    - Predicted Functions (2):
        - ✅ `TestParsePlusBuildExpr`
        - ✅ `TestPlusBuildLines`

- **File:** `src/go/build/constraint/vers.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `GoVersion`
        - ❌ `andVersion`
        - ❌ `minVersion`
        - ❌ `orVersion`

- **File:** `src/go/build/constraint/vers_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestGoVersion`

- **File:** `src/go/printer/gobuild.go`
    - Ground Truth Functions (5):
        - `appendLines`
        - `commentTextAt`
        - `fixGoBuildLines`
        - `isNL`
        - `lineAt`
    - Predicted Functions (0):

- **File:** `src/go/printer/printer.go`
    - Ground Truth Functions (3):
        - `fprint`
        - `printNode`
        - `writeComment`
    - Predicted Functions (0):

- **File:** `src/runtime/auxv_none.go`
    - Ground Truth Functions (1):
        - `sysargs`
    - Predicted Functions (0):

- **File:** `src/runtime/mkduff.go`
    - Ground Truth Functions (2):
        - `tagsMIPS64x`
        - `tagsPPC64x`
    - Predicted Functions (0):

- **File:** `src/runtime/mkpreempt.go`
    - Ground Truth Functions (1):
        - `header`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/mprof_test.go`
    - Ground Truth Functions (1):
        - `TestMemoryProfiler`
    - Predicted Functions (0):

- **File:** `src/runtime/wincallback.go`
    - Ground Truth Functions (1):
        - `genasm386Amd64`
    - Predicted Functions (0):


### 📊 **Proposal #46121 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 100.0% | 20.0% | 1/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/html/template/template.go`
    - Ground Truth Functions (1):
        - `Funcs`
    - Predicted Functions (1):
        - ✅ `Funcs`

- **File:** `src/html/template/template_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/text/template/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `DefinedTemplates`
        - ❌ `Execute`
        - ❌ `ExecuteTemplate`
        - ❌ `execute`

- **File:** `src/text/template/funcs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `addFuncs`
        - ❌ `builtinFuncs`
        - ❌ `builtins`

- **File:** `src/text/template/template.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Funcs`


### 📊 **Proposal #49580 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.0% | 12.0% | 17.1% | 3/25 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/writer.go`
    - Ground Truth Functions (1):
        - `AddFS`
    - Predicted Functions (0):

- **File:** `src/archive/tar/writer_test.go`
    - Ground Truth Functions (1):
        - `TestWriterAddFS`
    - Predicted Functions (0):

- **File:** `src/archive/zip/reader.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `(*File) Open`
        - ❌ `(*File) OpenRaw`
        - ❌ `(*Reader) Open`
        - ❌ `NewReader`
        - ❌ `OpenReader`

- **File:** `src/archive/zip/writer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `AddFS`

- **File:** `src/archive/zip/zip_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/io/fs/readlink.go`
    - Ground Truth Functions (2):
        - `Lstat`
        - `ReadLink`
    - Predicted Functions (1):
        - ✅ `ReadLink`

- **File:** `src/io/fs/readlink_test.go`
    - Ground Truth Functions (2):
        - `TestLstat`
        - `TestReadLink`
    - Predicted Functions (2):
        - ✅ `TestLstat`
        - ✅ `TestReadLink`

- **File:** `src/io/fs/sub.go`
    - Ground Truth Functions (2):
        - `Lstat`
        - `ReadLink`
    - Predicted Functions (0):

- **File:** `src/io/fs/walk_test.go`
    - Ground Truth Functions (1):
        - `TestWalkDirSymlink`
    - Predicted Functions (0):

- **File:** `src/os/dir.go`
    - Ground Truth Functions (1):
        - `CopyFS`
    - Predicted Functions (0):

- **File:** `src/os/file.go`
    - Ground Truth Functions (2):
        - `Lstat`
        - `ReadLink`
    - Predicted Functions (0):

- **File:** `src/os/file_test.go`
    - Ground Truth Functions (3):
        - `TestDirFSLstat`
        - `TestDirFSReadLink`
        - `TestDirFSWalkDir`
    - Predicted Functions (0):

- **File:** `src/os/os_test.go`
    - Ground Truth Functions (1):
        - `TestCopyFSWithSymlinks`
    - Predicted Functions (0):

- **File:** `src/path/filepath/symlink.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `walkSymlinks`

- **File:** `src/testing/fstest/mapfs.go`
    - Ground Truth Functions (5):
        - `Lstat`
        - `Open`
        - `ReadLink`
        - `lstat`
        - `resolveSymlinks`
    - Predicted Functions (0):

- **File:** `src/testing/fstest/mapfs_test.go`
    - Ground Truth Functions (1):
        - `TestMapFSSymlink`
    - Predicted Functions (0):

- **File:** `src/testing/fstest/testfs.go`
    - Ground Truth Functions (2):
        - `checkDir`
        - `checkStat`
    - Predicted Functions (0):

- **File:** `src/testing/fstest/testfs_test.go`
    - Ground Truth Functions (1):
        - `TestSymlink`
    - Predicted Functions (0):


### 📊 **Proposal #50429 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/go/ast/ast.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `End`
        - ❌ `Pos`
        - ❌ `RangeStmt`

- **File:** `src/go/ast/ast_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/parser/parser.go`
    - Ground Truth Functions (1):
        - `parseForStmt`
    - Predicted Functions (0):

- **File:** `src/go/parser/parser_test.go`
    - Ground Truth Functions (1):
        - `TestRangePos`
    - Predicted Functions (0):


### 📊 **Proposal #44196 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 2/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `lib/time/mkzip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/time/time.go`
    - Ground Truth Functions (2):
        - `UnixMicro`
        - `UnixMilli`
    - Predicted Functions (4):
        - ❌ `Unix`
        - ✅ `UnixMicro`
        - ✅ `UnixMilli`
        - ❌ `UnixNano`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (4):
        - `BenchmarkNowUnixMicro`
        - `BenchmarkNowUnixMilli`
        - `TestUnixMicro`
        - `TestUnixMilli`
    - Predicted Functions (0):


### 📊 **Proposal #37196 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 4.0% | 5.6% | 1/25 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/ssagen/ssa.go`
    - Ground Truth Functions (1):
        - `referenceTypeBuiltin`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/_builtin/runtime.go`
    - Ground Truth Functions (1):
        - `chancap`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/builtin.go`
    - Ground Truth Functions (3):
        - `isByteCount`
        - `isChanLenCap`
        - `walkLenCap`
    - Predicted Functions (0):

- **File:** `src/runtime/chan.go`
    - Ground Truth Functions (5):
        - `chancap`
        - `chanlen`
        - `reflect_chancap`
        - `reflectlite_chanlen`
        - `timerchandrain`
    - Predicted Functions (0):

- **File:** `src/runtime/time.go`
    - Ground Truth Functions (9):
        - `addHeap`
        - `hchan`
        - `maybeRunAsync`
        - `modify`
        - `newTimer`
        - `stop`
        - `trace`
        - `trace1`
        - `unlockAndRun`
    - Predicted Functions (0):

- **File:** `src/time/sleep.go`
    - Ground Truth Functions (2):
        - `NewTimer`
        - `syncTimer`
    - Predicted Functions (4):
        - ✅ `NewTimer`
        - ❌ `Reset`
        - ❌ `Stop`
        - ❌ `sendTime`

- **File:** `src/time/tick.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `NewTicker`
        - ❌ `Reset`
        - ❌ `Stop`

- **File:** `src/time/tick_test.go`
    - Ground Truth Functions (4):
        - `Reset`
        - `Stop`
        - `TestChan`
        - `testTimerChan`
    - Predicted Functions (0):

- **File:** `src/time/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `NewTimer`
        - ❌ `Reset`
        - ❌ `Stop`
        - ❌ `Ticker`


### 📊 **Proposal #45454 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/cfg/cfg.go`
    - Ground Truth Functions (2):
        - `defaultContext`
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/flag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Flagparse`
        - ❌ `expandArgs`

- **File:** `src/cmd/internal/objabi/flag_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/util.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/elf.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `goarch`

- **File:** `src/cmd/internal/objfile/goobj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `goarch`
        - ❌ `loadAddress`

- **File:** `src/cmd/internal/objfile/macho.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `goarch`

- **File:** `src/cmd/internal/objfile/pe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `goarch`

- **File:** `src/cmd/internal/objfile/xcoff.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `goarch`

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (1):
        - `defaultContext`
    - Predicted Functions (3):
        - ❌ `goodOSArchFile`
        - ❌ `matchTag`
        - ❌ `shouldBuild`

- **File:** `src/go/build/build_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestAllTags`
        - ❌ `TestDirectives`

- **File:** `src/internal/buildcfg/cfg.go`
    - Ground Truth Functions (3):
        - `experimentTags`
        - `gogoarchTags`
        - `toolTags`
    - Predicted Functions (0):

- **File:** `src/runtime/defs_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/defs_linux_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/defs_linux_arm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/defs_linux_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/defs_linux_ppc64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/defs_linux_ppc64le.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/defs_linux_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/defs_linux_s390x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #41790 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 33.3% | 25.0% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/database/sql/driver/driver.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/database/sql/fakedb_test.go`
    - Ground Truth Functions (1):
        - `Close`
    - Predicted Functions (0):

- **File:** `src/database/sql/sql.go`
    - Ground Truth Functions (1):
        - `Close`
    - Predicted Functions (5):
        - ✅ `Close`
        - ❌ `Conn`
        - ❌ `Driver`
        - ❌ `closeDBLocked`
        - ❌ `finalClose`

- **File:** `src/database/sql/sql_test.go`
    - Ground Truth Functions (1):
        - `TestOpenConnector`
    - Predicted Functions (0):


### 📊 **Proposal #47164 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 38.9% | 87.5% | 53.8% | 7/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/log/log.go`
    - Ground Truth Functions (7):
        - `New`
        - `Output`
        - `Prefix`
        - `Print`
        - `Printf`
        - `Println`
        - `SetOutput`
    - Predicted Functions (16):
        - ❌ `Fatal`
        - ❌ `Fatalf`
        - ❌ `Fatalln`
        - ❌ `Flags`
        - ✅ `Output`
        - ❌ `Panic`
        - ❌ `Panicf`
        - ❌ `Panicln`
        - ✅ `Prefix`
        - ✅ `Print`
        - ✅ `Printf`
        - ✅ `Println`
        - ❌ `SetFlags`
        - ✅ `SetOutput`
        - ❌ `SetPrefix`
        - ❌ `Writer`

- **File:** `src/log/log_test.go`
    - Ground Truth Functions (1):
        - `TestDiscard`
    - Predicted Functions (2):
        - ❌ `BenchmarkDiscard`
        - ✅ `TestDiscard`


### 📊 **Proposal #45100 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 100.0% | 36.4% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/url/url.go`
    - Ground Truth Functions (1):
        - `Has`
    - Predicted Functions (7):
        - ❌ `Add`
        - ❌ `Del`
        - ❌ `Encode`
        - ❌ `Get`
        - ✅ `Has`
        - ❌ `ParseQuery`
        - ❌ `Set`

- **File:** `src/net/url/url_test.go`
    - Ground Truth Functions (1):
        - `TestQueryValues`
    - Predicted Functions (2):
        - ❌ `TestParseQuery`
        - ✅ `TestQueryValues`


### 📊 **Proposal #43744 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 11.1% | 13.3% | 1/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/proc.go`
    - Ground Truth Functions (4):
        - `handoffp`
        - `procresize`
        - `sysmon`
        - `wakeNetPoller`
    - Predicted Functions (0):

- **File:** `src/testing/benchmark.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Benchmark`
        - ❌ `ReportMetric`
        - ❌ `Run`

- **File:** `src/testing/benchmark_test.go`
    - Ground Truth Functions (1):
        - `ExampleB_ReportMetric`
    - Predicted Functions (3):
        - ✅ `ExampleB_ReportMetric`
        - ❌ `ExampleB_ReportMetric_parallel`
        - ❌ `TestReportMetric`

- **File:** `src/time/sleep_test.go`
    - Ground Truth Functions (4):
        - `BenchmarkParallelTimerLatency`
        - `BenchmarkStaggeredTickerLatency`
        - `doWork`
        - `warmupScheduler`
    - Predicted Functions (0):


### 📊 **Proposal #53466 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.7% | 5.7% | 7.7% | 7/123 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `extLink`
    - Predicted Functions (0):

- **File:** `src/cmd/link/elf_test.go`
    - Ground Truth Functions (1):
        - `TestMinusRSymsWithSameName`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/lib.go`
    - Ground Truth Functions (1):
        - `extld`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/riscv64/obj.go`
    - Ground Truth Functions (2):
        - `Init`
        - `archinit`
    - Predicted Functions (0):

- **File:** `src/cmd/link/link_test.go`
    - Ground Truth Functions (1):
        - `TestIssue33979`
    - Predicted Functions (0):

- **File:** `src/internal/cpu/cpu_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `doinit`
        - ❌ `isSet`

- **File:** `src/internal/goos/goos.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `GetSupportedArch`
        - ❌ `GetSupportedOS`
        - ❌ `IsSupportedArch`
        - ❌ `IsSupportedOS`
        - ❌ `funcLiteral`

- **File:** `src/internal/goos/zgoos_freebsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `FreeBSD`
        - ❌ `GetSyscall`
        - ❌ `Init`
        - ❌ `SetSyscall`
        - ❌ `funcLiteral`

- **File:** `src/runtime/defs_freebsd_riscv64.go`
    - Ground Truth Functions (2):
        - `setNsec`
        - `set_usec`
    - Predicted Functions (2):
        - ✅ `setNsec`
        - ✅ `set_usec`

- **File:** `src/runtime/signal_freebsd_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (41):
        - ❌ `a0`
        - ❌ `a1`
        - ❌ `a2`
        - ❌ `a3`
        - ❌ `a4`
        - ❌ `a5`
        - ❌ `a6`
        - ❌ `a7`
        - ❌ `gp`
        - ❌ `pc`
        - ❌ `ra`
        - ❌ `regs`
        - ❌ `s0`
        - ❌ `s1`
        - ❌ `s10`
        - ❌ `s11`
        - ❌ `s2`
        - ❌ `s3`
        - ❌ `s4`
        - ❌ `s5`
        - ❌ `s6`
        - ❌ `s7`
        - ❌ `s8`
        - ❌ `s9`
        - ❌ `set_gp`
        - ❌ `set_pc`
        - ❌ `set_ra`
        - ❌ `set_sigaddr`
        - ❌ `set_sigcode`
        - ❌ `set_sp`
        - ❌ `sigaddr`
        - ❌ `sigcode`
        - ❌ `sp`
        - ❌ `t0`
        - ❌ `t1`
        - ❌ `t2`
        - ❌ `t3`
        - ❌ `t4`
        - ❌ `t5`
        - ❌ `t6`
        - ❌ `tp`

- **File:** `src/runtime/vdso_freebsd_riscv64.go`
    - Ground Truth Functions (1):
        - `getTimecounter`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_freebsd_riscv64.go`
    - Ground Truth Functions (7):
        - `SetControllen`
        - `SetKevent`
        - `SetLen`
        - `Syscall9`
        - `sendfile`
        - `setTimespec`
        - `setTimeval`
    - Predicted Functions (5):
        - ✅ `SetKevent`
        - ✅ `Syscall9`
        - ✅ `sendfile`
        - ✅ `setTimespec`
        - ✅ `setTimeval`

- **File:** `src/syscall/zsyscall_freebsd_riscv64.go`
    - Ground Truth Functions (106):
        - `Access`
        - `Adjtime`
        - `Chdir`
        - `Chflags`
        - `Chmod`
        - `Chown`
        - `Chroot`
        - `Close`
        - `Dup`
        - `Dup2`
        - `Fchdir`
        - `Fchflags`
        - `Fchmod`
        - `Fchown`
        - `Flock`
        - `Fpathconf`
        - `Fstat`
        - `Fstatat`
        - `Fstatfs`
        - `Fsync`
        - `Ftruncate`
        - `Getdtablesize`
        - `Getegid`
        - `Geteuid`
        - `Getgid`
        - `Getpgid`
        - `Getpgrp`
        - `Getpid`
        - `Getppid`
        - `Getpriority`
        - `Getrlimit`
        - `Getrusage`
        - `Getsid`
        - `Gettimeofday`
        - `Getuid`
        - `Issetugid`
        - `Kill`
        - `Kqueue`
        - `Lchown`
        - `Link`
        - `Listen`
        - `Mkdir`
        - `Mkfifo`
        - `Nanosleep`
        - `Open`
        - `Pathconf`
        - `Readlink`
        - `Rename`
        - `Revoke`
        - `Rmdir`
        - `Seek`
        - `Select`
        - `Setegid`
        - `Seteuid`
        - `Setgid`
        - `Setlogin`
        - `Setpgid`
        - `Setpriority`
        - `Setregid`
        - `Setreuid`
        - `Setsid`
        - `Settimeofday`
        - `Setuid`
        - `Shutdown`
        - `Statfs`
        - `Symlink`
        - `Sync`
        - `Truncate`
        - `Umask`
        - `Undelete`
        - `Unlink`
        - `Unmount`
        - `accept`
        - `accept4`
        - `bind`
        - `connect`
        - `fcntl`
        - `futimes`
        - `getcwd`
        - `getdirentries`
        - `getgroups`
        - `getpeername`
        - `getsockname`
        - `getsockopt`
        - `kevent`
        - `mknodat`
        - `mmap`
        - `munmap`
        - `pipe2`
        - `pread`
        - `pwrite`
        - `read`
        - `readlen`
        - `recvfrom`
        - `recvmsg`
        - `sendmsg`
        - `sendto`
        - `setgroups`
        - `setsockopt`
        - `socket`
        - `socketpair`
        - `sysctl`
        - `utimensat`
        - `utimes`
        - `wait4`
        - `write`
    - Predicted Functions (0):


### 📊 **Proposal #51430 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.9% | 2.5% | 4.1% | 4/163 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/base/flag.go`
    - Ground Truth Functions (2):
        - `ParseFlags`
        - `readCoverageCfg`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/coverage/cover.go`
    - Ground Truth Functions (4):
        - `Fixup`
        - `addInitHookCall`
        - `metaHashAndLen`
        - `registerMeta`
    - Predicted Functions (4):
        - ✅ `Fixup`
        - ✅ `addInitHookCall`
        - ✅ `metaHashAndLen`
        - ✅ `registerMeta`

- **File:** `src/cmd/compile/internal/gc/main.go`
    - Ground Truth Functions (1):
        - `Main`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/builtin.go`
    - Ground Truth Functions (4):
        - `coverageTypes`
        - `newSig`
        - `params`
        - `runtimeTypes`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/mkbuiltin.go`
    - Ground Truth Functions (2):
        - `main`
        - `mkbuiltin`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/syms.go`
    - Ground Truth Functions (2):
        - `InitCoverage`
        - `LookupCoverage`
    - Predicted Functions (0):

- **File:** `src/cmd/covdata/argsmerge.go`
    - Ground Truth Functions (2):
        - `ArgsSummary`
        - `Merge`
    - Predicted Functions (0):

- **File:** `src/cmd/covdata/covdata.go`
    - Ground Truth Functions (7):
        - `Exit`
        - `atExit`
        - `dbgtrace`
        - `fatal`
        - `main`
        - `usage`
        - `warn`
    - Predicted Functions (0):

- **File:** `src/cmd/covdata/dump.go`
    - Ground Truth Functions (11):
        - `BeginCounterDataFile`
        - `BeginPackage`
        - `BeginPod`
        - `EndPod`
        - `Finish`
        - `Setup`
        - `Usage`
        - `VisitFunc`
        - `VisitFuncCounterData`
        - `VisitMetaDataFile`
        - `makeDumpOp`
    - Predicted Functions (0):

- **File:** `src/cmd/covdata/merge.go`
    - Ground Truth Functions (11):
        - `BeginCounterDataFile`
        - `BeginPackage`
        - `BeginPod`
        - `EndPod`
        - `Finish`
        - `Setup`
        - `Usage`
        - `VisitFunc`
        - `VisitFuncCounterData`
        - `VisitMetaDataFile`
        - `makeMergeOp`
    - Predicted Functions (0):

- **File:** `src/cmd/covdata/metamerge.go`
    - Ground Truth Functions (12):
        - `VisitFuncs`
        - `beginCounterDataFile`
        - `beginPod`
        - `copyMetaDataFile`
        - `emitCounters`
        - `emitMeta`
        - `endPod`
        - `newMetaMerge`
        - `visitFunc`
        - `visitFuncCounterData`
        - `visitMetaDataFile`
        - `visitPackage`
    - Predicted Functions (0):

- **File:** `src/cmd/covdata/subtractintersect.go`
    - Ground Truth Functions (12):
        - `BeginCounterDataFile`
        - `BeginPackage`
        - `BeginPod`
        - `EndCounters`
        - `EndPod`
        - `Setup`
        - `Usage`
        - `VisitFunc`
        - `VisitFuncCounterData`
        - `VisitMetaDataFile`
        - `makeSubtractIntersectOp`
        - `pruneCounters`
    - Predicted Functions (0):

- **File:** `src/cmd/covdata/testdata/dep.go`
    - Ground Truth Functions (2):
        - `Dep1`
        - `PDep`
    - Predicted Functions (0):

- **File:** `src/cmd/covdata/testdata/prog1.go`
    - Ground Truth Functions (5):
        - `first`
        - `fourth`
        - `main`
        - `second`
        - `third`
    - Predicted Functions (0):

- **File:** `src/cmd/covdata/testdata/prog2.go`
    - Ground Truth Functions (3):
        - `fifth`
        - `main`
        - `sixth`
    - Predicted Functions (0):

- **File:** `src/cmd/covdata/tool_test.go`
    - Ground Truth Functions (19):
        - `TestCovTool`
        - `buildProg`
        - `dumplines`
        - `emitFile`
        - `gobuild`
        - `runDumpChecks`
        - `runToolOp`
        - `testCommandLineErrors`
        - `testCounterClash`
        - `testDump`
        - `testEmpty`
        - `testIntersect`
        - `testMergeCombinePrograms`
        - `testMergeSelect`
        - `testMergeSimple`
        - `testPercent`
        - `testPkgList`
        - `testSubtract`
        - `testTextfmt`
    - Predicted Functions (0):

- **File:** `src/cmd/cover/cover.go`
    - Ground Truth Functions (0):
    - Predicted Functions (12):
        - ❌ `addCounters`
        - ❌ `annotate`
        - ❌ `atomicCounterStmt`
        - ❌ `emitMetaData`
        - ❌ `emitMetaFile`
        - ❌ `incCounterStmt`
        - ❌ `main`
        - ❌ `newCounter`
        - ❌ `parseFlags`
        - ❌ `readOutFileList`
        - ❌ `readPackageConfig`
        - ❌ `setCounterStmt`

- **File:** `src/cmd/cover/cover_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestCover`
        - ❌ `TestCoverFunc`
        - ❌ `TestCoverWithToolExec`
        - ❌ `TestDirectives`

- **File:** `src/cmd/cover/testdata/html/html.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/cover/testdata/html/html_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestAll`

- **File:** `src/cmd/cover/testdata/pkgcfg/a/a.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `A`
        - ❌ `Get`
        - ❌ `Set`

- **File:** `src/cmd/cover/testdata/pkgcfg/a/a_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestA`

- **File:** `src/cmd/cover/testdata/pkgcfg/noFuncsNoTests/nfnt.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/cover/testdata/pkgcfg/yesFuncsNoTests/yfnt.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/cov/mreader.go`
    - Ground Truth Functions (4):
        - `NewMreader`
        - `Read`
        - `ReadByte`
        - `Seek`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/cov/readcovdata.go`
    - Ground Truth Functions (7):
        - `MakeCovDataReader`
        - `Visit`
        - `fatal`
        - `processPackage`
        - `verb`
        - `visitPod`
        - `warn`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/calloc/batchcounteralloc.go`
    - Ground Truth Functions (1):
        - `AllocateCounters`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/cformat/fmt_test.go`
    - Ground Truth Functions (1):
        - `TestBasics`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/cformat/format.go`
    - Ground Truth Functions (7):
        - `AddUnit`
        - `EmitFuncs`
        - `EmitPercent`
        - `EmitTextual`
        - `NewFormatter`
        - `SetPackage`
        - `sortUnits`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/cmerge/merge.go`
    - Ground Truth Functions (6):
        - `Granularity`
        - `MergeCounters`
        - `Mode`
        - `ResetModeAndGranularity`
        - `SaturatingAdd`
        - `SetModeAndGranularity`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/cmerge/merge_test.go`
    - Ground Truth Functions (2):
        - `TestBasic`
        - `TestClash`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/decodecounter/decodecounterfile.go`
    - Ground Truth Functions (13):
        - `BeginNextSegment`
        - `Goarch`
        - `Goos`
        - `NewCounterDataReader`
        - `NextFunc`
        - `NumFunctionsInSegment`
        - `NumSegments`
        - `OsArgs`
        - `checkMagic`
        - `readArgs`
        - `readFooter`
        - `readSegmentPreamble`
        - `readStringTable`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/encodecounter/encode.go`
    - Ground Truth Functions (9):
        - `AppendSegment`
        - `NewCoverageDataWriter`
        - `Write`
        - `padToFourByteBoundary`
        - `writeBytes`
        - `writeCounters`
        - `writeFooter`
        - `writeHeader`
        - `writeSegmentPreamble`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/pods/pods.go`
    - Ground Truth Functions (4):
        - `CollectPods`
        - `CollectPodsFromFiles`
        - `collectPodsImpl`
        - `warning`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/pods/pods_test.go`
    - Ground Truth Functions (1):
        - `TestPodCollection`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/stringtab/stringtab.go`
    - Ground Truth Functions (5):
        - `Entries`
        - `Freeze`
        - `Get`
        - `Lookup`
        - `NewReader`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/test/counter_test.go`
    - Ground Truth Functions (4):
        - `TestCounterDataAppendSegment`
        - `TestCounterDataWriterReader`
        - `VisitFuncs`
        - `mkfunc`
    - Predicted Functions (0):

- **File:** `src/runtime/coverage/coverage.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `ClearCounters`
        - ❌ `WriteCounters`
        - ❌ `WriteCountersDir`
        - ❌ `WriteMeta`
        - ❌ `WriteMetaDir`

- **File:** `src/testing/cover.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `RegisterCover`


### 📊 **Proposal #44853 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 19.5% | 14.3% | 16.5% | 8/56 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/base/flag.go`
    - Ground Truth Functions (1):
        - `ParseFlags`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/gc/main.go`
    - Ground Truth Functions (1):
        - `Main`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/gc/obj.go`
    - Ground Truth Functions (1):
        - `ggloblnod`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/import.go`
    - Ground Truth Functions (1):
        - `openPackage`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/reader.go`
    - Ground Truth Functions (1):
        - `objIdx`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/pkginit/initAsanGlobals.go`
    - Ground Truth Functions (4):
        - `GetRedzoneSizeForGlobal`
        - `canInstrumentGlobal`
        - `createtypes`
        - `instrumentGlobals`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/reflectdata/reflect.go`
    - Ground Truth Functions (1):
        - `WriteBasicTypes`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssagen/ssa.go`
    - Ground Truth Functions (4):
        - `InitConfig`
        - `exprCheckPtr`
        - `instrument2`
        - `instrumentFields`
    - Predicted Functions (0):

- **File:** `src/cmd/go/go_test.go`
    - Ground Truth Functions (1):
        - `TestMain`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/pkg.go`
    - Ground Truth Functions (1):
        - `LinkerDeps`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (1):
        - `AddBuildFlags`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (1):
        - `cgo`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/init.go`
    - Ground Truth Functions (2):
        - `compilerRequiredAsanVersion`
        - `instrumentInit`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/config.go`
    - Ground Truth Functions (1):
        - `mustLinkExternal`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/lib.go`
    - Ground Truth Functions (2):
        - `libinit`
        - `loadlib`
    - Predicted Functions (0):

- **File:** `src/internal/asan/asan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Read`
        - ❌ `Write`

- **File:** `src/internal/asan/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `asanCheckGlobal`
        - ❌ `asanCheckHeap`
        - ❌ `asanFree`
        - ❌ `asanInit`
        - ❌ `asanMalloc`
        - ❌ `asanPoison`
        - ❌ `asanReport`
        - ❌ `asanUnpoison`

- **File:** `src/internal/asan/noasan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Read`
        - ❌ `Write`

- **File:** `src/runtime/asan.go`
    - Ground Truth Functions (7):
        - `ASanRead`
        - `ASanWrite`
        - `asanpoison`
        - `asanread`
        - `asanregisterglobals`
        - `asanunpoison`
        - `asanwrite`
    - Predicted Functions (12):
        - ✅ `ASanRead`
        - ✅ `ASanWrite`
        - ✅ `asanpoison`
        - ✅ `asanread`
        - ✅ `asanregisterglobals`
        - ✅ `asanunpoison`
        - ✅ `asanwrite`
        - ❌ `doasanread`
        - ❌ `doasanwrite`
        - ❌ `lsandoleakcheck`
        - ❌ `lsanregisterrootregion`
        - ❌ `lsanunregisterrootregion`

- **File:** `src/runtime/asan/asan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `asanCalloc`
        - ❌ `asanCheck`
        - ❌ `asanFree`
        - ❌ `asanInit`
        - ❌ `asanMalloc`
        - ❌ `asanPoison`
        - ❌ `asanRealloc`
        - ❌ `asanReport`
        - ❌ `asanUnpoison`

- **File:** `src/runtime/cgo_sigaction.go`
    - Ground Truth Functions (1):
        - `sigaction`
    - Predicted Functions (0):

- **File:** `src/runtime/iface.go`
    - Ground Truth Functions (2):
        - `convT`
        - `convTnoptr`
    - Predicted Functions (0):

- **File:** `src/runtime/malloc.go`
    - Ground Truth Functions (1):
        - `mallocgc`
    - Predicted Functions (8):
        - ✅ `mallocgc`
        - ❌ `mallocgcLarge`
        - ❌ `mallocgcSmallNoscan`
        - ❌ `mallocgcSmallScanHeader`
        - ❌ `mallocgcSmallScanNoHeader`
        - ❌ `mallocgcTiny`
        - ❌ `newarray`
        - ❌ `newobject`

- **File:** `src/runtime/mbarrier.go`
    - Ground Truth Functions (2):
        - `reflect_typedmemmove`
        - `typedslicecopy`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcsweep.go`
    - Ground Truth Functions (1):
        - `sweep`
    - Predicted Functions (0):

- **File:** `src/runtime/mheap.go`
    - Ground Truth Functions (1):
        - `freeSpan`
    - Predicted Functions (0):

- **File:** `src/runtime/mprof.go`
    - Ground Truth Functions (1):
        - `BlockProfile`
    - Predicted Functions (0):

- **File:** `src/runtime/msan/msan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/proc.go`
    - Ground Truth Functions (2):
        - `gfget`
        - `newm1`
    - Predicted Functions (0):

- **File:** `src/runtime/select.go`
    - Ground Truth Functions (1):
        - `selectgo`
    - Predicted Functions (0):

- **File:** `src/runtime/slice.go`
    - Ground Truth Functions (3):
        - `growslice`
        - `makeslicecopy`
        - `slicecopy`
    - Predicted Functions (0):

- **File:** `src/runtime/stack.go`
    - Ground Truth Functions (2):
        - `stackalloc`
        - `stackfree`
    - Predicted Functions (0):

- **File:** `src/runtime/string.go`
    - Ground Truth Functions (3):
        - `slicebytetostring`
        - `slicebytetostringtmp`
        - `slicerunetostring`
    - Predicted Functions (0):

- **File:** `src/runtime/traceback.go`
    - Ground Truth Functions (2):
        - `callCgoSymbolizer`
        - `cgoContextPCs`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_unix.go`
    - Ground Truth Functions (2):
        - `Read`
        - `Write`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (2):
        - `Read`
        - `Write`
    - Predicted Functions (0):


### 📊 **Proposal #48257 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/workcmd/use.go`
    - Ground Truth Functions (2):
        - `init`
        - `runUse`
    - Predicted Functions (0):


### 📊 **Proposal #34652 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 27.7% | 61.9% | 38.2% | 13/21 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/html/template/escape.go`
    - Ground Truth Functions (1):
        - `escape`
    - Predicted Functions (0):

- **File:** `src/html/template/template.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `AddParseTree`
        - ❌ `Parse`

- **File:** `src/html/template/template_test.go`
    - Ground Truth Functions (1):
        - `TestSkipEscapeComments`
    - Predicted Functions (1):
        - ✅ `TestSkipEscapeComments`

- **File:** `src/text/template/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `CommentNode`
        - ❌ `Parse`
        - ❌ `ParseWithOptions`

- **File:** `src/text/template/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/text/template/examplefiles_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/text/template/examplefunc_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/text/template/exec.go`
    - Ground Truth Functions (1):
        - `walk`
    - Predicted Functions (5):
        - ❌ `Execute`
        - ❌ `ExecuteTemplate`
        - ❌ `execute`
        - ✅ `walk`
        - ❌ `walkTemplate`

- **File:** `src/text/template/exec_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestBlock`
        - ❌ `TestExecError`
        - ❌ `TestExecute`
        - ❌ `TestExecuteError`
        - ❌ `TestTree`

- **File:** `src/text/template/funcs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/text/template/helper.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Must`
        - ❌ `ParseFS`
        - ❌ `ParseFiles`
        - ❌ `ParseGlob`

- **File:** `src/text/template/link_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/text/template/multi_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestAddParseTree`
        - ❌ `TestAddParseTreeToUnparsedTemplate`
        - ❌ `TestParse`

- **File:** `src/text/template/option.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Option`
        - ❌ `setOption`

- **File:** `src/text/template/parse/lex.go`
    - Ground Truth Functions (2):
        - `lex`
        - `lexComment`
    - Predicted Functions (4):
        - ❌ `emitItem`
        - ✅ `lex`
        - ✅ `lexComment`
        - ❌ `nextItem`

- **File:** `src/text/template/parse/lex_test.go`
    - Ground Truth Functions (1):
        - `collect`
    - Predicted Functions (6):
        - ❌ `TestDelims`
        - ❌ `TestDelimsAlphaNumeric`
        - ❌ `TestDelimsAndMarkers`
        - ❌ `TestLex`
        - ❌ `TestPos`
        - ❌ `parseLexer`

- **File:** `src/text/template/parse/node.go`
    - Ground Truth Functions (5):
        - `Copy`
        - `String`
        - `newComment`
        - `tree`
        - `writeTo`
    - Predicted Functions (5):
        - ✅ `Copy`
        - ✅ `String`
        - ✅ `newComment`
        - ✅ `tree`
        - ✅ `writeTo`

- **File:** `src/text/template/parse/parse.go`
    - Ground Truth Functions (8):
        - `IsEmptyTree`
        - `Parse`
        - `add`
        - `blockControl`
        - `itemList`
        - `parse`
        - `term`
        - `textOrAction`
    - Predicted Functions (4):
        - ✅ `Parse`
        - ✅ `add`
        - ✅ `parse`
        - ❌ `parseDefinition`

- **File:** `src/text/template/parse/parse_test.go`
    - Ground Truth Functions (2):
        - `TestParseWithComments`
        - `TestSkipFuncCheck`
    - Predicted Functions (1):
        - ✅ `TestParseWithComments`

- **File:** `src/text/template/template.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `AddParseTree`
        - ❌ `Parse`


### 📊 **Proposal #51668 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 83.3% | 71.4% | 76.9% | 5/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/fmt/format.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `FormatString`

- **File:** `src/fmt/print.go`
    - Ground Truth Functions (1):
        - `FormatString`
    - Predicted Functions (0):

- **File:** `src/fmt/state_test.go`
    - Ground Truth Functions (6):
        - `Flag`
        - `Precision`
        - `TestFormatString`
        - `Width`
        - `Write`
        - `mkState`
    - Predicted Functions (5):
        - ✅ `Flag`
        - ✅ `Precision`
        - ✅ `TestFormatString`
        - ✅ `Width`
        - ✅ `Write`


### 📊 **Proposal #38017 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 25.0% | 40.0% | 3/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `lib/time/mkzip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/time/export_test.go`
    - Ground Truth Functions (1):
        - `LoadFromEmbeddedTZData`
    - Predicted Functions (0):

- **File:** `src/time/tzdata/tzdata.go`
    - Ground Truth Functions (5):
        - `get2s`
        - `get4s`
        - `init`
        - `loadFromEmbeddedTZData`
        - `registerLoadFromEmbeddedTZData`
    - Predicted Functions (3):
        - ✅ `init`
        - ✅ `loadFromEmbeddedTZData`
        - ✅ `registerLoadFromEmbeddedTZData`

- **File:** `src/time/tzdata_test.go`
    - Ground Truth Functions (2):
        - `TestEmbeddedTZData`
        - `equal`
    - Predicted Functions (0):

- **File:** `src/time/zoneinfo_read.go`
    - Ground Truth Functions (4):
        - `Error`
        - `loadLocation`
        - `readFile`
        - `registerLoadFromEmbeddedTZData`
    - Predicted Functions (0):


### 📊 **Proposal #50489 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/math/big/rat.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `FloatPrec`
        - ❌ `FloatString`
        - ❌ `SetString`

- **File:** `src/math/big/rat_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestRatSetFrac64Rat`
        - ❌ `TestSetFloat64NonFinite`

- **File:** `src/math/big/ratconv.go`
    - Ground Truth Functions (1):
        - `FloatPrec`
    - Predicted Functions (0):

- **File:** `src/math/big/ratconv_test.go`
    - Ground Truth Functions (3):
        - `BenchmarkFloatPrecExact`
        - `BenchmarkFloatPrecInexact`
        - `TestFloatPrec`
    - Predicted Functions (0):


### 📊 **Proposal #32779 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 4.2% | 25.0% | 7.1% | 1/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/json/decode.go`
    - Ground Truth Functions (1):
        - `objectInterface`
    - Predicted Functions (5):
        - ❌ `Unmarshal`
        - ❌ `literalStore`
        - ❌ `object`
        - ✅ `objectInterface`
        - ❌ `unmarshal`

- **File:** `src/encoding/json/decode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestUnmarshal`
        - ❌ `TestUnmarshalMapWithTextUnmarshalerStringKey`
        - ❌ `Unmarshal`
        - ❌ `UnmarshalJSON`

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `(*encodeState) error`
        - ❌ `(*encodeState) interfaceEncoder`
        - ❌ `(*encodeState) mapEncoder`
        - ❌ `(*encodeState) marshal`
        - ❌ `(*encodeState) reflectValue`
        - ❌ `(*encodeState) stringEncoder`
        - ❌ `newEncodeState`
        - ❌ `newMapEncoder`

- **File:** `src/encoding/json/jsontext/decode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `NewDecoder`
        - ❌ `ReadToken`
        - ❌ `ReadValue`
        - ❌ `Reset`
        - ❌ `SkipValue`

- **File:** `src/encoding/json/jsontext/decode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestDecoder`
        - ❌ `TestDecoderErrors`

- **File:** `src/encoding/json/stream.go`
    - Ground Truth Functions (1):
        - `Token`
    - Predicted Functions (0):

- **File:** `src/encoding/json/stream_test.go`
    - Ground Truth Functions (2):
        - `TestDecodeInStream`
        - `TestDecoder`
    - Predicted Functions (0):


### 📊 **Proposal #37112 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 26.5% | 29.0% | 27.7% | 9/31 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (1):
        - `gc`
    - Predicted Functions (0):

- **File:** `src/runtime/export_test.go`
    - Ground Truth Functions (3):
        - `Count`
        - `ReadMetricsSlow`
        - `Record`
    - Predicted Functions (0):

- **File:** `src/runtime/histogram.go`
    - Ground Truth Functions (2):
        - `record`
        - `timeHistogramMetricsBuckets`
    - Predicted Functions (0):

- **File:** `src/runtime/histogram_test.go`
    - Ground Truth Functions (1):
        - `TestTimeHistogram`
    - Predicted Functions (0):

- **File:** `src/runtime/metrics.go`
    - Ground Truth Functions (10):
        - `compute`
        - `difference`
        - `empty`
        - `ensure`
        - `float64HistOrInit`
        - `has`
        - `initMetrics`
        - `makeStatDepSet`
        - `readMetrics`
        - `union`
    - Predicted Functions (0):

- **File:** `src/runtime/metrics/description.go`
    - Ground Truth Functions (1):
        - `All`
    - Predicted Functions (2):
        - ✅ `All`
        - ❌ `init`

- **File:** `src/runtime/metrics/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `Float64Histogram`
        - ❌ `Get`
        - ❌ `Histogram`
        - ❌ `List`
        - ❌ `NewMetric`
        - ❌ `Read`
        - ❌ `Register`
        - ❌ `TimeHistogram`
        - ❌ `Unregister`

- **File:** `src/runtime/metrics/histogram.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `Add`
        - ❌ `Get`
        - ❌ `Histogram`
        - ❌ `Merge`
        - ❌ `NewHistogram`
        - ❌ `Record`
        - ❌ `Reset`
        - ❌ `Set`
        - ❌ `Value`

- **File:** `src/runtime/metrics/sample.go`
    - Ground Truth Functions (2):
        - `Read`
        - `runtime_readMetrics`
    - Predicted Functions (2):
        - ✅ `Read`
        - ✅ `runtime_readMetrics`

- **File:** `src/runtime/metrics/value.go`
    - Ground Truth Functions (4):
        - `Float64`
        - `Float64Histogram`
        - `Kind`
        - `Uint64`
    - Predicted Functions (4):
        - ✅ `Float64`
        - ✅ `Float64Histogram`
        - ✅ `Kind`
        - ✅ `Uint64`

- **File:** `src/runtime/metrics_test.go`
    - Ground Truth Functions (3):
        - `TestReadMetrics`
        - `TestReadMetricsConsistency`
        - `prepareAllMetricsSamples`
    - Predicted Functions (8):
        - ❌ `BenchmarkReadMetricsLatency`
        - ❌ `TestCPUMetricsSleep`
        - ❌ `TestCPUStats`
        - ✅ `TestReadMetrics`
        - ✅ `TestReadMetricsConsistency`
        - ❌ `TestReadMetricsCumulative`
        - ❌ `TestRuntimeLockMetricsAndProfile`
        - ❌ `TestSchedPauseMetrics`

- **File:** `src/runtime/mgc.go`
    - Ground Truth Functions (3):
        - `gcMarkDone`
        - `gcMarkTermination`
        - `gcStart`
    - Predicted Functions (0):

- **File:** `src/runtime/mstats.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):


### 📊 **Proposal #48187 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 13.6% | 75.0% | 23.1% | 3/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/version/version.go`
    - Ground Truth Functions (3):
        - `isGoBinaryCandidate`
        - `scanDir`
        - `scanFile`
    - Predicted Functions (3):
        - ✅ `isGoBinaryCandidate`
        - ❌ `runVersion`
        - ✅ `scanFile`

- **File:** `src/cmd/link/internal/ld/ar.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `hostArchive`
        - ❌ `readArmap`

- **File:** `src/debug/buildinfo/buildinfo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `(*elfExe) DataReader`
        - ❌ `(*machoExe) DataReader`
        - ❌ `(*peExe) DataReader`
        - ❌ `(*plan9objExe) DataReader`
        - ❌ `(*xcoffExe) DataReader`
        - ❌ `Read`
        - ❌ `ReadFile`
        - ❌ `readData`
        - ❌ `readDataInto`
        - ❌ `readRawBuildInfo`

- **File:** `src/debug/buildinfo/buildinfo_test.go`
    - Ground Truth Functions (1):
        - `TestReadFile`
    - Predicted Functions (3):
        - ❌ `TestIssue54968`
        - ❌ `TestNotGo`
        - ✅ `TestReadFile`

- **File:** `src/go/version/version.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Compare`
        - ❌ `IsValid`
        - ❌ `Lang`
        - ❌ `stripGo`


### 📊 **Proposal #49097 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.6% | 16.7% | 8.3% | 1/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/dial.go`
    - Ground Truth Functions (1):
        - `DialContext`
    - Predicted Functions (5):
        - ❌ `Dial`
        - ✅ `DialContext`
        - ❌ `DialTimeout`
        - ❌ `Dialer.Dial`
        - ❌ `Dialer.DialContext`

- **File:** `src/net/ip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ParseCIDR`
        - ❌ `ParseIP`

- **File:** `src/net/iprawsock.go`
    - Ground Truth Functions (1):
        - `DialIP`
    - Predicted Functions (0):

- **File:** `src/net/net.go`
    - Ground Truth Functions (1):
        - `Error`
    - Predicted Functions (6):
        - ❌ `DialIP`
        - ❌ `DialIPContext`
        - ❌ `DialTCP`
        - ❌ `DialTCPContext`
        - ❌ `DialUDP`
        - ❌ `DialUDPContext`

- **File:** `src/net/netip/netip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Addr`
        - ❌ `AddrPort`
        - ❌ `AddrPortFrom`
        - ❌ `MustParseAddrPort`
        - ❌ `ParseAddrPort`

- **File:** `src/net/tcpsock.go`
    - Ground Truth Functions (1):
        - `DialTCP`
    - Predicted Functions (0):

- **File:** `src/net/udpsock.go`
    - Ground Truth Functions (1):
        - `DialUDP`
    - Predicted Functions (0):

- **File:** `src/net/unixsock.go`
    - Ground Truth Functions (1):
        - `DialUnix`
    - Predicted Functions (0):


### 📊 **Proposal #34974 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 20.0% | 11.8% | 1/5 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/zip/reader.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `DataOffset`
        - ❌ `Open`
        - ❌ `OpenRaw`

- **File:** `src/archive/zip/writer.go`
    - Ground Truth Functions (3):
        - `CreateHeader`
        - `Write`
        - `close`
    - Predicted Functions (4):
        - ❌ `Copy`
        - ✅ `CreateHeader`
        - ❌ `CreateHeaderRaw`
        - ❌ `RegisterCompressor`

- **File:** `src/archive/zip/writer_test.go`
    - Ground Truth Functions (2):
        - `TestWriterDirAttributes`
        - `testCreate`
    - Predicted Functions (0):

- **File:** `src/archive/zip/zip_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestFileHeaderRoundTrip`
        - ❌ `TestFileHeaderRoundTrip64`
        - ❌ `TestHeaderIgnoredSize`
        - ❌ `TestHeaderInvalidTagAndSize`
        - ❌ `TestZeroLengthHeader`


### 📊 **Proposal #46771 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 66.7% | 28.6% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/mime/multipart/formdata.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `CreateFormFile`
        - ❌ `CreateFormFileWithContentType`
        - ❌ `FileContentDisposition`

- **File:** `src/mime/multipart/multipart.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `NewReader`
        - ❌ `NextPart`
        - ❌ `NextRawPart`
        - ❌ `parseContentDisposition`
        - ❌ `populateHeaders`

- **File:** `src/mime/multipart/writer.go`
    - Ground Truth Functions (2):
        - `CreateFormFile`
        - `FileContentDisposition`
    - Predicted Functions (3):
        - ✅ `CreateFormFile`
        - ❌ `CreateFormFileWithContentType`
        - ✅ `FileContentDisposition`

- **File:** `src/mime/multipart/writer_test.go`
    - Ground Truth Functions (1):
        - `TestFileContentDisposition`
    - Predicted Functions (0):


### 📊 **Proposal #33920 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 80.0% | 53.3% | 4/5 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/io/ioutil/tempfile.go`
    - Ground Truth Functions (2):
        - `TempDir`
        - `TempFile`
    - Predicted Functions (2):
        - ✅ `TempDir`
        - ✅ `TempFile`

- **File:** `src/io/ioutil/tempfile_test.go`
    - Ground Truth Functions (2):
        - `TestTempDir_BadPattern`
        - `TestTempFile_BadPattern`
    - Predicted Functions (6):
        - ❌ `TestTempDir`
        - ❌ `TestTempDir_BadDir`
        - ✅ `TestTempDir_BadPattern`
        - ❌ `TestTempFile`
        - ✅ `TestTempFile_BadPattern`
        - ❌ `TestTempFile_pattern`

- **File:** `src/os/os_test.go`
    - Ground Truth Functions (1):
        - `TestStatDirWithTrailingSlash`
    - Predicted Functions (0):

- **File:** `src/path/filepath/path.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Base`
        - ❌ `Join`


### 📊 **Proposal #47066 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (1):
        - `TestBytes`
    - Predicted Functions (0):

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (1):
        - `Bytes`
    - Predicted Functions (3):
        - ✅ `Bytes`
        - ❌ `SetBytes`
        - ❌ `Slice`


### 📊 **Proposal #50062 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 50.0% | 16.7% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ZoneBounds`

- **File:** `src/runtime/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/time/time.go`
    - Ground Truth Functions (1):
        - `ZoneBounds`
    - Predicted Functions (3):
        - ❌ `IsDST`
        - ❌ `Zone`
        - ✅ `ZoneBounds`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (1):
        - `TestZoneBounds`
    - Predicted Functions (0):

- **File:** `src/time/zoneinfo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `firstZoneUsed`
        - ❌ `lookup`
        - ❌ `lookupFirstZone`
        - ❌ `lookupName`

- **File:** `src/time/zoneinfo_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestLoadLocationFromTZData`
        - ❌ `TestLoadLocationFromTZDataSlim`


### 📊 **Proposal #47342 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 34.1% | 71.4% | 46.2% | 15/21 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `registerTests`
    - Predicted Functions (0):

- **File:** `src/hash/maphash/maphash.go`
    - Ground Truth Functions (8):
        - `Bytes`
        - `MakeSeed`
        - `String`
        - `Sum`
        - `Sum64`
        - `Write`
        - `WriteString`
        - `flush`
    - Predicted Functions (17):
        - ❌ `BlockSize`
        - ✅ `Bytes`
        - ❌ `Clone`
        - ❌ `Comparable`
        - ❌ `Hash`
        - ✅ `MakeSeed`
        - ❌ `Reset`
        - ❌ `Seed`
        - ❌ `SetSeed`
        - ❌ `Size`
        - ✅ `String`
        - ✅ `Sum`
        - ✅ `Sum64`
        - ✅ `Write`
        - ❌ `WriteByte`
        - ❌ `WriteComparable`
        - ✅ `WriteString`

- **File:** `src/hash/maphash/maphash_purego.go`
    - Ground Truth Functions (8):
        - `mix`
        - `r3`
        - `r4`
        - `r8`
        - `randUint64`
        - `rthash`
        - `rthashString`
        - `wyhash`
    - Predicted Functions (12):
        - ❌ `appendT`
        - ❌ `comparableHash`
        - ❌ `float64`
        - ✅ `mix`
        - ✅ `r3`
        - ✅ `r4`
        - ✅ `r8`
        - ✅ `randUint64`
        - ✅ `rthash`
        - ✅ `rthashString`
        - ❌ `writeComparable`
        - ✅ `wyhash`

- **File:** `src/hash/maphash/maphash_runtime.go`
    - Ground Truth Functions (4):
        - `randUint64`
        - `rthash`
        - `rthashString`
        - `runtime_memhash`
    - Predicted Functions (0):

- **File:** `src/hash/maphash/maphash_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (15):
        - ❌ `BenchmarkHash`
        - ❌ `TestComparable`
        - ❌ `TestComparableShouldPanic`
        - ❌ `TestHashBytesVsString`
        - ❌ `TestHashGrouping`
        - ❌ `TestHashHighBytes`
        - ❌ `TestHashInterface`
        - ❌ `TestSeedFromFlush`
        - ❌ `TestSeedFromReset`
        - ❌ `TestSeedFromSeed`
        - ❌ `TestSeedFromSum64`
        - ❌ `TestSeededHash`
        - ❌ `TestUnseededHash`
        - ❌ `TestWriteComparable`
        - ❌ `benchmarkComparable`


### 📊 **Proposal #48218 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (1):
        - `FieldByIndexErr`
    - Predicted Functions (2):
        - ❌ `FieldByIndex`
        - ✅ `FieldByIndexErr`

- **File:** `src/reflect/visiblefields_test.go`
    - Ground Truth Functions (1):
        - `TestFieldByIndexErr`
    - Predicted Functions (0):


### 📊 **Proposal #5901 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 18.2% | 17.4% | 4/22 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/json/bench_test.go`
    - Ground Truth Functions (1):
        - `BenchmarkTypeFieldsCache`
    - Predicted Functions (0):

- **File:** `src/encoding/json/decode.go`
    - Ground Truth Functions (4):
        - `array`
        - `indirect`
        - `literalStore`
        - `object`
    - Predicted Functions (5):
        - ❌ `(*decodeState) arrayInterface`
        - ❌ `(*decodeState) objectInterface`
        - ❌ `(*decodeState) unmarshal`
        - ❌ `(*decodeState) valueInterface`
        - ❌ `Unmarshal`

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (16):
        - `cachedTypeFields`
        - `encode`
        - `encodeByteSlice`
        - `isEmptyValue`
        - `isValidNumber`
        - `newArrayEncoder`
        - `newEncodeState`
        - `newMapEncoder`
        - `newPtrEncoder`
        - `newSliceEncoder`
        - `newStructEncoder`
        - `newTypeEncoder`
        - `reflectValue`
        - `typeEncoder`
        - `typeFields`
        - `valueEncoder`
    - Predicted Functions (12):
        - ❌ `(*encodeState) error`
        - ❌ `(*encodeState) marshal`
        - ❌ `Marshal`
        - ❌ `MarshalIndent`
        - ❌ `addrMarshalerEncoder`
        - ❌ `addrTextMarshalerEncoder`
        - ❌ `marshalerEncoder`
        - ✅ `newEncodeState`
        - ✅ `newTypeEncoder`
        - ❌ `textMarshalerEncoder`
        - ✅ `typeEncoder`
        - ✅ `valueEncoder`

- **File:** `src/encoding/json/example_marshaling_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Example_customMarshalJSON`
        - ❌ `MarshalJSON`
        - ❌ `UnmarshalJSON`

- **File:** `src/encoding/json/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `ExampleDecoder`
        - ❌ `ExampleDecoder_Decode_stream`
        - ❌ `ExampleMarshal`
        - ❌ `ExampleUnmarshal`

- **File:** `src/encoding/json/stream.go`
    - Ground Truth Functions (1):
        - `Encode`
    - Predicted Functions (0):

- **File:** `src/syscall/js/js.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/js/js_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #42322 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 40.0% | 36.4% | 6/15 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/embed/embed.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Open`
        - ❌ `ReadDir`
        - ❌ `ReadFile`

- **File:** `src/embed/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/embed/internal/embedtest/embed_test.go`
    - Ground Truth Functions (1):
        - `TestGlobal`
    - Predicted Functions (0):

- **File:** `src/io/fs/fs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Sub`
        - ❌ `SubFS`

- **File:** `src/io/fs/readdir_test.go`
    - Ground Truth Functions (1):
        - `TestReadDir`
    - Predicted Functions (0):

- **File:** `src/io/fs/readfile_test.go`
    - Ground Truth Functions (1):
        - `TestReadFile`
    - Predicted Functions (0):

- **File:** `src/io/fs/sub.go`
    - Ground Truth Functions (8):
        - `Glob`
        - `Open`
        - `ReadDir`
        - `ReadFile`
        - `Sub`
        - `fixErr`
        - `fullName`
        - `shorten`
    - Predicted Functions (7):
        - ✅ `Glob`
        - ❌ `Lstat`
        - ✅ `Open`
        - ✅ `ReadDir`
        - ✅ `ReadFile`
        - ❌ `ReadLink`
        - ✅ `Sub`

- **File:** `src/io/fs/sub_test.go`
    - Ground Truth Functions (1):
        - `TestSub`
    - Predicted Functions (1):
        - ✅ `TestSub`

- **File:** `src/net/http/fs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `FileServer`
        - ❌ `FileServerFS`
        - ❌ `Open`
        - ❌ `ServeFile`
        - ❌ `ServeFileFS`

- **File:** `src/net/http/http.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/testing/fstest/mapfs.go`
    - Ground Truth Functions (1):
        - `Sub`
    - Predicted Functions (0):

- **File:** `src/testing/fstest/testfs.go`
    - Ground Truth Functions (2):
        - `TestFS`
        - `testFS`
    - Predicted Functions (0):


### 📊 **Proposal #42088 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/load/pkg.go`
    - Ground Truth Functions (8):
        - `AllFiles`
        - `Error`
        - `GoFilesPackage`
        - `ImportPath`
        - `PackagesAndErrors`
        - `PackagesAndErrorsOutsideModule`
        - `copyBuild`
        - `mainPackagesOnly`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/run/run.go`
    - Ground Truth Functions (2):
        - `runRun`
        - `shouldUseOutsideModuleMode`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (2):
        - `FindExecCmd`
        - `installOutsideModule`
    - Predicted Functions (0):


### 📊 **Proposal #47916 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 27.3% | 12.7% | 9/33 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/noder/writer.go`
    - Ground Truth Functions (3):
        - `method`
        - `objTypeParams`
        - `pkgDecl`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/call.go`
    - Ground Truth Functions (1):
        - `selector`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/lookup.go`
    - Ground Truth Functions (1):
        - `missingMethod`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/signature.go`
    - Ground Truth Functions (1):
        - `funcType`
    - Predicted Functions (0):

- **File:** `src/go/types/alias.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `NewAlias`
        - ❌ `SetTypeParams`
        - ❌ `TypeArgs`
        - ❌ `TypeParams`

- **File:** `src/go/types/api.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Check`
        - ❌ `ObjectOf`
        - ❌ `PkgNameOf`
        - ❌ `TypeOf`
        - ❌ `recordTypes`

- **File:** `src/go/types/api_test.go`
    - Ground Truth Functions (1):
        - `TestInstantiate`
    - Predicted Functions (6):
        - ❌ `TestGenericMethodInfo`
        - ✅ `TestInstantiate`
        - ❌ `TestInstantiateConcurrent`
        - ❌ `TestInstantiateErrors`
        - ❌ `TestInstantiatedObjects`
        - ❌ `TestLookupFieldOrMethod_RecursiveGeneric`

- **File:** `src/go/types/array.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/assignments.go`
    - Ground Truth Functions (1):
        - `assignment`
    - Predicted Functions (11):
        - ❌ `assignError`
        - ❌ `assignVar`
        - ❌ `assignVars`
        - ✅ `assignment`
        - ❌ `initConst`
        - ❌ `initVar`
        - ❌ `initVars`
        - ❌ `lhsVar`
        - ❌ `returnError`
        - ❌ `shortVarDecl`
        - ❌ `typesSummary`

- **File:** `src/go/types/badlinkname.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `badlinkname_Checker_infer`

- **File:** `src/go/types/basic.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/builtins.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `applyTypeFunc`
        - ❌ `builtin`
        - ❌ `makeSig`

- **File:** `src/go/types/call.go`
    - Ground Truth Functions (4):
        - `arguments`
        - `callExpr`
        - `funcInst`
        - `selector`
    - Predicted Functions (5):
        - ✅ `arguments`
        - ✅ `callExpr`
        - ✅ `funcInst`
        - ❌ `genericExprList`
        - ❌ `instantiateSignature`

- **File:** `src/go/types/chan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/check.go`
    - Ground Truth Functions (1):
        - `NewChecker`
    - Predicted Functions (5):
        - ✅ `NewChecker`
        - ❌ `checkFiles`
        - ❌ `processDelayed`
        - ❌ `recordCommaOkTypesInSyntax`
        - ❌ `recordTypeAndValueInSyntax`

- **File:** `src/go/types/context.go`
    - Ground Truth Functions (1):
        - `NewContext`
    - Predicted Functions (1):
        - ✅ `NewContext`

- **File:** `src/go/types/conversions.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/decl.go`
    - Ground Truth Functions (1):
        - `typeDecl`
    - Predicted Functions (4):
        - ❌ `collectMethods`
        - ❌ `collectTypeParams`
        - ❌ `declareTypeParam`
        - ❌ `isImportedConstraint`

- **File:** `src/go/types/errors.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/eval.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `CheckExpr`
        - ❌ `Eval`

- **File:** `src/go/types/expr.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `exprOrType`
        - ❌ `genericExpr`

- **File:** `src/go/types/format.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/gotype.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/index.go`
    - Ground Truth Functions (1):
        - `indexExpr`
    - Predicted Functions (0):

- **File:** `src/go/types/infer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `infer`
        - ❌ `isParameterized`
        - ❌ `renameTParams`
        - ❌ `varList`

- **File:** `src/go/types/instantiate.go`
    - Ground Truth Functions (2):
        - `Instantiate`
        - `instance`
    - Predicted Functions (5):
        - ✅ `Instantiate`
        - ❌ `implements`
        - ✅ `instance`
        - ❌ `validateTArgLen`
        - ❌ `verify`

- **File:** `src/go/types/instantiate_test.go`
    - Ground Truth Functions (2):
        - `TestInstantiateEquality`
        - `TestInstantiateNonEquality`
    - Predicted Functions (0):

- **File:** `src/go/types/interface.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `IsMethodSet`
        - ❌ `NewInterface`
        - ❌ `NewInterfaceType`
        - ❌ `interfaceType`

- **File:** `src/go/types/lookup.go`
    - Ground Truth Functions (1):
        - `missingMethod`
    - Predicted Functions (0):

- **File:** `src/go/types/named.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `AddMethod`
        - ❌ `Method`
        - ❌ `NewNamed`
        - ❌ `NumMethods`
        - ❌ `SetTypeParams`
        - ❌ `TypeArgs`
        - ❌ `TypeParams`
        - ❌ `Underlying`

- **File:** `src/go/types/object.go`
    - Ground Truth Functions (1):
        - `writeObject`
    - Predicted Functions (6):
        - ❌ `(*Func) Origin`
        - ❌ `(*Func) Signature`
        - ❌ `NewFunc`
        - ❌ `NewParam`
        - ❌ `NewTypeName`
        - ❌ `NewVar`

- **File:** `src/go/types/operand.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `assignableTo`

- **File:** `src/go/types/pointer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/predicates.go`
    - Ground Truth Functions (2):
        - `identical`
        - `isGeneric`
    - Predicted Functions (0):

- **File:** `src/go/types/range.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `rangeKeyVal`
        - ❌ `rangeStmt`

- **File:** `src/go/types/return.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/signature.go`
    - Ground Truth Functions (1):
        - `funcType`
    - Predicted Functions (5):
        - ❌ `NewSignature`
        - ❌ `NewSignatureType`
        - ❌ `Recv`
        - ❌ `RecvTypeParams`
        - ❌ `TypeParams`

- **File:** `src/go/types/struct.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Field`
        - ❌ `NewStruct`
        - ❌ `NumFields`
        - ❌ `String`
        - ❌ `Tag`
        - ❌ `Underlying`

- **File:** `src/go/types/subst.go`
    - Ground Truth Functions (2):
        - `subst`
        - `typ`
    - Predicted Functions (0):

- **File:** `src/go/types/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `Constraint`
        - ❌ `Info.Inferred`
        - ❌ `Info.Instances`
        - ❌ `Instantiate`
        - ❌ `NewSignatureType`
        - ❌ `Origin`
        - ❌ `RecvTypeParams`
        - ❌ `SetConstraint`
        - ❌ `TypeArgs`
        - ❌ `TypeParams`

- **File:** `src/go/types/typelists.go`
    - Ground Truth Functions (1):
        - `bindTParams`
    - Predicted Functions (0):

- **File:** `src/go/types/typeparam.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Constraint`
        - ❌ `Index`
        - ❌ `NewTypeParam`
        - ❌ `SetConstraint`
        - ❌ `newTypeParam`

- **File:** `src/go/types/typeset.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `IsMethodSet`
        - ❌ `LookupMethod`
        - ❌ `Method`
        - ❌ `NumMethods`

- **File:** `src/go/types/typestring.go`
    - Ground Truth Functions (5):
        - `error`
        - `newTypeHasher`
        - `signature`
        - `tuple`
        - `typ`
    - Predicted Functions (0):

- **File:** `src/go/types/union.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/util.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/version.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #37168 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/22 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/aes/aes.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `NewCipher`

- **File:** `src/crypto/cipher/cbc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `BlockSize`
        - ❌ `CryptBlocks`
        - ❌ `NewCBCDecrypter`
        - ❌ `NewCBCEncrypter`
        - ❌ `SetIV`

- **File:** `src/crypto/cipher/ctr.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `NewCTR`
        - ❌ `XORKeyStream`
        - ❌ `refill`

- **File:** `src/crypto/cipher/gcm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `NewGCM`
        - ❌ `NewGCMWithNonceSize`
        - ❌ `NewGCMWithRandomNonce`
        - ❌ `NewGCMWithTagSize`
        - ❌ `Open`
        - ❌ `Seal`
        - ❌ `gcmAuth`
        - ❌ `gcmCounterCryptGeneric`

- **File:** `src/crypto/des/block.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `cryptBlock`
        - ❌ `feistel`
        - ❌ `generateSubkeys`
        - ❌ `initFeistelBox`
        - ❌ `ksRotate`
        - ❌ `permuteBlock`
        - ❌ `permuteFinalBlock`
        - ❌ `permuteInitialBlock`
        - ❌ `unpack`

- **File:** `src/crypto/dsa/dsa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `GenerateKey`
        - ❌ `GenerateParameters`
        - ❌ `Sign`
        - ❌ `Verify`

- **File:** `src/crypto/ecdsa/ecdsa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `GenerateKey`
        - ❌ `Sign`
        - ❌ `VerifyASN1`

- **File:** `src/crypto/ed25519/ed25519.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `GenerateKey`
        - ❌ `Sign`
        - ❌ `Verify`

- **File:** `src/crypto/elliptic/elliptic.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `P224`
        - ❌ `P256`
        - ❌ `P384`
        - ❌ `P521`

- **File:** `src/crypto/hmac/hmac.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Equal`
        - ❌ `New`

- **File:** `src/crypto/rc4/rc4.go`
    - Ground Truth Functions (1):
        - `XORKeyStream`
    - Predicted Functions (0):

- **File:** `src/crypto/rc4/rc4_test.go`
    - Ground Truth Functions (2):
        - `TestBlock`
        - `benchmark`
    - Predicted Functions (0):

- **File:** `src/crypto/rsa/rsa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Decrypt`
        - ❌ `GenerateKey`
        - ❌ `GenerateMultiPrimeKey`
        - ❌ `Sign`
        - ❌ `Validate`

- **File:** `src/crypto/sha1/sha1.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `BlockSize`
        - ❌ `ConstantTimeSum`
        - ❌ `New`
        - ❌ `Size`
        - ❌ `Sum`
        - ❌ `Write`
        - ❌ `checkSum`
        - ❌ `constSum`

- **File:** `src/crypto/sha256/sha256.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `New`
        - ❌ `New224`
        - ❌ `Sum224`
        - ❌ `Sum256`

- **File:** `src/crypto/sha512/sha512.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `New`
        - ❌ `New384`
        - ❌ `New512_224`
        - ❌ `New512_256`
        - ❌ `Sum384`
        - ❌ `Sum512`
        - ❌ `Sum512_224`
        - ❌ `Sum512_256`

- **File:** `src/image/image_test.go`
    - Ground Truth Functions (19):
        - `BenchmarkAlpha16At`
        - `BenchmarkAlphaAt`
        - `BenchmarkAlphaSetAlpha`
        - `BenchmarkAlphaSetAlpha16`
        - `BenchmarkAt`
        - `BenchmarkGray16At`
        - `BenchmarkGrayAt`
        - `BenchmarkGraySetGray`
        - `BenchmarkGraySetGray16`
        - `BenchmarkNRGBA64At`
        - `BenchmarkNRGBA64SetNRGBA64`
        - `BenchmarkNRGBAAt`
        - `BenchmarkNRGBASetNRGBA`
        - `BenchmarkRGBA64At`
        - `BenchmarkRGBA64SetRGBA64`
        - `BenchmarkRGBAAt`
        - `BenchmarkRGBASetRGBA`
        - `BenchmarkSet`
        - `TestImage`
    - Predicted Functions (0):

- **File:** `src/math/big/internal/asmgen/amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `amd64Add`
        - ❌ `amd64JmpADX`
        - ❌ `x86Hint`
        - ❌ `x86MulWide`
        - ❌ `x86Op3`
        - ❌ `x86Suffix`

- **File:** `src/math/big/internal/asmgen/arm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `armLoadDecN`
        - ❌ `armLoadIncN`
        - ❌ `armMulWide`
        - ❌ `armStoreDecN`
        - ❌ `armStoreIncN`

- **File:** `src/math/big/internal/asmgen/arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `arm64LoadDecN`
        - ❌ `arm64LoadIncN`
        - ❌ `arm64StoreDecN`
        - ❌ `arm64StoreIncN`

- **File:** `src/math/big/internal/asmgen/mips.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `mipsMulWide`

- **File:** `src/math/big/internal/asmgen/mips64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `mips64MulWide`

- **File:** `src/math/big/internal/asmgen/s390x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `s390MulWide`
        - ❌ `s390xHint`
        - ❌ `s390xOp3`
        - ❌ `s390xSetup`


### 📊 **Proposal #42098 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 100.0% | 18.2% | 1/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/os/exec/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `CreateProcess`
        - ❌ `StartProcess`
        - ❌ `funcLiteral`

- **File:** `src/os/exec/exec_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestNoInheritHandles`

- **File:** `src/syscall/exec_windows.go`
    - Ground Truth Functions (1):
        - `StartProcess`
    - Predicted Functions (2):
        - ❌ `Exec`
        - ✅ `StartProcess`

- **File:** `src/syscall/exec_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestChangingProcessParent`

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `CreateProcess`
        - ❌ `CreateProcessAsUser`
        - ❌ `GetStartupInfo`


### 📊 **Proposal #51115 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/io/io.go`
    - Ground Truth Functions (1):
        - `Read`
    - Predicted Functions (2):
        - ❌ `LimitReader`
        - ✅ `Read`

- **File:** `src/net/http/http.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/request.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `MaxBytesReader`
        - ❌ `maxBytesReader.Close`
        - ❌ `maxBytesReader.Read`

- **File:** `src/net/http/response.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #48052 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/debug/elf/elf.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ErrNoSymbols`

- **File:** `src/debug/plan9obj/file.go`
    - Ground Truth Functions (1):
        - `Symbols`
    - Predicted Functions (4):
        - ❌ `Open`
        - ❌ `Section`
        - ✅ `Symbols`
        - ❌ `walksymtab`


### 📊 **Proposal #38079 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/httputil/reverseproxy.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (3):
        - ❌ `NewSingleHostReverseProxy`
        - ✅ `ServeHTTP`
        - ❌ `SetXForwarded`

- **File:** `src/net/http/httputil/reverseproxy_test.go`
    - Ground Truth Functions (1):
        - `TestXForwardedFor_Omit`
    - Predicted Functions (2):
        - ❌ `TestXForwardedFor`
        - ✅ `TestXForwardedFor_Omit`


### 📊 **Proposal #42387 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 31.2% | 83.3% | 45.5% | 5/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/io/fs/fs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `FileInfoToDirEntry`

- **File:** `src/io/fs/readdir.go`
    - Ground Truth Functions (5):
        - `FileInfoToDirEntry`
        - `Info`
        - `IsDir`
        - `Name`
        - `Type`
    - Predicted Functions (7):
        - ✅ `FileInfoToDirEntry`
        - ✅ `Info`
        - ✅ `IsDir`
        - ✅ `Name`
        - ❌ `ReadDir`
        - ❌ `String`
        - ✅ `Type`

- **File:** `src/io/fs/readdir_test.go`
    - Ground Truth Functions (1):
        - `TestFileInfoToDirEntry`
    - Predicted Functions (0):

- **File:** `src/os/dir.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `ReadDir`
        - ❌ `Readdir`
        - ❌ `Readdirnames`

- **File:** `src/os/file.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Lstat`
        - ❌ `ReadDir`
        - ❌ `Stat`

- **File:** `src/os/stat.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Lstat`
        - ❌ `Stat`


### 📊 **Proposal #46293 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/test/inl_test.go`
    - Ground Truth Functions (1):
        - `TestIntendedInlining`
    - Predicted Functions (0):

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (2):
        - `TestMapIterReset`
        - `TestMapIterSet`
    - Predicted Functions (0):

- **File:** `src/reflect/iter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `MapIter`
        - ❌ `Reset`

- **File:** `src/reflect/iter_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/map_noswiss.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Key`
        - ❌ `MapIter.Reset`
        - ❌ `MapRange`
        - ❌ `Next`
        - ❌ `Value`

- **File:** `src/reflect/map_noswiss_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/map_swiss.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `MapIter.Key`
        - ❌ `MapIter.Next`
        - ❌ `MapIter.Reset`
        - ❌ `MapIter.Value`
        - ❌ `Value.MapRange`

- **File:** `src/reflect/map_swiss_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #43947 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 12.5% | 14.8% | 2/16 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (1):
        - `xinit`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (5):
        - `flattenCmdline`
        - `registerRaceBenchTest`
        - `registerStdTest`
        - `registerTests`
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/util.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/os/exec/dot_test.go`
    - Ground Truth Functions (1):
        - `TestLookPath`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (5):
        - `Command`
        - `Error`
        - `Start`
        - `String`
        - `writerDescriptor`
    - Predicted Functions (7):
        - ❌ `CombinedOutput`
        - ✅ `Command`
        - ❌ `CommandContext`
        - ❌ `LookPath`
        - ❌ `Output`
        - ❌ `Run`
        - ✅ `Start`

- **File:** `src/os/exec/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Command`
        - ❌ `LookPath`

- **File:** `src/os/exec/exec_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_plan9.go`
    - Ground Truth Functions (1):
        - `LookPath`
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_unix.go`
    - Ground Truth Functions (1):
        - `LookPath`
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_windows.go`
    - Ground Truth Functions (1):
        - `LookPath`
    - Predicted Functions (0):

- **File:** `src/syscall/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Exec`
        - ❌ `StartProcess`

- **File:** `src/syscall/exec_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #37475 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 1.4% | 2.4% | 1/74 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/go_test.go`
    - Ground Truth Functions (1):
        - `TestLdFlagsLongArgumentsIssue42295`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/flag.go`
    - Ground Truth Functions (1):
        - `set`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/pkg.go`
    - Ground Truth Functions (2):
        - `load`
        - `setBuildInfo`
    - Predicted Functions (3):
        - ❌ `LoadPackage`
        - ❌ `loadPackageData`
        - ✅ `setBuildInfo`

- **File:** `src/cmd/go/internal/modload/build.go`
    - Ground Truth Functions (2):
        - `ModInfoProg`
        - `findModule`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vcs/vcs.go`
    - Ground Truth Functions (10):
        - `Error`
        - `FromDir`
        - `Is`
        - `TagSync`
        - `gitStatus`
        - `hgStatus`
        - `parseGOVCS`
        - `repoRootForImportDynamic`
        - `repoRootFromVCSPaths`
        - `runOutputVerboseOnly`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vcs/vcs_test.go`
    - Ground Truth Functions (1):
        - `TestFromDir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/version/version.go`
    - Ground Truth Functions (1):
        - `scanFile`
    - Predicted Functions (1):
        - ❌ `runVersion`

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (1):
        - `AddBuildFlags`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `(*Builder) build`
        - ❌ `(*Builder) cleanup`
        - ❌ `(*Builder) installHeader`
        - ❌ `(*Builder) link`
        - ❌ `(*Builder) writeLinkImportcfg`

- **File:** `src/debug/buildinfo/buildinfo.go`
    - Ground Truth Functions (6):
        - `DataStart`
        - `Read`
        - `ReadFile`
        - `imageBase`
        - `readRawBuildInfo`
        - `readString`
    - Predicted Functions (0):

- **File:** `src/debug/buildinfo/buildinfo_test.go`
    - Ground Truth Functions (1):
        - `TestReadFile`
    - Predicted Functions (0):

- **File:** `src/encoding/binary/binary_test.go`
    - Ground Truth Functions (36):
        - `BenchmarkLittleEndianPutUint16`
        - `BenchmarkLittleEndianPutUint32`
        - `BenchmarkLittleEndianPutUint64`
        - `BenchmarkPutUint16`
        - `BenchmarkPutUint32`
        - `BenchmarkPutUint64`
        - `BenchmarkReadFloats`
        - `BenchmarkReadInts`
        - `BenchmarkReadSlice1000Float32s`
        - `BenchmarkReadSlice1000Int32s`
        - `BenchmarkReadSlice1000Uint8s`
        - `BenchmarkReadStruct`
        - `BenchmarkWriteFloats`
        - `BenchmarkWriteInts`
        - `BenchmarkWriteSlice1000Float32s`
        - `BenchmarkWriteSlice1000Int32s`
        - `BenchmarkWriteSlice1000Uint8s`
        - `BenchmarkWriteStruct`
        - `TestBlankFields`
        - `TestEarlyBoundsChecks`
        - `TestReadBool`
        - `TestReadBoolSlice`
        - `TestReadErrorMsg`
        - `TestReadInvalidDestination`
        - `TestReadSlice`
        - `TestReadTruncated`
        - `TestSizeStructCache`
        - `TestSliceRoundTrip`
        - `TestUnexportedRead`
        - `TestWriteSlice`
        - `TestWriteT`
        - `testPutUint64SmallSliceLengthPanics`
        - `testRead`
        - `testReadInvalidDestination`
        - `testUint64SmallSliceLengthPanics`
        - `testWrite`
    - Predicted Functions (0):

- **File:** `src/encoding/binary/varint_test.go`
    - Ground Truth Functions (11):
        - `BenchmarkPutUvarint32`
        - `BenchmarkPutUvarint64`
        - `TestBufferTooBigWithOverflow`
        - `TestBufferTooSmall`
        - `TestConstants`
        - `TestNonCanonicalZero`
        - `TestOverflow`
        - `testConstant`
        - `testOverflow`
        - `testUvarint`
        - `testVarint`
    - Predicted Functions (0):

- **File:** `src/runtime/debug/mod.go`
    - Ground Truth Functions (1):
        - `ReadBuildInfo`
    - Predicted Functions (0):


### 📊 **Proposal #52746 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `lib/time/mkzip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/vcs.go`
    - Ground Truth Functions (1):
        - `fossilParseStat`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vcs/vcs.go`
    - Ground Truth Functions (1):
        - `fossilStatus`
    - Predicted Functions (0):

- **File:** `src/runtime/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/time/format.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `AppendFormat`
        - ❌ `Format`
        - ❌ `Parse`

- **File:** `src/time/format_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `FuzzFormatRFC3339`
        - ❌ `FuzzParseRFC3339`
        - ❌ `TestFormat`
        - ❌ `TestFormatAndParse`
        - ❌ `TestParse`

- **File:** `src/time/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (24):
        - ❌ `Add`
        - ❌ `AddDate`
        - ❌ `Clock`
        - ❌ `Date`
        - ❌ `Day`
        - ❌ `Hour`
        - ❌ `ISOWeek`
        - ❌ `In`
        - ❌ `Local`
        - ❌ `Location`
        - ❌ `Minute`
        - ❌ `Month`
        - ❌ `Nanosecond`
        - ❌ `Parse`
        - ❌ `Second`
        - ❌ `Sub`
        - ❌ `UTC`
        - ❌ `Unix`
        - ❌ `UnixMicro`
        - ❌ `UnixMilli`
        - ❌ `UnixNano`
        - ❌ `Weekday`
        - ❌ `Year`
        - ❌ `Zone`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `BenchmarkFormat`
        - ❌ `BenchmarkFormatRFC3339`
        - ❌ `BenchmarkParse`
        - ❌ `BenchmarkParseRFC3339TZ`
        - ❌ `BenchmarkParseRFC3339UTC`


### 📊 **Proposal #46648 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.8% | 33.3% | 1.6% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/go/types/alias.go`
    - Ground Truth Functions (0):
    - Predicted Functions (15):
        - ❌ `NewAlias`
        - ❌ `Obj`
        - ❌ `Origin`
        - ❌ `Rhs`
        - ❌ `SetTypeParams`
        - ❌ `String`
        - ❌ `TypeArgs`
        - ❌ `TypeParams`
        - ❌ `Unalias`
        - ❌ `Underlying`
        - ❌ `asNamed`
        - ❌ `cleanup`
        - ❌ `newAlias`
        - ❌ `newAliasInstance`
        - ❌ `unalias`

- **File:** `src/go/types/api.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Check`

- **File:** `src/go/types/api_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestFileVersions`
        - ❌ `TestModuleVersion`
        - ❌ `TestTooNew`
        - ❌ `mustTypecheck`
        - ❌ `typecheck`

- **File:** `src/go/types/array.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/assignments.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/badlinkname.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/basic.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/builtins.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/builtins_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/call.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/chan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/check.go`
    - Ground Truth Functions (1):
        - `NewChecker`
    - Predicted Functions (4):
        - ✅ `NewChecker`
        - ❌ `checkFiles`
        - ❌ `cleanup`
        - ❌ `processDelayed`

- **File:** `src/go/types/check_test.go`
    - Ground Truth Functions (1):
        - `testFiles`
    - Predicted Functions (3):
        - ❌ `TestCheck`
        - ❌ `TestExamples`
        - ❌ `TestSpec`

- **File:** `src/go/types/commentMap_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/const.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/context.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/context_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/conversions.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/decl.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `constDecl`
        - ❌ `declare`
        - ❌ `funcDecl`
        - ❌ `typeDecl`
        - ❌ `varDecl`
        - ❌ `walkDecl`
        - ❌ `walkDecls`

- **File:** `src/go/types/errorcalls_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/errors.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `error`
        - ❌ `errorf`
        - ❌ `softErrorf`
        - ❌ `versionErrorf`

- **File:** `src/go/types/errors_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/errsupport.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/eval.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `CheckExpr`
        - ❌ `Eval`

- **File:** `src/go/types/eval_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestCheckExpr`

- **File:** `src/go/types/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/expr.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `expr`
        - ❌ `genericExpr`
        - ❌ `implicitTypeAndValue`
        - ❌ `newTarget`
        - ❌ `updateExprType`
        - ❌ `updateExprVal`

- **File:** `src/go/types/exprstring.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/exprstring_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/format.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/gccgosizes.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/gcsizes.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/generate.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Config`
        - ❌ `GetGoVersion`
        - ❌ `SetGoVersion`

- **File:** `src/go/types/generate_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/gotype.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `checkPkgFiles`
        - ❌ `initParserMode`
        - ❌ `parse`

- **File:** `src/go/types/hilbert_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/index.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/infer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/initorder.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/instantiate.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Instantiate`
        - ❌ `implements`
        - ❌ `instance`
        - ❌ `validateTArgLen`
        - ❌ `verify`

- **File:** `src/go/types/instantiate_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/interface.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `NewInterface`
        - ❌ `NewInterfaceType`
        - ❌ `interfaceType`

- **File:** `src/go/types/issues_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/iter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/labels.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/literals.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `basicLit`
        - ❌ `compositeLit`
        - ❌ `funcLit`
        - ❌ `indexedElts`
        - ❌ `langCompat`

- **File:** `src/go/types/lookup.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/lookup_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/main_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/map.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/methodset.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/methodset_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestIssue60634`
        - ❌ `TestNewMethodSet`
        - ❌ `TestNewMethodSet_RecursiveGeneric`

- **File:** `src/go/types/mono.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/mono_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/named.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `NewNamed`
        - ❌ `newNamed`
        - ❌ `newNamedInstance`

- **File:** `src/go/types/named_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/object.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `NewConst`
        - ❌ `NewField`
        - ❌ `NewFunc`
        - ❌ `NewParam`
        - ❌ `NewPkgName`
        - ❌ `NewTypeName`
        - ❌ `NewVar`

- **File:** `src/go/types/object_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/objset.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/operand.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/package.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `GoVersion`

- **File:** `src/go/types/pointer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/predicates.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `isGeneric`
        - ❌ `isTypeParam`
        - ❌ `isTyped`
        - ❌ `isUntyped`

- **File:** `src/go/types/range.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/recording.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/resolver.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/resolver_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/return.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/scope.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/scope2.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/scope2_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/selection.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/self_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/signature.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `NewSignature`
        - ❌ `NewSignatureType`
        - ❌ `Params`
        - ❌ `Recv`
        - ❌ `RecvTypeParams`
        - ❌ `Results`
        - ❌ `String`
        - ❌ `TypeParams`
        - ❌ `Underlying`
        - ❌ `Variadic`

- **File:** `src/go/types/sizeof_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/sizes.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Config`
        - ❌ `alignof`
        - ❌ `offsetof`
        - ❌ `offsetsof`
        - ❌ `sizeof`

- **File:** `src/go/types/sizes_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/slice.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/stdlib_test.go`
    - Ground Truth Functions (1):
        - `testTestDir`
    - Predicted Functions (0):

- **File:** `src/go/types/stmt.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `closeScope`
        - ❌ `funcBody`
        - ❌ `openScope`
        - ❌ `stmt`
        - ❌ `stmtList`

- **File:** `src/go/types/struct.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/subst.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/termlist.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/termlist_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/token_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/tuple.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Config`
        - ❌ `GetGoVersion`
        - ❌ `SetGoVersion`

- **File:** `src/go/types/typelists.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/typeparam.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/typeset.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/typeset_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/typestring.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/typestring_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/typeterm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/typeterm_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/typexpr.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `definedType`
        - ❌ `genericType`
        - ❌ `instantiatedType`
        - ❌ `typ`
        - ❌ `typInternal`
        - ❌ `validVarType`
        - ❌ `varType`

- **File:** `src/go/types/under.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/unify.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/union.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/universe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/util.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/util_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/validtype.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `validType`
        - ❌ `validType0`

- **File:** `src/go/types/version.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `allowVersion`
        - ❌ `asGoVersion`
        - ❌ `verifyVersionf`


### 📊 **Proposal #42710 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 37.5% | 25.0% | 30.0% | 3/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/hash/maphash/maphash.go`
    - Ground Truth Functions (9):
        - `Bytes`
        - `SetSeed`
        - `String`
        - `Sum64`
        - `Write`
        - `WriteByte`
        - `WriteString`
        - `flush`
        - `initSeed`
    - Predicted Functions (6):
        - ❌ `(*Hash) Sum64`
        - ❌ `(*Hash) Write`
        - ❌ `(*Hash) WriteString`
        - ✅ `Bytes`
        - ❌ `MakeSeed`
        - ✅ `String`

- **File:** `src/hash/maphash/maphash_test.go`
    - Ground Truth Functions (3):
        - `BenchmarkHash`
        - `TestHashGrouping`
        - `benchmarkSize`
    - Predicted Functions (2):
        - ✅ `BenchmarkHash`
        - ❌ `TestHashBytesVsString`


### 📊 **Proposal #37033 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 54.5% | 85.7% | 66.7% | 6/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/link/internal/ld/lib.go`
    - Ground Truth Functions (1):
        - `loadlib`
    - Predicted Functions (0):

- **File:** `src/runtime/cgo/cgo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Delete`
        - ❌ `MustDelete`
        - ❌ `MustValue`
        - ❌ `NewHandle`
        - ❌ `Value`

- **File:** `src/runtime/cgo/handle.go`
    - Ground Truth Functions (3):
        - `Delete`
        - `NewHandle`
        - `Value`
    - Predicted Functions (3):
        - ✅ `Delete`
        - ✅ `NewHandle`
        - ✅ `Value`

- **File:** `src/runtime/cgo/handle_test.go`
    - Ground Truth Functions (3):
        - `BenchmarkHandle`
        - `TestHandle`
        - `TestInvalidHandle`
    - Predicted Functions (3):
        - ✅ `BenchmarkHandle`
        - ✅ `TestHandle`
        - ✅ `TestInvalidHandle`

- **File:** `src/runtime/runtime.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #47142 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 31.2% | 20.8% | 25.0% | 5/24 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/database/sql/driver/driver.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/database/sql/fakedb_test.go`
    - Ground Truth Functions (12):
        - `Begin`
        - `Commit`
        - `Error`
        - `ExecContext`
        - `NumInput`
        - `PrepareContext`
        - `Query`
        - `QueryContext`
        - `ResetSession`
        - `Rollback`
        - `Unwrap`
        - `isDirtyAndMark`
    - Predicted Functions (0):

- **File:** `src/database/sql/sql.go`
    - Ground Truth Functions (11):
        - `BeginTx`
        - `Commit`
        - `Conn`
        - `ExecContext`
        - `PingContext`
        - `PrepareContext`
        - `QueryContext`
        - `closemuRUnlockCondReleaseConn`
        - `conn`
        - `putConn`
        - `rollback`
    - Predicted Functions (16):
        - ❌ `Close`
        - ✅ `Conn`
        - ❌ `Driver`
        - ❌ `Exec`
        - ✅ `ExecContext`
        - ❌ `Ping`
        - ✅ `PingContext`
        - ❌ `Prepare`
        - ✅ `PrepareContext`
        - ❌ `Query`
        - ✅ `QueryContext`
        - ❌ `QueryRow`
        - ❌ `QueryRowContext`
        - ❌ `grabConn`
        - ❌ `resetSession`
        - ❌ `validateConnection`

- **File:** `src/database/sql/sql_test.go`
    - Ground Truth Functions (1):
        - `TestTxEndBadConn`
    - Predicted Functions (0):


### 📊 **Proposal #53002 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 46.2% | 46.2% | 46.2% | 6/13 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/httputil/example_test.go`
    - Ground Truth Functions (1):
        - `ExampleReverseProxy`
    - Predicted Functions (0):

- **File:** `src/net/http/httputil/httputil.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `AppendXForwarded`
        - ❌ `ReverseProxy`
        - ❌ `SetURL`
        - ❌ `SetXForwarded`

- **File:** `src/net/http/httputil/reverseproxy.go`
    - Ground Truth Functions (9):
        - `NewSingleHostReverseProxy`
        - `ServeHTTP`
        - `SetURL`
        - `SetXForwarded`
        - `copyHeader`
        - `getErrorHandler`
        - `modifyResponse`
        - `removeHopByHopHeaders`
        - `rewriteRequestURL`
    - Predicted Functions (4):
        - ✅ `NewSingleHostReverseProxy`
        - ✅ `ServeHTTP`
        - ✅ `SetURL`
        - ✅ `SetXForwarded`

- **File:** `src/net/http/httputil/reverseproxy_test.go`
    - Ground Truth Functions (3):
        - `TestReverseProxyRewriteReplacesOut`
        - `TestReverseProxyRewriteStripsForwarded`
        - `TestSetURL`
    - Predicted Functions (5):
        - ❌ `AppendXForwarded`
        - ❌ `SetURL`
        - ❌ `SetXForwarded`
        - ✅ `TestReverseProxyRewriteReplacesOut`
        - ✅ `TestReverseProxyRewriteStripsForwarded`


### 📊 **Proposal #44815 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 50.0% | 16.7% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/bufio/bufio.go`
    - Ground Truth Functions (1):
        - `ReadFrom`
    - Predicted Functions (2):
        - ❌ `Flush`
        - ✅ `ReadFrom`

- **File:** `src/bufio/bufio_test.go`
    - Ground Truth Functions (3):
        - `ReadFrom`
        - `TestWriterReadFromWithBufferedData`
        - `Write`
    - Predicted Functions (5):
        - ❌ `TestWriterReadFrom`
        - ❌ `TestWriterReadFromCounts`
        - ❌ `TestWriterReadFromErrors`
        - ❌ `TestWriterReadFromWhileFull`
        - ✅ `TestWriterReadFromWithBufferedData`

- **File:** `src/io/fs/fs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/io/fs/fs_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/http.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `WriteTo`

- **File:** `src/net/http/request.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `MaxBytesReader`
        - ❌ `ParseForm`
        - ❌ `ParseMultipartForm`
        - ❌ `ReadRequest`
        - ❌ `Write`
        - ❌ `WriteProxy`
        - ❌ `readRequest`
        - ❌ `write`

- **File:** `src/net/http/response.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Write`

- **File:** `src/net/http/transfer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `doBodyCopy`
        - ❌ `writeBody`
        - ❌ `writeHeader`


### 📊 **Proposal #50436 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 34.8% | 37.2% | 8/23 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (17):
        - `CombinedOutput`
        - `CommandContext`
        - `Error`
        - `Start`
        - `StderrPipe`
        - `StdinPipe`
        - `StdoutPipe`
        - `Unwrap`
        - `Wait`
        - `argv`
        - `awaitGoroutines`
        - `childStderr`
        - `childStdin`
        - `childStdout`
        - `interfaceEqual`
        - `watchCtx`
        - `writerDescriptor`
    - Predicted Functions (10):
        - ✅ `CombinedOutput`
        - ❌ `Command`
        - ✅ `CommandContext`
        - ❌ `Output`
        - ❌ `Run`
        - ✅ `Start`
        - ✅ `StderrPipe`
        - ✅ `StdinPipe`
        - ✅ `StdoutPipe`
        - ✅ `Wait`

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (6):
        - `Read`
        - `TestCancelErrors`
        - `TestWaitInterrupt`
        - `cmdHang`
        - `newTickReader`
        - `startHang`
    - Predicted Functions (3):
        - ❌ `TestContext`
        - ❌ `TestContextCancel`
        - ✅ `TestWaitInterrupt`

- **File:** `src/os/exec_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `kill`
        - ❌ `setInterruptSignal`
        - ❌ `setWaitDelay`
        - ❌ `startProcess`
        - ❌ `wait`

- **File:** `src/os/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `signal`
        - ❌ `wait`


### 📊 **Proposal #44505 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/asm/internal/lex/tokenizer.go`
    - Ground Truth Functions (1):
        - `Next`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (2):
        - `cmdbootstrap`
        - `findgoversion`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/buildtool.go`
    - Ground Truth Functions (1):
        - `bootstrapBuildTools`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `makeGOROOTUnwritable`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/util.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/sort/slice.go`
    - Ground Truth Functions (3):
        - `Slice`
        - `SliceIsSorted`
        - `SliceStable`
    - Predicted Functions (0):

- **File:** `test/fixedbugs/issue23536.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #53021 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 11.1% | 20.0% | 1/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/bytes/bytes.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/cipher/cbc.go`
    - Ground Truth Functions (1):
        - `CryptBlocks`
    - Predicted Functions (0):

- **File:** `src/crypto/cipher/cfb.go`
    - Ground Truth Functions (1):
        - `XORKeyStream`
    - Predicted Functions (0):

- **File:** `src/crypto/cipher/ctr.go`
    - Ground Truth Functions (1):
        - `XORKeyStream`
    - Predicted Functions (0):

- **File:** `src/crypto/cipher/ofb.go`
    - Ground Truth Functions (1):
        - `XORKeyStream`
    - Predicted Functions (0):

- **File:** `src/crypto/subtle/xor.go`
    - Ground Truth Functions (1):
        - `XORBytes`
    - Predicted Functions (1):
        - ✅ `XORBytes`

- **File:** `src/crypto/subtle/xor_test.go`
    - Ground Truth Functions (4):
        - `BenchmarkXORBytes`
        - `TestXORBytes`
        - `TestXorBytesPanic`
        - `mustPanic`
    - Predicted Functions (0):


### 📊 **Proposal #33232 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/389 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/reader_test.go`
    - Ground Truth Functions (1):
        - `TestFileReader`
    - Predicted Functions (0):

- **File:** `src/archive/tar/writer_test.go`
    - Ground Truth Functions (2):
        - `TestFileWriter`
        - `TestWriter`
    - Predicted Functions (0):

- **File:** `src/builtin/builtin.go`
    - Ground Truth Functions (2):
        - `panic`
        - `recover`
    - Predicted Functions (0):

- **File:** `src/bytes/reader_test.go`
    - Ground Truth Functions (1):
        - `TestReaderAt`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/asm/endtoend_test.go`
    - Ground Truth Functions (2):
        - `testEndToEnd`
        - `testErrors`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/asm/parse.go`
    - Ground Truth Functions (1):
        - `errorf`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/gcc.go`
    - Ground Truth Functions (2):
        - `loadType`
        - `mangle`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/out.go`
    - Ground Truth Functions (1):
        - `writeExports`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/base/timings.go`
    - Ground Truth Functions (1):
        - `add`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/importer/testdata/exports.go`
    - Ground Truth Functions (1):
        - `F5`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/copyelim_test.go`
    - Ground Truth Functions (1):
        - `benchmarkCopyElim`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssagen/ssa.go`
    - Ground Truth Functions (1):
        - `Fatalf`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/syntax/printer.go`
    - Ground Truth Functions (1):
        - `printRawNode`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/test/iface_test.go`
    - Ground Truth Functions (4):
        - `TestEfaceConv1`
        - `TestEfaceConv2`
        - `TestIfaceConv1`
        - `TestIfaceConv2`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/test/shift_test.go`
    - Ground Truth Functions (1):
        - `TestShiftGeneric`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/test/testdata/compound_test.go`
    - Ground Truth Functions (2):
        - `interface_ssa`
        - `testInterface`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/expr.go`
    - Ground Truth Functions (1):
        - `exprInternal`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/subst.go`
    - Ground Truth Functions (1):
        - `typ`
    - Predicted Functions (0):

- **File:** `src/cmd/cover/testdata/test.go`
    - Ground Truth Functions (2):
        - `testEmptySwitches`
        - `testTypeSwitch`
    - Predicted Functions (0):

- **File:** `src/cmd/doc/pkg.go`
    - Ground Truth Functions (1):
        - `emit`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/cftype.go`
    - Ground Truth Functions (1):
        - `typefix`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/fix.go`
    - Ground Truth Functions (1):
        - `renameTop`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/gotypes.go`
    - Ground Truth Functions (1):
        - `fixGoExact`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/netipv6zone.go`
    - Ground Truth Functions (1):
        - `netipv6zone`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/printerconfig.go`
    - Ground Truth Functions (1):
        - `printerconfig`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/typecheck.go`
    - Ground Truth Functions (2):
        - `typecheck`
        - `typecheck1`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cmdflag/flag.go`
    - Ground Truth Functions (1):
        - `ParseOne`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/list/list.go`
    - Ground Truth Functions (1):
        - `runList`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/pkg.go`
    - Ground Truth Functions (3):
        - `goModPath`
        - `isDir`
        - `loadPackageData`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/cache.go`
    - Ground Truth Functions (4):
        - `GoMod`
        - `Latest`
        - `Stat`
        - `Versions`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/git.go`
    - Ground Truth Functions (1):
        - `Stat`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/vcs.go`
    - Ground Truth Functions (1):
        - `NewRepo`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/coderepo.go`
    - Ground Truth Functions (1):
        - `convert`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/fetch.go`
    - Ground Truth Functions (2):
        - `Download`
        - `DownloadZip`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/repo.go`
    - Ground Truth Functions (1):
        - `Lookup`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modget/get.go`
    - Ground Truth Functions (2):
        - `checkWildcardVersions`
        - `matchInModule`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/buildlist.go`
    - Ground Truth Functions (1):
        - `readModGraph`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/import.go`
    - Ground Truth Functions (1):
        - `dirInModule`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/load.go`
    - Ground Truth Functions (1):
        - `pkg`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/modfile.go`
    - Ground Truth Functions (2):
        - `queryLatestVersionIgnoringRetractions`
        - `rawGoModSummary`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/vendor.go`
    - Ground Truth Functions (1):
        - `checkVendorConsistency`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/mvs/mvs.go`
    - Ground Truth Functions (1):
        - `buildList`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vcs/vcs.go`
    - Ground Truth Functions (1):
        - `metaImportsForPrefix`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/build_test.go`
    - Ground Truth Functions (1):
        - `TestRespectSetgidDir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (1):
        - `gccld`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (3):
        - `asmArgs`
        - `gc`
        - `toolVerify`
    - Predicted Functions (0):

- **File:** `src/cmd/go/proxy_test.go`
    - Ground Truth Functions (2):
        - `proxyHandler`
        - `readArchive`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/buildid/buildid_test.go`
    - Ground Truth Functions (1):
        - `TestFindAndHash`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/link.go`
    - Ground Truth Functions (2):
        - `NewFileInfo`
        - `NewFuncInfo`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/pcln.go`
    - Ground Truth Functions (1):
        - `linkpcln`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/test2json/test2json_test.go`
    - Ground Truth Functions (1):
        - `diffJSON`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/testdata/deadcode/reflectcall.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/loadelf/ldelf.go`
    - Ground Truth Functions (1):
        - `Load`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/loadmacho/ldmacho.go`
    - Ground Truth Functions (1):
        - `Load`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/loadxcoff/ldxcoff.go`
    - Ground Truth Functions (1):
        - `Load`
    - Predicted Functions (0):

- **File:** `src/cmd/pack/pack_test.go`
    - Ground Truth Functions (1):
        - `TestLargeDefs`
    - Predicted Functions (0):

- **File:** `src/container/list/list_test.go`
    - Ground Truth Functions (5):
        - `TestExtending`
        - `TestInsertAfterUnknownMark`
        - `TestInsertBeforeUnknownMark`
        - `TestMoveUnknownMark`
        - `TestZeroList`
    - Predicted Functions (0):

- **File:** `src/container/ring/example_test.go`
    - Ground Truth Functions (4):
        - `ExampleRing_Do`
        - `ExampleRing_Link`
        - `ExampleRing_Move`
        - `ExampleRing_Unlink`
    - Predicted Functions (0):

- **File:** `src/container/ring/ring_test.go`
    - Ground Truth Functions (1):
        - `verify`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/generate_cert.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (1):
        - `establishKeys`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_client_test.go`
    - Ground Truth Functions (1):
        - `connFromCommand`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server.go`
    - Ground Truth Functions (1):
        - `establishKeys`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server_test.go`
    - Ground Truth Functions (3):
        - `TestTLS12OnlyCipherSuites`
        - `TestTLSPointFormats`
        - `connFromCommand`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/name_constraints_test.go`
    - Ground Truth Functions (1):
        - `TestConstraintCases`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/verify.go`
    - Ground Truth Functions (2):
        - `checkNameConstraints`
        - `isValid`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (3):
        - `TestCRLCreation`
        - `TestCreateCertificateRequest`
        - `TestCreateSelfSignedCertificate`
    - Predicted Functions (0):

- **File:** `src/database/sql/convert.go`
    - Ground Truth Functions (1):
        - `convertAssignRows`
    - Predicted Functions (0):

- **File:** `src/database/sql/convert_test.go`
    - Ground Truth Functions (4):
        - `TestConversions`
        - `TestDriverArgs`
        - `TestRawBytesAllocs`
        - `conversionTests`
    - Predicted Functions (0):

- **File:** `src/database/sql/fakedb_test.go`
    - Ground Truth Functions (4):
        - `QueryContext`
        - `colTypeToReflectType`
        - `execInsert`
        - `prepareInsert`
    - Predicted Functions (0):

- **File:** `src/database/sql/sql.go`
    - Ground Truth Functions (1):
        - `rowsColumnInfoSetupConnLocked`
    - Predicted Functions (0):

- **File:** `src/database/sql/sql_test.go`
    - Ground Truth Functions (6):
        - `TestConnIsValid`
        - `TestConnRaw`
        - `TestExec`
        - `TestInvalidNilValues`
        - `TestNamedValueChecker`
        - `TestRowsColumnTypes`
    - Predicted Functions (0):

- **File:** `src/debug/dwarf/entry.go`
    - Ground Truth Functions (1):
        - `entry`
    - Predicted Functions (0):

- **File:** `src/debug/dwarf/entry_test.go`
    - Ground Truth Functions (1):
        - `TestUnitIteration`
    - Predicted Functions (0):

- **File:** `src/debug/pe/file.go`
    - Ground Truth Functions (1):
        - `readOptionalHeader`
    - Predicted Functions (0):

- **File:** `src/embed/internal/embedtest/embed_test.go`
    - Ground Truth Functions (1):
        - `TestAliases`
    - Predicted Functions (0):

- **File:** `src/encoding/asn1/asn1.go`
    - Ground Truth Functions (1):
        - `parseField`
    - Predicted Functions (0):

- **File:** `src/encoding/asn1/asn1_test.go`
    - Ground Truth Functions (2):
        - `TestMarshalNilValue`
        - `TestUnmarshalWithNilOrNonPointer`
    - Predicted Functions (0):

- **File:** `src/encoding/asn1/marshal_test.go`
    - Ground Truth Functions (2):
        - `BenchmarkUnmarshal`
        - `TestIssue11130`
    - Predicted Functions (0):

- **File:** `src/encoding/binary/binary_test.go`
    - Ground Truth Functions (3):
        - `TestReadErrorMsg`
        - `TestSizeStructCache`
        - `testReadInvalidDestination`
    - Predicted Functions (0):

- **File:** `src/encoding/binary/example_test.go`
    - Ground Truth Functions (1):
        - `ExampleWrite_multi`
    - Predicted Functions (0):

- **File:** `src/encoding/gob/codec_test.go`
    - Ground Truth Functions (2):
        - `TestFuzz`
        - `encFuzzDec`
    - Predicted Functions (0):

- **File:** `src/encoding/gob/encoder_test.go`
    - Ground Truth Functions (7):
        - `Test29ElementSlice`
        - `TestBasicEncoderDecoder`
        - `TestGobMapInterfaceEncode`
        - `TestNestedInterfaces`
        - `TestNilPointerInsideInterface`
        - `TestNilPointerPanics`
        - `TestPtrToMapOfMap`
    - Predicted Functions (0):

- **File:** `src/encoding/gob/timing_test.go`
    - Ground Truth Functions (5):
        - `BenchmarkDecodeInterfaceSlice`
        - `BenchmarkEncodeInterfaceSlice`
        - `BenchmarkEndToEndByteBuffer`
        - `BenchmarkEndToEndPipe`
        - `BenchmarkEndToEndSliceByteBuffer`
    - Predicted Functions (0):

- **File:** `src/encoding/gob/type_test.go`
    - Ground Truth Functions (2):
        - `TestRegistrationNaming`
        - `TestTypeRace`
    - Predicted Functions (0):

- **File:** `src/encoding/json/bench_test.go`
    - Ground Truth Functions (1):
        - `BenchmarkDecoderStream`
    - Predicted Functions (0):

- **File:** `src/encoding/json/decode.go`
    - Ground Truth Functions (2):
        - `arrayInterface`
        - `objectInterface`
    - Predicted Functions (0):

- **File:** `src/encoding/json/decode_test.go`
    - Ground Truth Functions (11):
        - `TestInterfaceSet`
        - `TestInvalidStringOption`
        - `TestPrefilled`
        - `TestSkipArrayObjects`
        - `TestUnmarshalEmbeddedUnexported`
        - `TestUnmarshalErrorAfterMultipleJSON`
        - `TestUnmarshalInterface`
        - `TestUnmarshalMarshal`
        - `TestUnmarshalMaxDepth`
        - `TestUnmarshalRecursivePointer`
        - `TestUnmarshalSyntax`
    - Predicted Functions (0):

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (1):
        - `newEncodeState`
    - Predicted Functions (0):

- **File:** `src/encoding/json/encode_test.go`
    - Ground Truth Functions (7):
        - `TestAnonymousFields`
        - `TestEncodeBytekind`
        - `TestMarshalFloat`
        - `TestMarshalRawMessageValue`
        - `TestNilMarshal`
        - `TestOmitEmpty`
        - `init`
    - Predicted Functions (0):

- **File:** `src/encoding/json/example_test.go`
    - Ground Truth Functions (1):
        - `ExampleRawMessage_unmarshal`
    - Predicted Functions (0):

- **File:** `src/encoding/json/scanner_test.go`
    - Ground Truth Functions (2):
        - `genArray`
        - `genMap`
    - Predicted Functions (0):

- **File:** `src/encoding/json/stream.go`
    - Ground Truth Functions (1):
        - `Token`
    - Predicted Functions (0):

- **File:** `src/encoding/json/stream_test.go`
    - Ground Truth Functions (4):
        - `TestBlocking`
        - `TestDecodeInStream`
        - `TestDecoder`
        - `TestEncoderSetEscapeHTML`
    - Predicted Functions (0):

- **File:** `src/encoding/json/tagkey_test.go`
    - Ground Truth Functions (1):
        - `TestStructTagObjectKey`
    - Predicted Functions (0):

- **File:** `src/encoding/json/v2/arshal_any.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `marshalArrayAny`
        - ❌ `marshalObjectAny`
        - ❌ `marshalValueAny`
        - ❌ `unmarshalArrayAny`
        - ❌ `unmarshalObjectAny`
        - ❌ `unmarshalValueAny`

- **File:** `src/encoding/xml/marshal_test.go`
    - Ground Truth Functions (2):
        - `TestEncodeToken`
        - `TestStructPointerMarshal`
    - Predicted Functions (0):

- **File:** `src/errors/wrap.go`
    - Ground Truth Functions (1):
        - `As`
    - Predicted Functions (0):

- **File:** `src/errors/wrap_test.go`
    - Ground Truth Functions (2):
        - `TestAs`
        - `TestAsValidation`
    - Predicted Functions (0):

- **File:** `src/expvar/expvar.go`
    - Ground Truth Functions (1):
        - `Init`
    - Predicted Functions (0):

- **File:** `src/expvar/expvar_test.go`
    - Ground Truth Functions (2):
        - `TestFunc`
        - `TestMapCounter`
    - Predicted Functions (0):

- **File:** `src/fmt/fmt_test.go`
    - Ground Truth Functions (4):
        - `BenchmarkFprintIntNoAlloc`
        - `BenchmarkSprintfStructure`
        - `BenchmarkSprintfTruncateBytes`
        - `TestFmtInterface`
    - Predicted Functions (0):

- **File:** `src/fmt/scan_test.go`
    - Ground Truth Functions (1):
        - `testScanfMulti`
    - Predicted Functions (0):

- **File:** `src/go/ast/print.go`
    - Ground Truth Functions (1):
        - `fprint`
    - Predicted Functions (0):

- **File:** `src/go/doc/testdata/benchmark.go`
    - Ground Truth Functions (2):
        - `Benchmark`
        - `RunBenchmarks`
    - Predicted Functions (0):

- **File:** `src/go/doc/testdata/testing.go`
    - Ground Truth Functions (1):
        - `RunTests`
    - Predicted Functions (0):

- **File:** `src/go/internal/gcimporter/testdata/exports.go`
    - Ground Truth Functions (1):
        - `F5`
    - Predicted Functions (0):

- **File:** `src/go/token/serialize_test.go`
    - Ground Truth Functions (1):
        - `checkSerialize`
    - Predicted Functions (0):

- **File:** `src/go/types/expr.go`
    - Ground Truth Functions (1):
        - `exprInternal`
    - Predicted Functions (0):

- **File:** `src/go/types/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/go/types/subst.go`
    - Ground Truth Functions (1):
        - `typ`
    - Predicted Functions (0):

- **File:** `src/html/template/content_test.go`
    - Ground Truth Functions (2):
        - `TestEscapingNilNonemptyInterfaces`
        - `TestTypedContent`
    - Predicted Functions (0):

- **File:** `src/html/template/escape_test.go`
    - Ground Truth Functions (3):
        - `TestEscape`
        - `TestEscapeSet`
        - `TestRedundantFuncs`
    - Predicted Functions (0):

- **File:** `src/html/template/example_test.go`
    - Ground Truth Functions (1):
        - `Example_escape`
    - Predicted Functions (0):

- **File:** `src/html/template/exec_test.go`
    - Ground Truth Functions (4):
        - `TestEvalFieldErrors`
        - `TestExecutePanicDuringCall`
        - `TestInterfaceValues`
        - `TestTemplateFuncsAfterClone`
    - Predicted Functions (0):

- **File:** `src/html/template/js.go`
    - Ground Truth Functions (1):
        - `jsValEscaper`
    - Predicted Functions (0):

- **File:** `src/html/template/js_test.go`
    - Ground Truth Functions (4):
        - `TestEscapersOnLower7AndSelectHighCodepoints`
        - `TestJSRegexpEscaper`
        - `TestJSStrEscaper`
        - `TestJSValEscaper`
    - Predicted Functions (0):

- **File:** `src/html/template/url_test.go`
    - Ground Truth Functions (1):
        - `TestURLFilters`
    - Predicted Functions (0):

- **File:** `src/internal/fmtsort/sort_test.go`
    - Ground Truth Functions (1):
        - `TestInterface`
    - Predicted Functions (0):

- **File:** `src/internal/reflectlite/all_test.go`
    - Ground Truth Functions (6):
        - `TestAllocations`
        - `TestFunctionValue`
        - `TestImportPath`
        - `TestInterfaceValue`
        - `TestInvalid`
        - `TestIsNil`
    - Predicted Functions (0):

- **File:** `src/internal/reflectlite/value.go`
    - Ground Truth Functions (5):
        - `Elem`
        - `assignTo`
        - `ifaceE2I`
        - `packEface`
        - `valueInterface`
    - Predicted Functions (0):

- **File:** `src/internal/singleflight/singleflight_test.go`
    - Ground Truth Functions (3):
        - `TestDo`
        - `TestDoDupSuppress`
        - `TestDoErr`
    - Predicted Functions (0):

- **File:** `src/math/big/floatconv_test.go`
    - Ground Truth Functions (1):
        - `TestFloatFormat`
    - Predicted Functions (0):

- **File:** `src/math/bits/make_examples.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/math/rand/example_test.go`
    - Ground Truth Functions (1):
        - `Example_rand`
    - Predicted Functions (0):

- **File:** `src/math/rand/regress_test.go`
    - Ground Truth Functions (1):
        - `TestRegress`
    - Predicted Functions (0):

- **File:** `src/mime/quotedprintable/reader_test.go`
    - Ground Truth Functions (2):
        - `TestExhaustive`
        - `TestReader`
    - Predicted Functions (0):

- **File:** `src/net/http/clientserver_test.go`
    - Ground Truth Functions (2):
        - `TestBidiStreamReverseProxy`
        - `TestH12_AutoGzip_Disabled`
    - Predicted Functions (0):

- **File:** `src/net/http/h2_bundle.go`
    - Ground Truth Functions (2):
        - `ServeConn`
        - `http2h1ServerKeepAlivesDisabled`
    - Predicted Functions (0):

- **File:** `src/net/http/httptrace/trace.go`
    - Ground Truth Functions (1):
        - `WithClientTrace`
    - Predicted Functions (0):

- **File:** `src/net/http/response_test.go`
    - Ground Truth Functions (2):
        - `TestReadResponseCloseInMiddle`
        - `TestReadResponseErrors`
    - Predicted Functions (0):

- **File:** `src/net/http/roundtrip_js.go`
    - Ground Truth Functions (2):
        - `Read`
        - `RoundTrip`
    - Predicted Functions (0):

- **File:** `src/net/http/serve_test.go`
    - Ground Truth Functions (4):
        - `TestRequestBodyTimeoutClosesConnection`
        - `testContentEncodingNoSniffing`
        - `testServerContext_LocalAddrContextKey`
        - `testTransportAndServerSharedBodyRace`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (0):

- **File:** `src/net/http/transport.go`
    - Ground Truth Functions (1):
        - `logf`
    - Predicted Functions (0):

- **File:** `src/net/http/transport_test.go`
    - Ground Truth Functions (5):
        - `TestRetryRequestsOnError`
        - `TestTransportEventTraceRealDNS`
        - `TestTransportEventTraceTLSVerify`
        - `TestTransportServerClosingUnexpectedly`
        - `testTransportEventTrace`
    - Predicted Functions (0):

- **File:** `src/net/lookup.go`
    - Ground Truth Functions (2):
        - `ipAddrsEface`
        - `lookupIPAddr`
    - Predicted Functions (0):

- **File:** `src/net/lookup_test.go`
    - Ground Truth Functions (1):
        - `TestLookupIPAddrPreservesContextValues`
    - Predicted Functions (0):

- **File:** `src/net/rpc/debug.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (0):

- **File:** `src/net/rpc/jsonrpc/server.go`
    - Ground Truth Functions (1):
        - `ReadRequestBody`
    - Predicted Functions (0):

- **File:** `src/net/url/url_test.go`
    - Ground Truth Functions (1):
        - `ufmt`
    - Predicted Functions (0):

- **File:** `src/os/user/lookup_unix.go`
    - Ground Truth Functions (2):
        - `matchGroupIndexValue`
        - `matchUserIndexValue`
    - Predicted Functions (0):

- **File:** `src/plugin/plugin_dlopen.go`
    - Ground Truth Functions (2):
        - `lastmoduleinit`
        - `open`
    - Predicted Functions (0):

- **File:** `src/reflect/abi_test.go`
    - Ground Truth Functions (1):
        - `TestMethodValueCallABI`
    - Predicted Functions (0):

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (29):
        - `TestAllocations`
        - `TestArrayOf`
        - `TestArrayOfGC`
        - `TestChanOfGC`
        - `TestExported`
        - `TestFuncLayout`
        - `TestFuncOf`
        - `TestFunctionValue`
        - `TestGCBits`
        - `TestImportPath`
        - `TestInterfaceExtraction`
        - `TestInterfaceGet`
        - `TestInterfaceSet`
        - `TestInterfaceValue`
        - `TestInvalid`
        - `TestIsNil`
        - `TestIsZero`
        - `TestMapIterSet`
        - `TestMapOfGCKeys`
        - `TestMapOfGCValues`
        - `TestMethod5`
        - `TestPtrToGC`
        - `TestSliceOfGC`
        - `TestStructOf`
        - `TestStructOfGC`
        - `TestStructOfWithInterface`
        - `TestSwapper`
        - `TestVariadic`
        - `init`
    - Predicted Functions (0):

- **File:** `src/reflect/example_test.go`
    - Ground Truth Functions (2):
        - `ExampleKind`
        - `ExampleMakeFunc`
    - Predicted Functions (0):

- **File:** `src/reflect/export_test.go`
    - Ground Truth Functions (1):
        - `gcbits`
    - Predicted Functions (0):

- **File:** `src/reflect/set_test.go`
    - Ground Truth Functions (1):
        - `TestImplicitMapConversion`
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (7):
        - `ArrayOf`
        - `ChanOf`
        - `FuncOf`
        - `SliceOf`
        - `StructOf`
        - `funcLayout`
        - `ptrTo`
    - Predicted Functions (0):

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (6):
        - `Elem`
        - `assignTo`
        - `cvtT2I`
        - `ifaceE2I`
        - `packEface`
        - `valueInterface`
    - Predicted Functions (0):

- **File:** `src/runtime/abi_test.go`
    - Ground Truth Functions (1):
        - `TestFinalizerRegisterABI`
    - Predicted Functions (0):

- **File:** `src/runtime/cgo/handle_test.go`
    - Ground Truth Functions (1):
        - `TestHandle`
    - Predicted Functions (0):

- **File:** `src/runtime/chan_test.go`
    - Ground Truth Functions (1):
        - `TestChanSendInterface`
    - Predicted Functions (0):

- **File:** `src/runtime/debugcall.go`
    - Ground Truth Functions (1):
        - `debugCallPanicked`
    - Predicted Functions (0):

- **File:** `src/runtime/gcinfo_test.go`
    - Ground Truth Functions (1):
        - `TestGCInfo`
    - Predicted Functions (0):

- **File:** `src/runtime/iface_test.go`
    - Ground Truth Functions (6):
        - `BenchmarkAssertE2E2`
        - `BenchmarkAssertE2E2Blank`
        - `BenchmarkAssertI2E`
        - `BenchmarkAssertI2E2`
        - `BenchmarkAssertI2E2Blank`
        - `TestNonEscapingConvT2E`
    - Predicted Functions (0):

- **File:** `src/runtime/malloc_test.go`
    - Ground Truth Functions (1):
        - `TestMemStats`
    - Predicted Functions (0):

- **File:** `src/runtime/map_benchmark_test.go`
    - Ground Truth Functions (2):
        - `BenchmarkMapInterfacePtr`
        - `BenchmarkMapInterfaceString`
    - Predicted Functions (0):

- **File:** `src/runtime/map_test.go`
    - Ground Truth Functions (2):
        - `TestDeferDeleteSlow`
        - `TestMapInterfaceKey`
    - Predicted Functions (0):

- **File:** `src/runtime/mfinal_test.go`
    - Ground Truth Functions (2):
        - `TestFinalizerInterfaceBig`
        - `TestFinalizerType`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcscavenge.go`
    - Ground Truth Functions (1):
        - `bgscavenge`
    - Predicted Functions (0):

- **File:** `src/runtime/os_windows.go`
    - Ground Truth Functions (2):
        - `goenvs`
        - `monitorSuspendResume`
    - Predicted Functions (0):

- **File:** `src/runtime/plugin.go`
    - Ground Truth Functions (1):
        - `plugin_lastmoduleinit`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/pprof.go`
    - Ground Truth Functions (1):
        - `NewProfile`
    - Predicted Functions (0):

- **File:** `src/runtime/race/race_test.go`
    - Ground Truth Functions (1):
        - `TestIssue8102`
    - Predicted Functions (0):

- **File:** `src/runtime/race/testdata/issue12664_test.go`
    - Ground Truth Functions (1):
        - `TestRaceIssue12664_3`
    - Predicted Functions (0):

- **File:** `src/runtime/race/testdata/mop_test.go`
    - Ground Truth Functions (8):
        - `TestRaceCaseType`
        - `TestRaceCaseTypeBody`
        - `TestRaceCaseTypeIssue5890`
        - `TestRaceEfaceConv`
        - `TestRaceEfaceWW`
        - `TestRaceEmptyInterface1`
        - `TestRaceEmptyInterface2`
        - `TestRaceTypeAssert`
    - Predicted Functions (0):

- **File:** `src/runtime/race/testdata/pool_test.go`
    - Ground Truth Functions (2):
        - `TestNoRacePool`
        - `TestRacePool`
    - Predicted Functions (0):

- **File:** `src/runtime/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/strings/reader_test.go`
    - Ground Truth Functions (1):
        - `TestReaderAt`
    - Predicted Functions (0):

- **File:** `src/sync/atomic/value.go`
    - Ground Truth Functions (1):
        - `CompareAndSwap`
    - Predicted Functions (0):

- **File:** `src/sync/atomic/value_test.go`
    - Ground Truth Functions (1):
        - `TestValueConcurrent`
    - Predicted Functions (0):

- **File:** `src/sync/map.go`
    - Ground Truth Functions (4):
        - `delete`
        - `dirtyLocked`
        - `load`
        - `tryLoadOrStore`
    - Predicted Functions (0):

- **File:** `src/sync/map_reference_test.go`
    - Ground Truth Functions (5):
        - `Load`
        - `LoadOrStore`
        - `Range`
        - `Store`
        - `dirty`
    - Predicted Functions (0):

- **File:** `src/sync/map_test.go`
    - Ground Truth Functions (2):
        - `TestConcurrentRange`
        - `applyCalls`
    - Predicted Functions (0):

- **File:** `src/sync/pool_test.go`
    - Ground Truth Functions (4):
        - `BenchmarkPoolExpensiveNew`
        - `BenchmarkPoolSTW`
        - `TestPoolNew`
        - `TestPoolStress`
    - Predicted Functions (0):

- **File:** `src/sync/poolqueue.go`
    - Ground Truth Functions (3):
        - `popHead`
        - `popTail`
        - `pushHead`
    - Predicted Functions (0):

- **File:** `src/syscall/fs_js.go`
    - Ground Truth Functions (1):
        - `fsCall`
    - Predicted Functions (0):

- **File:** `src/syscall/js/js.go`
    - Ground Truth Functions (1):
        - `ValueOf`
    - Predicted Functions (0):

- **File:** `src/syscall/js/js_test.go`
    - Ground Truth Functions (5):
        - `ExampleFuncOf`
        - `TestFuncOf`
        - `TestGlobal`
        - `TestInterleavedFunctions`
        - `TestInvokeFunction`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (1):
        - `compileCallback`
    - Predicted Functions (0):

- **File:** `src/testing/quick/quick.go`
    - Ground Truth Functions (1):
        - `toInterfaces`
    - Predicted Functions (0):

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (1):
        - `tRunner`
    - Predicted Functions (0):

- **File:** `src/text/template/exec_test.go`
    - Ground Truth Functions (3):
        - `TestEvalFieldErrors`
        - `TestExecutePanicDuringCall`
        - `TestInterfaceValues`
    - Predicted Functions (0):


### 📊 **Proposal #40481 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 5.9% | 10.0% | 1/17 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/ir/expr.go`
    - Ground Truth Functions (1):
        - `SetOp`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/fmt.go`
    - Ground Truth Functions (1):
        - `exprFmt`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/op_string.go`
    - Ground Truth Functions (1):
        - `_`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssagen/ssa.go`
    - Ground Truth Functions (1):
        - `expr`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/builtin.go`
    - Ground Truth Functions (1):
        - `runtimeTypes`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/func.go`
    - Ground Truth Functions (3):
        - `tcCall`
        - `tcUnsafeAdd`
        - `tcUnsafeSlice`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/typecheck.go`
    - Ground Truth Functions (1):
        - `typecheck1`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/builtin.go`
    - Ground Truth Functions (1):
        - `walkUnsafeSlice`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/expr.go`
    - Ground Truth Functions (1):
        - `walkExpr1`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/autotype.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/flag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/funcid.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/path.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/reloctype.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/symkind.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/elf.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/goobj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/macho.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/objfile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/pe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/plan9obj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/xcoff.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/builtins.go`
    - Ground Truth Functions (1):
        - `builtin`
    - Predicted Functions (0):

- **File:** `src/runtime/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `reflect_unsafeslice`
        - ❌ `unsafeslice`

- **File:** `src/unsafe/unsafe.go`
    - Ground Truth Functions (2):
        - `Add`
        - `Slice`
    - Predicted Functions (1):
        - ✅ `Add`

- **File:** `test/unsafebuiltins.go`
    - Ground Truth Functions (3):
        - `assert`
        - `main`
        - `mustPanic`
    - Predicted Functions (0):


### 📊 **Proposal #42681 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/asm/internal/lex/input.go`
    - Ground Truth Functions (1):
        - `predefine`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (2):
        - `runInstall`
        - `xinit`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/buildruntime.go`
    - Ground Truth Functions (1):
        - `mkzversion`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (2):
        - `buildActionID`
        - `printLinkerConfig`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (1):
        - `asmArgs`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/util.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Fieldtrack_enabled`
        - ❌ `Preemptibleloops_enabled`
        - ❌ `Regabi_enabled`
        - ❌ `Staticlockranking_enabled`

- **File:** `src/cmd/link/internal/ld/main.go`
    - Ground Truth Functions (1):
        - `Main`
    - Predicted Functions (0):

- **File:** `src/runtime/heapdump.go`
    - Ground Truth Functions (1):
        - `dumpparams`
    - Predicted Functions (0):


### 📊 **Proposal #50842 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 4/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/io/io.go`
    - Ground Truth Functions (3):
        - `Copy`
        - `CopyBuffer`
        - `copyBuffer`
    - Predicted Functions (5):
        - ❌ `(*OffsetWriter) WriteTo`
        - ❌ `(*nopCloserWriterTo) WriteTo`
        - ✅ `Copy`
        - ✅ `CopyBuffer`
        - ❌ `CopyN`

- **File:** `src/io/multi.go`
    - Ground Truth Functions (2):
        - `WriteTo`
        - `writeToWithBuffer`
    - Predicted Functions (3):
        - ❌ `MultiReader`
        - ✅ `WriteTo`
        - ✅ `writeToWithBuffer`

- **File:** `src/io/multi_test.go`
    - Ground Truth Functions (1):
        - `TestMultiReaderAsWriterTo`
    - Predicted Functions (0):


### 📊 **Proposal #27628 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/30 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/cache/hash.go`
    - Ground Truth Functions (1):
        - `Subkey`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/buildid.go`
    - Ground Truth Functions (4):
        - `flushOutput`
        - `showStdout`
        - `updateBuildID`
        - `useCache`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (16):
        - `build`
        - `ccompile`
        - `cgo`
        - `cover`
        - `dynimport`
        - `gcc`
        - `gccld`
        - `getPkgConfigFlags`
        - `gfortran`
        - `gxx`
        - `ld`
        - `link`
        - `linkShared`
        - `swig`
        - `swigOne`
        - `vet`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (5):
        - `asm`
        - `ld`
        - `ldShared`
        - `pack`
        - `toolVerify`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/gccgo.go`
    - Ground Truth Functions (4):
        - `asm`
        - `cc`
        - `link`
        - `pack`
    - Predicted Functions (0):


### 📊 **Proposal #47209 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 4/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/fsys/fsys_test.go`
    - Ground Truth Functions (1):
        - `TestWalkSkipAll`
    - Predicted Functions (0):

- **File:** `src/io/fs/walk.go`
    - Ground Truth Functions (1):
        - `WalkDir`
    - Predicted Functions (0):

- **File:** `src/path/filepath/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `SkipAll`
        - ❌ `SkipDir`

- **File:** `src/path/filepath/path.go`
    - Ground Truth Functions (3):
        - `Walk`
        - `WalkDir`
        - `walk`
    - Predicted Functions (4):
        - ✅ `Walk`
        - ✅ `WalkDir`
        - ✅ `walk`
        - ❌ `walkDir`

- **File:** `src/path/filepath/path_test.go`
    - Ground Truth Functions (1):
        - `TestWalkSkipAllOnFile`
    - Predicted Functions (2):
        - ✅ `TestWalkSkipAllOnFile`
        - ❌ `TestWalkSkipDirOnFile`


### 📊 **Proposal #49471 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/crash_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestCrashHandler`
        - ❌ `TestGoexitCrash`
        - ❌ `TestPanicTraceback`
        - ❌ `TestRuntimePanic`

- **File:** `src/runtime/os_windows.go`
    - Ground Truth Functions (1):
        - `loadOptionalSyscalls`
    - Predicted Functions (0):

- **File:** `src/runtime/panic.go`
    - Ground Truth Functions (2):
        - `fatalpanic`
        - `fatalthrow`
    - Predicted Functions (0):

- **File:** `src/runtime/runtime.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `setCrashFD`

- **File:** `src/runtime/signal_windows.go`
    - Ground Truth Functions (9):
        - `crash`
        - `exceptionhandler`
        - `initExceptionHandler`
        - `initsig`
        - `isAbort`
        - `lastcontinuehandler`
        - `lastcontinuetramp`
        - `sigenable`
        - `winthrow`
    - Predicted Functions (0):

- **File:** `src/runtime/trace.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `CreateFile`
        - ❌ `GetQueuedCompletionStatus`
        - ❌ `Getpid`
        - ❌ `Getppid`
        - ❌ `MiniDumpWriteDump`
        - ❌ `PostQueuedCompletionStatus`


### 📊 **Proposal #45428 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 13.5% | 33.3% | 19.2% | 5/15 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/alert.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/tls/auth.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/tls/cipher_suites.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `CipherSuites`
        - ❌ `InsecureCipherSuites`
        - ❌ `cipher3DES`
        - ❌ `cipherAES`
        - ❌ `cipherRC4`
        - ❌ `macSHA1`
        - ❌ `macSHA256`
        - ❌ `selectCipherSuite`
        - ❌ `tls10MAC`

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (5):
        - `SupportsCertificate`
        - `cipherSuites`
        - `maxSupportedVersion`
        - `mutualVersion`
        - `supportedVersions`
    - Predicted Functions (7):
        - ❌ `(*Config) cipherSuites`
        - ❌ `(*Config) maxSupportedVersion`
        - ❌ `(*Config) mutualVersion`
        - ❌ `(*Config) supportedCipherSuites`
        - ❌ `(*Config) supportedVersions`
        - ❌ `defaultConfig`
        - ❌ `supportedVersionsFromMax`

- **File:** `src/crypto/tls/conn.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Config.MinVersion`
        - ❌ `ConnectionState`
        - ❌ `Handshake`
        - ❌ `HandshakeContext`

- **File:** `src/crypto/tls/defaults.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `defaultCipherSuites`
        - ❌ `supportedCipherSuites`

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (3):
        - `clientHandshake`
        - `makeClientHello`
        - `pickTLSVersion`
    - Predicted Functions (4):
        - ✅ `clientHandshake`
        - ❌ `doFullHandshake`
        - ❌ `handshake`
        - ✅ `pickTLSVersion`

- **File:** `src/crypto/tls/handshake_server.go`
    - Ground Truth Functions (3):
        - `pickCipherSuite`
        - `processClientHello`
        - `readClientHello`
    - Predicted Functions (5):
        - ❌ `cipherSuiteOk`
        - ✅ `pickCipherSuite`
        - ✅ `processClientHello`
        - ✅ `readClientHello`
        - ❌ `serverHandshake`

- **File:** `src/crypto/tls/handshake_server_test.go`
    - Ground Truth Functions (2):
        - `TestVersion`
        - `testCrossVersionResume`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server_tls13.go`
    - Ground Truth Functions (1):
        - `processClientHello`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_test.go`
    - Ground Truth Functions (1):
        - `runMain`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/tls.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `(*Dialer) Dial`
        - ❌ `(*Dialer) DialContext`
        - ❌ `Client`
        - ❌ `Dial`
        - ❌ `DialWithDialer`
        - ❌ `Server`


### 📊 **Proposal #51644 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 50.0% | 26.7% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/binary/binary.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `AppendUint32`

- **File:** `src/encoding/binary/binary_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `BenchmarkAppendInts`
        - ❌ `BenchmarkAppendSlice1000Int32s`
        - ❌ `BenchmarkAppendSlice1000Structs`
        - ❌ `BenchmarkAppendUint64`

- **File:** `src/encoding/binary/varint.go`
    - Ground Truth Functions (2):
        - `AppendUvarint`
        - `AppendVarint`
    - Predicted Functions (2):
        - ✅ `AppendUvarint`
        - ✅ `AppendVarint`

- **File:** `src/encoding/binary/varint_test.go`
    - Ground Truth Functions (2):
        - `testUvarint`
        - `testVarint`
    - Predicted Functions (4):
        - ❌ `BenchmarkPutUvarint32`
        - ❌ `BenchmarkPutUvarint64`
        - ❌ `TestUvarint`
        - ❌ `TestVarint`


### 📊 **Proposal #34293 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/doc/main.go`
    - Ground Truth Functions (1):
        - `do`
    - Predicted Functions (0):

- **File:** `src/cmd/doc/pkg.go`
    - Ground Truth Functions (1):
        - `packageDoc`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/doc/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `runDoc`

- **File:** `src/go/doc/comment.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ToHTML`
        - ❌ `ToText`

- **File:** `src/go/doc/comment_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestComment`

- **File:** `src/go/doc/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `HTML`
        - ❌ `Markdown`
        - ❌ `New`
        - ❌ `NewFromFiles`
        - ❌ `Text`
        - ❌ `collectFuncs`
        - ❌ `collectTypes`
        - ❌ `collectValues`


### 📊 **Proposal #41682 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 45.5% | 27.8% | 34.5% | 5/18 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/parser.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `ParseCertificate`
        - ❌ `ParseCertificates`
        - ❌ `parseCertificate`

- **File:** `src/crypto/x509/parser_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/x509/verify.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Verify`
        - ❌ `VerifyHostname`

- **File:** `src/crypto/x509/verify_test.go`
    - Ground Truth Functions (1):
        - `TestGoVerify`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (5):
        - `CheckSignature`
        - `CheckSignatureFrom`
        - `CreateCertificate`
        - `Error`
        - `checkSignature`
    - Predicted Functions (4):
        - ❌ `CheckCRLSignature`
        - ✅ `CheckSignature`
        - ✅ `CheckSignatureFrom`
        - ✅ `checkSignature`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (12):
        - `BenchmarkParseCertificate`
        - `Public`
        - `Sign`
        - `TestCreateCertificateBrokenSigner`
        - `TestCreateCertificateLegacy`
        - `TestCreateCertificateRequest`
        - `TestCreateSelfSignedCertificate`
        - `TestDisableSHA1ForCertOnly`
        - `TestInsecureAlgorithmErrorString`
        - `TestSHA1`
        - `allCerts`
        - `mustCert`
    - Predicted Functions (2):
        - ✅ `TestDisableSHA1ForCertOnly`
        - ✅ `TestSHA1`


### 📊 **Proposal #48801 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`
    - Ground Truth Functions (2):
        - `badFormatAt`
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/runtime/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestFakeTime`
        - ❌ `TestTimeTimerType`
        - ❌ `parseFakeTime`

- **File:** `src/time/format.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `AppendFormat`
        - ❌ `Format`
        - ❌ `Parse`
        - ❌ `ParseInLocation`
        - ❌ `appendFormat`

- **File:** `src/time/format_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestFormat`
        - ❌ `TestFormatAndParse`
        - ❌ `TestParse`

- **File:** `src/time/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (11):
        - ❌ `AddDate`
        - ❌ `Date`
        - ❌ `Day`
        - ❌ `MarshalText`
        - ❌ `Month`
        - ❌ `Unix`
        - ❌ `UnixMicro`
        - ❌ `UnixMilli`
        - ❌ `UnixNano`
        - ❌ `UnmarshalText`
        - ❌ `Year`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestDate`
        - ❌ `TestMarshalInvalidTimes`
        - ❌ `TestParse`
        - ❌ `TestTimeIsDST`
        - ❌ `TestUnmarshalInvalidTimes`


### 📊 **Proposal #43993 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/10 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (2):
        - `TestSmallZero`
        - `TestZeroSet`
    - Predicted Functions (0):

- **File:** `src/reflect/deepequal.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `DeepEqual`
        - ❌ `deepValueEqual`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (2):
        - `Set`
        - `Zero`
    - Predicted Functions (0):

- **File:** `src/text/template/exec.go`
    - Ground Truth Functions (5):
        - `evalCall`
        - `evalField`
        - `evalPipeline`
        - `isMissing`
        - `notAFunction`
    - Predicted Functions (0):

- **File:** `src/text/template/funcs.go`
    - Ground Truth Functions (1):
        - `isNil`
    - Predicted Functions (0):


### 📊 **Proposal #39214 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/23 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/gc/main.go`
    - Ground Truth Functions (1):
        - `Main`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types/pkg.go`
    - Ground Truth Functions (1):
        - `InternString`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/sym.go`
    - Ground Truth Functions (1):
        - `LookupInit`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/x86/obj6.go`
    - Ground Truth Functions (2):
        - `preprocess`
        - `stacksplit`
    - Predicted Functions (0):

- **File:** `src/internal/cpu/cpu.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/cpu/cpu_no_name.go`
    - Ground Truth Functions (1):
        - `Name`
    - Predicted Functions (0):

- **File:** `src/internal/cpu/cpu_x86.go`
    - Ground Truth Functions (3):
        - `Name`
        - `appendBytes`
        - `doinit`
    - Predicted Functions (0):

- **File:** `src/strconv/atof.go`
    - Ground Truth Functions (8):
        - `ParseFloat`
        - `atof32`
        - `atof64`
        - `commonPrefixLenIgnoreCase`
        - `parseFloatPrefix`
        - `readFloat`
        - `set`
        - `special`
    - Predicted Functions (0):

- **File:** `src/strconv/atof_test.go`
    - Ground Truth Functions (1):
        - `TestParseFloatPrefix`
    - Predicted Functions (0):

- **File:** `src/strconv/internal_test.go`
    - Ground Truth Functions (1):
        - `ParseFloatPrefix`
    - Predicted Functions (0):

- **File:** `src/strings/strings.go`
    - Ground Truth Functions (1):
        - `ToLower`
    - Predicted Functions (0):

- **File:** `src/strings/strings_test.go`
    - Ground Truth Functions (1):
        - `BenchmarkToLower`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_arm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_ppc64x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_s390x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/testing/benchmark.go`
    - Ground Truth Functions (2):
        - `Run`
        - `run`
    - Predicted Functions (0):


### 📊 **Proposal #42502 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 6.3% | 10.4% | 4/63 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/cgocall.go`
    - Ground Truth Functions (1):
        - `cgocallbackg1`
    - Predicted Functions (0):

- **File:** `src/runtime/cpuprof.go`
    - Ground Truth Functions (2):
        - `SetCPUProfileRate`
        - `add`
    - Predicted Functions (0):

- **File:** `src/runtime/os3_plan9.go`
    - Ground Truth Functions (1):
        - `setThreadCPUProfiler`
    - Predicted Functions (0):

- **File:** `src/runtime/os3_solaris.go`
    - Ground Truth Functions (2):
        - `setProcessCPUProfiler`
        - `setThreadCPUProfiler`
    - Predicted Functions (0):

- **File:** `src/runtime/os_aix.go`
    - Ground Truth Functions (2):
        - `setProcessCPUProfiler`
        - `setThreadCPUProfiler`
    - Predicted Functions (0):

- **File:** `src/runtime/os_darwin.go`
    - Ground Truth Functions (2):
        - `setProcessCPUProfiler`
        - `setThreadCPUProfiler`
    - Predicted Functions (0):

- **File:** `src/runtime/os_dragonfly.go`
    - Ground Truth Functions (2):
        - `setProcessCPUProfiler`
        - `setThreadCPUProfiler`
    - Predicted Functions (0):

- **File:** `src/runtime/os_freebsd.go`
    - Ground Truth Functions (2):
        - `setProcessCPUProfiler`
        - `setThreadCPUProfiler`
    - Predicted Functions (0):

- **File:** `src/runtime/os_linux.go`
    - Ground Truth Functions (4):
        - `osinit`
        - `setProcessCPUProfiler`
        - `setThreadCPUProfiler`
        - `validSIGPROF`
    - Predicted Functions (0):

- **File:** `src/runtime/os_netbsd.go`
    - Ground Truth Functions (2):
        - `setProcessCPUProfiler`
        - `setThreadCPUProfiler`
    - Predicted Functions (0):

- **File:** `src/runtime/os_openbsd.go`
    - Ground Truth Functions (2):
        - `setProcessCPUProfiler`
        - `setThreadCPUProfiler`
    - Predicted Functions (0):

- **File:** `src/runtime/os_windows.go`
    - Ground Truth Functions (4):
        - `profileLoop`
        - `profilem`
        - `setThreadCPUProfiler`
        - `stdcall`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/defs_darwin.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `SetCPUProfileRate`
        - ❌ `StartCPUProfile`

- **File:** `src/runtime/pprof/defs_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `SetCPUProfileRate`
        - ❌ `StartCPUProfile`
        - ❌ `StartCPUProfileWithSpecifiedRate`

- **File:** `src/runtime/pprof/defs_darwin_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `SetCPUProfileRate`
        - ❌ `StartCPUProfile`
        - ❌ `StartCPUProfileWithSpecifiedRate`

- **File:** `src/runtime/pprof/pprof.go`
    - Ground Truth Functions (5):
        - `StartCPUProfile`
        - `StopCPUProfile`
        - `printCountCycleProfile`
        - `printCountProfile`
        - `profileWriter`
    - Predicted Functions (2):
        - ✅ `StartCPUProfile`
        - ✅ `StopCPUProfile`

- **File:** `src/runtime/pprof/pprof_test.go`
    - Ground Truth Functions (18):
        - `BenchmarkGoroutine`
        - `TestCPUProfile`
        - `TestCPUProfileInlining`
        - `TestCPUProfileLabel`
        - `TestCPUProfileMultithreadMagnitude`
        - `TestCPUProfileMultithreaded`
        - `TestCPUProfileRecursion`
        - `TestGoroutineProfileLabelRace`
        - `TestGoroutineSwitch`
        - `TestLabelRace`
        - `TestLabelSystemstack`
        - `TestMathBigDivide`
        - `TestMorestack`
        - `TestTimeVDSO`
        - `TestTryAdd`
        - `avoidFunctions`
        - `recursionChainTop`
        - `testCPUProfile`
    - Predicted Functions (4):
        - ✅ `TestCPUProfile`
        - ✅ `TestCPUProfileLabel`
        - ❌ `TestCPUProfileRateAdjust`
        - ❌ `TestCPUProfileWithFork`

- **File:** `src/runtime/pprof/proto.go`
    - Ground Truth Functions (3):
        - `addCPUData`
        - `build`
        - `newProfileBuilder`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/proto_test.go`
    - Ground Truth Functions (1):
        - `translateCPUProfile`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/protomem.go`
    - Ground Truth Functions (1):
        - `writeHeapProto`
    - Predicted Functions (0):

- **File:** `src/runtime/proc.go`
    - Ground Truth Functions (3):
        - `execute`
        - `setcpuprofilerate`
        - `sigprof`
    - Predicted Functions (0):

- **File:** `src/runtime/signal_unix.go`
    - Ground Truth Functions (4):
        - `sighandler`
        - `sigprofNonGo`
        - `sigprofNonGoPC`
        - `sigtrampgo`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprogcgo/threadpprof.go`
    - Ground Truth Functions (1):
        - `pprofThread`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprogcgo/tracebackctxt.go`
    - Ground Truth Functions (1):
        - `TracebackContextPreemptionGoFunction`
    - Predicted Functions (0):


### 📊 **Proposal #46131 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (1):
        - `TestMapIterSet`
    - Predicted Functions (0):

- **File:** `src/reflect/iter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `SetKey`
        - ❌ `SetValue`

- **File:** `src/reflect/iter_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `SetKey`
        - ❌ `SetValue`

- **File:** `src/reflect/map_noswiss.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Key`
        - ❌ `MapIter`
        - ❌ `Next`
        - ❌ `Reset`
        - ❌ `SetKey`
        - ❌ `SetValue`
        - ❌ `Value`

- **File:** `src/reflect/map_noswiss_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/map_swiss.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `MapIter`
        - ❌ `SetIterKey`
        - ❌ `SetIterValue`

- **File:** `src/reflect/map_swiss_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/map.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/stress/maps.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `AddItem`
        - ❌ `DelItem`
        - ❌ `GetItem`
        - ❌ `Len`
        - ❌ `NewMap`
        - ❌ `RangeAll`
        - ❌ `mapTypes`
        - ❌ `stressMapType`
        - ❌ `stressMaps`


### 📊 **Proposal #33136 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 4.2% | 5.4% | 4.7% | 2/37 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/json/decode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `(*decodeState) array`
        - ❌ `(*decodeState) object`
        - ❌ `(*decodeState) unmarshal`
        - ❌ `(*decodeState) value`
        - ❌ `(*decodeState) valueInterface`
        - ❌ `Unmarshal`

- **File:** `src/encoding/json/decode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestUnmarshal`
        - ❌ `TestUnmarshalEmbeddedUnexported`
        - ❌ `TestUnmarshalNulls`
        - ❌ `TestUnmarshalPtrPtr`

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (24):
        - ❌ `addrMarshalerEncoder`
        - ❌ `addrTextMarshalerEncoder`
        - ❌ `arrayEncoder`
        - ❌ `boolEncoder`
        - ❌ `condAddrEncoder`
        - ❌ `floatEncoder`
        - ❌ `intEncoder`
        - ❌ `interfaceEncoder`
        - ❌ `invalidValueEncoder`
        - ❌ `isEmptyValue`
        - ❌ `mapEncoder`
        - ❌ `marshalerEncoder`
        - ❌ `newCondAddrEncoder`
        - ❌ `newTypeEncoder`
        - ❌ `ptrEncoder`
        - ❌ `reflectValue`
        - ❌ `sliceEncoder`
        - ❌ `stringEncoder`
        - ❌ `structEncoder`
        - ❌ `textMarshalerEncoder`
        - ❌ `typeEncoder`
        - ❌ `uintEncoder`
        - ❌ `unsupportedTypeEncoder`
        - ❌ `valueEncoder`

- **File:** `src/encoding/json/encode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestMarshalFloat`
        - ❌ `TestMarshalRawMessageValue`
        - ❌ `TestOmitZero`
        - ❌ `TestOmitZeroMap`

- **File:** `src/encoding/json/internal/jsonwire/decode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `ConsumeFalse`
        - ❌ `ConsumeNull`
        - ❌ `ConsumeNumber`
        - ❌ `ConsumeString`
        - ❌ `ConsumeTrue`

- **File:** `src/encoding/json/internal/jsonwire/decode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/abi.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/abi_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (2):
        - `TestSmallZero`
        - `TestZeroSet`
    - Predicted Functions (0):

- **File:** `src/reflect/iter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/iter_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (35):
        - `Addr`
        - `Bool`
        - `Bytes`
        - `Cap`
        - `Close`
        - `Complex`
        - `Copy`
        - `Elem`
        - `Field`
        - `Float`
        - `Index`
        - `Int`
        - `Interface`
        - `InterfaceData`
        - `IsNil`
        - `Len`
        - `Pointer`
        - `Select`
        - `Set`
        - `SetPointer`
        - `Slice`
        - `Slice3`
        - `String`
        - `Uint`
        - `Zero`
        - `call`
        - `callReflect`
        - `methodReceiver`
        - `packEface`
        - `pointer`
        - `runes`
        - `send`
        - `storeRcvr`
        - `typesMustMatch`
        - `valueInterface`
    - Predicted Functions (5):
        - ✅ `Set`
        - ❌ `SetZero`
        - ✅ `Zero`
        - ❌ `typedmemclr`
        - ❌ `typedmemmove`


### 📊 **Proposal #45754 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 4.2% | 33.3% | 7.4% | 2/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/flag/example_flagset_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Func`
        - ❌ `TextVar`
        - ❌ `Var`

- **File:** `src/flag/example_func_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/flag/example_textvar_test.go`
    - Ground Truth Functions (1):
        - `ExampleTextVar`
    - Predicted Functions (1):
        - ✅ `ExampleTextVar`

- **File:** `src/flag/example_value_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ExampleValue`

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (5):
        - `Get`
        - `Set`
        - `String`
        - `TextVar`
        - `newTextValue`
    - Predicted Functions (8):
        - ❌ `BoolVar`
        - ❌ `DurationVar`
        - ❌ `Float64Var`
        - ❌ `Func`
        - ❌ `IntVar`
        - ❌ `StringVar`
        - ✅ `TextVar`
        - ❌ `Var`

- **File:** `src/flag/flag_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestUserDefined`
        - ❌ `TestUserDefinedBool`
        - ❌ `TestUserDefinedBoolUsage`
        - ❌ `TestUserDefinedForCommandLine`
        - ❌ `TestUserDefinedFunc`

- **File:** `src/math/big/float.go`
    - Ground Truth Functions (0):
    - Predicted Functions (11):
        - ❌ `Abs`
        - ❌ `Copy`
        - ❌ `Neg`
        - ❌ `NewFloat`
        - ❌ `Set`
        - ❌ `SetFloat64`
        - ❌ `SetInf`
        - ❌ `SetInt`
        - ❌ `SetInt64`
        - ❌ `SetRat`
        - ❌ `SetUint64`

- **File:** `src/math/big/int.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Bytes`
        - ❌ `FillBytes`
        - ❌ `NewInt`
        - ❌ `SetBytes`
        - ❌ `SetString`

- **File:** `src/math/big/rat.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Set`
        - ❌ `SetFrac`
        - ❌ `SetFrac64`
        - ❌ `SetInt`
        - ❌ `SetInt64`
        - ❌ `SetUint64`

- **File:** `src/net/ip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `MarshalText`
        - ❌ `UnmarshalText`

- **File:** `src/testing/flag_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestFlag`
        - ❌ `testFlagHelper`

- **File:** `src/time/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `MarshalText`
        - ❌ `UnmarshalText`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `BenchmarkMarshalText`
        - ❌ `TestUnmarshalTextAllocations`


### 📊 **Proposal #47658 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 23.5% | 66.7% | 34.8% | 4/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/test/inl_test.go`
    - Ground Truth Functions (1):
        - `TestIntendedInlining`
    - Predicted Functions (0):

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (1):
        - `TestCanIntUintFloatComplex`
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `CanSeq`
        - ❌ `Float`
        - ❌ `Int`
        - ❌ `Kind`
        - ❌ `OverflowComplex`
        - ❌ `OverflowFloat`
        - ❌ `OverflowInt`
        - ❌ `OverflowUint`
        - ❌ `Uint`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (4):
        - `CanComplex`
        - `CanFloat`
        - `CanInt`
        - `CanUint`
    - Predicted Functions (8):
        - ✅ `CanComplex`
        - ✅ `CanFloat`
        - ✅ `CanInt`
        - ✅ `CanUint`
        - ❌ `Complex`
        - ❌ `Float`
        - ❌ `Int`
        - ❌ `Uint`


### 📊 **Proposal #40025 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 80.0% | 9.3% | 16.7% | 4/43 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/io/example_test.go`
    - Ground Truth Functions (1):
        - `ExampleReadAll`
    - Predicted Functions (0):

- **File:** `src/io/io.go`
    - Ground Truth Functions (6):
        - `CopyBuffer`
        - `NopCloser`
        - `ReadAll`
        - `ReadFrom`
        - `Write`
        - `WriteString`
    - Predicted Functions (3):
        - ✅ `NopCloser`
        - ✅ `ReadAll`
        - ❌ `discard`

- **File:** `src/io/ioutil/example_test.go`
    - Ground Truth Functions (2):
        - `ExampleReadDir`
        - `ExampleTempDir`
    - Predicted Functions (0):

- **File:** `src/io/ioutil/ioutil.go`
    - Ground Truth Functions (5):
        - `NopCloser`
        - `ReadAll`
        - `ReadDir`
        - `ReadFile`
        - `WriteFile`
    - Predicted Functions (2):
        - ✅ `NopCloser`
        - ✅ `ReadAll`

- **File:** `src/io/ioutil/ioutil_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/dir.go`
    - Ground Truth Functions (1):
        - `ReadDir`
    - Predicted Functions (0):

- **File:** `src/os/example_test.go`
    - Ground Truth Functions (7):
        - `ExampleCreateTemp`
        - `ExampleCreateTemp_suffix`
        - `ExampleMkdirTemp`
        - `ExampleMkdirTemp_suffix`
        - `ExampleReadDir`
        - `ExampleReadFile`
        - `ExampleWriteFile`
    - Predicted Functions (0):

- **File:** `src/os/file.go`
    - Ground Truth Functions (2):
        - `ReadFile`
        - `WriteFile`
    - Predicted Functions (0):

- **File:** `src/os/os_test.go`
    - Ground Truth Functions (2):
        - `TestReadFileProc`
        - `checkSize`
    - Predicted Functions (0):

- **File:** `src/os/read_test.go`
    - Ground Truth Functions (5):
        - `TestReadDir`
        - `TestReadFile`
        - `TestReadOnlyWriteFile`
        - `TestWriteFile`
        - `checkNamedSize`
    - Predicted Functions (0):

- **File:** `src/os/removeall_test.go`
    - Ground Truth Functions (1):
        - `TestRemoveAllButReadOnlyAndPathError`
    - Predicted Functions (0):

- **File:** `src/os/tempfile.go`
    - Ground Truth Functions (5):
        - `CreateTemp`
        - `MkdirTemp`
        - `joinPath`
        - `nextRandom`
        - `prefixAndSuffix`
    - Predicted Functions (0):

- **File:** `src/os/tempfile_test.go`
    - Ground Truth Functions (6):
        - `TestCreateTemp`
        - `TestCreateTempBadPattern`
        - `TestCreateTempPattern`
        - `TestMkdirTemp`
        - `TestMkdirTempBadDir`
        - `TestMkdirTempBadPattern`
    - Predicted Functions (0):


### 📊 **Proposal #51972 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 44.4% | 28.6% | 34.8% | 4/14 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/sync/hashtriemap.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `CompareAndDelete`
        - ❌ `CompareAndSwap`
        - ❌ `LoadAndStore`
        - ❌ `Swap`

- **File:** `src/sync/map.go`
    - Ground Truth Functions (9):
        - `CompareAndDelete`
        - `CompareAndSwap`
        - `LoadOrStore`
        - `Store`
        - `Swap`
        - `swapLocked`
        - `tryCompareAndSwap`
        - `trySwap`
        - `unexpungeLocked`
    - Predicted Functions (4):
        - ✅ `CompareAndDelete`
        - ✅ `CompareAndSwap`
        - ❌ `LoadAndStore`
        - ✅ `Swap`

- **File:** `src/sync/map_reference_test.go`
    - Ground Truth Functions (3):
        - `CompareAndDelete`
        - `CompareAndSwap`
        - `Swap`
    - Predicted Functions (0):

- **File:** `src/sync/map_test.go`
    - Ground Truth Functions (2):
        - `TestCompareAndSwap_NonExistingKey`
        - `apply`
    - Predicted Functions (1):
        - ✅ `TestCompareAndSwap_NonExistingKey`

- **File:** `src/sync/mutex.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #47527 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 66.7% | 30.8% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/bufio/bufio.go`
    - Ground Truth Functions (1):
        - `AvailableBuffer`
    - Predicted Functions (5):
        - ❌ `Available`
        - ✅ `AvailableBuffer`
        - ❌ `NewWriter`
        - ❌ `NewWriterSize`
        - ❌ `Write`

- **File:** `src/bufio/bufio_test.go`
    - Ground Truth Functions (1):
        - `TestWriterAppend`
    - Predicted Functions (5):
        - ❌ `TestWriter`
        - ✅ `TestWriterAppend`
        - ❌ `TestWriterReadFrom`
        - ❌ `TestWriterReset`
        - ❌ `TestWriterSize`

- **File:** `src/bufio/example_test.go`
    - Ground Truth Functions (1):
        - `ExampleWriter_AvailableBuffer`
    - Predicted Functions (0):


### 📊 **Proposal #28089 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 33.3% | 16.7% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/go/ast/ast.go`
    - Ground Truth Functions (2):
        - `IsGenerated`
        - `generator`
    - Predicted Functions (1):
        - ✅ `IsGenerated`

- **File:** `src/go/ast/ast_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestCommentText`
        - ❌ `TestIsDirective`

- **File:** `src/go/ast/issues_test.go`
    - Ground Truth Functions (1):
        - `TestIssue28089`
    - Predicted Functions (0):

- **File:** `src/go/parser/parser.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `consumeComment`
        - ❌ `consumeCommentGroup`
        - ❌ `parseFile`

- **File:** `src/go/parser/parser_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestCommentGroups`
        - ❌ `TestLeadAndLineComments`
        - ❌ `TestParseFile`


### 📊 **Proposal #41792 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 23.1% | 50.0% | 31.6% | 3/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/internal/objabi/flag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Flagparse`

- **File:** `src/cmd/internal/objabi/flag_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (3):
        - `Var`
        - `failf`
        - `sprintf`
    - Predicted Functions (10):
        - ❌ `BoolFunc`
        - ❌ `BoolVar`
        - ❌ `DurationVar`
        - ❌ `Float64Var`
        - ❌ `Func`
        - ❌ `IntVar`
        - ❌ `Parse`
        - ❌ `StringVar`
        - ❌ `TextVar`
        - ✅ `Var`

- **File:** `src/flag/flag_test.go`
    - Ground Truth Functions (3):
        - `TestInvalidFlags`
        - `TestRedefinedFlags`
        - `mustPanic`
    - Predicted Functions (2):
        - ✅ `TestInvalidFlags`
        - ✅ `TestRedefinedFlags`

- **File:** `test/fixedbugs/issue41736.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #46485 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.7% | 11.1% | 5.6% | 1/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/cgo/ast.go`
    - Ground Truth Functions (1):
        - `ParseGo`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/test.go`
    - Ground Truth Functions (1):
        - `load`
    - Predicted Functions (0):

- **File:** `src/cmd/gofmt/gofmt.go`
    - Ground Truth Functions (1):
        - `initParserMode`
    - Predicted Functions (0):

- **File:** `src/cmd/gofmt/simplify.go`
    - Ground Truth Functions (1):
        - `Visit`
    - Predicted Functions (0):

- **File:** `src/go/internal/srcimporter/srcimporter.go`
    - Ground Truth Functions (2):
        - `cgo`
        - `parseFiles`
    - Predicted Functions (0):

- **File:** `src/go/parser/parser.go`
    - Ground Truth Functions (1):
        - `parseFile`
    - Predicted Functions (15):
        - ❌ `parseBody`
        - ❌ `parseDecl`
        - ❌ `parseExprList`
        - ❌ `parseFieldDecl`
        - ✅ `parseFile`
        - ❌ `parseFuncDecl`
        - ❌ `parseFuncType`
        - ❌ `parseIdent`
        - ❌ `parseIdentList`
        - ❌ `parseParamDecl`
        - ❌ `parseParameters`
        - ❌ `parseQualifiedIdent`
        - ❌ `parseStmtList`
        - ❌ `parseType`
        - ❌ `parseTypeName`

- **File:** `src/go/parser/parser_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestObjects`
        - ❌ `TestParseFile`
        - ❌ `TestUnresolved`

- **File:** `src/go/parser/performance_test.go`
    - Ground Truth Functions (2):
        - `BenchmarkParseOnly`
        - `BenchmarkResolve`
    - Predicted Functions (0):

- **File:** `src/go/parser/resolver.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `declare`
        - ❌ `declareList`
        - ❌ `resolve`
        - ❌ `resolveFile`

- **File:** `src/go/parser/resolver_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestResolution`
        - ❌ `annotatedObj`
        - ❌ `declsFromComments`
        - ❌ `declsFromParser`
        - ❌ `positionMarkers`


### 📊 **Proposal #45899 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 57.1% | 53.3% | 4/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/io/fs/fs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/io/io.go`
    - Ground Truth Functions (4):
        - `NewOffsetWriter`
        - `Seek`
        - `Write`
        - `WriteAt`
    - Predicted Functions (8):
        - ❌ `CopyAt`
        - ❌ `CopyAtBuffer`
        - ❌ `CopyFileRange`
        - ✅ `NewOffsetWriter`
        - ❌ `NewSectionReader`
        - ✅ `Seek`
        - ✅ `Write`
        - ✅ `WriteAt`

- **File:** `src/io/io_test.go`
    - Ground Truth Functions (3):
        - `TestOffsetWriter_Seek`
        - `TestOffsetWriter_Write`
        - `TestOffsetWriter_WriteAt`
    - Predicted Functions (0):


### 📊 **Proposal #39444 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/os/exec/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `signal`

- **File:** `src/os/exec_unix.go`
    - Ground Truth Functions (1):
        - `signal`
    - Predicted Functions (2):
        - ❌ `pidSignal`
        - ✅ `signal`

- **File:** `src/os/exec_unix_test.go`
    - Ground Truth Functions (1):
        - `TestErrProcessDone`
    - Predicted Functions (0):

- **File:** `src/os/signal/signal.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #52463 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/gofmt/gofmt.go`
    - Ground Truth Functions (1):
        - `initParserMode`
    - Predicted Functions (0):

- **File:** `src/cmd/gofmt/simplify.go`
    - Ground Truth Functions (1):
        - `Visit`
    - Predicted Functions (0):

- **File:** `src/go/ast/ast.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Object`
        - ❌ `Scope`

- **File:** `src/go/ast/ast_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/ast/import.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/ast/resolve.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `resolve`

- **File:** `src/go/ast/scope.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Insert`
        - ❌ `Lookup`
        - ❌ `NewObj`

- **File:** `src/go/parser/parser.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `parseDecl`
        - ❌ `parseFieldDecl`
        - ❌ `parseFile`
        - ❌ `parseFuncDecl`
        - ❌ `parseIdent`
        - ❌ `parseParamDecl`
        - ❌ `parseQualifiedIdent`
        - ❌ `parseTypeName`


### 📊 **Proposal #35998 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 40.0% | 26.7% | 2/5 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/web/file_test.go`
    - Ground Truth Functions (1):
        - `TestGetFileURL`
    - Predicted Functions (0):

- **File:** `src/io/ioutil/tempfile_test.go`
    - Ground Truth Functions (2):
        - `TestTempDir_BadPattern`
        - `TestTempFile_BadPattern`
    - Predicted Functions (0):

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (1):
        - `TempDir`
    - Predicted Functions (6):
        - ❌ `(*T) Parallel`
        - ❌ `(*T) Run`
        - ❌ `Chdir`
        - ❌ `Cleanup`
        - ❌ `Setenv`
        - ✅ `TempDir`

- **File:** `src/testing/testing_test.go`
    - Ground Truth Functions (1):
        - `TestTempDir`
    - Predicted Functions (4):
        - ✅ `TestTempDir`
        - ❌ `TestTempDirInBenchmark`
        - ❌ `TestTempDirInCleanup`
        - ❌ `testTempDir`


### 📊 **Proposal #48866 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/json/decode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/mime/mediatype.go`
    - Ground Truth Functions (1):
        - `ParseMediaType`
    - Predicted Functions (2):
        - ✅ `ParseMediaType`
        - ❌ `consumeMediaParam`

- **File:** `src/mime/mediatype_test.go`
    - Ground Truth Functions (1):
        - `TestParseMediaType`
    - Predicted Functions (2):
        - ✅ `TestParseMediaType`
        - ❌ `TestParseMediaTypeBogus`


### 📊 **Proposal #37023 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.0% | 42.9% | 35.3% | 3/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/debug/panic_test.go`
    - Ground Truth Functions (1):
        - `TestPanicOnFault`
    - Predicted Functions (1):
        - ✅ `TestPanicOnFault`

- **File:** `src/runtime/error.go`
    - Ground Truth Functions (2):
        - `Addr`
        - `Error`
    - Predicted Functions (0):

- **File:** `src/runtime/os_plan9.go`
    - Ground Truth Functions (1):
        - `sigpanic`
    - Predicted Functions (0):

- **File:** `src/runtime/panic.go`
    - Ground Truth Functions (1):
        - `panicmemAddr`
    - Predicted Functions (5):
        - ❌ `gopanic`
        - ❌ `gorecover`
        - ❌ `panicmem`
        - ✅ `panicmemAddr`
        - ❌ `throw`

- **File:** `src/runtime/runtime.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `panicmem`

- **File:** `src/runtime/signal_unix.go`
    - Ground Truth Functions (1):
        - `sigpanic`
    - Predicted Functions (3):
        - ❌ `crash`
        - ❌ `dieFromSignal`
        - ✅ `sigpanic`

- **File:** `src/runtime/signal_windows.go`
    - Ground Truth Functions (1):
        - `sigpanic`
    - Predicted Functions (0):


### 📊 **Proposal #38627 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/html/template/template.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Parse`
        - ❌ `ParseFS`
        - ❌ `ParseFiles`
        - ❌ `ParseGlob`

- **File:** `src/html/template/template_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestSkipEscapeComments`
        - ❌ `mustExecute`
        - ❌ `mustNotParse`
        - ❌ `mustParse`

- **File:** `src/text/template/option.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Option`
        - ❌ `setOption`

- **File:** `src/text/template/parse/lex.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `lex`
        - ❌ `lexComment`
        - ❌ `lexField`
        - ❌ `lexFieldOrVariable`
        - ❌ `lexIdentifier`
        - ❌ `lexInsideAction`
        - ❌ `lexLeftDelim`
        - ❌ `lexRightDelim`
        - ❌ `lexText`
        - ❌ `lexVariable`

- **File:** `src/text/template/parse/lex_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `TestDelims`
        - ❌ `TestDelimsAlphaNumeric`
        - ❌ `TestDelimsAndMarkers`
        - ❌ `TestLex`
        - ❌ `TestPos`
        - ❌ `parseLexer`

- **File:** `src/text/template/parse/parse.go`
    - Ground Truth Functions (1):
        - `term`
    - Predicted Functions (4):
        - ❌ `Parse`
        - ❌ `checkPipeline`
        - ❌ `hasFunction`
        - ❌ `parse`

- **File:** `src/text/template/parse/parse_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestParse`
        - ❌ `TestParseWithComments`
        - ❌ `TestSkipFuncCheck`


### 📊 **Proposal #38781 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/transport_test.go`
    - Ground Truth Functions (1):
        - `TestTransportClosesBodyOnError`
    - Predicted Functions (0):

- **File:** `src/testing/iotest/example_test.go`
    - Ground Truth Functions (1):
        - `ExampleErrReader`
    - Predicted Functions (0):

- **File:** `src/testing/iotest/logger_test.go`
    - Ground Truth Functions (2):
        - `TestReadLogger`
        - `TestReadLogger_errorOnRead`
    - Predicted Functions (0):

- **File:** `src/testing/iotest/reader.go`
    - Ground Truth Functions (2):
        - `ErrReader`
        - `Read`
    - Predicted Functions (0):

- **File:** `src/testing/iotest/reader_test.go`
    - Ground Truth Functions (1):
        - `TestErrReader`
    - Predicted Functions (0):


### 📊 **Proposal #53346 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 38.5% | 35.7% | 5/13 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/writer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Close`
        - ❌ `Flush`

- **File:** `src/archive/tar/writer_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/zip/writer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Close`
        - ❌ `Flush`

- **File:** `src/archive/zip/writer_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestWriterFlush`

- **File:** `src/encoding/xml/marshal.go`
    - Ground Truth Functions (12):
        - `Close`
        - `Encode`
        - `EncodeElement`
        - `EncodeToken`
        - `Flush`
        - `Marshal`
        - `MarshalIndent`
        - `NewEncoder`
        - `Write`
        - `WriteByte`
        - `WriteString`
        - `isValidDirective`
    - Predicted Functions (4):
        - ✅ `Close`
        - ✅ `EncodeToken`
        - ✅ `Flush`
        - ✅ `NewEncoder`

- **File:** `src/encoding/xml/marshal_test.go`
    - Ground Truth Functions (1):
        - `TestClose`
    - Predicted Functions (3):
        - ✅ `TestClose`
        - ❌ `TestEncodeToken`
        - ❌ `TestMarshalFlush`

- **File:** `src/encoding/xml/xml.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Close`
        - ❌ `EncodeToken`
        - ❌ `Flush`


### 📊 **Proposal #53482 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 16.7% | 13.3% | 1/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/interface.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Flags.String`
        - ❌ `Interface.Addrs`
        - ❌ `Interface.MulticastAddrs`
        - ❌ `InterfaceAddrs`
        - ❌ `InterfaceByIndex`
        - ❌ `InterfaceByName`
        - ❌ `Interfaces`

- **File:** `src/net/interface_aix.go`
    - Ground Truth Functions (1):
        - `linkFlags`
    - Predicted Functions (0):

- **File:** `src/net/interface_bsd.go`
    - Ground Truth Functions (1):
        - `linkFlags`
    - Predicted Functions (0):

- **File:** `src/net/interface_linux.go`
    - Ground Truth Functions (1):
        - `linkFlags`
    - Predicted Functions (1):
        - ✅ `linkFlags`

- **File:** `src/net/interface_plan9.go`
    - Ground Truth Functions (1):
        - `readInterface`
    - Predicted Functions (0):

- **File:** `src/net/interface_solaris.go`
    - Ground Truth Functions (1):
        - `linkFlags`
    - Predicted Functions (0):

- **File:** `src/net/interface_windows.go`
    - Ground Truth Functions (1):
        - `interfaceTable`
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_linux_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `IFF_RUNNING`


### 📊 **Proposal #47651 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 1.7% | 3.2% | 2/119 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/fix/cftype.go`
    - Ground Truth Functions (1):
        - `typefix`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/typecheck.go`
    - Ground Truth Functions (1):
        - `typecheck1`
    - Predicted Functions (0):

- **File:** `src/cmd/gofmt/rewrite.go`
    - Ground Truth Functions (1):
        - `subst`
    - Predicted Functions (0):

- **File:** `src/database/sql/convert.go`
    - Ground Truth Functions (2):
        - `callValuerValue`
        - `convertAssignRows`
    - Predicted Functions (0):

- **File:** `src/database/sql/driver/types.go`
    - Ground Truth Functions (2):
        - `ConvertValue`
        - `callValuerValue`
    - Predicted Functions (0):

- **File:** `src/encoding/asn1/asn1.go`
    - Ground Truth Functions (2):
        - `Error`
        - `UnmarshalWithParams`
    - Predicted Functions (0):

- **File:** `src/encoding/binary/binary.go`
    - Ground Truth Functions (1):
        - `Read`
    - Predicted Functions (0):

- **File:** `src/encoding/gob/decode.go`
    - Ground Truth Functions (5):
        - `decAlloc`
        - `decodeArrayHelper`
        - `decodeMap`
        - `decodeStruct`
        - `gobDecodeOpFor`
    - Predicted Functions (0):

- **File:** `src/encoding/gob/decoder.go`
    - Ground Truth Functions (2):
        - `Decode`
        - `DecodeValue`
    - Predicted Functions (0):

- **File:** `src/encoding/gob/encode.go`
    - Ground Truth Functions (3):
        - `encodeInterface`
        - `gobEncodeOpFor`
        - `valid`
    - Predicted Functions (0):

- **File:** `src/encoding/gob/encoder.go`
    - Ground Truth Functions (1):
        - `EncodeValue`
    - Predicted Functions (0):

- **File:** `src/encoding/gob/type.go`
    - Ground Truth Functions (4):
        - `Register`
        - `implementsInterface`
        - `isSent`
        - `validUserType`
    - Predicted Functions (0):

- **File:** `src/encoding/gob/type_test.go`
    - Ground Truth Functions (1):
        - `TestRegistrationNaming`
    - Predicted Functions (0):

- **File:** `src/encoding/json/decode.go`
    - Ground Truth Functions (5):
        - `Error`
        - `indirect`
        - `literalStore`
        - `object`
        - `unmarshal`
    - Predicted Functions (0):

- **File:** `src/encoding/json/decode_test.go`
    - Ground Truth Functions (1):
        - `TestUnmarshal`
    - Predicted Functions (0):

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (8):
        - `encode`
        - `isEmptyValue`
        - `marshalerEncoder`
        - `newSliceEncoder`
        - `newTypeEncoder`
        - `textMarshalerEncoder`
        - `typeByIndex`
        - `typeFields`
    - Predicted Functions (0):

- **File:** `src/encoding/xml/marshal.go`
    - Ground Truth Functions (5):
        - `indirect`
        - `isEmptyValue`
        - `marshalAttr`
        - `marshalStruct`
        - `marshalValue`
    - Predicted Functions (0):

- **File:** `src/encoding/xml/read.go`
    - Ground Truth Functions (4):
        - `DecodeElement`
        - `copyValue`
        - `unmarshal`
        - `unmarshalAttr`
    - Predicted Functions (0):

- **File:** `src/encoding/xml/typeinfo.go`
    - Ground Truth Functions (3):
        - `getTypeInfo`
        - `lookupXMLName`
        - `value`
    - Predicted Functions (0):

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (1):
        - `isZeroValue`
    - Predicted Functions (0):

- **File:** `src/fmt/print.go`
    - Ground Truth Functions (3):
        - `catchPanic`
        - `fmtPointer`
        - `printValue`
    - Predicted Functions (0):

- **File:** `src/fmt/scan.go`
    - Ground Truth Functions (1):
        - `scanOne`
    - Predicted Functions (0):

- **File:** `src/fmt/scan_test.go`
    - Ground Truth Functions (2):
        - `TestScanf`
        - `testScan`
    - Predicted Functions (0):

- **File:** `src/go/ast/print.go`
    - Ground Truth Functions (2):
        - `NotNilFilter`
        - `print`
    - Predicted Functions (0):

- **File:** `src/html/template/content.go`
    - Ground Truth Functions (2):
        - `indirect`
        - `indirectToStringerOrError`
    - Predicted Functions (0):

- **File:** `src/html/template/js.go`
    - Ground Truth Functions (1):
        - `indirectToJSONMarshaler`
    - Predicted Functions (0):

- **File:** `src/internal/fmtsort/sort.go`
    - Ground Truth Functions (1):
        - `compare`
    - Predicted Functions (0):

- **File:** `src/internal/reflectlite/tostring_test.go`
    - Ground Truth Functions (1):
        - `valueToStringImpl`
    - Predicted Functions (0):

- **File:** `src/internal/reflectlite/value.go`
    - Ground Truth Functions (2):
        - `Elem`
        - `IsNil`
    - Predicted Functions (0):

- **File:** `src/net/rpc/server.go`
    - Ground Truth Functions (4):
        - `isExportedOrBuiltinType`
        - `readRequest`
        - `register`
        - `suitableMethods`
    - Predicted Functions (0):

- **File:** `src/reflect/abi.go`
    - Ground Truth Functions (1):
        - `regAssign`
    - Predicted Functions (1):
        - ❌ `dumpPtrBitMap`

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (8):
        - `TestArrayOfDirectIface`
        - `TestCanSetField`
        - `TestGCBits`
        - `TestIsZero`
        - `TestPtrTo`
        - `TestPtrToGC`
        - `TestStructOfWithInterface`
        - `TestTypeOfTypeOf`
    - Predicted Functions (0):

- **File:** `src/reflect/deepequal.go`
    - Ground Truth Functions (1):
        - `deepValueEqual`
    - Predicted Functions (0):

- **File:** `src/reflect/iter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/tostring_test.go`
    - Ground Truth Functions (1):
        - `valueToString`
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (12):
        - `Elem`
        - `FieldByIndex`
        - `FieldByNameFunc`
        - `StructOf`
        - `TypeOf`
        - `addTypeBits`
        - `append`
        - `funcStr`
        - `haveIdenticalUnderlyingType`
        - `isReflexive`
        - `needKeyUpdate`
        - `uncommon`
    - Predicted Functions (3):
        - ❌ `PointerTo`
        - ❌ `PtrTo`
        - ❌ `ptrTo`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (14):
        - `Addr`
        - `CanConvert`
        - `Elem`
        - `FieldByIndex`
        - `Index`
        - `Indirect`
        - `IsNil`
        - `IsZero`
        - `New`
        - `NewAt`
        - `Pointer`
        - `UnsafePointer`
        - `convertOp`
        - `cvtSliceArrayPtr`
    - Predicted Functions (3):
        - ✅ `Pointer`
        - ❌ `SetPointer`
        - ✅ `UnsafePointer`

- **File:** `src/reflect/visiblefields.go`
    - Ground Truth Functions (1):
        - `walk`
    - Predicted Functions (0):

- **File:** `src/testing/quick/quick.go`
    - Ground Truth Functions (1):
        - `sizedValue`
    - Predicted Functions (0):

- **File:** `src/text/template/exec.go`
    - Ground Truth Functions (6):
        - `canBeNil`
        - `evalField`
        - `indirect`
        - `isTrue`
        - `printableValue`
        - `validateType`
    - Predicted Functions (0):

- **File:** `test/fixedbugs/issue32901.dir/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `test/reflectmethod7.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #35804 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 100.0% | 44.4% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/database/sql/sql.go`
    - Ground Truth Functions (1):
        - `Err`
    - Predicted Functions (4):
        - ✅ `Err`
        - ❌ `QueryRow`
        - ❌ `QueryRowContext`
        - ❌ `Scan`

- **File:** `src/database/sql/sql_test.go`
    - Ground Truth Functions (1):
        - `TestRowErr`
    - Predicted Functions (3):
        - ❌ `QueryRowContext`
        - ❌ `TestQueryRow`
        - ✅ `TestRowErr`


### 📊 **Proposal #48152 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.3% | 40.0% | 6.2% | 2/5 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (2):
        - `Error`
        - `Unwrap`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (1):
        - `verifyServerCertificate`
    - Predicted Functions (3):
        - ❌ `clientHandshake`
        - ❌ `getClientCertificate`
        - ✅ `verifyServerCertificate`

- **File:** `src/crypto/tls/handshake_client_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `CertificateVerificationError`
        - ❌ `TestVerifyConnection`
        - ❌ `TestVerifyPeerCertificate`
        - ❌ `VerifyConnection`
        - ❌ `VerifyPeerCertificate`

- **File:** `src/crypto/tls/handshake_messages.go`
    - Ground Truth Functions (0):
    - Predicted Functions (12):
        - ❌ `(*certificateMsg) marshal`
        - ❌ `(*certificateMsg) unmarshal`
        - ❌ `(*certificateMsgTLS13) marshal`
        - ❌ `(*certificateMsgTLS13) unmarshal`
        - ❌ `(*certificateRequestMsg) marshal`
        - ❌ `(*certificateRequestMsg) unmarshal`
        - ❌ `(*certificateRequestMsgTLS13) marshal`
        - ❌ `(*certificateRequestMsgTLS13) unmarshal`
        - ❌ `(*clientKeyExchangeMsg) marshal`
        - ❌ `(*clientKeyExchangeMsg) unmarshal`
        - ❌ `marshalCertificate`
        - ❌ `unmarshalCertificate`

- **File:** `src/crypto/tls/handshake_messages_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Error`
        - ❌ `Generate`

- **File:** `src/crypto/tls/handshake_server.go`
    - Ground Truth Functions (1):
        - `processCertsFromClient`
    - Predicted Functions (4):
        - ❌ `handshake`
        - ✅ `processCertsFromClient`
        - ❌ `readClientHello`
        - ❌ `serverHandshake`

- **File:** `src/crypto/tls/handshake_server_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestClientAuth`
        - ❌ `TestClientHelloFailure`
        - ❌ `TestHandshakeServerSNIGetCertificateError`
        - ❌ `TestSNIGivenOnFailure`

- **File:** `src/crypto/x509/verify.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `CertificateInvalidError`
        - ❌ `HostnameError`
        - ❌ `SystemRootsError`
        - ❌ `UnknownAuthorityError`
        - ❌ `Verify`
        - ❌ `VerifyHostname`

- **File:** `src/crypto/x509/verify_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestSystemRootsError`
        - ❌ `TestSystemRootsErrorUnwrap`
        - ❌ `TestSystemVerify`
        - ❌ `TestUnknownAuthorityError`
        - ❌ `TestVerify`

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `CheckCRLSignature`
        - ❌ `CheckSignature`
        - ❌ `CheckSignatureFrom`
        - ❌ `CreateCertificate`
        - ❌ `CreateCertificateRequest`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (14):
        - ❌ `TestCertificateParse`
        - ❌ `TestCreateCertificateBrokenSigner`
        - ❌ `TestCreateCertificateLegacy`
        - ❌ `TestCreateCertificateRequest`
        - ❌ `TestCreateRevocationList`
        - ❌ `TestCreateSelfSignedCertificate`
        - ❌ `TestMatchHostnames`
        - ❌ `TestMatchIP`
        - ❌ `TestParseCertificateWithDSASignatureAlgorithm`
        - ❌ `TestParseCertificateWithDsaPublicKey`
        - ❌ `TestParsePKIXPublicKey`
        - ❌ `TestParseRevocationList`
        - ❌ `TestRevocationListCheckSignatureFrom`
        - ❌ `TestVerifyCertificateWithDSASignature`

- **File:** `src/net/http/transport_test.go`
    - Ground Truth Functions (1):
        - `testTransportEventTraceTLSVerify`
    - Predicted Functions (0):


### 📊 **Proposal #48424 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/51 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/noder/noder.go`
    - Ground Truth Functions (1):
        - `LoadPackage`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/syntax/error_test.go`
    - Ground Truth Functions (1):
        - `testSyntaxErrors`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/syntax/parser.go`
    - Ground Truth Functions (9):
        - `fieldDecl`
        - `funcDeclOrNil`
        - `interfaceType`
        - `methodDecl`
        - `nameList`
        - `paramDeclOrNil`
        - `paramList`
        - `qualifiedName`
        - `typeDecl`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/syntax/parser_test.go`
    - Ground Truth Functions (2):
        - `TestParse`
        - `TestVerify`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/syntax/printer_test.go`
    - Ground Truth Functions (1):
        - `TestPrintString`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/check_test.go`
    - Ground Truth Functions (1):
        - `testFiles`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/decl.go`
    - Ground Truth Functions (2):
        - `bound`
        - `collectTypeParams`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/interface.go`
    - Ground Truth Functions (1):
        - `interfaceType`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/typeparam.go`
    - Ground Truth Functions (2):
        - `SetConstraint`
        - `iface`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/typestring.go`
    - Ground Truth Functions (1):
        - `typ`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/universe.go`
    - Ground Truth Functions (1):
        - `defPredeclaredTypes`
    - Predicted Functions (0):

- **File:** `src/go/internal/gcimporter/gcimporter_test.go`
    - Ground Truth Functions (1):
        - `TestImportTypeparamTests`
    - Predicted Functions (0):

- **File:** `src/go/parser/parser.go`
    - Ground Truth Functions (17):
        - `embeddedElem`
        - `embeddedTerm`
        - `parseArrayFieldOrTypeInstance`
        - `parseFuncType`
        - `parseGenericType`
        - `parseIndexOrSliceOrInstance`
        - `parseInterfaceType`
        - `parseMapType`
        - `parseMethodSpec`
        - `parseParamDecl`
        - `parseParameterList`
        - `parseParameters`
        - `parseQualifiedIdent`
        - `parseTypeInstance`
        - `parseTypeSpec`
        - `parseValueSpec`
        - `tryIdentOrType`
    - Predicted Functions (0):

- **File:** `src/go/types/decl.go`
    - Ground Truth Functions (2):
        - `bound`
        - `collectTypeParams`
    - Predicted Functions (0):

- **File:** `src/go/types/interface.go`
    - Ground Truth Functions (1):
        - `interfaceType`
    - Predicted Functions (0):

- **File:** `src/go/types/typeparam.go`
    - Ground Truth Functions (2):
        - `SetConstraint`
        - `iface`
    - Predicted Functions (0):

- **File:** `src/go/types/typestring.go`
    - Ground Truth Functions (1):
        - `typ`
    - Predicted Functions (0):

- **File:** `src/go/types/universe.go`
    - Ground Truth Functions (1):
        - `defPredeclaredTypes`
    - Predicted Functions (0):

- **File:** `src/maps/maps.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Clone`
        - ❌ `EqualFunc`

- **File:** `src/maps/maps_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestClone`
        - ❌ `TestEqualFunc`

- **File:** `test/typeparam/issue48424.go`
    - Ground Truth Functions (4):
        - `identity`
        - `main`
        - `max`
        - `min`
    - Predicted Functions (0):


### 📊 **Proposal #39557 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 75.0% | 31.6% | 3/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/internal/objabi/flag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Flagfn1`
        - ❌ `Set`
        - ❌ `String`

- **File:** `src/flag/example_flagset_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ExampleFlagSet`

- **File:** `src/flag/example_func_test.go`
    - Ground Truth Functions (1):
        - `ExampleFunc`
    - Predicted Functions (2):
        - ❌ `ExampleBoolFunc`
        - ✅ `ExampleFunc`

- **File:** `src/flag/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Set`
        - ❌ `String`

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (1):
        - `Func`
    - Predicted Functions (5):
        - ❌ `Callback`
        - ✅ `Func`
        - ❌ `PrintDefaults`
        - ❌ `Set`
        - ❌ `Var`

- **File:** `src/flag/flag_test.go`
    - Ground Truth Functions (2):
        - `TestEverything`
        - `TestUserDefinedFunc`
    - Predicted Functions (2):
        - ❌ `TestUserDefinedBoolFunc`
        - ✅ `TestUserDefinedFunc`


### 📊 **Proposal #40281 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
    - Ground Truth Functions (1):
        - `validateStructTag`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/testdata/structtag/structtag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `CheckStructTag`
        - ❌ `ParseStructTag`
        - ❌ `funcLiteral`

- **File:** `src/encoding/json/tags.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `parseTag`

- **File:** `src/encoding/json/tags_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestTagParsing`

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (1):
        - `Lookup`
    - Predicted Functions (0):


### 📊 **Proposal #41730 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/20 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/go_test.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/envcmd/env.go`
    - Ground Truth Functions (1):
        - `MkEnv`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/proxy.go`
    - Ground Truth Functions (1):
        - `proxyList`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modget/get.go`
    - Ground Truth Functions (2):
        - `Set`
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vcs/vcs.go`
    - Ground Truth Functions (10):
        - `FromDir`
        - `RepoRootForImportPath`
        - `allow`
        - `checkGOVCS`
        - `httpPrefix`
        - `matchGoImport`
        - `parseGOVCS`
        - `repoRootForImportDynamic`
        - `repoRootFromVCSPaths`
        - `validateRepoRoot`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vcs/vcs_test.go`
    - Ground Truth Functions (4):
        - `TestGOVCS`
        - `TestGOVCSErrors`
        - `TestRepoRootForImportPath`
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/main.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):


### 📊 **Proposal #48530 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/net.go`
    - Ground Truth Functions (1):
        - `genericWriteTo`
    - Predicted Functions (0):

- **File:** `src/net/splice_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `spliceFrom`
        - ❌ `spliceTo`

- **File:** `src/net/tcpsock.go`
    - Ground Truth Functions (1):
        - `WriteTo`
    - Predicted Functions (0):

- **File:** `src/net/tcpsock_plan9.go`
    - Ground Truth Functions (1):
        - `writeTo`
    - Predicted Functions (0):

- **File:** `src/net/tcpsock_posix.go`
    - Ground Truth Functions (1):
        - `writeTo`
    - Predicted Functions (0):


### 📊 **Proposal #51766 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/net.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `IPv6LinkLocalAllRouters`

- **File:** `src/net/netip/netip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `AddrFrom16`
        - ❌ `IPv6LinkLocalAllNodes`
        - ❌ `IPv6LinkLocalAllRouters`

- **File:** `src/net/netip/netip_test.go`
    - Ground Truth Functions (2):
        - `TestAddrWellKnown`
        - `TestNoAllocs`
    - Predicted Functions (0):


### 📊 **Proposal #34875 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/go/doc/comment.go`
    - Ground Truth Functions (2):
        - `ToHTML`
        - `ToText`
    - Predicted Functions (2):
        - ✅ `ToHTML`
        - ✅ `ToText`

- **File:** `src/go/doc/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `HTML`
        - ❌ `Markdown`
        - ❌ `Text`

- **File:** `src/net/http/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #39034 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 13.6% | 50.0% | 21.4% | 3/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `lib/time/mkzip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/fmt/format.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `fmtQ`
        - ❌ `fmtS`

- **File:** `src/fmt/print.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `Fprintf`
        - ❌ `Print`
        - ❌ `Printf`
        - ❌ `Sprint`
        - ❌ `Sprintf`
        - ❌ `fmtPointer`
        - ❌ `fmtString`
        - ❌ `handleMethods`
        - ❌ `printValue`

- **File:** `src/time/format.go`
    - Ground Truth Functions (3):
        - `AppendFormat`
        - `GoString`
        - `quote`
    - Predicted Functions (4):
        - ✅ `AppendFormat`
        - ❌ `Format`
        - ✅ `GoString`
        - ❌ `String`

- **File:** `src/time/format_test.go`
    - Ground Truth Functions (3):
        - `TestGoString`
        - `TestParseYday`
        - `TestQuote`
    - Predicted Functions (1):
        - ✅ `TestGoString`

- **File:** `src/time/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Date`
        - ❌ `GoString`
        - ❌ `Location`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `BenchmarkGoString`
        - ❌ `TestDate`
        - ❌ `TestTimeIsDST`


### 📊 **Proposal #46518 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 64.7% | 23.1% | 34.0% | 33/143 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/internal/fuzz/fuzz.go`
    - Ground Truth Functions (1):
        - `shouldPrintDebugInfo`
    - Predicted Functions (0):

- **File:** `src/internal/godebug/godebug_test.go`
    - Ground Truth Functions (1):
        - `TestGet`
    - Predicted Functions (0):

- **File:** `src/net/conf.go`
    - Ground Truth Functions (1):
        - `goDebugNetDNS`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (1):
        - `onceSetNextProtoDefaults`
    - Predicted Functions (0):

- **File:** `src/net/http/transport.go`
    - Ground Truth Functions (1):
        - `onceSetNextProtoDefaults`
    - Predicted Functions (0):

- **File:** `src/net/lookup.go`
    - Ground Truth Functions (1):
        - `LookupNetIP`
    - Predicted Functions (0):

- **File:** `src/net/net.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `LookupNetAddr`
        - ❌ `ReadMsgUDPAddrPort`
        - ❌ `TCPAddrPort`
        - ❌ `UDPAddrPort`
        - ❌ `WriteMsgUDPAddrPort`
        - ❌ `WriteToUDPAddrPort`

- **File:** `src/net/netip/export_test.go`
    - Ground Truth Functions (2):
        - `Mk128`
        - `MkAddr`
    - Predicted Functions (0):

- **File:** `src/net/netip/inlining_test.go`
    - Ground Truth Functions (1):
        - `TestInlining`
    - Predicted Functions (0):

- **File:** `src/net/netip/netip.go`
    - Ground Truth Functions (58):
        - `AddrFrom16`
        - `AddrFrom4`
        - `AddrFromSlice`
        - `AppendTo`
        - `As16`
        - `As4`
        - `BitLen`
        - `Compare`
        - `Contains`
        - `Error`
        - `Is4`
        - `Is4In6`
        - `Is6`
        - `IsGlobalUnicast`
        - `IsInterfaceLocalMulticast`
        - `IsLinkLocalMulticast`
        - `IsLinkLocalUnicast`
        - `IsLoopback`
        - `IsMulticast`
        - `IsPrivate`
        - `IsUnspecified`
        - `MarshalBinary`
        - `MarshalText`
        - `Masked`
        - `MustParseAddr`
        - `MustParseAddrPort`
        - `MustParsePrefix`
        - `Next`
        - `Overlaps`
        - `ParseAddr`
        - `ParseAddrPort`
        - `ParsePrefix`
        - `Prefix`
        - `PrefixFrom`
        - `Prev`
        - `String`
        - `StringExpanded`
        - `Unmap`
        - `UnmarshalBinary`
        - `UnmarshalText`
        - `WithZone`
        - `Zone`
        - `appendDecimal`
        - `appendHex`
        - `appendHexPad`
        - `appendTo4`
        - `appendTo6`
        - `hasZone`
        - `isZero`
        - `parseIPv4`
        - `parseIPv6`
        - `splitAddrPort`
        - `string4`
        - `string6`
        - `v4`
        - `v6`
        - `v6u16`
        - `withoutZone`
    - Predicted Functions (29):
        - ✅ `AddrFrom16`
        - ✅ `AddrFrom4`
        - ✅ `AddrFromSlice`
        - ❌ `AddrPortFrom`
        - ✅ `AppendTo`
        - ✅ `As16`
        - ✅ `As4`
        - ✅ `BitLen`
        - ✅ `Compare`
        - ✅ `Contains`
        - ✅ `Is4`
        - ✅ `Is4In6`
        - ✅ `Is6`
        - ❌ `IsSingleIP`
        - ❌ `IsValid`
        - ❌ `Less`
        - ✅ `MustParseAddr`
        - ✅ `MustParseAddrPort`
        - ✅ `Next`
        - ✅ `Overlaps`
        - ✅ `ParseAddr`
        - ✅ `ParseAddrPort`
        - ✅ `Prefix`
        - ✅ `PrefixFrom`
        - ✅ `Prev`
        - ✅ `String`
        - ✅ `Unmap`
        - ✅ `WithZone`
        - ✅ `Zone`

- **File:** `src/net/netip/netip_pkg_test.go`
    - Ground Truth Functions (11):
        - `BenchmarkIPNextPrev`
        - `TestAddrPortMarshalUnmarshal`
        - `TestIPBitLen`
        - `TestIPNextPrev`
        - `TestIPv6Accessor`
        - `TestParseAddrPort`
        - `TestParseIPError`
        - `TestPrefixContains`
        - `TestPrefixValid`
        - `doNextPrev`
        - `testAppendToMarshal`
    - Predicted Functions (0):

- **File:** `src/net/netip/netip_test.go`
    - Ground Truth Functions (41):
        - `BenchmarkAddrPortMarshalText`
        - `BenchmarkAddrPortString`
        - `BenchmarkBinaryMarshalRoundTrip`
        - `BenchmarkIPStringExpanded`
        - `BenchmarkIPv4`
        - `BenchmarkIPv4Contains`
        - `BenchmarkIPv4_inline`
        - `BenchmarkIPv6`
        - `BenchmarkIPv6Contains`
        - `BenchmarkParseAddr`
        - `BenchmarkParseAddrPort`
        - `BenchmarkPrefixMarshalText`
        - `BenchmarkPrefixMasking`
        - `BenchmarkStdIPv4`
        - `BenchmarkStdIPv6`
        - `BenchmarkStdParseIP`
        - `TestAddrFrom16`
        - `TestAddrMarshalUnmarshal`
        - `TestAddrMarshalUnmarshalBinary`
        - `TestAddrWellKnown`
        - `TestAs4`
        - `TestIPProperties`
        - `TestIPStringExpanded`
        - `TestIPv4Constructors`
        - `TestIs4AndIs6`
        - `TestIs4In6`
        - `TestNoAllocs`
        - `TestParseAddr`
        - `TestParsePrefixAllocs`
        - `TestParsePrefixError`
        - `TestPrefix`
        - `TestPrefixFromInvalidBits`
        - `TestPrefixIsSingleIP`
        - `TestPrefixMarshalUnmarshal`
        - `TestPrefixMasked`
        - `TestPrefixMasking`
        - `TestPrefixOverlaps`
        - `TestPrefixString`
        - `TestPrefixUnmarshalTextNonZero`
        - `mustIPs`
        - `newip4i_v4`
    - Predicted Functions (16):
        - ❌ `TestAddrAppendText`
        - ✅ `TestAddrFrom16`
        - ❌ `TestAddrFromSlice`
        - ❌ `TestAddrLessCompare`
        - ✅ `TestAddrMarshalUnmarshal`
        - ✅ `TestAddrMarshalUnmarshalBinary`
        - ❌ `TestAddrPortCompare`
        - ❌ `TestAddrPortString`
        - ❌ `TestAddrString`
        - ❌ `TestAsSlice`
        - ✅ `TestIPProperties`
        - ✅ `TestNoAllocs`
        - ✅ `TestParseAddr`
        - ❌ `TestPrefixCompare`
        - ✅ `TestPrefixIsSingleIP`
        - ✅ `TestPrefixOverlaps`

- **File:** `src/net/netip/slow_test.go`
    - Ground Truth Functions (4):
        - `normalizeIPv6Slow`
        - `parseIPSlow`
        - `parseIPv4Slow`
        - `parseWord`
    - Predicted Functions (0):

- **File:** `src/net/netip/uint128.go`
    - Ground Truth Functions (10):
        - `addOne`
        - `and`
        - `bitsClearedFrom`
        - `bitsSetFrom`
        - `halves`
        - `mask6`
        - `not`
        - `or`
        - `subOne`
        - `xor`
    - Predicted Functions (0):

- **File:** `src/net/netip/uint128_test.go`
    - Ground Truth Functions (3):
        - `TestBitsClearedFrom`
        - `TestBitsSetFrom`
        - `TestUint128AddSub`
    - Predicted Functions (0):

- **File:** `src/net/parse_test.go`
    - Ground Truth Functions (1):
        - `TestDtoi`
    - Predicted Functions (0):

- **File:** `src/net/tcpsock.go`
    - Ground Truth Functions (1):
        - `AddrPort`
    - Predicted Functions (0):

- **File:** `src/net/udpsock.go`
    - Ground Truth Functions (5):
        - `AddrPort`
        - `ReadMsgUDPAddrPort`
        - `UDPAddrFromAddrPort`
        - `WriteMsgUDPAddrPort`
        - `WriteToUDPAddrPort`
    - Predicted Functions (0):


### 📊 **Proposal #42537 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 1.9% | 3.4% | 2/108 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/strconv.go`
    - Ground Truth Functions (5):
        - `formatPAXRecord`
        - `hasNUL`
        - `parsePAXRecord`
        - `parsePAXTime`
        - `validPAXRecord`
    - Predicted Functions (0):

- **File:** `src/archive/tar/writer_test.go`
    - Ground Truth Functions (1):
        - `TestIssue12594`
    - Predicted Functions (0):

- **File:** `src/archive/zip/writer_test.go`
    - Ground Truth Functions (1):
        - `TestWriterDirAttributes`
    - Predicted Functions (0):

- **File:** `src/bytes/bytes.go`
    - Ground Truth Functions (2):
        - `CutPrefix`
        - `CutSuffix`
    - Predicted Functions (0):

- **File:** `src/bytes/bytes_test.go`
    - Ground Truth Functions (2):
        - `TestCutPrefix`
        - `TestCutSuffix`
    - Predicted Functions (0):

- **File:** `src/cmd/doc/dirs.go`
    - Ground Truth Functions (1):
        - `findCodeRoots`
    - Predicted Functions (0):

- **File:** `src/cmd/doc/pkg.go`
    - Ground Truth Functions (1):
        - `oneLineNodeDepth`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/typecheck.go`
    - Ground Truth Functions (1):
        - `typecheck1`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/clean/clean.go`
    - Ground Truth Functions (1):
        - `clean`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/pkg.go`
    - Ground Truth Functions (1):
        - `PackagesAndErrorsOutsideModule`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/load.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/go/proxy_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `proxyHandler`

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (1):
        - `errorCheck`
    - Predicted Functions (0):

- **File:** `src/crypto/ecdsa/ecdsa_test.go`
    - Ground Truth Functions (1):
        - `TestVectors`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_client_test.go`
    - Ground Truth Functions (1):
        - `Write`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_test.go`
    - Ground Truth Functions (1):
        - `parseTestData`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/pem_decrypt.go`
    - Ground Truth Functions (1):
        - `DecryptPEMBlock`
    - Predicted Functions (0):

- **File:** `src/encoding/asn1/common.go`
    - Ground Truth Functions (1):
        - `parseFieldParameters`
    - Predicted Functions (0):

- **File:** `src/encoding/json/tags.go`
    - Ground Truth Functions (2):
        - `Contains`
        - `parseTag`
    - Predicted Functions (0):

- **File:** `src/encoding/pem/pem.go`
    - Ground Truth Functions (1):
        - `Decode`
    - Predicted Functions (0):

- **File:** `src/encoding/xml/typeinfo.go`
    - Ground Truth Functions (1):
        - `structFieldInfo`
    - Predicted Functions (0):

- **File:** `src/encoding/xml/xml.go`
    - Ground Truth Functions (3):
        - `emitCDATA`
        - `nsname`
        - `procInst`
    - Predicted Functions (0):

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (4):
        - `findImportComment`
        - `goodOSArchFile`
        - `hasSubdir`
        - `saveCgo`
    - Predicted Functions (0):

- **File:** `src/go/build/build_test.go`
    - Ground Truth Functions (1):
        - `TestMissingImportErrorRepetition`
    - Predicted Functions (0):

- **File:** `src/go/build/read.go`
    - Ground Truth Functions (1):
        - `parseGoEmbed`
    - Predicted Functions (0):

- **File:** `src/go/build/read_test.go`
    - Ground Truth Functions (1):
        - `testRead`
    - Predicted Functions (0):

- **File:** `src/go/constant/value_test.go`
    - Ground Truth Functions (2):
        - `testNumbers`
        - `val`
    - Predicted Functions (0):

- **File:** `src/go/doc/headscan.go`
    - Ground Truth Functions (2):
        - `appendHeadings`
        - `main`
    - Predicted Functions (0):

- **File:** `src/go/importer/importer_test.go`
    - Ground Truth Functions (1):
        - `TestForCompiler`
    - Predicted Functions (0):

- **File:** `src/go/printer/comment.go`
    - Ground Truth Functions (1):
        - `formatDocComment`
    - Predicted Functions (0):

- **File:** `src/go/printer/nodes.go`
    - Ground Truth Functions (1):
        - `normalizedNumber`
    - Predicted Functions (0):

- **File:** `src/go/printer/printer.go`
    - Ground Truth Functions (1):
        - `stripCommonPrefix`
    - Predicted Functions (0):

- **File:** `src/go/types/eval_test.go`
    - Ground Truth Functions (1):
        - `split`
    - Predicted Functions (0):

- **File:** `src/html/template/attr.go`
    - Ground Truth Functions (1):
        - `attrType`
    - Predicted Functions (0):

- **File:** `src/html/template/js.go`
    - Ground Truth Functions (1):
        - `isJSType`
    - Predicted Functions (0):

- **File:** `src/html/template/url.go`
    - Ground Truth Functions (1):
        - `isSafeURL`
    - Predicted Functions (0):

- **File:** `src/mime/encodedword.go`
    - Ground Truth Functions (1):
        - `Decode`
    - Predicted Functions (0):

- **File:** `src/mime/mediatype.go`
    - Ground Truth Functions (2):
        - `FormatMediaType`
        - `ParseMediaType`
    - Predicted Functions (0):

- **File:** `src/net/http/cgi/child.go`
    - Ground Truth Functions (1):
        - `envMap`
    - Predicted Functions (0):

- **File:** `src/net/http/cgi/host.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (0):

- **File:** `src/net/http/cgi/host_test.go`
    - Ground Truth Functions (1):
        - `runResponseChecks`
    - Predicted Functions (0):

- **File:** `src/net/http/client_test.go`
    - Ground Truth Functions (1):
        - `testRedirectsByMethod`
    - Predicted Functions (0):

- **File:** `src/net/http/cookie.go`
    - Ground Truth Functions (3):
        - `readCookies`
        - `readSetCookies`
        - `sanitizeCookieValue`
    - Predicted Functions (0):

- **File:** `src/net/http/fs.go`
    - Ground Truth Functions (1):
        - `parseRange`
    - Predicted Functions (0):

- **File:** `src/net/http/internal/chunked.go`
    - Ground Truth Functions (1):
        - `removeChunkExtension`
    - Predicted Functions (0):

- **File:** `src/net/http/main_test.go`
    - Ground Truth Functions (1):
        - `interestingGoroutines`
    - Predicted Functions (0):

- **File:** `src/net/http/request.go`
    - Ground Truth Functions (3):
        - `BasicAuth`
        - `parseBasicAuth`
        - `parseRequestLine`
    - Predicted Functions (0):

- **File:** `src/net/http/response.go`
    - Ground Truth Functions (1):
        - `ReadResponse`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (1):
        - `stripHostPort`
    - Predicted Functions (0):

- **File:** `src/net/http/transport.go`
    - Ground Truth Functions (1):
        - `dialConn`
    - Predicted Functions (0):

- **File:** `src/net/mail/message.go`
    - Ground Truth Functions (1):
        - `ParseDate`
    - Predicted Functions (0):

- **File:** `src/net/main_posix_test.go`
    - Ground Truth Functions (1):
        - `disableSocketConnect`
    - Predicted Functions (0):

- **File:** `src/net/main_test.go`
    - Ground Truth Functions (1):
        - `runningGoroutines`
    - Predicted Functions (0):

- **File:** `src/net/platform_test.go`
    - Ground Truth Functions (3):
        - `testableAddress`
        - `testableListenArgs`
        - `testableNetwork`
    - Predicted Functions (0):

- **File:** `src/net/smtp/smtp.go`
    - Ground Truth Functions (1):
        - `ehlo`
    - Predicted Functions (0):

- **File:** `src/net/textproto/reader.go`
    - Ground Truth Functions (1):
        - `ReadMIMEHeader`
    - Predicted Functions (0):

- **File:** `src/net/url/url.go`
    - Ground Truth Functions (6):
        - `Parse`
        - `String`
        - `parse`
        - `parseAuthority`
        - `parseQuery`
        - `resolvePath`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (2):
        - `addCriticalEnv`
        - `dedupEnvCase`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (1):
        - `TestCatGoodAndBadFile`
    - Predicted Functions (0):

- **File:** `src/os/os_test.go`
    - Ground Truth Functions (1):
        - `TestHostname`
    - Predicted Functions (0):

- **File:** `src/os/user/cgo_lookup_unix.go`
    - Ground Truth Functions (1):
        - `buildUser`
    - Predicted Functions (0):

- **File:** `src/os/user/lookup_unix.go`
    - Ground Truth Functions (1):
        - `matchUserIndexValue`
    - Predicted Functions (0):

- **File:** `src/regexp/exec_test.go`
    - Ground Truth Functions (2):
        - `parseResult`
        - `testFowler`
    - Predicted Functions (0):

- **File:** `src/regexp/regexp.go`
    - Ground Truth Functions (2):
        - `expand`
        - `extract`
    - Predicted Functions (0):

- **File:** `src/regexp/syntax/parse.go`
    - Ground Truth Functions (1):
        - `Parse`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/pprof_test.go`
    - Ground Truth Functions (2):
        - `containsInOrder`
        - `stackContainsLabeled`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/proto.go`
    - Ground Truth Functions (1):
        - `parseProcSelfMaps`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/proto_test.go`
    - Ground Truth Functions (1):
        - `TestProcSelfMaps`
    - Predicted Functions (0):

- **File:** `src/runtime/runtime-gdb_test.go`
    - Ground Truth Functions (1):
        - `testGdbPython`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprog/numcpu_freebsd.go`
    - Ground Truth Functions (1):
        - `getList`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprog/traceback_ancestors.go`
    - Ground Truth Functions (2):
        - `goroutineID`
        - `printStack`
    - Predicted Functions (0):

- **File:** `src/strconv/fp_test.go`
    - Ground Truth Functions (2):
        - `myatof32`
        - `myatof64`
    - Predicted Functions (0):

- **File:** `src/strings/compare.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TrimPrefix`
        - ❌ `TrimSuffix`

- **File:** `src/strings/reader.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strings/replace.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strings/strings.go`
    - Ground Truth Functions (2):
        - `CutPrefix`
        - `CutSuffix`
    - Predicted Functions (5):
        - ❌ `Cut`
        - ✅ `CutPrefix`
        - ✅ `CutSuffix`
        - ❌ `TrimPrefix`
        - ❌ `TrimSuffix`

- **File:** `src/strings/strings_test.go`
    - Ground Truth Functions (2):
        - `TestCutPrefix`
        - `TestCutSuffix`
    - Predicted Functions (0):

- **File:** `src/testing/benchmark.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/testing/benchmark_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/testing/fstest/mapfs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/testing/fstest/mapfs_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/text/template/option.go`
    - Ground Truth Functions (1):
        - `setOption`
    - Predicted Functions (0):

- **File:** `test/zerodivide.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #46746 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 42.9% | 54.5% | 3/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (4):
        - `TestConvert`
        - `TestConvertPanic`
        - `TestValue_Comparable`
        - `TestValue_Equal`
    - Predicted Functions (0):

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (3):
        - `CanConvert`
        - `Comparable`
        - `Equal`
    - Predicted Functions (4):
        - ✅ `CanConvert`
        - ✅ `Comparable`
        - ❌ `Convert`
        - ✅ `Equal`


### 📊 **Proposal #37974 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/go/ast/ast.go`
    - Ground Truth Functions (2):
        - `Text`
        - `isDirective`
    - Predicted Functions (0):

- **File:** `src/go/ast/ast_test.go`
    - Ground Truth Functions (1):
        - `TestIsDirective`
    - Predicted Functions (0):

- **File:** `src/go/doc/comment.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ToHTML`
        - ❌ `ToText`

- **File:** `src/go/doc/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `HTML`
        - ❌ `Markdown`
        - ❌ `Parser`
        - ❌ `Printer`
        - ❌ `Text`
        - ❌ `collectFuncs`
        - ❌ `collectTypes`
        - ❌ `collectValues`
        - ❌ `lookupPackage`
        - ❌ `lookupSym`


### 📊 **Proposal #37533 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/internal/objabi/flag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Flagparse`

- **File:** `src/cmd/internal/objabi/flag_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (1):
        - `Parse`
    - Predicted Functions (3):
        - ❌ `NewFlagSet`
        - ✅ `Parse`
        - ❌ `usage`

- **File:** `src/flag/flag_test.go`
    - Ground Truth Functions (1):
        - `TestExitCode`
    - Predicted Functions (3):
        - ✅ `TestExitCode`
        - ❌ `TestHelp`
        - ❌ `TestUsageOutput`

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestExitCode`
        - ❌ `TestExitStatus`

- **File:** `src/testing/flag_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestFlag`

- **File:** `test/fixedbugs/issue37513.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #43401 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 66.7% | 50.0% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/csv/reader.go`
    - Ground Truth Functions (2):
        - `InputOffset`
        - `readLine`
    - Predicted Functions (5):
        - ✅ `InputOffset`
        - ❌ `Read`
        - ❌ `ReadAll`
        - ✅ `readLine`
        - ❌ `readRecord`

- **File:** `src/encoding/csv/reader_test.go`
    - Ground Truth Functions (1):
        - `TestRead`
    - Predicted Functions (0):

- **File:** `src/encoding/csv/writer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/csv/writer_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #41773 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/serve_test.go`
    - Ground Truth Functions (1):
        - `TestOptionsHandler`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (5):
        - ❌ `(*Server).ListenAndServe`
        - ❌ `(*Server).Serve`
        - ❌ `(*Server).ServeTLS`
        - ❌ `globalOptionsHandler.ServeHTTP`
        - ❌ `serverHandler.ServeHTTP`


### 📊 **Proposal #46731 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/32 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/cgo/gcc.go`
    - Ground Truth Functions (4):
        - `Init`
        - `badPointerTypedef`
        - `badVoidPointerTypedef`
        - `loadType`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/out.go`
    - Ground Truth Functions (1):
        - `writeDefs`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/noder.go`
    - Ground Truth Functions (1):
        - `pragma`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/reader.go`
    - Ground Truth Functions (2):
        - `expr`
        - `typeExt`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/writer.go`
    - Ground Truth Functions (1):
        - `Visit`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typebits/typebits.go`
    - Ground Truth Functions (1):
        - `Set`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/func.go`
    - Ground Truth Functions (1):
        - `tcUnsafeSlice`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types/size.go`
    - Ground Truth Functions (1):
        - `CalcSize`
    - Predicted Functions (0):

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (2):
        - `TestIssue50208`
        - `TestMethodCallValueCodePtr`
    - Predicted Functions (0):

- **File:** `src/reflect/deepequal.go`
    - Ground Truth Functions (1):
        - `deepValueEqual`
    - Predicted Functions (0):

- **File:** `src/reflect/nih_test.go`
    - Ground Truth Functions (1):
        - `TestNotInHeapDeref`
    - Predicted Functions (0):

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (1):
        - `New`
    - Predicted Functions (0):

- **File:** `src/runtime/cgo/cgo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Incomplete`

- **File:** `src/runtime/debuglog.go`
    - Ground Truth Functions (9):
        - `byte`
        - `bytes`
        - `ensure`
        - `peek`
        - `printVal`
        - `readUint16LEAt`
        - `readUint64LEAt`
        - `uvarint`
        - `writeFrameAt`
    - Predicted Functions (0):

- **File:** `src/runtime/malloc.go`
    - Ground Truth Functions (1):
        - `add`
    - Predicted Functions (0):

- **File:** `src/runtime/mcheckmark.go`
    - Ground Truth Functions (2):
        - `setCheckmark`
        - `startCheckmarks`
    - Predicted Functions (0):

- **File:** `src/runtime/mheap.go`
    - Ground Truth Functions (1):
        - `bytep`
    - Predicted Functions (0):

- **File:** `src/runtime/mmap.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `mmap`
        - ❌ `munmap`

- **File:** `test/directive.go`
    - Ground Truth Functions (1):
        - `f`
    - Predicted Functions (0):

- **File:** `test/fixedbugs/issue40954.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #47005 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/url/url.go`
    - Ground Truth Functions (1):
        - `JoinPath`
    - Predicted Functions (3):
        - ✅ `JoinPath`
        - ❌ `Parse`
        - ❌ `ResolveReference`

- **File:** `src/net/url/url_test.go`
    - Ground Truth Functions (1):
        - `TestJoinPath`
    - Predicted Functions (3):
        - ❌ `Join`
        - ❌ `JoinPath`
        - ❌ `TestJoin`


### 📊 **Proposal #43620 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/testing/benchmark.go`
    - Ground Truth Functions (1):
        - `Elapsed`
    - Predicted Functions (3):
        - ✅ `Elapsed`
        - ❌ `ReportMetric`
        - ❌ `StopTimer`

- **File:** `src/testing/benchmark_test.go`
    - Ground Truth Functions (1):
        - `ExampleB_ReportMetric`
    - Predicted Functions (3):
        - ✅ `ExampleB_ReportMetric`
        - ❌ `ExampleB_ReportMetric_parallel`
        - ❌ `TestReportMetric`


### 📊 **Proposal #53573 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 20.0% | 22.2% | 1/5 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/parser.go`
    - Ground Truth Functions (1):
        - `ParseRevocationList`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/pkix/pkix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (1):
        - `CreateRevocationList`
    - Predicted Functions (4):
        - ❌ `(*RevocationList) CheckSignatureFrom`
        - ✅ `CreateRevocationList`
        - ❌ `ParseCRL`
        - ❌ `ParseDERCRL`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (3):
        - `TestCreateRevocationList`
        - `TestParseRevocationList`
        - `TestParseUniqueID`
    - Predicted Functions (0):


### 📊 **Proposal #40728 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/89 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/base/flag.go`
    - Ground Truth Functions (4):
        - `AddModCommonFlags`
        - `AddModFlag`
        - `Set`
        - `String`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/fmtcmd/fmt.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/list/list.go`
    - Ground Truth Functions (1):
        - `runList`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/download.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/edit.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/graph.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/init.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/tidy.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/vendor.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/verify.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/why.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modget/get.go`
    - Ground Truth Functions (32):
        - `Set`
        - `checkAllowedOr`
        - `checkWildcardVersions`
        - `chooseArbitrarily`
        - `disambiguate`
        - `findAndUpgradeImports`
        - `findMissingWildcards`
        - `init`
        - `initialSelected`
        - `isNoSuchModuleVersion`
        - `isNoSuchPackageVersion`
        - `loadPackages`
        - `matchInModule`
        - `newResolver`
        - `noneForPath`
        - `parseArgs`
        - `performLocalQueries`
        - `performPathQueries`
        - `performPatternAllQueries`
        - `performWildcardQueries`
        - `queryModule`
        - `queryNone`
        - `queryPackages`
        - `queryPath`
        - `queryPattern`
        - `queryWildcard`
        - `reportChanges`
        - `resolve`
        - `runGet`
        - `selected`
        - `tryWildcard`
        - `updateBuildList`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modget/query.go`
    - Ground Truth Functions (11):
        - `Error`
        - `ResolvedString`
        - `canMatchInModule`
        - `isWildcard`
        - `matchesPath`
        - `newQuery`
        - `pathOnce`
        - `reportConflict`
        - `reportError`
        - `validate`
        - `versionOkForMainModule`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/buildlist.go`
    - Ground Truth Functions (2):
        - `EditBuildList`
        - `Error`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/import.go`
    - Ground Truth Functions (4):
        - `Error`
        - `ImportPath`
        - `Unwrap`
        - `queryImport`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/init.go`
    - Ground Truth Functions (2):
        - `WriteGoMod`
        - `setDefaultBuildMod`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/load.go`
    - Ground Truth Functions (1):
        - `load`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/modfile.go`
    - Ground Truth Functions (3):
        - `Error`
        - `Unwrap`
        - `indexModFile`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/mvs.go`
    - Ground Truth Functions (1):
        - `Previous`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/query.go`
    - Ground Truth Functions (13):
        - `Error`
        - `IsRevisionQuery`
        - `Latest`
        - `QueryPattern`
        - `Stat`
        - `Versions`
        - `allowsVersion`
        - `filterVersions`
        - `lookupRepo`
        - `newQueryMatcher`
        - `queryPrefixModules`
        - `queryProxy`
        - `replacementStat`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/query_test.go`
    - Ground Truth Functions (1):
        - `TestQuery`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/search.go`
    - Ground Truth Functions (2):
        - `MatchInModule`
        - `matchPackages`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (2):
        - `AddBuildFlags`
        - `Set`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/init.go`
    - Ground Truth Functions (1):
        - `buildModeInit`
    - Predicted Functions (0):


### 📊 **Proposal #35567 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 6.2% | 7.1% | 1/16 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/go/build/deps_test.go`
    - Ground Truth Functions (1):
        - `findImports`
    - Predicted Functions (0):

- **File:** `src/runtime/debug/stack_test.go`
    - Ground Truth Functions (1):
        - `TestStack`
    - Predicted Functions (0):

- **File:** `src/testing/benchmark.go`
    - Ground Truth Functions (1):
        - `RunBenchmarks`
    - Predicted Functions (3):
        - ❌ `Benchmark`
        - ❌ `Run`
        - ✅ `RunBenchmarks`

- **File:** `src/testing/benchmark_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `ExampleB_ReportMetric`
        - ❌ `ExampleB_ReportMetric_parallel`
        - ❌ `ExampleB_RunParallel`
        - ❌ `TestBenchmarkContext`

- **File:** `src/testing/example.go`
    - Ground Truth Functions (1):
        - `RunExamples`
    - Predicted Functions (0):

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (12):
        - `CoverMode`
        - `Main`
        - `MainStart`
        - `Run`
        - `RunTests`
        - `after`
        - `before`
        - `listTests`
        - `startAlarm`
        - `stopAlarm`
        - `toOutputDir`
        - `writeProfiles`
    - Predicted Functions (5):
        - ❌ `(*T) Parallel`
        - ❌ `(*T) Run`
        - ❌ `InternalBenchmark`
        - ❌ `InternalExample`
        - ❌ `InternalTest`


### 📊 **Proposal #51682 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.8% | 13.3% | 12.5% | 2/15 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/types2/api_test.go`
    - Ground Truth Functions (2):
        - `TestInstantiatedObjects`
        - `originObject`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/object.go`
    - Ground Truth Functions (2):
        - `NewFunc`
        - `Origin`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/subst.go`
    - Ground Truth Functions (2):
        - `func_`
        - `replaceRecvType`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/flag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/flag_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/elf.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/macho.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/objfile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/pe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/plan9obj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/xcoff.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/alias.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Origin`

- **File:** `src/go/types/api.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ObjectOf`
        - ❌ `TypeOf`

- **File:** `src/go/types/api_predicates.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/api_test.go`
    - Ground Truth Functions (3):
        - `TestInstantiatedObjects`
        - `TestUsesInfo`
        - `originObject`
    - Predicted Functions (0):

- **File:** `src/go/types/builtins.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/check.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/decl.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `funcDecl`
        - ❌ `varDecl`

- **File:** `src/go/types/errors.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/expr.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/generate.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Origin`

- **File:** `src/go/types/instantiate.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/object.go`
    - Ground Truth Functions (2):
        - `NewFunc`
        - `Origin`
    - Predicted Functions (3):
        - ✅ `NewFunc`
        - ❌ `NewVar`
        - ✅ `Origin`

- **File:** `src/go/types/scope.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `(*Scope) Insert`
        - ❌ `(*Scope) Lookup`
        - ❌ `(*lazyObject) Name`
        - ❌ `(*lazyObject) Type`
        - ❌ `NewScope`

- **File:** `src/go/types/signature.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/go/types/subst.go`
    - Ground Truth Functions (2):
        - `func_`
        - `replaceRecvType`
    - Predicted Functions (0):

- **File:** `src/go/types/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Func`
        - ❌ `Origin`
        - ❌ `Var`

- **File:** `src/go/types/typeparam.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #50859 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/race/race.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `Acquire`
        - ❌ `Disable`
        - ❌ `Enable`
        - ❌ `Read`
        - ❌ `Release`
        - ❌ `SetFinalizer`
        - ❌ `Write`
        - ❌ `funcVar`

- **File:** `src/runtime/race/race_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestIssue8102`
        - ❌ `TestIssue9137`
        - ❌ `TestRace`

- **File:** `src/sync/atomic/atomic_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (24):
        - ❌ `TestAddInt32`
        - ❌ `TestAddInt64`
        - ❌ `TestAddUint32`
        - ❌ `TestAddUint64`
        - ❌ `TestCompareAndSwapInt32`
        - ❌ `TestCompareAndSwapInt64`
        - ❌ `TestCompareAndSwapUint32`
        - ❌ `TestCompareAndSwapUint64`
        - ❌ `TestLoadInt32`
        - ❌ `TestLoadInt64`
        - ❌ `TestLoadUint32`
        - ❌ `TestLoadUint64`
        - ❌ `TestStoreInt32`
        - ❌ `TestStoreInt64`
        - ❌ `TestStoreLoadRelAcq32`
        - ❌ `TestStoreLoadRelAcq64`
        - ❌ `TestStoreLoadSeqCst32`
        - ❌ `TestStoreLoadSeqCst64`
        - ❌ `TestStoreUint32`
        - ❌ `TestStoreUint64`
        - ❌ `TestSwapInt32`
        - ❌ `TestSwapInt64`
        - ❌ `TestSwapUint32`
        - ❌ `TestSwapUint64`

- **File:** `src/sync/atomic/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (12):
        - ❌ `CompareAndSwapInt32`
        - ❌ `CompareAndSwapPointer`
        - ❌ `CompareAndSwapUint32`
        - ❌ `CompareAndSwapUintptr`
        - ❌ `LoadInt32`
        - ❌ `LoadPointer`
        - ❌ `LoadUint32`
        - ❌ `LoadUintptr`
        - ❌ `StoreInt32`
        - ❌ `StorePointer`
        - ❌ `StoreUint32`
        - ❌ `StoreUintptr`

- **File:** `src/sync/atomic/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Add`
        - ❌ `And`
        - ❌ `CompareAndSwap`
        - ❌ `Load`
        - ❌ `Or`
        - ❌ `Store`
        - ❌ `Swap`

- **File:** `src/sync/atomic/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `CompareAndSwap`
        - ❌ `Load`
        - ❌ `Store`
        - ❌ `Swap`

- **File:** `src/sync/atomic/value_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `BenchmarkValueRead`
        - ❌ `TestValue`
        - ❌ `TestValueConcurrent`
        - ❌ `TestValue_CompareAndSwap`

- **File:** `src/sync/cond.go`
    - Ground Truth Functions (1):
        - `check`
    - Predicted Functions (0):


### 📊 **Proposal #45973 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 50.0% | 26.7% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/http.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `AllowQuerySemicolons`

- **File:** `src/net/http/request.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `FormValue`
        - ❌ `NewRequest`
        - ❌ `NewRequestWithContext`
        - ❌ `ParseForm`
        - ❌ `ParseMultipartForm`
        - ❌ `PathValue`
        - ❌ `PostFormValue`
        - ❌ `SetPathValue`

- **File:** `src/net/http/response.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/serve_test.go`
    - Ground Truth Functions (2):
        - `TestQuerySemicolon`
        - `testQuerySemicolon`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (2):
        - `AllowQuerySemicolons`
        - `ServeHTTP`
    - Predicted Functions (2):
        - ✅ `AllowQuerySemicolons`
        - ✅ `ServeHTTP`


### 📊 **Proposal #29770 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 52.9% | 36.0% | 42.9% | 9/25 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/html/template/exec_test.go`
    - Ground Truth Functions (1):
        - `TestUnterminatedStringError`
    - Predicted Functions (0):

- **File:** `src/text/template/exec_test.go`
    - Ground Truth Functions (1):
        - `TestUnterminatedStringError`
    - Predicted Functions (0):

- **File:** `src/text/template/parse/lex.go`
    - Ground Truth Functions (11):
        - `atRightDelim`
        - `atTerminator`
        - `hasLeftTrimMarker`
        - `hasRightTrimMarker`
        - `isSpace`
        - `lex`
        - `lexInsideAction`
        - `lexLeftDelim`
        - `lexRightDelim`
        - `lexSpace`
        - `lexText`
    - Predicted Functions (6):
        - ✅ `isSpace`
        - ✅ `lex`
        - ✅ `lexInsideAction`
        - ✅ `lexLeftDelim`
        - ✅ `lexRightDelim`
        - ✅ `lexSpace`

- **File:** `src/text/template/parse/lex_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestDelims`
        - ❌ `TestDelimsAlphaNumeric`
        - ❌ `TestDelimsAndMarkers`
        - ❌ `TestLex`

- **File:** `src/text/template/parse/parse.go`
    - Ground Truth Functions (12):
        - `action`
        - `blockControl`
        - `checkPipeline`
        - `clearActionLine`
        - `command`
        - `elseControl`
        - `parseControl`
        - `pipeline`
        - `templateControl`
        - `term`
        - `textOrAction`
        - `unexpected`
    - Predicted Functions (4):
        - ❌ `Parse`
        - ✅ `action`
        - ✅ `checkPipeline`
        - ✅ `pipeline`

- **File:** `src/text/template/parse/parse_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `BenchmarkParseLarge`
        - ❌ `TestParse`
        - ❌ `TestParseWithComments`


### 📊 **Proposal #50770 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 25.0% | 20.0% | 1/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/time/mono_test.go`
    - Ground Truth Functions (3):
        - `TestMonotonicAdd`
        - `TestMonotonicOverflow`
        - `TestMonotonicSub`
    - Predicted Functions (0):

- **File:** `src/time/time.go`
    - Ground Truth Functions (1):
        - `Compare`
    - Predicted Functions (4):
        - ❌ `After`
        - ❌ `Before`
        - ✅ `Compare`
        - ❌ `Equal`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestAddDate`
        - ❌ `TestSub`


### 📊 **Proposal #45435 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.9% | 33.3% | 11.4% | 2/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/h2_bundle.go`
    - Ground Truth Functions (0):
    - Predicted Functions (23):
        - ❌ `CanTakeNewRequest`
        - ❌ `ReserveNewRequest`
        - ❌ `addConnIfNeeded`
        - ❌ `addConnLocked`
        - ❌ `closeIdleConnections`
        - ❌ `getClientConn`
        - ❌ `getStartDialLocked`
        - ❌ `newStream`
        - ❌ `newWriterAndRequest`
        - ❌ `newWriterAndRequestNoBody`
        - ❌ `processData`
        - ❌ `processFrame`
        - ❌ `processGoAway`
        - ❌ `processHeaders`
        - ❌ `processResetStream`
        - ❌ `processSettings`
        - ❌ `processWindowUpdate`
        - ❌ `writeData`
        - ❌ `writeDataFromHandler`
        - ❌ `writeFrame`
        - ❌ `writeFrameFromHandler`
        - ❌ `writeHeaders`
        - ❌ `writePushPromise`

- **File:** `src/sync/mutex.go`
    - Ground Truth Functions (1):
        - `TryLock`
    - Predicted Functions (3):
        - ❌ `Lock`
        - ✅ `TryLock`
        - ❌ `Unlock`

- **File:** `src/sync/mutex_test.go`
    - Ground Truth Functions (2):
        - `HammerMutex`
        - `TestMutex`
    - Predicted Functions (3):
        - ✅ `TestMutex`
        - ❌ `TestMutexFairness`
        - ❌ `TestMutexMisuse`

- **File:** `src/sync/rwmutex.go`
    - Ground Truth Functions (2):
        - `TryLock`
        - `TryRLock`
    - Predicted Functions (0):

- **File:** `src/sync/rwmutex_test.go`
    - Ground Truth Functions (1):
        - `TestRWMutex`
    - Predicted Functions (0):


### 📊 **Proposal #41066 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.3% | 33.3% | 9.1% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/alert.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/tls/auth.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/tls/cache.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/tls/cipher_suites.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `errClosed`

- **File:** `src/crypto/tls/conn.go`
    - Ground Truth Functions (2):
        - `Close`
        - `Write`
    - Predicted Functions (10):
        - ✅ `Close`
        - ❌ `CloseWrite`
        - ❌ `Handshake`
        - ❌ `Read`
        - ❌ `handshakeContext`
        - ❌ `sendAlert`
        - ❌ `sendAlertLocked`
        - ❌ `write`
        - ❌ `writeHandshakeRecord`
        - ❌ `writeRecordLocked`

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/tls/tls.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `(*Dialer) Dial`
        - ❌ `(*Dialer) netDialer`
        - ❌ `Dial`
        - ❌ `DialContext`
        - ❌ `DialWithDialer`

- **File:** `src/crypto/tls/tls_test.go`
    - Ground Truth Functions (1):
        - `TestConnCloseBreakingWrite`
    - Predicted Functions (0):

- **File:** `src/net/http/http.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/net.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Close`
        - ❌ `Error`
        - ❌ `Is`


### 📊 **Proposal #42027 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 73.3% | 31.4% | 44.0% | 11/35 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `makeGOROOTUnwritable`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/main.go`
    - Ground Truth Functions (1):
        - `walkDir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/go_test.go`
    - Ground Truth Functions (2):
        - `TestNewReleaseRebuildsStalePackagesInGOPATH`
        - `removeAll`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/fetch.go`
    - Ground Truth Functions (2):
        - `RemoveAll`
        - `makeDirsReadOnly`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/version/version.go`
    - Ground Truth Functions (1):
        - `scanDir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/testdata/addmod.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/go/testdata/savedir.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/gofmt/long_test.go`
    - Ground Truth Functions (1):
        - `genFilenames`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/moddeps/moddeps_test.go`
    - Ground Truth Functions (1):
        - `findGorootModules`
    - Predicted Functions (0):

- **File:** `src/compress/gzip/issue14937_test.go`
    - Ground Truth Functions (1):
        - `TestGZIPFilesHaveZeroMTimes`
    - Predicted Functions (0):

- **File:** `src/go/build/deps_test.go`
    - Ground Truth Functions (1):
        - `listStdPkgs`
    - Predicted Functions (0):

- **File:** `src/go/doc/headscan.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/index/suffixarray/suffixarray_test.go`
    - Ground Truth Functions (1):
        - `makeText`
    - Predicted Functions (0):

- **File:** `src/io/fs/walk.go`
    - Ground Truth Functions (2):
        - `WalkDir`
        - `walkDir`
    - Predicted Functions (2):
        - ✅ `WalkDir`
        - ✅ `walkDir`

- **File:** `src/io/fs/walk_test.go`
    - Ground Truth Functions (4):
        - `TestWalkDir`
        - `makeTree`
        - `mark`
        - `walkTree`
    - Predicted Functions (0):

- **File:** `src/path/filepath/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/path/filepath/export_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `WalkDir`
        - ❌ `WalkDirFunc`

- **File:** `src/path/filepath/path.go`
    - Ground Truth Functions (6):
        - `Base`
        - `Walk`
        - `WalkDir`
        - `readDirNames`
        - `walk`
        - `walkDir`
    - Predicted Functions (4):
        - ✅ `Walk`
        - ✅ `WalkDir`
        - ✅ `walk`
        - ✅ `walkDir`

- **File:** `src/path/filepath/path_test.go`
    - Ground Truth Functions (7):
        - `TestWalk`
        - `TestWalkDir`
        - `TestWalkFileError`
        - `TestWalkSkipDirOnFile`
        - `mark`
        - `testWalk`
        - `touch`
    - Predicted Functions (7):
        - ✅ `TestWalk`
        - ✅ `TestWalkDir`
        - ✅ `TestWalkFileError`
        - ❌ `TestWalkSkipAllOnFile`
        - ✅ `TestWalkSkipDirOnFile`
        - ❌ `TestWalkSymlink`
        - ✅ `testWalk`

- **File:** `test/winbatch.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #34626 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 66.7% | 50.0% | 4/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/testing/benchmark.go`
    - Ground Truth Functions (3):
        - `String`
        - `launch`
        - `prettyPrint`
    - Predicted Functions (6):
        - ❌ `BenchmarkResult.NsPerOp`
        - ❌ `BenchmarkResult.String`
        - ❌ `ReportMetric`
        - ❌ `Run`
        - ❌ `RunBenchmarks`
        - ✅ `prettyPrint`

- **File:** `src/testing/benchmark_test.go`
    - Ground Truth Functions (3):
        - `TestPrettyPrint`
        - `TestReportMetric`
        - `TestResultString`
    - Predicted Functions (4):
        - ❌ `ExampleB_ReportMetric`
        - ✅ `TestPrettyPrint`
        - ✅ `TestReportMetric`
        - ✅ `TestResultString`


### 📊 **Proposal #48157 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/11 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/internal/fuzz/minimize_test.go`
    - Ground Truth Functions (2):
        - `TestMinimizeFlaky`
        - `TestMinimizeInput`
    - Predicted Functions (0):

- **File:** `src/internal/fuzz/worker.go`
    - Ground Truth Functions (5):
        - `RunFuzzWorker`
        - `coordinate`
        - `fuzz`
        - `minimize`
        - `minimizeInput`
    - Predicted Functions (0):

- **File:** `src/internal/fuzz/worker_test.go`
    - Ground Truth Functions (1):
        - `BenchmarkWorkerFuzzOverhead`
    - Predicted Functions (0):

- **File:** `src/internal/testenv/testenv.go`
    - Ground Truth Functions (1):
        - `WriteImportcfg`
    - Predicted Functions (0):

- **File:** `src/runtime/crash_test.go`
    - Ground Truth Functions (1):
        - `runBuiltTestProg`
    - Predicted Functions (0):

- **File:** `src/runtime/runtime-gdb_test.go`
    - Ground Truth Functions (1):
        - `TestGdbBacktrace`
    - Predicted Functions (0):


### 📊 **Proposal #51082 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 85.7% | 7.1% | 13.2% | 24/337 |

##### Ground Truth vs Predicted Functions per File

- **File:** `misc/cgo/gmp/gmp.go`
    - Ground Truth Functions (1):
        - `CmpInt`
    - Predicted Functions (0):

- **File:** `src/archive/zip/reader_test.go`
    - Ground Truth Functions (1):
        - `biggestZipBytes`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/asm/parse.go`
    - Ground Truth Functions (1):
        - `symRefAttrs`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/gcc.go`
    - Ground Truth Functions (2):
        - `checkIndex`
        - `splitQuoted`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/importer/gcimporter.go`
    - Ground Truth Functions (1):
        - `Import`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/fmt.go`
    - Ground Truth Functions (2):
        - `Format`
        - `fmtNode`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/block.go`
    - Ground Truth Functions (1):
        - `String`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/compile.go`
    - Ground Truth Functions (1):
        - `PhaseOption`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/debug.go`
    - Ground Truth Functions (1):
        - `PopulateABIInRegArgOps`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/debug_test.go`
    - Ground Truth Functions (1):
        - `TestNexting`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/syntax/parser.go`
    - Ground Truth Functions (1):
        - `list`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/syntax/syntax.go`
    - Ground Truth Functions (1):
        - `Parse`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/test/zerorange_test.go`
    - Ground Truth Functions (1):
        - `TestZerorange45372`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/mkbuiltin.go`
    - Ground Truth Functions (1):
        - `mkbuiltin`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types/fmt.go`
    - Ground Truth Functions (1):
        - `Format`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/api.go`
    - Ground Truth Functions (2):
        - `ObjectOf`
        - `TypeOf`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/builtins.go`
    - Ground Truth Functions (1):
        - `builtin`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/expr.go`
    - Ground Truth Functions (4):
        - `expr`
        - `exprInternal`
        - `exprWithHint`
        - `rawExpr`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/lookup.go`
    - Ground Truth Functions (2):
        - `LookupFieldOrMethod`
        - `MissingMethod`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/operand.go`
    - Ground Truth Functions (2):
        - `Pos`
        - `operandString`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/selection.go`
    - Ground Truth Functions (1):
        - `SelectionString`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/typexpr.go`
    - Ground Truth Functions (3):
        - `definedType`
        - `ident`
        - `typInternal`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/universe.go`
    - Ground Truth Functions (1):
        - `def`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/builtin.go`
    - Ground Truth Functions (1):
        - `walkCopy`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/order.go`
    - Ground Truth Functions (3):
        - `exprInPlace`
        - `exprNoLHS`
        - `orderBlock`
    - Predicted Functions (0):

- **File:** `src/cmd/cover/cover_test.go`
    - Ground Truth Functions (1):
        - `TestCover`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/buildruntime.go`
    - Ground Truth Functions (2):
        - `mkobjabi`
        - `mkzversion`
    - Predicted Functions (0):

- **File:** `src/cmd/doc/pkg.go`
    - Ground Truth Functions (5):
        - `ToText`
        - `emit`
        - `joinStrings`
        - `packageDoc`
        - `printFieldDoc`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cache/cache.go`
    - Ground Truth Functions (1):
        - `Open`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/imports/build.go`
    - Ground Truth Functions (1):
        - `ShouldBuild`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/load.go`
    - Ground Truth Functions (1):
        - `stackText`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/query.go`
    - Ground Truth Functions (1):
        - `allowsVersion`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/riscv/obj.go`
    - Ground Truth Functions (1):
        - `stackOffset`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/x86/asm6.go`
    - Ground Truth Functions (1):
        - `regIndex`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/flag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/funcid.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/head.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/line.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/path.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/reloctype.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/stack.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/symkind.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/symkind_string.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/util.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/elf.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/goobj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/macho.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/pe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/plan9obj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/xcoff.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/dwarf_test.go`
    - Ground Truth Functions (1):
        - `processParams`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/loader/loader.go`
    - Ground Truth Functions (1):
        - `Errorf`
    - Predicted Functions (0):

- **File:** `src/container/ring/ring.go`
    - Ground Truth Functions (4):
        - `Len`
        - `Link`
        - `Move`
        - `Unlink`
    - Predicted Functions (0):

- **File:** `src/debug/dwarf/entry.go`
    - Ground Truth Functions (1):
        - `Val`
    - Predicted Functions (0):

- **File:** `src/debug/gosym/pclntab_test.go`
    - Ground Truth Functions (1):
        - `read115Executable`
    - Predicted Functions (0):

- **File:** `src/encoding/ascii85/ascii85.go`
    - Ground Truth Functions (1):
        - `Decode`
    - Predicted Functions (0):

- **File:** `src/encoding/binary/varint.go`
    - Ground Truth Functions (2):
        - `Uvarint`
        - `Varint`
    - Predicted Functions (0):

- **File:** `src/encoding/json/decode.go`
    - Ground Truth Functions (1):
        - `Unmarshal`
    - Predicted Functions (0):

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (1):
        - `Marshal`
    - Predicted Functions (0):

- **File:** `src/go/ast/ast.go`
    - Ground Truth Functions (2):
        - `End`
        - `String`
    - Predicted Functions (0):

- **File:** `src/go/ast/commentmap.go`
    - Ground Truth Functions (6):
        - `NewCommentMap`
        - `nodeList`
        - `pop`
        - `push`
        - `sortComments`
        - `summary`
    - Predicted Functions (0):

- **File:** `src/go/ast/filter.go`
    - Ground Truth Functions (7):
        - `FileExports`
        - `MergePackageFiles`
        - `PackageExports`
        - `fieldName`
        - `filterFile`
        - `filterPackage`
        - `nameOf`
    - Predicted Functions (0):

- **File:** `src/go/ast/resolve.go`
    - Ground Truth Functions (1):
        - `NewPackage`
    - Predicted Functions (0):

- **File:** `src/go/ast/scope.go`
    - Ground Truth Functions (2):
        - `Insert`
        - `Lookup`
    - Predicted Functions (0):

- **File:** `src/go/ast/walk.go`
    - Ground Truth Functions (2):
        - `Inspect`
        - `Walk`
    - Predicted Functions (0):

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (2):
        - `Import`
        - `splitQuoted`
    - Predicted Functions (0):

- **File:** `src/go/constant/value.go`
    - Ground Truth Functions (7):
        - `BinaryOp`
        - `Compare`
        - `Make`
        - `Shift`
        - `UnaryOp`
        - `Val`
        - `match`
    - Predicted Functions (0):

- **File:** `src/go/doc/comment.go`
    - Ground Truth Functions (2):
        - `ToHTML`
        - `ToText`
    - Predicted Functions (0):

- **File:** `src/go/doc/comment/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `DocLink`
        - ❌ `Format`
        - ❌ `NewComment`
        - ❌ `Parse`

- **File:** `src/go/doc/comment/html.go`
    - Ground Truth Functions (5):
        - `HTML`
        - `block`
        - `escape`
        - `inc`
        - `text`
    - Predicted Functions (0):

- **File:** `src/go/doc/comment/markdown.go`
    - Ground Truth Functions (5):
        - `Markdown`
        - `block`
        - `escape`
        - `rawText`
        - `text`
    - Predicted Functions (5):
        - ✅ `Markdown`
        - ✅ `block`
        - ✅ `escape`
        - ✅ `rawText`
        - ✅ `text`

- **File:** `src/go/doc/comment/parse.go`
    - Ground Truth Functions (33):
        - `BlankBefore`
        - `BlankBetween`
        - `DefaultLookupPackage`
        - `Parse`
        - `autoURL`
        - `code`
        - `commonPrefix`
        - `docLink`
        - `heading`
        - `ident`
        - `indented`
        - `isBlank`
        - `isHeading`
        - `isHost`
        - `isIdentASCII`
        - `isList`
        - `isName`
        - `isOldHeading`
        - `isPath`
        - `isPunct`
        - `isScheme`
        - `isStdPkg`
        - `leadingSpace`
        - `list`
        - `listMarker`
        - `lookupPkg`
        - `oldHeading`
        - `paragraph`
        - `parseLink`
        - `parseLinkedText`
        - `parseText`
        - `splitDocName`
        - `unindent`
    - Predicted Functions (6):
        - ✅ `Parse`
        - ✅ `docLink`
        - ✅ `heading`
        - ✅ `list`
        - ✅ `parseLinkedText`
        - ✅ `parseText`

- **File:** `src/go/doc/comment/print.go`
    - Ground Truth Functions (10):
        - `Comment`
        - `DefaultID`
        - `DefaultURL`
        - `blankBefore`
        - `block`
        - `docLinkURL`
        - `headingID`
        - `headingLevel`
        - `indent`
        - `text`
    - Predicted Functions (6):
        - ✅ `Comment`
        - ✅ `DefaultID`
        - ✅ `DefaultURL`
        - ✅ `docLinkURL`
        - ✅ `headingID`
        - ✅ `headingLevel`

- **File:** `src/go/doc/comment/std_test.go`
    - Ground Truth Functions (1):
        - `TestStd`
    - Predicted Functions (0):

- **File:** `src/go/doc/comment/testdata_test.go`
    - Ground Truth Functions (4):
        - `TestTestdata`
        - `dump`
        - `dumpNL`
        - `dumpTo`
    - Predicted Functions (0):

- **File:** `src/go/doc/comment/text.go`
    - Ground Truth Functions (6):
        - `Text`
        - `block`
        - `oneLongLine`
        - `text`
        - `wrap`
        - `writeNL`
    - Predicted Functions (0):

- **File:** `src/go/doc/comment_test.go`
    - Ground Truth Functions (1):
        - `TestComment`
    - Predicted Functions (0):

- **File:** `src/go/doc/doc.go`
    - Ground Truth Functions (12):
        - `HTML`
        - `Markdown`
        - `New`
        - `NewFromFiles`
        - `Parser`
        - `Printer`
        - `Text`
        - `collectFuncs`
        - `collectTypes`
        - `collectValues`
        - `lookupPackage`
        - `lookupSym`
    - Predicted Functions (7):
        - ✅ `HTML`
        - ✅ `Markdown`
        - ✅ `New`
        - ✅ `NewFromFiles`
        - ✅ `Parser`
        - ✅ `Printer`
        - ✅ `Text`

- **File:** `src/go/doc/doc_test.go`
    - Ground Truth Functions (1):
        - `TestFuncs`
    - Predicted Functions (0):

- **File:** `src/go/doc/example.go`
    - Ground Truth Functions (1):
        - `classifyExamples`
    - Predicted Functions (0):

- **File:** `src/go/doc/exports.go`
    - Ground Truth Functions (7):
        - `copyConstType`
        - `fileExports`
        - `filterFieldList`
        - `filterIdentList`
        - `filterParamList`
        - `filterType`
        - `hasExportedName`
    - Predicted Functions (0):

- **File:** `src/go/doc/filter.go`
    - Ground Truth Functions (1):
        - `Filter`
    - Predicted Functions (0):

- **File:** `src/go/doc/reader.go`
    - Ground Truth Functions (20):
        - `add`
        - `assumedPackageName`
        - `baseTypeName`
        - `clean`
        - `cleanupTypes`
        - `collectEmbeddedMethods`
        - `computeMethodSets`
        - `fields`
        - `lookupType`
        - `readFile`
        - `readFunc`
        - `readNote`
        - `readNotes`
        - `readPackage`
        - `readType`
        - `readValue`
        - `recordAnonymousField`
        - `recvString`
        - `set`
        - `sortedValues`
    - Predicted Functions (0):

- **File:** `src/go/doc/synopsis.go`
    - Ground Truth Functions (2):
        - `Synopsis`
        - `firstSentence`
    - Predicted Functions (0):

- **File:** `src/go/doc/synopsis_test.go`
    - Ground Truth Functions (1):
        - `TestSynopsis`
    - Predicted Functions (0):

- **File:** `src/go/format/benchmark_test.go`
    - Ground Truth Functions (1):
        - `array1`
    - Predicted Functions (0):

- **File:** `src/go/format/format.go`
    - Ground Truth Functions (2):
        - `Node`
        - `Source`
    - Predicted Functions (0):

- **File:** `src/go/internal/gccgoimporter/parser.go`
    - Ground Truth Functions (2):
        - `getPkg`
        - `parseType`
    - Predicted Functions (0):

- **File:** `src/go/internal/gcimporter/gcimporter.go`
    - Ground Truth Functions (1):
        - `Import`
    - Predicted Functions (0):

- **File:** `src/go/parser/error_test.go`
    - Ground Truth Functions (2):
        - `compareErrors`
        - `expectedErrors`
    - Predicted Functions (0):

- **File:** `src/go/parser/interface.go`
    - Ground Truth Functions (4):
        - `ParseDir`
        - `ParseExprFrom`
        - `ParseFile`
        - `readSource`
    - Predicted Functions (0):

- **File:** `src/go/parser/parser.go`
    - Ground Truth Functions (5):
        - `consumeCommentGroup`
        - `expectClosing`
        - `next`
        - `parseOperand`
        - `safePos`
    - Predicted Functions (0):

- **File:** `src/go/parser/resolver.go`
    - Ground Truth Functions (1):
        - `resolve`
    - Predicted Functions (0):

- **File:** `src/go/printer/comment.go`
    - Ground Truth Functions (3):
        - `allStars`
        - `formatDocComment`
        - `isDirective`
    - Predicted Functions (0):

- **File:** `src/go/printer/nodes.go`
    - Ground Truth Functions (7):
        - `binaryExpr`
        - `funcBody`
        - `indentList`
        - `keepTypeColumn`
        - `linebreak`
        - `nodeSize`
        - `spec`
    - Predicted Functions (0):

- **File:** `src/go/printer/printer.go`
    - Ground Truth Functions (9):
        - `commentBefore`
        - `commentSizeBefore`
        - `intersperseComments`
        - `isBlank`
        - `print`
        - `stripCommonPrefix`
        - `writeCommentPrefix`
        - `writeCommentSuffix`
        - `writeString`
    - Predicted Functions (0):

- **File:** `src/go/printer/printer_test.go`
    - Ground Truth Functions (2):
        - `TestLineComments`
        - `checkEqual`
    - Predicted Functions (0):

- **File:** `src/go/printer/testdata/parser.go`
    - Ground Truth Functions (4):
        - `checkExprOrType`
        - `consumeCommentGroup`
        - `next`
        - `parseOperand`
    - Predicted Functions (0):

- **File:** `src/go/scanner/errors.go`
    - Ground Truth Functions (1):
        - `PrintError`
    - Predicted Functions (0):

- **File:** `src/go/scanner/scanner.go`
    - Ground Truth Functions (2):
        - `Init`
        - `Scan`
    - Predicted Functions (0):

- **File:** `src/go/token/position.go`
    - Ground Truth Functions (11):
        - `AddFile`
        - `AddLine`
        - `Base`
        - `IsValid`
        - `MergeLine`
        - `Offset`
        - `SetLines`
        - `String`
        - `file`
        - `searchInts`
        - `unpack`
    - Predicted Functions (0):

- **File:** `src/go/token/token.go`
    - Ground Truth Functions (6):
        - `IsIdentifier`
        - `IsKeyword`
        - `IsOperator`
        - `Lookup`
        - `Precedence`
        - `String`
    - Predicted Functions (0):

- **File:** `src/go/types/api.go`
    - Ground Truth Functions (2):
        - `ObjectOf`
        - `TypeOf`
    - Predicted Functions (0):

- **File:** `src/go/types/builtins.go`
    - Ground Truth Functions (1):
        - `builtin`
    - Predicted Functions (0):

- **File:** `src/go/types/eval.go`
    - Ground Truth Functions (1):
        - `CheckExpr`
    - Predicted Functions (0):

- **File:** `src/go/types/expr.go`
    - Ground Truth Functions (4):
        - `expr`
        - `exprInternal`
        - `exprWithHint`
        - `rawExpr`
    - Predicted Functions (0):

- **File:** `src/go/types/lookup.go`
    - Ground Truth Functions (2):
        - `LookupFieldOrMethod`
        - `MissingMethod`
    - Predicted Functions (0):

- **File:** `src/go/types/operand.go`
    - Ground Truth Functions (2):
        - `Pos`
        - `operandString`
    - Predicted Functions (0):

- **File:** `src/go/types/selection.go`
    - Ground Truth Functions (1):
        - `SelectionString`
    - Predicted Functions (0):

- **File:** `src/go/types/typexpr.go`
    - Ground Truth Functions (3):
        - `definedType`
        - `ident`
        - `typInternal`
    - Predicted Functions (0):

- **File:** `src/go/types/universe.go`
    - Ground Truth Functions (1):
        - `def`
    - Predicted Functions (0):

- **File:** `src/html/template/template.go`
    - Ground Truth Functions (1):
        - `Option`
    - Predicted Functions (0):

- **File:** `src/index/suffixarray/suffixarray.go`
    - Ground Truth Functions (3):
        - `Bytes`
        - `FindAllIndex`
        - `Lookup`
    - Predicted Functions (0):

- **File:** `src/internal/fmtsort/sort.go`
    - Ground Truth Functions (1):
        - `Sort`
    - Predicted Functions (0):

- **File:** `src/math/big/float.go`
    - Ground Truth Functions (3):
        - `Cmp`
        - `Sign`
        - `ord`
    - Predicted Functions (0):

- **File:** `src/math/big/floatconv.go`
    - Ground Truth Functions (1):
        - `Parse`
    - Predicted Functions (0):

- **File:** `src/math/big/int.go`
    - Ground Truth Functions (6):
        - `Cmp`
        - `DivMod`
        - `Jacobi`
        - `QuoRem`
        - `Sign`
        - `modSqrt3Mod4Prime`
    - Predicted Functions (0):

- **File:** `src/math/big/intconv.go`
    - Ground Truth Functions (2):
        - `Format`
        - `scan`
    - Predicted Functions (0):

- **File:** `src/math/big/natconv.go`
    - Ground Truth Functions (2):
        - `convertWords`
        - `scan`
    - Predicted Functions (0):

- **File:** `src/math/big/rat.go`
    - Ground Truth Functions (2):
        - `Cmp`
        - `Sign`
    - Predicted Functions (0):

- **File:** `src/math/rand/exp.go`
    - Ground Truth Functions (1):
        - `ExpFloat64`
    - Predicted Functions (0):

- **File:** `src/math/rand/normal.go`
    - Ground Truth Functions (1):
        - `NormFloat64`
    - Predicted Functions (0):

- **File:** `src/net/http/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/fs.go`
    - Ground Truth Functions (1):
        - `FileServer`
    - Predicted Functions (0):

- **File:** `src/net/textproto/reader.go`
    - Ground Truth Functions (4):
        - `ReadCodeLine`
        - `ReadContinuedLine`
        - `ReadMIMEHeader`
        - `ReadResponse`
    - Predicted Functions (0):

- **File:** `src/net/textproto/textproto.go`
    - Ground Truth Functions (1):
        - `Cmd`
    - Predicted Functions (0):

- **File:** `src/path/filepath/match.go`
    - Ground Truth Functions (1):
        - `Match`
    - Predicted Functions (0):

- **File:** `src/path/match.go`
    - Ground Truth Functions (1):
        - `Match`
    - Predicted Functions (0):

- **File:** `src/reflect/makefunc.go`
    - Ground Truth Functions (1):
        - `MakeFunc`
    - Predicted Functions (0):

- **File:** `src/regexp/exec_test.go`
    - Ground Truth Functions (1):
        - `TestRE2Search`
    - Predicted Functions (0):

- **File:** `src/regexp/syntax/parse.go`
    - Ground Truth Functions (1):
        - `factor`
    - Predicted Functions (0):

- **File:** `src/runtime/chan.go`
    - Ground Truth Functions (2):
        - `selectnbrecv`
        - `selectnbsend`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/pprof.go`
    - Ground Truth Functions (1):
        - `Add`
    - Predicted Functions (0):

- **File:** `src/runtime/trace/annotation.go`
    - Ground Truth Functions (1):
        - `StartRegion`
    - Predicted Functions (0):

- **File:** `src/sort/search.go`
    - Ground Truth Functions (2):
        - `Search`
        - `SearchInts`
    - Predicted Functions (0):

- **File:** `src/sort/search_test.go`
    - Ground Truth Functions (1):
        - `log2`
    - Predicted Functions (0):

- **File:** `src/strconv/itoa.go`
    - Ground Truth Functions (1):
        - `formatBits`
    - Predicted Functions (0):

- **File:** `src/sync/cond.go`
    - Ground Truth Functions (1):
        - `Wait`
    - Predicted Functions (0):

- **File:** `src/sync/once.go`
    - Ground Truth Functions (1):
        - `Do`
    - Predicted Functions (0):

- **File:** `src/testing/fstest/testfs.go`
    - Ground Truth Functions (1):
        - `TestFS`
    - Predicted Functions (0):

- **File:** `src/text/tabwriter/tabwriter.go`
    - Ground Truth Functions (5):
        - `Init`
        - `Write`
        - `endEscape`
        - `format`
        - `startEscape`
    - Predicted Functions (0):

- **File:** `src/text/template/option.go`
    - Ground Truth Functions (1):
        - `Option`
    - Predicted Functions (0):

- **File:** `src/unicode/letter.go`
    - Ground Truth Functions (1):
        - `SimpleFold`
    - Predicted Functions (0):


### 📊 **Proposal #41260 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 66.7% | 28.6% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/os/env_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestClearenv`
        - ❌ `TestLookupEnv`
        - ❌ `TestUnsetenv`

- **File:** `src/os/exec_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (2):
        - `Parallel`
        - `Setenv`
    - Predicted Functions (2):
        - ❌ `Cleanup`
        - ✅ `Setenv`

- **File:** `src/testing/testing_test.go`
    - Ground Truth Functions (1):
        - `TestSetenv`
    - Predicted Functions (6):
        - ✅ `TestSetenv`
        - ❌ `TestSetenvWithParallelAfter`
        - ❌ `TestSetenvWithParallelBefore`
        - ❌ `TestSetenvWithParallelGrandParentBefore`
        - ❌ `TestSetenvWithParallelParentBefore`
        - ❌ `tSetenv`


### 📊 **Proposal #39057 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/log/log.go`
    - Ground Truth Functions (0):
    - Predicted Functions (17):
        - ❌ `Default`
        - ❌ `Fatal`
        - ❌ `Fatalf`
        - ❌ `Fatalln`
        - ❌ `Flags`
        - ❌ `Output`
        - ❌ `Panic`
        - ❌ `Panicf`
        - ❌ `Panicln`
        - ❌ `Prefix`
        - ❌ `Print`
        - ❌ `Printf`
        - ❌ `Println`
        - ❌ `SetFlags`
        - ❌ `SetOutput`
        - ❌ `SetPrefix`
        - ❌ `Writer`

- **File:** `src/log/log_test.go`
    - Ground Truth Functions (1):
        - `TestDefault`
    - Predicted Functions (0):


### 📊 **Proposal #44167 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 56.2% | 12.0% | 19.8% | 9/75 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/export_test.go`
    - Ground Truth Functions (8):
        - `AssistWorkPerByte`
        - `EndCycle`
        - `HeapGoal`
        - `HeapLive`
        - `HeapMarked`
        - `NewGCController`
        - `Revise`
        - `StartCycle`
    - Predicted Functions (0):

- **File:** `src/runtime/mcache.go`
    - Ground Truth Functions (4):
        - `allocLarge`
        - `prepareForSweep`
        - `refill`
        - `releaseAll`
    - Predicted Functions (0):

- **File:** `src/runtime/metrics.go`
    - Ground Truth Functions (1):
        - `compute`
    - Predicted Functions (0):

- **File:** `src/runtime/mgc.go`
    - Ground Truth Functions (12):
        - `GC`
        - `gcBgMarkWorker`
        - `gcMark`
        - `gcMarkDone`
        - `gcMarkTermination`
        - `gcResetMarkState`
        - `gcStart`
        - `gcSweep`
        - `gcWaitOnMark`
        - `gcinit`
        - `setGCPhase`
        - `test`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcmark.go`
    - Ground Truth Functions (9):
        - `gcDrain`
        - `gcDrainN`
        - `gcDumpObject`
        - `gcFlushBgCredit`
        - `gcmarknewobject`
        - `markroot`
        - `markrootBlock`
        - `scanobject`
        - `scanstack`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcpacer.go`
    - Ground Truth Functions (12):
        - `addGlobals`
        - `addScannableStack`
        - `commit`
        - `endCycle`
        - `enlistWorker`
        - `findRunnableGCWorker`
        - `init`
        - `resetLive`
        - `revise`
        - `setGCPercent`
        - `startCycle`
        - `update`
    - Predicted Functions (11):
        - ✅ `addGlobals`
        - ✅ `addScannableStack`
        - ✅ `endCycle`
        - ❌ `heapGoal`
        - ✅ `init`
        - ❌ `memoryLimitHeapGoal`
        - ✅ `revise`
        - ✅ `setGCPercent`
        - ❌ `setMemoryLimit`
        - ✅ `startCycle`
        - ❌ `trigger`

- **File:** `src/runtime/mgcpacer_test.go`
    - Ground Truth Functions (20):
        - `String`
        - `TestGcPacer`
        - `assertInEpsilon`
        - `assertInRange`
        - `check`
        - `constant`
        - `delay`
        - `goalRatio`
        - `limit`
        - `max`
        - `min`
        - `next`
        - `offset`
        - `oscillate`
        - `quantize`
        - `ramp`
        - `random`
        - `scale`
        - `sum`
        - `unit`
    - Predicted Functions (5):
        - ✅ `TestGcPacer`
        - ❌ `TestIdleMarkWorkerCount`
        - ✅ `goalRatio`
        - ❌ `runway`
        - ❌ `triggerRatio`

- **File:** `src/runtime/mgcscavenge.go`
    - Ground Truth Functions (1):
        - `gcPaceScavenger`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcsweep.go`
    - Ground Truth Functions (2):
        - `deductSweepCredit`
        - `gcPaceSweeper`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcwork.go`
    - Ground Truth Functions (1):
        - `dispose`
    - Predicted Functions (0):

- **File:** `src/runtime/mstats.go`
    - Ground Truth Functions (1):
        - `readmemstats_m`
    - Predicted Functions (0):

- **File:** `src/runtime/proc.go`
    - Ground Truth Functions (2):
        - `goexit0`
        - `newproc1`
    - Predicted Functions (0):

- **File:** `src/runtime/stack.go`
    - Ground Truth Functions (1):
        - `copystack`
    - Predicted Functions (0):

- **File:** `src/runtime/symtab.go`
    - Ground Truth Functions (1):
        - `modulesinit`
    - Predicted Functions (0):


### 📊 **Proposal #46336 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.6% | 0.5% | 0.9% | 1/198 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/strconv.go`
    - Ground Truth Functions (4):
        - `hasNUL`
        - `parsePAXRecord`
        - `parsePAXTime`
        - `validPAXRecord`
    - Predicted Functions (0):

- **File:** `src/archive/tar/writer_test.go`
    - Ground Truth Functions (1):
        - `TestIssue12594`
    - Predicted Functions (0):

- **File:** `src/bytes/bytes.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Cut`
        - ❌ `CutPrefix`
        - ❌ `CutSuffix`
        - ❌ `Index`
        - ❌ `IndexByte`
        - ❌ `IndexRune`
        - ❌ `SplitN`

- **File:** `src/cmd/asm/internal/asm/operand_test.go`
    - Ground Truth Functions (1):
        - `TestFuncAddress`
    - Predicted Functions (0):

- **File:** `src/cmd/asm/internal/lex/input.go`
    - Ground Truth Functions (1):
        - `predefine`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/gcc.go`
    - Ground Truth Functions (3):
        - `badCFType`
        - `guessKinds`
        - `loadDefines`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/godefs.go`
    - Ground Truth Functions (1):
        - `godefs`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/out.go`
    - Ground Truth Functions (1):
        - `checkImportSymName`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/base/flag.go`
    - Ground Truth Functions (1):
        - `readImportCfg`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/liveness/plive.go`
    - Ground Truth Functions (1):
        - `showlive`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/logopt/log_opts.go`
    - Ground Truth Functions (1):
        - `parseLogFlag`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/noder.go`
    - Ground Truth Functions (2):
        - `parseGoEmbed`
        - `pragma`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/debug_test.go`
    - Ground Truth Functions (5):
        - `canonFileName`
        - `printVariableAndNormalize`
        - `quit`
        - `read`
        - `varsToPrint`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/html.go`
    - Ground Truth Functions (1):
        - `WriteAST`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (2):
        - `shouldbuild`
        - `timelog`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/imports.go`
    - Ground Truth Functions (1):
        - `resolveVendor`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `flattenCmdline`
    - Predicted Functions (0):

- **File:** `src/cmd/doc/dirs.go`
    - Ground Truth Functions (1):
        - `findCodeRoots`
    - Predicted Functions (0):

- **File:** `src/cmd/doc/pkg.go`
    - Ground Truth Functions (1):
        - `oneLineNodeDepth`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/typecheck.go`
    - Ground Truth Functions (1):
        - `typecheck1`
    - Predicted Functions (0):

- **File:** `src/cmd/go/go_test.go`
    - Ground Truth Functions (2):
        - `isStale`
        - `parallel`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/base/base.go`
    - Ground Truth Functions (1):
        - `LongName`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/base/goflags.go`
    - Ground Truth Functions (3):
        - `InGOFLAGS`
        - `InitGOFLAGS`
        - `SetFromGOFLAGS`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cache/hash.go`
    - Ground Truth Functions (1):
        - `stripExperiment`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cmdflag/flag.go`
    - Ground Truth Functions (1):
        - `ParseOne`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/envcmd/env.go`
    - Ground Truth Functions (4):
        - `PrintEnv`
        - `argKey`
        - `lineToKey`
        - `runEnv`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/imports/build.go`
    - Ground Truth Functions (1):
        - `MatchFile`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/imports/read_test.go`
    - Ground Truth Functions (1):
        - `testRead`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/flag.go`
    - Ground Truth Functions (1):
        - `set`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/pkg.go`
    - Ground Truth Functions (1):
        - `PackagesAndErrorsOutsideModule`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/edit.go`
    - Ground Truth Functions (4):
        - `flagReplace`
        - `parsePathVersion`
        - `parsePathVersionOptional`
        - `parseVersionInterval`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/vcs.go`
    - Ground Truth Functions (1):
        - `bzrParseStat`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modget/query.go`
    - Ground Truth Functions (1):
        - `newQuery`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/build.go`
    - Ground Truth Functions (1):
        - `ModuleInfo`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/init.go`
    - Ground Truth Functions (1):
        - `fixVersion`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/list.go`
    - Ground Truth Functions (1):
        - `listModules`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/modfile.go`
    - Ground Truth Functions (1):
        - `ShortMessage`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/query.go`
    - Ground Truth Functions (1):
        - `QueryPattern`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/mvs/mvs_test.go`
    - Ground Truth Functions (1):
        - `Test`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/search/search.go`
    - Ground Truth Functions (4):
        - `CleanPatterns`
        - `IsRelativePath`
        - `IsStandardImportPath`
        - `MatchDirs`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/test/test.go`
    - Ground Truth Functions (2):
        - `computeTestInputsID`
        - `tryCacheWithID`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vcs/vcs.go`
    - Ground Truth Functions (3):
        - `bzrResolveRepo`
        - `parseGOVCS`
        - `svnRemoteRepo`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vet/vetflag.go`
    - Ground Truth Functions (1):
        - `parseVettoolFlag`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (1):
        - `installOutsideModule`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/buildid.go`
    - Ground Truth Functions (2):
        - `actionID`
        - `contentID`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/gccgo.go`
    - Ground Truth Functions (1):
        - `buildImportcfgSymlinks`
    - Predicted Functions (0):

- **File:** `src/cmd/go/proxy_test.go`
    - Ground Truth Functions (1):
        - `proxyHandler`
    - Predicted Functions (0):

- **File:** `src/cmd/go/testdata/addmod.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/gofmt/gofmt_test.go`
    - Ground Truth Functions (1):
        - `runTest`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/stringer.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/test2json/test2json.go`
    - Ground Truth Functions (1):
        - `handleInputLine`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/data.go`
    - Ground Truth Functions (1):
        - `addstrdata1`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/dwarf.go`
    - Ground Truth Functions (1):
        - `writeDirFileTables`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/go.go`
    - Ground Truth Functions (3):
        - `ldpkg`
        - `loadcgo`
        - `setCgoAttr`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/ld.go`
    - Ground Truth Functions (1):
        - `readImportCfg`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/main.go`
    - Ground Truth Functions (1):
        - `Main`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/pe.go`
    - Ground Truth Functions (1):
        - `initdynimport`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/github.com/google/pprof/internal/binutils/addr2liner.go`
    - Ground Truth Functions (1):
        - `readFrame`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/github.com/google/pprof/internal/binutils/binutils.go`
    - Ground Truth Functions (1):
        - `initTools`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/github.com/google/pprof/internal/driver/commands.go`
    - Ground Truth Functions (1):
        - `usage`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/github.com/google/pprof/internal/driver/driver_focus.go`
    - Ground Truth Functions (1):
        - `compileTagFilter`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/github.com/google/pprof/internal/driver/interactive.go`
    - Ground Truth Functions (1):
        - `interactive`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/github.com/google/pprof/internal/report/source.go`
    - Ground Truth Functions (1):
        - `trimPath`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/github.com/google/pprof/profile/legacy_profile.go`
    - Ground Truth Functions (2):
        - `parseContention`
        - `parseProcMapsFromScanner`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/arch/ppc64/ppc64asm/plan9.go`
    - Ground Truth Functions (1):
        - `GoSyntax`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/mod/modfile/rule.go`
    - Ground Truth Functions (1):
        - `setIndirect`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/mod/module/module.go`
    - Ground Truth Functions (3):
        - `CheckPath`
        - `MatchPrefixPatterns`
        - `checkElem`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/mod/sumdb/note/note.go`
    - Ground Truth Functions (3):
        - `NewSigner`
        - `NewVerifier`
        - `Open`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/mod/sumdb/server.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/plan9/syscall.go`
    - Ground Truth Functions (1):
        - `ByteSliceFromString`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall.go`
    - Ground Truth Functions (1):
        - `ByteSliceFromString`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/xattr_bsd.go`
    - Ground Truth Functions (1):
        - `xattrnamespace`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/windows/syscall.go`
    - Ground Truth Functions (1):
        - `ByteSliceFromString`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/asmdecl/asmdecl.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/buildtag/buildtag.go`
    - Ground Truth Functions (3):
        - `file`
        - `goBuildLine`
        - `plusBuildLine`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/framepointer/framepointer.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
    - Ground Truth Functions (2):
        - `checkTagDuplicates`
        - `validateStructTag`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (1):
        - `errorCheck`
    - Predicted Functions (0):

- **File:** `src/crypto/ecdsa/ecdsa_test.go`
    - Ground Truth Functions (1):
        - `TestVectors`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_test.go`
    - Ground Truth Functions (1):
        - `parseTestData`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/pem_decrypt.go`
    - Ground Truth Functions (1):
        - `DecryptPEMBlock`
    - Predicted Functions (0):

- **File:** `src/encoding/asn1/common.go`
    - Ground Truth Functions (1):
        - `parseFieldParameters`
    - Predicted Functions (0):

- **File:** `src/encoding/json/tags.go`
    - Ground Truth Functions (2):
        - `Contains`
        - `parseTag`
    - Predicted Functions (0):

- **File:** `src/encoding/xml/typeinfo.go`
    - Ground Truth Functions (1):
        - `structFieldInfo`
    - Predicted Functions (0):

- **File:** `src/encoding/xml/xml.go`
    - Ground Truth Functions (2):
        - `nsname`
        - `procInst`
    - Predicted Functions (0):

- **File:** `src/fmt/fmt_test.go`
    - Ground Truth Functions (1):
        - `presentInMap`
    - Predicted Functions (0):

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (2):
        - `goodOSArchFile`
        - `saveCgo`
    - Predicted Functions (0):

- **File:** `src/go/build/build_test.go`
    - Ground Truth Functions (1):
        - `TestMissingImportErrorRepetition`
    - Predicted Functions (0):

- **File:** `src/go/build/read.go`
    - Ground Truth Functions (1):
        - `parseGoEmbed`
    - Predicted Functions (0):

- **File:** `src/go/build/read_test.go`
    - Ground Truth Functions (1):
        - `testRead`
    - Predicted Functions (0):

- **File:** `src/go/constant/value_test.go`
    - Ground Truth Functions (2):
        - `testNumbers`
        - `val`
    - Predicted Functions (0):

- **File:** `src/go/doc/headscan.go`
    - Ground Truth Functions (2):
        - `appendHeadings`
        - `main`
    - Predicted Functions (0):

- **File:** `src/go/importer/importer_test.go`
    - Ground Truth Functions (1):
        - `TestForCompiler`
    - Predicted Functions (0):

- **File:** `src/go/printer/nodes.go`
    - Ground Truth Functions (1):
        - `normalizedNumber`
    - Predicted Functions (0):

- **File:** `src/go/printer/printer.go`
    - Ground Truth Functions (1):
        - `stripCommonPrefix`
    - Predicted Functions (0):

- **File:** `src/go/types/eval_test.go`
    - Ground Truth Functions (1):
        - `split`
    - Predicted Functions (0):

- **File:** `src/html/template/attr.go`
    - Ground Truth Functions (1):
        - `attrType`
    - Predicted Functions (0):

- **File:** `src/html/template/js.go`
    - Ground Truth Functions (1):
        - `isJSType`
    - Predicted Functions (0):

- **File:** `src/html/template/url.go`
    - Ground Truth Functions (1):
        - `isSafeURL`
    - Predicted Functions (0):

- **File:** `src/internal/goroot/gc.go`
    - Ground Truth Functions (1):
        - `isStandard`
    - Predicted Functions (0):

- **File:** `src/math/big/ratconv.go`
    - Ground Truth Functions (1):
        - `SetString`
    - Predicted Functions (0):

- **File:** `src/mime/encodedword.go`
    - Ground Truth Functions (4):
        - `Decode`
        - `DecodeHeader`
        - `convert`
        - `decode`
    - Predicted Functions (0):

- **File:** `src/mime/mediatype.go`
    - Ground Truth Functions (2):
        - `FormatMediaType`
        - `ParseMediaType`
    - Predicted Functions (0):

- **File:** `src/net/http/cgi/child.go`
    - Ground Truth Functions (1):
        - `envMap`
    - Predicted Functions (0):

- **File:** `src/net/http/cgi/host.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (0):

- **File:** `src/net/http/cgi/host_test.go`
    - Ground Truth Functions (1):
        - `runResponseChecks`
    - Predicted Functions (0):

- **File:** `src/net/http/client_test.go`
    - Ground Truth Functions (1):
        - `removeCommonLines`
    - Predicted Functions (0):

- **File:** `src/net/http/cookie.go`
    - Ground Truth Functions (3):
        - `readCookies`
        - `readSetCookies`
        - `sanitizeCookieValue`
    - Predicted Functions (0):

- **File:** `src/net/http/fs.go`
    - Ground Truth Functions (1):
        - `parseRange`
    - Predicted Functions (0):

- **File:** `src/net/http/main_test.go`
    - Ground Truth Functions (1):
        - `interestingGoroutines`
    - Predicted Functions (0):

- **File:** `src/net/http/request.go`
    - Ground Truth Functions (3):
        - `ParseHTTPVersion`
        - `parseBasicAuth`
        - `parseRequestLine`
    - Predicted Functions (0):

- **File:** `src/net/http/response.go`
    - Ground Truth Functions (1):
        - `ReadResponse`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (1):
        - `stripHostPort`
    - Predicted Functions (0):

- **File:** `src/net/http/transport.go`
    - Ground Truth Functions (1):
        - `dialConn`
    - Predicted Functions (0):

- **File:** `src/net/mail/message.go`
    - Ground Truth Functions (1):
        - `ParseDate`
    - Predicted Functions (0):

- **File:** `src/net/main_test.go`
    - Ground Truth Functions (1):
        - `runningGoroutines`
    - Predicted Functions (0):

- **File:** `src/net/smtp/smtp.go`
    - Ground Truth Functions (1):
        - `ehlo`
    - Predicted Functions (0):

- **File:** `src/net/url/url.go`
    - Ground Truth Functions (7):
        - `Parse`
        - `String`
        - `parse`
        - `parseAuthority`
        - `parseHost`
        - `parseQuery`
        - `resolvePath`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (2):
        - `addCriticalEnv`
        - `dedupEnvCase`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (1):
        - `TestCatGoodAndBadFile`
    - Predicted Functions (0):

- **File:** `src/os/os_test.go`
    - Ground Truth Functions (1):
        - `TestHostname`
    - Predicted Functions (0):

- **File:** `src/os/user/cgo_lookup_unix.go`
    - Ground Truth Functions (1):
        - `buildUser`
    - Predicted Functions (0):

- **File:** `src/os/user/lookup_unix.go`
    - Ground Truth Functions (1):
        - `matchUserIndexValue`
    - Predicted Functions (0):

- **File:** `src/regexp/exec_test.go`
    - Ground Truth Functions (2):
        - `parseResult`
        - `testFowler`
    - Predicted Functions (0):

- **File:** `src/regexp/syntax/parse.go`
    - Ground Truth Functions (3):
        - `Parse`
        - `parsePerlFlags`
        - `parseUnicodeClass`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/pprof_test.go`
    - Ground Truth Functions (2):
        - `containsInOrder`
        - `stackContainsLabeled`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/proto_test.go`
    - Ground Truth Functions (1):
        - `TestProcSelfMaps`
    - Predicted Functions (0):

- **File:** `src/strconv/fp_test.go`
    - Ground Truth Functions (2):
        - `myatof32`
        - `myatof64`
    - Predicted Functions (0):

- **File:** `src/strings/builder.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strings/compare.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strings/iter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Index`
        - ❌ `IndexByte`
        - ❌ `IndexRune`
        - ❌ `LastIndex`
        - ❌ `LastIndexByte`
        - ❌ `SplitN`

- **File:** `src/strings/replace.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strings/strings.go`
    - Ground Truth Functions (1):
        - `Cut`
    - Predicted Functions (5):
        - ✅ `Cut`
        - ❌ `Index`
        - ❌ `IndexByte`
        - ❌ `IndexRune`
        - ❌ `SplitN`

- **File:** `src/testing/fstest/mapfs.go`
    - Ground Truth Functions (1):
        - `Open`
    - Predicted Functions (0):

- **File:** `src/testing/fstest/testfs.go`
    - Ground Truth Functions (1):
        - `checkBadPath`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/net/http/httpguts/httplex.go`
    - Ground Truth Functions (1):
        - `headerValueContainsToken`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/net/idna/idna10.0.0.go`
    - Ground Truth Functions (2):
        - `label`
        - `validateLabel`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/net/idna/idna9.0.0.go`
    - Ground Truth Functions (2):
        - `label`
        - `validateLabel`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu.go`
    - Ground Truth Functions (1):
        - `processOptions`
    - Predicted Functions (0):


### 📊 **Proposal #46742 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/10 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/typecheck/builtin.go`
    - Ground Truth Functions (1):
        - `runtimeTypes`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/func.go`
    - Ground Truth Functions (1):
        - `tcUnsafeSlice`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/builtin.go`
    - Ground Truth Functions (1):
        - `walkUnsafeSlice`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/flag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/elf.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/goobj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/macho.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/objfile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/pe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/plan9obj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/xcoff.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/checkptr.go`
    - Ground Truth Functions (2):
        - `checkptrAlignment`
        - `checkptrStraddles`
    - Predicted Functions (0):

- **File:** `src/runtime/checkptr_test.go`
    - Ground Truth Functions (1):
        - `TestCheckPtr`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprog/checkptr.go`
    - Ground Truth Functions (3):
        - `CheckPtrSliceFail`
        - `CheckPtrSliceOK`
        - `init`
    - Predicted Functions (0):

- **File:** `src/runtime/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `panicunsafeslicelen`
        - ❌ `panicunsafeslicenilptr`
        - ❌ `unsafeslice`

- **File:** `src/unsafe/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Slice`

- **File:** `test/unsafebuiltins.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #50860 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.8% | 16.9% | 19.4% | 13/77 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/escape/utils.go`
    - Ground Truth Functions (1):
        - `HeapAllocReason`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/test/inl_test.go`
    - Ground Truth Functions (1):
        - `TestIntendedInlining`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types/size.go`
    - Ground Truth Functions (1):
        - `calcStructOffset`
    - Predicted Functions (0):

- **File:** `src/sync/atomic/atomic_test.go`
    - Ground Truth Functions (72):
        - `TestAddInt32Method`
        - `TestAddInt64`
        - `TestAddInt64Method`
        - `TestAddUint32`
        - `TestAddUint32Method`
        - `TestAddUint64`
        - `TestAddUint64Method`
        - `TestAddUintptrMethod`
        - `TestAutoAligned64`
        - `TestCompareAndSwapInt32`
        - `TestCompareAndSwapInt32Method`
        - `TestCompareAndSwapInt64`
        - `TestCompareAndSwapInt64Method`
        - `TestCompareAndSwapPointerMethod`
        - `TestCompareAndSwapUint32Method`
        - `TestCompareAndSwapUint64Method`
        - `TestCompareAndSwapUintptrMethod`
        - `TestHammerStoreLoad`
        - `TestLoadInt32Method`
        - `TestLoadInt64`
        - `TestLoadInt64Method`
        - `TestLoadPointer`
        - `TestLoadPointerMethod`
        - `TestLoadUint32Method`
        - `TestLoadUint64`
        - `TestLoadUint64Method`
        - `TestLoadUintptrMethod`
        - `TestNilDeref`
        - `TestStoreInt32Method`
        - `TestStoreInt64`
        - `TestStoreInt64Method`
        - `TestStorePointerMethod`
        - `TestStoreUint32Method`
        - `TestStoreUint64`
        - `TestStoreUint64Method`
        - `TestStoreUintptrMethod`
        - `TestSwapInt32Method`
        - `TestSwapInt64`
        - `TestSwapInt64Method`
        - `TestSwapPointerMethod`
        - `TestSwapUint32Method`
        - `TestSwapUint64`
        - `TestSwapUint64Method`
        - `TestSwapUintptrMethod`
        - `TestUnaligned64`
        - `hammerAddInt32Method`
        - `hammerAddInt64Method`
        - `hammerAddUint32Method`
        - `hammerAddUint64Method`
        - `hammerAddUintptr32Method`
        - `hammerAddUintptr64Method`
        - `hammerCompareAndSwapInt32Method`
        - `hammerCompareAndSwapInt64Method`
        - `hammerCompareAndSwapUint32Method`
        - `hammerCompareAndSwapUint64Method`
        - `hammerCompareAndSwapUintptr32Method`
        - `hammerCompareAndSwapUintptr64Method`
        - `hammerStoreLoadInt32Method`
        - `hammerStoreLoadInt64Method`
        - `hammerStoreLoadPointerMethod`
        - `hammerStoreLoadUint32Method`
        - `hammerStoreLoadUint64Method`
        - `hammerStoreLoadUintptrMethod`
        - `hammerSwapInt32Method`
        - `hammerSwapInt64Method`
        - `hammerSwapUint32Method`
        - `hammerSwapUint64Method`
        - `hammerSwapUintptr32Method`
        - `hammerSwapUintptr64Method`
        - `init`
        - `testCompareAndSwapUint64`
        - `testPointers`
    - Predicted Functions (29):
        - ❌ `TestAddInt32`
        - ✅ `TestAddInt64`
        - ✅ `TestAddUint32`
        - ✅ `TestAddUint64`
        - ❌ `TestAddUintptr`
        - ✅ `TestCompareAndSwapInt32`
        - ✅ `TestCompareAndSwapInt64`
        - ❌ `TestCompareAndSwapPointer`
        - ❌ `TestCompareAndSwapUint32`
        - ❌ `TestCompareAndSwapUint64`
        - ❌ `TestCompareAndSwapUintptr`
        - ❌ `TestLoadInt32`
        - ✅ `TestLoadInt64`
        - ✅ `TestLoadPointer`
        - ❌ `TestLoadUint32`
        - ✅ `TestLoadUint64`
        - ❌ `TestLoadUintptr`
        - ❌ `TestStoreInt32`
        - ✅ `TestStoreInt64`
        - ❌ `TestStorePointer`
        - ❌ `TestStoreUint32`
        - ✅ `TestStoreUint64`
        - ❌ `TestStoreUintptr`
        - ❌ `TestSwapInt32`
        - ✅ `TestSwapInt64`
        - ❌ `TestSwapPointer`
        - ❌ `TestSwapUint32`
        - ✅ `TestSwapUint64`
        - ❌ `TestSwapUintptr`

- **File:** `src/sync/atomic/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (19):
        - ❌ `AddInt32`
        - ❌ `AddUint32`
        - ❌ `AddUintptr`
        - ❌ `CompareAndSwapInt32`
        - ❌ `CompareAndSwapPointer`
        - ❌ `CompareAndSwapUint32`
        - ❌ `CompareAndSwapUintptr`
        - ❌ `LoadInt32`
        - ❌ `LoadPointer`
        - ❌ `LoadUint32`
        - ❌ `LoadUintptr`
        - ❌ `StoreInt32`
        - ❌ `StorePointer`
        - ❌ `StoreUint32`
        - ❌ `StoreUintptr`
        - ❌ `SwapInt32`
        - ❌ `SwapPointer`
        - ❌ `SwapUint32`
        - ❌ `SwapUintptr`

- **File:** `src/sync/atomic/type.go`
    - Ground Truth Functions (2):
        - `CompareAndSwap`
        - `b32`
    - Predicted Functions (5):
        - ❌ `Add`
        - ✅ `CompareAndSwap`
        - ❌ `Load`
        - ❌ `Store`
        - ❌ `Swap`

- **File:** `src/sync/atomic/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `CompareAndSwap`
        - ❌ `Load`
        - ❌ `Store`
        - ❌ `Swap`


### 📊 **Proposal #53747 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 42.9% | 50.0% | 3/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/flag/example_func_test.go`
    - Ground Truth Functions (1):
        - `ExampleBoolFunc`
    - Predicted Functions (0):

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (4):
        - `BoolFunc`
        - `Func`
        - `TextVar`
        - `UnquoteUsage`
    - Predicted Functions (3):
        - ✅ `BoolFunc`
        - ✅ `Func`
        - ❌ `IsBoolFlag`

- **File:** `src/flag/flag_test.go`
    - Ground Truth Functions (2):
        - `TestEverything`
        - `TestUserDefinedBoolFunc`
    - Predicted Functions (2):
        - ❌ `IsBoolFlag`
        - ✅ `TestUserDefinedBoolFunc`


### 📊 **Proposal #36771 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/strconv.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/tar/strconv_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strconv/atoc.go`
    - Ground Truth Functions (2):
        - `ParseComplex`
        - `convErr`
    - Predicted Functions (0):

- **File:** `src/strconv/atoc_test.go`
    - Ground Truth Functions (1):
        - `TestParseComplex`
    - Predicted Functions (0):

- **File:** `src/strconv/atof.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ParseFloat`

- **File:** `src/strconv/atoi.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ParseFloat`

- **File:** `src/strconv/atoi_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strconv/ctoa.go`
    - Ground Truth Functions (1):
        - `FormatComplex`
    - Predicted Functions (0):

- **File:** `src/strconv/decimal.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strconv/ftoa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `FormatFloat`
        - ❌ `ParseFloat`


### 📊 **Proposal #40592 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 14.3% | 14.3% | 2/14 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (1):
        - `encode`
    - Predicted Functions (0):

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (6):
        - `TestEmbeddedMethods`
        - `TestMethodValue`
        - `TestNestedMethods`
        - `TestSlice`
        - `TestSlice3`
        - `verifyGCBitsSlice`
    - Predicted Functions (0):

- **File:** `src/reflect/deepequal.go`
    - Ground Truth Functions (1):
        - `deepValueEqual`
    - Predicted Functions (0):

- **File:** `src/reflect/set_test.go`
    - Ground Truth Functions (1):
        - `TestImplicitMapConversion`
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (1):
        - `StructOf`
    - Predicted Functions (9):
        - ❌ `Addr`
        - ❌ `Elem`
        - ❌ `Field`
        - ❌ `FieldByIndex`
        - ❌ `FieldByName`
        - ❌ `FieldByNameFunc`
        - ❌ `NumField`
        - ❌ `Pointer`
        - ❌ `UnsafeAddr`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (4):
        - `Pointer`
        - `Recv`
        - `UnsafePointer`
        - `recv`
    - Predicted Functions (5):
        - ❌ `Addr`
        - ❌ `InterfaceData`
        - ✅ `Pointer`
        - ❌ `UnsafeAddr`
        - ✅ `UnsafePointer`


### 📊 **Proposal #46279 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/link/internal/ld/ld_test.go`
    - Ground Truth Functions (1):
        - `TestMemProfileCheck`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/lib.go`
    - Ground Truth Functions (1):
        - `linksetup`
    - Predicted Functions (0):

- **File:** `src/runtime/runtime.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/select.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `block`
        - ❌ `reflect_rselect`
        - ❌ `selectgo`
        - ❌ `selectsetpc`
        - ❌ `sellock`
        - ❌ `selparkcommit`
        - ❌ `selunlock`

- **File:** `src/syscall/rlimit.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Setrlimit`

- **File:** `src/syscall/rlimit_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestOpenFileLimit`

- **File:** `src/syscall/syscall.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Getrlimit`
        - ❌ `Setrlimit`


### 📊 **Proposal #45430 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 23.1% | 15.8% | 18.7% | 3/19 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/cipher_suites.go`
    - Ground Truth Functions (3):
        - `CipherSuites`
        - `InsecureCipherSuites`
        - `selectCipherSuite`
    - Predicted Functions (7):
        - ✅ `CipherSuites`
        - ✅ `InsecureCipherSuites`
        - ❌ `cipher3DES`
        - ❌ `cipherAES`
        - ❌ `cipherSuiteByID`
        - ❌ `mutualCipherSuite`
        - ✅ `selectCipherSuite`

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (3):
        - `cipherSuites`
        - `isSupportedSignatureAlgorithm`
        - `unexpectedMessageError`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (1):
        - `makeClientHello`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server.go`
    - Ground Truth Functions (1):
        - `pickCipherSuite`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server_test.go`
    - Ground Truth Functions (7):
        - `TestAESCipherReordering`
        - `TestAESCipherReorderingTLS13`
        - `TestCipherSuitePreference`
        - `TestHandshakeServerExportKeyingMaterial`
        - `TestHandshakeServerRSAPSS`
        - `TestServerHandshakeContextCancellation`
        - `TestServerResumption`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_server_tls13.go`
    - Ground Truth Functions (1):
        - `processClientHello`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_test.go`
    - Ground Truth Functions (1):
        - `runMain`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/tls.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `(*Dialer) Dial`
        - ❌ `(*Dialer) DialContext`
        - ❌ `Client`
        - ❌ `Dial`
        - ❌ `DialWithDialer`
        - ❌ `Server`

- **File:** `src/crypto/tls/tls_test.go`
    - Ground Truth Functions (2):
        - `TestCipherSuites`
        - `http2isBadCipher`
    - Predicted Functions (0):


### 📊 **Proposal #51684 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.7% | 50.0% | 13.3% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/regexp/regexp.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `Compile`
        - ❌ `Find`
        - ❌ `FindAll`
        - ❌ `FindString`
        - ❌ `Match`
        - ❌ `MatchString`
        - ❌ `MustCompile`
        - ❌ `expand`

- **File:** `src/regexp/syntax/parse.go`
    - Ground Truth Functions (2):
        - `checkHeight`
        - `parse`
    - Predicted Functions (5):
        - ❌ `Error`
        - ❌ `String`
        - ✅ `checkHeight`
        - ❌ `checkLimits`
        - ❌ `newRegexp`


### 📊 **Proposal #47257 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/25 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/importer/gcimporter_test.go`
    - Ground Truth Functions (1):
        - `TestImportTestdata`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/issues_test.go`
    - Ground Truth Functions (1):
        - `TestIssue43124`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/self_test.go`
    - Ground Truth Functions (2):
        - `BenchmarkCheck`
        - `TestSelf`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/sizes_test.go`
    - Ground Truth Functions (1):
        - `TestAtomicAlign`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/typestring_test.go`
    - Ground Truth Functions (1):
        - `TestTypeString`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (3):
        - `packagefile`
        - `runInstall`
        - `setup`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/go/go_test.go`
    - Ground Truth Functions (1):
        - `TestGoInstallPkgdir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/pkg.go`
    - Ground Truth Functions (2):
        - `copyBuild`
        - `load`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modindex/index_test.go`
    - Ground Truth Functions (1):
        - `TestIndex`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modindex/read.go`
    - Ground Truth Functions (1):
        - `Import`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/action.go`
    - Ground Truth Functions (2):
        - `CompileAction`
        - `linkSharedAction`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (1):
        - `InstallPackages`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (2):
        - `buildActionID`
        - `installShlibname`
    - Predicted Functions (0):

- **File:** `src/cmd/link/link_test.go`
    - Ground Truth Functions (1):
        - `TestUnlinkableObj`
    - Predicted Functions (0):

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (1):
        - `Import`
    - Predicted Functions (0):

- **File:** `src/go/internal/gcimporter/gcimporter_test.go`
    - Ground Truth Functions (2):
        - `TestImportTestdata`
        - `TestImportTypeparamTests`
    - Predicted Functions (0):

- **File:** `src/net/http/client.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `CloseIdleConnections`
        - ❌ `Get`
        - ❌ `Head`
        - ❌ `Post`
        - ❌ `PostForm`

- **File:** `src/net/http/cookiejar/jar.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/cookiejar/jar_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/httptest/httptest.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/httptrace/trace.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/httputil/httputil.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/pprof/pprof.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Handler`
        - ❌ `Profile`
        - ❌ `ServeHTTP`
        - ❌ `Trace`

- **File:** `src/net/http/pprof/pprof_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (0):
    - Predicted Functions (12):
        - ❌ `Handle`
        - ❌ `HandleFunc`
        - ❌ `ListenAndServe`
        - ❌ `ListenAndServeTLS`
        - ❌ `NotFound`
        - ❌ `NotFoundHandler`
        - ❌ `Redirect`
        - ❌ `Serve`
        - ❌ `ServeHTTP`
        - ❌ `ServeTLS`
        - ❌ `StripPrefix`
        - ❌ `TimeoutHandler`

- **File:** `src/runtime/sys_darwin.go`
    - Ground Truth Functions (1):
        - `crypto_x509_syscall`
    - Predicted Functions (0):

- **File:** `src/syscall/net.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #38687 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/generate/generate.go`
    - Ground Truth Functions (3):
        - `init`
        - `run`
        - `runGenerate`
    - Predicted Functions (0):


### 📊 **Proposal #47781 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/25 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/cgo/ast.go`
    - Ground Truth Functions (1):
        - `walk`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/ast_go1.go`
    - Ground Truth Functions (1):
        - `walkUnexpected`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/ast_go118.go`
    - Ground Truth Functions (1):
        - `walkUnexpected`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/gcc.go`
    - Ground Truth Functions (1):
        - `rewriteName`
    - Predicted Functions (0):

- **File:** `src/go/ast/ast.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `FuncDecl`
        - ❌ `FuncType`
        - ❌ `IndexListExpr`
        - ❌ `MultiIndexExpr`

- **File:** `src/go/ast/ast_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/ast/walk.go`
    - Ground Truth Functions (1):
        - `Walk`
    - Predicted Functions (0):

- **File:** `src/go/parser/parser.go`
    - Ground Truth Functions (4):
        - `parseFuncDecl`
        - `parseGenericType`
        - `parseMethodSpec`
        - `parsePrimaryExpr`
    - Predicted Functions (0):

- **File:** `src/go/parser/resolver.go`
    - Ground Truth Functions (2):
        - `Visit`
        - `walkFuncType`
    - Predicted Functions (0):

- **File:** `src/go/printer/nodes.go`
    - Ground Truth Functions (3):
        - `expr1`
        - `signature`
        - `spec`
    - Predicted Functions (0):

- **File:** `src/go/token/token.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/token/token_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/types/call.go`
    - Ground Truth Functions (1):
        - `arguments`
    - Predicted Functions (0):

- **File:** `src/go/types/decl.go`
    - Ground Truth Functions (2):
        - `funcDecl`
        - `typeDecl`
    - Predicted Functions (0):

- **File:** `src/go/types/expr.go`
    - Ground Truth Functions (1):
        - `exprInternal`
    - Predicted Functions (0):

- **File:** `src/go/types/exprstring.go`
    - Ground Truth Functions (1):
        - `WriteExpr`
    - Predicted Functions (0):

- **File:** `src/go/types/interface.go`
    - Ground Truth Functions (1):
        - `interfaceType`
    - Predicted Functions (0):

- **File:** `src/go/types/resolver.go`
    - Ground Truth Functions (2):
        - `collectObjects`
        - `unpackRecv`
    - Predicted Functions (0):

- **File:** `src/go/types/signature.go`
    - Ground Truth Functions (1):
        - `funcType`
    - Predicted Functions (0):

- **File:** `src/go/types/struct.go`
    - Ground Truth Functions (1):
        - `embeddedFieldIdent`
    - Predicted Functions (0):

- **File:** `src/go/types/typexpr.go`
    - Ground Truth Functions (1):
        - `typInternal`
    - Predicted Functions (0):


### 📊 **Proposal #50332 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/21 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/doc/main.go`
    - Ground Truth Functions (1):
        - `do`
    - Predicted Functions (0):

- **File:** `src/cmd/go/chdir_test.go`
    - Ground Truth Functions (1):
        - `TestChdir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/base/flag.go`
    - Ground Truth Functions (1):
        - `AddChdirFlag`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/bug/bug.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/envcmd/env.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/fmtcmd/fmt.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/download.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/edit.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/graph.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/init.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/tidy.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/vendor.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/verify.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/why.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/tool/tool.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/version/version.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (1):
        - `AddBuildFlags`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/workcmd/edit.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/workcmd/init.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/workcmd/sync.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/workcmd/use.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):


### 📊 **Proposal #45964 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.7% | 2.0% | 3.1% | 1/50 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/internal/poll/sock_cloexec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `accept`

- **File:** `src/syscall/exec_linux.go`
    - Ground Truth Functions (3):
        - `forkAndExecInChild1`
        - `formatIDMappings`
        - `writeIDMappings`
    - Predicted Functions (3):
        - ❌ `forkAndExecFailureCleanup`
        - ❌ `forkAndExecInChild`
        - ✅ `forkAndExecInChild1`

- **File:** `src/syscall/syscall_linux.go`
    - Ground Truth Functions (6):
        - `Accept`
        - `Futimes`
        - `Futimesat`
        - `Pipe`
        - `Pipe2`
        - `UtimesNano`
    - Predicted Functions (6):
        - ❌ `Mmap`
        - ❌ `Munmap`
        - ❌ `RawSyscall`
        - ❌ `RawSyscall6`
        - ❌ `Syscall`
        - ❌ `Syscall6`

- **File:** `src/syscall/syscall_linux_amd64.go`
    - Ground Truth Functions (2):
        - `SetControllen`
        - `SetLen`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_arm.go`
    - Ground Truth Functions (2):
        - `Seek`
        - `seek`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_mips64x.go`
    - Ground Truth Functions (2):
        - `Ioperm`
        - `Iopl`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_mipsx.go`
    - Ground Truth Functions (1):
        - `mmap`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_ppc64x.go`
    - Ground Truth Functions (3):
        - `SetControllen`
        - `SetLen`
        - `SyncFileRange`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_riscv64.go`
    - Ground Truth Functions (3):
        - `InotifyInit`
        - `SetControllen`
        - `SetLen`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_s390x.go`
    - Ground Truth Functions (1):
        - `mmap`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestFaccessat`
        - ❌ `TestFchmodat`
        - ❌ `TestPrlimitFileLimit`
        - ❌ `TestPrlimitOtherProcess`
        - ❌ `TestPrlimitSelf`

- **File:** `src/syscall/zsyscall_linux_386.go`
    - Ground Truth Functions (3):
        - `Dup2`
        - `Munlockall`
        - `pipe2`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_amd64.go`
    - Ground Truth Functions (2):
        - `pipe2`
        - `utimes`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_arm.go`
    - Ground Truth Functions (2):
        - `Munlockall`
        - `pipe2`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_arm64.go`
    - Ground Truth Functions (2):
        - `Gettimeofday`
        - `pipe2`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_mips.go`
    - Ground Truth Functions (3):
        - `EpollWait`
        - `mmap2`
        - `pipe2`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_mips64.go`
    - Ground Truth Functions (2):
        - `pipe2`
        - `utimes`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_mips64le.go`
    - Ground Truth Functions (2):
        - `pipe2`
        - `utimes`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_mipsle.go`
    - Ground Truth Functions (3):
        - `EpollWait`
        - `mmap2`
        - `pipe2`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_ppc64.go`
    - Ground Truth Functions (2):
        - `pipe2`
        - `utimes`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_ppc64le.go`
    - Ground Truth Functions (2):
        - `pipe2`
        - `utimes`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_riscv64.go`
    - Ground Truth Functions (2):
        - `Gettimeofday`
        - `pipe2`
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_linux_s390x.go`
    - Ground Truth Functions (2):
        - `pipe2`
        - `utimes`
    - Predicted Functions (0):


### 📊 **Proposal #41696 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/16 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (1):
        - `cmdbootstrap`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/go/go_test.go`
    - Ground Truth Functions (4):
        - `TestImportPath`
        - `TestInstallWithTags`
        - `TestNewReleaseRebuildsStalePackagesInGOPATH`
        - `TestParallelTest`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/test/test.go`
    - Ground Truth Functions (1):
        - `runTest`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/test/testflag.go`
    - Ground Truth Functions (2):
        - `init`
        - `testFlags`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (5):
        - `InstallPackages`
        - `init`
        - `omitTestOnly`
        - `runBuild`
        - `runInstall`
    - Predicted Functions (0):

- **File:** `src/cmd/link/dwarf_test.go`
    - Ground Truth Functions (2):
        - `TestMain`
        - `testDWARF`
    - Predicted Functions (0):

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Import`
        - ❌ `ImportDir`
        - ❌ `shouldBuild`

- **File:** `src/go/build/build_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestImportCmd`


### 📊 **Proposal #50674 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 22.2% | 22.2% | 2/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/parser.go`
    - Ground Truth Functions (4):
        - `ParseRevocationList`
        - `parseExtension`
        - `parseTime`
        - `parseValidity`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/pkix/pkix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `CertificateList`
        - ❌ `CheckCRLSignature`
        - ❌ `ParseCRL`
        - ❌ `ParseDERCRL`

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (2):
        - `CheckSignatureFrom`
        - `ParseDERCRL`
    - Predicted Functions (5):
        - ❌ `CheckCRLSignature`
        - ✅ `CheckSignatureFrom`
        - ❌ `ParseCRL`
        - ✅ `ParseDERCRL`
        - ❌ `ParseRevocationList`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (3):
        - `TestCreateRevocationList`
        - `TestParseRevocationList`
        - `TestRevocationListCheckSignatureFrom`
    - Predicted Functions (0):


### 📊 **Proposal #51414 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/time/abs_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/time/time.go`
    - Ground Truth Functions (1):
        - `Abs`
    - Predicted Functions (3):
        - ✅ `Abs`
        - ❌ `Compare`
        - ❌ `Sub`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (1):
        - `TestDurationAbs`
    - Predicted Functions (2):
        - ✅ `TestDurationAbs`
        - ❌ `TestSub`


### 📊 **Proposal #41563 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 9.1% | 10.0% | 1/11 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/asn1/asn1.go`
    - Ground Truth Functions (1):
        - `parseField`
    - Predicted Functions (0):

- **File:** `src/encoding/asn1/marshal.go`
    - Ground Truth Functions (1):
        - `makeBody`
    - Predicted Functions (0):

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (1):
        - `typeFields`
    - Predicted Functions (0):

- **File:** `src/encoding/xml/typeinfo.go`
    - Ground Truth Functions (1):
        - `getTypeInfo`
    - Predicted Functions (0):

- **File:** `src/net/rpc/server.go`
    - Ground Truth Functions (1):
        - `suitableMethods`
    - Predicted Functions (0):

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (2):
        - `TestFieldPkgPath`
        - `TestMethodPkgPath`
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (3):
        - `IsExported`
        - `StructOf`
        - `runtimeStructField`
    - Predicted Functions (5):
        - ❌ `Field`
        - ✅ `IsExported`
        - ❌ `Method`
        - ❌ `NumMethod`
        - ❌ `PkgPath`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Field`
        - ❌ `Method`
        - ❌ `NumField`
        - ❌ `NumMethod`

- **File:** `src/text/template/exec.go`
    - Ground Truth Functions (1):
        - `evalField`
    - Predicted Functions (0):


### 📊 **Proposal #37776 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 30.0% | 31.6% | 3/10 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/url/example_test.go`
    - Ground Truth Functions (2):
        - `ExampleURL_EscapedFragment`
        - `ExampleURL_EscapedPath`
    - Predicted Functions (0):

- **File:** `src/net/url/url.go`
    - Ground Truth Functions (7):
        - `EscapedFragment`
        - `EscapedPath`
        - `Parse`
        - `ResolveReference`
        - `String`
        - `setFragment`
        - `validEncoded`
    - Predicted Functions (5):
        - ✅ `EscapedFragment`
        - ✅ `EscapedPath`
        - ❌ `RawFragment`
        - ✅ `setFragment`
        - ❌ `setPath`

- **File:** `src/net/url/url_test.go`
    - Ground Truth Functions (1):
        - `ufmt`
    - Predicted Functions (4):
        - ❌ `TestParse`
        - ❌ `TestResolveReference`
        - ❌ `TestShouldEscape`
        - ❌ `TestURLString`


### 📊 **Proposal #44808 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 16.7% | 18.2% | 3/18 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/image/draw/bench_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `BenchmarkRGBA64ImageMaskOver`

- **File:** `src/image/draw/draw.go`
    - Ground Truth Functions (2):
        - `DrawMask`
        - `drawRGBA`
    - Predicted Functions (3):
        - ❌ `RGBA64At`
        - ❌ `SetRGBA64`
        - ❌ `drawRGBA64ImageMaskOver`

- **File:** `src/image/draw/draw_test.go`
    - Ground Truth Functions (10):
        - `At`
        - `PixOffset`
        - `RGBA64At`
        - `Set`
        - `SetRGBA64`
        - `TestDraw`
        - `convertToSlowerRGBA`
        - `convertToSlowestRGBA`
        - `init`
        - `makeGolden`
    - Predicted Functions (0):

- **File:** `src/image/geom.go`
    - Ground Truth Functions (1):
        - `RGBA64At`
    - Predicted Functions (0):

- **File:** `src/image/image.go`
    - Ground Truth Functions (2):
        - `RGBA64At`
        - `SetRGBA64`
    - Predicted Functions (8):
        - ❌ `NewAlpha16`
        - ❌ `NewCMYK`
        - ❌ `NewGray`
        - ❌ `NewNRGBA64`
        - ❌ `NewPaletted`
        - ❌ `NewRGBA64`
        - ✅ `RGBA64At`
        - ✅ `SetRGBA64`

- **File:** `src/image/image_test.go`
    - Ground Truth Functions (1):
        - `TestRGBA64Image`
    - Predicted Functions (3):
        - ❌ `BenchmarkRGBA64At`
        - ❌ `BenchmarkRGBA64SetRGBA64`
        - ✅ `TestRGBA64Image`

- **File:** `src/image/names.go`
    - Ground Truth Functions (1):
        - `RGBA64At`
    - Predicted Functions (0):

- **File:** `src/image/ycbcr.go`
    - Ground Truth Functions (1):
        - `RGBA64At`
    - Predicted Functions (0):


### 📊 **Proposal #51566 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 33.3% | 22.2% | 2/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/bytes/bytes.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `NopCloser`
        - ❌ `nopCloserForward`
        - ❌ `nopCloserSimple`

- **File:** `src/bytes/bytes_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `nopCloserForward`
        - ❌ `nopCloserSimple`

- **File:** `src/bytes/reader.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `WriteTo`

- **File:** `src/bytes/reader_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestReaderWriteTo`

- **File:** `src/io/io.go`
    - Ground Truth Functions (2):
        - `NopCloser`
        - `WriteTo`
    - Predicted Functions (4):
        - ❌ `Close`
        - ✅ `NopCloser`
        - ✅ `WriteTo`
        - ❌ `nopCloserWriterTo`

- **File:** `src/io/io_test.go`
    - Ground Truth Functions (1):
        - `TestNopCloserWriterToForwarding`
    - Predicted Functions (0):

- **File:** `src/io/ioutil/ioutil.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `NopCloser`

- **File:** `src/net/http/transfer.go`
    - Ground Truth Functions (3):
        - `isKnownInMemoryReader`
        - `unwrapBody`
        - `unwrapNopCloser`
    - Predicted Functions (0):


### 📊 **Proposal #40082 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 33.3% | 30.8% | 2/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/database/sql/driver/types.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ConvertValue`

- **File:** `src/database/sql/fakedb_test.go`
    - Ground Truth Functions (2):
        - `colTypeToReflectType`
        - `converterForType`
    - Predicted Functions (0):

- **File:** `src/database/sql/sql.go`
    - Ground Truth Functions (2):
        - `Scan`
        - `Value`
    - Predicted Functions (6):
        - ❌ `NullByte`
        - ❌ `NullInt16`
        - ❌ `NullInt32`
        - ❌ `NullInt64`
        - ✅ `Scan`
        - ✅ `Value`

- **File:** `src/database/sql/sql_test.go`
    - Ground Truth Functions (2):
        - `TestNullByteParam`
        - `TestNullInt16Param`
    - Predicted Functions (0):


### 📊 **Proposal #44011 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.7% | 12.5% | 8.7% | 1/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestExtraFiles`
        - ❌ `TestExtraFilesRace`
        - ❌ `TestPipes`
        - ❌ `cmdPipeTest`

- **File:** `src/os/exec/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `StartProcess`
        - ❌ `getSysProcAttr`
        - ❌ `setSysProcAttr`
        - ❌ `syscallStartProcess`

- **File:** `src/os/exec/exec_windows_test.go`
    - Ground Truth Functions (1):
        - `TestPipePassing`
    - Predicted Functions (0):

- **File:** `src/os/exec/internal/fdtest/exists_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/file_windows.go`
    - Ground Truth Functions (1):
        - `Pipe`
    - Predicted Functions (0):

- **File:** `src/os/os_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestStartProcessAttr`

- **File:** `src/syscall/exec_windows.go`
    - Ground Truth Functions (1):
        - `StartProcess`
    - Predicted Functions (0):

- **File:** `src/syscall/exec_windows_test.go`
    - Ground Truth Functions (1):
        - `TestChangingProcessParent`
    - Predicted Functions (0):

- **File:** `src/syscall/security_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (1):
        - `newProcThreadAttributeList`
    - Predicted Functions (6):
        - ❌ `(*procThreadAttributeListContainer) delete`
        - ❌ `(*procThreadAttributeListContainer) list`
        - ❌ `(*procThreadAttributeListContainer) update`
        - ❌ `CreateFile`
        - ❌ `GetStartupInfo`
        - ✅ `newProcThreadAttributeList`

- **File:** `src/syscall/zsyscall_windows.go`
    - Ground Truth Functions (3):
        - `deleteProcThreadAttributeList`
        - `initializeProcThreadAttributeList`
        - `updateProcThreadAttribute`
    - Predicted Functions (0):


### 📊 **Proposal #43724 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/internal/objabi/flag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/funcid.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/head.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/line.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/path.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/reloctype.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/reloctype_string.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/stack.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/symkind.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/symkind_string.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objabi/util.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/elf.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/goobj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/macho.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/objfile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/pe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/plan9obj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/internal/objfile/xcoff.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/syscall/windows/zsyscall_windows.go`
    - Ground Truth Functions (2):
        - `GetComputerNameEx`
        - `SetFileInformationByHandle`
    - Predicted Functions (0):

- **File:** `src/os/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Command`
        - ❌ `CommandContext`
        - ❌ `LookPath`

- **File:** `src/os/exec/dot_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestLookPath`

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `CombinedOutput`
        - ❌ `Command`
        - ❌ `CommandContext`
        - ❌ `Output`
        - ❌ `Run`
        - ❌ `Start`

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestCommandRelativeName`
        - ❌ `TestNoExistExecutable`
        - ❌ `TestPathRace`

- **File:** `src/syscall/mksyscall_windows.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #39351 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 17.4% | 27.6% | 4/23 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/expvar/expvar.go`
    - Ground Truth Functions (13):
        - `Add`
        - `AddFloat`
        - `Do`
        - `Get`
        - `NewFloat`
        - `NewMap`
        - `NewString`
        - `Publish`
        - `Set`
        - `String`
        - `Value`
        - `addKey`
        - `memstats`
    - Predicted Functions (0):

- **File:** `src/expvar/expvar_test.go`
    - Ground Truth Functions (2):
        - `RemoveAll`
        - `TestString`
    - Predicted Functions (0):

- **File:** `src/sync/atomic/atomic_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestCompareAndSwapPointer`
        - ❌ `TestSwapPointer`

- **File:** `src/sync/atomic/value.go`
    - Ground Truth Functions (4):
        - `CompareAndSwap`
        - `Load`
        - `Store`
        - `Swap`
    - Predicted Functions (4):
        - ✅ `CompareAndSwap`
        - ✅ `Load`
        - ✅ `Store`
        - ✅ `Swap`

- **File:** `src/sync/atomic/value_test.go`
    - Ground Truth Functions (4):
        - `TestValueCompareAndSwapConcurrent`
        - `TestValueSwapConcurrent`
        - `TestValue_CompareAndSwap`
        - `TestValue_Swap`
    - Predicted Functions (0):


### 📊 **Proposal #44435 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/modcmd/download.go`
    - Ground Truth Functions (1):
        - `runDownload`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/modfile.go`
    - Ground Truth Functions (1):
        - `pruningForGoVersion`
    - Predicted Functions (0):


### 📊 **Proposal #46308 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (1):
        - `VersionName`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/tls.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `VersionName`

- **File:** `src/crypto/tls/tls_test.go`
    - Ground Truth Functions (1):
        - `TestVersionName`
    - Predicted Functions (1):
        - ✅ `TestVersionName`


### 📊 **Proposal #43823 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.7% | 50.0% | 10.3% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/strconv/decimal.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Assign`
        - ❌ `Round`
        - ❌ `RoundDown`
        - ❌ `RoundUp`
        - ❌ `RoundedInteger`
        - ❌ `String`

- **File:** `src/strconv/decimal_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestDecimalRound`
        - ❌ `TestDecimalRoundedInteger`
        - ❌ `TestDecimalShift`

- **File:** `src/time/format.go`
    - Ground Truth Functions (4):
        - `commaOrPeriod`
        - `nextStdChunk`
        - `parse`
        - `parseNanoseconds`
    - Predicted Functions (6):
        - ❌ `Parse`
        - ❌ `ParseInLocation`
        - ✅ `commaOrPeriod`
        - ❌ `leadingFraction`
        - ✅ `parse`
        - ❌ `stdFracSecond`

- **File:** `src/time/format_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestFormatFractionalSecondSeparators`
        - ❌ `TestParseFractionalSecondsLongerThanNineDigits`

- **File:** `src/time/time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `Add`
        - ❌ `Date`
        - ❌ `MarshalJSON`
        - ❌ `MarshalText`
        - ❌ `Nanosecond`
        - ❌ `Parse`
        - ❌ `Second`
        - ❌ `Sub`
        - ❌ `UnmarshalJSON`
        - ❌ `UnmarshalText`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `TestDate`
        - ❌ `TestMarshalInvalidTimes`
        - ❌ `TestParseDuration`
        - ❌ `TestParseDurationErrors`
        - ❌ `TestParseDurationRoundTrip`
        - ❌ `TestTimeGob`
        - ❌ `TestTimeJSON`
        - ❌ `TestUnmarshalInvalidTimes`


### 📊 **Proposal #34527 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/21 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/cfg/cfg.go`
    - Ground Truth Functions (1):
        - `gopathDir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/clean/clean.go`
    - Ground Truth Functions (1):
        - `runClean`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/envcmd/env.go`
    - Ground Truth Functions (1):
        - `MkEnv`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/cache.go`
    - Ground Truth Functions (4):
        - `DownloadDir`
        - `SideLock`
        - `cacheDir`
        - `readDiskStatByHash`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/codehost.go`
    - Ground Truth Functions (1):
        - `WorkDir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/git_test.go`
    - Ground Truth Functions (1):
        - `testMain`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/shell.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/coderepo_test.go`
    - Ground Truth Functions (1):
        - `testMain`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/fetch.go`
    - Ground Truth Functions (3):
        - `Download`
        - `Sum`
        - `checkMod`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/sumdb.go`
    - Ground Truth Functions (4):
        - `ReadCache`
        - `ReadConfig`
        - `WriteCache`
        - `WriteConfig`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/init.go`
    - Ground Truth Functions (2):
        - `Init`
        - `WillBeEnabled`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/query_test.go`
    - Ground Truth Functions (1):
        - `testMain`
    - Predicted Functions (0):


### 📊 **Proposal #47216 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/11 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/metrics.go`
    - Ground Truth Functions (4):
        - `compute`
        - `ensure`
        - `initMetrics`
        - `nsToSec`
    - Predicted Functions (0):

- **File:** `src/runtime/metrics_test.go`
    - Ground Truth Functions (3):
        - `TestReadMetrics`
        - `TestReadMetricsConsistency`
        - `withinEpsilon`
    - Predicted Functions (0):

- **File:** `src/runtime/mgc.go`
    - Ground Truth Functions (1):
        - `gcMarkTermination`
    - Predicted Functions (0):

- **File:** `src/runtime/mgclimit.go`
    - Ground Truth Functions (1):
        - `stop`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcscavenge.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/runtime/mheap.go`
    - Ground Truth Functions (1):
        - `allocSpan`
    - Predicted Functions (0):

- **File:** `src/runtime/runtime.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `GOMAXPROCS`
        - ❌ `NumCPU`
        - ❌ `NumCgoCall`
        - ❌ `Version`


### 📊 **Proposal #44006 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/syscall/js/js.go`
    - Ground Truth Functions (2):
        - `ValueOf`
        - `makeValue`
    - Predicted Functions (2):
        - ❌ `JSValue`
        - ✅ `ValueOf`


### 📊 **Proposal #44221 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 26.3% | 62.5% | 37.0% | 5/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/reader.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/tar/reader_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/tar/writer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/tar/writer_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/zip/reader.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/zip/reader_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/zip/writer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/zip/writer_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/bufio/bufio.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/bufio/bufio_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `FieldPos`
        - ❌ `TestReadLine`
        - ❌ `TestReader`
        - ❌ `TestReaderWriteTo`
        - ❌ `TestWriterReadFrom`

- **File:** `src/bufio/scan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ScanLines`

- **File:** `src/bufio/scan_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestScanLineEmptyFinalLine`
        - ❌ `TestScanLineEmptyFinalLineWithCR`
        - ❌ `TestScanLineNoNewline`
        - ❌ `TestScanLineTooLong`
        - ❌ `TestScanLongLines`

- **File:** `src/bytes/bytes.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/bytes/bytes_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/bytes/reader.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/bytes/reader_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/csv/reader.go`
    - Ground Truth Functions (4):
        - `FieldPos`
        - `nextRune`
        - `readLine`
        - `readRecord`
    - Predicted Functions (3):
        - ✅ `FieldPos`
        - ❌ `ParseError`
        - ❌ `Read`

- **File:** `src/encoding/csv/reader_test.go`
    - Ground Truth Functions (4):
        - `TestRead`
        - `errorWithPosition`
        - `firstError`
        - `makePositions`
    - Predicted Functions (5):
        - ❌ `FieldPos`
        - ✅ `TestRead`
        - ✅ `errorWithPosition`
        - ✅ `firstError`
        - ✅ `makePositions`

- **File:** `src/encoding/csv/writer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/csv/writer_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #42102 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 16.7% | 28.6% | 2/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/time/format.go`
    - Ground Truth Functions (1):
        - `parse`
    - Predicted Functions (0):

- **File:** `src/time/time.go`
    - Ground Truth Functions (5):
        - `Date`
        - `IsDST`
        - `UnmarshalBinary`
        - `Zone`
        - `locabs`
    - Predicted Functions (0):

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (1):
        - `TestTimeIsDST`
    - Predicted Functions (0):

- **File:** `src/time/zoneinfo.go`
    - Ground Truth Functions (3):
        - `lookup`
        - `lookupName`
        - `tzset`
    - Predicted Functions (2):
        - ✅ `lookup`
        - ✅ `tzset`

- **File:** `src/time/zoneinfo_read.go`
    - Ground Truth Functions (1):
        - `LoadLocationFromTZData`
    - Predicted Functions (0):

- **File:** `src/time/zoneinfo_test.go`
    - Ground Truth Functions (1):
        - `TestTzset`
    - Predicted Functions (0):


### 📊 **Proposal #39904 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 62.5% | 76.9% | 5/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/testing/match.go`
    - Ground Truth Functions (5):
        - `fullName`
        - `matches`
        - `newMatcher`
        - `splitRegexp`
        - `verify`
    - Predicted Functions (3):
        - ✅ `matches`
        - ✅ `splitRegexp`
        - ✅ `verify`

- **File:** `src/testing/match_test.go`
    - Ground Truth Functions (3):
        - `GoString`
        - `TestMatcher`
        - `TestSplitRegexp`
    - Predicted Functions (2):
        - ✅ `TestMatcher`
        - ✅ `TestSplitRegexp`


### 📊 **Proposal #47609 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 3/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/test/inl_test.go`
    - Ground Truth Functions (1):
        - `TestIntendedInlining`
    - Predicted Functions (0):

- **File:** `src/encoding/json/decode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/json/decode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestMarshalInvalidUTF8`
        - ❌ `TestUnmarshal`

- **File:** `src/encoding/json/encode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `appendString`

- **File:** `src/encoding/json/encode_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `MarshalJSON`
        - ❌ `MarshalText`
        - ❌ `TestEncodeString`
        - ❌ `TestMarshalFloat`

- **File:** `src/unicode/utf8/utf8.go`
    - Ground Truth Functions (2):
        - `AppendRune`
        - `appendRuneNonASCII`
    - Predicted Functions (2):
        - ✅ `AppendRune`
        - ❌ `EncodeRune`

- **File:** `src/unicode/utf8/utf8_test.go`
    - Ground Truth Functions (3):
        - `BenchmarkAppendASCIIRune`
        - `BenchmarkAppendJapaneseRune`
        - `TestAppendRune`
    - Predicted Functions (3):
        - ✅ `BenchmarkAppendASCIIRune`
        - ✅ `TestAppendRune`
        - ❌ `TestEncodeRune`


### 📊 **Proposal #42026 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 37.5% | 3.4% | 6.2% | 12/355 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/reader_test.go`
    - Ground Truth Functions (1):
        - `TestReadTruncation`
    - Predicted Functions (0):

- **File:** `src/archive/tar/tar_test.go`
    - Ground Truth Functions (1):
        - `TestFileInfoHeaderSymlink`
    - Predicted Functions (0):

- **File:** `src/archive/tar/writer_test.go`
    - Ground Truth Functions (1):
        - `TestWriter`
    - Predicted Functions (0):

- **File:** `src/archive/zip/reader_test.go`
    - Ground Truth Functions (2):
        - `messWith`
        - `readTestFile`
    - Predicted Functions (0):

- **File:** `src/archive/zip/writer_test.go`
    - Ground Truth Functions (1):
        - `TestWriterTime`
    - Predicted Functions (0):

- **File:** `src/cmd/addr2line/addr2line_test.go`
    - Ground Truth Functions (2):
        - `TestAddr2Line`
        - `testAddr2Line`
    - Predicted Functions (0):

- **File:** `src/cmd/cover/cover.go`
    - Ground Truth Functions (1):
        - `annotate`
    - Predicted Functions (0):

- **File:** `src/cmd/cover/cover_test.go`
    - Ground Truth Functions (3):
        - `TestCover`
        - `TestDirectives`
        - `TestMain`
    - Predicted Functions (0):

- **File:** `src/cmd/cover/html.go`
    - Ground Truth Functions (1):
        - `htmlOutput`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/main.go`
    - Ground Truth Functions (1):
        - `processFile`
    - Predicted Functions (0):

- **File:** `src/cmd/fix/typecheck.go`
    - Ground Truth Functions (1):
        - `typecheck`
    - Predicted Functions (0):

- **File:** `src/cmd/go/go_test.go`
    - Ground Truth Functions (5):
        - `TestMain`
        - `TestNewReleaseRebuildsStalePackagesInGOPATH`
        - `TestTwoPkgConfigs`
        - `makeTempdir`
        - `tempFile`
    - Predicted Functions (0):

- **File:** `src/cmd/go/go_windows_test.go`
    - Ground Truth Functions (1):
        - `TestAbsolutePath`
    - Predicted Functions (0):

- **File:** `src/cmd/go/help_test.go`
    - Ground Truth Functions (1):
        - `TestDocsUpToDate`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/bug/bug.go`
    - Ground Truth Functions (2):
        - `printGlibcVersion`
        - `printOSDetails`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cache/cache.go`
    - Ground Truth Functions (2):
        - `GetBytes`
        - `putIndexEntry`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cache/cache_test.go`
    - Ground Truth Functions (4):
        - `TestBasic`
        - `TestCacheTrim`
        - `TestGrowth`
        - `TestVerifyPanic`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cache/default.go`
    - Ground Truth Functions (1):
        - `initDefaultCache`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cache/hash_test.go`
    - Ground Truth Functions (1):
        - `TestHashFile`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cfg/cfg.go`
    - Ground Truth Functions (1):
        - `initEnvCache`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/clean/clean.go`
    - Ground Truth Functions (1):
        - `clean`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/envcmd/env.go`
    - Ground Truth Functions (1):
        - `updateEnvFile`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/fsys/fsys.go`
    - Ground Truth Functions (1):
        - `Init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/fsys/fsys_test.go`
    - Ground Truth Functions (1):
        - `initOverlay`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/generate/generate.go`
    - Ground Truth Functions (1):
        - `generate`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/imports/scan_test.go`
    - Ground Truth Functions (1):
        - `TestScanDir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/load/pkg.go`
    - Ground Truth Functions (3):
        - `goModPath`
        - `hasGoFiles`
        - `load`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/lockedfile/internal/filelock/filelock_test.go`
    - Ground Truth Functions (1):
        - `mustTempFile`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/lockedfile/lockedfile_test.go`
    - Ground Truth Functions (2):
        - `TestCanLockExistingFile`
        - `TestSpuriousEDEADLK`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/vendor.go`
    - Ground Truth Functions (4):
        - `copyDir`
        - `matchMetadata`
        - `matchPotentialSourceFile`
        - `runVendor`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modcmd/verify.go`
    - Ground Truth Functions (1):
        - `verifyMod`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/cache.go`
    - Ground Truth Functions (1):
        - `rewriteVersionList`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/cache_test.go`
    - Ground Truth Functions (1):
        - `TestWriteDiskCache`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/codehost.go`
    - Ground Truth Functions (1):
        - `WorkDir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/git_test.go`
    - Ground Truth Functions (1):
        - `testMain`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/shell.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/vcs.go`
    - Ground Truth Functions (1):
        - `ReadZip`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/coderepo.go`
    - Ground Truth Functions (1):
        - `Zip`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/coderepo_test.go`
    - Ground Truth Functions (4):
        - `TestCodeRepo`
        - `TestCodeRepoVersions`
        - `TestLatest`
        - `testMain`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/fetch.go`
    - Ground Truth Functions (2):
        - `download`
        - `downloadZip`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/zip_sum_test/zip_sum_test.go`
    - Ground Truth Functions (1):
        - `TestZipSums`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/init.go`
    - Ground Truth Functions (3):
        - `CreateModFile`
        - `findImportComment`
        - `findModulePath`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/query_test.go`
    - Ground Truth Functions (1):
        - `testMain`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/vendor.go`
    - Ground Truth Functions (1):
        - `readVendorList`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/test/test.go`
    - Ground Truth Functions (3):
        - `builderTest`
        - `hashOpen`
        - `saveOutput`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vcs/vcs_test.go`
    - Ground Truth Functions (1):
        - `TestFromDir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/web/file_test.go`
    - Ground Truth Functions (1):
        - `TestGetFileURL`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/build_test.go`
    - Ground Truth Functions (2):
        - `TestRespectSetgidDir`
        - `TestSharedLibName`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/buildid.go`
    - Ground Truth Functions (1):
        - `gccgoBuildIDFile`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (7):
        - `Do`
        - `build`
        - `cgo`
        - `gccSupportsFlag`
        - `installShlibname`
        - `passLongArgsInResponseFiles`
        - `swigDoIntSize`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (2):
        - `pluginPath`
        - `toolVerify`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/gccgo.go`
    - Ground Truth Functions (1):
        - `link`
    - Predicted Functions (0):

- **File:** `src/cmd/go/proxy_test.go`
    - Ground Truth Functions (1):
        - `readModList`
    - Predicted Functions (0):

- **File:** `src/cmd/go/testdata/addmod.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/go/testdata/savedir.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/gofmt/gofmt.go`
    - Ground Truth Functions (2):
        - `backupFile`
        - `processFile`
    - Predicted Functions (0):

- **File:** `src/cmd/gofmt/gofmt_test.go`
    - Ground Truth Functions (3):
        - `TestBackupFile`
        - `TestCRLF`
        - `runTest`
    - Predicted Functions (0):

- **File:** `src/cmd/nm/nm_test.go`
    - Ground Truth Functions (2):
        - `testGoExec`
        - `testGoLib`
    - Predicted Functions (0):

- **File:** `src/cmd/objdump/objdump_test.go`
    - Ground Truth Functions (1):
        - `TestGoobjFileNumber`
    - Predicted Functions (0):

- **File:** `src/cmd/pack/pack_test.go`
    - Ground Truth Functions (4):
        - `TestExtract`
        - `TestHello`
        - `TestIssue21703`
        - `TestLargeDefs`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (1):
        - `wantedErrors`
    - Predicted Functions (0):

- **File:** `src/compress/bzip2/bzip2_test.go`
    - Ground Truth Functions (1):
        - `mustLoadFile`
    - Predicted Functions (0):

- **File:** `src/compress/flate/deflate_test.go`
    - Ground Truth Functions (1):
        - `TestDeflateInflateString`
    - Predicted Functions (0):

- **File:** `src/compress/flate/huffman_bit_writer_test.go`
    - Ground Truth Functions (3):
        - `testBlock`
        - `testBlockHuff`
        - `testWriterEOF`
    - Predicted Functions (0):

- **File:** `src/compress/flate/reader_test.go`
    - Ground Truth Functions (1):
        - `doBench`
    - Predicted Functions (0):

- **File:** `src/compress/lzw/reader_test.go`
    - Ground Truth Functions (1):
        - `BenchmarkDecoder`
    - Predicted Functions (0):

- **File:** `src/compress/lzw/writer_test.go`
    - Ground Truth Functions (1):
        - `BenchmarkEncoder`
    - Predicted Functions (0):

- **File:** `src/compress/zlib/writer_test.go`
    - Ground Truth Functions (1):
        - `testFileLevelDictReset`
    - Predicted Functions (0):

- **File:** `src/crypto/md5/gen.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/handshake_test.go`
    - Ground Truth Functions (1):
        - `tempFile`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/link_test.go`
    - Ground Truth Functions (1):
        - `TestLinkerGC`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/tls.go`
    - Ground Truth Functions (1):
        - `LoadX509KeyPair`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/name_constraints_test.go`
    - Ground Truth Functions (1):
        - `writePEMsToTempFile`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/root_plan9.go`
    - Ground Truth Functions (1):
        - `loadSystemRoots`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/root_unix.go`
    - Ground Truth Functions (3):
        - `isSameDirSymlink`
        - `loadSystemRoots`
        - `readUniqueDirectoryEntries`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/root_unix_test.go`
    - Ground Truth Functions (1):
        - `TestLoadSystemCertsLoadColonSeparatedDirs`
    - Predicted Functions (0):

- **File:** `src/debug/dwarf/dwarf5ranges_test.go`
    - Ground Truth Functions (1):
        - `TestDwarf5Ranges`
    - Predicted Functions (0):

- **File:** `src/debug/gosym/pclntab_test.go`
    - Ground Truth Functions (2):
        - `Test115PclnParsing`
        - `dotest`
    - Predicted Functions (0):

- **File:** `src/debug/pe/file_test.go`
    - Ground Truth Functions (4):
        - `TestBSSHasZeros`
        - `TestBuildingWindowsGUI`
        - `TestImportedSymbolsNoPanicMissingOptionalHeader`
        - `testDWARF`
    - Predicted Functions (0):

- **File:** `src/embed/internal/embedtest/embedx_test.go`
    - Ground Truth Functions (1):
        - `TestXGlobal`
    - Predicted Functions (0):

- **File:** `src/go/build/build_test.go`
    - Ground Truth Functions (3):
        - `TestImportDirNotExist`
        - `TestImportPackageOutsideModule`
        - `TestMissingImportErrorRepetition`
    - Predicted Functions (0):

- **File:** `src/go/build/deps_test.go`
    - Ground Truth Functions (1):
        - `findImports`
    - Predicted Functions (0):

- **File:** `src/go/doc/doc_test.go`
    - Ground Truth Functions (1):
        - `test`
    - Predicted Functions (0):

- **File:** `src/go/format/benchmark_test.go`
    - Ground Truth Functions (1):
        - `BenchmarkFormat`
    - Predicted Functions (0):

- **File:** `src/go/format/format_test.go`
    - Ground Truth Functions (2):
        - `TestNode`
        - `TestSource`
    - Predicted Functions (0):

- **File:** `src/go/importer/importer_test.go`
    - Ground Truth Functions (1):
        - `TestForCompiler`
    - Predicted Functions (0):

- **File:** `src/go/internal/gccgoimporter/importer_test.go`
    - Ground Truth Functions (1):
        - `TestObjImporter`
    - Predicted Functions (0):

- **File:** `src/go/internal/gcimporter/gcimporter_test.go`
    - Ground Truth Functions (2):
        - `TestVersionHandling`
        - `mktmpdir`
    - Predicted Functions (0):

- **File:** `src/go/internal/srcimporter/srcimporter.go`
    - Ground Truth Functions (1):
        - `cgo`
    - Predicted Functions (0):

- **File:** `src/go/internal/srcimporter/srcimporter_test.go`
    - Ground Truth Functions (1):
        - `walkDir`
    - Predicted Functions (0):

- **File:** `src/go/parser/error_test.go`
    - Ground Truth Functions (1):
        - `TestErrors`
    - Predicted Functions (0):

- **File:** `src/go/parser/interface.go`
    - Ground Truth Functions (2):
        - `ParseDir`
        - `readSource`
    - Predicted Functions (0):

- **File:** `src/go/parser/performance_test.go`
    - Ground Truth Functions (1):
        - `readFile`
    - Predicted Functions (0):

- **File:** `src/go/printer/performance_test.go`
    - Ground Truth Functions (1):
        - `initialize`
    - Predicted Functions (0):

- **File:** `src/go/printer/printer_test.go`
    - Ground Truth Functions (3):
        - `TestBaseIndent`
        - `TestWriteErrors`
        - `runcheck`
    - Predicted Functions (0):

- **File:** `src/go/types/check_test.go`
    - Ground Truth Functions (1):
        - `testDir`
    - Predicted Functions (0):

- **File:** `src/go/types/hilbert_test.go`
    - Ground Truth Functions (1):
        - `TestHilbert`
    - Predicted Functions (0):

- **File:** `src/go/types/stdlib_test.go`
    - Ground Truth Functions (2):
        - `testTestDir`
        - `walk`
    - Predicted Functions (0):

- **File:** `src/hash/crc32/gen_const_ppc64le.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/html/template/examplefiles_test.go`
    - Ground Truth Functions (1):
        - `createTestDir`
    - Predicted Functions (0):

- **File:** `src/html/template/template.go`
    - Ground Truth Functions (1):
        - `readFileOS`
    - Predicted Functions (0):

- **File:** `src/image/color/palette/gen.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/image/gif/reader_test.go`
    - Ground Truth Functions (1):
        - `BenchmarkDecode`
    - Predicted Functions (0):

- **File:** `src/image/internal/imageutil/gen.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/image/jpeg/reader_test.go`
    - Ground Truth Functions (3):
        - `TestDecodeEOF`
        - `TestTruncatedSOSDataDoesntPanic`
        - `benchmarkDecode`
    - Predicted Functions (0):

- **File:** `src/image/png/reader_test.go`
    - Ground Truth Functions (1):
        - `benchmarkDecode`
    - Predicted Functions (0):

- **File:** `src/index/suffixarray/gen.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/index/suffixarray/suffixarray_test.go`
    - Ground Truth Functions (1):
        - `makeText`
    - Predicted Functions (0):

- **File:** `src/internal/cpu/cpu_s390x_test.go`
    - Ground Truth Functions (1):
        - `getFeatureList`
    - Predicted Functions (0):

- **File:** `src/internal/obscuretestdata/obscuretestdata.go`
    - Ground Truth Functions (1):
        - `DecodeToTempFile`
    - Predicted Functions (0):

- **File:** `src/internal/poll/read_test.go`
    - Ground Truth Functions (1):
        - `TestRead`
    - Predicted Functions (0):

- **File:** `src/internal/trace/gc_test.go`
    - Ground Truth Functions (1):
        - `TestMMUTrace`
    - Predicted Functions (0):

- **File:** `src/io/fs/readdir.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `FileInfoToDirEntry`
        - ❌ `ReadDir`

- **File:** `src/io/fs/readdir_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestFileInfoToDirEntry`
        - ❌ `TestReadDir`
        - ❌ `TestReadDirPath`

- **File:** `src/io/fs/readfile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ReadFile`

- **File:** `src/io/fs/readfile_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestReadFile`
        - ❌ `TestReadFilePath`

- **File:** `src/io/ioutil/ioutil.go`
    - Ground Truth Functions (4):
        - `NopCloser`
        - `ReadDir`
        - `ReadFile`
        - `WriteFile`
    - Predicted Functions (3):
        - ✅ `ReadDir`
        - ✅ `ReadFile`
        - ✅ `WriteFile`

- **File:** `src/io/ioutil/ioutil_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestReadDir`
        - ❌ `TestReadFile`
        - ❌ `TestWriteFile`

- **File:** `src/io/ioutil/tempfile.go`
    - Ground Truth Functions (2):
        - `TempDir`
        - `TempFile`
    - Predicted Functions (0):

- **File:** `src/io/ioutil/tempfile_test.go`
    - Ground Truth Functions (2):
        - `TestTempDir_BadPattern`
        - `TestTempFile_BadPattern`
    - Predicted Functions (0):

- **File:** `src/log/syslog/syslog_test.go`
    - Ground Truth Functions (1):
        - `startServer`
    - Predicted Functions (0):

- **File:** `src/math/big/link_test.go`
    - Ground Truth Functions (1):
        - `TestLinkerGC`
    - Predicted Functions (0):

- **File:** `src/math/bits/make_examples.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/math/bits/make_tables.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/mime/multipart/formdata.go`
    - Ground Truth Functions (1):
        - `readForm`
    - Predicted Functions (0):

- **File:** `src/net/dnsclient_unix_test.go`
    - Ground Truth Functions (1):
        - `newResolvConfTest`
    - Predicted Functions (0):

- **File:** `src/net/error_test.go`
    - Ground Truth Functions (1):
        - `TestFileError`
    - Predicted Functions (0):

- **File:** `src/net/http/filetransport_test.go`
    - Ground Truth Functions (1):
        - `TestFileTransport`
    - Predicted Functions (0):

- **File:** `src/net/http/fs_test.go`
    - Ground Truth Functions (3):
        - `TestFileServerImplicitLeadingSlash`
        - `TestLinuxSendfile`
        - `TestServeFile`
    - Predicted Functions (0):

- **File:** `src/net/http/request_test.go`
    - Ground Truth Functions (1):
        - `benchmarkFileAndServer`
    - Predicted Functions (0):

- **File:** `src/net/http/transfer_test.go`
    - Ground Truth Functions (1):
        - `TestTransferWriterWriteBodyReaderTypes`
    - Predicted Functions (0):

- **File:** `src/net/http/transport_test.go`
    - Ground Truth Functions (1):
        - `TestTransportRequestWriteRoundTrip`
    - Predicted Functions (0):

- **File:** `src/net/mockserver_test.go`
    - Ground Truth Functions (1):
        - `testUnixAddr`
    - Predicted Functions (0):

- **File:** `src/net/net_windows_test.go`
    - Ground Truth Functions (1):
        - `runCmd`
    - Predicted Functions (0):

- **File:** `src/net/unixsock_test.go`
    - Ground Truth Functions (1):
        - `TestUnixUnlink`
    - Predicted Functions (0):

- **File:** `src/os/dir.go`
    - Ground Truth Functions (1):
        - `ReadDir`
    - Predicted Functions (0):

- **File:** `src/os/error_test.go`
    - Ground Truth Functions (3):
        - `TestErrIsExist`
        - `TestErrIsNotExist`
        - `TestErrPathNUL`
    - Predicted Functions (0):

- **File:** `src/os/example_test.go`
    - Ground Truth Functions (7):
        - `ExampleCreateTemp`
        - `ExampleCreateTemp_suffix`
        - `ExampleMkdirTemp`
        - `ExampleMkdirTemp_suffix`
        - `ExampleReadDir`
        - `ExampleReadFile`
        - `ExampleWriteFile`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (2):
        - `TestExtraFiles`
        - `TestPipeLookPathLeak`
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_unix_test.go`
    - Ground Truth Functions (1):
        - `TestLookPathUnixEmptyPath`
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_windows_test.go`
    - Ground Truth Functions (1):
        - `TestCommand`
    - Predicted Functions (0):

- **File:** `src/os/fifo_test.go`
    - Ground Truth Functions (1):
        - `TestFifoEOF`
    - Predicted Functions (0):

- **File:** `src/os/file.go`
    - Ground Truth Functions (2):
        - `ReadFile`
        - `WriteFile`
    - Predicted Functions (5):
        - ❌ `Create`
        - ❌ `Mkdir`
        - ✅ `ReadFile`
        - ❌ `TempDir`
        - ✅ `WriteFile`

- **File:** `src/os/file_plan9.go`
    - Ground Truth Functions (1):
        - `rename`
    - Predicted Functions (0):

- **File:** `src/os/file_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/os_test.go`
    - Ground Truth Functions (18):
        - `TestChdirAndGetwd`
        - `TestLongPath`
        - `TestProgWideChdir`
        - `TestReadFileProc`
        - `TestReaddirNValues`
        - `TestReaddirOfFile`
        - `TestReaddirStatFailures`
        - `TestRemoveAllRace`
        - `TestRenameOverwriteDest`
        - `TestSeek`
        - `TestStatDirModeExec`
        - `TestStatDirWithTrailingSlash`
        - `TestStatRelativeSymlink`
        - `TestWriteAt`
        - `checkSize`
        - `newFile`
        - `testChtimes`
        - `writeFile`
    - Predicted Functions (9):
        - ❌ `TestFileReadDir`
        - ❌ `TestReadDir`
        - ✅ `TestReaddirNValues`
        - ✅ `TestReaddirOfFile`
        - ✅ `TestReaddirStatFailures`
        - ❌ `TestReaddirnamesOneAtATime`
        - ❌ `testReadDir`
        - ❌ `testReaddir`
        - ❌ `testReaddirnames`

- **File:** `src/os/os_unix_test.go`
    - Ground Truth Functions (1):
        - `TestReaddirRemoveRace`
    - Predicted Functions (0):

- **File:** `src/os/os_windows_test.go`
    - Ground Truth Functions (7):
        - `TestCmdArgs`
        - `TestDeleteReadOnly`
        - `TestNetworkSymbolicLink`
        - `TestOpenVolumeName`
        - `TestSameWindowsFile`
        - `TestSymlinkCreation`
        - `testDirLinks`
    - Predicted Functions (0):

- **File:** `src/os/path_test.go`
    - Ground Truth Functions (1):
        - `TestMkdirAllWithSymlink`
    - Predicted Functions (0):

- **File:** `src/os/path_windows_test.go`
    - Ground Truth Functions (1):
        - `TestMkdirAllExtendedLength`
    - Predicted Functions (0):

- **File:** `src/os/pipe_test.go`
    - Ground Truth Functions (1):
        - `testClosedPipeRace`
    - Predicted Functions (0):

- **File:** `src/os/read_test.go`
    - Ground Truth Functions (5):
        - `TestReadDir`
        - `TestReadFile`
        - `TestReadOnlyWriteFile`
        - `TestWriteFile`
        - `checkNamedSize`
    - Predicted Functions (0):

- **File:** `src/os/removeall_test.go`
    - Ground Truth Functions (9):
        - `TestRemoveAll`
        - `TestRemoveAllButReadOnlyAndPathError`
        - `TestRemoveAllDot`
        - `TestRemoveAllDotDot`
        - `TestRemoveAllLarge`
        - `TestRemoveAllLongPath`
        - `TestRemoveAllWithMoreErrorThanReqSize`
        - `TestRemoveReadOnlyDir`
        - `TestRemoveUnreadableDir`
    - Predicted Functions (0):

- **File:** `src/os/signal/signal_test.go`
    - Ground Truth Functions (1):
        - `TestDetectNohup`
    - Predicted Functions (0):

- **File:** `src/os/signal/signal_windows_test.go`
    - Ground Truth Functions (1):
        - `TestCtrlBreak`
    - Predicted Functions (0):

- **File:** `src/os/stat_test.go`
    - Ground Truth Functions (3):
        - `TestDirAndSymlinkStats`
        - `TestFileAndSymlinkStats`
        - `TestSymlinkWithTrailingSlash`
    - Predicted Functions (0):

- **File:** `src/os/tempfile.go`
    - Ground Truth Functions (5):
        - `CreateTemp`
        - `MkdirTemp`
        - `joinPath`
        - `nextRandom`
        - `prefixAndSuffix`
    - Predicted Functions (2):
        - ✅ `CreateTemp`
        - ✅ `MkdirTemp`

- **File:** `src/os/tempfile_test.go`
    - Ground Truth Functions (6):
        - `TestCreateTemp`
        - `TestCreateTempBadPattern`
        - `TestCreateTempPattern`
        - `TestMkdirTemp`
        - `TestMkdirTempBadDir`
        - `TestMkdirTempBadPattern`
    - Predicted Functions (2):
        - ✅ `TestCreateTemp`
        - ✅ `TestMkdirTemp`

- **File:** `src/os/timeout_test.go`
    - Ground Truth Functions (1):
        - `TestNonpollableDeadline`
    - Predicted Functions (0):

- **File:** `src/os/user/lookup_plan9.go`
    - Ground Truth Functions (1):
        - `current`
    - Predicted Functions (0):

- **File:** `src/path/filepath/example_unix_walk_test.go`
    - Ground Truth Functions (1):
        - `prepareTestDirTree`
    - Predicted Functions (0):

- **File:** `src/path/filepath/match_test.go`
    - Ground Truth Functions (2):
        - `TestGlobSymlink`
        - `TestWindowsGlob`
    - Predicted Functions (0):

- **File:** `src/path/filepath/path_test.go`
    - Ground Truth Functions (11):
        - `TestAbs`
        - `TestAbsEmptyString`
        - `TestEvalSymlinks`
        - `TestEvalSymlinksAboveRoot`
        - `TestEvalSymlinksAboveRootChdir`
        - `TestIssue13582`
        - `TestIssue29372`
        - `TestWalkFileError`
        - `TestWalkSkipDirOnFile`
        - `testWalk`
        - `testWalkSymlink`
    - Predicted Functions (0):

- **File:** `src/path/filepath/path_windows_test.go`
    - Ground Truth Functions (5):
        - `TestEvalSymlinksCanonicalNames`
        - `TestNTNamespaceSymlink`
        - `TestToNorm`
        - `TestWindowsEvalSymlinks`
        - `testWinSplitListTestIsValid`
    - Predicted Functions (0):

- **File:** `src/runtime/crash_test.go`
    - Ground Truth Functions (1):
        - `buildTestProg`
    - Predicted Functions (0):

- **File:** `src/runtime/crash_unix_test.go`
    - Ground Truth Functions (1):
        - `TestCrashDumpsAllThreads`
    - Predicted Functions (0):

- **File:** `src/runtime/debug/heapdump_test.go`
    - Ground Truth Functions (2):
        - `TestWriteHeapDumpFinalizers`
        - `TestWriteHeapDumpNonempty`
    - Predicted Functions (0):

- **File:** `src/runtime/debug_test.go`
    - Ground Truth Functions (1):
        - `skipUnderDebugger`
    - Predicted Functions (0):

- **File:** `src/runtime/memmove_linux_amd64_test.go`
    - Ground Truth Functions (1):
        - `TestMemmoveOverflow`
    - Predicted Functions (0):

- **File:** `src/runtime/mkduff.go`
    - Ground Truth Functions (1):
        - `gen`
    - Predicted Functions (0):

- **File:** `src/runtime/mkfastlog2table.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/pprof_test.go`
    - Ground Truth Functions (2):
        - `TestAtomicLoadStore64`
        - `TestTracebackAll`
    - Predicted Functions (0):

- **File:** `src/runtime/pprof/proto_test.go`
    - Ground Truth Functions (1):
        - `testPCs`
    - Predicted Functions (0):

- **File:** `src/runtime/race/output_test.go`
    - Ground Truth Functions (1):
        - `TestOutput`
    - Predicted Functions (0):

- **File:** `src/runtime/race/testdata/io_test.go`
    - Ground Truth Functions (1):
        - `TestNoRaceIOFile`
    - Predicted Functions (0):

- **File:** `src/runtime/runtime-gdb_test.go`
    - Ground Truth Functions (6):
        - `TestGdbAutotmpTypes`
        - `TestGdbBacktrace`
        - `TestGdbConst`
        - `TestGdbInfCallstack`
        - `TestGdbPanic`
        - `testGdbPython`
    - Predicted Functions (0):

- **File:** `src/runtime/runtime-lldb_test.go`
    - Ground Truth Functions (1):
        - `TestLldbPython`
    - Predicted Functions (0):

- **File:** `src/runtime/signal_windows_test.go`
    - Ground Truth Functions (2):
        - `TestLibraryCtrlHandler`
        - `TestVectoredHandlerDontCrashOnLibrary`
    - Predicted Functions (0):

- **File:** `src/runtime/syscall_windows_test.go`
    - Ground Truth Functions (7):
        - `BenchmarkRunningGoProgram`
        - `TestBigStackCallbackSyscall`
        - `TestDLLPreloadMitigation`
        - `TestFloatArgs`
        - `TestFloatReturn`
        - `TestReturnAfterStackGrowInCallback`
        - `TestStdcallAndCDeclCallbacks`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprog/memprof.go`
    - Ground Truth Functions (1):
        - `MemProf`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprog/syscalls_linux.go`
    - Ground Truth Functions (1):
        - `tidExists`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprog/timeprof.go`
    - Ground Truth Functions (1):
        - `TimeProf`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprog/vdso.go`
    - Ground Truth Functions (1):
        - `signalInVDSO`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprogcgo/pprof.go`
    - Ground Truth Functions (1):
        - `CgoPprof`
    - Predicted Functions (0):

- **File:** `src/runtime/testdata/testprogcgo/threadpprof.go`
    - Ground Truth Functions (1):
        - `pprofThread`
    - Predicted Functions (0):

- **File:** `src/runtime/trace/trace_test.go`
    - Ground Truth Functions (1):
        - `saveTrace`
    - Predicted Functions (0):

- **File:** `src/runtime/wincallback.go`
    - Ground Truth Functions (3):
        - `genasm386Amd64`
        - `genasmArm`
        - `gengo`
    - Predicted Functions (0):

- **File:** `src/strconv/makeisprint.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/syscall/dirent_test.go`
    - Ground Truth Functions (2):
        - `TestDirent`
        - `TestDirentRepeat`
    - Predicted Functions (0):

- **File:** `src/syscall/exec_linux_test.go`
    - Ground Truth Functions (4):
        - `TestUnshare`
        - `TestUnshareMountNameSpace`
        - `TestUnshareMountNameSpaceChroot`
        - `testAmbientCaps`
    - Predicted Functions (0):

- **File:** `src/syscall/getdirentries_test.go`
    - Ground Truth Functions (1):
        - `testGetdirentries`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_test.go`
    - Ground Truth Functions (2):
        - `TestSyscallNoError`
        - `compareStatus`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_unix_test.go`
    - Ground Truth Functions (3):
        - `TestFcntlFlock`
        - `TestPassFD`
        - `passFDChild`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_windows_test.go`
    - Ground Truth Functions (1):
        - `TestWin32finddata`
    - Predicted Functions (0):

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (1):
        - `TempDir`
    - Predicted Functions (0):

- **File:** `src/testing/testing_test.go`
    - Ground Truth Functions (1):
        - `testTempDir`
    - Predicted Functions (0):

- **File:** `src/text/template/examplefiles_test.go`
    - Ground Truth Functions (1):
        - `createTestDir`
    - Predicted Functions (0):

- **File:** `src/text/template/helper.go`
    - Ground Truth Functions (1):
        - `readFileOS`
    - Predicted Functions (0):

- **File:** `src/text/template/link_test.go`
    - Ground Truth Functions (1):
        - `TestLinkerGC`
    - Predicted Functions (0):

- **File:** `src/time/genzabbrs.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #33184 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 27.3% | 50.0% | 35.3% | 3/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `lib/time/mkzip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/time.go`
    - Ground Truth Functions (1):
        - `goroutineReady`
    - Predicted Functions (3):
        - ❌ `reset`
        - ❌ `resetTimer`
        - ❌ `stopTimer`

- **File:** `src/runtime/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestTicker`

- **File:** `src/time/tick.go`
    - Ground Truth Functions (2):
        - `Reset`
        - `Tick`
    - Predicted Functions (3):
        - ❌ `NewTicker`
        - ✅ `Reset`
        - ❌ `Stop`

- **File:** `src/time/tick_test.go`
    - Ground Truth Functions (3):
        - `BenchmarkTickerReset`
        - `BenchmarkTickerResetNaive`
        - `TestTicker`
    - Predicted Functions (4):
        - ✅ `BenchmarkTickerReset`
        - ❌ `Reset`
        - ✅ `TestTicker`
        - ❌ `TestTickerResetLtZeroDuration`


### 📊 **Proposal #44143 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/context/context.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Background`
        - ❌ `TODO`

- **File:** `src/context/context_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `XTestCancelRemoves`
        - ❌ `XTestChildFinishesFirst`
        - ❌ `XTestCustomContextGoroutines`
        - ❌ `XTestParentFinishesChild`

- **File:** `src/net/http/socks_bundle.go`
    - Ground Truth Functions (1):
        - `Dial`
    - Predicted Functions (0):


### 📊 **Proposal #49390 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (4):
        - `checkNotStale`
        - `cmdbootstrap`
        - `goCmd`
        - `setNoOpt`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `cmdtest`
    - Predicted Functions (0):

- **File:** `src/internal/testenv/noopt.go`
    - Ground Truth Functions (1):
        - `OptimizationOff`
    - Predicted Functions (0):

- **File:** `src/internal/testenv/opt.go`
    - Ground Truth Functions (1):
        - `OptimizationOff`
    - Predicted Functions (0):

- **File:** `src/internal/testenv/testenv.go`
    - Ground Truth Functions (1):
        - `SkipIfOptimizationOff`
    - Predicted Functions (0):

- **File:** `src/runtime/runtime.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/runtime_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestEqString`
        - ❌ `TestSetPanicOnFault`
        - ❌ `TestStopCPUProfilingWithProfilerOff`
        - ❌ `TestTimediv`


### 📊 **Proposal #51428 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 50.0% | 14.3% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/context/context.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Done`
        - ❌ `Err`

- **File:** `src/context/context_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `XTestCancelRemoves`

- **File:** `src/net/dial.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Dial`
        - ❌ `DialContext`
        - ❌ `DialTimeout`
        - ❌ `Dialer.Dial`
        - ❌ `Dialer.DialContext`

- **File:** `src/net/error_test.go`
    - Ground Truth Functions (1):
        - `TestContextError`
    - Predicted Functions (0):

- **File:** `src/net/net.go`
    - Ground Truth Functions (1):
        - `Is`
    - Predicted Functions (4):
        - ❌ `(*OpError).Error`
        - ❌ `(*OpError).Unwrap`
        - ✅ `Is`
        - ❌ `canceledError`


### 📊 **Proposal #46059 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 33.3% | 20.0% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/url/url.go`
    - Ground Truth Functions (2):
        - `String`
        - `parse`
    - Predicted Functions (4):
        - ❌ `Hostname`
        - ❌ `OmitHost`
        - ❌ `Parse`
        - ✅ `String`

- **File:** `src/net/url/url_test.go`
    - Ground Truth Functions (1):
        - `ufmt`
    - Predicted Functions (3):
        - ❌ `TestParse`
        - ❌ `TestURLHostnameAndPort`
        - ❌ `TestURLString`


### 📊 **Proposal #51914 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.1% | 50.0% | 12.5% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/http.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `WriteHeader`

- **File:** `src/net/http/httputil/httputil.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ReverseProxy`

- **File:** `src/net/http/httputil/reverseproxy.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (5):
        - ❌ `Forward103Responses`
        - ❌ `NewSingleHostReverseProxy`
        - ✅ `ServeHTTP`
        - ❌ `handleUpgradeResponse`
        - ❌ `modifyResponse`

- **File:** `src/net/http/httputil/reverseproxy_test.go`
    - Ground Truth Functions (1):
        - `Test1xxResponses`
    - Predicted Functions (0):

- **File:** `src/net/http/response.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Write`

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Flush`
        - ❌ `Header`
        - ❌ `Hijack`
        - ❌ `ServeHTTP`
        - ❌ `Write`
        - ❌ `WriteHeader`


### 📊 **Proposal #40995 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 13.7% | 1.4% | 2.5% | 7/510 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/mips64/obj.go`
    - Ground Truth Functions (2):
        - `Init`
        - `archinit`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/sockcmsg_unix_other.go`
    - Ground Truth Functions (1):
        - `cmsgAlignOf`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall.go`
    - Ground Truth Functions (2):
        - `BytePtrToString`
        - `ByteSliceToString`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_aix.go`
    - Ground Truth Functions (4):
        - `Access`
        - `Chmod`
        - `Chown`
        - `Creat`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_bsd.go`
    - Ground Truth Functions (2):
        - `Getwd`
        - `anyToSockaddr`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin.go`
    - Ground Truth Functions (11):
        - `Getfsstat`
        - `Getxattr`
        - `IoctlCtlInfo`
        - `IoctlGetIfreqMTU`
        - `IoctlSetIfreqMTU`
        - `Lgetxattr`
        - `Pipe`
        - `anyToSockaddrGOOS`
        - `direntReclen`
        - `sockaddr`
        - `xattrPointer`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin_amd64.go`
    - Ground Truth Functions (1):
        - `setTimespec`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_darwin_arm64.go`
    - Ground Truth Functions (1):
        - `setTimespec`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_dragonfly.go`
    - Ground Truth Functions (3):
        - `Accept4`
        - `Getfsstat`
        - `anyToSockaddrGOOS`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_freebsd.go`
    - Ground Truth Functions (3):
        - `Accept4`
        - `Getfsstat`
        - `anyToSockaddrGOOS`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_netbsd.go`
    - Ground Truth Functions (3):
        - `Getdirentries`
        - `anyToSockaddrGOOS`
        - `sendfile`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_openbsd.go`
    - Ground Truth Functions (4):
        - `Getdirentries`
        - `Sendfile`
        - `anyToSockaddrGOOS`
        - `sendfile`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/syscall_solaris.go`
    - Ground Truth Functions (1):
        - `IoctlSetTermio`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_amd64.go`
    - Ground Truth Functions (3):
        - `Fstat`
        - `Getcwd`
        - `pipe`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_darwin_arm64.go`
    - Ground Truth Functions (2):
        - `Getcwd`
        - `pipe`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/unix/zsyscall_dragonfly_amd64.go`
    - Ground Truth Functions (2):
        - `sysctl`
        - `utimes`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/windows/syscall.go`
    - Ground Truth Functions (3):
        - `BytePtrToString`
        - `ByteSliceFromString`
        - `ByteSliceToString`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/windows/syscall_windows.go`
    - Ground Truth Functions (4):
        - `GetProcAddressByOrdinal`
        - `UTF16ToString`
        - `WSARecvMsg`
        - `WSASendMsg`
    - Predicted Functions (0):

- **File:** `src/cmd/vendor/golang.org/x/sys/windows/zsyscall_windows.go`
    - Ground Truth Functions (312):
        - `AcceptEx`
        - `AdjustTokenGroups`
        - `AdjustTokenPrivileges`
        - `AllocateAndInitializeSid`
        - `AssignProcessToJobObject`
        - `CancelIo`
        - `CancelIoEx`
        - `CertAddCertificateContextToStore`
        - `CertCloseStore`
        - `CertCreateCertificateContext`
        - `CertEnumCertificatesInStore`
        - `CertFreeCertificateChain`
        - `CertFreeCertificateContext`
        - `CertGetCertificateChain`
        - `CertOpenStore`
        - `CertOpenSystemStore`
        - `CertVerifyCertificateChainPolicy`
        - `ChangeServiceConfig`
        - `ChangeServiceConfig2`
        - `CloseHandle`
        - `CloseServiceHandle`
        - `Closesocket`
        - `CoTaskMemFree`
        - `ControlService`
        - `ConvertSidToStringSid`
        - `ConvertStringSidToSid`
        - `CopySid`
        - `CreateDirectory`
        - `CreateEnvironmentBlock`
        - `CreateEvent`
        - `CreateEventEx`
        - `CreateFile`
        - `CreateFileMapping`
        - `CreateHardLink`
        - `CreateIoCompletionPort`
        - `CreateJobObject`
        - `CreateMutex`
        - `CreateMutexEx`
        - `CreatePipe`
        - `CreateProcess`
        - `CreateService`
        - `CreateSymbolicLink`
        - `CreateToolhelp32Snapshot`
        - `CryptAcquireContext`
        - `CryptGenRandom`
        - `CryptReleaseContext`
        - `DefineDosDevice`
        - `DeleteFile`
        - `DeleteService`
        - `DeleteVolumeMountPoint`
        - `DeregisterEventSource`
        - `DestroyEnvironmentBlock`
        - `DeviceIoControl`
        - `DnsNameCompare`
        - `DnsQuery`
        - `DnsRecordListFree`
        - `DuplicateHandle`
        - `DuplicateTokenEx`
        - `EnumServicesStatusEx`
        - `EqualSid`
        - `ExitProcess`
        - `ExitWindowsEx`
        - `FindClose`
        - `FindFirstVolume`
        - `FindFirstVolumeMountPoint`
        - `FindNextVolume`
        - `FindNextVolumeMountPoint`
        - `FindVolumeClose`
        - `FindVolumeMountPointClose`
        - `FlushFileBuffers`
        - `FlushViewOfFile`
        - `FormatMessage`
        - `FreeAddrInfoW`
        - `FreeEnvironmentStrings`
        - `FreeLibrary`
        - `FreeSid`
        - `GenerateConsoleCtrlEvent`
        - `GetACP`
        - `GetAcceptExSockaddrs`
        - `GetAdaptersAddresses`
        - `GetAdaptersInfo`
        - `GetAddrInfoW`
        - `GetCommandLine`
        - `GetComputerName`
        - `GetComputerNameEx`
        - `GetConsoleMode`
        - `GetConsoleScreenBufferInfo`
        - `GetCurrentDirectory`
        - `GetCurrentProcessId`
        - `GetCurrentThreadId`
        - `GetDiskFreeSpaceEx`
        - `GetDriveType`
        - `GetEnvironmentStrings`
        - `GetEnvironmentVariable`
        - `GetExitCodeProcess`
        - `GetFileAttributes`
        - `GetFileAttributesEx`
        - `GetFileInformationByHandle`
        - `GetFileInformationByHandleEx`
        - `GetFileType`
        - `GetFullPathName`
        - `GetHostByName`
        - `GetIfEntry`
        - `GetLastError`
        - `GetLengthSid`
        - `GetLogicalDriveStrings`
        - `GetLogicalDrives`
        - `GetLongPathName`
        - `GetModuleFileName`
        - `GetModuleHandleEx`
        - `GetOverlappedResult`
        - `GetPriorityClass`
        - `GetProcAddress`
        - `GetProcessId`
        - `GetProcessShutdownParameters`
        - `GetProcessTimes`
        - `GetProcessWorkingSetSizeEx`
        - `GetProtoByName`
        - `GetQueuedCompletionStatus`
        - `GetServByName`
        - `GetShortPathName`
        - `GetStdHandle`
        - `GetSystemTimeAsFileTime`
        - `GetSystemTimePreciseAsFileTime`
        - `GetTempPath`
        - `GetTimeZoneInformation`
        - `GetTokenInformation`
        - `GetUserNameEx`
        - `GetUserProfileDirectory`
        - `GetVersion`
        - `GetVolumeInformation`
        - `GetVolumeInformationByHandle`
        - `GetVolumeNameForVolumeMountPoint`
        - `GetVolumePathName`
        - `GetVolumePathNamesForVolumeName`
        - `Getsockopt`
        - `ImpersonateSelf`
        - `InitiateSystemShutdownEx`
        - `IsWow64Process`
        - `LoadLibrary`
        - `LoadLibraryEx`
        - `LocalFree`
        - `LockFileEx`
        - `LookupAccountName`
        - `LookupAccountSid`
        - `LookupPrivilegeValue`
        - `MapViewOfFile`
        - `MessageBox`
        - `MoveFile`
        - `MoveFileEx`
        - `MultiByteToWideChar`
        - `NetApiBufferFree`
        - `NetGetJoinInformation`
        - `NetUserGetInfo`
        - `NotifyServiceStatusChange`
        - `Ntohs`
        - `OpenEvent`
        - `OpenMutex`
        - `OpenProcess`
        - `OpenProcessToken`
        - `OpenSCManager`
        - `OpenService`
        - `OpenThread`
        - `OpenThreadToken`
        - `PostQueuedCompletionStatus`
        - `Process32First`
        - `Process32Next`
        - `ProcessIdToSessionId`
        - `PulseEvent`
        - `QueryDosDevice`
        - `QueryInformationJobObject`
        - `QueryServiceConfig`
        - `QueryServiceConfig2`
        - `QueryServiceLockStatus`
        - `QueryServiceStatus`
        - `QueryServiceStatusEx`
        - `ReadConsole`
        - `ReadDirectoryChanges`
        - `RegCloseKey`
        - `RegEnumKeyEx`
        - `RegOpenKeyEx`
        - `RegQueryInfoKey`
        - `RegQueryValueEx`
        - `RegisterEventSource`
        - `ReleaseMutex`
        - `RemoveDirectory`
        - `ReportEvent`
        - `ResetEvent`
        - `ResumeThread`
        - `RevertToSelf`
        - `SetConsoleMode`
        - `SetCurrentDirectory`
        - `SetEndOfFile`
        - `SetEnvironmentVariable`
        - `SetErrorMode`
        - `SetEvent`
        - `SetFileAttributes`
        - `SetFileCompletionNotificationModes`
        - `SetFilePointer`
        - `SetFileTime`
        - `SetHandleInformation`
        - `SetInformationJobObject`
        - `SetNamedSecurityInfo`
        - `SetPriorityClass`
        - `SetProcessPriorityBoost`
        - `SetProcessShutdownParameters`
        - `SetProcessWorkingSetSizeEx`
        - `SetSecurityInfo`
        - `SetServiceStatus`
        - `SetStdHandle`
        - `SetThreadToken`
        - `SetTokenInformation`
        - `SetVolumeLabel`
        - `SetVolumeMountPoint`
        - `Setsockopt`
        - `ShellExecute`
        - `SleepEx`
        - `StartService`
        - `StartServiceCtrlDispatcher`
        - `TerminateJobObject`
        - `TerminateProcess`
        - `Thread32First`
        - `Thread32Next`
        - `TranslateName`
        - `TransmitFile`
        - `UnlockFileEx`
        - `UnmapViewOfFile`
        - `VirtualAlloc`
        - `VirtualFree`
        - `VirtualLock`
        - `VirtualProtect`
        - `VirtualUnlock`
        - `WSACleanup`
        - `WSAEnumProtocols`
        - `WSAIoctl`
        - `WSARecv`
        - `WSARecvFrom`
        - `WSASend`
        - `WSASendTo`
        - `WSAStartup`
        - `WTSEnumerateSessions`
        - `WTSFreeMemory`
        - `WTSQueryUserToken`
        - `WaitForSingleObject`
        - `WriteConsole`
        - `_DnsQuery`
        - `_GetHostByName`
        - `_GetProcAddress`
        - `_GetProtoByName`
        - `_GetServByName`
        - `_LoadLibrary`
        - `_LoadLibraryEx`
        - `_SetNamedSecurityInfo`
        - `_convertStringSecurityDescriptorToSecurityDescriptor`
        - `_getNamedSecurityInfo`
        - `bind`
        - `buildSecurityDescriptor`
        - `checkTokenMembership`
        - `clsidFromString`
        - `coCreateGuid`
        - `connect`
        - `convertSecurityDescriptorToStringSecurityDescriptor`
        - `convertStringSecurityDescriptorToSecurityDescriptor`
        - `createWellKnownSid`
        - `errnoErr`
        - `findFirstFile1`
        - `findNextFile1`
        - `getNamedSecurityInfo`
        - `getProcessPreferredUILanguages`
        - `getSecurityDescriptorControl`
        - `getSecurityDescriptorDacl`
        - `getSecurityDescriptorGroup`
        - `getSecurityDescriptorLength`
        - `getSecurityDescriptorOwner`
        - `getSecurityDescriptorRMControl`
        - `getSecurityDescriptorSacl`
        - `getSecurityInfo`
        - `getSidIdentifierAuthority`
        - `getSidSubAuthority`
        - `getSidSubAuthorityCount`
        - `getSystemDirectory`
        - `getSystemPreferredUILanguages`
        - `getSystemWindowsDirectory`
        - `getThreadPreferredUILanguages`
        - `getTickCount64`
        - `getUserPreferredUILanguages`
        - `getWindowsDirectory`
        - `getpeername`
        - `getsockname`
        - `initializeSecurityDescriptor`
        - `isValidSecurityDescriptor`
        - `isValidSid`
        - `isWellKnownSid`
        - `listen`
        - `makeAbsoluteSD`
        - `makeSelfRelativeSD`
        - `recvfrom`
        - `rtlGetNtVersionNumbers`
        - `rtlGetVersion`
        - `sendto`
        - `setEntriesInAcl`
        - `setSecurityDescriptorControl`
        - `setSecurityDescriptorDacl`
        - `setSecurityDescriptorGroup`
        - `setSecurityDescriptorOwner`
        - `setSecurityDescriptorRMControl`
        - `setSecurityDescriptorSacl`
        - `shGetKnownFolderPath`
        - `shutdown`
        - `socket`
        - `stringFromGUID2`
        - `waitForMultipleObjects`
    - Predicted Functions (0):

- **File:** `src/runtime/defs_openbsd_mips64.go`
    - Ground Truth Functions (2):
        - `setNsec`
        - `set_usec`
    - Predicted Functions (0):

- **File:** `src/runtime/mheap.go`
    - Ground Truth Functions (1):
        - `allocSpan`
    - Predicted Functions (0):

- **File:** `src/runtime/os_openbsd.go`
    - Ground Truth Functions (4):
        - `mpreinit`
        - `osStackAlloc`
        - `osStackFree`
        - `osStackRemap`
    - Predicted Functions (0):

- **File:** `src/runtime/os_openbsd_mips64.go`
    - Ground Truth Functions (1):
        - `cputicks`
    - Predicted Functions (0):

- **File:** `src/runtime/signal_openbsd_mips64.go`
    - Ground Truth Functions (3):
        - `regs`
        - `set_sigaddr`
        - `sigaddr`
    - Predicted Functions (47):
        - ❌ `hi`
        - ❌ `link`
        - ❌ `lo`
        - ❌ `pc`
        - ❌ `r0`
        - ❌ `r1`
        - ❌ `r10`
        - ❌ `r11`
        - ❌ `r12`
        - ❌ `r13`
        - ❌ `r14`
        - ❌ `r15`
        - ❌ `r16`
        - ❌ `r17`
        - ❌ `r18`
        - ❌ `r19`
        - ❌ `r2`
        - ❌ `r20`
        - ❌ `r21`
        - ❌ `r22`
        - ❌ `r23`
        - ❌ `r24`
        - ❌ `r25`
        - ❌ `r26`
        - ❌ `r27`
        - ❌ `r28`
        - ❌ `r29`
        - ❌ `r3`
        - ❌ `r30`
        - ❌ `r31`
        - ❌ `r4`
        - ❌ `r5`
        - ❌ `r6`
        - ❌ `r7`
        - ❌ `r8`
        - ❌ `r9`
        - ✅ `regs`
        - ❌ `set_link`
        - ❌ `set_pc`
        - ❌ `set_r28`
        - ❌ `set_r30`
        - ✅ `set_sigaddr`
        - ❌ `set_sigcode`
        - ❌ `set_sp`
        - ✅ `sigaddr`
        - ❌ `sigcode`
        - ❌ `sp`

- **File:** `src/runtime/stack.go`
    - Ground Truth Functions (5):
        - `freeStackSpans`
        - `stackalloc`
        - `stackfree`
        - `stackpoolalloc`
        - `stackpoolfree`
    - Predicted Functions (0):

- **File:** `src/syscall/exec_bsd.go`
    - Ground Truth Functions (1):
        - `forkAndExecInChild`
    - Predicted Functions (0):

- **File:** `src/syscall/exec_unix_test.go`
    - Ground Truth Functions (1):
        - `TestForeground`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_openbsd_mips64.go`
    - Ground Truth Functions (5):
        - `SetControllen`
        - `SetKevent`
        - `SetLen`
        - `setTimespec`
        - `setTimeval`
    - Predicted Functions (4):
        - ✅ `SetKevent`
        - ✅ `SetLen`
        - ✅ `setTimespec`
        - ✅ `setTimeval`

- **File:** `src/syscall/zsyscall_openbsd_mips64.go`
    - Ground Truth Functions (103):
        - `Access`
        - `Adjtime`
        - `Chdir`
        - `Chflags`
        - `Chmod`
        - `Chown`
        - `Chroot`
        - `Close`
        - `Dup`
        - `Dup2`
        - `Fchdir`
        - `Fchflags`
        - `Fchmod`
        - `Fchown`
        - `Flock`
        - `Fpathconf`
        - `Fstat`
        - `Fstatfs`
        - `Fsync`
        - `Ftruncate`
        - `Getegid`
        - `Geteuid`
        - `Getgid`
        - `Getpgid`
        - `Getpgrp`
        - `Getpid`
        - `Getppid`
        - `Getpriority`
        - `Getrlimit`
        - `Getrusage`
        - `Getsid`
        - `Gettimeofday`
        - `Getuid`
        - `Issetugid`
        - `Kill`
        - `Kqueue`
        - `Lchown`
        - `Link`
        - `Listen`
        - `Lstat`
        - `Mkdir`
        - `Mkfifo`
        - `Mknod`
        - `Nanosleep`
        - `Open`
        - `Pathconf`
        - `Readlink`
        - `Rename`
        - `Revoke`
        - `Rmdir`
        - `Seek`
        - `Select`
        - `Setegid`
        - `Seteuid`
        - `Setgid`
        - `Setlogin`
        - `Setpgid`
        - `Setpriority`
        - `Setregid`
        - `Setreuid`
        - `Setsid`
        - `Settimeofday`
        - `Setuid`
        - `Shutdown`
        - `Stat`
        - `Statfs`
        - `Symlink`
        - `Sync`
        - `Truncate`
        - `Umask`
        - `Unlink`
        - `Unmount`
        - `accept`
        - `accept4`
        - `bind`
        - `connect`
        - `fcntl`
        - `futimes`
        - `getcwd`
        - `getdents`
        - `getgroups`
        - `getpeername`
        - `getsockname`
        - `getsockopt`
        - `kevent`
        - `mmap`
        - `munmap`
        - `pipe2`
        - `read`
        - `readlen`
        - `recvfrom`
        - `recvmsg`
        - `sendmsg`
        - `sendto`
        - `setgroups`
        - `setsockopt`
        - `socket`
        - `socketpair`
        - `sysctl`
        - `utimensat`
        - `utimes`
        - `wait4`
        - `write`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_arm64.go`
    - Ground Truth Functions (4):
        - `archInit`
        - `parseARM64SystemRegisters`
        - `readARM64Registers`
        - `setMinimalFeatures`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_linux_s390x.go`
    - Ground Truth Functions (1):
        - `initS390Xbase`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_netbsd_arm64.go`
    - Ground Truth Functions (5):
        - `doinit`
        - `nametomib`
        - `sysctl`
        - `sysctlCPUID`
        - `sysctlNodes`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_other_mips64x.go`
    - Ground Truth Functions (1):
        - `archInit`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_s390x.go`
    - Ground Truth Functions (4):
        - `Has`
        - `bitIsSet`
        - `doinit`
        - `initOptions`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_x86.go`
    - Ground Truth Functions (2):
        - `archInit`
        - `initOptions`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_zos.go`
    - Ground Truth Functions (1):
        - `archInit`
    - Predicted Functions (0):

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_zos_s390x.go`
    - Ground Truth Functions (1):
        - `initS390Xbase`
    - Predicted Functions (0):


### 📊 **Proposal #43931 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/13 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/gc/main.go`
    - Ground Truth Functions (1):
        - `Main`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/noder.go`
    - Ground Truth Functions (1):
        - `LoadPackage`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/staticdata/embed.go`
    - Ground Truth Functions (5):
        - `WriteEmbed`
        - `embedFileLess`
        - `embedFileList`
        - `embedFileNameSplit`
        - `embedKind`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (2):
        - `registerStdTest`
        - `registerTests`
    - Predicted Functions (0):

- **File:** `src/embed/internal/embedtest/embed_test.go`
    - Ground Truth Functions (3):
        - `TestDir`
        - `TestHidden`
        - `TestUninitialized`
    - Predicted Functions (0):

- **File:** `src/go/types/stdlib_test.go`
    - Ground Truth Functions (1):
        - `TestStdTest`
    - Predicted Functions (0):

- **File:** `src/go/types/typeparam.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Constraint`
        - ❌ `NewTypeParam`
        - ❌ `SetConstraint`
        - ❌ `String`
        - ❌ `Underlying`
        - ❌ `newTypeParam`


### 📊 **Proposal #50599 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 8.0% | 11.4% | 4/50 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/vcs/vcs.go`
    - Ground Truth Functions (1):
        - `run1`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (1):
        - `gccSupportsFlag`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/moddeps/moddeps_test.go`
    - Ground Truth Functions (4):
        - `TestAllDependencies`
        - `findGorootModules`
        - `makeGOROOTCopy`
        - `run`
    - Predicted Functions (0):

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (1):
        - `importGo`
    - Predicted Functions (0):

- **File:** `src/os/exec/env_test.go`
    - Ground Truth Functions (1):
        - `TestDedupEnv`
    - Predicted Functions (0):

- **File:** `src/os/exec/example_test.go`
    - Ground Truth Functions (1):
        - `ExampleCmd_Environ`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (5):
        - `Environ`
        - `Start`
        - `argv`
        - `dedupEnvCase`
        - `environ`
    - Predicted Functions (7):
        - ❌ `CombinedOutput`
        - ❌ `Command`
        - ❌ `CommandContext`
        - ✅ `Environ`
        - ❌ `Output`
        - ❌ `Run`
        - ✅ `Start`

- **File:** `src/os/exec/exec_linux_test.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_posix_test.go`
    - Ground Truth Functions (6):
        - `TestCredentialNoSetGroups`
        - `TestExplicitPWD`
        - `TestImplicitPWD`
        - `TestWaitid`
        - `cmdPwd`
        - `init`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (24):
        - `Read`
        - `TestCatGoodAndBadFile`
        - `TestClosePipeOnCopyError`
        - `TestCommandRelativeName`
        - `TestContextCancel`
        - `TestDedupEnvEcho`
        - `TestExtraFiles`
        - `TestExtraFilesRace`
        - `TestMain`
        - `TestString`
        - `cmdCat`
        - `cmdDescribeFiles`
        - `cmdEcho`
        - `cmdEchoEnv`
        - `cmdExit`
        - `cmdPipeTest`
        - `cmdStderrFail`
        - `cmdStdinClose`
        - `cmdYes`
        - `helperCommand`
        - `helperCommandContext`
        - `init`
        - `maySkipHelperCommand`
        - `registerHelperCommand`
    - Predicted Functions (6):
        - ✅ `TestCommandRelativeName`
        - ✅ `TestDedupEnvEcho`
        - ❌ `TestEcho`
        - ❌ `TestEnvNULCharacter`
        - ❌ `TestNoPath`
        - ❌ `TestStringPathNotResolved`

- **File:** `src/os/exec/exec_windows_test.go`
    - Ground Truth Functions (3):
        - `TestChildCriticalEnv`
        - `cmdPipeHandle`
        - `init`
    - Predicted Functions (0):

- **File:** `src/os/exec/internal/fdtest/exists_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/internal/fdtest/exists_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_windows_test.go`
    - Ground Truth Functions (2):
        - `init`
        - `installBat`
    - Predicted Functions (0):

- **File:** `src/syscall/exec_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `forkAndExecInChild`

- **File:** `src/syscall/exec_linux_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Exec`
        - ❌ `ForkExec`
        - ❌ `StartProcess`
        - ❌ `forkExec`

- **File:** `src/syscall/exec_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestExec`
        - ❌ `TestInvalidExec`


### 📊 **Proposal #53003 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 14.3% | 22.2% | 3/21 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/escape/expr.go`
    - Ground Truth Functions (1):
        - `exprSkipInit`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/expr.go`
    - Ground Truth Functions (1):
        - `SetOp`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/op_string.go`
    - Ground Truth Functions (1):
        - `_`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/reader.go`
    - Ground Truth Functions (1):
        - `expr`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/writer.go`
    - Ground Truth Functions (1):
        - `expr`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssagen/ssa.go`
    - Ground Truth Functions (2):
        - `softfloatInit`
        - `stmt`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/const.go`
    - Ground Truth Functions (1):
        - `callOrChan`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/func.go`
    - Ground Truth Functions (2):
        - `tcCall`
        - `tcUnsafeString`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/typecheck.go`
    - Ground Truth Functions (1):
        - `typecheck1`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/builtins.go`
    - Ground Truth Functions (1):
        - `builtin`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/builtin.go`
    - Ground Truth Functions (1):
        - `walkUnsafeString`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/walk/expr.go`
    - Ground Truth Functions (1):
        - `walkExpr1`
    - Predicted Functions (0):

- **File:** `src/go/types/builtins.go`
    - Ground Truth Functions (1):
        - `builtin`
    - Predicted Functions (0):

- **File:** `src/runtime/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `unsafeslice`
        - ❌ `unsafestring`

- **File:** `src/unsafe/unsafe.go`
    - Ground Truth Functions (3):
        - `SliceData`
        - `String`
        - `StringData`
    - Predicted Functions (4):
        - ❌ `Slice`
        - ✅ `SliceData`
        - ✅ `String`
        - ✅ `StringData`

- **File:** `test/unsafe_slice_data.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `test/unsafe_string.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `test/unsafebuiltins.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #50601 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 93.8% | 83.3% | 88.2% | 15/18 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/common.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/tar/reader.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/archive/tar/writer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/encoding/binary/binary.go`
    - Ground Truth Functions (3):
        - `AppendUint16`
        - `AppendUint32`
        - `AppendUint64`
    - Predicted Functions (4):
        - ✅ `AppendUint16`
        - ✅ `AppendUint32`
        - ✅ `AppendUint64`
        - ❌ `String`

- **File:** `src/encoding/binary/binary_test.go`
    - Ground Truth Functions (15):
        - `BenchmarkAppendUint16`
        - `BenchmarkAppendUint32`
        - `BenchmarkAppendUint64`
        - `BenchmarkLittleEndianAppendUint16`
        - `BenchmarkLittleEndianAppendUint32`
        - `BenchmarkLittleEndianAppendUint64`
        - `BenchmarkLittleEndianPutUint16`
        - `BenchmarkLittleEndianPutUint32`
        - `BenchmarkLittleEndianPutUint64`
        - `BenchmarkPutUint16`
        - `BenchmarkPutUint32`
        - `BenchmarkPutUint64`
        - `BenchmarkReadInts`
        - `BenchmarkWriteInts`
        - `TestByteOrder`
    - Predicted Functions (12):
        - ✅ `BenchmarkAppendUint16`
        - ✅ `BenchmarkAppendUint32`
        - ✅ `BenchmarkAppendUint64`
        - ✅ `BenchmarkLittleEndianAppendUint16`
        - ✅ `BenchmarkLittleEndianAppendUint32`
        - ✅ `BenchmarkLittleEndianAppendUint64`
        - ✅ `BenchmarkLittleEndianPutUint16`
        - ✅ `BenchmarkLittleEndianPutUint32`
        - ✅ `BenchmarkLittleEndianPutUint64`
        - ✅ `BenchmarkPutUint16`
        - ✅ `BenchmarkPutUint32`
        - ✅ `BenchmarkPutUint64`


### 📊 **Proposal #38248 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/24 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/gc/compile.go`
    - Ground Truth Functions (1):
        - `enqueueFunc`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ir/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/noder/noder.go`
    - Ground Truth Functions (1):
        - `pragma`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssagen/abi.go`
    - Ground Truth Functions (1):
        - `CreateWasmImportWrapper`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/objfile.go`
    - Ground Truth Functions (3):
        - `Aux`
        - `genFuncInfoSyms`
        - `nAuxSym`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/plist.go`
    - Ground Truth Functions (2):
        - `Flushplist`
        - `InitTextSym`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/sym.go`
    - Ground Truth Functions (1):
        - `traverseFuncAux`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/wasm/wasmobj.go`
    - Ground Truth Functions (3):
        - `assemble`
        - `instinit`
        - `preprocess`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/wasm/asm.go`
    - Ground Truth Functions (9):
        - `asmb`
        - `asmb2`
        - `assignAddress`
        - `fieldsToTypes`
        - `lookupType`
        - `readWasmImport`
        - `writeImportSec`
        - `writeSecHeader`
        - `writeTypeSec`
    - Predicted Functions (0):

- **File:** `src/syscall/js/js_test.go`
    - Ground Truth Functions (2):
        - `TestWasmImport`
        - `testAdd`
    - Predicted Functions (0):


### 📊 **Proposal #37519 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/modfetch/repo.go`
    - Ground Truth Functions (1):
        - `lookupDirect`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/sumdb.go`
    - Ground Truth Functions (1):
        - `useSumDB`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modget/get.go`
    - Ground Truth Functions (1):
        - `runGet`
    - Predicted Functions (0):


### 📊 **Proposal #37255 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 11.1% | 13.3% | 1/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/context/context.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `WithCancel`
        - ❌ `WithDeadline`
        - ❌ `WithTimeout`
        - ❌ `WithValue`

- **File:** `src/context/context_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `XTestCancelRemoves`

- **File:** `src/os/signal/example_unix_test.go`
    - Ground Truth Functions (1):
        - `ExampleNotifyContext`
    - Predicted Functions (0):

- **File:** `src/os/signal/signal.go`
    - Ground Truth Functions (3):
        - `NotifyContext`
        - `String`
        - `stop`
    - Predicted Functions (1):
        - ✅ `NotifyContext`

- **File:** `src/os/signal/signal_test.go`
    - Ground Truth Functions (5):
        - `TestNotifyContextCancelParent`
        - `TestNotifyContextPrematureCancelParent`
        - `TestNotifyContextSimultaneousStop`
        - `TestNotifyContextStop`
        - `TestNotifyContextStringer`
    - Predicted Functions (0):


### 📊 **Proposal #45428 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`


### 📊 **Proposal #48801 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat`
- `src/cmd/vet`

**Predicted Directories (3):**
- ❌ `src/runtime`
- ❌ `src/time`
- ❌ `src/vet`


### 📊 **Proposal #34875 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/doc`

**Predicted Directories (3):**
- ❌ `doc`
- ✅ `src/go/doc`
- ❌ `src/net/http`


### 📊 **Proposal #32716 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`


### 📊 **Proposal #51777 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/netip`

**Predicted Directories (3):**
- ❌ `fix`
- ❌ `src/net`
- ✅ `src/net/netip`


### 📊 **Proposal #47164 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/log`

**Predicted Directories (1):**
- ✅ `src/log`


### 📊 **Proposal #42710 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/hash/maphash`

**Predicted Directories (1):**
- ✅ `src/hash/maphash`


### 📊 **Proposal #46259 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (5):**
- ❌ `internal/runtime/sys`
- ❌ `src/os/exec`
- ❌ `src/os/exec/internal/fdtest`
- ❌ `src/sys`
- ✅ `src/syscall`


### 📊 **Proposal #47257 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/11 |

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

**Predicted Directories (7):**
- ❌ `src/net/http`
- ❌ `src/net/http/cookiejar`
- ❌ `src/net/http/httptest`
- ❌ `src/net/http/httptrace`
- ❌ `src/net/http/httputil`
- ❌ `src/net/http/pprof`
- ❌ `src/syscall`


### 📊 **Proposal #47216 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (3):**
- ❌ `internal/runtime`
- ✅ `src/runtime`
- ❌ `src/runtime/metrics`


### 📊 **Proposal #53747 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (3):**
- ❌ `go/internal/cmdflag`
- ✅ `src/flag`
- ❌ `testing`


### 📊 **Proposal #34974 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/archive/zip`

**Predicted Directories (2):**
- ✅ `src/archive/zip`
- ❌ `src/compress/zip`


### 📊 **Proposal #34626 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (2):**
- ❌ `src/cmd/internal/objfile`
- ✅ `src/testing`


### 📊 **Proposal #48530 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (3):**
- ❌ `src`
- ✅ `src/net`
- ❌ `src/poll`


### 📊 **Proposal #50102 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/archive/tar`

**Predicted Directories (1):**
- ✅ `src/archive/tar`


### 📊 **Proposal #38687 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/go/internal/generate`

**Predicted Directories (1):**
- ❌ `go/internal/generate`


### 📊 **Proposal #50062 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (2):**
- ❌ `src/runtime`
- ✅ `src/time`


### 📊 **Proposal #46731 (Directory Level)**

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
- ❌ `internal/runtime/sys`
- ❌ `src/cmd/compile/internal/objabi`
- ❌ `src/cmd/compile/internal/objfile`
- ❌ `src/cmd/compile/internal/osinfo`
- ❌ `src/cmd/compile/internal/robustio`
- ❌ `src/cmd/compile/internal/telemetry`
- ❌ `src/cmd/compile/internal/telemetry/counter`
- ✅ `src/runtime`
- ❌ `src/runtime/cgo`
- ❌ `src/runtime/internal/sys`
- ❌ `src/runtime/sys`
- ✅ `test`


### 📊 **Proposal #33184 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/time`

**Predicted Directories (3):**
- ❌ `lib/time`
- ✅ `src/runtime`
- ✅ `src/time`


### 📊 **Proposal #50489 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/math/big`

**Predicted Directories (1):**
- ✅ `src/math/big`


### 📊 **Proposal #47342 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/dist`
- `src/hash/maphash`

**Predicted Directories (1):**
- ✅ `src/hash/maphash`


### 📊 **Proposal #37255 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os/signal`

**Predicted Directories (3):**
- ❌ `doc`
- ❌ `src/context`
- ✅ `src/os/signal`


### 📊 **Proposal #42502 (Directory Level)**

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


### 📊 **Proposal #42782 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (2):**
- ❌ `interface`
- ✅ `src/reflect`


### 📊 **Proposal #38248 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 12.5% | 16.7% | 1/8 |

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

**Predicted Directories (4):**
- ❌ `src/cmd/compile/internal/wasm`
- ❌ `src/compile/internal/abi`
- ✅ `src/syscall/js`
- ❌ `src/wasm`


### 📊 **Proposal #46279 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/link/internal/ld`

**Predicted Directories (6):**
- ❌ `internal/runtime/sys`
- ❌ `src/runtime`
- ❌ `src/runtime/sys`
- ❌ `src/sys`
- ❌ `src/sys/unix`
- ❌ `src/syscall`


### 📊 **Proposal #40724 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 4.4% | 7.3% | 2/45 |

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

**Predicted Directories (10):**
- ❌ `cmd/asm`
- ❌ `cmd/compile`
- ❌ `cmd/link`
- ❌ `runtime`
- ❌ `src/cmd/compile`
- ❌ `src/compile/internal/abi`
- ✅ `src/internal/abi`
- ✅ `src/runtime`
- ❌ `src/runtime/pprof`
- ❌ `test/abi`


### 📊 **Proposal #51914 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (2):**
- ❌ `src/net/http`
- ✅ `src/net/http/httputil`


### 📊 **Proposal #40481 (Directory Level)**

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


### 📊 **Proposal #46552 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/syscall`

**Predicted Directories (5):**
- ✅ `src/runtime`
- ❌ `src/runtime/syscall`
- ❌ `src/runtime/syscall/windows`
- ❌ `src/sys`
- ✅ `src/syscall`


### 📊 **Proposal #33136 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (4):**
- ❌ `interface`
- ❌ `src/encoding/json`
- ❌ `src/encoding/json/internal/jsonwire`
- ✅ `src/reflect`


### 📊 **Proposal #52221 (Directory Level)**

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


### 📊 **Proposal #44853 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 8.3% | 10.5% | 1/12 |

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

**Predicted Directories (7):**
- ❌ `cmd/dist`
- ❌ `runtime`
- ❌ `src/crypto`
- ❌ `src/internal/asan`
- ✅ `src/runtime`
- ❌ `src/runtime/asan`
- ❌ `src/runtime/msan`


### 📊 **Proposal #50599 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 20.0% | 25.0% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/go/internal/vcs`
- `src/cmd/go/internal/work`
- `src/cmd/internal/moddeps`
- `src/go/build`
- `src/os/exec`

**Predicted Directories (3):**
- ✅ `src/os/exec`
- ❌ `src/os/exec/internal/fdtest`
- ❌ `src/syscall`


### 📊 **Proposal #42537 (Directory Level)**

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
- ✅ `src/strings`
- ❌ `src/testing`
- ❌ `src/testing/fstest`
- ✅ `test`


### 📊 **Proposal #40995 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 28.6% | 26.7% | 2/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/dist`
- `src/cmd/link/internal/mips64`
- `src/cmd/vendor/golang.org/x/sys/unix`
- `src/cmd/vendor/golang.org/x/sys/windows`
- `src/runtime`
- `src/syscall`
- `src/vendor/golang.org/x/sys/cpu`

**Predicted Directories (8):**
- ❌ `src/compile/internal/abi`
- ❌ `src/compile/internal/mips/mips64`
- ❌ `src/os`
- ✅ `src/runtime`
- ❌ `src/runtime/cpu`
- ❌ `src/sys`
- ✅ `src/syscall`
- ❌ `src/syscall/unix`


### 📊 **Proposal #39034 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (3):**
- ❌ `lib/time`
- ❌ `src/fmt`
- ✅ `src/time`


### 📊 **Proposal #45100 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (2):**
- ❌ `src/net`
- ✅ `src/net/url`


### 📊 **Proposal #47005 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (1):**
- ✅ `src/net/url`


### 📊 **Proposal #53482 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (5):**
- ❌ `net`
- ❌ `src`
- ✅ `src/net`
- ❌ `src/syscall`
- ❌ `syscall`


### 📊 **Proposal #37112 (Directory Level)**

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
- ❌ `src`
- ✅ `src/runtime`
- ✅ `src/runtime/metrics`


### 📊 **Proposal #46771 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/mime/multipart`

**Predicted Directories (1):**
- ✅ `src/mime/multipart`


### 📊 **Proposal #48424 (Directory Level)**

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

**Predicted Directories (2):**
- ❌ `src/maps`
- ❌ `typeparam`


### 📊 **Proposal #46485 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 20.0% | 33.3% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/cgo`
- `src/cmd/go/internal/load`
- `src/cmd/gofmt`
- `src/go/internal/srcimporter`
- `src/go/parser`

**Predicted Directories (1):**
- ✅ `src/go/parser`


### 📊 **Proposal #34652 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 3/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/html/template`
- `src/text/template`
- `src/text/template/parse`

**Predicted Directories (3):**
- ✅ `src/html/template`
- ✅ `src/text/template`
- ✅ `src/text/template/parse`


### 📊 **Proposal #42098 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (2):**
- ❌ `src/os/exec`
- ✅ `src/syscall`


### 📊 **Proposal #35998 (Directory Level)**

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


### 📊 **Proposal #43698 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/embed`
- `src/embed/internal/embedtest`

**Predicted Directories (2):**
- ❌ `cmd/vet`
- ❌ `src/cmd/vet`


### 📊 **Proposal #51414 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (2):**
- ❌ `lib`
- ✅ `src/time`


### 📊 **Proposal #37023 (Directory Level)**

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


### 📊 **Proposal #46258 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (5):**
- ❌ `go/internal/base`
- ❌ `src/os/exec`
- ❌ `src/os/signal`
- ❌ `src/sys`
- ✅ `src/syscall`


### 📊 **Proposal #51430 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 6.7% | 8.0% | 1/15 |

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

**Predicted Directories (10):**
- ✅ `src/cmd/compile/internal/coverage`
- ❌ `src/cmd/cover`
- ❌ `src/cmd/cover/testdata/html`
- ❌ `src/cmd/cover/testdata/pkgcfg/a`
- ❌ `src/cmd/cover/testdata/pkgcfg/noFuncsNoTests`
- ❌ `src/cmd/cover/testdata/pkgcfg/yesFuncsNoTests`
- ❌ `src/coverage`
- ❌ `src/coverage/test`
- ❌ `src/runtime/coverage`
- ❌ `src/testing`


### 📊 **Proposal #46308 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`


### 📊 **Proposal #37033 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/link/internal/ld`
- `src/runtime/cgo`

**Predicted Directories (2):**
- ❌ `src/runtime`
- ✅ `src/runtime/cgo`


### 📊 **Proposal #51766 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/netip`

**Predicted Directories (2):**
- ❌ `src/net`
- ✅ `src/net/netip`


### 📊 **Proposal #51684 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/regexp/syntax`

**Predicted Directories (2):**
- ❌ `src/regexp`
- ✅ `src/regexp/syntax`


### 📊 **Proposal #51896 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/unicode/utf16`

**Predicted Directories (1):**
- ✅ `src/unicode/utf16`


### 📊 **Proposal #42088 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/run`
- `src/cmd/go/internal/work`

**Predicted Directories (0):**


### 📊 **Proposal #19367 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (2):**
- ❌ `src`
- ❌ `src/unsafe`


### 📊 **Proposal #37168 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/rc4`
- `src/image`

**Predicted Directories (16):**
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
- ❌ `src/math/big/internal/asmgen`
- ❌ `vendor/golang.org/x/crypto/chacha20`
- ❌ `vendor/golang.org/x/crypto/chacha20poly1305`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305`


### 📊 **Proposal #29062 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/test`
- `src/cmd/objdump`
- `src/internal/testenv`

**Predicted Directories (3):**
- ❌ `src/os`
- ❌ `src/os/exec`
- ❌ `src/testing`


### 📊 **Proposal #43823 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (2):**
- ❌ `src/strconv`
- ✅ `src/time`


### 📊 **Proposal #48157 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/internal/fuzz`
- `src/internal/testenv`
- `src/runtime`

**Predicted Directories (0):**


### 📊 **Proposal #32779 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/json`

**Predicted Directories (2):**
- ✅ `src/encoding/json`
- ❌ `src/encoding/json/jsontext`


### 📊 **Proposal #46131 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (6):**
- ❌ `interface`
- ✅ `src/reflect`
- ❌ `src/runtime/maps`
- ❌ `src/types`
- ❌ `test`
- ❌ `test/stress`


### 📊 **Proposal #51225 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/compile/internal/base`
- `src/cmd/compile/internal/noder`
- `src/cmd/go/internal/work`

**Predicted Directories (6):**
- ❌ `cmd/compile`
- ❌ `cmd/compile/flags`
- ❌ `cmd/compile/internal/importer`
- ❌ `src/cmd/compile/internal/objabi`
- ❌ `src/cmd/compile/internal/objfile`
- ❌ `src/go/build`


### 📊 **Proposal #40025 (Directory Level)**

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


### 📊 **Proposal #47527 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/bufio`

**Predicted Directories (1):**
- ✅ `src/bufio`


### 📊 **Proposal #37974 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/ast`

**Predicted Directories (3):**
- ❌ `src/go`
- ❌ `src/go/doc`
- ❌ `src/runtime`


### 📊 **Proposal #37776 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (3):**
- ❌ `src/net`
- ✅ `src/net/url`
- ❌ `web`


### 📊 **Proposal #40357 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/list`
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modload`

**Predicted Directories (1):**
- ❌ `cmd/go`


### 📊 **Proposal #39557 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (3):**
- ❌ `go/internal/cmdflag`
- ❌ `src/cmd/internal/objabi`
- ✅ `src/flag`


### 📊 **Proposal #35804 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/database/sql`

**Predicted Directories (1):**
- ✅ `src/database/sql`


### 📊 **Proposal #53003 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 10.0% | 16.7% | 1/10 |

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
- ❌ `src/runtime`
- ✅ `src/unsafe`


### 📊 **Proposal #40281 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag`
- `src/reflect`

**Predicted Directories (3):**
- ❌ `src/cmd/vet/testdata/structtag`
- ❌ `src/encoding/json`
- ✅ `src/reflect`


### 📊 **Proposal #41563 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 16.7% | 25.0% | 1/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/encoding/asn1`
- `src/encoding/json`
- `src/encoding/xml`
- `src/net/rpc`
- `src/reflect`
- `src/text/template`

**Predicted Directories (2):**
- ✅ `src/reflect`
- ❌ `src/reflectlite`


### 📊 **Proposal #46121 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/html/template`

**Predicted Directories (2):**
- ✅ `src/html/template`
- ❌ `src/text/template`


### 📊 **Proposal #43947 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/dist`
- `src/os/exec`

**Predicted Directories (4):**
- ❌ `src/cmd/internal/objabi`
- ✅ `src/os/exec`
- ❌ `src/syscall`
- ❌ `src/syscall/execenv/windows`


### 📊 **Proposal #50860 (Directory Level)**

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


### 📊 **Proposal #52444 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (1):**
- ✅ `src/crypto/x509`


### 📊 **Proposal #43724 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/syscall/windows`
- `src/syscall`

**Predicted Directories (4):**
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/os`
- ❌ `src/os/exec`


### 📊 **Proposal #41730 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/go`
- `src/cmd/go/internal/envcmd`
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modget`
- `src/cmd/go/internal/vcs`

**Predicted Directories (2):**
- ❌ `go/internal/modfetch/codehost`
- ❌ `go/internal/vcs`


### 📊 **Proposal #51668 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/fmt`

**Predicted Directories (2):**
- ✅ `src/fmt`
- ❌ `src/types`


### 📊 **Proposal #41980 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/diff`
- `src/testing`

**Predicted Directories (2):**
- ❌ `src/cmp`
- ✅ `src/testing`


### 📊 **Proposal #41792 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (4):**
- ❌ `src/cmd/internal/objabi`
- ✅ `src/flag`
- ❌ `test/fixedbugs`
- ❌ `testing`


### 📊 **Proposal #45453 (Directory Level)**

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

**Predicted Directories (0):**


### 📊 **Proposal #40276 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/work`

**Predicted Directories (0):**


### 📊 **Proposal #42322 (Directory Level)**

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


### 📊 **Proposal #42100 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 25.0% | 22.2% | 1/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `misc/ios`
- `src/cmd/dist`
- `src/cmd/go/internal/work`
- `src/cmd/link/internal/ld`

**Predicted Directories (5):**
- ✅ `misc/ios`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/go/goos`
- ❌ `src/runtime`
- ❌ `src/syscall`


### 📊 **Proposal #37475 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 44.4% | 38.1% | 4/9 |

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

**Predicted Directories (12):**
- ❌ `cmd/go/internal/load`
- ❌ `cmd/go/internal/modfetch/codehost`
- ❌ `cmd/go/internal/version`
- ❌ `cmd/go/internal/work`
- ❌ `runtime/debug`
- ✅ `src/cmd/go/internal/load`
- ✅ `src/cmd/go/internal/version`
- ✅ `src/cmd/go/internal/work`
- ❌ `src/go/internal/load`
- ❌ `src/go/internal/version`
- ❌ `src/go/internal/work`
- ✅ `src/runtime/debug`


### 📊 **Proposal #39567 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/net/http`


### 📊 **Proposal #44808 (Directory Level)**

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


### 📊 **Proposal #45754 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (7):**
- ❌ `go/internal/cmdflag`
- ❌ `src/encoding`
- ✅ `src/flag`
- ❌ `src/math/big`
- ❌ `src/net`
- ❌ `src/testing`
- ❌ `src/time`


### 📊 **Proposal #47651 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 4.8% | 8.3% | 1/21 |

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

**Predicted Directories (3):**
- ❌ `interface`
- ✅ `src/reflect`
- ❌ `src/runtime/reflectlite`


### 📊 **Proposal #48052 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/debug/plan9obj`

**Predicted Directories (2):**
- ❌ `src/debug/elf`
- ✅ `src/debug/plan9obj`


### 📊 **Proposal #33920 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/io/ioutil`
- `src/os`

**Predicted Directories (2):**
- ✅ `src/io/ioutil`
- ❌ `src/path/filepath`


### 📊 **Proposal #47209 (Directory Level)**

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


### 📊 **Proposal #48152 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/tls`
- `src/net/http`

**Predicted Directories (3):**
- ✅ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/testtls`


### 📊 **Proposal #41682 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (1):**
- ✅ `src/crypto/x509`


### 📊 **Proposal #53200 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/token`

**Predicted Directories (1):**
- ✅ `src/go/token`


### 📊 **Proposal #40082 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/database/sql`

**Predicted Directories (2):**
- ✅ `src/database/sql`
- ❌ `src/database/sql/driver`


### 📊 **Proposal #45963 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/test`
- `src/cmd/go/internal/work`

**Predicted Directories (20):**
- ❌ `src/cmd/go/analysis/internal/analysisflags`
- ❌ `src/cmd/go/analysis/passes/assign`
- ❌ `src/cmd/go/analysis/passes/atomic`
- ❌ `src/cmd/go/analysis/passes/cgocall`
- ❌ `src/cmd/go/analysis/passes/composite`
- ❌ `src/cmd/go/analysis/passes/defers`
- ❌ `src/cmd/go/analysis/passes/hostport`
- ❌ `src/cmd/go/analysis/passes/httpresponse`
- ❌ `src/cmd/go/analysis/passes/ifaceassert`
- ❌ `src/cmd/go/analysis/passes/loopclosure`
- ❌ `src/cmd/go/analysis/passes/lostcancel`
- ❌ `src/cmd/go/analysis/passes/nilfunc`
- ❌ `src/cmd/go/analysis/passes/print`
- ❌ `src/cmd/go/analysis/passes/printf`
- ❌ `src/cmd/go/analysis/passes/shift`
- ❌ `src/cmd/go/analysis/passes/sigchanyzer`
- ❌ `src/cmd/go/analysis/passes/structtag`
- ❌ `src/cmd/go/analysis/passes/testinggoroutine`
- ❌ `src/cmd/go/analysis/passes/unusedresult`
- ❌ `src/cmd/vet`


### 📊 **Proposal #46518 (Directory Level)**

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


### 📊 **Proposal #40337 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (4):**
- ❌ `src/crypto/dsa`
- ✅ `src/crypto/x509`
- ❌ `vendor/golang.org/x/crypto/ssh`
- ❌ `vendor/golang.org/x/crypto/x509`


### 📊 **Proposal #45973 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (3):**
- ✅ `src/net/http`
- ❌ `vendor/golang.org/x/net/http`
- ❌ `vendor/golang.org/x/net/http/httpguts`


### 📊 **Proposal #49471 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (4):**
- ❌ `internal/runtime`
- ✅ `src/runtime`
- ❌ `src/runtime/syscall`
- ❌ `src/syscall`


### 📊 **Proposal #52746 (Directory Level)**

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


### 📊 **Proposal #34293 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/doc`

**Predicted Directories (7):**
- ❌ `cmd/go`
- ❌ `go/doc`
- ❌ `internal/lsp/cmd`
- ❌ `internal/lsp/source`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/doc`
- ❌ `src/go/doc`


### 📊 **Proposal #31804 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/ed25519`

**Predicted Directories (1):**
- ✅ `src/crypto/ed25519`


### 📊 **Proposal #43744 (Directory Level)**

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


### 📊 **Proposal #47916 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 2.9% | 33.3% | 5.3% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/types2`
- `src/go/types`

**Predicted Directories (35):**
- ✅ `src/go/types`
- ❌ `src/types`
- ❌ `src/types/types2`
- ❌ `typeparam/absdiffimp.dir`
- ❌ `typeparam/aliasimp.dir`
- ❌ `typeparam/chansimp.dir`
- ❌ `typeparam/dedup.dir`
- ❌ `typeparam/factimp.dir`
- ❌ `typeparam/gencrawler.dir`
- ❌ `typeparam/geninline.dir`
- ❌ `typeparam/issue46461b.dir`
- ❌ `typeparam/issue47514c.dir`
- ❌ `typeparam/issue47892.dir`
- ❌ `typeparam/issue48094.dir`
- ❌ `typeparam/issue50121.dir`
- ❌ `typeparam/issue50437.dir`
- ❌ `typeparam/issue50481b.dir`
- ❌ `typeparam/issue50481c.dir`
- ❌ `typeparam/issue50552.dir`
- ❌ `typeparam/issue50561.dir`
- ❌ `typeparam/issue50598.dir`
- ❌ `typeparam/issue50841.dir`
- ❌ `typeparam/issue51219.dir`
- ❌ `typeparam/issue51219b.dir`
- ❌ `typeparam/issue51250a.dir`
- ❌ `typeparam/issue51367.dir`
- ❌ `typeparam/issue51423.dir`
- ❌ `typeparam/issue51836.dir`
- ❌ `typeparam/issue52117.dir`
- ❌ `typeparam/issue54302.dir`
- ❌ `typeparam/listimp.dir`
- ❌ `typeparam/mapimp.dir`
- ❌ `typeparam/mapsimp.dir`
- ❌ `typeparam/orderedmapsimp.dir`
- ❌ `typeparam/valimp.dir`


### 📊 **Proposal #40356 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods`

**Predicted Directories (5):**
- ❌ `cmd/vet`
- ❌ `src/cmd/vet`
- ❌ `src/cmd/vet/testdata/stdmethods`
- ❌ `src/errors`
- ❌ `src/fmt`


### 📊 **Proposal #40034 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/smtp`

**Predicted Directories (1):**
- ✅ `src/net/smtp`


### 📊 **Proposal #53002 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (1):**
- ✅ `src/net/http/httputil`


### 📊 **Proposal #44196 (Directory Level)**

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


### 📊 **Proposal #50465 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (2):**
- ❌ `src/net/http/httpproxy`
- ✅ `src/net/http/httputil`


### 📊 **Proposal #41696 (Directory Level)**

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

**Predicted Directories (2):**
- ❌ `cmd`
- ❌ `src/go/build`


### 📊 **Proposal #46336 (Directory Level)**

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


### 📊 **Proposal #44011 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 100.0% | 75.0% | 3/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/os`
- `src/os/exec`
- `src/syscall`

**Predicted Directories (5):**
- ✅ `src/os`
- ✅ `src/os/exec`
- ❌ `src/os/exec/internal/fdtest`
- ❌ `src/sys`
- ✅ `src/syscall`


### 📊 **Proposal #43620 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (1):**
- ✅ `src/testing`


### 📊 **Proposal #48256 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go`
- `src/cmd/go/internal/workcmd`

**Predicted Directories (2):**
- ❌ `go/work`
- ❌ `src/mod/internal/modfile`


### 📊 **Proposal #38017 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/time`
- `src/time/tzdata`

**Predicted Directories (2):**
- ❌ `lib/time`
- ✅ `src/time/tzdata`


### 📊 **Proposal #50601 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/binary`

**Predicted Directories (2):**
- ❌ `src/archive/tar`
- ✅ `src/encoding/binary`


### 📊 **Proposal #50842 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (1):**
- ✅ `src/io`


### 📊 **Proposal #41790 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/database/sql`

**Predicted Directories (2):**
- ✅ `src/database/sql`
- ❌ `src/database/sql/driver`


### 📊 **Proposal #5901 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/json`

**Predicted Directories (2):**
- ✅ `src/encoding/json`
- ❌ `src/syscall/js`


### 📊 **Proposal #52792 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modload`

**Predicted Directories (1):**
- ❌ `src/cmd/go/internal/modinfo`


### 📊 **Proposal #28308 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/23 |

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

**Predicted Directories (3):**
- ❌ `src`
- ❌ `src/cmd/vet/hostport`
- ❌ `src/net`


### 📊 **Proposal #44006 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall/js`

**Predicted Directories (1):**
- ✅ `src/syscall/js`


### 📊 **Proposal #53021 (Directory Level)**

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


### 📊 **Proposal #49580 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 25.0% | 28.6% | 1/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `src/archive/tar`
- `src/io/fs`
- `src/os`
- `src/testing/fstest`

**Predicted Directories (3):**
- ❌ `src/archive/zip`
- ✅ `src/io/fs`
- ❌ `src/path/filepath`


### 📊 **Proposal #53015 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/html/template`
- `src/text/template`
- `src/text/template/parse`

**Predicted Directories (3):**
- ❌ `interface`
- ✅ `src/html/template`
- ✅ `src/text/template`


### 📊 **Proposal #41048 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (3):**
- ✅ `src/net/http`
- ❌ `vendor/golang.org/x/net/http/httpguts`
- ❌ `vendor/golang.org/x/net/http/httpproxy`


### 📊 **Proposal #48409 (Directory Level)**

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


### 📊 **Proposal #42102 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (1):**
- ✅ `src/time`


### 📊 **Proposal #39904 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (1):**
- ✅ `src/testing`


### 📊 **Proposal #42027 (Directory Level)**

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
- ❌ `src/fmt`
- ✅ `src/io/fs`
- ✅ `src/path/filepath`


### 📊 **Proposal #27628 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/cache`
- `src/cmd/go/internal/work`

**Predicted Directories (0):**


### 📊 **Proposal #51868 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/debug/pe`

**Predicted Directories (2):**
- ✅ `src/debug/pe`
- ❌ `src/runtime/debug`


### 📊 **Proposal #28089 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/ast`

**Predicted Directories (2):**
- ✅ `src/go/ast`
- ❌ `src/go/parser`


### 📊 **Proposal #41773 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/net/http`


### 📊 **Proposal #50674 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (5):**
- ✅ `src/crypto/x509`
- ❌ `src/crypto/x509/pkix`
- ❌ `vendor/golang.org/x/crypto/cryptobyte`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/asn1`
- ❌ `vendor/golang.org/x/crypto/x509/pkix`


### 📊 **Proposal #26535 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/compress/lzw`

**Predicted Directories (1):**
- ✅ `src/compress/lzw`


### 📊 **Proposal #45964 (Directory Level)**

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


### 📊 **Proposal #39444 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os`

**Predicted Directories (3):**
- ✅ `src/os`
- ❌ `src/os/exec`
- ❌ `src/os/signal`


### 📊 **Proposal #45430 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (2):**
- ✅ `src/crypto/tls`
- ❌ `src/testtls`


### 📊 **Proposal #37533 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (7):**
- ❌ `cmd`
- ❌ `internal/cmdflag`
- ❌ `src/cmd/internal/objabi`
- ✅ `src/flag`
- ❌ `src/os/exec`
- ❌ `src/testing`
- ❌ `test/fixedbugs`


### 📊 **Proposal #47781 (Directory Level)**

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
- ❌ `src/go/ast/inspector`
- ❌ `src/go/token`
- ❌ `src/go/types/objectpath`
- ❌ `src/go/types/typeutil`


### 📊 **Proposal #46057 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (2):**
- ✅ `src/crypto/x509`
- ❌ `src/reflect`


### 📊 **Proposal #43401 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/csv`

**Predicted Directories (1):**
- ✅ `src/encoding/csv`


### 📊 **Proposal #40728 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

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
- ❌ `cmd/go/modload`


### 📊 **Proposal #43993 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/reflect`
- `src/text/template`

**Predicted Directories (2):**
- ❌ `interface`
- ✅ `src/reflect`


### 📊 **Proposal #50770 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (2):**
- ❌ `src/runtime`
- ✅ `src/time`


### 📊 **Proposal #44221 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/csv`

**Predicted Directories (5):**
- ❌ `src/archive/tar`
- ❌ `src/archive/zip`
- ❌ `src/bufio`
- ❌ `src/bytes`
- ✅ `src/encoding/csv`


### 📊 **Proposal #44143 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (1):**
- ❌ `src/context`


### 📊 **Proposal #43931 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 16.7% | 22.2% | 1/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/cmd/compile/internal/gc`
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/staticdata`
- `src/cmd/dist`
- `src/embed/internal/embedtest`
- `src/go/types`

**Predicted Directories (3):**
- ❌ `src/compile/internal/types2`
- ✅ `src/go/types`
- ❌ `typeparam`


### 📊 **Proposal #48294 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`


### 📊 **Proposal #51428 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (2):**
- ❌ `src/context`
- ✅ `src/net`


### 📊 **Proposal #52463 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/gofmt`

**Predicted Directories (3):**
- ❌ `src/go/ast`
- ❌ `src/go/parser`
- ❌ `src/go/types`


### 📊 **Proposal #51115 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (2):**
- ✅ `src/io`
- ❌ `src/net/http`


### 📊 **Proposal #35567 (Directory Level)**

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


### 📊 **Proposal #40255 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 11.1% | 12.5% | 1/9 |

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

**Predicted Directories (7):**
- ❌ `src/compile/internal`
- ❌ `src/compile/internal/abi`
- ✅ `src/runtime`
- ❌ `src/runtime/atomic`
- ❌ `src/runtime/goarch`
- ❌ `src/runtime/syscall`
- ❌ `src/syscall`


### 📊 **Proposal #46648 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/types`

**Predicted Directories (4):**
- ❌ `src/cmd/internal/types2`
- ✅ `src/go/types`
- ❌ `src/types`
- ❌ `src/types/types2`


### 📊 **Proposal #53346 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/xml`

**Predicted Directories (3):**
- ❌ `src/archive/tar`
- ❌ `src/archive/zip`
- ✅ `src/encoding/xml`


### 📊 **Proposal #40127 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/json`

**Predicted Directories (6):**
- ✅ `src/encoding/json`
- ❌ `src/encoding/json/internal/jsonflags`
- ❌ `src/encoding/json/internal/jsonopts`
- ❌ `src/encoding/json/internal/jsontest`
- ❌ `src/encoding/json/internal/jsonwire`
- ❌ `src/encoding/json/jsontext`


### 📊 **Proposal #51082 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 4.6% | 8.3% | 3/65 |

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

**Predicted Directories (7):**
- ❌ `go/doc`
- ❌ `gofmt`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ✅ `src/go/doc`
- ✅ `src/go/doc/comment`
- ✅ `src/net/http`


### 📊 **Proposal #35833 (Directory Level)**

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


### 📊 **Proposal #45460 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/net/http`


### 📊 **Proposal #42387 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io/fs`

**Predicted Directories (2):**
- ✅ `src/io/fs`
- ❌ `src/os`


### 📊 **Proposal #45454 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.7% | 33.3% | 12.5% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/cfg`
- `src/go/build`
- `src/internal/buildcfg`

**Predicted Directories (13):**
- ❌ `cmd/go/internal/flags`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/cmd/link/internal/amd64`
- ❌ `src/cmd/link/internal/arm`
- ❌ `src/cmd/link/internal/arm64`
- ❌ `src/cmd/link/internal/ppc64`
- ❌ `src/cmd/link/internal/riscv64`
- ❌ `src/cmd/link/internal/s390x`
- ❌ `src/cmd/link/internal/x86`
- ❌ `src/cmd/link/testdata/deadcode`
- ✅ `src/go/build`
- ❌ `src/runtime`


### 📊 **Proposal #50436 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os/exec`

**Predicted Directories (2):**
- ❌ `src/os`
- ✅ `src/os/exec`


### 📊 **Proposal #44167 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (3):**
- ❌ `internal/runtime/sys`
- ✅ `src/runtime`
- ❌ `src/runtime/gc`


### 📊 **Proposal #39178 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (2):**
- ✅ `src/net`
- ❌ `src/net/http`


### 📊 **Proposal #46287 (Directory Level)**

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


### 📊 **Proposal #48257 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/go/internal/workcmd`

**Predicted Directories (2):**
- ❌ `go/work`
- ❌ `go/workcmd`


### 📊 **Proposal #46293 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/reflect`

**Predicted Directories (2):**
- ✅ `src/reflect`
- ❌ `src/runtime/maps`


### 📊 **Proposal #42026 (Directory Level)**

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


### 📊 **Proposal #45435 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/sync`

**Predicted Directories (3):**
- ❌ `src/net/http`
- ❌ `src/net/http2/hpack`
- ✅ `src/sync`


### 📊 **Proposal #48187 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/version`
- `src/debug/buildinfo`

**Predicted Directories (8):**
- ❌ `internal/runtime/sys`
- ❌ `src/cgo/internal/testcarchive`
- ❌ `src/cgo/internal/testcshared`
- ✅ `src/cmd/go/internal/version`
- ❌ `src/cmd/link/internal/ld`
- ✅ `src/debug/buildinfo`
- ❌ `src/go/version`
- ❌ `test/fixedbugs`


### 📊 **Proposal #37519 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modget`

**Predicted Directories (3):**
- ❌ `cmd/go/internal/get`
- ❌ `cmd/go/internal/modget`
- ❌ `src/cmd/go/internal/get`


### 📊 **Proposal #38627 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/text/template/parse`

**Predicted Directories (3):**
- ❌ `src/html/template`
- ❌ `src/text/template`
- ✅ `src/text/template/parse`


### 📊 **Proposal #41260 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (2):**
- ❌ `src/os`
- ✅ `src/testing`


### 📊 **Proposal #44505 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/asm/internal/lex`
- `src/cmd/dist`
- `src/sort`

**Predicted Directories (1):**
- ❌ `test/fixedbugs`


### 📊 **Proposal #50429 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/parser`

**Predicted Directories (5):**
- ❌ `interface`
- ❌ `interface/structinit.dir`
- ❌ `src/go`
- ❌ `src/go/ast`
- ❌ `syntax`


### 📊 **Proposal #53573 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (2):**
- ✅ `src/crypto/x509`
- ❌ `src/crypto/x509/pkix`


### 📊 **Proposal #46059 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (1):**
- ✅ `src/net/url`


### 📊 **Proposal #42681 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/asm/internal/lex`
- `src/cmd/dist`
- `src/cmd/go/internal/work`
- `src/cmd/link/internal/ld`
- `src/runtime`

**Predicted Directories (3):**
- ❌ `cmd`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/go/goexperiment`


### 📊 **Proposal #40592 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/encoding/json`
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`


### 📊 **Proposal #51644 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/binary`

**Predicted Directories (1):**
- ✅ `src/encoding/binary`


### 📊 **Proposal #34527 (Directory Level)**

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

**Predicted Directories (1):**
- ❌ `cmd/go/modfetch`


### 📊 **Proposal #45628 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/xml`

**Predicted Directories (3):**
- ❌ `src/encoding`
- ✅ `src/encoding/xml`
- ❌ `test/fixedbugs`


### 📊 **Proposal #46746 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (2):**
- ❌ `interface`
- ✅ `src/reflect`


### 📊 **Proposal #44940 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/unicode/utf16`

**Predicted Directories (1):**
- ✅ `src/unicode/utf16`


### 📊 **Proposal #41066 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (5):**
- ✅ `src/crypto/tls`
- ❌ `src/net`
- ❌ `src/net/http`
- ❌ `src/testtls`
- ❌ `vendor/golang.org/x/net`


### 📊 **Proposal #41184 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 12.5% | 18.2% | 2/16 |

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

**Predicted Directories (6):**
- ❌ `cmd/go`
- ❌ `cmd/go/dist`
- ❌ `cmd/go/fix`
- ❌ `src/cmd/go`
- ✅ `src/go/build`
- ✅ `src/go/build/constraint`


### 📊 **Proposal #48866 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/mime`

**Predicted Directories (3):**
- ❌ `bytes`
- ❌ `src/encoding/json`
- ✅ `src/mime`


### 📊 **Proposal #50332 (Directory Level)**

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


### 📊 **Proposal #53466 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 33.3% | 28.6% | 2/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/cmd/dist`
- `src/cmd/link`
- `src/cmd/link/internal/ld`
- `src/cmd/link/internal/riscv64`
- `src/runtime`
- `src/syscall`

**Predicted Directories (8):**
- ❌ `src/asm/internal/arch`
- ❌ `src/internal/cpu`
- ❌ `src/internal/goos`
- ❌ `src/os`
- ✅ `src/runtime`
- ❌ `src/sys`
- ✅ `src/syscall`
- ❌ `src/sysinfo`


### 📊 **Proposal #49097 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (3):**
- ❌ `src`
- ✅ `src/net`
- ❌ `src/net/netip`


### 📊 **Proposal #49390 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/dist`
- `src/internal/testenv`

**Predicted Directories (1):**
- ❌ `src/runtime`


### 📊 **Proposal #39351 (Directory Level)**

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


### 📊 **Proposal #47142 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/database/sql`

**Predicted Directories (2):**
- ✅ `src/database/sql`
- ❌ `src/database/sql/driver`


### 📊 **Proposal #46742 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 20.0% | 22.2% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/compile/internal/typecheck`
- `src/cmd/compile/internal/walk`
- `src/runtime`
- `src/runtime/testdata/testprog`
- `test`

**Predicted Directories (4):**
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ✅ `src/runtime`
- ❌ `src/unsafe`


### 📊 **Proposal #46505 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/sha256`
- `src/crypto/sha512`

**Predicted Directories (1):**
- ❌ `interface`


### 📊 **Proposal #52376 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`


### 📊 **Proposal #44815 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/bufio`

**Predicted Directories (3):**
- ✅ `src/bufio`
- ❌ `src/io/fs`
- ❌ `src/net/http`


### 📊 **Proposal #45033 (Directory Level)**

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


### 📊 **Proposal #48218 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`


### 📊 **Proposal #47066 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`


### 📊 **Proposal #51572 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/dist`
- `src/cmd/go/internal/imports`
- `src/go/build`

**Predicted Directories (18):**
- ❌ `doc`
- ❌ `go/gofmt`
- ❌ `go/internal/base`
- ❌ `go/internal/lockedfile`
- ❌ `go/internal/mmap`
- ❌ `go/internal/telemetrystats`
- ❌ `go/internal/tool`
- ❌ `go/internal/toolchain`
- ❌ `go/test`
- ❌ `src/net`
- ❌ `src/net/http`
- ❌ `src/os`
- ❌ `src/os/exec`
- ❌ `src/runtime/syscall`
- ❌ `src/sync/atomic`
- ❌ `src/sys/unix`
- ❌ `src/syscall`
- ❌ `src/time`


### 📊 **Proposal #39057 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/log`

**Predicted Directories (1):**
- ✅ `src/log`


### 📊 **Proposal #38781 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/net/http`
- `src/testing/iotest`

**Predicted Directories (2):**
- ✅ `src/testing/iotest`
- ❌ `testing/iotest`


### 📊 **Proposal #36771 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/strconv`

**Predicted Directories (2):**
- ❌ `src/archive/tar`
- ✅ `src/strconv`


### 📊 **Proposal #44435 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modload`

**Predicted Directories (2):**
- ❌ `go/internal/modcmd`
- ❌ `go/internal/modload`


### 📊 **Proposal #50101 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/syscall/unix`
- `src/net`

**Predicted Directories (3):**
- ❌ `src`
- ✅ `src/net`
- ❌ `src/net/http`


### 📊 **Proposal #29770 (Directory Level)**

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


### 📊 **Proposal #51566 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/io`
- `src/net/http`

**Predicted Directories (3):**
- ❌ `src/bytes`
- ✅ `src/io`
- ❌ `src/io/ioutil`


### 📊 **Proposal #37196 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 20.0% | 28.6% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/compile/internal/ssagen`
- `src/cmd/compile/internal/typecheck/_builtin`
- `src/cmd/compile/internal/walk`
- `src/runtime`
- `src/time`

**Predicted Directories (2):**
- ❌ `lib`
- ✅ `src/time`


### 📊 **Proposal #38079 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (1):**
- ✅ `src/net/http/httputil`


### 📊 **Proposal #51682 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 50.0% | 22.2% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/types2`
- `src/go/types`

**Predicted Directories (7):**
- ❌ `src`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/objfile`
- ❌ `src/cmd/internal/objfile/testdata`
- ❌ `src/cmd/internal/objfile/testdata/testfilenum`
- ✅ `src/go/types`
- ❌ `src/types`


### 📊 **Proposal #39214 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 12.5% | 14.3% | 1/8 |

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

**Predicted Directories (6):**
- ✅ `src/internal/cpu`
- ❌ `src/runtime`
- ❌ `src/runtime/cpu`
- ❌ `src/sys`
- ❌ `src/sys/cpu`
- ❌ `src/syscall`


### 📊 **Proposal #30715 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (2):**
- ✅ `src/net/http`
- ❌ `test/fixedbugs`


### 📊 **Proposal #51972 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/sync`

**Predicted Directories (1):**
- ✅ `src/sync`


### 📊 **Proposal #50859 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/sync`

**Predicted Directories (6):**
- ❌ `interface`
- ❌ `internal/runtime/sys`
- ❌ `src/runtime/atomic`
- ❌ `src/runtime/race`
- ❌ `src/runtime/sync`
- ❌ `src/sync/atomic`


### 📊 **Proposal #32406 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/tls`
- `src/net/http`

**Predicted Directories (2):**
- ✅ `src/crypto/tls`
- ✅ `src/net/http`


### 📊 **Proposal #35044 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (2):**
- ✅ `src/crypto/x509`
- ❌ `src/net/http`


### 📊 **Proposal #45899 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (2):**
- ✅ `src/io`
- ❌ `src/io/fs`


### 📊 **Proposal #33232 (Directory Level)**

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


### 📊 **Proposal #47658 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`


### 📊 **Proposal #47609 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/unicode/utf8`

**Predicted Directories (2):**
- ❌ `src/encoding/json`
- ✅ `src/unicode/utf8`


### 📊 **Proposal #38776 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 75.0% | 54.5% | 6/8 |

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

**Predicted Directories (14):**
- ❌ `internal/hash`
- ❌ `src/crypto/adler32`
- ❌ `src/crypto/crc32`
- ❌ `src/crypto/crc64`
- ❌ `src/crypto/fnv`
- ✅ `src/crypto/sha1`
- ✅ `src/crypto/sha256`
- ❌ `src/crypto/sha3`
- ✅ `src/crypto/sha512`
- ❌ `src/hash`
- ❌ `src/hash/adler32`
- ✅ `src/hash/crc32`
- ✅ `src/hash/crc64`
- ✅ `src/hash/fnv`


### 📊 **Proposal #45428 (File Level)**

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


### 📊 **Proposal #48801 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`
- `src/cmd/vet/main.go`

**Predicted Files (9):**
- ❌ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ❌ `src/time/format.go`
- ❌ `src/time/format_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`
- ❌ `src/vet/doc.go`
- ❌ `src/vet/main.go`
- ❌ `src/vet/vet_test.go`


### 📊 **Proposal #34875 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/go/doc/comment.go`

**Predicted Files (6):**
- ❌ `doc/doc.go`
- ❌ `doc/doc_test.go`
- ✅ `src/go/doc/comment.go`
- ❌ `src/go/doc/doc.go`
- ❌ `src/go/doc/markdown.go`
- ❌ `src/net/http/doc.go`


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


### 📊 **Proposal #51777 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/netip/netip_test.go`

**Predicted Files (4):**
- ❌ `fix/netipv6zone.go`
- ❌ `fix/netipv6zone_test.go`
- ❌ `src/net/net.go`
- ❌ `src/net/netip/netip.go`


### 📊 **Proposal #47164 (File Level)**

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


### 📊 **Proposal #42710 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/hash/maphash/maphash.go`
- `src/hash/maphash/maphash_test.go`

**Predicted Files (2):**
- ✅ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_test.go`


### 📊 **Proposal #46259 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 50.0% | 18.2% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/syscall/exec_freebsd.go`
- `src/syscall/exec_freebsd_test.go`

**Predicted Files (9):**
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `src/os/exec/exec_freebsd.go`
- ❌ `src/os/exec/internal/fdtest/exists_freebsd.go`
- ❌ `src/sys/syscall_freebsd.go`
- ❌ `src/syscall/exec_bsd.go`
- ✅ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/syscall_freebsd.go`
- ❌ `src/syscall/syscall_freebsd_test.go`
- ❌ `src/syscall/sysnum_freebsd.go`


### 📊 **Proposal #47257 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/18 |

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

**Predicted Files (11):**
- ❌ `src/net/http/client.go`
- ❌ `src/net/http/cookiejar/jar.go`
- ❌ `src/net/http/cookiejar/jar_test.go`
- ❌ `src/net/http/httptest/httptest.go`
- ❌ `src/net/http/httptrace/httptrace_test.go`
- ❌ `src/net/http/httptrace/trace.go`
- ❌ `src/net/http/httputil/httputil.go`
- ❌ `src/net/http/pprof/pprof.go`
- ❌ `src/net/http/pprof/pprof_test.go`
- ❌ `src/net/http/server.go`
- ❌ `src/syscall/net.go`


### 📊 **Proposal #47216 (File Level)**

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

**Predicted Files (4):**
- ❌ `internal/runtime/metrics.go`
- ❌ `src/runtime/metrics/metrics.go`
- ❌ `src/runtime/metrics/metrics_test.go`
- ❌ `src/runtime/runtime.go`


### 📊 **Proposal #53747 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/flag/example_func_test.go`
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (4):**
- ❌ `go/internal/cmdflag/flag.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`
- ❌ `testing/flag_test.go`


### 📊 **Proposal #34974 (File Level)**

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


### 📊 **Proposal #34626 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/benchmark.go`
- `src/testing/benchmark_test.go`

**Predicted Files (5):**
- ❌ `src/cmd/internal/objfile/bench.go`
- ❌ `src/cmd/internal/objfile/bench_test.go`
- ❌ `src/testing/bench_test.go`
- ✅ `src/testing/benchmark.go`
- ✅ `src/testing/benchmark_test.go`


### 📊 **Proposal #48530 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/net/net.go`
- `src/net/tcpsock.go`
- `src/net/tcpsock_plan9.go`
- `src/net/tcpsock_posix.go`

**Predicted Files (8):**
- ❌ `src/net.go`
- ❌ `src/net/conn.go`
- ❌ `src/net/splice_linux.go`
- ❌ `src/net/tcp.go`
- ❌ `src/net/tcp_test.go`
- ❌ `src/net/tcpconn.go`
- ❌ `src/poll/splice_linux.go`
- ❌ `src/poll/splice_linux_test.go`


### 📊 **Proposal #50102 (File Level)**

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


### 📊 **Proposal #38687 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/cmd/go/internal/generate/generate.go`

**Predicted Files (2):**
- ❌ `go/internal/generate/generate.go`
- ❌ `go/internal/generate/generate_test.go`


### 📊 **Proposal #50062 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/time.go`
- `src/time/time_test.go`

**Predicted Files (5):**
- ❌ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ✅ `src/time/time.go`
- ❌ `src/time/zoneinfo.go`
- ❌ `src/time/zoneinfo_test.go`


### 📊 **Proposal #46731 (File Level)**

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

**Predicted Files (33):**
- ❌ `cmd/cgo/internal/test/issue41761.go`
- ❌ `cmd/cgo/internal/test/issue41761a/a.go`
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `src/cmd/compile/internal/objabi/flag.go`
- ❌ `src/cmd/compile/internal/objfile/elf.go`
- ❌ `src/cmd/compile/internal/objfile/goobj.go`
- ❌ `src/cmd/compile/internal/objfile/macho.go`
- ❌ `src/cmd/compile/internal/objfile/pe.go`
- ❌ `src/cmd/compile/internal/objfile/plan9obj.go`
- ❌ `src/cmd/compile/internal/objfile/xcoff.go`
- ❌ `src/cmd/compile/internal/osinfo/os_js.go`
- ❌ `src/cmd/compile/internal/osinfo/os_plan9.go`
- ❌ `src/cmd/compile/internal/osinfo/os_solaris.go`
- ❌ `src/cmd/compile/internal/osinfo/os_syscall.go`
- ❌ `src/cmd/compile/internal/osinfo/os_sysctl.go`
- ❌ `src/cmd/compile/internal/osinfo/os_uname.go`
- ❌ `src/cmd/compile/internal/osinfo/os_windows.go`
- ❌ `src/cmd/compile/internal/robustio/robustio.go`
- ❌ `src/cmd/compile/internal/robustio/robustio_darwin.go`
- ❌ `src/cmd/compile/internal/robustio/robustio_flaky.go`
- ❌ `src/cmd/compile/internal/robustio/robustio_other.go`
- ❌ `src/cmd/compile/internal/robustio/robustio_windows.go`
- ❌ `src/cmd/compile/internal/telemetry/counter/counter.go`
- ❌ `src/cmd/compile/internal/telemetry/counter/counter_bootstrap.go`
- ❌ `src/cmd/compile/internal/telemetry/telemetry.go`
- ❌ `src/cmd/compile/internal/telemetry/telemetry_bootstrap.go`
- ❌ `src/runtime/cgo/cgo.go`
- ❌ `src/runtime/internal/sys/sys.go`
- ❌ `src/runtime/mmap.go`
- ❌ `src/runtime/sys/nih.go`
- ❌ `test/notinheap.go`
- ❌ `test/notinheap2.go`
- ❌ `test/notinheap3.go`


### 📊 **Proposal #33184 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 100.0% | 60.0% | 3/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/time.go`
- `src/time/tick.go`
- `src/time/tick_test.go`

**Predicted Files (7):**
- ❌ `lib/time/mkzip.go`
- ✅ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ✅ `src/time/tick.go`
- ✅ `src/time/tick_test.go`
- ❌ `src/time/ticker.go`
- ❌ `src/time/ticker_test.go`


### 📊 **Proposal #50489 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/math/big/ratconv.go`
- `src/math/big/ratconv_test.go`

**Predicted Files (3):**
- ❌ `src/math/big/rat.go`
- ❌ `src/math/big/rat_test.go`
- ❌ `src/math/big/rational.go`


### 📊 **Proposal #47342 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 50.0% | 36.4% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/cmd/dist/test.go`
- `src/hash/maphash/maphash.go`
- `src/hash/maphash/maphash_purego.go`
- `src/hash/maphash/maphash_runtime.go`

**Predicted Files (7):**
- ❌ `map.go`
- ❌ `mapimp.go`
- ❌ `maps.go`
- ❌ `mapsimp.go`
- ✅ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_purego.go`
- ❌ `src/hash/maphash/maphash_test.go`


### 📊 **Proposal #37255 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 33.3% | 25.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/os/signal/example_unix_test.go`
- `src/os/signal/signal.go`
- `src/os/signal/signal_test.go`

**Predicted Files (5):**
- ❌ `doc/signal_notunix.go`
- ❌ `doc/signal_unix.go`
- ❌ `src/context/context.go`
- ❌ `src/context/context_test.go`
- ✅ `src/os/signal/signal.go`


### 📊 **Proposal #42502 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 9.5% | 15.4% | 2/21 |

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

**Predicted Files (5):**
- ❌ `src/runtime/pprof/defs_darwin.go`
- ❌ `src/runtime/pprof/defs_darwin_amd64.go`
- ❌ `src/runtime/pprof/defs_darwin_arm64.go`
- ✅ `src/runtime/pprof/pprof.go`
- ✅ `src/runtime/pprof/pprof_test.go`


### 📊 **Proposal #42782 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 100.0% | 36.4% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/visiblefields.go`
- `src/reflect/visiblefields_test.go`

**Predicted Files (9):**
- ❌ `interface/embed.go`
- ❌ `interface/embed1.go`
- ❌ `interface/embed2.go`
- ❌ `interface/embed3.go`
- ❌ `interface/struct.go`
- ❌ `src/reflect/reflect.go`
- ❌ `src/reflect/type.go`
- ✅ `src/reflect/visiblefields.go`
- ✅ `src/reflect/visiblefields_test.go`


### 📊 **Proposal #38248 (File Level)**

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

**Predicted Files (9):**
- ❌ `src/cmd/compile/internal/wasm/asm.go`
- ❌ `src/cmd/compile/internal/wasm/obj.go`
- ❌ `src/compile/internal/abi/abiutils.go`
- ❌ `src/syscall/js/fs_js.go`
- ❌ `src/syscall/js/syscall_js.go`
- ❌ `src/wasm/ssa.go`
- ❌ `wasmexport.go`
- ❌ `wasmexport2.go`
- ❌ `wasmmemsize.go`


### 📊 **Proposal #46279 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/link/internal/ld/ld_test.go`
- `src/cmd/link/internal/ld/lib.go`

**Predicted Files (23):**
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `select.go`
- ❌ `src/runtime/rlimit_unix.go`
- ❌ `src/runtime/runtime.go`
- ❌ `src/runtime/select.go`
- ❌ `src/runtime/sys/syscall_linux.go`
- ❌ `src/runtime/sys/syscall_linux_test.go`
- ❌ `src/runtime/syscall_unix.go`
- ❌ `src/sys/arch.go`
- ❌ `src/sys/syscall.go`
- ❌ `src/sys/unix/affinity_linux.go`
- ❌ `src/sys/unix/aliases.go`
- ❌ `src/sys/unix/auxv.go`
- ❌ `src/sys/unix/fcntl.go`
- ❌ `src/sys/unix/ioctl_linux.go`
- ❌ `src/sys/unix/syscall_linux.go`
- ❌ `src/sys/unix/syscall_linux_amd64.go`
- ❌ `src/sys/unix/syscall_linux_arm.go`
- ❌ `src/sys/unix/syscall_linux_arm64.go`
- ❌ `src/syscall/rlimit.go`
- ❌ `src/syscall/rlimit_test.go`
- ❌ `src/syscall/syscall.go`
- ❌ `src/syscall/syscall_unix.go`


### 📊 **Proposal #40724 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 2.4% | 1.3% | 1.7% | 2/152 |

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

**Predicted Files (83):**
- ❌ `cmd/asm/asm.go`
- ❌ `cmd/compile/internal-abi.md`
- ❌ `cmd/compile/runtimemeta.go`
- ❌ `cmd/link/link.go`
- ❌ `runtime/runtime.go`
- ❌ `src/cmd/compile/abi.go`
- ❌ `src/cmd/compile/abi_test.go`
- ❌ `src/cmd/compile/compile.go`
- ❌ `src/cmd/compile/compile_test.go`
- ❌ `src/cmd/compile/internal-abi.md`
- ❌ `src/cmd/compile/ssa.go`
- ❌ `src/cmd/compile/ssa_test.go`
- ❌ `src/compile/internal/abi/abi_string.go`
- ❌ `src/compile/internal/abi/abi_test.go`
- ❌ `src/compile/internal/abi/abi_testdata.go`
- ❌ `src/compile/internal/abi/abiutils.go`
- ❌ `src/compile/internal/abi/abiutils_test.go`
- ✅ `src/internal/abi/abi.go`
- ❌ `src/internal/abi/abi_amd64.go`
- ❌ `src/internal/abi/abi_arm64.go`
- ❌ `src/internal/abi/abi_generic.go`
- ❌ `src/internal/abi/abi_loong64.go`
- ❌ `src/internal/abi/abi_ppc64x.go`
- ❌ `src/internal/abi/abi_riscv64.go`
- ✅ `src/internal/abi/abi_test.go`
- ❌ `src/runtime/pprof/defs_darwin.go`
- ❌ `src/runtime/pprof/defs_darwin_amd64.go`
- ❌ `src/runtime/pprof/defs_darwin_arm64.go`
- ❌ `src/runtime/pprof/defs_freebsd.go`
- ❌ `src/runtime/pprof/defs_freebsd_amd64.go`
- ❌ `src/runtime/pprof/defs_freebsd_arm.go`
- ❌ `src/runtime/pprof/defs_freebsd_arm64.go`
- ❌ `src/runtime/pprof/defs_linux.go`
- ❌ `src/runtime/pprof/defs_linux_amd64.go`
- ❌ `src/runtime/pprof/defs_linux_arm.go`
- ❌ `src/runtime/pprof/defs_linux_arm64.go`
- ❌ `src/runtime/pprof/defs_linux_loong64.go`
- ❌ `src/runtime/pprof/defs_linux_mips64x.go`
- ❌ `src/runtime/pprof/defs_linux_mipsx.go`
- ❌ `src/runtime/pprof/defs_linux_ppc64.go`
- ❌ `src/runtime/pprof/defs_linux_ppc64le.go`
- ❌ `src/runtime/pprof/defs_linux_riscv64.go`
- ❌ `src/runtime/pprof/defs_linux_s390x.go`
- ❌ `src/runtime/pprof/defs_plan9.go`
- ❌ `src/runtime/pprof/defs_plan9_amd64.go`
- ❌ `src/runtime/pprof/defs_plan9_arm.go`
- ❌ `src/runtime/pprof/defs_solaris.go`
- ❌ `src/runtime/pprof/defs_solaris_amd64.go`
- ❌ `src/runtime/pprof/defs_windows.go`
- ❌ `src/runtime/pprof/defs_windows_amd64.go`
- ❌ `src/runtime/pprof/defs_windows_arm.go`
- ❌ `src/runtime/pprof/defs_windows_arm64.go`
- ❌ `src/runtime/pprof/pprof.go`
- ❌ `src/runtime/pprof/pprof_norusage.go`
- ❌ `src/runtime/pprof/pprof_rusage.go`
- ❌ `src/runtime/pprof/pprof_test.go`
- ❌ `src/runtime/pprof/pprof_windows.go`
- ❌ `src/runtime/pprof/proto.go`
- ❌ `src/runtime/pprof/proto_test.go`
- ❌ `src/runtime/pprof/protobuf.go`
- ❌ `src/runtime/pprof/protomem.go`
- ❌ `src/runtime/pprof/protomem_test.go`
- ❌ `src/runtime/runtime.go`
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
- ❌ `test/abi/reg_not_ssa.go`
- ❌ `test/abi/result_live.go`
- ❌ `test/abi/result_regalloc.go`
- ❌ `test/abi/return_stuff.go`
- ❌ `test/abi/spills3.go`
- ❌ `test/abi/spills4.go`
- ❌ `test/abi/store_reg_args.go`
- ❌ `test/abi/struct_lower_1.go`


### 📊 **Proposal #51914 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/httputil/reverseproxy.go`
- `src/net/http/httputil/reverseproxy_test.go`

**Predicted Files (6):**
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/httputil/httputil.go`
- ✅ `src/net/http/httputil/reverseproxy.go`
- ❌ `src/net/http/net.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/server.go`


### 📊 **Proposal #40481 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 4.8% | 8.3% | 6.1% | 1/12 |

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

**Predicted Files (21):**
- ❌ `src/cmd/internal/objabi/autotype.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/funcid.go`
- ❌ `src/cmd/internal/objabi/path.go`
- ❌ `src/cmd/internal/objabi/reloctype.go`
- ❌ `src/cmd/internal/objabi/symkind.go`
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


### 📊 **Proposal #46552 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 66.7% | 30.8% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/syscall_windows.go`
- `src/runtime/syscall_windows_test.go`
- `src/syscall/dll_windows.go`

**Predicted Files (10):**
- ❌ `src/runtime/syscall/syscall.go`
- ❌ `src/runtime/syscall/windows/mksyscall.go`
- ❌ `src/runtime/syscall/windows/syscall_windows.go`
- ✅ `src/runtime/syscall_windows.go`
- ✅ `src/runtime/syscall_windows_test.go`
- ❌ `src/sys/mksyscall.go`
- ❌ `src/sys/syscall.go`
- ❌ `src/sys/syscall_windows.go`
- ❌ `src/syscall/mksyscall_windows.go`
- ❌ `src/syscall/syscall_windows.go`


### 📊 **Proposal #33136 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.0% | 50.0% | 9.1% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (20):**
- ❌ `interface/reflectmethod1.go`
- ❌ `interface/reflectmethod2.go`
- ❌ `interface/reflectmethod3.go`
- ❌ `interface/reflectmethod4.go`
- ❌ `interface/reflectmethod5.go`
- ❌ `interface/reflectmethod6.go`
- ❌ `interface/reflectmethod7.go`
- ❌ `interface/reflectmethod8.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encode_test.go`
- ❌ `src/encoding/json/internal/jsonwire/decode.go`
- ❌ `src/encoding/json/internal/jsonwire/decode_test.go`
- ❌ `src/reflect/abi.go`
- ❌ `src/reflect/abi_test.go`
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/value.go`


### 📊 **Proposal #52221 (File Level)**

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


### 📊 **Proposal #44853 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.4% | 6.5% | 6.9% | 2/31 |

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

**Predicted Files (27):**
- ❌ `cmd/dist/build.go`
- ❌ `cmd/dist/build_test.go`
- ❌ `cmd/dist/buildruntime.go`
- ❌ `cmd/dist/buildtag.go`
- ❌ `cmd/dist/buildtag_test.go`
- ❌ `cmd/dist/exec.go`
- ❌ `cmd/dist/imports.go`
- ❌ `cmd/dist/notgo122.go`
- ❌ `cmd/dist/quoted.go`
- ❌ `cmd/dist/supported_test.go`
- ❌ `cmd/dist/sys_default.go`
- ❌ `cmd/dist/test.go`
- ❌ `cmd/dist/testjson_test.go`
- ❌ `cmd/dist/util.go`
- ❌ `cmd/dist/util_gc.go`
- ❌ `cmd/dist/util_gccgo.go`
- ❌ `runtime/asan.go`
- ❌ `runtime/malloc.go`
- ❌ `src/crypto/asan.go`
- ❌ `src/internal/asan/asan.go`
- ❌ `src/internal/asan/doc.go`
- ❌ `src/internal/asan/noasan.go`
- ✅ `src/runtime/asan.go`
- ❌ `src/runtime/asan/asan.go`
- ✅ `src/runtime/malloc.go`
- ❌ `src/runtime/memstats.go`
- ❌ `src/runtime/msan/msan.go`


### 📊 **Proposal #50599 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 16.7% | 20.0% | 2/12 |

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

**Predicted Files (8):**
- ✅ `src/os/exec/exec.go`
- ✅ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/internal/fdtest/exists_test.go`
- ❌ `src/os/exec/internal/fdtest/exists_unix.go`
- ❌ `src/syscall/exec_linux.go`
- ❌ `src/syscall/exec_linux_test.go`
- ❌ `src/syscall/exec_unix.go`
- ❌ `src/syscall/exec_unix_test.go`


### 📊 **Proposal #42537 (File Level)**

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
- ❌ `src/strings/reader.go`
- ❌ `src/strings/replace.go`
- ✅ `src/strings/strings.go`
- ❌ `src/testing/benchmark.go`
- ❌ `src/testing/benchmark_test.go`
- ❌ `src/testing/fstest/mapfs.go`
- ❌ `src/testing/fstest/mapfs_test.go`
- ❌ `test/run.go`


### 📊 **Proposal #40995 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.5% | 5.3% | 7.0% | 2/38 |

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

**Predicted Files (19):**
- ❌ `src/compile/internal/abi/abi.go`
- ❌ `src/compile/internal/abi/abiutils.go`
- ❌ `src/compile/internal/abi/abiutils_test.go`
- ❌ `src/compile/internal/mips/mips64/galign.go`
- ❌ `src/compile/internal/mips/mips64/ggen.go`
- ❌ `src/compile/internal/mips/mips64/ssa.go`
- ❌ `src/os/os_openbsd_mips64.go`
- ❌ `src/runtime/cpu/cpu_mips.go`
- ❌ `src/runtime/cpu/cpu_mips64x.go`
- ✅ `src/runtime/signal_openbsd_mips64.go`
- ❌ `src/runtime/sys_openbsd_mips64.go`
- ❌ `src/sys/arch.go`
- ❌ `src/sys/syscall_openbsd_mips64.go`
- ✅ `src/syscall/syscall_openbsd_mips64.go`
- ❌ `src/syscall/unix/arc4random_openbsd.go`
- ❌ `src/syscall/unix/at_openbsd.go`
- ❌ `src/syscall/unix/faccessat_openbsd.go`
- ❌ `src/syscall/unix/kernel_version_openbsd.go`
- ❌ `src/syscall/unix/net_openbsd.go`


### 📊 **Proposal #39034 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 100.0% | 44.4% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/format.go`
- `src/time/format_test.go`

**Predicted Files (7):**
- ❌ `lib/time/mkzip.go`
- ❌ `src/fmt/format.go`
- ❌ `src/fmt/print.go`
- ✅ `src/time/format.go`
- ✅ `src/time/format_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`


### 📊 **Proposal #45100 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/url/url.go`
- `src/net/url/url_test.go`

**Predicted Files (3):**
- ❌ `src/net/url.go`
- ✅ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`


### 📊 **Proposal #47005 (File Level)**

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


### 📊 **Proposal #53482 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 16.7% | 16.7% | 1/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/net/interface_aix.go`
- `src/net/interface_bsd.go`
- `src/net/interface_linux.go`
- `src/net/interface_plan9.go`
- `src/net/interface_solaris.go`
- `src/net/interface_windows.go`

**Predicted Files (6):**
- ❌ `net/interface_linux.go`
- ❌ `src/net.go`
- ❌ `src/net/interface.go`
- ✅ `src/net/interface_linux.go`
- ❌ `src/syscall/zerrors_linux_amd64.go`
- ❌ `syscall/zerrors_linux_amd64.go`


### 📊 **Proposal #37112 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 44.4% | 36.4% | 40.0% | 4/11 |

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
- ❌ `internal/runtime/metrics.go`
- ❌ `src/runtime/`
- ✅ `src/runtime/metrics/description.go`
- ❌ `src/runtime/metrics/doc.go`
- ❌ `src/runtime/metrics/histogram.go`
- ❌ `src/runtime/metrics/metrics.go`
- ✅ `src/runtime/metrics/sample.go`
- ✅ `src/runtime/metrics/value.go`
- ✅ `src/runtime/metrics_test.go`


### 📊 **Proposal #46771 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/mime/multipart/writer.go`
- `src/mime/multipart/writer_test.go`

**Predicted Files (3):**
- ❌ `src/mime/multipart/formdata.go`
- ❌ `src/mime/multipart/multipart.go`
- ✅ `src/mime/multipart/writer.go`


### 📊 **Proposal #48424 (File Level)**

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

**Predicted Files (3):**
- ❌ `src/maps/maps.go`
- ❌ `src/maps/maps_test.go`
- ❌ `typeparam/issue48424.go`


### 📊 **Proposal #46485 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 14.3% | 18.2% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/cgo/ast.go`
- `src/cmd/go/internal/load/test.go`
- `src/cmd/gofmt/gofmt.go`
- `src/cmd/gofmt/simplify.go`
- `src/go/internal/srcimporter/srcimporter.go`
- `src/go/parser/parser.go`
- `src/go/parser/performance_test.go`

**Predicted Files (4):**
- ✅ `src/go/parser/parser.go`
- ❌ `src/go/parser/parser_test.go`
- ❌ `src/go/parser/resolver.go`
- ❌ `src/go/parser/resolver_test.go`


### 📊 **Proposal #34652 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 87.5% | 48.3% | 7/8 |

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

**Predicted Files (21):**
- ❌ `src/html/template/template.go`
- ✅ `src/html/template/template_test.go`
- ❌ `src/text/template/doc.go`
- ❌ `src/text/template/example_test.go`
- ❌ `src/text/template/examplefiles_test.go`
- ❌ `src/text/template/examplefunc_test.go`
- ✅ `src/text/template/exec.go`
- ❌ `src/text/template/exec_test.go`
- ❌ `src/text/template/funcs.go`
- ❌ `src/text/template/helper.go`
- ❌ `src/text/template/link_test.go`
- ❌ `src/text/template/multi_test.go`
- ❌ `src/text/template/option.go`
- ❌ `src/text/template/parse.go`
- ✅ `src/text/template/parse/lex.go`
- ✅ `src/text/template/parse/lex_test.go`
- ✅ `src/text/template/parse/node.go`
- ✅ `src/text/template/parse/parse.go`
- ✅ `src/text/template/parse/parse_test.go`
- ❌ `src/text/template/parse_test.go`
- ❌ `src/text/template/template.go`


### 📊 **Proposal #42098 (File Level)**

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
- ❌ `src/syscall/exec_windows_test.go`
- ❌ `src/syscall/syscall_windows.go`


### 📊 **Proposal #35998 (File Level)**

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


### 📊 **Proposal #43698 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/embed/embed.go`
- `src/embed/internal/embedtest/embed_test.go`

**Predicted Files (5):**
- ❌ `cmd/vet/vet.go`
- ❌ `cmd/vet/vetflag.go`
- ❌ `src/cmd/vet/doc.go`
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/vet_test.go`


### 📊 **Proposal #51414 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/time.go`
- `src/time/time_test.go`

**Predicted Files (4):**
- ❌ `lib/time/`
- ❌ `src/time/abs_test.go`
- ✅ `src/time/time.go`
- ✅ `src/time/time_test.go`


### 📊 **Proposal #37023 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 3/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/runtime/debug/panic_test.go`
- `src/runtime/error.go`
- `src/runtime/os_plan9.go`
- `src/runtime/panic.go`
- `src/runtime/signal_unix.go`
- `src/runtime/signal_windows.go`

**Predicted Files (6):**
- ❌ `recover.go`
- ❌ `runtime.go`
- ✅ `src/runtime/debug/panic_test.go`
- ✅ `src/runtime/panic.go`
- ❌ `src/runtime/runtime.go`
- ✅ `src/runtime/signal_unix.go`


### 📊 **Proposal #46258 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.0% | 50.0% | 13.8% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/syscall/exec_freebsd.go`
- `src/syscall/exec_pdeathsig_test.go`
- `src/syscall/syscall_freebsd_test.go`
- `src/syscall/syscall_linux_test.go`

**Predicted Files (25):**
- ❌ `go/internal/base/signal.go`
- ❌ `go/internal/base/signal_notunix.go`
- ❌ `go/internal/base/signal_unix.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_freebsd.go`
- ❌ `src/os/exec/exec_unix.go`
- ❌ `src/os/signal/signal.go`
- ❌ `src/os/signal/signal_freebsd.go`
- ❌ `src/os/signal/signal_unix.go`
- ❌ `src/sys/syscall_freebsd.go`
- ❌ `src/syscall/defs_linux.go`
- ❌ `src/syscall/defs_linux_amd64.go`
- ❌ `src/syscall/defs_linux_arm.go`
- ❌ `src/syscall/defs_linux_arm64.go`
- ❌ `src/syscall/defs_linux_mips64x.go`
- ❌ `src/syscall/defs_linux_mipsx.go`
- ❌ `src/syscall/defs_linux_ppc64x.go`
- ❌ `src/syscall/defs_linux_riscv64.go`
- ❌ `src/syscall/defs_linux_s390x.go`
- ✅ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/getrandom_freebsd.go`
- ❌ `src/syscall/kernel_version_freebsd.go`
- ❌ `src/syscall/syscall_freebsd.go`
- ✅ `src/syscall/syscall_freebsd_test.go`
- ❌ `src/syscall/sysnum_freebsd.go`


### 📊 **Proposal #51430 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.9% | 3.4% | 4.3% | 1/29 |

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

**Predicted Files (17):**
- ✅ `src/cmd/compile/internal/coverage/cover.go`
- ❌ `src/cmd/cover/cover.go`
- ❌ `src/cmd/cover/cover_test.go`
- ❌ `src/cmd/cover/profile.go`
- ❌ `src/cmd/cover/testdata/html/html.go`
- ❌ `src/cmd/cover/testdata/html/html_test.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/a/a.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/a/a_test.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/noFuncsNoTests/nfnt.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/yesFuncsNoTests/yfnt.go`
- ❌ `src/coverage/emit.go`
- ❌ `src/coverage/encode.go`
- ❌ `src/coverage/merge.go`
- ❌ `src/coverage/test/counter_test.go`
- ❌ `src/coverage/test/roundtrip_test.go`
- ❌ `src/runtime/coverage/coverage.go`
- ❌ `src/testing/cover.go`


### 📊 **Proposal #46308 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/tls_test.go`

**Predicted Files (4):**
- ❌ `src/crypto/tls/tls.go`
- ✅ `src/crypto/tls/tls_test.go`
- ❌ `src/crypto/tls/version.go`
- ❌ `src/crypto/tls/version_test.go`


### 📊 **Proposal #37033 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/link/internal/ld/lib.go`
- `src/runtime/cgo/handle.go`
- `src/runtime/cgo/handle_test.go`

**Predicted Files (4):**
- ❌ `src/runtime/cgo/cgo.go`
- ✅ `src/runtime/cgo/handle.go`
- ✅ `src/runtime/cgo/handle_test.go`
- ❌ `src/runtime/runtime.go`


### 📊 **Proposal #51766 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/netip/netip_test.go`

**Predicted Files (2):**
- ❌ `src/net/net.go`
- ❌ `src/net/netip/netip.go`


### 📊 **Proposal #51684 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/regexp/syntax/parse.go`

**Predicted Files (2):**
- ❌ `src/regexp/regexp.go`
- ✅ `src/regexp/syntax/parse.go`


### 📊 **Proposal #51896 (File Level)**

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


### 📊 **Proposal #42088 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/run/run.go`
- `src/cmd/go/internal/work/build.go`

**Predicted Files (0):**


### 📊 **Proposal #19367 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/runtime/checkptr.go`
- `src/runtime/select.go`

**Predicted Files (5):**
- ❌ `src/unsafe.go`
- ❌ `src/unsafe/unsafe.go`
- ❌ `unsafe_slice_data.go`
- ❌ `unsafe_string.go`
- ❌ `unsafe_string_data.go`


### 📊 **Proposal #37168 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/rc4/rc4.go`
- `src/crypto/rc4/rc4_test.go`
- `src/image/image_test.go`

**Predicted Files (35):**
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
- ❌ `src/math/big/internal/asmgen/amd64.go`
- ❌ `src/math/big/internal/asmgen/arm.go`
- ❌ `src/math/big/internal/asmgen/arm64.go`
- ❌ `src/math/big/internal/asmgen/mips.go`
- ❌ `src/math/big/internal/asmgen/mips64.go`
- ❌ `src/math/big/internal/asmgen/s390x.go`
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
- ❌ `vendor/golang.org/x/crypto/internal/poly1305/mac_noasm.go`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305/poly1305.go`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305/sum_asm.go`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305/sum_generic.go`
- ❌ `vendor/golang.org/x/crypto/internal/poly1305/sum_s390x.go`


### 📊 **Proposal #29062 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/test/test.go`
- `src/cmd/objdump/objdump_test.go`
- `src/internal/testenv/testenv.go`

**Predicted Files (4):**
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/os_test.go`
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`


### 📊 **Proposal #43823 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/time/format.go`

**Predicted Files (6):**
- ❌ `src/strconv/decimal.go`
- ❌ `src/strconv/decimal_test.go`
- ✅ `src/time/format.go`
- ❌ `src/time/format_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`


### 📊 **Proposal #48157 (File Level)**

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

**Predicted Files (0):**


### 📊 **Proposal #32779 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 33.3% | 14.3% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/encoding/json/decode.go`
- `src/encoding/json/stream.go`
- `src/encoding/json/stream_test.go`

**Predicted Files (11):**
- ✅ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ❌ `src/encoding/json/decoder.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encoder.go`
- ❌ `src/encoding/json/internal.go`
- ❌ `src/encoding/json/json.go`
- ❌ `src/encoding/json/jsontext/decode.go`
- ❌ `src/encoding/json/jsontext/decode_test.go`
- ❌ `src/encoding/json/marshal.go`
- ❌ `src/encoding/json/unmarshal.go`


### 📊 **Proposal #46131 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/reflect/all_test.go`

**Predicted Files (15):**
- ❌ `interface/map.go`
- ❌ `interface/mapimp.go`
- ❌ `interface/maps.go`
- ❌ `interface/mapsimp.go`
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`
- ❌ `src/reflect/map_noswiss.go`
- ❌ `src/reflect/map_noswiss_test.go`
- ❌ `src/reflect/map_swiss.go`
- ❌ `src/reflect/map_swiss_test.go`
- ❌ `src/runtime/maps/map.go`
- ❌ `src/runtime/maps/map_test.go`
- ❌ `src/types/map.go`
- ❌ `test/map.go`
- ❌ `test/stress/maps.go`


### 📊 **Proposal #51225 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/base/flag.go`
- `src/cmd/compile/internal/noder/import.go`
- `src/cmd/go/internal/work/gc.go`

**Predicted Files (20):**
- ❌ `cmd/compile/flags/flags.go`
- ❌ `cmd/compile/internal/importer/gcimporter.go`
- ❌ `cmd/compile/internal/importer/gcimporter_test.go`
- ❌ `cmd/compile/main.go`
- ❌ `src/cmd/compile/internal/objabi/flag.go`
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
- ❌ `src/cmd/compile/internal/objfile/xcoff.go`
- ❌ `src/cmd/compile/internal/objfile/xcoff_test.go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`


### 📊 **Proposal #40025 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 16.7% | 26.7% | 2/12 |

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

**Predicted Files (3):**
- ✅ `src/io/io.go`
- ✅ `src/io/ioutil/ioutil.go`
- ❌ `src/io/ioutil/ioutil_test.go`


### 📊 **Proposal #47527 (File Level)**

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


### 📊 **Proposal #37974 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/ast/ast.go`
- `src/go/ast/ast_test.go`

**Predicted Files (7):**
- ❌ `directive.go`
- ❌ `directive2.go`
- ❌ `src/go/doc.go`
- ❌ `src/go/doc/comment.go`
- ❌ `src/go/doc/doc.go`
- ❌ `src/go/doc/print.go`
- ❌ `src/runtime/doc.go`


### 📊 **Proposal #37776 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 66.7% | 50.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/net/url/example_test.go`
- `src/net/url/url.go`
- `src/net/url/url_test.go`

**Predicted Files (5):**
- ❌ `src/net/url.go`
- ✅ `src/net/url/url.go`
- ✅ `src/net/url/url_test.go`
- ❌ `web/url.go`
- ❌ `web/url_test.go`


### 📊 **Proposal #40357 (File Level)**

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

**Predicted Files (2):**
- ❌ `cmd/go/modfile.go`
- ❌ `cmd/go/modload.go`


### 📊 **Proposal #39557 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 100.0% | 60.0% | 3/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/flag/example_func_test.go`
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (7):**
- ❌ `go/internal/cmdflag/flag.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/flag/example_flagset_test.go`
- ✅ `src/flag/example_func_test.go`
- ❌ `src/flag/example_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`


### 📊 **Proposal #35804 (File Level)**

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


### 📊 **Proposal #53003 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 5.9% | 9.1% | 1/17 |

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

**Predicted Files (5):**
- ❌ `src/runtime/unsafe.go`
- ✅ `src/unsafe/unsafe.go`
- ❌ `unsafe_slice_data.go`
- ❌ `unsafe_string.go`
- ❌ `unsafe_string_data.go`


### 📊 **Proposal #40281 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- `src/reflect/type.go`

**Predicted Files (4):**
- ❌ `src/cmd/vet/testdata/structtag/structtag.go`
- ❌ `src/encoding/json/tags.go`
- ❌ `src/encoding/json/tags_test.go`
- ❌ `src/reflect/reflect.go`


### 📊 **Proposal #41563 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 12.5% | 15.4% | 1/8 |

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

**Predicted Files (5):**
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/type.go`
- ❌ `src/reflect/value.go`
- ❌ `src/reflectlite/type.go`
- ❌ `src/reflectlite/value.go`


### 📊 **Proposal #46121 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/html/template/template.go`

**Predicted Files (5):**
- ✅ `src/html/template/template.go`
- ❌ `src/html/template/template_test.go`
- ❌ `src/text/template/exec.go`
- ❌ `src/text/template/funcs.go`
- ❌ `src/text/template/template.go`


### 📊 **Proposal #43947 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 12.5% | 12.5% | 1/8 |

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

**Predicted Files (8):**
- ❌ `src/cmd/internal/objabi/exec_windows.go`
- ❌ `src/cmd/internal/objabi/os_windows.go`
- ✅ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_windows.go`
- ❌ `src/os/exec/exec_windows_test.go`
- ❌ `src/syscall/exec_windows.go`
- ❌ `src/syscall/exec_windows_test.go`
- ❌ `src/syscall/execenv/windows/exec_windows_test.go`


### 📊 **Proposal #50860 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 40.0% | 28.6% | 2/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/compile/internal/escape/utils.go`
- `src/cmd/compile/internal/test/inl_test.go`
- `src/cmd/compile/internal/types/size.go`
- `src/sync/atomic/atomic_test.go`
- `src/sync/atomic/type.go`

**Predicted Files (9):**
- ❌ `atomicload.go`
- ❌ `intrinsic_atomic.go`
- ❌ `src/runtime/atomic/atomic.go`
- ❌ `src/runtime/atomic/atomic_test.go`
- ❌ `src/sync/atomic/atomic.go`
- ✅ `src/sync/atomic/atomic_test.go`
- ❌ `src/sync/atomic/doc.go`
- ✅ `src/sync/atomic/type.go`
- ❌ `src/sync/atomic/value.go`


### 📊 **Proposal #52444 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (4):**
- ❌ `src/crypto/x509/pem_decrypt.go`
- ❌ `src/crypto/x509/pem_decrypt_test.go`
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`


### 📊 **Proposal #43724 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/internal/syscall/windows/zsyscall_windows.go`
- `src/syscall/mksyscall_windows.go`

**Predicted Files (22):**
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
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/objfile.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/os/exec.go`
- ❌ `src/os/exec/dot_test.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`


### 📊 **Proposal #41730 (File Level)**

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
- ❌ `go/internal/modfetch/codehost/git.go`
- ❌ `go/internal/modfetch/codehost/svn.go`
- ❌ `go/internal/vcs/git.go`
- ❌ `go/internal/vcs/svn.go`


### 📊 **Proposal #51668 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/fmt/print.go`
- `src/fmt/state_test.go`

**Predicted Files (3):**
- ❌ `src/fmt/format.go`
- ✅ `src/fmt/state_test.go`
- ❌ `src/types/fmt.go`


### 📊 **Proposal #41980 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/internal/diff/diff_test.go`
- `src/testing/example.go`

**Predicted Files (4):**
- ❌ `src/cmp/cmp.go`
- ❌ `src/cmp/cmp_test.go`
- ❌ `src/testing/example_test.go`
- ❌ `src/testing/run_example.go`


### 📊 **Proposal #41792 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (6):**
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`
- ❌ `test/fixedbugs/issue41736.go`
- ❌ `testing/flag_test.go`


### 📊 **Proposal #45453 (File Level)**

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

**Predicted Files (0):**


### 📊 **Proposal #40276 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modload/init.go`
- `src/cmd/go/internal/work/build.go`

**Predicted Files (0):**


### 📊 **Proposal #42322 (File Level)**

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


### 📊 **Proposal #42100 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.8% | 20.0% | 6.5% | 1/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `misc/ios/go_ios_exec.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/cmd/go/internal/work/init.go`
- `src/cmd/link/internal/ld/config.go`

**Predicted Files (26):**
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
- ❌ `src/go/goos/goos.go`
- ❌ `src/go/goos/zgoos_ios.go`
- ❌ `src/runtime/defs_darwin_amd64.go`
- ❌ `src/runtime/signal_darwin_amd64.go`
- ❌ `src/syscall/rlimit_darwin.go`
- ❌ `src/syscall/route_darwin.go`
- ❌ `src/syscall/syscall_darwin_amd64.go`
- ❌ `src/syscall/syscall_darwin_arm64.go`
- ❌ `src/syscall/zsysnum_darwin_amd64.go`
- ❌ `src/syscall/ztypes_darwin_amd64.go`
- ❌ `src/syscall/ztypes_darwin_arm64.go`


### 📊 **Proposal #37475 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 15.4% | 14.8% | 2/13 |

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
- ❌ `cmd/go/internal/modfetch/codehost/git.go`
- ❌ `cmd/go/internal/version/version.go`
- ❌ `cmd/go/internal/work/exec.go`
- ❌ `runtime/debug/buildinfo.go`
- ✅ `src/cmd/go/internal/load/pkg.go`
- ✅ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/go/internal/load/pkg.go`
- ❌ `src/go/internal/version/version.go`
- ❌ `src/go/internal/work/exec.go`
- ❌ `src/runtime/debug/buildinfo.go`
- ❌ `src/runtime/debug/debug.go`
- ❌ `src/runtime/debug/readbuildinfo.go`


### 📊 **Proposal #39567 (File Level)**

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


### 📊 **Proposal #44808 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 42.9% | 54.5% | 3/7 |

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
- ❌ `src/image/draw/bench_test.go`
- ✅ `src/image/draw/draw.go`
- ✅ `src/image/image.go`
- ✅ `src/image/image_test.go`


### 📊 **Proposal #45754 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 13.3% | 100.0% | 23.5% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/example_textvar_test.go`
- `src/flag/flag.go`

**Predicted Files (15):**
- ❌ `go/internal/cmdflag/flag.go`
- ❌ `src/encoding/text.go`
- ❌ `src/flag/example_flagset_test.go`
- ❌ `src/flag/example_func_test.go`
- ✅ `src/flag/example_textvar_test.go`
- ❌ `src/flag/example_value_test.go`
- ✅ `src/flag/flag.go`
- ❌ `src/flag/flag_test.go`
- ❌ `src/math/big/float.go`
- ❌ `src/math/big/int.go`
- ❌ `src/math/big/rat.go`
- ❌ `src/net/ip.go`
- ❌ `src/testing/flag_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`


### 📊 **Proposal #47651 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.8% | 7.3% | 10.5% | 3/41 |

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

**Predicted Files (16):**
- ❌ `interface/pointer.go`
- ❌ `interface/reflectmethod1.go`
- ❌ `interface/reflectmethod2.go`
- ❌ `interface/reflectmethod3.go`
- ❌ `interface/reflectmethod4.go`
- ❌ `interface/reflectmethod5.go`
- ❌ `interface/reflectmethod6.go`
- ❌ `interface/reflectmethod7.go`
- ❌ `interface/reflectmethod8.go`
- ✅ `src/reflect/abi.go`
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/type.go`
- ✅ `src/reflect/value.go`
- ❌ `src/runtime/reflectlite/type.go`
- ❌ `src/runtime/reflectlite/value.go`


### 📊 **Proposal #48052 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/debug/plan9obj/file.go`

**Predicted Files (2):**
- ❌ `src/debug/elf/elf.go`
- ✅ `src/debug/plan9obj/file.go`


### 📊 **Proposal #33920 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/io/ioutil/tempfile.go`
- `src/io/ioutil/tempfile_test.go`
- `src/os/os_test.go`

**Predicted Files (3):**
- ✅ `src/io/ioutil/tempfile.go`
- ✅ `src/io/ioutil/tempfile_test.go`
- ❌ `src/path/filepath/path.go`


### 📊 **Proposal #47209 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 50.0% | 57.1% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/cmd/go/internal/fsys/fsys_test.go`
- `src/io/fs/walk.go`
- `src/path/filepath/path.go`
- `src/path/filepath/path_test.go`

**Predicted Files (3):**
- ❌ `src/path/filepath/example_test.go`
- ✅ `src/path/filepath/path.go`
- ✅ `src/path/filepath/path_test.go`


### 📊 **Proposal #48152 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/net/http/transport_test.go`

**Predicted Files (12):**
- ✅ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_client_test.go`
- ❌ `src/crypto/tls/handshake_messages.go`
- ❌ `src/crypto/tls/handshake_messages_test.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/x509/verify.go`
- ❌ `src/crypto/x509/verify_test.go`
- ❌ `src/crypto/x509/x509.go`
- ❌ `src/crypto/x509/x509_test.go`
- ❌ `src/testtls/tls.go`
- ❌ `src/testtls/tls_test.go`


### 📊 **Proposal #41682 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 66.7% | 50.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/x509/verify_test.go`
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (5):**
- ❌ `src/crypto/x509/parser.go`
- ❌ `src/crypto/x509/parser_test.go`
- ❌ `src/crypto/x509/verify.go`
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`


### 📊 **Proposal #53200 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/token/position.go`
- `src/go/token/position_test.go`

**Predicted Files (6):**
- ❌ `src/go/token/file.go`
- ❌ `src/go/token/file_test.go`
- ✅ `src/go/token/position.go`
- ✅ `src/go/token/position_test.go`
- ❌ `src/go/token/token.go`
- ❌ `src/go/token/token_test.go`


### 📊 **Proposal #40082 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/database/sql/fakedb_test.go`
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`

**Predicted Files (2):**
- ❌ `src/database/sql/driver/types.go`
- ✅ `src/database/sql/sql.go`


### 📊 **Proposal #45963 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/test/testflag.go`
- `src/cmd/go/internal/work/exec.go`

**Predicted Files (21):**
- ❌ `src/cmd/go/analysis/internal/analysisflags/flags.go`
- ❌ `src/cmd/go/analysis/passes/assign/assign.go`
- ❌ `src/cmd/go/analysis/passes/atomic/atomic.go`
- ❌ `src/cmd/go/analysis/passes/cgocall/cgocall.go`
- ❌ `src/cmd/go/analysis/passes/composite/composite.go`
- ❌ `src/cmd/go/analysis/passes/defers/defers.go`
- ❌ `src/cmd/go/analysis/passes/hostport/hostport.go`
- ❌ `src/cmd/go/analysis/passes/httpresponse/httpresponse.go`
- ❌ `src/cmd/go/analysis/passes/ifaceassert/ifaceassert.go`
- ❌ `src/cmd/go/analysis/passes/loopclosure/loopclosure.go`
- ❌ `src/cmd/go/analysis/passes/lostcancel/lostcancel.go`
- ❌ `src/cmd/go/analysis/passes/nilfunc/nilfunc.go`
- ❌ `src/cmd/go/analysis/passes/print/print.go`
- ❌ `src/cmd/go/analysis/passes/printf/printf.go`
- ❌ `src/cmd/go/analysis/passes/shift/shift.go`
- ❌ `src/cmd/go/analysis/passes/sigchanyzer/sigchanyzer.go`
- ❌ `src/cmd/go/analysis/passes/structtag/structtag.go`
- ❌ `src/cmd/go/analysis/passes/testinggoroutine/testinggoroutine.go`
- ❌ `src/cmd/go/analysis/passes/unusedresult/unusedresult.go`
- ❌ `src/cmd/vet/vet.go`
- ❌ `src/cmd/vet/vetflag.go`


### 📊 **Proposal #46518 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 11.8% | 20.0% | 2/17 |

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
- ❌ `src/net/net.go`
- ✅ `src/net/netip/netip.go`
- ✅ `src/net/netip/netip_test.go`


### 📊 **Proposal #40337 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (4):**
- ❌ `src/crypto/dsa/dsa.go`
- ✅ `src/crypto/x509/x509.go`
- ❌ `vendor/golang.org/x/crypto/ssh/keys.go`
- ❌ `vendor/golang.org/x/crypto/x509/x509.go`


### 📊 **Proposal #45973 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/serve_test.go`
- `src/net/http/server.go`

**Predicted Files (6):**
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ✅ `src/net/http/server.go`
- ❌ `vendor/golang.org/x/net/http/httpguts/guts.go`
- ❌ `vendor/golang.org/x/net/http/httplex.go`


### 📊 **Proposal #49471 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/os_windows.go`
- `src/runtime/panic.go`
- `src/runtime/signal_windows.go`

**Predicted Files (8):**
- ❌ `internal/runtime/runtime.go`
- ❌ `src/runtime/crash.go`
- ❌ `src/runtime/crash_test.go`
- ❌ `src/runtime/runtime.go`
- ❌ `src/runtime/syscall/syscall_windows.go`
- ❌ `src/runtime/trace.go`
- ❌ `src/runtime/trace_test.go`
- ❌ `src/syscall/syscall_windows.go`


### 📊 **Proposal #52746 (File Level)**

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


### 📊 **Proposal #34293 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/doc/main.go`
- `src/cmd/doc/pkg.go`

**Predicted Files (11):**
- ❌ `cmd/go/doc.go`
- ❌ `go/doc/doc.go`
- ❌ `internal/lsp/cmd/definition.go`
- ❌ `internal/lsp/source/comment.go`
- ❌ `src/cmd/go/doc.go`
- ❌ `src/cmd/go/internal/doc/doc.go`
- ❌ `src/go/doc/comment.go`
- ❌ `src/go/doc/comment_test.go`
- ❌ `src/go/doc/doc.go`
- ❌ `src/go/doc/html.go`
- ❌ `src/go/doc/markdown.go`


### 📊 **Proposal #31804 (File Level)**

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


### 📊 **Proposal #43744 (File Level)**

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


### 📊 **Proposal #47916 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.0% | 50.0% | 15.3% | 10/20 |

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

**Predicted Files (111):**
- ❌ `src/go/types/alias.go`
- ❌ `src/go/types/api.go`
- ✅ `src/go/types/api_test.go`
- ❌ `src/go/types/array.go`
- ✅ `src/go/types/assignments.go`
- ❌ `src/go/types/badlinkname.go`
- ❌ `src/go/types/basic.go`
- ❌ `src/go/types/builtins.go`
- ✅ `src/go/types/call.go`
- ❌ `src/go/types/chan.go`
- ✅ `src/go/types/check.go`
- ✅ `src/go/types/context.go`
- ❌ `src/go/types/conversions.go`
- ✅ `src/go/types/decl.go`
- ❌ `src/go/types/errors.go`
- ❌ `src/go/types/eval.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/format.go`
- ❌ `src/go/types/gotype.go`
- ✅ `src/go/types/index.go`
- ❌ `src/go/types/infer.go`
- ✅ `src/go/types/instantiate.go`
- ❌ `src/go/types/interface.go`
- ❌ `src/go/types/named.go`
- ✅ `src/go/types/object.go`
- ❌ `src/go/types/operand.go`
- ❌ `src/go/types/pointer.go`
- ❌ `src/go/types/range.go`
- ❌ `src/go/types/return.go`
- ✅ `src/go/types/signature.go`
- ❌ `src/go/types/struct.go`
- ❌ `src/go/types/type.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/go/types/typeset.go`
- ❌ `src/go/types/union.go`
- ❌ `src/go/types/util.go`
- ❌ `src/go/types/version.go`
- ❌ `src/types/type.go`
- ❌ `src/types/types.go`
- ❌ `src/types/types2/typeparam.go`
- ❌ `typeparam/absdiffimp.dir/a.go`
- ❌ `typeparam/absdiffimp.dir/main.go`
- ❌ `typeparam/aliasimp.dir/a.go`
- ❌ `typeparam/aliasimp.dir/main.go`
- ❌ `typeparam/chansimp.dir/a.go`
- ❌ `typeparam/chansimp.dir/main.go`
- ❌ `typeparam/dedup.dir/a.go`
- ❌ `typeparam/dedup.dir/b.go`
- ❌ `typeparam/dedup.dir/c.go`
- ❌ `typeparam/dedup.dir/main.go`
- ❌ `typeparam/factimp.dir/a.go`
- ❌ `typeparam/factimp.dir/main.go`
- ❌ `typeparam/gencrawler.dir/a.go`
- ❌ `typeparam/gencrawler.dir/main.go`
- ❌ `typeparam/geninline.dir/a.go`
- ❌ `typeparam/geninline.dir/main.go`
- ❌ `typeparam/issue46461b.dir/a.go`
- ❌ `typeparam/issue46461b.dir/b.go`
- ❌ `typeparam/issue47514c.dir/a.go`
- ❌ `typeparam/issue47514c.dir/main.go`
- ❌ `typeparam/issue47892.dir/a.go`
- ❌ `typeparam/issue47892.dir/main.go`
- ❌ `typeparam/issue48094.dir/a.go`
- ❌ `typeparam/issue48094.dir/main.go`
- ❌ `typeparam/issue50121.dir/a.go`
- ❌ `typeparam/issue50121.dir/main.go`
- ❌ `typeparam/issue50437.dir/a.go`
- ❌ `typeparam/issue50437.dir/b.go`
- ❌ `typeparam/issue50481b.dir/b.go`
- ❌ `typeparam/issue50481b.dir/main.go`
- ❌ `typeparam/issue50481c.dir/a.go`
- ❌ `typeparam/issue50481c.dir/main.go`
- ❌ `typeparam/issue50552.dir/a.go`
- ❌ `typeparam/issue50552.dir/main.go`
- ❌ `typeparam/issue50561.dir/diameter.go`
- ❌ `typeparam/issue50561.dir/main.go`
- ❌ `typeparam/issue50598.dir/a0.go`
- ❌ `typeparam/issue50598.dir/a1.go`
- ❌ `typeparam/issue50598.dir/a2.go`
- ❌ `typeparam/issue50598.dir/main.go`
- ❌ `typeparam/issue50841.dir/a.go`
- ❌ `typeparam/issue50841.dir/b.go`
- ❌ `typeparam/issue51219.dir/a.go`
- ❌ `typeparam/issue51219.dir/main.go`
- ❌ `typeparam/issue51219b.dir/a.go`
- ❌ `typeparam/issue51219b.dir/b.go`
- ❌ `typeparam/issue51219b.dir/p.go`
- ❌ `typeparam/issue51250a.dir/a.go`
- ❌ `typeparam/issue51250a.dir/b.go`
- ❌ `typeparam/issue51250a.dir/main.go`
- ❌ `typeparam/issue51367.dir/a.go`
- ❌ `typeparam/issue51367.dir/main.go`
- ❌ `typeparam/issue51423.dir/a.go`
- ❌ `typeparam/issue51423.dir/b.go`
- ❌ `typeparam/issue51836.dir/a.go`
- ❌ `typeparam/issue51836.dir/aa.go`
- ❌ `typeparam/issue51836.dir/p.go`
- ❌ `typeparam/issue52117.dir/a.go`
- ❌ `typeparam/issue52117.dir/b.go`
- ❌ `typeparam/issue54302.dir/a.go`
- ❌ `typeparam/issue54302.dir/main.go`
- ❌ `typeparam/listimp.dir/a.go`
- ❌ `typeparam/listimp.dir/main.go`
- ❌ `typeparam/mapimp.dir/a.go`
- ❌ `typeparam/mapimp.dir/main.go`
- ❌ `typeparam/mapsimp.dir/a.go`
- ❌ `typeparam/mapsimp.dir/main.go`
- ❌ `typeparam/orderedmapsimp.dir/a.go`
- ❌ `typeparam/orderedmapsimp.dir/main.go`
- ❌ `typeparam/valimp.dir/a.go`
- ❌ `typeparam/valimp.dir/main.go`


### 📊 **Proposal #40356 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf/printf.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer/sigchanyzer.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods/stdmethods.go`

**Predicted Files (14):**
- ❌ `cmd/vet/vet.go`
- ❌ `src/cmd/vet/doc.go`
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/testdata/stdmethods/doc.go`
- ❌ `src/cmd/vet/testdata/stdmethods/stdmethods.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/errors/errors.go`
- ❌ `src/errors/errors_test.go`
- ❌ `src/errors/join.go`
- ❌ `src/errors/join_test.go`
- ❌ `src/errors/wrap.go`
- ❌ `src/errors/wrap_test.go`
- ❌ `src/fmt/errors.go`
- ❌ `src/fmt/errors_test.go`


### 📊 **Proposal #40034 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/smtp/smtp.go`
- `src/net/smtp/smtp_test.go`

**Predicted Files (3):**
- ❌ `src/net/smtp/auth.go`
- ✅ `src/net/smtp/smtp.go`
- ✅ `src/net/smtp/smtp_test.go`


### 📊 **Proposal #53002 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/net/http/httputil/example_test.go`
- `src/net/http/httputil/reverseproxy.go`
- `src/net/http/httputil/reverseproxy_test.go`

**Predicted Files (3):**
- ❌ `src/net/http/httputil/httputil.go`
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`


### 📊 **Proposal #44196 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/time.go`
- `src/time/time_test.go`

**Predicted Files (4):**
- ❌ `lib/time/mkzip.go`
- ❌ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ✅ `src/time/time.go`


### 📊 **Proposal #50465 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/httputil/reverseproxy.go`
- `src/net/http/httputil/reverseproxy_test.go`

**Predicted Files (3):**
- ❌ `src/net/http/httpproxy/proxy.go`
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`


### 📊 **Proposal #41696 (File Level)**

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

**Predicted Files (3):**
- ❌ `cmd/go`
- ❌ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`


### 📊 **Proposal #46336 (File Level)**

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
- ❌ `src/strings/iter.go`
- ❌ `src/strings/replace.go`
- ✅ `src/strings/strings.go`


### 📊 **Proposal #44011 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 16.7% | 13.3% | 1/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/os/exec/exec_windows_test.go`
- `src/os/file_windows.go`
- `src/syscall/exec_windows.go`
- `src/syscall/exec_windows_test.go`
- `src/syscall/syscall_windows.go`
- `src/syscall/zsyscall_windows.go`

**Predicted Files (9):**
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/exec_windows.go`
- ❌ `src/os/exec/internal/fdtest/exists_windows.go`
- ❌ `src/os/os_windows.go`
- ❌ `src/os/os_windows_test.go`
- ❌ `src/sys/syscall.go`
- ❌ `src/sys/syscall_windows.go`
- ❌ `src/syscall/security_windows.go`
- ✅ `src/syscall/syscall_windows.go`


### 📊 **Proposal #43620 (File Level)**

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


### 📊 **Proposal #48256 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/workcmd/edit.go`
- `src/cmd/go/internal/workcmd/init.go`
- `src/cmd/go/main.go`

**Predicted Files (4):**
- ❌ `go/work/edit.go`
- ❌ `go/work/init.go`
- ❌ `go/work/sync.go`
- ❌ `src/mod/internal/modfile/work.go`


### 📊 **Proposal #38017 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 25.0% | 28.6% | 1/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/time/export_test.go`
- `src/time/tzdata/tzdata.go`
- `src/time/tzdata_test.go`
- `src/time/zoneinfo_read.go`

**Predicted Files (3):**
- ❌ `lib/time/mkzip.go`
- ✅ `src/time/tzdata/tzdata.go`
- ❌ `src/time/tzdata/tzdata_test.go`


### 📊 **Proposal #50601 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/binary/binary.go`
- `src/encoding/binary/binary_test.go`

**Predicted Files (5):**
- ❌ `src/archive/tar/common.go`
- ❌ `src/archive/tar/reader.go`
- ❌ `src/archive/tar/writer.go`
- ✅ `src/encoding/binary/binary.go`
- ✅ `src/encoding/binary/binary_test.go`


### 📊 **Proposal #50842 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/io/io.go`
- `src/io/multi.go`
- `src/io/multi_test.go`

**Predicted Files (4):**
- ✅ `src/io/io.go`
- ✅ `src/io/multi.go`
- ❌ `src/io/multi_reader.go`
- ❌ `src/io/writer_to.go`


### 📊 **Proposal #41790 (File Level)**

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


### 📊 **Proposal #5901 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 50.0% | 30.8% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/encoding/json/bench_test.go`
- `src/encoding/json/decode.go`
- `src/encoding/json/encode.go`
- `src/encoding/json/stream.go`

**Predicted Files (9):**
- ✅ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decoder.go`
- ✅ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encoder.go`
- ❌ `src/encoding/json/example_marshaling_test.go`
- ❌ `src/encoding/json/example_test.go`
- ❌ `src/encoding/json/internal.go`
- ❌ `src/syscall/js/js.go`
- ❌ `src/syscall/js/js_test.go`


### 📊 **Proposal #52792 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modfetch/fetch.go`
- `src/cmd/go/internal/modload/build.go`

**Predicted Files (1):**
- ❌ `src/cmd/go/internal/modinfo/info.go`


### 📊 **Proposal #28308 (File Level)**

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

**Predicted Files (4):**
- ❌ `src/cmd/vet/hostport/hostport.go`
- ❌ `src/net.go`
- ❌ `src/net/dial.go`
- ❌ `src/net/net.go`


### 📊 **Proposal #44006 (File Level)**

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


### 📊 **Proposal #53021 (File Level)**

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
- ❌ `src/crypto/cipher/xor_generic.go`
- ❌ `src/crypto/subtle/subtle.go`
- ✅ `src/crypto/subtle/xor.go`
- ❌ `src/crypto/subtle/xor_generic.go`


### 📊 **Proposal #49580 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 14.3% | 19.0% | 2/14 |

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

**Predicted Files (7):**
- ❌ `src/archive/zip/reader.go`
- ❌ `src/archive/zip/writer.go`
- ❌ `src/archive/zip/zip_test.go`
- ❌ `src/io/fs/fsys.go`
- ✅ `src/io/fs/readlink.go`
- ✅ `src/io/fs/readlink_test.go`
- ❌ `src/path/filepath/symlink.go`


### 📊 **Proposal #53015 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 14.3% | 16.7% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/html/template/escape.go`
- `src/html/template/escape_test.go`
- `src/text/template/exec.go`
- `src/text/template/parse/lex.go`
- `src/text/template/parse/lex_test.go`
- `src/text/template/parse/node.go`
- `src/text/template/parse/parse.go`

**Predicted Files (5):**
- ❌ `interface/returntype.go`
- ❌ `src/html/template/template.go`
- ❌ `src/html/template/template_test.go`
- ✅ `src/text/template/exec.go`
- ❌ `src/text/template/template.go`


### 📊 **Proposal #41048 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/transport.go`
- `src/net/http/transport_test.go`

**Predicted Files (4):**
- ✅ `src/net/http/transport.go`
- ✅ `src/net/http/transport_test.go`
- ❌ `vendor/golang.org/x/net/http/httpguts/guts.go`
- ❌ `vendor/golang.org/x/net/http/httpproxy/proxy.go`


### 📊 **Proposal #48409 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 7.1% | 10.5% | 2/28 |

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

**Predicted Files (10):**
- ❌ `src/runtime/debug/debug.go`
- ✅ `src/runtime/debug/garbage.go`
- ❌ `src/runtime/debug/garbage_test.go`
- ❌ `src/runtime/debug/heapdump_test.go`
- ❌ `src/runtime/debug/mod.go`
- ❌ `src/runtime/debug/mod_test.go`
- ❌ `src/runtime/debug/panic_test.go`
- ❌ `src/runtime/debug/stack.go`
- ❌ `src/runtime/debug/stack_test.go`
- ✅ `src/runtime/debug/stubs.go`


### 📊 **Proposal #42102 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 16.7% | 28.6% | 1/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/time/format.go`
- `src/time/time.go`
- `src/time/time_test.go`
- `src/time/zoneinfo.go`
- `src/time/zoneinfo_read.go`
- `src/time/zoneinfo_test.go`

**Predicted Files (1):**
- ✅ `src/time/zoneinfo.go`


### 📊 **Proposal #39904 (File Level)**

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


### 📊 **Proposal #42027 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 16.7% | 25.0% | 3/18 |

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

**Predicted Files (6):**
- ❌ `src/fmt/fmt.go`
- ✅ `src/io/fs/walk.go`
- ❌ `src/path/filepath/example_test.go`
- ❌ `src/path/filepath/export_test.go`
- ✅ `src/path/filepath/path.go`
- ✅ `src/path/filepath/path_test.go`


### 📊 **Proposal #27628 (File Level)**

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


### 📊 **Proposal #51868 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/debug/pe/symbol.go`
- `src/debug/pe/symbols_test.go`

**Predicted Files (5):**
- ❌ `src/debug/pe/file.go`
- ❌ `src/debug/pe/pe.go`
- ❌ `src/debug/pe/section.go`
- ✅ `src/debug/pe/symbol.go`
- ❌ `src/runtime/debug/pe.go`


### 📊 **Proposal #28089 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/ast/ast.go`
- `src/go/ast/issues_test.go`

**Predicted Files (4):**
- ✅ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/parser_test.go`


### 📊 **Proposal #41773 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/serve_test.go`
- `src/net/http/server.go`

**Predicted Files (1):**
- ✅ `src/net/http/server.go`


### 📊 **Proposal #50674 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 33.3% | 20.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/x509/parser.go`
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (7):**
- ❌ `src/crypto/x509/pkix/pkix.go`
- ✅ `src/crypto/x509/x509.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/asn1.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/asn1/asn1.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/builder.go`
- ❌ `vendor/golang.org/x/crypto/cryptobyte/string.go`
- ❌ `vendor/golang.org/x/crypto/x509/pkix/pkix.go`


### 📊 **Proposal #26535 (File Level)**

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


### 📊 **Proposal #45964 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 9.5% | 15.4% | 2/21 |

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

**Predicted Files (5):**
- ❌ `src/internal/poll/sock_cloexec.go`
- ❌ `src/runtime/internal/atomic/sys_linux_arm.s`
- ✅ `src/syscall/exec_linux.go`
- ✅ `src/syscall/syscall_linux.go`
- ❌ `src/syscall/syscall_linux_test.go`


### 📊 **Proposal #39444 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/os/exec_unix.go`
- `src/os/exec_unix_test.go`

**Predicted Files (4):**
- ❌ `src/os/exec/exec_unix.go`
- ✅ `src/os/exec_unix.go`
- ❌ `src/os/signal/signal.go`
- ❌ `src/os/signal_unix.go`


### 📊 **Proposal #45430 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 12.5% | 16.7% | 1/8 |

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

**Predicted Files (4):**
- ✅ `src/crypto/tls/cipher_suites.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/testtls/tls.go`
- ❌ `src/testtls/tls_test.go`


### 📊 **Proposal #37533 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (10):**
- ❌ `cmd/flag.go`
- ❌ `internal/cmdflag/flag.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/testing/flag_test.go`
- ❌ `test/fixedbugs/issue37513.go`


### 📊 **Proposal #47781 (File Level)**

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

**Predicted Files (17):**
- ❌ `src/compile/internal/ir/type.go`
- ❌ `src/compile/internal/types/typeparam.go`
- ❌ `src/compile/internal/types/typeset.go`
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`
- ❌ `src/go/ast/inspector/inspector.go`
- ❌ `src/go/ast/inspector/iter.go`
- ❌ `src/go/ast/inspector/typeof.go`
- ❌ `src/go/ast/inspector/walk.go`
- ❌ `src/go/token/token.go`
- ❌ `src/go/token/token_test.go`
- ❌ `src/go/types/objectpath/objectpath.go`
- ❌ `src/go/types/typeutil/callee.go`
- ❌ `src/go/types/typeutil/imports.go`
- ❌ `src/go/types/typeutil/map.go`
- ❌ `src/go/types/typeutil/methodsetcache.go`
- ❌ `src/go/types/typeutil/ui.go`


### 📊 **Proposal #46057 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/cert_pool.go`
- `src/crypto/x509/cert_pool_test.go`

**Predicted Files (5):**
- ✅ `src/crypto/x509/cert_pool.go`
- ✅ `src/crypto/x509/cert_pool_test.go`
- ❌ `src/crypto/x509/example_test.go`
- ❌ `src/reflect/deepequal.go`
- ❌ `src/reflect/deepequal_test.go`


### 📊 **Proposal #43401 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/csv/reader.go`
- `src/encoding/csv/reader_test.go`

**Predicted Files (5):**
- ❌ `src/encoding/csv/csv.go`
- ✅ `src/encoding/csv/reader.go`
- ✅ `src/encoding/csv/reader_test.go`
- ❌ `src/encoding/csv/writer.go`
- ❌ `src/encoding/csv/writer_test.go`


### 📊 **Proposal #40728 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/24 |

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
- ❌ `cmd/go/modload/build.go`
- ❌ `cmd/go/modload/edit.go`
- ❌ `cmd/go/modload/help.go`
- ❌ `cmd/go/modload/import.go`
- ❌ `cmd/go/modload/list.go`
- ❌ `cmd/go/modload/load.go`
- ❌ `cmd/go/modload/modfile.go`
- ❌ `cmd/go/modload/mvs.go`
- ❌ `cmd/go/modload/query.go`
- ❌ `cmd/go/modload/search.go`
- ❌ `cmd/go/modload/vendor.go`


### 📊 **Proposal #43993 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`
- `src/text/template/exec.go`
- `src/text/template/funcs.go`

**Predicted Files (3):**
- ❌ `interface/equal.go`
- ❌ `src/reflect/deepequal.go`
- ❌ `src/reflect/reflect.go`


### 📊 **Proposal #50770 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/mono_test.go`
- `src/time/time.go`

**Predicted Files (4):**
- ❌ `src/runtime/time.go`
- ❌ `src/runtime/time_test.go`
- ✅ `src/time/time.go`
- ❌ `src/time/time_test.go`


### 📊 **Proposal #44221 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 100.0% | 16.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/csv/reader.go`
- `src/encoding/csv/reader_test.go`

**Predicted Files (22):**
- ❌ `src/archive/tar/reader.go`
- ❌ `src/archive/tar/reader_test.go`
- ❌ `src/archive/tar/writer.go`
- ❌ `src/archive/tar/writer_test.go`
- ❌ `src/archive/zip/reader.go`
- ❌ `src/archive/zip/reader_test.go`
- ❌ `src/archive/zip/writer.go`
- ❌ `src/archive/zip/writer_test.go`
- ❌ `src/bufio/bufio.go`
- ❌ `src/bufio/bufio_test.go`
- ❌ `src/bufio/scan.go`
- ❌ `src/bufio/scan_test.go`
- ❌ `src/bytes/bytes.go`
- ❌ `src/bytes/bytes_test.go`
- ❌ `src/bytes/reader.go`
- ❌ `src/bytes/reader_test.go`
- ❌ `src/encoding/csv/csv.go`
- ❌ `src/encoding/csv/line_reader.go`
- ✅ `src/encoding/csv/reader.go`
- ✅ `src/encoding/csv/reader_test.go`
- ❌ `src/encoding/csv/writer.go`
- ❌ `src/encoding/csv/writer_test.go`


### 📊 **Proposal #44143 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/http/socks_bundle.go`

**Predicted Files (2):**
- ❌ `src/context/context.go`
- ❌ `src/context/context_test.go`


### 📊 **Proposal #43931 (File Level)**

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

**Predicted Files (95):**
- ❌ `src/compile/internal/types2/typeparam.go`
- ❌ `src/compile/internal/types2/typeset.go`
- ❌ `src/compile/internal/types2/typeset_test.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `typeparam/absdiff.go`
- ❌ `typeparam/absdiff2.go`
- ❌ `typeparam/absdiff3.go`
- ❌ `typeparam/absdiffimp.go`
- ❌ `typeparam/absdiffimp2.go`
- ❌ `typeparam/fact.go`
- ❌ `typeparam/factimp.go`
- ❌ `typeparam/gencrawler.go`
- ❌ `typeparam/genembed.go`
- ❌ `typeparam/genembed2.go`
- ❌ `typeparam/geninline.go`
- ❌ `typeparam/issue48185a.go`
- ❌ `typeparam/issue48185b.go`
- ❌ `typeparam/issue48280.go`
- ❌ `typeparam/issue48306.go`
- ❌ `typeparam/issue48337a.go`
- ❌ `typeparam/issue48337b.go`
- ❌ `typeparam/issue48454.go`
- ❌ `typeparam/issue48462.go`
- ❌ `typeparam/issue48537.go`
- ❌ `typeparam/issue48538.go`
- ❌ `typeparam/issue48602.go`
- ❌ `typeparam/issue48604.go`
- ❌ `typeparam/issue48609.go`
- ❌ `typeparam/issue48645a.go`
- ❌ `typeparam/issue48645b.go`
- ❌ `typeparam/issue48711.go`
- ❌ `typeparam/issue48716.go`
- ❌ `typeparam/issue48962.go`
- ❌ `typeparam/issue49027.go`
- ❌ `typeparam/issue49241.go`
- ❌ `typeparam/issue49246.go`
- ❌ `typeparam/issue49524.go`
- ❌ `typeparam/issue49536.go`
- ❌ `typeparam/issue49538.go`
- ❌ `typeparam/issue49547.go`
- ❌ `typeparam/issue49611.go`
- ❌ `typeparam/issue49659.go`
- ❌ `typeparam/issue49667.go`
- ❌ `typeparam/issue49893.go`
- ❌ `typeparam/issue50121.go`
- ❌ `typeparam/issue50121b.go`
- ❌ `typeparam/issue50437.go`
- ❌ `typeparam/issue50481b.go`
- ❌ `typeparam/issue50481c.go`
- ❌ `typeparam/issue50485.go`
- ❌ `typeparam/issue50486.go`
- ❌ `typeparam/issue50552.go`
- ❌ `typeparam/issue50561.go`
- ❌ `typeparam/issue50598.go`
- ❌ `typeparam/issue51219.go`
- ❌ `typeparam/issue51219b.go`
- ❌ `typeparam/issue51232.go`
- ❌ `typeparam/issue51233.go`
- ❌ `typeparam/issue51236.go`
- ❌ `typeparam/issue51245.go`
- ❌ `typeparam/issue51250a.go`
- ❌ `typeparam/issue51303.go`
- ❌ `typeparam/issue51355.go`
- ❌ `typeparam/issue51367.go`
- ❌ `typeparam/issue51423.go`
- ❌ `typeparam/issue51521.go`
- ❌ `typeparam/issue51522a.go`
- ❌ `typeparam/issue51522b.go`
- ❌ `typeparam/issue51700.go`
- ❌ `typeparam/issue51765.go`
- ❌ `typeparam/issue51832.go`
- ❌ `typeparam/issue51836.go`
- ❌ `typeparam/issue51840.go`
- ❌ `typeparam/issue51909.go`
- ❌ `typeparam/issue51925.go`
- ❌ `typeparam/issue52026.go`
- ❌ `typeparam/issue52117.go`
- ❌ `typeparam/issue52124.go`
- ❌ `typeparam/issue52228.go`
- ❌ `typeparam/issue52241.go`
- ❌ `typeparam/issue53087.go`
- ❌ `typeparam/issue53254.go`
- ❌ `typeparam/issue53390.go`
- ❌ `typeparam/issue53406.go`
- ❌ `typeparam/issue53419.go`
- ❌ `typeparam/issue53477.go`
- ❌ `typeparam/issue54135.go`
- ❌ `typeparam/issue54225.go`
- ❌ `typeparam/issue54302.go`
- ❌ `typeparam/issue54456.go`
- ❌ `typeparam/issue54497.go`
- ❌ `typeparam/issue54535.go`
- ❌ `typeparam/issue54537.go`
- ❌ `typeparam/issue54765.go`
- ❌ `typeparam/issue55101.go`


### 📊 **Proposal #48294 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/reflect/all_test.go`

**Predicted Files (10):**
- ❌ `reflectmethod1.go`
- ❌ `reflectmethod2.go`
- ❌ `reflectmethod3.go`
- ❌ `reflectmethod4.go`
- ❌ `reflectmethod5.go`
- ❌ `reflectmethod6.go`
- ❌ `reflectmethod7.go`
- ❌ `reflectmethod8.go`
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`


### 📊 **Proposal #51428 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/error_test.go`
- `src/net/net.go`

**Predicted Files (5):**
- ❌ `src/context/context.go`
- ❌ `src/context/context_test.go`
- ❌ `src/net/dial.go`
- ❌ `src/net/error.go`
- ✅ `src/net/net.go`


### 📊 **Proposal #52463 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/gofmt/gofmt.go`
- `src/cmd/gofmt/simplify.go`

**Predicted Files (7):**
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`
- ❌ `src/go/ast/import.go`
- ❌ `src/go/ast/resolve.go`
- ❌ `src/go/ast/scope.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/types/types.go`


### 📊 **Proposal #51115 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/io/io.go`

**Predicted Files (5):**
- ✅ `src/io/io.go`
- ❌ `src/io/limited_reader.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`


### 📊 **Proposal #35567 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 40.0% | 50.0% | 2/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/go/build/deps_test.go`
- `src/runtime/debug/stack_test.go`
- `src/testing/benchmark.go`
- `src/testing/example.go`
- `src/testing/testing.go`

**Predicted Files (3):**
- ✅ `src/testing/benchmark.go`
- ❌ `src/testing/benchmark_test.go`
- ✅ `src/testing/testing.go`


### 📊 **Proposal #40255 (File Level)**

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

**Predicted Files (23):**
- ❌ `issue12970.go`
- ❌ `issue13923.go`
- ❌ `issue17357.go`
- ❌ `issue22429.go`
- ❌ `issue23536.go`
- ❌ `issue27516.go`
- ❌ `issue36400.go`
- ❌ `issue4798.go`
- ❌ `src/compile/internal/abi/abiutils.go`
- ❌ `src/compile/internal/abi/abiutils_test.go`
- ❌ `src/compile/internal/softfloat.go`
- ❌ `src/runtime/atomic/atomic_386.go`
- ❌ `src/runtime/goarch/goarch_386.go`
- ❌ `src/runtime/signal_386.go`
- ❌ `src/runtime/stubs_386.go`
- ❌ `src/runtime/syscall/defs_linux_386.go`
- ❌ `src/syscall/syscall_freebsd_386.go`
- ❌ `src/syscall/syscall_linux_386.go`
- ❌ `src/syscall/syscall_openbsd_386.go`
- ❌ `src/syscall/syscall_plan9_386.go`
- ❌ `src/syscall/types_windows_386.go`
- ❌ `src/syscall/zerrors_linux_386.go`
- ❌ `src/syscall/zsyscall_linux_386.go`


### 📊 **Proposal #46648 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 2.8% | 100.0% | 5.4% | 3/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/go/types/check.go`
- `src/go/types/check_test.go`
- `src/go/types/stdlib_test.go`

**Predicted Files (108):**
- ❌ `src/cmd/internal/types2/types.go`
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
- ❌ `src/types/goversion.go`
- ❌ `src/types/types.go`
- ❌ `src/types/types2/api.go`


### 📊 **Proposal #53346 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 100.0% | 36.4% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/xml/marshal.go`
- `src/encoding/xml/marshal_test.go`

**Predicted Files (9):**
- ❌ `src/archive/tar/writer.go`
- ❌ `src/archive/tar/writer_test.go`
- ❌ `src/archive/zip/writer.go`
- ❌ `src/archive/zip/writer_test.go`
- ❌ `src/encoding/xml/encoder.go`
- ❌ `src/encoding/xml/encoder_test.go`
- ✅ `src/encoding/xml/marshal.go`
- ✅ `src/encoding/xml/marshal_test.go`
- ❌ `src/encoding/xml/xml.go`


### 📊 **Proposal #40127 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/json/indent.go`
- `src/encoding/json/stream.go`

**Predicted Files (17):**
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
- ❌ `src/encoding/json/internal/jsonwire/encode_test.go`
- ❌ `src/encoding/json/internal/jsonwire/wire.go`
- ❌ `src/encoding/json/internal/jsonwire/wire_test.go`
- ❌ `src/encoding/json/jsontext/encode.go`
- ❌ `src/encoding/json/jsontext/encode_test.go`
- ❌ `src/encoding/json/jsontext/token.go`
- ❌ `src/encoding/json/jsontext/token_test.go`


### 📊 **Proposal #51082 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 3.2% | 4.8% | 4/125 |

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

**Predicted Files (40):**
- ❌ `go/doc/doc.go`
- ❌ `gofmt/doc.go`
- ❌ `gofmt/gofmt.go`
- ❌ `gofmt/printer.go`
- ❌ `src/cmd/internal/objabi/doc.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/funcid.go`
- ❌ `src/cmd/internal/objabi/head.go`
- ❌ `src/cmd/internal/objabi/line.go`
- ❌ `src/cmd/internal/objabi/path.go`
- ❌ `src/cmd/internal/objabi/reloctype.go`
- ❌ `src/cmd/internal/objabi/stack.go`
- ❌ `src/cmd/internal/objabi/symkind.go`
- ❌ `src/cmd/internal/objabi/symkind_string.go`
- ❌ `src/cmd/internal/objabi/util.go`
- ❌ `src/cmd/internal/objfile/doc.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/elf_test.go`
- ❌ `src/cmd/internal/objfile/flag_test.go`
- ❌ `src/cmd/internal/objfile/funcid_test.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/line_test.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/macho_test.go`
- ❌ `src/cmd/internal/objfile/path_test.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/pe_test.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/plan9obj_test.go`
- ❌ `src/cmd/internal/objfile/reloctype_test.go`
- ❌ `src/cmd/internal/objfile/stack_test.go`
- ❌ `src/cmd/internal/objfile/symkind_test.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/cmd/internal/objfile/xcoff_test.go`
- ❌ `src/go/doc/comment/doc.go`
- ✅ `src/go/doc/comment/markdown.go`
- ✅ `src/go/doc/comment/parse.go`
- ✅ `src/go/doc/comment/print.go`
- ✅ `src/go/doc/doc.go`
- ❌ `src/net/http/doc.go`


### 📊 **Proposal #35833 (File Level)**

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


### 📊 **Proposal #45460 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/http/transport.go`

**Predicted Files (2):**
- ❌ `src/net/http/request.go`
- ✅ `src/net/http/transport.go`


### 📊 **Proposal #42387 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/io/fs/readdir.go`
- `src/io/fs/readdir_test.go`

**Predicted Files (5):**
- ❌ `src/io/fs/fs.go`
- ✅ `src/io/fs/readdir.go`
- ❌ `src/os/dir.go`
- ❌ `src/os/file.go`
- ❌ `src/os/stat.go`


### 📊 **Proposal #45454 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 2.6% | 33.3% | 4.8% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/cfg/cfg.go`
- `src/go/build/build.go`
- `src/internal/buildcfg/cfg.go`

**Predicted Files (39):**
- ❌ `cmd/go/internal/flags/flagdefs.go`
- ❌ `cmd/go/internal/flags/flagdefs_test.go`
- ❌ `cmd/go/internal/flags/flags.go`
- ❌ `cmd/go/internal/flags/flags_test.go`
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ❌ `src/cmd/internal/objabi/util.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/cmd/link/internal/amd64/ld.go`
- ❌ `src/cmd/link/internal/arm/ld.go`
- ❌ `src/cmd/link/internal/arm64/ld.go`
- ❌ `src/cmd/link/internal/ppc64/ld.go`
- ❌ `src/cmd/link/internal/riscv64/ld.go`
- ❌ `src/cmd/link/internal/s390x/ld.go`
- ❌ `src/cmd/link/internal/x86/ld.go`
- ❌ `src/cmd/link/testdata/deadcode/globalmap.go`
- ❌ `src/cmd/link/testdata/deadcode/ifacemethod.go`
- ❌ `src/cmd/link/testdata/deadcode/ifacemethod2.go`
- ❌ `src/cmd/link/testdata/deadcode/ifacemethod3.go`
- ❌ `src/cmd/link/testdata/deadcode/ifacemethod4.go`
- ❌ `src/cmd/link/testdata/deadcode/ifacemethod5.go`
- ❌ `src/cmd/link/testdata/deadcode/ifacemethod6.go`
- ❌ `src/cmd/link/testdata/deadcode/reflectcall.go`
- ❌ `src/cmd/link/testdata/deadcode/structof_funcof.go`
- ❌ `src/cmd/link/testdata/deadcode/typedesc.go`
- ✅ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/runtime/defs_linux.go`
- ❌ `src/runtime/defs_linux_amd64.go`
- ❌ `src/runtime/defs_linux_arm.go`
- ❌ `src/runtime/defs_linux_arm64.go`
- ❌ `src/runtime/defs_linux_ppc64.go`
- ❌ `src/runtime/defs_linux_ppc64le.go`
- ❌ `src/runtime/defs_linux_riscv64.go`
- ❌ `src/runtime/defs_linux_s390x.go`


### 📊 **Proposal #50436 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/os/exec/exec.go`
- `src/os/exec/exec_test.go`

**Predicted Files (5):**
- ✅ `src/os/exec/exec.go`
- ✅ `src/os/exec/exec_test.go`
- ❌ `src/os/exec_linux.go`
- ❌ `src/os/exec_linux_test.go`
- ❌ `src/os/exec_windows.go`


### 📊 **Proposal #44167 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 14.3% | 19.0% | 2/14 |

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

**Predicted Files (7):**
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `src/runtime/gc.go`
- ❌ `src/runtime/gc/malloc.go`
- ❌ `src/runtime/gc/scan.go`
- ❌ `src/runtime/gc/sizeclasses.go`
- ✅ `src/runtime/mgcpacer.go`
- ✅ `src/runtime/mgcpacer_test.go`


### 📊 **Proposal #39178 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/lookup.go`
- `src/net/lookup_test.go`

**Predicted Files (3):**
- ❌ `src/net/http/client.go`
- ✅ `src/net/lookup.go`
- ❌ `src/net/net.go`


### 📊 **Proposal #46287 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 57.1% | 36.4% | 44.4% | 4/11 |

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

**Predicted Files (7):**
- ✅ `src/crypto/x509/cert_pool.go`
- ❌ `src/crypto/x509/cert_pool_test.go`
- ❌ `src/crypto/x509/example_test.go`
- ✅ `src/crypto/x509/verify.go`
- ✅ `src/crypto/x509/verify_test.go`
- ❌ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`


### 📊 **Proposal #48257 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/cmd/go/internal/workcmd/use.go`

**Predicted Files (3):**
- ❌ `go/work/work.go`
- ❌ `go/work/work_test.go`
- ❌ `go/workcmd/use.go`


### 📊 **Proposal #46293 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/reflect/all_test.go`

**Predicted Files (17):**
- ❌ `reflectmethod1.go`
- ❌ `reflectmethod2.go`
- ❌ `reflectmethod3.go`
- ❌ `reflectmethod4.go`
- ❌ `reflectmethod5.go`
- ❌ `reflectmethod6.go`
- ❌ `reflectmethod7.go`
- ❌ `reflectmethod8.go`
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`
- ❌ `src/reflect/map_noswiss.go`
- ❌ `src/reflect/map_noswiss_test.go`
- ❌ `src/reflect/map_swiss.go`
- ❌ `src/reflect/map_swiss_test.go`
- ❌ `src/reflect/reflect.go`
- ❌ `src/runtime/maps/map.go`
- ❌ `src/runtime/maps/map_test.go`


### 📊 **Proposal #42026 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 3.1% | 5.8% | 6/194 |

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

**Predicted Files (14):**
- ❌ `src/io/fs/readdir.go`
- ❌ `src/io/fs/readdir_test.go`
- ❌ `src/io/fs/readfile.go`
- ❌ `src/io/fs/readfile_test.go`
- ✅ `src/io/ioutil/ioutil.go`
- ❌ `src/io/ioutil/ioutil_test.go`
- ❌ `src/os/exec/exec.go`
- ✅ `src/os/exec/exec_test.go`
- ✅ `src/os/file.go`
- ❌ `src/os/file_test.go`
- ❌ `src/os/os.go`
- ✅ `src/os/os_test.go`
- ✅ `src/os/tempfile.go`
- ✅ `src/os/tempfile_test.go`


### 📊 **Proposal #45435 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/sync/mutex.go`
- `src/sync/mutex_test.go`
- `src/sync/rwmutex.go`
- `src/sync/rwmutex_test.go`

**Predicted Files (8):**
- ❌ `src/net/http/h2_bundle.go`
- ❌ `src/net/http2/hpack/encode.go`
- ❌ `src/net/http2/hpack/hpack.go`
- ❌ `src/net/http2/hpack/huffman.go`
- ❌ `src/net/http2/hpack/static_table.go`
- ❌ `src/net/http2/hpack/tables.go`
- ✅ `src/sync/mutex.go`
- ✅ `src/sync/mutex_test.go`


### 📊 **Proposal #48187 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/version/version.go`
- `src/debug/buildinfo/buildinfo_test.go`

**Predicted Files (10):**
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `src/cgo/internal/testcarchive/testcarchive_test.go`
- ❌ `src/cgo/internal/testcshared/testcshared_test.go`
- ✅ `src/cmd/go/internal/version/version.go`
- ❌ `src/cmd/link/internal/ld/ar.go`
- ❌ `src/debug/buildinfo/buildinfo.go`
- ✅ `src/debug/buildinfo/buildinfo_test.go`
- ❌ `src/go/version/version.go`
- ❌ `test/fixedbugs/issue48185a.go`
- ❌ `test/fixedbugs/issue48185b.go`


### 📊 **Proposal #37519 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/modfetch/repo.go`
- `src/cmd/go/internal/modfetch/sumdb.go`
- `src/cmd/go/internal/modget/get.go`

**Predicted Files (8):**
- ❌ `cmd/go/internal/get/get.go`
- ❌ `cmd/go/internal/modget/get.go`
- ❌ `cmd/go/internal/modget/modget.go`
- ❌ `cmd/go/internal/modget/modget_test.go`
- ❌ `cmd/go/internal/modget/modindex.go`
- ❌ `cmd/go/internal/modget/modinfo.go`
- ❌ `cmd/go/internal/modget/query.go`
- ❌ `src/cmd/go/internal/get/get.go`


### 📊 **Proposal #38627 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/text/template/parse/parse.go`

**Predicted Files (7):**
- ❌ `src/html/template/template.go`
- ❌ `src/html/template/template_test.go`
- ❌ `src/text/template/option.go`
- ❌ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/lex_test.go`
- ✅ `src/text/template/parse/parse.go`
- ❌ `src/text/template/parse/parse_test.go`


### 📊 **Proposal #41260 (File Level)**

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


### 📊 **Proposal #44505 (File Level)**

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

**Predicted Files (1):**
- ❌ `test/fixedbugs/issue23536.go`


### 📊 **Proposal #50429 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/parser/parser.go`
- `src/go/parser/parser_test.go`

**Predicted Files (16):**
- ❌ `interface/embed.go`
- ❌ `interface/embed1.go`
- ❌ `interface/embed2.go`
- ❌ `interface/embed3.go`
- ❌ `interface/receiver.go`
- ❌ `interface/receiver1.go`
- ❌ `interface/struct.go`
- ❌ `interface/structinit.dir/a.go`
- ❌ `interface/structinit.dir/b.go`
- ❌ `interface/structinit.dir/main.go`
- ❌ `interface/structinit.go`
- ❌ `src/go/ast.go`
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`
- ❌ `syntax/for.go`
- ❌ `syntax/typesw.go`


### 📊 **Proposal #53573 (File Level)**

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


### 📊 **Proposal #46059 (File Level)**

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


### 📊 **Proposal #42681 (File Level)**

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

**Predicted Files (4):**
- ❌ `cmd/compile`
- ❌ `cmd/go`
- ❌ `src/cmd/internal/objabi/util.go`
- ❌ `src/go/goexperiment/flags.go`


### 📊 **Proposal #40592 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 33.3% | 23.5% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/encoding/json/encode.go`
- `src/reflect/all_test.go`
- `src/reflect/deepequal.go`
- `src/reflect/set_test.go`
- `src/reflect/type.go`
- `src/reflect/value.go`

**Predicted Files (11):**
- ❌ `issue23536.go`
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


### 📊 **Proposal #51644 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/binary/varint.go`
- `src/encoding/binary/varint_test.go`

**Predicted Files (4):**
- ❌ `src/encoding/binary/binary.go`
- ❌ `src/encoding/binary/binary_test.go`
- ✅ `src/encoding/binary/varint.go`
- ✅ `src/encoding/binary/varint_test.go`


### 📊 **Proposal #34527 (File Level)**

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

**Predicted Files (5):**
- ❌ `cmd/go/modfetch/cache.go`
- ❌ `cmd/go/modfetch/fetch.go`
- ❌ `cmd/go/modfetch/proxy.go`
- ❌ `cmd/go/modfetch/repo.go`
- ❌ `cmd/go/modfetch/sumdb.go`


### 📊 **Proposal #45628 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/xml/xml.go`
- `src/encoding/xml/xml_test.go`

**Predicted Files (4):**
- ❌ `src/encoding/xml`
- ✅ `src/encoding/xml/xml.go`
- ✅ `src/encoding/xml/xml_test.go`
- ❌ `test/fixedbugs/issue45628.go`


### 📊 **Proposal #46746 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 50.0% | 14.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (12):**
- ❌ `interface/convert.go`
- ❌ `interface/convert1.go`
- ❌ `interface/convert2.go`
- ❌ `interface/convert3.go`
- ❌ `interface/convert4.go`
- ❌ `interface/receiver.go`
- ❌ `interface/receiver1.go`
- ❌ `interface/recursive.go`
- ❌ `interface/recursive1.go`
- ❌ `interface/struct.go`
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/value.go`


### 📊 **Proposal #44940 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/unicode/utf16/utf16.go`
- `src/unicode/utf16/utf16_test.go`

**Predicted Files (3):**
- ✅ `src/unicode/utf16/utf16.go`
- ✅ `src/unicode/utf16/utf16_test.go`
- ❌ `utf.go`


### 📊 **Proposal #41066 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.1% | 50.0% | 12.5% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/tls/conn.go`
- `src/crypto/tls/tls_test.go`

**Predicted Files (14):**
- ❌ `src/crypto/tls/alert.go`
- ❌ `src/crypto/tls/auth.go`
- ❌ `src/crypto/tls/cache.go`
- ❌ `src/crypto/tls/cipher_suites.go`
- ❌ `src/crypto/tls/common.go`
- ✅ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/net.go`
- ❌ `src/testtls/tls.go`
- ❌ `src/testtls/tls_test.go`
- ❌ `vendor/golang.org/x/net/net.go`


### 📊 **Proposal #41184 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 13.3% | 17.4% | 4/30 |

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

**Predicted Files (16):**
- ❌ `cmd/go/buildtag.go`
- ❌ `cmd/go/buildtag_test.go`
- ❌ `cmd/go/dist/buildtag.go`
- ❌ `cmd/go/dist/buildtag_test.go`
- ❌ `cmd/go/fix/buildtag.go`
- ❌ `cmd/go/fix/buildtag_test.go`
- ❌ `src/cmd/go/build.go`
- ❌ `src/cmd/go/parse.go`
- ❌ `src/cmd/go/vet.go`
- ✅ `src/go/build/build.go`
- ✅ `src/go/build/build_test.go`
- ❌ `src/go/build/constraint.go`
- ✅ `src/go/build/constraint/expr.go`
- ✅ `src/go/build/constraint/expr_test.go`
- ❌ `src/go/build/constraint/vers.go`
- ❌ `src/go/build/constraint/vers_test.go`


### 📊 **Proposal #48866 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/mime/mediatype.go`
- `src/mime/mediatype_test.go`

**Predicted Files (5):**
- ❌ `bytes/boundary_test.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/encode.go`
- ✅ `src/mime/mediatype.go`
- ✅ `src/mime/mediatype_test.go`


### 📊 **Proposal #50332 (File Level)**

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


### 📊 **Proposal #53466 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.4% | 20.0% | 17.4% | 2/10 |

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

**Predicted Files (13):**
- ❌ `src/asm/internal/arch/riscv64.go`
- ❌ `src/internal/cpu/cpu_riscv64.go`
- ❌ `src/internal/goos/goos.go`
- ❌ `src/internal/goos/zgoos_freebsd.go`
- ❌ `src/os/os_freebsd_riscv64.go`
- ✅ `src/runtime/defs_freebsd_riscv64.go`
- ❌ `src/runtime/signal_freebsd_riscv64.go`
- ❌ `src/sys/syscall_freebsd_riscv64.go`
- ❌ `src/sys/zerrors_freebsd_riscv64.go`
- ✅ `src/syscall/syscall_freebsd_riscv64.go`
- ❌ `src/syscall/sysnum_freebsd.go`
- ❌ `src/sysinfo/sysinfo.go`
- ❌ `src/sysinfo/sysinfo_test.go`


### 📊 **Proposal #49097 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 33.3% | 30.8% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/net/dial.go`
- `src/net/iprawsock.go`
- `src/net/net.go`
- `src/net/tcpsock.go`
- `src/net/udpsock.go`
- `src/net/unixsock.go`

**Predicted Files (7):**
- ❌ `src/net.go`
- ✅ `src/net/dial.go`
- ❌ `src/net/ip.go`
- ✅ `src/net/net.go`
- ❌ `src/net/netip/netip.go`
- ❌ `src/net/tcp.go`
- ❌ `src/net/udp.go`


### 📊 **Proposal #49390 (File Level)**

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

**Predicted Files (2):**
- ❌ `src/runtime/runtime.go`
- ❌ `src/runtime/runtime_test.go`


### 📊 **Proposal #39351 (File Level)**

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


### 📊 **Proposal #47142 (File Level)**

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


### 📊 **Proposal #46742 (File Level)**

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

**Predicted Files (31):**
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objfile/autotype.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/elf_test.go`
- ❌ `src/cmd/internal/objfile/flag_test.go`
- ❌ `src/cmd/internal/objfile/funcid.go`
- ❌ `src/cmd/internal/objfile/goobj.go`
- ❌ `src/cmd/internal/objfile/head.go`
- ❌ `src/cmd/internal/objfile/line.go`
- ❌ `src/cmd/internal/objfile/line_test.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/macho_test.go`
- ❌ `src/cmd/internal/objfile/objfile.go`
- ❌ `src/cmd/internal/objfile/path.go`
- ❌ `src/cmd/internal/objfile/path_test.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/pe_test.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/plan9obj_test.go`
- ❌ `src/cmd/internal/objfile/reloctype.go`
- ❌ `src/cmd/internal/objfile/reloctype_string.go`
- ❌ `src/cmd/internal/objfile/stack.go`
- ❌ `src/cmd/internal/objfile/stack_test.go`
- ❌ `src/cmd/internal/objfile/symkind.go`
- ❌ `src/cmd/internal/objfile/symkind_string.go`
- ❌ `src/cmd/internal/objfile/util.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/cmd/internal/objfile/xcoff_test.go`
- ❌ `src/runtime/unsafe.go`
- ❌ `src/unsafe/unsafe.go`
- ❌ `unsafe_slice_data.go`


### 📊 **Proposal #46505 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/sha256/sha256.go`
- `src/crypto/sha512/sha512.go`

**Predicted Files (6):**
- ❌ `interface/convert.go`
- ❌ `interface/convert1.go`
- ❌ `interface/convert2.go`
- ❌ `interface/convert3.go`
- ❌ `interface/convert4.go`
- ❌ `interface/slices.go`


### 📊 **Proposal #52376 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (6):**
- ❌ `src/reflect/abi.go`
- ❌ `src/reflect/abi_test.go`
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/value.go`


### 📊 **Proposal #44815 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/bufio/bufio.go`
- `src/bufio/bufio_test.go`

**Predicted Files (8):**
- ✅ `src/bufio/bufio.go`
- ✅ `src/bufio/bufio_test.go`
- ❌ `src/io/fs/fs.go`
- ❌ `src/io/fs/fs_test.go`
- ❌ `src/net/http/http.go`
- ❌ `src/net/http/request.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/transfer.go`


### 📊 **Proposal #45033 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.4% | 50.0% | 23.5% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/strconv/bytealg.go`
- `src/strconv/bytealg_bootstrap.go`
- `src/strconv/quote.go`
- `src/strconv/quote_test.go`

**Predicted Files (13):**
- ❌ `src/bufio/scan.go`
- ❌ `src/fmt/scan.go`
- ❌ `src/reflect/type.go`
- ❌ `src/strconv/atoi.go`
- ❌ `src/strconv/atoi_test.go`
- ✅ `src/strconv/quote.go`
- ✅ `src/strconv/quote_test.go`
- ❌ `src/strconv/quoted/quoted.go`
- ❌ `src/strconv/quoted/quoted_test.go`
- ❌ `src/strconv/strconv.go`
- ❌ `src/strconv/strconv_test.go`
- ❌ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/lex_test.go`


### 📊 **Proposal #48218 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/value.go`
- `src/reflect/visiblefields_test.go`

**Predicted Files (1):**
- ✅ `src/reflect/value.go`


### 📊 **Proposal #47066 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (2):**
- ❌ `src/reflect/reflect.go`
- ✅ `src/reflect/value.go`


### 📊 **Proposal #51572 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/dist/build.go`
- `src/cmd/go/internal/imports/build.go`
- `src/go/build/build.go`

**Predicted Files (46):**
- ❌ `doc/signal_notunix.go`
- ❌ `doc/signal_unix.go`
- ❌ `go/gofmt/gofmt_unix_test.go`
- ❌ `go/internal/base/error_unix.go`
- ❌ `go/internal/base/signal_unix.go`
- ❌ `go/internal/lockedfile/lockedfile_unix.go`
- ❌ `go/internal/mmap/mmap_unix.go`
- ❌ `go/internal/telemetrystats/version_unix.go`
- ❌ `go/internal/tool/path_unix.go`
- ❌ `go/internal/toolchain/umask_unix.go`
- ❌ `go/test/go_unix_test.go`
- ❌ `src/net/http/http_unix.go`
- ❌ `src/net/http/http_unix_test.go`
- ❌ `src/net/net_unix.go`
- ❌ `src/net/net_unix_test.go`
- ❌ `src/os/exec/exec_unix.go`
- ❌ `src/os/exec/exec_unix_test.go`
- ❌ `src/os/os_unix.go`
- ❌ `src/os/os_unix_test.go`
- ❌ `src/runtime/syscall/copy_file_range_unix.go`
- ❌ `src/runtime/syscall/errno_unix.go`
- ❌ `src/runtime/syscall/fcntl_unix.go`
- ❌ `src/runtime/syscall/net_unix.go`
- ❌ `src/runtime/syscall/renameat2_sysnum_linux.go`
- ❌ `src/runtime/syscall/renameat_sysnum_linux.go`
- ❌ `src/runtime/syscall/unix.go`
- ❌ `src/sync/atomic/atomic_unix.go`
- ❌ `src/sync/atomic/atomic_unix_test.go`
- ❌ `src/sys/unix/syscall_darwin.go`
- ❌ `src/sys/unix/syscall_freebsd.go`
- ❌ `src/sys/unix/syscall_linux.go`
- ❌ `src/sys/unix/syscall_netbsd.go`
- ❌ `src/sys/unix/syscall_openbsd.go`
- ❌ `src/sys/unix/syscall_unix.go`
- ❌ `src/syscall/env_unix.go`
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


### 📊 **Proposal #39057 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/log/log_test.go`

**Predicted Files (1):**
- ❌ `src/log/log.go`


### 📊 **Proposal #38781 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/net/http/transport_test.go`
- `src/testing/iotest/example_test.go`
- `src/testing/iotest/logger_test.go`
- `src/testing/iotest/reader.go`
- `src/testing/iotest/reader_test.go`

**Predicted Files (4):**
- ❌ `src/testing/iotest/iotest.go`
- ❌ `src/testing/iotest/iotest_test.go`
- ❌ `testing/iotest/reader.go`
- ❌ `testing/iotest/reader_test.go`


### 📊 **Proposal #36771 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/strconv/atoc.go`
- `src/strconv/atoc_test.go`
- `src/strconv/ctoa.go`

**Predicted Files (7):**
- ❌ `src/archive/tar/strconv.go`
- ❌ `src/archive/tar/strconv_test.go`
- ❌ `src/strconv/atof.go`
- ❌ `src/strconv/atoi.go`
- ❌ `src/strconv/atoi_test.go`
- ❌ `src/strconv/decimal.go`
- ❌ `src/strconv/ftoa.go`


### 📊 **Proposal #44435 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modcmd/download.go`
- `src/cmd/go/internal/modload/modfile.go`

**Predicted Files (2):**
- ❌ `go/internal/modcmd/download.go`
- ❌ `go/internal/modload/modfile.go`


### 📊 **Proposal #50101 (File Level)**

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
- ❌ `src/net.go`
- ❌ `src/net/http/server.go`
- ✅ `src/net/lookup.go`
- ✅ `src/net/lookup_unix.go`
- ✅ `src/net/lookup_windows.go`


### 📊 **Proposal #29770 (File Level)**

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


### 📊 **Proposal #51566 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 33.3% | 22.2% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/io/io.go`
- `src/io/io_test.go`
- `src/net/http/transfer.go`

**Predicted Files (6):**
- ❌ `src/bytes/bytes.go`
- ❌ `src/bytes/bytes_test.go`
- ❌ `src/bytes/reader.go`
- ❌ `src/bytes/reader_test.go`
- ✅ `src/io/io.go`
- ❌ `src/io/ioutil/ioutil.go`


### 📊 **Proposal #37196 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 14.3% | 18.2% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/compile/internal/ssagen/ssa.go`
- `src/cmd/compile/internal/typecheck/_builtin/runtime.go`
- `src/cmd/compile/internal/walk/builtin.go`
- `src/runtime/chan.go`
- `src/runtime/time.go`
- `src/time/sleep.go`
- `src/time/tick_test.go`

**Predicted Files (4):**
- ❌ `lib/time/`
- ✅ `src/time/sleep.go`
- ❌ `src/time/tick.go`
- ❌ `src/time/time.go`


### 📊 **Proposal #38079 (File Level)**

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


### 📊 **Proposal #51682 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 2.7% | 12.5% | 4.4% | 1/8 |

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

**Predicted Files (37):**
- ❌ `src/cmd/internal/objabi/flag.go`
- ❌ `src/cmd/internal/objabi/flag_test.go`
- ❌ `src/cmd/internal/objfile/elf.go`
- ❌ `src/cmd/internal/objfile/elf_test.go`
- ❌ `src/cmd/internal/objfile/macho.go`
- ❌ `src/cmd/internal/objfile/macho_test.go`
- ❌ `src/cmd/internal/objfile/objfile.go`
- ❌ `src/cmd/internal/objfile/pe.go`
- ❌ `src/cmd/internal/objfile/pe_test.go`
- ❌ `src/cmd/internal/objfile/plan9obj.go`
- ❌ `src/cmd/internal/objfile/plan9obj_test.go`
- ❌ `src/cmd/internal/objfile/testdata/fmthello.go`
- ❌ `src/cmd/internal/objfile/testdata/fmthellocgo.go`
- ❌ `src/cmd/internal/objfile/testdata/testdata.go`
- ❌ `src/cmd/internal/objfile/testdata/testfilenum/a.go`
- ❌ `src/cmd/internal/objfile/testdata/testfilenum/b.go`
- ❌ `src/cmd/internal/objfile/testdata/testfilenum/c.go`
- ❌ `src/cmd/internal/objfile/xcoff.go`
- ❌ `src/cmd/internal/objfile/xcoff_test.go`
- ❌ `src/go/types/alias.go`
- ❌ `src/go/types/api.go`
- ❌ `src/go/types/api_predicates.go`
- ❌ `src/go/types/builtins.go`
- ❌ `src/go/types/check.go`
- ❌ `src/go/types/decl.go`
- ❌ `src/go/types/errors.go`
- ❌ `src/go/types/expr.go`
- ❌ `src/go/types/generate.go`
- ❌ `src/go/types/instantiate.go`
- ✅ `src/go/types/object.go`
- ❌ `src/go/types/scope.go`
- ❌ `src/go/types/signature.go`
- ❌ `src/go/types/type.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/types.go`
- ❌ `src/types/object.go`
- ❌ `src/types/types.go`


### 📊 **Proposal #39214 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/12 |

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

**Predicted Files (23):**
- ❌ `src/internal/cpu/cpu.go`
- ❌ `src/runtime/cpu.go`
- ❌ `src/runtime/cpu/cpu.go`
- ❌ `src/runtime/cpu/cpu_arm.go`
- ❌ `src/runtime/cpu/cpu_arm64.go`
- ❌ `src/runtime/cpu/cpu_loong64.go`
- ❌ `src/runtime/cpu/cpu_mips.go`
- ❌ `src/runtime/cpu/cpu_ppc64x.go`
- ❌ `src/runtime/cpu/cpu_riscv64.go`
- ❌ `src/runtime/cpu/cpu_s390x.go`
- ❌ `src/runtime/cpu/cpu_x86.go`
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
- ❌ `src/syscall/syscall_linux_test.go`


### 📊 **Proposal #30715 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 50.0% | 22.2% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/request.go`
- `src/net/http/serve_test.go`

**Predicted Files (7):**
- ✅ `src/net/http/request.go`
- ❌ `src/net/http/request_test.go`
- ❌ `test/fixedbugs/issue41440.go`
- ❌ `test/fixedbugs/issue48094.go`
- ❌ `test/fixedbugs/issue48094b.go`
- ❌ `test/fixedbugs/issue48094c.go`
- ❌ `test/fixedbugs/issue48094d.go`


### 📊 **Proposal #51972 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 66.7% | 40.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/sync/map.go`
- `src/sync/map_reference_test.go`
- `src/sync/map_test.go`

**Predicted Files (7):**
- ❌ `map.go`
- ❌ `maps.go`
- ❌ `src/sync/hashtriemap.go`
- ❌ `src/sync/hashtriemap_test.go`
- ✅ `src/sync/map.go`
- ✅ `src/sync/map_test.go`
- ❌ `src/sync/mutex.go`


### 📊 **Proposal #50859 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/sync/cond.go`

**Predicted Files (127):**
- ❌ `interface/convert.go`
- ❌ `interface/convert1.go`
- ❌ `interface/convert2.go`
- ❌ `interface/convert3.go`
- ❌ `interface/convert4.go`
- ❌ `interface/convert5.go`
- ❌ `interface/convert6.go`
- ❌ `interface/convert7.go`
- ❌ `interface/convert8.go`
- ❌ `interface/escape.go`
- ❌ `interface/escape10.go`
- ❌ `interface/escape100.go`
- ❌ `interface/escape11.go`
- ❌ `interface/escape12.go`
- ❌ `interface/escape13.go`
- ❌ `interface/escape14.go`
- ❌ `interface/escape15.go`
- ❌ `interface/escape16.go`
- ❌ `interface/escape17.go`
- ❌ `interface/escape18.go`
- ❌ `interface/escape19.go`
- ❌ `interface/escape2.go`
- ❌ `interface/escape20.go`
- ❌ `interface/escape21.go`
- ❌ `interface/escape22.go`
- ❌ `interface/escape23.go`
- ❌ `interface/escape24.go`
- ❌ `interface/escape25.go`
- ❌ `interface/escape26.go`
- ❌ `interface/escape27.go`
- ❌ `interface/escape28.go`
- ❌ `interface/escape29.go`
- ❌ `interface/escape3.go`
- ❌ `interface/escape30.go`
- ❌ `interface/escape31.go`
- ❌ `interface/escape32.go`
- ❌ `interface/escape33.go`
- ❌ `interface/escape34.go`
- ❌ `interface/escape35.go`
- ❌ `interface/escape36.go`
- ❌ `interface/escape37.go`
- ❌ `interface/escape38.go`
- ❌ `interface/escape39.go`
- ❌ `interface/escape4.go`
- ❌ `interface/escape40.go`
- ❌ `interface/escape41.go`
- ❌ `interface/escape42.go`
- ❌ `interface/escape43.go`
- ❌ `interface/escape44.go`
- ❌ `interface/escape45.go`
- ❌ `interface/escape46.go`
- ❌ `interface/escape47.go`
- ❌ `interface/escape48.go`
- ❌ `interface/escape49.go`
- ❌ `interface/escape5.go`
- ❌ `interface/escape50.go`
- ❌ `interface/escape51.go`
- ❌ `interface/escape52.go`
- ❌ `interface/escape53.go`
- ❌ `interface/escape54.go`
- ❌ `interface/escape55.go`
- ❌ `interface/escape56.go`
- ❌ `interface/escape57.go`
- ❌ `interface/escape58.go`
- ❌ `interface/escape59.go`
- ❌ `interface/escape6.go`
- ❌ `interface/escape60.go`
- ❌ `interface/escape61.go`
- ❌ `interface/escape62.go`
- ❌ `interface/escape63.go`
- ❌ `interface/escape64.go`
- ❌ `interface/escape65.go`
- ❌ `interface/escape66.go`
- ❌ `interface/escape67.go`
- ❌ `interface/escape68.go`
- ❌ `interface/escape69.go`
- ❌ `interface/escape7.go`
- ❌ `interface/escape70.go`
- ❌ `interface/escape71.go`
- ❌ `interface/escape72.go`
- ❌ `interface/escape73.go`
- ❌ `interface/escape74.go`
- ❌ `interface/escape75.go`
- ❌ `interface/escape76.go`
- ❌ `interface/escape77.go`
- ❌ `interface/escape78.go`
- ❌ `interface/escape79.go`
- ❌ `interface/escape8.go`
- ❌ `interface/escape80.go`
- ❌ `interface/escape81.go`
- ❌ `interface/escape82.go`
- ❌ `interface/escape83.go`
- ❌ `interface/escape84.go`
- ❌ `interface/escape85.go`
- ❌ `interface/escape86.go`
- ❌ `interface/escape87.go`
- ❌ `interface/escape88.go`
- ❌ `interface/escape89.go`
- ❌ `interface/escape9.go`
- ❌ `interface/escape90.go`
- ❌ `interface/escape91.go`
- ❌ `interface/escape92.go`
- ❌ `interface/escape93.go`
- ❌ `interface/escape94.go`
- ❌ `interface/escape95.go`
- ❌ `interface/escape96.go`
- ❌ `interface/escape97.go`
- ❌ `interface/escape98.go`
- ❌ `interface/escape99.go`
- ❌ `interface/escape_runtime_atomic.go`
- ❌ `interface/escape_sync_atomic.go`
- ❌ `interface/receiver.go`
- ❌ `interface/receiver1.go`
- ❌ `interface/struct.go`
- ❌ `interface/structinit.go`
- ❌ `internal/runtime/sys/inlinegcpc.go`
- ❌ `src/runtime/atomic/atomic.go`
- ❌ `src/runtime/atomic/atomic_test.go`
- ❌ `src/runtime/race/race.go`
- ❌ `src/runtime/race/race_test.go`
- ❌ `src/runtime/sync/mutex.go`
- ❌ `src/runtime/sync/sync.go`
- ❌ `src/sync/atomic/atomic_test.go`
- ❌ `src/sync/atomic/doc.go`
- ❌ `src/sync/atomic/type.go`
- ❌ `src/sync/atomic/value.go`
- ❌ `src/sync/atomic/value_test.go`


### 📊 **Proposal #32406 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 25.0% | 40.0% | 3/12 |

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

**Predicted Files (3):**
- ✅ `src/crypto/tls/conn.go`
- ✅ `src/crypto/tls/tls.go`
- ✅ `src/net/http/server.go`


### 📊 **Proposal #35044 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/crypto/x509/cert_pool.go`

**Predicted Files (4):**
- ✅ `src/crypto/x509/cert_pool.go`
- ❌ `src/crypto/x509/cert_pool_test.go`
- ❌ `src/crypto/x509/example_test.go`
- ❌ `src/net/http/clone.go`


### 📊 **Proposal #45899 (File Level)**

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


### 📊 **Proposal #33232 (File Level)**

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


### 📊 **Proposal #47658 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 33.3% | 33.3% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (3):**
- ❌ `src/reflect/reflect.go`
- ❌ `src/reflect/type.go`
- ✅ `src/reflect/value.go`


### 📊 **Proposal #47609 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 66.7% | 33.3% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/unicode/utf8/utf8.go`
- `src/unicode/utf8/utf8_test.go`

**Predicted Files (9):**
- ❌ `append.go`
- ❌ `src/encoding/json/decode.go`
- ❌ `src/encoding/json/decode_test.go`
- ❌ `src/encoding/json/encode.go`
- ❌ `src/encoding/json/encode_test.go`
- ❌ `src/encoding/json/internal.go`
- ✅ `src/unicode/utf8/utf8.go`
- ✅ `src/unicode/utf8/utf8_test.go`
- ❌ `utf.go`


### 📊 **Proposal #38776 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 33.3% | 23.5% | 4/12 |

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

**Predicted Files (22):**
- ❌ `internal/hash/hash.go`
- ❌ `src/crypto/adler32/adler32.go`
- ❌ `src/crypto/adler32/adler32_test.go`
- ❌ `src/crypto/crc32/crc32.go`
- ❌ `src/crypto/crc32/crc32_test.go`
- ❌ `src/crypto/crc64/crc64.go`
- ❌ `src/crypto/crc64/crc64_test.go`
- ❌ `src/crypto/fnv/fnv.go`
- ❌ `src/crypto/fnv/fnv_test.go`
- ✅ `src/crypto/sha1/sha1.go`
- ✅ `src/crypto/sha1/sha1_test.go`
- ❌ `src/crypto/sha256/sha256.go`
- ✅ `src/crypto/sha256/sha256_test.go`
- ❌ `src/crypto/sha3/sha3.go`
- ❌ `src/crypto/sha3/sha3_test.go`
- ❌ `src/crypto/sha512/sha512.go`
- ✅ `src/crypto/sha512/sha512_test.go`
- ❌ `src/hash/adler32/adler32.go`
- ❌ `src/hash/crc32/crc32.go`
- ❌ `src/hash/crc64/crc64.go`
- ❌ `src/hash/fnv/fnv.go`
- ❌ `src/hash/hash.go`
