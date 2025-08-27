# Dancing Letter GIF Generator

You know those wacky aah goofy little dancing letter GIFs on Discord and other sites?
These bad boys: <br>
![A dancing letter A](https://www.artiestick.com/toons/alphabet/ralph/arg-a-5O-tRyA.gif)
![A dancing letter B](https://www.artiestick.com/toons/alphabet/ralph/arg-B-5O-tganz2x4vs-stolen.gif)
![A dancing letter C](https://www.artiestick.com/toons/alphabet/ralph/arg-c-50-trans-url.gif)

I often see people (try to) make words out of them on Discord servers and etc., but it's kind of a hassle: You have to search and find the correct letter, send them one by one... it just does not look good.
So taking matters into my own hands, I created this GIF generator that, when input a sentence, does two things:
- Turns all correct characters (Letters of the English alphabet, numbers 0-9, space and these characters: `&`,`@`,`$`,`?`,`!`) into their dancing GIF forms and spits them out into a nicely copy-pasteable list
- Takes this list and merges it into one big GIF you can just copy straight away!

Example:

![The sentence "Hello Github" made up entirely of dancing letters](https://github.com/user-attachments/assets/5aa9e252-c9d1-42f7-8538-001045a85d05)

<br>
The system also supports line breaks, variable GIF widths and many more. Some more examples:

![The sentence "Line breaks are also supported!" made up entirely of dancing letters, with a line break in the middle](https://github.com/user-attachments/assets/5caf02a8-6179-483b-a8cf-93c2c30ab349)


![A generated GIF of dancing letters, showing off all the special characters one can use](https://github.com/user-attachments/assets/9cce8c9a-62de-48fc-92aa-f8ca3a1e5d04)

<br>

# How to use
Just go to [The website](http://89.168.88.97:5500/) (sorry, no domain yet, working on it!) and try it out yourself!

<br>

# How to self-host
The program is self-hostable! However, before running you do need to set up a folder called `dancing_letter_gifs` in the project's root and fill it with the gifs.
I could've supplied this with the project but considering the GIFs are not my property, even though they are allowed for non-commercial usage, I still wanted to be cautious.

The naming scheme is like this (this is what the program expects so you should name your downloaded GIFs like this): <br>

Every letter → `dancing_` + letter in uppercase + `.gif`. For example: `dancing_A.gif`

Numbers → `dancing_` + number + `.gif`. For example: `dancing_1.gif`

Special characters:
- Space → `dancing_space.gif` (Can be any gif since it's just a placeholder and the program generates the space characer on the fly. I am using a fully empty GIF sized 170x160 if you're curious)
- `&` → `dancing_and.gif`
- `@` → `dancing_at.gif`
- `?` → `dancing_question.gif`
- `!` → `dancing_exclamation.gif`

# Acknowledgements
Dancing letter gifs made by GIFs made by [ARG! Cartoon Animation](https://www.artiestick.com/), free to use on non-commercial pages that link to their website.

Dancing Letter GIF Generator made by [Laky2k8](https://laky2k8.hu).

