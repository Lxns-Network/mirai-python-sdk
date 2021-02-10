# mirai-python-sdk
基于 kuriyama（Python SDK v3）的修改版本

### 这是什么?
以 OICQ(QQ) 协议驱动的高性能机器人开发框架 [Mirai](https://github.com/mamoe/mirai) 的 Python 接口, 通过其提供的 `HTTP API` 与无头客户端 `Mirai` 交互.

### 开始使用
#### 从 Pypi 安装
``` bash
pip install kuriyama-lxnet
```

#### 开始开发

由于 `python-mirai` 依赖于 `mirai` 提供的 `mirai-http-api` 插件, 所以你需要先运行一个 `mirai-core` 或是 `mirai-console` 实例以支撑你的应用运行.

仓库地址: https://github.com/Lxns-Network/mirai-python-sdk 

### 依赖版本
- mirai-core-all *v2.1.1*：https://github.com/mamoe/mirai
- mirai-api-http *v1.9.7*：https://github.com/project-mirai/mirai-api-http
### 语音组件
#### 第三方依赖
ffmpeg 环境：https://ffmpeg.org/
#### 使用方法
MessageChain：`Voice.fromFileSystem(Path, convert_type="silk")`
### 示例
```python
from mirai import Mirai, Plain, MessageChain, Friend, Group, Member, Source, BotInvitedJoinGroupRequestEvent
import asyncio

app = Mirai(
    host = "127.0.0.1",
    port = "8880",
    authKey = "INITKEY",
    qq = "114514",
    websocket = True
)

@app.receiver("FriendMessage")
async def _(app: Mirai, friend: Friend, message: MessageChain):
    pass

@app.receiver("GroupMessage")
async def _(app: Mirai, group: Group, member: Member, message: MessageChain, source: Source):
    await app.sendGroupMessage(group, [
            Plain(text="收到消息：" + message.toString())
        ], quoteSource=source)
    return True

@app.receiver("BotInvitedJoinGroupRequestEvent")
async def _(app: Mirai, event: BotInvitedJoinGroupRequestEvent):
    await app.respondRequest(event, 1) # 自动同意入群邀请
    return True

@app.receiver("AppInitEvent")
async def _(app: Mirai):
    print("应用初始化完成，您可以在此直接获取到 app")

if __name__ == "__main__":
    app.run()
```

### 许可证
我们使用 [`GNU AGPLv3`](https://choosealicense.com/licenses/agpl-3.0/) 作为本项目的开源许可证, 而由于原项目 [`mirai`](https://github.com/mamoe/mirai) 同样使用了 `GNU AGPLv3` 作为开源许可证, 因此你在使用时需要遵守相应的规则.  
