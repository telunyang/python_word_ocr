import cv2, subprocess, codecs

# image setting and read it
img_sn = "04"
img_ext = "jpg"
img = cv2.imread("media\\sample" + img_sn + "." + img_ext)

# retrieve image detail ex. height, width
height, width, channels = img.shape

# crop image (purify frame) and show it
img_cropped = img[10:(height - 10), 10:(width - 10)].copy()
cv2.namedWindow("Image")
cv2.imshow("Image", img_cropped)
cv2.waitKey(0)
cv2.destroyWindow("Image")

# converts image into grayscale form
gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)

# if pixel value is greater than 135, it will assign white color,
# else it will assign black color.
_, inv = cv2.threshold(gray, 135, 255, cv2.THRESH_BINARY_INV)

# algorithm
for i in range(len(inv)):
    for j in range(len(inv[i])):
        if inv[i][j] == 255:
            count = 0
            for k in range(-7, 8):
                for l in range(-7, 8):
                    try:
                        if inv[i+k][j+l] == 255:
                            count += 1
                    except IndexError:
                        pass
            if count <= 105:
                inv[i][j] = 0

# dilate range of image   
dilation = cv2.dilate(inv, (4,4), iterations = 1)

# save image after dilation
cv2.imwrite("media\\target" + img_sn + "." + img_ext, dilation)

# show image before OCR testing
img_tg = cv2.imread("media\\target" + img_sn + "." + img_ext)
cv2.namedWindow("Image")
cv2.imshow("Image", img_tg)
cv2.waitKey(0)

# recognize words from image and print them
ocr = subprocess.Popen("tesseract media\\target" + img_sn + "." + img_ext + " media\\result" + img_sn)
ocr.wait()
text = codecs.open("media\\result" + img_sn + ".txt", "r", "utf-8").read().strip()
print(text)