from skimage.metrics import structural_similarity as ssim
from skimage import io, transform

def image_similarity(image1_path, image2_path):
    # 读取图像
    image1 = io.imread(image1_path, as_gray=True)
    image2 = io.imread(image2_path, as_gray=True)

    # 调整图像大小为相同的尺寸
    min_height = min(image1.shape[0], image2.shape[0])
    min_width = min(image1.shape[1], image2.shape[1])
    image1 = transform.resize(image1[:min_height, :min_width], (min_height, min_width))
    image2 = transform.resize(image2[:min_height, :min_width], (min_height, min_width))

    # 计算SSIM，指定data_range为1
    similarity = ssim(image1, image2, data_range=1)

    return similarity


image1_path = "alert.png"
image2_path = "finish.png"
image3_path = "D:\python文件\测试刷课脚本\screenshots\screenshot_20231013_125826.png"
image4_path = "D:\python文件\测试刷课脚本\screenshots\screenshot_20231017_233916.png"
similarity_alert = image_similarity(image1_path, image4_path)
similarity_finish = image_similarity(image2_path, image4_path)

print(similarity_alert)
print(similarity_finish)