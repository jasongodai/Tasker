from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm

# Create your views here.
@login_required
def list_projects(request):
    projects_list = Project.objects.filter(owner=request.user)
    context = {"projects_list": projects_list}
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    task_details = get_object_or_404(Project, id=id)
    context = {
        "task_detail": task_details,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST or None)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)
