# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from course_app import facade


def index():
    cmd = facade.list_courses_cmd()
    course_list = cmd()
    course_short = [facade.short_course_dct(n) for n in course_list]
    return JsonResponse(course_short)


def save(**course_properties):
    cmd = facade.save_course_cmd(**course_properties)
    return _save_or_update_json_response(cmd)


def update(course_id, **course_properties):
    cmd = facade.update_course_cmd(course_id, **course_properties)
    return _save_or_update_json_response(cmd)


def delete(course_id):
    facade.delete_course_cmd(course_id)()


def _save_or_update_json_response(cmd):
    try:
        course = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    return JsonResponse(facade.detail_course_dct(course))

