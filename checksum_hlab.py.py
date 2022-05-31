import hashlib


print("""

           |    |              _.-7
           |\.-.|             ( ,(_
           | a a|              \\  \,
           ) ["||          _.--' \  \\
        .-'  '-''-..____.-'    ___)  )\
       F   _/-``-.__;-.-.--`--' . .' \_L_
      |   l  {~~} ,_\  '.'.      ` __.' )\
      (    -.;___,;  | '- _       :__.'( /
      | -.__ _/_.'.-'      '-._ .'      \\
      |     .'   |  -- _                 '\,
      |  \ /--,--{ .    '---.__.       .'  .'
      J  ;/ __;__]. '.-.            .-' )_/
      J  (-.     '\'. '. '-._.-.-'--._ /
      |  |  '. .' | \'. '.    ._       \
      |   \   T   |  \  '. '._  '-._    '.
      F   J   |   |  '.    .  '._   '-,_.--`
      F   \   \   F .  \    '.   '.  /
     J     \  |  J   \  '.   '.    '/
     J      '.L__|    .   \    '    |
     |   .    \  |     \   '.   '. /
     |    '    '.|      |    ,-.  (
     F   | ' ___  ',._   .  /   '. \
     F   (.'`|| (-._\ '.  \-      '-\
     \ .-'  ( L `._ '\ '._ (
snd  /'  |  /  '-._\      ''\
         `-'

    """)
checksum = input("MD5 checksum: ") 
filename = input("Ruta del fichero: ")
with open(filename, "rb") as f:
    bytes = f.read()
    readable_hash = hashlib.md5(bytes).hexdigest()
    print("---------------------------------------")
    print(checksum)
    print(readable_hash)
    print("======> RESULTADO ")
    if readable_hash == checksum:
        print("El fichero parece seguro")
    else:
        print("El fichero parece sospechoso")
    print("---------------------------------------")
