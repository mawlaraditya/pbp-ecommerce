from django.urls import path
from main.views import home
from main.views import home, add_new_hat
# from main.views import home, add_new_hat, show_xml
# from main.views import home, add_new_hat, show_xml, show_json
# from main.views import home, add_new_hat, show_xml, show_json, show_xml_by_id, show_json_by_id


app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('add-new-hat', add_new_hat, name='add_new_hat'),
    # path('xml/', show_xml, name='show_xml'),
    # path('json/', show_json, name='show_json'),
    # path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    # path('json/<str:id>/', show_json_by_
]

# urlpatterns = [
#     path('', home, name='home'),
#     path('add-new-hat', add_new_hat, name='add_new_hat'),
#     path('xml/', show_xml, name='show_xml'),
#     path('json/', show_json, name='show_json'),
#     path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
# path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
# ]