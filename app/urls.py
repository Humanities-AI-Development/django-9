from django.urls import path
from . import views
app_name='app'
urlpatterns=[
    path('',views.HelloClass.as_view(),name='index'),
    path('list/',views.AppList.as_view(),name='app-list'),
    path('detail/<int:pk>/',views.AppDetail.as_view(),name='app-detail'),
    path('create/',views.AppCreate.as_view(),name='app-create'),
    path('delete/<int:pk>',views.AppDelete.as_view(),name='app-delete'),
    path('update/<int:pk>',views.AppUpdate.as_view(),name='app-update'),
    path('comment/create/<int:key>',views.CommentCreate.as_view(),name='comment-create'),
    


    
]