from django.shortcuts import render
from django.views import generic
from .models import Review


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.object.filter(status=1).order_by('-created_on')
    template_name = 'membership.html'