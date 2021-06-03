from PIL import Image, ImageEnhance
import numpy as np
import imutils
import os
import Database_Get


# 尺寸调整

def ImgResize(Img, ScaleFactor):
    ImgSize = Img.size  # 获得图像原始尺寸
    NewSize = [int(ImgSize[0] * ScaleFactor), int(ImgSize[1] * ScaleFactor)]  # 获得图像新尺寸，保持长宽比
    Img = Img.resize(NewSize)  # 利用PIL的函数进行图像resize，类似matlab的imresize函数
    return Img

# 旋转

def ImgRotate(Img, Degree):
    return Img.rotate(Degree)  # 利用PIL的函数进行图像旋转，类似matlab imrotate函数


# 利用PIL的函数进行水平镜像

def ImgLRMirror(Img):
    return Img.transpose(Image.FLIP_LEFT_RIGHT)


# 亮度,增强因子为1.0是原始图像

def BrightEnchance(Img, factor):
    enh_bri = ImageEnhance.Brightness(Img)
    image_brightened = enh_bri.enhance(factor)
    return image_brightened


# 色度,增强因子为1.0是原始图像

def ColorEnchance(Img, factor):
    enh_col = ImageEnhance.Color(Img)
    image_colored = enh_col.enhance(factor)
    return image_colored


# 对比度，增强因子为1.0是原始图片

def ContrastEnchance(Img, factor):
    enh_con = ImageEnhance.Contrast(Img)
    image_contrasted = enh_con.enhance(factor)
    return image_contrasted


# 锐度，增强因子为1.0是原始图片

def SharpEnchance(Img, factor):
    enh_sha = ImageEnhance.Sharpness(Img)
    image_sharped = enh_sha.enhance(factor)
    return image_sharped

def check_path(nums):
    index = []   # 记录哪些是原来没有的文件，也就是说记录新添加的信息  的 索引值
    for i in range(len(nums)):
        path1 = "./face_database/{}".format(nums[i])
        if not os.path.exists(path1):
            index.append(i)
            os.mkdir(path1)
        path2 = "./face_encode/{}".format(nums[i])
        if not os.path.exists(path2):
            os.mkdir(path2)
    return index

