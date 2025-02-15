(function() {
    const externalFileUrls = [
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
            await displayExternalFileContent(currentFileIndex);
        });

        similarButton.addEventListener('click', (event) => {
            event.preventDefault();
            event.stopPropagation();

            if (!isSimilarCodeDisplayed) {
                displayExternalFileContent(currentFileIndex);
                isSimilarCodeDisplayed = true;
            } else {
                clearCodeContainer();
                isSimilarCodeDisplayed = false;
            }
        });
    }

    async function displayExternalFileContent(index) {
        const fileUrl = externalFileUrls[index];
        console.log('test : 외부 파일 요청 URL:', fileUrl);

        try {
            const response = await fetch(fileUrl);
            if (!response.ok) {
                throw new Error(`test : 파일을 읽을 수 없습니다: ${response.statusText}`);
            }

            const fileContent = await response.text();
            const codeContainer = document.querySelector('.CodeMirror-code');
            if (!codeContainer) {
                console.warn('test : 코드 컨테이너(.CodeMirror-code)를 찾을 수 없습니다.');
                return;
            }

            codeContainer.innerHTML = '';
            const preElement = document.createElement('pre');
            preElement.textContent = fileContent;
            preElement.style.whiteSpace = 'pre-wrap';
            preElement.style.fontFamily = 'monospace';
            preElement.style.fontSize = '14px';
            preElement.style.lineHeight = '1.5';

            codeContainer.appendChild(preElement);
            console.log('test : 파일이 성공적으로 표시되었습니다.');
        } catch (error) {
            console.error('test : 파일을 처리하는 중 오류가 발생했습니다:', error);
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
