from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def city_aqi(request):
    c=request.POST['city']
    return render(request,'aqi_city.html',{'name':c})

def prediction(request,city):
    p1 = float(request.POST['pm10'])
    p2 = float(request.POST['pm2'])
    s = float(request.POST['so'])
    c = float(request.POST['co'])
    nx = float(request.POST['nox'])
    nh = float(request.POST['nh3'])
    o3 = float(request.POST['o3'])
    if city=="THRISSUR":
        data_2023 = pd.read_excel(r"AQI DATASET_2023_2022.xlsx",sheet_name = '2023')
        data_2022 = pd.read_excel(r"AQI DATASET_2023_2022.xlsx",sheet_name = '2022')
        data_2022_2=pd.read_excel(r"AQI DATASET_2023_2022.xlsx",sheet_name = '2022_AUG_DEC')
        data_2023.dropna(inplace=True)
        data_2022_2.dropna(inplace=True)
        data_2022.dropna(inplace=True)
        PM10 = pd.concat([data_2022_2[' PM10_'], data_2023['PM10'], data_2022['PM10(µg/m3)']])
        PM2 = pd.concat([data_2022_2[' PM2.5_'], data_2023['PM2.5_'], data_2022['PM2.5(µg/m3)']])
        SO = pd.concat([data_2022_2[' SO2_'], data_2023['SO2'], data_2022['SO2(µg/m3)']])
        CO = pd.concat([data_2022_2[' CO_'], data_2023['CO_'], data_2022['CO(mg/m3)']])
        NOX = pd.concat([data_2022_2[' NOx_'], data_2023['NOX'], data_2022['NOx(µg/m3)']])
        NH3 = pd.concat([data_2022_2[' NH3'], data_2023['NH3_'], data_2022['NH3(µg/m3)']])
        O3 = pd.concat([data_2022_2[' O3_'], data_2023['O3_'], data_2022['O3(µg/m3)']])
        AQI = pd.concat([data_2022_2['AQI'], data_2023['AQI'], data_2022['AQI']])
        data = pd.DataFrame({'PM10': PM10, 'PM2': PM2, 'SO': SO, 'CO': CO, 'NOX': NOX, 'NH3': NH3, 'O3': O3, 'AQI': AQI})
        X = data.drop(columns=['AQI'])
        y = data['AQI']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        z=np.array([[p1,p2,s,c,nx,nh,o3]])
        result=model.predict(z)

    elif city=="PLAMOOD":
       
        datap_2022 = pd.read_excel(r"plamood_aqi.xlsx", sheet_name='2022')
        datap_2023 = pd.read_excel(r"plamood_aqi.xlsx", sheet_name='2023')
        datap_2022.dropna(inplace=True)
        datap_2023.dropna(inplace=True)
        PM10 = pd.concat([datap_2022['PM10(µg/m3)'], datap_2023['PM10']])
        PM2 = pd.concat([datap_2022['PM2.5(µg/m3)'], datap_2023['PM2.5']])
        SO = pd.concat([datap_2022['SO2(µg/m3)'], datap_2023['SO2']])
        CO = pd.concat([datap_2022['CO(mg/m3)'], datap_2023['CO']])
        NOX = pd.concat([datap_2022['NOx(µg/m3)'], datap_2023['NOX']])
        NH3 = pd.concat([datap_2022['NH3(µg/m3)'], datap_2023['NH3']])
        O3 = pd.concat([datap_2022['O3(µg/m3)'], datap_2023['Ozone']])
        AQI = pd.concat([datap_2022['AQI'], datap_2023['AQI']])
        datap = pd.DataFrame({'PM10': PM10, 'PM2': PM2, 'SO': SO, 'CO': CO, 'NOX': NOX, 'NH3': NH3, 'O3': O3, 'AQI': AQI})
        X = datap.drop(columns=['AQI'])
        y = datap['AQI']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        regressor = RandomForestRegressor(n_estimators=10, random_state=0)
        regressor.fit(X_train, y_train)
        result=regressor.predict(np.array([[p1, p2, s, c, nx, nh, o3]]))
    elif city == "KARYAVATTOM":
        
        # C:\Users\AQI\karyavattom_aqi.xlsx
        datak_2022 = pd.read_excel(r"karyavattom_aqi.xlsx", sheet_name='2022')
        datak_2023 = pd.read_excel(r"karyavattom_aqi.xlsx", sheet_name='2023')
        datak_2022.dropna(inplace=True)
        datak_2023.dropna(inplace=True)
        PM10 = pd.concat([datak_2022['PM10(µg/m3)'], datak_2023[' PM10']])
        PM2 = pd.concat([datak_2022['PM2.5(µg/m3)'], datak_2023[' PM25']])
        SO = pd.concat([datak_2022['SO2(µg/m3)'], datak_2023[' SO2']])
        CO = pd.concat([datak_2022['CO(mg/m3)'], datak_2023[' CO']])
        NOX = pd.concat([datak_2022['NOx(µg/m3)'], datak_2023[' NOX']])
        NH3 = pd.concat([datak_2022['NH3(µg/m3)'], datak_2023[' NH3']])
        O3 = pd.concat([datak_2022['O3(µg/m3)'], datak_2023[' O3']])
        AQI = pd.concat([datak_2022['AQI'], datak_2023['AQI']])
        datak = pd.DataFrame({'PM10': PM10, 'PM2': PM2, 'SO': SO, 'CO': CO, 'NOX': NOX, 'NH3': NH3, 'O3': O3, 'AQI': AQI})
        X = datak.drop(columns=['AQI'])
        y = datak['AQI']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        regressor = RandomForestRegressor(n_estimators=10, random_state=0)
        regressor.fit(X_train, y_train)
        result=regressor.predict(np.array([[p1, p2, s, c, nx, nh, o3]]))
    category = ""
    h = ""
    s = ""
    c = ""
    if result>0 and result<=50:
        category="GOOD"
    elif result>50 and result<=100:
        category="SATISFACTORY"
    elif result>100 and result<=200:
        category="MODERATE"
    elif result>200 and result<=300:
        category="POOR"
    elif result > 300 and result <= 400:
        category ="VERY POOR"
    elif result>400:
        category="SEVERE"
    status=category
    if status == "GOOD":
        h = "Air quality is satisfactory and poses little and no risk"
        s = "No health implications for population"
        c = "Enjoy outdoor activities without concerns"

    elif status == "SATISFACTORY":
        h = "Sensitive individuals avoid outdoor activities and they may experience respiratory symptoms"
        s = "People with respiratory/heart issues,childrens"
        c = "Sensitive individuals should consider reducing prolonged outdoor activities"

    elif status == "MODERATE":
        h = "Gneral public and sensitive individuals may experience irritation and respiratory problems"
        s = "People with respiratory/heart issues,childrens"
        c = "Sensitive groups should limit outdoor activities"

    elif status == "POOR":
        h = "Increased likelihood of adverse effects & issues to heart and lungs among general public"
        s = "People with respiratory/heart issues,childrens"
        c = "Everyone should reduce prolonged outdoor activities"

    elif status == "VERY POOR":
        h = "General public will be noticably affected .Sensitive groups should restrict outdoor activities"
        s = "General public and those with respiratory/heart conditions,childrens,elders"
        c = "Avoid outdoor activities, stay indoor as possible."

    elif status == "SEVERE":
        h = "General public at high risk of experiencing strong irritation and adverse health effects.Should avoid outdoor activities"
        s = "Everyone and those with respiratory/heart conditions,childrens,elders"
        c = "Avoid outdoor exposure completely,remains indoor always."
    return render(request,"statement_page.html",{'key':result,'status':category,"h":h,"s":s,"c":c})




      # return render(request,"statement_page.html",{'category':status,"h":h,"s":s,"c":c})

      # return HttpResponse(status)

def announcement(request):
    return render(request,"announcement.html")

def trends(request):
    return render(request,"plots.html")

def aqi(request):
    return render(request,"AQI.html")

def pollutants(request):
    return render(request,"pollutants.html")

def health(request):
    return render(request,"health.html")

def calc(request):
    return render(request,"calc.html")

def use(request):
    return render(request,"use.html")

def con(request):
    return render(request,"CONTACT.html")

















