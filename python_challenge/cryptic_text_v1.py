import sys

user_input = None

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    print(f"Text to decrypt: {user_input}")
else:
    print("No input entered")

# Problem's main variable
cryptic_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "

# Handling translation
table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
if user_input:
    result = user_input.translate(table)
else:
    result = cryptic_text.translate(table)

print(result)