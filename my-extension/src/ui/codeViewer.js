// src/ui/codeViewer.js
export async function displayExternalFileContent(fileUrl) {
    try {
        const fileContent = await fetchFileContent(fileUrl);
        const codeContainer = document.querySelector('.CodeMirror-code');
        if (!codeContainer) {
            console.warn('코드 컨테이너(.CodeMirror-code)를 찾을 수 없습니다.');
            return;
        }

        // 기존 내용 삭제 후 새 콘텐츠 추가
        codeContainer.innerHTML = '';
        const preElement = document.createElement('pre');
        const codeElement = document.createElement('code');
        codeElement.className = 'language-python'; // 하이라이팅을 위해 클래스 추가
        codeElement.textContent = fileContent;
        preElement.appendChild(codeElement);
        codeContainer.appendChild(preElement);

        // Prism.js 코드 하이라이팅 적용 (있다면)
        if (window.Prism) {
            Prism.highlightElement(codeElement);
        }
    } catch (error) {
        console.error('displayExternalFileContent error:', error);
    }
}

// fetchFileContent 함수는 api.js의 함수를 사용해도 되지만, 여기서 직접 호출해도 됩니다.
import { fetchFileContent } from '../api/api.js';

export function clearCodeContainer() {
    const codeContainer = document.querySelector('.CodeMirror-code');
    if (codeContainer) {
        codeContainer.innerHTML = '';
    }
}
