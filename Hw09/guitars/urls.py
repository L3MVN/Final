from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from . import views

app_name = "guitars"

urlpatterns = [
    # Empty (root) path goes to the index view
    path("about", views.about, name="about"),
    path('', views.DepartmentListView.as_view(), name='home'),
    path("<int:pk>", views.DepartmentDetailView.as_view(), name="detail"),
    path("add", permission_required('guitars.add_guitar')(views.DepartmentCreateView.as_view()), name="create"),
    path("<int:pk>/update", permission_required('guitars.change_guitar')(views.DepartmentUpdateView.as_view()), name="update"),
    path("<int:pk>/delete", permission_required('guitars.delete_guitar')(views.DepartmentDeleteView.as_view()), name="delete"),
]