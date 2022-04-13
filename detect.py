import yolov5_dnn
from yolov5_torch_dnnload import mult_test

if __name__ == "__main__":
    path_i = 0
    print("是否使用摄像头?" +"\n" "Y/N")
    sele = input()
    if sele == 'Y':video = 1
    elif sele == 'N':
        video = 0
        print("是否使用自定义图片地址?" +"\n" "Y/N")
        sele1 = input()
        if sele1 == 'Y':path_i = input()
    if (path_i):
        input_path = path_i
    else:
        input_path = r'./input'

    onnx_path = r'.\weights\best.onnx'
    save_path = r'./output'

    #video=True代表开启摄像头
    mult_test(onnx_path, input_path, save_path, video=video)
    #yolov5_dnn.mult_test(onnx_path, input_path, save_path, video=0) # opencv