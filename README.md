# procurement-responses
Business Services, Fingerprints of God (Service Provider. Advocating. AI Coaching and Consulting)

## Structure
/docs   (or /root)
│
├── index.md                (Home)
├── services.md             (Services)
├── compliance.md           (Compliance & Credentials)
├── who-we-serve.md         (Who We Serve)
├── request-services.md     (Request Services)
│
├── /assets
│   ├── /pdf
│   │   ├── capability-statement.pdf
│   │   ├── compliance-summary.pdf
│   │   ├── pricing-narrative.pdf
│   │   ├── Government-Ready_Screening-Service-Summary_One-Pager.pdf
│   │   └── Compliance-Readiness-Checklist_Printable.pdf
│   └── /css
│       └── styles.css
│
├── _config.yml             (if using Jekyll)
├── generate_pdfs.py        (PDF generation script)
├── requirements.txt        (Python dependencies)
└── README.md

## PDF Generation

This repository includes a Python script to generate compliance and service documentation PDFs.

### Requirements
- Python 3.7 or higher
- ReportLab library

### Installation
```bash
pip install -r requirements.txt
```

### Usage
```bash
python3 generate_pdfs.py
```

This will generate two PDF documents in the `assets/pdf/` directory:
- **Government-Ready_Screening-Service-Summary_One-Pager.pdf** - A one-page summary of background screening support services
- **Compliance-Readiness-Checklist_Printable.pdf** - A printable checklist for compliance readiness preparation
