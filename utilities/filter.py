from skimage import io, filters, morphology, util
import numpy as np



def float2int8(img):
    float_img = (img - np.min(img))/(
        np.max(img) - np.min(img))
    return util.img_as_ubyte(float_img)

def filter_fast(img, min_diff=0, to_int8=True):
    mean_val = np.mean(img)
    res_img = np.maximum(np.abs(img - mean_val) - min_diff, 0)
    return float2int8(res_img) if to_int8 else res_img
        

def filter_percise(img, block_size=81, method='median', offset=0, min_diff=0, blend_rate=0, to_int8=True):
    # generate local threshold background
    background = filters.threshold_local(img, block_size=block_size, method=method, offset=offset)
    mean_val = np.mean(img)
    background = blend_rate*background + (1-blend_rate)*mean_val
    # get the thresholded img
    thresholded_image = np.maximum(np.abs(img - background) - min_diff, 0)
    return float2int8(thresholded_image) if to_int8 else thresholded_image
