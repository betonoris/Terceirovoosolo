from django.shortcuts import render
import operator

def paginainicial(request):
    return render(request, 'inicio.html')

def contar(request):
    textotexto = request.GET['textotexto']
    listadepalavras=textotexto.split()
    dicionariodepalavras={}
    for palavra in listadepalavras:
        if palavra in dicionariodepalavras:
            dicionariodepalavras[palavra] += 1
        else:
            dicionariodepalavras[palavra] = 1
    palavrasarrumadas=sorted(dicionariodepalavras.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'contar.html', {'textotexto':textotexto, 'contar':len(listadepalavras), 'palavrasarrumadas':palavrasarrumadas})



def notas(request):
    return render(request, 'notas.html')

