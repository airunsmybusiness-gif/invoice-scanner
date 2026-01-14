# 📄 InvoiceScan Pro

**AI-Powered Invoice & Receipt Scanner for Oilfield Operations**

Extract data from invoice/receipt photos using Claude Vision → Preview & Edit → Export to Google Sheets

100% FREE to run (no paid tiers required)

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- 📸 **Upload multiple invoices** - JPG, PNG, GIF, WebP supported
- 🤖 **AI extraction** - Claude Vision handles messy receipts
- ✏️ **Editable preview** - Review and correct before export
- 📊 **Google Sheets export** - One-click append to your sheet
- 📥 **CSV download** - Always have a backup
- 🎨 **Beautiful UI** - Professional dark theme

---

## 🚀 BABY-STEP SETUP (15 Steps)

### Part A: Get Your Claude API Key (FREE)

**Step 1:** Go to https://console.anthropic.com

**Step 2:** Sign up or log in (free account)

**Step 3:** Click "API Keys" in the left sidebar

**Step 4:** Click "Create Key" → Name it "InvoiceScan"

**Step 5:** Copy the key (starts with `sk-ant-...`) → Save it somewhere safe!

> 💡 **Free Tier:** 50 requests/minute, $5 free credits to start

---

### Part B: Set Up Google Sheets Export (FREE - Optional)

**Step 6:** Go to https://console.cloud.google.com

**Step 7:** Create new project → Name: "InvoiceScan"

**Step 8:** Search "Google Sheets API" → Click → Enable

**Step 9:** Search "Google Drive API" → Click → Enable

**Step 10:** Go to "IAM & Admin" → "Service Accounts" → Create Service Account
- Name: "invoicescan-sheets"
- Click "Create and Continue" → Skip optional steps → Done

**Step 11:** Click on your new service account → "Keys" tab → "Add Key" → "Create new key" → JSON → Download

**Step 12:** Create a Google Sheet → Share it with the service account email
- (Email looks like: `invoicescan-sheets@your-project.iam.gserviceaccount.com`)
- Give it "Editor" access

---

### Part C: Run Locally (Mac/VS Code/Terminal)

**Step 13:** Open Terminal and run:

```bash
# Create project folder
mkdir invoice_scanner
cd invoice_scanner

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install streamlit anthropic pandas pydantic gspread google-auth
```

**Step 14:** Create secrets file:

```bash
mkdir -p .streamlit
nano .streamlit/secrets.toml
```

Paste this (replace with your actual values):

```toml
ANTHROPIC_API_KEY = "sk-ant-api03-YOUR-KEY-HERE"

[gcp_service_account]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-private-key-id"
private_key = "-----BEGIN PRIVATE KEY-----\nYOUR_KEY\n-----END PRIVATE KEY-----\n"
client_email = "your-email@your-project.iam.gserviceaccount.com"
client_id = "123456789"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/your-email"
```

Save: `Ctrl+O`, `Enter`, `Ctrl+X`

**Step 15:** Run the app:

```bash
streamlit run invoice_scanner.py
```

🎉 **Open http://localhost:8501 in your browser!**

---

## 🌐 Deploy to Streamlit Cloud (FREE)

1. Push your code to GitHub (public repo)
2. Go to https://share.streamlit.io
3. Click "New app" → Connect your GitHub repo
4. Set main file: `invoice_scanner.py`
5. Go to "Advanced settings" → "Secrets"
6. Paste your `secrets.toml` content
7. Click "Deploy"

🎉 **Your app is live at `https://your-app.streamlit.app`**

---

## 📊 Free Tier Limits (Confirmed)

| Service | Free Limit | Notes |
|---------|-----------|-------|
| **Claude API** | 50 RPM | $5 free credits |
| **Google Sheets** | Unlimited | No write limits |
| **Streamlit Cloud** | 1GB RAM | Public apps free |

---

## 🔧 Extracted Data Fields

| Field | Description | Example |
|-------|-------------|---------|
| `invoice_number` | Invoice/receipt # | INV-2024-0847 |
| `company_name` | Vendor/provider | Northern Energy Services |
| `date` | YYYY-MM-DD format | 2024-01-15 |
| `sold_to` | Customer/buyer | Rick's Oilfield Hauling |
| `description` | Goods/services | Crude oil transport - 3 loads |
| `total_amount` | Total as float | 4875.50 |

---

## 🛠️ Troubleshooting

**"API Key not configured"**
- Add key to `.streamlit/secrets.toml` or paste in sidebar

**"Google Sheets error"**
- Ensure you shared the Sheet with your service account email
- Check that both Sheets API and Drive API are enabled

**"Rate limit exceeded"**
- Wait 1 minute (free tier: 50 requests/min)
- Process fewer images at once

---

## 📁 Project Structure

```
invoice_scanner/
├── invoice_scanner.py      # Main Streamlit app
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .streamlit/
│   └── secrets.toml.example  # Secrets template
└── README.md              # This file
```

---

## 🤝 Built For

**Alberta Oilfield Operations** - TicketDrop style SaaS

- Rick's Oilfield Hauling Ltd.
- And any company tired of manual invoice entry!

---

## 📄 License

MIT License - Use freely, modify as needed.

---

**Made with ❤️ using Claude AI + Streamlit**
