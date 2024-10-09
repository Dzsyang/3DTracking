#for image processing, 1st ruihua
import numpy as np
from PIL import Image

# 定义卷积核
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])

# 读取PNG图像
image_path = "00.png"
input_image = Image.open(image_path)
input_array = np.array(input_image)

# 获取图像尺寸和通道数
height, width, channels = input_array.shape

# 对图像进行边缘填充，以适应卷积核
padded_image = np.pad(input_array, ((1, 1), (1, 1), (0, 0)), mode='constant')

# 创建一个与输入图像相同尺寸的零矩阵，用于存储卷积结果
output_array = np.zeros_like(input_array)

# 执行卷积操作
for y in range(height):
    for x in range(width):
        for c in range(channels):
            # 从输入图像中提取感兴趣的区域
            region = padded_image[y:y+3, x:x+3, c]
            # 计算卷积结果并存储
            output_array[y, x, c] = np.sum(region * kernel)

# 将结果转换为0到255之间的整数
output_array = np.clip(output_array, 0, 255).astype(np.uint8)

# 将NumPy数组转换回PIL图像
output_image = Image.fromarray(output_array)

# 保存结果图像
output_image.save("output_00.png")