import Foundation
import AppKit
import PDFKit
let args=CommandLine.arguments
let path=args[1], out=args[2]
try FileManager.default.createDirectory(atPath:out,withIntermediateDirectories:true)
guard let doc=PDFDocument(url:URL(fileURLWithPath:path)) else {fatalError("cannot open PDF")}
var records:[[String:Any]]=[]
var text=""
let scale:CGFloat=1.5
var thumbnails:[NSImage]=[]
for n in 0..<doc.pageCount {
 guard let page=doc.page(at:n) else {continue}
 let box=page.bounds(for:.mediaBox)
 let w=Int(box.width*scale), h=Int(box.height*scale)
 let bitmap=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:w,pixelsHigh:h,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
 NSGraphicsContext.saveGraphicsState()
 NSGraphicsContext.current=NSGraphicsContext(bitmapImageRep:bitmap)
 let ctx=NSGraphicsContext.current!.cgContext
 ctx.setFillColor(NSColor.white.cgColor);ctx.fill(CGRect(x:0,y:0,width:w,height:h))
 ctx.scaleBy(x:scale,y:scale)
 page.draw(with:.mediaBox,to:ctx)
 NSGraphicsContext.restoreGraphicsState()
 let png=bitmap.representation(using:.png,properties:[:])!
 let file=String(format:"page-%02d.png",n+1)
 try png.write(to:URL(fileURLWithPath:out+"/"+file))
 let string=page.string ?? ""
 text+="\n--- PAGE \(n+1) ---\n"+string+"\n"
 records.append(["page":n+1,"width":box.width,"height":box.height,"textCharacters":string.count,"image":file])
 thumbnails.append(NSImage(data:png)!)
}
let tw=420, th=760, gap=14, cols=3, rows=(doc.pageCount+2)/3
let contact=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:cols*(tw+gap)+gap,pixelsHigh:rows*(th+gap)+gap,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
NSGraphicsContext.saveGraphicsState();NSGraphicsContext.current=NSGraphicsContext(bitmapImageRep:contact)
NSColor.lightGray.setFill();NSRect(x:0,y:0,width:contact.pixelsWide,height:contact.pixelsHigh).fill()
for (i,img) in thumbnails.enumerated(){let x=gap+(i%cols)*(tw+gap),y=contact.pixelsHigh-gap-th-(i/cols)*(th+gap);img.draw(in:NSRect(x:x,y:y,width:tw,height:th))}
NSGraphicsContext.restoreGraphicsState()
try contact.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:out+"/contact.png"))
try text.write(toFile:out+"/extracted-text.txt",atomically:true,encoding:.utf8)
try JSONSerialization.data(withJSONObject:["pages":doc.pageCount,"records":records],options:.prettyPrinted).write(to:URL(fileURLWithPath:out+"/pages.json"))
print("Rendered \(doc.pageCount) PDF pages at \(scale)x")
