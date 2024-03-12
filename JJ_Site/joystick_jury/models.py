from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename): 
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return 'user_{0}/{1}'.format(instance.user.id, filename) 

# Create your models here.
class UserProfile(models.Model):  # TODO: Can probably customize the User class instead?
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to = user_directory_path)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    post_date = models.DateTimeField("date published")

    num_stars = models.SmallIntegerField(default=0)
    review_title = models.CharField(max_length=200)
    review_text = models.CharField(max_length=5000)
    game_id = models.CharField(max_length=200)

    def __str__(self):
        return self.review_title