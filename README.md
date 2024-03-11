# Setup and usage instructions
First create the virtual environment and install the package:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

Then copy the `.env.example` file to `.env` and fill in the necessary values.

```bash
cp .env.example .env
```

Note that the OpenAI token you supply will need to have money added to it in
order to use the API. I suggest spending around $10 to get started.

Then you can use the package as follows:

```bash
python main.py
```

Feel free to update the ideal and generated values with your own code examples.