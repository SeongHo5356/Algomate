// src/ui/buttons.js
import { fetchSimilarCodeUrls } from '../api/api.js';
import { displayExternalFileContent, clearCodeContainer } from './codeViewer.js';
import { getSubmissionIdFromUrl } from '../utils/utils.js';

let currentFileIndex = 0;
let externalFileUrls = [
    'http://127.0.0.1:8000/files/sample1.py',
    'http://127.0.0.1:8000/files/sample2.py',
    'http://127.0.0.1:8000/files/sample3.py',
    'http://127.0.0.1:8000/files/sample4.py',
];
let isSimilarCodeDisplayed = false;

export function createNextAndSimilarButtons() {
    const languageSettingLink = document.querySelector('a[href="/setting/language"]');
    if (!languageSettingLink) {
        console.warn('"언어 설정" 버튼을 찾을 수 없습니다.');
        return;
    }

    // 버튼 스타일 설정 함수
    const setButtonStyle = (button) => {
        nextButton.style.marginLeft = '10px';
        nextButton.style.padding = '5px 10px';
        nextButton.style.fontSize = '14px';
        nextButton.style.cursor = 'pointer';
    }

    // "다음 파일" 버튼 생성
    const nextButton = document.createElement('button');
    nextButton.id = 'next-file-button';
    nextButton.textContent = '다음 파일';
    setButtonStyle(nextButton);

    // "유사한 코드 살펴보기" 버튼 생성
    const similarButton = document.createElement('button');
    similarButton.id = 'similar-code-button';
    similarButton.textContent = '내 코드 제출하기';
    setButtonStyle(similarButton);

    // "코드 저장하기" 버튼 생성 (새 버튼 추가)
    const resultButton = document.createElement('button');
    resultButton.id = 'save-code-button';
    resultButton.textContent = '결과 살펴보기';
    setButtonStyle(resultButton);

    // 버튼을 언어 설정 버튼의 부모에 추가
    languageSettingLink.parentNode.appendChild(nextButton);
    languageSettingLink.parentNode.appendChild(resultButton);

    // "다음 파일" 버튼 클릭 이벤트
    nextButton.addEventListener('click', async (event) => {
        event.preventDefault();
        event.stopPropagation();
        currentFileIndex = (currentFileIndex + 1) % externalFileUrls.length;
        isSimilarCodeDisplayed = false;
        await displayExternalFileContent(externalFileUrls[currentFileIndex]);
    });

    // "유사한 코드 살펴보기" 버튼 클릭 이벤트
    resultButton.addEventListener('click', async (event) => {
        event.preventDefault();
        event.stopPropagation();
        if (!isSimilarCodeDisplayed) {
            const submissionId = getSubmissionIdFromUrl();
            const fileUrls = await fetchSimilarCodeUrls(submissionId);
            console.log('받은 유사 코드 파일 경로들:', fileUrls);
            if (fileUrls.length > 0) {
                externalFileUrls = fileUrls;
                currentFileIndex = 0;
                await displayExternalFileContent(externalFileUrls[currentFileIndex]);
                isSimilarCodeDisplayed = true;
            } else {
                console.log('유사한 코드가 없습니다.');
            }
        } else {
            clearCodeContainer();
            isSimilarCodeDisplayed = false;
        }
    });
}
