import argparse
from steganogan import SteganoGAN

def main():
    parser = argparse.ArgumentParser(description="Decode a hidden message from an image using SteganoGAN.")
    parser.add_argument("--input", required=True, help="Stego image path (PNG or JPEG)")
    parser.add_argument("--output", required=True, help="File path to save decoded text")
    parser.add_argument("--arch", default="dense", choices=["basic", "dense"], help="Architecture used in encoding")
    parser.add_argument("--cpu", action="store_true", help="Use CPU instead of GPU")
    args = parser.parse_args()

    use_cuda = not args.cpu
    steganogan = SteganoGAN.load(architecture=args.arch, cuda=use_cuda)
    print(f"[+] Decoding using arch={args.arch}, cuda={use_cuda}")
    message = steganogan.decode(args.input)

    with open(args.output, "w", encoding="utf‑8") as f:
        f.write(message)

    print(f"[+] Decoded message saved to '{args.output}'")

if __name__ == "__main__":
    main()
