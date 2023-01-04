import sampling as sp 
import numpy as np
import gray as gr
import time 
import PDF as pd
import util as u 
import stippling as st
import cv2 as cv2
inPath = 'data/images/colosseo.jpeg'
nPoints = 500
threshold = 200
resolution = 1
iterations = 10 
rMin = 1
rMax = 1


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
    print(stipples)
    for i in range(1, iterations):
       print('Iteration', i)
       stipples, densities = st.Centroids(stipples, pdf, gray.shape, step)
    print('Stippling completed!')
    print('Next step: normalize densities...')
    print('Densities normalization in progress...')
    radiuses = u.rescaleFloat64s(densities, rMin, rMax)
    print('Densities normalized!')
    print('Next step: drawing stippled image...')
    cv2.imread(stippled)
    print('Drawing stippled image in progress...')
    for i, s in enumerate(stipples):
        cv2.circle(stippled, int(s[0]), int(s[1]), radiuses[i], (0, 0, 0), -1)
    cv2.imwrite(stippled, stippled)
    print('Stippled image drawn!')
    print('MAIN COMPLETED!')


if __name__ == '__main__':
    main()