# nahum flores NC 0065
# ejemplo 2 numero 21 nutria

import cv2

# Cargar imagen (Cambiado a nutria.jpg)
imagen = cv2.imread("imagenes/nutria.jpg")
# Comprobar imagen
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a imagen binaria mediante umbral
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# Detectar contornos
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Dibujar los contornos
resultado = imagen.copy()

cv2.drawContours(
    resultado,
    contornos,
    -1,
    (0, 255, 0),
    2
)

# Mostrar resultados
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen binaria", binaria)
cv2.imshow("Contornos detectados", resultado)

# Guardar resultado
cv2.imwrite(
    "../resultados/ejemplo2_contornos.jpg",
    resultado
)

print("Cantidad de contornos encontrados:", len(contornos))
print("Resultado guardado en ../resultados/ejemplo2_contornos.jpg")

# Esperar
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("nahum flores NC 0065")