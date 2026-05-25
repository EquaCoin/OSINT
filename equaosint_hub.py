import streamlit as st
import pandas as pd

st.set_page_config(page_title="EquaOSINT Hub", page_icon="🔍", layout="wide")
st.title("🔍 EquaOSINT Hub")
st.markdown("**Your personal launcher for the most performant free OSINT tools (2026)** — Marco's curated collection")

# Curated tools data (most performant free ones)
tools_data = {
    "Category": [
        "Framework", "Framework", "Framework", 
        "Username", "Username", "Email/Phone", "Email/Phone",
        "Domain/IP", "Domain/IP", "Domain/IP", "Domain/IP",
        "Threat Intel", "Threat Intel", "Threat Intel",
        "People Search", "People Search",
        "Image/Video", "Image/Video",
        "Scientific Research",
        "Environment",
        "Automation/CLI"
    ],
    "Tool Name": [
        "OSINT Framework", "SpiderFoot", "Recon-ng",
        "WhatsMyName", "Maigret", "Epieos", "Holehe",
        "Shodan", "Censys", "DNSDumpster", "theHarvester",
        "Have I Been Pwned", "VirusTotal", "AlienVault OTX",
        "FastPeopleSearch", "Lenso.ai",
        "ExifTool", "Google Earth Pro",
        "Sci-Bot.ru",
        "RadiaVerse",
        "SpiderFoot CLI / Recon-ng / theHarvester"
    ],
    "Description": [
        "Ultimate curated directory of 100s of free OSINT resources (best starting point)",
        "Automated OSINT recon with 200+ modules — self-hostable web UI, extremely fast",
        "Modular CLI framework for web recon (highly customizable)",
        "Best username checker across 500+ sites (lightning-fast)",
        "Collects full dossier on a username (social + leaks)",
        "EU-hosted email/phone reverse lookup (very accurate & privacy-friendly)",
        "Checks if email exists on 100+ sites via password-reset trick",
        "Internet-connected devices search engine (gold standard)",
        "Alternative to Shodan — strong on certificates & cloud assets",
        "Free domain recon & subdomain mapping (visual DNS map)",
        "Fast email + subdomain harvesting from public sources",
        "Check if email/phone appears in known breaches",
        "Multi-engine malware/URL scanner + reputation",
        "Open Threat Exchange — free IOC sharing & threat intel",
        "US people search (addresses, relatives, phones)",
        "Advanced reverse image & face search",
        "Metadata extractor (images/documents) — CLI gold standard",
        "Geolocation & historical satellite imagery verification",
        "Academic & scientific paper search engine (Russian + global sources, fast indexing)",
        "Real-time global environmental radiation monitoring map (crowdsourced + official sensors)",
        "Local CLI power tools (install once, run forever)"
    ],
    "Link": [
        "https://osintframework.com/",
        "https://www.spiderfoot.net/",
        "https://github.com/lanmaster53/recon-ng",
        "https://whatsmyname.app/",
        "https://github.com/soxoj/maigret",
        "https://epieos.com/",
        "https://github.com/megadose/holehe",
        "https://www.shodan.io/",
        "https://censys.io/",
        "https://dnsdumpster.com/",
        "https://github.com/laramies/theHarvester",
        "https://haveibeenpwned.com/",
        "https://www.virustotal.com/",
        "https://otx.alienvault.com/",
        "https://fastpeoplesearch.com/",
        "https://lenso.ai/",
        "https://exiftool.org/",
        "https://www.google.com/earth/versions/",
        "https://sci-bot.ru/",
        "https://map.radiaverse.com/#5.21/42.14/12.88",
        "https://github.com/smicallef/spiderfoot"
    ],
    "Why Performant": [
        "Single source for everything free & updated daily",
        "Automates 100s of queries in minutes; self-hosted = unlimited",
        "Battle-tested modular design used by pentesters worldwide",
        "Fastest & most complete username checker (2026)",
        "Deep social + leak aggregation in one run",
        "Privacy-first EU tool, excellent accuracy on European data",
        "Zero API key needed, works on any email",
        "Most comprehensive IoT/device database",
        "Strong certificate & cloud focus, generous free tier",
        "Instant visual subdomain map — no signup",
        "Passive recon king — pulls from Google, LinkedIn, etc.",
        "Authoritative breach database",
        "50+ AV engines + rich context",
        "Free IOC & threat feed used by professionals",
        "Quick US people recon (addresses/phones)",
        "Best free reverse image/face search 2026",
        "Industry standard for metadata forensics",
        "Historical imagery + measurement tools",
        "Fast academic search across Russian & international databases, no paywall",
        "Live radiation levels from official + citizen sensors worldwide — essential for environmental OSINT",
        "Run locally with no limits once installed"
    ],
    "Type": ["Web", "Self-hosted/Web", "CLI", "Web", "CLI", "Web", "CLI", "Web", "Web", "Web", "CLI", "Web", "Web", "Web", "Web", "Web", "CLI", "Desktop", "Web", "Web", "CLI"]
}

df = pd.DataFrame(tools_data)

# Sidebar filters
st.sidebar.header("Filters")
category_filter = st.sidebar.multiselect("Category", options=sorted(df["Category"].unique()), default=sorted(df["Category"].unique()))
type_filter = st.sidebar.multiselect("Type", options=sorted(df["Type"].unique()), default=sorted(df["Type"].unique()))

# Search
search_term = st.text_input("🔎 Search tools (name, description, or keyword)", "")

# Filter dataframe
filtered_df = df[
    (df["Category"].isin(category_filter)) &
    (df["Type"].isin(type_filter))
]

if search_term:
    mask = (
        filtered_df["Tool Name"].str.contains(search_term, case=False) |
        filtered_df["Description"].str.contains(search_term, case=False) |
        filtered_df["Why Performant"].str.contains(search_term, case=False)
    )
    filtered_df = filtered_df[mask]

# Display as beautiful cards
st.subheader(f"🚀 {len(filtered_df)} Performant Free OSINT Tools")

cols = st.columns(3)
for i, row in filtered_df.iterrows():
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**{row['Tool Name']}**")
            st.caption(row["Category"] + " • " + row["Type"])
            st.write(row["Description"])
            st.write(f"⭐ **Why performant:** {row['Why Performant']}")
            st.link_button("Open Tool →", row["Link"], use_container_width=True)

# Quick install commands for CLI tools
st.divider()
st.subheader("⚡ One-click local CLI install (recommended for power users)")
st.code("""
# SpiderFoot (full automation)
git clone https://github.com/smicallef/spiderfoot.git && cd spiderfoot && pip install -r requirements.txt && python sf.py

# theHarvester
pip install theHarvester

# Recon-ng
git clone https://github.com/lanmaster53/recon-ng.git && cd recon-ng && pip install -r REQUIREMENTS

# Maigret / Holehe
pip install maigret holehe
""", language="bash")

st.info("💡 Pro tip: Run SpiderFoot locally once → you get your own unlimited OSINT automation server.")

st.caption("Curated by Grok for Marco / EquaCoin • May 2026 • All tools are free or have strong free tiers • Use responsibly & ethically.")
