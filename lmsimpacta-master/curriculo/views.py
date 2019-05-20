from django.shortcuts import render, get_object_or_404

from curriculo.models import Curso
from curriculo.models import Disciplina

def curso(request, sigla):
    c = get_object_or_404(Curso, sigla=sigla)
    context = {
        'curso': c,
        'matriz': c.monta_matriz()
    }
    return render(request, 'curriculo/curso.html', context)

def cursos(request):
    context = {
        'cursos': Curso.objects.all()
    }
    return render(request, 'curriculo/cursos.html', context)



def disciplina(request,id_disciplina):
    context = {
        'disciplina': get_object_or_404(Disciplina, id=id_disciplina)

    }
    return render(request, 'curriculo/disciplina.html', context)





