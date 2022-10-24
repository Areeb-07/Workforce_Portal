from django.urls import re_path,path,include
from .views import *
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'cgs',views.CGViewSet)
router.register(r'tasks',views.TaskViewSet)
router.register(r'progress',views.ProgressViewSet)
router.register(r'coordinators',views.CoordinatorViewSet)

urlpatterns = [ 
    path('',include(router.urls)),
    path('coordinators', views.coordinator),
    path('cgs', views.cg),
]