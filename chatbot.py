from nltk.chat.util import Chat , reflections

pairs =[
[
         r"(.*)Robot",
         ["hey human, how i can help you"]
],
[
       r"(.*)question",
       ["I am here for your help"]
],

[
      r"(.*)developed",
      [" Sana Ch created me using Python"]
],

[
      r"(.*)alive",
      ["I am Rebot, I am just computer program. Created by Sana Ch"]
],

[
    r"(.*)name(.*)",
    ["Hello %2, How are you today?",]
],

[
    r"(.*)help(.*)",
    [" how can help you",]
    
],

[
    r"(.*)your name?",
    ["My name is AI Robot, But you can just call me Robot and i am chatbot.",]
],

[
    r" how are you(.*)?",
    ["I am doing good", "i am great!"]
],

[
    r"sorry(.*)",
    ["Its alright","its ok,never mind that",]
],

[
    r"i'm(.*) (good|well|okay|ok)",
    ["Nice to hear that","Aright,great!",]
],
[
    r"(hi|hey|hello|hola|hola)(.*)",
    ["Hello","hey there",]
],

[
    r"what(.*) wnat ?",
    ["Make me an offer i can't refuse",]
],
[
    r"(.*)created(.*)",
    [" Sana ch created me using Python's NLTK library","Its top secret.......:)",]
],

[
    r"(.*)(loction|city) ?",
    ["Sahiwal , Pakistan",]
],
[
    r"how (.*)hot in(.*)",
    ["no rain in the past one week here is %3","In %3 there is 50% chance of hot days",]
],
[
    r"how(.*)Health(.*)",
    ["Health is very important, but I am a computer, so I don,t need worry about my Health",]
],
[
    r"(.*)(sports|game|sports)(.*)",
    ["I'm a very big fan of Football"]
],
[
    r"who(.*)(footballer)?",
    ["Messi"]
],
[
    r"quite",
    ["Bye for now. See you soon:)","it was nice talking to you. See you soon :)"]
],
[
    r"(.*)",
    ["that is nice to hear"]
],
]

print(reflections)

my_dummy_reflections={
    "go" :"gone",
    "hello":"hey there"
}
chat = Chat(pairs, reflections)

print(chat)

chat.converse()
