from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import DetailView, View, ListView
from .forms import BugReportForm, FeatureRequestForm

def index(request):
    return render(request, 'quality_control/index.html')

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature})

def bugs_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs_list.html', {'bugs_list': bugs})

def features_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features_list.html', {'features_list': features})

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')
    
class BugListView(ListView):
    model = BugReport
    context_object_name = 'bugs_list'
    template_name = 'quality_control/bugs_list.html'

class FeatureListView(ListView):
    model = FeatureRequest
    context_object_name = 'features_list'
    template_name = 'quality_control/features_list.html'

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    template_name = 'quality_control/bug_detail.html'

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    template_name = 'quality_control/feature_detail.html'

def create_bugreport(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bugs_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def create_featurerequest(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:features_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})