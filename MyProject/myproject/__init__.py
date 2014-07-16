import transaction
from pyramid.config import Configurator
from webassets import Bundle
from os import path
from webassets.filter import get_filter

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .db_config import get_db_engine

from .models.pyramid_base import DBSession, Base


def _bundle_app_css(debug=False):
    sass = get_filter('sass', as_output=True)
    if debug:
        bundle = Bundle(
            Bundle(
                path.join('assets', 'css', 'theme.css'),
                path.join('assets', 'css', 'extra.css'),
            ),
            Bundle(
                path.join('assets', 'sass', 'dyno.sass'),
                filters=(sass,),
                output=path.join('assets', 'gen', 'css', 'dyno.css')
            ),
            output=path.join('gen', 'css', 'style.css')
        )
    else:
        bundle = Bundle(
            Bundle(
                path.join('assets', 'css', 'theme.css'),
                path.join('assets', 'css', 'extra.css')
            ),
            Bundle(
                path.join('assets', 'sass', 'dyno.sass'),
                filters=(sass,),
                output=path.join('assets', 'gen', 'css', 'dyno.css')
            ),
            filters=('cssmin',),
            output=path.join('gen', 'css', 'style.css')
        )

    return bundle


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = get_db_engine()
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    
    config = Configurator(settings=settings)
    config.add_jinja2_extension('webassets.ext.jinja2.AssetsExtension')
    assets_env = config.get_webassets_env()
    jinja2_env = config.get_jinja2_environment()
    if jinja2_env:
        jinja2_env.assets_environment = assets_env
    webassets_env = config.get_webassets_env()
    config.add_webasset('css_theme',
                        _bundle_app_css(debug=webassets_env.debug))
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include('pyramid_chameleon')
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
