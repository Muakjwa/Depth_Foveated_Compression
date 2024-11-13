import numpy as np
import h5py
import cv2 as cv

psnr_list = []
data_size = []
time_list = []
img_num = 1448

def load_image():
    path_to_depth = './NYU_v2/nyu_depth_v2_labeled.mat'

    f = h5py.File(path_to_depth)

    img = f['images'][img_num]

    img_ = np.empty([480, 640, 3])
    img_[:,:,0] = img[0,:,:].T
    img_[:,:,1] = img[1,:,:].T
    img_[:,:,2] = img[2,:,:].T
    cv.imwrite('decode.jpg', img_)

    depth = f['depths'][img_num]
    
    return img_, depth

def save_depth_map(depth):
    depth_map = np.empty([480, 640, 3])
    depth_map[:,:,0] = depth[:,:].T
    depth_map[:,:,1] = depth[:,:].T
    depth_map[:,:,2] = depth[:,:].T

    cv.imwrite('./image_transformed/depth_map.jpg', depth_map * 255 / np.max(depth_map))


image, depth = load_image()


# Only Apply Depth Information to compress image
retval, encode_D = cv.imencode_D('.jpg', image, depth)

# Apply Depth & Foveation Information to compress image
# cv.IMWRITE_JPEG_FOVEATION_DISTANCE parameter value를 이용하여 사용자가 화면으로부터 떨어져 있는 거리 설정
# META Quest 기기를 기준으로 설정하면 62
retval, encode_DF = cv.imencode_D('.jpg', image, depth, [cv.IMWRITE_JPEG_FOVEATION_DISTANCE, 62])

# Only Apply Foveation Information to compress image
retval, encode_F = cv.imencode('.jpg', image, [cv.IMWRITE_JPEG_FOVEATION_DISTANCE, 62])


decode_D = cv.imdecode(encode_D, 1)
decode_DF = cv.imdecode(encode_DF, 1)
decode_F = cv.imdecode(encode_F, 1)

cv.imwrite('./image_transformed/D_a1000_1448.jpg', decode_D)
cv.imwrite('./image_transformed/DF_a1000_1448.jpg', encode_DF)
cv.imwrite('./image_transformed/F_1448.jpg', encode_F)
save_depth_map(depth)
