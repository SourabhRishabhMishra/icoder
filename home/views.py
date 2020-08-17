from django.shortcuts import render , HttpResponse, redirect
from .models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Views for html pages.

def home(request):
    return render(request,'home/home.html')


def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name,email,phone,content)


        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'please fill the form correctly')
        else:
            contact= Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request, 'Your message has been successfully sent')

    return render(request,'home/contact.html')


def about(request):
    return render(request,'home/about.html')


def search(request):
    search = request.GET['search']
    if len(search)>78:
        allPosts = Posts.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=search)    
        allPostsContent = Post.objects.filter(content__icontains=search)
        allPosts = allPostsTitle.union(allPostsContent)

    if allPosts.count() ==0:
        messages.warning(request, 'No search result found refine your query')
    context = {'allPosts':allPosts,'search':search}
    return render(request,'home/search.html',context)


#Authentication APIS

def handleSignup(request):
    if request.method == "POST":
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        print(username)


        #check for errorneous input 
        if len(username) > 15:
            messages.error(request,"Please enter username less then 15 character")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"username must be alpha numeric")
            return redirect('home')


        if pass1 != pass2:
            messages.error(request,"password do not match")
            return redirect('home')


        #Create a users
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = firstname
        myuser.last_name  = lastname
        myuser.save()
        messages.success(request,"your icoder account has been successfully created")
        return redirect('home')
        
    else:
        return HttpResponse('404 not found')    


def handleLogin(request):
    if request.method == "POST":
        loginusername=request.POST['loginusername']
        loginpass=request.POST['loginpass']

        user = authenticate(request, username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request,"Sucessfully logIn")
            return redirect('home')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('home')



    return HttpResponse('404 not found')


def handleLogout(request):
    logout(request)
    messages.success(request,"Sucessfully logged Out")
    return redirect('home')
    


    return HttpResponse('404 not found')