from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from gestion.models import demonio, Batalla, Objetos_Dororo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from gestion.forms import insertBattle, addObject

class login (LoginRequiredMixin, generic.TemplateView):
    template_name = 'login.html'
    login_url = 'login'
    login_url = 'gestion:login'

class Home (LoginRequiredMixin, generic.ListView):
    model = demonio
    template_name='listar.html'
    context_object_name = "obj"
    login_url = 'gestion:login'

class Hist (LoginRequiredMixin, generic.ListView):
    model = Batalla
    template_name = 'historial.html'
    context_object_name = 'obj'
    login_url = 'gestion:login'

class Pelea (LoginRequiredMixin, generic.ListView):
    model = demonio
    template_name = 'pelea.html'
    context_object_name = 'obj'
    login_url = 'gestion:login'

class items (LoginRequiredMixin, generic.ListView):
    model = Objetos_Dororo
    template_name = 'elementos.html'
    context_object_name = 'obj'
    login_url = 'gestion:login'

class insertBattle (LoginRequiredMixin, generic.CreateView):
    model = Batalla
    template_name = 'add_pelea.html'
    context_object_name = 'obj'
    login_url = 'gestion:login'
    success_url = reverse_lazy('gestion:home')
    form_class = insertBattle

class insertObject (LoginRequiredMixin, generic.CreateView):
    model = Objetos_Dororo
    template_name = 'add_elemento.html'
    context_object_name = 'obj'
    login_url = 'gestion:login'
    success_url = reverse_lazy('gestion:objetos')
    form_class = addObject

def demon_print(self, pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import Table

    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rigthMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
    )
    demonios = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de demonios", styles['Heading1'])
    demonios.append(header)
    headings = ('ID','Nombre','Parte en Posesion','Lugar de Ubicacion')
    if not pk:
        todosdemonios = [(p.id, p.nombre, p.lugar.nombre, p.parte.nombre)
                         for p in demonio.objects.all().order_by('pk')]
    else:
        todosdemonios = [(p.id, p.nombre, p.lugar.nombre, p.parte.nombre)
                         for p in demonio.objects.filter(id=pk)]
    t = Table([headings] + todosdemonios)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue),
        ]
    ))

    demonios.append(t)
    doc.build(demonios)
    response.write(buff.getvalue())
    buff.close()
    return response