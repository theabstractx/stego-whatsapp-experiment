import argparse
from steganogan import SteganoGAN

def main():
    parser = argparse.ArgumentParser(description="Encode a message from a text file into an image using SteganoGAN.")
    parser.add_argument("--input", required=True, help="PNG cover image path")
    parser.add_argument("--output", required=True, help="Output stego-image path")
    parser.add_argument("--text", required=True, help="Text file with secret")
    parser.add_argument("--arch", default="dense", choices=["basic", "dense"], help="Pretrained architecture")
    parser.add_argument("--cpu", action="store_true", help="Use CPU instead of GPU")
    args = parser.parse_args()

    with open(args.text, "r", encoding="utf‑8") as f:
        message = f.read()

    use_cuda = not args.cpu
    steganogan = SteganoGAN.load(architecture=args.arch, cuda=use_cuda)
    print(f"[+] Encoding using arch={args.arch}, cuda={use_cuda}")
    steganogan.encode(args.input, args.output, message)
    print(f"[+] Saved stego image to '{args.output}'")

if __name__ == "__main__":
    main()
