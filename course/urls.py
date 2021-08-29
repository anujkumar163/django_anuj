from django.urls import path
from course import views

urlpatterns = [
    
    path('learn_django/', views.learn_django),
    path('learnpy/', views.learn_python),
    path('learnv/', views.learn_var),
    path('learnm/', views.learn_math),
    path('learnf/', views.learn_format),
]