from collections import defaultdict

print("\ncount_pairs function example")
def count_pairs(ids):
    counts = defaultdict(int) # 初期化キーがなくても0で初期化される
    for pair in zip(ids, ids[1:]): # 隣接するIDのペアを生成。少ない方のリストに合わせてペアが作られる。
        counts[pair] += 1
    return counts

# 使用例
ids = [1, 2, 3, 1, 2, 1, 2, 3, 1, 2]
counts = count_pairs(ids)
print(f"counts: {counts}")  # {(1, 2): 2, (2, 3): 1, (3, 1): 1}


print("\nmerge function example")
def merge(ids, pair, new_id):
    """
    マージ処理を行う関数。

    ids: 元のID列
    pair: マージする隣接ペア
    new_id: 新しいID

    return: マージ後のID列
    """
    merged_ids = []
    i = 0

    while i < len(ids):
        if i < len(ids) - 1 and (ids[i], ids[i+1]) == pair:
            merged_ids.append(new_id)
            i += 2
        else:
            merged_ids.append(ids[i])
            i += 1

    return merged_ids

# 使用例
ids = [1, 2, 3, 1, 2]
merged = merge(ids, (1, 2), 4) # (1, 2) を 4 にマージ
print(f"merged: {merged}")  # [4, 3, 4]


print("\nBPE training example")
def train_bpe(text, vocab_size):
    # テキストを0~255のID列に変換
    ids = list(text.encode("utf-8"))
    print(f"initial ids: {ids}")  # エンコード後のID列を表示

    # マージ回数を決定
    num_merges = vocab_size - 256  # 256は初期の語彙サイズ
    merge_rules = {}

    for step in range(num_merges):
        # 隣接ペアの統計を取得
        counts = count_pairs(ids)

        # ペアが存在しない場合の処理
        if not counts:
            break

        # 最頻出ペアを選択
        best_pair = max(counts, key=counts.get) # 最頻出ペアを選択し、そのキーを取得
        # best_pair = max(counts, key=lambda pair: (counts[pair], pair[0], pair[1]))

        # 新しいトークンIDを割り当て
        new_id = 256 + step
        merge_rules[best_pair] = new_id

        # マージを実行
        ids = merge(ids, best_pair, new_id)

    return merge_rules

# 使用例
text = "Hello world! This is BPE training."
merge_rules = train_bpe(text, vocab_size=260)
print(f"merge_rules: {merge_rules}")  # {(105, 115): 256, (256, 32): 257, (105, 110): 258, (72, 101): 259}