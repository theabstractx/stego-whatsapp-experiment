import argparse
from blind_watermark import WaterMark

def main():
    parser = argparse.ArgumentParser(description="Embed a file into an image using blind watermarking.")
    parser.add_argument("--input", required=True, help="Path to input image (JPG/PNG)")
    parser.add_argument("--output", required=True, help="Path to output watermarked image")
    parser.add_argument("--file", required=True, help="Path to file to embed")
    parser.add_argument("--wm_len_out", required=True, help="Where to save length of embedded bits")
    args = parser.parse_args()

    with open(args.file, "rb") as f:
        file_bytes = f.read()

    # Bytes → Bitfolge
    bit_string = ''.join(format(byte, '08b') for byte in file_bytes)
    bit_array = [int(b) for b in bit_string]

    bwm1 = WaterMark(password_img=1, password_wm=1)
    bwm1.read_img(args.input)
    bwm1.read_wm(bit_array, mode='bit')
    bwm1.embed(args.output)

    print(f"[+] Embedded file '{args.file}' into image '{args.output}'")
    print(f"[+] Bit length: {len(bit_array)}")

    with open(args.wm_len_out, "w") as f:
        f.write(str(len(bit_array)))

if __name__ == "__main__":
    main()
