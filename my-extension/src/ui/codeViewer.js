 import { fetchFileContent } from '../api/api.js';

 export async function displayExternalFileContent(fileUrl) {
     try {
         const fileContent = await fetchFileContent(fileUrl);
         const codeContainer = document.querySelector('.CodeMirror-code');

         if (!codeContainer) {
             console.warn('코드 컨테이너(.CodeMirror-code)를 찾을 수 없습니다.');
             return;
         }

         // 기존 내용 삭제 후 새 콘텐츠 추가
         clearCodeContainer();

         const preElement = document.createElement('pre');
         const codeElement = document.createElement('code');

         // Prism.js 코드 하이라이팅을 위해 언어 클래스 추가
         codeElement.className = 'language-python';
         codeElement.textContent = fileContent;

         // 코드 스타일 유지 (줄바꿈 적용)
         preElement.style.whiteSpace = 'pre-wrap';
         preElement.style.wordBreak = 'break-word';

         preElement.appendChild(codeElement);
         codeContainer.appendChild(preElement);

         console.log(document.querySelector('.CodeMirror-code').innerHTML);

         // Prism.js 로드 여부 확인 후 하이라이팅 적용
         if (window.Prism) {
             Prism.highlightElement(codeElement);
         } else {
             console.warn('Prism.js가 로드되지 않았습니다. 동적으로 로드합니다.');
             loadPrismJS(() => {
                 Prism.highlightElement(codeElement);
             });
         }
     } catch (error) {
         console.error('displayExternalFileContent error:', error);
     }
 }

 // 코드 컨테이너 내용 지우기 (안전한 방식)
 export function clearCodeContainer() {
     const codeContainer = document.querySelector('.CodeMirror-code');
     if (codeContainer) {
         while (codeContainer.firstChild) {
             codeContainer.removeChild(codeContainer.firstChild);
         }
     }
 }

 // Prism.js가 이미 로드되었는지 확인 후 로드
 function loadPrismJS(callback) {
     if (window.Prism) {
         callback();
         return;
     }

     const script = document.createElement('script');
     script.src = chrome.runtime.getURL("src/lib/prism.js"); // 🔥 경로 확인!
     script.onload = callback;
     document.head.appendChild(script);
 }

 // Prism.css도 추가 (없으면 스타일 적용이 안 됨)
 (function loadPrismCSS() {
     const existingLink = document.querySelector('link[href*="prism.css"]');
     if (!existingLink) {
         const link = document.createElement('link');
         link.rel = 'stylesheet';
         link.href = chrome.runtime.getURL("src/lib/prism.css"); // 🔥 경로 확인!
         document.head.appendChild(link);
     }
 })();
