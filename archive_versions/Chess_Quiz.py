import streamlit as st

#--------------------------------------------------------------------------------------------------------------------
#Starting of the homepage
#----------------------------------------------------------------------------------------------------------------
  
st.title( " Chess Opening AI")
st.write( "A simple AI style chess opening recommender based on your style of play.")
 
#-----------------------------------------------------------------------------------------------------------------
#Make decisions based on user inputs
#----------------------------------------------------------------------------------------------------

#Decide skill levels
skill = st.selectbox(
"what is your current chess skill level?",
["Beginner", "Intermediate", "Advanced" ] )

#Play style input
style = st.selectbox(
    "How do you like to play?",
    ["Defensive", "Positional", "Agressive"] )

#Side selection 
color = st.selectbox(
    "Do you play as White or as Black?",
    ["White", "Black"] )

#Button to generate all the opening results
if st.button("Get Recommendations"):
    st.subheader("Your Reccommened Chess Opening")

    #---------------------------------------------------------------------------------------------------------
    #White piece recommendations
    #----------------------------------------------------------------------------------------------------

    if color == "White":
        if style == "Defensive":
            st.write("Colle System - A safe and simple setup.")
            st.write("King's Indian Attack- A flexibile and solid structure offering a early kings side attack.")
            st.write("London System - Very solid and stable.")

        elif style == "Positional":
            st.write("London System - Solid and pretty easy to master/learn.")
            st.write("Queen's Gambit - Starts by sacrificing a pawn but in return you get strong center control.")
            st.write("Catalan Opening - Long-term strategic pressure on the opponents King.")

        else: #This is going to be for aggressive
            st.write("Italian Game - Easy attacking chances for beginners.")
            st.write("Vienna Game - Flexibile and aggressive.")
            st.write("Scotch Game - Open posisitions and quick development of pieces.")

    #--------------------------------------------------------------------------------------------------------
    #Black piece recommendations
    #-----------------------------------------------------------------------------------------------------
    else:

        if style == "Defensive":
            st.write("Petroff Defense - Extremely solid and really safe.")
            st.write("Caro-Kann Defense - REALLY GOOD when mastered and hard to break through.")
            st.write("French Defense - Defensive but strong long-term.")
        
        elif style == "Positional":
            st.write("Caro-Kann - Solid and strategic. Really good when mastered.")
            st.write("French Defense - Strong pawn structure.")
            st.write("Slav Defense - Very reliable setup for anyone.")

        else: #Agressive for black
            st.write("Sicilian Defense - Sharp and tactical play.")
            st.write("King's Indian Defense - Strong counterattacking play with strong positional advantage.")
            st.write("Pirc Defense - Flexible and dynamic positions.")

    #-------------------------------------------------------------------------------------------------------------------
    #Explanations
    #------------------------------------------------------------------------------------------------------------
    st.divider()
    st.subheader("Explanation")

    if style == "Aggressive":
        st.write("You prefer attacking play, so these openings give early pressure and tactics you can deploy against your opponents.")
    elif style == "Positional":
        st.write("You prefer controlling the board slowly and building long-term advantages.")
    else: #Defensive
        st.write("You prefer safety and strong stuctures, reducing risk or a early attack and offers a solid middlegame.")
    
    #Skill based message
    if skill == "Beginner":
        st.info("Tip: Start with 1-2 openings only and master the ideas not memorizing deep theory.")
    elif skill == "Intermediate":
        st.info("Tip: Learn common traps and typical middlegame plans. Understand the purpose of openings and master endgames.")
    else: #Advanced skill level
        st.info("Tip: Focus on deep theory, tactics recognition and dive into modifying opening to make it more unique.")

                    
