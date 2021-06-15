from django.urls import path
from . import views 


app_name = 'bloglist'

urlpatterns = [
    # post views
    #path('', views.post_list, name='post_list'),
    path('', views.home, name='home'),
    path('index.html', views.home),
    path('prova.html', views.prova, name='prova'),
    path('<slug>', views.Dettaglio.as_view()),
    #path('', views.PostListView.as_view(), name='post_list'),
    #path('<int:year>/<int:month>/<int:day>/<slug:post>/',views.post_detail,name='post_detail'),
    #path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),     
] 