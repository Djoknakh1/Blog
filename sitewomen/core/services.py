def get_menu(request):
    menu = [
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
    ]
    if request.user.is_authenticated:
        menu.append({'title': 'Добавить статью', 'url_name': 'add_post'})
        menu.append({'title': 'Выйти', 'url_name': 'users:logout'})
    else:
        menu.append({'title': 'Войти', 'url_name': 'users:login'})
        if 'register' not in request.path:
            menu.append({'title': 'Регистрация', 'url_name': 'users:register'})
    return menu
