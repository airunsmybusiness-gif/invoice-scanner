"""
InvoiceScan Pro - AI-Powered Invoice & Receipt Scanner
Extracts data from photos using Claude Vision, exports to Google Sheets
Built for Alberta oilfield operations - TicketDrop style
"""

import streamlit as st
import anthropic
import base64
import json
import re
from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional, List
import pandas as pd
from io import BytesIO

# ══════════════════════════════════════════════════════════════════════════════
# PYDANTIC MODEL FOR STRUCTURED OUTPUT
# ══════════════════════════════════════════════════════════════════════════════

class InvoiceData(BaseModel):
    """Structured invoice/receipt data model"""
    invoice_number: str = Field(default="N/A", description="Invoice or receipt number")
    company_name: str = Field(default="Unknown", description="Service provider/vendor name")
    date: str = Field(default="", description="Date in YYYY-MM-DD format")
    sold_to: str = Field(default="N/A", description="Customer/buyer name or company")
    description: str = Field(default="", description="Brief description of goods/services")
    total_amount: float = Field(default=0.0, description="Total amount as float")
    
    @validator('date', pre=True, always=True)
    def validate_date(cls, v):
        if not v:
            return datetime.now().strftime("%Y-%m-%d")
        # Try to parse and reformat various date formats
        for fmt in ["%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%B %d, %Y", "%b %d, %Y"]:
            try:
                return datetime.strptime(str(v), fmt).strftime("%Y-%m-%d")
            except:
                continue
        return v if v else datetime.now().strftime("%Y-%m-%d")
    
    @validator('total_amount', pre=True, always=True)
    def validate_amount(cls, v):
        if isinstance(v, (int, float)):
            return float(v)
        if isinstance(v, str):
            # Remove currency symbols and commas
            cleaned = re.sub(r'[^\d.]', '', v)
            try:
                return float(cleaned) if cleaned else 0.0
            except:
                return 0.0
        return 0.0


# ══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIG & CUSTOM CSS
# ══════════════════════════════════════════════════════════════════════════════

