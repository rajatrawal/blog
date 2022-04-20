from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('createPost/',views.create_post,name='create_post'),
    path('myPosts/',views.my_posts,name='my_posts'),
    path('blogNo/<int:id>/',views.blog_no,name='blog_no'),
    path('unDraft/<int:id>/',views.un_draft,name='un_draft'),
    path('doctors',views.doctors,name='doctors'),
    path('book_apmt',views.book_apmt,name='book_apmt'),
    path('my_apmt',views.my_apmt,name='my_apmt'),
]
