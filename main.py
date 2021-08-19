from pdf2image import convert_from_path
pages = convert_from_path('path-to-pdf-file')
count = 0
for page in pages:
     count +=1
     page.save('file-'+str(count)+'.jpg', 'JPEG')