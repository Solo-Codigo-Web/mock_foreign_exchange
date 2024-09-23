# mock_foreign_exchange

Unit tests and mock for currency exchange.

## Test Execution

```bash
pytest test_app.py
```

Resultado:

```bash
================================ test session starts ==============================
platform Linux -- Python 3.12.1, pytest-8.3.3, pluggy-1.5.0
cachedir: .pytest_cache
collected 2 items

test_app.py::test_convert_euros_to_dollars PASSED                                                               [ 50%] 
test_app.py::test_convert_euros_to_dollars_error_api PASSED                                                               [100%] 

================================== 2 passed in 0.49s ================================
```