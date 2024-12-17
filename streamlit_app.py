import streamlit as st

def load_dictionary(file_path):
    """Load dictionary words from a text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = file.read().splitlines()
        return set(words)  # Convert to a set for faster lookups
    except FileNotFoundError:
        st.error(f"Dictionary file '{file_path}' not found!")
        return set()

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
    st.title("বাংলা প্যাসেজ প্রক্রিয়াজাতকরণ অ্যাপ")
    
    # Load dictionary words from an external file
    dictionary = load_dictionary("dictionary.txt")

    # User Inputs
    passage = st.text_area("বাংলা প্যাসেজ লিখুন:", height=150)
    insert_char = st.text_input("অক্ষরের মাঝে যুক্ত করার ক্যারেক্টার লিখুন:")

    if st.button("প্রক্রিয়াজাত করুন"):
        if passage and insert_char:
            # Process the passage
            processed_passage = process_passage(passage, dictionary, insert_char)

            # Display result
            st.success("প্রক্রিয়াজাত প্যাসেজ:")
            st.write(processed_passage)

            # Add Copy Button (HTML + JS)
            st.components.v1.html(
                f"""
                <div>
                    <textarea id="copyText" style="display:none;">{processed_passage}</textarea>
                    <button onclick="copyToClipboard()">Copy Processed Passage</button>
                </div>
                <script>
                    function copyToClipboard() {{
                        var copyText = document.getElementById("copyText");
                        copyText.style.display = "block";
                        copyText.select();
                        document.execCommand("copy");
                        copyText.style.display = "none";
                        alert("Processed passage copied to clipboard!");
                    }}
                </script>
                """,
                height=50,
            )
        else:
            st.error("দয়া করে একটি প্যাসেজ এবং ক্যারেক্টার প্রদান করুন!")

if __name__ == "__main__":
    main()