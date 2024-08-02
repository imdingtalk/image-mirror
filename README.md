

# image-mirror

![workflow build](https://github.com/imdingtalk/image-mirror/actions/workflows/image-mirror.yml/badge.svg)
[![Version](https://img.shields.io/github/v/release/imdingtalk/image-mirror)](https://github.com/imdingtalk/image-mirror/releases)
[![License](https://img.shields.io/github/license/imdingtalk/image-mirror)](https://www.apache.org/licenses/LICENSE-2.0.html)

`image-mirror` 是一个帮助加速下载某些难以下载的镜像的工具，可以加速下载各国外大厂的某些无法下载的镜像

## Features

- 支持公网所有基于Docker Registry V2搭建的docker镜像仓库同步
- 基于上一条，除了gcr.io , k8s.gcr.io , registry.k8s.io , quay.io, ghcr.io仓库可以加速外，公网的公开仓库大概都可以
- ...

## 使用

### fork 使用(推荐)

- 广而告之: 阿里云目前提供个人版镜像仓库，限额`3`个`namespace`,`300`个镜像。对于个人足够用了，所以我个人推荐是`fork`使用，把镜像同步到自己的个人仓库,自己个人镜像也可以`push`到上面


1. fork 本仓库，然后在仓库设置中打开`issue`功能  
2. 设置自己的目标仓库信息  
![image](https://github.com/imdingtalk/image-mirror/assets/16778873/a83b8765-3bd1-4391-afb3-cd8d4bc4718d)
![image](https://github.com/imdingtalk/image-mirror/assets/16778873/b4623fca-43c2-4f55-bfb1-cef2e949fb93)
比如我们要同步一个外部镜像到`registry.cn-hangzhou.aliyuncs.com/imdingtalk/kube-apiserver:v1.27.12`

#### 需要设置一些变量 `variables`  
- **TARGET_NAMESPACE:** 目标`NAMESPACE`,该例子中应该设置为`imdingtalk`  
- **TARGET_REGISTRY:** 目标仓库，该例子中应该设置为`registry.cn-hangzhou.aliyuncs.com`  
- **TARGET_REGISTRY_USER:** 目标仓库的用户名 
 
#### 一些`secrets`
- **TARGET_REGISTRY_PASSWORD:** 目标仓库的密码

该例子中，需要确保使用目标仓库的用户名和密码，使用命令 `docker login registry.cn-hangzhou.aliyuncs.com`能够成功登录  
4. 按照直接使用的方式在自己的仓库提交issue  

### 直接使用

提交一个issue即可，issue内容为你无法正常下载的镜像，[示例](https://github.com/imdingtalk/image-mirror/issues/30)如下：  
![image](https://github.com/imdingtalk/image-mirror/assets/16778873/b1778053-c251-4003-ad86-caa8637b6b76)

![image](https://github.com/imdingtalk/image-mirror/assets/16778873/18609b09-f41a-46e9-a240-d7eddd925b53)

就会触发GitHub action，同步镜像到 `registry.cn-hangzhou.aliyuncs.com`(默认同步到`imdingtalk`的`NAMESPACE`下)  

GitHub action bot会在action完成后，提示同步成功的镜像


 




## Tools


- [image-syncer](https://github.com/AliyunContainerService/image-syncer)   是一个docker镜像同步工具，可用来进行多对多的镜像仓库同步，支持目前绝大多数主流的docker镜像仓库服务  



