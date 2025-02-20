// src/utils/utils.js
export function getSubmissionIdFromUrl() {
    const urlParts = window.location.pathname.split('/');
    return urlParts[urlParts.length - 1]; // 마지막 부분이 제출 ID
}

// 현재 URL에서 문제 ID와 백준 ID 추출
export function extractProblemAndBkId() {
    const currentUrl = window.location.href;
    if (currentUrl.includes("acmicpc.net/problems/")) {
        return {
            problemId: currentUrl.split("/")[4],
            bkId: ""
        };
    }
    if (currentUrl.includes("acmicpc.net/submit/")) {
        const urlParts = currentUrl.split("/");
        return {
            problemId: urlParts[4] || null,
            bkId: urlParts[5] || null
        };
    }
    return { problemId: null, bkId: null };
}

// 언어 추출
export function getLanguageFromEditor() {
    const codeTextArea = document.querySelector("textarea[name='source']");
    if (!codeTextArea) return "Unknown";

    const mimeType = codeTextArea.getAttribute("data-mime");
    if (!mimeType) return "Unknown";

    if (mimeType.includes("c++")) return "C++";
    if (mimeType.includes("python")) return "Python";
    if (mimeType.includes("javascript")) return "JavaScript";
    if (mimeType.includes("java")) return "Java";
    if (mimeType.includes("c")) return "C";

    return "Unknown";
}

// 사용자 ID 추출
export function getUserId() {
    const userIdElement = document.querySelector('.username');
    return userIdElement ? userIdElement.innerText.trim() : null;
}