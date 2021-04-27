# Ihave created this file

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # param= {'name':'manish', 'place':'delhi'} #we can pass variable also through render
    return render(request, 'index.html')


def aboutme(request):
    return render(request, 'aboutme.html')


def contactme(request):
    return render(request, 'contactme.html')


def analyse(request):
    # here we are getting the text from text area
    sitetext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    print(removepunc)
    print(sitetext)

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analysed = ""
        for char in sitetext:
            if char not in punctuations:
                analysed = analysed+char
        params = {'purpose': 'Removed Punctuation', 'analysed_text': analysed}
        sitetext = analysed
        # return render(request,'analyse.html', params)

    if fullcaps == 'on':
        analysed = ''
        for char in sitetext:
            analysed = analysed + char.upper()
        params = {'purpose': 'Capatalize Text', 'analysed_text': analysed}
        sitetext = analysed
        # return render(request,'analyse.html', params)

    if newlineremover == 'on':
        analysed = ''
        for char in sitetext:
            if char != "\n" and char != "\r":
                analysed = analysed+char
        params = {'purpose': 'New Line Removing', 'analysed_text': analysed}
        sitetext = analysed
        # return render(request,'analyse.html', params)

    if extraspaceremover == 'on':
        analysed = ''
        for index, char in enumerate(sitetext):
            if sitetext[index] == ' ' and sitetext[index+1] == ' ':
                pass
            else:
                analysed = analysed+char
        params = {'purpose': 'Extra Space Removing', 'analysed_text': analysed}
        sitetext = analysed
        # return render(request,'analyse.html', params)

    if charcounter == 'on':
        analysed = ''
        analysed2 = str(len(sitetext))+" characters are there"

        analysed = sitetext+"\n" + analysed2
        params = {'purpose': 'Character Counting', 'analysed_text': analysed}

    if(removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcounter != 'on'):
        return HttpResponse('You did not select any options<br><a href="/">Home</a>')

    return render(request, 'analyse.html', params)
