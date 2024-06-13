


# 典型使用场景Tips
## ~~配置镜像加速~~
20240606之后，应该加速的方式都逐步不可用了  
获取阿里云镜像[加速地址](https://cr.console.aliyun.com/cn-hangzhou/instances/mirrors)  
根据提示配置镜像加速  
```bash
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://xxxx.mirror.aliyuncs.com"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

将**镜像信息**部分的的两个文件保存到本地  
**然后愉快的使用以下脚本跑起来**
## 联网环境拉取到本地并且tag为原始tag
适用于无法拉取外网地址或拉取外网地址缓慢

```shell
img=$(cat dockerhub-image.yml)
for i in ${img[@]}
do
    tagName=$(echo $i | awk -F "/" '{print $NF}');
    docker pull $i;
    sourceTag=$(cat images-init.yml | grep $tagName);
    docker tag $i $sourceTag;
done
```


## 联网环境拉取到本地打包

适用于内网环境需要将公网镜像打包到内网镜像仓库
```shell
img=$(cat dockerhub-image.yml)
for i in ${img[@]}
do
    tagName=$(echo $i | awk -F "/" '{print $NF}');
    filePrefix=$(echo $tagName | awk -F ":" '{print $1}');
    fileSuffix=$(echo $tagName | awk -F ":" '{print $NF}');
    fileName=$filePrefix--$fileSuffix.gz
    docker pull $i;
    mkdir localImage || echo 0
    docker save $i -o localImage/$fileName 
done
    # tar -zcf localImage.tar.gz localImage
```

## 将本地镜像包解压并且上传到私有仓库

```shell
# 将压缩好的镜像文件放在localImage目录
img=$(ls localImage)
# 本地仓库信息 LOCAL_REGISTRY 和 LOCAL_NAMESPACE 需要指定
# 如镜像local.harbor.dev/ingress-nginx/kube-webhook-certgen:v1.1.1
# LOCAL_REGISTRY则为：local.harbor.dev
# LOCAL_NAMESPACE则为：ingress-nginx
LOCAL_REGISTRY=
LOCAL_NAMESPACE=
# 首先解压镜像
for i in ${img[@]}
do
    docker load -i $i；
done

# 解压完成后，重新打tag并且上传指定仓库，需要确保需要有对应仓库的权限
img=$(cat dockerhub-image.yml)
for i in ${img[@]}
do
    tagName=$(echo $i | awk -F "/" '{print $NF}');
    specialTag=$LOCAL_REGISTRY/$LOCAL_NAMESPACE/$tagName;
    docker tag $i $specialTag;
    docker push $specialTag;
done
```
