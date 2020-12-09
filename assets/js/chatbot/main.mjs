

class Chat {

    constructor(url) {
        this.url = url;
    }

    /**
     * Print a given message to the chat, send it to the bot,
     * and print the returned response to the chat.
     * @param {string} message - The message to send.
     **/
    sendMessage(message) {

        // Display the message written bu user to the chat
        this.displayMessage('user', message)

        // Send the message to the bot and display its response
        this.sendRequest('Hello').then(response => {
            this.displayMessage('bot', response.message)

            // TODO: implement a way to recognize Bot and narrator messages
        })
    }


    displayMessage(type, message) {
        // TODO: Message appear to the UI
    }


    /**
     * Send a POST request to the ChatBot REST API.
     * Return a the message responded by the bot.
     * @param {string} message - The message to send.
     * @param {number} [sender] - The user which send a message.
     * @return {json} - A json object with "message" and "sender" keys.
     **/
    async sendRequest(message, sender = 1) {

        // Send a JSON request with the message and the sender
        const response = await fetch(this.url, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "message": message,
                "sender": sender
            })
        });

        // Return the response message
        return await response.json();
    }
}


export { Chat };