import os

from PIL import Image


def resize(filestr, basepath, savepath = "web", height = 1920, width = 1080):
	full_path = basepath + "\\" + savepath + "\\"
	print("Savepath is " + full_path )
	img = Image.open(basepath + "\\" + filestr)
	img.thumbnail((height, width), Image.ANTIALIAS)
	try:
		os.stat(full_path)
		print("Write Directory exists")
	except:
		os.mkdir(full_path)
		print("Creating new directory")
	img.save(full_path + filestr, "JPEG")
	print("Image saved")


def find_dir(path):
	test_list = os.listdir(path)
	file_list = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

	for file in file_list:
		print("File detail: " + file)
		if file.split(".")[-1] == "jpg":
			print("Resizing to full 2040p")
			resize(file, path, "full2040", 3640, 2040)
			print("Resizing to full 1080p")
			resize(file, path, "full1080")
			print("Resizing to full 720p")
			resize(file, path, "full720", 1280, 720)
			print("Resizing to thumbnail 512p")
			resize(file, path, "thumb512", 512, 512)
			print("Resizing to thumbnail 256p")
			resize(file, path, "thumb256", 256, 256)
			print("Resizing to thumbnail 128p")
			resize(file, path, "thumb128", 128, 128)

	print("Done!")


convert_dir = raw_input("Which directory needs to be converted?\n")
print("Converting " + convert_dir)
find_dir(convert_dir)