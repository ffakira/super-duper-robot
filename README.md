* Assumption that `pip` is installed in your system
* Assumption that a minimum of Python `^3.4.0` is installed
* Assumption how to create a `venv` environment.
* Optional have `node` and `npm` installed to run npm commands

<hr>

`src` folder contains all files to create the API endpoints, and also the business logic. This was originally translated from `*.ts` files.

```bash
# npm available
$ npm run start

# If not
$ python src/main.py
```

&nbsp;

`tests` contains all the test cases.

```bash
# npm available
$ npm run test

# If not
$ python tests/test_coin.py && python tests/test_wallet.py
```

You may also choose to run individual tests.
```bash
# npm available
$ npm run test-{file_name}
$ npm run test-coin # Example

# If not
$ python tests/test_{file_name}
$ python tests/test_coin.py # Example
```