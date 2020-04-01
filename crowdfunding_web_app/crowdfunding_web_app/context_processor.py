def base(request):
    user = {'is_signedin': request.user.is_authenticated}
    context = {'user': user}

    return context
