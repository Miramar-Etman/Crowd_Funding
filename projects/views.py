from pyexpat.errors import messages
from django.contrib import messages
from django.db.models import Q
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import CreateView
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Project, Donate, Comment, Rating
from .forms import ProjectForm, DonateForm, CommentForm, RateForm, ReportProjectForm, ReportCommentForm


####################Create Project######################
@login_required
def create_project(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.project_creator = request.user
            new_form.save()
            return redirect("show_projects")
        context = {
            'form': form,
            "categories": categories}
        return render(request, 'projects/create_project.html', context)
    else:

        form = ProjectForm()
        context = {
            'form': form,
            "categories": categories
        }
    return render(request, 'projects/create_project.html', context)

####################Show all user Projects ###############
@login_required
def show_all(request):
    projects = Project.objects.filter(project_creator=request.user)
    context = {"projects": projects}
    return render(request, 'projects/view_all_projects.html', context)

###################Show avaliable projects for donations ##############
@login_required
def avaliable_all(request):
    projects= Project.objects.filter(~Q(project_creator=request.user))
    context = {"projects": projects}
    return render(request, 'projects/avaliable_projects.html', context)

####################3 single project details #######################333
def single_project(request,id):
    project = get_object_or_404(Project, id=id)

      #####   Average rate for project ######
    average_rate = 0
    if Rating.objects.filter(project=project):
        rate_proj=str(Rating.objects.filter(project=project)[0])
        for rate in rate_proj:
            average_rate += int(rate)
        average_rate /= len(rate_proj)

    context = {"project": project,"average_rate":average_rate}
    return render(request, 'projects/view_project.html', context)

##################### Donation for specific project #################
@login_required
def donate(request,id):
    project_donate_now = get_object_or_404(Project, pk=id)
    total_donate = project_donate_now.total_donate
    if request.method == 'POST':
                 ######### validate amount #########
        user_amount = float(request.POST['amount'])
        if user_amount + total_donate > project_donate_now.target :
            form = DonateForm()
            messages.error(request, "Your donation exceeds the target amount")
            context = {
                'form': form,
                "project_donate": project_donate_now}
            return render(request, 'projects/donate.html', context)
        form = DonateForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user_donated = request.user
            new_form.project = project_donate_now
            new_form.save()
            project_donate_now.total_donate+= user_amount
            project_donate_now.save()
            return redirect('avaliable_proj')
        context = {
            'form': form,
            "project_donate": project_donate_now}
        return render(request, 'projects/donate.html', context)
    else:
        form = DonateForm()
        context = {
            'form': form,
            "project_donate": project_donate_now}
    return render(request, 'projects/donate.html', context)

###################Cancel Project #####################
@login_required
def cancel_project(request,id):
    project_donate_now = get_object_or_404(Project, pk=id)
    if project_donate_now.total_donate > project_donate_now.target / 4:
        messages.error(request, "Your Cannot Cancel Project it already exceeds 25%")
        return redirect("show_projects")
    else:
        project_donate_now.delete()
        return redirect("show_projects")

####################Add Comments ##########################

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'projects/add_comment.html'
    def form_valid(self, form):
        form.instance.project_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_absolute_url(self):
        return reverse('add_comment', args=[str(self.id)])

####################### Rating Project ##########################

@login_required
def AddRateView(request, pk):
    project_rate = get_object_or_404(Project, pk=pk)
    if request.method == "POST":
        rate = request.POST.get('scale', '')
        if int(rate) <= 5 and rate.isnumeric():
            validate_rate(pk, request.user, rate)
            form = RateForm()
            context = {
                'form': form}
            return render(request, 'projects/rate_project.html', context)
        else:
            if int(rate) > 5:
                form = RateForm()
                context = {
                    'form': form}
                messages.error(request, "Only Values Between 1 - 5 are acceptable")
                return render(request, 'projects/rate_project.html', context)

    else:
        form = RateForm()
        context = {
            'form': form,
            "project_rate": project_rate}
        return render(request,'projects/rate_project.html',context)


def validate_rate(pk, user, rate):
    past_rate = Rating.objects.filter(project_id=pk, user_id=user.id)
    if past_rate:
        past_rate[0].scale = int(rate)
        past_rate[0].save()

    else:
        Rating.objects.create(
            scale=rate, project_id=pk, user_id=user.id)

#######################Previous User Donations ############################
@login_required
def donations(request):
    donations = Donate.objects.filter(user_donated_id=request.user.id)
    context = {
        "donations": donations}
    return render(request, 'projects/donations.html', context)

#######################  SEARCH ############################
def search_project(request):
    if request.method == "POST":
        projects = Project.objects.filter(title=request.POST['searched'])
        context = {
        "projects": projects}
        return render(request, 'projects/search_result.html', context)
    else:
        return render(request, 'projects/search_result.html')


###################### Reporting Project ##################
@login_required
def report_project(request,pk):
    if request.method == 'POST':
        form = ReportProjectForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user_report = request.user
            project = Project.objects.get(pk=pk)
            new_form.project = project
            new_form.save()
            return redirect("avaliable_proj")
        context = {
            'form': form}
        return render(request, 'projects/report_project.html', context)
    else:

        form = ReportProjectForm()
        context = {
            'form': form,
        }
    return render(request, 'projects/report_project.html', context)

###################### Reporting Commets ##################
@login_required
def report_comment(request,pk):
    if request.method == 'POST':
        form = ReportCommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user_report = request.user
            comment = Comment.objects.get(pk=pk)
            new_form.comment = comment
            new_form.save()
            return redirect("avaliable_proj")
        context = {
            'form': form}
        return render(request, 'projects/report_comment.html', context)

    else:

        form = ReportProjectForm()
        context = {
            'form': form,
        }
    return render(request, 'projects/report_comment.html', context)