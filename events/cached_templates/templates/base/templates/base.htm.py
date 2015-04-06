# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428360258.940362
_enable_loop = True
_template_filename = 'C:\\Users\\brian_000\\projects\\intex/base/templates/base.htm'
_template_uri = '/base/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['homepage', 'events', 'meta', 'foot_links', 'admin', 'shop', 'head_links']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def admin():
            return render_admin(context._locals(__M_locals))
        def events():
            return render_events(context._locals(__M_locals))
        def shop():
            return render_shop(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def homepage():
            return render_homepage(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def meta():
            return render_meta(context._locals(__M_locals))
        def foot_links():
            return render_foot_links(context._locals(__M_locals))
        def head_links():
            return render_head_links(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n\r\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta'):
            context['self'].meta(**pageargs)
        

        __M_writer('\r\n\r\n  <head>\r\n\r\n    <title>Colonial Heritage Foundation</title>\r\n\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\r\n    <!-- ajax jquery form plugin -->\r\n\r\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('base/media/jquery.form.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('base/media/jquery.loadmodal.js"></script>\r\n\r\n    <!-- bootstrap plugins -->\r\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('base/media/bootstrap-notify.js"></script>\r\n    <link rel="stylesheet" href="')
        __M_writer(str( STATIC_URL))
        __M_writer('base/media/animate.css">\r\n    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\r\n\r\n\r\n    <!-- login page plugins -->\r\n    <link href="http://getbootstrap.com/examples/signin/signin.css" rel="stylesheet">\r\n\r\n    <!-- Latest compiled and minified CSS -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\r\n\r\n    <!-- Optional theme -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\r\n\r\n    <!-- Google Fonts -->\r\n    <link href=\'http://fonts.googleapis.com/css?family=Arimo|Petit+Formal+Script|Alice\' rel=\'stylesheet\' type=\'text/css\'>\r\n                \r\n    <!-- Latest compiled and minified JavaScript -->\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_links'):
            context['self'].head_links(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n\r\n  </head>\r\n  <body>\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'homepage'):
            context['self'].homepage(**pageargs)
        

        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shop'):
            context['self'].shop(**pageargs)
        

        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'admin'):
            context['self'].admin(**pageargs)
        

        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'events'):
            context['self'].events(**pageargs)
        

        __M_writer('\r\n\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'foot_links'):
            context['self'].foot_links(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n\r\n  </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_homepage(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def homepage():
            return render_homepage(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_events(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def events():
            return render_events(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_foot_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def foot_links():
            return render_foot_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admin(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def admin():
            return render_admin(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shop(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shop():
            return render_shop(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head_links():
            return render_head_links(context)
        __M_writer = context.writer()
        __M_writer('\r\n      <!-- App specific head links can be organized into here -->\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/base/templates/base.htm", "line_map": {"65": 50, "66": 53, "67": 53, "68": 53, "73": 60, "138": 74, "78": 64, "16": 4, "120": 70, "18": 0, "83": 68, "174": 48, "150": 66, "186": 180, "88": 72, "132": 10, "156": 66, "93": 76, "94": 79, "95": 79, "96": 79, "144": 74, "162": 62, "180": 48, "102": 58, "40": 2, "41": 4, "42": 5, "108": 58, "46": 5, "168": 62, "114": 70, "51": 13, "52": 20, "53": 24, "54": 24, "55": 25, "56": 25, "57": 28, "58": 28, "59": 29, "60": 29, "126": 10}, "source_encoding": "ascii", "filename": "C:\\Users\\brian_000\\projects\\intex/base/templates/base.htm"}
__M_END_METADATA
"""
