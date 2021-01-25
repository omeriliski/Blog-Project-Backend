from django.urls import path
from .views import post_list_create,post_update_delete,comment_list_create,like_list_create_delete,postview_list_create
urlpatterns=[
    path("post_list_create/",post_list_create),
    path("<int:post_id>/post_update_delete",post_update_delete),
    path("<int:post_id>/comment_list_create",comment_list_create),
    path("<int:post_id>/like_list_create_delete",like_list_create_delete),
    path("<int:post_id>/postview_list_create",postview_list_create) 
    # path("get_posts_list",get_posts_list,name="get_posts_list"),
    # path("create_post",create_post,name="create_post")
]