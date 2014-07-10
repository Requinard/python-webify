import os

from PIL import Image


def resize(filestr, basepath, savepath = "web", width = 1080):
	full_path = basepath + "\\" + savepath + "\\"

	print("Savepath is " + full_path )

	img = Image.open(basepath + "\\" + filestr)
	img_ratio = img.size[0] / img.size[1]
	img.thumbnail((width * img_ratio, width), Image.ANTIALIAS)

	try:
		os.stat(full_path)
		print("Write Directory exists")
	except:
		os.mkdir(full_path)
		print("Creating new directory")

	img.save(full_path + filestr, "JPEG")

	print("Image saved")


def find_dir(path, sizes):
	test_list = os.listdir(path)
	file_list = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

	for file in file_list:
		print("File detail: " + file)
		if file.split(".")[-1] in ("jpg", "png", "gif"):
			for size in sizes:
				print("Resizing to " + str(size))
				resize(file, path, "img" + str(size), size)

		print("Done with file")
	print("Done!")


if True:
	size_list = []
	convert_dir = raw_input("Which directory needs to be converted?\n")
	print("Converting " + convert_dir)

	while True:
		size = raw_input(
			"List a resolution it needs to be converted to (2160, 1080, 720, etc). Leave empty to finish:\n")
		if size == "":
			break
		try:
			size_list.append(int(size))
		except:
			print(size + " is not a valid number")

	find_dir(convert_dir, size_list)