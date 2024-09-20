from django.db import models

# Create your models here.
 
class ProjectState(models.Model):
    state_of = models.CharField(max_length=200)

    def __str__(self):
        return self.state_of

class TechStack(models.Model):
    stack_name = models.CharField(max_length=200)

    def __str__(self):
        return self.stack_name

class Porfolio(models.Model):
    site_name = models.CharField(max_length=100)
    site_url = models.URLField(max_length=200)
    git_repo = models.URLField(max_length=200)
    site_image = models.ImageField(upload_to="site_images/")
    stacks = models.ManyToManyField(TechStack)
    state_of_project = models.OneToOneField(ProjectState, on_delete=models.CASCADE)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.site_name
    