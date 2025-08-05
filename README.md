# Stego-WhatsApp Experiment

This repository contains the code and instructions for reproducing experiments from the paper *"Media-Based Steganography: Concealing Data in Digital Media"*. In these experiments, we hide secret data in images (steganography), send the images via **WhatsApp**, and then attempt to recover the hidden data from the received images. We evaluate the image quality degradation and data recovery success using standard metrics (PSNR, SSIM for image fidelity, and BER for data bit errors).

Four different steganography techniques are implemented, each in its own folder:

- **F5 (JPEG Steganography)** – Hides data in JPEG images using the F5 algorithm.
- **LSB (Least Significant Bit)** – Hides data by directly modifying the LSBs of image pixels.
- **Blind Watermark** – Hides data using a blind watermarking library (robust to some distortions).
- **SteganoGAN** – Uses a deep learning approach (the SteganoGAN library) to embed data in images.

Each method has its own setup requirements and usage steps, detailed below. To reproduce the experiments, follow the instructions for each technique. **All images and files should be kept in the same working directory** (as assumed by the scripts).

---

## General Prerequisites

- **Python 3.x** is required for the LSB, Blind Watermark, and SteganoGAN methods.  
- Required Python libraries:
  - `pillow`, `bitarray`, `scikit-image` (install with `pip`)  
  - Method-specific libraries are listed below
- WhatsApp application (for actual file transmission testing)

---

## Method Overviews & Instructions

Each method has its own subfolder containing `how-to.txt` files and source code. Refer to those or follow these detailed instructions:

### 1. F5 (JPEG Steganography)

**Requirements:**

- Java (JDK or JRE)
- Download `f5.jar` (e.g. from: https://code.google.com/archive/p/f5-steganography/)

**Steps:**

```bash
# Embed
java -jar f5.jar e -e secret.txt -p password cover.jpg stego.jpg

# Send stego.jpg via WhatsApp, then save received file as received.jpg

# Extract
java -jar f5.jar x -p password -e extracted.txt received.jpg

# Evaluate
python evaluate.py stego.jpg received.jpg secret.txt extracted.txt
```

### 2. LSB (Least Significant Bit)

**Install dependencies:**

```bash
pip install pillow bitarray scikit-image
```

**Usage:**

1. Prepare a cover image (`cover.png`) and a text file (`secret.txt`).
2. **Embed secret:**

   ```bash
   python lsb_embed.py cover.png secret.txt stego.png
   ```

3. Send `stego.png` via WhatsApp, download the received file as `received.jpg`.
4. **Extract secret:**

   ```bash
   python lsb_extract.py received.jpg extracted.txt
   ```

5. **Evaluate:**

   ```bash
   python evaluate.py cover.png received.jpg secret.txt extracted.txt
   ```

---

### 3. Blind Watermark

Based on: [guofei9987/blind_watermark](https://github.com/guofei9987/blind_watermark)


**Install dependencies:**

```bash
pip install blind-watermark
```

**Usage:**

1. Prepare a cover image (`cover.jpg`) and secret file (`secret.txt`).
2. **Embed secret:**

   ```bash
   python embed.py --input cover.jpg --output stego.jpg --file secret.txt --wm_len_out wm_len.txt
   ```

3. Send `stego.jpg` via WhatsApp, download the received image as `received.jpg`.
4. **Extract secret:**

   ```bash
   python extract.py --input received.jpg --wm_len_in wm_len.txt --output extracted.txt
   ```

5. **Evaluate:**

   ```bash
   python evaluate.py stego.jpg received.jpg secret.txt extracted.txt
   ```

---

### 4. SteganoGAN

Based on: [DAI-Lab/SteganoGAN](https://github.com/DAI-Lab/SteganoGAN)

**Important:** SteganoGAN **requires** `torch==1.0.0`, which is only compatible with **Python 3.6**. You should create a separate virtual environment with Python 3.6 for this method.

**Install dependencies:**

```bash
pip install steganogan torch==1.0.0 pillow bitarray scikit-image
```

**Usage:**

1. Prepare a PNG cover image (`cover.png`) and text file (`secret.txt`).
2. **Embed secret:**

   ```bash
   python encode.py --input cover.png --output stego.png --text secret.txt --arch dense
   ```

3. Send `stego.png` via WhatsApp, save the received file as `received.jpg`.
4. **Extract secret:**

   ```bash
   python decode.py --input received.jpg --output extracted.txt --arch dense
   ```

5. **Evaluate:**

   ```bash
   python evaluate.py cover.png received.jpg secret.txt extracted.txt
   ```

