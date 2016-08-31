import cv2
import numpy as np
from scipy.spatial import distance
from scipy.spatial.distance import euclidean
from skimage.measure import perimeter
from scipy.stats.stats import pearsonr


def _get_medoid(descritor):

    soma = 0
    indice = 0
    matriz_correlacao = np.corrcoef(descritor)
    for i in range(len(matriz_correlacao)):
        if (sum(matriz_correlacao[i]) > soma):
            soma = sum(matriz_correlacao[i])
            indice = i

    return indice, descritor[indice]


def get_shape_similarity(first_image, second_image):

    orb = cv2.ORB_create()
    kp_1, descritores_1 = orb.detectAndCompute(first_image, None)
    kp_2, descritores_2 = orb.detectAndCompute(second_image, None)
    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    # Match descriptors.
    matches = bf.match(descritores_1, descritores_2)
    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)
    match_images = cv2.drawMatches(first_image, kp_1, second_image, kp_2, matches, None, flags=2)

    [idx_1, d_1] = _get_medoid(descritores_1)
    [idx_2, d_2] = _get_medoid(descritores_2)

    dist_1 = 0
    dist_2 = 0
    m_1 = kp_1[idx_1].pt
    m_2 = kp_2[idx_2].pt
    for l in range(len(kp_1)):
        dist_1 += euclidean(m_1, kp_1[l].pt)
    for l in range(len(kp_2)):
        dist_2 += euclidean(m_2, kp_2[l].pt)

    # EXTRACAO DE CARACTERISTICAS
    f_1 = [0, 0, 0]
    f_2 = [0, 0, 0]

    first_image = np.divide(first_image, 255.0)
    second_image = np.divide(second_image, 255.0)

    prop1 = first_image.shape[0]*first_image.shape[1]
    prop2 = second_image.shape[0]*second_image.shape[1]

    # AREAS
    f_1[0] = np.sum(first_image)/prop1
    f_2[0] = np.sum(second_image)/prop2

    # PERIMETROS
    f_1[1] = perimeter(first_image)/prop1
    f_2[1] = perimeter(second_image)/prop2

    f_1[2] = dist_1/prop1
    f_2[2] = dist_2/prop2

    person = pearsonr(f_1, f_2)
    dist = (distance.euclidean(f_1, f_2))*100

    rate_shape_similarity = np.abs((person[0]*100)-dist)
    return match_images, rate_shape_similarity
