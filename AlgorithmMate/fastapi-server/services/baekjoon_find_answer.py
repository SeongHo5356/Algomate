# 결과 중 1개를 찾아서 코드를 return

import requests
from bs4 import BeautifulSoup
import re
import base64
from language_options import determine_baekjoon_language

def search_github_commits(query, token):
    """GitHub API를 사용하여 커밋을 검색합니다."""
    url = f"https://api.github.com/search/commits?q={query}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.cloak-preview"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # 여기서 [] 을 바꾸면 -> 몇번째 검색 결과를 정답으로 할지 결정 가능
        return response.json()['items'][0]['html_url']
    else:
        ## 대부분 재 검색하면 다시 가능 ... 아마도 뭔가 반복적으로  api를 사용해서 그런걸지도..
        raise Exception(f"GitHub API 검색 실패: {response.status_code}")


def get_file_path(commit_url):
    """커밋 페이지에서 파일 경로를 추출합니다."""
    commit_response = requests.get(commit_url)
    if commit_response.status_code == 200:
        soup = BeautifulSoup(commit_response.content, 'html.parser')
        file_paths = [entry['data-file-path'] for entry in soup.find_all('copilot-diff-entry')]
        print("file_paths : ", file_paths, "length : ", len(file_paths))
        return file_paths[-1] if file_paths else None
    else:
        raise Exception(f"커밋 페이지 검색 실패: {commit_response.status_code}")


def extract_owner_repo(commit_url):
    """커밋 URL에서 owner와 repo를 추출합니다."""
    match = re.search(r"github\.com/([^/]+)/([^/]+)/", commit_url)
    if match:
        return match.group(1), match.group(2)
    else:
        raise Exception("Owner와 Repo를 찾을 수 없습니다.")


def get_file_content(owner, repo, file_path, token):
    """GitHub API를 사용하여 파일 내용을 가져옵니다."""
    code_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(code_url, headers=headers)
    if response.status_code == 200:
        file_content = response.json()['content']
        decoded_bytes = base64.b64decode(file_content)
        return decoded_bytes.decode('utf-8')
    else:
        raise Exception(f"파일 내용 검색 실패: {response.status_code}")

"""
1. 찾은 커밋 url
2. 찾은 커밋의 커밋된 파일 목록
3. 찾은 파일의 경로
4. 찾은 커밋 repo의 owner
5. 찾은 커밋의 repo 이름
6. 찾은 커밋에서 정답 코드의 이름
"""
def main(query, token):
    try:
        commit_url = search_github_commits(query, token)
        print(f"찾은 커밋 URL: {commit_url}")

        file_path = get_file_path(commit_url)
        print(f"file_path: {file_path}")

        # 언어 결정
        submit_lang = determine_baekjoon_language(file_path)
        print(f"submit lang: {submit_lang}")

        owner, repo = extract_owner_repo(commit_url)
        print(f"Owner: {owner}")
        print(f"Repo: {repo}")

        file_content = get_file_content(owner, repo, file_path, token)
        print("\n파일 내용:")
        print(file_content)

        return file_content, submit_lang

    except Exception as e:
        print(f"오류 발생: {str(e)}")



if __name__ == "__main__":
    # GitHub Personal Access Token
    # Test
    token = "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"  # 여기에 생성한 토큰을 입력하세요.
    query = "[Gold IV] Title: 고층 건물"
    main(query, token)