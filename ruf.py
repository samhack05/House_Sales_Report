import urllib.request
for i in range(22390,22398):
    urllib.request.urlretrieve("https://erp.psit.in/assets/img/Simages/"+str(i)+".jpg", str(i)+".jpg")
