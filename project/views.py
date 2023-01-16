from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Review
from .forms import CommentForm


def home(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'membership.html'
    paginate_by = 6


class ReviewDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        review = get_object_or_404(queryset, slug=slug)
        print(review)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "review.html",
            {
                "review": review,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
