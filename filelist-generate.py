import os
import datetime

webPageFile = open("archive/data/filelist.js", "w+")
webPageFile.writelines("var filelistjs = [\n")
scanDir = "LF"
studentID = "is0385rx"

for (root, dirs, files) in os.walk(scanDir):
	for file in files:
		filePath = os.path.join(root, file).replace("\\", "/")
		updatetime = datetime.datetime.fromtimestamp(os.path.getmtime(filePath)).strftime("%Y-%m-%d")
		webPageFile.writelines("{ category: \"" + filePath.replace(scanDir, "").replace(file, "").replace("/", "") + "\", name: \"" + file + "\", update: \"" + updatetime + "\", path: \"/~" + studentID + "/" + filePath + "\"},\n")

webPageFile.writelines("]")
webPageFile.close()
