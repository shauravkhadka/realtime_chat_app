# Real-Time Chat Application

This is a real-time chat application built with Python Flask, Flask-SocketIO, and Apache ActiveMQ Artemis.

## Local Configuration

Follow these steps to set up and run the chat application locally on your machine:

### Prerequisites

- Python 3.x installed on your system
- Internet connection (for accessing JavaScript libraries)

### Installation

1. Clone this repository to your local machine:

    ```
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```
    cd realtime_chat_app
    ```

3. Install Python dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Flask server by running the following command:

    ```
    python app.py
    ```

2. Open a web browser and visit [http://localhost:5000](http://localhost:5000) to access the chat application.

### Usage

- Enter your name in the provided form and click "Join Chat" to enter the chat room.
- Type your message in the input field at the bottom of the page and click "Send" to broadcast your message to other users in the chat room.
- Messages will be displayed in real-time as they are sent by other users.

### Dependencies

- Flask: Web framework for Python
- Flask-SocketIO: WebSocket integration for Flask
- stomp.py: Python STOMP client for Apache ActiveMQ Artemis
- socket.io: JavaScript library for WebSocket communication

## Credits

- This project was created by Shaurav Khadka.

