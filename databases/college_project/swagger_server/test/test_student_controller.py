# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.student import Student  # noqa: E501
from swagger_server.models.student_input import StudentInput  # noqa: E501
from swagger_server.models.student_response import StudentResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStudentController(BaseTestCase):
    """StudentController integration test stubs"""

    def test_students_get(self):
        """Test case for students_get

        Retrieve all students
        """
        response = self.client.open(
            '/college_api/students',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_students_id_delete(self):
        """Test case for students_id_delete

        Delete a student
        """
        response = self.client.open(
            '/college_api/students/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_students_id_put(self):
        """Test case for students_id_put

        Update an existing student
        """
        body = StudentInput()
        response = self.client.open(
            '/college_api/students/{id}'.format(id=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_students_post(self):
        """Test case for students_post

        Add a new student
        """
        body = StudentInput()
        response = self.client.open(
            '/college_api/students',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
