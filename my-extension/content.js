(function() {
    let externalFileUrls = [
        'http://127.0.0.1:8000/files/sample1.py',
        'http://127.0.0.1:8000/files/sample2.py',
        'http://127.0.0.1:8000/files/sample3.py',
        'http://127.0.0.1:8000/files/sample4.py',
    ];
    let currentFileIndex = 0;
    let isSimilarCodeDisplayed = false;

    // 데이터 추출 및 서버 전송
    const currentUrl = window.location.href;
    const pageTitle = document.title;
    const pageContent = document.body.innerText;

    const userIdElement = document.querySelector('.username');
    let userId = userIdElement ? userIdElement.innerText : null;
    console.log('Page data success0_user_id:', userId);

    if (currentUrl.includes("acmicpc.net/problem/")) {
        const urlParts = currentUrl.split("/")
        const problemId = urlParts[4]
        // 문제 페이지에서 서버에 페이지 데이터를 전송 -> 문제페이지에 접근 시 크롤링 시작하기 위해서
        fetch('http://localhost:8080/api/v1/submit-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: problemId,
                content: pageContent,
                userId: userId
            })
        })
        .then(response => response.json())
        .then(data => console.log('Page data success1_data:', data))
        .catch((error) => console.error('Page data error:', error));
    }

    else if (currentUrl.includes("acmicpc.net/submit/")) {
        // 내 제출 수정 페이지에서 제출 코드 서버로 전송
        const urlParts = currentUrl.split("/")
        const problemId = urlParts[4]
        const bkId = urlParts[5]
        window.onload = () => {
            const codeTextArea = document.querySelector("textarea[name='source']");
            if (codeTextArea && codeTextArea.value.trim() !== "") {
                const codeContent = codeTextArea.value;
                console.log('Page data success5_codeCodeContent:', codeContent);

                const mimeType = codeTextArea.getAttribute("data-mime");
                let language = "Unknown";
                if (mimeType) {
                    if (mimeType.includes("c++")) language = "C++";
                    else if (mimeType.includes("python")) language = "Python";
                    else if (mimeType.includes("java")) language = "Java";
                    else if (mimeType.includes("c")) language = "C";
                }
                console.log('Page data success9_language: ', language);

                fetch('http://localhost:8080/api/v1/submission/submit-code', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        code: codeContent,
                        problemId: problemId,
                        userId: userId,
                        language: language,
                        bkId : bkId
                    })
                })
                .then(response => response.json())
                .then(data => console.log('Code data success:', data))
                .catch((error) => console.error('Code data error:', error));
            } else {
                console.error("Code text area not found or empty");
            }
        };
    }

    // "다음 파일" 및 "유사한 코드 살펴보기" 버튼 생성
    function createNextAndSimilarButtons() {
        const languageSettingLink = document.querySelector('a[href="/setting/language"]');
        if (!languageSettingLink) {
            console.warn('test : "언어 설정" 버튼을 찾을 수 없습니다.');
            return;
        }

        const nextButton = document.createElement('button');
        nextButton.id = 'next-file-button';
        nextButton.textContent = '다음 파일';
        nextButton.style.marginLeft = '10px';
        nextButton.style.padding = '5px 10px';
        nextButton.style.fontSize = '14px';
        nextButton.style.cursor = 'pointer';

        const similarButton = document.createElement('button');
        similarButton.id = 'similar-code-button';
        similarButton.textContent = '유사한 코드 살펴보기';
        similarButton.style.marginLeft = '10px';
        similarButton.style.padding = '5px 10px';
        similarButton.style.fontSize = '14px';
        similarButton.style.cursor = 'pointer';

        languageSettingLink.parentNode.appendChild(nextButton);
        languageSettingLink.parentNode.appendChild(similarButton);

        nextButton.addEventListener('click', async (event) => {
            event.preventDefault();
            event.stopPropagation();

            currentFileIndex = (currentFileIndex + 1) % externalFileUrls.length;
            isSimilarCodeDisplayed = false;
            await displayExternalFileContent(externalFileUrls, currentFileIndex);
        });

        similarButton.addEventListener('click', async (event) => {
            event.preventDefault();
            event.stopPropagation();

            if (!isSimilarCodeDisplayed) {
                try {
                    const submissionId = getSubmissionIdFromUrl(); // 제출 ID 가져오기
                    const fileUrls = await fetchSimilarCodeUrls(submissionId); // 서버에서 파일 목록 가져오기

                    console.log("받은 유사 코드 파일 경로들:", fileUrls);

                    if (fileUrls.length > 0) {
                        externalFileUrls = fileUrls;
                        currentFileIndex = 0;
                        await displayExternalFileContent(fileUrls, currentFileIndex);
                        isSimilarCodeDisplayed = true;
                    } else {
                        console.log('유사한 코드가 없습니다.');
                    }
                } catch (error) {
                    console.error('유사 코드 요청 중 오류 발생:', error);
                }
            } else {
                clearCodeContainer();
                isSimilarCodeDisplayed = false;
            }
        });
    }
    function getSubmissionIdFromUrl() {
        const urlParts = window.location.pathname.split('/');
        return urlParts[urlParts.length - 1]; // URL의 마지막 부분이 제출 ID
    }

    async function fetchSimilarCodeUrls(submissionId) {
        try {
            const response = await fetch(`http://localhost:8080/api/v1/similarity/select5?bkId=${submissionId}`, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' }
            });

            if (!response.ok) {
                throw new Error(`서버 요청 실패: ${response.statusText}`);
            }

            const result = await response.json();

            // 🔹 파일 경로를 올바른 정적 리소스 URL로 변환
            return result.map(filePath => `http://localhost:8080/${filePath}`);
        } catch (error) {
            console.error('유사 코드 요청 중 오류 발생:', error);
            return [];
        }
    }



    async function displayExternalFileContent(externalFileUrls, index) {
        const fileUrl = externalFileUrls[index];

        console.log('외부 파일 요청 URL:', fileUrl);

        try {
            const response = await fetch(fileUrl);
            if (!response.ok) {
                throw new Error(`파일을 읽을 수 없습니다: ${response.statusText}`);
            }

            const fileContent = await response.text();
            const codeContainer = document.querySelector('.CodeMirror-code');
            if (!codeContainer) {
                console.warn('코드 컨테이너(.CodeMirror-code)를 찾을 수 없습니다.');
                return;
            }

            // 기존 코드 삭제
            codeContainer.innerHTML = '';

            // 🔹 <pre><code> 태그로 감싸서 코드 하이라이팅 적용
            const preElement = document.createElement('pre');
            const codeElement = document.createElement('code');
            codeElement.className = 'language-python'; // 파이썬 코드 하이라이팅 적용
            codeElement.textContent = fileContent;

            preElement.appendChild(codeElement);
            codeContainer.appendChild(preElement);

            // 🔹 코드 하이라이팅 라이브러리 Prism.js 적용
            if (window.Prism) {
                Prism.highlightElement(codeElement);
            }

            console.log('파일이 성공적으로 표시되었습니다.');
        } catch (error) {
            console.error('파일을 처리하는 중 오류가 발생했습니다:', error);
        }
    }


    function clearCodeContainer() {
        const codeContainer = document.querySelector('.CodeMirror-code');
        if (!codeContainer) {
            console.warn('test : 코드 컨테이너(.CodeMirror-code)를 찾을 수 없습니다.');
            return;
        }
        codeContainer.innerHTML = '';
    }

    window.addEventListener('load', () => {
        try {
            const problemMatch = currentUrl.match(/^https:\/\/www\.acmicpc\.net\/problem\/\d+$/);
            const submitMatch = currentUrl.match(/^https:\/\/www\.acmicpc\.net\/submit\/\d+\/\d+$/);

            if (!problemMatch && !submitMatch) {
                console.log('test : 조건에 맞지 않는 URL입니다. 스크립트를 실행하지 않습니다.');
                return;
            }

            console.log('test : 조건에 맞는 URL입니다.');
            createNextAndSimilarButtons();
        } catch (error) {
            console.error('test : 스크립트 실행 중 오류 발생:', error);
        }
    });
})();
