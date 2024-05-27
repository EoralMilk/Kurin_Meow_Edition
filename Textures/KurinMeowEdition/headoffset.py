import os
from PIL import Image

def crop_images_in_folder(folder_path):
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			if file.lower().endswith('.jpg') or file.lower().endswith('.png'):
				file_path = os.path.join(root, file)
				needProcess = False;
				if file.lower().endswith('eastm.png') or file.lower().endswith('east.png') or file.lower().endswith('westm.png') or file.lower().endswith('west.png'):
					image = Image.open(file_path)
					width, height = image.size
					rightAddCut = int(height * 0.12);
					leftAddCut = int(height * 0.06);
					topAddCut = int(height * 0.09);
					bottomAddCut = int(height * 0.09);
					needProcess = True;
				elif file.lower().endswith('southm.png') or file.lower().endswith('south.png') or  file.lower().endswith('northm.png') or file.lower().endswith('north.png'):
					image = Image.open(file_path)
					width, height = image.size
					rightAddCut = int(height * 0.085);
					leftAddCut = int(height * 0.085);
					topAddCut = int(height * 0.06);
					bottomAddCut = int(height * 0.11);
					needProcess = True;

				if needProcess:
					left = leftAddCut
					top = topAddCut
					right = width - rightAddCut
					bottom = height - bottomAddCut
					cropped_image = image.crop((left, top, right, bottom))
					# cropped_image.save(file_path)
					print(f"Cropped {file}")
					
					
					# Resize to a square image
					size = max(cropped_image.size)
					# size = 2 ** (size - 1).bit_length()  # 获取最接近的2的幂次方边长
					if size > 384:
						size = 512
					elif size > 256:
						size = 384
					elif size > 128:
						size = 256
					else:
						size = 128
					resized_image = cropped_image.resize((size, size))
					resized_image.save(file_path)
					print(f"Cropped and resized {file}")
				else:
					print(f"___Skipped {file}")

# 用法示例
folder_path = './Temp'
crop_images_in_folder(folder_path)