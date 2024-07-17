import streamlit as st
import random

# List of compliments
compliments = [
    "You're amazing!",
    "I love you so much, you can literally do anything you put your mind to",
    "My favourite thing about you is your goofy smile, it can make me move worlds",
    "You are so fantastic that I like you more than I like filter coffee",
    "I am incredibly proud of you, keep going mister",
    "You are the most grounded and calm person I know, thank you for being you",
    "You are dependable as hell, you are there for me even when I don't even know I need you",
    "I love how kind you are",
    "The favourite part of any day is coming home to call you ",
    "You might be the best thing that happened to me since 2023 [And trust me, so much has happened]",
    "You are a fantastic problem solver.",
    "I love the dumb jokes you make, I'd laugh till I have tears for those, damn.",
    "You're an actual rockstar - you tirelessly work crazy amounts balancing everything, i am so proud of you :) "
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