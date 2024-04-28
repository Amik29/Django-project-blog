from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


posts = [
    {
        'author': 'Admin',
        'title': 'First Life!',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi hendrerit velit et nisi vulputate, non fringilla ante aliquet. Aenean sodales ultricies gravida. Donec tellus tellus, volutpat quis dignissim sit amet, lacinia placerat odio. Ut tempus, sapien in egestas dictum, dui est feugiat augue, ac pulvinar magna elit id justo. Duis non finibus ipsum. Nulla ac urna ut dolor pellentesque commodo a sed massa. Morbi non suscipit massa. Quisque ut finibus tortor. Donec sit amet maximus purus, a aliquet lectus. Ut imperdiet mi ut vulputate bibendum. Cras elementum est libero, a vestibulum neque tincidunt non. Donec blandit eget neque quis hendrerit. Nulla commodo lectus purus, ac pulvinar nulla tempor eu. Sed volutpat aliquet diam, a consequat nulla volutpat in. Nunc viverra ut ante at rhoncus.',
        'date_posted': '26 апреля, 2024'
    },
    {
        'author': 'User_1',
        'title': 'Second Life!',
        'content': 'n fringilla ante aliquet. Aenean sodales ultricies gravida. Donec tellus tellus, volutpat quis dignissim sit amet, lacinia placerat odio. Ut tempus, sapien in egestas dictum, dui est feugiat augue, ac pulvinar magna elit id justo. Duis non finibus ipsum. Nulla ac urna ut dolor pellentesque commodo a sed massa. Morbi non suscipit massa. Quisque ut finibus tortor. Donec sit amet maximus purus, a aliquet lectus. Ut imperdiet mi ut vulputate bibendum. Cras elementum est libero, a vestibulum neque tincidunt non. Donec blandit eget neque quis hendrerit. Nulla commodo lectus purus, ac pulvinar nulla tempor eu. Sed volutpat aliquet diam, a consequat nulla volutpat in. Nunc viverra ut ante at rhoncus.',
        'date_posted': '26 апреля, 2024'
    }
]



def home(request):
    context = {
        'posts': posts
    }
    return render(request,'main/home.html',context)


def profile(request):
    return HttpResponse("User_info")


def about(request):
    return render(request,'main/about.html')