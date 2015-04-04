# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428037736.711241
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/return.html'
_template_uri = 'return.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['foot_links', 'head_links', 'center']


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
        def foot_links():
            return render_foot_links(context._locals(__M_locals))
        def head_links():
            return render_head_links(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head_links'):
            context['self'].head_links(**pageargs)
        

        __M_writer('\n\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'center'):
            context['self'].center(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'foot_links'):
            context['self'].foot_links(**pageargs)
        

        __M_writer(' <!-- foot_links -->\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_foot_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def foot_links():
            return render_foot_links(context)
        __M_writer = context.writer()
        __M_writer('\n\n<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.6.3/css/bootstrap-select.min.css">\n<script src="//cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.6.3/js/bootstrap-select.min.js"></script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_links(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def head_links():
            return render_head_links(context)
        __M_writer = context.writer()
        __M_writer('\n<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="container top">\n    <div class="row">\n        <div class="col-md-12">\n            <div class="well well-sm">\n                <form class="form-horizontal" method="post">\n                    <fieldset>\n                        <legend class="text-center header">Return</legend>\n\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"></span>\n                            <div class="col-md-8">\n                                ')
        __M_writer(str( form['name'] ))
        __M_writer('\n                                ')
        __M_writer(str( form['name'].errors ))
        __M_writer('\n                            </div>\n                        </div>\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"></span>\n                            <div class="col-md-8">\n                                ')
        __M_writer(str( form['late_fee'] ))
        __M_writer('\n                                ')
        __M_writer(str( form['late_fee'].errors ))
        __M_writer('\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"></span>\n                            <div class="col-md-4">\n                                ')
        __M_writer(str( form['late_fee_waived'].label ))
        __M_writer('\n                                ')
        __M_writer(str( form['late_fee_waived'] ))
        __M_writer('\n                                ')
        __M_writer(str( form['late_fee_waived'].errors ))
        __M_writer('\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"></span>\n                            <div class="col-md-8">\n                                ')
        __M_writer(str( form['damage_fee'] ))
        __M_writer('\n                                ')
        __M_writer(str( form['damage_fee'].errors ))
        __M_writer('\n                            </div>\n                        </div>\n\n\n\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"></span>\n                            <div class="col-md-4">\n                                ')
        __M_writer(str( form['damage_fee_waived'].label ))
        __M_writer('\n                                ')
        __M_writer(str( form['damage_fee_waived'] ))
        __M_writer('\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <span class="col-md-1 col-md-offset-2 text-center"></span>\n                            <div class="col-md-8">\n                                ')
        __M_writer(str( form['damage'] ))
        __M_writer('\n                            </div>\n                        </div>\n\n                        <div class="form-group">\n                            <div class="col-md-12 text-center">\n                                <button type="submit" class="btn btn-primary btn-lg">Return Item</button>\n                            </div>\n                        </div>\n                    </fieldset>\n                </form>\n            </div>\n        </div>\n    </div>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/return.html", "line_map": {"66": 83, "107": 47, "113": 58, "72": 4, "108": 48, "78": 4, "84": 10, "27": 0, "92": 23, "93": 23, "94": 24, "95": 24, "96": 30, "97": 30, "98": 31, "99": 31, "100": 38, "101": 38, "102": 39, "39": 1, "104": 40, "105": 40, "106": 47, "103": 39, "44": 6, "109": 48, "110": 57, "111": 57, "112": 58, "49": 81, "91": 10, "115": 65, "54": 88, "121": 115, "114": 65, "60": 83}, "uri": "return.html"}
__M_END_METADATA
"""
