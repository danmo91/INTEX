# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427949018.269763
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/orders.html'
_template_uri = 'orders.html'
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
        orders = context.get('orders', UNDEFINED)
        def center():
            return render_center(context._locals(__M_locals))
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
        orders = context.get('orders', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="jumbotron">\n      <div class="container">\n        <h1>Orders</h1>\n      </div>\n    </div>\n\n\n    <a href="/manager/orders.create/" id="btn_create" class="btn btn-success pull-right create">Create new order</a>\n\n\t\t<table class="table table-striped table-bordered table-hover">\n\n      <thead>\n        <tr>\n  \t\t\t\t<th>Order Date</th>\n  \t\t\t\t<th>Total</th>\n  \t\t\t\t<th>User</th>\n  \t\t\t\t<th>Charge ID</th>\n          <th>Actions</th>\n  \t\t\t</tr>\n      </thead>\n\n      <tbody>\n')
        for order in orders:
            __M_writer('          <tr>\n            <td>')
            __M_writer(str( order.order_date ))
            __M_writer('</td>\n            <td>$')
            __M_writer(str( order.total ))
            __M_writer('</td>\n            <td>')
            __M_writer(str( order.user ))
            __M_writer('</td>\n            <td>')
            __M_writer(str( order.charge_id ))
            __M_writer('</td>\n            <td>\n              <a href="/manager/orders.edit/')
            __M_writer(str(order.id))
            __M_writer('"/> Edit </a>\n              |\n              <a href="/manager/orders.delete/')
            __M_writer(str(order.id))
            __M_writer('"> Delete </a>\n            </td>\n          </tr>\n')
        __M_writer('      </tbody>\n\n\t\t</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "orders.html", "source_encoding": "ascii", "line_map": {"64": 34, "65": 34, "66": 36, "35": 1, "68": 40, "40": 44, "74": 68, "46": 3, "59": 30, "67": 36, "53": 3, "54": 27, "55": 28, "56": 29, "57": 29, "58": 30, "27": 0, "60": 31, "61": 31, "62": 32, "63": 32}, "filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/orders.html"}
__M_END_METADATA
"""
