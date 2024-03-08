import qrcode

name = input("Write your name: ")
phone = input("write your phone number: ")
qr = qrcode.make(name + "," + phone)
qr.save("myQR.png")
