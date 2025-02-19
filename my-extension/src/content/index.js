// src/content/index.js
import { sendProblemData, submitCode } from '../api/api.js';
import { createNextAndSimilarButtons } from '../ui/buttons.js';

(function() {
    const currentUrl = window.location.href;
    const pageTitle = document.title;
    const pageContent = document.body.innerText;
    const userIdElement = document.querySelector('.username');
    const userId = userIdElement ? userIdElement.innerText : null;
    console.log('User ID:', userId);

    // 문제 페이지인 경우: 페이지 데이터를 서버에 전송
    if (currentUrl.includes("acmicpc.net/problem/")) {
        const urlParts = currentUrl.split("/");
        const problemId = urlParts[4];
        sendProblemData(problemId, pageContent, userId)
            .then(data => console.log('문제 데이터 전송 성공:', data))
            .catch(error => console.error('문제 데이터 전송 오류:', error));
    }
    // 제출 페이지인 경우: 제출 코드 전송
    else if (currentUrl.includes("acmicpc.net/submit/")) {
        window.onload = () => {
            const urlParts = currentUrl.split("/");
            const problemId = urlParts[4];
            const bkId = urlParts[5];
            const codeTextArea = document.querySelector("textarea[name='source']");
            if (codeTextArea && codeTextArea.value.trim() !== "") {
                const codeContent = codeTextArea.value;
                const mimeType = codeTextArea.getAttribute("data-mime");
                let language = "Unknown";
                if (mimeType) {
                    if (mimeType.includes("c++")) language = "C++";
                    else if (mimeType.includes("python")) language = "Python";
                    else if (mimeType.includes("java")) language = "Java";
                    else if (mimeType.includes("c")) language = "C";
                }
                submitCode(problemId, bkId, codeContent, userId, language)
                    .then(data => console.log('제출 코드 전송 성공:', data))
                    .catch(error => console.error('제출 코드 전송 오류:', error));
            } else {
                console.error("코드 영역을 찾을 수 없거나 비어 있습니다.");
            }
        };
    }

    // 페이지 로드 시 URL 조건에 맞으면 버튼 생성
    window.addEventListener('load', () => {
        try {
            const problemMatch = currentUrl.match(/^https:\/\/www\.acmicpc\.net\/problem\/\d+$/);
            const submitMatch = currentUrl.match(/^https:\/\/www\.acmicpc\.net\/submit\/\d+\/\d+$/);
            if (!problemMatch && !submitMatch) {
                console.log('URL 조건에 맞지 않아 스크립트를 실행하지 않습니다.');
                return;
            }
            createNextAndSimilarButtons();
        } catch (error) {
            console.error('콘텐츠 스크립트 실행 중 오류:', error);
        }
    });
})();
