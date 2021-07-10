* Assumption that `pip` is installed in your system
* Assumption that a minimum of Python `^3.5.0` is installed
* Assumption how to create a `venv` environment.
* Optional have `node` and `npm` installed to run npm commands

<hr>

`src` folder contains all files to create the API endpoints, and also the business logic. This was originally translated from `*.ts` files.

```bash
# required pip and npm
$ npm run install

# If no npm
$ pip install -r requirements.txt
```

`tests` contains all the test cases.
```bash
# npm available
$ npm run test

# If not
$ python -m unittest discover -s tests -v
```

You may also choose to run individual tests.
```bash
# npm available
$ npm run test-{file_name}
$ npm run test-coin # Example

# If not
$ python tests.test_{file_name}.{classname} -v
$ python tests.test_coin.CoinTestCase -v # Example
```
