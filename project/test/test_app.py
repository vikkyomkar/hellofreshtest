from copy import deepcopy
import unittest
import json
import sys
sys.path.append('app/')
import app


BASE_URL = 'http://127.0.0.1:5000/configs'
NONEXIST_CONFIG_URL = '{}/test3'.format(BASE_URL)
EXIST_CONFIG_URL = '{}/test1'.format(BASE_URL)
SEARCH_URL = 'http://127.0.0.1:5000/search?'

class TestFlaskApi(unittest.TestCase):

    def setUp(self):
        self.backup_configs = deepcopy(app.configs)  # Backup of current configs data
        self.app = app.app.test_client()
        self.app.testing = True


###### Get: testcase
    def test_get_all(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['configs']), 2)


    def test_get_one(self):
        response = self.app.get(EXIST_CONFIG_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)


    def test_item_not_exist(self):
        response = self.app.get(NONEXIST_CONFIG_URL)
        self.assertEqual(response.status_code, 404)

##### POST: tastcase
    def test_post_with_missing_name(self):
        item = {"data" : {"age": 20}}
        response = self.app.post(BASE_URL,data=json.dumps(item),content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_post_with_missing_age(self):
        item = {"name": "test11"}
        response = self.app.post(BASE_URL,data=json.dumps(item),content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_post_with_non_int_age(self):
        item = {"name": "test11","data" : {"age": "20"}}
        response = self.app.post(BASE_URL,data=json.dumps(item),content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_post_correct_data(self):
        item = {"name": "test11","data" : {"age": 20}}
        response = self.app.post(BASE_URL,data=json.dumps(item),content_type='application/json')
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['config']['name'], 'test11')
        self.assertEqual(data['config']['data']['age'], 20)


    def test_post_same_data_again(self):
        item = {"name": "test11","data" : {"age": 20}}
        response = self.app.post(BASE_URL,data=json.dumps(item),content_type='application/json')
        self.assertEqual(response.status_code, 400)

###### PUT testcase
    def test_put_for_existing_config(self):
        item = {"data" : {"age" : 30}}
        response = self.app.put(EXIST_CONFIG_URL,data=json.dumps(item),content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['config']['data']['age'], 30)
        self.assertEqual(self.backup_configs[0]['data']['age'], 10)  # old age

    def test_put_for_non_existing_config(self):
        item = {"data" : {"age" : 35}}
        response = self.app.put(NONEXIST_CONFIG_URL,data=json.dumps(item),content_type='application/json')
        self.assertEqual(response.status_code, 404)


    def test_put_for_non_int_age(self):
        item = {"data" : {"age" : "ten"}}
        response = self.app.put(NONEXIST_CONFIG_URL,data=json.dumps(item),content_type='application/json')
        self.assertEqual(response.status_code, 404)

##### Search testcase
    def test_search_existing_data(self):
        ##### make a new test entry
        item = {"name": "test12","data" : {"age": 20}}
        response = self.app.post(BASE_URL,data=json.dumps(item),content_type='application/json')
        response = self.app.get(SEARCH_URL + "name=test12&data.age=20")
        self.assertEqual(response.status_code, 200)

    def test_search_non_existing_data(self):
        response = self.app.get(SEARCH_URL + "name=test22&data.age=10")
        self.assertEqual(response.status_code, 404)

    def test_search_with_bad_request(self):
        response = self.app.get(SEARCH_URL + "name=test22&data.age=")
        self.assertEqual(response.status_code, 400)

    def test_search_with_age_as_string(self):
        response = self.app.get(SEARCH_URL + "name=test22&data.age=abc")
        self.assertEqual(response.status_code, 404)




##### Delete testcase
    def test_delete_present_entry(self):
        ##### make a new entry
        item = {"name": "test12","data" : {"age": 20}}
        response = self.app.post(BASE_URL,data=json.dumps(item),content_type='application/json')
        self.assertEqual(response.status_code, 201)
        #### Delete the entry
        response = self.app.delete(BASE_URL + "/test12")
        self.assertEqual(response.status_code, 204)


    def test_delete_absent_entry(self):
        response = self.app.delete(BASE_URL + "/test12")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
