# AVIF_generator

## 介绍

AVIF生成器是一个简单的Web应用，可以帮助用户将图像文件转换为AVIF格式。AVIF是一种新型的图像文件格式，它具有更高的压缩比和更好的性能。

## 功能

* 支持将图像和视频转为AVIF格式
* 视频将生成AVIF格式的动态图片
* 支持预览和下载转换后的AVIF文件

## 截图

![界面截图](/20241104165818.avif)

## 使用方法

1. 点击"选择文件"按钮选择要转换的图像文件。
2. 点击"上传文件"按钮上传图像文件到服务器。
3. 服务器将图像文件转换为AVIF格式并生成预览图。
4. 点击"下载AVIF"按钮下载转换后的AVIF文件。

## 技术栈

* 前端：Vue.js、Element Plus
* 后端：Flask、Python
* FFmpeg：用于图像格式转换

## 安装和部署

1. 克隆代码库：`git clone https://github.com/username/avif-generator.git`
2. 安装依赖包：`pip install Flask`
3. 安装ffmpeg并添加到环境变量：[https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z)
4. 启动后端服务器：`python app.py`
5. 在浏览器中打开应用：`http://localhost:5000`


