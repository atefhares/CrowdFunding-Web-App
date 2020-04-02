def base(request):
    context = {'user_data': request.user}
    print(context)
    return context

