from PIL import Image
from glob import glob
import os
import cv2

def crop_image(image_dir, save_dir, image_type, save_type):
    """
    @param image_dir: Path to folder of images
    @param save_dir: Path to folder to save the cropped images
    @param image_type: Image type ('jpg' or 'png)
    @param save_type: Saved cropped image type ('jpg' or 'png)
    Saves a centered, square crop of each image in image_dir to save_dir
    """
    if image_type == 'jpg':
        filelist = glob(os.path.join(image_dir, '*.jpg'))
    elif image_type == 'png':
        filelist = glob(os.path.join(image_dir, '*.png'))
    for file in filelist:
        img = cv2.imread(file, 1)
        m = img.shape[0]
        n = img.shape[1]
        image_obj = Image.open(file)
        if m > n:
            shift = int((m-n)/2)
            cropped_img = image_obj.crop((shift, 0, n+shift, n))
        else:
            shift = int((n-m) / 2)
            cropped_img = image_obj.crop((0, shift, m, m+shift))
        cropped_img.show()
        temp = file.replace(image_dir, save_dir)
        temp2 = temp[:len(temp) - 4]
        if save_type == 'jpg':
            save_location = temp2 + '.jpg'
        elif save_type == 'png':
            save_location = temp2 + '.png'
        cropped_img.save(save_location)


if __name__ == '__main__':
    #image_dir = 'pots/images'
    #save_dir = 'pots/cropped_images'
    #crop_image(image_dir, save_dir, 'jpg', 'jpg')
    #image_dir = 'pots/labels'
    #save_dir = 'pots/cropped_labels'
    #crop_image(image_dir, save_dir, 'png', 'png')
    #image_dir = 'hands/test'
    #save_dir = 'hands/cropped_test'
    #crop_image(image_dir, save_dir, 'png', 'png')
    image_dir = 'hands/test_ground_truth'
    save_dir = 'hands/cropped_test_ground_truth'
    crop_image(image_dir, save_dir, 'png', 'png')