import sampB as sp 
import numpy as np
import gray as gr
import time 
import PDF as pd
import util as u 
import stip as st
import cv2 as cv2

inPath = 'data/images/figura.png'
nPoints = 20000
threshold = 255
resolution = 1
iterations = 10
rMin = 0.9
rMax = 1.2


def main():
    img = cv2.imread(inPath)
    img = np.ones((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
    img = img * 255
    stippled = 'data/stippled/stippled_' + inPath.split('/')[2]
    cv2.imwrite(stippled, img)
    print('Converting images to grayscale...')
    gray = gr.gray(inPath)
    print('Converted!')
    print('Next step: sampling creation...')
    points = sp.sampling(nPoints, gray, threshold, np.random.default_rng(seed=int(time.time())))
    print('Sampling created!')
    print('Next step: PDF creation...')
    pdf = pd.makePDF('data/gray_images/gray_' + inPath.split('/')[2])
    print('PDF created successfully!')
    step = 1/resolution
    print('Next step: stippling...')
    print('Stippling in progress... please be patient')
    stipples, densities = st.Centroids(points, pdf, gray.shape, step)
    for i in range(1, iterations):
       print('Iteration', i)
       stipples, densities = st.Centroids(stipples, pdf, gray.shape, step)
    print('Stippling completed!')
    print('Next step: normalize densities...')
    print('Densities normalization in progress...')
    radiuses = u.rescaleFloat64s(densities, rMin, rMax)
    print('Densities normalized!')
    print('Next step: drawing stippled image...')
    stipple = cv2.imread(stippled)
    print('Drawing stippled image in progress...')
    for j, s in enumerate(stipples):
        try:
            stipple = cv2.circle(stipple, (np.uint64(s[1]), np.uint64(s[0])), int(radiuses[j]), (0, 0, 0), -1)
        except:
            pass
    cv2.imwrite(stippled, stipple)
    print('Stippled image drawn!')
    print('MAIN COMPLETED!')


if __name__ == '__main__':
    main()