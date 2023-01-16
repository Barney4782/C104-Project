import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(
    img,
    "Sun",
    (20, 300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Mercury",
    (110, 250),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Venus",
    (190, 170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Earth",
    (290, 260),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Mars",
    (380, 170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Jupiter",
    (470, 300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Saturn",
    (680, 170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Uranus",
    (950, 250),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)

cv2.putText(
    img,
    "Neptune",
    (1100, 170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255, 255, 255)
)


cv2.imshow("output", img)

cv2.waitKey(0)

filename = "SolarSystemWithName.jpg"

cv2.imwrite(filename, img)
