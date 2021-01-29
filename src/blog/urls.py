from django.urls import path
from .views import get_posts,create_post,get_post,update_delete_post,get_comments,create_comment,get_likes,create_delete_like,get_postviews,create_postview
urlpatterns=[
    path("get_posts/",get_posts),
    path("create_post/",create_post),
    path("<int:post_id>/get_post/",get_post),
    path("<int:post_id>/update_delete_post/",update_delete_post),
    path("<int:post_id>/get_comments/",get_comments),
    path("<int:post_id>/create_comment/",create_comment),
    path("<int:post_id>/get_likes/",get_likes),
    path("<int:post_id>/create_delete_like/",create_delete_like),
    path("<int:post_id>/get_postviews/",get_postviews),
    path("<int:post_id>/create_postview/",create_postview)
    # path("get_posts_list",get_posts_list,name="get_posts_list"),
    # path("create_post",create_post,name="create_post")
]