from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.todo_fun,name='todo_fun'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('cbvlist',views.Tasklistview.as_view(),name='cbvlist'),
    path('cbvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteview.as_view(), name='cbvdelete'),

]
