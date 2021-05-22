from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import CreateForm
from django.urls import reverse_lazy,reverse
from .models import Blog
from django.conf import settings
from django.contrib.auth.models import User
# Create your views here.




class PicCreateview(LoginRequiredMixin,View):
    template_name = 'blogs/form.html'
    success_url = reverse_lazy('pics:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(reverse("blogs:after"))



class Articles_View(LoginRequiredMixin,View):

    def get(self,request,pk):
        objects=Blog.objects.filter(owner=pk)

        ctx ={"objects":objects}
        return render(request,"blogs/done.html",ctx)


class Searched_Articles_View(LoginRequiredMixin,View):

    def get(self,request,pk):
        objects=Blog.objects.filter(owner=pk,public=True)

        ctx ={"objects":objects}
        return render(request,"blogs/done.html",ctx)



def stream_file(request, pk):
    pic = get_object_or_404(Blog, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response


class ArticlesView2(View,LoginRequiredMixin):

    def get(self, request):
        username = request.GET.get("searched")
        objects1 = User.objects.filter(username=username)
        objects=None
        try:
            objects = Blog.objects.filter(owner=objects1[0].id,public=True)
        except:
            objects=None

        ctx = {"objects": objects}
        return render(request, "blogs/done.html", ctx)


class HomeView(View):

    def get(self,request):

        return render(request,"blogs/home.html")



class After_Adding_View(View,LoginRequiredMixin):

    def get(self,request):
        user = request.user.id

        objects = Blog.objects.filter(owner=user)
        return render(request,"blogs/list.html",{"objects":objects})






