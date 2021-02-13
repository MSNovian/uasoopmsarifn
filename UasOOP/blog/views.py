from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
	posts = Post.objects.all()

	context = {
		'Title':'Welcome To News',
		'Heading':'MACHINING - ELECTRICAL - COUNSTRUKSI',
		'Posts':posts,
	}

	return render(request,'blog/index.html',context)