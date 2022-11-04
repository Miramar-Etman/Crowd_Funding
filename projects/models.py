import datetime
from datetime import timedelta

from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


#############Ctegory Model ####################

class Category(models.Model):
    label = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return str(self.label)

############################# Project Model ############################
class Project(models.Model):
    title = models.CharField(max_length=150)
    details = models.TextField(max_length=1000)
    start_date = models.DateTimeField(default=datetime.datetime.now())
    end_date = models.DateTimeField(default=datetime.datetime.now()+timedelta(days=30))
    create_date = models.DateTimeField(blank=True,default=datetime.datetime.now())
    project_creator = models.ForeignKey(User, on_delete=models.CASCADE,default=None,blank=True, related_name="project")
    Category = models.ForeignKey(Category, on_delete=models.PROTECT,related_name="category")
    tags = TaggableManager(blank=True)
    target = models.PositiveIntegerField()
    total_donate = models.PositiveIntegerField(blank=True,default=0)
    is_featured = models.BooleanField(default=False)
    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('show_projects')
###################### Class Photo ###############################
class Photo(models.Model):
    project =models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project",blank=True)
    image = models.ImageField(null=True,blank=False,upload_to='media/',default='media/media/istockphoto-913374922-612x612.jpg')
    def __str__(self):
        return str(self.image)
#####################Model Donations for projects #################
class Donate(models.Model):
    amount = models.PositiveIntegerField()
    project = models.ForeignKey(
    Project, on_delete=models.CASCADE, related_name="donate",blank=True)
    user_donated = models.ForeignKey(User, on_delete= models.CASCADE,default=None, related_name="donate",blank=True)
    def __str__(self):
        return str(self.amount)


#######################Comment Model ########################
class Comment(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="comments")
    name = models.CharField(Project,max_length=150 )
    body = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' %(self.project.title,self.name)
    def get_absolute_url(self):  # new
        return reverse('single_proj', args=[str(self.project.id)])

###################### Rating #####################

class Rating(models.Model):
    scale = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.scale)

    class Meta:
        unique_together = ('project', 'user',)

###################### Reporting Project ###################
class ProjectReport(models.Model):
    reason = models.TextField(max_length=2000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="proj_rep")
    user_report = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return str(self.reason)

################### Reporting Comments #################
class CommentReport(models.Model):
    reason = models.TextField(max_length=2000)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user_report = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return str(self.reason)