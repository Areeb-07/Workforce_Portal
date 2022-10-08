from django.urls import re_path,path,include
from .views import coordinator_list
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register(r'cg',views.CGViewSet)
router.register(r'coordinators',views.CoordinatorViewSet)

urlpatterns = [ 
    path('',include(router.urls)),
    path('coordinators', views.coordinator_list),
]