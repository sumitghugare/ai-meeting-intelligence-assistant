// // // ======================================
// // // RUN ANALYSIS
// // // ======================================

// // async function runAnalysis() {

// //   const source =
// //     document.getElementById(
// //       "sourceInput"
// //     ).value.trim();

// //   if(source === "") {

// //     alert("Please enter source");

// //     return;
// //   }

// //   const runBtn =
// //     document.querySelector(
// //       ".run-btn"
// //     );

// //   runBtn.innerText =
// //     "Analyzing...";

// //   runBtn.disabled = true;

// //   // LOADING TEXT

// //   document.getElementById(
// //     "summary"
// //   ).innerText =
// //     "Analyzing meeting...";

// //   try {

// //     const response = await fetch(
// //       "http://127.0.0.1:8000/analyze",
// //       {

// //         method: "POST",

// //         headers: {
// //           "Content-Type":
// //           "application/json"
// //         },

// //         body: JSON.stringify({

// //           source: source,

// //           language: "english"

// //         })

// //       }
// //     );

// //     const data =
// //       await response.json();

// //     console.log(data);

// //     // RESET BUTTON

// //     runBtn.innerText =
// //       "▶ Run Analysis";

// //     runBtn.disabled = false;

// //     // CHECK ERROR

// //     if(!data.success) {

// //       alert(data.summary);

// //       return;
// //     }

// //     // =========================
// //     // TITLE
// //     // =========================

// //     document.getElementById(
// //       "meetingTitle"
// //     ).innerText =
// //       data.title;

// //     // =========================
// //     // SUMMARY
// //     // =========================

// //     document.getElementById(
// //       "summary"
// //     ).innerText =
// //       data.summary;

// //     // =========================
// //     // TRANSCRIPT
// //     // =========================

// //     document.getElementById(
// //       "transcript"
// //     ).innerHTML = `
// //       <pre>${data.transcript}</pre>
// //     `;

// //     // =========================
// //     // ACTION ITEMS
// //     // =========================

// //     const actions =
// //       document.getElementById(
// //         "actions"
// //       );

// //     actions.innerHTML = "";

// //     data.action_items.forEach(
// //       item => {

// //         actions.innerHTML += `
// //           <li>${item}</li>
// //         `;

// //     });

// //     // =========================
// //     // DECISIONS
// //     // =========================

// //     const decisions =
// //       document.getElementById(
// //         "decisions"
// //       );

// //     decisions.innerHTML = "";

// //     data.key_decisions.forEach(
// //       item => {

// //         decisions.innerHTML += `
// //           <li>${item}</li>
// //         `;

// //     });

// //     // =========================
// //     // QUESTIONS
// //     // =========================

// //     const questions =
// //       document.getElementById(
// //         "questions"
// //       );

// //     questions.innerHTML = "";

// //     data.questions.forEach(
// //       item => {

// //         questions.innerHTML += `
// //           <li>${item}</li>
// //         `;

// //     });

// //   }

// //   catch(error) {

// //     console.log(error);

// //     runBtn.innerText =
// //       "▶ Run Analysis";

// //     runBtn.disabled = false;

// //     alert(
// //       "Backend connection failed"
// //     );

// //   }

// // }

// // // ======================================
// // // CHAT SYSTEM
// // // ======================================

// // async function sendMessage() {

// //   const input =
// //     document.getElementById(
// //       "chatInput"
// //     );

// //   const question =
// //     input.value.trim();

// //   const chatBody =
// //     document.getElementById(
// //       "chatBody"
// //     );

// //   if(question === "")
// //     return;

// //   // USER MESSAGE

// //   const userDiv =
// //     document.createElement("div");

// //   userDiv.classList.add(
// //     "message",
// //     "user"
// //   );

// //   userDiv.innerText =
// //     question;

// //   chatBody.appendChild(
// //     userDiv
// //   );

// //   input.value = "";

// //   // LOADING

// //   const loadingDiv =
// //     document.createElement("div");

// //   loadingDiv.classList.add(
// //     "message",
// //     "bot"
// //   );

