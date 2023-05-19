from django.urls import path,include
from . import views
urlpatterns = [
    path('dashboard/',views.student),
    path('courses/',views.coureses),
    path('view_student/',views.view_student),
    path('index/',views.index),
    path('',views.sign_up),
    path('registration/',views.registration),
    path('course_add/',views.course_add),
    path('user_login/',views.user_login),
    path('addstudent/',views.addstudent),
    path('deletecourse/',views.deletecourse),
     path("update/<int:uid>/",views.update),  
    path('updatecourse/',views.updatecourse),
    
]
