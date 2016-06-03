from django.shortcuts import render, resolve_url
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Event
from .models import Tag
from comments.models import Comment
from .forms import *
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django import forms
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin


class EventList(ListView):
    template_name = "events/event_list.html"
    model = Event
    def dispatch(self, request, *args, **kwargs):
        self.form = EventListForm(request.GET)
        self.form.is_valid()
        self.qform = QuesForm(request.POST or None)
        return super(EventList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        #eventSet = Event.objects.all()
        #eventSet = eventSet.annotate(comments_count=Count('comments__id'))
        eventSet = super(EventList, self).get_queryset()
        eventSet = eventSet.for_user(self.request.user)
        if self.form.cleaned_data.get('search'):
            eventSet = eventSet.filter(title__contains=self.form.cleaned_data.get('search'))
        if self.form.cleaned_data.get('sort_field'):
            eventSet = eventSet.order_by(self.form.cleaned_data.get('sort_field'))
        return eventSet[:10]

    def get_context_data(self, **kwargs):
        context = super(EventList, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['createForm'] = self.qform
        return context

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    template_name = 'events/create.html'
    fields = ('title', 'text', 'blog','tags')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(EventCreate, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('events:event_detail', pk=self.object.pk)

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = 'events/update.html'
    fields = ('title', 'text', 'blog', 'tags')
    def get_success_url(self):
        return reverse_lazy('events:event_detail',kwargs={'pk': self.get_object().id})

class EventDetail(CreateView):
    model = Comment
    template_name = 'events/event.html'
    fields = ('text', )


    def dispatch(self, request, pk=None, *args, **kwargs):
        self.event = get_object_or_404(Event, id=pk)
        return super(EventDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['event'] = self.event
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.event = self.event
        return super(EventDetail, self).form_valid(form)

    def get_success_url(self):
        return resolve_url("events:event_detail", pk=self.event.id)

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        events = Event.objects.filter(text__icontains=q)
        return render_to_response('events/search_results.html',
            {'events': events, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')

class EventView(DetailView):
    model = Event
    template_name = 'events/event.html'

def get_name(request):
    if request.method == 'POST':
        form = MyCoolForm(request.POST)
        if form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = MyCoolForm()
    return render(request, template_name, {'form': form})

class TagDetail(DetailView):

    model = Tag
    template_name = 'events/tag_detail.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super(TagDetail, self).get_context_data(**kwargs)
        context['tags'] = self.object.tags.for_user(self.request.user)
        return context