// //   loadingDiv.innerText =
// //     "Thinking...";

// //   chatBody.appendChild(
// //     loadingDiv
// //   );

// //   chatBody.scrollTop =
// //     chatBody.scrollHeight;

// //   try {

// //     const response = await fetch(
// //       "http://127.0.0.1:8000/chat",
// //       {

// //         method: "POST",

// //         headers: {
// //           "Content-Type":
// //           "application/json"
// //         },

// //         body: JSON.stringify({

// //           question: question

// //         })

// //       }
// //     );

// //     const data =
// //       await response.json();

// //     // REMOVE LOADING

// //     loadingDiv.remove();

// //     // BOT MESSAGE

// //     const botDiv =
// //       document.createElement(
// //         "div"
// //       );

// //     botDiv.classList.add(
// //       "message",
// //       "bot"
// //     );

// //     botDiv.innerText =
// //       data.answer;

// //     chatBody.appendChild(
// //       botDiv
// //     );

// //     chatBody.scrollTop =
// //       chatBody.scrollHeight;

// //   }

// //   catch(error) {

// //     console.log(error);

// //     loadingDiv.innerText =
// //       "Chat backend failed.";

// //   }

// // }

// // // ======================================
// // // ENTER KEY SUPPORT
// // // ======================================

// // document
// //   .getElementById("chatInput")
// //   .addEventListener("keypress", function(e) {

// //     if(e.key === "Enter") {

// //       sendMessage();

// //     }

// // });
// // ======================================
// // RUN ANALYSIS
// // ======================================

// async function runAnalysis() {

//   const source =
//     document.getElementById(
//       "sourceInput"
//     ).value;

//   if(source === "") {

//     alert("Please enter source");

//     return;
//   }

//   // LOADING

//   document.getElementById(
//     "summary"
//   ).innerText =
//     "Analyzing meeting...";

//   try {

//     // ======================================
//     // API CALL
//     // ======================================

//     const response = await fetch(
//       "http://127.0.0.1:8000/analyze",
//       {

//         method: "POST",

//         headers: {
//           "Content-Type":
//           "application/json"
//         },

//         body: JSON.stringify({

//           source: source,
//           language: "english"

//         })

//       }
//     );

//     // ======================================
//     // RESPONSE JSON
//     // ======================================

//     const data =
//       await response.json();

//     console.log(data);

//     // ======================================
//     // TITLE
//     // ======================================

//     document.getElementById(
//       "meetingTitle"
//     ).innerText =
//       data.title || "No Title";

//     // ======================================
//     // SUMMARY
//     // ======================================

//     document.getElementById(
//       "summary"
//     ).innerText =
//       data.summary || "No Summary";

//     // ======================================
//     // TRANSCRIPT
//     // ======================================

//     document.getElementById(
//       "transcript"
//     ).innerHTML = `
//       <pre>
// ${data.transcript || "No Transcript"}
//       </pre>
//     `;

//     // ======================================
//     // ACTION ITEMS
//     // ======================================

//     const actions =
//       document.getElementById(
//         "actions"
//       );

//     actions.innerHTML = "";

//     if(
//       Array.isArray(data.action_items)
//     ) {

//       data.action_items.forEach(
//         item => {

//         actions.innerHTML += `
//           <li>${item}</li>
//         `;

//       });

//     }

//     else {

//       actions.innerHTML =
//         "<li>No action items</li>";

//     }

//     // ======================================
//     // DECISIONS
//     // ======================================

//     const decisions =
//       document.getElementById(
//         "decisions"
//       );

//     decisions.innerHTML = "";

//     if(
//       Array.isArray(data.key_decisions)
//     ) {

//       data.key_decisions.forEach(
//         item => {

//         decisions.innerHTML += `
//           <li>${item}</li>
//         `;

//       });

//     }

//     else {

//       decisions.innerHTML =
//         "<li>No decisions</li>";

//     }

//     // ======================================
//     // QUESTIONS
//     // ======================================

//     const questions =
//       document.getElementById(
//         "questions"
//       );

