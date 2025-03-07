# Code Mate - VS Code Extension & ChatBot Application
To reduce the load in your PC just run the normal lama version, we will run the finetuned model at the Finals

## Prerequisites
Ensure you have the following installed:
- **Olama** (Required for chatbot functionality)
- **Python 3.10+** (Check with `python --version`)
- **pip** (Check with `pip --version`)
- **Node.js & npm** (Check with `node -v` and `npm -v`)
- **VS Code** with `vsce` (VS Code Extension Manager)

## 1. Setting Up the Flask Backend
### Step 1: Clone the Repository
```sh
git clone <your-repo-url>
cd your-repo
```

### Step 2: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 3: Run the Flask Server
```sh
python app.py
```
The Flask server will run at **http://127.0.0.1:5000**.

---

## 2. Running the Frontend
- All necessary code is already included in **index.html**.
- Simply open the file in a browser or integrate it with the Flask backend.

---

## 3. Setting Up the VS Code Extension
### Step 1: Navigate to the Extension Directory
```sh
cd vscode-extension
```

### Step 2: Install Dependencies
```sh
npm install
```

### Step 3: Build the Extension
```sh
npm run build
```

### Step 4: Run the Extension
Open VS Code, add the extension code, and follow the build process above.

---

## 4. Running the Full Application
1. **Install Olama** (Required for chatbot functionality)
2. **Start the Flask server** (`python gdsc.py`)
3. **Open VS Code and test the extension**
4. The extension should communicate with Flask and return AI-generated responses.

---

## 5. Debugging Issues
### Flask Issues
- Ensure Flask is running on **port 5000**.
- Check the terminal for errors and fix missing dependencies.

### VS Code Extension Issues
- Run `npm install` again if dependencies are missing.
- Restart VS Code after installing the extension.

Enjoy Folks -- 6th Sense Coders ;)

