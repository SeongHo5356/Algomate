# 저장 폴더 매핑
# MIME 매핑 딕셔너리
MIME_MAP = {
    "c++": ("cpp", "cpp"),
    "text/x-c++src": ("cpp", "cpp"),
    "text/x-csrc": ("c", "c"),
    "text/x-rustsrc": ("rs", "rust"),
    "text/x-ruby": ("rb", "ruby"),
    "text/x-kotlin": ("kt", "kotlin"),
    "text/x-swift": ("swift", "swift"),
    "text/x-csharp": ("cs", "csharp"),
    "text/javascript": ("js", "javascript"),
    "text/x-go": ("go", "go"),
    "text/x-d": ("d", "d"),
    "text/x-python": ("py", "python"),
    "python": ("py", "python"),
    "text/x-java": ("java", "java"),
    "java": ("java", "java"),
    "text/plain": ("txt", "text"),
}

def get_file_extension_and_folder(mime_type):
    for key, value in MIME_MAP.items():
        if key in mime_type:
            return value
    return "txt", "other"