st.set_page_config(
    page_title="InvoiceScan Pro",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful, professional UI
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Root variables */
    :root {
        --primary: #0066FF;
        --primary-dark: #0052CC;
        --accent: #00D4AA;
        --bg-dark: #0A0E14;
        --bg-card: #141A22;
        --bg-elevated: #1A222D;
        --text-primary: #F4F7FA;
        --text-secondary: #8B9AAF;
        --border: #2A3544;
        --success: #00D4AA;
        --warning: #FFB020;
        --error: #FF4757;
    }
    
    /* Global styles */
    .stApp {
        background: linear-gradient(145deg, var(--bg-dark) 0%, #0F151D 50%, #0A0E14 100%);
        font-family: 'DM Sans', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, var(--bg-card) 0%, var(--bg-elevated) 100%);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 2rem 2.5rem;
        margin-bottom: 2rem;
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--primary), var(--accent));
    }
    
    .main-header h1 {
        font-size: 2.2rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.02em;
    }
    
    .main-header p {
        color: var(--text-secondary);
        font-size: 1rem;
        margin: 0;
    }
    
    .badge {
        display: inline-block;
        background: linear-gradient(135deg, var(--primary), var(--accent));
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-left: 0.75rem;
        vertical-align: middle;
    }
    
    /* Card styling */
    .card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .card-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin-bottom: 1rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid var(--border);
    }
    
    .card-header h3 {
        color: var(--text-primary);
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0;
    }
    
    .card-icon {
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, var(--primary), var(--accent));
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem;
    }
    
    /* Upload zone */
    .upload-zone {
        border: 2px dashed var(--border);
        border-radius: 12px;
        padding: 3rem 2rem;
        text-align: center;
        background: var(--bg-elevated);
        transition: all 0.3s ease;
    }
    
    .upload-zone:hover {
        border-color: var(--primary);
        background: rgba(0, 102, 255, 0.05);
    }
    
    .upload-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    /* Status indicators */
    .status-success {
        background: rgba(0, 212, 170, 0.1);
        border: 1px solid var(--success);
        color: var(--success);
        padding: 0.75rem 1rem;
        border-radius: 8px;
        font-weight: 500;
    }
    
    .status-error {
        background: rgba(255, 71, 87, 0.1);
        border: 1px solid var(--error);
        color: var(--error);
        padding: 0.75rem 1rem;
        border-radius: 8px;
        font-weight: 500;
    }
    
    .status-info {
        background: rgba(0, 102, 255, 0.1);
        border: 1px solid var(--primary);
        color: var(--primary);
        padding: 0.75rem 1rem;
        border-radius: 8px;
        font-weight: 500;
    }
    
    /* Data table styling */
    .dataframe {
        font-family: 'JetBrains Mono', monospace !important;
        font-size: 0.85rem !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary), var(--primary-dark)) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-family: 'DM Sans', sans-serif !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(0, 102, 255, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(0, 102, 255, 0.4) !important;
    }
    
    /* Secondary button */
    .secondary-btn > button {
        background: var(--bg-elevated) !important;
        border: 1px solid var(--border) !important;
        box-shadow: none !important;
    }
    
    .secondary-btn > button:hover {
        border-color: var(--primary) !important;
        background: rgba(0, 102, 255, 0.1) !important;
    }
    
    /* Input styling */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        background: var(--bg-elevated) !important;
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
        color: var(--text-primary) !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 2px rgba(0, 102, 255, 0.2) !important;
    }
    
    /* Stats card */
    .stat-card {
        background: linear-gradient(135deg, var(--bg-card), var(--bg-elevated));
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
    }
    
    .stat-value {
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--accent);
        font-family: 'JetBrains Mono', monospace;
    }
    
    .stat-label {
        color: var(--text-secondary);
        font-size: 0.85rem;
        margin-top: 0.25rem;
    }
    
    /* Spinner override */
    .stSpinner > div {
        border-color: var(--primary) transparent transparent transparent !important;
    }
    
    /* File uploader */
    .stFileUploader > div {
        background: var(--bg-elevated) !important;
        border: 2px dashed var(--border) !important;
        border-radius: 12px !important;
    }
    
    .stFileUploader > div:hover {
        border-color: var(--primary) !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: var(--bg-elevated) !important;
        border-radius: 8px !important;
    }
    
    /* Data editor */
    [data-testid="stDataEditor"] {
        border: 1px solid var(--border) !important;
        border-radius: 8px !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: var(--text-secondary);
        font-size: 0.85rem;
        border-top: 1px solid var(--border);
        margin-top: 3rem;
    }
    
    .footer a {
        color: var(--primary);
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# CLAUDE VISION EXTRACTION
# ══════════════════════════════════════════════════════════════════════════════

EXTRACTION_PROMPT = """You are an expert invoice and receipt data extractor. Analyze this image carefully and extract the following information.

INSTRUCTIONS:
1. Look for ANY text that indicates invoice/receipt number (Invoice #, Receipt #, Order #, Reference #, etc.)
2. Find the company/vendor name (usually at the top, the one PROVIDING the service/goods)
3. Extract the date - convert to YYYY-MM-DD format
4. Find who it was sold to / billed to / customer name
5. Summarize what was purchased (goods/services) in a brief description
6. Find the TOTAL amount due (look for "Total", "Amount Due", "Grand Total", etc.)

Handle messy, crumpled, or partially visible receipts by making best reasonable guesses.
If a field is truly unreadable or missing, use "N/A" for text fields and 0.0 for amounts.

RESPOND ONLY WITH VALID JSON in this exact format:
{
    "invoice_number": "string",
    "company_name": "string",
    "date": "YYYY-MM-DD",
    "sold_to": "string",
    "description": "string",
    "total_amount": 0.00
}

Extract now:"""


def encode_image(uploaded_file) -> tuple[str, str]:
    """Encode uploaded image to base64 and determine media type"""
    bytes_data = uploaded_file.getvalue()
    base64_image = base64.standard_b64encode(bytes_data).decode("utf-8")
    
    # Determine media type
    file_type = uploaded_file.type
    if file_type in ["image/jpeg", "image/jpg"]:
        media_type = "image/jpeg"
    elif file_type == "image/png":
        media_type = "image/png"
    elif file_type == "image/gif":
        media_type = "image/gif"
    elif file_type == "image/webp":
        media_type = "image/webp"
    else:
        media_type = "image/jpeg"  # Default fallback
    
    return base64_image, media_type


def extract_invoice_data(uploaded_file, api_key: str) -> InvoiceData:
    """Use Claude Vision to extract invoice data from image"""
    
    base64_image, media_type = encode_image(uploaded_file)
    
    client = anthropic.Anthropic(api_key=api_key)
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": media_type,
                            "data": base64_image,
                        },
                    },
                    {
                        "type": "text",
                        "text": EXTRACTION_PROMPT
                    }
                ],
            }
        ],
    )
    
    # Parse response
    response_text = message.content[0].text.strip()
    
    # Clean up response - remove markdown code blocks if present
    if response_text.startswith("```"):
        response_text = re.sub(r'^```json?\n?', '', response_text)
        response_text = re.sub(r'\n?```$', '', response_text)
    
    # Parse JSON
    try:
        data = json.loads(response_text)
        return InvoiceData(**data)
    except json.JSONDecodeError as e:
        st.error(f"Failed to parse Claude response: {e}")
        st.code(response_text)
        return InvoiceData()


