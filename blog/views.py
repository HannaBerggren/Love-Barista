from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm, UpdatePostForm
from .forms import CommentForm
from .models import Comment
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class DeletePost(generic.DeleteView):
    """
    Class to allow to delete a post
    """
    model = Post
    template_name = "delete_post.html"
    success_message = "Post was deleted successfully."

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        """
        Set the reverse url for the successful delete
        of the post to the database
        """
        return reverse("user-post-list")


@login_required()
def update_post(request, slug):
    """
    Users can update their blog post that they have created
    """
    post = get_object_or_404(Post, slug=slug)
    if request.user.id == post.author.id:
        if request.method == "POST":
            form = UpdatePostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.slug = slugify(post.title)
                post.status = 1
                form.save()
                messages.success(request, "Your post updated successfully!")
                return redirect(reverse("user-post-list"))
            else:
                messages.error(request, "Failed to update the post.")
        else:
            form = UpdatePostForm(instance=post)
    else:
        messages.error(request, "Sorry, This is not your post.")

    template = ("update_post.html",)
    context = {"form": form, "post": post}
    return render(request, template, context)


class AddPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Add a blog post only when user is logged in
    """
    model = Post
    form_class = AddPostForm
    template_name = "add_post.html"
    success_message = "You have added a new post, It's awaiting approval!"

    def get_success_url(self):
        """
        Set the reverse url for the successful addition
        of the post to the database
        """
        return reverse("user-page")

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.slug = slugify(post.title)
        form.save()
        return super().form_valid(form)


class User(LoginRequiredMixin, generic.ListView):
    """
    Render the user page
    """
    model = Post
    template_name = "user_page.html"


class UserPostList(LoginRequiredMixin, generic.ListView):
    """
    Display all posts of a particular logged in user in one place
    """
    model = Post
    author = Post.author
    template_name = "user_post_list.html"

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(
            author=self.request.user, status=1).order_by(
            "-created_on"
        )
