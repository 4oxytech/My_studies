import img2pdf
from PIL import Image

img_path = "C:/Users/leram/PycharmProjects/pythonProject16/png/png.png"
pdf_path = "C:/Users/leram/PycharmProjects/pythonProject16/pdf/file.pdf"
#Открываем картинку
image = Image.open(img_path)

#Конвертируем
pdf_bytes = img2pdf.convert(image.filename)

#открываем и изменяем пдф файл
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
#закрываем пдф файл
file.close()
print("Всё удачно")