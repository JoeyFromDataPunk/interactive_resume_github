import streamlit as st

# Create two columns
col1, col2 = st.columns([1, 4])  # Adjust ratio as needed

# Left column: Image
with col1:
    st.write("")
    st.image("https://raw.githubusercontent.com/JoeyFromDataPunk/interactive_resume_github/main/interactive_resume/jb_headshot.jpg", width=150)

# Title and subtitle
with col2:
    st.title("Joseph Boyle")
    st.subheader("Data Visualization | GIS Specialist | Python Developer")
    # Contact
    st.markdown("[Email](mailto:joey@datapunk.me) | [LinkedIn](https://linkedin.com/in/rjosephboyle) | [Website](https://datapunk.me)")

# Page setup
st.set_page_config(page_title="Interactive Resume", layout="centered")

# Intro/About
st.markdown("""
Hi! I'm Joseph, a data science professional with expertise in Python, SQL, GIS, and Tableau.  
I am currently pursuing a B.S. in Data Science at the University of Maryland. I have over 13 years of experience in analytics, visualization, and operations working for Fortune 50 companies.
""")

# Link to source code
st.markdown("""
This interactive resume was built using **Python** and [Streamlit](https://streamlit.io/).

[View the source code on GitHub](https://github.com/JoeyFromDataPunk/interactive_resume_github/blob/main/interactive_resume/resume_app.py)
""")

# --- Work experience ---
st.divider()
st.subheader("Work Experience")
st.markdown("""
            #### DATA ANALYST 4
###### Comcast NBC Universal | 2023-2025
""")

st.write("")  # adds a vertical space

st.markdown("""
• Maintained and audited national broadband infrastructure data sets and shapefiles used for expansion planning and
government grant applications.

• Utilized SQL-based models to blend proprietary data with government data sets from Census Bureau and FCC to
analyze population density in areas underserved by broadband providers.

• Contributed to internal CRM and data pipeline processes, uploading validated partner and location data for field
sales teams.
            
• Optimized SQL queries to efficiently handle larger datasets, ensuring seamless Tableau performance without
overloading servers or causing slowdowns.
            
• Supported Central Division's Network Expansion and Hyper Local teams with ad hoc reporting and geospatial
analysis, utilizing Tableau, SQL, ArcGIS, Python.
            
• Automated the processing of building permit data, reducing divisional analyst workload and enhancing reporting
accuracy.
            
• Wrote and maintained Central Division Network Expansion process documentation in Confluence.

""")
st.write("")
st.write("")
st.write("")
st.markdown("""
            #### BI ANALYST II / CONSULTANT – COMCAST BUSINESS
###### Pyramid Consulting | 2022-2023
""")
st.write("")
st.markdown("""
• Led geospatial analysis to identify broadband gaps using ArcGIS, SQL, Python tools, supporting state and federal
grant applications for network expansion.
            
• Developed geospatial analysis that secured over $170M in broadband infrastructure grants through Florida and
Georgia government.
            
• Conducted desk research and QA reviews of public permit data for commercial construction projects.
            
• Developed and maintained geographic shapefiles and metadata in ArcGIS for network expansion projects,
integrating marketing data through SQL for enhanced analysis.

""")
st.write("")
st.write("")
st.write("")
st.markdown("""
            #### BUSINESS INTELLIGENCE ANALYST – TEAM LEAD
###### Apple Inc | 2018-2022
""")
st.write("")
st.markdown("""
• Spearheaded data analysis and reporting initiatives, resulting in $99M in cost savings by reducing vendor
chargebacks due to shipping issues; received Apple’s operational excellence award for this achievement.
            
• Collaborated with cross-functional project teams in Ireland and Singapore to optimize shipment management
worldwide, leveraging Tableau, SAP BusinessObjects, and Excel to drive actionable insights.
            
• Led training on advanced BusinessObjects techniques for 400+ global attendees, improving analytics adoption
across international teams.

""")
st.write("")
st.write("")
st.write("")
st.markdown("""
            #### BUSINESS SUPPORT SPECIALIST
###### Apple Inc | 2012-2018
""")
st.write("")
st.markdown("""
• Conducted statistical analysis and built Tableau reports on returns data, identifying top drivers of product returns and
recommending process improvements.

""")

# --- Educational Experience ---
st.write("")
st.divider()
st.subheader("Education")
st.markdown("""
            #### UNIVERSITY OF MARYLAND
###### Adelphi, MD | 2024-Present
""")

st.write("")  

st.markdown("""
• Bachelor's in Data Science - Expected 2026

• Certification in Artificial Intelligence Foundations - Completed 2025

• Dean's List
""")
st.write("")
st.write("")
st.write("")

st.markdown("""
            #### GENERAL ASSEMBLY TECHNICAL SCHOOL
###### Austin, TX | 2021
""")

st.write("")  

st.markdown("""
• Certification in Data Analytics

• Tableau, SQL, Advanced Excel
""")

# --- Create two columns for skills ---

st.write("")

st.divider()
st.subheader("Skills")

st.write("")  # adds a vertical space

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
            ###### Software Skills
""")
    st.write("")
    st.markdown("""
SQL (SSMS, Postgres, MySQL, Teradata, Trino), Tableau, Power BI, Geographic Information Systems (GIS: QGIS, AEGIS, ArcGIS),
SAP BusinessObjects, Microsoft Office Suite, Google Suite, Mac and Windows platforms, Python (pandas, NumPy, matplotlib,
geopandas, seaborn, scikit-learn, streamlit)
            
Advanced Excel skills (INDEX/MATCH, lookups, arrays, macros, scripting, pivot tables) and cloud-based spreadsheet tools such as
Smartsheet, Google Sheets, Numbers, Quip
            
""")

with col2:
    st.markdown("""
            ###### General Skills
""")
    st.write("")
    st.markdown("""
            
• Business Requirements Gathering          
• Cross-Functional/Stakeholder Collaboration            
• Public Speaking/Presentation
• Shipping/Logistics/Supply Chain           
• Product Roadmaps/Process Improvement          
• KPI Reporting
            
""")
st.write("")
st.write("")

# --- Download Resume Button ---
# this allows the code to pull the local file if I am testing the code
# once the code is deployed it can't access the local file
# so this tries to find the local file, and if not available pulls it from GitHub
import os

pdf_path = "interactive_resume/Joseph_Boyle_Resume.pdf"
if not os.path.exists(pdf_path):
    pdf_path = "Joseph_Boyle_Resume.pdf"  # fallback for local testing

with open(pdf_path, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📄 Download PDF Resume",
    data=PDFbyte,
    file_name="Joseph_Boyle_Resume.pdf",
    mime="application/pdf"
)