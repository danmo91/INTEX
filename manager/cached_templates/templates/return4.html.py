# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428123497.2018
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/return4.html'
_template_uri = 'return4.html'
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
        rentals = context.get('rentals', UNDEFINED)
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
        rentals = context.get('rentals', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="jumbotron">\n  <div class="container">\n    <h1>Rentals</h1>\n  </div>\n</div>\n\n<div class="container">\n\n    <table class="table table-striped table-bordered table-hover display" id="">\n\n      <thead>\n\n        <tr>\n                  <th>Item</th>\n                  <th>Rental Date</th>\n                  <th>Due Date</th>\n                  <th>Return Date</th>\n                  <th>Customer</th>\n                  <th>Actions</th>\n              </tr>\n\n      </thead>\n\n      <tbody>\n\n')
        for rental in rentals:
            __M_writer('                  <tr>\n                      <td>')
            __M_writer(str( rental.description ))
            __M_writer('</td>\n                      <td>')
            __M_writer(str( rental.rental_date ))
            __M_writer('</td>\n                      <td>')
            __M_writer(str( rental.due_date ))
            __M_writer('</td>\n                      <td>')
            __M_writer(str( rental.return_date ))
            __M_writer('</td>\n\n')
            if rental.user is not None:
                __M_writer('            <td>')
                __M_writer(str( rental.user.first_name + ' ' + rental.user.last_name ))
                __M_writer('</td>\n\n')
            else:
                __M_writer('            <td>None</td>\n\n')
            __M_writer("                      <td>\n                          <a data-id ='")
            __M_writer(str(rental.id))
            __M_writer('\' class="btn btn-danger return"/> Return </a>\n                      </td>\n                  </tr>\n')
        __M_writer('\n      </tbody>\n\n    </table>\n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "return4.html", "line_map": {"64": 37, "65": 38, "66": 38, "67": 38, "68": 40, "69": 41, "70": 44, "71": 45, "72": 45, "73": 49, "79": 73, "27": 0, "35": 1, "40": 56, "46": 3, "53": 3, "54": 30, "55": 31, "56": 32, "57": 32, "58": 33, "59": 33, "60": 34, "61": 34, "62": 35, "63": 35}, "source_encoding": "ascii", "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/return4.html"}
__M_END_METADATA
"""