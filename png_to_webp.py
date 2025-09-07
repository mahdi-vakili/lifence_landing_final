# import os
# from PIL import Image

# # مسیر پایه‌ای که می‌خوای جستجو از اونجا شروع بشه (درایو یا پوشه خاص)
# base_path = r'C:\Users\Mehdi\Desktop\lifence_landing_final'

# # کیفیت خروجی WebP
# quality = 80  # مقدار کمتر = حجم کمتر

# # عبور از همه‌ی فایل‌ها
# for root, dirs, files in os.walk(base_path):
#     for file in files:
#         if file.lower().endswith(".png"):
#             png_path = os.path.join(root, file)
#             webp_path = os.path.join(root, file[:-4] + ".webp")

#             try:
#                 with Image.open(png_path) as img:
#                     img = img.convert("RGB")  # چون تصویر شفافیت نداره
#                     img.save(webp_path, format='webp', quality=quality, method=6)
#                 print(f"✅ تبدیل شد: {png_path}")
#             except Exception as e:
#                 print(f"❌ خطا در {png_path}: {e}")




import os

# مسیر پوشه‌ی اصلی
base_path = r'C:\Users\Mehdi\Desktop\lifence_landing_final'  # ← مسیر دلخواهتو بزن

# عبور از تمام فایل‌ها
for root, dirs, files in os.walk(base_path):
    for file in files:
        if file.lower() == 'index.html':
            file_path = os.path.join(root, file)

            try:
                # خواندن محتوای فایل
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # جایگزینی تمام .png با .webp
                new_content = content.replace('.png', '.webp')

                # ذخیره محتوای جدید در همان فایل
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                print(f'✅ ویرایش شد: {file_path}')
            except Exception as e:
                print(f'❌ خطا در {file_path}: {e}')
