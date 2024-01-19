# Chatbot for FAQs - Task 3

In this section, we delve into the creation of a basic chatbot application to answer frequently asked questions (FAQs) on a specific topic. Users can interact with the chatbot by typing questions, and the chatbot will provide relevant answers.

## Description

Created a basic chatbot application using GPT-3-like capabilities to address common questions users may have on a specific topic. This project serves as an introduction to integrating a chatbot into a website or application, showcasing the fundamental principles of conversational interfaces.

## Output of the code

![Alt text](https://github.com/bhaktim19/Slash_Mark-Prompt-Engineer-Intern/blob/main/Images/Output.png)



Chatbot Project Setup Instructions 
===================================

1. **Python Installation:**
   - Download and install Python 3.9.7 from the official Python website: https://www.python.org/downloads/.

2. **Update pip (Python Package Manager):**
   - Open your command line or terminal and run the following command to update `pip` to the latest version:
     ```
     pip install --upgrade pip
     ```

3. **Create a Project Folder:**
   - Create a folder for your project. You can name it whatever you like, e.g., "ChatbotProject."

4. **Create a Virtual Environment (Optional but Recommended):**
   - To create a virtual environment, run the following commands in your project folder:
     ```
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       venv\Scripts\activate
       ```
     - On macOS and Linux:
       ```
       source venv/bin/activate
       ```

5. **Install Required Libraries:**
   - Create a `requirements.txt` file in your project folder and add the following lines:
     ```
     python==3.9.7
     pip==21.3.1
     numpy==1.21.2
     transformers==4.11.3
     # Add any other project-specific libraries here
     ```
   - Install the libraries using the following command:
     ```
     pip install -r requirements.txt
     ```

6. **Install Visual Studio Code (VS Code):**
   - Download and install Visual Studio Code from the official website: https://code.visualstudio.com/.

7. **Install VS Code Extensions (Optional):**
   - Open VS Code and go to the Extensions view (click on the square icon on the left sidebar).
   - Search for and install any VS Code extensions you find useful for your development, such as Python extensions or code formatting extensions.

8. **Create a Chatbot Script:**
   - Create a Python file for your chatbot code in the project folder. Name it, e.g., "chatbot.py."

9. **Add Chatbot Code:**
   - Create your chatbot code in the "chatbot.py" file. You can use the provided sample code as a starting point. Add more FAQs and Rules to the directory.
   - Now the chatbot code is ready to run.

10. **Run Your Chatbot:**
    - Open a terminal within VS Code or use your system's command line to navigate to the project folder.
    - Activate the virtual environment if you created one.
    - Run your chatbot script using the following command:
      ```
      python chatbot.py
      ```

11. **Interact with Your Chatbot:**
    - Your chatbot will now be running in the terminal or command line. You can interact with it by typing input, and it will respond based on the rules and FAQs you defined.

12. **Exit Your Chatbot:**
    - To exit your chatbot, type 'bye' in the terminal, and it will respond with a goodbye message.

That's it! You've successfully set up your chatbot project with all the required instructions in a single `setup_instructions.txt` file.
