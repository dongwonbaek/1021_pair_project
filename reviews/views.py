from django.shortcuts import render, redirect
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            form = review_form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, '작성되었습니다.')
            return redirect('reviews:detail', form.pk)
    else:
        review_form = ReviewForm()
    context = {
        'review_form': review_form,
    }
    return render(request, 'reviews/create.html', context)

@login_required
def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review,
        'comment_form':CommentForm(),
        'comments': review.comment_set.all()
    }
    return render(request, 'reviews/detail.html', context)

@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review_user = review_form.save(commit=False)
                review_user.user = request.user
                review_user.save()
                messages.success(request, '수정되었습니다.')
                return redirect('reviews:detail', review.pk)
        else:
            review_form=ReviewForm(instance=review)
        context = {
            'review_form': review_form,
        }
        return render(request, 'reviews/update.html', context)
    else:
        messages.warning(request, '작성자만 수정 가능합니다.')
        return redirect('reviews:detail', pk)

@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST' and review.user == request.user:
        review.delete()
        return redirect('reviews:index')
    else:
        messages.warning(request, '작성자만 삭제 가능합니다.')
        return redirect('reviews:detail', pk)

@login_required
def create_comment(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
            return redirect('reviews:detail', review.pk)

@login_required
def delete_comment(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'POST' and comment.user == request.user:
        comment.delete()
    else:
        messages.warning(request, '작성자만 삭제 가능합니다.')
    return redirect('reviews:detail', review_pk)
