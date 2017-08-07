from django.db import models
from markdown import markdown
from .utils import gen_dirname

class PostManager(models.Manager):
    def create_post(self, title, author, content, owner):
        post = self.create(
            title=title, author=author, content=content, owner=owner)
        post.html = markdown(content)
        return post


class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    owner = models.IntegerField(default=0)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)
    html = models.TextField()

    def __str__(self):
        return self.title

    objects = PostManager()

    class Meta:
        permissions = (("can_post", "Can post"), ("can_vote_posts",
                                                  "Can vote on posts"), )


class Comment(models.Model):
    author = models.CharField(max_length=128)
    owner = models.IntegerField(default=0)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)
    votes = models.IntegerField(default=0)
    post = models.IntegerField(default=0)

    def __str__(self):
        return str(self.pk)

    class Meta:
        permissions = (("can_comment", "Can comment"),
                       ("can_vote_comments", "Can vote on comments"), )


class File(models.Model):
    author = models.CharField(max_length=128)
    owner = models.IntegerField(default=0)
    filename = models.CharField(max_length=128)
    content = models.FileField(upload_to=gen_dirname)
    mime = models.CharField(max_length=64)

    def __str__(self):
        return self.filename

    class Meta:
        permissions = (("can_upload", "Can upload files"), )
