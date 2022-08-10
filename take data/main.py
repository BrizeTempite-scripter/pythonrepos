from datetime import datetime
from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import *
import sys
from selenium.webdriver.common.by import By
from selenium import webdriver
from threading import *
import time
import os
os.chdir(os.path.dirname(__file__))
if os.path.exists(os.getcwd()+"/data")==False:
  os.mkdir(os.getcwd()+"/data")
if os.path.exists(os.getcwd()+"/setting")==False:
  os.mkdir(os.getcwd()+"/setting")


class App(QMainWindow):
  def __init__(self):
    super(App, self).__init__()
    self.ui=Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.start_wath_data)
    self.ui.pushButton_2.clicked.connect(self.get_link)
    self.ui.save_data.stateChanged.connect(self.save_data_anim)
    self.ui.pushButton_3.clicked.connect(self.last_settings)
    self.ui.textEdit_3.setText("1")
    self.ui.textEdit_4.setText("1000")
    t1=Thread(target=self.start_driver)
    t1.start()

  def last_settings(self):
    if os.path.exists(os.getcwd()+"/setting/op.txt"):
      with open(os.getcwd()+"/setting/op.txt", "r") as f:
        reads=f.readlines()
        self.ui.textEdit_2.setText(reads[0])
        self.get_link()
        self.ui.textEdit.setText(reads[1])
        reads[2]=int(reads[2])  
        if reads[2]==2:
          self.ui.save_data.setChecked(True)
        else:
          self.ui.save_data.setChecked(False)
        self.ui.textEdit_3.setText(reads[3])
        self.ui.textEdit_4.setText(reads[4])

      



  def save_data_anim(self):
    t1=Thread(target=self.save_data_anim_clac)
    t1.start()

  def save_data_anim_clac(self):
    print(self.ui.save_data.checkState())
    if(self.ui.save_data.checkState()==2):
      self.ui.frame_save.setFixedHeight(171)
    else:
      self.ui.frame_save.setFixedHeight(71)



  def get_link(self):
    link=self.ui.textEdit_2.toPlainText()
    self.ui.state.setText("true")
    self.driver.get(link)
    self.ui.label_5.setEnabled(True)
    self.ui.textEdit.setEnabled(True)
    self.ui.pushButton.setEnabled(True)
    
  def start_driver(self):
    optionse = webdriver.ChromeOptions()
    optionse.add_argument('headless')
    self.driver = webdriver.Chrome('chromedriver', options=optionse)

  def start_wath_data(self):
    t2=Thread(target=self.open_precess_window)
    t2.start()
    t1=Thread(target=self.watch_data)
    t1.start()
    with open(os.getcwd()+"/setting/op.txt", "w") as f:
      text1=self.ui.textEdit_2.toPlainText()
      text1=text1.replace("\n","")
      text2=self.ui.textEdit.toPlainText()
      text2 = text2.replace("\n","")
      text3 =self.ui.textEdit_3.toPlainText()
      text3=text3.replace("\n","")
      text4=self.ui.textEdit_4.toPlainText()
      text4=text4.replace("\n","")
      f.write(text1+"\n")
      f.write(text2+"\n")
      f.write(str(self.ui.save_data.checkState())+"\n")
      f.write(text3+"\n")
      f.write(text4+"\n")

  def open_precess_window(self):
    for i in range(16,601,5):
      time.sleep(0.01)
      self.ui.frame_statu_main.setFixedHeight(i)


  def watch_data(self):
    files=[]
    delay=int(self.ui.textEdit_3.toPlainText())
    ranger=int(self.ui.textEdit_4.toPlainText())
    start_time=datetime.now()
    xpats=self.ui.textEdit.toPlainText()
    xpats_list=xpats.split("!")
    save_file=self.ui.save_data.checkState()
    if(save_file==2):
      for i in xpats_list:
        file=open(os.getcwd()+f"/data/{xpats_list.index(i)}.txt","a+")
        
        files.append(file)
    for a in range(ranger):

      time.sleep(delay)
      self.ui.label_11.setText(str(a)+"/"+str(ranger))
      atributes=[]
      for i in xpats_list:
        atribute=self.driver.find_element(By.XPATH,i).get_attribute("innerHTML")
        atributes.append(atribute)
      string=""
      for i in atributes:
        string+="data"+"["+str(atribute.index(i))+"]"+" = " +i
        if(save_file==2):
          files[atributes.index(i)].write(i+"\n")
      self.ui.label_15.setText(string+"  !!!!!!"+str(a))
      end_time=datetime.now()
      self.ui.label_12.setText(str(end_time-start_time))
      
      

def app():
  app = QApplication(sys.argv)
  win=App()
  win.show()
  sys.exit(app.exec_())
  
app()

