import os
from docx import Document

filePath = 'E:/zyd2017/TianHongBauMu/app/src/main/java/com/fanqie/tianhong/business/mine'
saveFileName = 'test.docx'

def ergodicFile(document , path):
    fileLists = os.listdir(path)
    for fileItem in fileLists:
        filePath = path + "/" + fileItem
        print("filePath:" + filePath)
        if filePath.endswith(".java"):
            with open(filePath , 'r', encoding='UTF-8') as readContent:
                document.add_paragraph(readContent.read())
        else:
            print("not endwith filePath:" + filePath)
            ergodicFile(document , filePath)



document = Document()
ergodicFile(document , filePath)
document.save(saveFileName)
