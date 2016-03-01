from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from .forms import ProfileForm
from .models import Profile


class FormMixin(object):
    """
    Form dependepcy mixin.

    Adds form_class and success_url for classes that accept POST.
    Modifies POST behavior to inject user data.
    """

    form_class = ProfileForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        post_data = request.POST.copy()  # because immutable
        post_data['user'] = request.user.id
        request.POST = post_data
        return super().post(request, *args, **kwargs)


class ModelMixin(object):
    """
    Model dependency mixin.

    Adds model to CBV.
    Adds helper methods for user profile.
    Modifies get_object method to return profile.
    Modifies GET method to check whether user has or must create a new profile.
    """

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


class ProfileCreateView(ModelMixin, FormMixin, CreateView):
    """
    Create view class which inherts model and form mixin behavior.

    Modifies GET method to check whether user needs to login, view own profile, or create new profile.
    """

    @method_decorator(login_required)  # so AnonymousUsers get redirected to signup instead of new profile
    def get(self, request, *args, **kwargs):
        if self.has_profile():
            return HttpResponseRedirect(reverse_lazy('main:detail'))
        return super(CreateView, self).get(self, request, *args, **kwargs)  # ProfixeMixin.get = infinite loop


class ProfileDetailView(ModelMixin, DetailView):
    """Detail view class which inherts model mixin behaviors."""

    pass


class ProfileUpdateView(ModelMixin, FormMixin, UpdateView):
    """Update view class which inherts model and form mixin behaviors."""

    pass


class ProfileDeleteView(ModelMixin, DeleteView):
    """Delete view class which inherts model mixin behavior."""

    pass
