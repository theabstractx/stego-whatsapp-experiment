from PIL import Image
import sys

def extract(image_path, output_text):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    w, h = img.size

    bits = ""
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            bits += str(r & 1) + str(g & 1) + str(b & 1)

    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    msg = ''.join(chars).split(chr(0))[0]

    with open(output_text, "w", encoding="utf-8") as f:
        f.write(msg)
    print(f"[+] Extracted message → {output_text}")

if __name__ == "__main__":
    extract(sys.argv[1], sys.argv[2])
