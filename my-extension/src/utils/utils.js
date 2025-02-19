// src/utils/utils.js
export function getSubmissionIdFromUrl() {
    const urlParts = window.location.pathname.split('/');
    return urlParts[urlParts.length - 1]; // 마지막 부분이 제출 ID
}
