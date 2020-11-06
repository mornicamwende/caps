from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()  
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# class Comment(models.Model):
#     comment = models.TextField(null=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(post,on_delete=models.CASCADE,related_name='comments')
#     created_on = models.DateTimeField(auto_now_add=True)
    

#     def save_comment(self):
#         self.save()

#     def delete_comment(self):
#         self.delete()
        
#     @classmethod
#     def get_comments(cls,id):
#         comments = cls.objects.filter(post__id=id)
#         return comments 
       
#     class Meta:
#         ordering = ['created_on']

#     def __str__(self):
#         return 'Comment {} by {}'.format(self.comment, self.author)