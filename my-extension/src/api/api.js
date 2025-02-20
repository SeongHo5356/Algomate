// src/api/api.js
export async function sendProblemData(problemId, pageContent, userId) {
    const response = await fetch('http://localhost:8080/api/v1/problemData/submit-data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            title: problemId,
            content: pageContent,
            userId: userId
        })
    });
    return response.text();
}

export async function submitCode(problemId, bkId, codeContent, userId, language) {
    const response = await fetch('http://localhost:8080/api/v1/submission/submit-code', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            code: codeContent,
            problemId: problemId,
            userId: userId,
            language: language,
            bkId: bkId
        })
    });
    return response.text();
}

export async function requestSimilarityCalculate(bkId, problemId, language) {
    const response = await fetch('http://localhost:8080/api/v2/similarity/compare', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            bkId: bkId.toString(),
            problemId: problemId,
            language: language
        })
    })
    return response.text();
}

export async function fetchSimilarCodeUrls(submissionId) {
    try {
        const response = await fetch(`http://localhost:8080/api/v2/similarity/select5?bkId=${submissionId}`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' }
        });
        if (!response.ok) {
            throw new Error(`서버 요청 실패: ${response.statusText}`);
        }
        const result = await response.json();
        // 파일 경로를 올바른 URL로 변환
        return result.map(filePath => `http://localhost:8080/${filePath}`);
    } catch (error) {
        console.error('fetchSimilarCodeUrls error:', error);
        return [];
    }
}

export async function fetchFileContent(fileUrl) {
    const response = await fetch(fileUrl);
    if (!response.ok) {
        throw new Error(`파일을 읽을 수 없습니다: ${response.statusText}`);
    }
    return response.text();
}
