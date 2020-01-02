from django.shortcuts import render, get_object_or_404, redirect

from codeshare.models import Problem, Code


def home(request):
    codes = Code.objects.all()[:20]
    return render(request, 'index.html', {'codes': codes})


def show_problem(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    codes = Code.objects.filter(problem=problem)
    return render(request, 'problem.html', {'problem': problem, 'codes': codes})


def show_code(request, code_id):
    code = get_object_or_404(Code, pk=code_id)
    return render(request, 'code.html', {'code': code})


def show_submit(request, problem_id):
    if request.method == "POST":
        code = Code(score=request.POST['score'], handle=request.POST['handle'], code=request.POST['code'],
                    description=request.POST['description'], problem_id=problem_id)
        code.save()
        return redirect('show_problem', problem_id=problem_id)
    else:
        problem = get_object_or_404(Problem, pk=problem_id)
        return render(request, 'submit.html', {'problem': problem})
