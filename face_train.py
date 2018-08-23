import os

Base_dir = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(Base_dir,"image")

for root,dirs,files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root,file)
			label = os.path.basename(root).replace(" ","-").lower()
			print(label,path)


