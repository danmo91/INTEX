# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428360156.267143
_enable_loop = True
_template_filename = 'C:\\Users\\brian_000\\projects\\intex\\homepage\\templates/index.loginform.html'
_template_uri = 'index.loginform.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t\t<form class=form-signin id="loginform" method="POST" action="/homepage/index.loginform/">\r\n\r\n')
        for error in form.non_field_errors():
            __M_writer('\r\n\t\t\t\t\t<p><span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span> ')
            __M_writer(str( error ))
            __M_writer(' </p>\r\n\r\n\r\n')
        __M_writer('\r\n')
        for field in form:
            __M_writer('\r\n\t\t\t\t<label class="sr-only"> ')
            __M_writer(str( field.name ))
            __M_writer('</label>\r\n\r\n\t\t\t\t\t')
            __M_writer(str( field ))
            __M_writer('\r\n\r\n')
            if field.errors != '':
                __M_writer('\r\n\t\t\t\t\t\t')
                __M_writer(str( field.errors ))
                __M_writer('\r\n\r\n')
            __M_writer('\r\n')
        __M_writer('\r\n\t\t\t<button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>\r\n\r\n\t\t</form>\r\n\r\n\t\t<a id="forgot_password">Forgot my password</a>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.loginform.html", "line_map": {"64": 19, "65": 21, "66": 22, "67": 23, "68": 23, "69": 26, "70": 28, "76": 70, "27": 0, "35": 1, "40": 36, "46": 4, "53": 4, "54": 8, "55": 9, "56": 10, "57": 10, "58": 14, "59": 15, "60": 16, "61": 17, "62": 17, "63": 19}, "source_encoding": "ascii", "filename": "C:\\Users\\brian_000\\projects\\intex\\homepage\\templates/index.loginform.html"}
__M_END_METADATA
"""
