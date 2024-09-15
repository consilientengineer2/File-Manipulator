import sys
import os
import shutil

# 引数
if len(sys.argv) < 3:
    print(sys.argv)
    print("引数が足りません")
    sys.exit()

inputpath = sys.argv[1]
outputpath = sys.argv[2]

# 読み込みファイルの存在チェック
if not os.path.exists(inputpath):
    print("変換元のファイルが存在しません")
    sys.exit()

shutil.copy(inputpath, outputpath)



