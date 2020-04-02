def base(request):
    user = {'is_signedin': request.user.is_authenticated, 'test': "test"}
    context = {'user_data': request.user}
    print(context)
    return context

