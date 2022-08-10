
import os 
import datetime

while True:
  os.chdir(os.path.dirname(__file__))
  data=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  data=str(data)
  if os.path.exists(os.getcwd()+ "/data")==False:
    os.mkdir(os.getcwd()+"/data")
  if os.path.exists(os.getcwd()+"/data/update.dat"):
    with open(os.getcwd()+"/data/update.dat", "r")as file:
      data= file.read()
    list_data=data.split(".")
    data=str(list_data[0])
    date_time_obj = datetime.datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
    dif=datetime.datetime.now()-date_time_obj
    minute=dif.seconds/60
    print("time since last update :"+str(minute))
    if(minute<1440):
      break

  with open(os.getcwd()+"/data/update.dat","w")as file:
    file.write(data)

  os.system("python -m pip install --upgrade pip")
  os.system("pip install selenium")
  break