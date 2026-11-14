import Foundation
import AppKit
import PDFKit
let a=CommandLine.arguments
let doc=PDFDocument(url:URL(fileURLWithPath:a[1]))!
let page=doc.page(at:45)!,box=page.bounds(for:.mediaBox),scale:CGFloat=1.25
let w=Int(box.width*scale),h=Int(box.height*scale)
let b=NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:w,pixelsHigh:h,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0)!
NSGraphicsContext.saveGraphicsState();NSGraphicsContext.current=NSGraphicsContext(bitmapImageRep:b)
let c=NSGraphicsContext.current!.cgContext;c.setFillColor(NSColor.white.cgColor);c.fill(CGRect(x:0,y:0,width:w,height:h));c.scaleBy(x:scale,y:scale);page.draw(with:.mediaBox,to:c);NSGraphicsContext.restoreGraphicsState()
try b.representation(using:.png,properties:[:])!.write(to:URL(fileURLWithPath:a[2]));print("Rendered official Q&A page46")
