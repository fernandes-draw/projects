from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ProjectProcess


@login_required
def dashboard_view(request):
    # Traz todos os processos buscando os dados do item e cliente de uma só vez
    processes = ProjectProcess.objects.select_related(
        'item', 'item__customer').all()
    montar_pasta_count = processes.filter(status='montar_pasta').count()

    context = {
        'processes': processes,
        'montar_pasta_count': montar_pasta_count,
    }

    return render(request, 'projects/dashboard.html', context)
