#mumbai
#getting the live  wind speed and direction
#======================================
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
url="https://weather.com/en-IN/weather/tenday/l/bc7797d0f3a030a46ffd2fe99d531f7818ef054a8768ac9988747d5a6f4b7949"
#get the html
r =requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup=BeautifulSoup(htmlcontent,"html.parser")
speed=soup.find_all("span", {"class": "Wind--windWrapper--3Ly7c DailyContent--value--1Jers", "data-testid": "Wind"})
#print(speed)
all_speed=[]
for word in speed:
    all_example = word.get_text()
    all_speed.append(all_example)
    
#rint(all_speed)
#==================================

#now seperation the wind speed values and typecasting it into int form string
#======================================
wspeed1=[]
for i in all_speed:
    a2=i[-7:-5]
    wspeed1.append(int(a2))
print(wspeed1)
#======================================

#now seperation the wind direction
#======================================
wdir=[]
for i in all_speed:
    a=i[0:3]
    wdir.append(a)
for i in wdir:
     if i=='W 1':
        x=wdir.index(i)
        wdir[x]="W "
print("Mumbai:",wdir)
#======================================
#wspeed1
#wdir




#chennai
#getting the live  wind speed and direction
#======================================
import requests
from bs4 import BeautifulSoup
url="https://weather.com/en-IN/weather/tenday/l/680edc8aa8a645e29b5c7528ef5ffeb1a7bc4b825dd02f8ec17574c12f91017d"
#get the html
r =requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup=BeautifulSoup(htmlcontent,"html.parser")
speed2=soup.find_all("span", {"class": "Wind--windWrapper--3Ly7c DailyContent--value--1Jers", "data-testid": "Wind"})
#print(speed2)
all_speed2=[]
for word in speed2:
    all_example2 = word.get_text()
    all_speed2.append(all_example2)
    
#all_speed2
#print(all_speed2)
#======================================

#now seperating the wind speed values and typecasting it into int form string
#======================================
wspeed2=[]
for i in all_speed2:
    a1=i[-7:-5]
    wspeed2.append(int(a1))
print(wspeed2)
#print(len(wspeed2))
#======================================

#now seperating the wind direction
#======================================
wdir2=[]
for i in all_speed2:
    a=i[0:3]
    wdir2.append(a)

for i in wdir2:
    if i=='S 1':
        x=wdir2.index(i)
        wdir2[x]="S "
    elif i=='S 2':
        x=wdir2.index(i)
        wdir2[x]="S "
        
print("Chennai:",wdir2)
#======================================
#wspeed2
#wdir2




#delhi
#getting the live  wind speed and direction
#======================================
import requests
from bs4 import BeautifulSoup
url="https://weather.com/en-IN/weather/tenday/l/c6b355c14f71d06998f2f563bbcf7d20916a998d77aa907c7e354657aa458d51"
#get the html
r =requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup=BeautifulSoup(htmlcontent,"html.parser")
speed3=soup.find_all("span", {"class": "Wind--windWrapper--3Ly7c DailyContent--value--1Jers", "data-testid": "Wind"})
#print(speed3)
all_speed3=[]
for word in speed3:
    all_example3 = word.get_text()
    all_speed3.append(all_example3)
    
all_speed3
#======================================

#getting wind speed values and converting it into int from string
#======================================
wspeed3=[]
for i in all_speed3:
    a3=i[-7:-5]
    wspeed3.append(int(a3))
print(wspeed3)
#======================================
 
#getting wind direction
#======================================   
wdir3=[]

for i in all_speed3:
    a=i[0:3]
    wdir3.append(a)
for i in wdir3:
    if i=='W 1':
        x=wdir3.index(i)
        wdir3[x]="W "
    elif i=='W 9':
        x=wdir3.index(i)
        wdir3[x]="W "
#======================================   

print("delhi",wdir3)
#wspeed3
#wdir3





#mumbai 
#getting the humidity
#======================================
import requests
from bs4 import BeautifulSoup
url="https://weather.com/en-IN/weather/tenday/l/d7a5333ba0420943bb2ec89f99f411f2f8e74d683fdc6c5cb309bc19ec107711#detailIndex5"
#get the html
r =requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup=BeautifulSoup(htmlcontent,"html.parser")
hum1=soup.find_all("span", {"class": "DetailsTable--value--2YD0-", "data-testid": "PercentageValue"})
#print(hum1)
all_hum1=[]
for word in hum1:
    all_humx = word.get_text()
    all_hum1.append(all_humx)
print(all_hum1)
#======================================

#converting the string percentage values into integer
#======================================
mhum=[]
for i in all_hum1:
    if len(i)==2:
        a=i[0:1]
    else:
        a=i[0:2]
    
    mhum.append(int(a))    
print("hello:",mhum)
#======================================
#mhum




#chennai 
#getting the humidity
#======================================
import requests
from bs4 import BeautifulSoup
url="https://weather.com/en-IN/weather/tenday/l/680edc8aa8a645e29b5c7528ef5ffeb1a7bc4b825dd02f8ec17574c12f91017d#detailIndex5"
#get the html
r =requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup=BeautifulSoup(htmlcontent,"html.parser")
hum2=soup.find_all("span", {"class": "DetailsTable--value--2YD0-", "data-testid": "PercentageValue"})
#print(hum2)
all_hum2=[]
for word in hum2:
    all_humx = word.get_text()
    all_hum2.append(all_humx)
print(all_hum2)
#======================================

