# baidu-dropbox-sniffer
百度网盘文件链接嗅探器

## 1. 项目结构说明
- lib/

	登录认证以及网盘相关操作
- out/

	结果文件
- main.py

	主程序入口
- requirements.txt

	python依赖库

## 2. 项目运行说明
### 1. 搭建python开发环境
- 推荐安装pyenv和pyenv-virtualenv, 完全隔离不同项目的开发环境.
- pyenv的安装, 请参考[https://github.com/yyuu/pyenv](https://github.com/yyuu/pyenv)
- pyenv-virtualenv的安装, 请参考[https://github.com/yyuu/pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)
- 当然, 你也可以直接使用系统默认安装的python进行操作, 不过平时要养成良好的习惯, 推荐使用前面的方式操作.
- 安装python虚拟环境

  		pyenv virtualenv 2.7.6 env_baidu_dropbox_sniffer_2.7.6        // 2.7.6: 虚拟环境的python版本, env_baidu_dropbox_sniffer_2.7.6: 虚拟环境

  其中, 安装不同版本的python:

	  pyenv install 2.7.6         // 指定版本号

### 2. 运行项目

      pyenv activate env_baidu_dropbox_sniffer_2.7.6             // 切换到项目对应的虚拟环境
      pip install -r requirements.txt                 			// 安装依赖库
      python main.py                                  			// 运行项目

## 3. TODO
- auth认证模块实现
- sign3, sign1自动获取
- dlinks缓存(百度网盘默认链接８小时失效)

## 3. 如何贡献
- fork
- modify
- pull request
