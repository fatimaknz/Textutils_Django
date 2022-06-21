# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    #check checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')


    #check which checkbox is on
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"/,<>./?@#$%^&*_~'''
        analyzed = " "
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext = analyzed


    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'changed to upper case', 'analyzed_text': analyzed}
        djtext = analyzed


    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        djtext = analyzed


    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate (djtext):
            if not(djtext[index] == " " and djtext[index+1]== " "):
                analyzed = analyzed + char

        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Error: Please select the any operation")


    return render(request, 'analyze.html', params)

