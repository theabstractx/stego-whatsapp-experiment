from PIL import Image
import sys

def embed(image_path, text_path, output_path):
    img = Image.open(image_path).convert("RGB")
    with open(text_path, "r", encoding="utf-8") as f:
        msg = f.read() + chr(0)  # Null terminator
    bits = ''.join(format(ord(c), "08b") for c in msg)

    pixels = img.load()
    w, h = img.size
    idx = 0

    for y in range(h):
        for x in range(w):
            if idx >= len(bits): break
            r, g, b = pixels[x, y]
            if idx < len(bits): r = (r & ~1) | int(bits[idx]); idx += 1
            if idx < len(bits): g = (g & ~1) | int(bits[idx]); idx += 1
            if idx < len(bits): b = (b & ~1) | int(bits[idx]); idx += 1
            pixels[x, y] = (r, g, b)
        if idx >= len(bits): break

    img.save(output_path)
    print(f"[+] Embedded {len(bits)} bits in {output_path}")

if __name__ == "__main__":
    embed(sys.argv[1], sys.argv[2], sys.argv[3])
