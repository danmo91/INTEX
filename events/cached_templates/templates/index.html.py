# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428172797.785181
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/events/templates/index.html'
_template_uri = 'index.html'
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
        def center():
            return render_center(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        def center():
            return render_center(context)
        events = context.get('events', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="container">\n\n            <!-- Jumbotron Header -->\n            <header class="jumbotron hero-spacer">\n                <h1>Events</h1>\n                <p>Come experience American Colonial History like never before.</p>\n                <p><a class="btn btn-primary btn-large">\'Merica\'!</a>\n                </p>\n            </header>\n\n            <hr>\n\n            <!-- Title -->\n            <div class="row">\n                <div class="col-lg-12">\n                    <h3>Latest Features</h3>\n                </div>\n            </div>\n            <!-- /.row -->\n\n            <!-- Page Features -->\n            <div class="row text-center items">\n\n')
        for event in events:
            __M_writer('\n                <div class="col-md-3 col-sm-6 hero-feature">\n                    <div class="thumbnail">\n                        <img class="item_image" src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('events/media/event_images/')
            __M_writer(str( event.id))
            __M_writer('.png" alt="">\n                        <div class="caption">\n                            <h3>')
            __M_writer(str( event.name ))
            __M_writer('</h3>\n                            <p>')
            __M_writer(str( event.description ))
            __M_writer('</p>\n                            <p>\n                                <a href="/events/event_detail/')
            __M_writer(str( event.id ))
            __M_writer('" class="btn btn-default">More Info</a>\n                            </p>\n                        </div>\n                    </div>\n                </div>\n\n')
        __M_writer('\n\n            </div>\n            <!-- /.row -->\n\n            <hr>\n\n            <!-- Footer -->\n            <footer>\n                <div class="row">\n                    <div class="col-lg-12">\n                        <p>Copyright Your Website 2014</p>\n                    </div>\n                </div>\n            </footer>\n\n        </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 34, "65": 34, "66": 36, "27": 0, "36": 1, "68": 43, "41": 61, "74": 68, "47": 3, "67": 36, "55": 3, "56": 27, "57": 28, "58": 31, "59": 31, "60": 31, "61": 31, "62": 33, "63": 33}, "source_encoding": "ascii", "uri": "index.html", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/events/templates/index.html"}
__M_END_METADATA
"""
