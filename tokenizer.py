import os
from curtsies.fmtfuncs import cyan, bold, green, red, yellow
from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer


TRAIN_BASE = False
paths = ["python_text_data_file.txt"]

if TRAIN_BASE:
    # Initialize a tokenizer
    tokenizer = ByteLevelBPETokenizer()

    # Customize training
    tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>",
    ])

    # Save files to disk
    tokenizer.save_model("tokenizer")

inp = 'print("Hello World!")'

tokenizer = GPT2Tokenizer.from_pretrained('tokenizer')

tokenizer.add_special_tokens({
    "bos_token": "<s>",
    "pad_token": "<pad>",
    "eos_token": "</s>",
    "unk_token": "<unk>",
    "mask_token": "<mask>",
})

t = tokenizer.encode(inp)

print(t)