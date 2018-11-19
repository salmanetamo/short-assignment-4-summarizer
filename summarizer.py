def summarize(filename):
    # Initializing the input file and the output file
    input_file = open(filename, 'r')
    output_file = open(filename+'-summary', 'a')

    # Getting the paragraphs from the input as a list
    paragraphs = input_file.readlines()

    input_file.close()  # The input file is closed as it is no longer needed

    if len(paragraphs) <= 2:
        # If the input file has 2 paragraphs or less, then the summary is identical
        output_file.write(input_file.read())
    else:
        # More than 2 paragraphs, building up the summary
        summary = ''
        summary += paragraphs[0]  # Adding the first paragraph

        count = 1
        while count <= len(paragraphs) - 2:
            if paragraphs[count] == '\n':
                # Empty lines are automatically added
                summary += '\n'
            else:
                # Getting individual sentences in a paragraph as a list
                paragraph_sentences = paragraphs[count].split('.')

                summary += paragraph_sentences[0] + '.'  # Adding the first sentence of the paragraph
                if paragraph_sentences[len(paragraph_sentences) - 1] == '\n':
                    # Adding the last sentence provided it's not an empty line
                    summary += paragraph_sentences[len(paragraph_sentences) - 2] + '.\n'

            count += 1

        summary += paragraphs[len(paragraphs) - 1]  # Adding the last paragraph

        output_file.write(summary)  # Appending the summary to the output file
        output_file.close()  # Being polite, closing the file


def main():
    filename = input('Enter a file name: ')
    summarize(filename)


main()
