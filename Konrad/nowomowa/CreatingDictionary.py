def creator_dictionary(name_of_input="some_text.txt", name_of_output="dictionary.txt"):
    dictionary = {"a": ["dutch"]}
    previous_word = "a"
    with open(name_of_input, "r") as inputting:
        with open(name_of_output, "w") as outputfile:
            read_data = inputting.read()
            read_data.replace(" ", "\n")
            base_list_2 = read_data.split("\n")
            outputfile.write(read_data)
            for word in base_list_2:
                if previous_word not in dictionary:
                    dictionary.update({previous_word: [].append(word)})
                else:
                    dictionary[previous_word].append(word)
                previous_word = word
            outputfile.write(str(dictionary))

creator_dictionary()