#!/usr/bin/env python
# coding: utf-8

# Copyright 2018 Kazme Egawa. All Rights Reserved.
#

import serial
from datetime import datetime

ser = serial.Serial("/dev/ttyS0", baudrate = 9600, timeout = 2)

# [START def_sheetdasu]
def hikikaekendasu(num):
    ser.write(chr(0x1C)) # 0x1C
    ser.write(chr(0x57)) # 0x57
    ser.write(chr(0x01)) # 0x00 or 01
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x0C)) # 0x00 - 0x2F
    ser.write("百姓一揆#1\r")
    ser.write(chr(0x1C)) # 0x1C
    ser.write(chr(0x57)) # 0x57
    ser.write(chr(0x00)) # 0x00 or 01

    ser.write(chr(0x12)) # 0x12
    ser.write(chr(0x53)) # 0x53
    ser.write(chr(0x01)) # 0x00 or 01
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x06)) # 0x00 - 0x2F
    ser.write("日本橋馬喰町\r\r")
    ser.write(chr(0x12)) # 0x12
    ser.write(chr(0x53)) # 0x53
    ser.write(chr(0x00)) # 0x00 or 01

    ser.write("\r");  # Line Feed
    date = datetime.today().strftime("%Y年%m月%d日 %H:%M")
    ser.write(date)
    ser.write("\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x22)) # 0x00 - 0x2F
    ser.write("水呑百姓東京\r\r\r\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x28)) # 0x00 - 0x2F
    ser.write("様\r")

    ser.write("-----------------------------\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x57)) # 0x57
    ser.write(chr(0x01)) # 0x00 or 01
    ser.write("引換券\r\r")
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x57)) # 0x57
    ser.write(chr(0x00)) # 0x00 or 01

    ser.write(" 　　　　　　　数量 1\r\r\r")

    ser.write("\r（内注意　２階の物販コーナーへ商品を引き換えに行ってください）\r\r\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x68)) # 0x68
    ser.write(chr(0x00)) # 0x00 or 01 or 02 or 03
    ser.write(chr(0x12)) # 0x12
    ser.write(chr(0x53)) # 0x53
    ser.write(chr(0x01)) # 0x00 or 01
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x1D)) # 0x00 - 0x2F
    ser.write("レシート No.00\r")
    ser.write(num)
    ser.write("\r")
    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x68)) # 0x68
    ser.write(chr(0x01)) # 0x00 or 01 or 02 or 03
    ser.write(chr(0x12)) # 0x12
    ser.write(chr(0x53)) # 0x53
    ser.write(chr(0x00)) # 0x00 or 01

    ser.write("-----------------------------\r")

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x04)) # 0x00 - 0x2F
    ser.write("》》》 百姓一揆#1《《《\r")

    ser.write("百姓一揆#1 にお越しいただきありがとうございました！\r")
    ser.write("\rmizunomi.tokyo\r\r")

    # Barcode Print
    # ser.write(chr(0x1D))
    # ser.write(chr(0x68))
    # ser.write(chr(0x01))
    # ser.write(chr(0x1D))
    # ser.write(chr(0x78))
    # ser.write(chr(0x4C))
    # ser.write(chr(0x16))
    # ser.write("https://mizunomi.tokyo")   # DATA
    # ser.write("\r\r\r\r\r\r");  # Line Feed

    ser.write(chr(0x1B)) # 0x1B
    ser.write(chr(0x6C)) # 0x6C
    ser.write(chr(0x0D)) # 0x00 - 0x2F
    # QRcode Print
    ser.write(chr(0x1D))
    ser.write(chr(0x79))
    ser.write(chr(0x01))
    ser.write(chr(0x1D))
    ser.write(chr(0x78))
    ser.write(chr(0x4C))
    ser.write(chr(0x16))
    ser.write("https://mizunomi.tokyo")   # DATA
    ser.write("\r\r\r\r\r\r");  # Line Feed
# [END def_sheetdasu]

while True:
    num = raw_input('Reciept Number: ')
    print(num)
    hikikaekendasu(num)
