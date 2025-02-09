# Text Analyzer

## About the Project
This project implements a Python-based text analysis tool that provides various insights into a given text. It analyzes the structure of the text, detects its language, evaluates sentiment (for English texts), and identifies the most frequent words. This tool is useful for linguistic analysis, natural language processing tasks, or general text exploration.

## How It Works
1. The program prompts the user to input a block of text.
2. It performs the following analyses:
   - Counts the number of sentences.
   - Counts the number of words.
   - Calculates the total number of characters (with and without spaces).
   - Identifies the most frequent words in the text.
   - Detects the language of the text with a confidence score.
   - Analyzes sentiment (for English texts only).
3. The results are displayed in a structured format.

## Getting Started

### Prerequisites
- Python 3.x
- Required Python libraries:
  - `re`
  - `collections`
  - `langdetect`
  - `langcodes`
  - `textblob`

You can install the required libraries using pip:

pip install langdetect langcodes textblob

### Installation
1. Clone the repository:

git clone https://github.com/BernardoMarta/Text_analyzer
cd Text_analyzer

## Usage
Run the script from the command line:

python text_analyzer.py

Follow the prompts to input a block of text for analysis.

## Running Tests
Unit tests are included to verify the functionality of individual components. To run the tests:

pytest test_text_analyzer.py


## Features
- Counts sentences, words, and characters (with and without spaces).
- Identifies the most frequent words in the text.
- Detects language with confidence scores.
- Performs sentiment analysis for English texts.
- Handles invalid or short inputs gracefully.

## Example

**Input:**
The user enters a block of text when prompted, e.g., "Hello world! How are you today?"

**Output:**
The program will display:
- Number of sentences: 2
- Number of words: 6
- Number of all characters: 31
- Number of characters without spaces: 26
- Most frequent words: "hello", "world", "how", "are", "you"
- Language: English (probability: 100%)
- Sentiment: Positive

## Contributing
Feel free to fork this repository and submit pull requests to [BernardoMarta's repository](https://github.com/BernardoMarta/Text_analyzer)!

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to open-source libraries like `langdetect`, `langcodes`, and `textblob` for enabling language detection and sentiment analysis.
