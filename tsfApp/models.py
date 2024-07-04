from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import NamedValuesListIterable
from django.views.generic import TemplateView
from braces import views

# Create your models here.

#backend user model
class user(models.Model):
    user_id = models.CharField(max_length=100, default = '0')
    name = models.CharField(max_length=100, default = '0')
    email = models.EmailField(max_length=100, default = '0')
    password = models.CharField(max_length=100, default = '0')
    phone = models.CharField(max_length=100, default = '0')
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    donation_value = models.IntegerField(default=0)

    objects = models.Manager()

    #perminssions

    comments_allowed = models.BooleanField(default=False)
    donation_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class member(User):
    additional_field = models.CharField(max_length=100)
    events_allowed = models.BooleanField(default=True)
    settings_allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class visitor(models.Model):
    visitor_id = models.CharField(max_length=100, default = '0')
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

    #perminssions

    donation_allowed = models.BooleanField(default=True)
    def __str__(self):
        return self.visitor_id

#backend funcionalities model

'''
    class comment(models.Model):
    comment_id = models.CharField(max_length=100)
    comment_user = models.ForeignKey(user, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_created_at = models.DateTimeField(auto_now_add=True)
    comment_deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_id
'''

class post(models.Model):
    post_id = models.CharField(max_length=100, default = '0')
    post_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=100, default='Default project text')
    post_text = models.TextField(default = '0')
    post_image = models.ImageField(upload_to='post_images')
    #post_comments = models.ForeignKey(comment, on_delete=models.CASCADE)
    post_created_at = models.DateTimeField(auto_now_add=True)
    post_deleted_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.post_id

class event(models.Model):
    event_id = models.CharField(max_length=100, default = '0')
    event_name = models.CharField(max_length=100, default = '0')
    event_description = models.TextField(default = '0')
    event_date = models.DateTimeField(auto_now_add=True)
    event_location = models.CharField(max_length=100, default = '0')
    event_image = models.ImageField(upload_to='event_images')
    envent_user = models.ForeignKey(User, on_delete=models.CASCADE, default = 0)
    #event_comments = models.ForeignKey(comment, on_delete=models.CASCADE)
    event_created_at = models.DateTimeField(auto_now_add=True)
    event_deleted_at = models.DateTimeField(auto_now_add=True)
    event_hours_value = models.IntegerField(default=0)

    objects = models.Manager()


    def __str__(self):
        return self.event_name

class donation(models.Model):
    donation_id = models.CharField(max_length=100, default = '0')
    donation_user = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_value = models.IntegerField()
    donation_created_at = models.DateTimeField(auto_now_add=True)
    donation_deleted_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


    def __str__(self):
        return self.donation_id


class project(models.Model):
    project_id = models.CharField(max_length=100, default = '0')
    project_name = models.CharField(max_length=100, default = '0')
    project_description = models.TextField(default='Default project text')
    project_text = models.TextField(default='Default project text')
    project_image = models.ImageField(upload_to='project_images')
    #project_comments = models.ForeignKey(comment, on_delete=models.CASCADE)
    project_created_at = models.DateTimeField(auto_now_add=True)
    project_deleted_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


    def __str__(self):
        return self.project_name
