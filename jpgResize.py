from PIL import Image

# Wczytanie obrazu
input_image = "input.jpg"
output_image = "output.jpg"
image = Image.open(input_image)

# Nowy rozmiar obrazu
new_size = (300, 300)

# Zmiana rozmiaru obrazu
resized_image = image.resize(new_size)

# Zapisanie zmienionego obrazu
resized_image.save(output_image)