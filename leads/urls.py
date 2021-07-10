from leads.forms import LeadCategoryUpdateForm
from django.urls import path
from .views import  (
    AssignAgentView,
    CategoryDeleteView,
    CategoryDetailView,
    CategoryUpdateView,
    LeadCreateView, 
    LeadDeleteView, 
    LeadDetailView, 
    LeadListView, 
    LeadUpdateView, 
    CategoryListView,
    LeadCategoryUpdateView,
    CategoryCreateView,
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'), 
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='assign-agent'),
    path('<int:pk>/catagory/', LeadCategoryUpdateView.as_view(), name='lead-category-update'),   
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('create-category/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('categories/<int:pk>/update', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete', CategoryDeleteView.as_view(), name='category-delete'), 
    
]