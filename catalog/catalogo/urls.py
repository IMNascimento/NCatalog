from django.urls import path
from catalogo.views import *

urlpatterns = [
    path('', index, name='index'),
    path('jobs', jobs, name="jobs"),
    path('sobre', sobre, name="sobre"),
    path('imagem/show/<int:id>', read_photography, name="get_foto"),
    path('imagem/edit/<int:id>', edit_photography, name="edit_foto"),
    path('imagem/update/<int:id>', update_photography, name="update_foto"),
    path('imagem/delete/<int:id>', delete_photography, name="delete_foto"),
    path('imagem/create', register_photography, name="create_foto"),
    path('imagem', all_photography, name="all_foto")
]

