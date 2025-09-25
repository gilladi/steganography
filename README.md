# steganography
A Python GUI application that hides and reveals secret messages inside PNG images using LSB (Least Significant Bit) steganography.

---

# Features
- **Hide text messages** inside PNG images  
- **Extract hidden messages** from stego-images  
- Clean and simple **Tkinter-based GUI**  
- Built-in **capacity check** to prevent oversized messages  
- **Integrity check** to ensure encoded messages decode correctly  

---

# Tutorial
Here’s a quick overview of how the tool works:

**Encoding**  
- Select a PNG image to use as the cover image.  
- Enter your secret text message in the input box.  
- Save the new image (stego-image) with the hidden message embedded.  
- The tool verifies that the message can be successfully extracted.  

**Decoding**  
- Select a stego-image (previously encoded).  
- The tool extracts and displays the hidden message in a popup.  
- If no valid hidden message exists, an error will be shown.  

---

# Setup
1. Clone the repository:
git clone https://github.com/gilladi/steganography.git
cd steganography

2. - python -m venv venv
- source venv/bin/activate   # macOS/Linux
- venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the Program:
python stego_gui.py

---

# Future Updates
Add support for hiding binary files (not just text)
Encrypt messages before embedding for extra security
Add drag-and-drop support in the GUI
Support additional image formats (JPEG, BMP)
Implement batch encoding/decoding for multiple images
