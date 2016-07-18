
## DELETE

We need to override the method (normally either a GET or POST) with DELETE.

```python
    data = urllib.parse.urlencode({'id': 3}).encode('utf-8')
    req = urllib.request.Request('http://example.com/api', data, method = "DELETE")
    with urllib.request.urlopen(req) as response:
        print('status', response.getcode())
        print(response.read().encode('utf-8'))
```

## PUT



We need to override the method (normally either a GET or POST) with DELETE.

```python
    data = urllib.parse.urlencode({'id': 3, 'name': fred}).encode('utf-8')
    req = urllib.request.Request('http://example.com/api', data, method = "PUT")
    with urllib.request.urlopen(req) as response:
        print('status', response.getcode())
        print(response.read().encode('utf-8'))
```

FIXME: Need to double check if PUT passes data via "Request" object or via "urlopen()"?

