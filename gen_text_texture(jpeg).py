import os
import platform
import glob
from PIL import Image, ImageDraw, ImageFont

# Пути
label = "label.txt"
output = "text_tex.jpg"
padding = 20      # Отступы вокруг текста
max_width = 800   # Максимальная ширина холста

# Определяем ОС и задаем путь к шрифту
system = platform.system()

if system == "Windows":
    default_font = "C:/Windows/Fonts/arial.ttf"
    font_dir = "C:/Windows/Fonts"
elif system == "Linux":
    default_font = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    font_dir = "/usr/share/fonts"
elif system == "Darwin":  # macOS
    default_font = "/System/Library/Fonts/Supplemental/Arial.ttf"
    font_dir = "/System/Library/Fonts"
else:
    raise RuntimeError(f"Неизвестная система: {system}")

# Проверяем наличие шрифта, если нет — ищем первый попавшийся .ttf
if os.path.exists(default_font):
    font_path = default_font
else:
    candidates = glob.glob(os.path.join(font_dir, "**", "*.ttf"), recursive=True)
    if not candidates:
        raise RuntimeError("Не найдено ни одного TTF-шрифта в системе!")
    font_path = candidates[0]  # Берем первый доступный
    print(f"⚠️ Используется найденный шрифт: {font_path}")

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
print(f"Создана текстура: {output}, размер: {img.size}, font_size: {font_size}, font: {font_path}")
