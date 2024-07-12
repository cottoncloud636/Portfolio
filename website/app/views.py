from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Contact, Like
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')
 
projs=[
    {'id':1, 'name':'Kickball League', 'brief':'A basic full-stack web app in Java Spring', 'image':'/static/assets/media/spring-boot.jpg'},
    {'id':2, 'name':'Airbite (group project)', 'brief':'socket application, client-server architecture','image':'/static/assets/media/airbite.png'},
    {'id':3, 'name':'Language Modeling', 'brief':'A basic language model training', 'image':'/static/assets/media/NLP.jpg'},
    {'id':4, 'name':'GameDev (group project)', 'brief':'A comprehensive full-stack web app developed with aesthetically pleasing CSS', 'image':'/static/assets/media/gamedev.png'},
    {'id':5, 'name':'Portfolio Site', 'brief':'A personal portfolio website in Django', 'image':'/static/assets/media/personalsite.png'},
    {'id':6, 'name':'Art Marche', 'brief':'A full-stack MERN web app', 'image':'/static/assets/media/ArtMarche.png'},
]

def projects(request):
    # context = [
    #     {'url':'project/1', 'label':'GUI in Java', 'image_url':'/static/assets/media/candles.jpg'},
    #     {'url':'project/2', 'label':'Socket Programming', 'image_url':'/static/assets/media/airbite.png'},
    #     {'url':'project/3', 'label':'full-stack Java Website_1', 'image_url':'/static/assets/media/airbite.png'}
    # ]
    return render(request, 'projects.html', {'projects': projs}) #"projectlist" is the name of how
                                            #we want to address it in template, "projects": to specify 
                                            #what we are passing in
    
def project(request, pk):
    projects = Project.objects.get(id=pk)
    context = {'project': projects}
    return render(request, "project.html", context) 

def like_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    like, created= Like.objects.get_or_create(project=project)
    like.count += 1
    like.save()
    return JsonResponse({'likes': like.count})


def contact(request):
    if request.method == "POST": #first, get the user input from the form, then sends the query to admin interface
        fname = request.POST.get('viewername')     #by using query = Contact xxx, with the help of matching field
        femail = request.POST.get('emailaddr')     #then save the user input by using query.save() to admin interface
        fphonenumber = request.POST.get('phone')
        fmessage = request.POST.get('message')
        query = Contact(name=fname, email=femail, phonenumber=fphonenumber, msg=fmessage)
        query.save()
        messages.success(request, "Thank you for contacting me, I will get back to you soon!")
        # if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        #     return JsonResponse({"success": True})
        # else:
        
        return redirect('/contact')
    return render(request, 'contact.html') 