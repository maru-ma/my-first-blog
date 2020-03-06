from django.shortcuts import render

# Create your views here.
def post_list(request):
    # 'render' : reproduce, construye el template.
    return render(request, 'blog/post_list.html', {})