//     questions.innerHTML = "";

//     if(
//       Array.isArray(data.questions)
//     ) {

//       data.questions.forEach(
//         item => {

//         questions.innerHTML += `
//           <li>${item}</li>
//         `;

//       });

//     }

//     else {

//       questions.innerHTML =
//         "<li>No questions</li>";

//     }

//   }

//   catch(error) {

//     console.log(error);

//     alert(
//       "Frontend rendering failed"
//     );

//   }

// }

// // ======================================
// // CHAT SYSTEM
// // ======================================

// async function sendMessage() {

//   const input =
//     document.getElementById(
//       "chatInput"
//     );

//   const question =
//     input.value.trim();

//   const chatBody =
//     document.getElementById(
//       "chatBody"
//     );

//   if(question === "")
//     return;

//   // USER MESSAGE

//   const userDiv =
//     document.createElement("div");

//   userDiv.classList.add(
//     "message",
//     "user"
//   );

//   userDiv.innerText =
//     question;

//   chatBody.appendChild(
//     userDiv
//   );

//   input.value = "";

//   // LOADING

//   const loadingDiv =
//     document.createElement("div");

//   loadingDiv.classList.add(
//     "message",
//     "bot"
//   );

//   loadingDiv.innerText =
//     "Thinking...";

//   chatBody.appendChild(
//     loadingDiv
//   );

//   try {

//     const response = await fetch(
//       "http://127.0.0.1:8000/chat",
//       {

//         method: "POST",

//         headers: {
//           "Content-Type":
//           "application/json"
//         },

//         body: JSON.stringify({

//           question: question

//         })

//       }
//     );

//     const data =
//       await response.json();

//     loadingDiv.remove();

//     // BOT MESSAGE

//     const botDiv =
//       document.createElement(
//         "div"
//       );

//     botDiv.classList.add(
//       "message",
//       "bot"
//     );

//     botDiv.innerText =
//       data.answer || "No Answer";

//     chatBody.appendChild(
//       botDiv
//     );

//     chatBody.scrollTop =
//       chatBody.scrollHeight;

//   }

//   catch(error) {

//     console.log(error);

//     loadingDiv.innerText =
//       "Chat failed.";

//   }

// }
// ======================================
// API BASE URL
// ======================================




// const API_URL = "http://127.0.0.1:8000";

// // ======================================
// // RUN ANALYSIS
// // ======================================

// async function runAnalysis() {

//     const source =
//         document.getElementById(
//             "sourceInput"
//         ).value.trim();

//     if(source === "") {

//         alert(
//             "Please enter source"
//         );

//         return;
//     }

//     // ======================================
//     // LOADING UI
//     // ======================================

//     document.getElementById(
//         "summary"
//     ).innerText =
//         "Analyzing meeting...";

//     try {

//         console.log(
//             "Starting analysis..."
//         );

//         // ======================================
//         // FETCH API
//         // ======================================

//         const response =
//             await fetch(
//                 `${API_URL}/analyze`,
//                 {

//                     method: "POST",

//                     headers: {
//                         "Content-Type":
//                         "application/json"
//                     },

//                     body: JSON.stringify({

//                         source: source,

//                         language: "english"

//                     })

//                 }
//             );

//         console.log(response);

//         // ======================================
//         // CHECK RESPONSE
//         // ======================================

//         if(!response.ok){

//             throw new Error(
//                 "Server Error"
//             );

//         }

//         // ======================================
//         // RESPONSE JSON
//         // ======================================

//         const data =
//             await response.json();

//         console.log(data);

//         // ======================================
//         // CHECK SUCCESS
//         // ======================================

//         if(!data.success){

//             alert(data.summary);

//             return;

//         }

//         // ======================================
//         // TITLE
//         // ======================================

//         document.getElementById(
//             "meetingTitle"
//         ).innerText =
//             data.title || "No Title";

//         // ======================================
//         // SUMMARY
//         // ======================================

//         document.getElementById(
//             "summary"
//         ).innerText =
//             data.summary || "No Summary";

