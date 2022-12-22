from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostUpdate, PostDelete, CategoryListView, subscribe


urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('catigories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('catigories/<int:pk>/subscribe', subscribe, name='subscribe')
]