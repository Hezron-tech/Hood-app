from django.test import TestCase
from .models import HoodMember,Neighborhood,Service,Post,Review,Business
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
# Create your tests here.
class NeighboardTestClass(TestCase):
    def setUp(self):
         self.user1 = User(username='psang',first_name='Enock',last_name ='kipsang',email='psang254@gmail.com',password ='sjsiuwueufbccn')
         self.hood1 = Neighborhood(name='runda',location ='nairobi', creator = self.user1,profile_pic ='picture')
         self.post1 = Post(content = 'good hood',author = self.user1,neighborhood = self.hood1)
         self.member1 = HoodMember(member = self.user1, hood =self.hood1)
         self.business1 =Business(owner = self.user1,name ='shoeshop',type ='wholesale',directions ='opp coop.bank',neighborhood=self.hood1,contact ='kipsang1998@gmail.com')
         
         
    def test_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.hood1,Neighborhood))
        self.assertTrue(isinstance(self.post1,Post))
        self.assertTrue(isinstance(self.member1,HoodMember))
        self.assertTrue(isinstance(self.business1,Business))
        
        
    # Testing Save Method
    def test_create_neighborhood(self):
        self.user1.save()
        self.hood1.save()
        self.post1.save()
        self.member1.save()
        users = User.objects.all()
        hoods  = Neighborhood.objects.all()
        posts = Post.objects.all()
        self.assertTrue(len(posts) > 0)
        self.assertTrue(len(users) > 0)
        self.assertTrue(len(hoods) > 0)
     
      # Testing Delete Method   
    def test_delete_neighborhood(self):
        self.user1.save()
        self.hood1.save()
        hood = get_object_or_404(Neighborhood,creator=self.user1)
        hood.delete_hood()
        hoods = Neighborhood.objects.all()
        self.assertTrue(len(hoods)==0)
        
        
      # Test get all images 
    def test_get_all_hoods(self):
        self.user1.save()
        self.hood2 = Neighborhood(name='CBd',location ='nairobi', creator = self.user1,profile_pic ='picture') 
        self.hood1.save()
        self.hood2.save()
        hoods = Neighborhood.all_hoods()
        self.assertTrue(len(hoods) == 2)
