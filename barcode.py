import treepoem
import cv2
import PIL
image = treepoem.generate_barcode(
    barcode_type = (input("select type: qrcode, interleaverd2of5, code128, isbn, micropdf417,ean13(must be 11-12 chars) ")),  # One of the BWIPP supported codes.
    # barcode_type="qrcode",  
    # One of the BWIPP supported codes.
    # barcode_type="interleaved2of5",  # One of the BWIPP supported codes.
    # barcode_type="code128",  # One of the BWIPP supported codes.
    #    # barcode_type="isbn",  # One of the BWIPP supported codes.
    #    # data="978-3-16-148410-0",
    #   barcode_type="code128",  # One of the BWIPP supported codes.
    #   barcode_type="micropdf417",  # One of the BWIPP supported codes.
    #   barcode_type="ean13",  # One of the BWIPP supported codes.
    data=(input('Type something here...')),
    
)
img = image.convert("1").save("output.png")
im = PIL.Image.open(r'output.png') 
im.show()
