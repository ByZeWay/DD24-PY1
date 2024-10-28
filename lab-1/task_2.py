symbSize = 4
symbLine = 25
linePage = 50
pageBook = 100
diskSize = 1.44*1024*1024

bookCnt = int(diskSize // (pageBook * linePage * symbLine * symbSize))

print("Количество книг, помещающихся на дискету:", bookCnt)
