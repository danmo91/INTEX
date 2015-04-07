# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428424273.080274
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/INTEX/events/templates/event_detail.html'
_template_uri = 'event_detail.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        areas = context.get('areas', UNDEFINED)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def center():
            return render_center(context)
        areas = context.get('areas', UNDEFINED)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="container">\n\n            <!-- Jumbotron Header -->\n            <header class="jumbotron hero-spacer">\n                <h1>')
        __M_writer(str( event.name ))
        __M_writer('</h1>\n                <p> ')
        __M_writer(str( event.description ))
        __M_writer('</p>\n                <p><a class="btn btn-primary btn-large">\'Merica\'!</a>\n                </p>\n            </header>\n\n            <hr>\n\n            <!-- Title -->\n            <div class="row">\n                <div class="col-lg-12">\n                    <h3>Featured Areas</h3>\n                </div>\n            </div>\n            <!-- /.row -->\n\n            <!-- Page Features -->\n            <div class="row text-center items">\n\n')
        for area in areas:
            __M_writer('\n                <div class="col-md-3 col-sm-6 hero-feature">\n                    <div class="thumbnail">\n                        <img class="item_image" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('events/media/area_images/')
            __M_writer(str( area.id))
            __M_writer('.jpg" alt="">\n                        <div class="caption">\n                            <h3>')
            __M_writer(str( area.name ))
            __M_writer('</h3>\n                            <p>')
            __M_writer(str( area.description ))
            __M_writer('</p>\n                            <p>\n                                <a href="/events/area_detail/')
            __M_writer(str( area.id ))
            __M_writer('" class="btn btn-default">More Info</a>\n                            </p>\n                        </div>\n                    </div>\n                </div>\n\n')
        __M_writer('\n\n            </div>\n            <!-- /.row -->\n\n            <hr>\n\n            <!-- Footer -->\n            <footer>\n                <div class="row">\n                    <div class="col-lg-12">\n                        <p>Copyright Your Website 2014</p>\n                    </div>\n                </div>\n            </footer>\n\n        </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 31, "65": 31, "66": 31, "67": 31, "68": 33, "69": 33, "70": 34, "71": 34, "72": 36, "73": 36, "74": 43, "80": 74, "27": 0, "37": 1, "42": 61, "48": 3, "57": 3, "58": 8, "59": 8, "60": 9, "61": 9, "62": 27, "63": 28}, "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/INTEX/events/templates/event_detail.html", "uri": "event_detail.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
