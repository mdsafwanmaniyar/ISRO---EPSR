# ISRO---EPSR

# 🌑 Lunar Image Enhancement and Segmentation using AI + Flask Web App

This project leverages deep learning models (U-Net and MIRNet) combined with a Flask web interface to enhance and segment lunar images, focusing on **Permanently Shadowed Regions (PSRs)** from Chandrayaan-2 data. Achieves **80% success rate** in image enhancement.

---

## 🚀 Features
1. **U-Net Segmentation**: Identifies lunar craters in low-light conditions.
2. **MIRNet Enhancement**: Improves image clarity using physics-based post-processing.
3. **Flask Web App**: User-friendly interface to upload images and view enhanced/segmented results.
4. **Custom Dataset**: Curated lunar images and masks for training/testing.

---

## 📁 Project Structure
```bash
.
├── isro.py                  # U-Net model training
├── mir.py                   # MIRNet enhancement + physics post-processing
├── app.py                   # Flask web server
├── templates/               # HTML frontend
├── static/                  # CSS/JS/assets
├── dataset/                 # Training/validation images and masks
├── requirements.txt         # Dependencies
└── README.md
🛠️ Installation
Clone the repository:

bash
git clone [your-repo-link]
cd ISRO---EPSR
Install dependencies:

bash
pip install -r requirements.txt
Or manually:

bash
pip install flask tensorflow opencv-python huggingface_hub
� Usage
1. Train U-Net Model (Segmentation)
bash
python isro.py
Input: Images (dataset/train/images/) and masks (dataset/train/masks/).

Output: Trained model (unet.keras).

2. Enhance Images with MIRNet
bash
python mir.py
Applies brightness compensation, noise reduction, and BRDF reflectance.

3. Launch Flask Web App
bash
python app.py
Access at http://127.0.0.1:5000.

Upload images to view segmented/enhanced results.

📊 Results
Original Image	Enhanced Image	Segmented Output
Original	Enhanced	Segmented
🔮 Future Work
Deploy as a hosted service (AWS/Heroku).

Merge U-Net and MIRNet into a unified pipeline.

Add user authentication and image history.

👨‍💻 Author
Maniyar Safwan

📫 Contact: [Your Email]

🔗 LinkedIn: [Your Profile]

🏆 Hackathon Winner (Smart India Hackathon 2024, 36-Hour Hackathon 2022).

📜 License
MIT License. See LICENSE for details.


### Key Improvements:
1. **Professional Tone**: Emphasizes your achievements (80% success rate, hackathon wins).
2. **Visual Structure**: Clear headers, code blocks, and a results table.
3. **Author Section**: Highlights your credentials (e.g., ISRO project, hackathons).
4. **Future Work**: Shows project scalability for recruiters.
