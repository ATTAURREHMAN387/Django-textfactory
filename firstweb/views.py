from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyse(request):
    djtext = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    captilization = (request.POST.get('captilization', 'off'))
    newlineremover = (request.POST.get('newlineremover', 'off'))
    extraspaceremover = (request.POST.get('extraspaceremover', 'off'))
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in djtext:
            if char not in punctuations:
              analysed = analysed + char

        params = {'purpose': 'Removed Punctuations','' 'text': analysed}
        djtext = analysed

    if(captilization=="on"):
        analysed =""
        for char in djtext:
            analysed = analysed + char.upper()

        params = {'purpose': 'Change To Upper Case', 'text': analysed}
        djtext = analysed

    if (newlineremover == "on"):
        analysed = ""
        for char in djtext:
           if char != "\n" and char !="\r":
            analysed = analysed + char
           else:
               print("no")
           print("pre", analysed)

        params = {'purpose': 'Removed NewLines', 'text': analysed}
        djtext = analysed

    if (extraspaceremover == "on"):
        analysed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
              analysed = analysed + char

        params = {'purpose': 'Removed NewLines', 'text': analysed}

    if(removepunc != "on" and captilization != "on" and newlineremover != "on" and extraspaceremover != "on" ):
        return HttpResponse("Please select Operation and Try Again")
    return render(request, "analyse.html", params)