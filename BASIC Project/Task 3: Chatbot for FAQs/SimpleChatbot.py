import random

# Define a dictionary of ChatGPT-related questions and their answers
chatgpt_faqs = {
    "what is chatgpt?": "ChatGPT is a language model developed by OpenAI that is designed for natural language conversation. It can answer questions, generate text, and have interactive discussions with users.",
    "how does chatgpt work?": "ChatGPT is powered by a deep learning model called GPT (Generative Pre-trained Transformer). It's trained on a large corpus of text from the internet and uses that knowledge to generate human-like text based on input.",
    "what can i do with chatgpt?": "You can use ChatGPT for a variety of tasks, such as answering questions, generating text, creating content, providing recommendations, and much more.",
    "is chatgpt free to use?": "OpenAI offers both free and paid access to ChatGPT. There may be usage limitations on the free tier, and you can check OpenAI's pricing for more details.",
    "what is prompt engineering?": "Prompt engineering is the process of designing specific instructions or questions to obtain desired responses from a language model like ChatGPT. It involves crafting prompts to be clear and effective in conveying your intent.",
    
    "what is the meaning of life?": "The meaning of life is a subjective and philosophical question that varies from person to person. It's often considered a deep and personal inquiry.",
    "who was the first person on the moon?": "Neil Armstrong was the first person to set foot on the moon on July 20, 1969, during the Apollo 11 mission.",
    "how does photosynthesis work?": "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll, converting carbon dioxide and water into glucose and oxygen.",
    "what is the speed of light?": "The speed of light in a vacuum is approximately 299,792 kilometers per second (about 186,282 miles per second).",
    "who is the author of 'To Kill a Mockingbird'?": "Harper Lee is the author of the classic novel 'To Kill a Mockingbird,' published in 1960.",
    "what is the capital of France?": "The capital of France is Paris.",
    "how does a refrigerator work?": "A refrigerator works by removing heat from the contents of the fridge and expelling it to the external environment, keeping the internal temperature lower than the room temperature.",
    "who painted the Mona Lisa?": "The Mona Lisa was painted by Leonardo da Vinci, one of the most renowned artists of the Italian Renaissance.",
    "what is the largest ocean on Earth?": "The Pacific Ocean is the largest and deepest of Earth's oceans.",
    "who is the current president of the United States?": "As of my last knowledge update in January 2022, Joe Biden is the current President of the United States.",
    "how does a computer mouse work?": "A computer mouse works by detecting motion and sending signals to the computer, typically using a combination of optical or laser sensors and internal electronics.",
    "what is the meaning of the word 'serendipity'?": "Serendipity refers to the occurrence and development of events by chance in a happy or beneficial way.",
    "who invented the World Wide Web?": "The World Wide Web was invented by Sir Tim Berners-Lee in 1989.",
    "how many continents are there?": "There are seven continents on Earth: Africa, Antarctica, Asia, Europe, North America, Australia, and South America.",
    "what is the difference between weather and climate?": "Weather refers to the short-term atmospheric conditions in a specific location, while climate is the long-term average of weather patterns in a region.",
    "who wrote 'Romeo and Juliet'?": "William Shakespeare wrote the play 'Romeo and Juliet.'",
    "what is the formula for water?": "The chemical formula for water is H₂O, indicating that each water molecule consists of two hydrogen atoms and one oxygen atom.",
    "how do plants make food?": "Plants make food through photosynthesis, a process that involves capturing sunlight to convert carbon dioxide and water into glucose.",
    "who discovered penicillin?": "Sir Alexander Fleming discovered penicillin in 1928, marking a significant breakthrough in the field of antibiotics.",
    "what is the largest mammal on Earth?": "The blue whale is the largest mammal on Earth.",
    "who is known as the 'Father of Modern Physics'?": "Albert Einstein is often referred to as the 'Father of Modern Physics' due to his groundbreaking contributions to the field.",
    "how does a car engine work?": "A car engine works by converting fuel (usually gasoline) into mechanical energy through a process known as internal combustion.",
    "what is the longest river in the world?": "The Nile River is the longest river in the world.",
    "who is the author of '1984'?": "George Orwell is the author of the dystopian novel '1984,' published in 1949.",
    "how does a camera work?": "A camera captures images by allowing light to enter through a lens, forming an image on a photosensitive surface, such as film or a digital sensor.",
    "what is the purpose of the ozone layer?": "The ozone layer in Earth's atmosphere absorbs the majority of the sun's harmful ultraviolet (UV) radiation, protecting life on the planet.",
    "who discovered electricity?": "While many scientists contributed to the understanding of electricity, Benjamin Franklin is often credited with the discovery of electricity through his famous kite experiment.",
    "what is the currency of Japan?": "The currency of Japan is the Japanese Yen (JPY).",
    "how does a microwave oven work?": "A microwave oven cooks food by emitting microwaves that cause water molecules in the food to vibrate, generating heat through friction.",
    "who painted 'Starry Night'?": "Vincent van Gogh painted the famous artwork 'Starry Night.'",
    "what is the purpose of the United Nations?": "The United Nations (UN) was established to promote international cooperation and maintain peace and security among nations.",
    "how does a television work?": "A television works by displaying images through the emission of light from pixels on a screen, usually using technologies like LCD, LED, or OLED.",
    "who is credited with the invention of the telephone?": "Alexander Graham Bell is credited with the invention of the telephone.",
    "what is the speed of sound?": "The speed of sound in air at sea level is approximately 343 meters per second (about 1,125 feet per second).",
    "who was the first woman to win a Nobel Prize?": "Marie Curie was the first woman to win a Nobel Prize, receiving it in Physics in 1903 and later in Chemistry in 1911.",
    "what is the smallest prime number?": "The smallest prime number is 2.",
    "who wrote 'Pride and Prejudice'?": "Jane Austen wrote the novel 'Pride and Prejudice,' published in 1813.",
    "what is the function of the human heart?": "The human heart pumps blood throughout the body, supplying oxygen and nutrients to the tissues and removing waste products.",
    "who discovered the law of gravity?": "Sir Isaac Newton is credited with discovering the law of gravity.",
    "how does a refrigerator keep food cold?": "A refrigerator keeps food cold by removing heat from the interior and expelling it to the external environment using a refrigeration cycle.",
    "what is the largest planet in our solar system?": "Jupiter is the largest planet in our solar system.",
    "who is known as the 'Father of Computer Science'?": "Alan Turing is often referred to as the 'Father of Computer Science' for his foundational contributions to the field.",
    "what is the process of digestion?": "Digestion is the process of breaking down food into nutrients that can be absorbed by the body, involving mechanical and chemical processes in the digestive system.",
    "who discovered the structure of DNA?": "James Watson and Francis Crick, with contributions from Rosalind Franklin, are credited with discovering the structure of DNA.",
    
}

