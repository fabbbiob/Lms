from django.views.generic import ListView
from django.views.generic.edit import DeleteView


from alerts.models import Alert

class AlertList(ListView):
    context_object_name = "alerts"
    template_name = "alerts/list.html"

    def get_queryset(self):
        return Alert.objects.filter(sent_to = self.request.user)

def acknowledge(request):
    if request.method == 'POST':
        pka = request.POST['pk']
    else:
        pka = '0'
        
    return DeleteView(request, Alert, '/', pk = pka)
    
