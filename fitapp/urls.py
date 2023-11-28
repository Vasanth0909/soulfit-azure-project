
from django.urls import path
from fitapp import views
from .views import register

urlpatterns = [
    path('',views.home,name="home"),
    path('ridepopup/register/',views.register_view,name="register"),
    path('ridepopup/',views.ridepopup,name="ridepopup"),
    path('soul/',views.soul,name="soul"),
    path('spirit/',views.spirit,name="spirit"),
    path('soul/register/',views.register_view,name="register"),
    path('gear/',views.gear,name="gear"),
    path('fitzz/',views.fitzz,name="fitzz"),
    path('fitzz/cheackout/',views.cheackout,name="cheackout"),
    path('spirit/register/',views.register_view, name="register"),
    path('gear/cheackout/',views.cheackout,name="cheackout"),
    path('login/',views.login,name="login"),
    path('bot/' ,views.bot,name="bot"),
    path('signup/',views.signup, name="signup"),
    path('register/', register, name='register'),
]