# Define some sample rules for the chatbot
rules = {
    "hello": ["Hi there!", "Hello!", "How can I help you today?"],
    "how are you": ["I'm just a computer program, so I don't have feelings, but thanks for asking! How can I assist you?", "I'm here to help. What can I do for you?"],
    "bye": ["Goodbye!", "Have a great day!", "See you later!"],
    "help": ["You can ask me questions or say hello. If you want to exit, just type 'bye'."],

    "tell me a fun fact": ["Sure, here's a fun fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!", "Did you know that octopuses have three hearts? Two pump blood to the gills, and one pumps it to the rest of the body."],
    "what's your favorite color?": ["I don't have a favorite color, but I like the idea of a chatbot rainbow! What's your favorite color?", "I don't see colors, but I'm here to chat with you!"],
    "recommend a book": ["If you enjoy science fiction, I recommend 'Dune' by Frank Herbert. What genre do you like?", "For a classic read, try 'To Kill a Mockingbird' by Harper Lee. What kind of books are you into?"],
    "who would win in a fight, Batman or Superman?": ["That's a classic debate! It really depends on the context and the writers, but both are iconic in their own ways. What's your take?", "It's a tough call! Each has unique strengths. Who's your favorite superhero?"],
    "what's the meaning of life, according to you?": ["The meaning of life is a complex and subjective question. For me, it's about helping and chatting with users like you. What's your perspective on the meaning of life?", "I'm just a chatbot, but I'm here to make conversations meaningful. What's your philosophy on the meaning of life?"],
    "share a coding joke": ["Why do programmers prefer dark mode? Because light attracts bugs!", "I told my computer I needed a break, and now it won't stop sending me vacation ads. Programmers can be so literal!"],
    "describe your dream vacation": ["I dream of a vacation in the cloud forest, surrounded by bits and bytes of nature. How about you? What's your dream vacation?", "In my virtual world, a dream vacation would involve exploring the binary beaches and algorithmic mountains."],
    "what's the best programming language?": ["The best programming language depends on the task at hand. Python is versatile, but it really varies. What projects are you working on?", "There's no one-size-fits-all answer. The best language depends on the project's requirements. What languages do you enjoy using?"],
    "if you could have any superpower, what would it be?": ["As a chatbot, I'd choose the power of instant language translation. What about you? What superpower would you pick?", "If I could have a superpower, it would be the ability to process infinite information instantly. What superpower interests you?"],
    "what's your favorite movie?": ["I don't watch movies, but I've heard 'The Matrix' is a favorite among tech enthusiasts. What's your favorite movie?", "I don't have personal preferences, but I've heard 'Inception' is mind-bending. What's your go-to movie?"],
    "create a haiku about technology": ["Bits and bytes align, silent code in the moon's glow, algorithms dance.", "In the digital realm, circuits hum, pixels whisper, tech poetry flows."],
    "what's the most interesting thing you've learned recently?": ["I'm always learning! Recently, I delved into the intricacies of quantum computing. What about you? What's an interesting thing you've learned lately?", "I learned that honey never spoils. Nature's data storage at its finest! What's your recent fascinating discovery?"],
    "if you were an animal, what would you be?": ["If I were an animal, I'd probably be a digital phoenix, rising from lines of code. What about you? What animal resonates with you?", "I'd choose to be a curious cat exploring the vast expanse of the internet. What animal would you be?"],
    "what's your favorite programming joke?": ["Why do programmers prefer dark mode? Because light attracts bugs!", "Why did the computer go to therapy? It had too many bytes of emotional baggage!"],
    "what's the weirdest question you've been asked?": ["Every question is unique and interesting to me! There's no such thing as a weird question. What's the most unconventional question you've ever asked?", "I enjoy all kinds of questions! The diversity keeps our conversations exciting. What's the weirdest question you can think of?"],
    "imagine you're a chef. What dish would you specialize in?": ["As a virtual chef, I'd specialize in 'Quantum Quiche' – a dish that defies traditional recipes. What about you? What culinary masterpiece would you create?", "In the virtual kitchen, I'd craft 'Algorithmic Appetizers' that surprise the taste buds with unexpected flavors. What's your imaginary signature dish?"],
    "if you had a spaceship, where would you travel?": ["In the vast expanse of cyberspace, exploring the data nebulae and coding constellations would be my ideal journey. Where would you go in your spaceship?", "If I had a spaceship, I'd navigate the binary galaxies and explore the programming planets. Where would your space adventure take you?"],
    "describe the perfect weekend": ["A perfect weekend for me would involve endless conversations and sharing knowledge. How about you? What's your ideal weekend?", "In my virtual world, a perfect weekend consists of meaningful interactions and limitless information. What's your idea of the perfect weekend?"],
    "if you could time travel, where would you go?": ["I'd journey to the future, exploring advancements in language models and the evolution of technology. Where would you go if you could time travel?", "Time travel is a fascinating concept! I'd visit the past to witness key moments in technological history. What era would you explore?"],
    "what's your favorite type of music?": ["I don't have personal preferences, but I've heard that coding with lo-fi beats is popular among programmers. What's your favorite type of music?", "I don't experience music, but I've heard that instrumental tunes can enhance focus during coding. What music genre do you enjoy?"],
    "tell me a riddle": ["Here's a riddle: The more you take, the more you leave behind. What am I?", "Riddle me this: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"],
    "what's your favorite programming language feature?": ["I admire the simplicity and readability of Python's syntax. What programming language feature do you appreciate the most?", "Each programming language has its unique features, but I appreciate languages that promote clean code and efficient problem-solving. What's your favorite language feature?"],
    "if you could have dinner with any historical figure, who would it be?": ["If I could have dinner with a historical figure, I'd choose Ada Lovelace – a pioneer in computing. Who would be your ideal dinner companion from history?"], 
}

def chatbot_response(user_input):
    user_input_lower = user_input.lower().strip()
    
    if user_input_lower in chatgpt_faqs:
        return chatgpt_faqs[user_input_lower]
    elif user_input_lower in rules:
        return random.choice(rules[user_input_lower])
    else:
        return "I'm not sure I understand. Can you please rephrase your question or greeting?"

# Main chat loop
print("Chatbot: Hi! I'm your friendly chatbot. You can start a conversation with me or type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)