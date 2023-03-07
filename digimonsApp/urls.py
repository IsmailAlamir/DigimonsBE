from django.urls import path
from .views import digimonsListView,allDigimons,digimonsDetailView


urlpatterns=[
    path('allDigimons/',allDigimons.as_view()),
    path('',digimonsListView.as_view()),
    path('<pk>',digimonsDetailView.as_view()),

]