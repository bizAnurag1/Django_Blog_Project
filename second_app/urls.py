from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name = 'index'),
    path('about/', views.about, name="about"),
    path('contactus/', views.contactus, name="contactus"),
    path('detailed_blog/<int:id>', views.detailed_blog, name="detailed_blog"),
    path('author_detail/', views.author_detail, name ="author_detail"),
    path('author_blog/<int:id>', views.author_blog, name ="author_blog"),
    path('new_blog/', views.BlogCreateView.as_view(), name="new_blog"),
    path('edit_blog/<int:pk>', views.BlogUpdateView.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>', views.BlogDeleteView.as_view(), name='delete_blog'),
    path('add_commment/', views.AddCommentView.as_view(), name="add_comment"),
]