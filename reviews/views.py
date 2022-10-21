from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
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

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review,
        'comment_form':CommentForm(),
        'comments': review.comment_set.all()
    }
    return render(request, 'reviews/detail.html', context)

def update(request, pk):
    review = Review.objects.get(pk=pk)
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

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('reviews:index')

def create_comment(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('reviews:detail', review.pk)

def delete_comment(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', review_pk)