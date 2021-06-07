#!/usr/bin/python3
import unittest
import json
from models.base import Base


class TestBaseCls(unittest.TestCase):
    def test_id(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b12 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b12.id, 12)
        self.assertEqual(b3.id, 3)

    def test_ToJsonString(self):
        Base._Base__nb_objects = 0
        temp = Base.to_json_string([])
        self.assertEqual(temp, "[]")
        temp = Base.to_json_string(None)
        self.assertEqual(temp, "[]")
        temp = Base.to_json_string([{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}])
        self.assertEqual(temp, json.dumps([{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}]))
        temp = Base.to_json_string([{}])
        self.assertEqual(temp, json.dumps([{}]))
        temp = Base.to_json_string([None])
        self.assertEqual(temp, json.dumps([None]))
        temp = Base.to_json_string([{"a": None}])
        self.assertEqual(temp, json.dumps([{"a": None}]))

    def test_FromJsonString(self):
        Base._Base__nb_objects = 0
        temp = Base.from_json_string(json.dumps([]))
        self.assertEqual(temp, [])
        temp = Base.from_json_string(None)
        self.assertEqual(temp, [])
        json_str = json.dumps([{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}])
        temp = Base.from_json_string(json_str)
        self.assertEqual(temp, json.loads(json_str))

    def test_SaveToFile(self):
        pass
if __name__ == "__main_":
    unittest.main()
