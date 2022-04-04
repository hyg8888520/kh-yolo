# kh-yolo
## Features

- 这是一个简单的目标检测，你可以使用yolov5、ssd等算法获得onnx权重来使用它
- best.onnx为本人制作的训练集所训练的模型，它并不完美，如果你有更好的模型也可以替换它
- 它可以检测人脸与戴口罩的人脸


## Tech

- 它需要这些库来支持:

- [numpy](https://github.com/numpy/numpy)
- [opencv](https://github.com/opencv)

> 你可以点击以访问它们的GitHub仓库


## Usage

- 如果你有自己的onnx权重，请放到weight文件夹，并在main.py中把best.onnx改为你自己的模型
- 图片可以放在input中，也可以在运行时输入存储路径，或者使用摄像头
- 输出的结果放在output中





## Images
> 下面是一些output

![image](https://github.com/hyg8888520/kh-yolo/tree/main/images%20-%20result/02d6dc923c0d21e923d71fb5ca22c135.jpeg)
![image](https://github.com/hyg8888520/kh-yolo/tree/main/images%20-%20result/175a246c769747911130c9c96e4e118e.jpeg)
![image](https://github.com/hyg8888520/kh-yolo/tree/main/images%20-%20result/2ae33fd854e6325b6a0c2aded96811d2.jpeg)
![image](https://github.com/hyg8888520/kh-yolo/tree/main/images%20-%20result/2be1eae9c106d2255ff88bfeb0bd06f3.jpeg)
![image](https://github.com/hyg8888520/kh-yolo/tree/main/images%20-%20result/2f86fbd36618afe6cfd778d3acc4bf02.jpeg)
![image](https://github.com/hyg8888520/kh-yolo/tree/main/images%20-%20result/5e6166af217b94cfe8b3d76ad255d018.jpeg)
![image](https://github.com/hyg8888520/kh-yolo/tree/main/images%20-%20result/7c582300de0eafa838443bc003170f6b.jpeg)
![image](https://github.com/hyg8888520/kh-yolo/tree/main/images%20-%20result/7c582300de0eafa838443bc003170f6b.jpeg)

