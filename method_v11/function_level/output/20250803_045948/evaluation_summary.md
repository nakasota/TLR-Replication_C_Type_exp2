# LLM Directory, File & Function-Level Evaluation Summary

## Directory-Level Macro Metrics

- **Number of Processed Proposals**: 210
- **Number of Proposals with at least one correct link (precision > 0)**: 195
- **Macro Precision**: 0.738
- **Macro Recall**: 0.699
- **Macro F1**: 0.671

## File-Level Macro Metrics

- **Number of Processed Proposals**: 210
- **Number of Proposals with at least one correct link (precision > 0)**: 184
- **Macro Precision**: 0.489
- **Macro Recall**: 0.517
- **Macro F1**: 0.460

## Function-Level Macro Metrics

- **Number of Processed Proposals**: 210
- **Number of Proposals with at least one correct link (precision > 0)**: 175
- **Macro Precision**: 0.261
- **Macro Recall**: 0.411
- **Macro F1**: 0.283


### 📊 **Proposal #51082 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 5.1% | 8.0% | 14/273 |

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

- **File:** `src/cmd/gofmt/gofmt.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `gofmtMain`
        - ❌ `processFile`
        - ❌ `writeFile`

- **File:** `src/cmd/internal/obj/riscv/obj.go`
    - Ground Truth Functions (1):
        - `stackOffset`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/x86/asm6.go`
    - Ground Truth Functions (1):
        - `regIndex`
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
    - Predicted Functions (2):
        - ✅ `ToHTML`
        - ✅ `ToText`

- **File:** `src/go/doc/comment/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/doc/comment/html.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `HTML`
        - ❌ `block`
        - ❌ `escape`
        - ❌ `text`

- **File:** `src/go/doc/comment/markdown.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Markdown`
        - ❌ `block`
        - ❌ `escape`
        - ❌ `rawText`
        - ❌ `text`

- **File:** `src/go/doc/comment/parse.go`
    - Ground Truth Functions (0):
    - Predicted Functions (22):
        - ❌ `BlankBefore`
        - ❌ `BlankBetween`
        - ❌ `DefaultLookupPackage`
        - ❌ `Parse`
        - ❌ `autoURL`
        - ❌ `block`
        - ❌ `docLink`
        - ❌ `heading`
        - ❌ `isHeading`
        - ❌ `isList`
        - ❌ `isOldHeading`
        - ❌ `list`
        - ❌ `listMarker`
        - ❌ `lookupPkg`
        - ❌ `oldHeading`
        - ❌ `paragraph`
        - ❌ `parseLink`
        - ❌ `parseLinkedText`
        - ❌ `parseSpans`
        - ❌ `parseText`
        - ❌ `splitDocName`
        - ❌ `text`

- **File:** `src/go/doc/comment/parse_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Test52353`

- **File:** `src/go/doc/comment/print.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `Comment`
        - ❌ `DefaultID`
        - ❌ `DefaultURL`
        - ❌ `block`
        - ❌ `docLinkURL`
        - ❌ `headingID`
        - ❌ `headingLevel`
        - ❌ `text`

- **File:** `src/go/doc/comment/std.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/go/doc/comment/std_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestStd`

- **File:** `src/go/doc/comment/testdata_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestTestdata`
        - ❌ `dump`
        - ❌ `dumpNL`
        - ❌ `dumpTo`

- **File:** `src/go/doc/comment/text.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Text`
        - ❌ `block`
        - ❌ `oneLongLine`
        - ❌ `text`
        - ❌ `wrap`
        - ❌ `wrapPenalty`

- **File:** `src/go/doc/comment/wrap_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestWrap`
        - ❌ `wrapSlow`

- **File:** `src/go/doc/comment_test.go`
    - Ground Truth Functions (1):
        - `TestComment`
    - Predicted Functions (1):
        - ✅ `TestComment`

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
    - Predicted Functions (1):
        - ✅ `formatDocComment`

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
    - Predicted Functions (4):
        - ❌ `Fprint`
        - ❌ `writeComment`
        - ✅ `writeCommentPrefix`
        - ✅ `writeCommentSuffix`

- **File:** `src/go/printer/printer_test.go`
    - Ground Truth Functions (2):
        - `TestLineComments`
        - `checkEqual`
    - Predicted Functions (6):
        - ❌ `TestBadComments`
        - ❌ `TestFiles`
        - ✅ `TestLineComments`
        - ❌ `check`
        - ❌ `format`
        - ❌ `testComment`

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


### 📊 **Proposal #50842 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 100.0% | 60.0% | 3/3 |

##### Ground Truth vs Predicted Functions per File

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
    - Predicted Functions (4):
        - ❌ `TestMultiReader`
        - ✅ `TestMultiReaderAsWriterTo`
        - ❌ `TestMultiReaderCopy`
        - ❌ `TestMultiReaderFlatten`


### 📊 **Proposal #51684 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/regexp/syntax/parse.go`
    - Ground Truth Functions (2):
        - `checkHeight`
        - `parse`
    - Predicted Functions (4):
        - ❌ `Error`
        - ❌ `calcHeight`
        - ✅ `checkHeight`
        - ❌ `checkLimits`

- **File:** `src/regexp/syntax/parse_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestParseInvalidRegexps`


### 📊 **Proposal #52444 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 100.0% | 75.0% | 3/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (1):
        - `CreateCertificate`
    - Predicted Functions (2):
        - ✅ `CreateCertificate`
        - ❌ `CreateRevocationList`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (2):
        - `TestCreateNegativeSerial`
        - `TestParseNegativeSerial`
    - Predicted Functions (3):
        - ✅ `TestCreateNegativeSerial`
        - ❌ `TestEmptySerialNumber`
        - ✅ `TestParseNegativeSerial`


### 📊 **Proposal #42387 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/io/fs/fs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `FileInfoToDirEntry`
        - ❌ `IsDir`
        - ❌ `IsRegular`
        - ❌ `Perm`
        - ❌ `String`
        - ❌ `Type`

- **File:** `src/io/fs/fs_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/io/fs/readdir.go`
    - Ground Truth Functions (5):
        - `FileInfoToDirEntry`
        - `Info`
        - `IsDir`
        - `Name`
        - `Type`
    - Predicted Functions (0):

- **File:** `src/io/fs/readdir_test.go`
    - Ground Truth Functions (1):
        - `TestFileInfoToDirEntry`
    - Predicted Functions (0):


### 📊 **Proposal #44940 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 66.7% | 36.4% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/unicode/utf16/utf16.go`
    - Ground Truth Functions (2):
        - `Encode`
        - `RuneLen`
    - Predicted Functions (4):
        - ❌ `DecodeRune`
        - ❌ `EncodeRune`
        - ❌ `IsSurrogate`
        - ✅ `RuneLen`

- **File:** `src/unicode/utf16/utf16_test.go`
    - Ground Truth Functions (1):
        - `TestRuneLen`
    - Predicted Functions (4):
        - ❌ `AppendRune`
        - ❌ `DecodeRune`
        - ❌ `EncodeRune`
        - ✅ `TestRuneLen`


### 📊 **Proposal #39557 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/flag/example_func_test.go`
    - Ground Truth Functions (1):
        - `ExampleFunc`
    - Predicted Functions (0):

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (1):
        - `Func`
    - Predicted Functions (4):
        - ✅ `Func`
        - ❌ `Set`
        - ❌ `String`
        - ❌ `Var`

- **File:** `src/flag/flag_test.go`
    - Ground Truth Functions (2):
        - `TestEverything`
        - `TestUserDefinedFunc`
    - Predicted Functions (2):
        - ❌ `TestUserDefinedBoolFunc`
        - ✅ `TestUserDefinedFunc`


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
    - Predicted Functions (3):
        - ❌ `builderPrintTest`
        - ❌ `printExitStatus`
        - ❌ `runTest`

- **File:** `src/cmd/go/internal/test/testflag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `exitWithUsage`
        - ❌ `testFlags`

- **File:** `src/cmd/objdump/objdump_test.go`
    - Ground Truth Functions (1):
        - `TestMain`
    - Predicted Functions (0):

- **File:** `src/internal/testenv/testenv.go`
    - Ground Truth Functions (1):
        - `HasGoBuild`
    - Predicted Functions (0):

- **File:** `src/os/exec/bench_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/dot_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/env_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ExampleCmd_Run`
        - ❌ `ExampleCmd_Start`

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `CombinedOutput`
        - ❌ `Output`
        - ❌ `Run`
        - ❌ `Start`
        - ❌ `Wait`

- **File:** `src/os/exec/exec_linux_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_other_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_plan9.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_posix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestMain`
        - ❌ `cmdExit`

- **File:** `src/os/exec/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/internal/fdtest/exists_plan9.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/internal/fdtest/exists_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestExists`

- **File:** `src/os/exec/internal/fdtest/exists_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/internal/fdtest/exists_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/internal_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_linux_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_plan9.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_wasm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/read3.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Exit`
        - ❌ `FailNow`
        - ❌ `Fatal`
        - ❌ `Fatalf`
        - ❌ `Main`
        - ❌ `Run`
        - ❌ `SetPanicOnExit0`

- **File:** `src/testing/testing_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestMain`
        - ❌ `runTest`


### 📊 **Proposal #50770 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 25.0% | 15.4% | 1/4 |

##### Ground Truth vs Predicted Functions per File

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
    - Predicted Functions (5):
        - ❌ `After`
        - ❌ `Before`
        - ❌ `Compare`
        - ❌ `Equal`
        - ❌ `TestSub`


### 📊 **Proposal #40281 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
    - Ground Truth Functions (1):
        - `validateStructTag`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/testdata/structtag/structtag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/vet/testdata/tagtest/file1.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/vet/testdata/tagtest/file2.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (1):
        - `Lookup`
    - Predicted Functions (3):
        - ❌ `Get`
        - ❌ `IsExported`
        - ✅ `Lookup`

- **File:** `src/reflect/type_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Get`
        - ❌ `Lookup`
        - ❌ `StructTag`


### 📊 **Proposal #42026 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 52.6% | 2.8% | 5.3% | 10/355 |

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

- **File:** `src/io/fs/readfile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ReadFile`

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
    - Predicted Functions (3):
        - ✅ `ReadDir`
        - ❌ `Readdir`
        - ❌ `Readdirnames`

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
    - Predicted Functions (0):

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

- **File:** `src/os/path.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `MkdirAll`

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
    - Predicted Functions (0):

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


### 📊 **Proposal #44815 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 27.3% | 75.0% | 40.0% | 3/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/bufio/bufio.go`
    - Ground Truth Functions (1):
        - `ReadFrom`
    - Predicted Functions (3):
        - ❌ `Flush`
        - ✅ `ReadFrom`
        - ❌ `Write`

- **File:** `src/bufio/bufio_test.go`
    - Ground Truth Functions (3):
        - `ReadFrom`
        - `TestWriterReadFromWithBufferedData`
        - `Write`
    - Predicted Functions (8):
        - ✅ `ReadFrom`
        - ❌ `TestWriterReadFrom`
        - ❌ `TestWriterReadFromCounts`
        - ❌ `TestWriterReadFromErrNoProgress`
        - ❌ `TestWriterReadFromErrors`
        - ❌ `TestWriterReadFromUntilEOF`
        - ❌ `TestWriterReadFromWhileFull`
        - ✅ `TestWriterReadFromWithBufferedData`


### 📊 **Proposal #46121 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/html/template/template.go`
    - Ground Truth Functions (1):
        - `Funcs`
    - Predicted Functions (1):
        - ✅ `Funcs`

- **File:** `src/text/template/funcs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `addFuncs`

- **File:** `src/text/template/template.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Funcs`


### 📊 **Proposal #40357 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 25.0% | 21.1% | 2/8 |

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
    - Predicted Functions (3):
        - ✅ `ListModules`
        - ✅ `listModules`
        - ❌ `modinfoError`

- **File:** `src/cmd/go/internal/modload/modfile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `CheckDeprecation`
        - ❌ `CheckRetractions`
        - ❌ `ModuleRetractedError`
        - ❌ `retractionLoadingError`

- **File:** `src/cmd/go/internal/modload/query.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Latest`
        - ❌ `Query`
        - ❌ `Stat`
        - ❌ `queryProxy`


### 📊 **Proposal #37168 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.7% | 13.6% | 1.3% | 3/22 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/aes/aes.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `NewCipher`

- **File:** `src/crypto/aes/aes_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `BenchmarkDecrypt`
        - ❌ `BenchmarkEncrypt`
        - ❌ `TestAESBlock`
        - ❌ `TestCipherDecrypt`
        - ❌ `TestCipherEncrypt`
        - ❌ `benchmarkDecrypt`
        - ❌ `benchmarkEncrypt`
        - ❌ `testAESBlock`
        - ❌ `testCipherDecrypt`
        - ❌ `testCipherEncrypt`

- **File:** `src/crypto/cipher/cipher.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `NewGCM`
        - ❌ `NewGCMWithNonceSize`
        - ❌ `NewGCMWithTagSize`
        - ❌ `gcmAble`

- **File:** `src/crypto/cipher/gcm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `NewGCM`
        - ❌ `NewGCMWithNonceSize`
        - ❌ `NewGCMWithTagSize`
        - ❌ `gcmAuth`
        - ❌ `gcmCounterCryptGeneric`
        - ❌ `gcmInc32`
        - ❌ `newGCM`
        - ❌ `newGCMFallback`

- **File:** `src/crypto/cipher/gcm_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestAESGCM`
        - ❌ `TestGCMAEAD`
        - ❌ `TestGCMAsm`
        - ❌ `testAESGCM`
        - ❌ `testGCMAEAD`

- **File:** `src/crypto/des/block.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `cryptBlock`
        - ❌ `feistel`
        - ❌ `permuteBlock`
        - ❌ `permuteFinalBlock`
        - ❌ `permuteInitialBlock`

- **File:** `src/crypto/des/cipher.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Decrypt`
        - ❌ `Encrypt`
        - ❌ `NewCipher`
        - ❌ `NewTripleDESCipher`

- **File:** `src/crypto/des/des_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `BenchmarkDecrypt`
        - ❌ `BenchmarkEncrypt`
        - ❌ `BenchmarkTDESDecrypt`
        - ❌ `BenchmarkTDESEncrypt`
        - ❌ `TestDESDecryptBlock`
        - ❌ `TestDESEncryptBlock`

- **File:** `src/crypto/dsa/dsa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `GenerateKey`
        - ❌ `GenerateParameters`
        - ❌ `Sign`
        - ❌ `Verify`

- **File:** `src/crypto/dsa/dsa_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `TestParameterGeneration`
        - ❌ `TestSignAndVerify`
        - ❌ `TestSignAndVerifyWithBadPublicKey`
        - ❌ `TestSigningWithDegenerateKeys`
        - ❌ `testParameterGeneration`
        - ❌ `testSignAndVerify`

- **File:** `src/crypto/ecdh/ecdh.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Bytes`
        - ❌ `Curve`
        - ❌ `ECDH`
        - ❌ `Equal`
        - ❌ `Public`
        - ❌ `PublicKey`

- **File:** `src/crypto/ecdh/ecdh_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `BenchmarkECDH`
        - ❌ `TestECDH`
        - ❌ `TestGenerateKey`
        - ❌ `TestLinker`
        - ❌ `TestNewPrivateKey`
        - ❌ `TestNewPublicKey`
        - ❌ `TestVectors`
        - ❌ `benchmarkAllCurves`
        - ❌ `testAllCurves`

- **File:** `src/crypto/ecdsa/ecdsa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `SignASN1`
        - ❌ `VerifyASN1`
        - ❌ `signFIPS`
        - ❌ `signFIPSDeterministic`
        - ❌ `signRFC6979`
        - ❌ `verifyFIPS`

- **File:** `src/crypto/ecdsa/ecdsa_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (35):
        - ❌ `BenchmarkGenerateKey`
        - ❌ `BenchmarkSign`
        - ❌ `BenchmarkVerify`
        - ❌ `TestINDCCA`
        - ❌ `TestInvalidPrivateKeys`
        - ❌ `TestInvalidPublicKeys`
        - ❌ `TestNegativeInputs`
        - ❌ `TestNegativeSignature`
        - ❌ `TestNonceSafety`
        - ❌ `TestParseAndBytesRoundTrip`
        - ❌ `TestRFC6979`
        - ❌ `TestRMinusNSignature`
        - ❌ `TestRPlusNSignature`
        - ❌ `TestSignAndVerify`
        - ❌ `TestSignAndVerifyASN1`
        - ❌ `TestVectors`
        - ❌ `TestZeroHashSignature`
        - ❌ `TestZeroSignature`
        - ❌ `benchmarkAllCurves`
        - ❌ `testAllCurves`
        - ❌ `testINDCCA`
        - ❌ `testInvalidPrivateKeys`
        - ❌ `testInvalidPublicKeys`
        - ❌ `testNegativeInputs`
        - ❌ `testNegativeSignature`
        - ❌ `testNonceSafety`
        - ❌ `testParseAndBytesRoundTrip`
        - ❌ `testRFC6979`
        - ❌ `testRMinusNSignature`
        - ❌ `testRPlusNSignature`
        - ❌ `testSignAndVerify`
        - ❌ `testSignAndVerifyASN1`
        - ❌ `testVectors`
        - ❌ `testZeroHashSignature`
        - ❌ `testZeroSignature`

- **File:** `src/crypto/ed25519/ed25519.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Sign`
        - ❌ `Verify`
        - ❌ `VerifyWithOptions`
        - ❌ `sign`

- **File:** `src/crypto/ed25519/ed25519_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `BenchmarkSigning`
        - ❌ `BenchmarkVerification`
        - ❌ `TestMalleability`
        - ❌ `TestSignVerify`
        - ❌ `TestSignVerifyContext`
        - ❌ `TestSignVerifyHashed`

- **File:** `src/crypto/elliptic/elliptic.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `P224`
        - ❌ `P256`
        - ❌ `P384`
        - ❌ `P521`

- **File:** `src/crypto/elliptic/elliptic_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `BenchmarkScalarBaseMult`
        - ❌ `BenchmarkScalarMult`
        - ❌ `benchmarkAllCurves`
        - ❌ `genericParamsForCurve`
        - ❌ `testAllCurves`

- **File:** `src/crypto/hmac/hmac.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Equal`
        - ❌ `New`

- **File:** `src/crypto/hmac/hmac_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `BenchmarkHMACSHA256_1K`
        - ❌ `BenchmarkHMACSHA256_32`
        - ❌ `BenchmarkNewWriteSum`

- **File:** `src/crypto/md5/md5.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Sum`
        - ❌ `Write`
        - ❌ `checkSum`

- **File:** `src/crypto/md5/md5_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (14):
        - ❌ `BenchmarkHash128`
        - ❌ `BenchmarkHash1K`
        - ❌ `BenchmarkHash1KUnaligned`
        - ❌ `BenchmarkHash1M`
        - ❌ `BenchmarkHash256`
        - ❌ `BenchmarkHash512`
        - ❌ `BenchmarkHash64`
        - ❌ `BenchmarkHash8Bytes`
        - ❌ `BenchmarkHash8BytesUnaligned`
        - ❌ `BenchmarkHash8K`
        - ❌ `BenchmarkHash8KUnaligned`
        - ❌ `BenchmarkHash8M`
        - ❌ `TestBlockGeneric`
        - ❌ `safeSum`

- **File:** `src/crypto/rc4/rc4.go`
    - Ground Truth Functions (1):
        - `XORKeyStream`
    - Predicted Functions (3):
        - ❌ `NewCipher`
        - ❌ `Reset`
        - ✅ `XORKeyStream`

- **File:** `src/crypto/rc4/rc4_test.go`
    - Ground Truth Functions (2):
        - `TestBlock`
        - `benchmark`
    - Predicted Functions (8):
        - ❌ `BenchmarkRC4_128`
        - ❌ `BenchmarkRC4_1K`
        - ❌ `BenchmarkRC4_8K`
        - ✅ `TestBlock`
        - ❌ `TestGolden`
        - ❌ `TestRC4Stream`
        - ✅ `benchmark`
        - ❌ `testEncrypt`

- **File:** `src/crypto/rsa/rsa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Decrypt`
        - ❌ `GenerateKey`
        - ❌ `GenerateMultiPrimeKey`
        - ❌ `Sign`

- **File:** `src/crypto/rsa/rsa_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (11):
        - ❌ `BenchmarkDecryptOAEP`
        - ❌ `BenchmarkDecryptPKCS1v15`
        - ❌ `BenchmarkEncryptOAEP`
        - ❌ `BenchmarkEncryptPKCS1v15`
        - ❌ `BenchmarkGenerateKey`
        - ❌ `BenchmarkSignPKCS1v15`
        - ❌ `BenchmarkSignPSS`
        - ❌ `BenchmarkVerifyPKCS1v15`
        - ❌ `BenchmarkVerifyPSS`
        - ❌ `benchmarkDecryptPKCS1v15`
        - ❌ `benchmarkSignPKCS1v15`

- **File:** `src/crypto/sha1/sha1.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `BlockSize`
        - ❌ `Size`
        - ❌ `Sum`
        - ❌ `Write`
        - ❌ `checkSum`

- **File:** `src/crypto/sha1/sha1_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (11):
        - ❌ `BenchmarkHash1K`
        - ❌ `BenchmarkHash320Bytes`
        - ❌ `BenchmarkHash8Bytes`
        - ❌ `BenchmarkHash8K`
        - ❌ `TestAllocations`
        - ❌ `TestGolden`
        - ❌ `TestGoldenMarshal`
        - ❌ `TestLargeHashes`
        - ❌ `testGolden`
        - ❌ `testGoldenMarshal`
        - ❌ `testLargeHashes`

- **File:** `src/crypto/sha256/sha256.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `New`
        - ❌ `New224`
        - ❌ `Sum224`
        - ❌ `Sum256`

- **File:** `src/crypto/sha256/sha256_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `BenchmarkHash1K`
        - ❌ `BenchmarkHash1M`
        - ❌ `BenchmarkHash256K`
        - ❌ `BenchmarkHash8Bytes`
        - ❌ `BenchmarkHash8K`
        - ❌ `TestAllocations`
        - ❌ `TestCgo`

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

- **File:** `src/crypto/sha512/sha512_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `BenchmarkHash1K`
        - ❌ `BenchmarkHash8Bytes`
        - ❌ `BenchmarkHash8K`
        - ❌ `TestAllocations`

- **File:** `src/crypto/subtle/constant_time.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `ConstantTimeByteEq`
        - ❌ `ConstantTimeCompare`
        - ❌ `ConstantTimeCopy`
        - ❌ `ConstantTimeEq`
        - ❌ `ConstantTimeLessOrEq`
        - ❌ `ConstantTimeSelect`

- **File:** `src/crypto/subtle/constant_time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestConstantTimeByteEq`
        - ❌ `TestConstantTimeCompare`
        - ❌ `TestConstantTimeCopy`
        - ❌ `TestConstantTimeEq`
        - ❌ `TestConstantTimeLessOrEq`

- **File:** `src/crypto/tls/tls.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/tls/tls_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestCipherSuites`
        - ❌ `TestECH`
        - ❌ `TestHandshakeMLKEM`
        - ❌ `TestVersionName`
        - ❌ `http2isBadCipher`

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `CheckCRLSignature`
        - ❌ `CheckSignature`
        - ❌ `CheckSignatureFrom`
        - ❌ `CreateCertificate`
        - ❌ `CreateCertificateRequest`
        - ❌ `CreateRevocationList`
        - ❌ `checkSignature`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestDisableSHA1ForCertOnly`
        - ❌ `TestMD5`
        - ❌ `TestRSAPSAParameters`
        - ❌ `TestSHA1`

- **File:** `src/hash/crc32/crc32_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `archAvailableCastagnoli`
        - ❌ `archAvailableIEEE`
        - ❌ `archInitCastagnoli`
        - ❌ `archInitIEEE`
        - ❌ `archUpdateCastagnoli`
        - ❌ `archUpdateIEEE`
        - ❌ `castagnoliSSE42`
        - ❌ `castagnoliSSE42Triple`
        - ❌ `castagnoliShift`
        - ❌ `ieeeCLMUL`

- **File:** `src/hash/crc32/crc32_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `archAvailableCastagnoli`
        - ❌ `archAvailableIEEE`
        - ❌ `archInitCastagnoli`
        - ❌ `archInitIEEE`
        - ❌ `archUpdateCastagnoli`
        - ❌ `archUpdateIEEE`
        - ❌ `castagnoliUpdate`
        - ❌ `ieeeUpdate`

- **File:** `src/hash/crc32/crc32_generic.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `simpleMakeTable`
        - ❌ `simplePopulateTable`
        - ❌ `simpleUpdate`
        - ❌ `slicingMakeTable`
        - ❌ `slicingUpdate`

- **File:** `src/hash/crc32/crc32_loong64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `archAvailableCastagnoli`
        - ❌ `archAvailableIEEE`
        - ❌ `archInitCastagnoli`
        - ❌ `archInitIEEE`
        - ❌ `archUpdateCastagnoli`
        - ❌ `archUpdateIEEE`
        - ❌ `castagnoliUpdate`
        - ❌ `ieeeUpdate`

- **File:** `src/hash/crc32/crc32_otherarch.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `archAvailableCastagnoli`
        - ❌ `archAvailableIEEE`
        - ❌ `archInitCastagnoli`
        - ❌ `archInitIEEE`
        - ❌ `archUpdateCastagnoli`
        - ❌ `archUpdateIEEE`

- **File:** `src/hash/crc32/crc32_ppc64le.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `archInitCastagnoli`
        - ❌ `archInitIEEE`
        - ❌ `archUpdateCastagnoli`
        - ❌ `archUpdateIEEE`
        - ❌ `ppc64SlicingUpdateBy8`
        - ❌ `vectorCrc32`

- **File:** `src/hash/crc32/crc32_s390x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `archAvailableCastagnoli`
        - ❌ `archAvailableIEEE`
        - ❌ `archInitCastagnoli`
        - ❌ `archInitIEEE`
        - ❌ `archUpdateCastagnoli`
        - ❌ `archUpdateIEEE`
        - ❌ `vectorizedCastagnoli`
        - ❌ `vectorizedIEEE`

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

- **File:** `src/math/big/arith.go`
    - Ground Truth Functions (0):
    - Predicted Functions (14):
        - ❌ `addMulVVWW_g`
        - ❌ `addVV_g`
        - ❌ `addVW`
        - ❌ `addVW_ref`
        - ❌ `divWW`
        - ❌ `lshVU_g`
        - ❌ `mulAddVWW_g`
        - ❌ `mulAddWWW_g`
        - ❌ `mulWW`
        - ❌ `reciprocalWord`
        - ❌ `rshVU_g`
        - ❌ `subVV_g`
        - ❌ `subVW`
        - ❌ `subVW_ref`

- **File:** `src/math/big/arith_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `addMulVVW`
        - ❌ `addVV`
        - ❌ `addVW`
        - ❌ `divWVW`
        - ❌ `mulAddVWW`
        - ❌ `shlVU`
        - ❌ `shrVU`
        - ❌ `subVV`
        - ❌ `subVW`

- **File:** `src/math/big/arith_amd64_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestAddMulVVWWNoADX`

- **File:** `src/math/big/arith_decl.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `addMulVVW`
        - ❌ `addMulVVWW`
        - ❌ `addVV`
        - ❌ `lshVU`
        - ❌ `mulAddVWW`
        - ❌ `rshVU`
        - ❌ `shlVU`
        - ❌ `subVV`

- **File:** `src/math/big/arith_decl_pure.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `addMulVVWW`
        - ❌ `addVV`
        - ❌ `lshVU`
        - ❌ `mulAddVWW`
        - ❌ `rshVU`
        - ❌ `subVV`

- **File:** `src/math/big/arith_s390x_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestAddVVNoVec`
        - ❌ `TestSubVVNoVec`

- **File:** `src/math/big/arith_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (19):
        - ❌ `BenchmarkAddMulVVWW`
        - ❌ `BenchmarkAddVV`
        - ❌ `BenchmarkAddVW`
        - ❌ `BenchmarkLshVU`
        - ❌ `BenchmarkMulAddVWW`
        - ❌ `BenchmarkRshVU`
        - ❌ `BenchmarkSubVV`
        - ❌ `BenchmarkSubVW`
        - ❌ `TestAddMulVVWW`
        - ❌ `TestAddVV`
        - ❌ `TestAddVW`
        - ❌ `TestDivWW`
        - ❌ `TestLshVU`
        - ❌ `TestMulAddVWW`
        - ❌ `TestMulAddWWW`
        - ❌ `TestMulWW`
        - ❌ `TestRshVU`
        - ❌ `TestSubVV`
        - ❌ `TestSubVW`

- **File:** `src/math/big/arithvec_s390x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `addVVvec`
        - ❌ `subVVvec`

- **File:** `src/math/big/internal/asmgen/386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `_386MemIndex`

- **File:** `src/math/big/internal/asmgen/add.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `addOrSubVV`

- **File:** `src/math/big/internal/asmgen/amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `amd64Add`
        - ❌ `amd64JmpADX`
        - ❌ `x86Hint`
        - ❌ `x86MulWide`
        - ❌ `x86Op3`
        - ❌ `x86Suffix`

- **File:** `src/math/big/internal/asmgen/arch.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `HasShiftWide`
        - ❌ `IsImm`
        - ❌ `IsMem`
        - ❌ `String`
        - ❌ `Valid`
        - ❌ `mem`

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

- **File:** `src/math/big/internal/asmgen/asm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Add`
        - ❌ `AddWords`
        - ❌ `Lsh`
        - ❌ `MulWide`
        - ❌ `NewAsm`
        - ❌ `Rsh`
        - ❌ `Sub`

- **File:** `src/math/big/internal/asmgen/cheat.go`
    - Ground Truth Functions (0):
    - Predicted Functions (18):
        - ❌ `adcs`
        - ❌ `add`
        - ❌ `adds`
        - ❌ `and`
        - ❌ `loop`
        - ❌ `lsh`
        - ❌ `mem`
        - ❌ `mov`
        - ❌ `mul`
        - ❌ `mulWide`
        - ❌ `neg`
        - ❌ `or`
        - ❌ `rsh`
        - ❌ `sbcs`
        - ❌ `sub`
        - ❌ `subs`
        - ❌ `xor`
        - ❌ `zero`

- **File:** `src/math/big/internal/asmgen/func.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Arg`
        - ❌ `ArgHint`
        - ❌ `ArgPtr`
        - ❌ `Func`
        - ❌ `StoreArg`

- **File:** `src/math/big/internal/asmgen/loong64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/math/big/internal/asmgen/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `generate`

- **File:** `src/math/big/internal/asmgen/main_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Test`

- **File:** `src/math/big/internal/asmgen/mips.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `mipsMulWide`

- **File:** `src/math/big/internal/asmgen/mips64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `mips64MulWide`

- **File:** `src/math/big/internal/asmgen/mul.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `addMul`
        - ❌ `addMulAlt`
        - ❌ `addMulVVWW`
        - ❌ `addMulVirtualCarry`
        - ❌ `mulAddVWW`

- **File:** `src/math/big/internal/asmgen/pipe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (18):
        - ❌ `AtUnrollEnd`
        - ❌ `AtUnrollStart`
        - ❌ `Done`
        - ❌ `DropInput`
        - ❌ `LoadN`
        - ❌ `LoadPtrs`
        - ❌ `Loop`
        - ❌ `Pipe`
        - ❌ `Restart`
        - ❌ `SetBackward`
        - ❌ `SetHint`
        - ❌ `SetLabel`
        - ❌ `SetMaxColumns`
        - ❌ `SetUseIndexCounter`
        - ❌ `Start`
        - ❌ `StoreN`
        - ❌ `advancePtrs`
        - ❌ `unroll`

- **File:** `src/math/big/internal/asmgen/ppc64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `generatePPC64`
        - ❌ `writePPC64`

- **File:** `src/math/big/internal/asmgen/riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/math/big/internal/asmgen/s390x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `s390MulWide`
        - ❌ `s390xHint`
        - ❌ `s390xOp3`
        - ❌ `s390xSetup`

- **File:** `src/math/big/internal/asmgen/shift.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `shiftVU`


### 📊 **Proposal #42100 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 2.0% | 25.0% | 3.7% | 3/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `misc/ios/detect.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `detectMobileProvisionFiles`
        - ❌ `main`
        - ❌ `parseMobileProvision`
        - ❌ `plistExtract`

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
    - Predicted Functions (3):
        - ✅ `installSimulator`
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

- **File:** `src/cmd/link/internal/ld/config.go`
    - Ground Truth Functions (1):
        - `Set`
    - Predicted Functions (0):

- **File:** `src/internal/goos/goos.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goos/zgoos_ios.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/cgo/signal_ios_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `xx_cgo_panicmem`

- **File:** `src/syscall/syscall_darwin.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `RawSyscall`
        - ❌ `RawSyscall6`
        - ❌ `Syscall`
        - ❌ `Syscall6`
        - ❌ `rawSyscall`
        - ❌ `rawSyscall6`
        - ❌ `syscall`
        - ❌ `syscall6`
        - ❌ `syscallPtr`

- **File:** `src/syscall/syscall_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `SetControllen`
        - ❌ `SetKevent`
        - ❌ `SetLen`
        - ❌ `Syscall9`
        - ❌ `libc_sendfile_trampoline`
        - ❌ `sendfile`
        - ❌ `setTimespec`
        - ❌ `setTimeval`
        - ❌ `syscallX`

- **File:** `src/syscall/zerrors_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (123):
        - ❌ `Access`
        - ❌ `Adjtime`
        - ❌ `Chdir`
        - ❌ `Chflags`
        - ❌ `Chmod`
        - ❌ `Chown`
        - ❌ `Chroot`
        - ❌ `Close`
        - ❌ `Dup`
        - ❌ `Dup2`
        - ❌ `Exchangedata`
        - ❌ `Fchdir`
        - ❌ `Fchflags`
        - ❌ `Fchmod`
        - ❌ `Fchown`
        - ❌ `Flock`
        - ❌ `Fpathconf`
        - ❌ `Fstat`
        - ❌ `Fstatfs`
        - ❌ `Fsync`
        - ❌ `Ftruncate`
        - ❌ `Getdtablesize`
        - ❌ `Getegid`
        - ❌ `Geteuid`
        - ❌ `Getgid`
        - ❌ `Getpgid`
        - ❌ `Getpgrp`
        - ❌ `Getpid`
        - ❌ `Getppid`
        - ❌ `Getpriority`
        - ❌ `Getrlimit`
        - ❌ `Getrusage`
        - ❌ `Getsid`
        - ❌ `Gettimeofday`
        - ❌ `Getuid`
        - ❌ `Issetugid`
        - ❌ `Kqueue`
        - ❌ `Lchown`
        - ❌ `Link`
        - ❌ `Listen`
        - ❌ `Lstat`
        - ❌ `Mkdir`
        - ❌ `Mkfifo`
        - ❌ `Mknod`
        - ❌ `Mlock`
        - ❌ `Mlockall`
        - ❌ `Mprotect`
        - ❌ `Munlock`
        - ❌ `Munlockall`
        - ❌ `Open`
        - ❌ `Pathconf`
        - ❌ `Readlink`
        - ❌ `Rename`
        - ❌ `Revoke`
        - ❌ `Rmdir`
        - ❌ `Seek`
        - ❌ `Select`
        - ❌ `Setegid`
        - ❌ `Seteuid`
        - ❌ `Setgid`
        - ❌ `Setlogin`
        - ❌ `Setpgid`
        - ❌ `Setpriority`
        - ❌ `Setprivexec`
        - ❌ `Setregid`
        - ❌ `Setreuid`
        - ❌ `Setsid`
        - ❌ `Settimeofday`
        - ❌ `Setuid`
        - ❌ `Shutdown`
        - ❌ `Stat`
        - ❌ `Statfs`
        - ❌ `Symlink`
        - ❌ `Sync`
        - ❌ `Truncate`
        - ❌ `Umask`
        - ❌ `Undelete`
        - ❌ `Unlink`
        - ❌ `Unmount`
        - ❌ `accept`
        - ❌ `bind`
        - ❌ `closedir`
        - ❌ `connect`
        - ❌ `execve`
        - ❌ `exit`
        - ❌ `fcntl`
        - ❌ `fork`
        - ❌ `fstatat`
        - ❌ `futimes`
        - ❌ `getcwd`
        - ❌ `getgroups`
        - ❌ `getpeername`
        - ❌ `getsockname`
        - ❌ `getsockopt`
        - ❌ `ioctl`
        - ❌ `kevent`
        - ❌ `kill`
        - ❌ `mmap`
        - ❌ `msync`
        - ❌ `munmap`
        - ❌ `openat`
        - ❌ `pipe`
        - ❌ `pread`
        - ❌ `ptrace`
        - ❌ `pwrite`
        - ❌ `read`
        - ❌ `readdir_r`
        - ❌ `recvfrom`
        - ❌ `recvmsg`
        - ❌ `sendmsg`
        - ❌ `sendto`
        - ❌ `setgroups`
        - ❌ `setrlimit`
        - ❌ `setsockopt`
        - ❌ `socket`
        - ❌ `socketpair`
        - ❌ `sysctl`
        - ❌ `unlinkat`
        - ❌ `utimensat`
        - ❌ `utimes`
        - ❌ `wait4`
        - ❌ `write`
        - ❌ `writev`

- **File:** `src/syscall/ztypes_darwin_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #34652 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.8% | 33.3% | 32.0% | 4/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/html/template/escape.go`
    - Ground Truth Functions (1):
        - `escape`
    - Predicted Functions (0):

- **File:** `src/html/template/template_test.go`
    - Ground Truth Functions (1):
        - `TestSkipEscapeComments`
    - Predicted Functions (0):

- **File:** `src/text/template/exec.go`
    - Ground Truth Functions (1):
        - `walk`
    - Predicted Functions (0):

- **File:** `src/text/template/parse/lex.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `emit`
        - ❌ `ignore`
        - ❌ `lexComment`

- **File:** `src/text/template/parse/node.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Copy`
        - ❌ `String`
        - ❌ `newComment`
        - ❌ `tree`
        - ❌ `writeTo`

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
    - Predicted Functions (5):
        - ✅ `Parse`
        - ❌ `action`
        - ✅ `itemList`
        - ✅ `parse`
        - ✅ `textOrAction`

- **File:** `src/text/template/parse/parse_test.go`
    - Ground Truth Functions (1):
        - `TestParseWithComments`
    - Predicted Functions (0):


### 📊 **Proposal #43744 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/8 |

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
    - Predicted Functions (5):
        - ❌ `ReportMetric`
        - ❌ `RunBenchmarks`
        - ❌ `String`
        - ❌ `processBench`
        - ❌ `runBenchmarks`

- **File:** `src/testing/benchmark_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `ExampleB_ReportMetric`
        - ❌ `ExampleB_ReportMetric_parallel`
        - ❌ `TestReportMetric`

- **File:** `src/time/sleep_test.go`
    - Ground Truth Functions (4):
        - `BenchmarkParallelTimerLatency`
        - `BenchmarkStaggeredTickerLatency`
        - `doWork`
        - `warmupScheduler`
    - Predicted Functions (0):


### 📊 **Proposal #47527 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.5% | 66.7% | 16.7% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/bufio/bufio.go`
    - Ground Truth Functions (1):
        - `AvailableBuffer`
    - Predicted Functions (3):
        - ❌ `Available`
        - ✅ `AvailableBuffer`
        - ❌ `Write`

- **File:** `src/bufio/bufio_test.go`
    - Ground Truth Functions (1):
        - `TestWriterAppend`
    - Predicted Functions (18):
        - ❌ `BenchmarkWriterCopyNoReadFrom`
        - ❌ `BenchmarkWriterCopyOptimal`
        - ❌ `BenchmarkWriterCopyUnoptimal`
        - ❌ `BenchmarkWriterEmpty`
        - ❌ `BenchmarkWriterFlush`
        - ❌ `TestBufferFull`
        - ❌ `TestWriteString`
        - ❌ `TestWriter`
        - ✅ `TestWriterAppend`
        - ❌ `TestWriterReadFrom`
        - ❌ `TestWriterReadFromCounts`
        - ❌ `TestWriterReadFromErrNoProgress`
        - ❌ `TestWriterReadFromErrors`
        - ❌ `TestWriterReadFromUntilEOF`
        - ❌ `TestWriterReadFromWhileFull`
        - ❌ `TestWriterReadFromWithBufferedData`
        - ❌ `TestWriterReset`
        - ❌ `TestWriterSize`

- **File:** `src/bufio/example_test.go`
    - Ground Truth Functions (1):
        - `ExampleWriter_AvailableBuffer`
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

- **File:** `test/fixedbugs/issue39505.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `f`

- **File:** `test/fixedbugs/issue39505b.go`
    - Ground Truth Functions (0):
    - Predicted Functions (19):
        - ❌ `ge_f1`
        - ❌ `ge_f2`
        - ❌ `ge_f3`
        - ❌ `gt_f1`
        - ❌ `gt_f2`
        - ❌ `gt_f3`
        - ❌ `le_f1`
        - ❌ `le_f2`
        - ❌ `le_f3`
        - ❌ `lt_f1`
        - ❌ `lt_f2`
        - ❌ `lt_f3`
        - ❌ `lt_f4`
        - ❌ `lt_f5`
        - ❌ `lt_f6`
        - ❌ `lt_f7`
        - ❌ `lt_f8`
        - ❌ `lt_f9`
        - ❌ `main`


### 📊 **Proposal #41730 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 21.9% | 35.0% | 26.9% | 7/20 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/go_test.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/envcmd/env.go`
    - Ground Truth Functions (1):
        - `MkEnv`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modfetch/codehost/codehost.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Run`
        - ❌ `RunWithArgs`
        - ❌ `run`

- **File:** `src/cmd/go/internal/modfetch/codehost/git.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `newGitRepo`
        - ❌ `runGit`

- **File:** `src/cmd/go/internal/modfetch/codehost/svn.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `svnParseStat`
        - ❌ `svnReadZip`

- **File:** `src/cmd/go/internal/modfetch/codehost/vcs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `NewRepo`
        - ❌ `newVCSRepo`
        - ❌ `vcsErrorf`

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
    - Predicted Functions (7):
        - ✅ `RepoRootForImportPath`
        - ✅ `allow`
        - ✅ `checkGOVCS`
        - ✅ `parseGOVCS`
        - ✅ `repoRootForImportDynamic`
        - ✅ `repoRootFromVCSPaths`
        - ✅ `validateRepoRoot`

- **File:** `src/cmd/go/internal/vcs/vcs_test.go`
    - Ground Truth Functions (4):
        - `TestGOVCS`
        - `TestGOVCSErrors`
        - `TestRepoRootForImportPath`
        - `init`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vcweb/bzr.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Available`
        - ❌ `Handler`

- **File:** `src/cmd/go/internal/vcweb/fossil.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Available`
        - ❌ `Handler`

- **File:** `src/cmd/go/internal/vcweb/git.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Available`
        - ❌ `Handler`

- **File:** `src/cmd/go/internal/vcweb/hg.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Available`
        - ❌ `Handler`

- **File:** `src/cmd/go/internal/vcweb/svn.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Available`
        - ❌ `Close`
        - ❌ `Handler`
        - ❌ `serve`

- **File:** `src/cmd/go/internal/vcweb/vcweb.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `HandleScript`
        - ❌ `NewServer`
        - ❌ `ServeHTTP`

- **File:** `src/cmd/go/main.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):


### 📊 **Proposal #46731 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/30 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/cgo/ast.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `ParseGo`
        - ❌ `saveExport`
        - ❌ `saveExport2`

- **File:** `src/cmd/cgo/gcc.go`
    - Ground Truth Functions (4):
        - `Init`
        - `badPointerTypedef`
        - `badVoidPointerTypedef`
        - `loadType`
    - Predicted Functions (0):

- **File:** `src/cmd/cgo/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `incompleteTypedef`

- **File:** `src/cmd/cgo/out.go`
    - Ground Truth Functions (1):
        - `writeDefs`
    - Predicted Functions (3):
        - ❌ `cgoType`
        - ❌ `doCgoType`
        - ❌ `structType`

- **File:** `src/cmd/compile/internal/ir/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `NewDynamicType`
        - ❌ `Sym`
        - ❌ `ToStatic`
        - ❌ `Type`
        - ❌ `TypeNode`
        - ❌ `newTypeNode`

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

- **File:** `src/cmd/compile/internal/typecheck/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (48):
        - ❌ `typecheck`
        - ❌ `typecheck1`
        - ❌ `typecheckarraylit`
        - ❌ `typecheckclosure`
        - ❌ `typecheckcomplit`
        - ❌ `typecheckconv`
        - ❌ `typecheckdef`
        - ❌ `typecheckdefergo`
        - ❌ `typecheckdot`
        - ❌ `typecheckdottype`
        - ❌ `typecheckexpr`
        - ❌ `typecheckfunc`
        - ❌ `typecheckmapkey`
        - ❌ `typecheckmethod`
        - ❌ `typecheckmethods`
        - ❌ `typecheckpartialcall`
        - ❌ `typecheckrange`
        - ❌ `typecheckselect`
        - ❌ `typecheckslice`
        - ❌ `typecheckstructlit`
        - ❌ `typecheckswitch`
        - ❌ `typecheckunsafe`
        - ❌ `typecheckunsafebytes`
        - ❌ `typecheckunsafebytestoslice`
        - ❌ `typecheckunsafebytestostring`
        - ❌ `typecheckunsafebytestostringbyte`
        - ❌ `typecheckunsafebytestostringbyteptr`
        - ❌ `typecheckunsafebytestostringbyteptrptr`
        - ❌ `typecheckunsafebytestostringrune`
        - ❌ `typecheckunsafebytestostringruneptr`
        - ❌ `typecheckunsafebytestostringruneptrptr`
        - ❌ `typecheckunsafeslice`
        - ❌ `typecheckunsafeslicetobytes`
        - ❌ `typecheckunsafeslicetostring`
        - ❌ `typecheckunsafeslicetostringbyte`
        - ❌ `typecheckunsafeslicetostringbyteptr`
        - ❌ `typecheckunsafeslicetostringbyteptrptr`
        - ❌ `typecheckunsafeslicetostringrune`
        - ❌ `typecheckunsafeslicetostringruneptr`
        - ❌ `typecheckunsafeslicetostringruneptrptr`
        - ❌ `typecheckunsafestring`
        - ❌ `typecheckunsafestringtoslice`
        - ❌ `typecheckunsafestringtoslicebyte`
        - ❌ `typecheckunsafestringtoslicebyteptr`
        - ❌ `typecheckunsafestringtoslicebyteptrptr`
        - ❌ `typecheckunsafestringtoslicerune`
        - ❌ `typecheckunsafestringtosliceruneptr`
        - ❌ `typecheckunsafestringtosliceruneptrptr`

- **File:** `src/cmd/compile/internal/typecheck/typecheck.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `checkassignto`
        - ❌ `typecheck`
        - ❌ `typecheck1`

- **File:** `src/cmd/compile/internal/types2/api.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Check`
        - ❌ `Error`
        - ❌ `FullError`
        - ❌ `ObjectOf`
        - ❌ `PkgNameOf`
        - ❌ `TypeOf`

- **File:** `src/cmd/compile/internal/types2/api_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `TestAssignableTo`
        - ❌ `TestConvertibleTo`
        - ❌ `TestIdentical`
        - ❌ `mustParse`
        - ❌ `mustTypecheck`
        - ❌ `typecheck`

- **File:** `src/cmd/compile/internal/types2/object.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `IsAlias`
        - ❌ `NewTypeName`
        - ❌ `NewTypeNameLazy`
        - ❌ `TypeName`

- **File:** `src/cmd/compile/internal/types2/object_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/type.go`
    - Ground Truth Functions (0):
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
    - Predicted Functions (0):

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

- **File:** `src/runtime/mcheckmark.go`
    - Ground Truth Functions (2):
        - `setCheckmark`
        - `startCheckmarks`
    - Predicted Functions (0):

- **File:** `src/runtime/mheap.go`
    - Ground Truth Functions (1):
        - `bytep`
    - Predicted Functions (0):

- **File:** `test/directive.go`
    - Ground Truth Functions (1):
        - `f`
    - Predicted Functions (0):

- **File:** `test/fixedbugs/issue40954.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `test/fixedbugs/notinheap.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `f`

- **File:** `test/fixedbugs/notinheap2.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `f`
        - ❌ `g`
        - ❌ `h`

- **File:** `test/fixedbugs/notinheap3.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `f`
        - ❌ `g`
        - ❌ `h`
        - ❌ `sliceClear`


### 📊 **Proposal #51668 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 46.2% | 85.7% | 60.0% | 6/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/fmt/format.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `FormatString`
        - ❌ `String`

- **File:** `src/fmt/print.go`
    - Ground Truth Functions (1):
        - `FormatString`
    - Predicted Functions (6):
        - ❌ `Flag`
        - ✅ `FormatString`
        - ❌ `Precision`
        - ❌ `String`
        - ❌ `Width`
        - ❌ `Write`

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


### 📊 **Proposal #45430 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 21.4% | 15.8% | 18.2% | 3/19 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/cipher_suites.go`
    - Ground Truth Functions (3):
        - `CipherSuites`
        - `InsecureCipherSuites`
        - `selectCipherSuite`
    - Predicted Functions (4):
        - ❌ `isAESGCMPreferred`
        - ❌ `mutualCipherSuite`
        - ❌ `mutualCipherSuiteTLS13`
        - ✅ `selectCipherSuite`

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (3):
        - `cipherSuites`
        - `isSupportedSignatureAlgorithm`
        - `unexpectedMessageError`
    - Predicted Functions (3):
        - ✅ `cipherSuites`
        - ❌ `defaultConfig`
        - ❌ `supportedCipherSuites`

- **File:** `src/crypto/tls/conn.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Handshake`
        - ❌ `HandshakeContext`
        - ❌ `handshakeContext`

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (1):
        - `makeClientHello`
    - Predicted Functions (1):
        - ❌ `pickCipherSuite`

- **File:** `src/crypto/tls/handshake_server.go`
    - Ground Truth Functions (1):
        - `pickCipherSuite`
    - Predicted Functions (3):
        - ❌ `cipherSuiteOk`
        - ✅ `pickCipherSuite`
        - ❌ `processClientHello`

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

- **File:** `src/crypto/tls/tls_test.go`
    - Ground Truth Functions (2):
        - `TestCipherSuites`
        - `http2isBadCipher`
    - Predicted Functions (0):


### 📊 **Proposal #39444 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/os/exec_unix.go`
    - Ground Truth Functions (1):
        - `signal`
    - Predicted Functions (3):
        - ❌ `convertESRCH`
        - ❌ `pidSignal`
        - ✅ `signal`

- **File:** `src/os/exec_unix_test.go`
    - Ground Truth Functions (1):
        - `TestErrProcessDone`
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

- **File:** `src/debug/pe/symbol.go`
    - Ground Truth Functions (1):
        - `COFFSymbolReadSectionDefAux`
    - Predicted Functions (2):
        - ✅ `COFFSymbolReadSectionDefAux`
        - ❌ `removeAuxSymbols`

- **File:** `src/debug/pe/symbols_test.go`
    - Ground Truth Functions (1):
        - `TestReadCOFFSymbolAuxInfo`
    - Predicted Functions (0):


### 📊 **Proposal #36771 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.8% | 100.0% | 12.7% | 4/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/fmt/scan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `complexTokens`
        - ❌ `scanComplex`

- **File:** `src/fmt/scan_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestInf`
        - ❌ `TestNaN`

- **File:** `src/strconv/atoc.go`
    - Ground Truth Functions (2):
        - `ParseComplex`
        - `convErr`
    - Predicted Functions (2):
        - ✅ `ParseComplex`
        - ✅ `convErr`

- **File:** `src/strconv/atoc_test.go`
    - Ground Truth Functions (1):
        - `TestParseComplex`
    - Predicted Functions (2):
        - ✅ `TestParseComplex`
        - ❌ `TestParseComplexIncorrectBitSize`

- **File:** `src/strconv/atof.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `ParseFloat`
        - ❌ `atof32`
        - ❌ `atof64`
        - ❌ `atofHex`
        - ❌ `parseFloatPrefix`
        - ❌ `readFloat`
        - ❌ `special`

- **File:** `src/strconv/atof_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `TestAtof`
        - ❌ `TestAtofSlow`
        - ❌ `TestParseFloatIncorrectBitSize`
        - ❌ `TestParseFloatPrefix`
        - ❌ `TestRoundTrip`
        - ❌ `TestRoundTrip32`
        - ❌ `testAtof`

- **File:** `src/strconv/atoi.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `bitSizeError`
        - ❌ `rangeError`
        - ❌ `syntaxError`

- **File:** `src/strconv/atoi_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (13):
        - ❌ `TestAtoi`
        - ❌ `TestParseInt`
        - ❌ `TestParseInt32`
        - ❌ `TestParseInt64`
        - ❌ `TestParseInt64Base`
        - ❌ `TestParseIntBase`
        - ❌ `TestParseIntBitSize`
        - ❌ `TestParseUint`
        - ❌ `TestParseUint32`
        - ❌ `TestParseUint64`
        - ❌ `TestParseUint64Base`
        - ❌ `TestParseUintBase`
        - ❌ `TestParseUintBitSize`

- **File:** `src/strconv/ctoa.go`
    - Ground Truth Functions (1):
        - `FormatComplex`
    - Predicted Functions (1):
        - ✅ `FormatComplex`

- **File:** `src/strconv/ctoa_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestFormatComplex`
        - ❌ `TestFormatComplexInvalidBitSize`

- **File:** `src/strconv/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `FormatFloat`
        - ❌ `ParseFloat`

- **File:** `src/strconv/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `FormatFloat`
        - ❌ `ParseFloat`

- **File:** `src/strconv/export_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strconv/ftoa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `AppendFloat`
        - ❌ `FormatFloat`
        - ❌ `fmtB`
        - ❌ `fmtE`
        - ❌ `fmtF`
        - ❌ `fmtX`

- **File:** `src/strconv/ftoa_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `FormatFloat`

- **File:** `src/strconv/isprint.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/strconv/quote.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `FormatFloat`
        - ❌ `ParseFloat`

- **File:** `src/strconv/quote_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `BenchmarkUnquoteEasy`
        - ❌ `BenchmarkUnquoteHard`
        - ❌ `TestUnquote`
        - ❌ `TestUnquoteInvalidUTF8`
        - ❌ `testUnquote`


### 📊 **Proposal #40255 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 31.2% | 25.6% | 28.2% | 10/39 |

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
    - Predicted Functions (22):
        - ✅ `rewriteValue386_Op386ADDSD`
        - ❌ `rewriteValue386_Op386ADDSDload`
        - ✅ `rewriteValue386_Op386ADDSS`
        - ❌ `rewriteValue386_Op386ADDSSload`
        - ✅ `rewriteValue386_Op386DIVSD`
        - ❌ `rewriteValue386_Op386DIVSDload`
        - ✅ `rewriteValue386_Op386DIVSS`
        - ❌ `rewriteValue386_Op386DIVSSload`
        - ❌ `rewriteValue386_Op386MOVSDconst`
        - ❌ `rewriteValue386_Op386MOVSDload`
        - ❌ `rewriteValue386_Op386MOVSDstore`
        - ❌ `rewriteValue386_Op386MOVSSconst`
        - ❌ `rewriteValue386_Op386MOVSSload`
        - ❌ `rewriteValue386_Op386MOVSSstore`
        - ✅ `rewriteValue386_Op386MULSD`
        - ❌ `rewriteValue386_Op386MULSDload`
        - ✅ `rewriteValue386_Op386MULSS`
        - ❌ `rewriteValue386_Op386MULSSload`
        - ✅ `rewriteValue386_Op386SUBSD`
        - ✅ `rewriteValue386_Op386SUBSDload`
        - ✅ `rewriteValue386_Op386SUBSS`
        - ✅ `rewriteValue386_Op386SUBSSload`

- **File:** `src/cmd/compile/internal/ssa/rewrite386splitload.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `rewriteBlock386splitload`
        - ❌ `rewriteValue386splitload`
        - ❌ `rewriteValue386splitload_Op386CMPBconstload`
        - ❌ `rewriteValue386splitload_Op386CMPBload`
        - ❌ `rewriteValue386splitload_Op386CMPLconstload`
        - ❌ `rewriteValue386splitload_Op386CMPLload`
        - ❌ `rewriteValue386splitload_Op386CMPWconstload`
        - ❌ `rewriteValue386splitload_Op386CMPWload`

- **File:** `src/cmd/compile/internal/ssa/softfloat.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `softfloat`

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

- **File:** `test/fixedbugs/issue22429.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `f`


### 📊 **Proposal #45454 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/base/env.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `AppendPATH`
        - ❌ `AppendPWD`

- **File:** `src/cmd/go/internal/cfg/cfg.go`
    - Ground Truth Functions (2):
        - `defaultContext`
        - `init`
    - Predicted Functions (2):
        - ❌ `GetArchEnv`
        - ❌ `computeExperiment`

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `CFlags`
        - ❌ `build`
        - ❌ `gccArchArgs`

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (1):
        - `defaultContext`
    - Predicted Functions (4):
        - ❌ `goodOSArchFile`
        - ❌ `matchFile`
        - ❌ `matchTag`
        - ❌ `shouldBuild`

- **File:** `src/go/build/constraint/expr.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Eval`
        - ❌ `Parse`
        - ❌ `isValidTag`
        - ❌ `tag`

- **File:** `src/go/build/constraint/expr_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestExprEval`
        - ❌ `TestParseExpr`

- **File:** `src/internal/buildcfg/cfg.go`
    - Ground Truth Functions (3):
        - `experimentTags`
        - `gogoarchTags`
        - `toolTags`
    - Predicted Functions (0):


### 📊 **Proposal #46057 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/cert_pool.go`
    - Ground Truth Functions (1):
        - `Equal`
    - Predicted Functions (4):
        - ❌ `AddCert`
        - ❌ `Clone`
        - ✅ `Equal`
        - ❌ `Subjects`

- **File:** `src/crypto/x509/cert_pool_test.go`
    - Ground Truth Functions (1):
        - `TestCertPoolEqual`
    - Predicted Functions (1):
        - ✅ `TestCertPoolEqual`


### 📊 **Proposal #51572 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.3% | 33.3% | 0.6% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/cgo/internal/test/test_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (1):
        - `matchtag`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/base/error_notunix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `IsETXTBSY`

- **File:** `src/cmd/go/internal/base/error_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `IsETXTBSY`

- **File:** `src/cmd/go/internal/base/signal_notunix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/base/signal_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/imports/build.go`
    - Ground Truth Functions (1):
        - `matchTag`
    - Predicted Functions (0):

- **File:** `src/go/build/build.go`
    - Ground Truth Functions (1):
        - `matchTag`
    - Predicted Functions (5):
        - ❌ `MatchFile`
        - ❌ `goodOSArchFile`
        - ❌ `matchFile`
        - ✅ `matchTag`
        - ❌ `shouldBuild`

- **File:** `src/go/build/build_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestAllTags`
        - ❌ `TestGoodOSArchFile`
        - ❌ `TestMatchFile`
        - ❌ `TestShouldBuild`

- **File:** `src/mime/type_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `initMimeUnix`

- **File:** `src/mime/type_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestTypeByExtensionUNIX`
        - ❌ `initMimeUnixTest`

- **File:** `src/net/cgo_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `cgoLookupAddrPTR`
        - ❌ `cgoLookupCNAME`
        - ❌ `cgoLookupHost`
        - ❌ `cgoLookupHostIP`
        - ❌ `cgoLookupIP`
        - ❌ `cgoLookupPTR`
        - ❌ `cgoLookupPort`
        - ❌ `cgoLookupServicePort`
        - ❌ `cgoResSearch`
        - ❌ `cgoSockaddr`

- **File:** `src/net/cgo_unix_cgo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/cgo_unix_cgo_res.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `_C_res_nclose`
        - ❌ `_C_res_ninit`
        - ❌ `_C_res_nsearch`

- **File:** `src/net/cgo_unix_cgo_resn.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `_C_res_nclose`
        - ❌ `_C_res_ninit`
        - ❌ `_C_res_nsearch`

- **File:** `src/net/cgo_unix_syscall.go`
    - Ground Truth Functions (0):
    - Predicted Functions (17):
        - ❌ `_C_ai_addr`
        - ❌ `_C_ai_family`
        - ❌ `_C_ai_flags`
        - ❌ `_C_ai_next`
        - ❌ `_C_ai_protocol`
        - ❌ `_C_ai_socktype`
        - ❌ `_C_free`
        - ❌ `_C_freeaddrinfo`
        - ❌ `_C_gai_strerror`
        - ❌ `_C_getaddrinfo`
        - ❌ `_C_malloc`
        - ❌ `_C_res_nclose`
        - ❌ `_C_res_ninit`
        - ❌ `_C_res_nsearch`
        - ❌ `cgoNameinfoPTR`
        - ❌ `cgoSockaddrInet4`
        - ❌ `cgoSockaddrInet6`

- **File:** `src/net/cgo_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/dnsclient_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `getSystemDNSConfig`
        - ❌ `init`
        - ❌ `releaseSema`
        - ❌ `tryAcquireSema`
        - ❌ `tryUpdate`

- **File:** `src/net/dnsclient_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/dnsconfig_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `dnsDefaultSearch`
        - ❌ `dnsReadConfig`
        - ❌ `ensureRooted`

- **File:** `src/net/dnsconfig_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestDNSDefaultSearch`
        - ❌ `TestDNSNameLength`
        - ❌ `TestDNSReadConfig`
        - ❌ `TestDNSReadMissingFile`

- **File:** `src/net/error_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `isConnError`

- **File:** `src/net/error_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `isENOBUFS`
        - ❌ `isPlatformError`
        - ❌ `samePlatformError`

- **File:** `src/net/fd_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `accept`
        - ❌ `connect`
        - ❌ `dup`
        - ❌ `init`
        - ❌ `newFD`
        - ❌ `newUnixFile`

- **File:** `src/net/file_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `dupFileSocket`

- **File:** `src/net/file_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestFileFdBlocks`

- **File:** `src/net/hook_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/interface_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestInterfaceArrivalAndDeparture`
        - ❌ `TestInterfaceArrivalAndDepartureZoneCache`
        - ❌ `TestPointToPointInterface`
        - ❌ `setup`
        - ❌ `teardown`

- **File:** `src/net/lookup_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `lookupAddr`
        - ❌ `lookupCNAME`
        - ❌ `lookupHost`
        - ❌ `lookupIP`
        - ❌ `lookupMX`
        - ❌ `lookupNS`
        - ❌ `lookupPort`
        - ❌ `lookupProtocol`
        - ❌ `lookupSRV`
        - ❌ `lookupTXT`

- **File:** `src/net/main_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/platform_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `supportsUnixSocket`

- **File:** `src/net/rawconn_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/rlimit_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `concurrentThreadsLimit`

- **File:** `src/net/sendfile_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestCopyFromTTY`

- **File:** `src/net/tcpconn_keepalive_conf_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `maybeSkipKeepAliveTest`

- **File:** `src/net/tcpsock_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `SetKeepAliveConfig`

- **File:** `src/net/tcpsock_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestTCPSpuriousConnSetupCompletion`
        - ❌ `TestTCPSpuriousConnSetupCompletionWithCancel`

- **File:** `src/net/tcpsockopt_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `setKeepAliveCount`
        - ❌ `setKeepAliveIdle`
        - ❌ `setKeepAliveInterval`

- **File:** `src/net/unixsock.go`
    - Ground Truth Functions (0):
    - Predicted Functions (25):
        - ❌ `Accept`
        - ❌ `AcceptUnix`
        - ❌ `Addr`
        - ❌ `Close`
        - ❌ `CloseRead`
        - ❌ `CloseWrite`
        - ❌ `DialUnix`
        - ❌ `File`
        - ❌ `ListenUnix`
        - ❌ `ListenUnixgram`
        - ❌ `Network`
        - ❌ `ReadFrom`
        - ❌ `ReadFromUnix`
        - ❌ `ReadMsgUnix`
        - ❌ `ResolveUnixAddr`
        - ❌ `SetDeadline`
        - ❌ `String`
        - ❌ `SyscallConn`
        - ❌ `WriteMsgUnix`
        - ❌ `WriteTo`
        - ❌ `WriteToUnix`
        - ❌ `isWildcard`
        - ❌ `newUnixConn`
        - ❌ `ok`
        - ❌ `opAddr`

- **File:** `src/net/unixsock_linux_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestUnixAbstractLongNameNulStart`
        - ❌ `TestUnixAutobindClose`
        - ❌ `TestUnixgramAutobind`
        - ❌ `TestUnixgramLinuxAbstractLongName`

- **File:** `src/net/unixsock_posix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (19):
        - ❌ `SetUnlinkOnClose`
        - ❌ `accept`
        - ❌ `close`
        - ❌ `dialUnix`
        - ❌ `family`
        - ❌ `file`
        - ❌ `listenUnix`
        - ❌ `listenUnixgram`
        - ❌ `readFrom`
        - ❌ `readMsg`
        - ❌ `sockaddr`
        - ❌ `sockaddrToUnix`
        - ❌ `sockaddrToUnixgram`
        - ❌ `sockaddrToUnixpacket`
        - ❌ `sotypeToNet`
        - ❌ `toLocal`
        - ❌ `unixSocket`
        - ❌ `writeMsg`
        - ❌ `writeTo`

- **File:** `src/net/unixsock_readmsg_cloexec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `setReadMsgCloseOnExec`

- **File:** `src/net/unixsock_readmsg_cmsg_cloexec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `setReadMsgCloseOnExec`

- **File:** `src/net/unixsock_readmsg_other.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `setReadMsgCloseOnExec`

- **File:** `src/net/unixsock_readmsg_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestUnixConnReadMsgUnixSCMRightsCloseOnExec`

- **File:** `src/net/unixsock_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/write_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestEndlessWrite`

- **File:** `src/net/writev_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `writeBuffers`

- **File:** `src/os/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `convertESRCH`
        - ❌ `findProcess`
        - ❌ `pidSignal`
        - ❌ `pidWait`
        - ❌ `signal`
        - ❌ `systemTime`
        - ❌ `userTime`
        - ❌ `wait`

- **File:** `src/os/exec_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestUNIXProcessAlive`

- **File:** `src/os/file_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (24):
        - ❌ `Info`
        - ❌ `IsDir`
        - ❌ `Link`
        - ❌ `Name`
        - ❌ `Remove`
        - ❌ `String`
        - ❌ `Symlink`
        - ❌ `Truncate`
        - ❌ `Type`
        - ❌ `close`
        - ❌ `epipecheck`
        - ❌ `fd`
        - ❌ `fixLongPath`
        - ❌ `net_newUnixFile`
        - ❌ `newFile`
        - ❌ `newFileFromNewFile`
        - ❌ `newUnixDirent`
        - ❌ `openDirNolog`
        - ❌ `openFileNolog`
        - ❌ `readlink`
        - ❌ `rename`
        - ❌ `seek`
        - ❌ `sigpipe`
        - ❌ `tempDir`

- **File:** `src/os/getwd_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestGetwdDeep`
        - ❌ `TestGetwdDeepWithPWDSet`
        - ❌ `testGetwdDeep`

- **File:** `src/os/os_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `TestChown`
        - ❌ `TestFileChown`
        - ❌ `TestIssue60181`
        - ❌ `TestLchown`
        - ❌ `TestMkdirStickyUmask`
        - ❌ `TestNewFileBlock`
        - ❌ `TestNewFileInvalid`
        - ❌ `TestNewFileNonBlock`
        - ❌ `TestReaddirRemoveRace`
        - ❌ `TestSplitPath`

- **File:** `src/os/path_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `IsPathSeparator`
        - ❌ `splitPath`

- **File:** `src/os/pipe_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Pipe`

- **File:** `src/os/readfrom_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `TestCopyFile`
        - ❌ `createTempFile`
        - ❌ `mustContainData`
        - ❌ `mustSeekStart`
        - ❌ `newCopyFileTest`
        - ❌ `testCopyFile`

- **File:** `src/os/removeall_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `isErrNoFollow`
        - ❌ `newDirFile`

- **File:** `src/os/root_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (22):
        - ❌ `afterResolvingSymlink`
        - ❌ `checkSymlink`
        - ❌ `chmodat`
        - ❌ `chownat`
        - ❌ `chtimesat`
        - ❌ `lchownat`
        - ❌ `linkat`
        - ❌ `mkdirat`
        - ❌ `modeAt`
        - ❌ `newRoot`
        - ❌ `openRootInRoot`
        - ❌ `openRootNolog`
        - ❌ `readlinkat`
        - ❌ `removeat`
        - ❌ `removedirat`
        - ❌ `removefileat`
        - ❌ `renameat`
        - ❌ `rootOpenDir`
        - ❌ `rootOpenFileNolog`
        - ❌ `rootStat`
        - ❌ `rootSymlink`
        - ❌ `symlinkat`

- **File:** `src/os/root_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestRootChown`
        - ❌ `TestRootConsistencyChown`
        - ❌ `TestRootConsistencyLchown`
        - ❌ `TestRootLchown`

- **File:** `src/os/stat_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Stat`
        - ❌ `lstatNolog`
        - ❌ `statNolog`

- **File:** `src/os/sys_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/timeout_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestTTYClose`

- **File:** `src/path/filepath/example_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/path/filepath/example_unix_walk_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ExampleWalk`

- **File:** `src/path/filepath/path_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `HasPrefix`
        - ❌ `abs`
        - ❌ `join`
        - ❌ `sameWord`
        - ❌ `splitList`

- **File:** `src/path/filepath/symlink_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `evalSymlinks`

- **File:** `src/runtime/os_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `closeonexec`

- **File:** `src/runtime/signal_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (12):
        - ❌ `clearSignalHandlers`
        - ❌ `initsig`
        - ❌ `minitSignalMask`
        - ❌ `minitSignalStack`
        - ❌ `minitSignals`
        - ❌ `os_sigpipe`
        - ❌ `sigInstallGoHandler`
        - ❌ `sigdisable`
        - ❌ `sigenable`
        - ❌ `sighandler`
        - ❌ `sigignore`
        - ❌ `unminitSignals`

- **File:** `src/runtime/syscall_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestSyscallFlagAlignment`

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
    - Predicted Functions (0):

- **File:** `src/syscall/linkname_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/mmap_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestMmap`

- **File:** `src/syscall/sockcmsg_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `CmsgLen`
        - ❌ `CmsgSpace`
        - ❌ `ParseSocketControlMessage`
        - ❌ `ParseUnixRights`
        - ❌ `UnixRights`
        - ❌ `data`
        - ❌ `socketControlMessageHeaderAndData`

- **File:** `src/syscall/sockcmsg_unix_other.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `cmsgAlignOf`

- **File:** `src/syscall/syscall_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (25):
        - ❌ `Bind`
        - ❌ `Connect`
        - ❌ `Getpeername`
        - ❌ `GetsockoptInt`
        - ❌ `Pread`
        - ❌ `Pwrite`
        - ❌ `Read`
        - ❌ `Recvfrom`
        - ❌ `Recvmsg`
        - ❌ `Sendfile`
        - ❌ `Sendmsg`
        - ❌ `SendmsgN`
        - ❌ `Sendto`
        - ❌ `SetsockoptByte`
        - ❌ `SetsockoptICMPv6Filter`
        - ❌ `SetsockoptIPMreq`
        - ❌ `SetsockoptIPv6Mreq`
        - ❌ `SetsockoptInet4Addr`
        - ❌ `SetsockoptInt`
        - ❌ `SetsockoptLinger`
        - ❌ `SetsockoptString`
        - ❌ `SetsockoptTimeval`
        - ❌ `Socket`
        - ❌ `Socketpair`
        - ❌ `Write`

- **File:** `src/syscall/syscall_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `TestENFILETemporary`
        - ❌ `TestFcntlFlock`
        - ❌ `TestPassFD`
        - ❌ `TestSeekFailure`
        - ❌ `TestSetsockoptString`
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
    - Predicted Functions (1):
        - ❌ `TestEnvTZUsage`


### 📊 **Proposal #39904 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 71.4% | 62.5% | 66.7% | 5/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/testing/match.go`
    - Ground Truth Functions (5):
        - `fullName`
        - `matches`
        - `newMatcher`
        - `splitRegexp`
        - `verify`
    - Predicted Functions (5):
        - ❌ `alternationMatch`
        - ✅ `matches`
        - ❌ `simpleMatch`
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


### 📊 **Proposal #53573 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 20.0% | 20.0% | 1/5 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/parser.go`
    - Ground Truth Functions (1):
        - `ParseRevocationList`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/pkix/pkix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `HasExpired`

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (1):
        - `CreateRevocationList`
    - Predicted Functions (4):
        - ❌ `CheckSignatureFrom`
        - ✅ `CreateRevocationList`
        - ❌ `ParseCRL`
        - ❌ `ParseDERCRL`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (3):
        - `TestCreateRevocationList`
        - `TestParseRevocationList`
        - `TestParseUniqueID`
    - Predicted Functions (0):


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

- **File:** `src/net/http/socks_bundle.go`
    - Ground Truth Functions (1):
        - `Dial`
    - Predicted Functions (0):


### 📊 **Proposal #27628 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.0% | 13.3% | 14.5% | 4/30 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/cache/hash.go`
    - Ground Truth Functions (1):
        - `Subkey`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/action.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Act`
        - ❌ `BuildActionID`
        - ❌ `BuildContentID`
        - ❌ `BuildID`
        - ❌ `cacheAction`

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `InstallPackages`
        - ❌ `runBuild`
        - ❌ `runInstall`

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
    - Predicted Functions (7):
        - ✅ `build`
        - ❌ `cacheObjdirFile`
        - ❌ `findCachedObjdirFile`
        - ✅ `link`
        - ❌ `loadCachedCompiledGoFiles`
        - ❌ `loadCachedObjdirFile`
        - ❌ `loadCachedVet`

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (5):
        - `asm`
        - `ld`
        - `ldShared`
        - `pack`
        - `toolVerify`
    - Predicted Functions (4):
        - ❌ `compiler`
        - ❌ `gc`
        - ✅ `ld`
        - ❌ `linker`

- **File:** `src/cmd/go/internal/work/gccgo.go`
    - Ground Truth Functions (4):
        - `asm`
        - `cc`
        - `link`
        - `pack`
    - Predicted Functions (6):
        - ✅ `cc`
        - ❌ `compiler`
        - ❌ `gc`
        - ❌ `ld`
        - ❌ `ldShared`
        - ❌ `linker`


### 📊 **Proposal #41696 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 18.8% | 21.4% | 3/16 |

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
    - Predicted Functions (3):
        - ✅ `InstallPackages`
        - ✅ `runBuild`
        - ✅ `runInstall`

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `BuildInstallFunc`
        - ❌ `installHeader`
        - ❌ `link`

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `gc`
        - ❌ `ld`
        - ❌ `pack`

- **File:** `src/cmd/go/internal/work/gccgo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `gc`
        - ❌ `ld`
        - ❌ `link`

- **File:** `src/cmd/go/internal/work/security.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/link/dwarf_test.go`
    - Ground Truth Functions (2):
        - `TestMain`
        - `testDWARF`
    - Predicted Functions (0):


### 📊 **Proposal #28089 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/go/ast/ast.go`
    - Ground Truth Functions (2):
        - `IsGenerated`
        - `generator`
    - Predicted Functions (2):
        - ✅ `IsGenerated`
        - ✅ `generator`

- **File:** `src/go/ast/ast_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestCommentText`
        - ❌ `TestIsDirective`

- **File:** `src/go/ast/issues_test.go`
    - Ground Truth Functions (1):
        - `TestIssue28089`
    - Predicted Functions (0):


### 📊 **Proposal #37255 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 88.9% | 64.0% | 8/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/context/context.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `WithCancel`
        - ❌ `WithCancelCause`
        - ❌ `cancel`
        - ❌ `cancelCtx`
        - ❌ `propagateCancel`
        - ❌ `withCancel`

- **File:** `src/os/signal/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Notify`

- **File:** `src/os/signal/example_unix_test.go`
    - Ground Truth Functions (1):
        - `ExampleNotifyContext`
    - Predicted Functions (0):

- **File:** `src/os/signal/signal.go`
    - Ground Truth Functions (3):
        - `NotifyContext`
        - `String`
        - `stop`
    - Predicted Functions (3):
        - ✅ `NotifyContext`
        - ✅ `String`
        - ✅ `stop`

- **File:** `src/os/signal/signal_test.go`
    - Ground Truth Functions (5):
        - `TestNotifyContextCancelParent`
        - `TestNotifyContextPrematureCancelParent`
        - `TestNotifyContextSimultaneousStop`
        - `TestNotifyContextStop`
        - `TestNotifyContextStringer`
    - Predicted Functions (6):
        - ✅ `TestNotifyContextCancelParent`
        - ❌ `TestNotifyContextNotifications`
        - ✅ `TestNotifyContextPrematureCancelParent`
        - ✅ `TestNotifyContextSimultaneousStop`
        - ✅ `TestNotifyContextStop`
        - ✅ `TestNotifyContextStringer`


### 📊 **Proposal #43993 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 10.0% | 9.5% | 1/10 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/vet/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestVet`
        - ❌ `errorCheck`
        - ❌ `wantedErrors`

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
    - Predicted Functions (5):
        - ❌ `DeepEqual`
        - ❌ `Equal`
        - ❌ `Interface`
        - ❌ `ValueOf`
        - ✅ `Zero`

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


### 📊 **Proposal #47658 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 66.7% | 40.0% | 4/6 |

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
    - Predicted Functions (5):
        - ❌ `Kind`
        - ❌ `OverflowComplex`
        - ❌ `OverflowFloat`
        - ❌ `OverflowInt`
        - ❌ `OverflowUint`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (4):
        - `CanComplex`
        - `CanFloat`
        - `CanInt`
        - `CanUint`
    - Predicted Functions (9):
        - ✅ `CanComplex`
        - ✅ `CanFloat`
        - ✅ `CanInt`
        - ✅ `CanUint`
        - ❌ `Complex`
        - ❌ `Float`
        - ❌ `Int`
        - ❌ `Kind`
        - ❌ `Uint`


### 📊 **Proposal #45964 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 2.7% | 4.0% | 3.3% | 2/50 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/internal/poll/sock_cloexec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `accept`

- **File:** `src/runtime/defs_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/defs_linux_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/defs_linux_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/defs_linux_arm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/defs_linux_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/defs_linux_loong64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/defs_linux_mips64x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/defs_linux_mipsx.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/defs_linux_ppc64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/defs_linux_ppc64le.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/defs_linux_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/defs_linux_s390x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `setNsec`
        - ❌ `set_usec`

- **File:** `src/runtime/os_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `clone`
        - ❌ `futex`
        - ❌ `futexsleep`
        - ❌ `futexwakeup`
        - ❌ `pipe2`
        - ❌ `rtsigprocmask`
        - ❌ `sigprocmask`
        - ❌ `timer_create`
        - ❌ `timer_delete`
        - ❌ `timer_settime`

- **File:** `src/runtime/os_linux_arm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `archauxv`
        - ❌ `osArchInit`

- **File:** `src/runtime/os_linux_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `archauxv`
        - ❌ `cputicks`
        - ❌ `osArchInit`

- **File:** `src/runtime/os_linux_be64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `sigaddset`
        - ❌ `sigdelset`
        - ❌ `sigfillset`

- **File:** `src/runtime/os_linux_generic.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/os_linux_loong64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `archauxv`
        - ❌ `osArchInit`

- **File:** `src/runtime/os_linux_mips64x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/os_linux_mipsx.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/os_linux_noauxv.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `archauxv`

- **File:** `src/runtime/os_linux_novdso.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `vdsoauxv`

- **File:** `src/runtime/os_linux_ppc64x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `archauxv`
        - ❌ `osArchInit`

- **File:** `src/runtime/os_linux_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `internal_cpu_riscvHWProbe`
        - ❌ `osArchInit`

- **File:** `src/runtime/os_linux_s390x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `archauxv`
        - ❌ `checkS390xCPU`
        - ❌ `osArchInit`

- **File:** `src/runtime/os_linux_x86.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osArchInit`

- **File:** `src/syscall/exec_linux.go`
    - Ground Truth Functions (3):
        - `forkAndExecInChild1`
        - `formatIDMappings`
        - `writeIDMappings`
    - Predicted Functions (4):
        - ❌ `doCheckClonePidfd`
        - ❌ `forkAndExecInChild`
        - ✅ `forkAndExecInChild1`
        - ❌ `os_checkClonePidfd`

- **File:** `src/syscall/syscall_linux.go`
    - Ground Truth Functions (6):
        - `Accept`
        - `Futimes`
        - `Futimesat`
        - `Pipe`
        - `Pipe2`
        - `UtimesNano`
    - Predicted Functions (16):
        - ❌ `EpollCreate`
        - ❌ `GetsockoptUcred`
        - ✅ `Pipe2`
        - ❌ `PtraceAttach`
        - ❌ `PtraceCont`
        - ❌ `PtraceDetach`
        - ❌ `PtraceGetEventMsg`
        - ❌ `PtraceGetRegs`
        - ❌ `PtracePeekData`
        - ❌ `PtracePeekText`
        - ❌ `PtracePokeData`
        - ❌ `PtracePokeText`
        - ❌ `PtraceSetOptions`
        - ❌ `PtraceSetRegs`
        - ❌ `PtraceSingleStep`
        - ❌ `PtraceSyscall`

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


### 📊 **Proposal #45754 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 46.2% | 100.0% | 63.2% | 6/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/flag/example_textvar_test.go`
    - Ground Truth Functions (1):
        - `ExampleTextVar`
    - Predicted Functions (1):
        - ✅ `ExampleTextVar`

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (5):
        - `Get`
        - `Set`
        - `String`
        - `TextVar`
        - `newTextValue`
    - Predicted Functions (6):
        - ✅ `Get`
        - ✅ `Set`
        - ✅ `String`
        - ✅ `TextVar`
        - ❌ `Var`
        - ✅ `newTextValue`

- **File:** `src/flag/flag_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `TestUserDefined`
        - ❌ `TestUserDefinedBool`
        - ❌ `TestUserDefinedBoolFunc`
        - ❌ `TestUserDefinedBoolUsage`
        - ❌ `TestUserDefinedForCommandLine`
        - ❌ `TestUserDefinedFunc`


### 📊 **Proposal #43620 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 50.0% | 20.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/testing/benchmark.go`
    - Ground Truth Functions (1):
        - `Elapsed`
    - Predicted Functions (4):
        - ✅ `Elapsed`
        - ❌ `ReportMetric`
        - ❌ `StartTimer`
        - ❌ `StopTimer`

- **File:** `src/testing/benchmark_test.go`
    - Ground Truth Functions (1):
        - `ExampleB_ReportMetric`
    - Predicted Functions (0):

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Elapsed`
        - ❌ `ReportMetric`
        - ❌ `StartTimer`
        - ❌ `StopTimer`


### 📊 **Proposal #50599 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.5% | 6.0% | 7.9% | 3/50 |

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
    - Predicted Functions (3):
        - ✅ `Environ`
        - ❌ `addCriticalEnv`
        - ✅ `environ`

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
    - Predicted Functions (2):
        - ✅ `TestDedupEnvEcho`
        - ❌ `TestEnvNULCharacter`

- **File:** `src/os/exec/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `skipStdinCopyError`

- **File:** `src/os/exec/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/os/exec/exec_windows_test.go`
    - Ground Truth Functions (3):
        - `TestChildCriticalEnv`
        - `cmdPipeHandle`
        - `init`
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_windows_test.go`
    - Ground Truth Functions (2):
        - `init`
        - `installBat`
    - Predicted Functions (0):

- **File:** `src/syscall/exec_aix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/exec_bsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `forkAndExecInChild`

- **File:** `src/syscall/exec_freebsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `forkAndExecInChild`

- **File:** `src/syscall/exec_freebsd_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/exec_libc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `execve`
        - ❌ `forkAndExecInChild`

- **File:** `src/syscall/exec_libc2.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `forkAndExecInChild`

- **File:** `src/syscall/exec_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `forkAndExecInChild`
        - ❌ `forkAndExecInChild1`

- **File:** `src/syscall/exec_linux_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/exec_pdeathsig_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/exec_plan9.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Exec`
        - ❌ `ForkExec`
        - ❌ `StartProcess`
        - ❌ `forkAndExecInChild`
        - ❌ `forkExec`
        - ❌ `startProcess`

- **File:** `src/syscall/exec_solaris_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `ForkExec`
        - ❌ `StartProcess`
        - ❌ `forkExec`

- **File:** `src/syscall/exec_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestExec`
        - ❌ `TestExecHelper`

- **File:** `src/syscall/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `StartProcess`
        - ❌ `createEnvBlock`

- **File:** `src/syscall/exec_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #52376 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.1% | 33.3% | 11.8% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (1):
        - `TestIsZero`
    - Predicted Functions (6):
        - ❌ `TestClear`
        - ❌ `TestMapSetNil`
        - ❌ `TestPtrSetNil`
        - ❌ `TestSet`
        - ❌ `TestSetValue`
        - ❌ `TestZeroSet`

- **File:** `src/reflect/export_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Set`
        - ❌ `Zero`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (2):
        - `IsZero`
        - `SetZero`
    - Predicted Functions (4):
        - ❌ `Set`
        - ✅ `SetZero`
        - ❌ `Zero`
        - ❌ `isZero`

- **File:** `test/clear.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `checkClearMap`
        - ❌ `checkClearSlice`


### 📊 **Proposal #43823 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 75.0% | 54.5% | 3/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/time/format.go`
    - Ground Truth Functions (4):
        - `commaOrPeriod`
        - `nextStdChunk`
        - `parse`
        - `parseNanoseconds`
    - Predicted Functions (4):
        - ✅ `commaOrPeriod`
        - ✅ `parse`
        - ✅ `parseNanoseconds`
        - ❌ `stdFracSecond`

- **File:** `src/time/format_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestFormatFractionalSecondSeparators`
        - ❌ `TestParse`
        - ❌ `TestParseFractionalSecondsLongerThanNineDigits`


### 📊 **Proposal #42322 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.0% | 40.0% | 34.3% | 6/15 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/embed/internal/embedtest/embed_test.go`
    - Ground Truth Functions (1):
        - `TestGlobal`
    - Predicted Functions (0):

- **File:** `src/io/fs/fs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `ValidPath`
        - ❌ `errClosed`
        - ❌ `errExist`
        - ❌ `errInvalid`
        - ❌ `errNotExist`
        - ❌ `errPermission`

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
    - Predicted Functions (2):
        - ❌ `Open`
        - ✅ `TestSub`

- **File:** `src/net/http/fs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `FS`
        - ❌ `FileServer`
        - ❌ `FileServerFS`
        - ❌ `Open`
        - ❌ `ServeHTTP`

- **File:** `src/testing/fstest/mapfs.go`
    - Ground Truth Functions (1):
        - `Sub`
    - Predicted Functions (0):

- **File:** `src/testing/fstest/testfs.go`
    - Ground Truth Functions (2):
        - `TestFS`
        - `testFS`
    - Predicted Functions (0):


### 📊 **Proposal #53747 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 50.0% | 30.8% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/flag/example_func_test.go`
    - Ground Truth Functions (1):
        - `ExampleBoolFunc`
    - Predicted Functions (0):

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (1):
        - `BoolFunc`
    - Predicted Functions (4):
        - ✅ `BoolFunc`
        - ❌ `Func`
        - ❌ `IsBoolFlag`
        - ❌ `Set`

- **File:** `src/flag/flag_test.go`
    - Ground Truth Functions (2):
        - `TestEverything`
        - `TestUserDefinedBoolFunc`
    - Predicted Functions (5):
        - ❌ `IsBoolFlag`
        - ❌ `Set`
        - ❌ `String`
        - ✅ `TestUserDefinedBoolFunc`
        - ❌ `boolFlagVar`


### 📊 **Proposal #50102 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 8.3% | 11.8% | 1/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/common.go`
    - Ground Truth Functions (2):
        - `FileInfoHeader`
        - `isHeaderOnlyType`
    - Predicted Functions (4):
        - ✅ `FileInfoHeader`
        - ❌ `FileInfoNames`
        - ❌ `Gname`
        - ❌ `Uname`

- **File:** `src/archive/tar/stat_unix.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (1):
        - ❌ `statUnix`

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


### 📊 **Proposal #46552 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 47.6% | 90.9% | 62.5% | 10/11 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/internal/syscall/windows/syscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/syscall/windows/zsyscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `SyscallN`

- **File:** `src/runtime/syscall_windows.go`
    - Ground Truth Functions (7):
        - `syscall_Syscall`
        - `syscall_Syscall12`
        - `syscall_Syscall15`
        - `syscall_Syscall18`
        - `syscall_Syscall6`
        - `syscall_Syscall9`
        - `syscall_SyscallN`
    - Predicted Functions (8):
        - ✅ `syscall_Syscall`
        - ✅ `syscall_Syscall12`
        - ✅ `syscall_Syscall15`
        - ✅ `syscall_Syscall18`
        - ✅ `syscall_Syscall6`
        - ✅ `syscall_Syscall9`
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
    - Predicted Functions (9):
        - ❌ `Addr`
        - ✅ `Call`
        - ❌ `Syscall`
        - ❌ `Syscall12`
        - ❌ `Syscall15`
        - ❌ `Syscall18`
        - ❌ `Syscall6`
        - ❌ `Syscall9`
        - ✅ `SyscallN`

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `SyscallN`

- **File:** `src/syscall/zsyscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `SyscallN`


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
    - Predicted Functions (10):
        - ❌ `TestFloat32Distribution`
        - ❌ `TestFloat64Distribution`
        - ❌ `TestIssue2379`
        - ❌ `TestIssue3521`
        - ❌ `TestRatSetFrac64Rat`
        - ❌ `TestSetFloat64NonFinite`
        - ❌ `checkIsBestApprox32`
        - ❌ `checkIsBestApprox64`
        - ❌ `checkNonLossyRoundtrip32`
        - ❌ `checkNonLossyRoundtrip64`

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


### 📊 **Proposal #39178 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 33.3% | 28.6% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/lookup.go`
    - Ground Truth Functions (1):
        - `lookupIPAddr`
    - Predicted Functions (4):
        - ❌ `LookupIP`
        - ❌ `LookupIPAddr`
        - ❌ `LookupNetIP`
        - ✅ `lookupIPAddr`

- **File:** `src/net/lookup_test.go`
    - Ground Truth Functions (2):
        - `TestDNSTimeout`
        - `TestLookupContextCancel`
    - Predicted Functions (0):


### 📊 **Proposal #48801 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.7% | 33.3% | 12.5% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat/timeformat.go`
    - Ground Truth Functions (2):
        - `badFormatAt`
        - `run`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (1):
        - ✅ `main`

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestVet`
        - ❌ `errorCheck`
        - ❌ `wantedErrors`

- **File:** `src/time/format.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `AppendFormat`
        - ❌ `Format`
        - ❌ `Parse`
        - ❌ `ParseInLocation`
        - ❌ `appendFormat`
        - ❌ `parse`

- **File:** `src/time/format_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Format`
        - ❌ `Parse`
        - ❌ `ParseInLocation`


### 📊 **Proposal #53466 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 64.2% | 95.0% | 76.7% | 115/121 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/asm/internal/arch/riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `IsRISCV64AMO`
        - ❌ `IsRISCV64VTypeI`
        - ❌ `RISCV64SpecialOperand`
        - ❌ `RISCV64ValidateVectorType`

- **File:** `src/cmd/compile/internal/riscv64/galign.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Init`

- **File:** `src/cmd/compile/internal/riscv64/ggen.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `zeroRange`

- **File:** `src/cmd/compile/internal/riscv64/gsubr.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ginsnop`

- **File:** `src/cmd/compile/internal/riscv64/ssa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `largestMove`
        - ❌ `loadByType`
        - ❌ `ssaGenBlock`
        - ❌ `ssaGenValue`
        - ❌ `storeByType`

- **File:** `src/cmd/dist/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `extLink`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/lib.go`
    - Ground Truth Functions (1):
        - `extld`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/outbuf_freebsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `fallocate`

- **File:** `src/cmd/link/internal/riscv64/obj.go`
    - Ground Truth Functions (2):
        - `Init`
        - `archinit`
    - Predicted Functions (0):

- **File:** `src/internal/abi/abi_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/cpu/cpu_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `doinit`
        - ❌ `isSet`

- **File:** `src/internal/cpu/cpu_riscv64_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `osInit`
        - ❌ `riscvHWProbe`

- **File:** `src/internal/cpu/cpu_riscv64_other.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osInit`

- **File:** `src/internal/goarch/goarch_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goarch/zgoarch_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/defs_freebsd_riscv64.go`
    - Ground Truth Functions (2):
        - `setNsec`
        - `set_usec`
    - Predicted Functions (2):
        - ✅ `setNsec`
        - ✅ `set_usec`

- **File:** `src/runtime/os_freebsd_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osArchInit`

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
    - Predicted Functions (7):
        - ✅ `SetControllen`
        - ✅ `SetKevent`
        - ✅ `SetLen`
        - ✅ `Syscall9`
        - ✅ `sendfile`
        - ✅ `setTimespec`
        - ✅ `setTimeval`

- **File:** `src/syscall/zerrors_freebsd_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

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
    - Predicted Functions (110):
        - ✅ `Access`
        - ✅ `Adjtime`
        - ✅ `Chdir`
        - ✅ `Chflags`
        - ✅ `Chmod`
        - ✅ `Chown`
        - ✅ `Chroot`
        - ✅ `Close`
        - ✅ `Dup`
        - ✅ `Dup2`
        - ✅ `Fchdir`
        - ✅ `Fchflags`
        - ✅ `Fchmod`
        - ✅ `Fchown`
        - ✅ `Flock`
        - ✅ `Fpathconf`
        - ✅ `Fstat`
        - ✅ `Fstatat`
        - ✅ `Fstatfs`
        - ✅ `Fsync`
        - ✅ `Ftruncate`
        - ✅ `Getdtablesize`
        - ✅ `Getegid`
        - ✅ `Geteuid`
        - ✅ `Getgid`
        - ✅ `Getpgid`
        - ✅ `Getpgrp`
        - ✅ `Getpid`
        - ✅ `Getppid`
        - ✅ `Getpriority`
        - ✅ `Getrlimit`
        - ✅ `Getrusage`
        - ✅ `Getsid`
        - ✅ `Gettimeofday`
        - ✅ `Getuid`
        - ✅ `Issetugid`
        - ✅ `Kill`
        - ✅ `Kqueue`
        - ✅ `Lchown`
        - ✅ `Link`
        - ✅ `Listen`
        - ✅ `Mkdir`
        - ✅ `Mkfifo`
        - ✅ `Nanosleep`
        - ✅ `Open`
        - ✅ `Pathconf`
        - ✅ `Readlink`
        - ✅ `Rename`
        - ✅ `Revoke`
        - ✅ `Rmdir`
        - ✅ `Seek`
        - ✅ `Select`
        - ✅ `Setegid`
        - ✅ `Seteuid`
        - ✅ `Setgid`
        - ✅ `Setlogin`
        - ✅ `Setpgid`
        - ✅ `Setpriority`
        - ✅ `Setregid`
        - ✅ `Setreuid`
        - ✅ `Setsid`
        - ✅ `Settimeofday`
        - ✅ `Setuid`
        - ✅ `Shutdown`
        - ✅ `Statfs`
        - ✅ `Symlink`
        - ✅ `Sync`
        - ✅ `Truncate`
        - ✅ `Umask`
        - ✅ `Undelete`
        - ✅ `Unlink`
        - ✅ `Unmount`
        - ✅ `accept`
        - ✅ `accept4`
        - ✅ `bind`
        - ✅ `connect`
        - ✅ `fcntl`
        - ❌ `fcntlPtr`
        - ✅ `futimes`
        - ✅ `getcwd`
        - ✅ `getdirentries`
        - ✅ `getgroups`
        - ✅ `getpeername`
        - ✅ `getsockname`
        - ✅ `getsockopt`
        - ❌ `ioctl`
        - ❌ `ioctlPtr`
        - ✅ `kevent`
        - ✅ `mknodat`
        - ✅ `mmap`
        - ✅ `munmap`
        - ✅ `pipe2`
        - ✅ `pread`
        - ✅ `pwrite`
        - ✅ `read`
        - ✅ `readlen`
        - ✅ `recvfrom`
        - ✅ `recvmsg`
        - ✅ `sendmsg`
        - ✅ `sendto`
        - ✅ `setgroups`
        - ❌ `setrlimit`
        - ✅ `setsockopt`
        - ✅ `socket`
        - ✅ `socketpair`
        - ✅ `sysctl`
        - ✅ `utimensat`
        - ✅ `utimes`
        - ✅ `wait4`
        - ✅ `write`

- **File:** `src/syscall/zsysnum_freebsd_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/ztypes_freebsd_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #44505 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 50.0% | 14.3% | 3/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/asm/internal/lex/tokenizer.go`
    - Ground Truth Functions (1):
        - `Next`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/build.go`
    - Ground Truth Functions (2):
        - `cmdbootstrap`
        - `findgoversion`
    - Predicted Functions (2):
        - ✅ `cmdbootstrap`
        - ❌ `requiredBootstrapVersion`

- **File:** `src/cmd/dist/build_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestRequiredBootstrapVersion`

- **File:** `src/cmd/dist/buildgo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `defaultCCFunc`
        - ❌ `mktzdata`
        - ❌ `mkzdefaultcc`
        - ❌ `writeHeader`

- **File:** `src/cmd/dist/buildruntime.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `mkbuildcfg`
        - ❌ `mkobjabi`
        - ❌ `mkzversion`

- **File:** `src/cmd/dist/buildtag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `validtag`

- **File:** `src/cmd/dist/buildtag_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestBuildParser`

- **File:** `src/cmd/dist/buildtool.go`
    - Ground Truth Functions (1):
        - `bootstrapBuildTools`
    - Predicted Functions (3):
        - ✅ `bootstrapBuildTools`
        - ❌ `bootstrapFixImports`
        - ❌ `bootstrapRewriteFile`

- **File:** `src/cmd/dist/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `setDir`
        - ❌ `setEnv`
        - ❌ `unsetEnv`

- **File:** `src/cmd/dist/imports.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `readimports`
        - ❌ `resolveVendor`

- **File:** `src/cmd/dist/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `main`
        - ❌ `xmain`

- **File:** `src/cmd/dist/notgo122.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/quoted.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/supported_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestSupported`

- **File:** `src/cmd/dist/sys_default.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `sysinit`

- **File:** `src/cmd/dist/sys_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `sysinit`

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `makeGOROOTUnwritable`
    - Predicted Functions (8):
        - ❌ `buildModeSupported`
        - ❌ `cmdtest`
        - ❌ `hasBash`
        - ❌ `raceDetectorSupported`
        - ❌ `registerTest`
        - ❌ `registerTests`
        - ❌ `run`
        - ❌ `shouldRunTest`

- **File:** `src/cmd/dist/testjson.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/testjson_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/util.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (3):
        - ✅ `run`
        - ❌ `runEnv`
        - ❌ `xflagparse`

- **File:** `src/cmd/dist/util_gc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/util_gccgo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #49580 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 16.0% | 22.9% | 4/25 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/archive/tar/writer.go`
    - Ground Truth Functions (1):
        - `AddFS`
    - Predicted Functions (0):

- **File:** `src/archive/tar/writer_test.go`
    - Ground Truth Functions (1):
        - `TestWriterAddFS`
    - Predicted Functions (0):

- **File:** `src/io/fs/fs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `ValidPath`
        - ❌ `errClosed`
        - ❌ `errExist`
        - ❌ `errInvalid`
        - ❌ `errNotExist`
        - ❌ `errPermission`

- **File:** `src/io/fs/readlink.go`
    - Ground Truth Functions (2):
        - `Lstat`
        - `ReadLink`
    - Predicted Functions (2):
        - ✅ `Lstat`
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


### 📊 **Proposal #41184 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 27.6% | 7.4% | 11.7% | 27/364 |

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
    - Predicted Functions (46):
        - ❌ `NewParser`
        - ❌ `Parse`
        - ❌ `address`
        - ❌ `at`
        - ❌ `atRegisterExtension`
        - ❌ `atRegisterShift`
        - ❌ `atStartOfRegister`
        - ❌ `atof`
        - ❌ `atoi`
        - ❌ `back`
        - ❌ `errorf`
        - ❌ `expect`
        - ❌ `expectOperandEnd`
        - ❌ `expr`
        - ❌ `factor`
        - ❌ `floatExpr`
        - ❌ `funcAddress`
        - ❌ `get`
        - ❌ `have`
        - ❌ `instruction`
        - ✅ `line`
        - ❌ `more`
        - ❌ `next`
        - ✅ `nextToken`
        - ❌ `operand`
        - ❌ `parseScale`
        - ❌ `peek`
        - ❌ `pos`
        - ❌ `positiveAtoi`
        - ❌ `pseudo`
        - ❌ `qualifySymbol`
        - ❌ `register`
        - ❌ `registerExtension`
        - ❌ `registerIndirect`
        - ❌ `registerList`
        - ❌ `registerListARM`
        - ❌ `registerListX86`
        - ❌ `registerNumber`
        - ❌ `registerReference`
        - ❌ `registerShift`
        - ❌ `setPseudoRegister`
        - ❌ `start`
        - ❌ `symDefRef`
        - ❌ `symRefAttrs`
        - ❌ `symbolReference`
        - ❌ `term`

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

- **File:** `src/cmd/compile/internal/syntax/parser.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `clearPragma`
        - ❌ `commentText`
        - ❌ `takePragma`
        - ❌ `updateBase`

- **File:** `src/cmd/fix/buildtag.go`
    - Ground Truth Functions (2):
        - `buildtag`
        - `init`
    - Predicted Functions (2):
        - ✅ `buildtag`
        - ✅ `init`

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
    - Predicted Functions (8):
        - ✅ `AllFiles`
        - ❌ `InternalAllGoFiles`
        - ❌ `InternalGoFiles`
        - ❌ `InternalXGoFiles`
        - ❌ `LoadPackage`
        - ❌ `ResolveImportPath`
        - ❌ `loadImport`
        - ❌ `loadPackageData`

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `AddBuildFlags`
        - ❌ `runBuild`
        - ❌ `runInstall`

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (1):
        - `buildVetConfig`
    - Predicted Functions (3):
        - ❌ `build`
        - ❌ `checkDirectives`
        - ❌ `vet`

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

- **File:** `src/cmd/vet/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`

- **File:** `src/cmd/vet/testdata/buildtag/buildtag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/vet/testdata/buildtag/buildtag2.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/vet/testdata/buildtag/buildtag3.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/vet/testdata/buildtag/buildtag4.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/vet/testdata/buildtag/buildtag5.go`
    - Ground Truth Functions (0):
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
    - Predicted Functions (5):
        - ❌ `MatchFile`
        - ✅ `goodOSArchFile`
        - ✅ `isGoBuildComment`
        - ✅ `matchFile`
        - ✅ `shouldBuild`

- **File:** `src/go/build/build_test.go`
    - Ground Truth Functions (2):
        - `TestMatch`
        - `TestShouldBuild`
    - Predicted Functions (0):

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
    - Predicted Functions (9):
        - ✅ `IsGoBuild`
        - ✅ `IsPlusBuild`
        - ✅ `Parse`
        - ✅ `PlusBuildLines`
        - ✅ `isValidTag`
        - ✅ `parseExpr`
        - ✅ `parsePlusBuildExpr`
        - ✅ `splitGoBuild`
        - ✅ `splitPlusBuild`

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
    - Predicted Functions (4):
        - ✅ `TestParseError`
        - ✅ `TestParseExpr`
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
    - Predicted Functions (4):
        - ✅ `appendLines`
        - ✅ `commentTextAt`
        - ✅ `fixGoBuildLines`
        - ✅ `lineAt`

- **File:** `src/go/printer/printer.go`
    - Ground Truth Functions (3):
        - `fprint`
        - `printNode`
        - `writeComment`
    - Predicted Functions (4):
        - ❌ `intersperseComments`
        - ✅ `writeComment`
        - ❌ `writeCommentPrefix`
        - ❌ `writeCommentSuffix`

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


### 📊 **Proposal #51225 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 50.0% | 36.4% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/base/flag.go`
    - Ground Truth Functions (2):
        - `ParseFlags`
        - `readImportCfg`
    - Predicted Functions (5):
        - ✅ `ParseFlags`
        - ❌ `addImportDir`
        - ✅ `readImportCfg`
        - ❌ `registerFlags`
        - ❌ `usage`

- **File:** `src/cmd/compile/internal/gc/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Main`

- **File:** `src/cmd/compile/internal/noder/import.go`
    - Ground Truth Functions (1):
        - `openPackage`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (1):
        - `gc`
    - Predicted Functions (0):


### 📊 **Proposal #38776 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.4% | 4.5% | 3.9% | 1/22 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/internal/boring/sha.go`
    - Ground Truth Functions (3):
        - `MarshalBinary`
        - `NewSHA512`
        - `sum`
    - Predicted Functions (0):

- **File:** `src/crypto/sha1/sha1.go`
    - Ground Truth Functions (1):
        - `Write`
    - Predicted Functions (3):
        - ✅ `Write`
        - ❌ `WriteByte`
        - ❌ `WriteString`

- **File:** `src/crypto/sha1/sha1_test.go`
    - Ground Truth Functions (3):
        - `TestAllocations`
        - `TestGolden`
        - `TestLargeHashes`
    - Predicted Functions (0):

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
    - Predicted Functions (0):

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

- **File:** `src/crypto/sha512/sha512_test.go`
    - Ground Truth Functions (5):
        - `TestAllocations`
        - `TestGolden`
        - `TestLargeHashes`
        - `benchmarkSize`
        - `testHash`
    - Predicted Functions (0):

- **File:** `src/hash/adler32/adler32.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Write`
        - ❌ `WriteByte`
        - ❌ `WriteString`

- **File:** `src/hash/crc32/crc32.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Write`
        - ❌ `WriteByte`
        - ❌ `WriteString`

- **File:** `src/hash/crc64/crc64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Write`
        - ❌ `WriteByte`
        - ❌ `WriteString`

- **File:** `src/hash/fnv/fnv.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Write`
        - ❌ `WriteByte`
        - ❌ `WriteString`

- **File:** `src/hash/maphash/maphash.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `WriteByte`
        - ❌ `WriteString`


### 📊 **Proposal #38781 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 60.0% | 66.7% | 3/5 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/testing/iotest/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ExampleErrReader`

- **File:** `src/testing/iotest/logger_test.go`
    - Ground Truth Functions (2):
        - `TestReadLogger`
        - `TestReadLogger_errorOnRead`
    - Predicted Functions (0):

- **File:** `src/testing/iotest/reader.go`
    - Ground Truth Functions (2):
        - `ErrReader`
        - `Read`
    - Predicted Functions (2):
        - ✅ `ErrReader`
        - ✅ `Read`

- **File:** `src/testing/iotest/reader_test.go`
    - Ground Truth Functions (1):
        - `TestErrReader`
    - Predicted Functions (1):
        - ✅ `TestErrReader`


### 📊 **Proposal #30715 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 50.0% | 44.4% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/request.go`
    - Ground Truth Functions (3):
        - `Error`
        - `MaxBytesReader`
        - `Read`
    - Predicted Functions (5):
        - ❌ `Close`
        - ❌ `MaxBytesError`
        - ✅ `MaxBytesReader`
        - ✅ `Read`
        - ❌ `parsePostForm`

- **File:** `src/net/http/serve_test.go`
    - Ground Truth Functions (1):
        - `testRequestBodyLimit`
    - Predicted Functions (0):


### 📊 **Proposal #28308 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 2.2% | 3.5% | 2/91 |

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
    - Predicted Functions (1):
        - ✅ `main`

- **File:** `src/cmd/vet/testdata/hostport/hostport.go`
    - Ground Truth Functions (1):
        - `_`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (1):
        - `TestVet`
    - Predicted Functions (3):
        - ✅ `TestVet`
        - ❌ `errorCheck`
        - ❌ `wantedErrors`

- **File:** `src/fmt/format.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `fmtBs`
        - ❌ `fmtBx`
        - ❌ `fmtQ`
        - ❌ `fmtS`
        - ❌ `fmtSbx`
        - ❌ `fmtSx`

- **File:** `src/net/dial.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Dial`
        - ❌ `DialContext`
        - ❌ `DialTimeout`
        - ❌ `dialParallel`
        - ❌ `dialSerial`
        - ❌ `dialSingle`

- **File:** `src/net/dial_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestDialLocal`
        - ❌ `TestDialWithNonZeroDeadline`
        - ❌ `TestDialerControl`
        - ❌ `TestDialerControlContext`
        - ❌ `TestDialerDualStack`

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


### 📊 **Proposal #38687 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 66.7% | 44.4% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/generate/generate.go`
    - Ground Truth Functions (3):
        - `init`
        - `run`
        - `runGenerate`
    - Predicted Functions (3):
        - ❌ `generate`
        - ✅ `run`
        - ✅ `runGenerate`

- **File:** `src/cmd/go/internal/generate/generate_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestGenerateCommandParse`
        - ❌ `TestGenerateCommandShortHand2`
        - ❌ `TestGenerateCommandShorthand`


### 📊 **Proposal #37519 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 33.3% | 18.2% | 1/3 |

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
    - Predicted Functions (8):
        - ❌ `newResolver`
        - ❌ `parseArgs`
        - ❌ `queryModule`
        - ❌ `queryPackages`
        - ❌ `queryPath`
        - ❌ `resolveQueries`
        - ✅ `runGet`
        - ❌ `updateBuildList`


### 📊 **Proposal #51766 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Functions per File

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
    - Predicted Functions (2):
        - ❌ `AddrFrom16`
        - ✅ `TestAddrWellKnown`


### 📊 **Proposal #51896 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 26.7% | 100.0% | 42.1% | 4/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/unicode/utf16/utf16.go`
    - Ground Truth Functions (1):
        - `AppendRune`
    - Predicted Functions (4):
        - ✅ `AppendRune`
        - ❌ `Encode`
        - ❌ `EncodeRune`
        - ❌ `RuneLen`

- **File:** `src/unicode/utf16/utf16_test.go`
    - Ground Truth Functions (3):
        - `BenchmarkAppendRuneValidASCII`
        - `BenchmarkAppendRuneValidJapaneseChars`
        - `TestAppendRune`
    - Predicted Functions (11):
        - ❌ `AppendRune`
        - ✅ `BenchmarkAppendRuneValidASCII`
        - ✅ `BenchmarkAppendRuneValidJapaneseChars`
        - ❌ `BenchmarkEncodeRune`
        - ❌ `BenchmarkEncodeValidASCII`
        - ❌ `BenchmarkEncodeValidJapaneseChars`
        - ❌ `Encode`
        - ❌ `EncodeRune`
        - ✅ `TestAppendRune`
        - ❌ `TestEncode`
        - ❌ `TestEncodeRune`


### 📊 **Proposal #34527 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/cache/cache.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `GetFile`
        - ❌ `Open`
        - ❌ `PutBytes`
        - ❌ `PutNoVerify`
        - ❌ `initEnv`

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
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `CachePath`
        - ❌ `DownloadDir`
        - ❌ `cacheDir`
        - ❌ `checkCacheDir`

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

- **File:** `src/cmd/go/internal/modfetch/sumdb.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `ReadCache`
        - ❌ `ReadConfig`
        - ❌ `WriteCache`
        - ❌ `WriteConfig`


### 📊 **Proposal #51566 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 3/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/io/io.go`
    - Ground Truth Functions (2):
        - `NopCloser`
        - `WriteTo`
    - Predicted Functions (3):
        - ❌ `Close`
        - ✅ `NopCloser`
        - ✅ `WriteTo`

- **File:** `src/io/io_test.go`
    - Ground Truth Functions (1):
        - `TestNopCloserWriterToForwarding`
    - Predicted Functions (3):
        - ❌ `TestCopyWriteTo`
        - ✅ `TestNopCloserWriterToForwarding`
        - ❌ `WriteTo`

- **File:** `src/net/http/transfer.go`
    - Ground Truth Functions (3):
        - `isKnownInMemoryReader`
        - `unwrapBody`
        - `unwrapNopCloser`
    - Predicted Functions (0):


### 📊 **Proposal #39214 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.7% | 13.0% | 7.9% | 3/23 |

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
    - Predicted Functions (1):
        - ❌ `Initialize`

- **File:** `src/internal/cpu/cpu_arm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `doinit`
        - ❌ `isSet`
        - ❌ `isV7`

- **File:** `src/internal/cpu/cpu_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `getMIDR`

- **File:** `src/internal/cpu/cpu_arm64_android.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osInit`

- **File:** `src/internal/cpu/cpu_arm64_darwin.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `getsysctlbyname`
        - ❌ `osInit`
        - ❌ `sysctlEnabled`

- **File:** `src/internal/cpu/cpu_arm64_freebsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osInit`

- **File:** `src/internal/cpu/cpu_arm64_hwcap.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `hwcapInit`
        - ❌ `isSet`

- **File:** `src/internal/cpu/cpu_arm64_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osInit`

- **File:** `src/internal/cpu/cpu_arm64_openbsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osInit`

- **File:** `src/internal/cpu/cpu_arm64_other.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osInit`

- **File:** `src/internal/cpu/cpu_loong64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `doinit`

- **File:** `src/internal/cpu/cpu_loong64_hwcap.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `hwcIsSet`
        - ❌ `hwcapInit`

- **File:** `src/internal/cpu/cpu_loong64_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osInit`

- **File:** `src/internal/cpu/cpu_mips.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `doinit`

- **File:** `src/internal/cpu/cpu_mips64x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `doinit`
        - ❌ `isSet`

- **File:** `src/internal/cpu/cpu_mipsle.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `doinit`

- **File:** `src/internal/cpu/cpu_no_name.go`
    - Ground Truth Functions (1):
        - `Name`
    - Predicted Functions (1):
        - ✅ `Name`

- **File:** `src/internal/cpu/cpu_ppc64x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Name`

- **File:** `src/internal/cpu/cpu_ppc64x_aix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `getsystemcfg`
        - ❌ `osinit`

- **File:** `src/internal/cpu/cpu_ppc64x_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osinit`

- **File:** `src/internal/cpu/cpu_ppc64x_other.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osinit`

- **File:** `src/internal/cpu/cpu_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `doinit`
        - ❌ `isSet`

- **File:** `src/internal/cpu/cpu_riscv64_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osInit`

- **File:** `src/internal/cpu/cpu_riscv64_other.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `osInit`

- **File:** `src/internal/cpu/cpu_s390x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `doinit`

- **File:** `src/internal/cpu/cpu_s390x_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestS390XAgainstCPUInfo`
        - ❌ `getFeatureList`

- **File:** `src/internal/cpu/cpu_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `MustSupportFeatureDetection`
        - ❌ `TestAllCapabilitiesDisabled`
        - ❌ `TestDisableAllCapabilities`

- **File:** `src/internal/cpu/cpu_wasm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `doinit`

- **File:** `src/internal/cpu/cpu_x86.go`
    - Ground Truth Functions (3):
        - `Name`
        - `appendBytes`
        - `doinit`
    - Predicted Functions (2):
        - ✅ `Name`
        - ✅ `doinit`

- **File:** `src/internal/cpu/cpu_x86_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestDisableSSE3`
        - ❌ `TestSSE3DebugOption`

- **File:** `src/internal/cpu/export_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/cpu/export_x86_test.go`
    - Ground Truth Functions (0):
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

- **File:** `src/testing/benchmark.go`
    - Ground Truth Functions (2):
        - `Run`
        - `run`
    - Predicted Functions (4):
        - ❌ `RunBenchmarks`
        - ❌ `prettyPrint`
        - ❌ `processBench`
        - ❌ `runBenchmarks`

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Main`
        - ❌ `Printf`
        - ❌ `RunTests`
        - ❌ `report`
        - ❌ `runTests`


### 📊 **Proposal #34626 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 66.7% | 50.0% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/testing/benchmark.go`
    - Ground Truth Functions (1):
        - `prettyPrint`
    - Predicted Functions (3):
        - ❌ `NsPerOp`
        - ❌ `String`
        - ✅ `prettyPrint`

- **File:** `src/testing/benchmark_test.go`
    - Ground Truth Functions (2):
        - `TestReportMetric`
        - `TestResultString`
    - Predicted Functions (2):
        - ❌ `TestPrettyPrint`
        - ✅ `TestResultString`


### 📊 **Proposal #45100 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 100.0% | 44.4% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/url/url.go`
    - Ground Truth Functions (1):
        - `Has`
    - Predicted Functions (5):
        - ❌ `Add`
        - ❌ `Del`
        - ❌ `Get`
        - ✅ `Has`
        - ❌ `Set`

- **File:** `src/net/url/url_test.go`
    - Ground Truth Functions (1):
        - `TestQueryValues`
    - Predicted Functions (2):
        - ❌ `TestParseQuery`
        - ✅ `TestQueryValues`


### 📊 **Proposal #44167 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 36.0% | 45.0% | 27/75 |

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
    - Predicted Functions (6):
        - ✅ `gcBgMarkWorker`
        - ✅ `gcMark`
        - ✅ `gcMarkDone`
        - ✅ `gcMarkTermination`
        - ✅ `gcStart`
        - ✅ `gcSweep`

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
    - Predicted Functions (15):
        - ❌ `gcAssistAlloc`
        - ❌ `gcAssistAlloc1`
        - ✅ `gcDrain`
        - ❌ `gcDrainMarkWorkerDedicated`
        - ❌ `gcDrainMarkWorkerFractional`
        - ❌ `gcDrainMarkWorkerIdle`
        - ✅ `gcDrainN`
        - ✅ `gcFlushBgCredit`
        - ❌ `gcMarkTinyAllocs`
        - ❌ `gcParkAssist`
        - ❌ `gcWakeAllAssists`
        - ✅ `gcmarknewobject`
        - ❌ `greyobject`
        - ❌ `scanblock`
        - ✅ `scanobject`

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
    - Predicted Functions (14):
        - ✅ `addGlobals`
        - ✅ `addScannableStack`
        - ✅ `commit`
        - ✅ `endCycle`
        - ❌ `heapGoal`
        - ❌ `heapGoalInternal`
        - ✅ `init`
        - ❌ `memoryLimitHeapGoal`
        - ✅ `revise`
        - ✅ `setGCPercent`
        - ❌ `setMemoryLimit`
        - ✅ `startCycle`
        - ❌ `trigger`
        - ✅ `update`

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
    - Predicted Functions (8):
        - ✅ `String`
        - ✅ `TestGcPacer`
        - ❌ `applyMemoryLimitHeapGoalHeadroom`
        - ✅ `check`
        - ✅ `goalRatio`
        - ✅ `next`
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
    - Predicted Functions (2):
        - ✅ `deductSweepCredit`
        - ✅ `gcPaceSweeper`

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

- **File:** `test/gc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/gc1.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/gc2.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #51430 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.1% | 33.1% | 33.1% | 54/163 |

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
    - Predicted Functions (3):
        - ✅ `fatal`
        - ✅ `main`
        - ✅ `usage`

- **File:** `src/cmd/covdata/doc.go`
    - Ground Truth Functions (0):
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
    - Predicted Functions (5):
        - ✅ `first`
        - ✅ `fourth`
        - ✅ `main`
        - ✅ `second`
        - ✅ `third`

- **File:** `src/cmd/covdata/testdata/prog2.go`
    - Ground Truth Functions (3):
        - `fifth`
        - `main`
        - `sixth`
    - Predicted Functions (3):
        - ✅ `fifth`
        - ✅ `main`
        - ✅ `sixth`

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
        - ❌ `mkCounterVarName`
        - ❌ `mkMetaVar`
        - ❌ `mkPackageIdExpression`
        - ❌ `mkPackageIdVar`
        - ❌ `newCounter`
        - ❌ `setCounterStmt`

- **File:** `src/cmd/cover/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/cover/testdata/html/html.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `f`
        - ❌ `g`

- **File:** `src/cmd/cover/testdata/html/html_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestAll`

- **File:** `src/cmd/cover/testdata/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `check`
        - ❌ `checkVal`
        - ❌ `count`
        - ❌ `main`
        - ❌ `verify`
        - ❌ `verifyPanic`

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

- **File:** `src/cmd/cover/testdata/test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (14):
        - ❌ `testAll`
        - ❌ `testBlockRun`
        - ❌ `testEmptySwitches`
        - ❌ `testFor`
        - ❌ `testFunctionLiteral`
        - ❌ `testGoto`
        - ❌ `testIf`
        - ❌ `testPanic`
        - ❌ `testRange`
        - ❌ `testSelect1`
        - ❌ `testSelect2`
        - ❌ `testSimple`
        - ❌ `testSwitch`
        - ❌ `testTypeSwitch`

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

- **File:** `src/internal/coverage/cfile/apis.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `ClearCounters`
        - ❌ `WriteCounters`
        - ❌ `WriteCountersDir`
        - ❌ `WriteMeta`
        - ❌ `WriteMetaDir`

- **File:** `src/internal/coverage/cfile/emit.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `MarkProfileEmitted`
        - ❌ `emitCounterData`
        - ❌ `emitCounterDataFile`
        - ❌ `emitCounterDataToDirectory`
        - ❌ `emitMetaData`
        - ❌ `emitMetaDataFile`
        - ❌ `emitMetaDataToDirectory`

- **File:** `src/internal/coverage/cfile/hooks.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `InitHook`

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
    - Predicted Functions (7):
        - ✅ `AddUnit`
        - ✅ `EmitFuncs`
        - ✅ `EmitPercent`
        - ✅ `EmitTextual`
        - ✅ `NewFormatter`
        - ✅ `SetPackage`
        - ✅ `sortUnits`

- **File:** `src/internal/coverage/cmerge/merge.go`
    - Ground Truth Functions (6):
        - `Granularity`
        - `MergeCounters`
        - `Mode`
        - `ResetModeAndGranularity`
        - `SaturatingAdd`
        - `SetModeAndGranularity`
    - Predicted Functions (7):
        - ✅ `Granularity`
        - ✅ `MergeCounters`
        - ✅ `Mode`
        - ✅ `ResetModeAndGranularity`
        - ✅ `SaturatingAdd`
        - ✅ `SetModeAndGranularity`
        - ❌ `SetModeMergePolicy`

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
    - Predicted Functions (13):
        - ✅ `BeginNextSegment`
        - ✅ `Goarch`
        - ✅ `Goos`
        - ✅ `NewCounterDataReader`
        - ✅ `NextFunc`
        - ✅ `NumFunctionsInSegment`
        - ✅ `NumSegments`
        - ✅ `OsArgs`
        - ✅ `checkMagic`
        - ✅ `readArgs`
        - ✅ `readFooter`
        - ✅ `readSegmentPreamble`
        - ✅ `readStringTable`

- **File:** `src/internal/coverage/decodemeta/decode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `ModulePath`
        - ❌ `NewCoverageMetaDataDecoder`
        - ❌ `NumFuncs`
        - ❌ `PackageName`
        - ❌ `PackagePath`
        - ❌ `ReadFunc`
        - ❌ `readHeader`
        - ❌ `readStringTable`

- **File:** `src/internal/coverage/decodemeta/decodefile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `CounterGranularity`
        - ❌ `CounterMode`
        - ❌ `FileHash`
        - ❌ `GetPackageDecoder`
        - ❌ `GetPackagePayload`
        - ❌ `NewCoverageMetaFileReader`
        - ❌ `NumPackages`
        - ❌ `readFileHeader`

- **File:** `src/internal/coverage/defs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `ParseCounterMode`
        - ❌ `Round4`
        - ❌ `String`

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
    - Predicted Functions (5):
        - ✅ `NewCoverageDataWriter`
        - ✅ `Write`
        - ✅ `writeCounters`
        - ✅ `writeFooter`
        - ✅ `writeHeader`

- **File:** `src/internal/coverage/encodemeta/encode.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `AddFunc`
        - ❌ `Emit`
        - ❌ `HashFuncDesc`
        - ❌ `NewCoverageMetaDataBuilder`

- **File:** `src/internal/coverage/encodemeta/encodefile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `NewCoverageMetaFileWriter`
        - ❌ `Write`

- **File:** `src/internal/coverage/pkid.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `HardCodedPkgID`

- **File:** `src/internal/coverage/pods/pods.go`
    - Ground Truth Functions (4):
        - `CollectPods`
        - `CollectPodsFromFiles`
        - `collectPodsImpl`
        - `warning`
    - Predicted Functions (3):
        - ✅ `CollectPods`
        - ✅ `CollectPodsFromFiles`
        - ✅ `collectPodsImpl`

- **File:** `src/internal/coverage/pods/pods_test.go`
    - Ground Truth Functions (1):
        - `TestPodCollection`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/rtcov/rtcov.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `AddMeta`

- **File:** `src/internal/coverage/slicereader/slicereader.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `NewReader`
        - ❌ `Read`
        - ❌ `ReadString`
        - ❌ `ReadULEB128`
        - ❌ `ReadUint32`
        - ❌ `ReadUint64`
        - ❌ `ReadUint8`
        - ❌ `Seek`

- **File:** `src/internal/coverage/slicewriter/slicewriter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `BytesWritten`
        - ❌ `Read`
        - ❌ `Seek`
        - ❌ `Write`

- **File:** `src/internal/coverage/stringtab/stringtab.go`
    - Ground Truth Functions (5):
        - `Entries`
        - `Freeze`
        - `Get`
        - `Lookup`
        - `NewReader`
    - Predicted Functions (10):
        - ✅ `Entries`
        - ✅ `Freeze`
        - ✅ `Get`
        - ❌ `InitWriter`
        - ✅ `Lookup`
        - ❌ `Nentries`
        - ✅ `NewReader`
        - ❌ `Read`
        - ❌ `Size`
        - ❌ `Write`

- **File:** `src/internal/coverage/test/counter_test.go`
    - Ground Truth Functions (4):
        - `TestCounterDataAppendSegment`
        - `TestCounterDataWriterReader`
        - `VisitFuncs`
        - `mkfunc`
    - Predicted Functions (0):

- **File:** `src/internal/coverage/uleb128/uleb128.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `AppendUleb128`

- **File:** `src/runtime/coverage/coverage.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `ClearCounters`
        - ❌ `WriteCounters`
        - ❌ `WriteCountersDir`
        - ❌ `WriteMeta`
        - ❌ `WriteMetaDir`

- **File:** `src/runtime/covercounter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `coverage_getCovCounterList`

- **File:** `src/runtime/covermeta.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `addCovMeta`

- **File:** `src/testing/cover.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `RegisterCover`

- **File:** `src/testing/newcover.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Coverage`
        - ❌ `coverReport`
        - ❌ `registerCover`


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
    - Predicted Functions (6):
        - ❌ `Field`
        - ✅ `IsExported`
        - ❌ `Method`
        - ❌ `NumField`
        - ❌ `NumMethod`
        - ❌ `PkgPath`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `IsExported`
        - ❌ `mustBeExported`
        - ❌ `mustBeExportedSlow`

- **File:** `src/text/template/exec.go`
    - Ground Truth Functions (1):
        - `evalField`
    - Predicted Functions (0):


### 📊 **Proposal #31804 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 57.1% | 50.0% | 53.3% | 4/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/ed25519/ed25519.go`
    - Ground Truth Functions (5):
        - `Sign`
        - `Verify`
        - `VerifyWithOptions`
        - `newKeyFromSeed`
        - `sign`
    - Predicted Functions (3):
        - ❌ `HashFunc`
        - ✅ `Sign`
        - ✅ `VerifyWithOptions`

- **File:** `src/crypto/ed25519/ed25519_test.go`
    - Ground Truth Functions (3):
        - `TestCryptoSigner`
        - `TestSignVerifyContext`
        - `TestSignVerifyHashed`
    - Predicted Functions (3):
        - ❌ `Example_ed25519ctx`
        - ✅ `TestSignVerifyContext`
        - ✅ `TestSignVerifyHashed`

- **File:** `src/crypto/ed25519/ed25519vectors_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestEd25519Vectors`


### 📊 **Proposal #33920 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 80.0% | 80.0% | 80.0% | 4/5 |

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
    - Predicted Functions (3):
        - ✅ `TestTempDir_BadPattern`
        - ✅ `TestTempFile_BadPattern`
        - ❌ `TestTempFile_pattern`

- **File:** `src/os/os_test.go`
    - Ground Truth Functions (1):
        - `TestStatDirWithTrailingSlash`
    - Predicted Functions (0):


### 📊 **Proposal #33184 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 50.0% | 46.2% | 3/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/time.go`
    - Ground Truth Functions (1):
        - `goroutineReady`
    - Predicted Functions (0):

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
        - ✅ `BenchmarkTickerResetNaive`
        - ❌ `Reset`
        - ❌ `TestTickerResetLtZeroDuration`


### 📊 **Proposal #42537 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.2% | 4.6% | 6.7% | 5/108 |

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
    - Predicted Functions (1):
        - ❌ `stdVendor`

- **File:** `src/cmd/go/proxy_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `proxyGoSum`
        - ❌ `proxyGoSumWrong`
        - ❌ `proxyHandler`
        - ❌ `readArchive`

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
    - Predicted Functions (2):
        - ✅ `ParseMediaType`
        - ❌ `consumeValue`

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

- **File:** `src/strings/strings.go`
    - Ground Truth Functions (2):
        - `CutPrefix`
        - `CutSuffix`
    - Predicted Functions (7):
        - ❌ `Cut`
        - ✅ `CutPrefix`
        - ✅ `CutSuffix`
        - ❌ `HasPrefix`
        - ❌ `HasSuffix`
        - ❌ `TrimPrefix`
        - ❌ `TrimSuffix`

- **File:** `src/strings/strings_test.go`
    - Ground Truth Functions (2):
        - `TestCutPrefix`
        - `TestCutSuffix`
    - Predicted Functions (3):
        - ❌ `TestCut`
        - ✅ `TestCutPrefix`
        - ✅ `TestCutSuffix`

- **File:** `src/testing/benchmark.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `trimOutput`

- **File:** `src/testing/fstest/mapfs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (23):
        - ❌ `Close`
        - ❌ `Glob`
        - ❌ `Info`
        - ❌ `IsDir`
        - ❌ `Lstat`
        - ❌ `ModTime`
        - ❌ `Mode`
        - ❌ `Name`
        - ❌ `Open`
        - ❌ `Read`
        - ❌ `ReadAt`
        - ❌ `ReadDir`
        - ❌ `ReadFile`
        - ❌ `ReadLink`
        - ❌ `Seek`
        - ❌ `Size`
        - ❌ `Stat`
        - ❌ `String`
        - ❌ `Sub`
        - ❌ `Sys`
        - ❌ `Type`
        - ❌ `lstat`
        - ❌ `resolveSymlinks`

- **File:** `src/text/template/option.go`
    - Ground Truth Functions (1):
        - `setOption`
    - Predicted Functions (0):

- **File:** `test/zerodivide.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #32716 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.6% | 20.6% | 21.5% | 7/34 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/auth_test.go`
    - Ground Truth Functions (1):
        - `TestSignatureSelection`
    - Predicted Functions (1):
        - ❌ `TestLegacyTypeAndHash`

- **File:** `src/crypto/tls/cipher_suites.go`
    - Ground Truth Functions (4):
        - `Size`
        - `macSHA1`
        - `macSHA256`
        - `newConstantTimeHash`
    - Predicted Functions (4):
        - ❌ `cipher3DES`
        - ❌ `cipherRC4`
        - ❌ `rsaKA`
        - ❌ `tls10MAC`

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (3):
        - `maxSupportedVersion`
        - `mutualVersion`
        - `supportedVersions`
    - Predicted Functions (4):
        - ✅ `maxSupportedVersion`
        - ✅ `mutualVersion`
        - ✅ `supportedVersions`
        - ❌ `supportedVersionsFromMax`

- **File:** `src/crypto/tls/conn.go`
    - Ground Truth Functions (4):
        - `Write`
        - `decrypt`
        - `handleRenegotiation`
        - `roundUp`
    - Predicted Functions (5):
        - ❌ `connectionStateLocked`
        - ❌ `handshakeContext`
        - ❌ `readChangeCipherSpec`
        - ❌ `readRecord`
        - ❌ `readRecordOrCCS`

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
    - Predicted Functions (6):
        - ✅ `TestRejectBadProtocolVersion`
        - ❌ `runServerTestForVersion`
        - ❌ `runServerTestTLS10`
        - ❌ `runServerTestTLS11`
        - ❌ `runServerTestTLS12`
        - ✅ `runServerTestTLS13`

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
    - Predicted Functions (3):
        - ❌ `hashForServerKeyExchange`
        - ❌ `md5SHA1Hash`
        - ❌ `sha1Hash`

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
    - Predicted Functions (4):
        - ❌ `prf10`
        - ❌ `prf12`
        - ✅ `prfAndHashForVersion`
        - ✅ `prfForVersion`

- **File:** `src/crypto/tls/prf_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestKeysFromPreMasterSecret`
        - ❌ `TestSplitPreMasterSecret`

- **File:** `src/crypto/tls/tls_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestCipherSuites`
        - ❌ `TestVersionName`


### 📊 **Proposal #42681 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/asm/internal/lex/input.go`
    - Ground Truth Functions (1):
        - `predefine`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/base/base.go`
    - Ground Truth Functions (0):
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

- **File:** `src/cmd/go/internal/base/env.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/cfg/cfg.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `computeExperiment`

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
    - Predicted Functions (1):
        - ❌ `HeaderString`

- **File:** `src/cmd/link/internal/ld/main.go`
    - Ground Truth Functions (1):
        - `Main`
    - Predicted Functions (0):

- **File:** `src/internal/goexperiment/exp_fieldtrack_off.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goexperiment/exp_fieldtrack_on.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goexperiment/exp_preemptibleloops_off.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goexperiment/exp_preemptibleloops_on.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goexperiment/exp_staticlockranking_off.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goexperiment/exp_staticlockranking_on.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goexperiment/flags.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Fieldtrack_enabled`
        - ❌ `Preemptibleloops_enabled`
        - ❌ `Regabi_enabled`
        - ❌ `Staticlockranking_enabled`

- **File:** `src/runtime/heapdump.go`
    - Ground Truth Functions (1):
        - `dumpparams`
    - Predicted Functions (0):


### 📊 **Proposal #46746 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 37.5% | 42.9% | 40.0% | 3/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (4):
        - `TestConvert`
        - `TestConvertPanic`
        - `TestValue_Comparable`
        - `TestValue_Equal`
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Comparable`
        - ❌ `ConvertibleTo`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (3):
        - `CanConvert`
        - `Comparable`
        - `Equal`
    - Predicted Functions (6):
        - ✅ `CanConvert`
        - ❌ `CanInterface`
        - ✅ `Comparable`
        - ❌ `Convert`
        - ✅ `Equal`
        - ❌ `Interface`


### 📊 **Proposal #47142 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 17.6% | 12.5% | 14.6% | 3/24 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/database/sql/driver/driver.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `LastInsertId`
        - ❌ `RowsAffected`

- **File:** `src/database/sql/driver/types.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ConvertValue`

- **File:** `src/database/sql/driver/types_test.go`
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
    - Predicted Functions (10):
        - ❌ `beginDC`
        - ✅ `conn`
        - ❌ `execDC`
        - ❌ `prepareDC`
        - ✅ `putConn`
        - ❌ `putConnDBLocked`
        - ❌ `queryDC`
        - ❌ `releaseConn`
        - ❌ `retry`
        - ❌ `validateConnection`

- **File:** `src/database/sql/sql_test.go`
    - Ground Truth Functions (1):
        - `TestTxEndBadConn`
    - Predicted Functions (4):
        - ❌ `TestConnIsValid`
        - ❌ `TestErrBadConnReconnect`
        - ❌ `TestManyErrBadConn`
        - ✅ `TestTxEndBadConn`


### 📊 **Proposal #26535 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 41.7% | 58.8% | 10/24 |

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
        - ✅ `NewReader`
        - ✅ `Reset`
        - ✅ `init`
        - ✅ `newReader`

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
        - ✅ `NewWriter`
        - ✅ `Reset`
        - ✅ `init`
        - ✅ `newWriter`

- **File:** `src/compress/lzw/writer_test.go`
    - Ground Truth Functions (2):
        - `BenchmarkEncoder`
        - `TestWriterReset`
    - Predicted Functions (1):
        - ✅ `TestWriterReset`


### 📊 **Proposal #45973 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/http.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Close`
        - ❌ `Read`
        - ❌ `WriteTo`

- **File:** `src/net/http/serve_test.go`
    - Ground Truth Functions (2):
        - `TestQuerySemicolon`
        - `testQuerySemicolon`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (2):
        - `AllowQuerySemicolons`
        - `ServeHTTP`
    - Predicted Functions (3):
        - ✅ `AllowQuerySemicolons`
        - ❌ `HandlerFunc`
        - ✅ `ServeHTTP`


### 📊 **Proposal #43931 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/staticdata/embed.go`
    - Ground Truth Functions (5):
        - `WriteEmbed`
        - `embedFileLess`
        - `embedFileList`
        - `embedFileNameSplit`
        - `embedKind`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/instantiate.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Instantiate`
        - ❌ `implements`
        - ❌ `instance`
        - ❌ `mentions`
        - ❌ `validateTArgLen`
        - ❌ `verify`

- **File:** `src/cmd/compile/internal/types2/instantiate_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestImmutableSignatures`
        - ❌ `TestInstantiateEquality`
        - ❌ `TestInstantiateNonEquality`
        - ❌ `TestMethodInstantiation`

- **File:** `src/cmd/compile/internal/types2/subst.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `func_`
        - ❌ `subst`
        - ❌ `term`
        - ❌ `tuple`
        - ❌ `typ`
        - ❌ `typOrNil`
        - ❌ `var_`

- **File:** `src/cmd/compile/internal/types2/typeparam.go`
    - Ground Truth Functions (0):
    - Predicted Functions (11):
        - ❌ `Constraint`
        - ❌ `Index`
        - ❌ `NewTypeParam`
        - ❌ `Obj`
        - ❌ `SetConstraint`
        - ❌ `String`
        - ❌ `Underlying`
        - ❌ `cleanup`
        - ❌ `iface`
        - ❌ `is`
        - ❌ `typeset`

- **File:** `src/cmd/compile/internal/types2/typeset.go`
    - Ground Truth Functions (0):
    - Predicted Functions (14):
        - ❌ `IsAll`
        - ❌ `IsComparable`
        - ❌ `IsEmpty`
        - ❌ `IsMethodSet`
        - ❌ `LookupMethod`
        - ❌ `Method`
        - ❌ `NumMethods`
        - ❌ `computeInterfaceTypeSet`
        - ❌ `computeUnionTypeSet`
        - ❌ `hasTerms`
        - ❌ `intersectTermLists`
        - ❌ `is`
        - ❌ `subsetOf`
        - ❌ `typeset`

- **File:** `src/cmd/compile/internal/types2/typeset_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestInvalidTypeSet`
        - ❌ `TestTypeSetString`

- **File:** `src/cmd/compile/internal/types2/unify.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `newUnifier`
        - ❌ `nify`
        - ❌ `unify`

- **File:** `src/embed/internal/embedtest/embed_test.go`
    - Ground Truth Functions (3):
        - `TestDir`
        - `TestHidden`
        - `TestUninitialized`
    - Predicted Functions (0):

- **File:** `src/go/internal/gcimporter/gcimporter.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Import`

- **File:** `src/go/internal/gcimporter/gcimporter_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestImportTypeparamTests`

- **File:** `src/go/internal/gcimporter/testdata/generics.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ImplicitFunc`
        - ❌ `ToInt`

- **File:** `src/go/types/api.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Check`
        - ❌ `Error`
        - ❌ `ObjectOf`
        - ❌ `PkgNameOf`
        - ❌ `TypeOf`

- **File:** `src/go/types/api_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `TestGenericMethodInfo`
        - ❌ `TestInstanceIdentity`
        - ❌ `TestInstantiate`
        - ❌ `TestInstantiateConcurrent`
        - ❌ `TestInstantiateErrors`
        - ❌ `TestInstantiatedObjects`
        - ❌ `TestLookupFieldOrMethod_RecursiveGeneric`
        - ❌ `originObject`

- **File:** `src/go/types/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `ExampleInfo`
        - ❌ `ExampleMethodSet`
        - ❌ `ExampleScope`

- **File:** `src/go/types/infer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `coreTerm`
        - ❌ `infer`
        - ❌ `isParameterized`
        - ❌ `renameTParams`

- **File:** `src/go/types/instantiate.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Instantiate`
        - ❌ `implements`
        - ❌ `instance`
        - ❌ `mentions`
        - ❌ `validateTArgLen`
        - ❌ `verify`

- **File:** `src/go/types/instantiate_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestImmutableSignatures`
        - ❌ `TestInstantiateEquality`
        - ❌ `TestInstantiateNonEquality`
        - ❌ `TestMethodInstantiation`

- **File:** `src/go/types/stdlib_test.go`
    - Ground Truth Functions (1):
        - `TestStdTest`
    - Predicted Functions (0):

- **File:** `src/go/types/subst.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `func_`
        - ❌ `subst`
        - ❌ `term`
        - ❌ `tuple`
        - ❌ `typ`
        - ❌ `typOrNil`
        - ❌ `var_`

- **File:** `src/go/types/typelists.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `At`
        - ❌ `Len`
        - ❌ `bindTParams`
        - ❌ `list`
        - ❌ `newTypeList`

- **File:** `src/go/types/typeparam.go`
    - Ground Truth Functions (0):
    - Predicted Functions (11):
        - ❌ `Constraint`
        - ❌ `Index`
        - ❌ `NewTypeParam`
        - ❌ `Obj`
        - ❌ `SetConstraint`
        - ❌ `String`
        - ❌ `Underlying`
        - ❌ `cleanup`
        - ❌ `iface`
        - ❌ `is`
        - ❌ `typeset`

- **File:** `src/go/types/typeset.go`
    - Ground Truth Functions (0):
    - Predicted Functions (14):
        - ❌ `IsAll`
        - ❌ `IsComparable`
        - ❌ `IsEmpty`
        - ❌ `IsMethodSet`
        - ❌ `LookupMethod`
        - ❌ `Method`
        - ❌ `NumMethods`
        - ❌ `computeInterfaceTypeSet`
        - ❌ `computeUnionTypeSet`
        - ❌ `hasTerms`
        - ❌ `intersectTermLists`
        - ❌ `is`
        - ❌ `subsetOf`
        - ❌ `typeset`

- **File:** `src/go/types/typeset_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestInvalidTypeSet`
        - ❌ `TestTypeSetString`

- **File:** `src/go/types/typeterm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `String`
        - ❌ `disjoint`
        - ❌ `equal`
        - ❌ `includes`
        - ❌ `intersect`
        - ❌ `subsetOf`
        - ❌ `union`

- **File:** `src/go/types/typeterm_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `TestTermDisjoint`
        - ❌ `TestTermEqual`
        - ❌ `TestTermIncludes`
        - ❌ `TestTermIntersection`
        - ❌ `TestTermString`
        - ❌ `TestTermSubsetOf`
        - ❌ `TestTermUnion`

- **File:** `src/go/types/union.go`
    - Ground Truth Functions (0):
    - Predicted Functions (12):
        - ❌ `Len`
        - ❌ `NewTerm`
        - ❌ `NewUnion`
        - ❌ `String`
        - ❌ `Term`
        - ❌ `Tilde`
        - ❌ `Type`
        - ❌ `Underlying`
        - ❌ `flattenUnion`
        - ❌ `overlappingTerm`
        - ❌ `parseTilde`
        - ❌ `parseUnion`


### 📊 **Proposal #46771 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 100.0% | 75.0% | 3/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/mime/multipart/writer.go`
    - Ground Truth Functions (2):
        - `CreateFormFile`
        - `FileContentDisposition`
    - Predicted Functions (4):
        - ✅ `CreateFormFile`
        - ❌ `CreateFormFileWithContentType`
        - ✅ `FileContentDisposition`
        - ❌ `escapeQuotes`

- **File:** `src/mime/multipart/writer_test.go`
    - Ground Truth Functions (1):
        - `TestFileContentDisposition`
    - Predicted Functions (1):
        - ✅ `TestFileContentDisposition`


### 📊 **Proposal #45033 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 66.7% | 52.2% | 6/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/fmt/scan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `quotedString`

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `funcStr`
        - ❌ `stringFor`

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
    - Predicted Functions (4):
        - ✅ `QuotedPrefix`
        - ✅ `Unquote`
        - ❌ `UnquoteChar`
        - ✅ `unquote`

- **File:** `src/strconv/quote_test.go`
    - Ground Truth Functions (3):
        - `TestUnquote`
        - `TestUnquoteInvalidUTF8`
        - `testUnquote`
    - Predicted Functions (5):
        - ❌ `BenchmarkUnquoteEasy`
        - ❌ `BenchmarkUnquoteHard`
        - ✅ `TestUnquote`
        - ✅ `TestUnquoteInvalidUTF8`
        - ✅ `testUnquote`

- **File:** `src/text/template/parse/lex.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `lexQuote`
        - ❌ `lexRawQuote`


### 📊 **Proposal #40337 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.0% | 66.7% | 14.3% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/dsa/dsa.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `GenerateKey`
        - ❌ `GenerateParameters`
        - ❌ `Sign`
        - ❌ `Verify`

- **File:** `src/crypto/dsa/dsa_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `TestParameterGeneration`
        - ❌ `TestSignAndVerify`
        - ❌ `TestSignAndVerifyWithBadPublicKey`
        - ❌ `TestSigningWithDegenerateKeys`
        - ❌ `testParameterGeneration`
        - ❌ `testSignAndVerify`

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (2):
        - `CheckCRLSignature`
        - `checkSignature`
    - Predicted Functions (12):
        - ❌ `CheckSignature`
        - ❌ `CheckSignatureFrom`
        - ❌ `CreateCertificate`
        - ❌ `CreateRevocationList`
        - ❌ `MarshalPKIXPublicKey`
        - ❌ `ParseCertificateRequest`
        - ❌ `ParsePKIXPublicKey`
        - ✅ `checkSignature`
        - ❌ `getPublicKeyAlgorithmFromOID`
        - ❌ `marshalPublicKey`
        - ❌ `parseCertificateRequest`
        - ❌ `signingParamsForKey`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (1):
        - `TestVerifyCertificateWithDSASignature`
    - Predicted Functions (3):
        - ❌ `TestParseCertificateWithDSASignatureAlgorithm`
        - ❌ `TestParseCertificateWithDsaPublicKey`
        - ✅ `TestVerifyCertificateWithDSASignature`


### 📊 **Proposal #47651 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 0.8% | 1.6% | 1/119 |

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
    - Predicted Functions (0):

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
    - Predicted Functions (4):
        - ❌ `Kind`
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
    - Predicted Functions (4):
        - ❌ `Kind`
        - ✅ `Pointer`
        - ❌ `PointerTo`
        - ❌ `PtrTo`

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
        - ❌ `Seq`
        - ❌ `Seq2`

- **File:** `src/reflect/iter_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestValueSeq`
        - ❌ `TestValueSeq2`

- **File:** `src/reflect/map_noswiss.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Key`
        - ❌ `Next`
        - ❌ `Reset`
        - ❌ `SetIterKey`
        - ❌ `SetIterValue`
        - ❌ `Value`

- **File:** `src/reflect/map_noswiss_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `testGCBitsMap`

- **File:** `src/reflect/map_swiss.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Key`
        - ❌ `Next`
        - ❌ `SetIterKey`
        - ❌ `SetIterValue`
        - ❌ `Value`

- **File:** `src/reflect/map_swiss_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestGroupSizeZero`
        - ❌ `testGCBitsMap`

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `MapIter.SetKey`
        - ❌ `MapIter.SetValue`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `mapaccess`
        - ❌ `mapaccess_faststr`
        - ❌ `mapassign`
        - ❌ `mapassign_faststr`
        - ❌ `mapclear`
        - ❌ `mapdelete`
        - ❌ `mapdelete_faststr`
        - ❌ `maplen`


### 📊 **Proposal #50860 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 32.6% | 54.5% | 40.8% | 42/77 |

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
    - Predicted Functions (58):
        - ❌ `TestAddInt32`
        - ✅ `TestAddInt32Method`
        - ✅ `TestAddInt64`
        - ✅ `TestAddInt64Method`
        - ✅ `TestAddUint32`
        - ✅ `TestAddUint32Method`
        - ✅ `TestAddUint64`
        - ✅ `TestAddUint64Method`
        - ❌ `TestAddUintptr`
        - ✅ `TestAddUintptrMethod`
        - ✅ `TestCompareAndSwapInt32`
        - ✅ `TestCompareAndSwapInt32Method`
        - ✅ `TestCompareAndSwapInt64`
        - ✅ `TestCompareAndSwapInt64Method`
        - ❌ `TestCompareAndSwapPointer`
        - ✅ `TestCompareAndSwapPointerMethod`
        - ❌ `TestCompareAndSwapUint32`
        - ✅ `TestCompareAndSwapUint32Method`
        - ❌ `TestCompareAndSwapUint64`
        - ✅ `TestCompareAndSwapUint64Method`
        - ❌ `TestCompareAndSwapUintptr`
        - ✅ `TestCompareAndSwapUintptrMethod`
        - ❌ `TestLoadInt32`
        - ✅ `TestLoadInt32Method`
        - ✅ `TestLoadInt64`
        - ✅ `TestLoadInt64Method`
        - ✅ `TestLoadPointer`
        - ✅ `TestLoadPointerMethod`
        - ❌ `TestLoadUint32`
        - ✅ `TestLoadUint32Method`
        - ✅ `TestLoadUint64`
        - ✅ `TestLoadUint64Method`
        - ❌ `TestLoadUintptr`
        - ✅ `TestLoadUintptrMethod`
        - ❌ `TestStoreInt32`
        - ✅ `TestStoreInt32Method`
        - ✅ `TestStoreInt64`
        - ✅ `TestStoreInt64Method`
        - ❌ `TestStorePointer`
        - ✅ `TestStorePointerMethod`
        - ❌ `TestStoreUint32`
        - ✅ `TestStoreUint32Method`
        - ✅ `TestStoreUint64`
        - ✅ `TestStoreUint64Method`
        - ❌ `TestStoreUintptr`
        - ✅ `TestStoreUintptrMethod`
        - ❌ `TestSwapInt32`
        - ✅ `TestSwapInt32Method`
        - ✅ `TestSwapInt64`
        - ✅ `TestSwapInt64Method`
        - ❌ `TestSwapPointer`
        - ✅ `TestSwapPointerMethod`
        - ❌ `TestSwapUint32`
        - ✅ `TestSwapUint32Method`
        - ✅ `TestSwapUint64`
        - ✅ `TestSwapUint64Method`
        - ❌ `TestSwapUintptr`
        - ✅ `TestSwapUintptrMethod`

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

- **File:** `src/sync/atomic/doc_32.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `AddInt64`
        - ❌ `AddUint64`
        - ❌ `CompareAndSwapInt64`
        - ❌ `CompareAndSwapUint64`
        - ❌ `LoadInt64`
        - ❌ `LoadUint64`
        - ❌ `StoreInt64`
        - ❌ `StoreUint64`
        - ❌ `SwapInt64`
        - ❌ `SwapUint64`

- **File:** `src/sync/atomic/doc_64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `AddInt64`
        - ❌ `AddUint64`
        - ❌ `CompareAndSwapInt64`
        - ❌ `CompareAndSwapUint64`
        - ❌ `LoadInt64`
        - ❌ `LoadUint64`
        - ❌ `StoreInt64`
        - ❌ `StoreUint64`
        - ❌ `SwapInt64`
        - ❌ `SwapUint64`

- **File:** `src/sync/atomic/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `ExampleValue_config`
        - ❌ `ExampleValue_readMostly`
        - ❌ `loadConfig`
        - ❌ `requests`

- **File:** `src/sync/atomic/type.go`
    - Ground Truth Functions (2):
        - `CompareAndSwap`
        - `b32`
    - Predicted Functions (7):
        - ❌ `Add`
        - ❌ `And`
        - ✅ `CompareAndSwap`
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
    - Predicted Functions (8):
        - ❌ `TestValue`
        - ❌ `TestValueCompareAndSwapConcurrent`
        - ❌ `TestValueConcurrent`
        - ❌ `TestValueLarge`
        - ❌ `TestValuePanic`
        - ❌ `TestValueSwapConcurrent`
        - ❌ `TestValue_CompareAndSwap`
        - ❌ `TestValue_Swap`

- **File:** `test/atomicload.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `f`
        - ❌ `main`

- **File:** `test/escape_runtime_atomic.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Casp1`
        - ❌ `Loadp`
        - ❌ `Storep`

- **File:** `test/escape_sync_atomic.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `CompareAndSwapPointer`
        - ❌ `LoadPointer`
        - ❌ `StorePointer`
        - ❌ `SwapPointer`


### 📊 **Proposal #51972 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 42.9% | 60.0% | 6/14 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/sync/export_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

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
    - Predicted Functions (5):
        - ✅ `CompareAndDelete`
        - ✅ `CompareAndSwap`
        - ✅ `Swap`
        - ✅ `tryCompareAndSwap`
        - ✅ `trySwap`

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


### 📊 **Proposal #48052 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/debug/plan9obj/file.go`
    - Ground Truth Functions (1):
        - `Symbols`
    - Predicted Functions (2):
        - ❌ `Section`
        - ✅ `Symbols`

- **File:** `src/debug/plan9obj/plan9obj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `DynamicSymbols`
        - ❌ `Symbols`


### 📊 **Proposal #50436 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 56.2% | 39.1% | 46.2% | 9/23 |

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
    - Predicted Functions (8):
        - ✅ `CombinedOutput`
        - ✅ `CommandContext`
        - ❌ `Output`
        - ❌ `Run`
        - ✅ `Start`
        - ✅ `Wait`
        - ✅ `awaitGoroutines`
        - ✅ `watchCtx`

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (6):
        - `Read`
        - `TestCancelErrors`
        - `TestWaitInterrupt`
        - `cmdHang`
        - `newTickReader`
        - `startHang`
    - Predicted Functions (6):
        - ❌ `TestContext`
        - ❌ `TestContextCancel`
        - ✅ `TestWaitInterrupt`
        - ✅ `cmdHang`
        - ❌ `helperCommandContext`
        - ✅ `startHang`

- **File:** `src/os/exec/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `skipStdinCopyError`

- **File:** `src/os/exec/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `skipStdinCopyError`


### 📊 **Proposal #45899 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 7/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/io/io.go`
    - Ground Truth Functions (4):
        - `NewOffsetWriter`
        - `Seek`
        - `Write`
        - `WriteAt`
    - Predicted Functions (10):
        - ❌ `Copy`
        - ❌ `CopyBuffer`
        - ✅ `NewOffsetWriter`
        - ❌ `NewSectionReader`
        - ❌ `Read`
        - ❌ `ReadAt`
        - ✅ `Seek`
        - ❌ `Size`
        - ✅ `Write`
        - ✅ `WriteAt`

- **File:** `src/io/io_test.go`
    - Ground Truth Functions (3):
        - `TestOffsetWriter_Seek`
        - `TestOffsetWriter_Write`
        - `TestOffsetWriter_WriteAt`
    - Predicted Functions (4):
        - ✅ `TestOffsetWriter_Seek`
        - ✅ `TestOffsetWriter_Write`
        - ✅ `TestOffsetWriter_WriteAt`
        - ❌ `TestWriteAt_PositionPriorToBase`


### 📊 **Proposal #46259 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 37.5% | 50.0% | 42.9% | 3/6 |

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
    - Predicted Functions (1):
        - ✅ `forkAndExecInChild`

- **File:** `src/syscall/exec_freebsd_test.go`
    - Ground Truth Functions (2):
        - `TestJailAttach`
        - `prepareJail`
    - Predicted Functions (2):
        - ✅ `TestJailAttach`
        - ✅ `prepareJail`

- **File:** `src/syscall/syscall_freebsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `RawSyscall`
        - ❌ `RawSyscall6`
        - ❌ `Syscall`
        - ❌ `Syscall6`


### 📊 **Proposal #48866 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/mime/mediatype.go`
    - Ground Truth Functions (1):
        - `ParseMediaType`
    - Predicted Functions (2):
        - ✅ `ParseMediaType`
        - ❌ `consumeMediaParam`

- **File:** `src/mime/mediatype_test.go`
    - Ground Truth Functions (1):
        - `TestParseMediaType`
    - Predicted Functions (3):
        - ❌ `ParseMediaType`
        - ✅ `TestParseMediaType`
        - ❌ `TestParseMediaTypeBogus`


### 📊 **Proposal #42782 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.0% | 100.0% | 46.2% | 3/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Field`
        - ❌ `FieldByIndex`
        - ❌ `FieldByName`
        - ❌ `FieldByNameFunc`
        - ❌ `IsExported`
        - ❌ `NumField`

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


### 📊 **Proposal #49471 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/debug.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `GOTRACEBACK`

- **File:** `src/runtime/os_windows.go`
    - Ground Truth Functions (1):
        - `loadOptionalSyscalls`
    - Predicted Functions (4):
        - ❌ `exit`
        - ❌ `mdestroy`
        - ❌ `minit`
        - ❌ `unminit`

- **File:** `src/runtime/panic.go`
    - Ground Truth Functions (2):
        - `fatalpanic`
        - `fatalthrow`
    - Predicted Functions (0):

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

- **File:** `src/syscall/dll_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `LoadDLL`
        - ❌ `MustLoadDLL`
        - ❌ `NewLazyDLL`
        - ❌ `Syscall`
        - ❌ `Syscall12`
        - ❌ `Syscall15`
        - ❌ `Syscall18`
        - ❌ `Syscall6`
        - ❌ `Syscall9`
        - ❌ `SyscallN`

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `CreateFile`
        - ❌ `LoadCreateSymbolicLink`

- **File:** `src/syscall/zsyscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `MiniDumpWriteDump`


### 📊 **Proposal #48157 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/11 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/test/test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `runTest`
        - ❌ `testBinaryName`

- **File:** `src/cmd/go/internal/test/testflag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `testFlags`

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

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Deadline`
        - ❌ `SetTimeout`
        - ❌ `startAlarm`
        - ❌ `stopAlarm`

- **File:** `src/testing/testing_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestContext`
        - ❌ `TestMain`
        - ❌ `TestRunningTests`
        - ❌ `TestRunningTestsInCleanup`
        - ❌ `runTest`


### 📊 **Proposal #52221 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.4% | 29.8% | 35.0% | 14/47 |

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
    - Predicted Functions (14):
        - ❌ `Bytes`
        - ❌ `Curve`
        - ❌ `ECDH`
        - ❌ `Equal`
        - ❌ `GenerateKey`
        - ❌ `NewPrivateKey`
        - ❌ `NewPublicKey`
        - ❌ `Public`
        - ❌ `PublicKey`
        - ✅ `TestECDH`
        - ✅ `TestGenerateKey`
        - ❌ `TestMismatchedCurves`
        - ❌ `TestNewPrivateKey`
        - ❌ `TestNewPublicKey`

- **File:** `src/crypto/ecdh/nist.go`
    - Ground Truth Functions (4):
        - `GenerateKey`
        - `NewPrivateKey`
        - `NewPublicKey`
        - `String`
    - Predicted Functions (8):
        - ✅ `GenerateKey`
        - ✅ `NewPrivateKey`
        - ✅ `NewPublicKey`
        - ❌ `P256`
        - ❌ `P384`
        - ❌ `P521`
        - ✅ `String`
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


### 📊 **Proposal #37974 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/doc/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `do`
        - ❌ `objectPath`
        - ❌ `runCmd`

- **File:** `src/go/ast/ast.go`
    - Ground Truth Functions (2):
        - `Text`
        - `isDirective`
    - Predicted Functions (0):

- **File:** `src/go/ast/ast_test.go`
    - Ground Truth Functions (1):
        - `TestIsDirective`
    - Predicted Functions (0):

- **File:** `src/go/doc/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Text`

- **File:** `src/go/doc/doc_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Test`
        - ❌ `TestFuncs`

- **File:** `test/directive.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `f`
        - ❌ `f1`
        - ❌ `f2`

- **File:** `test/directive2.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `f`
        - ❌ `g`


### 📊 **Proposal #41048 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 50.0% | 30.8% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/transport.go`
    - Ground Truth Functions (2):
        - `Clone`
        - `dialConn`
    - Predicted Functions (5):
        - ❌ `connectMethodForRequest`
        - ✅ `dialConn`
        - ❌ `getConn`
        - ❌ `proxyAuth`
        - ❌ `roundTrip`

- **File:** `src/net/http/transport_test.go`
    - Ground Truth Functions (2):
        - `TestTransportClone`
        - `TestTransportProxyGetConnectHeader`
    - Predicted Functions (4):
        - ❌ `TestTransportProxyConnectHeader`
        - ✅ `TestTransportProxyGetConnectHeader`
        - ❌ `testTransportProxyConnectHeader`
        - ❌ `testTransportProxyGetConnectHeader`


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
    - Predicted Functions (2):
        - ❌ `FuncType`
        - ❌ `IndexListExpr`

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
    - Predicted Functions (4):
        - ❌ `IsIdentifier`
        - ❌ `IsKeyword`
        - ❌ `Lookup`
        - ❌ `String`

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


### 📊 **Proposal #47342 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 36.0% | 85.7% | 50.7% | 18/21 |

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
    - Predicted Functions (18):
        - ❌ `BlockSize`
        - ✅ `Bytes`
        - ❌ `Clone`
        - ❌ `Comparable`
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
        - ✅ `flush`
        - ❌ `initSeed`

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
    - Predicted Functions (2):
        - ✅ `rthash`
        - ✅ `rthashString`

- **File:** `src/hash/maphash/maphash_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (18):
        - ❌ `BenchmarkComparable`
        - ❌ `BenchmarkHash`
        - ❌ `TestComparable`
        - ❌ `TestComparableAllocations`
        - ❌ `TestComparableShouldPanic`
        - ❌ `TestHashBytesVsString`
        - ❌ `TestHashGrouping`
        - ❌ `TestHashHighBytes`
        - ❌ `TestHashInterface`
        - ❌ `TestRepeat`
        - ❌ `TestSeedFromFlush`
        - ❌ `TestSeedFromReset`
        - ❌ `TestSeedFromSeed`
        - ❌ `TestSeedFromSum64`
        - ❌ `TestSeededHash`
        - ❌ `TestUnseededHash`
        - ❌ `TestWriteComparable`
        - ❌ `TestWriteComparableNoncommute`


### 📊 **Proposal #43947 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.8% | 18.8% | 18.8% | 3/16 |

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
    - Predicted Functions (3):
        - ✅ `Command`
        - ❌ `CommandContext`
        - ❌ `LookPath`

- **File:** `src/os/exec/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `skipStdinCopyError`

- **File:** `src/os/exec/lp_plan9.go`
    - Ground Truth Functions (1):
        - `LookPath`
    - Predicted Functions (0):

- **File:** `src/os/exec/lp_unix.go`
    - Ground Truth Functions (1):
        - `LookPath`
    - Predicted Functions (2):
        - ✅ `LookPath`
        - ❌ `findExecutable`

- **File:** `src/os/exec/lp_windows.go`
    - Ground Truth Functions (1):
        - `LookPath`
    - Predicted Functions (2):
        - ✅ `LookPath`
        - ❌ `lookPath`

- **File:** `src/os/exec/lp_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestLookPathWindows`

- **File:** `src/syscall/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `FullPath`
        - ❌ `StartProcess`

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `ConnectEx`
        - ❌ `CreateFile`
        - ❌ `LoadConnectEx`
        - ❌ `LoadGetAddrInfo`
        - ❌ `connectEx`


### 📊 **Proposal #46742 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.7% | 10.0% | 8.7% | 1/10 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/test/testdata/unsafe_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestUnsafe`

- **File:** `src/cmd/compile/internal/typecheck/builtin.go`
    - Ground Truth Functions (1):
        - `runtimeTypes`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/typecheck/func.go`
    - Ground Truth Functions (1):
        - `tcUnsafeSlice`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/types2/slice.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `NewSlice`

- **File:** `src/cmd/compile/internal/walk/builtin.go`
    - Ground Truth Functions (1):
        - `walkUnsafeSlice`
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

- **File:** `src/runtime/slice.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `makeslice`
        - ❌ `makeslice64`

- **File:** `src/runtime/testdata/testprog/checkptr.go`
    - Ground Truth Functions (3):
        - `CheckPtrSliceFail`
        - `CheckPtrSliceOK`
        - `init`
    - Predicted Functions (0):

- **File:** `src/runtime/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `panicunsafeslicenilptr`
        - ❌ `unsafeslice`
        - ❌ `unsafeslice64`
        - ❌ `unsafeslicecheckptr`

- **File:** `src/unsafe/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Slice`

- **File:** `test/unsafe_slice_data.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`

- **File:** `test/unsafe_string.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/unsafe_string_data.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/unsafebuiltins.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (3):
        - ❌ `assert`
        - ✅ `main`
        - ❌ `mustPanic`


### 📊 **Proposal #47005 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/url/url.go`
    - Ground Truth Functions (1):
        - `JoinPath`
    - Predicted Functions (4):
        - ✅ `JoinPath`
        - ❌ `Parse`
        - ❌ `ResolveReference`
        - ❌ `String`

- **File:** `src/net/url/url_test.go`
    - Ground Truth Functions (1):
        - `TestJoinPath`
    - Predicted Functions (4):
        - ❌ `JoinPath`
        - ❌ `ResolveReference`
        - ✅ `TestJoinPath`
        - ❌ `TestResolveReference`


### 📊 **Proposal #48257 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/workcmd/use.go`
    - Ground Truth Functions (2):
        - `init`
        - `runUse`
    - Predicted Functions (2):
        - ✅ `runUse`
        - ❌ `workUse`


### 📊 **Proposal #45628 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 66.7% | 36.4% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/xml/read.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Decode`
        - ❌ `DecodeElement`
        - ❌ `Skip`

- **File:** `src/encoding/xml/read_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestInputLineNum`

- **File:** `src/encoding/xml/xml.go`
    - Ground Truth Functions (2):
        - `InputPos`
        - `getc`
    - Predicted Functions (4):
        - ❌ `InputOffset`
        - ✅ `InputPos`
        - ✅ `getc`
        - ❌ `ungetc`

- **File:** `src/encoding/xml/xml_test.go`
    - Ground Truth Functions (1):
        - `TestInputLinePos`
    - Predicted Functions (0):


### 📊 **Proposal #43401 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 100.0% | 60.0% | 3/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/csv/reader.go`
    - Ground Truth Functions (2):
        - `InputOffset`
        - `readLine`
    - Predicted Functions (4):
        - ✅ `InputOffset`
        - ❌ `Read`
        - ✅ `readLine`
        - ❌ `readRecord`

- **File:** `src/encoding/csv/reader_test.go`
    - Ground Truth Functions (1):
        - `TestRead`
    - Predicted Functions (3):
        - ✅ `TestRead`
        - ❌ `errorWithPosition`
        - ❌ `makePositions`


### 📊 **Proposal #39567 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 33.3% | 22.2% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/serve_test.go`
    - Ground Truth Functions (2):
        - `TestMaxBytesHandler`
        - `testMaxBytesHandler`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (1):
        - `MaxBytesHandler`
    - Predicted Functions (5):
        - ✅ `MaxBytesHandler`
        - ❌ `Read`
        - ❌ `hitReadLimit`
        - ❌ `requestTooLarge`
        - ❌ `setReadLimit`

- **File:** `src/net/http/server_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ServeHTTP`


### 📊 **Proposal #53003 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/builtin/builtin.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `cap`
        - ❌ `len`

- **File:** `src/cmd/compile/internal/types2/builtins.go`
    - Ground Truth Functions (1):
        - `builtin`
    - Predicted Functions (0):

- **File:** `src/go/types/builtins.go`
    - Ground Truth Functions (1):
        - `builtin`
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `ArrayOf`
        - ❌ `SliceOf`
        - ❌ `String`
        - ❌ `TypeFor`
        - ❌ `TypeOf`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `Bytes`
        - ❌ `Pointer`
        - ❌ `SetBytes`
        - ❌ `SetString`
        - ❌ `String`
        - ❌ `UnsafeAddr`
        - ❌ `UnsafePointer`
        - ❌ `cvtBytesString`
        - ❌ `cvtStringBytes`

- **File:** `src/runtime/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `reflect_unsafeslice`
        - ❌ `unsafeslice`
        - ❌ `unsafeslice64`
        - ❌ `unsafeslicecheckptr`
        - ❌ `unsafestring`
        - ❌ `unsafestring64`
        - ❌ `unsafestringcheckptr`

- **File:** `src/unsafe/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Slice`
        - ❌ `SliceData`
        - ❌ `String`
        - ❌ `StringData`

- **File:** `test/unsafe_slice_data.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/unsafe_string.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/unsafe_string_data.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`


### 📊 **Proposal #41260 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.0% | 100.0% | 46.2% | 3/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/testing/testing.go`
    - Ground Truth Functions (2):
        - `Parallel`
        - `Setenv`
    - Predicted Functions (4):
        - ❌ `Cleanup`
        - ✅ `Parallel`
        - ✅ `Setenv`
        - ❌ `checkParallel`

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


### 📊 **Proposal #51414 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/time/time.go`
    - Ground Truth Functions (1):
        - `Abs`
    - Predicted Functions (2):
        - ✅ `Abs`
        - ❌ `Sub`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (1):
        - `TestDurationAbs`
    - Predicted Functions (2):
        - ✅ `TestDurationAbs`
        - ❌ `abs`


### 📊 **Proposal #40481 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 44.4% | 23.5% | 30.8% | 4/17 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/builtin/builtin.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

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

- **File:** `src/cmd/compile/internal/test/testdata/unsafe_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestUnsafe`

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

- **File:** `src/go/types/builtins.go`
    - Ground Truth Functions (1):
        - `builtin`
    - Predicted Functions (0):

- **File:** `src/runtime/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `reflect_unsafeslice`
        - ❌ `unsafeslice`
        - ❌ `unsafeslice64`
        - ❌ `unsafeslicecheckptr`

- **File:** `src/unsafe/unsafe.go`
    - Ground Truth Functions (2):
        - `Add`
        - `Slice`
    - Predicted Functions (1):
        - ✅ `Add`

- **File:** `test/unsafe_slice_data.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/unsafe_string.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/unsafe_string_data.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/unsafebuiltins.go`
    - Ground Truth Functions (3):
        - `assert`
        - `main`
        - `mustPanic`
    - Predicted Functions (3):
        - ✅ `assert`
        - ✅ `main`
        - ✅ `mustPanic`


### 📊 **Proposal #47209 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 66.7% | 44.4% | 4/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/fsys/fsys_test.go`
    - Ground Truth Functions (1):
        - `TestWalkSkipAll`
    - Predicted Functions (0):

- **File:** `src/io/fs/walk.go`
    - Ground Truth Functions (1):
        - `WalkDir`
    - Predicted Functions (0):

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

- **File:** `src/path/filepath/path_plan9.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/path/filepath/path_test.go`
    - Ground Truth Functions (1):
        - `TestWalkSkipAllOnFile`
    - Predicted Functions (5):
        - ❌ `TestWalk`
        - ❌ `TestWalkDir`
        - ✅ `TestWalkSkipAllOnFile`
        - ❌ `TestWalkSkipDirOnFile`
        - ❌ `testWalk`

- **File:** `src/path/filepath/path_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/path/filepath/path_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/path/filepath/symlink.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `walkSymlinks`

- **File:** `src/path/filepath/symlink_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `evalSymlinks`

- **File:** `src/path/filepath/symlink_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `evalSymlinks`


### 📊 **Proposal #40276 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 4.2% | 33.3% | 7.4% | 2/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/load/pkg.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `DefaultExecName`
        - ❌ `EnsureImport`
        - ❌ `InstallTargetDir`
        - ❌ `LoadPackage`
        - ❌ `PackagesAndErrorsOutsideModule`
        - ❌ `ResolveImportPath`
        - ❌ `loadImport`
        - ❌ `loadPackageData`
        - ❌ `resolveImportPath`

- **File:** `src/cmd/go/internal/modget/get.go`
    - Ground Truth Functions (0):
    - Predicted Functions (11):
        - ❌ `newResolver`
        - ❌ `parseArgs`
        - ❌ `performToolQueries`
        - ❌ `performWorkQueries`
        - ❌ `queryModule`
        - ❌ `queryPackages`
        - ❌ `queryPattern`
        - ❌ `resolve`
        - ❌ `resolveQueries`
        - ❌ `runGet`
        - ❌ `updateTools`

- **File:** `src/cmd/go/internal/modload/init.go`
    - Ground Truth Functions (4):
        - `BinDir`
        - `Enabled`
        - `Init`
        - `WillBeEnabled`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/query.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `Query`
        - ❌ `QueryPackages`
        - ❌ `QueryPattern`
        - ❌ `lookupRepo`
        - ❌ `modulePrefixesExcludingTarget`
        - ❌ `queryPrefixModules`
        - ❌ `queryProxy`
        - ❌ `versionHasGoMod`

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (2):
        - `installOutsideModule`
        - `runInstall`
    - Predicted Functions (3):
        - ❌ `InstallPackages`
        - ✅ `installOutsideModule`
        - ✅ `runInstall`

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `BuildInstallFunc`
        - ❌ `ccompile`
        - ❌ `gccld`
        - ❌ `installHeader`
        - ❌ `link`

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `gc`
        - ❌ `ld`
        - ❌ `pack`

- **File:** `src/cmd/go/internal/work/gccgo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `ld`
        - ❌ `ldShared`
        - ❌ `link`
        - ❌ `linker`

- **File:** `src/cmd/go/internal/work/security.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `checkCompilerFlags`
        - ❌ `checkCompilerFlagsForInternalLink`
        - ❌ `checkFlags`
        - ❌ `checkLinkerFlags`

- **File:** `src/cmd/go/internal/workcmd/work.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `runInstall`


### 📊 **Proposal #45453 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.7% | 3.3% | 4.2% | 2/61 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/amd64/galign.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Init`

- **File:** `src/cmd/compile/internal/amd64/ggen.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ginsnop`
        - ❌ `zerorange`

- **File:** `src/cmd/compile/internal/amd64/ssa.go`
    - Ground Truth Functions (1):
        - `ssaGenValue`
    - Predicted Functions (2):
        - ❌ `ssaGenBlock`
        - ✅ `ssaGenValue`

- **File:** `src/cmd/compile/internal/amd64/versions_test.go`
    - Ground Truth Functions (2):
        - `TestGoAMD64v1`
        - `setOf`
    - Predicted Functions (9):
        - ❌ `TestAndNot`
        - ❌ `TestBLSI`
        - ❌ `TestBLSMSK`
        - ❌ `TestBLSR`
        - ❌ `TestFMA`
        - ✅ `TestGoAMD64v1`
        - ❌ `TestPopCnt`
        - ❌ `TestRound`
        - ❌ `TestTrailingZeros`

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

- **File:** `src/cmd/internal/objabi/head.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Set`
        - ❌ `String`

- **File:** `src/cmd/internal/sys/arch.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `InFamily`

- **File:** `src/cmd/link/internal/amd64/asm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `archreloc`
        - ❌ `archrelocvariant`
        - ❌ `gentext`

- **File:** `src/cmd/link/internal/amd64/l.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/amd64/obj.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Init`
        - ❌ `archinit`

- **File:** `src/internal/buildcfg/cfg.go`
    - Ground Truth Functions (1):
        - `goamd64`
    - Predicted Functions (0):

- **File:** `src/internal/buildcfg/cfg_test.go`
    - Ground Truth Functions (1):
        - `TestConfigFlags`
    - Predicted Functions (0):

- **File:** `src/internal/cpu/cpu.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Initialize`
        - ❌ `processOptions`

- **File:** `src/internal/cpu/cpu_x86.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `doinit`
        - ❌ `getGOAMD64level`

- **File:** `src/internal/cpu/cpu_x86_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `TestDisableSSE3`
        - ❌ `TestSSE3DebugOption`
        - ❌ `TestX86ifAVX2hasAVX`
        - ❌ `TestX86ifAVX512BWhasAVX512F`
        - ❌ `TestX86ifAVX512FhasAVX2`
        - ❌ `TestX86ifAVX512VLhasAVX512F`

- **File:** `src/vendor/golang.org/x/sys/cpu/cpu_x86.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `archInit`
        - ❌ `initOptions`
        - ❌ `isSet`

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


### 📊 **Proposal #48409 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 51.0% | 22.2% | 31.0% | 26/117 |

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
        - ❌ `FreeOSMemory`
        - ❌ `SetGCPercent`

- **File:** `src/runtime/debug/stubs.go`
    - Ground Truth Functions (1):
        - `setMemoryLimit`
    - Predicted Functions (0):

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
    - Ground Truth Functions (5):
        - `gcMarkDone`
        - `gcMarkTermination`
        - `gcStart`
        - `gcinit`
        - `test`
    - Predicted Functions (5):
        - ❌ `gcBgMarkWorker`
        - ❌ `gcMark`
        - ✅ `gcMarkTermination`
        - ✅ `gcStart`
        - ❌ `gcSweep`

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
    - Predicted Functions (6):
        - ✅ `finishGCTransition`
        - ✅ `limiting`
        - ✅ `resetCapacity`
        - ✅ `startGCTransition`
        - ✅ `update`
        - ✅ `updateLocked`

- **File:** `src/runtime/mgclimit_test.go`
    - Ground Truth Functions (1):
        - `TestGCCPULimiter`
    - Predicted Functions (1):
        - ✅ `TestGCCPULimiter`

- **File:** `src/runtime/mgcmark.go`
    - Ground Truth Functions (2):
        - `gcAssistAlloc`
        - `gcAssistAlloc1`
    - Predicted Functions (8):
        - ✅ `gcAssistAlloc`
        - ✅ `gcAssistAlloc1`
        - ❌ `gcDrain`
        - ❌ `gcDrainMarkWorkerDedicated`
        - ❌ `gcDrainMarkWorkerFractional`
        - ❌ `gcDrainMarkWorkerIdle`
        - ❌ `gcDrainN`
        - ❌ `gcFlushBgCredit`

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
    - Predicted Functions (5):
        - ✅ `heapGoal`
        - ✅ `heapGoalInternal`
        - ✅ `memoryLimitHeapGoal`
        - ✅ `setGCPercent`
        - ✅ `setMemoryLimit`

- **File:** `src/runtime/mgcpacer_test.go`
    - Ground Truth Functions (4):
        - `TestGcPacer`
        - `TestIdleMarkWorkerCount`
        - `runway`
        - `triggerRatio`
    - Predicted Functions (1):
        - ❌ `applyMemoryLimitHeapGoalHeadroom`

- **File:** `src/runtime/mgcscavenge.go`
    - Ground Truth Functions (9):
        - `fillAligned`
        - `find`
        - `findScavengeCandidate`
        - `gcPaceScavenger`
        - `heapRetained`
        - `init`
        - `printScavTrace`
        - `scavenge`
        - `scavengeOne`
    - Predicted Functions (5):
        - ❌ `bgscavenge`
        - ✅ `gcPaceScavenger`
        - ✅ `heapRetained`
        - ✅ `scavenge`
        - ✅ `scavengeOne`

- **File:** `src/runtime/mgcscavenge_test.go`
    - Ground Truth Functions (1):
        - `TestScavengeIndex`
    - Predicted Functions (2):
        - ❌ `TestPageAllocScavenge`
        - ❌ `TestScavenger`

- **File:** `src/runtime/mgcsweep.go`
    - Ground Truth Functions (2):
        - `sweep`
        - `sweepone`
    - Predicted Functions (0):

- **File:** `src/runtime/mgcwork.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `balance`
        - ❌ `dispose`
        - ❌ `empty`
        - ❌ `freeSomeWbufs`
        - ❌ `init`

- **File:** `src/runtime/mheap.go`
    - Ground Truth Functions (5):
        - `allocSpan`
        - `freeSpanLocked`
        - `grow`
        - `runtime_debug_freeOSMemory`
        - `scavengeAll`
    - Predicted Functions (8):
        - ✅ `allocSpan`
        - ❌ `freeSpan`
        - ✅ `freeSpanLocked`
        - ✅ `grow`
        - ❌ `reclaim`
        - ❌ `reclaimChunk`
        - ✅ `runtime_debug_freeOSMemory`
        - ✅ `scavengeAll`

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
    - Ground Truth Functions (2):
        - `findRunnable`
        - `procresize`
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
        - ❌ `stmtNode`

- **File:** `src/go/parser/parser.go`
    - Ground Truth Functions (1):
        - `parseForStmt`
    - Predicted Functions (0):

- **File:** `src/go/parser/parser_test.go`
    - Ground Truth Functions (1):
        - `TestRangePos`
    - Predicted Functions (0):

- **File:** `src/go/token/token.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `IsIdentifier`
        - ❌ `IsKeyword`
        - ❌ `IsLiteral`
        - ❌ `IsOperator`
        - ❌ `Lookup`
        - ❌ `String`

- **File:** `test/range.go`
    - Ground Truth Functions (0):
    - Predicted Functions (18):
        - ❌ `testarray`
        - ❌ `testarray1`
        - ❌ `testarray2`
        - ❌ `testarrayptr`
        - ❌ `testarrayptr1`
        - ❌ `testarrayptr2`
        - ❌ `testblankvars`
        - ❌ `testchan`
        - ❌ `testmap`
        - ❌ `testmap1`
        - ❌ `testmap2`
        - ❌ `testslice`
        - ❌ `testslice1`
        - ❌ `testslice2`
        - ❌ `testslice3`
        - ❌ `teststring`
        - ❌ `teststring1`
        - ❌ `teststring2`

- **File:** `test/range2.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/range3.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `main`
        - ❌ `testint1`
        - ❌ `testint2`
        - ❌ `testint3`
        - ❌ `testint4`
        - ❌ `testint5`

- **File:** `test/range4.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `test/rangegen.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `gen`
        - ❌ `genLoop`


### 📊 **Proposal #44196 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 100.0% | 85.7% | 6/6 |

##### Ground Truth vs Predicted Functions per File

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
    - Predicted Functions (4):
        - ✅ `BenchmarkNowUnixMicro`
        - ✅ `BenchmarkNowUnixMilli`
        - ✅ `TestUnixMicro`
        - ✅ `TestUnixMilli`


### 📊 **Proposal #42710 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 46.7% | 58.3% | 51.9% | 7/12 |

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
    - Predicted Functions (7):
        - ✅ `Bytes`
        - ❌ `MakeSeed`
        - ✅ `SetSeed`
        - ✅ `String`
        - ✅ `Sum64`
        - ✅ `Write`
        - ✅ `WriteString`

- **File:** `src/hash/maphash/maphash_purego.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `rthash`
        - ❌ `rthashString`
        - ❌ `wyhash`

- **File:** `src/hash/maphash/maphash_runtime.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `rthash`
        - ❌ `rthashString`
        - ❌ `runtime_memhash`

- **File:** `src/hash/maphash/maphash_test.go`
    - Ground Truth Functions (3):
        - `BenchmarkHash`
        - `TestHashGrouping`
        - `benchmarkSize`
    - Predicted Functions (2):
        - ✅ `BenchmarkHash`
        - ❌ `TestHashBytesVsString`

- **File:** `test/escape_hash_maphash.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #53346 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 23.1% | 27.3% | 3/13 |

##### Ground Truth vs Predicted Functions per File

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
    - Predicted Functions (3):
        - ✅ `Close`
        - ✅ `EncodeToken`
        - ✅ `Flush`

- **File:** `src/encoding/xml/marshal_test.go`
    - Ground Truth Functions (1):
        - `TestClose`
    - Predicted Functions (0):

- **File:** `src/encoding/xml/xml.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Close`
        - ❌ `EncodeToken`
        - ❌ `Flush`

- **File:** `src/encoding/xml/xml_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Close`
        - ❌ `EncodeToken`
        - ❌ `Flush`


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
    - Predicted Functions (2):
        - ❌ `globalOptionsHandler.ServeHTTP`
        - ❌ `serverHandler.ServeHTTP`


### 📊 **Proposal #53021 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 44.4% | 53.3% | 4/9 |

##### Ground Truth vs Predicted Functions per File

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

- **File:** `src/crypto/subtle/xor_linux_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestXORBytesBoundary`

- **File:** `src/crypto/subtle/xor_test.go`
    - Ground Truth Functions (4):
        - `BenchmarkXORBytes`
        - `TestXORBytes`
        - `TestXorBytesPanic`
        - `mustPanic`
    - Predicted Functions (4):
        - ✅ `BenchmarkXORBytes`
        - ❌ `BenchmarkXORBytesAlignment`
        - ✅ `TestXORBytes`
        - ✅ `TestXorBytesPanic`


### 📊 **Proposal #37033 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 75.0% | 60.0% | 3/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/link/internal/ld/lib.go`
    - Ground Truth Functions (1):
        - `loadlib`
    - Predicted Functions (0):

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
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `BenchmarkHandle`
        - ❌ `TestHandle`
        - ❌ `TestInvalidHandle`


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
    - Predicted Functions (2):
        - ❌ `Seq`
        - ❌ `Seq2`

- **File:** `src/reflect/iter_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (15):
        - ❌ `MapIndex`
        - ❌ `MapKeys`
        - ❌ `MapRange`
        - ❌ `Set`
        - ❌ `SetBool`
        - ❌ `SetBytes`
        - ❌ `SetCap`
        - ❌ `SetComplex`
        - ❌ `SetFloat`
        - ❌ `SetInt`
        - ❌ `SetLen`
        - ❌ `SetMapIndex`
        - ❌ `SetPointer`
        - ❌ `SetString`
        - ❌ `SetUint`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `MapIndex`
        - ❌ `MapKeys`
        - ❌ `MapRange`
        - ❌ `Set`
        - ❌ `SetIterKey`
        - ❌ `SetIterValue`
        - ❌ `SetKey`
        - ❌ `SetMapIndex`
        - ❌ `SetValue`


### 📊 **Proposal #40728 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 4.5% | 7.1% | 4/88 |

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

- **File:** `src/cmd/go/internal/modcmd/mod.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `download`
        - ❌ `query`
        - ❌ `resolvePath`
        - ❌ `runGet`

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
    - Predicted Functions (6):
        - ✅ `Error`
        - ✅ `ImportPath`
        - ✅ `Unwrap`
        - ❌ `importFromModules`
        - ❌ `mustHaveSums`
        - ✅ `queryImport`

- **File:** `src/cmd/go/internal/modload/import_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestQueryImport`

- **File:** `src/cmd/go/internal/modload/init.go`
    - Ground Truth Functions (2):
        - `WriteGoMod`
        - `setDefaultBuildMod`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/load.go`
    - Ground Truth Functions (1):
        - `load`
    - Predicted Functions (7):
        - ❌ `ImportFromFiles`
        - ❌ `LoadPackages`
        - ❌ `Lookup`
        - ❌ `checkTidyCompatibility`
        - ❌ `loadFromRoots`
        - ❌ `resolveMissingImports`
        - ❌ `updateRequirements`

- **File:** `src/cmd/go/internal/modload/modfile.go`
    - Ground Truth Functions (3):
        - `Error`
        - `Unwrap`
        - `indexModFile`
    - Predicted Functions (6):
        - ❌ `CheckAllowed`
        - ❌ `CheckDeprecation`
        - ❌ `CheckExclusions`
        - ❌ `CheckRetractions`
        - ❌ `ReadModFile`
        - ❌ `queryLatestVersionIgnoringRetractions`

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


### 📊 **Proposal #44853 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.9% | 10.7% | 10.8% | 6/56 |

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
    - Predicted Functions (4):
        - ✅ `GetRedzoneSizeForGlobal`
        - ✅ `canInstrumentGlobal`
        - ✅ `createtypes`
        - ✅ `instrumentGlobals`

- **File:** `src/cmd/compile/internal/reflectdata/reflect.go`
    - Ground Truth Functions (1):
        - `WriteBasicTypes`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/compile.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Compile`

- **File:** `src/cmd/compile/internal/ssagen/ssa.go`
    - Ground Truth Functions (4):
        - `InitConfig`
        - `exprCheckPtr`
        - `instrument2`
        - `instrumentFields`
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `raceDetectorSupported`
        - ❌ `registerCgoTests`
        - ❌ `registerRaceTests`

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
    - Predicted Functions (3):
        - ✅ `AddBuildFlags`
        - ❌ `runBuild`
        - ❌ `runInstall`

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

- **File:** `src/cmd/link/internal/ld/ld.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `addlib`
        - ❌ `addlibpath`

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
    - Predicted Functions (0):

- **File:** `src/internal/asan/noasan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Read`
        - ❌ `Write`

- **File:** `src/internal/msan/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/msan/msan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Free`
        - ❌ `Malloc`
        - ❌ `Move`
        - ❌ `Read`
        - ❌ `Write`

- **File:** `src/internal/msan/nomsan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Free`
        - ❌ `Malloc`
        - ❌ `Move`
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
    - Predicted Functions (0):

- **File:** `src/runtime/asan/asan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `asanpoison`
        - ❌ `asanread`
        - ❌ `asanregisterglobals`
        - ❌ `asanunpoison`
        - ❌ `asanwrite`

- **File:** `src/runtime/asan0.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `asanpoison`
        - ❌ `asanread`
        - ❌ `asanregisterglobals`
        - ❌ `asanunpoison`
        - ❌ `asanwrite`

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
    - Predicted Functions (5):
        - ✅ `mallocgc`
        - ❌ `persistentalloc`
        - ❌ `persistentalloc1`
        - ❌ `redZoneSize`
        - ❌ `sysAlloc`

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

- **File:** `src/runtime/msan.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `MSanRead`
        - ❌ `MSanWrite`
        - ❌ `domsanread`
        - ❌ `msanfree`
        - ❌ `msanmalloc`
        - ❌ `msanmove`
        - ❌ `msanread`
        - ❌ `msanwrite`

- **File:** `src/runtime/msan0.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `msanfree`
        - ❌ `msanmalloc`
        - ❌ `msanmove`
        - ❌ `msanread`
        - ❌ `msanwrite`

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


### 📊 **Proposal #37533 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 100.0% | 44.4% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (1):
        - `Parse`
    - Predicted Functions (5):
        - ✅ `Parse`
        - ❌ `commandLineUsage`
        - ❌ `defaultUsage`
        - ❌ `parseOne`
        - ❌ `usage`

- **File:** `src/flag/flag_test.go`
    - Ground Truth Functions (1):
        - `TestExitCode`
    - Predicted Functions (2):
        - ✅ `TestExitCode`
        - ❌ `TestHelp`


### 📊 **Proposal #46287 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 45.8% | 56.4% | 50.6% | 22/39 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `registerTests`
    - Predicted Functions (0):

- **File:** `src/crypto/x509/cert_pool.go`
    - Ground Truth Functions (1):
        - `SystemCertPool`
    - Predicted Functions (5):
        - ❌ `AddCert`
        - ❌ `AppendCertsFromPEM`
        - ❌ `Equal`
        - ❌ `Subjects`
        - ✅ `SystemCertPool`

- **File:** `src/crypto/x509/cert_pool_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestCertPoolEqual`

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
    - Predicted Functions (20):
        - ✅ `BytesToCFData`
        - ✅ `CFArrayAppendValue`
        - ✅ `CFArrayCreateMutable`
        - ❌ `CFArrayGetCount`
        - ❌ `CFArrayGetValueAtIndex`
        - ❌ `CFDataGetBytePtr`
        - ❌ `CFDataGetLength`
        - ❌ `CFDataToSlice`
        - ✅ `CFDateCreate`
        - ❌ `CFDictionaryGetValueIfPresent`
        - ❌ `CFEqual`
        - ✅ `CFErrorCopyDescription`
        - ❌ `CFErrorGetCode`
        - ❌ `CFNumberGetValue`
        - ❌ `CFRelease`
        - ✅ `CFStringCreateExternalRepresentation`
        - ✅ `CFStringToString`
        - ✅ `ReleaseCFArray`
        - ❌ `StringToCFString`
        - ✅ `TimeToCFDateRef`

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
    - Predicted Functions (8):
        - ❌ `SecCertificateCopyData`
        - ✅ `SecCertificateCreateWithData`
        - ✅ `SecPolicyCreateSSL`
        - ❌ `SecTrustCopyCertificateChain`
        - ✅ `SecTrustCreateWithCertificates`
        - ✅ `SecTrustEvaluate`
        - ✅ `SecTrustEvaluateWithError`
        - ✅ `SecTrustSetVerifyDate`

- **File:** `src/crypto/x509/root_darwin.go`
    - Ground Truth Functions (3):
        - `exportCertificate`
        - `loadSystemRoots`
        - `systemVerify`
    - Predicted Functions (2):
        - ✅ `loadSystemRoots`
        - ✅ `systemVerify`

- **File:** `src/crypto/x509/root_windows.go`
    - Ground Truth Functions (2):
        - `loadSystemRoots`
        - `systemVerify`
    - Predicted Functions (3):
        - ✅ `loadSystemRoots`
        - ✅ `systemVerify`
        - ❌ `verifyChain`

- **File:** `src/crypto/x509/verify.go`
    - Ground Truth Functions (1):
        - `Verify`
    - Predicted Functions (6):
        - ❌ `SystemCertPool`
        - ✅ `Verify`
        - ❌ `VerifyHostname`
        - ❌ `buildChains`
        - ❌ `checkChainForKeyUsage`
        - ❌ `checkNameConstraints`

- **File:** `src/crypto/x509/verify_test.go`
    - Ground Truth Functions (1):
        - `TestSystemRootsError`
    - Predicted Functions (3):
        - ✅ `TestSystemRootsError`
        - ❌ `TestSystemRootsErrorUnwrap`
        - ❌ `TestSystemVerify`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (1):
        - `TestSystemCertPool`
    - Predicted Functions (0):

- **File:** `src/runtime/sys_darwin.go`
    - Ground Truth Functions (1):
        - `crypto_x509_syscall`
    - Predicted Functions (0):


### 📊 **Proposal #47916 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.8% | 8.0% | 5.1% | 2/25 |

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

- **File:** `src/go/types/api.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `ArgumentError`
        - ❌ `Check`
        - ❌ `Error`
        - ❌ `ObjectOf`
        - ❌ `PkgNameOf`
        - ❌ `TypeOf`

- **File:** `src/go/types/api_test.go`
    - Ground Truth Functions (1):
        - `TestInstantiate`
    - Predicted Functions (0):

- **File:** `src/go/types/assignments.go`
    - Ground Truth Functions (1):
        - `assignment`
    - Predicted Functions (0):

- **File:** `src/go/types/call.go`
    - Ground Truth Functions (4):
        - `arguments`
        - `callExpr`
        - `funcInst`
        - `selector`
    - Predicted Functions (0):

- **File:** `src/go/types/context.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `NewContext`
        - ❌ `getID`
        - ❌ `instanceHash`
        - ❌ `lookup`
        - ❌ `update`

- **File:** `src/go/types/decl.go`
    - Ground Truth Functions (1):
        - `typeDecl`
    - Predicted Functions (0):

- **File:** `src/go/types/index.go`
    - Ground Truth Functions (1):
        - `indexExpr`
    - Predicted Functions (0):

- **File:** `src/go/types/infer.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `coreTerm`
        - ❌ `infer`
        - ❌ `isParameterized`
        - ❌ `renameTParams`

- **File:** `src/go/types/instantiate.go`
    - Ground Truth Functions (2):
        - `Instantiate`
        - `instance`
    - Predicted Functions (6):
        - ✅ `Instantiate`
        - ❌ `implements`
        - ✅ `instance`
        - ❌ `mentions`
        - ❌ `validateTArgLen`
        - ❌ `verify`

- **File:** `src/go/types/interface.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `Embedded`
        - ❌ `EmbeddedType`
        - ❌ `ExplicitMethod`
        - ❌ `IsComparable`
        - ❌ `IsMethodSet`
        - ❌ `Method`
        - ❌ `NewInterfaceType`
        - ❌ `NumEmbeddeds`
        - ❌ `NumExplicitMethods`
        - ❌ `NumMethods`

- **File:** `src/go/types/lookup.go`
    - Ground Truth Functions (1):
        - `missingMethod`
    - Predicted Functions (0):

- **File:** `src/go/types/named.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `NewNamed`
        - ❌ `Origin`
        - ❌ `SetTypeParams`
        - ❌ `TypeArgs`
        - ❌ `TypeParams`
        - ❌ `context`
        - ❌ `newNamedInstance`

- **File:** `src/go/types/object.go`
    - Ground Truth Functions (1):
        - `writeObject`
    - Predicted Functions (4):
        - ❌ `NewFunc`
        - ❌ `NewTypeName`
        - ❌ `Origin`
        - ❌ `Signature`

- **File:** `src/go/types/predicates.go`
    - Ground Truth Functions (2):
        - `identical`
        - `isGeneric`
    - Predicted Functions (0):

- **File:** `src/go/types/signature.go`
    - Ground Truth Functions (1):
        - `funcType`
    - Predicted Functions (7):
        - ❌ `NewSignatureType`
        - ❌ `Params`
        - ❌ `Recv`
        - ❌ `RecvTypeParams`
        - ❌ `Results`
        - ❌ `TypeParams`
        - ❌ `Variadic`

- **File:** `src/go/types/subst.go`
    - Ground Truth Functions (1):
        - `typ`
    - Predicted Functions (0):

- **File:** `src/go/types/typelists.go`
    - Ground Truth Functions (1):
        - `bindTParams`
    - Predicted Functions (0):

- **File:** `src/go/types/typeparam.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Constraint`
        - ❌ `NewTypeParam`
        - ❌ `SetConstraint`
        - ❌ `Underlying`

- **File:** `src/go/types/typestring.go`
    - Ground Truth Functions (2):
        - `signature`
        - `typ`
    - Predicted Functions (0):


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

- **File:** `src/io/io_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestCopy`
        - ❌ `TestCopyN`
        - ❌ `TestReadAtLeast`


### 📊 **Proposal #35833 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 28.6% | 26.7% | 2/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/elliptic/elliptic.go`
    - Ground Truth Functions (3):
        - `GenerateKey`
        - `Marshal`
        - `Unmarshal`
    - Predicted Functions (0):

- **File:** `src/crypto/rsa/pkcs1v15.go`
    - Ground Truth Functions (2):
        - `EncryptPKCS1v15`
        - `decryptPKCS1v15`
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
    - Predicted Functions (5):
        - ❌ `Bytes`
        - ❌ `FillBytes`
        - ❌ `TestBytes`
        - ✅ `TestFillBytes`
        - ❌ `checkBytes`


### 📊 **Proposal #42027 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 70.6% | 34.3% | 46.2% | 12/35 |

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
    - Predicted Functions (6):
        - ❌ `TestIssue51617`
        - ✅ `TestWalkDir`
        - ❌ `TestWalkDirSymlink`
        - ✅ `makeTree`
        - ✅ `mark`
        - ✅ `walkTree`

- **File:** `src/path/filepath/path.go`
    - Ground Truth Functions (6):
        - `Base`
        - `Walk`
        - `WalkDir`
        - `readDirNames`
        - `walk`
        - `walkDir`
    - Predicted Functions (5):
        - ✅ `Walk`
        - ✅ `WalkDir`
        - ✅ `readDirNames`
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
    - Predicted Functions (3):
        - ✅ `TestWalkDir`
        - ❌ `WalkDir`
        - ❌ `walkTree`

- **File:** `src/path/filepath/path_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/path/filepath/path_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `WalkDir`

- **File:** `test/winbatch.go`
    - Ground Truth Functions (1):
        - `main`
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

- **File:** `src/runtime/metrics/description.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `All`
        - ❌ `init`

- **File:** `src/runtime/metrics/description_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestDocs`
        - ❌ `TestNames`
        - ❌ `runtime_readMetricNames`

- **File:** `src/runtime/metrics/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/metrics/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ExampleRead_readingAllMetrics`
        - ❌ `ExampleRead_readingOneMetric`

- **File:** `src/runtime/metrics/histogram.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/metrics/sample.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Read`
        - ❌ `runtime_readMetrics`

- **File:** `src/runtime/metrics/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Float64`
        - ❌ `Float64Histogram`
        - ❌ `Kind`
        - ❌ `Uint64`

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


### 📊 **Proposal #50465 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 4/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/httputil/reverseproxy.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (3):
        - ✅ `ServeHTTP`
        - ❌ `SetXForwarded`
        - ❌ `modifyResponse`

- **File:** `src/net/http/httputil/reverseproxy_test.go`
    - Ground Truth Functions (7):
        - `TestClonesRequestHeaders`
        - `TestModifyResponseClosesBody`
        - `TestReverseProxy`
        - `TestReverseProxyRewriteStripsForwarded`
        - `TestServeHTTPDeepCopy`
        - `TestXForwardedFor`
        - `TestXForwardedFor_Omit`
    - Predicted Functions (5):
        - ✅ `TestReverseProxyRewriteStripsForwarded`
        - ❌ `TestReverseProxyStripEmptyConnection`
        - ❌ `TestReverseProxyStripHeadersPresentInConnection`
        - ✅ `TestXForwardedFor`
        - ✅ `TestXForwardedFor_Omit`


### 📊 **Proposal #45435 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.7% | 100.0% | 34.3% | 6/6 |

##### Ground Truth vs Predicted Functions per File

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
    - Predicted Functions (10):
        - ❌ `BenchmarkMutex`
        - ❌ `BenchmarkMutexNoSpin`
        - ❌ `BenchmarkMutexSlack`
        - ❌ `BenchmarkMutexSpin`
        - ❌ `BenchmarkMutexWork`
        - ❌ `BenchmarkMutexWorkSlack`
        - ✅ `HammerMutex`
        - ✅ `TestMutex`
        - ❌ `TestMutexFairness`
        - ❌ `TestMutexMisuse`

- **File:** `src/sync/rwmutex.go`
    - Ground Truth Functions (2):
        - `TryLock`
        - `TryRLock`
    - Predicted Functions (2):
        - ✅ `TryLock`
        - ✅ `TryRLock`

- **File:** `src/sync/rwmutex_test.go`
    - Ground Truth Functions (1):
        - `TestRWMutex`
    - Predicted Functions (14):
        - ❌ `BenchmarkRWMutexUncontended`
        - ❌ `BenchmarkRWMutexWorkWrite10`
        - ❌ `BenchmarkRWMutexWorkWrite100`
        - ❌ `BenchmarkRWMutexWrite10`
        - ❌ `BenchmarkRWMutexWrite100`
        - ❌ `HammerRWMutex`
        - ❌ `TestParallelReaders`
        - ❌ `TestRLocker`
        - ✅ `TestRWMutex`
        - ❌ `benchmarkRWMutex`
        - ❌ `doTestParallelReaders`
        - ❌ `parallelReader`
        - ❌ `reader`
        - ❌ `writer`


### 📊 **Proposal #33136 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.4% | 50.0% | 23.5% | 2/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (2):
        - `TestSmallZero`
        - `TestZeroSet`
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Set`
        - ❌ `SetZero`
        - ❌ `Zero`
        - ❌ `typedmemclr`
        - ❌ `typedmemmove`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (2):
        - `Set`
        - `Zero`
    - Predicted Functions (5):
        - ✅ `Set`
        - ❌ `SetZero`
        - ✅ `Zero`
        - ❌ `typedmemclr`
        - ❌ `typedmemmove`

- **File:** `test/clear.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `checkClearMap`
        - ❌ `checkClearSlice`
        - ❌ `main`


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

- **File:** `src/cmd/vet/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `errorCheck`

- **File:** `src/errors/errors.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Error`

- **File:** `src/errors/wrap.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `As`
        - ❌ `Is`
        - ❌ `Unwrap`

- **File:** `src/errors/wrap_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `As`
        - ❌ `Is`
        - ❌ `Unwrap`


### 📊 **Proposal #44808 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 16.7% | 24.0% | 3/18 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/image/color/color.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `RGBA`
        - ❌ `RGBA64`

- **File:** `src/image/draw/draw.go`
    - Ground Truth Functions (2):
        - `DrawMask`
        - `drawRGBA`
    - Predicted Functions (3):
        - ❌ `Draw`
        - ✅ `DrawMask`
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
    - Predicted Functions (2):
        - ✅ `RGBA64At`
        - ✅ `SetRGBA64`

- **File:** `src/image/image_test.go`
    - Ground Truth Functions (1):
        - `TestRGBA64Image`
    - Predicted Functions (0):

- **File:** `src/image/names.go`
    - Ground Truth Functions (1):
        - `RGBA64At`
    - Predicted Functions (0):

- **File:** `src/image/ycbcr.go`
    - Ground Truth Functions (1):
        - `RGBA64At`
    - Predicted Functions (0):


### 📊 **Proposal #41066 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 33.3% | 28.6% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/conn.go`
    - Ground Truth Functions (2):
        - `Close`
        - `Write`
    - Predicted Functions (3):
        - ✅ `Close`
        - ❌ `CloseWrite`
        - ❌ `closeNotify`

- **File:** `src/crypto/tls/conn_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Close`

- **File:** `src/crypto/tls/tls_test.go`
    - Ground Truth Functions (1):
        - `TestConnCloseBreakingWrite`
    - Predicted Functions (0):


### 📊 **Proposal #38017 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 26.7% | 33.3% | 29.6% | 4/12 |

##### Ground Truth vs Predicted Functions per File

- **File:** `lib/time/mkzip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `main`
        - ❌ `usage`

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
    - Predicted Functions (2):
        - ✅ `loadFromEmbeddedTZData`
        - ✅ `registerLoadFromEmbeddedTZData`

- **File:** `src/time/tzdata_test.go`
    - Ground Truth Functions (2):
        - `TestEmbeddedTZData`
        - `equal`
    - Predicted Functions (0):

- **File:** `src/time/zoneinfo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `LoadLocation`
        - ❌ `firstZoneUsed`
        - ❌ `lookup`
        - ❌ `lookupFirstZone`
        - ❌ `lookupName`

- **File:** `src/time/zoneinfo_read.go`
    - Ground Truth Functions (4):
        - `Error`
        - `loadLocation`
        - `readFile`
        - `registerLoadFromEmbeddedTZData`
    - Predicted Functions (4):
        - ❌ `LoadLocationFromTZData`
        - ✅ `loadLocation`
        - ❌ `loadTzinfo`
        - ✅ `registerLoadFromEmbeddedTZData`

- **File:** `src/time/zoneinfo_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestLoadLocationFromTZData`
        - ❌ `TestLoadLocationFromTZDataSlim`


### 📊 **Proposal #42088 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 27.3% | 25.0% | 26.1% | 3/12 |

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
    - Predicted Functions (3):
        - ❌ `buildRunProgram`
        - ✅ `runRun`
        - ✅ `shouldUseOutsideModuleMode`

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (2):
        - `FindExecCmd`
        - `installOutsideModule`
    - Predicted Functions (3):
        - ✅ `installOutsideModule`
        - ❌ `runBuild`
        - ❌ `runInstall`

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Do`
        - ❌ `build`
        - ❌ `buildActionID`
        - ❌ `link`
        - ❌ `linkActionID`


### 📊 **Proposal #50062 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 50.0% | 20.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/time/time.go`
    - Ground Truth Functions (1):
        - `ZoneBounds`
    - Predicted Functions (4):
        - ❌ `IsDST`
        - ❌ `Zone`
        - ✅ `ZoneBounds`
        - ❌ `lookup`

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


### 📊 **Proposal #35998 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 25.0% | 16.7% | 1/4 |

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
    - Predicted Functions (4):
        - ❌ `Cleanup`
        - ✅ `TempDir`
        - ❌ `private`
        - ❌ `removeAll`

- **File:** `src/testing/testing_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestTempDir`
        - ❌ `TestTempDirInBenchmark`
        - ❌ `TestTempDirInCleanup`
        - ❌ `testTempDir`


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
        - ❌ `Seq`
        - ❌ `Seq2`

- **File:** `src/reflect/iter_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestValueSeq`
        - ❌ `TestValueSeq2`

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `MapIter`
        - ❌ `Reset`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `MapIter`
        - ❌ `Reset`


### 📊 **Proposal #44011 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 17.9% | 62.5% | 27.8% | 5/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/internal/syscall/windows/exec_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestRunAtLowIntegrity`
        - ❌ `getIntegrityLevelToken`
        - ❌ `getProcessIntegrityLevel`
        - ❌ `tokenGetInfo`

- **File:** `src/internal/syscall/windows/syscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/syscall/windows/types_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `init`

- **File:** `src/internal/syscall/windows/zsyscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `CreateEvent`
        - ❌ `CreateIoCompletionPort`
        - ❌ `CreateNamedPipe`

- **File:** `src/os/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `StartProcess`

- **File:** `src/os/exec/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `skipStdinCopyError`

- **File:** `src/os/exec/exec_windows_test.go`
    - Ground Truth Functions (1):
        - `TestPipePassing`
    - Predicted Functions (0):

- **File:** `src/os/exec_posix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `startProcess`

- **File:** `src/os/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `closeHandle`
        - ❌ `findProcess`
        - ❌ `signal`
        - ❌ `wait`

- **File:** `src/os/file_windows.go`
    - Ground Truth Functions (1):
        - `Pipe`
    - Predicted Functions (0):

- **File:** `src/syscall/exec_windows.go`
    - Ground Truth Functions (1):
        - `StartProcess`
    - Predicted Functions (1):
        - ✅ `StartProcess`

- **File:** `src/syscall/exec_windows_test.go`
    - Ground Truth Functions (1):
        - `TestChangingProcessParent`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (1):
        - `newProcThreadAttributeList`
    - Predicted Functions (4):
        - ❌ `delete`
        - ❌ `list`
        - ✅ `newProcThreadAttributeList`
        - ❌ `update`

- **File:** `src/syscall/types_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Nanoseconds`
        - ❌ `NsecToFiletime`
        - ❌ `NsecToTimeval`
        - ❌ `copyFindData`

- **File:** `src/syscall/zsyscall_windows.go`
    - Ground Truth Functions (3):
        - `deleteProcThreadAttributeList`
        - `initializeProcThreadAttributeList`
        - `updateProcThreadAttribute`
    - Predicted Functions (4):
        - ❌ `CreateProcess`
        - ✅ `deleteProcThreadAttributeList`
        - ✅ `initializeProcThreadAttributeList`
        - ✅ `updateProcThreadAttribute`


### 📊 **Proposal #48218 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 50.0% | 28.6% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (1):
        - `FieldByIndexErr`
    - Predicted Functions (5):
        - ❌ `Field`
        - ❌ `FieldByIndex`
        - ✅ `FieldByIndexErr`
        - ❌ `FieldByName`
        - ❌ `FieldByNameFunc`

- **File:** `src/reflect/visiblefields_test.go`
    - Ground Truth Functions (1):
        - `TestFieldByIndexErr`
    - Predicted Functions (0):


### 📊 **Proposal #32406 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 13/26 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (1):
        - `Context`
    - Predicted Functions (4):
        - ✅ `Context`
        - ❌ `HandshakeContext`
        - ❌ `SupportsCertificate`
        - ❌ `getCertificate`

- **File:** `src/crypto/tls/conn.go`
    - Ground Truth Functions (4):
        - `Handshake`
        - `HandshakeContext`
        - `handleRenegotiation`
        - `handshakeContext`
    - Predicted Functions (3):
        - ✅ `Handshake`
        - ✅ `HandshakeContext`
        - ✅ `handshakeContext`

- **File:** `src/crypto/tls/conn_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestCertificateSelection`

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (3):
        - `certificateRequestInfoFromMsg`
        - `clientHandshake`
        - `doFullHandshake`
    - Predicted Functions (3):
        - ✅ `clientHandshake`
        - ❌ `getClientCertificate`
        - ❌ `verifyServerCertificate`

- **File:** `src/crypto/tls/handshake_client_test.go`
    - Ground Truth Functions (1):
        - `TestClientHandshakeContextCancellation`
    - Predicted Functions (3):
        - ✅ `TestClientHandshakeContextCancellation`
        - ❌ `TestGetClientCertificate`
        - ❌ `testGetClientCertificate`

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
    - Predicted Functions (5):
        - ✅ `clientHelloInfo`
        - ✅ `handshake`
        - ✅ `processClientHello`
        - ✅ `readClientHello`
        - ✅ `serverHandshake`

- **File:** `src/crypto/tls/handshake_server_test.go`
    - Ground Truth Functions (3):
        - `TestSNIGivenOnFailure`
        - `TestServerHandshakeContextCancellation`
        - `testClientHelloFailure`
    - Predicted Functions (2):
        - ❌ `TestHandshakeContextHierarchy`
        - ✅ `TestServerHandshakeContextCancellation`

- **File:** `src/crypto/tls/handshake_server_tls13.go`
    - Ground Truth Functions (1):
        - `pickCertificate`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/tls.go`
    - Ground Truth Functions (2):
        - `Dial`
        - `dial`
    - Predicted Functions (0):

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (1):
        - `serve`
    - Predicted Functions (5):
        - ❌ `ListenAndServeTLS`
        - ❌ `ServeTLS`
        - ❌ `newConn`
        - ✅ `serve`
        - ❌ `setupHTTP2_ServeTLS`

- **File:** `src/net/http/transport.go`
    - Ground Truth Functions (2):
        - `addTLS`
        - `dialConn`
    - Predicted Functions (0):

- **File:** `src/net/http/transport_test.go`
    - Ground Truth Functions (1):
        - `TestTransportDialTLSContext`
    - Predicted Functions (0):


### 📊 **Proposal #48424 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.6% | 13.7% | 17.1% | 7/51 |

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
    - Predicted Functions (5):
        - ❌ `Constraint`
        - ❌ `NewTypeParam`
        - ✅ `SetConstraint`
        - ✅ `iface`
        - ❌ `typeset`

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
    - Predicted Functions (5):
        - ❌ `Constraint`
        - ❌ `NewTypeParam`
        - ✅ `SetConstraint`
        - ✅ `iface`
        - ❌ `typeset`

- **File:** `src/go/types/typestring.go`
    - Ground Truth Functions (1):
        - `typ`
    - Predicted Functions (0):

- **File:** `src/go/types/universe.go`
    - Ground Truth Functions (1):
        - `defPredeclaredTypes`
    - Predicted Functions (0):

- **File:** `src/slices/slices.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Clone`
        - ❌ `CompactFunc`
        - ❌ `CompareFunc`
        - ❌ `ContainsFunc`
        - ❌ `DeleteFunc`
        - ❌ `EqualFunc`
        - ❌ `IndexFunc`

- **File:** `src/slices/slices_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (11):
        - ❌ `BenchmarkCompactFunc`
        - ❌ `BenchmarkCompactFunc_Large`
        - ❌ `BenchmarkEqualFunc_Large`
        - ❌ `BenchmarkIndexFunc_Large`
        - ❌ `TestCompactFunc`
        - ❌ `TestCompareFunc`
        - ❌ `TestContainsFunc`
        - ❌ `TestDeleteFunc`
        - ❌ `TestEqualFunc`
        - ❌ `TestIndexFunc`
        - ❌ `TestInference`

- **File:** `test/typeparam/issue48424.go`
    - Ground Truth Functions (4):
        - `identity`
        - `main`
        - `max`
        - `min`
    - Predicted Functions (3):
        - ✅ `identity`
        - ✅ `max`
        - ✅ `min`


### 📊 **Proposal #40724 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 26.8% | 5.6% | 9.2% | 26/467 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/asm/internal/arch/arch.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `archArm`
        - ❌ `archArm64`
        - ❌ `archLoong64`
        - ❌ `archMips`
        - ❌ `archMips64`
        - ❌ `archPPC64`
        - ❌ `archRISCV64`
        - ❌ `archS390x`
        - ❌ `archWasm`
        - ❌ `archX86`

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

- **File:** `src/cmd/asm/internal/asm/operand_test.go`
    - Ground Truth Functions (4):
        - `TestAMD64OperandParser`
        - `TestFuncAddress`
        - `newParser`
        - `testOperandParser`
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
    - Predicted Functions (34):
        - ❌ `ABIAnalyze`
        - ❌ `ABIAnalyzeFuncType`
        - ❌ `ABIAnalyzeTypes`
        - ❌ `ArgWidth`
        - ❌ `ComputePadding`
        - ❌ `Config`
        - ❌ `Copy`
        - ❌ `FloatIndexFor`
        - ✅ `FrameOffset`
        - ❌ `InParam`
        - ❌ `InParams`
        - ❌ `InRegistersUsed`
        - ❌ `LocalsOffset`
        - ❌ `NewABIConfig`
        - ❌ `NumParamRegs`
        - ❌ `Offset`
        - ❌ `OutParam`
        - ❌ `OutParams`
        - ❌ `OutRegistersUsed`
        - ❌ `RegisterTypes`
        - ❌ `RegisterTypesAndOffsets`
        - ❌ `SpillAreaOffset`
        - ❌ `SpillAreaSize`
        - ❌ `String`
        - ❌ `ToString`
        - ❌ `Which`
        - ❌ `align`
        - ❌ `alignTo`
        - ❌ `allocateRegs`
        - ❌ `assignParam`
        - ❌ `nextSlot`
        - ❌ `setup`
        - ❌ `tryAllocRegs`
        - ✅ `updateOffset`

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

- **File:** `src/cmd/compile/internal/ir/abi.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `InitLSym`
        - ❌ `setupTextLSym`

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
    - Predicted Functions (10):
        - ❌ `ArgOpAndRegisterFor`
        - ❌ `ParamAssignmentForArgName`
        - ❌ `decomposeAsNecessary`
        - ❌ `decomposeOne`
        - ❌ `decomposePair`
        - ✅ `expandCalls`
        - ❌ `rewriteCallArgs`
        - ❌ `rewriteFuncResults`
        - ❌ `rewriteSelectOrArg`
        - ❌ `rewriteWideSelectToStores`

- **File:** `src/cmd/compile/internal/ssa/export_test.go`
    - Ground Truth Functions (1):
        - `SplitSlot`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssa/func.go`
    - Ground Truth Functions (1):
        - `spSb`
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
    - Predicted Functions (6):
        - ✅ `GenABIWrappers`
        - ✅ `NewSymABIs`
        - ✅ `ReadSymABIs`
        - ✅ `canonicalize`
        - ✅ `forEachWrapperABI`
        - ✅ `makeABIWrapper`

- **File:** `src/cmd/compile/internal/ssagen/nowb.go`
    - Ground Truth Functions (1):
        - `newNowritebarrierrecChecker`
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/ssagen/ssa.go`
    - Ground Truth Functions (9):
        - `buildssa`
        - `call`
        - `callTargetLSym`
        - `deferstruct`
        - `emitArgInfo`
        - `emitOpenDeferInfo`
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

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (1):
        - `asmArgs`
    - Predicted Functions (0):

- **File:** `src/cmd/internal/obj/abi_string.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `String`

- **File:** `src/cmd/internal/obj/link.go`
    - Ground Truth Functions (5):
        - `ABISetOf`
        - `Get`
        - `ParseABI`
        - `Set`
        - `String`
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
    - Ground Truth Functions (1):
        - `preprocess`
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
    - Predicted Functions (0):

- **File:** `src/internal/abi/abi_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

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

- **File:** `src/internal/goexperiment/exp_regabiargs_off.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goexperiment/exp_regabiargs_on.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goexperiment/exp_regabiwrappers_off.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goexperiment/exp_regabiwrappers_on.go`
    - Ground Truth Functions (0):
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
    - Predicted Functions (12):
        - ✅ `addArg`
        - ✅ `addRcvr`
        - ✅ `assignFloatN`
        - ✅ `assignIntN`
        - ❌ `dumpPtrBitMap`
        - ❌ `floatFromReg`
        - ❌ `floatToReg`
        - ❌ `intFromReg`
        - ❌ `intToReg`
        - ✅ `newAbiDesc`
        - ✅ `regAssign`
        - ✅ `stackAssign`

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
    - Predicted Functions (8):
        - ✅ `AllRegsCall`
        - ✅ `RegsAndStackCall`
        - ✅ `SpillStructCall`
        - ✅ `TestMethodValueCallABI`
        - ✅ `TestReflectCallABI`
        - ✅ `TestReflectMakeFuncCallABI`
        - ❌ `ValueRegMethodSpillInt`
        - ❌ `ValueRegMethodSpillPtr`

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
    - Ground Truth Functions (6):
        - `call`
        - `callMethod`
        - `callReflect`
        - `cvtIntString`
        - `methodReceiver`
        - `storeRcvr`
    - Predicted Functions (0):

- **File:** `src/runtime/abi_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestFinalizerRegisterABI`
        - ❌ `m`
        - ❌ `regFinalizerIface`
        - ❌ `regFinalizerPointer`

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

- **File:** `src/runtime/proc.go`
    - Ground Truth Functions (4):
        - `newproc`
        - `newproc1`
        - `oneNewExtraM`
        - `sigprof`
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

- **File:** `src/runtime/wincallback.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `genasm386Amd64`
        - ❌ `genasmArm`
        - ❌ `genasmArm64`
        - ❌ `gengo`

- **File:** `src/runtime/zcallback_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

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


### 📊 **Proposal #48152 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.5% | 40.0% | 16.7% | 2/5 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (2):
        - `Error`
        - `Unwrap`
    - Predicted Functions (0):

- **File:** `src/crypto/tls/conn.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Handshake`
        - ❌ `HandshakeContext`
        - ❌ `VerifyHostname`
        - ❌ `handshakeContext`

- **File:** `src/crypto/tls/conn_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestCertificateSelection`

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (1):
        - `verifyServerCertificate`
    - Predicted Functions (2):
        - ❌ `getClientCertificate`
        - ✅ `verifyServerCertificate`

- **File:** `src/crypto/tls/handshake_client_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestVerifyConnection`
        - ❌ `TestVerifyPeerCertificate`
        - ❌ `testVerifyConnection`
        - ❌ `testVerifyPeerCertificate`

- **File:** `src/crypto/tls/handshake_server.go`
    - Ground Truth Functions (1):
        - `processCertsFromClient`
    - Predicted Functions (3):
        - ❌ `doFullHandshake`
        - ❌ `handshake`
        - ✅ `processCertsFromClient`

- **File:** `src/crypto/tls/handshake_server_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestClientAuth`
        - ❌ `TestHandshakeServerEmptyCertificates`
        - ❌ `TestHandshakeServerSNIGetCertificateError`
        - ❌ `TestSNIGivenOnFailure`

- **File:** `src/crypto/tls/handshake_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `testHandshake`

- **File:** `src/net/http/transport_test.go`
    - Ground Truth Functions (1):
        - `testTransportEventTraceTLSVerify`
    - Predicted Functions (0):


### 📊 **Proposal #47609 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 29.4% | 83.3% | 43.5% | 5/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/test/inl_test.go`
    - Ground Truth Functions (1):
        - `TestIntendedInlining`
    - Predicted Functions (0):

- **File:** `src/runtime/utf8.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `encoderune`

- **File:** `src/unicode/utf8/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `AppendRune`
        - ❌ `EncodeRune`

- **File:** `src/unicode/utf8/utf8.go`
    - Ground Truth Functions (2):
        - `AppendRune`
        - `appendRuneNonASCII`
    - Predicted Functions (4):
        - ✅ `AppendRune`
        - ❌ `EncodeRune`
        - ✅ `appendRuneNonASCII`
        - ❌ `encodeRuneNonASCII`

- **File:** `src/unicode/utf8/utf8_test.go`
    - Ground Truth Functions (3):
        - `BenchmarkAppendASCIIRune`
        - `BenchmarkAppendJapaneseRune`
        - `TestAppendRune`
    - Predicted Functions (10):
        - ✅ `BenchmarkAppendASCIIRune`
        - ✅ `BenchmarkAppendJapaneseRune`
        - ❌ `BenchmarkAppendMaxRune`
        - ❌ `BenchmarkAppendSpanishRune`
        - ❌ `BenchmarkEncodeASCIIRune`
        - ❌ `BenchmarkEncodeJapaneseRune`
        - ❌ `BenchmarkEncodeMaxRune`
        - ❌ `BenchmarkEncodeSpanishRune`
        - ✅ `TestAppendRune`
        - ❌ `TestEncodeRune`

- **File:** `test/utf.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #50601 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 71.4% | 83.3% | 76.9% | 15/18 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/binary/binary.go`
    - Ground Truth Functions (3):
        - `AppendUint16`
        - `AppendUint32`
        - `AppendUint64`
    - Predicted Functions (7):
        - ✅ `AppendUint16`
        - ✅ `AppendUint32`
        - ✅ `AppendUint64`
        - ❌ `PutUint16`
        - ❌ `PutUint32`
        - ❌ `PutUint64`
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
    - Predicted Functions (14):
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
        - ❌ `TestBigEndianWrite`
        - ❌ `TestLittleEndianWrite`


### 📊 **Proposal #53482 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 100.0% | 30.8% | 6/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/interface.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `InterfaceByIndex`
        - ❌ `InterfaceByName`
        - ❌ `Interfaces`
        - ❌ `String`
        - ❌ `interfaceByIndex`

- **File:** `src/net/interface_aix.go`
    - Ground Truth Functions (1):
        - `linkFlags`
    - Predicted Functions (1):
        - ✅ `linkFlags`

- **File:** `src/net/interface_bsd.go`
    - Ground Truth Functions (1):
        - `linkFlags`
    - Predicted Functions (1):
        - ✅ `linkFlags`

- **File:** `src/net/interface_bsd_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `setBroadcast`
        - ❌ `setLinkLocal`
        - ❌ `setPointToPoint`

- **File:** `src/net/interface_bsdvar.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `interfaceMessages`
        - ❌ `interfaceMulticastAddrTable`

- **File:** `src/net/interface_darwin.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `interfaceMessages`
        - ❌ `interfaceMulticastAddrTable`

- **File:** `src/net/interface_freebsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `interfaceMessages`
        - ❌ `interfaceMulticastAddrTable`

- **File:** `src/net/interface_linux.go`
    - Ground Truth Functions (1):
        - `linkFlags`
    - Predicted Functions (1):
        - ✅ `linkFlags`

- **File:** `src/net/interface_linux_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestParseProcNet`
        - ❌ `setBroadcast`
        - ❌ `setLinkLocal`
        - ❌ `setPointToPoint`

- **File:** `src/net/interface_plan9.go`
    - Ground Truth Functions (1):
        - `readInterface`
    - Predicted Functions (2):
        - ❌ `interfaceTable`
        - ✅ `readInterface`

- **File:** `src/net/interface_solaris.go`
    - Ground Truth Functions (1):
        - `linkFlags`
    - Predicted Functions (1):
        - ✅ `linkFlags`

- **File:** `src/net/interface_stub.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `interfaceTable`

- **File:** `src/net/interface_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestInterfaces`
        - ❌ `loopbackInterface`

- **File:** `src/net/interface_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `TestInterfaceArrivalAndDeparture`
        - ❌ `TestInterfaceArrivalAndDepartureZoneCache`
        - ❌ `TestPointToPointInterface`
        - ❌ `setup`
        - ❌ `teardown`

- **File:** `src/net/interface_windows.go`
    - Ground Truth Functions (1):
        - `interfaceTable`
    - Predicted Functions (1):
        - ✅ `interfaceTable`

- **File:** `src/syscall/zerrors_aix_ppc64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_freebsd_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_freebsd_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_freebsd_arm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_freebsd_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_linux_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_linux_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_linux_s390x.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_netbsd_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_openbsd_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #43698 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/vet/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestVet`
        - ❌ `errorCheck`
        - ❌ `wantedErrors`

- **File:** `src/embed/embed.go`
    - Ground Truth Functions (2):
        - `lookup`
        - `readDir`
    - Predicted Functions (3):
        - ❌ `Open`
        - ❌ `ReadDir`
        - ❌ `ReadFile`

- **File:** `src/embed/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/embed/internal/embedtest/embed_test.go`
    - Ground Truth Functions (1):
        - `TestUninitialized`
    - Predicted Functions (0):


### 📊 **Proposal #50859 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/runtime/mbarrier.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `memclrHasPointers`
        - ❌ `typedmemclr`
        - ❌ `typedmemmove`
        - ❌ `wbMove`
        - ❌ `wbZero`

- **File:** `src/runtime/mem.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/sync/atomic/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (16):
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

- **File:** `src/sync/atomic/doc_32.go`
    - Ground Truth Functions (0):
    - Predicted Functions (14):
        - ❌ `AddInt64`
        - ❌ `AddUint64`
        - ❌ `AndInt64`
        - ❌ `AndUint64`
        - ❌ `CompareAndSwapInt64`
        - ❌ `CompareAndSwapUint64`
        - ❌ `LoadInt64`
        - ❌ `LoadUint64`
        - ❌ `OrInt64`
        - ❌ `OrUint64`
        - ❌ `StoreInt64`
        - ❌ `StoreUint64`
        - ❌ `SwapInt64`
        - ❌ `SwapUint64`

- **File:** `src/sync/atomic/doc_64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (14):
        - ❌ `AddInt64`
        - ❌ `AddUint64`
        - ❌ `AndInt64`
        - ❌ `AndUint64`
        - ❌ `CompareAndSwapInt64`
        - ❌ `CompareAndSwapUint64`
        - ❌ `LoadInt64`
        - ❌ `LoadUint64`
        - ❌ `OrInt64`
        - ❌ `OrUint64`
        - ❌ `StoreInt64`
        - ❌ `StoreUint64`
        - ❌ `SwapInt64`
        - ❌ `SwapUint64`

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

- **File:** `src/sync/cond.go`
    - Ground Truth Functions (1):
        - `check`
    - Predicted Functions (3):
        - ❌ `Broadcast`
        - ❌ `Signal`
        - ❌ `Wait`

- **File:** `src/sync/mutex.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Lock`
        - ❌ `TryLock`
        - ❌ `Unlock`

- **File:** `src/sync/rwmutex.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Lock`
        - ❌ `RLock`
        - ❌ `RLocker`
        - ❌ `RUnlock`
        - ❌ `TryLock`
        - ❌ `TryRLock`
        - ❌ `Unlock`

- **File:** `src/sync/waitgroup.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Add`
        - ❌ `Done`
        - ❌ `Wait`


### 📊 **Proposal #51914 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/httputil/reverseproxy.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (4):
        - ✅ `ServeHTTP`
        - ❌ `copyBuffer`
        - ❌ `copyResponse`
        - ❌ `modifyResponse`

- **File:** `src/net/http/httputil/reverseproxy_test.go`
    - Ground Truth Functions (1):
        - `Test1xxResponses`
    - Predicted Functions (2):
        - ❌ `Test1xxHeadersNotModifiedAfterRoundTrip`
        - ✅ `Test1xxResponses`

- **File:** `src/net/http/response.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Write`
        - ❌ `WriteHeader`

- **File:** `src/net/http/server.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `WriteHeader`
        - ❌ `checkWriteHeaderCode`
        - ❌ `writeHeader`
        - ❌ `writeStatusLine`


### 📊 **Proposal #46648 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 33.3% | 20.0% | 1/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/types2/version.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `allowVersion`
        - ❌ `asGoVersion`
        - ❌ `cmp`
        - ❌ `isValid`
        - ❌ `verifyVersionf`

- **File:** `src/go/types/check.go`
    - Ground Truth Functions (1):
        - `NewChecker`
    - Predicted Functions (2):
        - ✅ `NewChecker`
        - ❌ `versionMax`

- **File:** `src/go/types/check_test.go`
    - Ground Truth Functions (1):
        - `testFiles`
    - Predicted Functions (0):

- **File:** `src/go/types/stdlib_test.go`
    - Ground Truth Functions (1):
        - `testTestDir`
    - Predicted Functions (0):


### 📊 **Proposal #42102 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 36.4% | 33.3% | 34.8% | 4/12 |

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
    - Predicted Functions (4):
        - ✅ `IsDST`
        - ❌ `Location`
        - ✅ `Zone`
        - ❌ `ZoneBounds`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (1):
        - `TestTimeIsDST`
    - Predicted Functions (0):

- **File:** `src/time/zoneinfo.go`
    - Ground Truth Functions (3):
        - `lookup`
        - `lookupName`
        - `tzset`
    - Predicted Functions (7):
        - ✅ `lookup`
        - ❌ `tzruleTime`
        - ✅ `tzset`
        - ❌ `tzsetName`
        - ❌ `tzsetNum`
        - ❌ `tzsetOffset`
        - ❌ `tzsetRule`

- **File:** `src/time/zoneinfo_read.go`
    - Ground Truth Functions (1):
        - `LoadLocationFromTZData`
    - Predicted Functions (0):

- **File:** `src/time/zoneinfo_test.go`
    - Ground Truth Functions (1):
        - `TestTzset`
    - Predicted Functions (0):


### 📊 **Proposal #50332 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 9.5% | 12.5% | 2/21 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/doc/main.go`
    - Ground Truth Functions (1):
        - `do`
    - Predicted Functions (0):

- **File:** `src/cmd/go/chdir_test.go`
    - Ground Truth Functions (1):
        - `TestChdir`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/base/base.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Run`
        - ❌ `RunErr`
        - ❌ `hasFlag`

- **File:** `src/cmd/go/internal/base/flag.go`
    - Ground Truth Functions (1):
        - `AddChdirFlag`
    - Predicted Functions (2):
        - ✅ `AddChdirFlag`
        - ❌ `ChdirFlag`

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
    - Predicted Functions (3):
        - ✅ `AddBuildFlags`
        - ❌ `runBuild`
        - ❌ `runInstall`

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

- **File:** `src/cmd/go/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `handleChdirFlag`
        - ❌ `invoke`
        - ❌ `main`


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


### 📊 **Proposal #46059 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 66.7% | 40.0% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/url/url.go`
    - Ground Truth Functions (2):
        - `String`
        - `parse`
    - Predicted Functions (3):
        - ❌ `Parse`
        - ✅ `String`
        - ✅ `parse`

- **File:** `src/net/url/url_test.go`
    - Ground Truth Functions (1):
        - `ufmt`
    - Predicted Functions (4):
        - ❌ `Parse`
        - ❌ `String`
        - ❌ `TestParse`
        - ❌ `TestURLString`


### 📊 **Proposal #38079 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/httputil/reverseproxy.go`
    - Ground Truth Functions (1):
        - `ServeHTTP`
    - Predicted Functions (2):
        - ✅ `ServeHTTP`
        - ❌ `SetXForwarded`

- **File:** `src/net/http/httputil/reverseproxy_test.go`
    - Ground Truth Functions (1):
        - `TestXForwardedFor_Omit`
    - Predicted Functions (2):
        - ❌ `TestXForwardedFor`
        - ✅ `TestXForwardedFor_Omit`


### 📊 **Proposal #37776 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 20.0% | 21.1% | 2/10 |

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
    - Predicted Functions (2):
        - ✅ `EscapedFragment`
        - ✅ `setFragment`

- **File:** `src/net/url/url_test.go`
    - Ground Truth Functions (1):
        - `ufmt`
    - Predicted Functions (7):
        - ❌ `BenchmarkPathEscape`
        - ❌ `BenchmarkPathUnescape`
        - ❌ `BenchmarkQueryEscape`
        - ❌ `BenchmarkQueryUnescape`
        - ❌ `TestPathEscape`
        - ❌ `TestQueryEscape`
        - ❌ `TestUnescape`


### 📊 **Proposal #40025 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 29.6% | 19.5% | 23.5% | 8/41 |

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
    - Predicted Functions (21):
        - ❌ `Close`
        - ❌ `Copy`
        - ✅ `CopyBuffer`
        - ❌ `CopyN`
        - ❌ `LimitReader`
        - ✅ `NopCloser`
        - ❌ `Outer`
        - ❌ `Read`
        - ✅ `ReadAll`
        - ❌ `ReadAt`
        - ❌ `ReadAtLeast`
        - ✅ `ReadFrom`
        - ❌ `ReadFull`
        - ❌ `Seek`
        - ❌ `Size`
        - ❌ `TeeReader`
        - ✅ `Write`
        - ❌ `WriteAt`
        - ✅ `WriteString`
        - ❌ `WriteTo`
        - ❌ `copyBuffer`

- **File:** `src/io/io_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestNopCloserWriterToForwarding`

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
    - Predicted Functions (3):
        - ❌ `TestReadDir`
        - ❌ `TestReadFile`
        - ❌ `TestWriteFile`

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
    - Predicted Functions (3):
        - ❌ `IsExported`
        - ❌ `NewIdent`
        - ❌ `String`

- **File:** `src/go/ast/scope.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Insert`
        - ❌ `Lookup`
        - ❌ `NewObj`
        - ❌ `NewScope`
        - ❌ `Pos`
        - ❌ `String`

- **File:** `src/go/parser/parser.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `parseFile`
        - ❌ `parseIdent`
        - ❌ `parseQualifiedIdent`
        - ❌ `parseTypeName`

- **File:** `src/go/parser/resolver.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `closeScope`
        - ❌ `declare`
        - ❌ `openScope`
        - ❌ `resolve`
        - ❌ `resolveFile`

- **File:** `src/go/types/object.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `NewConst`
        - ❌ `NewField`
        - ❌ `NewFunc`
        - ❌ `NewLabel`
        - ❌ `NewParam`
        - ❌ `NewPkgName`
        - ❌ `NewTypeName`
        - ❌ `NewVar`
        - ❌ `ObjectString`
        - ❌ `String`


### 📊 **Proposal #39351 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 34.8% | 51.6% | 8/23 |

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
    - Predicted Functions (4):
        - ✅ `TestValueCompareAndSwapConcurrent`
        - ✅ `TestValueSwapConcurrent`
        - ✅ `TestValue_CompareAndSwap`
        - ✅ `TestValue_Swap`

- **File:** `test/atomicload.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #38627 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/text/template/parse/node.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `NewIdentifier`
        - ❌ `newCommand`
        - ❌ `newPipeline`

- **File:** `src/text/template/parse/parse.go`
    - Ground Truth Functions (1):
        - `term`
    - Predicted Functions (3):
        - ❌ `Parse`
        - ❌ `checkPipeline`
        - ❌ `hasFunction`


### 📊 **Proposal #41790 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 33.3% | 33.3% | 1/3 |

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
    - Predicted Functions (3):
        - ✅ `Close`
        - ❌ `closeDBLocked`
        - ❌ `finalClose`

- **File:** `src/database/sql/sql_test.go`
    - Ground Truth Functions (1):
        - `TestOpenConnector`
    - Predicted Functions (0):


### 📊 **Proposal #43724 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/internal/syscall/windows/zsyscall_windows.go`
    - Ground Truth Functions (2):
        - `GetComputerNameEx`
        - `SetFileInformationByHandle`
    - Predicted Functions (0):

- **File:** `src/os/exec/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `Command`
        - ❌ `CommandContext`
        - ❌ `LookPath`
        - ❌ `Run`
        - ❌ `Start`

- **File:** `src/os/exec/exec_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestAbsPathExec`
        - ❌ `TestCommandRelativeName`
        - ❌ `TestNoExistExecutable`
        - ❌ `TestPathRace`

- **File:** `src/os/exec/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `skipStdinCopyError`

- **File:** `src/os/exec/exec_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestChildCriticalEnv`
        - ❌ `TestNoInheritHandles`
        - ❌ `TestPipePassing`

- **File:** `src/os/exec/lp_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestLookPathNotFound`

- **File:** `src/os/exec/lp_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `LookPath`
        - ❌ `findExecutable`
        - ❌ `lookPath`

- **File:** `src/os/exec/lp_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Command`
        - ❌ `LookPath`
        - ❌ `TestCommand`
        - ❌ `TestLookPathWindows`

- **File:** `src/syscall/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Exec`
        - ❌ `ForkExec`
        - ❌ `StartProcess`
        - ❌ `forkExec`

- **File:** `src/syscall/exec_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Exec`
        - ❌ `FullPath`
        - ❌ `StartProcess`

- **File:** `src/syscall/mksyscall_windows.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):


### 📊 **Proposal #51777 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

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
    - Predicted Functions (3):
        - ❌ `AddrFrom16`
        - ❌ `IPv6Loopback`
        - ✅ `TestAddrWellKnown`


### 📊 **Proposal #37475 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.7% | 8.7% | 7.5% | 2/23 |

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
    - Ground Truth Functions (1):
        - `setBuildInfo`
    - Predicted Functions (2):
        - ❌ `load`
        - ✅ `setBuildInfo`

- **File:** `src/cmd/go/internal/modfetch/codehost/codehost.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `AllHex`
        - ❌ `Run`
        - ❌ `RunWithArgs`
        - ❌ `ShortenSHA1`
        - ❌ `run`

- **File:** `src/cmd/go/internal/modfetch/codehost/git.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `RecentTag`
        - ❌ `Stat`
        - ❌ `loadLocalTags`
        - ❌ `loadRefs`
        - ❌ `newGitRepo`
        - ❌ `runGit`
        - ❌ `stat`
        - ❌ `statLocal`

- **File:** `src/cmd/go/internal/modfetch/codehost/svn.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `svnParseStat`
        - ❌ `svnReadZip`

- **File:** `src/cmd/go/internal/modfetch/codehost/vcs.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `CheckReuse`
        - ❌ `Latest`
        - ❌ `NewRepo`
        - ❌ `Stat`
        - ❌ `fetch`
        - ❌ `newVCSRepo`
        - ❌ `statLocal`

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

- **File:** `src/cmd/go/internal/work/build.go`
    - Ground Truth Functions (1):
        - `AddBuildFlags`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `build`
        - ❌ `disableBuildID`
        - ❌ `link`

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

- **File:** `src/runtime/debug/mod.go`
    - Ground Truth Functions (1):
        - `ReadBuildInfo`
    - Predicted Functions (3):
        - ❌ `ParseBuildInfo`
        - ✅ `ReadBuildInfo`
        - ❌ `String`


### 📊 **Proposal #50101 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.8% | 13.0% | 10.5% | 3/23 |

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
    - Ground Truth Functions (3):
        - `cgoLookupCNAME`
        - `cgoLookupIP`
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
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `absDomainName`
        - ❌ `equalASCIIName`
        - ❌ `isDomainName`
        - ❌ `reverseaddr`

- **File:** `src/net/dnsclient_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/dnsclient_unix.go`
    - Ground Truth Functions (2):
        - `goLookupCNAME`
        - `goLookupIPCNAMEOrder`
    - Predicted Functions (4):
        - ✅ `goLookupCNAME`
        - ✅ `goLookupIPCNAMEOrder`
        - ❌ `lookup`
        - ❌ `tryOneName`

- **File:** `src/net/dnsclient_unix_test.go`
    - Ground Truth Functions (1):
        - `TestLongDNSNames`
    - Predicted Functions (4):
        - ❌ `TestGoLookupIPCNAMEOrderHostsAliasesDNSFilesMode`
        - ❌ `TestGoLookupIPCNAMEOrderHostsAliasesFilesDNSMode`
        - ❌ `TestGoLookupIPCNAMEOrderHostsAliasesFilesOnlyMode`
        - ❌ `testGoLookupIPCNAMEOrderHostsAliases`

- **File:** `src/net/dnsconfig.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/net/dnsconfig_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `dnsDefaultSearch`
        - ❌ `dnsReadConfig`

- **File:** `src/net/dnsconfig_unix_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestDNSDefaultSearch`
        - ❌ `TestDNSReadConfig`

- **File:** `src/net/dnsconfig_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `dnsReadConfig`

- **File:** `src/net/lookup.go`
    - Ground Truth Functions (1):
        - `parseCNAMEFromResources`
    - Predicted Functions (2):
        - ❌ `LookupCNAME`
        - ✅ `parseCNAMEFromResources`

- **File:** `src/net/lookup_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestLookupCNAME`
        - ❌ `lookupLocalhost`

- **File:** `src/net/lookup_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `lookupCNAME`

- **File:** `src/net/lookup_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `lookupCNAME`
        - ❌ `resolveCNAME`

- **File:** `src/net/lookup_windows_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `TestNSLookupCNAME`
        - ❌ `nslookupCNAME`

- **File:** `src/syscall/dll_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Syscall`
        - ❌ `Syscall12`
        - ❌ `Syscall15`
        - ❌ `Syscall18`
        - ❌ `Syscall6`
        - ❌ `Syscall9`
        - ❌ `SyscallN`

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `DnsQuery`


### 📊 **Proposal #53200 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.6% | 50.0% | 10.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/go/token/position.go`
    - Ground Truth Functions (1):
        - `RemoveFile`
    - Predicted Functions (10):
        - ❌ `AddExistingFiles`
        - ❌ `AddFile`
        - ❌ `Base`
        - ❌ `File`
        - ❌ `Iterate`
        - ❌ `NewFileSet`
        - ❌ `Position`
        - ❌ `PositionFor`
        - ✅ `RemoveFile`
        - ❌ `file`

- **File:** `src/go/token/position_test.go`
    - Ground Truth Functions (1):
        - `TestRemoveFile`
    - Predicted Functions (0):

- **File:** `src/go/token/token.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `IsExported`
        - ❌ `IsIdentifier`
        - ❌ `IsKeyword`
        - ❌ `IsLiteral`
        - ❌ `IsOperator`
        - ❌ `Lookup`
        - ❌ `Precedence`
        - ❌ `String`


### 📊 **Proposal #46308 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (1):
        - `VersionName`
    - Predicted Functions (5):
        - ✅ `VersionName`
        - ❌ `maxSupportedVersion`
        - ❌ `mutualVersion`
        - ❌ `supportedVersions`
        - ❌ `supportedVersionsFromMax`

- **File:** `src/crypto/tls/common_string.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `String`

- **File:** `src/crypto/tls/tls.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/crypto/tls/tls_test.go`
    - Ground Truth Functions (1):
        - `TestVersionName`
    - Predicted Functions (0):


### 📊 **Proposal #53002 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 80.0% | 61.5% | 69.6% | 8/13 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/http/httputil/example_test.go`
    - Ground Truth Functions (1):
        - `ExampleReverseProxy`
    - Predicted Functions (0):

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
    - Predicted Functions (6):
        - ✅ `NewSingleHostReverseProxy`
        - ✅ `SetURL`
        - ✅ `SetXForwarded`
        - ✅ `copyHeader`
        - ✅ `removeHopByHopHeaders`
        - ✅ `rewriteRequestURL`

- **File:** `src/net/http/httputil/reverseproxy_test.go`
    - Ground Truth Functions (3):
        - `TestReverseProxyRewriteReplacesOut`
        - `TestReverseProxyRewriteStripsForwarded`
        - `TestSetURL`
    - Predicted Functions (4):
        - ❌ `TestReverseProxyQueryParameterSmugglingRewrite`
        - ❌ `TestReverseProxyQueryParameterSmugglingRewritePreservesRawQuery`
        - ✅ `TestReverseProxyRewriteStripsForwarded`
        - ✅ `TestSetURL`


### 📊 **Proposal #51644 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 4/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/binary/binary.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `Append`
        - ❌ `AppendUint16`
        - ❌ `AppendUint32`
        - ❌ `AppendUint64`

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
        - ❌ `TestUvarint`
        - ❌ `TestVarint`
        - ✅ `testUvarint`
        - ✅ `testVarint`


### 📊 **Proposal #42098 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 1/1 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/syscall/exec_windows.go`
    - Ground Truth Functions (1):
        - `StartProcess`
    - Predicted Functions (1):
        - ✅ `StartProcess`

- **File:** `src/syscall/syscall_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `delete`
        - ❌ `list`
        - ❌ `makeInheritSa`
        - ❌ `newProcThreadAttributeList`
        - ❌ `update`


### 📊 **Proposal #50674 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 43.8% | 77.8% | 56.0% | 7/9 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/parser.go`
    - Ground Truth Functions (4):
        - `ParseRevocationList`
        - `parseExtension`
        - `parseTime`
        - `parseValidity`
    - Predicted Functions (3):
        - ✅ `ParseRevocationList`
        - ❌ `parseAuthorityKeyIdentifier`
        - ✅ `parseExtension`

- **File:** `src/crypto/x509/parser_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ParseASN1String`

- **File:** `src/crypto/x509/pkix/pkix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `HasExpired`

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (2):
        - `CheckSignatureFrom`
        - `ParseDERCRL`
    - Predicted Functions (6):
        - ❌ `CheckCRLSignature`
        - ✅ `CheckSignatureFrom`
        - ❌ `CreateRevocationList`
        - ❌ `ParseCRL`
        - ✅ `ParseDERCRL`
        - ❌ `ParseRevocationList`

- **File:** `src/crypto/x509/x509_test.go`
    - Ground Truth Functions (3):
        - `TestCreateRevocationList`
        - `TestParseRevocationList`
        - `TestRevocationListCheckSignatureFrom`
    - Predicted Functions (5):
        - ✅ `TestCreateRevocationList`
        - ❌ `TestParseDERCRL`
        - ❌ `TestParsePEMCRL`
        - ✅ `TestParseRevocationList`
        - ✅ `TestRevocationListCheckSignatureFrom`


### 📊 **Proposal #41682 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/18 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/x509/verify.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Verify`
        - ❌ `isValid`

- **File:** `src/crypto/x509/verify_test.go`
    - Ground Truth Functions (1):
        - `TestGoVerify`
    - Predicted Functions (2):
        - ❌ `expectHashError`
        - ❌ `testVerify`

- **File:** `src/crypto/x509/x509.go`
    - Ground Truth Functions (5):
        - `CheckSignature`
        - `CheckSignatureFrom`
        - `CreateCertificate`
        - `Error`
        - `checkSignature`
    - Predicted Functions (0):

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
    - Predicted Functions (0):


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


### 📊 **Proposal #51682 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 13.3% | 18.2% | 2/15 |

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

- **File:** `src/go/types/api_test.go`
    - Ground Truth Functions (3):
        - `TestInstantiatedObjects`
        - `TestUsesInfo`
        - `originObject`
    - Predicted Functions (0):

- **File:** `src/go/types/object.go`
    - Ground Truth Functions (2):
        - `NewFunc`
        - `Origin`
    - Predicted Functions (6):
        - ❌ `NewField`
        - ✅ `NewFunc`
        - ❌ `NewParam`
        - ❌ `NewVar`
        - ✅ `Origin`
        - ❌ `newVar`

- **File:** `src/go/types/object_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestObjectString`

- **File:** `src/go/types/sizeof_test.go`
    - Ground Truth Functions (1):
        - `TestSizeof`
    - Predicted Functions (0):

- **File:** `src/go/types/subst.go`
    - Ground Truth Functions (2):
        - `func_`
        - `replaceRecvType`
    - Predicted Functions (0):


### 📊 **Proposal #19367 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `SliceHeader`
        - ❌ `SliceOf`
        - ❌ `StringHeader`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `MakeSlice`
        - ❌ `Pointer`
        - ❌ `Slice`
        - ❌ `Slice3`
        - ❌ `UnsafePointer`
        - ❌ `unsafeslice`

- **File:** `src/runtime/checkptr.go`
    - Ground Truth Functions (2):
        - `checkptrAlignment`
        - `checkptrArithmetic`
    - Predicted Functions (0):

- **File:** `src/runtime/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `panicunsafeslicelen`
        - ❌ `panicunsafeslicelen1`
        - ❌ `panicunsafeslicenilptr`
        - ❌ `panicunsafeslicenilptr1`
        - ❌ `reflect_unsafeslice`
        - ❌ `unsafeslice`
        - ❌ `unsafeslice64`
        - ❌ `unsafeslicecheckptr`

- **File:** `src/unsafe/unsafe.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Slice`
        - ❌ `String`

- **File:** `test/unsafe_slice_data.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`

- **File:** `test/unsafe_string.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`

- **File:** `test/unsafe_string_data.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`


### 📊 **Proposal #48187 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 75.0% | 37.5% | 3/4 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/version/version.go`
    - Ground Truth Functions (3):
        - `isGoBinaryCandidate`
        - `scanDir`
        - `scanFile`
    - Predicted Functions (2):
        - ✅ `isGoBinaryCandidate`
        - ✅ `scanFile`

- **File:** `src/debug/buildinfo/buildinfo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `DataReader`
        - ❌ `DataStart`
        - ❌ `Read`
        - ❌ `ReadFile`
        - ❌ `readData`
        - ❌ `readDataInto`
        - ❌ `readRawBuildInfo`
        - ❌ `searchMagic`

- **File:** `src/debug/buildinfo/buildinfo_test.go`
    - Ground Truth Functions (1):
        - `TestReadFile`
    - Predicted Functions (2):
        - ❌ `TestNotGo`
        - ✅ `TestReadFile`


### 📊 **Proposal #41792 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.8% | 50.0% | 27.3% | 3/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/flag/flag.go`
    - Ground Truth Functions (3):
        - `Var`
        - `failf`
        - `sprintf`
    - Predicted Functions (14):
        - ❌ `Bool`
        - ❌ `BoolFunc`
        - ❌ `Duration`
        - ❌ `Float64`
        - ❌ `Func`
        - ❌ `Int`
        - ❌ `Int64`
        - ❌ `Parse`
        - ❌ `String`
        - ❌ `TextVar`
        - ❌ `Uint`
        - ❌ `Uint64`
        - ✅ `Var`
        - ❌ `parseOne`

- **File:** `src/flag/flag_test.go`
    - Ground Truth Functions (3):
        - `TestInvalidFlags`
        - `TestRedefinedFlags`
        - `mustPanic`
    - Predicted Functions (2):
        - ✅ `TestInvalidFlags`
        - ✅ `TestRedefinedFlags`


### 📊 **Proposal #46518 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 57.1% | 65.0% | 60.8% | 93/143 |

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

- **File:** `src/net/ip.go`
    - Ground Truth Functions (0):
    - Predicted Functions (22):
        - ❌ `CIDRMask`
        - ❌ `Contains`
        - ❌ `Equal`
        - ❌ `IPv4`
        - ❌ `IPv4Mask`
        - ❌ `IsGlobalUnicast`
        - ❌ `IsInterfaceLocalMulticast`
        - ❌ `IsLinkLocalMulticast`
        - ❌ `IsLinkLocalUnicast`
        - ❌ `IsLoopback`
        - ❌ `IsMulticast`
        - ❌ `IsPrivate`
        - ❌ `IsUnspecified`
        - ❌ `MarshalText`
        - ❌ `Mask`
        - ❌ `ParseCIDR`
        - ❌ `ParseIP`
        - ❌ `String`
        - ❌ `To16`
        - ❌ `To4`
        - ❌ `UnmarshalText`
        - ❌ `appendTo`

- **File:** `src/net/ip_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (11):
        - ❌ `TestCIDRMask`
        - ❌ `TestIPAddrFamily`
        - ❌ `TestIPAddrScope`
        - ❌ `TestIPNetContains`
        - ❌ `TestIPNetString`
        - ❌ `TestIPString`
        - ❌ `TestJoinHostPort`
        - ❌ `TestNetworkNumberAndMask`
        - ❌ `TestParseCIDR`
        - ❌ `TestParseIP`
        - ❌ `TestSplitHostPort`

- **File:** `src/net/lookup.go`
    - Ground Truth Functions (1):
        - `LookupNetIP`
    - Predicted Functions (0):

- **File:** `src/net/netip/export_test.go`
    - Ground Truth Functions (2):
        - `Mk128`
        - `MkAddr`
    - Predicted Functions (6):
        - ❌ `Compare`
        - ❌ `IPv4`
        - ❌ `IsZero`
        - ❌ `MakeAddrDetail`
        - ✅ `Mk128`
        - ✅ `MkAddr`

- **File:** `src/net/netip/fuzz_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `FuzzParse`
        - ❌ `checkBinaryMarshaler`
        - ❌ `checkEncoding`
        - ❌ `checkStringParseRoundTrip`
        - ❌ `checkTextMarshalMatchesAppendTo`
        - ❌ `checkTextMarshalMatchesString`
        - ❌ `checkTextMarshaler`

- **File:** `src/net/netip/inlining_test.go`
    - Ground Truth Functions (1):
        - `TestInlining`
    - Predicted Functions (1):
        - ✅ `TestInlining`

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
    - Predicted Functions (50):
        - ❌ `Addr`
        - ✅ `AddrFrom16`
        - ✅ `AddrFrom4`
        - ✅ `AddrFromSlice`
        - ❌ `AddrPortFrom`
        - ✅ `AppendTo`
        - ✅ `As16`
        - ✅ `As4`
        - ❌ `AsSlice`
        - ✅ `BitLen`
        - ❌ `Bits`
        - ✅ `Compare`
        - ✅ `Contains`
        - ❌ `IPv6LinkLocalAllNodes`
        - ❌ `IPv6Unspecified`
        - ✅ `Is4`
        - ✅ `Is4In6`
        - ✅ `Is6`
        - ✅ `IsGlobalUnicast`
        - ✅ `IsInterfaceLocalMulticast`
        - ✅ `IsLinkLocalMulticast`
        - ✅ `IsLinkLocalUnicast`
        - ✅ `IsLoopback`
        - ✅ `IsMulticast`
        - ✅ `IsPrivate`
        - ❌ `IsSingleIP`
        - ✅ `IsUnspecified`
        - ❌ `IsValid`
        - ❌ `Less`
        - ✅ `MarshalBinary`
        - ✅ `MarshalText`
        - ✅ `MustParseAddr`
        - ✅ `MustParseAddrPort`
        - ✅ `MustParsePrefix`
        - ✅ `Next`
        - ✅ `Overlaps`
        - ✅ `ParseAddr`
        - ✅ `ParseAddrPort`
        - ✅ `ParsePrefix`
        - ❌ `Port`
        - ✅ `Prefix`
        - ✅ `PrefixFrom`
        - ✅ `Prev`
        - ✅ `String`
        - ✅ `StringExpanded`
        - ✅ `Unmap`
        - ✅ `UnmarshalBinary`
        - ✅ `UnmarshalText`
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
    - Predicted Functions (8):
        - ✅ `TestAddrPortMarshalUnmarshal`
        - ✅ `TestIPBitLen`
        - ✅ `TestIPNextPrev`
        - ✅ `TestIPv6Accessor`
        - ✅ `TestParseAddrPort`
        - ✅ `TestParseIPError`
        - ✅ `TestPrefixContains`
        - ✅ `TestPrefixValid`

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
    - Predicted Functions (40):
        - ❌ `BenchmarkAddrMarshalText`
        - ✅ `BenchmarkAddrPortMarshalText`
        - ✅ `BenchmarkAddrPortString`
        - ❌ `BenchmarkAddrString`
        - ❌ `BenchmarkAs16`
        - ✅ `BenchmarkIPStringExpanded`
        - ✅ `BenchmarkParseAddr`
        - ✅ `BenchmarkParseAddrPort`
        - ✅ `BenchmarkPrefixMarshalText`
        - ❌ `TestAddrAppendText`
        - ✅ `TestAddrFrom16`
        - ❌ `TestAddrFromSlice`
        - ❌ `TestAddrLessCompare`
        - ✅ `TestAddrMarshalUnmarshal`
        - ✅ `TestAddrMarshalUnmarshalBinary`
        - ❌ `TestAddrPortCompare`
        - ❌ `TestAddrPortMarshalTextString`
        - ❌ `TestAddrPortMarshalUnmarshalBinary`
        - ❌ `TestAddrPortString`
        - ❌ `TestAddrStringAllocs`
        - ✅ `TestAddrWellKnown`
        - ❌ `TestAsSlice`
        - ✅ `TestIPProperties`
        - ✅ `TestIPStringExpanded`
        - ✅ `TestIPv4Constructors`
        - ✅ `TestIs4AndIs6`
        - ✅ `TestIs4In6`
        - ✅ `TestNoAllocs`
        - ✅ `TestParseAddr`
        - ✅ `TestParsePrefixAllocs`
        - ✅ `TestPrefix`
        - ❌ `TestPrefixCompare`
        - ✅ `TestPrefixFromInvalidBits`
        - ✅ `TestPrefixIsSingleIP`
        - ❌ `TestPrefixMarshalTextString`
        - ✅ `TestPrefixMarshalUnmarshal`
        - ❌ `TestPrefixMarshalUnmarshalBinary`
        - ✅ `TestPrefixMasking`
        - ✅ `TestPrefixOverlaps`
        - ✅ `TestPrefixString`

- **File:** `src/net/netip/slow_test.go`
    - Ground Truth Functions (4):
        - `normalizeIPv6Slow`
        - `parseIPSlow`
        - `parseIPv4Slow`
        - `parseWord`
    - Predicted Functions (4):
        - ✅ `normalizeIPv6Slow`
        - ✅ `parseIPSlow`
        - ✅ `parseIPv4Slow`
        - ✅ `parseWord`

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
    - Predicted Functions (11):
        - ✅ `addOne`
        - ✅ `and`
        - ✅ `bitsClearedFrom`
        - ✅ `bitsSetFrom`
        - ✅ `halves`
        - ❌ `isZero`
        - ✅ `mask6`
        - ✅ `not`
        - ✅ `or`
        - ✅ `subOne`
        - ✅ `xor`

- **File:** `src/net/netip/uint128_test.go`
    - Ground Truth Functions (3):
        - `TestBitsClearedFrom`
        - `TestBitsSetFrom`
        - `TestUint128AddSub`
    - Predicted Functions (3):
        - ✅ `TestBitsClearedFrom`
        - ✅ `TestBitsSetFrom`
        - ✅ `TestUint128AddSub`

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


### 📊 **Proposal #40592 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 14.3% | 19.0% | 2/14 |

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
    - Predicted Functions (3):
        - ❌ `PointerTo`
        - ❌ `PtrTo`
        - ❌ `ptrTo`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (4):
        - `Pointer`
        - `Recv`
        - `UnsafePointer`
        - `recv`
    - Predicted Functions (4):
        - ❌ `Addr`
        - ✅ `Pointer`
        - ❌ `UnsafeAddr`
        - ✅ `UnsafePointer`

- **File:** `test/fixedbugs/issue36085.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #29770 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 59.1% | 52.0% | 55.3% | 13/25 |

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
    - Predicted Functions (8):
        - ✅ `atRightDelim`
        - ✅ `hasLeftTrimMarker`
        - ✅ `hasRightTrimMarker`
        - ✅ `isSpace`
        - ✅ `lexInsideAction`
        - ✅ `lexLeftDelim`
        - ✅ `lexRightDelim`
        - ✅ `lexSpace`

- **File:** `src/text/template/parse/lex_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `TestDelims`
        - ❌ `TestDelimsAndMarkers`
        - ❌ `TestLex`
        - ❌ `parseLexer`

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
    - Predicted Functions (7):
        - ✅ `action`
        - ✅ `command`
        - ❌ `operand`
        - ❌ `parse`
        - ✅ `pipeline`
        - ✅ `term`
        - ✅ `textOrAction`

- **File:** `src/text/template/parse/parse_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `BenchmarkParseLarge`
        - ❌ `TestParse`
        - ❌ `TestParseWithComments`


### 📊 **Proposal #37112 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 36.8% | 51.9% | 43.1% | 14/27 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/work/gc.go`
    - Ground Truth Functions (1):
        - `gc`
    - Predicted Functions (0):

- **File:** `src/runtime/export_test.go`
    - Ground Truth Functions (1):
        - `ReadMetricsSlow`
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
    - Predicted Functions (6):
        - ✅ `compute`
        - ✅ `float64HistOrInit`
        - ✅ `initMetrics`
        - ❌ `readMetricNames`
        - ✅ `readMetrics`
        - ❌ `readMetricsLocked`

- **File:** `src/runtime/metrics/description.go`
    - Ground Truth Functions (1):
        - `All`
    - Predicted Functions (2):
        - ✅ `All`
        - ❌ `init`

- **File:** `src/runtime/metrics/description_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestDocs`
        - ❌ `TestNames`
        - ❌ `runtime_readMetricNames`

- **File:** `src/runtime/metrics/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `All`
        - ❌ `Float64Histogram`
        - ❌ `Kind`
        - ❌ `Read`
        - ❌ `TimeHistogram`
        - ❌ `Value`

- **File:** `src/runtime/metrics/example_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Read_readingAllMetrics`
        - ❌ `Read_readingOneMetric`
        - ❌ `medianBucket`

- **File:** `src/runtime/metrics/histogram.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

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
    - Predicted Functions (12):
        - ❌ `BenchmarkReadMetricsLatency`
        - ❌ `TestCPUMetricsSleep`
        - ❌ `TestCPUStats`
        - ❌ `TestMetricHeapUnusedLargeObjectOverflow`
        - ❌ `TestMutexWaitTimeMetric`
        - ✅ `TestReadMetrics`
        - ✅ `TestReadMetricsConsistency`
        - ❌ `TestReadMetricsCumulative`
        - ❌ `TestRuntimeLockMetricsAndProfile`
        - ❌ `TestSchedPauseMetrics`
        - ✅ `prepareAllMetricsSamples`
        - ❌ `testSchedPauseMetrics`

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


### 📊 **Proposal #45428 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 60.0% | 54.5% | 9/15 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/crypto/tls/common.go`
    - Ground Truth Functions (5):
        - `SupportsCertificate`
        - `cipherSuites`
        - `maxSupportedVersion`
        - `mutualVersion`
        - `supportedVersions`
    - Predicted Functions (4):
        - ❌ `defaultConfig`
        - ✅ `maxSupportedVersion`
        - ✅ `mutualVersion`
        - ✅ `supportedVersions`

- **File:** `src/crypto/tls/conn.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `ConnectionState`
        - ❌ `Handshake`
        - ❌ `HandshakeContext`
        - ❌ `connectionStateLocked`
        - ❌ `handshakeContext`

- **File:** `src/crypto/tls/handshake_client.go`
    - Ground Truth Functions (3):
        - `clientHandshake`
        - `makeClientHello`
        - `pickTLSVersion`
    - Predicted Functions (3):
        - ✅ `clientHandshake`
        - ✅ `makeClientHello`
        - ✅ `pickTLSVersion`

- **File:** `src/crypto/tls/handshake_server.go`
    - Ground Truth Functions (3):
        - `pickCipherSuite`
        - `processClientHello`
        - `readClientHello`
    - Predicted Functions (6):
        - ❌ `cipherSuiteOk`
        - ❌ `handshake`
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


### 📊 **Proposal #47066 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.1% | 50.0% | 12.5% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/reflect/all_test.go`
    - Ground Truth Functions (1):
        - `TestBytes`
    - Predicted Functions (0):

- **File:** `src/reflect/type.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `Addr`
        - ❌ `Bytes`
        - ❌ `Elem`
        - ❌ `Field`
        - ❌ `Interface`
        - ❌ `Len`
        - ❌ `SetBytes`
        - ❌ `Slice`

- **File:** `src/reflect/value.go`
    - Ground Truth Functions (1):
        - `Bytes`
    - Predicted Functions (6):
        - ❌ `Addr`
        - ✅ `Bytes`
        - ❌ `CanAddr`
        - ❌ `SetBytes`
        - ❌ `Slice`
        - ❌ `bytesSlow`


### 📊 **Proposal #47164 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 36.8% | 87.5% | 51.9% | 7/8 |

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
    - Predicted Functions (3):
        - ❌ `BenchmarkDiscard`
        - ✅ `TestDiscard`
        - ❌ `Write`


### 📊 **Proposal #45963 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 66.7% | 26.7% | 2/3 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/test/test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `addTestVet`
        - ❌ `runTest`

- **File:** `src/cmd/go/internal/test/testflag.go`
    - Ground Truth Functions (2):
        - `Set`
        - `String`
    - Predicted Functions (2):
        - ✅ `Set`
        - ✅ `String`

- **File:** `src/cmd/go/internal/vet/vet.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `init`
        - ❌ `runVet`

- **File:** `src/cmd/go/internal/vet/vetflag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `parseVettoolFlag`
        - ❌ `vetFlags`

- **File:** `src/cmd/go/internal/work/exec.go`
    - Ground Truth Functions (1):
        - `buildVetConfig`
    - Predicted Functions (0):

- **File:** `src/cmd/vet/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `main`

- **File:** `src/cmd/vet/vet_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestVet`
        - ❌ `errorCheck`
        - ❌ `vetCmd`


### 📊 **Proposal #48256 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 28.6% | 23.5% | 2/7 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/workcmd/edit.go`
    - Ground Truth Functions (5):
        - `allowedVersionArg`
        - `flagEditworkReplace`
        - `init`
        - `parsePathVersionOptional`
        - `runEditwork`
    - Predicted Functions (7):
        - ❌ `flagEditworkDropGodebug`
        - ❌ `flagEditworkDropReplace`
        - ❌ `flagEditworkDropUse`
        - ❌ `flagEditworkGodebug`
        - ✅ `flagEditworkReplace`
        - ❌ `flagEditworkUse`
        - ✅ `runEditwork`

- **File:** `src/cmd/go/internal/workcmd/init.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (1):
        - ❌ `runInit`

- **File:** `src/cmd/go/internal/workcmd/work.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `edit`
        - ❌ `init`

- **File:** `src/cmd/go/main.go`
    - Ground Truth Functions (1):
        - `init`
    - Predicted Functions (0):


### 📊 **Proposal #52746 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/modfetch/codehost/vcs.go`
    - Ground Truth Functions (1):
        - `fossilParseStat`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/vcs/vcs.go`
    - Ground Truth Functions (1):
        - `fossilStatus`
    - Predicted Functions (0):

- **File:** `src/time/format.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Format`
        - ❌ `Parse`
        - ❌ `ParseInLocation`

- **File:** `src/time/format_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `TestFormat`
        - ❌ `TestFormatAndParse`
        - ❌ `TestParse`


### 📊 **Proposal #49390 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 37.5% | 46.2% | 3/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/compile/internal/base/debug.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/compile/internal/base/flag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `ParseFlags`
        - ❌ `registerFlags`

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
    - Predicted Functions (1):
        - ✅ `OptimizationOff`

- **File:** `src/internal/testenv/opt.go`
    - Ground Truth Functions (1):
        - `OptimizationOff`
    - Predicted Functions (1):
        - ✅ `OptimizationOff`

- **File:** `src/internal/testenv/testenv.go`
    - Ground Truth Functions (1):
        - `SkipIfOptimizationOff`
    - Predicted Functions (1):
        - ✅ `SkipIfOptimizationOff`


### 📊 **Proposal #46485 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/6 |

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

- **File:** `src/go/ast/resolve.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `declare`
        - ❌ `resolve`

- **File:** `src/go/internal/srcimporter/srcimporter.go`
    - Ground Truth Functions (2):
        - `cgo`
        - `parseFiles`
    - Predicted Functions (0):

- **File:** `src/go/parser/parser.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `parseDecl`
        - ❌ `parseExpr`
        - ❌ `parseFile`
        - ❌ `parseFuncDecl`
        - ❌ `parseGenDecl`
        - ❌ `parseIdent`
        - ❌ `parseImportSpec`
        - ❌ `parseStmt`
        - ❌ `parseTypeSpec`
        - ❌ `parseValueSpec`

- **File:** `src/go/parser/resolver.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `declare`
        - ❌ `resolve`
        - ❌ `resolveFile`


### 📊 **Proposal #40082 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 33.3% | 23.5% | 2/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/database/sql/convert.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Scan`
        - ❌ `Value`
        - ❌ `convertAssign`

- **File:** `src/database/sql/driver/types.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `ConvertValue`
        - ❌ `IsScanValue`
        - ❌ `IsValue`
        - ❌ `callValuerValue`

- **File:** `src/database/sql/fakedb_test.go`
    - Ground Truth Functions (2):
        - `colTypeToReflectType`
        - `converterForType`
    - Predicted Functions (0):

- **File:** `src/database/sql/sql.go`
    - Ground Truth Functions (2):
        - `Scan`
        - `Value`
    - Predicted Functions (4):
        - ❌ `NullByte`
        - ❌ `NullInt16`
        - ✅ `Scan`
        - ✅ `Value`

- **File:** `src/database/sql/sql_test.go`
    - Ground Truth Functions (2):
        - `TestNullByteParam`
        - `TestNullInt16Param`
    - Predicted Functions (0):


### 📊 **Proposal #39034 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 33.3% | 22.2% | 2/6 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/time/format.go`
    - Ground Truth Functions (3):
        - `AppendFormat`
        - `GoString`
        - `quote`
    - Predicted Functions (3):
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
    - Predicted Functions (7):
        - ❌ `Date`
        - ❌ `In`
        - ❌ `Local`
        - ❌ `Location`
        - ❌ `UTC`
        - ❌ `Zone`
        - ❌ `ZoneBounds`

- **File:** `src/time/time_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `BenchmarkGoString`


### 📊 **Proposal #44435 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 50.0% | 16.7% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/modcmd/download.go`
    - Ground Truth Functions (1):
        - `runDownload`
    - Predicted Functions (2):
        - ❌ `DownloadModule`
        - ✅ `runDownload`

- **File:** `src/cmd/go/internal/modload/load.go`
    - Ground Truth Functions (0):
    - Predicted Functions (5):
        - ❌ `LoadPackages`
        - ❌ `computePatternAll`
        - ❌ `loadFromRoots`
        - ❌ `preloadRootModules`
        - ❌ `resolveMissingImports`

- **File:** `src/cmd/go/internal/modload/modfile.go`
    - Ground Truth Functions (1):
        - `pruningForGoVersion`
    - Predicted Functions (0):

- **File:** `src/cmd/go/internal/modload/query.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `Query`
        - ❌ `QueryPackages`
        - ❌ `QueryPattern`


### 📊 **Proposal #46258 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.0% | 11.1% | 6.9% | 1/9 |

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
    - Predicted Functions (1):
        - ✅ `forkAndExecInChild`

- **File:** `src/syscall/exec_pdeathsig_test.go`
    - Ground Truth Functions (2):
        - `deathSignalChild`
        - `deathSignalParent`
    - Predicted Functions (0):

- **File:** `src/syscall/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `ForkExec`
        - ❌ `StartProcess`
        - ❌ `forkExec`

- **File:** `src/syscall/syscall_freebsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `RawSyscall`
        - ❌ `RawSyscall6`
        - ❌ `Syscall`
        - ❌ `Syscall6`

- **File:** `src/syscall/syscall_freebsd_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Syscall9`

- **File:** `src/syscall/syscall_freebsd_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Syscall9`

- **File:** `src/syscall/syscall_freebsd_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Syscall9`

- **File:** `src/syscall/syscall_freebsd_test.go`
    - Ground Truth Functions (1):
        - `TestMain`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_linux_test.go`
    - Ground Truth Functions (2):
        - `TestParseNetlinkMessage`
        - `TestSyscallNoError`
    - Predicted Functions (0):

- **File:** `src/syscall/syscall_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zerrors_freebsd_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/zsyscall_freebsd_386.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Kill`
        - ❌ `procctl`

- **File:** `src/syscall/zsyscall_freebsd_amd64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `procctl`

- **File:** `src/syscall/zsyscall_freebsd_arm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Kill`
        - ❌ `procctl`

- **File:** `src/syscall/zsyscall_freebsd_arm64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `procctl`

- **File:** `src/syscall/zsyscall_freebsd_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `Kill`
        - ❌ `procctl`

- **File:** `src/syscall/zsysnum_freebsd_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/ztypes_freebsd_riscv64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


### 📊 **Proposal #51428 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 50.0% | 15.4% | 1/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/net/dial.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Dial`
        - ❌ `DialContext`
        - ❌ `DialTimeout`
        - ❌ `dialParallel`
        - ❌ `dialSerial`
        - ❌ `dialSingle`

- **File:** `src/net/error_test.go`
    - Ground Truth Functions (1):
        - `TestContextError`
    - Predicted Functions (0):

- **File:** `src/net/net.go`
    - Ground Truth Functions (1):
        - `Is`
    - Predicted Functions (5):
        - ❌ `Error`
        - ✅ `Is`
        - ❌ `Temporary`
        - ❌ `Timeout`
        - ❌ `Unwrap`


### 📊 **Proposal #44221 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 62.5% | 76.9% | 5/8 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/encoding/csv/reader.go`
    - Ground Truth Functions (4):
        - `FieldPos`
        - `nextRune`
        - `readLine`
        - `readRecord`
    - Predicted Functions (3):
        - ✅ `FieldPos`
        - ✅ `readLine`
        - ✅ `readRecord`

- **File:** `src/encoding/csv/reader_test.go`
    - Ground Truth Functions (4):
        - `TestRead`
        - `errorWithPosition`
        - `firstError`
        - `makePositions`
    - Predicted Functions (2):
        - ✅ `errorWithPosition`
        - ✅ `makePositions`


### 📊 **Proposal #46279 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/go/internal/base/limit.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `AcquireNet`
        - ❌ `NetLimit`

- **File:** `src/cmd/link/internal/ld/ld_test.go`
    - Ground Truth Functions (1):
        - `TestMemProfileCheck`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/ld/lib.go`
    - Ground Truth Functions (1):
        - `linksetup`
    - Predicted Functions (0):

- **File:** `src/internal/syscall/unix/getrandom_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/syscall/unix/getrandom_linux_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/runtime/os_linux.go`
    - Ground Truth Functions (0):
    - Predicted Functions (2):
        - ❌ `osinit`
        - ❌ `sysargs`

- **File:** `src/syscall/exec_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (6):
        - ❌ `Exec`
        - ❌ `ForkExec`
        - ❌ `StartProcess`
        - ❌ `forkExec`
        - ❌ `runtime_AfterExec`
        - ❌ `runtime_BeforeExec`

- **File:** `src/syscall/rlimit.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `Setrlimit`

- **File:** `src/syscall/rlimit_darwin.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `adjustFileLimit`

- **File:** `src/syscall/rlimit_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestOpenFileLimit`

- **File:** `src/syscall/syscall_unix.go`
    - Ground Truth Functions (0):
    - Predicted Functions (18):
        - ❌ `Getpeername`
        - ❌ `GetsockoptInt`
        - ❌ `Recvfrom`
        - ❌ `Recvmsg`
        - ❌ `Sendmsg`
        - ❌ `SendmsgN`
        - ❌ `Sendto`
        - ❌ `SetsockoptByte`
        - ❌ `SetsockoptICMPv6Filter`
        - ❌ `SetsockoptIPMreq`
        - ❌ `SetsockoptIPv6Mreq`
        - ❌ `SetsockoptInet4Addr`
        - ❌ `SetsockoptInt`
        - ❌ `SetsockoptLinger`
        - ❌ `SetsockoptString`
        - ❌ `SetsockoptTimeval`
        - ❌ `Socket`
        - ❌ `Socketpair`


### 📊 **Proposal #47257 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 8.0% | 8.2% | 2/25 |

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
    - Predicted Functions (5):
        - ❌ `goInstall`
        - ❌ `install`
        - ✅ `packagefile`
        - ✅ `runInstall`
        - ❌ `startInstall`

- **File:** `src/cmd/dist/build_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/buildgo.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `defaultCCFunc`
        - ❌ `mkzdefaultcc`
        - ❌ `writeHeader`

- **File:** `src/cmd/dist/buildruntime.go`
    - Ground Truth Functions (0):
    - Predicted Functions (3):
        - ❌ `mkbuildcfg`
        - ❌ `mkobjabi`
        - ❌ `mkzversion`

- **File:** `src/cmd/dist/buildtag.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/buildtag_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestBuildParser`

- **File:** `src/cmd/dist/buildtool.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `bootstrapBuildTools`

- **File:** `src/cmd/dist/doc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/exec.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/imports.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `readimports`

- **File:** `src/cmd/dist/main.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `xmain`

- **File:** `src/cmd/dist/notgo122.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/quoted.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/supported_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `TestSupported`

- **File:** `src/cmd/dist/sys_default.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `sysinit`

- **File:** `src/cmd/dist/sys_windows.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/test.go`
    - Ground Truth Functions (1):
        - `run`
    - Predicted Functions (3):
        - ❌ `raceDetectorSupported`
        - ❌ `registerCgoTests`
        - ❌ `registerRaceTests`

- **File:** `src/cmd/dist/testjson.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/testjson_test.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/util.go`
    - Ground Truth Functions (0):
    - Predicted Functions (4):
        - ❌ `writefile`
        - ❌ `xreaddir`
        - ❌ `xremove`
        - ❌ `xremoveall`

- **File:** `src/cmd/dist/util_gc.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/dist/util_gccgo.go`
    - Ground Truth Functions (0):
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

- **File:** `src/runtime/sys_darwin.go`
    - Ground Truth Functions (1):
        - `crypto_x509_syscall`
    - Predicted Functions (0):


### 📊 **Proposal #40995 (Function Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 52.3% | 95.9% | 67.6% | 116/121 |

##### Ground Truth vs Predicted Functions per File

- **File:** `src/cmd/dist/main.go`
    - Ground Truth Functions (1):
        - `main`
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/mips64/asm.go`
    - Ground Truth Functions (0):
    - Predicted Functions (9):
        - ❌ `adddynrel`
        - ❌ `addpltsym`
        - ❌ `archreloc`
        - ❌ `archrelocvariant`
        - ❌ `elfreloc1`
        - ❌ `elfsetupplt`
        - ❌ `extreloc`
        - ❌ `gentext`
        - ❌ `machoreloc1`

- **File:** `src/cmd/link/internal/mips64/l.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/cmd/link/internal/mips64/obj.go`
    - Ground Truth Functions (2):
        - `Init`
        - `archinit`
    - Predicted Functions (2):
        - ✅ `Init`
        - ✅ `archinit`

- **File:** `src/internal/goarch/goarch_mips64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goarch/zgoarch_mips64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/goos/zgoos_openbsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/syscall/unix/arc4random_openbsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `ARC4Random`

- **File:** `src/internal/syscall/unix/at_openbsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `Fchmodat`
        - ❌ `Fchownat`
        - ❌ `Linkat`
        - ❌ `Mkdirat`
        - ❌ `Readlinkat`
        - ❌ `Renameat`
        - ❌ `Symlinkat`

- **File:** `src/internal/syscall/unix/at_sysnum_openbsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/internal/syscall/unix/faccessat_openbsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (1):
        - ❌ `faccessat`

- **File:** `src/runtime/defs_openbsd_mips64.go`
    - Ground Truth Functions (2):
        - `setNsec`
        - `set_usec`
    - Predicted Functions (2):
        - ✅ `setNsec`
        - ✅ `set_usec`

- **File:** `src/runtime/mheap.go`
    - Ground Truth Functions (1):
        - `allocSpan`
    - Predicted Functions (0):

- **File:** `src/runtime/os_openbsd.go`
    - Ground Truth Functions (1):
        - `mpreinit`
    - Predicted Functions (0):

- **File:** `src/runtime/os_openbsd_mips64.go`
    - Ground Truth Functions (1):
        - `cputicks`
    - Predicted Functions (1):
        - ✅ `cputicks`

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

- **File:** `src/runtime/sys_openbsd.go`
    - Ground Truth Functions (0):
    - Predicted Functions (10):
        - ❌ `pthread_attr_destroy`
        - ❌ `pthread_attr_destroy_trampoline`
        - ❌ `pthread_attr_getstacksize`
        - ❌ `pthread_attr_getstacksize_trampoline`
        - ❌ `pthread_attr_init`
        - ❌ `pthread_attr_init_trampoline`
        - ❌ `pthread_attr_setdetachstate`
        - ❌ `pthread_attr_setdetachstate_trampoline`
        - ❌ `pthread_create`
        - ❌ `pthread_create_trampoline`

- **File:** `src/runtime/sys_openbsd1.go`
    - Ground Truth Functions (0):
    - Predicted Functions (7):
        - ❌ `osyield`
        - ❌ `osyield_no_g`
        - ❌ `sched_yield_trampoline`
        - ❌ `thrsleep`
        - ❌ `thrsleep_trampoline`
        - ❌ `thrwakeup`
        - ❌ `thrwakeup_trampoline`

- **File:** `src/runtime/sys_openbsd2.go`
    - Ground Truth Functions (0):
    - Predicted Functions (8):
        - ❌ `madvise`
        - ❌ `madvise_trampoline`
        - ❌ `mmap`
        - ❌ `mmap_trampoline`
        - ❌ `munmap`
        - ❌ `munmap_trampoline`
        - ❌ `sigaltstack`
        - ❌ `sigaltstack_trampoline`

- **File:** `src/runtime/sys_openbsd3.go`
    - Ground Truth Functions (0):
    - Predicted Functions (16):
        - ❌ `syscall`
        - ❌ `syscall10`
        - ❌ `syscall10X`
        - ❌ `syscall6`
        - ❌ `syscall6X`
        - ❌ `syscallX`
        - ❌ `syscall_rawSyscall`
        - ❌ `syscall_rawSyscall10X`
        - ❌ `syscall_rawSyscall6`
        - ❌ `syscall_rawSyscall6X`
        - ❌ `syscall_syscall`
        - ❌ `syscall_syscall10`
        - ❌ `syscall_syscall10X`
        - ❌ `syscall_syscall6`
        - ❌ `syscall_syscall6X`
        - ❌ `syscall_syscallX`

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
    - Predicted Functions (5):
        - ✅ `SetControllen`
        - ✅ `SetKevent`
        - ✅ `SetLen`
        - ✅ `setTimespec`
        - ✅ `setTimeval`

- **File:** `src/syscall/zerrors_openbsd_mips64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

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
    - Predicted Functions (106):
        - ✅ `Access`
        - ✅ `Adjtime`
        - ✅ `Chdir`
        - ✅ `Chflags`
        - ✅ `Chmod`
        - ✅ `Chown`
        - ✅ `Chroot`
        - ✅ `Close`
        - ✅ `Dup`
        - ✅ `Dup2`
        - ✅ `Fchdir`
        - ✅ `Fchflags`
        - ✅ `Fchmod`
        - ✅ `Fchown`
        - ✅ `Flock`
        - ✅ `Fpathconf`
        - ✅ `Fstat`
        - ✅ `Fstatfs`
        - ✅ `Fsync`
        - ✅ `Ftruncate`
        - ✅ `Getegid`
        - ✅ `Geteuid`
        - ✅ `Getgid`
        - ✅ `Getpgid`
        - ✅ `Getpgrp`
        - ✅ `Getpid`
        - ✅ `Getppid`
        - ✅ `Getpriority`
        - ✅ `Getrlimit`
        - ✅ `Getrusage`
        - ✅ `Getsid`
        - ✅ `Gettimeofday`
        - ✅ `Getuid`
        - ✅ `Issetugid`
        - ✅ `Kill`
        - ✅ `Kqueue`
        - ✅ `Lchown`
        - ✅ `Link`
        - ✅ `Listen`
        - ✅ `Lstat`
        - ✅ `Mkdir`
        - ✅ `Mkfifo`
        - ✅ `Mknod`
        - ✅ `Nanosleep`
        - ✅ `Open`
        - ✅ `Pathconf`
        - ✅ `Readlink`
        - ✅ `Rename`
        - ✅ `Revoke`
        - ✅ `Rmdir`
        - ✅ `Seek`
        - ✅ `Select`
        - ✅ `Setegid`
        - ✅ `Seteuid`
        - ✅ `Setgid`
        - ✅ `Setlogin`
        - ✅ `Setpgid`
        - ✅ `Setpriority`
        - ✅ `Setregid`
        - ✅ `Setreuid`
        - ✅ `Setsid`
        - ✅ `Settimeofday`
        - ✅ `Setuid`
        - ✅ `Shutdown`
        - ✅ `Stat`
        - ✅ `Statfs`
        - ✅ `Symlink`
        - ✅ `Sync`
        - ✅ `Truncate`
        - ✅ `Umask`
        - ✅ `Unlink`
        - ✅ `Unmount`
        - ✅ `accept`
        - ✅ `accept4`
        - ✅ `bind`
        - ✅ `connect`
        - ✅ `fcntl`
        - ✅ `futimes`
        - ✅ `getcwd`
        - ✅ `getdents`
        - ✅ `getgroups`
        - ✅ `getpeername`
        - ✅ `getsockname`
        - ✅ `getsockopt`
        - ✅ `kevent`
        - ✅ `mmap`
        - ✅ `munmap`
        - ✅ `pipe2`
        - ❌ `pread`
        - ❌ `pwrite`
        - ✅ `read`
        - ✅ `readlen`
        - ✅ `recvfrom`
        - ✅ `recvmsg`
        - ✅ `sendmsg`
        - ✅ `sendto`
        - ✅ `setgroups`
        - ❌ `setrlimit`
        - ✅ `setsockopt`
        - ✅ `socket`
        - ✅ `socketpair`
        - ✅ `sysctl`
        - ✅ `utimensat`
        - ✅ `utimes`
        - ✅ `wait4`
        - ✅ `write`

- **File:** `src/syscall/zsysnum_openbsd_mips64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):

- **File:** `src/syscall/ztypes_openbsd_mips64.go`
    - Ground Truth Functions (0):
    - Predicted Functions (0):


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
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/timeformat`
- `src/cmd/vet`

**Predicted Directories (2):**
- ✅ `src/cmd/vet`
- ❌ `src/time`


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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/netip`

**Predicted Directories (1):**
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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/hash/maphash`

**Predicted Directories (2):**
- ✅ `src/hash/maphash`
- ❌ `test`


### 📊 **Proposal #46259 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (2):**
- ✅ `src/syscall`
- ❌ `syscall`


### 📊 **Proposal #47257 (Directory Level)**

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


### 📊 **Proposal #47216 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (1):**
- ❌ `src/runtime/metrics`


### 📊 **Proposal #53747 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (1):**
- ✅ `src/flag`


### 📊 **Proposal #34626 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (1):**
- ✅ `src/testing`


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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/go/internal/generate`

**Predicted Directories (1):**
- ✅ `src/cmd/go/internal/generate`


### 📊 **Proposal #50062 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (1):**
- ✅ `src/time`


### 📊 **Proposal #46731 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 37.5% | 40.0% | 3/8 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (8):**
- `src/cmd/cgo`
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/typebits`
- `src/cmd/compile/internal/typecheck`
- `src/reflect`
- `src/runtime`
- `test`
- `test/fixedbugs`

**Predicted Directories (7):**
- ✅ `src/cmd/cgo`
- ❌ `src/cmd/compile/internal/ir`
- ✅ `src/cmd/compile/internal/typecheck`
- ❌ `src/cmd/compile/internal/types2`
- ❌ `src/runtime/cgo`
- ❌ `src/runtime/internal/sys`
- ✅ `test/fixedbugs`


### 📊 **Proposal #33184 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/time`

**Predicted Directories (1):**
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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os/signal`

**Predicted Directories (2):**
- ❌ `src/context`
- ✅ `src/os/signal`


### 📊 **Proposal #42782 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`


### 📊 **Proposal #46279 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/link/internal/ld`

**Predicted Directories (4):**
- ❌ `src/cmd/go/internal/base`
- ❌ `src/internal/syscall/unix`
- ❌ `src/runtime`
- ❌ `src/syscall`


### 📊 **Proposal #40724 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 69.2% | 20.5% | 31.6% | 9/44 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (44):**
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

**Predicted Directories (13):**
- ❌ `src/cmd/asm/internal/arch`
- ❌ `src/cmd/compile`
- ✅ `src/cmd/compile/internal/abi`
- ✅ `src/cmd/compile/internal/ir`
- ✅ `src/cmd/compile/internal/ssa`
- ✅ `src/cmd/compile/internal/ssagen`
- ❌ `src/cmd/compile/internal/types`
- ✅ `src/cmd/internal/obj`
- ✅ `src/cmd/internal/objabi`
- ✅ `src/internal/abi`
- ❌ `src/internal/goexperiment`
- ✅ `src/reflect`
- ✅ `src/runtime`


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
| 40.0% | 28.6% | 33.3% | 2/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/compile/internal/ir`
- `src/cmd/compile/internal/ssagen`
- `src/cmd/compile/internal/typecheck`
- `src/cmd/compile/internal/walk`
- `src/go/types`
- `src/unsafe`
- `test`

**Predicted Directories (5):**
- ❌ `src/builtin`
- ❌ `src/cmd/compile/internal/test/testdata`
- ❌ `src/runtime`
- ✅ `src/unsafe`
- ✅ `test`


### 📊 **Proposal #46552 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/syscall`

**Predicted Directories (4):**
- ❌ `src/internal/syscall/windows`
- ✅ `src/runtime`
- ✅ `src/syscall`
- ❌ `uintptrescapes.dir`


### 📊 **Proposal #33136 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (2):**
- ✅ `src/reflect`
- ❌ `test`


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
| 33.3% | 33.3% | 33.3% | 4/12 |

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

**Predicted Directories (12):**
- ❌ `misc/cgo/testsanitizers`
- ❌ `misc/cgo/testsanitizers/testdata`
- ❌ `src/cmd/compile/internal/asan`
- ✅ `src/cmd/compile/internal/pkginit`
- ❌ `src/cmd/compile/internal/ssa`
- ❌ `src/cmd/dist`
- ✅ `src/cmd/go/internal/work`
- ✅ `src/cmd/link/internal/ld`
- ❌ `src/internal/asan`
- ❌ `src/internal/msan`
- ✅ `src/runtime`
- ❌ `src/runtime/asan`


### 📊 **Proposal #50599 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 20.0% | 28.6% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/go/internal/vcs`
- `src/cmd/go/internal/work`
- `src/cmd/internal/moddeps`
- `src/go/build`
- `src/os/exec`

**Predicted Directories (2):**
- ✅ `src/os/exec`
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
| 44.4% | 100.0% | 61.5% | 4/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `src/cmd/dist`
- `src/cmd/link/internal/mips64`
- `src/runtime`
- `src/syscall`

**Predicted Directories (9):**
- ✅ `src/cmd/dist`
- ❌ `src/cmd/link/internal/ld`
- ✅ `src/cmd/link/internal/mips64`
- ❌ `src/internal/goarch`
- ❌ `src/internal/goos`
- ❌ `src/internal/syscall/unix`
- ✅ `src/runtime`
- ❌ `src/runtime/internal/atomic`
- ✅ `src/syscall`


### 📊 **Proposal #39034 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (1):**
- ✅ `src/time`


### 📊 **Proposal #45100 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (1):**
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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (2):**
- ✅ `src/net`
- ❌ `src/syscall`


### 📊 **Proposal #37112 (Directory Level)**

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
| 75.0% | 42.9% | 54.5% | 3/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/syntax`
- `src/cmd/compile/internal/types2`
- `src/go/internal/gcimporter`
- `src/go/parser`
- `src/go/types`
- `test/typeparam`

**Predicted Directories (4):**
- ✅ `src/cmd/compile/internal/types2`
- ✅ `src/go/types`
- ❌ `src/slices`
- ✅ `test/typeparam`


### 📊 **Proposal #46485 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `src/cmd/cgo`
- `src/cmd/go/internal/load`
- `src/cmd/gofmt`
- `src/go/internal/srcimporter`

**Predicted Directories (2):**
- ❌ `src/go/ast`
- ❌ `src/go/parser`


### 📊 **Proposal #34652 (Directory Level)**

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


### 📊 **Proposal #42098 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (2):**
- ✅ `src/syscall`
- ❌ `syscall`


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
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/embed`
- `src/embed/internal/embedtest`

**Predicted Directories (2):**
- ❌ `src/cmd/vet`
- ✅ `src/embed`


### 📊 **Proposal #51414 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (1):**
- ✅ `src/time`


### 📊 **Proposal #46258 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (1):**
- ✅ `src/syscall`


### 📊 **Proposal #51430 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 37.5% | 60.0% | 46.2% | 9/15 |

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

**Predicted Directories (24):**
- ✅ `src/cmd/compile/internal/coverage`
- ✅ `src/cmd/covdata`
- ✅ `src/cmd/covdata/testdata`
- ❌ `src/cmd/cover`
- ❌ `src/cmd/cover/testdata`
- ❌ `src/cmd/cover/testdata/html`
- ❌ `src/cmd/cover/testdata/pkgcfg/a`
- ❌ `src/internal/coverage`
- ❌ `src/internal/coverage/cfile`
- ✅ `src/internal/coverage/cformat`
- ✅ `src/internal/coverage/cmerge`
- ✅ `src/internal/coverage/decodecounter`
- ❌ `src/internal/coverage/decodemeta`
- ✅ `src/internal/coverage/encodecounter`
- ❌ `src/internal/coverage/encodemeta`
- ✅ `src/internal/coverage/pods`
- ❌ `src/internal/coverage/rtcov`
- ❌ `src/internal/coverage/slicereader`
- ❌ `src/internal/coverage/slicewriter`
- ✅ `src/internal/coverage/stringtab`
- ❌ `src/internal/coverage/uleb128`
- ❌ `src/runtime`
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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/link/internal/ld`
- `src/runtime/cgo`

**Predicted Directories (1):**
- ✅ `src/runtime/cgo`


### 📊 **Proposal #51766 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/netip`

**Predicted Directories (1):**
- ✅ `src/net/netip`


### 📊 **Proposal #51684 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/regexp/syntax`

**Predicted Directories (1):**
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
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/run`
- `src/cmd/go/internal/work`

**Predicted Directories (2):**
- ✅ `src/cmd/go/internal/run`
- ✅ `src/cmd/go/internal/work`


### 📊 **Proposal #19367 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 100.0% | 33.3% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (5):**
- ❌ `src/cmd/compile/internal/test`
- ❌ `src/reflect`
- ✅ `src/runtime`
- ❌ `src/unsafe`
- ❌ `test`


### 📊 **Proposal #37168 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 4.8% | 50.0% | 8.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/rc4`
- `src/image`

**Predicted Directories (21):**
- ❌ `src/crypto/aes`
- ❌ `src/crypto/cipher`
- ❌ `src/crypto/des`
- ❌ `src/crypto/dsa`
- ❌ `src/crypto/ecdh`
- ❌ `src/crypto/ecdsa`
- ❌ `src/crypto/ed25519`
- ❌ `src/crypto/elliptic`
- ❌ `src/crypto/hmac`
- ❌ `src/crypto/md5`
- ✅ `src/crypto/rc4`
- ❌ `src/crypto/rsa`
- ❌ `src/crypto/sha1`
- ❌ `src/crypto/sha256`
- ❌ `src/crypto/sha512`
- ❌ `src/crypto/subtle`
- ❌ `src/crypto/tls`
- ❌ `src/crypto/x509`
- ❌ `src/hash/crc32`
- ❌ `src/math/big`
- ❌ `src/math/big/internal/asmgen`


### 📊 **Proposal #29062 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 33.3% | 28.6% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/test`
- `src/cmd/objdump`
- `src/internal/testenv`

**Predicted Directories (4):**
- ✅ `src/cmd/go/internal/test`
- ❌ `src/os/exec`
- ❌ `src/os/exec/internal/fdtest`
- ❌ `src/testing`


### 📊 **Proposal #43823 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (1):**
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

**Predicted Directories (3):**
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/test`
- ❌ `src/testing`


### 📊 **Proposal #46131 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`


### 📊 **Proposal #51225 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 33.3% | 33.3% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/compile/internal/base`
- `src/cmd/compile/internal/noder`
- `src/cmd/go/internal/work`

**Predicted Directories (3):**
- ❌ `src/cmd/compile`
- ✅ `src/cmd/compile/internal/base`
- ❌ `src/cmd/compile/internal/gc`


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
- ❌ `src/cmd/doc`
- ❌ `src/go/doc`
- ❌ `test`


### 📊 **Proposal #37776 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/url`

**Predicted Directories (1):**
- ✅ `src/net/url`


### 📊 **Proposal #40357 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/list`
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modload`

**Predicted Directories (1):**
- ✅ `src/cmd/go/internal/modload`


### 📊 **Proposal #39557 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (1):**
- ✅ `src/flag`


### 📊 **Proposal #53003 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/types2`
- `src/go/types`

**Predicted Directories (5):**
- ❌ `src/builtin`
- ❌ `src/reflect`
- ❌ `src/runtime`
- ❌ `src/unsafe`
- ❌ `test`


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
- ❌ `src/cmd/vet/testdata/tagtest`
- ✅ `src/reflect`


### 📊 **Proposal #41563 (Directory Level)**

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
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/dist`
- `src/os/exec`

**Predicted Directories (2):**
- ✅ `src/os/exec`
- ❌ `src/syscall`


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
- ✅ `src/sync/atomic`
- ❌ `test`


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
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/syscall/windows`
- `src/syscall`

**Predicted Directories (2):**
- ❌ `src/os/exec`
- ✅ `src/syscall`


### 📊 **Proposal #41730 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 20.0% | 25.0% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/go`
- `src/cmd/go/internal/envcmd`
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modget`
- `src/cmd/go/internal/vcs`

**Predicted Directories (3):**
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ✅ `src/cmd/go/internal/vcs`
- ❌ `src/cmd/go/internal/vcweb`


### 📊 **Proposal #51668 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/fmt`

**Predicted Directories (1):**
- ✅ `src/fmt`


### 📊 **Proposal #41792 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (1):**
- ✅ `src/flag`


### 📊 **Proposal #45453 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 14.3% | 15.4% | 1/7 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (7):**
- `src/cmd/compile/internal/amd64`
- `src/cmd/compile/internal/ssa`
- `src/cmd/dist`
- `src/cmd/go/internal/cfg`
- `src/cmd/go/internal/work`
- `src/internal/buildcfg`
- `test/codegen`

**Predicted Directories (6):**
- ✅ `src/cmd/compile/internal/amd64`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/cmd/internal/sys`
- ❌ `src/cmd/link/internal/amd64`
- ❌ `src/internal/cpu`
- ❌ `src/vendor/golang.org/x/sys/cpu`


### 📊 **Proposal #40276 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/work`

**Predicted Directories (5):**
- ❌ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modget`
- ✅ `src/cmd/go/internal/modload`
- ✅ `src/cmd/go/internal/work`
- ❌ `src/cmd/go/internal/workcmd`


### 📊 **Proposal #42322 (Directory Level)**

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


### 📊 **Proposal #42100 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 25.0% | 25.0% | 1/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `misc/ios`
- `src/cmd/dist`
- `src/cmd/go/internal/work`
- `src/cmd/link/internal/ld`

**Predicted Directories (4):**
- ✅ `misc/ios`
- ❌ `src/internal/goos`
- ❌ `src/runtime/cgo`
- ❌ `src/syscall`


### 📊 **Proposal #37475 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 50.0% | 54.5% | 3/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/cmd/go`
- `src/cmd/go/internal/load`
- `src/cmd/go/internal/vcs`
- `src/cmd/go/internal/work`
- `src/debug/buildinfo`
- `src/runtime/debug`

**Predicted Directories (5):**
- ✅ `src/cmd/go/internal/load`
- ❌ `src/cmd/go/internal/modfetch`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ✅ `src/cmd/go/internal/work`
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
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/image`
- `src/image/draw`

**Predicted Directories (3):**
- ✅ `src/image`
- ❌ `src/image/color`
- ✅ `src/image/draw`


### 📊 **Proposal #45754 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (1):**
- ✅ `src/flag`


### 📊 **Proposal #47651 (Directory Level)**

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


### 📊 **Proposal #48052 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/debug/plan9obj`

**Predicted Directories (1):**
- ✅ `src/debug/plan9obj`


### 📊 **Proposal #33920 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/io/ioutil`
- `src/os`

**Predicted Directories (1):**
- ✅ `src/io/ioutil`


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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/tls`
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`


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
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/test`
- `src/cmd/go/internal/work`

**Predicted Directories (4):**
- ❌ `src/cmd/go`
- ✅ `src/cmd/go/internal/test`
- ❌ `src/cmd/go/internal/vet`
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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (2):**
- ❌ `src/crypto/dsa`
- ✅ `src/crypto/x509`


### 📊 **Proposal #45973 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/net/http`


### 📊 **Proposal #49471 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (2):**
- ✅ `src/runtime`
- ❌ `src/syscall`


### 📊 **Proposal #52746 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/modfetch/codehost`
- `src/cmd/go/internal/vcs`

**Predicted Directories (1):**
- ❌ `src/time`


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
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/runtime`
- `src/time`

**Predicted Directories (1):**
- ❌ `src/testing`


### 📊 **Proposal #47916 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/compile/internal/noder`
- `src/cmd/compile/internal/types2`
- `src/go/types`

**Predicted Directories (1):**
- ✅ `src/go/types`


### 📊 **Proposal #40356 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods`

**Predicted Directories (2):**
- ❌ `src/cmd/vet`
- ❌ `src/errors`


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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (1):**
- ✅ `src/time`


### 📊 **Proposal #50465 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http/httputil`

**Predicted Directories (1):**
- ✅ `src/net/http/httputil`


### 📊 **Proposal #41696 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 20.0% | 33.3% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/dist`
- `src/cmd/go`
- `src/cmd/go/internal/test`
- `src/cmd/go/internal/work`
- `src/cmd/link`

**Predicted Directories (1):**
- ✅ `src/cmd/go/internal/work`


### 📊 **Proposal #44011 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 100.0% | 85.7% | 3/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/os`
- `src/os/exec`
- `src/syscall`

**Predicted Directories (4):**
- ❌ `src/internal/syscall/windows`
- ✅ `src/os`
- ✅ `src/os/exec`
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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go`
- `src/cmd/go/internal/workcmd`

**Predicted Directories (1):**
- ✅ `src/cmd/go/internal/workcmd`


### 📊 **Proposal #38017 (Directory Level)**

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


### 📊 **Proposal #50601 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/binary`

**Predicted Directories (1):**
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
| 33.3% | 4.3% | 7.7% | 1/23 |

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
- ✅ `src/cmd/vet`
- ❌ `src/fmt`
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
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/cipher`
- `src/crypto/subtle`

**Predicted Directories (2):**
- ✅ `src/crypto/cipher`
- ✅ `src/crypto/subtle`


### 📊 **Proposal #49580 (Directory Level)**

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


### 📊 **Proposal #41048 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/net/http`


### 📊 **Proposal #48409 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/runtime`
- `src/runtime/debug`
- `src/runtime/testdata/testprog`

**Predicted Directories (2):**
- ✅ `src/runtime`
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


### 📊 **Proposal #27628 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/go/internal/cache`
- `src/cmd/go/internal/work`

**Predicted Directories (1):**
- ✅ `src/cmd/go/internal/work`


### 📊 **Proposal #51868 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/debug/pe`

**Predicted Directories (1):**
- ✅ `src/debug/pe`


### 📊 **Proposal #28089 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/ast`

**Predicted Directories (1):**
- ✅ `src/go/ast`


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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (2):**
- ✅ `src/crypto/x509`
- ❌ `src/crypto/x509/pkix`


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
| 25.0% | 100.0% | 40.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/syscall`

**Predicted Directories (4):**
- ❌ `src/internal/poll`
- ❌ `src/runtime`
- ❌ `src/runtime/internal/atomic`
- ✅ `src/syscall`


### 📊 **Proposal #39444 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os`

**Predicted Directories (1):**
- ✅ `src/os`


### 📊 **Proposal #45430 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`


### 📊 **Proposal #37533 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/flag`

**Predicted Directories (1):**
- ✅ `src/flag`


### 📊 **Proposal #47781 (Directory Level)**

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


### 📊 **Proposal #46057 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/x509`

**Predicted Directories (1):**
- ✅ `src/crypto/x509`


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
| 100.0% | 33.3% | 50.0% | 2/6 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (6):**
- `src/cmd/go/internal/base`
- `src/cmd/go/internal/fmtcmd`
- `src/cmd/go/internal/modcmd`
- `src/cmd/go/internal/modget`
- `src/cmd/go/internal/modload`
- `src/cmd/go/internal/work`

**Predicted Directories (2):**
- ✅ `src/cmd/go/internal/modcmd`
- ✅ `src/cmd/go/internal/modload`


### 📊 **Proposal #43993 (Directory Level)**

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


### 📊 **Proposal #50770 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/time`

**Predicted Directories (1):**
- ✅ `src/time`


### 📊 **Proposal #44221 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/csv`

**Predicted Directories (1):**
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
| 16.7% | 33.3% | 22.2% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/compile/internal/staticdata`
- `src/embed/internal/embedtest`
- `src/go/types`

**Predicted Directories (6):**
- ❌ `src/cmd/compile/internal/types2`
- ❌ `src/go/internal/gcimporter`
- ❌ `src/go/internal/gcimporter/testdata`
- ❌ `src/go/internal/types/errors`
- ✅ `src/go/types`
- ❌ `src/go/types/testdata`


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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (1):**
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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (1):**
- ✅ `src/io`


### 📊 **Proposal #40255 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 11.1% | 18.2% | 1/9 |

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

**Predicted Directories (2):**
- ✅ `src/cmd/compile/internal/ssa`
- ❌ `test/fixedbugs`


### 📊 **Proposal #46648 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/types`

**Predicted Directories (2):**
- ❌ `src/cmd/compile/internal/types2`
- ✅ `src/go/types`


### 📊 **Proposal #53346 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/xml`

**Predicted Directories (1):**
- ✅ `src/encoding/xml`


### 📊 **Proposal #51082 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 4.7% | 8.5% | 3/64 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (64):**
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
- ❌ `src/cmd`
- ✅ `src/cmd/doc`
- ❌ `src/cmd/gofmt`
- ❌ `src/go`
- ✅ `src/go/doc`
- ❌ `src/go/doc/comment`
- ✅ `src/go/printer`


### 📊 **Proposal #35833 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 33.3% | 50.0% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/crypto/elliptic`
- `src/crypto/rsa`
- `src/math/big`

**Predicted Directories (1):**
- ✅ `src/math/big`


### 📊 **Proposal #42387 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io/fs`

**Predicted Directories (1):**
- ✅ `src/io/fs`


### 📊 **Proposal #45454 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 66.7% | 50.0% | 2/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/go/internal/cfg`
- `src/go/build`
- `src/internal/buildcfg`

**Predicted Directories (5):**
- ❌ `src/cmd/go/internal/base`
- ✅ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/go/internal/work`
- ✅ `src/go/build`
- ❌ `src/go/build/constraint`


### 📊 **Proposal #50436 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/os/exec`

**Predicted Directories (1):**
- ✅ `src/os/exec`


### 📊 **Proposal #44167 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/runtime`

**Predicted Directories (2):**
- ✅ `src/runtime`
- ❌ `test`


### 📊 **Proposal #39178 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net`

**Predicted Directories (1):**
- ✅ `src/net`


### 📊 **Proposal #46287 (Directory Level)**

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


### 📊 **Proposal #48257 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/cmd/go/internal/workcmd`

**Predicted Directories (1):**
- ✅ `src/cmd/go/internal/workcmd`


### 📊 **Proposal #46293 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/reflect`

**Predicted Directories (1):**
- ✅ `src/reflect`


### 📊 **Proposal #42026 (Directory Level)**

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


### 📊 **Proposal #45435 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/sync`

**Predicted Directories (1):**
- ✅ `src/sync`


### 📊 **Proposal #48187 (Directory Level)**

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


### 📊 **Proposal #37519 (Directory Level)**

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


### 📊 **Proposal #38627 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/text/template/parse`

**Predicted Directories (1):**
- ✅ `src/text/template/parse`


### 📊 **Proposal #41260 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing`

**Predicted Directories (1):**
- ✅ `src/testing`


### 📊 **Proposal #44505 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/asm/internal/lex`
- `src/cmd/dist`

**Predicted Directories (1):**
- ✅ `src/cmd/dist`


### 📊 **Proposal #50429 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/go/parser`

**Predicted Directories (4):**
- ❌ `ken`
- ❌ `src/go/ast`
- ❌ `src/go/token`
- ❌ `test`


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

**Predicted Directories (5):**
- ❌ `src/cmd/compile/internal/base`
- ❌ `src/cmd/go/internal/base`
- ❌ `src/cmd/go/internal/cfg`
- ❌ `src/cmd/internal/objabi`
- ❌ `src/internal/goexperiment`


### 📊 **Proposal #40592 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/encoding/json`
- `src/reflect`

**Predicted Directories (2):**
- ✅ `src/reflect`
- ❌ `test/fixedbugs`


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
| 50.0% | 20.0% | 28.6% | 1/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/go/internal/cfg`
- `src/cmd/go/internal/clean`
- `src/cmd/go/internal/envcmd`
- `src/cmd/go/internal/modfetch`
- `src/cmd/go/internal/modfetch/codehost`

**Predicted Directories (2):**
- ❌ `src/cmd/go/internal/cache`
- ✅ `src/cmd/go/internal/modfetch`


### 📊 **Proposal #45628 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/encoding/xml`

**Predicted Directories (1):**
- ✅ `src/encoding/xml`


### 📊 **Proposal #46746 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (1):**
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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/crypto/tls`

**Predicted Directories (1):**
- ✅ `src/crypto/tls`


### 📊 **Proposal #41184 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 72.7% | 50.0% | 59.3% | 8/16 |

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

**Predicted Directories (11):**
- ✅ `src/cmd/asm/internal/asm`
- ❌ `src/cmd/compile/internal/syntax`
- ✅ `src/cmd/fix`
- ❌ `src/cmd/go`
- ✅ `src/cmd/go/internal/load`
- ✅ `src/cmd/go/internal/work`
- ✅ `src/cmd/vet`
- ❌ `src/cmd/vet/testdata/buildtag`
- ✅ `src/go/build`
- ✅ `src/go/build/constraint`
- ✅ `src/go/printer`


### 📊 **Proposal #48866 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/mime`

**Predicted Directories (1):**
- ✅ `src/mime`


### 📊 **Proposal #50332 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 27.3% | 42.9% | 3/11 |

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

**Predicted Directories (3):**
- ✅ `src/cmd/go`
- ✅ `src/cmd/go/internal/base`
- ✅ `src/cmd/go/internal/work`


### 📊 **Proposal #53466 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 60.0% | 42.9% | 3/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/dist`
- `src/cmd/link/internal/ld`
- `src/cmd/link/internal/riscv64`
- `src/runtime`
- `src/syscall`

**Predicted Directories (9):**
- ❌ `src/cmd/asm/internal/arch`
- ❌ `src/cmd/compile/internal/riscv64`
- ✅ `src/cmd/link/internal/ld`
- ❌ `src/internal/abi`
- ❌ `src/internal/cpu`
- ❌ `src/internal/goarch`
- ✅ `src/runtime`
- ✅ `src/syscall`
- ❌ `src/vendor/golang.org/x/sys/unix`


### 📊 **Proposal #49390 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/dist`
- `src/internal/testenv`

**Predicted Directories (2):**
- ❌ `src/cmd/compile/internal/base`
- ✅ `src/internal/testenv`


### 📊 **Proposal #39351 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/expvar`
- `src/sync/atomic`

**Predicted Directories (2):**
- ✅ `src/sync/atomic`
- ❌ `test`


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
| 40.0% | 40.0% | 40.0% | 2/5 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (5):**
- `src/cmd/compile/internal/typecheck`
- `src/cmd/compile/internal/walk`
- `src/runtime`
- `src/runtime/testdata/testprog`
- `test`

**Predicted Directories (5):**
- ❌ `src/cmd/compile/internal/test/testdata`
- ❌ `src/cmd/compile/internal/types2`
- ✅ `src/runtime`
- ❌ `src/unsafe`
- ✅ `test`


### 📊 **Proposal #46505 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/crypto/sha256`
- `src/crypto/sha512`

**Predicted Directories (1):**
- ❌ `test/fixedbugs`


### 📊 **Proposal #52376 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/reflect`

**Predicted Directories (2):**
- ✅ `src/reflect`
- ❌ `test`


### 📊 **Proposal #44815 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/bufio`

**Predicted Directories (1):**
- ✅ `src/bufio`


### 📊 **Proposal #45033 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 100.0% | 25.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/strconv`

**Predicted Directories (7):**
- ❌ `fmt`
- ❌ `reflect`
- ❌ `src/fmt`
- ❌ `src/reflect`
- ✅ `src/strconv`
- ❌ `src/text/template/parse`
- ❌ `text/template/parse`


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
| 9.1% | 33.3% | 14.3% | 1/3 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (3):**
- `src/cmd/dist`
- `src/cmd/go/internal/imports`
- `src/go/build`

**Predicted Directories (11):**
- ❌ `src/cmd/cgo/internal/test`
- ❌ `src/cmd/go`
- ❌ `src/cmd/go/internal/base`
- ✅ `src/go/build`
- ❌ `src/mime`
- ❌ `src/net`
- ❌ `src/os`
- ❌ `src/path/filepath`
- ❌ `src/runtime`
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
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/testing/iotest`

**Predicted Directories (1):**
- ✅ `src/testing/iotest`


### 📊 **Proposal #36771 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/strconv`

**Predicted Directories (2):**
- ❌ `src/fmt`
- ✅ `src/strconv`


### 📊 **Proposal #44435 (Directory Level)**

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


### 📊 **Proposal #50101 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/internal/syscall/unix`
- `src/net`

**Predicted Directories (2):**
- ✅ `src/net`
- ❌ `src/syscall`


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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/io`
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/io`


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
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/types2`
- `src/go/types`

**Predicted Directories (1):**
- ✅ `src/go/types`


### 📊 **Proposal #39214 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 25.0% | 40.0% | 2/8 |

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

**Predicted Directories (2):**
- ✅ `src/internal/cpu`
- ✅ `src/testing`


### 📊 **Proposal #30715 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/net/http`

**Predicted Directories (1):**
- ✅ `src/net/http`


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
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/sync`

**Predicted Directories (3):**
- ❌ `src/runtime`
- ✅ `src/sync`
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


### 📊 **Proposal #45899 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (1):**
- `src/io`

**Predicted Directories (1):**
- ✅ `src/io`


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
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (2):**
- `src/cmd/compile/internal/test`
- `src/unicode/utf8`

**Predicted Directories (3):**
- ❌ `src/runtime`
- ✅ `src/unicode/utf8`
- ❌ `test`


### 📊 **Proposal #38776 (Directory Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 37.5% | 75.0% | 50.0% | 3/4 |

##### Ground Truth vs Predicted Directories

**Ground Truth Directories (4):**
- `src/crypto/internal/boring`
- `src/crypto/sha1`
- `src/crypto/sha256`
- `src/crypto/sha512`

**Predicted Directories (8):**
- ✅ `src/crypto/sha1`
- ✅ `src/crypto/sha256`
- ✅ `src/crypto/sha512`
- ❌ `src/hash/adler32`
- ❌ `src/hash/crc32`
- ❌ `src/hash/crc64`
- ❌ `src/hash/fnv`
- ❌ `src/hash/maphash`


### 📊 **Proposal #45428 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 75.0% | 50.0% | 60.0% | 3/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/crypto/tls/handshake_server_test.go`
- `src/crypto/tls/handshake_server_tls13.go`
- `src/crypto/tls/handshake_test.go`

**Predicted Files (4):**
- ✅ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/conn.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ✅ `src/crypto/tls/handshake_server.go`


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
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/time/format.go`
- ❌ `src/time/format_test.go`


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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/netip/netip_test.go`

**Predicted Files (2):**
- ❌ `src/net/netip/netip.go`
- ✅ `src/net/netip/netip_test.go`


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
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/hash/maphash/maphash.go`
- `src/hash/maphash/maphash_test.go`

**Predicted Files (5):**
- ✅ `src/hash/maphash/maphash.go`
- ❌ `src/hash/maphash/maphash_purego.go`
- ❌ `src/hash/maphash/maphash_runtime.go`
- ✅ `src/hash/maphash/maphash_test.go`
- ❌ `test/escape_hash_maphash.go`


### 📊 **Proposal #46259 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/syscall/exec_freebsd.go`
- `src/syscall/exec_freebsd_test.go`

**Predicted Files (5):**
- ❌ `src/syscall/exec_bsd.go`
- ✅ `src/syscall/exec_freebsd.go`
- ✅ `src/syscall/exec_freebsd_test.go`
- ❌ `src/syscall/syscall_freebsd.go`
- ❌ `syscall/exec_bsd.go`


### 📊 **Proposal #47257 (File Level)**

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
- ❌ `src/cmd/dist/buildtool.go`
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
- ❌ `src/cmd/dist/util.go`
- ❌ `src/cmd/dist/util_gc.go`
- ❌ `src/cmd/dist/util_gccgo.go`


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

**Predicted Files (7):**
- ❌ `src/runtime/metrics/description.go`
- ❌ `src/runtime/metrics/description_test.go`
- ❌ `src/runtime/metrics/doc.go`
- ❌ `src/runtime/metrics/example_test.go`
- ❌ `src/runtime/metrics/histogram.go`
- ❌ `src/runtime/metrics/sample.go`
- ❌ `src/runtime/metrics/value.go`


### 📊 **Proposal #53747 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/flag/example_func_test.go`
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (2):**
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`


### 📊 **Proposal #34626 (File Level)**

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
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/cmd/go/internal/generate/generate.go`

**Predicted Files (2):**
- ✅ `src/cmd/go/internal/generate/generate.go`
- ❌ `src/cmd/go/internal/generate/generate_test.go`


### 📊 **Proposal #50062 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/time.go`
- `src/time/time_test.go`

**Predicted Files (2):**
- ✅ `src/time/time.go`
- ❌ `src/time/zoneinfo.go`


### 📊 **Proposal #46731 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 5.3% | 6.2% | 5.7% | 1/16 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (16):**
- `src/cmd/cgo/gcc.go`
- `src/cmd/cgo/out.go`
- `src/cmd/compile/internal/noder/noder.go`
- `src/cmd/compile/internal/noder/reader.go`
- `src/cmd/compile/internal/noder/writer.go`
- `src/cmd/compile/internal/typebits/typebits.go`
- `src/cmd/compile/internal/typecheck/func.go`
- `src/reflect/all_test.go`
- `src/reflect/deepequal.go`
- `src/reflect/nih_test.go`
- `src/reflect/value.go`
- `src/runtime/debuglog.go`
- `src/runtime/mcheckmark.go`
- `src/runtime/mheap.go`
- `test/directive.go`
- `test/fixedbugs/issue40954.go`

**Predicted Files (19):**
- ❌ `src/cmd/cgo/ast.go`
- ❌ `src/cmd/cgo/main.go`
- ✅ `src/cmd/cgo/out.go`
- ❌ `src/cmd/compile/internal/ir/type.go`
- ❌ `src/cmd/compile/internal/typecheck/type.go`
- ❌ `src/cmd/compile/internal/typecheck/typecheck.go`
- ❌ `src/cmd/compile/internal/types2/api.go`
- ❌ `src/cmd/compile/internal/types2/api_test.go`
- ❌ `src/cmd/compile/internal/types2/object.go`
- ❌ `src/cmd/compile/internal/types2/object_test.go`
- ❌ `src/cmd/compile/internal/types2/type.go`
- ❌ `src/cmd/compile/internal/types2/type_test.go`
- ❌ `src/cmd/compile/internal/types2/types.go`
- ❌ `src/runtime/cgo/cgo.go`
- ❌ `src/runtime/internal/sys/nih.go`
- ❌ `src/runtime/internal/sys/sys.go`
- ❌ `test/fixedbugs/notinheap.go`
- ❌ `test/fixedbugs/notinheap2.go`
- ❌ `test/fixedbugs/notinheap3.go`


### 📊 **Proposal #33184 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/time.go`
- `src/time/tick.go`
- `src/time/tick_test.go`

**Predicted Files (2):**
- ✅ `src/time/tick.go`
- ✅ `src/time/tick_test.go`


### 📊 **Proposal #50489 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/math/big/ratconv.go`
- `src/math/big/ratconv_test.go`

**Predicted Files (2):**
- ❌ `src/math/big/rat.go`
- ❌ `src/math/big/rat_test.go`


### 📊 **Proposal #47342 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 75.0% | 66.7% | 3/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/cmd/dist/test.go`
- `src/hash/maphash/maphash.go`
- `src/hash/maphash/maphash_purego.go`
- `src/hash/maphash/maphash_runtime.go`

**Predicted Files (5):**
- ❌ `escape_hash_maphash.go`
- ✅ `src/hash/maphash/maphash.go`
- ✅ `src/hash/maphash/maphash_purego.go`
- ✅ `src/hash/maphash/maphash_runtime.go`
- ❌ `src/hash/maphash/maphash_test.go`


### 📊 **Proposal #37255 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 66.7% | 57.1% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/os/signal/example_unix_test.go`
- `src/os/signal/signal.go`
- `src/os/signal/signal_test.go`

**Predicted Files (4):**
- ❌ `src/context/context.go`
- ❌ `src/os/signal/doc.go`
- ✅ `src/os/signal/signal.go`
- ✅ `src/os/signal/signal_test.go`


### 📊 **Proposal #42782 (File Level)**

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


### 📊 **Proposal #46279 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/link/internal/ld/ld_test.go`
- `src/cmd/link/internal/ld/lib.go`

**Predicted Files (14):**
- ❌ `src/cmd/go/internal/base/limit.go`
- ❌ `src/internal/syscall/unix/getrandom_linux.go`
- ❌ `src/internal/syscall/unix/getrandom_linux_test.go`
- ❌ `src/internal/syscall/unix/syscall_linux.go`
- ❌ `src/internal/syscall/unix/syscall_linux_test.go`
- ❌ `src/runtime/os_linux.go`
- ❌ `src/runtime/rlimit_js.go`
- ❌ `src/runtime/rlimit_unix.go`
- ❌ `src/runtime/sys_unix.go`
- ❌ `src/syscall/exec_unix.go`
- ❌ `src/syscall/rlimit.go`
- ❌ `src/syscall/rlimit_darwin.go`
- ❌ `src/syscall/rlimit_test.go`
- ❌ `src/syscall/syscall_unix.go`


### 📊 **Proposal #40724 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 24.1% | 4.7% | 7.9% | 7/148 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (148):**
- `src/cmd/asm/internal/asm/asm.go`
- `src/cmd/asm/internal/asm/endtoend_test.go`
- `src/cmd/asm/internal/asm/expr_test.go`
- `src/cmd/asm/internal/asm/operand_test.go`
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

**Predicted Files (29):**
- ❌ `src/cmd/asm/internal/arch/arch.go`
- ❌ `src/cmd/compile/internal-abi.md`
- ❌ `src/cmd/compile/internal/abi/abi.go`
- ✅ `src/cmd/compile/internal/abi/abiutils.go`
- ❌ `src/cmd/compile/internal/ir/abi.go`
- ❌ `src/cmd/compile/internal/ssa/abiutils.go`
- ✅ `src/cmd/compile/internal/ssa/expand_calls.go`
- ✅ `src/cmd/compile/internal/ssagen/abi.go`
- ❌ `src/cmd/compile/internal/types/abi.go`
- ❌ `src/cmd/internal/obj/abi_string.go`
- ❌ `src/cmd/internal/objabi/abi.go`
- ✅ `src/internal/abi/abi.go`
- ❌ `src/internal/abi/abi_amd64.go`
- ❌ `src/internal/abi/abi_arm64.go`
- ❌ `src/internal/abi/abi_generic.go`
- ❌ `src/internal/abi/abi_loong64.go`
- ❌ `src/internal/abi/abi_ppc64x.go`
- ❌ `src/internal/abi/abi_riscv64.go`
- ✅ `src/internal/abi/abi_test.go`
- ❌ `src/internal/goexperiment/exp_regabiargs_off.go`
- ❌ `src/internal/goexperiment/exp_regabiargs_on.go`
- ❌ `src/internal/goexperiment/exp_regabiwrappers_off.go`
- ❌ `src/internal/goexperiment/exp_regabiwrappers_on.go`
- ✅ `src/reflect/abi.go`
- ✅ `src/reflect/abi_test.go`
- ❌ `src/runtime/abi.go`
- ❌ `src/runtime/abi_test.go`
- ❌ `src/runtime/wincallback.go`
- ❌ `src/runtime/zcallback_windows.go`


### 📊 **Proposal #51914 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/httputil/reverseproxy.go`
- `src/net/http/httputil/reverseproxy_test.go`

**Predicted Files (4):**
- ✅ `src/net/http/httputil/reverseproxy.go`
- ✅ `src/net/http/httputil/reverseproxy_test.go`
- ❌ `src/net/http/response.go`
- ❌ `src/net/http/server.go`


### 📊 **Proposal #40481 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 16.7% | 20.0% | 2/12 |

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

**Predicted Files (8):**
- ❌ `src/builtin/builtin.go`
- ❌ `src/cmd/compile/internal/test/testdata/unsafe_test.go`
- ❌ `src/runtime/unsafe.go`
- ✅ `src/unsafe/unsafe.go`
- ❌ `test/unsafe_slice_data.go`
- ❌ `test/unsafe_string.go`
- ❌ `test/unsafe_string_data.go`
- ✅ `test/unsafebuiltins.go`


### 📊 **Proposal #46552 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 100.0% | 40.0% | 3/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/syscall_windows.go`
- `src/runtime/syscall_windows_test.go`
- `src/syscall/dll_windows.go`

**Predicted Files (12):**
- ❌ `src/internal/syscall/windows/syscall_windows.go`
- ❌ `src/internal/syscall/windows/zsyscall_windows.go`
- ✅ `src/runtime/syscall_windows.go`
- ✅ `src/runtime/syscall_windows_test.go`
- ✅ `src/syscall/dll_windows.go`
- ❌ `src/syscall/syscall_windows.go`
- ❌ `src/syscall/zsyscall_windows.go`
- ❌ `uintptrescapes.dir/a.go`
- ❌ `uintptrescapes.dir/main.go`
- ❌ `uintptrescapes.go`
- ❌ `uintptrescapes2.go`
- ❌ `uintptrescapes3.go`


### 📊 **Proposal #33136 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (3):**
- ❌ `src/reflect/type.go`
- ✅ `src/reflect/value.go`
- ❌ `test/clear.go`


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
| 8.8% | 9.7% | 9.2% | 3/31 |

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

**Predicted Files (34):**
- ❌ `misc/cgo/testsanitizers/asan_test.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan1_fail.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan2_fail.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan3_fail.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan4_fail.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan5_fail.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan_global1_fail.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan_global2_fail.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan_global3_fail.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan_global4_fail.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan_global5.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan_unsafe_fail1.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan_unsafe_fail2.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan_unsafe_fail3.go`
- ❌ `misc/cgo/testsanitizers/testdata/asan_useAfterReturn.go`
- ❌ `src/cmd/compile/internal/asan/asan.go`
- ✅ `src/cmd/compile/internal/pkginit/initAsanGlobals.go`
- ❌ `src/cmd/compile/internal/ssa/compile.go`
- ❌ `src/cmd/dist/test.go`
- ❌ `src/cmd/go/internal/work/asan.go`
- ✅ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/link/internal/ld/asan.go`
- ❌ `src/cmd/link/internal/ld/ld.go`
- ❌ `src/internal/asan/asan.go`
- ❌ `src/internal/asan/doc.go`
- ❌ `src/internal/asan/noasan.go`
- ❌ `src/internal/msan/doc.go`
- ❌ `src/internal/msan/msan.go`
- ❌ `src/internal/msan/nomsan.go`
- ❌ `src/runtime/asan/asan.go`
- ❌ `src/runtime/asan0.go`
- ✅ `src/runtime/malloc.go`
- ❌ `src/runtime/msan.go`
- ❌ `src/runtime/msan0.go`


### 📊 **Proposal #50599 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.5% | 16.7% | 12.9% | 2/12 |

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

**Predicted Files (19):**
- ✅ `src/os/exec/exec.go`
- ✅ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/exec_unix.go`
- ❌ `src/os/exec/exec_windows.go`
- ❌ `src/syscall/exec_aix_test.go`
- ❌ `src/syscall/exec_bsd.go`
- ❌ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/exec_freebsd_test.go`
- ❌ `src/syscall/exec_libc.go`
- ❌ `src/syscall/exec_libc2.go`
- ❌ `src/syscall/exec_linux.go`
- ❌ `src/syscall/exec_linux_test.go`
- ❌ `src/syscall/exec_pdeathsig_test.go`
- ❌ `src/syscall/exec_plan9.go`
- ❌ `src/syscall/exec_solaris_test.go`
- ❌ `src/syscall/exec_unix.go`
- ❌ `src/syscall/exec_unix_test.go`
- ❌ `src/syscall/exec_windows.go`
- ❌ `src/syscall/exec_windows_test.go`


### 📊 **Proposal #42537 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 37.5% | 4.1% | 7.3% | 3/74 |

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

**Predicted Files (8):**
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/proxy_test.go`
- ✅ `src/mime/mediatype.go`
- ✅ `src/strings/strings.go`
- ✅ `src/strings/strings_test.go`
- ❌ `src/testing/benchmark.go`
- ❌ `src/testing/fstest/mapfs.go`
- ❌ `test/run.go`


### 📊 **Proposal #40995 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 22.2% | 54.5% | 31.6% | 6/11 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (11):**
- `src/cmd/dist/main.go`
- `src/cmd/link/internal/mips64/obj.go`
- `src/runtime/defs_openbsd_mips64.go`
- `src/runtime/mheap.go`
- `src/runtime/os_openbsd.go`
- `src/runtime/os_openbsd_mips64.go`
- `src/runtime/signal_openbsd_mips64.go`
- `src/syscall/exec_bsd.go`
- `src/syscall/exec_unix_test.go`
- `src/syscall/syscall_openbsd_mips64.go`
- `src/syscall/zsyscall_openbsd_mips64.go`

**Predicted Files (27):**
- ❌ `src/cmd/dist/dist.go`
- ❌ `src/cmd/link/internal/ld/arch_mips64.go`
- ❌ `src/cmd/link/internal/mips64/asm.go`
- ❌ `src/cmd/link/internal/mips64/l.go`
- ✅ `src/cmd/link/internal/mips64/obj.go`
- ❌ `src/internal/goarch/goarch_mips64.go`
- ❌ `src/internal/goarch/zgoarch_mips64.go`
- ❌ `src/internal/goos/zgoos_openbsd.go`
- ❌ `src/internal/syscall/unix/arc4random_openbsd.go`
- ❌ `src/internal/syscall/unix/at_openbsd.go`
- ❌ `src/internal/syscall/unix/at_sysnum_openbsd.go`
- ❌ `src/internal/syscall/unix/faccessat_openbsd.go`
- ❌ `src/internal/syscall/unix/nofollow_openbsd.go`
- ❌ `src/internal/syscall/unix/syscall_openbsd_mips64.go`
- ✅ `src/runtime/defs_openbsd_mips64.go`
- ❌ `src/runtime/internal/atomic/atomic_mips64x.go`
- ✅ `src/runtime/os_openbsd_mips64.go`
- ✅ `src/runtime/signal_openbsd_mips64.go`
- ❌ `src/runtime/sys_openbsd.go`
- ❌ `src/runtime/sys_openbsd1.go`
- ❌ `src/runtime/sys_openbsd2.go`
- ❌ `src/runtime/sys_openbsd3.go`
- ✅ `src/syscall/syscall_openbsd_mips64.go`
- ❌ `src/syscall/zerrors_openbsd_mips64.go`
- ✅ `src/syscall/zsyscall_openbsd_mips64.go`
- ❌ `src/syscall/zsysnum_openbsd_mips64.go`
- ❌ `src/syscall/ztypes_openbsd_mips64.go`


### 📊 **Proposal #39034 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/format.go`
- `src/time/format_test.go`

**Predicted Files (4):**
- ✅ `src/time/format.go`
- ✅ `src/time/format_test.go`
- ❌ `src/time/time.go`
- ❌ `src/time/time_test.go`


### 📊 **Proposal #45100 (File Level)**

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
| 24.0% | 100.0% | 38.7% | 6/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/net/interface_aix.go`
- `src/net/interface_bsd.go`
- `src/net/interface_linux.go`
- `src/net/interface_plan9.go`
- `src/net/interface_solaris.go`
- `src/net/interface_windows.go`

**Predicted Files (25):**
- ❌ `src/net/interface.go`
- ✅ `src/net/interface_aix.go`
- ✅ `src/net/interface_bsd.go`
- ❌ `src/net/interface_bsd_test.go`
- ❌ `src/net/interface_bsdvar.go`
- ❌ `src/net/interface_darwin.go`
- ❌ `src/net/interface_freebsd.go`
- ✅ `src/net/interface_linux.go`
- ❌ `src/net/interface_linux_test.go`
- ✅ `src/net/interface_plan9.go`
- ✅ `src/net/interface_solaris.go`
- ❌ `src/net/interface_stub.go`
- ❌ `src/net/interface_test.go`
- ❌ `src/net/interface_unix_test.go`
- ✅ `src/net/interface_windows.go`
- ❌ `src/syscall/zerrors_aix_ppc64.go`
- ❌ `src/syscall/zerrors_freebsd_386.go`
- ❌ `src/syscall/zerrors_freebsd_amd64.go`
- ❌ `src/syscall/zerrors_freebsd_arm.go`
- ❌ `src/syscall/zerrors_freebsd_arm64.go`
- ❌ `src/syscall/zerrors_linux_amd64.go`
- ❌ `src/syscall/zerrors_linux_riscv64.go`
- ❌ `src/syscall/zerrors_linux_s390x.go`
- ❌ `src/syscall/zerrors_netbsd_386.go`
- ❌ `src/syscall/zerrors_openbsd_arm64.go`


### 📊 **Proposal #37112 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 55.6% | 50.0% | 52.6% | 5/10 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (10):**
- `src/cmd/go/internal/work/gc.go`
- `src/runtime/export_test.go`
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


### 📊 **Proposal #46771 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/mime/multipart/writer.go`
- `src/mime/multipart/writer_test.go`

**Predicted Files (2):**
- ✅ `src/mime/multipart/writer.go`
- ✅ `src/mime/multipart/writer_test.go`


### 📊 **Proposal #48424 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 15.8% | 25.0% | 3/19 |

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

**Predicted Files (5):**
- ✅ `src/cmd/compile/internal/types2/typeparam.go`
- ✅ `src/go/types/typeparam.go`
- ❌ `src/slices/slices.go`
- ❌ `src/slices/slices_test.go`
- ✅ `test/typeparam/issue48424.go`


### 📊 **Proposal #46485 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/cgo/ast.go`
- `src/cmd/go/internal/load/test.go`
- `src/cmd/gofmt/gofmt.go`
- `src/cmd/gofmt/simplify.go`
- `src/go/internal/srcimporter/srcimporter.go`

**Predicted Files (3):**
- ❌ `src/go/ast/resolve.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/resolver.go`


### 📊 **Proposal #34652 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 20.0% | 25.0% | 1/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/html/template/escape.go`
- `src/html/template/template_test.go`
- `src/text/template/exec.go`
- `src/text/template/parse/parse.go`
- `src/text/template/parse/parse_test.go`

**Predicted Files (3):**
- ❌ `src/text/template/parse/lex.go`
- ❌ `src/text/template/parse/node.go`
- ✅ `src/text/template/parse/parse.go`


### 📊 **Proposal #42098 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/syscall/exec_windows.go`

**Predicted Files (3):**
- ✅ `src/syscall/exec_windows.go`
- ❌ `src/syscall/syscall_windows.go`
- ❌ `syscall/exec_windows.go`


### 📊 **Proposal #35998 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/web/file_test.go`
- `src/io/ioutil/tempfile_test.go`
- `src/testing/testing.go`

**Predicted Files (2):**
- ✅ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`


### 📊 **Proposal #43698 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/embed/embed.go`
- `src/embed/internal/embedtest/embed_test.go`

**Predicted Files (4):**
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/vet_test.go`
- ✅ `src/embed/embed.go`
- ❌ `src/embed/example_test.go`


### 📊 **Proposal #51414 (File Level)**

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


### 📊 **Proposal #46258 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 6.2% | 25.0% | 10.0% | 1/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/syscall/exec_freebsd.go`
- `src/syscall/exec_pdeathsig_test.go`
- `src/syscall/syscall_freebsd_test.go`
- `src/syscall/syscall_linux_test.go`

**Predicted Files (16):**
- ❌ `src/syscall/exec_bsd.go`
- ✅ `src/syscall/exec_freebsd.go`
- ❌ `src/syscall/exec_unix.go`
- ❌ `src/syscall/syscall_freebsd.go`
- ❌ `src/syscall/syscall_freebsd_amd64.go`
- ❌ `src/syscall/syscall_freebsd_arm64.go`
- ❌ `src/syscall/syscall_freebsd_riscv64.go`
- ❌ `src/syscall/syscall_unix.go`
- ❌ `src/syscall/zerrors_freebsd_riscv64.go`
- ❌ `src/syscall/zsyscall_freebsd_386.go`
- ❌ `src/syscall/zsyscall_freebsd_amd64.go`
- ❌ `src/syscall/zsyscall_freebsd_arm.go`
- ❌ `src/syscall/zsyscall_freebsd_arm64.go`
- ❌ `src/syscall/zsyscall_freebsd_riscv64.go`
- ❌ `src/syscall/zsysnum_freebsd_riscv64.go`
- ❌ `src/syscall/ztypes_freebsd_riscv64.go`


### 📊 **Proposal #51430 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 26.3% | 34.5% | 29.9% | 10/29 |

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

**Predicted Files (38):**
- ✅ `src/cmd/compile/internal/coverage/cover.go`
- ✅ `src/cmd/covdata/covdata.go`
- ❌ `src/cmd/covdata/doc.go`
- ✅ `src/cmd/covdata/testdata/prog1.go`
- ✅ `src/cmd/covdata/testdata/prog2.go`
- ❌ `src/cmd/cover/cover.go`
- ❌ `src/cmd/cover/doc.go`
- ❌ `src/cmd/cover/profile.go`
- ❌ `src/cmd/cover/testdata/html/html.go`
- ❌ `src/cmd/cover/testdata/html/html_test.go`
- ❌ `src/cmd/cover/testdata/main.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/a/a.go`
- ❌ `src/cmd/cover/testdata/pkgcfg/a/a_test.go`
- ❌ `src/cmd/cover/testdata/test.go`
- ❌ `src/internal/coverage/cfile/apis.go`
- ❌ `src/internal/coverage/cfile/emit.go`
- ❌ `src/internal/coverage/cfile/hooks.go`
- ✅ `src/internal/coverage/cformat/format.go`
- ✅ `src/internal/coverage/cmerge/merge.go`
- ✅ `src/internal/coverage/decodecounter/decodecounterfile.go`
- ❌ `src/internal/coverage/decodemeta/decode.go`
- ❌ `src/internal/coverage/decodemeta/decodefile.go`
- ❌ `src/internal/coverage/defs.go`
- ✅ `src/internal/coverage/encodecounter/encode.go`
- ❌ `src/internal/coverage/encodemeta/encode.go`
- ❌ `src/internal/coverage/encodemeta/encodefile.go`
- ❌ `src/internal/coverage/pkid.go`
- ✅ `src/internal/coverage/pods/pods.go`
- ❌ `src/internal/coverage/rtcov/rtcov.go`
- ❌ `src/internal/coverage/slicereader/slicereader.go`
- ❌ `src/internal/coverage/slicewriter/slicewriter.go`
- ✅ `src/internal/coverage/stringtab/stringtab.go`
- ❌ `src/internal/coverage/uleb128/uleb128.go`
- ❌ `src/runtime/coverage/coverage.go`
- ❌ `src/runtime/covercounter.go`
- ❌ `src/runtime/covermeta.go`
- ❌ `src/testing/cover.go`
- ❌ `src/testing/newcover.go`


### 📊 **Proposal #46308 (File Level)**

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


### 📊 **Proposal #37033 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/link/internal/ld/lib.go`
- `src/runtime/cgo/handle.go`

**Predicted Files (2):**
- ✅ `src/runtime/cgo/handle.go`
- ❌ `src/runtime/cgo/handle_test.go`


### 📊 **Proposal #51766 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/netip/netip_test.go`

**Predicted Files (2):**
- ❌ `src/net/netip/netip.go`
- ✅ `src/net/netip/netip_test.go`


### 📊 **Proposal #51684 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/regexp/syntax/parse.go`

**Predicted Files (2):**
- ✅ `src/regexp/syntax/parse.go`
- ❌ `src/regexp/syntax/parse_test.go`


### 📊 **Proposal #51896 (File Level)**

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


### 📊 **Proposal #42088 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/run/run.go`
- `src/cmd/go/internal/work/build.go`

**Predicted Files (3):**
- ✅ `src/cmd/go/internal/run/run.go`
- ✅ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/exec.go`


### 📊 **Proposal #19367 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/runtime/checkptr.go`

**Predicted Files (8):**
- ❌ `src/cmd/compile/internal/test/unsafe_test.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`
- ❌ `src/runtime/unsafe.go`
- ❌ `src/unsafe/unsafe.go`
- ❌ `test/unsafe_slice_data.go`
- ❌ `test/unsafe_string.go`
- ❌ `test/unsafe_string_data.go`


### 📊 **Proposal #37168 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 2.6% | 66.7% | 5.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/rc4/rc4.go`
- `src/crypto/rc4/rc4_test.go`
- `src/image/image_test.go`

**Predicted Files (77):**
- ❌ `src/crypto/aes/aes.go`
- ❌ `src/crypto/aes/aes_test.go`
- ❌ `src/crypto/aes/gcm_amd64.s`
- ❌ `src/crypto/cipher/cipher.go`
- ❌ `src/crypto/cipher/gcm.go`
- ❌ `src/crypto/cipher/gcm_test.go`
- ❌ `src/crypto/des/block.go`
- ❌ `src/crypto/des/cipher.go`
- ❌ `src/crypto/des/des_test.go`
- ❌ `src/crypto/dsa/dsa.go`
- ❌ `src/crypto/dsa/dsa_test.go`
- ❌ `src/crypto/ecdh/ecdh.go`
- ❌ `src/crypto/ecdh/ecdh_test.go`
- ❌ `src/crypto/ecdsa/ecdsa.go`
- ❌ `src/crypto/ecdsa/ecdsa_test.go`
- ❌ `src/crypto/ed25519/ed25519.go`
- ❌ `src/crypto/ed25519/ed25519_test.go`
- ❌ `src/crypto/elliptic/elliptic.go`
- ❌ `src/crypto/elliptic/elliptic_test.go`
- ❌ `src/crypto/elliptic/p256_asm_amd64.s`
- ❌ `src/crypto/hmac/hmac.go`
- ❌ `src/crypto/hmac/hmac_test.go`
- ❌ `src/crypto/md5/md5.go`
- ❌ `src/crypto/md5/md5_test.go`
- ✅ `src/crypto/rc4/rc4.go`
- ✅ `src/crypto/rc4/rc4_test.go`
- ❌ `src/crypto/rsa/rsa.go`
- ❌ `src/crypto/rsa/rsa_test.go`
- ❌ `src/crypto/sha1/sha1.go`
- ❌ `src/crypto/sha1/sha1_test.go`
- ❌ `src/crypto/sha256/sha256.go`
- ❌ `src/crypto/sha256/sha256_test.go`
- ❌ `src/crypto/sha512/sha512.go`
- ❌ `src/crypto/sha512/sha512_test.go`
- ❌ `src/crypto/subtle/constant_time.go`
- ❌ `src/crypto/subtle/constant_time_test.go`
- ❌ `src/crypto/tls/tls.go`
- ❌ `src/crypto/tls/tls_test.go`
- ❌ `src/crypto/x509/x509.go`
- ❌ `src/crypto/x509/x509_test.go`
- ❌ `src/hash/crc32/crc32_amd64.go`
- ❌ `src/hash/crc32/crc32_arm64.go`
- ❌ `src/hash/crc32/crc32_generic.go`
- ❌ `src/hash/crc32/crc32_loong64.go`
- ❌ `src/hash/crc32/crc32_otherarch.go`
- ❌ `src/hash/crc32/crc32_ppc64le.go`
- ❌ `src/hash/crc32/crc32_s390x.go`
- ❌ `src/math/big/arith.go`
- ❌ `src/math/big/arith_amd64.go`
- ❌ `src/math/big/arith_amd64_test.go`
- ❌ `src/math/big/arith_decl.go`
- ❌ `src/math/big/arith_decl_pure.go`
- ❌ `src/math/big/arith_s390x_test.go`
- ❌ `src/math/big/arith_test.go`
- ❌ `src/math/big/arithvec_s390x.go`
- ❌ `src/math/big/big.go`
- ❌ `src/math/big/big_test.go`
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


### 📊 **Proposal #29062 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 3.1% | 33.3% | 5.7% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/test/test.go`
- `src/cmd/objdump/objdump_test.go`
- `src/internal/testenv/testenv.go`

**Predicted Files (32):**
- ✅ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/go/internal/test/testflag.go`
- ❌ `src/os/exec/bench_test.go`
- ❌ `src/os/exec/dot_test.go`
- ❌ `src/os/exec/env_test.go`
- ❌ `src/os/exec/example_test.go`
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_linux_test.go`
- ❌ `src/os/exec/exec_other_test.go`
- ❌ `src/os/exec/exec_plan9.go`
- ❌ `src/os/exec/exec_posix_test.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/exec_unix.go`
- ❌ `src/os/exec/exec_unix_test.go`
- ❌ `src/os/exec/exec_windows.go`
- ❌ `src/os/exec/exec_windows_test.go`
- ❌ `src/os/exec/internal/fdtest/exists_plan9.go`
- ❌ `src/os/exec/internal/fdtest/exists_test.go`
- ❌ `src/os/exec/internal/fdtest/exists_unix.go`
- ❌ `src/os/exec/internal/fdtest/exists_windows.go`
- ❌ `src/os/exec/internal_test.go`
- ❌ `src/os/exec/lp_linux_test.go`
- ❌ `src/os/exec/lp_plan9.go`
- ❌ `src/os/exec/lp_test.go`
- ❌ `src/os/exec/lp_unix.go`
- ❌ `src/os/exec/lp_unix_test.go`
- ❌ `src/os/exec/lp_wasm.go`
- ❌ `src/os/exec/lp_windows.go`
- ❌ `src/os/exec/lp_windows_test.go`
- ❌ `src/os/exec/read3.go`
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`


### 📊 **Proposal #43823 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/time/format.go`

**Predicted Files (2):**
- ✅ `src/time/format.go`
- ❌ `src/time/format_test.go`


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

**Predicted Files (5):**
- ❌ `src/cmd/go/internal/test/test.go`
- ❌ `src/cmd/go/internal/test/testflag.go`
- ❌ `src/cmd/go/test.go`
- ❌ `src/testing/testing.go`
- ❌ `src/testing/testing_test.go`


### 📊 **Proposal #46131 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/reflect/all_test.go`

**Predicted Files (8):**
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`
- ❌ `src/reflect/map_noswiss.go`
- ❌ `src/reflect/map_noswiss_test.go`
- ❌ `src/reflect/map_swiss.go`
- ❌ `src/reflect/map_swiss_test.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`


### 📊 **Proposal #51225 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 33.3% | 28.6% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/base/flag.go`
- `src/cmd/compile/internal/noder/import.go`
- `src/cmd/go/internal/work/gc.go`

**Predicted Files (4):**
- ❌ `src/cmd/compile/doc.go`
- ✅ `src/cmd/compile/internal/base/flag.go`
- ❌ `src/cmd/compile/internal/gc/main.go`
- ❌ `src/cmd/compile/main.go`


### 📊 **Proposal #40025 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 18.2% | 26.7% | 2/11 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (11):**
- `src/io/example_test.go`
- `src/io/io.go`
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

**Predicted Files (5):**
- ❌ `src/cmd/doc/main.go`
- ❌ `src/go/doc/doc.go`
- ❌ `src/go/doc/doc_test.go`
- ❌ `test/directive.go`
- ❌ `test/directive2.go`


### 📊 **Proposal #37776 (File Level)**

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


### 📊 **Proposal #40357 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 20.0% | 25.0% | 1/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/go/internal/list/list.go`
- `src/cmd/go/internal/modcmd/download.go`
- `src/cmd/go/internal/modcmd/why.go`
- `src/cmd/go/internal/modload/build.go`
- `src/cmd/go/internal/modload/list.go`

**Predicted Files (3):**
- ✅ `src/cmd/go/internal/modload/list.go`
- ❌ `src/cmd/go/internal/modload/modfile.go`
- ❌ `src/cmd/go/internal/modload/query.go`


### 📊 **Proposal #39557 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/flag/example_func_test.go`
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (2):**
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`


### 📊 **Proposal #53003 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/compile/internal/types2/builtins.go`
- `src/go/types/builtins.go`

**Predicted Files (8):**
- ❌ `src/builtin/builtin.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`
- ❌ `src/runtime/unsafe.go`
- ❌ `src/unsafe/unsafe.go`
- ❌ `test/unsafe_slice_data.go`
- ❌ `test/unsafe_string.go`
- ❌ `test/unsafe_string_data.go`


### 📊 **Proposal #40281 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 50.0% | 25.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/structtag/structtag.go`
- `src/reflect/type.go`

**Predicted Files (6):**
- ❌ `src/cmd/vet/testdata/structtag/structtag.go`
- ❌ `src/cmd/vet/testdata/tagtest/file1.go`
- ❌ `src/cmd/vet/testdata/tagtest/file2.go`
- ✅ `src/reflect/type.go`
- ❌ `src/reflect/type_test.go`
- ❌ `src/reflect/value.go`


### 📊 **Proposal #41563 (File Level)**

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


### 📊 **Proposal #46121 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 100.0% | 50.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/html/template/template.go`

**Predicted Files (3):**
- ✅ `src/html/template/template.go`
- ❌ `src/text/template/funcs.go`
- ❌ `src/text/template/template.go`


### 📊 **Proposal #43947 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 37.5% | 40.0% | 3/8 |

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
- ✅ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_windows.go`
- ✅ `src/os/exec/lp_unix.go`
- ✅ `src/os/exec/lp_windows.go`
- ❌ `src/os/exec/lp_windows_test.go`
- ❌ `src/syscall/exec_windows.go`
- ❌ `src/syscall/syscall_windows.go`


### 📊 **Proposal #50860 (File Level)**

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
- ✅ `src/sync/atomic/atomic_test.go`
- ❌ `src/sync/atomic/doc.go`
- ❌ `src/sync/atomic/doc_32.go`
- ❌ `src/sync/atomic/doc_64.go`
- ❌ `src/sync/atomic/example_test.go`
- ✅ `src/sync/atomic/type.go`
- ❌ `src/sync/atomic/value.go`
- ❌ `src/sync/atomic/value_test.go`
- ❌ `test/atomicload.go`
- ❌ `test/escape_runtime_atomic.go`
- ❌ `test/escape_sync_atomic.go`


### 📊 **Proposal #52444 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (2):**
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

**Predicted Files (9):**
- ❌ `src/os/exec/exec.go`
- ❌ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/exec_windows.go`
- ❌ `src/os/exec/exec_windows_test.go`
- ❌ `src/os/exec/lp_test.go`
- ❌ `src/os/exec/lp_windows.go`
- ❌ `src/os/exec/lp_windows_test.go`
- ❌ `src/syscall/exec_unix.go`
- ❌ `src/syscall/exec_windows.go`


### 📊 **Proposal #41730 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 9.1% | 14.3% | 11.1% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/envcmd/env.go`
- `src/cmd/go/internal/modfetch/proxy.go`
- `src/cmd/go/internal/modget/get.go`
- `src/cmd/go/internal/vcs/vcs.go`
- `src/cmd/go/internal/vcs/vcs_test.go`
- `src/cmd/go/main.go`

**Predicted Files (11):**
- ❌ `src/cmd/go/internal/modfetch/codehost/codehost.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/git.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/svn.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ✅ `src/cmd/go/internal/vcs/vcs.go`
- ❌ `src/cmd/go/internal/vcweb/bzr.go`
- ❌ `src/cmd/go/internal/vcweb/fossil.go`
- ❌ `src/cmd/go/internal/vcweb/git.go`
- ❌ `src/cmd/go/internal/vcweb/hg.go`
- ❌ `src/cmd/go/internal/vcweb/svn.go`
- ❌ `src/cmd/go/internal/vcweb/vcweb.go`


### 📊 **Proposal #51668 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/fmt/print.go`
- `src/fmt/state_test.go`

**Predicted Files (3):**
- ❌ `src/fmt/format.go`
- ✅ `src/fmt/print.go`
- ✅ `src/fmt/state_test.go`


### 📊 **Proposal #41792 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (2):**
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`


### 📊 **Proposal #45453 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 15.4% | 16.7% | 16.0% | 2/12 |

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
- ❌ `src/cmd/compile/internal/amd64/galign.go`
- ❌ `src/cmd/compile/internal/amd64/ggen.go`
- ✅ `src/cmd/compile/internal/amd64/ssa.go`
- ✅ `src/cmd/compile/internal/amd64/versions_test.go`
- ❌ `src/cmd/internal/objabi/head.go`
- ❌ `src/cmd/internal/sys/arch.go`
- ❌ `src/cmd/link/internal/amd64/asm.go`
- ❌ `src/cmd/link/internal/amd64/l.go`
- ❌ `src/cmd/link/internal/amd64/obj.go`
- ❌ `src/internal/cpu/cpu.go`
- ❌ `src/internal/cpu/cpu_x86.go`
- ❌ `src/internal/cpu/cpu_x86_test.go`
- ❌ `src/vendor/golang.org/x/sys/cpu/cpu_x86.go`


### 📊 **Proposal #40276 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 50.0% | 18.2% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modload/init.go`
- `src/cmd/go/internal/work/build.go`

**Predicted Files (9):**
- ❌ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modget/get.go`
- ❌ `src/cmd/go/internal/modload/query.go`
- ✅ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`
- ❌ `src/cmd/go/internal/work/security.go`
- ❌ `src/cmd/go/internal/workcmd/work.go`


### 📊 **Proposal #42322 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 28.6% | 36.4% | 2/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/embed/internal/embedtest/embed_test.go`
- `src/io/fs/readdir_test.go`
- `src/io/fs/readfile_test.go`
- `src/io/fs/sub.go`
- `src/io/fs/sub_test.go`
- `src/testing/fstest/mapfs.go`
- `src/testing/fstest/testfs.go`

**Predicted Files (4):**
- ❌ `src/io/fs/fs.go`
- ✅ `src/io/fs/sub.go`
- ✅ `src/io/fs/sub_test.go`
- ❌ `src/net/http/fs.go`


### 📊 **Proposal #42100 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 10.0% | 20.0% | 13.3% | 1/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `misc/ios/go_ios_exec.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/cmd/go/internal/work/init.go`
- `src/cmd/link/internal/ld/config.go`

**Predicted Files (10):**
- ❌ `misc/ios/detect.go`
- ✅ `misc/ios/go_ios_exec.go`
- ❌ `src/internal/goos/goos.go`
- ❌ `src/internal/goos/zgoos_ios.go`
- ❌ `src/runtime/cgo/signal_ios_arm64.go`
- ❌ `src/syscall/syscall_darwin.go`
- ❌ `src/syscall/syscall_darwin_amd64.go`
- ❌ `src/syscall/zerrors_darwin_amd64.go`
- ❌ `src/syscall/zsyscall_darwin_amd64.go`
- ❌ `src/syscall/ztypes_darwin_amd64.go`


### 📊 **Proposal #37475 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 22.2% | 21.1% | 2/9 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (9):**
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/load/flag.go`
- `src/cmd/go/internal/load/pkg.go`
- `src/cmd/go/internal/vcs/vcs.go`
- `src/cmd/go/internal/vcs/vcs_test.go`
- `src/cmd/go/internal/work/build.go`
- `src/debug/buildinfo/buildinfo.go`
- `src/debug/buildinfo/buildinfo_test.go`
- `src/runtime/debug/mod.go`

**Predicted Files (10):**
- ✅ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/modfetch/codehost`
- ❌ `src/cmd/go/internal/modfetch/codehost/`
- ❌ `src/cmd/go/internal/modfetch/codehost/codehost.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/git.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/svn.go`
- ❌ `src/cmd/go/internal/modfetch/codehost/vcs.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/runtime/debug/buildinfo.go`
- ✅ `src/runtime/debug/mod.go`


### 📊 **Proposal #39567 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/serve_test.go`
- `src/net/http/server.go`

**Predicted Files (2):**
- ✅ `src/net/http/server.go`
- ❌ `src/net/http/server_test.go`


### 📊 **Proposal #44808 (File Level)**

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


### 📊 **Proposal #45754 (File Level)**

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


### 📊 **Proposal #47651 (File Level)**

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


### 📊 **Proposal #48052 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/debug/plan9obj/file.go`

**Predicted Files (2):**
- ✅ `src/debug/plan9obj/file.go`
- ❌ `src/debug/plan9obj/plan9obj.go`


### 📊 **Proposal #33920 (File Level)**

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


### 📊 **Proposal #47209 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/cmd/go/internal/fsys/fsys_test.go`
- `src/io/fs/walk.go`
- `src/path/filepath/path.go`
- `src/path/filepath/path_test.go`

**Predicted Files (8):**
- ✅ `src/path/filepath/path.go`
- ❌ `src/path/filepath/path_plan9.go`
- ✅ `src/path/filepath/path_test.go`
- ❌ `src/path/filepath/path_unix.go`
- ❌ `src/path/filepath/path_windows.go`
- ❌ `src/path/filepath/symlink.go`
- ❌ `src/path/filepath/symlink_unix.go`
- ❌ `src/path/filepath/symlink_windows.go`


### 📊 **Proposal #48152 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 28.6% | 50.0% | 36.4% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/crypto/tls/common.go`
- `src/crypto/tls/handshake_client.go`
- `src/crypto/tls/handshake_server.go`
- `src/net/http/transport_test.go`

**Predicted Files (7):**
- ❌ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/conn_test.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ❌ `src/crypto/tls/handshake_client_test.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ❌ `src/crypto/tls/handshake_server_test.go`
- ❌ `src/crypto/tls/handshake_test.go`


### 📊 **Proposal #41682 (File Level)**

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


### 📊 **Proposal #53200 (File Level)**

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


### 📊 **Proposal #40082 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 33.3% | 33.3% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/database/sql/fakedb_test.go`
- `src/database/sql/sql.go`
- `src/database/sql/sql_test.go`

**Predicted Files (3):**
- ❌ `src/database/sql/convert.go`
- ❌ `src/database/sql/driver/types.go`
- ✅ `src/database/sql/sql.go`


### 📊 **Proposal #45963 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 14.3% | 50.0% | 22.2% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/test/testflag.go`
- `src/cmd/go/internal/work/exec.go`

**Predicted Files (7):**
- ❌ `src/cmd/go/internal/test/test.go`
- ✅ `src/cmd/go/internal/test/testflag.go`
- ❌ `src/cmd/go/internal/vet/vet.go`
- ❌ `src/cmd/go/internal/vet/vetflag.go`
- ❌ `src/cmd/go/test.go`
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/vet_test.go`


### 📊 **Proposal #46518 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 72.7% | 47.1% | 57.1% | 8/17 |

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

**Predicted Files (11):**
- ❌ `src/net/ip.go`
- ❌ `src/net/ip_test.go`
- ✅ `src/net/netip/export_test.go`
- ❌ `src/net/netip/fuzz_test.go`
- ✅ `src/net/netip/inlining_test.go`
- ✅ `src/net/netip/netip.go`
- ✅ `src/net/netip/netip_pkg_test.go`
- ✅ `src/net/netip/netip_test.go`
- ✅ `src/net/netip/slow_test.go`
- ✅ `src/net/netip/uint128.go`
- ✅ `src/net/netip/uint128_test.go`


### 📊 **Proposal #40337 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (4):**
- ❌ `src/crypto/dsa/dsa.go`
- ❌ `src/crypto/dsa/dsa_test.go`
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`


### 📊 **Proposal #45973 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/serve_test.go`
- `src/net/http/server.go`

**Predicted Files (2):**
- ❌ `src/net/http/http.go`
- ✅ `src/net/http/server.go`


### 📊 **Proposal #49471 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 33.3% | 22.2% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/runtime/os_windows.go`
- `src/runtime/panic.go`
- `src/runtime/signal_windows.go`

**Predicted Files (6):**
- ❌ `src/runtime/crashdump.go`
- ❌ `src/runtime/debug.go`
- ✅ `src/runtime/os_windows.go`
- ❌ `src/syscall/dll_windows.go`
- ❌ `src/syscall/syscall_windows.go`
- ❌ `src/syscall/zsyscall_windows.go`


### 📊 **Proposal #52746 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modfetch/codehost/vcs.go`
- `src/cmd/go/internal/vcs/vcs.go`

**Predicted Files (2):**
- ❌ `src/time/format.go`
- ❌ `src/time/format_test.go`


### 📊 **Proposal #31804 (File Level)**

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


### 📊 **Proposal #43744 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/runtime/proc.go`
- `src/time/sleep_test.go`

**Predicted Files (2):**
- ❌ `src/testing/benchmark.go`
- ❌ `src/testing/benchmark_test.go`


### 📊 **Proposal #47916 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 30.0% | 17.6% | 22.2% | 3/17 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (17):**
- `src/cmd/compile/internal/noder/writer.go`
- `src/cmd/compile/internal/types2/call.go`
- `src/cmd/compile/internal/types2/lookup.go`
- `src/cmd/compile/internal/types2/signature.go`
- `src/go/types/api_test.go`
- `src/go/types/assignments.go`
- `src/go/types/call.go`
- `src/go/types/decl.go`
- `src/go/types/index.go`
- `src/go/types/instantiate.go`
- `src/go/types/lookup.go`
- `src/go/types/object.go`
- `src/go/types/predicates.go`
- `src/go/types/signature.go`
- `src/go/types/subst.go`
- `src/go/types/typelists.go`
- `src/go/types/typestring.go`

**Predicted Files (10):**
- ❌ `src/go/types/api.go`
- ❌ `src/go/types/context.go`
- ❌ `src/go/types/infer.go`
- ✅ `src/go/types/instantiate.go`
- ❌ `src/go/types/interface.go`
- ❌ `src/go/types/named.go`
- ✅ `src/go/types/object.go`
- ✅ `src/go/types/signature.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/go/types/types.go`


### 📊 **Proposal #40356 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/printf/printf.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/sigchanyzer/sigchanyzer.go`
- `src/cmd/vendor/golang.org/x/tools/go/analysis/passes/stdmethods/stdmethods.go`

**Predicted Files (6):**
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/stdmethods.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/errors/errors.go`
- ❌ `src/errors/wrap.go`
- ❌ `src/errors/wrap_test.go`


### 📊 **Proposal #53002 (File Level)**

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


### 📊 **Proposal #44196 (File Level)**

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


### 📊 **Proposal #50465 (File Level)**

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


### 📊 **Proposal #41696 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 14.3% | 16.7% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/cmd/go/go_test.go`
- `src/cmd/go/internal/test/test.go`
- `src/cmd/go/internal/test/testflag.go`
- `src/cmd/go/internal/work/build.go`
- `src/cmd/link/dwarf_test.go`

**Predicted Files (5):**
- ✅ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/go/internal/work/gc.go`
- ❌ `src/cmd/go/internal/work/gccgo.go`
- ❌ `src/cmd/go/internal/work/security.go`


### 📊 **Proposal #44011 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 3/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/os/exec/exec_windows_test.go`
- `src/os/file_windows.go`
- `src/syscall/exec_windows.go`
- `src/syscall/exec_windows_test.go`
- `src/syscall/syscall_windows.go`
- `src/syscall/zsyscall_windows.go`

**Predicted Files (12):**
- ❌ `src/internal/syscall/windows/exec_windows_test.go`
- ❌ `src/internal/syscall/windows/syscall_windows.go`
- ❌ `src/internal/syscall/windows/types_windows.go`
- ❌ `src/internal/syscall/windows/zsyscall_windows.go`
- ❌ `src/os/exec.go`
- ❌ `src/os/exec/exec_windows.go`
- ❌ `src/os/exec_posix.go`
- ❌ `src/os/exec_windows.go`
- ✅ `src/syscall/exec_windows.go`
- ✅ `src/syscall/syscall_windows.go`
- ❌ `src/syscall/types_windows.go`
- ✅ `src/syscall/zsyscall_windows.go`


### 📊 **Proposal #43620 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/benchmark.go`
- `src/testing/benchmark_test.go`

**Predicted Files (2):**
- ✅ `src/testing/benchmark.go`
- ❌ `src/testing/testing.go`


### 📊 **Proposal #48256 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/workcmd/edit.go`
- `src/cmd/go/internal/workcmd/init.go`
- `src/cmd/go/main.go`

**Predicted Files (3):**
- ✅ `src/cmd/go/internal/workcmd/edit.go`
- ✅ `src/cmd/go/internal/workcmd/init.go`
- ❌ `src/cmd/go/internal/workcmd/work.go`


### 📊 **Proposal #38017 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 50.0% | 44.4% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/time/export_test.go`
- `src/time/tzdata/tzdata.go`
- `src/time/tzdata_test.go`
- `src/time/zoneinfo_read.go`

**Predicted Files (5):**
- ❌ `lib/time/mkzip.go`
- ✅ `src/time/tzdata/tzdata.go`
- ❌ `src/time/zoneinfo.go`
- ✅ `src/time/zoneinfo_read.go`
- ❌ `src/time/zoneinfo_test.go`


### 📊 **Proposal #50601 (File Level)**

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


### 📊 **Proposal #50842 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/io/multi.go`
- `src/io/multi_test.go`

**Predicted Files (2):**
- ✅ `src/io/multi.go`
- ✅ `src/io/multi_test.go`


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
| 28.6% | 5.9% | 9.8% | 2/34 |

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

**Predicted Files (7):**
- ❌ `src/cmd/vet/README`
- ✅ `src/cmd/vet/main.go`
- ✅ `src/cmd/vet/vet_test.go`
- ❌ `src/fmt/format.go`
- ❌ `src/net/dial.go`
- ❌ `src/net/dial_test.go`
- ❌ `src/net/net.go`


### 📊 **Proposal #44006 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/syscall/js/js.go`

**Predicted Files (1):**
- ✅ `src/syscall/js/js.go`


### 📊 **Proposal #53021 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 33.3% | 33.3% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/crypto/cipher/cbc.go`
- `src/crypto/cipher/cfb.go`
- `src/crypto/cipher/ctr.go`
- `src/crypto/cipher/ofb.go`
- `src/crypto/subtle/xor.go`
- `src/crypto/subtle/xor_test.go`

**Predicted Files (6):**
- ❌ `src/crypto/cipher/xor_generic.go`
- ✅ `src/crypto/subtle/xor.go`
- ❌ `src/crypto/subtle/xor_asm.go`
- ❌ `src/crypto/subtle/xor_generic.go`
- ❌ `src/crypto/subtle/xor_linux_test.go`
- ✅ `src/crypto/subtle/xor_test.go`


### 📊 **Proposal #49580 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 14.3% | 23.5% | 2/14 |

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

**Predicted Files (3):**
- ❌ `src/io/fs/fs.go`
- ✅ `src/io/fs/readlink.go`
- ✅ `src/io/fs/readlink_test.go`


### 📊 **Proposal #41048 (File Level)**

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


### 📊 **Proposal #48409 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 83.3% | 35.7% | 50.0% | 10/28 |

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

**Predicted Files (12):**
- ✅ `src/runtime/debug/garbage.go`
- ❌ `src/runtime/debug/garbage_test.go`
- ✅ `src/runtime/mgc.go`
- ✅ `src/runtime/mgclimit.go`
- ✅ `src/runtime/mgclimit_test.go`
- ✅ `src/runtime/mgcmark.go`
- ✅ `src/runtime/mgcpacer.go`
- ✅ `src/runtime/mgcpacer_test.go`
- ✅ `src/runtime/mgcscavenge.go`
- ✅ `src/runtime/mgcscavenge_test.go`
- ❌ `src/runtime/mgcwork.go`
- ✅ `src/runtime/mheap.go`


### 📊 **Proposal #42102 (File Level)**

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
- ✅ `src/time/time.go`
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
| 66.7% | 22.2% | 33.3% | 4/18 |

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
- ✅ `src/io/fs/walk.go`
- ✅ `src/io/fs/walk_test.go`
- ✅ `src/path/filepath/path.go`
- ✅ `src/path/filepath/path_test.go`
- ❌ `src/path/filepath/path_unix.go`
- ❌ `src/path/filepath/path_windows.go`


### 📊 **Proposal #27628 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 60.0% | 60.0% | 3/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/go/internal/cache/hash.go`
- `src/cmd/go/internal/work/buildid.go`
- `src/cmd/go/internal/work/exec.go`
- `src/cmd/go/internal/work/gc.go`
- `src/cmd/go/internal/work/gccgo.go`

**Predicted Files (5):**
- ❌ `src/cmd/go/internal/work/action.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ✅ `src/cmd/go/internal/work/exec.go`
- ✅ `src/cmd/go/internal/work/gc.go`
- ✅ `src/cmd/go/internal/work/gccgo.go`


### 📊 **Proposal #51868 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/debug/pe/symbol.go`
- `src/debug/pe/symbols_test.go`

**Predicted Files (3):**
- ❌ `src/debug/pe/file.go`
- ❌ `src/debug/pe/pe.go`
- ✅ `src/debug/pe/symbol.go`


### 📊 **Proposal #28089 (File Level)**

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
| 60.0% | 100.0% | 75.0% | 3/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/crypto/x509/parser.go`
- `src/crypto/x509/x509.go`
- `src/crypto/x509/x509_test.go`

**Predicted Files (5):**
- ✅ `src/crypto/x509/parser.go`
- ❌ `src/crypto/x509/parser_test.go`
- ❌ `src/crypto/x509/pkix/pkix.go`
- ✅ `src/crypto/x509/x509.go`
- ✅ `src/crypto/x509/x509_test.go`


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
| 6.7% | 9.5% | 7.8% | 2/21 |

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

**Predicted Files (30):**
- ❌ `src/internal/poll/sock_cloexec.go`
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
- ❌ `src/runtime/internal/atomic/sys_linux_arm.s`
- ❌ `src/runtime/os_linux.go`
- ❌ `src/runtime/os_linux_arm.go`
- ❌ `src/runtime/os_linux_arm64.go`
- ❌ `src/runtime/os_linux_be64.go`
- ❌ `src/runtime/os_linux_generic.go`
- ❌ `src/runtime/os_linux_loong64.go`
- ❌ `src/runtime/os_linux_mips64x.go`
- ❌ `src/runtime/os_linux_mipsx.go`
- ❌ `src/runtime/os_linux_noauxv.go`
- ❌ `src/runtime/os_linux_novdso.go`
- ❌ `src/runtime/os_linux_ppc64x.go`
- ❌ `src/runtime/os_linux_riscv64.go`
- ❌ `src/runtime/os_linux_s390x.go`
- ❌ `src/runtime/os_linux_x86.go`
- ✅ `src/syscall/exec_linux.go`
- ✅ `src/syscall/syscall_linux.go`


### 📊 **Proposal #39444 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/os/exec_unix.go`
- `src/os/exec_unix_test.go`

**Predicted Files (1):**
- ✅ `src/os/exec_unix.go`


### 📊 **Proposal #45430 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 80.0% | 50.0% | 61.5% | 4/8 |

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

**Predicted Files (5):**
- ✅ `src/crypto/tls/cipher_suites.go`
- ✅ `src/crypto/tls/common.go`
- ❌ `src/crypto/tls/conn.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ✅ `src/crypto/tls/handshake_server.go`


### 📊 **Proposal #37533 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/flag/flag.go`
- `src/flag/flag_test.go`

**Predicted Files (2):**
- ✅ `src/flag/flag.go`
- ✅ `src/flag/flag_test.go`


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

**Predicted Files (4):**
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/ast_test.go`
- ❌ `src/go/token/token.go`
- ❌ `src/go/token/token_test.go`


### 📊 **Proposal #46057 (File Level)**

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


### 📊 **Proposal #43401 (File Level)**

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


### 📊 **Proposal #40728 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 13.0% | 21.4% | 3/23 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (23):**
- `src/cmd/go/internal/base/flag.go`
- `src/cmd/go/internal/fmtcmd/fmt.go`
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

**Predicted Files (5):**
- ❌ `src/cmd/go/internal/modcmd/mod.go`
- ✅ `src/cmd/go/internal/modload/import.go`
- ❌ `src/cmd/go/internal/modload/import_test.go`
- ✅ `src/cmd/go/internal/modload/load.go`
- ✅ `src/cmd/go/internal/modload/modfile.go`


### 📊 **Proposal #43993 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 25.0% | 25.0% | 1/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`
- `src/text/template/exec.go`
- `src/text/template/funcs.go`

**Predicted Files (4):**
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/vet_test.go`
- ❌ `src/reflect/deepequal.go`
- ✅ `src/reflect/value.go`


### 📊 **Proposal #50770 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/time/mono_test.go`
- `src/time/time.go`

**Predicted Files (2):**
- ✅ `src/time/time.go`
- ❌ `src/time/time_test.go`


### 📊 **Proposal #44221 (File Level)**

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


### 📊 **Proposal #44143 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/net/http/socks_bundle.go`

**Predicted Files (1):**
- ❌ `src/context/context.go`


### 📊 **Proposal #43931 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/staticdata/embed.go`
- `src/embed/internal/embedtest/embed_test.go`
- `src/go/types/stdlib_test.go`

**Predicted Files (38):**
- ❌ `src/cmd/compile/internal/types2/instantiate.go`
- ❌ `src/cmd/compile/internal/types2/instantiate_test.go`
- ❌ `src/cmd/compile/internal/types2/subst.go`
- ❌ `src/cmd/compile/internal/types2/typeparam.go`
- ❌ `src/cmd/compile/internal/types2/typeset.go`
- ❌ `src/cmd/compile/internal/types2/typeset_test.go`
- ❌ `src/cmd/compile/internal/types2/unify.go`
- ❌ `src/go/internal/gcimporter/gcimporter.go`
- ❌ `src/go/internal/gcimporter/gcimporter_test.go`
- ❌ `src/go/internal/gcimporter/testdata/generics.go`
- ❌ `src/go/internal/types/errors/codes.go`
- ❌ `src/go/internal/types/errors/codes_test.go`
- ❌ `src/go/internal/types/errors/generrordocs.go`
- ❌ `src/go/types/api.go`
- ❌ `src/go/types/api_test.go`
- ❌ `src/go/types/example_test.go`
- ❌ `src/go/types/infer.go`
- ❌ `src/go/types/infer_test.go`
- ❌ `src/go/types/instantiate.go`
- ❌ `src/go/types/instantiate_test.go`
- ❌ `src/go/types/subst.go`
- ❌ `src/go/types/subst_test.go`
- ❌ `src/go/types/testdata/typeinst0.go`
- ❌ `src/go/types/testdata/typeinst1.go`
- ❌ `src/go/types/testdata/typeinstcycles.go`
- ❌ `src/go/types/testdata/typeparams.go`
- ❌ `src/go/types/testdata/unions.go`
- ❌ `src/go/types/typelists.go`
- ❌ `src/go/types/typelists_test.go`
- ❌ `src/go/types/typeparam.go`
- ❌ `src/go/types/typeparam_test.go`
- ❌ `src/go/types/types.go`
- ❌ `src/go/types/typeset.go`
- ❌ `src/go/types/typeset_test.go`
- ❌ `src/go/types/typeterm.go`
- ❌ `src/go/types/typeterm_test.go`
- ❌ `src/go/types/union.go`
- ❌ `src/go/types/union_test.go`


### 📊 **Proposal #48294 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/reflect/all_test.go`

**Predicted Files (4):**
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`


### 📊 **Proposal #51428 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/error_test.go`
- `src/net/net.go`

**Predicted Files (2):**
- ❌ `src/net/dial.go`
- ✅ `src/net/net.go`


### 📊 **Proposal #52463 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/gofmt/gofmt.go`
- `src/cmd/gofmt/simplify.go`

**Predicted Files (5):**
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/ast/scope.go`
- ❌ `src/go/parser/parser.go`
- ❌ `src/go/parser/resolver.go`
- ❌ `src/go/types/object.go`


### 📊 **Proposal #51115 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/io/io.go`

**Predicted Files (2):**
- ✅ `src/io/io.go`
- ❌ `src/io/io_test.go`


### 📊 **Proposal #40255 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 6.7% | 10.5% | 1/15 |

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

**Predicted Files (4):**
- ✅ `src/cmd/compile/internal/ssa/rewrite386.go`
- ❌ `src/cmd/compile/internal/ssa/rewrite386splitload.go`
- ❌ `src/cmd/compile/internal/ssa/softfloat.go`
- ❌ `test/fixedbugs/issue22429.go`


### 📊 **Proposal #46648 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 33.3% | 28.6% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/go/types/check.go`
- `src/go/types/check_test.go`
- `src/go/types/stdlib_test.go`

**Predicted Files (4):**
- ❌ `src/cmd/compile/internal/types2/version.go`
- ✅ `src/go/types/check.go`
- ❌ `src/go/types/goversion.go`
- ❌ `src/go/types/types.go`


### 📊 **Proposal #53346 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/xml/marshal.go`
- `src/encoding/xml/marshal_test.go`

**Predicted Files (3):**
- ✅ `src/encoding/xml/marshal.go`
- ❌ `src/encoding/xml/xml.go`
- ❌ `src/encoding/xml/xml_test.go`


### 📊 **Proposal #51082 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 5.1% | 8.5% | 6/118 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (118):**
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

**Predicted Files (24):**
- ❌ `src/cmd/doc/`
- ❌ `src/cmd/doc/doc.go`
- ❌ `src/cmd/gofmt/gofmt.go`
- ❌ `src/go/doc/`
- ✅ `src/go/doc/comment.go`
- ❌ `src/go/doc/comment/`
- ❌ `src/go/doc/comment/comment.go`
- ❌ `src/go/doc/comment/doc.go`
- ❌ `src/go/doc/comment/html.go`
- ❌ `src/go/doc/comment/markdown.go`
- ❌ `src/go/doc/comment/parse.go`
- ❌ `src/go/doc/comment/parse_test.go`
- ❌ `src/go/doc/comment/print.go`
- ❌ `src/go/doc/comment/std.go`
- ❌ `src/go/doc/comment/std_test.go`
- ❌ `src/go/doc/comment/testdata_test.go`
- ❌ `src/go/doc/comment/text.go`
- ❌ `src/go/doc/comment/wrap_test.go`
- ✅ `src/go/doc/comment_test.go`
- ✅ `src/go/doc/doc.go`
- ❌ `src/go/printer/`
- ✅ `src/go/printer/comment.go`
- ✅ `src/go/printer/printer.go`
- ✅ `src/go/printer/printer_test.go`


### 📊 **Proposal #35833 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/crypto/elliptic/elliptic.go`
- `src/crypto/rsa/pkcs1v15.go`
- `src/math/big/int.go`
- `src/math/big/int_test.go`

**Predicted Files (2):**
- ✅ `src/math/big/int.go`
- ✅ `src/math/big/int_test.go`


### 📊 **Proposal #42387 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/io/fs/readdir.go`
- `src/io/fs/readdir_test.go`

**Predicted Files (2):**
- ❌ `src/io/fs/fs.go`
- ❌ `src/io/fs/fs_test.go`


### 📊 **Proposal #45454 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 66.7% | 44.4% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/cfg/cfg.go`
- `src/go/build/build.go`
- `src/internal/buildcfg/cfg.go`

**Predicted Files (6):**
- ❌ `src/cmd/go/internal/base/env.go`
- ✅ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/go/internal/work/exec.go`
- ✅ `src/go/build/build.go`
- ❌ `src/go/build/constraint/expr.go`
- ❌ `src/go/build/constraint/expr_test.go`


### 📊 **Proposal #50436 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/os/exec/exec.go`
- `src/os/exec/exec_test.go`

**Predicted Files (4):**
- ✅ `src/os/exec/exec.go`
- ✅ `src/os/exec/exec_test.go`
- ❌ `src/os/exec/exec_unix.go`
- ❌ `src/os/exec/exec_windows.go`


### 📊 **Proposal #44167 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 62.5% | 35.7% | 45.5% | 5/14 |

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

**Predicted Files (8):**
- ✅ `src/runtime/mgc.go`
- ✅ `src/runtime/mgcmark.go`
- ✅ `src/runtime/mgcpacer.go`
- ✅ `src/runtime/mgcpacer_test.go`
- ✅ `src/runtime/mgcsweep.go`
- ❌ `test/gc.go`
- ❌ `test/gc1.go`
- ❌ `test/gc2.go`


### 📊 **Proposal #39178 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/lookup.go`
- `src/net/lookup_test.go`

**Predicted Files (1):**
- ✅ `src/net/lookup.go`


### 📊 **Proposal #46287 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 87.5% | 63.6% | 73.7% | 7/11 |

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

**Predicted Files (8):**
- ✅ `src/crypto/x509/cert_pool.go`
- ❌ `src/crypto/x509/cert_pool_test.go`
- ✅ `src/crypto/x509/internal/macos/corefoundation.go`
- ✅ `src/crypto/x509/internal/macos/security.go`
- ✅ `src/crypto/x509/root_darwin.go`
- ✅ `src/crypto/x509/root_windows.go`
- ✅ `src/crypto/x509/verify.go`
- ✅ `src/crypto/x509/verify_test.go`


### 📊 **Proposal #48257 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/cmd/go/internal/workcmd/use.go`

**Predicted Files (1):**
- ✅ `src/cmd/go/internal/workcmd/use.go`


### 📊 **Proposal #46293 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/reflect/all_test.go`

**Predicted Files (4):**
- ❌ `src/reflect/iter.go`
- ❌ `src/reflect/iter_test.go`
- ❌ `src/reflect/type.go`
- ❌ `src/reflect/value.go`


### 📊 **Proposal #42026 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 62.5% | 2.6% | 5.0% | 5/194 |

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

**Predicted Files (8):**
- ❌ `src/io/fs/readdir.go`
- ❌ `src/io/fs/readfile.go`
- ✅ `src/io/ioutil/ioutil.go`
- ✅ `src/io/ioutil/tempfile.go`
- ✅ `src/os/dir.go`
- ✅ `src/os/file.go`
- ❌ `src/os/path.go`
- ✅ `src/os/tempfile.go`


### 📊 **Proposal #45435 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 4/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/sync/mutex.go`
- `src/sync/mutex_test.go`
- `src/sync/rwmutex.go`
- `src/sync/rwmutex_test.go`

**Predicted Files (4):**
- ✅ `src/sync/mutex.go`
- ✅ `src/sync/mutex_test.go`
- ✅ `src/sync/rwmutex.go`
- ✅ `src/sync/rwmutex_test.go`


### 📊 **Proposal #48187 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/version/version.go`
- `src/debug/buildinfo/buildinfo_test.go`

**Predicted Files (3):**
- ✅ `src/cmd/go/internal/version/version.go`
- ❌ `src/debug/buildinfo/buildinfo.go`
- ✅ `src/debug/buildinfo/buildinfo_test.go`


### 📊 **Proposal #37519 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 33.3% | 33.3% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/go/internal/modfetch/repo.go`
- `src/cmd/go/internal/modfetch/sumdb.go`
- `src/cmd/go/internal/modget/get.go`

**Predicted Files (3):**
- ❌ `src/cmd/go/internal/get/get.go`
- ✅ `src/cmd/go/internal/modget/get.go`
- ❌ `src/cmd/go/internal/modget/modget.go`


### 📊 **Proposal #38627 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 100.0% | 66.7% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/text/template/parse/parse.go`

**Predicted Files (2):**
- ❌ `src/text/template/parse/node.go`
- ✅ `src/text/template/parse/parse.go`


### 📊 **Proposal #41260 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/testing/testing.go`
- `src/testing/testing_test.go`

**Predicted Files (2):**
- ✅ `src/testing/testing.go`
- ✅ `src/testing/testing_test.go`


### 📊 **Proposal #44505 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 18.2% | 80.0% | 29.6% | 4/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/asm/internal/lex/tokenizer.go`
- `src/cmd/dist/build.go`
- `src/cmd/dist/buildtool.go`
- `src/cmd/dist/test.go`
- `src/cmd/dist/util.go`

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


### 📊 **Proposal #50429 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/go/parser/parser.go`
- `src/go/parser/parser_test.go`

**Predicted Files (8):**
- ❌ `ken/range.go`
- ❌ `src/go/ast/ast.go`
- ❌ `src/go/token/token.go`
- ❌ `test/range.go`
- ❌ `test/range2.go`
- ❌ `test/range3.go`
- ❌ `test/range4.go`
- ❌ `test/rangegen.go`


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

**Predicted Files (13):**
- ❌ `src/cmd/compile/internal/base/base.go`
- ❌ `src/cmd/go/internal/base/env.go`
- ❌ `src/cmd/go/internal/cfg/cfg.go`
- ❌ `src/cmd/internal/objabi/util.go`
- ❌ `src/internal/goexperiment/exp_fieldtrack_off.go`
- ❌ `src/internal/goexperiment/exp_fieldtrack_on.go`
- ❌ `src/internal/goexperiment/exp_preemptibleloops_off.go`
- ❌ `src/internal/goexperiment/exp_preemptibleloops_on.go`
- ❌ `src/internal/goexperiment/exp_regabi_off.go`
- ❌ `src/internal/goexperiment/exp_regabi_on.go`
- ❌ `src/internal/goexperiment/exp_staticlockranking_off.go`
- ❌ `src/internal/goexperiment/exp_staticlockranking_on.go`
- ❌ `src/internal/goexperiment/flags.go`


### 📊 **Proposal #40592 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 33.3% | 44.4% | 2/6 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (6):**
- `src/encoding/json/encode.go`
- `src/reflect/all_test.go`
- `src/reflect/deepequal.go`
- `src/reflect/set_test.go`
- `src/reflect/type.go`
- `src/reflect/value.go`

**Predicted Files (3):**
- ✅ `src/reflect/type.go`
- ✅ `src/reflect/value.go`
- ❌ `test/fixedbugs/issue36085.go`


### 📊 **Proposal #51644 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 100.0% | 80.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/binary/varint.go`
- `src/encoding/binary/varint_test.go`

**Predicted Files (3):**
- ❌ `src/encoding/binary/binary.go`
- ✅ `src/encoding/binary/varint.go`
- ✅ `src/encoding/binary/varint_test.go`


### 📊 **Proposal #34527 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/go/internal/cfg/cfg.go`
- `src/cmd/go/internal/clean/clean.go`
- `src/cmd/go/internal/envcmd/env.go`
- `src/cmd/go/internal/modfetch/codehost/codehost.go`
- `src/cmd/go/internal/modfetch/codehost/git_test.go`
- `src/cmd/go/internal/modfetch/codehost/shell.go`
- `src/cmd/go/internal/modfetch/coderepo_test.go`

**Predicted Files (3):**
- ❌ `src/cmd/go/internal/cache/cache.go`
- ❌ `src/cmd/go/internal/modfetch/cache.go`
- ❌ `src/cmd/go/internal/modfetch/sumdb.go`


### 📊 **Proposal #45628 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/encoding/xml/xml.go`
- `src/encoding/xml/xml_test.go`

**Predicted Files (3):**
- ❌ `src/encoding/xml/read.go`
- ❌ `src/encoding/xml/read_test.go`
- ✅ `src/encoding/xml/xml.go`


### 📊 **Proposal #46746 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (2):**
- ❌ `src/reflect/type.go`
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
| 50.0% | 50.0% | 50.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/tls/conn.go`
- `src/crypto/tls/tls_test.go`

**Predicted Files (2):**
- ✅ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/conn_test.go`


### 📊 **Proposal #41184 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 42.9% | 30.0% | 35.3% | 9/30 |

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

**Predicted Files (21):**
- ✅ `src/cmd/asm/internal/asm/parse.go`
- ❌ `src/cmd/compile/internal/syntax/parser.go`
- ✅ `src/cmd/fix/buildtag.go`
- ❌ `src/cmd/go/build.go`
- ✅ `src/cmd/go/internal/load/pkg.go`
- ❌ `src/cmd/go/internal/work/build.go`
- ✅ `src/cmd/go/internal/work/exec.go`
- ❌ `src/cmd/vet/main.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag2.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag3.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag4.go`
- ❌ `src/cmd/vet/testdata/buildtag/buildtag5.go`
- ✅ `src/go/build/build.go`
- ❌ `src/go/build/constraint/constraint.go`
- ✅ `src/go/build/constraint/expr.go`
- ✅ `src/go/build/constraint/expr_test.go`
- ❌ `src/go/build/constraint/vers.go`
- ❌ `src/go/build/constraint/vers_test.go`
- ✅ `src/go/printer/gobuild.go`
- ✅ `src/go/printer/printer.go`


### 📊 **Proposal #48866 (File Level)**

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


### 📊 **Proposal #50332 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 9.5% | 16.0% | 2/21 |

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

**Predicted Files (4):**
- ❌ `src/cmd/go/internal/base/base.go`
- ✅ `src/cmd/go/internal/base/flag.go`
- ✅ `src/cmd/go/internal/work/build.go`
- ❌ `src/cmd/go/main.go`


### 📊 **Proposal #53466 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.0% | 37.5% | 18.2% | 3/8 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (8):**
- `src/cmd/dist/main.go`
- `src/cmd/dist/test.go`
- `src/cmd/link/internal/ld/lib.go`
- `src/cmd/link/internal/riscv64/obj.go`
- `src/runtime/defs_freebsd_riscv64.go`
- `src/runtime/vdso_freebsd_riscv64.go`
- `src/syscall/syscall_freebsd_riscv64.go`
- `src/syscall/zsyscall_freebsd_riscv64.go`

**Predicted Files (25):**
- ❌ `src/cmd/asm/internal/arch/riscv64.go`
- ❌ `src/cmd/compile/internal/riscv64/galign.go`
- ❌ `src/cmd/compile/internal/riscv64/ggen.go`
- ❌ `src/cmd/compile/internal/riscv64/gsubr.go`
- ❌ `src/cmd/compile/internal/riscv64/ssa.go`
- ❌ `src/cmd/link/internal/ld/outbuf_freebsd.go`
- ❌ `src/internal/abi/abi_riscv64.go`
- ❌ `src/internal/cpu/cpu_riscv64.go`
- ❌ `src/internal/cpu/cpu_riscv64_linux.go`
- ❌ `src/internal/cpu/cpu_riscv64_other.go`
- ❌ `src/internal/goarch/goarch_riscv64.go`
- ❌ `src/internal/goarch/zgoarch_riscv64.go`
- ✅ `src/runtime/defs_freebsd_riscv64.go`
- ❌ `src/runtime/os_freebsd_riscv64.go`
- ❌ `src/runtime/signal_freebsd_riscv64.go`
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


### 📊 **Proposal #49390 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 60.0% | 60.0% | 60.0% | 3/5 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (5):**
- `src/cmd/dist/build.go`
- `src/cmd/dist/test.go`
- `src/internal/testenv/noopt.go`
- `src/internal/testenv/opt.go`
- `src/internal/testenv/testenv.go`

**Predicted Files (5):**
- ❌ `src/cmd/compile/internal/base/debug.go`
- ❌ `src/cmd/compile/internal/base/flag.go`
- ✅ `src/internal/testenv/noopt.go`
- ✅ `src/internal/testenv/opt.go`
- ✅ `src/internal/testenv/testenv.go`


### 📊 **Proposal #39351 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 50.0% | 57.1% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/expvar/expvar.go`
- `src/expvar/expvar_test.go`
- `src/sync/atomic/value.go`
- `src/sync/atomic/value_test.go`

**Predicted Files (3):**
- ✅ `src/sync/atomic/value.go`
- ✅ `src/sync/atomic/value_test.go`
- ❌ `test/atomicload.go`


### 📊 **Proposal #47142 (File Level)**

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


### 📊 **Proposal #46742 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 11.1% | 14.3% | 12.5% | 1/7 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (7):**
- `src/cmd/compile/internal/typecheck/builtin.go`
- `src/cmd/compile/internal/typecheck/func.go`
- `src/cmd/compile/internal/walk/builtin.go`
- `src/runtime/checkptr.go`
- `src/runtime/checkptr_test.go`
- `src/runtime/testdata/testprog/checkptr.go`
- `test/unsafebuiltins.go`

**Predicted Files (9):**
- ❌ `src/cmd/compile/internal/test/testdata/unsafe_test.go`
- ❌ `src/cmd/compile/internal/types2/slice.go`
- ❌ `src/runtime/slice.go`
- ❌ `src/runtime/unsafe.go`
- ❌ `src/unsafe/unsafe.go`
- ❌ `test/unsafe_slice_data.go`
- ❌ `test/unsafe_string.go`
- ❌ `test/unsafe_string_data.go`
- ✅ `test/unsafebuiltins.go`


### 📊 **Proposal #46505 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 0.0% | 0.0% | 0.0% | 0/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/crypto/sha256/sha256.go`
- `src/crypto/sha512/sha512.go`

**Predicted Files (2):**
- ❌ `test/fixedbugs/issue39505.go`
- ❌ `test/fixedbugs/issue39505b.go`


### 📊 **Proposal #52376 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 100.0% | 57.1% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (5):**
- ✅ `src/reflect/all_test.go`
- ❌ `src/reflect/export_test.go`
- ❌ `src/reflect/type.go`
- ✅ `src/reflect/value.go`
- ❌ `test/clear.go`


### 📊 **Proposal #44815 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 100.0% | 100.0% | 2/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/bufio/bufio.go`
- `src/bufio/bufio_test.go`

**Predicted Files (2):**
- ✅ `src/bufio/bufio.go`
- ✅ `src/bufio/bufio_test.go`


### 📊 **Proposal #45033 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 25.0% | 50.0% | 33.3% | 2/4 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (4):**
- `src/strconv/bytealg.go`
- `src/strconv/bytealg_bootstrap.go`
- `src/strconv/quote.go`
- `src/strconv/quote_test.go`

**Predicted Files (8):**
- ❌ `fmt/scan.go`
- ❌ `reflect/type.go`
- ❌ `src/fmt/scan.go`
- ❌ `src/reflect/type.go`
- ✅ `src/strconv/quote.go`
- ✅ `src/strconv/quote_test.go`
- ❌ `src/text/template/parse/lex.go`
- ❌ `text/template/parse/lex.go`


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
- ❌ `src/reflect/type.go`
- ✅ `src/reflect/value.go`


### 📊 **Proposal #51572 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 1.2% | 33.3% | 2.4% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/dist/build.go`
- `src/cmd/go/internal/imports/build.go`
- `src/go/build/build.go`

**Predicted Files (80):**
- ❌ `src/cmd/cgo/internal/test/test_unix.go`
- ❌ `src/cmd/go/build.go`
- ❌ `src/cmd/go/internal/base/error_notunix.go`
- ❌ `src/cmd/go/internal/base/error_unix.go`
- ❌ `src/cmd/go/internal/base/signal_notunix.go`
- ❌ `src/cmd/go/internal/base/signal_unix.go`
- ✅ `src/go/build/build.go`
- ❌ `src/go/build/build_test.go`
- ❌ `src/mime/type_unix.go`
- ❌ `src/mime/type_unix_test.go`
- ❌ `src/net/cgo_unix.go`
- ❌ `src/net/cgo_unix_cgo.go`
- ❌ `src/net/cgo_unix_cgo_res.go`
- ❌ `src/net/cgo_unix_cgo_resn.go`
- ❌ `src/net/cgo_unix_syscall.go`
- ❌ `src/net/cgo_unix_test.go`
- ❌ `src/net/dnsclient_unix.go`
- ❌ `src/net/dnsclient_unix_test.go`
- ❌ `src/net/dnsconfig_unix.go`
- ❌ `src/net/dnsconfig_unix_test.go`
- ❌ `src/net/error_unix.go`
- ❌ `src/net/error_unix_test.go`
- ❌ `src/net/fd_unix.go`
- ❌ `src/net/file_unix.go`
- ❌ `src/net/file_unix_test.go`
- ❌ `src/net/hook_unix.go`
- ❌ `src/net/interface_unix_test.go`
- ❌ `src/net/lookup_unix.go`
- ❌ `src/net/main_unix_test.go`
- ❌ `src/net/platform_unix_test.go`
- ❌ `src/net/rawconn_unix_test.go`
- ❌ `src/net/rlimit_unix.go`
- ❌ `src/net/sendfile_unix_test.go`
- ❌ `src/net/tcpconn_keepalive_conf_unix_test.go`
- ❌ `src/net/tcpsock_unix.go`
- ❌ `src/net/tcpsock_unix_test.go`
- ❌ `src/net/tcpsockopt_unix.go`
- ❌ `src/net/unixsock.go`
- ❌ `src/net/unixsock_linux_test.go`
- ❌ `src/net/unixsock_posix.go`
- ❌ `src/net/unixsock_readmsg_cloexec.go`
- ❌ `src/net/unixsock_readmsg_cmsg_cloexec.go`
- ❌ `src/net/unixsock_readmsg_other.go`
- ❌ `src/net/unixsock_readmsg_test.go`
- ❌ `src/net/unixsock_test.go`
- ❌ `src/net/write_unix_test.go`
- ❌ `src/net/writev_unix.go`
- ❌ `src/os/exec_unix.go`
- ❌ `src/os/exec_unix_test.go`
- ❌ `src/os/file_unix.go`
- ❌ `src/os/getwd_unix_test.go`
- ❌ `src/os/os_unix_test.go`
- ❌ `src/os/path_unix.go`
- ❌ `src/os/pipe_unix.go`
- ❌ `src/os/readfrom_unix_test.go`
- ❌ `src/os/removeall_unix.go`
- ❌ `src/os/root_unix.go`
- ❌ `src/os/root_unix_test.go`
- ❌ `src/os/stat_unix.go`
- ❌ `src/os/sys_unix.go`
- ❌ `src/os/timeout_unix_test.go`
- ❌ `src/path/filepath/example_unix_test.go`
- ❌ `src/path/filepath/example_unix_walk_test.go`
- ❌ `src/path/filepath/path_unix.go`
- ❌ `src/path/filepath/symlink_unix.go`
- ❌ `src/runtime/os_unix.go`
- ❌ `src/runtime/signal_unix.go`
- ❌ `src/runtime/syscall_unix_test.go`
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
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/testing/iotest/logger_test.go`
- `src/testing/iotest/reader.go`
- `src/testing/iotest/reader_test.go`

**Predicted Files (3):**
- ❌ `src/testing/iotest/example_test.go`
- ✅ `src/testing/iotest/reader.go`
- ✅ `src/testing/iotest/reader_test.go`


### 📊 **Proposal #36771 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 16.7% | 100.0% | 28.6% | 3/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/strconv/atoc.go`
- `src/strconv/atoc_test.go`
- `src/strconv/ctoa.go`

**Predicted Files (18):**
- ❌ `src/fmt/scan.go`
- ❌ `src/fmt/scan_test.go`
- ✅ `src/strconv/atoc.go`
- ✅ `src/strconv/atoc_test.go`
- ❌ `src/strconv/atof.go`
- ❌ `src/strconv/atof_test.go`
- ❌ `src/strconv/atoi.go`
- ❌ `src/strconv/atoi_test.go`
- ✅ `src/strconv/ctoa.go`
- ❌ `src/strconv/ctoa_test.go`
- ❌ `src/strconv/doc.go`
- ❌ `src/strconv/example_test.go`
- ❌ `src/strconv/export_test.go`
- ❌ `src/strconv/ftoa.go`
- ❌ `src/strconv/ftoa_test.go`
- ❌ `src/strconv/isprint.go`
- ❌ `src/strconv/quote.go`
- ❌ `src/strconv/quote_test.go`


### 📊 **Proposal #44435 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 33.3% | 50.0% | 40.0% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/cmd/go/internal/modcmd/download.go`
- `src/cmd/go/internal/modload/modfile.go`

**Predicted Files (3):**
- ✅ `src/cmd/go/internal/modcmd/download.go`
- ❌ `src/cmd/go/internal/modload/load.go`
- ❌ `src/cmd/go/internal/modload/query.go`


### 📊 **Proposal #50101 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 20.0% | 33.3% | 25.0% | 3/9 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (9):**
- `src/internal/syscall/unix/net_darwin.go`
- `src/net/cgo_unix.go`
- `src/net/cgo_unix_cgo_res.go`
- `src/net/cgo_unix_cgo_resn.go`
- `src/net/cgo_unix_syscall.go`
- `src/net/conf.go`
- `src/net/dnsclient_unix.go`
- `src/net/dnsclient_unix_test.go`
- `src/net/lookup.go`

**Predicted Files (15):**
- ❌ `src/net/dnsclient.go`
- ❌ `src/net/dnsclient_test.go`
- ✅ `src/net/dnsclient_unix.go`
- ✅ `src/net/dnsclient_unix_test.go`
- ❌ `src/net/dnsconfig.go`
- ❌ `src/net/dnsconfig_unix.go`
- ❌ `src/net/dnsconfig_unix_test.go`
- ❌ `src/net/dnsconfig_windows.go`
- ✅ `src/net/lookup.go`
- ❌ `src/net/lookup_test.go`
- ❌ `src/net/lookup_unix.go`
- ❌ `src/net/lookup_windows.go`
- ❌ `src/net/lookup_windows_test.go`
- ❌ `src/syscall/dll_windows.go`
- ❌ `src/syscall/syscall_windows.go`


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
| 100.0% | 66.7% | 80.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/io/io.go`
- `src/io/io_test.go`
- `src/net/http/transfer.go`

**Predicted Files (2):**
- ✅ `src/io/io.go`
- ✅ `src/io/io_test.go`


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
| 50.0% | 12.5% | 20.0% | 1/8 |

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

**Predicted Files (2):**
- ✅ `src/go/types/object.go`
- ❌ `src/go/types/object_test.go`


### 📊 **Proposal #39214 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 7.5% | 25.0% | 11.5% | 3/12 |

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

**Predicted Files (40):**
- ❌ `src/internal/cpu/cpu.go`
- ❌ `src/internal/cpu/cpu_aix.go`
- ❌ `src/internal/cpu/cpu_arm.go`
- ❌ `src/internal/cpu/cpu_arm64.go`
- ❌ `src/internal/cpu/cpu_arm64_android.go`
- ❌ `src/internal/cpu/cpu_arm64_darwin.go`
- ❌ `src/internal/cpu/cpu_arm64_freebsd.go`
- ❌ `src/internal/cpu/cpu_arm64_hwcap.go`
- ❌ `src/internal/cpu/cpu_arm64_linux.go`
- ❌ `src/internal/cpu/cpu_arm64_openbsd.go`
- ❌ `src/internal/cpu/cpu_arm64_other.go`
- ❌ `src/internal/cpu/cpu_linux.go`
- ❌ `src/internal/cpu/cpu_loong64.go`
- ❌ `src/internal/cpu/cpu_loong64_hwcap.go`
- ❌ `src/internal/cpu/cpu_loong64_linux.go`
- ❌ `src/internal/cpu/cpu_mips.go`
- ❌ `src/internal/cpu/cpu_mips64.go`
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
- ❌ `src/internal/cpu/cpu_zos.go`
- ❌ `src/internal/cpu/export_test.go`
- ❌ `src/internal/cpu/export_x86_test.go`
- ❌ `src/internal/cpu/proc_cpuinfo_linux.go`
- ❌ `src/internal/cpu/runtime_auxv.go`
- ✅ `src/testing/benchmark.go`
- ❌ `src/testing/testing.go`


### 📊 **Proposal #30715 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 100.0% | 50.0% | 66.7% | 1/2 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (2):**
- `src/net/http/request.go`
- `src/net/http/serve_test.go`

**Predicted Files (1):**
- ✅ `src/net/http/request.go`


### 📊 **Proposal #51972 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 66.7% | 66.7% | 66.7% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/sync/map.go`
- `src/sync/map_reference_test.go`
- `src/sync/map_test.go`

**Predicted Files (3):**
- ❌ `src/sync/export_test.go`
- ✅ `src/sync/map.go`
- ✅ `src/sync/map_test.go`


### 📊 **Proposal #50859 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 8.3% | 100.0% | 15.4% | 1/1 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (1):**
- `src/sync/cond.go`

**Predicted Files (12):**
- ❌ `src/runtime/mbarrier.go`
- ❌ `src/runtime/mem.go`
- ❌ `src/sync/atomic/doc.go`
- ❌ `src/sync/atomic/doc_32.go`
- ❌ `src/sync/atomic/doc_64.go`
- ❌ `src/sync/atomic/type.go`
- ❌ `src/sync/atomic/value.go`
- ✅ `src/sync/cond.go`
- ❌ `src/sync/doc.go`
- ❌ `src/sync/mutex.go`
- ❌ `src/sync/rwmutex.go`
- ❌ `src/sync/waitgroup.go`


### 📊 **Proposal #32406 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 87.5% | 58.3% | 70.0% | 7/12 |

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

**Predicted Files (8):**
- ✅ `src/crypto/tls/common.go`
- ✅ `src/crypto/tls/conn.go`
- ❌ `src/crypto/tls/conn_test.go`
- ✅ `src/crypto/tls/handshake_client.go`
- ✅ `src/crypto/tls/handshake_client_test.go`
- ✅ `src/crypto/tls/handshake_server.go`
- ✅ `src/crypto/tls/handshake_server_test.go`
- ✅ `src/net/http/server.go`


### 📊 **Proposal #45899 (File Level)**

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


### 📊 **Proposal #47658 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 50.0% | 33.3% | 40.0% | 1/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/reflect/all_test.go`
- `src/reflect/value.go`

**Predicted Files (2):**
- ❌ `src/reflect/type.go`
- ✅ `src/reflect/value.go`


### 📊 **Proposal #47609 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 40.0% | 66.7% | 50.0% | 2/3 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (3):**
- `src/cmd/compile/internal/test/inl_test.go`
- `src/unicode/utf8/utf8.go`
- `src/unicode/utf8/utf8_test.go`

**Predicted Files (5):**
- ❌ `src/runtime/utf8.go`
- ❌ `src/unicode/utf8/example_test.go`
- ✅ `src/unicode/utf8/utf8.go`
- ✅ `src/unicode/utf8/utf8_test.go`
- ❌ `test/utf.go`


### 📊 **Proposal #38776 (File Level)**

| **Precision** | **Recall** | **F1-Score** | **Found/Total** |
|-----------|--------|----------|-------------|
| 12.5% | 12.5% | 12.5% | 1/8 |

##### Ground Truth vs Predicted Files

**Ground Truth Files (8):**
- `src/crypto/internal/boring/sha.go`
- `src/crypto/sha1/sha1.go`
- `src/crypto/sha1/sha1_test.go`
- `src/crypto/sha1/sha1block_amd64.go`
- `src/crypto/sha1/sha1block_arm64.go`
- `src/crypto/sha1/sha1block_decl.go`
- `src/crypto/sha256/sha256_test.go`
- `src/crypto/sha512/sha512_test.go`

**Predicted Files (8):**
- ✅ `src/crypto/sha1/sha1.go`
- ❌ `src/crypto/sha256/sha256.go`
- ❌ `src/crypto/sha512/sha512.go`
- ❌ `src/hash/adler32/adler32.go`
- ❌ `src/hash/crc32/crc32.go`
- ❌ `src/hash/crc64/crc64.go`
- ❌ `src/hash/fnv/fnv.go`
- ❌ `src/hash/maphash/maphash.go`
