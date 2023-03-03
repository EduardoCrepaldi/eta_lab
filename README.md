# eta_lab
Atividade 2 - Pos Graduação CESAR SCHOOL - ETA 2022.1

#Result Coverage
<table class="index" data-sortable>
        <thead>
            <tr class="tablehead" title="Click to sort">
                <th class="name left" aria-sort="none" data-shortcut="n">Module</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="s">statements</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="m">missing</th>
                <th aria-sort="none" data-default-sort-order="descending" data-shortcut="x">excluded</th>
                <th class="right" aria-sort="none" data-shortcut="c">coverage</th>
            </tr>
        </thead>
        <tbody>
            <tr class="file">
                <td class="name left"><a href="src/phonebook.py">src/phonebook.py</a></td>
                <td>83</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="83 83">100%</td>
            </tr>
            <tr class="file">
                <td class="name left"><a href="test/test_phonebook.py">test/test_phonebook.py</a></td>
                <td>191</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="191 191">100%</td>
            </tr>
        </tbody>
        <tfoot>
            <tr class="total">
                <td class="name left">Total</td>
                <td>274</td>
                <td>0</td>
                <td>0</td>
                <td class="right" data-ratio="274 284">100%</td>
            </tr>
        </tfoot>
    </table>

## Setup

```bash
pip install -r requirements.txt
```

## Unittest

```bash
python -m unittest -v
```

## Pytest

```bash
pytest .
```

## Test Coverage

- `coverage` and `pytest-cov` packages are required
- Add `pragma: no cover` to exclude code from coverage report

### With `pytest`

Terminal report:

 ```bash
pytest --cov-report term-missing --cov .
 ```

HTML report:

```bash
pytest --cov-report html --cov .
```

### With `unittest`

To generate report:

```bash
python -m coverage run -m unittest
```

To view report in terminal:

```bash
python -m coverage report
```

To view report in HTML:

```bash
python -m coverage html
```

