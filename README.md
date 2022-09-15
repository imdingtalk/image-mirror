

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
### 直接使用

使用指定label提交一个issue即可，issue内容为你无法正常下载的镜像，[示例](https://github.com/imdingtalk/image-mirror/issues/14)如下：  


就会出发GitHub action，同步镜像到 `dockerhub`(默认同步到用户 `imdingtalk` 的docker仓库)  

GitHub action bot会在action完成后，提示同步成功的镜像


### fork 使用

1. fork 本仓库，然后在仓库设置中打开`issue`功能  
2. 设置自己的dockerhub仓库信息

3. 按照直接使用的方式在自己的仓库提交issue


## Tools


- [image-syncer](https://github.com/AliyunContainerService/image-syncer)   是一个docker镜像同步工具，可用来进行多对多的镜像仓库同步，支持目前绝大多数主流的docker镜像仓库服务  



