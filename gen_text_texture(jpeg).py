from PIL import Image, ImageDraw, ImageFont

# Пути
label = "label.txt"
output = "text_tex.jpg"
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # Или путь к Arial.ttf
padding = 20      # Отступы вокруг текста
max_width = 800   # Максимальная ширина холста (можешь поменять по нужде)

# Читаем текст
with open(label, "r", encoding="utf-8") as f:
    text = f.read().strip()

# Начальные параметры
font_size = 10
font = ImageFont.truetype(font_path, font_size)
draw_dummy = ImageDraw.Draw(Image.new("RGBA", (1, 1)))

# Подбираем максимальный размер шрифта
while True:
    bbox = draw_dummy.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    if text_w + padding * 2 > max_width:
        font_size -= 1
        font = ImageFont.truetype(font_path, font_size)
        break
    font_size += 2
    font = ImageFont.truetype(font_path, font_size)

# Создаем холст нужного размера
bbox = draw_dummy.textbbox((0, 0), text, font=font)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]
canvas_w = text_w + padding * 2
canvas_h = text_h + padding * 2

img = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))  # Белый фон
draw = ImageDraw.Draw(img)

# Центрируем и рисуем
cx, cy = canvas_w / 2, canvas_h / 2
draw.text((cx, cy), text, font=font, fill=(0, 0, 0), anchor="mm")

# Сохраняем
img.save(output, "JPEG", quality=95)
print(f"Создана текстура: {output}, размер: {img.size}, font_size: {font_size}")