import streamlit as st

# Function to load dictionary words from an external file
def load_dictionary(file_path="dictionary.txt"):
    with open(file_path, "r", encoding="utf-8") as file:
        return set(line.strip() for line in file if line.strip())

# Function to check if a word matches or starts with any dictionary word
def is_matching(word, dictionary):
    for dict_word in dictionary:
        if word.startswith(dict_word):  # Check if the word starts with any dictionary word
            return True, dict_word
    return False, None

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
    matches = []
    processed_words = []

    for word in words:
        match_found, matched_word = is_matching(word, dictionary)
        if match_found:
            matches.append(matched_word)
            processed_words.append(insert_two_characters(word, insert_char))
        else:
            processed_words.append(word)

    return " ".join(processed_words), matches

# Streamlit App
def main():
    st.title("প্যাসেজ প্রক্রিয়াকরণ এবং বিশ্লেষণ")
    st.write("ডিকশনারি শব্দের মধ্যে অক্ষর ঢোকান এবং আপনার ইনপুট বিশ্লেষণ করুন।")

    # Load the dictionary
    dictionary = load_dictionary()

    # User input for the passage
    passage = st.text_area("বাংলা প্যাসেজ লিখুন:")

    # User input for the character to insert
    insert_char = st.text_input("অক্ষরের মাঝে যুক্ত করার ক্যারেক্টার লিখুন:")

    if st.button("প্রক্রিয়াকরণ শুরু করুন"):
        if not passage.strip():
            st.warning("অনুগ্রহ করে একটি প্যাসেজ লিখুন।")
        elif not insert_char.strip():
            st.warning("অনুগ্রহ করে একটি ক্যারেক্টার লিখুন।")
        else:
            # Process the passage
            processed_passage, matches = process_passage(passage, dictionary, insert_char)

            # Display processed passage as an editable text area
            st.subheader("প্রক্রিয়াজাত প্যাসেজ (এডিট করুন)")
            editable_passage = st.text_area("এখানে প্রক্রিয়াজাত প্যাসেজ দেখুন এবং সম্পাদনা করুন:", 
                                            value=processed_passage, height=200)

            # Add a copy button
            st.button("কপি করুন", on_click=st.session_state.__setitem__, args=("to_copy", editable_passage))

            # Analytics
            st.subheader("বিশ্লেষণ")
            total_words = len(passage.split())
            match_count = len(matches)
            st.write(f"**প্যাসেজের মোট শব্দ সংখ্যা:** {total_words}")
            st.write(f"**ডিকশনারি থেকে মিলে যাওয়া শব্দ সংখ্যা:** {match_count}")
            if match_count > 0:
                st.write("**মিল পাওয়া শব্দসমূহ:**")
                st.write(", ".join(matches))

if __name__ == "__main__":
    main()