import sys
import os

# 引数
if len(sys.argv) < 3:
    print(sys.argv)
    print("引数が足りません")
    sys.exit()

def isint(s):  # 整数値を表しているかどうかを判定
    try:
        int(s, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True

inputpath = sys.argv[1]
duplicate_count = sys.argv[2]

# 読み込みファイルの存在チェック
if not os.path.exists(inputpath):
    print("変換元のファイルが存在しません")
    sys.exit()

# 複製回数のチェック
if not isint(duplicate_count):
    print("複製回数が不正です")

with open(inputpath) as r:
    contents = r.read()

new_contensts = ""

for i in range(int(duplicate_count)):
    new_contensts += contents  

with open(inputpath, "a") as w:
    w.write(new_contensts)