from django.urls import path
from .views import post_list_create,post_update_delete
urlpatterns=[
    path("list_create/",post_list_create),
    path("<int:id>/",post_update_delete)
    # path("get_posts_list",get_posts_list,name="get_posts_list"),
    # path("create_post",create_post,name="create_post")
]