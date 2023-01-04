import cv2 as cv

def gray(path):
    img = cv.imread(path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rel_path = path.split('/')[0]
    img_name = path.split('/')[2].split('.')[0]
    ext = path.split('/')[2].split('.')[1]
    cv.imwrite('data/gray_images/gray_' + img_name + '.' + ext, gray)
    return gray

