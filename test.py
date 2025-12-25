# import traceback, sys, os
# try:
#     open(r".\data\input\Multimodal Chain-of-Thought Reasoning A Comprehensive Survey.pdf", "rb").close()
#     print("open ok")
# except Exception:
#     traceback.print_exc()
#     print("os.path.exists:", os.path.exists(r"C:\path\to\your\file_or_folder"))
#     print("abspath:", os.path.abspath(r"C:\path\to\your\file_or_folder"))
#     print("normpath:", os.path.normpath(r"C:\path\to\your\file_or_folder"))
#     print("cwd:", os.getcwd())
    








import ollama







batch = ollama.embed(
  model='embeddinggemma',
  input=[
    'The quick brown fox jumps over the lazy dog.',
    'The five boxing wizards jump quickly.',
    'Jackdaws love my big sphinx of quartz.',
  ]
)
print(len(batch['embeddings']))  # number of vectors