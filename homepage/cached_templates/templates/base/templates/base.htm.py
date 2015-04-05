# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428204956.27071
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/base/templates/base.htm'
_template_uri = '/base/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['admin', 'homepage', 'head_links', 'events', 'shop', 'foot_links', 'meta']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def homepage():
            return render_homepage(context._locals(__M_locals))
        def head_links():
            return render_head_links(context._locals(__M_locals))
        def shop():
            return render_shop(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def admin():
            return render_admin(context._locals(__M_locals))
        def foot_links():
            return render_foot_links(context._locals(__M_locals))
        def events():
            return render_events(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def meta():
            return render_meta(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n\n  ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'meta'):
            context['self'].meta(**pageargs)
        

        __M_writer('\n\n  <head>\n\n    <title>Colonial Heritage Foundation</title>\n\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n\n    <!-- ajax jquery form plugin -->\n\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('base/media/jquery.form.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('base/media/jquery.loadmodal.js"></script>\n\n    <!-- bootstrap plugins -->\n    <script src="')
        __M_writer(str( STATIC_URL))
        __M_writer('base/media/bootstrap-notify.js"></script>\n    <link rel="stylesheet" href="')
        __M_writer(str( STATIC_URL))
        __M_writer('base/media/animate.css">\n    <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\n\n\n    <!-- login page plugins -->\n    <link href="http://getbootstrap.com/examples/signin/signin.css" rel="stylesheet">\n\n    <!-- Latest compiled and minified CSS -->\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\n\n    <!-- Optional theme -->\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap-theme.min.css">\n\n    <!-- Latest compiled and minified JavaScript -->\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_links'):
            context['self'].head_links(**pageargs)
        

        __M_writer('\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n  </head>\n  <body>\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'homepage'):
            context['self'].homepage(**pageargs)
        

        __M_writer('\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'shop'):
            context['self'].shop(**pageargs)
        

        __M_writer('\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'admin'):
            context['self'].admin(**pageargs)
        

        __M_writer('\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'events'):
            context['self'].events(**pageargs)
        

        __M_writer('\n\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'foot_links'):
            context['self'].foot_links(**pageargs)
        

        __M_writer('\n\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_admin(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def admin():
            return render_admin(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_homepage(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def homepage():
            return render_homepage(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head_links():
            return render_head_links(context)
        __M_writer = context.writer()
        __M_writer('\n      <!-- App specific head links can be organized into here -->\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_events(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def events():
            return render_events(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_shop(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def shop():
            return render_shop(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_foot_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def foot_links():
            return render_foot_links(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def meta():
            return render_meta(context)
        __M_writer = context.writer()
        __M_writer('\n\n\n  ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "/base/templates/base.htm", "line_map": {"65": 47, "66": 50, "67": 50, "68": 50, "73": 57, "138": 67, "78": 61, "16": 4, "120": 55, "18": 0, "83": 65, "174": 10, "150": 59, "186": 180, "88": 69, "132": 45, "156": 59, "93": 73, "94": 76, "95": 76, "96": 76, "144": 67, "162": 71, "180": 10, "102": 63, "40": 2, "41": 4, "42": 5, "108": 63, "46": 5, "168": 71, "114": 55, "51": 13, "52": 20, "53": 24, "54": 24, "55": 25, "56": 25, "57": 28, "58": 28, "59": 29, "60": 29, "126": 45}, "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/base/templates/base.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
