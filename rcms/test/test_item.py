from django.test import TestCase
from django.test import Client

from rcms.models import Item

client = Client()


class ItemTests(TestCase):
    @classmethod
    def setUpTestData(self):
        self.item = Item.objects.create(path="/app/test", comment="hello",
                                       value='{"test":"test"}')

    def test_add_item(self):
        r = client.post('/rcms/item/add', {
            'comment': '测试一下',
            'path': '/app/test1',
            'value': '{"test":"123456789"}',
        }, content_type="application/json")
        self.assertEqual(r.content, b'{"errcode": 0, "errmsg": "ok", "data": {"id": 2}}')

        item = Item.objects.get(id=2)
        self.assertEqual(item.comment, '测试一下')
        self.assertEqual(item.path, '/app/test1')
        self.assertEqual(item.value, '{"test":"123456789"}')




