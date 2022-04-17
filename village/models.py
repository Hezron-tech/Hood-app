from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField



class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    creator = models.ForeignKey(User,null =True,on_delete=models.SET_NULL)
    profile_pic = CloudinaryField('image', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
   
    def delete_hood(self):
        self.delete()

    def update_hood(self,value):
        self.name = value
        self.save()
        
    @classmethod
    def all_hoods(self):
        hoods = Neighborhood.objects.all()    
        return hoods
    
    @classmethod
    def search_hood(self,search_name):
        hoods = Neighborhood.objects.filter(location__icontains=search_name) 
        return hoods
    


# class HoodMember(models.Model):
#     member = models.ForeignKey(User,on_delete=models.CASCADE)
#     hood = models.ForeignKey(Neighborhood, related_name='members',on_delete=models.CASCADE)
    
    
#     def __str__(self):
#         return '{} in {}'.format(self.member, self.hood)
    
# class Post(models.Model):
#     image = CloudinaryField('image', null=True,blank =True)
#     content = models.TextField( max_length=500)
#     author = models.ForeignKey(User,related_name='posts', on_delete=models.CASCADE)
#     date_posted = models.DateTimeField(auto_now_add=True)
#     neighborhood = models.ForeignKey(Neighborhood,related_name='hoodposts',on_delete=models.CASCADE)
    
    
#     def __str__(self):
#         return self.content
    
#     def save_post(self):
#         self.save()
        
#     def delete_post(self):
#         self.delete()
        
#     def edit_post(self,new_content):
#         self.content = new_content
#         self.save()
    
        
#     @classmethod    
#     def get_posts(self):
#         posts = Post.objects.all()
#         return posts
    
#     @classmethod    
#     def search_post(self, search_title):
#         posts= Post.objects.filter(title__icontains=search_title)
#         return posts



# class Business(models.Model):
#     name = models.CharField(max_length=100)
#     type = models.CharField(max_length=100)
#     directions = models.CharField(max_length=100)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     neighborhood=models.ForeignKey(Neighborhood, related_name ='businesses', on_delete=models.CASCADE)
#     contact = models.CharField(max_length=500)
#     verified = models.BooleanField(default=False)    
 
    
    
#     def __str__(self):
#         return self.name
    
    
#     def delete(self):
#         self.delete()

#     def edit_name(self,name):
#         self.name = name
    
#     @classmethod
#     def business_type(self,key_word):
#         businesses = Business.objects.filter(type=key_word)
#         return businesses
    
#     @classmethod
#     def search_business(self,key_word):
#         businesses = Business.objects.filter(name__icontains=key_word)
#         return businesses
    
# class Service(models.Model):
#     name = models.CharField(max_length=200)
#     type = models.CharField(max_length=200)
#     description = models.TextField()
#     location = models.CharField(max_length=500,default=None)
#     Neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    
#     def __str__(self):
#         return self.name
        
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     about = models.TextField(max_length=500,blank=True)
#     profile_pic = CloudinaryField('image')
    
    
#     def __str__(self):  
#         return str(self.user)
    
#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()
        
        
# class Review(models.Model):
#     content = models.TextField(max_length=200)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     business = models.ForeignKey(Business, on_delete=models.CASCADE)
    
    
#     def __str__(self):
#         return 'Review by {}'.format(self.author)
