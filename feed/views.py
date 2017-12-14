from django.views.generic import DetailView

from feed.models import Post, Comment


class PostView(DetailView):
    model = Post


class CommentView(DetailView):
    model = Comment
