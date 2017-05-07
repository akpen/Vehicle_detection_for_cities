import urllib
import cv2
import numpy as np
import os

# Ref: Creating your own Haar Cascade OpenCV Python Tutorial: 
# Site: https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/

# People - Sports - http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513
# People - Misc - http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152

def store_raw_images():
    """This function downloads the positive 
    and negative images from 
    Image-Net
    """
    neg_images_link = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'   
    neg_image_urls = urllib.urlopen(neg_images_link).read().decode()
    pic_num = 1
    
    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.urlretrieve(i, "neg/"+str(pic_num)+".jpg")
            img = cv2.imread("neg/"+str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (450, 300))
            cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
            pic_num += 1
            
        except Exception as e:
            print(str(e))
			
			
store_raw_images()