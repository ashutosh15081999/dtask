from django.shortcuts import render,redirect
from django.http import HttpResponse
#from .models import Book
from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.mail import send_mail
from django.conf import settings
#from .views import *
from django.contrib.auth.models import User
def home(request):
    context = {
        #'books': Book.objects.all(),
    }
    return render(request, 'home/home.html', context)


# def book(request):
# 	listofbooks={
# 		'libooks':Book.objects.all(),
# 	}
# 	return render(request,'bookstore/book.html',listofbooks)

# class PostListView(LoginRequiredMixin,ListView):
# 	model = Book
# 	template_name = 'bookstore/book.html'
# 	context_object_name = 'libooks'
# 	ordering = ['-date']

# 	def form_valid(self,form):
# 		form.instance.owner_name = self.request.user
# 		return super().form_valid(form)


# #<app>/<model>_<viewtype.html>

# class PostDetailView(DetailView):
# 	model = Book
# 	template_name = 'bookstore/select_book.html'
# 	#context_object_name = 'libooks'

# class PostCreateView(LoginRequiredMixin,CreateView):
# 	model = Book
# 	template_name = 'bookstore/book_form.html'
# 	fields = [
# 		'book_name',
# 		'comment',
# 		'contact_no',
# 		'price',
# 		'image',
# 	]

# 	def form_valid(self,form):
# 		form.instance.owner_name = self.request.user
# 		return super().form_valid(form)


# class PostDeleteView(LoginRequiredMixin,DeleteView):
# 	model = Book
# 	template_name = 'bookstore/delete_book.html'
	
	
# 	success_url = '/store/book/email/'
# # def delete(request):
   
# # 	messages.success(request, f'Your account has been deleted!')
# # 	return redirect("/store/books/")

# def email(request):
#     subject = 'Your order has been confirmed ! Please call the owner of book for further steps...'
    
#     current_user = request.user
#     message = str(current_user.username)
#     email_from = 'deepakhack2199@gmail.com'
#     #current_user = request.user
#     recipient_list = [str(current_user.email)]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('/store/books/')

