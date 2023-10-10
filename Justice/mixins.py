from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Complaint

class FormValidMixin():
    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.complainant = self.request.user
        return super().form_valid(form)


class ComplainantAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        complaint = get_object_or_404(Complaint, pk=pk)
        if complaint.complainant == request.user or request.user.is_superuser and complaint.status != 'Y':
            return super().dispatch(request, pk, *args, **kwargs)
        else:
            raise Http404()


class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404()


class DeleteAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        complaint = get_object_or_404(Complaint, pk=pk)
        if complaint.status != 'Y':
            return super().dispatch(request, pk, *args, **kwargs)
        else:
            raise Http404()