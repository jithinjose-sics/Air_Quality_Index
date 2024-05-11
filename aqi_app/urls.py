from django.urls import path
from . import views
app_name='aqi_app'
urlpatterns=[
    path("",views.index,name='index'),
    path("city_aqi",views.city_aqi,name='city_aqi'),
    path("prediction/<city>",views.prediction,name='prediction'),
    # path("state_page",views.state_page,name="state_page"),
    path("announcement",views.announcement,name="announcement"),
    path("trends",views.trends,name="trends"),
    path("home",views.index,name='index'),
    path("aqi",views.aqi,name='aqi'),
    path("pollutants",views.pollutants,name='pollutants'),
    path("health",views.health,name='health'),
    path("calc",views.calc,name='calc'),
    path("use",views.use,name='use'),
    path("con",views.con,name="con"),
    path("work",views.work, name="work")

]