# ══════════════════════════════════════════════════════════════════════════════
# GOOGLE SHEETS INTEGRATION
# ══════════════════════════════════════════════════════════════════════════════

def append_to_sheets(df: pd.DataFrame, sheet_url: str) -> bool:
    """Append data to Google Sheet using gspread"""
    try:
        import gspread
        from google.oauth2.service_account import Credentials
        
        # Get credentials from secrets
        if "gcp_service_account" not in st.secrets:
            st.error("Google Cloud credentials not configured in secrets!")
            return False
        
        creds_dict = dict(st.secrets["gcp_service_account"])
        
        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        
        credentials = Credentials.from_service_account_info(creds_dict, scopes=scopes)
        gc = gspread.authorize(credentials)
        
        # Extract sheet ID from URL
        sheet_id_match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', sheet_url)
        if not sheet_id_match:
            st.error("Invalid Google Sheet URL format!")
            return False
        
        sheet_id = sheet_id_match.group(1)
        
        # Open sheet and append
        spreadsheet = gc.open_by_key(sheet_id)
        worksheet = spreadsheet.sheet1
        
        # Check if headers exist
        existing_data = worksheet.get_all_values()
        if not existing_data:
            # Add headers
            headers = ["invoice_number", "company_name", "date", "sold_to", "description", "total_amount", "extracted_at"]
            worksheet.append_row(headers)
        
        # Append each row
        for _, row in df.iterrows():
            row_data = [
                str(row.get('invoice_number', 'N/A')),
                str(row.get('company_name', 'Unknown')),
                str(row.get('date', '')),
                str(row.get('sold_to', 'N/A')),
                str(row.get('description', '')),
                float(row.get('total_amount', 0.0)),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ]
            worksheet.append_row(row_data)
        
        return True
        
    except Exception as e:
        st.error(f"Google Sheets error: {str(e)}")
        return False


