import argparse
from blind_watermark import WaterMark

def bits_to_bytes(bits):
    bit_str = ''.join(['1' if bit else '0' for bit in bits])
    return bytes(int(bit_str[i:i+8], 2) for i in range(0, len(bit_str), 8))


def main():
    parser = argparse.ArgumentParser(description="Extract embedded file from watermarked image.")
    parser.add_argument("--input", required=True, help="Path to watermarked image")
    parser.add_argument("--wm_len_in", required=True, help="Path to file that stores watermark bit length")
    parser.add_argument("--output", required=True, help="Path to write extracted file to")
    args = parser.parse_args()

    with open(args.wm_len_in, "r") as f:
        wm_len = int(f.read().strip())

    bwm1 = WaterMark(password_img=1, password_wm=1)
    wm_bits = bwm1.extract(args.input, wm_shape=wm_len, mode='bit')

    file_bytes = bits_to_bytes(wm_bits)

    with open(args.output, "wb") as f:
        f.write(file_bytes)

    print(f"[+] Extracted embedded file to '{args.output}'")

if __name__ == "__main__":
    main()
