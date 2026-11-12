#模块导入方式：
# Python导入模块的5种语法
# 1. import 模块名
# 样例：import random, os
# 调用方式：模块名.功能名
# 示例调用：random.randint(10, 100)

# 2. import 模块名 as 别名
# 样例：import random as rd
# 调用方式：别名.功能名
# 示例调用：rd.randint(10, 100)

# 3. from 模块名 import 功能名
# 样例：from random import randint,choice
# 调用方式：功能名
# 示例调用：randint(10, 100)

# 4. from 模块名 import 功能名 as 别名
# 样例：from random import randint as rint
# 调用方式：别名
# 示例调用：rint(10, 100)

# 5. from 模块名 import *，导入的是该模块中的所有功能
# 样例：from random import *
# 调用方式：功能名
# 示例调用：randint(10, 100)




import random as rb
#导入模块random且为他设置别名rb

a=rb.randint(1,100)
print(a)



