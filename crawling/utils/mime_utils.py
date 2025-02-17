# 저장 폴더 매핑
# MIME 매핑 딕셔너리
MIME_MAP = {
    "c++": ("cpp", "Cpp"),
    "text/x-c++src": ("cpp", "C++"),
    "text/x-csrc": ("c", "C"),
    "text/x-rustsrc": ("rs", "Rust"),
    "text/x-ruby": ("rb", "Ruby"),
    "text/x-kotlin": ("kt", "Kotlin"),
    "text/x-swift": ("swift", "swift"),
    "text/x-csharp": ("cs", "csharp"),
    "text/javascript": ("js", "Javascript"),
    "text/x-go": ("go", "Go"),
    "text/x-d": ("d", "d"),
    "text/x-python": ("py", "Python"),
    "python": ("py", "Python"),
    "text/x-java": ("java", "Java"),
    "java": ("java", "Java"),
    "text/plain": ("txt", "text"),
}

def get_file_extension_and_folder(mime_type):
    for key, value in MIME_MAP.items():
        if key in mime_type:
            return value
    return "txt", "other"