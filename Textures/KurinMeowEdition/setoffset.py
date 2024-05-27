import os
from PIL import Image

scaleOffset = 1

def move_images_in_folder(folder_path):
	for root, dirs, files in os.walk(folder_path):
		for file in files:
			if file.lower().endswith('.jpg') or file.lower().endswith('.png'):
				file_path = os.path.join(root, file)
				image = Image.open(file_path)
				image = image.resize((475, 475))
				new_file_name = None
				move_pixels = (0, 0)
				
				if file.lower().endswith('_eastm.png') or file.lower().endswith('_east.png'):
					new_file_name = file
					move_pixels = (0 * scaleOffset, -82 * scaleOffset)
				if file.lower().endswith('_westm.png') or file.lower().endswith('_west.png'):
					new_file_name = file
					move_pixels = (0 * scaleOffset, -82 * scaleOffset)
				elif file.lower().endswith('_southm.png') or file.lower().endswith('_south.png'):
					new_file_name = file
					if file.lower().startswith("foxearl"):
						move_pixels = (5 * scaleOffset, -85 * scaleOffset)
					else:
						move_pixels = (-5 * scaleOffset, -85 * scaleOffset)
					
				elif file.lower().endswith('_northm.png') or file.lower().endswith('_north.png'):
					new_file_name = file
					if file.lower().startswith("foxearl"):
						move_pixels = (-5 * scaleOffset, -88 * scaleOffset)
					else:
						move_pixels = (5 * scaleOffset, -88 * scaleOffset)
					# move_pixels = (-5 * scaleOffset, -85 * scaleOffset)
				
				if new_file_name:
					new_file_path = os.path.join(root, new_file_name)
					image = image.transform(image.size, Image.AFFINE, (1, 0, move_pixels[0], 0, 1, move_pixels[1]))
					os.remove(file_path)
					image.save(new_file_path)
					print(f"Moved and modified {file} to {new_file_name}")
				else:
					print(f"Skipped {file}")

# 用法示例
folder_path = './Temp'
move_images_in_folder(folder_path)