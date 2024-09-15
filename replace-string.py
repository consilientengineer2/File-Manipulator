import sys
import os

# 引数
if len(sys.argv) < 4:
    print(sys.argv)
    print("引数が足りません")
    sys.exit()

inputpath = sys.argv[1]
search_str = sys.argv[2]
replace_str = sys.argv[3]

# 読み込みファイルの存在チェック
if not os.path.exists(inputpath):
    print("変換元のファイルが存在しません")
    sys.exit()

with open(inputpath) as r:
    contents = r.read()
    
new_contents = contents.replace(search_str, replace_str)
print(new_contents)

with open(inputpath, "w") as w:
    w.write(new_contents)