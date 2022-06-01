# Positron - Flask Deployment made easy

Using Positron.py, you can deploy your Flask Apps to Desktop-ready Apps in a matter of minutes!

## Getting started with Positron

### Simple (Debug) Apps

Create a File in the same Directory as the Flask App, with the following Content:

```py
from positron import create_debug_app
from myapp import app

create_debug_app({
    "flask_address":"127.0.0.1",
    "flask_app":app,
    "name":"My App"
})
```

### Advanced Distributables

Create a File in the same Directory as the Flask App, with the following Content:

```py
from positron import freeze
from myapp import app

freeze("path/to/main/app.py", "output_dir", {
    "flask_address":"127.0.0.1",
    "flask_app":app,
    "name":"My App"
})
```

Create a File called `package.json` with this Content:

```json
{
    "entrypoint": "app filename (no .py)",
    "flask_host":"127.0.0.1",
    "name":"My App"
}
```

and run the Py File