from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from .models import Profile, Post, LikePost, FollowersCount, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q
from simple_search import search_filter
# Create your views here.


def index(request):
    return render(request, "index.html")

def register(request):
     if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(email=email).exists():

            messages.error(request, "Email exists")

        elif User.objects.filter(username=username).exists():

            messages.info(request, "Username exists")

        else:

            user = User.objects.create_user(username=username, email=email, password= password)
            user.save()
            messages.info(request, "Registered Successfully")
            return redirect('/login/')

     return render(request, "register.html")

def login(request):
      
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

   
        user = authenticate(request, username=username, password=password)
        if user is not None:

            auth.login(request, user)
            return redirect("/")

    else:
        messages.info(request,  "Invalid Info")
  
    return render(request, "login.html")

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect("/login")
@login_required(login_url='login')
def feed(request):
   
    pron = ""
    post = Post.objects.all()
    prof = Profile.objects.all()
    for p in post:
        sss = User.objects.get(username=p.username)
        pron = Profile.objects.get(username=sss)

    pro = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(username=pro)
    user_post = Post.objects.filter(username=request.user.username)
    lenus = len(user_post)
    user = request.user.username
    fol = request.user.username
    follower = len(FollowersCount.objects.filter(user=user))
    following = (len(FollowersCount.objects.filter(follower=user)))
   
    context = {'post': post,
                'profile':profile,
                'postlen': lenus,
                'prof': prof,
                "follower": follower,
                "following": following
                
     }
    return render(request, "feed.html", context)


@login_required(login_url='/login')
def profile(request, pk):
    pro = User.objects.get(username=pk)
    profile = Profile.objects.get(username=pro)
    user_posts = Post.objects.filter(username=pk)
    user_post_length = len(user_posts)
    shots = Post.objects.all()

    user = pk
    fol = request.user.username

    follower = len(FollowersCount.objects.filter(user=user))
    following = (len(FollowersCount.objects.filter(follower=user)))

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'
    
    context = {'profile' : profile,
    'user_posts' : user_posts,
    'user_post_length' : user_post_length,
    'pro': pro,
    'follower': follower,
    'following': following,
    'btn_text' : button_text

    }

    return render(request, "profile.html", context)

@login_required(login_url='/login')
def profile_edit(request):
    user = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(username=user)

   
    if request.method == "POST":
        bio = request.POST.get('bio')
        avatar = request.FILES.get('avatar')
        cover = request.FILES.get('cover')

        user_profile.cover = cover
        user_profile.save()
        user_profile.avatar = avatar
        user_profile.save()
        user_profile.bio = bio
        user_profile.save()
        
 
           
    profile = Profile.objects.get(username=user)
    context = {'profile' : profile}
    return render(request, "profile_edit.html", context)
@login_required(login_url='/login')
def post(request):
    post = ""


    if request.method == "POST":
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
      
        user = request.user.username

        post = Post.objects.create(username=user, caption=caption, image=image)
        post.save()
        messages.success(request, "Successfully, Uploaded your Post!")
            


       
          
    context = {'post' : post}
    
   
    return render(request, "post.html", context)

@login_required(login_url='login')
def like_post(request, id):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')
@login_required(login_url='login')
def shots(request, id):
   
    post_id = request.GET.get('post_id')
    
    profile = Profile.objects.all()
    shots = Post.objects.all()

    
    pro = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(username=pro)
    user_posts = Post.objects.filter(username=request.user.username)
    lenus = len(user_posts)

   
    p = get_object_or_404(Post, pk=id)
    context = {'profile' : profile, 'p':p,'profile' : profile,
    'user_posts' : user_posts,
    
   }
   
    return render(request, "shots.html", context)

@login_required(login_url='/login')
def profile_list(request):
    profiles = User.objects.all()
    return render(request, "profile_list.html", {"profiles": profiles})

@login_required(login_url='/login')
def settings(request):
    


        
    return render(request, 'setting.html')

@login_required(login_url='/login')
def like_post(request):
    username = request.user.username
    post_id = request.POST.get('post_id')
    print(post_id)
    post = Post.objects.get(id=post_id)

    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')


def comment(request):
    render(request, "sidebar.html")


@login_required(login_url='login')
def follow(request):
    if request.method == 'POST':
        follower = request.POST.get('follow')
        user = request.POST.get('user')

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
            
    else:
        return redirect('/')

@login_required(login_url='login')
def search(request):
    username = ""
    if request.method=='GET':
        
        username = request.GET.get('search')

   
    posts = Post.objects.filter(caption__icontains=username)
    profil = User.objects.filter(username__icontains=username)

    context = {
    'user_posts' : posts,
    
  }
    
    
    return render(request, 'search.html', context)

def about(request):
    return render(request, "about.html")