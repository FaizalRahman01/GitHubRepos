#Developer- Faizal Rahman
print("""Namaskar, main Amitabh Bachchan bol raha hoon. Swagat hai aapka Kaun Banega Crorepati me 
Doston, yeh ek aisa manch hai jahan gyaan hi aapko aapki manzil takle ja sakta hai.
Ek sahi jawab aapko lakhon, crodon rupay jeetne ka mauka de sakta hai
Doston, aaj ka khel shuru karne se pehle, ek baar zor daar taaliyanho jayein humare contestants ke liye
Swagat hai aapka hot seat par! Kaisa mehsoos ho raha hai?""")
batao=input("")
print("""whhh!! ,To Chalye hum apko Game k rule bata dete hai 📜 KBC Game Ke Rules:
1️⃣ Total 15 Questions 🎤

Contestant ko ek-ek karke multiple-choice questions diye jate hain.
Har question ka 4 options diye jate hain, jisme se ek sahi jawab hota hai.
2️⃣ Har Sahi Jawab Pe Prize Money 💰

Pehla question ₹1,000 se shuru hota hai.
Har sahi jawab par amount badhti hai.
Last question tak pahunchne par ₹7 crore tak jeet sakte hain!
3️⃣ Milestone Questions (Safe Levels) ✅

Question 5 (₹10,000) – Pehla safe level
Question 10 (₹3,20,000) – Dusra safe level
Question 15 (₹1 Crore) – Jackpot
Question 16 (₹7 Crore) – Ultimate Jackpot
🎯 Agar koi milestone cross karta hai, toh galat jawab dene ke baad bhi wo minimum itna paisa jeet chuka hota hai.

4️⃣ Lifelines (Help Options) 🛟

50:50 – Do galat options hata diye jate hain.
Audience Poll – Studio audience voting karti hai.
Phone-a-Friend – Contestant apne kisi dost se phone pe madad le sakta hai.
Flip the Question – Question badal diya jata hai.
5️⃣ Galat Jawab Par Game Over 🚫

Agar contestant galat jawab deta hai, toh pichhle milestone tak ka paisa milega.
Agar koi milestone tak nahi pahunchta aur galti karta hai, toh zero bhi ho sakta hai.
6️⃣ Quit Karna Allowed Hai 🏃

Agar contestant sure nahi hai, toh game chhod kar jeeti hui amount le sakta hai.
Quit karne se milne wala paisa safe hota hai.
🎶 Game Start Example:
Amitabh Bachchan:
"Toh bina kisi deri ke, chaliye khel shuru karte hain… Kaun Banega Crorepati!"

🎵 (Background music starts, screen pe pehla question dikhai deta hai!) 🎬""")
jawab = input()
question =["1️⃣ - Which is the national animal of India?\n(A) Tiger\n(B) Lion\n(C) Elephant\n(D) Deer",
         "2️⃣  -  Which festival is known as the festival of lights?\n(A) Holi\n(B) Diwali\n(C) Eid\n(D) Christmas",
         "3️⃣  -  How many states are there in India?\n(A) 25\n(B) 27\n(C) 28\n(D) 29",
         "4️⃣  -  Who wrote the Indian National Anthem 'Jana Gana Mana'?\n(A) Rabindranath Tagore\n(B) Bankim Chandra Chatterjee\n(C) Mahatma Gandhi\n(D) Subhas Chandra Bose",
         "5️⃣  -  Which planet is known as the Red Planet?\n(A) Venus\n(B) Mars\n(C) Jupiter\n(D) Saturn",
         """6️⃣ - Who was the first Prime Minister of India?

(A) Lal Bahadur Shastri
(B) Jawaharlal Nehru
(C) Sardar Patel
(D) Indira Gandhi
""",""""
7️⃣ – Which is the longest river in India?

(A) Yamuna
(B) Brahmaputra
(C) Ganga
(D) Godavari """,
""" 8️⃣ – Which organ in the human body purifies blood?

(A) Heart
(B) Lungs
(C) Liver
(D) Kidney""","""9️⃣ - Which Mughal emperor built the Taj Mahal?

(A) Akbar
(B) Jahangir
(C) Shah Jahan
(D) Aurangzeb""","""🔟 – Which is the largest continent in the world?

(A) Africa
(B) Asia
(C) Europe
(D) North America""","""🔥 Jackpot Round (Higher Amounts) 🔥
1️⃣ 1️⃣  – Who discovered gravity?

(A) Albert Einstein
(B) Isaac Newton
(C) Galileo Galilei
(D) Nikola Tesla""",""""1️⃣ 2️⃣ – What is the currency of Japan?

(A) Yen
(B) Won
(C) Ringgit
(D) Baht""","""1️⃣ 3️⃣ – Who was the first man to walk on the Moon?

(A) Yuri Gagarin
(B) Neil Armstrong
(C) Buzz Aldrin
(D) Michael Collins""","""1️⃣ 4️⃣ – Which Nobel Prize category was not part of the original five established in 1895?

(A) Literature
(B) Peace
(C) Economics
(D) Chemistry""","""1️⃣ 5️⃣ – Who was the first Indian to win an individual Olympic gold medal?

(A) Abhinav Bindra
(B) Milkha Singh
(C) P.V. Sindhu
(D) Leander Paes""","""🔥 Ultimate Jackpot Question (₹7 Crore) 🔥
Which is the only country to have won the FIFA World Cup in four different continents?

(A) Germany
(B) Brazil
(C) Argentina
(D) Italy"""]
print(question[0])
first=(input())
if (first =='a'):
    print("correct answer you won ₹1000 rupees\n")
