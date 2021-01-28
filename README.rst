mirai-python-sdk
================

基于 kuriyama（Python SDK v3）的修改版本

这是什么?
~~~~~~~~~

以 OICQ(QQ) 协议驱动的高性能机器人开发框架
`Mirai <https://github.com/mamoe/mirai>`__ 的 Python 接口, 通过其提供的
``HTTP API`` 与无头客户端 ``mirai`` 交互.

开始使用
~~~~~~~~

从 Pypi 安装
^^^^^^^^^^^^

.. code:: bash

    pip install kuriyama-lxnet

开始开发
^^^^^^^^

由于 ``python-mirai`` 依赖于 ``mirai`` 提供的 ``mirai-http-api`` 插件,
所以你需要先运行一个 ``mirai-core`` 或是 ``mirai-console``
实例以支撑你的应用运行.

仓库地址: https://github.com/Lxns-Network/mirai-python-sdk

依赖版本
~~~~~~~~

-  mirai-core-all *v2.1.1*：https://github.com/mamoe/mirai
-  mirai-api-http：https://github.com/project-mirai/mirai-api-http

许可证
~~~~~~

我们使用
`GNU AGPLv3 <https://choosealicense.com/licenses/agpl-3.0/>`__
作为本项目的开源许可证, 而由于原项目
`mirai <https://github.com/mamoe/mirai>`__ 同样使用了 ``GNU AGPLv3``
作为开源许可证, 因此你在使用时需要遵守相应的规则.
