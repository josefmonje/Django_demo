from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from .forms import ProfileForm
from .models import Profile


class SuccessURLMixin(object):
    success_url = reverse_lazy('home')


class FormMixin(object):
    form_class = ProfileForm

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()  # because immutable
        post_data['user'] = request.user.id
        request.POST = post_data
        return super().post(request, *args, **kwargs)


class ProfileMixin(object):
    model = Profile

    def has_profile(self):
        try:
            self.request.user.profile
        except Exception:
            return False
        else:
            return True

    def get(self, request, *args, **kwargs):
        if self.has_profile():
            return super().get(self, request, *args, **kwargs)
        return HttpResponseRedirect(reverse_lazy('main:new'))

    def get_profile(self):
        return self.request.user.profile

    def get_object(self, queryset=None):
        return self.get_profile()


class ProfileCreateView(ProfileMixin, FormMixin, SuccessURLMixin, CreateView):

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        if self.has_profile():
            return HttpResponseRedirect(reverse_lazy('main:detail'))
        return super(CreateView, self).get(self, request, *args, **kwargs)  # ProfixeMixin.get = infinite loop


class ProfileDetailView(ProfileMixin, DetailView):
    pass


class ProfileUpdateView(ProfileMixin, FormMixin, SuccessURLMixin, UpdateView):
    pass


class ProfileDeleteView(ProfileMixin, SuccessURLMixin, DeleteView):
    pass
