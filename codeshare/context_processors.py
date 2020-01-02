from codeshare.models import Problem


def search_context(request):
    return {'problems': Problem.objects.all()}
