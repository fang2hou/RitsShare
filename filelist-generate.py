import os
import time

webPageFile = open("1.js", "w+")
webPageFile.writelines("var filelistjs = [\n")
myroot = "./"

for (root, dirs, files) in os.walk(myroot):
	for file in files:
		filePath = os.path.join(root, file).replace("\\", "/")
		statinfo = os.stat(filePath)
		etime = time.localtime(statinfo.st_ctime)
		webPageFile.writelines("{ category: \"" + filePath.replace(myroot, "").replace(file, "").replace("/", "") + "\", name: \"" + file + "\", update: \"" + "\", path: \""+ filePath + "\"},\n")

webPageFile.writelines("]")
webPageFile.close()