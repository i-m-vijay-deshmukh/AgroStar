// chatbot.js - AI Chatbot Integration

document.querySelector(".chatbot-btn").addEventListener("click", () => {
    let userMessage = prompt("Ask AgroBot 🤖:");
    if (userMessage) {
        getChatbotResponse(userMessage);
    }
});

async function getChatbotResponse(message) {
    const chatbotAPI = "https://api.openai.com/v1/completions";
    const apiKey = "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";

    const response = await fetch(chatbotAPI, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: "gpt-4",
            prompt: message,
            max_tokens: 100
        })
    });

    const data = await response.json();
    alert("AgroBot: " + data.choices[0].text);
}