#converting the string percentage values into integer
#======================================
chum=[]
for i in all_hum2:
    if len(i)==2:
        a=i[0:1]
    else:
        a=i[0:2]
    
    chum.append(int(a))    
print(chum)
#======================================
#chum





#delhi
#getting the humidity
#======================================
import requests
from bs4 import BeautifulSoup
url="https://weather.com/en-IN/weather/tenday/l/c6b355c14f71d06998f2f563bbcf7d20916a998d77aa907c7e354657aa458d51#detailIndex5"
#get the html
r =requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup=BeautifulSoup(htmlcontent,"html.parser")
hum3=soup.find_all("span", {"class": "DetailsTable--value--2YD0-", "data-testid": "PercentageValue"})
#print(hum3)
all_hum3=[]
for word in hum3:
    all_humx = word.get_text()
    all_hum3.append(all_humx)
print(all_hum3)
#======================================

#converting the string percentage values into integer
#======================================
dhum=[]
for i in all_hum3:
    if len(i)==2:
        a=i[0:1]
    else:
        a=i[0:2]
    
    dhum.append(int(a))    
print(dhum)
#======================================

#dhum

'''
plt.scatter(wspeed1,mhum,color='blue',label="Wind speed Vs\n Humidity")
plt.savefig('image/mumbai.png')
plt.xlabel("Wind Speed")
plt.ylabel("Humidity")
plt.title("MUMBAI")
plt.legend()
plt.show()


plt.scatter(wspeed2,dhum,color='black',label="Wind speed Vs\n Humidity")
plt.savefig('image/delhi.png')
plt.xlabel("Wind Speed")
plt.ylabel("Humidity")
plt.title("DELHI")
plt.legend()
plt.show()


plt.scatter(wspeed3,chum,color='yellow',label="Wind speed Vs\n Humidity")
plt.savefig('image/chennai.png')
plt.xlabel("Wind Speed")
plt.ylabel("Humidity")
plt.title("CHENNAI")
plt.legend()
plt.show()
'''
import datetime
from datetime import datetime, timedelta

presentday = datetime.now() 
presentday_f=presentday.strftime('%d-%m-%Y')
print ('Current Date: ' + presentday_f)

# Get Yesterday
tomorrow = presentday + timedelta(1)
tomorrow_f=tomorrow.strftime('%d-%m-%Y')
print ('Previous Date: ' + tomorrow_f)

# Get Tomorrow
nextday = presentday + timedelta(2)
nextday_f=nextday.strftime('%d-%m-%Y')
print ('Next Date: ' + nextday_f)


import pickle
model = pickle.load(open("weather_model.pickle", "rb"))
value=model.predict([[73.776042,15.904271,259.469583]])[0]
print("test prediction:",value)




from flask import Flask, request, render_template
app = Flask(__name__, template_folder='', static_folder='')
@app.route('/')
def home():
    mwdir=259.469583
    x=[mhum[0],wspeed1[0],mwdir]
    x2=[mhum[1],wspeed1[1],mwdir]
    x3=[mhum[2],wspeed1[2],mwdir]
    
    m_predict=model.predict([x])[0]
    m_predict2=model.predict([x2])[0]
    m_predict3=model.predict([x3])[0]
    print(m_predict2)
    
    ddir=225.1236
    delx=[dhum[0],wspeed3[0],ddir]
    delx2=[dhum[1],wspeed3[2],ddir]
    delx3=[dhum[2],wspeed3[2],ddir]
    d_predict=model.predict([delx])[0]
    d_predict2=model.predict([delx2])[0]
    d_predict3=model.predict([delx3])[0]

    cdir=180.5478
    chenx=[chum[0],wspeed2[0],cdir]
    chenx2=[chum[1],wspeed2[1],cdir]
    chenx3=[chum[2],wspeed2[2],cdir]
    c_predict=model.predict([chenx])[0]
    c_predict2=model.predict([chenx2])[0]
    c_predict3=model.predict([chenx3])[0]
    
    
    
    
    
    return render_template('index.html',current=presentday_f ,nextd=tomorrow_f ,nnextd=nextday_f ,
                           mum_predict=m_predict,mhum=all_hum1[0],mspeed=wspeed1[0],mum_predict2=m_predict2,mhum2=all_hum1[1],mspeed2=wspeed1[1],mum_predict3= m_predict3,mhum3=all_hum1[2],mspeed3=wspeed1[2],
                           chen_predict=c_predict,chum=all_hum2[0],cspeed=wspeed2[0],chen_predict2=c_predict2,chum2=all_hum2[1],cspeed2=wspeed2[1],chen_predict3=c_predict3,chum3=all_hum2[2],cspeed3=wspeed2[2],
                           del_predict=d_predict,dhum=all_hum3[0],dspeed=wspeed3[0],del_predict2=d_predict2,dhum2=all_hum3[1],dspeed2=wspeed3[1],del_predict3=d_predict3,dhum3=all_hum3[2],dspeed3=wspeed3[2])


if __name__ == "__main__":
    app.run(debug=False)
'''
import os
for file in os.listdir('C:/Users/Lenovo/Desktop/PblProject/public_html/image'):
    if file.endswith('.png'):
        os.remove("C:/Users/Lenovo/Desktop/PblProject/public_html/image/mumbai.png")
        os.remove("C:/Users/Lenovo/Desktop/PblProject/public_html/image/delhi.png")
        os.remove("C:/Users/Lenovo/Desktop/PblProject/public_html/image/chennai.png") 
'''
