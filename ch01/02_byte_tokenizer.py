# 'A' の場合
print("byte encoding 'A'")
encoded = 'A'.encode("utf-8")
print(f"byteencoded: {encoded}")        # b'A'
print(f"list of byte encoded 'A': {list(encoded)}")  # [65]

print("\nbyte encoding 'あ'")
text = 'あ'
encoded = text.encode("utf-8")
print(f"byteencoded: {encoded}")        # b'\xe3\x81\x82'
print(f"list of byte encoded '{text}': {list(encoded)}")  # [227, 129, 130]

print("\nbyte decoding [65]")
ids = [65]
decoded = bytes(ids).decode("utf-8")
print(f"ids: {ids}")
print(f"decoded: {decoded}")
print("-----")


print("\nbyte tokenizer example")
class ByteTokenizer:
    def encode(self, text):
        return list(text.encode("utf-8"))

    def decode(self, ids):
        return bytes(ids).decode("utf-8")


# 使用例
tokenizer = ByteTokenizer()
text = "hello世界😁"

# エンコード
ids = tokenizer.encode(text)
print(f"encoded ids for '{text}': {ids}")
# print(ids)  # [104, 101, 108, 108, 111, 228, 184, 150, 231, 149, 140, 240, 159, 152, 129]

# デコード
decoded = tokenizer.decode(ids)
print(f"decoded from list: {decoded}")  # hello世界😁