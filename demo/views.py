from django.views.generic import DetailView, ListView
from main.models import Profile
from main.views import ProfileDetailView


class SlugMixin(object):
    slug_field = 'pk'


class ProfileListView(ListView):
	"""Plain list view class which overrides get_queryset to return reordered queryset."""

    model = Profile

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-modified')


class ProfileSlugDetailView(SlugMixin, ProfileDetailView, DetailView):
	"""Detail view class which reverts to DetailView.get_object method."""

    def get_object(self, **kwargs):
        return super(DetailView, self).get_object(**kwargs)
