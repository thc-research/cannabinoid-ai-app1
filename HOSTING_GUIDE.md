
# 🚀 HOSTING GUIDE: Cannabinoid Extraction AI App
## Free & Low-Cost Options for Your Python Streamlit App

---

## 🎯 RECOMMENDED: 3 Best Free Options

### **OPTION 1: Streamlit Community Cloud** ⭐ EASIEST
**Cost:** FREE forever | **Setup:** 5 minutes | **Best for:** Quick deployment

**How to Deploy:**

```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/cannabinoid-ai-app.git
git push -u origin main

# 2. Go to streamlit.io/cloud
# 3. Sign in with GitHub
# 4. Click "Create app"
# 5. Select your repo
# 6. Set main file to: app.py
# 7. Click Deploy! 🎉
```

**Your URL:** `https://yourusername-cannabinoid-ai-app.streamlit.app`

**Pros:**
- ✅ Built specifically for Streamlit
- ✅ One-click deployment
- ✅ Automatic updates on git push
- ✅ Custom domain support
- ✅ No server management

**Cons:**
- ❌ Requires public GitHub repo
- ❌ 1 GB RAM limit
- ❌ Sleeps after inactivity (wakes in ~10 sec)

---

### **OPTION 2: Render** ⭐ MOST FLEXIBLE
**Cost:** FREE tier | **Setup:** 10 minutes | **Best for:** Production

**How to Deploy:**

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New" → "Web Service"
4. Connect your GitHub repo
5. Configure:
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
   - **Plan:** Free
6. Click "Create Web Service"

**Your URL:** `https://cannabinoid-ai-app.onrender.com`

**Pros:**
- ✅ Supports private repos
- ✅ PostgreSQL database included
- ✅ Custom domains with SSL
- ✅ Great performance

**Cons:**
- ❌ Spins down after 15 min inactivity
- ❌ 512 MB RAM on free tier

---

### **OPTION 3: PythonAnywhere**
**Cost:** FREE tier | **Setup:** 30 minutes | **Best for:** Learning

**How to Deploy:**

1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Open Bash console
3. Clone your repo
4. Set up virtual environment
5. Configure WSGI file
6. Reload web app

**Pros:**
- ✅ Designed for Python
- ✅ Always-on (no sleep)
- ✅ MySQL database included
- ✅ Good for learning

**Cons:**
- ❌ Limited storage (512 MB)
- ❌ Daily CPU quota
- ❌ No custom domains on free tier

---

## 🖥️ CPANEL/SHARED HOSTING?

### **Short Answer: NOT RECOMMENDED**

**Why it's difficult:**
- Streamlit requires special setup for WSGI
- Most shared hosting doesn't support Streamlit natively
- Complex configuration needed
- Better free alternatives exist

**If you MUST use cPanel:**

Requirements:
- Python support ("Setup Python App" feature)
- SSH access
- WSGI/Passenger support
- Not ASGI (no real-time features)

**Supported hosts:**
- ✅ Namecheap (Business/Pro plans)
- ✅ InMotion Hosting
- ✅ A2 Hosting
- ❌ Basic shared hosting (usually no Python)

**Better approach:** Use a VPS ($5-6/month) instead of shared hosting.

---

## 📊 COMPARISON

| Feature | Streamlit Cloud | Render | PythonAnywhere | cPanel |
|---------|----------------|--------|----------------|--------|
| **Cost** | FREE | FREE | FREE | $5-20 |
| **Difficulty** | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Custom Domain** | ✅ | ✅ | ❌ | ✅ |
| **Always On** | ✅ | ❌ | ✅ | ✅ |
| **Best For** | Quick start | Production | Learning | Existing sites |
| **Setup Time** | 5 min | 10 min | 30 min | 1+ hour |

---

## 🎯 MY RECOMMENDATION FOR YOU

### **Phase 1: Start Free (Now)**
**Use Streamlit Community Cloud**
- Easiest deployment
- Built for Streamlit
- Perfect for demonstration
- No credit card needed

### **Phase 2: Scale Up (Later)**
**Upgrade to Render** ($7/month)
- Always-on (no sleep)
- Private repo support
- Better for production
- Custom domain

### **Phase 3: Full Control (Future)**
**DigitalOcean VPS** ($6/month)
- Complete server control
- Best performance
- Run multiple apps
- Professional solution

---

## 🚀 QUICK START CHECKLIST

Before deploying:

- [ ] App runs locally (`streamlit run app.py`)
- [ ] `requirements.txt` is complete
- [ ] No hardcoded secrets
- [ ] `.gitignore` includes secrets
- [ ] GitHub repo created
- [ ] Choose hosting platform

---

## 🔒 PRIVACY NOTE

**Streamlit Cloud Free** requires public GitHub repo.
- Anyone can see your code
- ✅ Good for: demos, open source
- ❌ Bad for: proprietary data

**For private data:**
- Use Render (private repos on free tier)
- Or self-host on DigitalOcean
- Keep secrets in environment variables

---

## 📞 SUPPORT

- **Streamlit Docs:** docs.streamlit.io
- **Render Docs:** render.com/docs
- **PythonAnywhere:** help.pythonanywhere.com

---

**Bottom Line:** Start with Streamlit Cloud (FREE, 5 minutes setup). Don't waste time on cPanel/shared hosting for this app. Scale up when you need to!
