from django.shortcuts import get_object_or_404, render, redirect
from .forms import DetailForm,CommentForm
from .models import Detail,Comment
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.conf.urls.static import static
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

def index(request):
        return render(request, 'index.html')

def layout(request):
        return render(request, 'layout.html')

# comment생성
def detail(request, pk):
        detail = get_object_or_404(Detail , id=pk)
        if request.method == "POST":
                form = CommentForm(request.POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.post = detail
                        comment.comment_text = form.cleaned_data["comment_text"]
                        comment.save()
                        return redirect("detail", pk)
        else:
                form = CommentForm()
                return render(request, "detail2.html", {"detail":detail, "form":form})

# 페이지를 생성하기 위한 함수입니다.
def new(request):
        return render(request,'new.html')
                  
def create(request, detail=None):
        if request.method =='POST':
                form = DetailForm(request.POST,instance=detail)
                if form.is_valid():
                        detail = form.save(commit=False)
                        detail.pub_date=timezone.now()
                        detail.save()
                        return redirect('home2')
        else:
                form = DetailForm(instance=detail)
                return render(request, 'new.html', {'form':form})       

def update(request, board_id):
        detail = Detail()
        detail.title = request.GET['title']
        detail.content = request.GET['content']
        detail.pub_date = timezone.datetime.now()
        detail.save()
        return redirect('/detail/')

def home2(request):
        details = Detail.objects
        return render(request, 'home2.html',{'details' :details})

def edit(request,pk):
    detail=get_object_or_404(Detail,pk=pk)
    return create(request,detail)

def remove(request,pk):
    detail=get_object_or_404(Detail,pk=pk)
    detail.delete()
    return redirect('home2')
        
def comment_edit(request,detail_id, pk):
        comment = get_object_or_404(Comment, pk=pk)
        if request.method=='POST':
                form=CommentForm(request.POST,instance=comment)
                if form.is_valid():
                        comment=form.save()
                        return redirect('detail', detail_id)
        else:
                form=CommentForm(instance=comment)
                return render(request,'detail2.html',{'form':form})

def comment_remove(request,detail_id,pk):
        comment=get_object_or_404(Comment, pk=pk)
        comment.delete()
        return redirect('detail', detail_id)

