# -*- coding:utf8 -*-
 
import os
import sys
import zlib
import time
import base64
import marshal
import py_compile
 
if sys.version_info[0] == 2:
    _input = "raw_input('%s')"
elif sys.version_info[0] == 3:
    _input = "input('%s')"
else:
    sys.exit("\n Your Python Version is not Supported!")

# Encoding Functions
zlb = lambda in_: zlib.compress(in_)
b16 = lambda in_: base64.b16encode(in_)
b32 = lambda in_: base64.b32encode(in_)
b64 = lambda in_: base64.b64encode(in_)
mar = lambda in_: marshal.dumps(compile(in_, '<x>', 'exec'))
note = "# Encrypted By Princ Inside\n # Github : https://github.com/PrinceTricker02/KARAN"

# New ASCII Logo
logo = ("""
 __       __  _______         _______   _______   ______  __    __   ______   ________ 
|  \     /  \|       \       |       \ |       \ |      \|  \  |  \ /      \ |        \ 
| $$\   /  $$| $$$$$$$\      | $$$$$$$\| $$$$$$$\ \$$$$$$| $$\ | $$|  $$$$$$\| $$$$$$$$ 
| $$$\ /  $$$| $$__| $$      | $$__/ $$| $$__| $$  | $$  | $$$\| $$| $$   \$$| $$__     
| $$$$\  $$$$| $$    $$      | $$    $$| $$    $$  | $$  | $$$$\ $$| $$      | $$  \    
| $$\$$ $$ $$| $$$$$$$\      | $$$$$$$ | $$$$$$$\  | $$  | $$\$$ $$| $$   __ | $$$$$    
| $$ \$$$| $$| $$  | $$      | $$      | $$  | $$ _| $$_ | $$ \$$$$| $$__/  \| $$_____  
| $$  \$ | $$| $$  | $$      | $$      | $$  | $$|   $$ \| $$  \$$$ \$$    $$| $$     \ 
 \$$      \$$ \$$   \$$       \$$       \$$   \$$ \$$$$$$ \$$   \$$  \$$$$$$  \$$$$$$$$ 
""")

def menu():  # Program Menu
    print("""
 [01] Encode Marshal
 [02] Encode Zlib
 [03] Encode Base16
 [04] Encode Base32
 [05] Encode Base64
 [06] Encode Zlib, Base16
 [07] Encode Zlib, Base32
 [08] Encode Zlib, Base64
 [09] Encode Marshal, Zlib
 [10] Encode Marshal, Base16
 [11] Encode Marshal, Base32
 [12] Encode Marshal, Base64
 [13] Encode Marshal, Zlib, Base16
 [14] Encode Marshal, Zlib, Base32
 [15] Encode Marshal, Zlib, Base64
 [16] Simple Encode
 [17] Exit
""")

class FileSize:
    def datas(self, z):
        for x in ['Byte', 'KB', 'MB', 'GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z, x)
            z /= 1024.0

    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [-] Encoded File Size : %s\n" % self.datas(dts))

def Encode(option, data, output):
    loop = int(eval(_input % " [-] Encode Count : "))
    encoding_methods = {
        1: ("mar(data.encode('utf8'))[::-1]", "_ = lambda __ : __import__('marshal').loads(__[::-1]);"),
        2: ("zlb(data.encode('utf8'))[::-1]", "_ = lambda __ : __import__('zlib').decompress(__[::-1]);"),
        3: ("b16(data.encode('utf8'))[::-1]", "_ = lambda __ : __import__('base64').b16decode(__[::-1]);"),
        4: ("b32(data.encode('utf8'))[::-1]", "_ = lambda __ : __import__('base64').b32decode(__[::-1]);"),
        5: ("b64(data.encode('utf8'))[::-1]", "_ = lambda __ : __import__('base64').b64decode(__[::-1]);"),
        6: ("b16(zlb(data.encode('utf8')))[::-1]", "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"),
        7: ("b32(zlb(data.encode('utf8')))[::-1]", "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"),
        8: ("b64(zlb(data.encode('utf8')))[::-1]", "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"),
        9: ("zlb(mar(data.encode('utf8')))[::-1]", "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));"),
        10: ("b16(mar(data.encode('utf8')))[::-1]", "_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]));"),
        11: ("b32(mar(data.encode('utf8')))[::-1]", "_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]));"),
        12: ("b64(mar(data.encode('utf8')))[::-1]", "_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]));"),
        13: ("b16(zlb(mar(data.encode('utf8'))))[::-1]", "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])));"),
        14: ("b32(zlb(mar(data.encode('utf8'))))[::-1]", "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));"),
        15: ("b64(zlb(mar(data.encode('utf8'))))[::-1]", "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"),
    }

    if option not in encoding_methods:
        sys.exit("\n Invalid Option!")

    xx, heading = encoding_methods[option]

    for _ in range(loop):
        try:
            data = "exec((_)(%s))" % repr(eval(xx))
        except TypeError as e:
            sys.exit(" TypeError : " + str(e))

    with open(output, 'w') as f:
        f.write(note + heading + data)

def MainMenu():
    try:
        os.system('clear')
        os.system('xdg-open https://github.com/PrinceTricker02'); time.sleep(5)
        print(logo)
        menu()
        option = int(eval(_input % " [-] Option : "))

        if option == 17:
            sys.exit("\n Thanks For Using Princ Tool")
        if option not in range(1, 17):
            sys.exit('\n Invalid Option !')

        file = eval(_input % " [-] File Name : ")
        data = open(file).read()
        output = file.lower().replace('.py', '') + '_enc.py'

        Encode(option, data, output)
        print("\n [-] Successfully Encrypted %s" % file)
        print(" [-] Saved as %s" % output)
        FileSize(output)

    except KeyboardInterrupt:
        sys.exit("\n User Interrupted!")

if __name__ == "__main__":
    MainMenu()
