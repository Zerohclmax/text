# import requests
#
# headers={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
# }
# proxy='127.0.0.1:9743'
# proxies={
#     "http":"http://"+proxy,
#     "https":"https://"+proxy,
# }
# try:
#     response=requests.get("https://www.google.com",headers=headers,proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#      print('Error',e.args)
# else:
#     print("run ok!")
from PyQt5 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget();
window.show()
sys.exit(app.exec_())