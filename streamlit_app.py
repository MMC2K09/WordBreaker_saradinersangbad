import streamlit as st

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

def process_passage(passage, dictionary, insert_char):
    """Process the passage by inserting characters into dictionary words."""
    words = passage.split()
    processed_words = [
        insert_two_characters(word, insert_char) if word in dictionary else word
        for word in words
    ]
    return " ".join(processed_words)

# Streamlit App
def main():
    st.title("বাংলা অনুচ্ছেদ প্রক্রিয়াজাতকরণ অ্যাপ")
    
    # Offensive Bangla words dictionary (using a set for faster lookup)
    dictionary = {
        "হত্যা", "মারা", "ইসরায়েল", "ইসরায়েলি", "সংঘর্ষ", "আগুন",
        "নিহত", "আহত", "মৃত", "মৃত্যু", "ইসরায়েলের", "ইসরায়েলকে",
        "ধ্বংস", "রক্ত", "সন্ত্রাস", "দাঙ্গা", "অপরাধ"
    }

    # Get user input
    passage = st.text_area("অনুচ্ছেদ লিখুন:", height=150)
    insert_char = st.text_input("অক্ষরের মাঝে যুক্ত করার চিহ্ন লিখুন:")

    # Process Button
    if st.button("প্রক্রিয়াজাত করুন"):
        if passage and insert_char:
            result = process_passage(passage, dictionary, insert_char)
            st.success("প্রক্রিয়াজাত অনুচ্ছেদ:")
            st.write(result)
        else:
            st.error("দয়া করে একটি অনুচ্ছেদ এবং চিহ্ন প্রদান করুন!")

if __name__ == "__main__":
    main()
