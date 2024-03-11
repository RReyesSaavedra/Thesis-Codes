import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

def encon_centro(imag):
    max_coords = np.unravel_index(np.argmax(imag), imag.shape)
    x, y = max_coords
    return x, y

def crop_image(image, dx, dy):
    alto, ancho = image.shape[:2]
    nuevo_alto = int(alto / 5)
    nuevo_ancho = int(ancho / 5)
    inicio_x = int((ancho - nuevo_ancho) / 2) + dx
    inicio_y = int((alto - nuevo_alto) / 2) + dy
    fin_x = inicio_x + nuevo_ancho
    fin_y = inicio_y + nuevo_alto
    imagen_recortada = image[inicio_y:fin_y, inicio_x:fin_x]
    return imagen_recortada

#07_1, -50, 46
#09_1: -46, 46
#10_1, -53, 44

def sum_error(nim1, nim2, d1, d2):
    ruta_imagen1 = '/Users/Rudy/DESKTOP/CFATA/TESIS/2023_12_13/IMG_00' + nim1 + '.JPG'
    ruta_imagen2 = '/Users/Rudy/DESKTOP/CFATA/TESIS/2023_12_13/IMG_00' + nim2 + '.JPG'
  
    # Leer las imágenes
    image_sr1 = cv2.imread(ruta_imagen1)
    image_sr2 = cv2.imread(ruta_imagen2)

    # Recortar las imágenes
    imagen1 = crop_image(image_sr1, d1[0], d1[1])
    imagen2 = crop_image(image_sr2, d2[0], d2[1]) # Ajusta dx, dy según sea necesario

    # Convertir las imágenes a escala de grises
    imagen_gris1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)
    imagen_gris2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)

    # Obtener las coordenadas del píxel con el valor máximo
    x, y = [400, 400]
    
    # Visualizar las patrones y su centro
    plt.imshow(imagen_gris1, cmap='gray')
    plt.scatter([x], [y], s=1, c='red', marker='o')
    plt.title('Imagen 00' + nim1)
    plt.show()

    plt.imshow(imagen_gris2, cmap='gray')
    plt.scatter([x], [y], s=1, c='red', marker='o')
    plt.title('Imagen 00' + nim2)
    plt.show()

    # Procesar y graficar vector izquierdo
    patron1_sum = np.zeros(400)
    for i, (imagen_gris, nim) in enumerate(zip([imagen_gris1, imagen_gris2], [nim1, nim2]), 1):
        patron1 = np.flip(imagen_gris[y, :x] / 255.0)
        patron1_sum = patron1_sum + patron1
        plt.plot(patron1, label=f'Patron {i}')
    # Ajustes de diseño
    plt.title('2 imagenes de 1 pulso, izquierda')
    plt.xlabel('Distancia del centro')
    plt.ylabel('Valor de intensidad normalizado')
    plt.legend()
    plt.show()
    patron1_prom = patron1_sum/2

    #Procesar y graficar vector derecho
    patron2_sum = np.zeros(400)
    for i, (imagen_gris, nim) in enumerate(zip([imagen_gris1, imagen_gris2], [nim1, nim2]), 1):
        patron2 = imagen_gris[y, x:] / 255.0
        patron2_sum = patron2_sum + patron2
        plt.plot(patron2, label=f'Patron {i}')
    # Ajustes de diseño
    plt.title('2 imagenes de 1 pulso, derecha')
    plt.xlabel('Distancia del centro')
    plt.ylabel('Valor de intensidad normalizado')
    plt.legend()
    plt.show()
    patron2_prom = patron2_sum/2

    # Procesar y graficar vector arriba 
    patron3_sum = np.zeros(400)
    for i, (imagen_gris, nim) in enumerate(zip([imagen_gris1, imagen_gris2], [nim1, nim2]), 1):
        patron3 = np.flip(imagen_gris[:y, x] / 255.0)
        patron3_sum = patron3_sum + patron3
        plt.plot(patron3, label=f'Patron {i}')
    # Ajustes de diseño
    plt.title('2 imagenes de 1 pulso, arriba')
    plt.xlabel('Distancia del centro')
    plt.ylabel('Valor de intensidad normalizado')
    plt.legend()
    plt.show()
    patron3_prom = patron3_sum/2
    
    # Procesar y graficar vector abajo
    patron4_sum = np.zeros(400)
    for i, (imagen_gris, nim) in enumerate(zip([imagen_gris1, imagen_gris2], [nim1, nim2]), 1):
        patron4 = imagen_gris[y:, x] / 255.0
        patron4_sum = patron4_sum + patron4
        plt.plot(patron4, label=f'Patron {i}')
    patron4_prom = patron4_sum/2
    
    # Ajustes de diseño
    plt.title('2 imagenes de 1 pulso, abajo')
    plt.xlabel('Distancia del centro')
    plt.ylabel('Valor de intensidad normalizado')
    plt.legend()
    plt.show()
    patrones = [patron1_prom, patron2_prom, patron3_prom, patron4_prom]
    return patrones
    
#pulso4 = sum_error("14_1", "15_1", "16_1", [-48,53], [-55,47], [-60,44])
#pulso9 = sum_error("27_1", "28_1", "29_1", [-52,46], [-57,47], [-56,47])
#pulso14 = sum_error("42_1", "43_1", "44_1", [-51,48], [-60,47], [-56,44]) 
pulso2 = sum_error("06_2", "07_1", [-47,49], [-49,48]) 
pulso20 = sum_error("62_1", "63_1", [-55,44], [-57,44]) 

titulos = ['Vector izquierdo procesado', 'Vector derecho procesado', 'Vector arriba procesado', 'Vector abajo procesado']
for i in range(4):
    # Graficar los patrones procesados
    plt.plot(pulso2[i], label='Pulso 2')
    plt.plot(pulso20[i], label='Pulso 20')
    # Ajustes de diseño
    plt.title(titulos[i])
    plt.xlabel('Distancia del centro')
    plt.ylabel('Valor de intensidad normalizado')
    plt.legend()
    plt.show()

"""
for i in range(4):
    # Graficar los patrones procesados
    plt.plot(pulso4[i], label='Pulso 4')
    plt.plot(pulso9[i], label='Pulso 9')
    plt.plot(pulso14[i], label='Pulso 14')
    # Ajustes de diseño
    plt.title(titulos[i])
    plt.xlabel('Distancia del centro')
    plt.ylabel('Valor de intensidad normalizado')
    plt.legend()
    plt.show()
"""

"""
    # Visualizar las patrones y su centro
    plt.imshow(imagen_gris1, cmap='gray')
    plt.scatter([x], [y], s=1, c='red', marker='o')
    plt.title('Imagen 00' + nim1)
    plt.show()

    plt.imshow(imagen_gris2, cmap='gray')
    plt.scatter([x], [y], s=1, c='red', marker='o')
    plt.title('Imagen 00' + nim2)
    plt.show()
    
    plt.imshow(imagen_gris3, cmap='gray')
    plt.scatter([x], [y], s=1, c='red', marker='o')
    plt.title('Imagen 00' + nim3)
    plt.show()
"""


