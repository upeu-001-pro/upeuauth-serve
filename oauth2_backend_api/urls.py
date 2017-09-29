from django.conf.urls import url, include
from rest_framework import routers

from .views.api_localuserinfo import LocalUserInfoView
from .views.api_user_menu import UserMenuView
from .views.api_routers import RouterView
from .views.api_logs import LogView

router = routers.DefaultRouter()
#router.register(r'menus', MenuViewSet)

urlpatterns = [

    url(r'^localuserinfo/$', LocalUserInfoView.as_view()),
    url(r'^usermenu/$', UserMenuView.as_view()),
    url(r'^usermenu/(?P<module>[^/]+)/$', UserMenuView.as_view()),
    url(r'^routers/$', RouterView.as_view()),
    url(r'^logs/(?P<param>[^/]+)/$', LogView.as_view()),
    #url(r'^', include(router.urls)),


]
