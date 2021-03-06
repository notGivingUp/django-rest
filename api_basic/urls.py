from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetail, GenericAPIView

urlpatterns = [
    #path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    #path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetail.as_view()),
    #path('generic/article/<int:id>/', GenericAPIView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
]