function submitQuestion() {
    var questionInput = document.getElementById('questionInput');
    var question = questionInput.value.trim();
    if (question !== '') {
        fetch('/submit_question', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: 'question=' + encodeURIComponent(question)
        })
        .then(response => response.json())
        .then(data => {
            displayMessage(question, data.answer);
            questionInput.value = ''; // Clear input field
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Please enter a question');
    }
}

function displayMessage(question, answer) {
    var messageContainer = document.getElementById('messageContainer');
    var messageDiv = document.createElement('div');
    messageDiv.classList.add('message');
    var questionDiv = document.createElement('div');
    questionDiv.classList.add('question');
    questionDiv.textContent = 'Question: ' + question;
    var answerDiv = document.createElement('div');
    answerDiv.classList.add('answer');
    answerDiv.textContent = 'Answer: ' + answer;
    messageDiv.appendChild(questionDiv);
    messageDiv.appendChild(answerDiv);
    messageContainer.appendChild(messageDiv);
}
