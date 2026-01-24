<div align="center">
  <img src="static/images/logo.png" alt="Envision Logo" width="120" height="120" style="border-radius: 20%;">
  
  # Envision
  ### Next-Gen AI Image Studio
  
  [![Django](https://img.shields.io/badge/Django-6.0.1-092e20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
  [![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-4.x-38bdf8?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
  [![Cloudinary](https://img.shields.io/badge/Cloudinary-AI_Powered-3448c5?style=for-the-badge&logo=cloudinary&logoColor=white)](https://cloudinary.com/)

**Envision** is a premium SaaS application designed for professional-grade image enhancement and manipulation. Powered by state-of-the-art AI neural networks, Envision allows you to upscale, transform, and engineer visual content with cinematic precision.

</div>

---

## ✨ Features

- 🖱️ **Interactive Comparison**: High-performance hero slider for "Before vs After" real-time visualization.
- 🚀 **Ultra Upscaling**: Transform low-resolution images into crystal-clear 4K visuals.
- 🖼️ **Background Studio**: Highly accurate background removal and extraction.
- 🪄 **Generative Fill**: Intelligently expand canvases or fill in missing image data.
- 📊 **Studio Dashboard**: Manage and track all your processed images in one place.
- 💎 **Credit System**: Flexible pay-as-you-go credit management for AI processing.
- 💳 **Paddle Integration**: Secure global payments and automated credit fulfillment.
- 🔍 **SEO Optimized**: Fully optimized with OG tags, Twitter Cards, JSON-LD, and automated sitemaps.
- 🌓 **Adaptive UI**: Premium glassmorphic design system with full Dark Mode support.

## 🛠️ Technology Stack

### Backend

- **Framework**: [Django 6.0.1](https://www.djangoproject.com/)
- **Image Processing**: [Cloudinary AI SDK](https://cloudinary.com/)
- **Payments**: [Paddle Python SDK](https://www.paddle.com/)
- **Environment Management**: `django-environ`
- **Database**: Local SQLite / Production-ready PostgreSQL (`dj-database-url`)

### Frontend

- **Engine**: [Tailwind CSS 4.x](https://tailwindcss.com/)
- **Components**: [daisyUI 5.x](https://daisyui.com/)
- **Typography**: Ubuntu (Google Fonts)
- **Design Pattern**: Glassmorphism, premium gradients, and micro-animations.
- **SEO & Social**: Meta Tags, Open Graph, Twitter Cards, and JSON-LD Structured Data.
- **Assets**: Professional logo, custom favicons, and commercial video mockups.

## 📦 Project Structure

- `core/`: Main configuration, settings, and root URL routing.
- `dj_cloudinary/`: Image models, Cloudinary integration logic, and AI transformation views.
- `payments/`: Credit purchasing logic, Paddle webhook handlers, and transaction tracking.
- `users/`: Custom user models and authentication flows (Signup/Login/Profile).
- `home/`: Public marketing pages (Hero, Features, Pricing, About).
- `templates/`: Comprehensive HTML structure using Django Template Language.
- `theme/`: Dedicated Tailwind CSS build environment.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Node.js (for Tailwind builds)
- Cloudinary Account
- Paddle Account (for payments)

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd envision
   ```

2. **Set up Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add:

   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   CLOUDINARY_CLOUD_NAME=your-cloud-name
   CLOUDINARY_API_KEY=your-api-key
   CLOUDINARY_API_SECRET=your-api-secret
   PADDLE_API_KEY=your-paddle-key
   PADDLE_WEBHOOK_SECRET=your-webhook-secret
   ```

5. **Run Migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Build Styles (Optional for development):**

   ```bash
   cd theme/static_src
   npm install
   npm run build
   ```

7. **Start Server:**

   ```bash
   python manage.py runserver
   ```

## 🧪 Testing

The project includes a comprehensive test suite covering AI transformations and payment flows.

```bash
python manage.py test dj_cloudinary payments
```

## 🚢 Deployment

Envision is configured for one-click deployment on **Railway**.

- Uses `whitenoise` for static asset serving.
- `dj_database_url` automatically detects production PostgreSQL.
- Ensure all `.env` keys are added to your Railway Variables.

---

Developed with ❤️ for creators by Talha Shahid Khan.
