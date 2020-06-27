from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Post, Category, Contact, BlogComment
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .forms import Contact

# Create your views here.

def home(request):
    
    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]
    cat = Category.objects.all()[0:3]
    context = {'RecentPost': Recent,
               'Categories': cat, }
    return render(request, 'home.html', context)

def blog(request):

    Posts = Post.objects.all().order_by('-postTimeDate')
    paginator = Paginator(Posts, 4)
    page = request.GET.get('page')

    #?page = 2

    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]

    Posts = paginator.get_page(page)
    cat = Category.objects.all()[0:3]

    context = {'Posts': Posts,
               'RecentPost': Recent,
               'Categories': cat,}
    return render(request, 'blog.html', context)


def readMore(request, slug):
    # return HttpResponse(f'this is blogPost : {slug}')

    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]
    post = Post.objects.filter(postId=slug).first()
    cat = Category.objects.all()[0:3]
    comment = BlogComment.objects.filter(post=post) 
    context = {'post': post,
               'RecentPost': Recent,
               'Categories': cat,
                'comments': comment,}
   
    return render(request, 'readMore.html', context)


def search(request):

    

    Recent = Post.objects.all().order_by('-postTimeDate')[0:4]
    query = request.GET['search']
    allPosts = Post.objects.filter(Q(postTitle__icontains=query) | Q(postText__contains=query))
    cat = Category.objects.all()[0:3]

   
    parms = {'allPosts': allPosts,
             'RecentPost': Recent,
             'Categories': cat,}
    return render(request, 'search.html', parms)


def aboutMe(request):
    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]
    cat = Category.objects.all()[0:3]
    context = {'RecentPost': Recent,
               'Categories': cat, }
    return render(request, 'aboutMe.html', context)




def categories(request, cat):
    # return HttpResponse(f'this is blogPost : {slug}')

    Recent = Post.objects.all().order_by('-postTimeDate')[0:3]
    allPosts = Post.objects.filter(Q(category__icontains=cat) | Q(postText__contains=cat))
    parms = {'allPosts': allPosts,
             'Categories': Category.objects.all(),
             'RecentPost': Recent}
    return render(request, 'home/category.html', parms)



def contactUs(request):
    context = {}
    if request.POST:
        form = Contact(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "your comment added successfully")
            context = {'form': form, 'RecentPost': Post.objects.all()[0:3],
                       'Categories': Category.objects.all()[0:4]}
            return render(request, 'contact.html', context)
        else:
            messages.error(request, "Please fill the form correctly")
            context = {'form': form, 'RecentPost': Post.objects.all()[0:3],
                       'Categories': Category.objects.all()[0:4]}
            return render(request, 'contact.html', context)
    else:  # GET request
        form = Contact()
        context = {'form': form, 'RecentPost': Post.objects.all()[0:3],
            'Categories': Category.objects.all()[0:4]}
    return render(request, 'contact.html', context)


def postComment(request):
    if request.method=='POST':
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(postId=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
           comment = BlogComment(comment=comment, user=user, post=post)
        else :
            parent = BlogComment.objects.get(sno=parentSno)
            comment =  BlogComment(comment=comment, user=user, post=post, parent=parent)
            messages.success(request, "your reply added successfully") 
        comment.save()
        messages.success(request, "your comment added successfully")
    else:
         messages.error(request, "your comment was not added successfully")
        

    return redirect("home")