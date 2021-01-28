from setuptools import setup, find_packages
import requests
import os
#os.chdir(r"F:\")


def md_to_rst(from_file, to_file):
    """
    将markdown格式转换为rst格式
    @param from_file: {str} markdown文件的路径
    @param to_file: {str} rst文件的路径
    """
    response = requests.post(
        url='http://c.docverter.com/convert',
        data={'to': 'rst', 'from': 'markdown'},
        files={'input_files[]': open(from_file, 'rb')}
    )

    if response.ok:
        with open(to_file, "wb") as f:
            f.write(response.content)
 

if __name__ == '__main__':
    # md_to_rst("README.md", "README.rst")
    pass


with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="kuriyama-lxnet",
    version='1.1',
    description='A framework for OICQ(QQ, made by Tencent) headless client "Mirai".',
    author='lxnet',
    author_email="personnpc@gmail.com",
    url="https://github.com/NatriumLab/python-mirai",
    packages=find_packages(include=("mirai", "mirai.*")),
    python_requires='>=3.7',
    keywords=["oicq qq qqbot", ],
    install_requires=[
        "aiohttp",
        "pydantic",
        "Logbook",
        "async_lru"
    ],
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: User Interfaces',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent"
    ]
)
