import os

# Define the root directory for landing pages
landing_pages_dir = "aether-landing-pages/domains/"

# Define domain clusters
clusters = {
    "investigative_media": ["thegoverningconspiracy.com", "omniversal.news", "lyranwars.com"],
    "tech_web": ["omniversal.cloud", "omniversal.team", "omniversalaether.com"],
    "branding_music": ["hawkeyetherapper.com", "reincarnated2resist.com", "reincarnated.store"],
}

# Define the standard footer format
FOOTER_TEMPLATE = """<footer>
    <p>Explore More:</p>
    <ul>
        {links}
    </ul>
</footer>
"""

# Ensure all domains link to OmniversalMedia.net
GLOBAL_LINK = '<li><a href="https://OmniversalMedia.net">Visit Our Main Hub</a></li>'

# Function to get relevant links for each domain
def get_footer_links(domain):
    related_links = []
    for cluster, domains in clusters.items():
        if domain in domains:
            related_links.extend([d for d in domains if d != domain])

    # Format as HTML list items
    formatted_links = [f'<li><a href="https://{d}">{d}</a></li>' for d in related_links]
    formatted_links.append(GLOBAL_LINK)  # Always include OmniversalMedia.net

    return FOOTER_TEMPLATE.format(links="\n        ".join(formatted_links))

# Function to update index.html files
def update_footers():
    for domain in os.listdir(landing_pages_dir):
        index_file = os.path.join(landing_pages_dir, domain, "index.html")

        if os.path.exists(index_file):
            with open(index_file, "r") as f:
                content = f.readlines()

            # Check if footer exists
            footer_start = next((i for i, line in enumerate(content) if "<footer>" in line), None)
            footer_end = next((i for i, line in enumerate(content) if "</footer>" in line), None)

            # Get correct footer for this domain
            new_footer = get_footer_links(domain)

            if footer_start is not None and footer_end is not None:
                # Replace existing footer
                content[footer_start:footer_end+1] = [new_footer + "\n"]
            else:
                # Append footer at the end if not found
                content.append("\n" + new_footer)

            # Write back the updated file
            with open(index_file, "w") as f:
                f.writelines(content)

            print(f"✅ Updated footer for {domain}")

# Function to verify global assets exist
def verify_global_assets():
    assets_dir = "aether-landing-pages/global-assets/"
    required_files = ["logo.png", "background.jpg", "style.css"]

    missing_files = [f for f in required_files if not os.path.exists(os.path.join(assets_dir, f))]

    if missing_files:
        print(f"⚠️ Missing global assets: {', '.join(missing_files)}")
    else:
        print("✅ All global assets are present.")

if __name__ == "__main__":
    print("🔄 Running interlinking fix script...")
    update_footers()
    verify_global_assets()
    print("🚀 All fixes applied successfully!")
