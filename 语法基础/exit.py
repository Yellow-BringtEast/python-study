import sys
import os

# 来自site module
# raise 了一个 SystemExit
# 但python并不总是在打开是自动 import site
# 推荐在python命令行中使用
quit()
exit()

# 同样相当于 raise 了一个 SystemExit
# 正式代码中推荐使用
# 同前2种方式一样均可以被 try..except.. 处理
sys.exit()

# 不能被 try..except.. 处理
# 不推荐在主进程使用
os._exit(0)
