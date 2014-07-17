from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    assets_env = request.webassets_env
    css_urls = assets_env['css_theme'].urls()
    return {'project': 'hello MyProject', 'css_urls': css_urls}
