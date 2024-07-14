# urls.py
from django.urls import path
from .views import MaterialGroupedView,VajillaListCreateView, MedallasListCreateView, LlaverosListCreateView, BanderinesListCreateView, ObjetoMagicoListCreateView, ArrojadizosListCreateView, MedallonListCreateView

urlpatterns = [
    path('vajillas/', VajillaListCreateView.as_view(), name='vajilla-list-create'),
    path('medallas/', MedallasListCreateView.as_view(), name='medallas-list-create'),
    path('llaveros/', LlaverosListCreateView.as_view(), name='llaveros-list-create'),
    path('banderines/', BanderinesListCreateView.as_view(), name='banderines-list-create'),
    path('objeto-magico/', ObjetoMagicoListCreateView.as_view(), name='objeto-magico-list-create'),
    path('arrojadizos/', ArrojadizosListCreateView.as_view(), name='arrojadizos-list-create'),
    path('medallones/', MedallonListCreateView.as_view(), name='medallon-list-create'),
    path('material/', MaterialGroupedView.as_view(), name='material_grouped'),

]