//         // ======================================
//         // TRANSCRIPT
//         // ======================================

//         document.getElementById(
//             "transcript"
//         ).innerHTML = `

// <pre>
// ${data.transcript || ""}
// </pre>

//         `;

//         // ======================================
//         // ACTION ITEMS
//         // ======================================

//         const actions =
//             document.getElementById(
//                 "actions"
//             );

//         actions.innerHTML = "";

//         if(
//             Array.isArray(
//                 data.action_items
//             )
//         ) {

//             data.action_items.forEach(
//                 item => {

//                     actions.innerHTML += `
// <li>${item}</li>
//                     `;

//                 }
//             );

//         }

//         else {

//             actions.innerHTML =
//                 "<li>No action items</li>";

//         }

//         // ======================================
//         // DECISIONS
//         // ======================================

//         const decisions =
//             document.getElementById(
//                 "decisions"
//             );

//         decisions.innerHTML = "";

//         if(
//             Array.isArray(
//                 data.key_decisions
//             )
//         ) {

//             data.key_decisions.forEach(
//                 item => {

//                     decisions.innerHTML += `
// <li>${item}</li>
//                     `;

//                 }
//             );

//         }

//         else {

//             decisions.innerHTML =
//                 "<li>No decisions</li>";

//         }

//         // ======================================
//         // QUESTIONS
//         // ======================================

//         const questions =
//             document.getElementById(
//                 "questions"
//             );

//         questions.innerHTML = "";

//         if(
//             Array.isArray(
//                 data.questions
//             )
//         ) {

//             data.questions.forEach(
//                 item => {

//                     questions.innerHTML += `
// <li>${item}</li>
//                     `;

//                 }
//             );

//         }

//         else {

//             questions.innerHTML =
//                 "<li>No questions</li>";

//         }

//         console.log(
//             "Analysis completed"
//         );

//     }

//     catch(error) {

//         console.log(error);

//         alert(
//             "Backend connection failed"
//         );

//     }

// }

// // ======================================
// // CHAT SYSTEM
// // ======================================

// async function sendMessage() {

//     const input =
//         document.getElementById(
//             "chatInput"
//         );

//     const question =
//         input.value.trim();

//     if(question === "")
//         return;

//     const chatBody =
//         document.getElementById(
//             "chatBody"
//         );

//     // ======================================
//     // USER MESSAGE
//     // ======================================

//     const userDiv =
//         document.createElement(
//             "div"
//         );

//     userDiv.classList.add(
//         "message",
//         "user"
//     );

//     userDiv.innerText =
//         question;

//     chatBody.appendChild(
//         userDiv
//     );

//     input.value = "";

//     // ======================================
//     // LOADING
//     // ======================================

//     const loadingDiv =
//         document.createElement(
//             "div"
//         );

//     loadingDiv.classList.add(
//         "message",
//         "bot"
//     );

//     loadingDiv.innerText =
//         "Thinking...";

//     chatBody.appendChild(
//         loadingDiv
//     );

//     chatBody.scrollTop =
//         chatBody.scrollHeight;

//     try {

//         const response =
//             await fetch(
//                 `${API_URL}/chat`,
//                 {

//                     method: "POST",

//                     headers: {
//                         "Content-Type":
//                         "application/json"
//                     },

//                     body: JSON.stringify({

//                         question: question

//                     })

//                 }
//             );

//         if(!response.ok){

//             throw new Error(
//                 "Chat Error"
//             );

//         }

//         const data =
//             await response.json();

//         loadingDiv.remove();

//         // ======================================
//         // BOT MESSAGE
//         // ======================================

//         const botDiv =
//             document.createElement(
//                 "div"
//             );

//         botDiv.classList.add(
//             "message",
//             "bot"
//         );

//         botDiv.innerText =
//             data.answer || "No answer";

//         chatBody.appendChild(
//             botDiv
//         );

//         chatBody.scrollTop =
//             chatBody.scrollHeight;

//     }

//     catch(error) {

//         console.log(error);

//         loadingDiv.innerText =
//             "Chat failed.";

//     }

// }

