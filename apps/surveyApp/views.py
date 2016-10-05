from django.shortcuts import render, redirect, HttpResponse

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    return render(request, "surveyApp/index.html")

def create_survey(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['locations'] = request.POST['locations']
        request.session['languages'] = request.POST['languages']
        request.session['comments'] = request.POST['comments']
        return redirect('/result')
    else:
        return redirect('/')

def submitted_info(request):
    return render (request, 'surveyApp/result.html')
