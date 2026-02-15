<!-- Generated: 2026-02-15T02:59:22.771602Z | Model: gpt-4.1-nano -->

# Desktop-Chat-App

## Overview
The **Desktop-Chat-App** is a cross-platform desktop application designed for real-time text communication, primarily aimed at couples or small groups. Built with JavaScript and Electron, it provides a simple chat interface with integrated text-to-speech (TTS) functionality, allowing users to hear incoming messages. The application includes a WebSocket server component for real-time message exchange, making it suitable for local or networked environments.

This repository is intended for developers interested in customizing or extending a lightweight chat application with TTS features, or for users seeking a self-hosted chat solution with voice capabilities.

## Key Features
- Cross-platform desktop application (Windows, macOS, Linux)
- Real-time chat via WebSocket
- User-configurable server and room selection
- Text-to-speech (TTS) for incoming messages
- Simple, minimal UI
- Modular architecture separating client and server code
- Built with Electron for desktop deployment
- Server implemented with Node.js and WebSocket

## Architecture / How It Works
The repository comprises two main components:

1. **Client Application (Electron-based GUI):**
   - Located in the `app` directory.
   - Provides a user interface for connecting to a WebSocket server, joining rooms, and sending messages.
   - Uses `main.js` for core Electron setup, `renderer.js` for UI logic, and `preload.js` for secure IPC communication.
   - Implements OS-specific TTS commands to speak incoming messages.

2. **WebSocket Server:**
   - Located in the `server` directory.
   - Uses the `ws` library to handle WebSocket connections.
   - Manages chat rooms and broadcasts messages to clients within the same room.
   - Handles user join events and message relaying.

The client communicates with the server via WebSocket, sending join requests and chat messages. Incoming messages are displayed in the UI, and non-user messages are spoken aloud using TTS.

## Notable Folders/Files
- **`app/`**: Contains the Electron app code, including UI (`index.html`), main process (`main.js`), preload scripts (`preload.js`), and renderer logic (`renderer.js`).
- **`server/`**: Contains the WebSocket server code (`server.js`) that manages real-time message exchange.
- **`pyproject.toml`**: Indicates some Python dependencies, possibly for other functionalities or integrations not detailed here.
- **`package.json` & `package-lock.json`**: Define dependencies and lock versions for both client (`app`) and server (`server`) projects.
- **`.gitignore`, `LICENSE`, `README.md`**: Standard project files.

## Setup & Run
### Prerequisites
- Node.js (version >= 12 recommended)
- For Linux TTS: `espeak` must be installed
- For Windows TTS: PowerShell available (default)
- For macOS TTS: `say` command available (default)
- Optional: Python 3.11 if additional backend features are used (not explicitly detailed)

### Installing Dependencies
Navigate to each directory and install dependencies:

```bash
# For the client (Electron app)
cd app
npm install

# For the server
cd ../server
npm install
```

### Running the Application
#### Start the WebSocket Server
```bash
cd server
npm start
```
This runs the server on default port 8080.

#### Launch the Electron Client
```bash
cd ../app
npm start
```
This opens the desktop chat interface.

## How to Use
1. **Connect to Server:**
   - Enter the WebSocket server URL (e.g., `ws://localhost:8080`) in the "Server" input.
   - Optionally specify a room ID (default is `room1`) and your username.
   - Click **Connect**.

2. **Chat:**
   - Type your message in the input box.
   - Press **Send** or hit Enter.
   - Your message appears in the chat window.
   - Incoming messages from others are displayed and automatically spoken aloud via TTS.

3. **Listening:**
   - Incoming messages from other users trigger the OS-level TTS to read the message aloud, enhancing accessibility and convenience.

## Testing / CI
No explicit testing or CI configurations are present in the provided files. 

## Deployment
- The client is packaged as an Electron app, which can be built into standalone executables using Electron's packaging tools (not detailed here).
- The server runs as a Node.js process and can be deployed on any machine supporting Node.js.

## Contribution Notes
No specific contribution guidelines are provided in the repository. 

## Limitations / TODOs (Inferred)
- **Security & Authentication:** No mention of user authentication or encryption; suitable for trusted environments.
- **Scalability:** Designed for small groups; not optimized for large-scale deployments.
- **Platform-specific TTS:** Relies on system commands (`say`, `powershell`, `espeak`); may require setup on Linux.
- **UI/UX:** Minimal UI; potential for enhancements.
- **Features:** No file sharing, message history, or advanced moderation.
- **Testing & CI:** No automated tests or CI/CD pipelines are evident.
- **Documentation:** Basic usage is inferred; more detailed instructions could improve usability.

---

For further details, refer to the individual files and scripts within the repository.
