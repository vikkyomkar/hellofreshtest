## Flask HTTP service testing
Below python modules are used for the testing purpose. 

- [unittest](https://docs.python.org/2/library/unittest.html)
- [coverage](https://coverage.readthedocs.io/en/v4.5.x/)


## Prerequisites
- python2.x
- pip
- unittest
- coverage

## Setup
_`pip install requirements.txt`_

## Usage
_Note: Run the tests from project Dir_
- **unittest**
```
$ python tests/test_app.py -v
test_delete_absent_entry (__main__.TestFlaskApi) ... ok
test_delete_present_entry (__main__.TestFlaskApi) ... ok
test_get_all (__main__.TestFlaskApi) ... ok
test_get_one (__main__.TestFlaskApi) ... ok
test_item_not_exist (__main__.TestFlaskApi) ... ok
test_post_correct_data (__main__.TestFlaskApi) ... ok
test_post_same_data_again (__main__.TestFlaskApi) ... ok
test_post_with_missing_age (__main__.TestFlaskApi) ... ok
test_post_with_missing_name (__main__.TestFlaskApi) ... ok
test_post_with_non_int_age (__main__.TestFlaskApi) ... ok
test_put_for_existing_config (__main__.TestFlaskApi) ... ok
test_put_for_non_existing_config (__main__.TestFlaskApi) ... ok
test_put_for_non_int_age (__main__.TestFlaskApi) ... ok
test_search_existing_data (__main__.TestFlaskApi) ... ok
test_search_non_existing_data (__main__.TestFlaskApi) ... ok
test_search_with_age_as_string (__main__.TestFlaskApi) ... ok
test_search_with_bad_request (__main__.TestFlaskApi) ... ok
----------------------------------------------------------------------
Ran 17 tests in 0.049s
OK
```
***Description***: Seventeen testcases were executed for this http service and all are passed

- **Coverage**
```
$ coverage run tests/test_app.py
.................
----------------------------------------------------------------------
Ran 17 tests in 0.072s
OK
```
```
$ coverage report app/app.py
Name         Stmts   Miss  Cover
--------------------------------
app/app.py      62      5    92%
--------------------------------
```
***Description***: Code coverage of http service is 92%

### Scenarios Covered by this test suite
```
- Test get all data
- Test get one data
- Test get non exit data
- Test post correct data
- Test post same data again
- test post with missing age
- Test post with missing name
- Test post with non int age
- Test put for existing config
- Test put for non existing config
- Test put for non int age
- Test search existing data
- Test search non existing data
- Test search with age as string
- Test search with bad request
- Test delete absent entry
- Test delete present entry
```

### Owner
 _vikkyomkar@gmail.com_
