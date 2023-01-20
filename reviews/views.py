from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Review
from .forms import CommentForm, ReviewForm


def home(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'reviews/membership.html'
    paginate_by = 6


class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "reviews/review.html",
            {
                "review": review,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        comments = review.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "reviews/review.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


def add_review(request):
    review_form = ReviewForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if review_form.is_valid():
            review_form.instance.slug = slugify(request.POST.get('title'))
            review_form.instance.author = request.user
            review_form.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('home')
        messages.error(request, 'Error, please try again')
    template = 'reviews/add_review.html'
    context = {
        'review_form': review_form,
    }
    return render(request, template, context)


def update_review(request, review_id):
    user = get_object_or_404(User, username=request.user.username)
    review = get_object_or_404(Review, id=review_id)
    if user != review.author:
        messages.error(request, 'Access denied')
        return redirect('home')
    review_form = ReviewForm(request.POST or None, request.FILES or None, instance=review)
    if request.method == 'POST':
        if review_form.is_valid():
            review_form.instance.slug = slugify(request.POST.get('title'))
            review_form.instance.author = request.user
            review_form.save()
            messages.success(request, 'Review updated successfully!')
            return redirect('home')
        messages.error(request, 'Error, please try again')
    template = 'reviews/update_review.html'
    context = {
        'review': review,
        'review_form': review_form,
    }
    return render(request, template, context)


def delete_review(request, review_id):
    user = get_object_or_404(User, username=request.user.username)
    review = get_object_or_404(Review, id=review_id)
    if user != review.author:
        messages.error(request, 'Access denied')
        return redirect('home')
    review.delete()
    messages.success(request, 'Review deleted')
    return redirect('home')
