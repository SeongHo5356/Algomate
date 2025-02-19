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

    // "다음 파일" 버튼 생성
    const nextButton = document.createElement('button');
    nextButton.id = 'next-file-button';
    nextButton.textContent = '다음 파일';
    nextButton.style.marginLeft = '10px';
    nextButton.style.padding = '5px 10px';
    nextButton.style.fontSize = '14px';
    nextButton.style.cursor = 'pointer';

    // "유사한 코드 살펴보기" 버튼 생성
    const similarButton = document.createElement('button');
    similarButton.id = 'similar-code-button';
    similarButton.textContent = '유사한 코드 살펴보기';
    similarButton.style.marginLeft = '10px';
    similarButton.style.padding = '5px 10px';
    similarButton.style.fontSize = '14px';
    similarButton.style.cursor = 'pointer';

    // 버튼을 언어 설정 버튼의 부모에 추가
    languageSettingLink.parentNode.appendChild(nextButton);
    languageSettingLink.parentNode.appendChild(similarButton);

    // "다음 파일" 버튼 클릭 이벤트
    nextButton.addEventListener('click', async (event) => {
        event.preventDefault();
        event.stopPropagation();
        currentFileIndex = (currentFileIndex + 1) % externalFileUrls.length;
        isSimilarCodeDisplayed = false;
        await displayExternalFileContent(externalFileUrls[currentFileIndex]);
    });

    // "유사한 코드 살펴보기" 버튼 클릭 이벤트
    similarButton.addEventListener('click', async (event) => {
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
