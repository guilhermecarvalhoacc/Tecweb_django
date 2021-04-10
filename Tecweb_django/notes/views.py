from django.shortcuts import render, redirect
from .models import Note


def add(title,content):
    note_obj = Note(title = title, content= content)
    note_obj.save()


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        ID = request.POST.get("Id")
        print(title,"\n",content,"\n",ID)
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        if ID == "":
            add(title,content)
        else:
            if title == None:
                Note.objects.filter(id=ID).delete()
            else:
                print("entrei no else loko")
                edition = Note.objects.get(id=ID)
                edition.title = title
                edition.content = content
                edition.save()
        return redirect('index')
    
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})
