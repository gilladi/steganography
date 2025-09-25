from PIL import Image

def text_to_bits(message: str) -> str:
    """Convert a string to a bit string."""
    byte_data = message.encode('utf-8')
    bits = ''.join(f'{byte:08b}' for byte in byte_data)
    return bits

def bits_to_text(bits: str) -> str:
    """Convert a bit string back to text."""
    bytes_list = [bits[i:i+8] for i in range(0, len(bits), 8)]
    byte_data = bytes(int(b, 2) for b in bytes_list)
    return byte_data.decode('utf-8')

def encode_message(image_path, output_path, message):
    img = Image.open(image_path).convert("RGB")

    # Check image mode
    if img.mode != "RGB":
        raise ValueError("Image must be in RGB mode (not RGBA or grayscale).")

    pixels = img.load()

    # Convert message to bits
    message_bytes = message.encode("utf-8")
    message_bits = ''.join([format(byte, "08b") for byte in message_bytes])
    length_bits = format(len(message_bits), "032b")  # 32-bit header
    full_bits = length_bits + message_bits

    width, height = img.size
    total_pixels = width * height * 3
    capacity = total_pixels // 8  # in bytes

    # Capacity check
    if len(message_bytes) > capacity:
        raise ValueError(f"Message too large! Max capacity: {capacity} bytes, your message: {len(message_bytes)} bytes.")

    # Embed bits
    bit_index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            if bit_index < len(full_bits):
                r = (r & ~1) | int(full_bits[bit_index]); bit_index += 1
            if bit_index < len(full_bits):
                g = (g & ~1) | int(full_bits[bit_index]); bit_index += 1
            if bit_index < len(full_bits):
                b = (b & ~1) | int(full_bits[bit_index]); bit_index += 1

            pixels[x, y] = (r, g, b)

    img.save(output_path, "PNG")

    # Post-encode integrity check
    decoded_test = decode_message(output_path)
    if decoded_test != message:
        raise ValueError("Integrity check failed: decoded message does not match input!")

    print(f"Message encoded and saved as {output_path}")
    print(f"Image capacity: {capacity} bytes")
    print(f"Message size  : {len(message_bytes)} bytes")
    print("Integrity check passed\n")

def decode_message(stego_path):
    img = Image.open(stego_path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    # Extract bits
    bits = ""
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            bits += str(r & 1)
            bits += str(g & 1)
            bits += str(b & 1)

    # First 32 bits = length
    length = int(bits[:32], 2)

    # Sanity check on length
    if length <= 0 or length > len(bits) - 32:
        raise ValueError("No valid hidden message found or corrupted data.")

    message_bits = bits[32:32+length]

    # Convert to bytes
    message_bytes = [message_bits[i:i+8] for i in range(0, len(message_bits), 8)]
    try:
        message = "".join([chr(int(b, 2)) for b in message_bytes])
    except Exception:
        raise ValueError("Failed to decode message — data may be corrupted.")
    return message

