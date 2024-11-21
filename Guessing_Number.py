import streamlit as st
import random


# Title of the app
st.title("🎲 Number Guessing Game 🎮")

# Instructions
st.markdown("""
    ## Welcome to the Number Guessing Game!  
    I am thinking of a number between 1 and 100. Try to guess it!  
    Each time you make a guess, I will tell you whether the number is **higher** or **lower**.  
    Let's see how many attempts it takes for you to guess the correct number!  
""")

# Start the game
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100) # Return random number and number of attempts
    st.session_state.attempts = 0

# Input for the player's guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Submit button
if st.button("Guess"):
    # Check if the guess is correct
    if guess < st.session_state.secret_number:
        st.session_state.attempts += 1
        st.success("🔼 Your guess is too low! Try again.")
    elif guess > st.session_state.secret_number:
        st.session_state.attempts += 1
        st.success("🔽 Your guess is too high! Try again.")
    else:
        st.session_state.attempts += 1
        st.success(f"🎉 Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
        st.session_state.secret_number = random.randint(1, 100) # Return random number and number of attempts
        st.session_state.attempts = 0
# Show number of attempts
st.sidebar.subheader("Game Starts")
st.sidebar.write(f"Attempts: {st.session_state.attempts}")

# Button to start a new game
if st.sidebar.button("Start New Game"):
    st.session_state.secret_number = random.randint(1, 100) # Return random number and number of attempts
    st.session_state.attempts = 0
    st.success("Game has been reset. Good luck!")
