# 공통 언어 매핑 딕셔너리
LANGUAGE_MAPPING = {
    "Python": ("python3", ".py"),
    "Python3": ("python3", ".py"),
    "PyPy3": ("python3", ".py"),
    "C": ("c", ".c"),
    "C99": ("c", ".c"),
    "C++": ("cpp", ".cpp"),
    "C++14": ("cpp", ".cpp"),
    "C++17": ("cpp", ".cpp"),
    "Java": ("java", ".java"),
    "Kotlin": ("kotlin", ".kt"),
    "C#": ("csharp", ".cs"),
    "Swift": ("swift", ".swift"),
    "Go": ("go", ".go"),
    "Rust": ("rust", ".rs"),
    "Scala": ("scala", ".scala"),
    "R": ("rlang", ".r"),
    "Text": ("text", ".txt"),
    "Scheme": ("scheme", ".scm")
}

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

def map_language_to_jplag_option(language_tag: str) -> str:
    """
    백준의 언어 태그를 JPlag 언어 옵션으로 매핑하는 함수.

    Args:
        language_tag (str): 백준에서 크롤링한 언어 태그

    Returns:
        str: JPlag에서 사용할 언어 옵션
    """
    # 매핑에 없는 경우 기본값 "text"
    return LANGUAGE_MAPPING.get(language_tag, ("text", ".txt"))[0]


def map_language_to_file_extension(language_tag: str) -> str:
    """
    백준의 언어 태그에 따라 로컬 파일 저장 확장자를 결정하는 함수.

    Args:
        language_tag (str): 백준에서 크롤링한 언어 태그

    Returns:
        str: 파일 확장자 (예: .py, .cpp, .java 등)
    """
    # 매핑에 없는 경우 기본값 ".txt"
    return LANGUAGE_MAPPING.get(language_tag, ("text", ".txt"))[1]

## 백준에서 제출 시 선태하게 될 언어 옵션
def determine_baekjoon_language(file_paths):
    """
    파일 경로 또는 경로 목록에서 확장자를 기반으로 백준 제출 언어를 결정합니다.

    Args:
        file_paths (str | list): 파일 경로나 파일 경로 목록.

    Returns:
        str: 백준 제출 언어 이름 (예: 'C++', 'Python', 'Java').

    Raises:
        ValueError: 지원되지 않는 확장자가 있을 경우 예외를 발생시킵니다.
    """
    # 확장자와 백준 언어 매핑
    extension_to_language = {
        ".cc": "C++17",
        ".cpp": "C++17",
        ".py": "Python 3",
        ".java": "Java 11",
        ".c": "C99",
        ".kt": "Kotlin (JVM)",
        ".rb": "Ruby",
        ".swift": "Swift",
        ".cs": "C#",  # C# 추가
        ".js": "node.js",
        ".go": "Go",
        ".d": "D",
        ".rs": "Rust 2018",
        ".txt": "Text",  # 텍스트 파일도 제출 가능한 경우
    }

    # 단일 경로를 리스트로 변환
    if isinstance(file_paths, str):
        file_paths = [file_paths]

    # 파일 목록에서 확장자 분석
    for file_path in file_paths:
        for ext, lang in extension_to_language.items():
            if file_path.endswith(ext):
                return lang

    # 지원되지 않는 확장자가 있는 경우
    raise ValueError("지원되지 않는 확장자가 포함되어 있습니다.")


def  get_file_extention_and_folder(mime_type):
    """
    MIME 타입을 기반으로 파일 확장자와 언어 폴더 이름을 반환합니다.

    Args:
        mime_type (str): MIME 타입 문자열.

    Returns:
        tuple: (파일 확장자, 언어 폴더 이름)
    """
    print("## mime_type : ", mime_type)

    # MIME 타입과 언어 매핑
    mime_map = {
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
        "python": ("py", "python"),  # 일반 python 포함
        "text/x-java": ("java", "java"),
        "java": ("java", "java"),  # 일반 java 포함
        "text/plain": ("txt", "text"),  # 일반 텍스트
    }

    # MIME 타입 키워드와 일치하는 확장자 및 폴더 이름 반환
    for key, value in mime_map.items():
        if key in mime_type:
            return value

    return "txt", "other"  # 기본값: 미지원 MIME 타입의 경우

def get_folder_from_extension(data_language):
    """
    LANGUAGE_MAPPING에서 확장자를 얻고, MIME_MAP에서 해당 확장자에 맞는 폴더명을 반환합니다.

    Args:
        data_language (str): 백준에서 사용된 언어 태그.

    Returns:
        str: 폴더명.
    """
    # 확장자를 LANGUAGE_MAPPING에서 얻음
    file_extension = LANGUAGE_MAPPING.get(data_language, ("text", ".txt"))[1]

    # MIME_MAP을 탐색하여 확장자와 매칭되는 폴더명을 반환
    extension_to_folder = {
        "cpp": "cpp",
        "py": "python",
        "java": "java",
        "c": "c",
        "rs": "rust",
        "kt": "kotlin",
        "swift": "swift",
        "cs": "csharp",
        "js": "javascript",
        "go": "go",
        "d": "d",
        "txt": "text",
    }


    # 확장자를 키로 매핑하여 폴더명을 반환
    folder_name = extension_to_folder.get(file_extension.strip("."), "other")
    return folder_name

# 사용 예시
if __name__ == "__main__":
    data_language = "Python3"
    jplag_language = map_language_to_jplag_option(data_language)
    print(f"JPlag language option: {jplag_language}")

    data_language = "Python3"
    file_extension = map_language_to_file_extension(data_language)
    print(f"File extension: {file_extension}")
