from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from datetime import date
import os

styles = getSampleStyleSheet()
title_style = ParagraphStyle('title', parent=styles['Title'], alignment=TA_CENTER, fontSize=18, spaceAfter=12)
h_style = ParagraphStyle('h', parent=styles['Heading2'], fontSize=12, spaceBefore=10, spaceAfter=6)
body_style = ParagraphStyle('body', parent=styles['BodyText'], fontSize=10, leading=13)
small_style = ParagraphStyle('small', parent=styles['BodyText'], fontSize=8, leading=10, textColor=colors.grey)

site_name = "Business-Fingerprints-Services-of-God"
site_url = "https://asputnik7network.github.io/Business-Fingerprints-Services-of-God/"
effective = "January 2026"

def build_one_pager(path):
    doc = SimpleDocTemplate(path, pagesize=LETTER, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
    story = []
    story.append(Paragraph("How Our Background Screening Support Works", title_style))
    story.append(Paragraph(f"{site_name} | {site_url}", ParagraphStyle('sub', parent=styles['BodyText'], alignment=TA_CENTER, fontSize=9, textColor=colors.grey)))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Service Summary", h_style))
    story.append(Paragraph(
        "We provide professional, compliance-aligned services supporting regulated programs, including certified LiveScan fingerprint data collection (in-person only), plus optional verification add-ons where authorized and requested.",
        body_style
    ))
    story.append(Paragraph("Key Compliance Principles", h_style))
    bullets = [
        "<b>In-person biometric collection only:</b> No fingerprint/biometric data is collected through this website.",
        "<b>Authorized workflows:</b> Data is captured using authorized LiveScan equipment and transmitted to the appropriate processing entity per the requesting program.",
        "<b>Data minimization:</b> We only collect administrative intake information necessary to schedule and deliver services.",
        "<b>Confidential handling:</b> We implement reasonable safeguards and follow applicable laws and agency requirements."
    ]
    story.append(Paragraph("<br/>".join([f"• {b}" for b in bullets]), body_style))
    story.append(Paragraph("Common Use Cases", h_style))
    story.append(Paragraph(
        "Applicants, employees, contractors, and volunteers serving children, seniors, individuals with disabilities, or other regulated populations; vendor onboarding; compliance readiness support.",
        body_style
    ))
    story.append(Paragraph("Service Request & Scheduling", h_style))
    story.append(Paragraph(
        "Use the website Request Services pathway to submit an inquiry or schedule an appointment. Service requests are confirmed upon eligibility verification and availability.",
        body_style
    ))
    story.append(Spacer(1, 10))
    t_data = [
        ["Policy Links (Website)", "Purpose"],
        ["Privacy Policy", "How we handle website and inquiry data"],
        ["Terms of Service", "Use of website and service conditions"],
        ["Accessibility Statement", "Accessibility commitment and contact"],
        ["Fingerprinting & Data Handling Disclosure", "Biometric handling and in-person collection only"]
    ]
    table = Table(t_data, colWidths=[2.6*inch, 3.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#111827")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 9),
        ('FONTSIZE', (0,1), (-1,-1), 9),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('BACKGROUND', (0,1), (-1,-1), colors.whitesmoke),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(table)
    story.append(Spacer(1, 10))
    story.append(Paragraph(f"Effective: {effective}. This one-page summary is informational and does not constitute legal advice.", small_style))
    doc.build(story)

def build_checklist(path):
    doc = SimpleDocTemplate(path, pagesize=LETTER, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
    story = []
    story.append(Paragraph("Compliance Readiness Checklist (Printable)", title_style))
    story.append(Paragraph(f"{site_name} | {site_url}", ParagraphStyle('sub2', parent=styles['BodyText'], alignment=TA_CENTER, fontSize=9, textColor=colors.grey)))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Use this checklist to prepare for regulated onboarding and screening requirements.", body_style))
    story.append(Spacer(1, 10))

    sections = {
        "Identity & Documentation": [
            "Valid government-issued photo ID available",
            "Correct ORI / agency code (if applicable)",
            "Employer / program instructions reviewed",
            "Legal name and DOB match supporting documents"
        ],
        "Appointment & Intake": [
            "Appointment requested/confirmed",
            "Contact information verified for follow-up",
            "Any required forms completed prior to arrival",
            "Payment method confirmed (if applicable)"
        ],
        "Data Handling & Consent": [
            "Understands fingerprints are collected in person only",
            "Reviewed Privacy Policy and Terms of Service",
            "Reviewed Fingerprinting & Data Handling Disclosure",
            "Consent provided as required by the requesting program"
        ],
        "Optional Verification Add-ons (as authorized)": [
            "Employment verification",
            "Education or GED verification",
            "Credential/certification verification",
            "County criminal/civil history (as requested)",
            "International searches (where applicable)"
        ]
    }

    for sec, items in sections.items():
        story.append(Paragraph(sec, h_style))
        rows = [["☐", it] for it in items]
        tbl = Table(rows, colWidths=[0.35*inch, 5.75*inch])
        tbl.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 0.25, colors.lightgrey),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('FONTSIZE', (0,0), (-1,-1), 10),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ]))
        story.append(tbl)
        story.append(Spacer(1, 10))

    story.append(Paragraph("Next Step: Request services via the website to confirm eligibility and scheduling.", body_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph(f"Effective: {effective}.", small_style))
    doc.build(story)

one_pager_path = "assets/pdf/Government-Ready_Screening-Service-Summary_One-Pager.pdf"
checklist_path = "assets/pdf/Compliance-Readiness-Checklist_Printable.pdf"

# Ensure the output directory exists
os.makedirs(os.path.dirname(one_pager_path), exist_ok=True)

build_one_pager(one_pager_path)
build_checklist(checklist_path)

print(f"Generated PDFs:")
print(f"  - {one_pager_path}")
print(f"  - {checklist_path}")