# ══════════════════════════════════════════════════════════════════════════════
# MAIN APPLICATION
# ══════════════════════════════════════════════════════════════════════════════

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>📄 InvoiceScan Pro <span class="badge">AI Powered</span></h1>
        <p>Extract invoice & receipt data instantly using Claude Vision • Export to Google Sheets</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize session state
    if 'extracted_data' not in st.session_state:
        st.session_state.extracted_data = []
    if 'processing' not in st.session_state:
        st.session_state.processing = False
    
    # Sidebar for settings
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        
        # API Key input (check secrets first)
        if "ANTHROPIC_API_KEY" in st.secrets:
            api_key = st.secrets["ANTHROPIC_API_KEY"]
            st.markdown('<div class="status-success">✓ API Key configured</div>', unsafe_allow_html=True)
        else:
            api_key = st.text_input(
                "Claude API Key",
                type="password",
                help="Get your free API key at console.anthropic.com"
            )
        
        st.markdown("---")
        
        # Google Sheet URL
        sheet_url = st.text_input(
            "Google Sheet URL",
            placeholder="https://docs.google.com/spreadsheets/d/...",
            help="Paste your Google Sheet URL here"
        )
        
        st.markdown("---")
        
        st.markdown("""
        ### 📊 Free Tier Limits
        - **Claude API**: 50 requests/min
        - **Google Sheets**: Unlimited writes
        - **Streamlit Cloud**: Free hosting
        """)
    
    # Main content area
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <div class="card-icon">📤</div>
                <h3>Upload Invoices</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_files = st.file_uploader(
            "Drop invoice/receipt images here",
            type=["jpg", "jpeg", "png", "gif", "webp"],
            accept_multiple_files=True,
            help="Supports JPG, PNG, GIF, WebP - messy receipts OK!"
        )
        
        if uploaded_files:
            st.markdown(f"**{len(uploaded_files)} file(s) selected**")
            
            # Preview thumbnails
            preview_cols = st.columns(min(len(uploaded_files), 4))
            for idx, file in enumerate(uploaded_files[:4]):
                with preview_cols[idx % 4]:
                    st.image(file, width=150, caption=file.name[:15] + "...")
        
        # Extract button
        if uploaded_files and api_key:
            if st.button("🔍 Extract Data", use_container_width=True):
                st.session_state.processing = True
                st.session_state.extracted_data = []
                
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                for idx, file in enumerate(uploaded_files):
                    status_text.markdown(f'<div class="status-info">Processing: {file.name}</div>', unsafe_allow_html=True)
                    
                    try:
                        extracted = extract_invoice_data(file, api_key)
                        st.session_state.extracted_data.append({
                            'filename': file.name,
                            'invoice_number': extracted.invoice_number,
                            'company_name': extracted.company_name,
                            'date': extracted.date,
                            'sold_to': extracted.sold_to,
                            'description': extracted.description,
                            'total_amount': extracted.total_amount
                        })
                    except Exception as e:
                        st.error(f"Error processing {file.name}: {str(e)}")
                    
                    progress_bar.progress((idx + 1) / len(uploaded_files))
                
                status_text.markdown('<div class="status-success">✓ Extraction complete!</div>', unsafe_allow_html=True)
                st.session_state.processing = False
        
        elif not api_key:
            st.warning("⚠️ Please configure your Claude API key in the sidebar")
    
    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-header">
                <div class="card-icon">📋</div>
                <h3>Extracted Data</h3>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.extracted_data:
            # Create editable dataframe
            df = pd.DataFrame(st.session_state.extracted_data)
            
            # Stats row
            stat_cols = st.columns(3)
            with stat_cols[0]:
                st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-value">{len(df)}</div>
                    <div class="stat-label">Invoices</div>
                </div>
                """, unsafe_allow_html=True)
            with stat_cols[1]:
                st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-value">${df['total_amount'].sum():,.2f}</div>
                    <div class="stat-label">Total Amount</div>
                </div>
                """, unsafe_allow_html=True)
            with stat_cols[2]:
                st.markdown(f"""
                <div class="stat-card">
                    <div class="stat-value">{df['company_name'].nunique()}</div>
                    <div class="stat-label">Vendors</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Editable data table
            edited_df = st.data_editor(
                df.drop(columns=['filename']),
                use_container_width=True,
                num_rows="dynamic",
                column_config={
                    "invoice_number": st.column_config.TextColumn("Invoice #", width="small"),
                    "company_name": st.column_config.TextColumn("Company", width="medium"),
                    "date": st.column_config.TextColumn("Date", width="small"),
                    "sold_to": st.column_config.TextColumn("Sold To", width="medium"),
                    "description": st.column_config.TextColumn("Description", width="large"),
                    "total_amount": st.column_config.NumberColumn("Amount", format="$%.2f", width="small"),
                }
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Action buttons
            btn_col1, btn_col2, btn_col3 = st.columns(3)
            
            with btn_col1:
                if sheet_url:
                    if st.button("📊 Export to Sheets", use_container_width=True):
                        with st.spinner("Exporting..."):
                            if append_to_sheets(edited_df, sheet_url):
                                st.success("✓ Data exported to Google Sheets!")
                            else:
                                st.error("Export failed - check your Sheet URL and credentials")
                else:
                    st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
                    st.button("📊 Export to Sheets", disabled=True, use_container_width=True, help="Configure Sheet URL in sidebar")
                    st.markdown('</div>', unsafe_allow_html=True)
            
            with btn_col2:
                csv_data = edited_df.to_csv(index=False)
                st.download_button(
                    "📥 Download CSV",
                    csv_data,
                    "invoices_export.csv",
                    "text/csv",
                    use_container_width=True
                )
            
            with btn_col3:
                if st.button("🗑️ Clear All", use_container_width=True):
                    st.session_state.extracted_data = []
                    st.rerun()
        
        else:
            st.markdown("""
            <div style="text-align: center; padding: 3rem; color: var(--text-secondary);">
                <div style="font-size: 3rem; margin-bottom: 1rem;">📄</div>
                <p>Upload invoices and click <strong>Extract Data</strong><br>to see results here</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Demo/Test section
    with st.expander("🧪 Test with Sample Data"):
        st.markdown("Don't have an invoice handy? Test the extraction with simulated data:")
        
        if st.button("Generate Sample Invoice Data"):
            sample_data = {
                'filename': 'sample_invoice.jpg',
                'invoice_number': 'INV-2024-0847',
                'company_name': 'Northern Energy Services Ltd.',
                'date': '2024-01-15',
                'sold_to': "Rick's Oilfield Hauling Ltd.",
                'description': 'Crude oil transport - 3 loads, Water hauling - 2 loads, Equipment rental',
                'total_amount': 4875.50
            }
            st.session_state.extracted_data.append(sample_data)
            st.rerun()
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>Built with ❤️ for Alberta Oilfield Operations</p>
        <p>Powered by <a href="https://anthropic.com" target="_blank">Claude AI</a> • 
        <a href="https://streamlit.io" target="_blank">Streamlit</a> • 
        <a href="https://docs.google.com/spreadsheets" target="_blank">Google Sheets</a></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
