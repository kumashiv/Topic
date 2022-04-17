from django.urls import path
from . import views

app_name='learning_logs'

urlpatterns = [
    #HomePage
    path('', views.index, name='index'),
    path('topics/<int:topic_id>', views.topic, name='topic'),
]