else:
    print("sorry correct answer is Tiger and you lost the game\n")
    exit()
print(question[1])
    
first=(input())
if (first =='b'):
    print("correct answer you won ₹2000 rupees\n")
else:
    print("sorry correct answer is Diwali and you lost the game\n")
    exit()
print(question[2])
    
first=(input())
if (first =='c'):
    print("correct answer you won ₹3000 rupees\n")
else:
    print("sorry correct answer is 28 and you lost the game\n")
    exit ()
print(question[3])
    
first=(input())
if (first =='a'):
    print("correct answer you won ₹5000 rupees\n")
else:
    print("sorry correct answer is Rabindranath Tagore and you lost the game\n")
    exit ()
print(question[4])
first=(input())
if (first =='b'):
    print("correct answer you won ₹10,000 rupees\n")
else:
    print("sorry correct answer is Mars and you lost the game\n")
    exit ()
print(question[5])
first=(input())
if (first =='b'):
    print("correct answer you won ₹20,000 rupees\n")
else:
    print("sorry correct answer is Jawaharlal Nehru and you lost the game\n")
    exit ()
print(question[6])
first=(input())
if (first =='c'):
    print("correct answer you won ₹40,000 rupees\n")
else:
    print("sorry correct answer is Ganga and you lost the game\n")
    exit ()
print(question[7])
first=(input())
if (first =='d'):
    print("correct answer you won ₹80,000 rupees\n")
else:
    print("sorry correct answer is Kidney and you lost the game\n")
    exit ()
print(question[8])
first=(input())
if (first =='c'):
    print("correct answer you won ₹1,60,000 rupees\n")
else:
    print("sorry correct answer is  Shah Jahan and you lost the game\n")
    exit ()
print(question[9])
first=(input())
if (first =='b'):
    print("correct answer you won ₹3,20,000 rupees\n")
else:
    print("sorry correct answer is  Asia and you lost the game\n")
    exit ()
print(question[10])
first=(input())
if (first =='b'):
    print("correct answer you won ₹6,40,000 rupees\n")
else:
    print("sorry correct answer is  Isaac Newton and you lost the game\n")
    exit ()
print(question[11])
first=(input())
if (first =='a'):
    print("correct answer you won ₹12,50,000 rupees\n")
else:
    print("sorry correct answer is  Yen and you lost the game\n")
    exit ()
print(question[12])
first=(input())
if (first =='b'):
    print("correct answer you won ₹25,00,0000 rupees\n")
else:
    print("sorry correct answer is  Neil Armstrong and you lost the game\n")
    exit ()
print(question[13])
first=(input())
if (first =='c'):
    print("correct answer you won ₹50,00,000 rupees\n")
else:
    print("sorry correct answer is Economics and you lost the game\n")
    exit ()
print(question[14])
first=(input())
if (first =='a'):
    print("correct answer you won ₹1Crore rupees\n")
else:
    print("sorry correct answer is Abhinav Bindra and you lost the game\n")
    exit ()
print(question[15])
first=(input())
if (first =='b'):
    print("\t \t 7 Crore 🥳🫂")
    print("correct answer you won ₹7Crore rupees\n")
    print("Bahoot Bahoot Badhai Bhai Sahab/Bahan jii  aapko Aap jit chuke hai ₹7Crore🥳🥳💥  ")
else:
    print("sorry correct answer is Brazil and you lost the game\n")
    exit ()
print("If You play Again The KBC Game Then Re run the code ▶️")