from projects.models import Category


def base(request):
    categories = Category.objects.order_by('name')[:6]
    context = {'user_data': request.user, 'categories': categories}
    print(context)
    return context

