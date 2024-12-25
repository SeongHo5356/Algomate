(function () {
    const externalFileUrls = [
        'http://127.0.0.1:8000/files/sample1.py',
        'http://127.0.0.1:8000/files/sample2.py',
        'http://127.0.0.1:8000/files/sample3.py',
        'http://127.0.0.1:8000/files/sample4.py',
    ];
    let currentFileIndex = 0;
    let isSimilarCodeDisplayed = false;
    let similarities = []; // 서버에서 받아온 유사도 배열

    const currentUrl = window.location.href;
    const pageTitle = document.title;
    const pageContent = document.body.innerText;

    const userIdElement = document.querySelector('.username');
    let userId = userIdElement ? userIdElement.innerText : null;

    console.log('Page data success0_user_id:', userId);

    if (currentUrl.includes("acmicpc.net/problem/")) {
        // 문제 페이지에서 서버에 데이터를 전송
        fetch('http://localhost:8000/submit-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                title: pageTitle,
                content: pageContent,
                userId: userId
            })
        })
            .then(response => response.json())
            .then(data => console.log('Page data success1_data:', data))
            .catch((error) => console.error('Page data error:', error));
    } else if (currentUrl.includes("acmicpc.net/submit/")) {
        // 내 제출 수정 페이지에서 제출 코드 서버로 전송
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

                fetch('http://localhost:8000/submit-code', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        code: codeContent,
                        problem_id: pageTitle,
                        userId: userId,
                        language: language,
                    }),
                })
                    .then((response) => response.json())
                    .then((data) => {
                        console.log('Code data success:', data);
                        if (data.similarities) {
                            similarities = data.similarities; // 유사도 배열 저장
                            updateSimilarityDisplay(); // 유사도 표시 업데이트
                        }
                    })
                    .catch((error) => console.error('Code data error:', error));
            } else {
                console.error("Code text area not found or empty");
            }
        };
    }

    function createNextAndSimilarButtons() {
        const languageSettingLink = document.querySelector('a[href="/setting/language"]');
        if (!languageSettingLink) {
            console.warn('test : "언어 설정" 버튼을 찾을 수 없습니다.');
            return;
        }

        const nextButton = document.createElement('button');
        nextButton.id = 'next-file-button';
        nextButton.textContent = '다음 파일';

        // 스타일 변경: 페이지 동질감을 위한 CSS
        nextButton.style.marginLeft = '8px'; // 페이지의 마진 규칙에 맞춤
        nextButton.style.padding = '6px 12px'; // 조화로운 패딩
        nextButton.style.fontSize = '13px'; // 기본 글꼴 크기
        nextButton.style.cursor = 'pointer';
        nextButton.style.backgroundColor = '#ffffff'; // 페이지 기본 배경색
        nextButton.style.border = 'none'; // 테두리 제거
        nextButton.style.borderRadius = '4px'; // 모서리를 부드럽게
        nextButton.style.color = '#0076C0'; // 페이지 텍스트 색상
        nextButton.style.fontFamily = 'inherit'; // 페이지와 동일한 글꼴
        nextButton.style.outline = 'none'; // 포커스 테두리 제거
        nextButton.style.transition = 'background-color 0.3s'; // 호버 시 부드러운 전환

        // 호버 스타일
        nextButton.addEventListener('mouseover', () => {
          nextButton.style.textDecoration = 'underline'; // 밑줄 추가
        });
        nextButton.addEventListener('mouseout', () => {
          nextButton.style.textDecoration = 'none'; // 밑줄 제거
        });

        const similarButton = document.createElement('button');
        similarButton.id = 'similar-code-button';
        similarButton.textContent = '유사한 코드 살펴보기';

        // 스타일 변경: nextButton과 동일한 스타일 적용
        similarButton.style.marginLeft = '2px'; // 페이지의 마진 규칙에 맞춤
        similarButton.style.padding = '6px 6px'; // 조화로운 패딩
        similarButton.style.fontSize = '13px'; // 기본 글꼴 크기
        similarButton.style.cursor = 'pointer';
        similarButton.style.backgroundColor = '#ffffff'; // 페이지 기본 배경색
        similarButton.style.border = 'none'; // 테두리 제거
        similarButton.style.borderRadius = '4px'; // 모서리를 부드럽게
        similarButton.style.color = '#0076C0'; // 페이지 텍스트 색상
        similarButton.style.fontFamily = 'inherit'; // 페이지와 동일한 글꼴
        similarButton.style.outline = 'none'; // 포커스 테두리 제거
        similarButton.style.transition = 'background-color 0.3s'; // 호버 시 부드러운 전환

        // 호버 스타일
        similarButton.addEventListener('mouseover', () => {
          similarButton.style.textDecoration = 'underline'; // 밑줄 추가
        });
        similarButton.addEventListener('mouseout', () => {
          similarButton.style.textDecoration = 'none'; // 밑줄 제거
        });

        languageSettingLink.parentNode.appendChild(nextButton);
        languageSettingLink.parentNode.appendChild(similarButton);

        nextButton.addEventListener('click', async (event) => {
            event.preventDefault();
            event.stopPropagation();

            currentFileIndex = (currentFileIndex + 1) % externalFileUrls.length;
            isSimilarCodeDisplayed = false;
            await displayExternalFileContent(currentFileIndex);
            updateSimilarityDisplay(); // 유사도 업데이트
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

            // 구문 강조를 위한 키워드 설정
            const keywordsBlue = ['import', 'def', 'while', 'for', 'in', 'if', 'and', 'else', 'elif']; // #006699
            const keywordsPurple = ['input', 'int', 'float', 'double', 'range', 'map', 'print']; // #3300AA

            // 키워드에 스타일을 적용하는 함수
            function highlightSyntax(content) {
                // 정규식으로 파란색 키워드 강조
                keywordsBlue.forEach(keyword => {
                    const regex = new RegExp(`\\b${keyword}\\b`, 'g');
                    content = content.replace(regex, `<span style="color: #006699;">${keyword}</span>`);
                });
                // 정규식으로 보라색 키워드 강조
                keywordsPurple.forEach(keyword => {
                    const regex = new RegExp(`\\b${keyword}\\b`, 'g');
                    content = content.replace(regex, `<span style="color: #3300AA;">${keyword}</span>`);
                });
                return content;
            }

            // 구문 강조 적용
            const highlightedContent = highlightSyntax(fileContent);

            // HTML로 삽입 (구문 강조된 텍스트 포함)
            preElement.innerHTML = highlightedContent;
            preElement.style.marginLeft = '0px'; // 페이지의 마진 규칙에 맞춤
            preElement.style.padding = '0px 0px'; // 조화로운 패딩
            preElement.style.whiteSpace = 'pre-wrap';
            preElement.style.fontFamily = 'Source Code Pro, Menlo, Monaco, monospace'; // 원하는 폰트 순서
            preElement.style.fontSize = '16px'; // 폰트 크기 조정
            preElement.style.lineHeight = '1.4'; // 줄 간격 조정
            preElement.style.backgroundColor = '#ffffff'; // 배경색 하얀색으로 설정
            preElement.style.color = '#000000'; // 텍스트 색상 검은색으로 설정
            preElement.style.padding = '10px'; // 내부 여백 추가
            preElement.style.borderRadius = '4px'; // 모서리를 약간 둥글게
            preElement.style.border = 'none'; // 테두리 완전히 제거
            preElement.style.outline = 'none'; // 포커스 아웃라인도 제거
            preElement.style.boxShadow = 'none'; // 그림자 효과 제거

            codeContainer.appendChild(preElement);
            console.log('test : 파일이 성공적으로 표시되었습니다.');
        } catch (error) {
            console.error('test : 파일을 처리하는 중 오류가 발생했습니다:', error);
        }
    }

    function updateSimilarityDisplay() {
    const languageElement = document.querySelector('#language_chosen > a.chosen-single > span');
    if (!languageElement) {
        console.warn('test : 유사도를 표시할 요소를 찾을 수 없습니다.');
        return;
    }

    const similarity = similarities[currentFileIndex] || 'N/A'; // 현재 파일에 대한 유사도
    languageElement.textContent = `유사도: ${similarity}%`; // 텍스트 업데이트
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
