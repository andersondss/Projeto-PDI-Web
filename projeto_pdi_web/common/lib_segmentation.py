import numpy as np
from numpy import size
import scipy.stats as SCI
import matplotlib.pyplot as plt
from skimage.segmentation import slic, mark_boundaries
from scipy.stats.mstats_basic import kurtosis
from scipy.spatial import distance
from sklearn.naive_bayes import GaussianNB
from scipy.stats.stats import pearsonr


def segmentation_slic(img, conceito):

    segments_slic = slic(img, n_segments=2000, compactness=10.0, sigma=3.0)
    plt.imshow(mark_boundaries(img, segments_slic))
    plt.show()

    features = np.zeros([len(np.unique(segments_slic)), 4])
    image_seg = np.array(img)

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

        imgFeatures = [MEAN, VARIANCE, SKEWNESS, KURTOSIS]
        features = np.load('SpaceFeature/FEATURES_' + str(conceito) + '.npy')
        pearson = []
        for m in range(size(features, 0)):
            amostra = features[m, 0:4]
            P = pearsonr(imgFeatures, amostra)
            if (P[1] < 0.05):
                pearson.append(P[0])

        # print np.mean(np.abs(pearson))
        if np.mean(np.abs(pearson)) > 0.99:
            image_seg[indices, 0] = 255
            image_seg[indices, 1] = 255
            image_seg[indices, 2] = 255
        else:
            image_seg[indices, 0] = 0
            image_seg[indices, 1] = 0
            image_seg[indices, 2] = 0

    a = np.array(img)
    a[:, :, 0] = np.multiply(img[:, :, 0], np.double(image_seg[:, :, 0]) / 255.0)
    a[:, :, 1] = np.multiply(img[:, :, 1], np.double(image_seg[:, :, 1]) / 255.0)
    a[:, :, 2] = np.multiply(img[:, :, 2], np.double(image_seg[:, :, 2]) / 255.0)

    plt.subplot(131), plt.imshow(mark_boundaries(img, segments_slic))
    plt.title('Image'), plt.xticks([]), plt.yticks([])

    plt.subplot(132), plt.imshow(image_seg, cmap='binary')
    plt.title('Segmentacao'), plt.xticks([]), plt.yticks([])

    plt.subplot(133), plt.imshow(a, cmap='gray')
    plt.title('OUTPUT'), plt.xticks([]), plt.yticks([])

    plt.show()
