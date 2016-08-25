import numpy as np
import scipy.stats as SCI
import matplotlib.pyplot as plt

from numpy import size
from skimage.segmentation import slic, mark_boundaries
from scipy.stats.mstats_basic import kurtosis
from scipy.spatial import distance
from sklearn.naive_bayes import GaussianNB
from scipy.stats.stats import pearsonr


def segmentation_slic(img, conceito):

    segments_slic = slic(img, n_segments=2000, compactness=10.0, sigma=3.0)
    plt.imshow(mark_boundaries(img, segments_slic))
    plt.show()

    FEATURES = np.zeros([len(np.unique(segments_slic)), 4])
    IMAGE_SEG = np.array(img)
    for j in range(len(np.unique(segments_slic))):
        color = np.array(img)
        indices = np.equal(segments_slic, j)
        color[:, :, 0] = np.multiply(color[:, :, 0], indices)
        color[:, :, 1] = np.multiply(color[:, :, 1], indices)
        color[:, :, 2] = np.multiply(color[:, :, 2], indices)
        regionR = color[color[:, :, 0] > 0, 0]
        regionG = color[color[:, :, 1] > 0, 1]
        regionB = color[color[:, :, 2] > 0, 2]
        # plt.imshow(color, cmap = 'gray')
        # plt.title('SLIC'), plt.xticks([]), plt.yticks([])
        # plt.show()

        MEAN = np.mean(regionR) + np.mean(regionG) + np.mean(regionB)
        VARIANCE = np.var(regionR) + np.var(regionG) + np.var(regionB)
        SKEWNESS = SCI.skew(regionR) + SCI.skew(regionG) + SCI.skew(regionB)
        KURTOSIS = kurtosis(regionR) + kurtosis(regionG) + kurtosis(regionB)
        # ENTROPY  = SCI.entropy(regionR) + SCI.entropy(regionG) + SCI.entropy(regionB)

        imgFeatures = [MEAN, VARIANCE, SKEWNESS, KURTOSIS]
        # imgFeatures=[MEAN,ENTROPY]
        # print imgFeatures
        FEATURES = np.load('SpaceFeature/FEATURES_' + str(conceito) + '.npy')
        DIST_EUCLIDIAN = 0
        target = np.ones([np.size(FEATURES, 0), 1])
        PEARSON = []
        for m in range(size(FEATURES, 0)):
            # amostra = FEATURES[m,:]
            amostra = FEATURES[m, 0:4]
            # DIST_EUCLIDIAN += distance.euclidean(imgFeatures,amostra)
            P = pearsonr(imgFeatures, amostra)
            # print P
            if (P[1] < 0.05):
                PEARSON.append(P[0])
            # else:
            #    PEARSON.append(0)

        # print np.mean(PEARSON)
        # print DIST_EUCLIDIAN
        # gnb = GaussianNB()
        # y_pred = gnb.fit(FEATURES,target).predict(imgFeatures)
        # if DIST_EUCLIDIAN >= 51000 or DIST_EUCLIDIAN <= 40000:
        # if y_pred == 1:
        # if DIST_EUCLIDIAN <= 36000:
        print np.mean(np.abs(PEARSON))
        if np.mean(np.abs(PEARSON)) > 0.99:
            IMAGE_SEG[indices, 0] = 255
            IMAGE_SEG[indices, 1] = 255
            IMAGE_SEG[indices, 2] = 255
        else:
            IMAGE_SEG[indices, 0] = 0
            IMAGE_SEG[indices, 1] = 0
            IMAGE_SEG[indices, 2] = 0

    a = np.array(img)
    a[:, :, 0] = np.multiply(img[:, :, 0], np.double(IMAGE_SEG[:, :, 0]) / 255.0)
    a[:, :, 1] = np.multiply(img[:, :, 1], np.double(IMAGE_SEG[:, :, 1]) / 255.0)
    a[:, :, 2] = np.multiply(img[:, :, 2], np.double(IMAGE_SEG[:, :, 2]) / 255.0)

    plt.subplot(131), plt.imshow(mark_boundaries(img, segments_slic))
    plt.title('Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(132), plt.imshow(IMAGE_SEG, cmap='binary')
    plt.title('SEGMENTACaO'), plt.xticks([]), plt.yticks([])

    plt.subplot(133), plt.imshow(a, cmap='gray')
    plt.title('OUTPUT'), plt.xticks([]), plt.yticks([])

    plt.show()

    '''
        EUCLIDIAN DISTANCE
    for i in range(10):
        FEATURES = np.load('SpaceFeature/FEATURES_' + str(i) + '.npy')
        DIST_EUCLIDIAN = 0
        for j  in range(size(FEATURES,1)):
            amostra = FEATURES[j,:]
            dst = distance.euclidean(imgFeatures,amostra)
    '''
