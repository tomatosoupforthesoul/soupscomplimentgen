import streamlit as st
import random

# List of compliments
compliments = [
    "Na naamam, nee viboothi, Abinand oru makku koodhi :* ",
    "I think the thing that draws me the most to you, that despite all this while, I am still giddy with butterflies when I am around you"
    "is how much I trust you? I know I can be my 100% authentic self with you and you love me for it."
    "My insecurities do not scare you"
    " and you just hold my hand and reassure me through it. I am truly lucky. ",
    "My favourite thing about you is your goofy smile, it can make me move worlds",
    "You are so fantastic that I like you more than I like filter coffee [or just as much]",
    "They say it's not the big things that make you fall in love with someone - no big romantic gestures, no major proclamations, rather - the small ones. "
    "For me, its the way you make fun of me and sportively take jokes on yourself, its the way you treat strangers and service workers, the calmness with which you carry yourself in most situations and the quiet way you whisper you love me "
    "when you most mean it. They are so much more likable and affable than the big stuff. ",
    "You are the most grounded and calm person I know, thank you for being you",
    "You are dependable as hell, you are there for me even when I don't even know I need you",
    "I like how much you are there for your friends. It is hard as hell to maintain one friendship, let alone ones like you in double digits, "
    "but you do it! You care a lot and are always there and that might be what I like most about you any given day",
    "The favourite part of any day is coming home to call you. It brightens up my mood, lifts up my spirits and all the exhaustion and annoyance from work just melts away.",
    "You might be the best thing that happened to me since 2023 [And trust me, so much has happened]",
    "I love how we come and tell each other everything, objectively the silliest of stuff that have no bearing on any of our lives. I like that"
    "we d not have drama or major fights, but just giggle over stupid updates from work or movies. It is peaceful and that is 100% what I love most about us.",
    "I love the dumb jokes you make, I'd laugh till I have tears for those, damn.",
    "You're an actual rockstar - you tirelessly work crazy amounts balancing everything, I am so proud of you :) "
]

# Streamlit app
def main():
    st.title("This is your daily cheerleader for times when Soups can't be around")
    st.write("Click the button below to get an ego boost!")


    # Functional Streamlit button to check for clicks
    if st.button("🔄 Generate"):
        compliment = random.choice(compliments)
        st.success(compliment)

if __name__ == "__main__":
    main()