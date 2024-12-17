import streamlit as st

# Function to load dictionary words from an external file
def load_dictionary(file_path="dictionary.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        return set(line.strip() for line in file if line.strip())

# Function to insert characters between letters of a word
def insert_two_characters(word, insert_char):
    """Insert exactly 2 characters between letters of a word."""
    result = ""
    insert_count = 0
    for i, char in enumerate(word):
        result += char
        if i < len(word) - 1 and insert_count < 2:
            result += insert_char
            insert_count += 1
    return result

# Function to process the passage
def process_passage(passage, dictionary, insert_char):
    """Process the passage by inserting characters into dictionary words."""
    words = passage.split()
    matches = [word for word in words if word in dictionary]
    processed_words = [
        insert_two_characters(word, insert_char) if word in dictionary else word
        for word in words
    ]
    return " ".join(processed_words), matches

# Streamlit App
def main():
    st.title("Passage Processor with Analytics")
    st.write("Insert characters into dictionary words and analyze your input!")

    # Load the dictionary
    dictionary = load_dictionary()

    # User input for the passage
    passage = st.text_area("Enter your Bangla passage:")

    # User input for the character to insert
    insert_char = st.text_input("Character to insert between letters:")

    if st.button("Process Passage"):
        if not passage.strip():
            st.warning("Please enter a passage.")
        elif not insert_char.strip():
            st.warning("Please enter a character to insert.")
        else:
            # Process the passage
            processed_passage, matches = process_passage(passage, dictionary, insert_char)

            # Analytics
            total_words = len(passage.split())
            match_count = len(matches)

            # Display results
            st.subheader("Processed Passage")
            st.code(processed_passage, language="text")  # Display processed passage

            # Copy button
            st.caption("Click the button below to copy the processed passage:")
            st.text_area("Copy Processed Passage", processed_passage)

            # Analytics
            st.subheader("Analytics")
            st.write(f"**Total words in passage:** {total_words}")
            st.write(f"**Number of matches found in dictionary:** {match_count}")
            if match_count > 0:
                st.write("**Matched Words:**")
                st.write(", ".join(matches))

if __name__ == "__main__":
    main()