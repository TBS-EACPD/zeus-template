

# First time setup

```bash
python3 -m virtualenv venv/
source venv/bin/activate
pip install -r requirements-dev.txt
source dev-scripts/create-db-user.sh
source dev-scripts/create-dev-db.sh
```

# Running tests

run this the first time, and whenever you need migrations reset, e.g. if you're testing master after having tested a branch with new migrations

```bash
source dev-scripts/create-test-db.sh
```

```bash
./manage.py test
```


# Recommended VSCode extensions

- [python runtime](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [django template syntax support](https://marketplace.visualstudio.com/items?itemName=bibhasdn.django-html)
- [yaml syntax support](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

