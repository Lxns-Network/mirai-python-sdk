# mirai-python-sdk
基于 kuriyama（Python SDK v3）的修改版本
### 依赖版本
- mirai-core-qqandroid *v1.2.2*：https://github.com/mamoe/mirai
- mirai-api-http *v1.8.0*：https://github.com/project-mirai/mirai-api-http
### 语音组件
#### 第三方依赖
ffmpeg 环境：https://ffmpeg.org/
#### 使用方法
MessageChain：`Voice.fromFileSystem(Path)`
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

if __name__ == "__main__":
    app.run()
```
