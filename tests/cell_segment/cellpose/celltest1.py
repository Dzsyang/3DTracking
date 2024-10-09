# import cellpose.models
# import numpy as np  
# import matplotlib.pyplot as plt  
# import cellpose  
# import cv2

# cap = cv2.VideoCapture("normalized.avi")
# if not cap.isOpened():  
#     print("无法打开视频文件")  
#     exit() 

# # 逐帧读取视频  
# #while True:  
# ret, image = cap.read()  # ret是一个布尔值，表示是否成功读取帧；frame是读取的帧
# if not ret:  
#     print("视频结束")  
#     #break

# # 转换为float32并归一化到[0, 1](黑白处理)
# if image.dtype != np.float32:
#     image = image.astype(np.float32) / 255.
# print(0)


# # 初始化模型（使用预训练的通用模型）  
# model = cellpose.models.Cellpose(gpu=False, model_type='cyto')  # gpu=True 如果你的机器有NVIDIA GPU  
# print(1)
# # # 如果你的图像是彩色的并且包含多个通道，你可能需要指定channels参数  
# # # 例如，对于RGB图像，channels=[0, 0, 0] 将使用所有通道（但这不是最佳实践，通常选择特定通道）  
# # # channels参数也取决于你的图像和模型  
# # channels = [0, 0, 0]  # 假设我们在这里使用所有RGB通道（但可能需要调整）  
  
# # 运行模型进行预测  
# masks, flows, styles, diams = model.eval(image, diameter=25)  
  
# # # masks现在包含了分割结果  
# # # 你可以通过查看masks来检查分割效果，或者将其可视化  
  
# # # 简单的可视化示例  
# # fig, axs = plt.subplots(1, 2)  
# # axs[0].imshow(image)  
# # axs[0].set_title('Original Image')  
# # axs[0].axis('off')  
# # axs[1].imshow(masks[:, 0], cmap='gray')  # 假设我们只关心第一个通道（通常是细胞掩码）  
# # axs[1].set_title('Cellpose Segmentation')  
# # axs[1].axis('off')  
# # plt.show()

# # 可视化分割结果
# visualization = image.copy()
# for mask in masks:
#     visualization[mask > 0] = [0, 255, 0]  # 将细胞轮廓标记为绿色

# # 显示可视化结果
# cv2.imshow('Cell Segmentation', visualization)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(2)

# cap.release()

# print(3)

# # 释放资源并关闭所有窗口

# '''cap.release()
# cv2.destroyAllWindows()'''


import cv2
from cellpose import models
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('111.png')

# 检查图像是否成功读取
if image is None:
    print("Error: Unable to read the image.")
    exit()

# 转换为灰度图像（如果是彩色图像）
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 创建模型
model = models.Cellpose(gpu=False, model_type='cyto')

# 运行细胞分割
masks, _, _, _ = model.eval(gray_image)
masks = masks.T

# 可视化分割结果
visualization = np.zeros_like(image)  # 创建与原始图像尺寸相同的数组，用于可视化结果
for mask in masks:
    # 将分割掩码应用于可视化结果
    visualization[mask > 0] = [0, 255, 0]  # 将细胞轮廓标记为绿色

print(1)

# 显示可视化结果
# 显示图像
plt.imshow(visualization)
plt.title('Cell Segmentation')
plt.axis('off')  # 关闭坐标轴
plt.show()
