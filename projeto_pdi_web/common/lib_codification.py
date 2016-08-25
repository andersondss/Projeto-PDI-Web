import cv2
from matplotlib import pyplot as plt


def run_orb(img):
    orb = cv2.ORB_create()
    kp, descriptors = orb.detectAndCompute(img, None)
    img_keypoints = cv2.drawKeypoints(img, kp, None, flags=2)
    # plt.imshow(img_keypoints)
    # plt.show()
    return kp, descriptors, img_keypoints
