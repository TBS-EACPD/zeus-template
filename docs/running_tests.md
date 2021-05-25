
# How to run tests


## Migrations?

If you ever run into a problem with missing columns, it's because migrations are out of sync with the test DB. Simply run `dropdb test-fast` and re-run tests.


## test selection

**Running all tests**

```bash
./manage.py test tests/
```

**running specific test**


```bash 
# file/path::method_name
./manage.py test tests/test_my_thing::test_something
```

**Runnning all tests in a directory**

```bash
./manage.py test tests/directory/
```

**Running multiple test files**

```bash 
./manage.py test tests/test_1.py tests/test_2.py
```

**Test selection shortcut**


pytest's handy `-k` argument for test selection has been remapped to our `-s` or `--select` argument. 

You can select tests by function name, e.g. `def test_something_specific() ...`, whether it's a new-style or old-style class method) by running 

```bash
./manage.py test -s test_something_specific
```

it also supports targetting file names, class name and more complex selection, like 
```bash
./manage.py test --select "test_something_specific or test_another_one" 
```


**Using pytest command directly**

you can run tests using the pytest command, which has extra options. You'll need to use the `--reuse-db` flag:


```bash

# normal test run
pytest --reuse-db tests/

# finish with a summary of failed tests
pytest  --reuse-db -rfE tests/
```

**Getting more verbose output**

you can pass -v 2 or -v 3 to get more output, like individual test runs outputted to the terminal


## Explicitly testing the french app

The vast majority of tests are run in english mode, because of a `LANGUAGE_CODE` variable in `settings/base.py`. If you'd like to test that the french app is working, you can change this variable before running your tests.

Note that you'll get a lot of false positive for failing tests, as a lot of tests are checking for english output, e.g. searching an HTTP response for a specific form error message or a program name substring.

running `pytest  --reuse-db -rfE tests/` will allow you to see all failing tests are their exceptions. If your tests look for english text, then you can expect false-failures of the form:

```
AssertionError: assert ['Sélectionne...disponibles.'] == ['Select a va...ble choices.']
```


## Repeating a test to trigger flakiness

Flakey tests are tests that fail randomly. When they happen in CI, you can't debug them, and they're difficult to reproduce locally. You can repeat a test a number of times to force it to fail.


```bash
for i in {1..10}
  do 
    ./manage.py test tests/path_to_test_file.py::test_name
done
```

Note that if the test is flakey because of sequences shared with other tests, this approach probably won't work. 