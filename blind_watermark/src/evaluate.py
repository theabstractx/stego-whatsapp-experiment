from skimage.metrics import structural_similarity as ssim, peak_signal_noise_ratio as psnr
from PIL import Image
from bitarray import bitarray
import numpy as np
import sys

def compare_images(img1_path, img2_path):
    img1 = Image.open(img1_path).convert("RGB")
    img2 = Image.open(img2_path).convert("RGB")

    # Resize img2 to match img1 if necessary
    if img1.size != img2.size:
        print(f"[!] Image dimensions differ: {img1.size} vs {img2.size}")
        print("[*] Resizing second image to match first.")
        img2 = img2.resize(img1.size, Image.LANCZOS)

    arr1 = np.array(img1)
    arr2 = np.array(img2)

    psnr_val = psnr(arr1, arr2)
    ssim_val = ssim(arr1, arr2, channel_axis=2)
    print(f"PSNR: {psnr_val:.2f} dB")
    print(f"SSIM: {ssim_val:.4f}")

def bit_error(original_path, extracted_path):
    with open(original_path, "rb") as f1, open(extracted_path, "rb") as f2:
        b1 = bitarray(); b1.fromfile(f1)
        b2 = bitarray(); b2.fromfile(f2)

    min_len = min(len(b1), len(b2))
    if min_len == 0:
        print("BER: 100.00% (no overlap)")
        return

    errors = sum(x != y for x, y in zip(b1[:min_len], b2[:min_len]))
    ber = errors / min_len
    print(f"BER: {ber*100:.2f}%")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python evaluate.py <image1> <image2> <original_text> <extracted_text>")
        sys.exit(1)

    compare_images(sys.argv[1], sys.argv[2])
    bit_error(sys.argv[3], sys.argv[4])
