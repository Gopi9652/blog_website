from django.shortcuts import render,redirect
from first.forms import signup_form,Post_form
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from first.models import post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.shortcuts import get_object_or_404

# Create your views here.
def signup_view(request):
    obj=signup_form()
    if request.method=='POST':
        obj=signup_form(request.POST)
        if obj.is_valid():
            obj.save()
            return redirect('login')
        else:
            msg="enter correct details"
            return render(request,'signup.html',{"obj":obj,"msg":msg})
    return render(request,'signup.html',{"obj":obj})
def login_view(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        request.session['username'] = username
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('post_list')
        else:
            msg="enter correct details"
            return render(request,'login.html',{"msg":msg})
    return render(request,'login.html')

@login_required
def home_view(request):
    return render(request, 'first/post_list.html')


@login_required(login_url='login')
def post_view(request):
    if request.method == 'POST':
        form = Post_form(request.POST, request.FILES)
        username=request.session.get('username')
        if form.is_valid():
            user = User.objects.get(username=username)
            form.instance.author = user

            form.save()
            form = Post_form()
            return render(request, 'first/post.html', {'form': form})
    else:
        form = Post_form()
    username = request.session.get('username')
    return render(request, 'first/post.html', {'form': form,"username":username})


@login_required(login_url='login')
def post_list_view(request):
    post_list=post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'first/post_list.html',{"post_list":post_list})


@login_required(login_url='login')
def post_detail_view(request,year,month,day,title,username):
    post1 = get_object_or_404(post,
                              publish__year=year,
                              publish__month=month,
                              publish__day=day,
                              title=title,
                              author__username=username)
    return render(request,'first/post_detail.html',{"post1":post1})

@login_required(login_url='login')
def latest_posts_view(request):
    posts = post.objects.all()[:10]
    return render(request,'first/latest_post.html',{"posts":posts})


@login_required(login_url='login')
def profile_view(request):
    posts = post.objects.filter(author__username=request.user.username)
    paginator = Paginator(posts,2)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'first/profile.html',{"posts":posts})
def logout_view(request):
    logout(request)
    return redirect('login')


