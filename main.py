import sampling as sp
import numpy as np
import gray as gr
import time
import PDF as pd
import util as u
import stippling as st
import cv2
import os

resolution = 1


def main(inPath, nPoints, iterations, rMin, rMax, loopStep):
    """
    Funzione che riunisce tutte le funzioni per lo stippling
    @param inPath: path dell'immagine da processare
    @param nPoints: numero di punti da utilizzare per lo stippling
    @param iterations: numero di iterazioni da utilizzare per lo stippling
    @param rMin: valore minimo del raggio da utilizzare per disegnare l'immagine puntinata
    @param rMax: valore massimo del raggio da utilizzare per disegnare l'immagine puntinata
    @param loopStep: valore di step da utilizzare per lo stippling
    """
    threshold = 255
    img = cv2.imread(inPath)
    img = np.ones((img.shape[0], img.shape[1], img.shape[2]), dtype=np.uint8)
    img = img * 255
    stippled = 'data/stippled/stippled_' + inPath.split('/')[2]
    cv2.imwrite(stippled, img)
    print('Converting images to grayscale...')
    gray = gr.gray(inPath)
    print('Converted!')
    print('Next step: sampling creation...')
    for x in range(1, threshold, loopStep):
        print(f"Threshold: {x} di {threshold}")
        points = sp.sampling(nPoints, gray, x, np.random.default_rng(seed=int(time.time())))
        pdf = pd.makePDF('data/gray_images/gray_' + inPath.split('/')[2])
        step = 1 / resolution
        stipples, densities = st.Centroids(points, pdf, gray.shape, step)
        for i in range(1, iterations):
            print('Iteration', i)
            stipples, densities = st.Centroids(stipples, pdf, gray.shape, step)
        radiuses = u.rescaleFloat64s(densities, rMin, rMax)
        stipple = cv2.imread(stippled)
        for j, s in enumerate(stipples):
            try:
                stipple = cv2.circle(stipple, (np.uint64(s[1]), np.uint64(s[0])), int(radiuses[j]), (0, 0, 0), -1)
            except:
                pass
        cv2.imwrite(stippled, stipple)
    print('MAIN COMPLETED!')


if __name__ == '__main__':
    print(
        f"Benvenuti su Stippling!\nUn programma che permette di creare immagini stippled a partire da immagini in "
        f"input.\nOra si trova nella cartella {os.getcwd()}")
    while True:
        try:
            bo = input("Si vogliono vedere i file a disposizione? [[Y]/n] ")
            if bo.upper() == "Y" or bo.upper() == "":
                print(os.listdir('data/images'))
            inPath = "data/images/" + input(
                "Inserire il nome dell'immagine da stipplingare(inserire solo il nome del file): ")
            nPoints = int(input("Inserire il numero di punti da utilizzare per la stippling: "))
            iterations = int(input("Inserire il numero di iterazioni da utilizzare per la stippling: "))
            rMin = float(input("Inserire il valore minimo del raggio da utilizzare per la stippling(pure float): "))
            rMax = float(input("Inserire il valore massimo del raggio da utilizzare per la stippling(pure float): "))
            loopStep = int(input(
                "Inserire il valore di step da utilizzare per la stippling(più iterazioni si fanno ci vorrà più "
                "tempo, ma si avrà una bell'immagine, consigliata se si ha tanto, ma TANTO tempo a disposizione): "))
            nPoints //= loopStep
            main(inPath, nPoints, iterations, rMin, rMax, loopStep)
            break

        except:
            print("Errore! file non trovato, Riprovare!")
            continue
