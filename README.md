# Omniversal Aether - Cloudflare Pages Deployment

## 📜 Overview
This repository hosts the "Coming Soon" landing pages for Omniversal Aether and its network of domains.

## 🚀 Features
- Fully **static HTML/CSS** optimized for Cloudflare Pages
- **SEO-optimized metadata** (title, description, OpenGraph)
- **Fast global CDN** for near-instant loading
- **Modular design** with a global  for all pages

## 📂 Project Structure
```
aether-landing-pages/
├── global-assets/  # Shared assets (logos, images, stylesheets)
│   ├── logo.png
│   ├── background.jpg
│   ├── style.css
├── domains/        # Each domain gets its own directory
│   ├── omniversal.cloud/
│   │   ├── index.html
│   ├── omniversal.news/
│   │   ├── index.html
│   ├── lyranwars.com/
│   │   ├── index.html
├── config/
│   ├── domains.txt # List of all domains
```

## 🌍 Cloudflare Pages Deployment
To deploy:
1. Connect this repo to **Cloudflare Pages**.
2. Set **each domain folder as a separate build output**.
3. Assign **custom domains** via **Cloudflare DNS**.

