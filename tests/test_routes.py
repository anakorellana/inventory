import unittest
import pytest
from contextlib import contextmanager
from flask import template_rendered
from proyecto_inventario import app
from pprint import pprint as pp


class TestRoutes(unittest.TestCase):

    def setUp(self):
        print("this is the set up")
        self.tester = app.test_client(self)

    def test_home_returns_200(self):
        # tester = app.test_client(self)
        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.data, '/')

    def test_storeform_200(self):
        # tester = app.test_client(self)
        response = self.tester.get('/storeform')
        self.assertEqual(response.status_code, 200)


    def test_getstorestable_200(self):
        # tester = app.test_client(self)
        response = self.tester.get('/list_stores')
        self.assertEqual(response.status_code, 200)

    def test_editstore_500(self):
        # tester = app.test_client(self)
        response = self.tester.get('/store/<string:store_id>/')
        self.assertEqual(response.status_code, 500)

    def test_getproducts_500(self):
        # tester = app.test_client(self)
        response = self.tester.get('/product_list')
        self.assertEqual(response.status_code, 500)

    def test_product_404(self):
        # tester = app.test_client(self)
        response = self.tester.get('/product/<string:name>')
        self.assertEqual(response.status_code, 404)

    def test_edit_product_500(self):
        # tester = app.test_client(self)
        response = self.tester.get('/products/<string:store>/<string:name>')
        self.assertEqual(response.status_code, 500)

    def test_delete_product_500(self):
        # tester = app.test_client(self)
        response = self.tester.get('/delete/product/<string:store_id>/<string:name>')
        self.assertEqual(response.status_code, 500)


    # @contextmanager
    # def captured_templates(app, recorded, **extra):
    #     def record(sender, template, context):
    #         recorded.append((template, context))
    #
    #     return template_rendered.connect(record, app)
    #     try:
    #         yield recorded
    #     finally:
    #         template_rendered.disconnect(record, app)
    # templates = []
    # with captured_templates(app) as templates:
    #     rv = app.test_client().get('/storesname')
    #     assert rv.status_code == 200
    #     assert len(templates) == 1
    #     template, context = templates[0]
    #     assert template.name == 'storesname.html'
    #     assert len(context['items']) == 10


if __name__ == '__main__':
    unittest.main()

