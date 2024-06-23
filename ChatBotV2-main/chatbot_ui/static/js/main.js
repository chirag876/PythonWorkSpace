const popup = document.querySelector('.chat-popup');
const chatBtn = document.querySelector('.chat-btn');
const chat_popup = document.querySelector('.popuptext')
const submitBtn = document.querySelector('.submit');
const micBtn = document.querySelector('.mic');
const sound = document.querySelector('.sound');
const chatArea = document.querySelector('.chat-area');
var inputElm = document.querySelector('input');
const typeStatus = document.querySelector(".type-status");



// function synthVoice(text) {
//     const synth = window.speechSynthesis;
//     const utterance = new SpeechSynthesisUtterance();
//     utterance.text = text;
//     synth.speak(utterance);
// }

//chat button toggler
chatBtn.addEventListener('click', () => {
    popup.classList.toggle('show');
    var chatpopup = document.getElementById("myPopup");
    chatpopup.classList.toggle("show");
    fetch("/web_ui?Message=" + "hello")
            .then(async (response) => {
                chatArea.innerHTML += await response.text();
                typeStatus.innerHTML = "Online"
                chatArea.scrollTop = chatArea.scrollHeight;
            });
})
chat_popup.addEventListener('click', () => {
    popup.classList.toggle('show');
    var chatpopup = document.getElementById("myPopup");
    chatpopup.classList.toggle("show");
})

// User Message Input Handling
const submitHandler = () => {
    let userInput = inputElm.value;
    if (userInput != "") {
        let temp = `<div class="out-msg">
        <span class="my-msg">${userInput}</span>
        <img src="static/images/person.jpg" class="avatar">
        </div>`;
        chatArea.insertAdjacentHTML("beforeend", temp);
        inputElm.value = '';

        typeStatus.innerHTML = "Typing..."

        fetch("/web_ui?Message=" + userInput)
            .then(async (response) => {
                chatArea.innerHTML += await response.text();
                typeStatus.innerHTML = "Online"
                chatArea.scrollTop = chatArea.scrollHeight;
            });
    };
}

submitBtn.addEventListener('click', submitHandler)

// Send message after pressing enter button
document.querySelector(".input-area>input").addEventListener("keypress", (e) => {
    if (e.charCode === 13 && e.target.value !== "")
        submitHandler()
})

// Chatbot reset function
function reset(){
    let welcomeMsgs = "";
    let msgs = document.querySelectorAll(".income-msg");
    for(var i =0;i<2;i++){
        welcomeMsgs +=`<div class="income-msg"> ${msgs[i].innerHTML}</div>`
    };
    chatArea.innerHTML = welcomeMsgs;
    fetch("/web_ui?Message=" + "hello")
            .then(async (response) => {
                chatArea.innerHTML += await response.text();
                typeStatus.innerHTML = "Online"
                chatArea.scrollTop = chatArea.scrollHeight;
            });
   
}

document.querySelector(".reset-btn").addEventListener("click", () => { reset() });


// working of options buttons
function optionHandler(e) {
    let btnname = e.getAttribute("name");
    let temp = `<div class="out-msg">
    <span class="my-msg">${btnname}</span>
    <img src="static/images/person.jpg" class="avatar">
    </div>`;
    chatArea.insertAdjacentHTML("beforeend", temp);
    typeStatus.innerHTML = "Typing..."
    fetch("/web_ui?Message=" + btnname)
    .then(async (response) => {
        chatArea.innerHTML += await response.text();
        typeStatus.innerHTML = "Online"
        chatArea.scrollTop = chatArea.scrollHeight;
    }) 
}

// Speech recognition Handling 
var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var recognition = new SpeechRecognition();
recognition.interimResults = false;

recognition.onresult = function(event) {
    var last = event.results.length -1;
    inputElm.value = event.results[last][0].transcript;
};

recognition.onspeechend = function() {
    recognition.stop();
    document.getElementsByName("text")[0].placeholder = "Type a message...";
    micBtn.innerHTML = `<i class="material-icons">mic</i>`
};

recognition.onerror = function(event) {
        console.log("Your browser does not support speech recognition" + event);
        document.getElementsByName("text")[0].placeholder = "Type a message...";
        micBtn.innerHTML = `<i class="material-icons">mic</i>`
}

micBtn.addEventListener('click', function(){
    sound.play();
    document.getElementsByName("text")[0].placeholder = "Listening...";
    micBtn.innerHTML = `<i class="material-icons">mic_off</i>`;
    recognition.start();
});