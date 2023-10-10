from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FormValidMixin, ComplainantAccessMixin, SuperUserAccessMixin, DeleteAccessMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User, Crime, Culprit, Complaint
from .forms import ProfileForm, SignupForm

class Index(ListView):
	template_name = 'justice/index.html'
	model = Crime


class CrimeDetail(DetailView):
	def get_object(self):
		slug = self.kwargs.get('slug')
		return get_object_or_404(Crime, slug=slug)


class Signup(CreateView):
	model = User
	form_class = SignupForm
	template_name = 'justice/signup.html'
	success_url = reverse_lazy('Justice:login')


class Profile(LoginRequiredMixin, ListView):
	template_name = 'justice/profile.html'

	def get_queryset(self):
		if self.request.user.is_superuser:
			return Complaint.objects.all()
		else:
			return Complaint.objects.filter(complainant=self.request.user)


class EditProfile(LoginRequiredMixin, UpdateView):
	model = User
	form_class = ProfileForm
	template_name = 'justice/edit_profile.html'
	success_url = reverse_lazy('Justice:login')

	def get_object(self):
		return User.objects.get(pk=self.request.user.pk)


class FileComplaint(LoginRequiredMixin, FormValidMixin, CreateView):
	model = Complaint
	fields = ['crime', 'urgency', 'date', 'discription', 'culprit', 'video', 'v_caption', 'audio', 'a_caption', 'picture', 'p_caption']
	template_name = 'justice/complain.html'


class ModifyComplaint(ComplainantAccessMixin, UpdateView):
	model = Complaint
	fields = ['crime', 'urgency', 'date', 'discription', 'culprit', 'video', 'v_caption', 'audio', 'a_caption', 'picture', 'p_caption']
	template_name = 'justice/complain.html'


class HandleComplaint(SuperUserAccessMixin, UpdateView):
	model = Complaint
	fields = ['crime', 'urgency', 'date', 'discription', 'culprit', 'video', 'v_caption', 'audio', 'a_caption', 'picture', 'p_caption', 'status']
	template_name = 'justice/complain.html'


class CloseComplaint(ComplainantAccessMixin, DeleteAccessMixin, DeleteView):
	model = Complaint
	success_url = reverse_lazy('Justice:profile')