from django.urls.conf import path
from .views import Index,json

urlpatterns=[
    path('api',json),
    path('',Index.as_view(),name="index")
]