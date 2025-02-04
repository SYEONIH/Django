from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def index(request):
    product_list = Product.objects.order_by('-pub_date')
    context = {'product_list': product_list}
    return render(request, 'pages/category1.html', context)

def detail(request, product_id):
    product_list = get_object_or_404(Product, pk=product_id)
    context = {'product_list': product_list}
    return render(request, 'product/product_detail.html', context)

@login_required(login_url='accounts:login')
def comment_create(request, product_id):
    product_list = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product_list  
            comment.author = request.user
            comment.save()
        return redirect('detail', product_id=product_list.id)
    else:
        form = CommentForm()

    context = {'product_list': product_list, 'form': form}
    return render(request, 'product/product_detail.html', context)

@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied 

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()  
            return redirect('detail', product_id=comment.product.id)  # 필드명 수정
    else:
        form = CommentForm(instance=comment)

    context = {'comment': comment, 'form': form}
    return render(request, 'product/comment_form.html', context)

@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    else:
        product_id = comment.product.id  
        comment.delete()
        return redirect('detail', product_id=product_id)  
