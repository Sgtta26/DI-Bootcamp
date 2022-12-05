from django.shortcuts import render
from datetime import date
from .models import Post, Author
from .forms import CommentForm

# Create your views here.
def homepage(request):

    # render
    # - request object
    # - template_name -> html name ('homepage.html')
    # - context -> dictionary of data

    all_posts = Post.objects.all().order_by('-date_created') # All of the posts

    context = {'time': date.today(), 'posts': all_posts}
    return render(request, 'homepage.html', context)


def authors(request):
    
    all_authors = Author.objects.all()
    context = {'authors': all_authors}

    return render(request, 'authors.html', context)


# Gets all posts of a specific author
def author_posts(request, id):

    author = Author.objects.get(id=id)
    author_posts = author.posts.all()
    
    context = {'author': author, 'posts': author_posts}

    return render(request, 'author_posts.html', context)


def post_details(request, id):

    post = Post.objects.get(id=id)

    comments = post.comment_set.all()

    comment_form = CommentForm()
    
    # if request.method == 'POST':

    #     filled_comment_form = CommentForm(request.POST)
    #     filled_comment_form.save()

    #     context = {'post': post, 'form':filled_comment_form}
    #     return render(request, 'post.html',context)

    # # print("GET dict: ", request.GET)
    # # print("POST dict: ", request.POST)

    context = {'post': post, 'form':comment_form, 'comments':comments}
    return render(request, 'post.html',context)
