from django.views.generic import DetailView, ListView
from main.models import Profile
from main.views import ProfileDetailView


class SlugMixin(object):
    slug_field = 'pk'


class ProfileListView(ListView):
    model = Profile

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-modified')


class ProfileSlugDetailView(SlugMixin, ProfileDetailView, DetailView):

    def get_object(self, **kwargs):
        return super(DetailView, self).get_object(**kwargs)