def start():

    database_get = Database_Get.DatabaseGet()
    images,nums = database_get.database_get_image()
    index = check_path(nums)

    img_path = './image/image.jpg'

    for i in index:

        fout = open('./image/image.jpg', 'wb')
        fout.write(images[i])
        fout.close()

        save_path = './face_database/{}/'.format(nums[i])

        Img = Image.open(img_path)

        # 1 尺寸

        scale_img1 = ImgResize(Img, 0.2)

        scale_img2 = ImgResize(Img, 1.5)

        scale_img3 = ImgResize(Img, 1)

        save_scale_path1 = os.path.join(save_path, 'scale_img1.jpg')

        save_scale_path2 = os.path.join(save_path, 'scale_img2.jpg')

        save_scale_path3 = os.path.join(save_path, 'img.jpg')

        scale_img1.save(save_scale_path1)

        scale_img2.save(save_scale_path2)

        scale_img3.save(save_scale_path3)

        # 2 旋转

        rotate_img1 = ImgRotate(Img, 10)

        rotate_img2 = ImgRotate(Img, 30)

        rotate_img3 = ImgRotate(Img, 45)

        rotate_img4 = ImgRotate(Img, 350)

        rotate_img5 = ImgRotate(Img, 330)

        rotate_img6 = ImgRotate(Img, 315)


        save_rotate_path1 = os.path.join(save_path, 'rotate_img1.jpg')

        save_rotate_path2 = os.path.join(save_path, 'rotate_img2.jpg')

        save_rotate_path3 = os.path.join(save_path, 'rotate_img3.jpg')

        save_rotate_path4 = os.path.join(save_path, 'rotate_img4.jpg')

        save_rotate_path5 = os.path.join(save_path, 'rotate_img5.jpg')

        save_rotate_path6 = os.path.join(save_path, 'rotate_img6.jpg')


        rotate_img1.save(save_rotate_path1)

        rotate_img2.save(save_rotate_path2)

        rotate_img3.save(save_rotate_path3)

        rotate_img4.save(save_rotate_path4)

        rotate_img5.save(save_rotate_path5)

        rotate_img6.save(save_rotate_path6)

        # 镜像

        mirror_img1 = ImgLRMirror(Img)

        save_mirror_path1 = os.path.join(save_path, 'mirror_img1.jpg')

        mirror_img1.save(save_mirror_path1)

        # 平移

        array_img = np.array(Img)  # PIL.Image 转 numpy.array

        translation_img1 = imutils.translate(array_img, 60, 60)

        translation_img2 = imutils.translate(array_img, -60, 60)

        translation_img3 = imutils.translate(array_img, 30, -30)

        translation_img4 = imutils.translate(array_img, -30, -30)

        save_translation_path1 = os.path.join(save_path, 'translation_img1.jpg')

        save_translation_path2 = os.path.join(save_path, 'translation_img2.jpg')

        save_translation_path3 = os.path.join(save_path, 'translation_img3.jpg')

        save_translation_path4 = os.path.join(save_path, 'translation_img4.jpg')

        translation_img1 = Image.fromarray(translation_img1)

        translation_img2 = Image.fromarray(translation_img2)

        translation_img3 = Image.fromarray(translation_img3)

        translation_img4 = Image.fromarray(translation_img4)

        translation_img1.save(save_translation_path1)

        translation_img2.save(save_translation_path2)

        translation_img3.save(save_translation_path3)

        translation_img4.save(save_translation_path4)


        # 以下只对原图操作，亮度,增强因子为0.0将产生黑色图像；为1.0将保持原始图像

        bright_img1 = BrightEnchance(Img, 0.3)

        bright_img2 = BrightEnchance(Img, 0.4)

        bright_img3 = BrightEnchance(Img, 0.5)

        bright_img4 = BrightEnchance(Img, 0.6)

        bright_img5 = BrightEnchance(Img, 0.7)

        bright_img6 = BrightEnchance(Img, 0.8)

        bright_img7 = BrightEnchance(Img, 0.9)

        bright_img8 = BrightEnchance(Img, 0.9)

        save_bright_path1 = os.path.join(save_path, 'bright_img1.jpg')

        save_bright_path2 = os.path.join(save_path, 'bright_img2.jpg')

        save_bright_path3 = os.path.join(save_path, 'bright_img3.jpg')

        save_bright_path4 = os.path.join(save_path, 'bright_img4.jpg')

        save_bright_path5 = os.path.join(save_path, 'bright_img5.jpg')

        save_bright_path6 = os.path.join(save_path, 'bright_img6.jpg')

        save_bright_path7 = os.path.join(save_path, 'bright_img7.jpg')

        save_bright_path8 = os.path.join(save_path, 'bright_img8.jpg')


        bright_img1.save(save_bright_path1)

        bright_img2.save(save_bright_path2)

        bright_img3.save(save_bright_path3)

        bright_img4.save(save_bright_path4)

        bright_img5.save(save_bright_path5)

        bright_img6.save(save_bright_path6)

        bright_img7.save(save_bright_path7)

        bright_img8.save(save_bright_path8)

        # 色度,增强因子为1.0是原始图像，大于1增强，小于1减弱

        color_img1 = ColorEnchance(Img, 0.5)

        color_img2 = ColorEnchance(Img, 1.5)

        save_color_path1 = os.path.join(save_path, 'color_img1.jpg')

        save_color_path2 = os.path.join(save_path, 'color_img2.jpg')

        color_img1.save(save_color_path1)

        color_img2.save(save_color_path2)


        # 对比度，增强因子为1.0是原始图片,大于1增强，小于1减弱

        contrast_img1 = ContrastEnchance(Img, 0.5)

        contrast_img2 = ContrastEnchance(Img, 1.5)

        save_contrast_path1 = os.path.join(save_path, 'contrast_img1.jpg')

        save_contrast_path2 = os.path.join(save_path, 'contrast_img2.jpg')

        contrast_img1.save(save_contrast_path1)

        contrast_img2.save(save_contrast_path2)

        # 锐度，增强因子为1.0是原始图片,大于1增强，小于1减弱

        sharp_img1 = SharpEnchance(Img, 0.5)

        sharp_img2 = SharpEnchance(Img, 1.5)

        save_sharp_path1 = os.path.join(save_path, 'sharp_img1.jpg')

        save_sharp_path2 = os.path.join(save_path, 'sharp_img2.jpg')

        sharp_img1.save(save_sharp_path1)

        sharp_img2.save(save_sharp_path2)
    return index
if __name__ == "__main__":
    start()
    pass