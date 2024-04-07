from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

def index(request):
    #another_page_url_bugs = reverse('quality_control:bugs')
    bugs_list_url = reverse('quality_control:bugs_list')
    features_list_url = reverse('quality_control:features_list')
    #html = f"<h1>Страница приложения quality_control</h1><a href='{another_page_url_bugs}'>Список всех багов</a>   <->   \
        #<a href='{another_page_url_reqs}'>Запросы на улучшение</a>"
    html = f"<h1>Страница приложения quality_control</h1><a href='{bugs_list_url}'>Список всех багов</a>   <->   \
        <a href='{features_list_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

#сейчас это отображение уже не нужно, т.к. есть bugs_list
def bug_list(request):
    return HttpResponse("Список отчетов об ошибках")

#сейчас это отображение уже не нужно, т.к. есть features_list
def features(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, bug_id):
    html = f"<h1>Детали бага {bug_id}</h1>"
    return HttpResponse(html)

def feature_id_detail(request, feature_id):
    html = f"<h1>Детали улучшения {feature_id}</h1>"
    return HttpResponse(html)

def bugs_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in bugs:
        #bugs_html += f"<li>{bug.title}, STATUS: {bug.status}</li>"
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}, STATUS: {bug.status}</a></li>'
    bugs_html += "</ul>"
    return HttpResponse(bugs_html)

def features_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        #bugs_html += f"<li>{bug.title}, STATUS: {bug.status}</li>"
        features_html += f'<li><a href="{feature.id}/">{feature.title}, STATUS: {feature.status}</a></li>'
    features_html += "</ul>"
    return HttpResponse(features_html)

'''def bug_detail_from_all_bugs(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'    заменили через DetailView
    return HttpResponse(response_html)'''

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = f'<h1>{bug.title}</h1><p>Description: {bug.description}</p>'
        response_html += f'<p>Status: {bug.status}</p>'
        response_html += f'<p>Priority: {bug.priority}</p>'
        response_html += f'<p>In which project: {bug.project}</p>'
        if bug.task:
            response_html += f'<p>In which task in project: {bug.task}</p>'
        return HttpResponse(response_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        response_html = f'<h1>{feature.title}</h1><p>Description: {feature.description}</p>'
        response_html += f'<p>Status: {feature.status}</p>'
        response_html += f'<p>Priority: {feature.priority}</p>'
        response_html += f'<p>In which project: {feature.project}</p>'
        if feature.task:
            response_html += f'<p>In which task in project: {feature.task}</p>'
        return HttpResponse(response_html)