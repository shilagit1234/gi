from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/tutorials', views.book_list),
    url(r'^api/tutorials/(pk)', views.book_detail),
    url(r'^api/tutorials/published', views.book_list_published),
    url(r'^api/tutorials/aut', views.author_list),
    url(r'^api/tutorials/author/(pk)', views.author_detail),
    url(r'^api/tutorials/published/author', views.author_list_published)
]
