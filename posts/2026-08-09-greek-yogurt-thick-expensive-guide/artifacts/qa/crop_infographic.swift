import Foundation
import CoreGraphics
import ImageIO
import UniformTypeIdentifiers

guard CommandLine.arguments.count == 5,
      let y = Int(CommandLine.arguments[3]),
      let height = Int(CommandLine.arguments[4]) else {
    fputs("usage: crop_infographic.swift INPUT OUTPUT Y HEIGHT\n", stderr)
    exit(2)
}

let input = URL(fileURLWithPath: CommandLine.arguments[1])
let output = URL(fileURLWithPath: CommandLine.arguments[2])
guard let source = CGImageSourceCreateWithURL(input as CFURL, nil),
      let image = CGImageSourceCreateImageAtIndex(source, 0, nil) else {
    fputs("cannot decode input\n", stderr)
    exit(1)
}

let rect = CGRect(x: 0, y: y, width: image.width, height: height)
guard let cropped = image.cropping(to: rect),
      let destination = CGImageDestinationCreateWithURL(
        output as CFURL,
        UTType.png.identifier as CFString,
        1,
        nil
      ) else {
    fputs("cannot create crop\n", stderr)
    exit(1)
}

CGImageDestinationAddImage(destination, cropped, nil)
guard CGImageDestinationFinalize(destination) else {
    fputs("cannot write crop\n", stderr)
    exit(1)
}
