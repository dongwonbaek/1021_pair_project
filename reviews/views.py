from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            form = review_form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form,
    }
    return render(request, 'reviews/create.html', context)

def detail(request, reviews_pk):
    review = Review.objects.get(pk=reviews_pk)
    context = {
        'review': review,
    }
    return render(request, 'reviews/detail.html', context)

def update(request, reviews_pk):
    review = Review.objects.get(pk=reviews_pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:detail', review.pk)
    else:
        review_form=ReviewForm(instance=review)
    context = {
        'review_form': review_form,
    }
    return render(request, 'reviews/update.html', context)

def delete(request, reviews_pk):
    Review.objects.get(pk=reviews_pk).delete()
    return redirect('reviews:index')


