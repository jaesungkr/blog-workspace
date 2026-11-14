import Foundation
import PDFKit
let path=CommandLine.arguments[1], out=CommandLine.arguments[2]
guard let doc=PDFDocument(url:URL(fileURLWithPath:path)) else {fatalError("PDF unavailable")}
var all=""
print("Pages:",doc.pageCount)
for i in 0..<doc.pageCount {let s=doc.page(at:i)?.string ?? "";all+="\n=== PAGE \(i+1) ===\n"+s+"\n";if s.contains("제출") && (s.contains("03") || s.contains("반입")){print("MATCH PAGE",i+1);print(s.prefix(5000))}}
try all.write(toFile:out,atomically:true,encoding:.utf8)
