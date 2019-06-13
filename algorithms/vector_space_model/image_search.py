# requires Pillow library
from PIL import Image
import operator
from math import floor, sqrt
from os.path import isfile


def histogram(lst: list, bins: int = 3*32) -> list:
    length = len(lst)
    no_of_pixels = sum(lst)
    # prepare a list with n elements where n == bins
    temp = [None]*bins
    # for each bin gather values, sum them, and assign to our list
    for i in range(bins):
        start_idx = floor((i*length)/bins)
        end_idx = floor(((i+1)*length)/bins)
        temp[i] = sum(lst[start_idx:end_idx]) / no_of_pixels  # normalize by dividing by total number of pixels
    return temp


def build_matrix_from_files(list_of_paths: list, bins: int = 3*32) -> dict:
    matrix = {}
    for path in list_of_paths:
        if isfile(path):
            img = Image.open(path)
            if img.mode == 'RGB' and img.getbands() == ('R', 'G', 'B'):
                matrix[path] = histogram(img.histogram(), bins)
            else:
                print('File:', path, 'is not an RGB image or contains different set of bands than expected.')
        else:
            print('Not a valid file path:', path)
    return matrix


def euclidean_distance(v: list, u: list) -> float:
    temp = [None]*len(v)
    for idx, vec in enumerate(zip(v, u)):
        temp[idx] = (vec[0]-vec[1])**2
    return sqrt(sum(temp))


def chi_sq_distance(v: list, u: list) -> float:
    temp = [None] * len(v)
    for idx, vec in enumerate(zip(v, u)):
        temp[idx] = (vec[0] - vec[1]) ** 2 / (vec[0] + vec[1])
    return sum(temp) / 2


def search(image_histogram: list, image_database: dict) -> list:
    temp = {}
    for key, value in image_database.items():
        # temp[key] = euclidean_distance(image_histogram, value)
        temp[key] = chi_sq_distance(image_histogram, value)
    return sorted(temp.items(), key=operator.itemgetter(1), reverse=False)


def find_similar_to_file(path: str, image_database: dict) -> list:
    if isfile(path):
        img = Image.open(path)
        if img.mode == 'RGB' and img.getbands() == ('R', 'G', 'B'):
            image_histogram = histogram(img.histogram())
        else:
            raise ValueError(f'File: {path} is not an RGB image or contains different set of bands than expected.')
    else:
        raise FileNotFoundError(f'Not a valid filepath: {path}')
    return search(image_histogram, image_database)
