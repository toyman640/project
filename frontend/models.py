from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name='First name')
    last_name = models.CharField(max_length=100, verbose_name='Last name')
    email = models.CharField(max_length=100, verbose_name='Email')
    p_img = models.ImageField(null=True, verbose_name='Profile Image', blank=True, upload_to='uploads/')


class UserProfile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, verbose_name='Profile Image', blank=True, upload_to='uploads/')

    def __str__(self):
        return self.user.username

    def pst_img(self):
        if self.avatar:
          return self.avatar.url



class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Category Name')
    cat_desc = models.TextField(blank=True, null=True, verbose_name='Description')
    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name_plural='Post Category'



    
class PostPage(models.Model):
    pst_image1 = models.ImageField(null=True, verbose_name='Image1', blank=True, upload_to='uploads/')
    pst_image2 = models.ImageField(null=True, verbose_name='Image2', blank=True, upload_to='uploads/')
    pst_image3 = models.ImageField(null=True, verbose_name='Image3', blank=True, upload_to='uploads/')
    pst_image4 = models.ImageField(null=True, verbose_name='Image4', blank=True, upload_to='uploads/')
    pst_image5 = models.ImageField(null=True, verbose_name='Image5', blank=True, upload_to='uploads/')
    pst_title = models.CharField(max_length=150, verbose_name='House type')
    pst_description = models.TextField(max_length=350, verbose_name='Description')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Price')
    room =  models.IntegerField(verbose_name='Rooms')
    bath = models.IntegerField( null=True, verbose_name='Bathrooms')
    toilet = models.IntegerField( null=True, verbose_name='Toilet')
    category = models.ManyToManyField(Category, verbose_name='Offer type')
    posted = models.DateTimeField(default = datetime.now)
    featured = models.BooleanField(blank=True)
    sponsored = models.BooleanField(blank=True)

    def __str__(self):
        return self.pst_title

    class Meta():
        verbose_name_plural = 'Post'

    def post_img1(self):
        if self.pst_image1:
          return self.pst_image1.url

    def post_img2(self):
        if self.pst_image1:
          return self.pst_image2.url

    def post_img3(self):
        if self.pst_image1:
          return self.pst_image3.url

    def post_img4(self):
        if self.pst_image1:
          return self.pst_image4.url

    def post_img5(self):
        if self.pst_image1:
          return self.pst_image5.url
