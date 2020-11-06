from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import post


def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'blogapp/home.html', context)

class PostListView(ListView):
    model = post
    template_name = 'blogapp/home.html' #<app>/<model> <viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post
   
class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'caption', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title', 'caption']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# def about(request):
#     return render(request, 'blogapp/about.html', {'title': 'About'})

# @login_required(login_url='/accounts/login/')
# def search_results(request):
#     if 'username' in request.GET and request.GET["username"]:
#         search_term = request.GET.get("username")
#         searched_users = User.objects.filter(username__icontains = search_term)
#         message = f"{search_term}"
#         print(searched_users)
#         profile_pic = User.objects.all()
#         return render(request, 'instaclone/search.html', {'message':message, 'results':searched_users, 'profile_pic':profile_pic})
#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'instaclone/search.html', {'message':message})


#     def comment(request,post_id):
#         current_user=request.user
#         post = post.objects.get(id=post_id)
#         profile_owner = User.objects.get(username=current_user.username)
#         comments = Comment.objects.filter(post=post)
#         for comm  in comments:
#             print(comm.comment)
#             print(comm.author)
#         if request.method == 'POST':
#                 form = CommentForm(request.POST, request.FILES)
#                 if form.is_valid():
#                         comment = form.save(commit=False)
#                         comment.post = post
#                         comment.author = request.user
#                         comment.save()
#                 return redirect('blogapp-home')
#         else:
#                 form = CommentForm()
 
#         return render(request, 'blogapp/comment.html',locals())
   