# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428171879.314584
_enable_loop = True
_template_filename = '/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/events.html'
_template_uri = 'events.html'
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
        events = context.get('events', UNDEFINED)
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
        events = context.get('events', UNDEFINED)
        def center():
            return render_center(context)
        __M_writer = context.writer()
        __M_writer('\n\n    <div class="jumbotron">\n      <div class="container">\n        <h1>Events</h1>\n      </div>\n    </div>\n\n\n    <a href="/manager/events.create/" id="btn_create" class="btn btn-success pull-right create">Create new event</a>\n\n\t\t<table class="table table-striped table-bordered table-hover">\n\n      <thead>\n        <tr>\n          <th>Name</th>\n          <th>Description</th>\n          <th>Start Date</th>\n          <th>End Date</th>\n          <th>Venue</th>\n          <th>Actions</th>\n        </tr>\n      </thead>\n\n      <tbody>\n')
        for event in events:
            __M_writer('          <tr>\n            <td>')
            __M_writer(str( event.name ))
            __M_writer('</td>\n            <td>')
            __M_writer(str( event.description ))
            __M_writer('</td>\n            <td>')
            __M_writer(str( event.start ))
            __M_writer('</td>\n            <td>')
            __M_writer(str( event.end ))
            __M_writer('</td>\n            <td>')
            __M_writer(str( event.venue ))
            __M_writer('</td>\n            <td>\n              <a href="/manager/events.edit/')
            __M_writer(str(event.id))
            __M_writer('"/> Edit </a>\n              |\n              <a href="/manager/events.delete/')
            __M_writer(str(event.id))
            __M_writer('"> Delete </a>\n\n\n            </td>\n          </tr>\n')
        __M_writer('      </tbody>\n\n\t\t</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Dan/Projects/IS 413/cheritagefoundation/sprint3/manager/templates/events.html", "line_map": {"64": 34, "65": 34, "66": 36, "67": 36, "68": 38, "69": 38, "70": 44, "76": 70, "27": 0, "35": 1, "40": 48, "46": 3, "53": 3, "54": 28, "55": 29, "56": 30, "57": 30, "58": 31, "59": 31, "60": 32, "61": 32, "62": 33, "63": 33}, "source_encoding": "ascii", "uri": "events.html"}
__M_END_METADATA
"""
