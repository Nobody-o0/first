#FastAPI是一个现代、快速、高性能的web框架，用于基于标准的Python类型提示构建API接口服务。
#FastAPI官网：https:j//fastapi.org.cn

#API接口:应用程序编程接口(Application Programming Interface)，就是对外提供的功能入口，供别人来调用（比如查询天气的APi接口）


#FastAPI使用步骤：
'''
1.导入FastAPI
2.创建FastAPI实例对象
3，创建路径操作函数
4.运行FastAPI服务
'''

from fastapi import FastAPI#导入FastAPI

#创建fastapi实例
app = FastAPI()

#定义功能接口--->该接口的返回值就是该api接口的返回的数据，接口访问路径是/,请求方式是GET
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def users():
    return [
        {"id":1,"name":"张三"},
        {"id":2,"name":"李四"},
        {"id":3,"name":"王五"}
    ]

#通过命令行运行服务有两种方法：
'''
1.在终端中输入   fastapi dev "xxxxx"便可以运行服务
2.在终端输入     uvicorn xxxx:app --reload  便可运行服务
'''

#也可以直接在代码中写出服务运行的方法，就如：
if __name__ == '__main__':
    import uvicorn
    #uvicron:Python中的轻量级web服务器
    uvicorn.run(app, host="127.0.0.1", port=8000)
    #格式为：uvicron.run("要启用的FastAPI实例","允许访问此API实例的主机编号","设置可访问的主机编号的端口号")







