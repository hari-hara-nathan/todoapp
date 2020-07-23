from django.urls import path,include
from Todoapp import views

urlpatterns =[
    path('',views.home,name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('addtodo', views.addtodo, name='addtodo'),
    path('delete/<int:del_id>',views.delete,name='delete'),
    path('done/<int:done_id>', views.done, name='done'),
    path('logout', views.logout, name='logout')
]