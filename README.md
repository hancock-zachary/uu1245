# uu1245

Small Python client for the [SAM.gov Get Opportunities Public API](https://open.gsa.gov/api/get-opportunities-public-api/). It pulls recent federal contract opportunities and prints them to the console.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- A SAM.gov account and public API key (see below)

## 1. Clone the repo

```bash
git clone https://github.com/hancock-zachary/uu1245.git
```

```bash
cd uu1245
```

## 2. Install dependencies

With uv, this creates a `.venv` and installs everything pinned in `uv.lock`:

```bash
uv sync
```

Or with pip:

```bash
python -m venv .venv
```

```bash
pip install pandas python-dotenv requests
```

Activate the virtual environment first (`.venv\Scripts\activate` on Windows, `source .venv/bin/activate` on macOS/Linux).

## 3. Get a SAM.gov API key

1. Go to [SAM.gov](https://sam.gov) and click **Sign In**. SAM.gov uses [Login.gov](https://login.gov) for authentication, so create a Login.gov account if you don't already have one and finish its email and two-factor setup.
2. Once signed in, open your profile menu in the top right and choose **Profile**, then **Account Details**.
3. Scroll to the **Public API Key** section and enter your Login.gov password when prompted.
4. Click to generate the key, then copy it. You can return to this page to view it again.

A few things to know:

- Keys **expire every 90 days**. Come back to the same page to generate a new one when requests start failing with an authentication error.
- Personal accounts without a SAM.gov role get a low daily request limit. Keep `limit` high and the number of calls low while testing.

## 4. Add the key to `.env`

Copy the example file and paste your key after the `=`:

```bash
cp .env.example .env
```

```
SAM_GOV_API_KEY=your-key-here
```

`.env` is in `.gitignore`, so the key stays out of version control. Don't commit it.

## 5. Run it

```bash
uv run src/sam_api.py
```

This queries opportunities posted in the last 7 days and prints the total match count followed by the posted date and title of each result.

## Project layout

```
src/sam_api.py   System_For_Award_Management_API class and script entry point
data/            Output folder for collected data (SQLite export is planned)
docs/            SAM.gov Get Opportunities API reference (PDF)
.env.example     Template for the API key
```

## License

See [LICENSE](LICENSE).
