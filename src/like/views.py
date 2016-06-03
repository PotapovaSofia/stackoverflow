from django.shortcuts import render
from django.views.generic import View
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from .models import Like
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

# Create your views here.
class LikeView(View):

	

    def dispatch(self, request, content_type_id=None, pk=None, *args, **kwargs):
        content_type = get_object_or_404(ContentType, id=content_type_id)
        model_class = content_type.model_class()
        self.object = get_object_or_404(model_class, id=pk)
        #self.object.inc()

        #TODO one user don't could to like

        if not Like.objects.filter(user=self.request.user, item_type=content_type, item_id=pk).exists():
        	like = Like(user=self.request.user, item = self.object)
        	like.save()
        else:
        	Like.objects.filter(user=self.request.user, item_type=content_type, item_id=pk).delete()
        #self.object.likes.count = 10
        super(LikeView, self).dispatch(request, *args, **kwargs)
        return redirect(self.request.META["HTTP_REFERER"])