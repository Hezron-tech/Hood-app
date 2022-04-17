from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout
from django.contrib.auth.models import User
from .forms import RegisterUserForm,newHoodForm, PostForm, BusinessForm,ServiceForm,ProfileForm

from .models import Neighborhood, Post, Profile, HoodMember,Business,Service



# Landing page
def index(request):
    return render(request,'index.html')


# Dashboard to show neighborhoods
def dashboard(request):
    
    hoods = Neighborhood.objects.all()
    context = {
        'hoods':hoods
    }
    
    return render(request,'dashboard.html',context)


# # search neighborhood by location   
# def search_hood(request):
#     if 'search' in request.GET and request.GET["search"]:
#         search_term = request.GET.get("search")
#         print(search_term)
#         hoods = Neighborhood.search_hood(search_term)
#         message = f"{search_term}"

#         return render(request, 'search.html',{'hoods':hoods})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})

# # Home posts and details
# @login_required(login_url='/accounts/login/')
# def home(request):
#     current_user = request.user
#     if request.method == "POST":
#         hood_group = HoodMember.objects.filter(member=current_user).first()
#         hood = hood_group.hood
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = current_user
#             post.neighborhood = hood
#             post.save()
#             messages.success(request,('Posted!'))
#             return redirect('home')
#     else:
#         hood_group = HoodMember.objects.filter(member=current_user).first()
#         if hood_group is not None:
#             hood = hood_group.hood
#             posts =Post.objects.filter(neighborhood =hood)
#             form = PostForm()
#             context = {
#                 'hood':hood,
#                 'posts':posts,
#                 'form':form,
#             }
#             return render(request,'home.html', context)
#         else:
#             return redirect('dashboard')
    
    

# # Creating new Neighborhood
# @login_required(login_url='/accounts/login/')
# def new_hood(request):
#     if request.method == 'POST':
#         current_user = request.user
#         form = newHoodForm(request.POST, request.FILES)
#         if form.is_valid():
#             hood = form.save(commit=False)
#             hood.creator = current_user
#             hood.save()
#             new_member = HoodMember(member=current_user,hood=hood)
#             new_member.save()
#             messages.success(request,('Neighborhood created!'))
#             return redirect('dashboard')
#     else:
#         form = newHoodForm()
#     return render(request,'new-hood.html', {'form':form})


# # Join a neighborhood
# @login_required(login_url='/accounts/login/')
# def join_hood(request,hood_id):
#     hood = get_object_or_404(Neighborhood,id=hood_id)
#     member = HoodMember.objects.filter(Neighborhood =hood,member =request.user)
#     if member is not None:
#         new_member = HoodMember(member = request.user, hood= hood)
#         new_member.save()
#         messages.success(request,("You've joined the group"))
#     else:
#         messages.success(request,("You're already a member"))
#     return redirect('home')


# # Leave neighborhood
# @login_required(login_url='/accounts/login/')
# def leave_hood(request,hood_id):
#     current_user = request.user
#     hood = get_object_or_404(Neighborhood,id=hood_id)
#     membership = HoodMember(member = current_user, hood= hood)
#     membership.delete()
#     return redirect('dashboard')
    
    
    
# # Creating newpost
# @login_required(login_url='/accounts/login/')
# def create_post(request):
#     if request.method == "POST":
#         current_user = request.user
#         hood_group = HoodMember.objects.filter(member=current_user).first()
#         hood = hood_group.hood
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = current_user
#             post.neighborhood = hood
#             post.save()
#             messages.success(request,('Posted!'))
#             message='posted successfully'
#             return redirect('home')
    
#         else:
#             return JsonResponse({'error': True, 'errors': form.errors},status=400)
   

# # Post and details
# def post(request,post_id):
#     post = get_object_or_404(Post,id=post_id)
#     return render(request,'post.html')

# # businesses
# def business(request):
#     current_user = request.user
#     hood_group = HoodMember.objects.filter(member=current_user).first()
#     hood = hood_group.hood
#     businesses = Business.objects.filter(neighborhood =hood)
#     if request.method == 'POST':
#         form = BusinessForm(request.POST)
#         if form.is_valid():
#             business = form.save(commit=False)
#             business.owner = current_user
#             business.neighborhood = hood
#             business.save()
#             new_member = HoodMember(member=current_user,hood=hood)
#             new_member.save()
#             messages.success(request,('Business Added!'))
#             return redirect('business')
#     else:
#         form = BusinessForm()
#     return render(request, 'business.html',{'form':form,'businesses':businesses })

# # Search business
# def search_business(request):
#     if 'search' in request.GET and request.GET["search"]:
#         search_term = request.GET.get("search")
#         print(search_term)
#         businesses = Business.search_business(search_term)
#         message = f"{search_term}"
        

#         return render(request, 'search_business.html',{'businesses':businesses,'message':message})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'search.html',{"message":message})
# #hospital
# def hospital(request):
#     current_user = request.user
#     hood_group = HoodMember.objects.filter(member=current_user).first()
#     hood = hood_group.hood
#     creator = hood.creator
#     hospitals = Service.objects.filter(type ='hospital',Neighborhood=hood)
#     if request.method == 'POST':
#         form = ServiceForm(request.POST)
#         if form.is_valid():
#             service = form.save(commit=False)
#             service.type = 'hospital'
#             service.Neighborhood = hood
#             service.save()
#             new_member = HoodMember(member=current_user,hood=hood)
#             new_member.save()
#             messages.success(request,('Hospital added!'))
#             return redirect('hospitals')
#     else:
#         form = ServiceForm()
#     return render(request, 'hospitals.html',{'form':form,'hospitals':hospitals, 'creator':creator })

# #school
# def school(request):
#     current_user = request.user
#     hood_group = HoodMember.objects.filter(member=current_user).first()
#     hood = hood_group.hood
#     creator = hood.creator
#     schools = Service.objects.filter(type ='school',Neighborhood=hood)
#     if request.method == 'POST':
#         form = ServiceForm(request.POST)
#         if form.is_valid():
#             service = form.save(commit=False)
#             service.type = 'school'
#             service.Neighborhood = hood
#             service.save()
#             new_member = HoodMember(member=current_user,hood=hood)
#             new_member.save()
#             messages.success(request,('School added!'))
#             return redirect('schools')
#     else:
#         form = ServiceForm()
#     return render(request, 'schools.html',{'form':form, 'schools':schools, 'creator':creator})



# # Register user
# def register_user(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             form.save()

#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             email = form.cleaned_data['email']
#             user = authenticate(username = username,password=password)
#             login(request,user)
#             messages.success(request,('Registration successfull and logged in'))
#             return redirect('dashboard')
           
#     else:
#         form = RegisterUserForm()
        
#     return render(request,'registration/registration_form.html', {'form':form})



# # Page for profile
# def user_profile(request,username):
#     user = User.objects.filter(username=username).first()
#     if user == request.user:
#         return redirect('my_profile')
#     profile = Profile.objects.filter(user=user).first()
#     posts = Post.objects.filter(author=user)
#     return render(request, 'profiles/userprofile.html', {'profile':profile,'posts':posts})


# #logged in user profile
# @login_required(login_url='/accounts/login/')
# def my_profile(request):
#     user = request.user
#     profile = get_object_or_404(Profile,user=user)
#     if request ==' POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             profileform = form.save(commit=False)
#             profileform.user = user
#             profileform.save()
#             messages.success(request,('Update saved'))
#         return redirect('my_profile')
#     else:
#         posts = Post.objects.filter(author=user) 
#         form = ProfileForm() 
#         return render(request, 'profiles/profile.html', {'user': user,'posts':posts,'form':form})
