from django.shortcuts import render, redirect
from .models import Note


def add(title,content,tag):
    note_obj = Note(title = title, content= content,tag = tag)
    note_obj.save()


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        ID = request.POST.get("Id")
        tag = request.POST.get("tag")
        print(title,"\n",content,"\n",ID, "\n",tag)
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        if ID == "":
            add(title,content,tag)
        else:
            if title == None:
                Note.objects.filter(id=ID).delete()
            else:
                print("entrei no else loko")
                edition = Note.objects.get(id=ID)
                edition.title = title
                edition.content = content
                edition.tag = tag
                edition.save()
        return redirect('index')
    
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def listatags(request):
    all_tags = Note.objects.values("tag").distinct()
    print(f"todas as tags: {all_tags}")

    listatags = [ i["tag"] for i in all_tags]
    print(listatags)
    return render(request, "notes/listatags.html", {"tags":listatags} )


